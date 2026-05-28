"""
Legacy-Cleanup fuer IONOS-Webspace.

Sichert ausgewaehlte Legacy-Pfade als TAR.GZ-Archiv und loescht sie anschliessend.

Modi (Umgebungsvariable CLEANUP_MODE):
  list     - listet nur, was vorhanden ist (read-only, default)
  backup   - backupt nach legacy-backup.tar.gz, ohne zu loeschen
  execute  - backupt UND loescht (irreversibel im Webspace)

Pfade werden ueber LEGACY_PATHS (komma-getrennt) gesteuert, default = sichere Auswahl.

ENV (gleich wie deploy_ionos.py):
  IONOS_SFTP_HOST
  IONOS_SFTP_USER
  IONOS_SFTP_PASS
  IONOS_SFTP_REMOTE   (optional, default /LIARastro)

Lokal aufrufen: python cleanup_legacy.py
In GitHub Action: per workflow_dispatch mit Mode-Auswahl.
"""
import io
import os
import sys
import stat
import tarfile
import time
from datetime import datetime

import paramiko


# ------------------------------------------------------------------
# Konfiguration
# ------------------------------------------------------------------

def env_required(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        sys.exit(f"FEHLER: ENV-Variable {key} nicht gesetzt.")
    return val


SFTP_HOST = env_required("IONOS_SFTP_HOST")
SFTP_USER = env_required("IONOS_SFTP_USER")
SFTP_PASS = env_required("IONOS_SFTP_PASS")

# Webspace-Root ableiten aus IONOS_SFTP_REMOTE (z.B. /LIARastro -> /)
REMOTE_LIARASTRO = os.environ.get("IONOS_SFTP_REMOTE", "/LIARastro")
WEBSPACE_ROOT = "/"  # Top-Level des IONOS-Webspace

MODE = os.environ.get("CLEANUP_MODE", "list").lower()
if MODE not in {"list", "backup", "execute"}:
    sys.exit(f"FEHLER: CLEANUP_MODE='{MODE}' ungueltig. Erlaubt: list | backup | execute")

# Default-Scope: das was wir besprochen haben
DEFAULT_PATHS = [
    # WordPress-Legacy im Webspace-Root (HTTP 404 von aussen)
    "/admin",
    "/login",
    "/content",
    "/assets",
    # Shell-Verlauf (sollte nicht auf Live-Server liegen)
    "/.bash_history",
    # Veraltete Sicherungsdateien in /LIARastro/
    "/LIARastro/.htaccess.bak-tag04",
    "/LIARastro/.htaccess.bak-tag04-patch4",
    "/LIARastro/robots.txt.bak-tag04",
    "/LIARastro/sitemap.xml.pre-tag05",
]

# Per ENV override moeglich (komma-getrennt)
override = os.environ.get("LEGACY_PATHS", "").strip()
if override:
    TARGET_PATHS = [p.strip() for p in override.split(",") if p.strip()]
else:
    TARGET_PATHS = DEFAULT_PATHS

# NIEMALS anfassen
PROTECTED = {
    "/LIARastro",        # Live-Site
    "/LIARastroBACKUP",  # Rollback-Versicherung
    "/LIAR-SEO",
    "/Pantomime",
    "/zauberer-nrw",
    "/ssl",
    "/logs",
    "/.htaccess",        # Root-htaccess steuert Domain-Routing
    "/index.php",
    "/php.ini",
}


def is_protected(path: str) -> bool:
    if path in PROTECTED:
        return True
    for p in PROTECTED:
        if path.startswith(p + "/"):
            return True
    return False


# ------------------------------------------------------------------
# SFTP-Helfer
# ------------------------------------------------------------------

def remote_exists(sftp, path):
    try:
        return sftp.stat(path)
    except FileNotFoundError:
        return None


def is_dir(attr):
    return attr is not None and stat.S_ISDIR(attr.st_mode)


def walk_remote(sftp, root):
    """Generator: (full_remote_path, is_directory, size) fuer alles unter root."""
    attr = remote_exists(sftp, root)
    if attr is None:
        return
    if not is_dir(attr):
        yield root, False, attr.st_size
        return
    yield root, True, 0
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            entries = sftp.listdir_attr(current)
        except Exception as e:
            print(f"  WARN: kann {current} nicht lesen: {e}")
            continue
        for entry in entries:
            full = current.rstrip("/") + "/" + entry.filename
            if is_dir(entry):
                yield full, True, 0
                stack.append(full)
            else:
                yield full, False, entry.st_size


def collect_remote_files(sftp, paths):
    """Sammelt alle Dateien (inkl. Unterordnern) zu den Top-Level-Paths."""
    collected = []  # (full_path, size, top_path)
    total_size = 0
    for top in paths:
        if is_protected(top):
            print(f"  GESCHUETZT, wird uebersprungen: {top}")
            continue
        attr = remote_exists(sftp, top)
        if attr is None:
            print(f"  Nicht vorhanden: {top}")
            continue
        n_files = 0
        n_dirs = 0
        for full, is_d, size in walk_remote(sftp, top):
            if is_d:
                n_dirs += 1
            else:
                n_files += 1
                total_size += size
                collected.append((full, size, top))
        print(f"  {top}: {n_files} Dateien, {n_dirs} Ordner")
    return collected, total_size


def download_to_archive(sftp, collected_files, archive_path):
    """Laedt alle Dateien runter und packt sie in ein tar.gz."""
    print(f"\nErstelle Archiv: {archive_path}")
    with tarfile.open(archive_path, "w:gz") as tar:
        for i, (full, size, top) in enumerate(collected_files, 1):
            # Pfad im Archiv: ohne fuehrenden Slash, mit Webspace-Praefix
            arcname = "webspace" + full
            try:
                buf = io.BytesIO()
                sftp.getfo(full, buf)
                buf.seek(0)
                info = tarfile.TarInfo(name=arcname)
                info.size = len(buf.getvalue())
                info.mtime = int(time.time())
                tar.addfile(info, buf)
                if i % 25 == 0 or i == len(collected_files):
                    print(f"  {i}/{len(collected_files)} Dateien archiviert")
            except Exception as e:
                print(f"  FEHLER beim Archivieren von {full}: {e}")
    actual_size = os.path.getsize(archive_path)
    print(f"Archiv fertig: {actual_size / 1024:.1f} KB")


def delete_recursive(sftp, path):
    """Loescht Pfad rekursiv (Datei oder Ordner)."""
    attr = remote_exists(sftp, path)
    if attr is None:
        return 0
    if not is_dir(attr):
        sftp.remove(path)
        return 1
    # Verzeichnis: erst Inhalt, dann sich selbst
    deleted = 0
    try:
        for entry in sftp.listdir_attr(path):
            full = path.rstrip("/") + "/" + entry.filename
            if is_dir(entry):
                deleted += delete_recursive(sftp, full)
            else:
                sftp.remove(full)
                deleted += 1
        sftp.rmdir(path)
    except Exception as e:
        print(f"  FEHLER beim Loeschen von {path}: {e}")
    return deleted


# ------------------------------------------------------------------
# Hauptablauf
# ------------------------------------------------------------------

def main():
    print(f"=== LEGACY-CLEANUP fuer {SFTP_HOST} ===")
    print(f"Modus: {MODE}")
    print(f"Ziele ({len(TARGET_PATHS)}):")
    for p in TARGET_PATHS:
        flag = "  GESCHUETZT" if is_protected(p) else ""
        print(f"  - {p}{flag}")

    print("\nVerbinde mit SFTP...")
    transport = paramiko.Transport((SFTP_HOST, 22))
    transport.connect(username=SFTP_USER, password=SFTP_PASS)
    sftp = paramiko.SFTPClient.from_transport(transport)
    print("Verbunden.\n")

    try:
        print("=== Phase 1: Inventur ===")
        collected, total_size = collect_remote_files(sftp, TARGET_PATHS)
        print(f"\nGesamt: {len(collected)} Dateien, {total_size / 1024:.1f} KB")

        if not collected:
            print("\nNichts zu tun. Beende.")
            return

        if MODE == "list":
            print("\nMODE=list -> nur Inventur, keine Aenderungen.")
            return

        print("\n=== Phase 2: Backup ===")
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        archive_path = f"legacy-backup-{timestamp}.tar.gz"
        download_to_archive(sftp, collected, archive_path)

        if MODE == "backup":
            print("\nMODE=backup -> Backup erstellt, keine Loeschung.")
            return

        print("\n=== Phase 3: Loeschen ===")
        total_deleted = 0
        for top in TARGET_PATHS:
            if is_protected(top):
                continue
            if remote_exists(sftp, top) is None:
                continue
            print(f"Loesche {top} ...")
            n = delete_recursive(sftp, top)
            print(f"  -> {n} Dateien geloescht")
            total_deleted += n
        print(f"\nGesamt geloescht: {total_deleted} Dateien")
        print(f"Backup-Archiv: {archive_path}")
    finally:
        sftp.close()
        transport.close()
        print("\nVerbindung geschlossen.")


if __name__ == "__main__":
    main()

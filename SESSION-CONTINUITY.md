# SESSION-CONTINUITY — Wie deploye ich liar-entertainer.com

**Erstellt:** 22.05.2026 | **Zweck:** Schnellreferenz für alle künftigen Claude-Sessions.

---

## 🎯 Das Wichtigste in 3 Sätzen

1. **Hier arbeiten:** `C:\Users\ben_m\Dev\liar-entertainer-blog\` (NICHT der Cowork-Sandbox-Ordner unter OneDrive — der ist nur ein unvollständiger Schnappschuss).
2. **Deployen geht so:** `git add -A && git commit -m "..." && git push origin main` → GitHub Actions baut + uploaded automatisch zu IONOS.
3. **Live-URL:** https://liar-entertainer.com (hostet auf IONOS Webspace Premium, Ordner `/LIARastro/`).

---

## 🏗 Stack-Übersicht

```
┌─────────────────────────────────────────────────────────┐
│  Source:  github.com/ben69mikail/liar-entertainer-blog  │
│  Branch:  main                                          │
└────────────────────┬────────────────────────────────────┘
                     │ git push
                     ▼
┌─────────────────────────────────────────────────────────┐
│  GitHub Actions: .github/workflows/deploy.yml          │
│  1. Checkout                                            │
│  2. Setup Node 20 + Cache                               │
│  3. Install Poppins-Fonts (für sharp/SVG-Overlay)       │
│  4. npm ci                                              │
│  5. npm run build  →  dist/                             │
│  6. python deploy_ionos.py  →  SFTP-Upload              │
│  7. (optional) n8n Webhook-Notify                       │
└────────────────────┬────────────────────────────────────┘
                     │ SFTP via paramiko
                     ▼
┌─────────────────────────────────────────────────────────┐
│  IONOS Webhosting Premium                               │
│  Server: home362401740.1and1-data.host                  │
│  User:   u62702423                                      │
│  Pfad:   /LIARastro/                                    │
│  Domain: liar-entertainer.com (+ CDN aktiv)             │
└─────────────────────────────────────────────────────────┘
```

---

## 🔑 GitHub-Secrets (alle gesetzt)

In `Settings → Secrets and variables → Actions`:

| Secret | Beschreibung |
|---|---|
| `IONOS_SFTP_HOST` | `home362401740.1and1-data.host` |
| `IONOS_SFTP_USER` | `u62702423` |
| `IONOS_SFTP_PASS` | (geheim, im Vault) |
| `IONOS_SFTP_REMOTE` | `/LIARastro` |

Wenn das Passwort mal neu gesetzt werden muss: IONOS-Kundenbereich → Hosting → SFTP & SSH → Verwalten → Hauptbenutzer u62702423 → Passwort neu setzen → in GitHub-Secret aktualisieren.

---

## ⚡ Lokal arbeiten

```bash
# Einmalig: Dependencies installieren
cd C:\Users\ben_m\Dev\liar-entertainer-blog
npm install

# Lokal entwickeln (Dev-Server auf http://localhost:4321)
npm run dev

# Lokal build prüfen (vor Push)
npm run build

# Lokal direkt zu IONOS deployen (ohne GitHub Actions, z.B. für Notfall)
# Voraussetzung: .env mit SFTP-Daten anlegen (siehe .env.example)
python deploy_ionos.py
```

---

## 🚀 Standard-Workflow für Code-Änderungen

```bash
cd C:\Users\ben_m\Dev\liar-entertainer-blog

# 1. Aktuellen Stand holen (wichtig wenn n8n-Bot zwischendurch committed hat)
git pull origin main

# 2. Änderungen machen, lokal testen
npm run dev

# 3. Committen + Pushen
git add -A
git commit -m "klare Beschreibung der Änderung"
git push origin main

# 4. Deploy beobachten
# → https://github.com/ben69mikail/liar-entertainer-blog/actions
# → Typische Dauer: 4-9 Min
```

---

## 📂 Wichtige Ordner im Repo

| Pfad | Zweck |
|---|---|
| `src/pages/` | Astro-Seiten (.astro Routes) |
| `src/content/blog/` | Blog-Posts als Markdown |
| `src/utils/heroOverlay.ts` | Hero-Image-Generator (sharp, 1200×630) |
| `src/utils/storyOverlay.ts` | Story-Image-Generator (1080×1920 für FB/IG) |
| `public/hero-generated/` | Generierte Cover-Bilder pro Blog-Post |
| `public/blog-images/<slug>/` | Cover, Inline 1-3, Story pro Blog-Post |
| `scripts/` | Build-Hooks (Prebuild für Overlays) |
| `.github/workflows/deploy.yml` | Die zentrale Deploy-Pipeline |
| `deploy_ionos.py` | SFTP-Upload-Script (von GitHub Actions UND lokal aufrufbar) |

---

## 🤖 Automation-Bridge: n8n

Es gibt einen n8n-Workflow `XxHIVhsD4ZPzVa78`, der Blog-Artikel automatisch generiert, ins Repo committed und damit den GitHub-Actions-Deploy triggered. Der Commit erscheint dann als `[skip ci] images: ...` oder `blog: ...` von `ben69mikail`.

**Folge:** Manchmal sind Commits im Repo, die nicht von dir kommen — immer `git pull` vor neuen Änderungen.

---

## 🌐 Weitere Domains am Webspace

Der IONOS-Webspace hostet **3 Domains** insgesamt:

1. **liar-entertainer.com** → `/LIARastro/` (dieser Astro-Code)
2. **zauberer-liar.de** → `/zauberer-nrw/` (separate Microsite "Französischer Zauberer")
3. **(1 weitere Domain)** → wahrscheinlich `/Pantomime/` oder `/LIAR-SEO/`

Diese 3 Microsites haben eigene Codebases — der LIAR-Astro-Code beeinflusst sie nicht.

---

## 🚮 Legacy-Ordner im Webspace (nicht löschen ohne Prüfung)

Aus der WordPress-Zeit (2015-2023) liegen noch im IONOS-Webspace-Root:

- `/admin/`, `/login/`, `/assets/`, `/content/` — von außen **HTTP 404** (nicht erreichbar, kein Sicherheitsrisiko)
- `/wp-admin/`, `/wp-login.php`, `/xmlrpc.php` — von außen **HTTP 301** Redirect (über .htaccess geschützt)
- `/LIARastroBACKUP/` — Backup vom 06.04.2026 (vor Astro-Migration), nicht löschen — Rollback-Sicherheit
- `/.bash_history`, `/.htaccess`, `/index.php`, `/php.ini` im Root — Legacy, momentan harmlos

**Site-Scan-Warnung von IONOS:** Wurde gemeldet, Ursache noch zu klären. Wahrscheinlich alte PHP-Version oder Security-Header.

---

## 🆘 Troubleshooting

### „Deploy ist fehlgeschlagen"
→ https://github.com/ben69mikail/liar-entertainer-blog/actions → letzter Run → Logs.
Häufige Ursachen: SFTP-Verbindungsfehler (IONOS down), Build-Fehler (npm-Dep-Konflikt), Sharp-Probleme.

### „Änderung nicht sichtbar nach Push"
→ Browser-Cache leeren (Strg+Shift+R). Astro generiert hashed CSS-Namen, die Cachen sind 1 Jahr immutable.
Falls weiterhin nicht sichtbar: Actions-Run prüfen, ob er wirklich grün ist.

### „SFTP-Passwort vergessen"
→ IONOS-Kundenbereich → Hosting f9acac9b-5403-436b-a1dd-663689c9c932 → SFTP & SSH → Hauptbenutzer u62702423 → Passwort neu setzen → GitHub-Secret `IONOS_SFTP_PASS` aktualisieren.

### „Lokaler Build geht nicht"
→ Node 20 verwenden (gleiche Version wie CI). `npm ci` statt `npm install`. Bei Sharp-Problemen: `npm rebuild sharp`.

---

## 🔗 Wichtige Links

- **Live-Site:** https://liar-entertainer.com
- **Repo:** https://github.com/ben69mikail/liar-entertainer-blog
- **Actions (Deploys):** https://github.com/ben69mikail/liar-entertainer-blog/actions
- **Secrets:** https://github.com/ben69mikail/liar-entertainer-blog/settings/secrets/actions
- **IONOS Webspace:** https://mein.ionos.de/webhosting/f9acac9b-5403-436b-a1dd-663689c9c932
- **Google Search Console:** https://search.google.com/search-console

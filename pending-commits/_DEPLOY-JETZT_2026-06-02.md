# Pending-Commits — Deploy-Anleitung (konsolidiert 2026-06-02)

> Von Claude gegen den Live-Repo-Stand geprüft. Schreibzugriff war blockiert
> (PAT read-only → `Authentication Failed`), daher Deploy lokal von deinem Rechner.
> Repo: `ben69mikail/Liar-Entertainer`, branch `main`.

## Schritt 0 — PAT erneuern (löst den Dauer-Blocker)
GitHub → Settings → Developer settings → **Fine-grained tokens** → neuer Token:
- Repository access: nur `ben69mikail/Liar-Entertainer`
- Permissions → **Contents: Read and write**
- Ablauf: 90 Tage (der neue Wächter-Task erinnert dich rechtzeitig)

Dann lokal:
```powershell
cd C:\Users\ben_m\Dev-Claude\Liar-Entertainer-fresh
git pull origin main
```

## Status der Pending-Commits (gegen Live geprüft)

| # | Inhalt | Live-Stand | Aktion |
|---|--------|-----------|--------|
| **A1** | City-410 `.htaccess` (Drop-in) | Live-`.htaccess` SHA `db0af6d` hat KEINEN 410-Block → City-URLs = 404 | ✅ **PUSHEN** |
| **A2** | robots.txt: 2 attachment-Disallow | Live-robots SHA `698b7698` hat sie NICHT | ✅ **PUSHEN** |
| **B** | sitemap.xml.ts: 2 Redirect-URLs filtern | Code-Fix, nicht live | ✅ **PUSHEN** |
| C | .htaccess WP-Legacy-Block (29.05.) | wp-content→410 ist BEREITS live | ⏭️ ÜBERSPRINGEN (überholt) |
| D | zauberer reviewCount 300→400 | Bereits live (400 bestätigt 01.06.) | ⏭️ ÜBERSPRINGEN (überholt) |
| E | ALT-Attrs / H2-Typo / Nav-titles (29.05.) | Unklar nach Redesign 01.06. — erst prüfen | ⚠️ PRÜFEN vor Push |

## Deploy der 3 offenen Commits

### A1 — City-410 .htaccess (höchste Priorität)
Die fertige Datei liegt in `pending-commits\2026-06-02-htaccess-city-410\.htaccess`.
```powershell
copy "C:\Users\ben_m\Dev-Claude\projects\Homepage LIAR\pending-commits\2026-06-02-htaccess-city-410\.htaccess" `
     "C:\Users\ben_m\Dev-Claude\Liar-Entertainer-fresh\public\.htaccess"
cd C:\Users\ben_m\Dev-Claude\Liar-Entertainer-fresh
git add public/.htaccess
git commit -m "fix(seo): [2026-06-02] city-URLs 410 statt 404 + wp-content Asset ohne 301-Hop"
```

### A2 — robots.txt
In `public\robots.txt` nach der Zeile `Disallow: /404` ergänzen:
```
Disallow: /*/attachment/*
Disallow: /attachment/*
```
```powershell
git add public/robots.txt
git commit -m "chore(seo): [2026-06-02] robots.txt attachment-disallow"
```

### B — sitemap.xml.ts (Diff in 2026-06-01_sitemap-redirect-fix.md)
`REDIRECTING_PATHS`-Set + `continue`-Zeile aus dem Diff einfügen in
`src\pages\sitemap.xml.ts`, dann:
```powershell
git add src/pages/sitemap.xml.ts
git commit -m "chore(seo): [2026-06-01] sitemap: redirect-URLs entfernen"
```

### Push (löst Auto-Deploy aus)
```powershell
git push origin main
# GitHub Actions baut + SFTP-Deploy nach IONOS (4-9 Min)
```

## Verifikation (60 Sek nach Deploy)
```bash
curl -sI -L https://liar-entertainer.com/zauberer/bochum/ | grep -i ^HTTP | tail -1   # erwartet: 410
curl -sI -L https://liar-entertainer.com/zauberer/zaubershow/ | grep -i ^HTTP | tail -1  # 200 (Whitelist!)
curl -sI -L https://liar-entertainer.com/clown/kindergeburtstag/ | grep -i ^HTTP | tail -1  # 200 (via 301)
curl -s https://liar-entertainer.com/robots.txt | grep attachment   # 2 Disallow-Zeilen
```

## Nach erfolgreichem Deploy
- Diesen Ordner `pending-commits\` leeren (gepushte Dateien archivieren/löschen).
- In GSC: City-URLs als 410 neu validieren, "Seite mit Weiterleitung" erneut anstoßen.

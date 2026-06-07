# Pending-Commits — Deploy-Anleitung (Stand 2026-06-02, Pfade: C:\Users\ben_m\Claude)

> Repo: ben69mikail/Liar-Entertainer, branch main. Workspace = dieses Repo.
> Schreibzugriff war blockiert (PAT-Cache der laufenden Session). In FRISCHEM Chat pushen,
> ODER lokal per git (der bewährte 49+-Deploy-Weg).

## 3 offene Commits (gegen Live geprüft)

| # | Inhalt | Live-Stand | Aktion |
|---|--------|-----------|--------|
| A1 | City-410 .htaccess (Drop-in) | Live db0af6d hat KEINEN 410-Block → City-URLs = 404 | PUSHEN |
| A2 | robots.txt: 2 attachment-Disallow | Live 698b7698 hat sie nicht | PUSHEN |
| B  | sitemap.xml.ts: 2 Redirect-URLs filtern | nicht live | PUSHEN |

ÜBERSPRINGEN (bereits live, geprüft): wp-content-410-Block, reviewCount 300→400.

## A1 — City-410 .htaccess (höchste Priorität)
Fertige Drop-in-Datei: `2026-06-02-htaccess-city-410/.htaccess` (kompletter public/.htaccess).
Basis-SHA `db0af6d`. Beim Deploy den ganzen Inhalt als `public/.htaccess` committen.
Einzige Unterschiede zur Live-Datei: (1) Asset-Endungen in der Trailing-Slash-Regel
ausgeschlossen, (2) City-410-Block am Ende (nach allen MUSTER-301), Whitelist schützt
echte Astro-Roots (zaubershow, clownshow, kinderzauberer, …).
Commit: `fix(seo): [2026-06-02] city-URLs 410 statt 404 + wp-content Asset ohne 301-Hop`

## A2 — robots.txt
Nach `Disallow: /404` zwei Zeilen ergänzen:
```
Disallow: /*/attachment/*
Disallow: /attachment/*
```
Commit: `chore(seo): [2026-06-02] robots.txt attachment-disallow`

## B — sitemap.xml.ts
`REDIRECTING_PATHS`-Set oben anlegen (`/clown/clown-zauberer/`, `/zauberer/zaubershow/karneval/`)
und im WP-Items-Loop `if (REDIRECTING_PATHS.has(path)) continue;` einfügen.
Commit: `chore(seo): [2026-06-01] sitemap: redirect-URLs entfernen`

## Push (lokal — der bewährte 49+-Deploy-Weg)
```powershell
cd C:\Users\ben_m\Claude\Liar-Entertainer-fresh
git pull origin main
# A1/A2/B anwenden
git add -A
git commit -m "fix(seo): [2026-06-02] city-410 + robots attachment + sitemap redirect-filter"
git push origin main
# → GitHub Actions baut + SFTP-Deploy nach IONOS (4-9 Min)
```

## Verifikation (60 Sek nach Deploy)
- curl -sI -L https://liar-entertainer.com/zauberer/bochum/  → erwartet 410
- curl -sI -L https://liar-entertainer.com/zauberer/zaubershow/ → erwartet 200 (Whitelist!)
- curl -sI -L https://liar-entertainer.com/clown/kindergeburtstag/ → erwartet 200 (via 301)
- curl -s https://liar-entertainer.com/robots.txt | grep attachment → 2 Zeilen

## Hinweis
Der City-410-`.htaccess`-Volltext ist im Daily-Autopilot-Wissen + GitHub-Historie reproduzierbar.
Falls die Drop-in-Datei fehlt: Live-`.htaccess` holen (get_file_contents), den City-410-Block
+ Asset-Ausschluss laut dieser Anleitung ergänzen.

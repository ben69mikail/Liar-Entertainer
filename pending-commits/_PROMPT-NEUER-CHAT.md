# Prompt für neuen Chat — kopieren & einfügen

Push die 3 offenen LIAR-Pending-Commits ins Repo `ben69mikail/Liar-Entertainer` (branch main).
Die fertigen Dateien + Anleitung liegen in `C:\Users\ben_m\Dev-Claude\projects\Homepage LIAR\pending-commits\`.
Lies dort zuerst `_DEPLOY-JETZT_2026-06-02.md` — sie listet exakt, was offen ist und was übersprungen wird.

Konkret committen (in dieser Reihenfolge, je ein Commit):
1. `public/.htaccess` — kompletter Inhalt aus `2026-06-02-htaccess-city-410/.htaccess` (City-410-Fix).
   Commit: `fix(seo): [2026-06-02] city-URLs 410 statt 404 + wp-content Asset ohne 301-Hop`
2. `public/robots.txt` — 2 Zeilen ergänzen nach `Disallow: /404`:
   `Disallow: /*/attachment/*` und `Disallow: /attachment/*`
   Commit: `chore(seo): [2026-06-02] robots.txt attachment-disallow`
3. `src/pages/sitemap.xml.ts` — REDIRECTING_PATHS-Diff aus `2026-06-01_sitemap-redirect-fix.md`.
   Commit: `chore(seo): [2026-06-01] sitemap: redirect-URLs entfernen`

NICHT pushen (bereits live, geprüft): wp-content-410-Block, reviewCount 300→400.

Nach jedem Push die SHA per get_file_contents frisch holen. Nach Deploy (60 Sek) verifizieren:
- curl -sI -L https://liar-entertainer.com/zauberer/bochum/  → erwartet 410
- curl -sI -L https://liar-entertainer.com/zauberer/zaubershow/ → erwartet 200 (Whitelist!)
- curl -sI -L https://liar-entertainer.com/clown/kindergeburtstag/ → erwartet 200 (via 301)
- curl -s https://liar-entertainer.com/robots.txt | grep attachment → 2 Zeilen

Falls wieder "Authentication Failed: Requires authentication": GitHub-MCP nutzt
`api.githubcopilot.com` und braucht ggf. einen CLASSIC PAT mit `repo`-Scope statt fine-grained.
Token liegt in der Umgebungsvariable GITHUB_PERSONAL_ACCESS_TOKEN.

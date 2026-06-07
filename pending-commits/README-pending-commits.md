# Pending Commits — LIAR SEO Autopilot (Stand: 29.05.2026)

GitHub MCP Auth ist temporär ausgefallen. Diese Dateien enthalten alle geplanten Änderungen.
Der Daily-Autopilot (läuft täglich 06:00) kann diese beim nächsten erfolgreichen Run pushen.

## Status

| Commit | Datei | Inhalt | Status |
|--------|-------|--------|--------|
| A | commit-1-robots-txt.txt | robots.txt + zauberer 300→400 | ⏳ Warte auf GitHub Auth |
| B | commit-2-ueber-mich-kinderzauberer-header.md | ALT-Attrs + H2-Typo + Nav titles | ⏳ Warte auf GitHub Auth |
| C | commit-3-htaccess-legacy-block.md | .htaccess WP-Legacy-Block | ⏳ Warte auf GitHub Auth |

## Commit A — robots.txt + zauberer Hero-Text
**Message:** `chore(seo): [autopilot 2026-05-29] robots.txt attachment-disallow + zauberer review-count 300→400`

Änderungen:
- `public/robots.txt`: 2 neue Disallow-Zeilen für `/*/attachment/*` und `/attachment/*`
- `src/pages/zauberer/index.astro`: Hero-Text "300" → "400" Bewertungen + imgAlt Tisch-Zauberer verbessert

## Commit B — ALT-Attribute + H2-Typo + Header Nav Titles
**Message:** `chore(seo): [autopilot 2026-05-29] ueber-mich ALT-fixes + kinderzauberer H2-typo + header-nav-titles`

Änderungen:
- `src/pages/ueber-mich/index.astro`: 3 ALT-Attribute keyword-optimiert
- `src/pages/kinderzauberer/index.astro`: H2-Typo "WISSENWERTES"/"ZAuberer" korrigiert
- `src/components/Header.astro`: title-Attribute auf alle Nav-Links ergänzt

## Commit C — .htaccess WordPress-Legacy-Block
**Message:** `chore(seo): [autopilot 2026-05-29] htaccess WordPress-Legacy-Aufräumblock`

Änderungen:
- `public/.htaccess`: 18 RewriteRules für WP-Legacy-Pfade ans Ende anhängen

## Manuelle Aktionen ausstehend (Michael)

1. **GA4 Measurement ID** eintragen in `src/layouts/BaseLayout.astro`:
   - Aktuell auskommentiert, Platzhalter `G-XXXXXXX`
   - GA4-Property öffnen → Admin → Data Streams → Measurement ID kopieren
   - In der Zeile `<!-- gtag('config', 'G-XXXXXXX'); -->` die ID ersetzen und Kommentar entfernen

2. **GSC Verification Meta Tag** in `src/layouts/BaseLayout.astro`:
   - GSC öffnen → Einstellungen → Eigentumsnachweis → HTML-Tag
   - Meta-Tag-Code in BaseLayout.astro eintragen (aktuell auskommentiert)

3. **Daily-Autopilot SKILL.md** aktualisieren:
   - Pfad: `C:\Users\ben_m\OneDrive\Dokumente\Claude\Scheduled\liar-daily-seo-autopilot\SKILL.md`
   - Die neue Version liegt unter: `C:\Users\ben_m\OneDrive\Dokumente\Claude\Projects\Homepage LIAR\liar-daily-seo-autopilot-v2-SKILL.md`

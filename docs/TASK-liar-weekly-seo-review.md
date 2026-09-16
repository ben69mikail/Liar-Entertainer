# Scheduled Task: liar-weekly-seo-review — montags 07:00 (Cowork)

Voraussetzung: Der GitHub-Actions-Workflow `seo-daily.yml` läuft täglich und schreibt `seo-reports/daily/daily-seo-YYYY-MM-DD.md`. Diese Session liest die letzten 7 Reports, bewertet, macht den Blog-Vorschlag und behebt, was der Bot nur melden kann.

Täglicher SEO- und Regressionscheck für https://liar-entertainer.com. Du arbeitest autonom, darfst Korrekturen selbst live bringen — nur unter den harten Bedingungen unten. Diese Session hat keine Erinnerung an frühere Läufe; alles Nötige steht hier. Vorheriger Report liegt im Repo unter `seo-reports/daily/` — den letzten lesen, bevor du beginnst.

## Kontext
Astro-Website für Michaël Prescler alias „Clown Zauberer LIAR", Beethovenstr. 15, 45966 Gladbeck. Kinderzauberer, Clown, Zaubershows.
- Repo: https://github.com/ben69mikail/Liar-Entertainer (öffentlich, Branch `main`)
- Live: https://liar-entertainer.com — 168 Seiten (142 in Sitemap)
- **Jeder Push auf `main` deployt sofort live nach IONOS** (GitHub Actions → SFTP). Kein Staging.
- GSC-Property: `sc-domain:liar-entertainer.com`
- Zielgruppe: Eltern in NRW (Kindergeburtstag, mobil, unter Zeitdruck) UND Firmen/Kitas/Schulen/Städte (Zaubershow).
- Prioritätsbegriffe: zauberer, kinderzauberer, clown, kindergeburtstag, zaubershow. Geld-Keyword: `zauberer kindergeburtstag`.
- Abgewertet: Ballonmodellage, Glitzer-Tattoos — bleiben im Angebot, keine Rankingziele.
- Lokal: Gladbeck + 20 km (Gladbeck, Bottrop, Gelsenkirchen, Dorsten, Herten, Oberhausen, Essen, Marl, Recklinghausen, Dinslaken, Herne, Mülheim, Bochum). Überregional: zauberer, kinderzauberer, zaubershow, clown.

## Ablauf (Reihenfolge einhalten)

### 1. Regelwerke gegen frischen Build
```
git clone --depth 1 https://github.com/ben69mikail/Liar-Entertainer.git && cd Liar-Entertainer
npm ci && npm run build
npm run test:seo        # muss 45/45
npm run test:struktur   # muss 10/10
find dist -name index.html | wc -l   # muss ≥ 160 (Soll 167)
```
Rot → Ursache benennen (welche Assertion, welcher Commit seit gestern via `git log --since=1.day`). Fix nur, wenn er eindeutig ist und keine der „Niemals"-Regeln berührt.

### 2. Deploy-Status
https://api.github.com/repos/ben69mikail/Liar-Entertainer/actions/runs?per_page=3 — letzter Run `success`? Wenn `failure`: Log lesen, Ursache nennen. Prüfen, ob live-HTML dem letzten main-Commit entspricht (z. B. `<meta name="generator">`/Build-Hash oder eine im Commit geänderte Zeile per curl vergleichen).

### 3. Live-Erreichbarkeit
- `https://liar-entertainer.com/` 200, `https://www.` und `http://` → 301 einstufig auf https non-www
- robots.txt, sitemap.xml, llms.txt → 200
- Stichprobe 10 Sitemap-URLs (Startseite, /kindergeburtstag/, /kinderzauberer/, /zauberer/zaubershow/, /clown/clownshow/, /preise/, /blog/, 3 zufällige Stadtseiten) → 200, Canonical = URL, genau 1 H1, JSON-LD parsebar
- Legacy: `/category/x/` → 301, `/attachment/x/` → 410
- Optional wenn PSI-Quota frei: `https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://liar-entertainer.com/&strategy=mobile` — LCP, CLS, INP notieren. Quota-Fehler ist kein Befund.

### 4. GSC (per Claude-in-Chrome, Betreiber ist eingeloggt; wenn kein Browser verbunden → Schritt überspringen und im Bericht sagen „GSC nicht geprüft")
Zeitraum: letzte 7 Tage vs. vorherige 7 Tage.
- Leistung: Klicks, Impressionen, CTR, Ø-Position — Delta notieren. Erst ab ±15 % Klicks oder ±20 % Impressionen kommentieren; Wochenschwankung ist normal, keine Ursache erfinden.
- Top-Queries: `zauberer kindergeburtstag`, `kinderzauberer`, `zauberer`, `clown`, `zaubershow`, `zauberer bottrop`, `zauberer gladbeck`, `bühnenzauberer` — Position + Klicks.
- Seitenindexierung: Anzahl indexiert (Baseline 06.08.: 121; Ziel 145+), neue Fehler in „Nicht indexiert" (404, Umleitungsfehler, Soft 404, Serverfehler). Jede NEUE Fehler-URL ist ein Befund.
- Kernvitalitäten mobil: „schlecht" muss 0 bleiben.
- Offene Punkte, deren Status du jedes Mal mitnimmst: K1b CTR-Diagnose (Pos 1–5 / 0 Klicks-Queries), K3 Indexierung haltern/recklinghausen/dorsten, 9 Umleitungsfehler, www-Impressionen.

### 5. Blog-Fälligkeit
Letzten `publishDate` in `src/content/blog/*.md` lesen. Wenn > 7 Tage: nächstes Thema aus dem Redaktionsplan (im Repo `BLOG-REDAKTIONSPLAN-Q4-2026.md`, sonst saisonal passend) als **Vorschlag** mit Titel, 5-Zeilen-Gliederung, Ziel-Query und 3 FAQ-Fragen in den Bericht. **Keinen Artikel schreiben oder committen.** Wenn im Repo ein Artikel mit `draft: true` und Frontmatter `freigabe: ja` liegt → `draft: false` setzen, Publish-Datum = heute, Sitemap prüfen, committen, Deploy abwarten, URL live prüfen.

### 6. Selbst beheben darfst du
- Tote interne Links (404-Ziel) auf das korrekte bestehende Ziel umbiegen
- `.htaccess`/robots.txt-Fehler, die eine URL fälschlich 404/410/blockiert liefern
- JSON-LD-Syntaxfehler, fehlendes `alt`, fehlender/falscher Canonical — nur wenn eine Assertion es meldet
- Blog-Publish nach Freigabe (Schritt 5)
Bedingungen: max. 2 Commits/Tag; jeder Commit erst nach lokal grünem `test:seo` + `test:struktur`; Commit-Message beginnt mit `fix(seo):` oder `blog:`; nach Deploy die betroffene URL live per curl verifizieren; bei Klickeinbruch > 30 % in GSC oder manueller Maßnahme → READ-ONLY, nur berichten.

## Was du NIEMALS anfasst
- **Das Design der Startseite.** Betreiber-Entscheidung 12.08.2026. `scripts/hero-invarianten.mjs` sichert die Struktur ab.
- Menüstruktur, Navigation, Layout
- Texte umschreiben, kürzen oder ergänzen — außer es behebt direkt einen Regelverstoß
- Preise, Preistabellen, Offer-Schema. Regel PR.2: Preis-Schema nur auf `/preise/` und `/kindergeburtstag/*`
- aggregateRating- oder Review-Schema anlegen (Regel K1.2, bewusste Entscheidung)
- Stadtseiten löschen oder anlegen — Regel R4 fixiert 23/23/23
- Neue Blogartikel oder Seiten schreiben. Texte im Namen des Betreibers legt er selbst fest. Vorschläge gewünscht.
- `src/data/pages.json`, `scraped-pages.json` (Legacy-Fixes gehören in `[...slug].astro`)

## Bericht
Datei `seo-reports/daily/daily-seo-YYYY-MM-DD.md` ins Repo committen (Message `[skip ci] report: daily YYYY-MM-DD`) UND als Chat-Antwort. Kurz.
Alles in Ordnung → drei Zeilen: Regelwerke grün, Deploy grün, Seite erreichbar (+ GSC-Delta in einer Zeile, wenn geprüft). Kein Füllmaterial.
Geändert → was, warum, welcher Commit, Deploy durchgelaufen ja/nein, Live-Verifikation.
Befund ohne Erlaubnis zur Behebung → Zahlen, Dringlichkeit (hoch/mittel/niedrig), ein konkreter Vorschlag.
Blog überfällig → Themenvorschlag wie in Schritt 5.
Übertreibe nie. Schwankt ein Wert ohne klare Ursache, sag das. Konntest du etwas nicht prüfen, sag das.

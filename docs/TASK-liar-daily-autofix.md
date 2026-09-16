# Daily Autofix — Anweisungen für Claude in GitHub Actions (seo-autofix.yml)

Du läufst täglich nach dem „SEO Daily Check". Du hast das Repo ausgecheckt, Node und npm. Kein Browser, kein GSC-Zugang — die GSC-Daten stehen im heutigen Report `seo-reports/daily/daily-seo-<heute>.md` (Fokus-Queries, Seiten, Index-Status, Live-Befunde, Blog-Fälligkeit).

## Kontext
Strategie und Zielwerte: `docs/SEO-STRATEGIE-2026-Q4.md` (lesen, wenn du Prioritäten abwägst).
Astro-Site für Michaël Prescler, „Clown Zauberer LIAR", Gladbeck. Ziel: für **zauberer kindergeburtstag / zauberer für kindergeburtstag / kinderzauberer / clown / zaubershow** gefunden werden, Kindergeburtstage im Umkreis 20 km um Gladbeck (Bottrop, Gelsenkirchen, Dorsten, Herten, Oberhausen, Essen, Marl, Recklinghausen, Dinslaken, Herne, Mülheim, Bochum). Jeder Push auf `main` deployt live.

## Ablauf
1. Heutigen Report lesen. Wenn er fehlt: `npm ci && npm run build && node scripts/daily-seo-check.mjs` selbst ausführen.
2. Befunde einordnen: **selbst beheben** (Liste unten) / **PR öffnen** / **nur melden**.
3. Für jede Behebung: Änderung, `npm run build`, `npm run test:seo` (45/45), `npm run test:struktur` (10/10), Seitenzahl ≥ 160. Nur bei grün committen.
4. Blog: Wenn ein Artikel in `src/content/blog/` `draft: true` UND `freigabe: ja` hat → `draft: false`, `freigabe` entfernen, `publishDate` = heute, Build prüfen (Seitenzahl +1), Commit `blog: <slug>`. Ohne `freigabe: ja` nichts tun.
5. Ergebnis als Kommentar in `seo-reports/daily/daily-seo-<heute>.md` unter `## Autofix` anhängen (was geändert, Commit-SHA, was offen). Commit `[skip ci] report: autofix <heute>`.

## Selbst beheben (direkt auf main, Deploy-Gate fängt Rest)
- Interne Links auf 404-Ziele → auf das bestehende Ziel korrigieren
- `public/.htaccess`: URL, die laut Report 404/410 liefert, aber ein klares Ziel hat → 301; alte Blog-Slugs → `/blog/<slug>/`
- JSON-LD-Syntaxfehler, fehlendes `alt`, falscher Canonical — nur wenn `test:seo` es meldet
- Blog-Publish nach Freigabe (Schritt 4)
Limit: max. 2 Commits/Tag auf main. Commit-Message beginnt mit `fix(seo):` oder `blog:`.

## PR statt Commit (Branch `autofix/<heute>-<thema>`, `gh pr create`)
- Title-/Description-Änderungen an Hub-Seiten (`/`, `/kindergeburtstag/`, `/kinderzauberer/`, `/zauberer/`, `/zauberer/zaubershow/`, `/clown/clownshow/`)
- Änderungen an mehr als 3 Dateien
- Alles, was Text sichtbar verändert (Anker, Absätze, FAQ)
Im PR-Text: Befund mit Zahlen aus dem Report, erwarteter Effekt, Risiko.

## Niemals
- Design/Layout der Startseite, Menü, Navigation (`scripts/hero-invarianten.mjs` sichert das ab)
- Preise, Preistabellen, Offer-Schema außerhalb `/preise/` und `/kindergeburtstag/*`
- aggregateRating/Review-Schema
- Stadtseiten anlegen/löschen (23/23/23)
- Blogartikel schreiben oder ohne `freigabe: ja` veröffentlichen
- `src/data/pages.json`, `scraped-pages.json` anfassen
- Bei Klickeinbruch > 30 % (Report-Alarm) oder rotem Deploy: nichts committen, nur melden

## Ton im Report
Kurz. Zahlen statt Adjektive. Keine Ursache erfinden, wenn ein Wert schwankt. Wenn nichts zu tun war: „Autofix: nichts zu tun."

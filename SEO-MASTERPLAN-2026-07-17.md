# SEO-MASTERPLAN — liar-entertainer.com (2026-07-17)

**Basis:** 7 parallele Spezial-Audits (Technik, GEO/KI-Suche, Local, Schema, Sitemap, Bilder, Content) auf Live-Site + Repo, plus frische GSC- und GA4-Daten (17.07.), Autopilot-State (`.seo-autopilot/state.json`), GSC-Wochenverlauf, Alt-Audits 04/2026 + ACTION-PLAN.md.
**Modus:** NUR PLAN — es wurde nichts geändert. Inhalte werden nicht angefasst, bis Michael freigibt.

---

## 0. WICHTIGSTER PROZESS-BEFUND

⚠️ **Das lokale Repo ist 31 Commits hinter origin/main** (lokal `26c1ab7` 02.07., origin `41d4852` 17.07., deployed). Die Live-Site = origin/main, u. a. mit „SEO Batch C/D/E" (Preis-Leaks raus, FAQ+Schema, neue Landingpages Hochzeit/Firmenfeier).
➡️ **Vor JEDER Umsetzung: `git pull`.** Mehrere Befunde der Alt-Audits (Review-Markup, sichtbare Preise, Glitzer-Tattoo-Schema) sind auf origin/main bereits erledigt.

---

## 1. EXECUTIVE SUMMARY

### Scores (heute)

| Bereich | Score | Trend vs. 04/2026 |
|---|---|---|
| Technical SEO | 88/100 | ↑ (www-Mismatch behoben, Redirects sauber, Security-Header komplett) |
| Local SEO / City-Pages | 76/100 | ↑↑ (Alt-Befunde Descriptions/Titles/Grammatik alle behoben) |
| Content / E-E-A-T | 68/100 | ↔ (City-Pages top, Blog-Money-Content fehlt weiter) |
| GEO / KI-Suche | 68/100 | ↑ (llms.txt vorbildlich, Leads auf Hubs; City-Pages noch nicht KI-zitierfähig) |
| Schema | gut, 1 Critical | ↑ (Review-Penalty-Risiko live beseitigt) |
| Bilder | kritisch im Blog | ↓ (410-Regel hat Legacy-Blog bildlos gemacht) |

### Frische Daten (17.07.)

**GSC (3 Monate, Stand ~15.07.):** 2.080 Klicks / 83.600 Impr. / CTR 2,5 % / Pos. 11,5 — stetig steigend (18.06.: 1.840 → 02.07.: 2.020 → jetzt 2.080).
**GSC Indexierung — Datenlag endlich aufgelöst:** Nicht-indexiert **792 → 546** ✅ (404er 258→190, Gecrawlt-nicht-indexiert 362→235, Weiterleitungen 152→99). Aber: **Indexiert 131 → 112** (↓19, beobachten!), robots-blockiert 8→10.
**GA4 (28 Tage):** 1.002 Sitzungen — 69,5 % Organic, 27,5 % Direct, **1,4 % „AI Assistant"** (KI-Suche liefert bereits messbar Traffic, Engagement 57 %). 🚨 **0 Schlüsselereignisse konfiguriert** — Conversions (Kontaktanfragen) sind komplett unmessbar.
**Neues Chancen-Keyword:** „kindergeburtstag bei hitze" 25 Klicks/429 Impr. — Saisonartikel wirken.

### Top-5-Sofortprobleme

1. 🔴 `/zauberer/hochzeit/` + `/zauberer/firmenfeier/` (heute deployed!) liefern **410 Gone** — alte Catch-All-Regel in `.htaccess` frisst sie; beide stehen in der Sitemap.
2. 🔴 **30 Legacy-Blogposts + Blog-Index seit ~6 Wochen mit kaputten Bildern** (eigene 410-Regel auf `/wp-content/uploads/*`) — Content-Bilder, Thumbnails UND og:image tot.
3. 🔴 **36 City-Pages (kinderzauberer-in-\*, clown-in-\*) mit `offers: 150 €` im Schema, aber ohne sichtbaren Preis** (Batch E hat Preise bewusst entfernt — Preis-Policy). Markup-Mismatch = Richtlinienverstoß. Fix: offers aus dem Schema entfernen, NICHT Preis sichtbar machen.
4. 🔴 **GA4 ohne Schlüsselereignisse** — SEO-Erfolg nicht in Anfragen messbar.
5. 🟠 **Title-Kannibalisierung** /kindergeburtstag/ vs. /kinderzauberer/ (fast identische Titles) — erklärt CTR 1,3 % bei 1.354 Impr. für „zauberer kindergeburtstag".

---

## 2. PHASE 0 — SOFORT (diese Woche)

| # | Maßnahme | Datei/Ort | Aufwand |
|---|---|---|---|
| 0.1 | **`git pull`** — Pflicht vor allem anderen | Repo | 1 Min |
| 0.2 | **410-Fix Landingpages:** Whitelist erweitern auf `^zauberer/(buehnen-zauberer\|tisch-zauberer\|zaubershow\|kinderzauberer\|hochzeit\|firmenfeier)(/.*)?$` | `public/.htaccess` ~Z. 412 (origin-Stand) | 10 Min |
| 0.3 | Nach 0.2: Sitemap in GSC neu einreichen + Indexierung für beide URLs beantragen | GSC | 5 Min |
| 0.4 | **Legacy-Blog-Bilder reparieren:** Bilder lokal einspielen (Backup/`src/assets`) + URL-Mapping in `posts.json`/`[...slug].astro`; mind. Sofortmaßnahme: `FALLBACK_IMG` in `src/utils/allPosts.ts` + Thumbnail-Logik auf lokale Assets → 30 kaputte Thumbnails auf /blog/ sofort weg | `src/data/posts.json`, `src/pages/[...slug].astro`, `src/utils/allPosts.ts` | 0,5–1 Tag |
| 0.5 | **`offers` aus 36 City-Schemas entfernen** (kinderzauberer-in-\*, clown-in-\*; die 23 geburtstag-in-\* behalten Offer — Preis dort sichtbar) | je `index.astro`, Frontmatter | 1–2 Std (skriptbar) |
| 0.6 | **GA4 Schlüsselereignisse:** Formular-Absenden (/kontakt/ → /kontakt/danke/), `tel:`-Klick, `mailto:`-Klick als Key Events markieren | GA4-Admin + ggf. Event-Snippets | 1 Std |
| 0.7 | og:image der Legacy-Posts + `ueber-mich`-Person-Schema-`image` von 410-URLs auf lokale Bilder | `[...slug].astro`, `ueber-mich/index.astro` | 30 Min |

## 3. PHASE 1 — HOCH (Woche 1–2)

| # | Maßnahme | Detail |
|---|---|---|
| 1.1 | **CTR-Paket Titles/Descriptions** (4 Seiten, Vorschläge fertig ausformuliert im Content-Audit): /kindergeburtstag/ „Zauberer für Kindergeburtstag NRW ab 150 € \| LIAR", /kinderzauberer/ entkannibalisieren („Kinderzauberer NRW buchen \| ab 150 € \| Clown LIAR"), /clown/clownshow/ („Clown für Kindergeburtstag NRW \| ab 150 € \| LIAR" + Wort „mieten" in Description/FAQ), /zauberer/zaubershow/ („Zaubershow für Kinder NRW \| 40 Min. ab 150 € \| LIAR"). Größter Hebel pro Aufwand: +2 pp CTR ≈ +27 Klicks/Monat allein auf Keyword #1 |
| 1.2 | **`kinderzauberer-in-gladbeck` erstellen** — Heimatstadt fehlt ausgerechnet in der Top-Keyword-Kategorie. USP: „keine Fahrtkosten" |
| 1.3 | **og:image absolut machen:** in `BaseLayout.astro` `new URL(ogImage, Astro.site)` erzwingen — aktuell relative Pfade → WhatsApp/Facebook-Previews kaputt auf ~60 Seiten |
| 1.4 | **`public/blog-images/` komprimieren:** 11 Dateien > 1 MB (max. 7,2 MB!) → ≤ 200 KB WebP oder in Astro-Pipeline (`src/assets/`) — LCP-Killer auf 6 neuen Blogposts |
| 1.5 | **Sichtbare FAQ auf /zauberer/:** Schema enthält 4 perfekte Fragen (inkl. Preis-Frage) — sichtbar als `<details>`-Accordion ausspielen (Schema-Content-Mismatch beheben). Nach git pull verifizieren, ob Batch D/E das schon erledigt hat |
| 1.6 | **Preis-FAQ sichtbar** auf /kindergeburtstag/, /kinderzauberer/, /preise/: „Was kostet ein Zauberer für den Kindergeburtstag?" mit 40–60-Wort-Direktantwort (150 € / 40 Min / bis 12 Kinder / ab 4 J. / +20 € Ballons / +40 € Tattoos / 0,40 €/km ab Gladbeck) — wichtigste Money-Query als zitierfähige Passage. Policy-konform (Kindergeburtstag-Kontext) |
| 1.7 | **BreadcrumbList auf alle 59 City-Pages** — BaseLayout-Prop existiert, nur befüllen |
| 1.8 | **`public/sitemap.xml` löschen** (tote Doublette, hat schon einmal einen wirkungslosen Fix verursacht — echter Generator ist `src/pages/sitemap.xml.ts`) |
| 1.9 | **GSC beobachten:** Indexiert-Rückgang 131→112 im nächsten Wochen-Check klären (vermutlich Legacy-Deindexierung, aber gegensteuern falls Kernseiten betroffen); robots-blockiert 8→10 prüfen |

## 4. PHASE 2 — MITTEL (Woche 3–6)

**KI-Suche (Priorität Michael):**
| # | Maßnahme |
|---|---|
| 2.1 | **KI-Antwort-Lead auf alle ~59 City-Pages** (`class="hero-subtitle"`, aktiviert zugleich den speakable-Selektor, der dort aktuell ins Leere läuft). ⚠️ Preis-Policy: auf geburtstag-in-\* mit „ab 150 €", auf kinderzauberer-/clown-City-Pages OHNE Preis (Stadt + Dauer + Alter + Anfahrt + Bewertungen). Skriptbar |
| 2.2 | **`public/llms-full.txt`** mit Volltexten der 5 Hubs + Preise + Über-mich; in llms.txt verlinken |
| 2.3 | **Entity-Graph schließen:** `@id`-Knoten `#person` (mit sameAs) ↔ `#business` (`founder`), `WebSite`-Knoten `#website`, `speakable` von LocalBusiness in einen per-Page-`WebPage`-Knoten verschieben, Service-`provider` als `{"@id": "#business"}` referenzieren (JSON-LD-Vorlagen im Schema-Audit) |
| 2.4 | **sameAs + YouTube:** Kanal-URL in LocalBusiness- und Person-sameAs (stärkstes KI-Zitations-Signal); www/non-www-Konsistenz in Schema/llms.txt prüfen (kanonisch = non-www) |
| 2.5 | **Fragen-H2s auf Hubs** („Wie läuft die Zaubershow ab?", „Für welches Alter geeignet?") statt Label-Überschriften |

**Content (nur nach Freigabe — Inhalte-Sperre beachten):**
| # | Maßnahme |
|---|---|
| 2.6 | **Blog-Pipeline reaktivieren** (letzter Artikel 21.05.!) + Autopilot-Briefing erweitern: Pflicht 2–3 City-Links + 1 Kontakt-Link pro Artikel |
| 2.7 | **Pillar-Artikel #1, #4, #6** aus ACTION-PLAN zuerst: „Was kostet ein Zauberer zum Kindergeburtstag?" (trifft 1.354-Impr-Keyword), „Clown oder Zauberer?", „Luftballonmodellage" — je mit FAQPage-Schema |
| 2.8 | **Blog-Template-Fixes (1× zentral, wirkt auf 36 Artikel):** Autorbox mit Credentials, `Person`-`@id`-Verknüpfung zu /ueber-mich/, echtes `dateModified`-Frontmatter-Feld |
| 2.9 | **Hub-Content-Tiefe:** /zauberer/zaubershow/ (~420 W.) und /kinderzauberer/ (~580 W.) auf 800+ Wörter |
| 2.10 | **„Bekannt von"-Referenzblock** auf /ueber-mich/ (IKEA Duisburg, ExtraSchicht, Appeltatenfest — steckt schon in Legacy-Posts) |

**Local:**
| # | Maßnahme |
|---|---|
| 2.11 | Restliche 9 City-Lücken: clown-in-moers, dann K+C für Castrop-Rauxel/Waltrop/Wesel/Xanten. ⚠️ Doorway-Schwelle: nur mit 60 %+ Unique-Content pro Seite, nicht weiter skalieren |
| 2.12 | LocalBusiness härten: `addressRegion: "NW"`, `image`/`logo`, `openingHoursSpecification`, geo exakt auf GBP-Pin |
| 2.13 | „Bewertung auf Google schreiben"-Link (Place-ID vorhanden) in GoogleReviews-Widget + Footer — Review-Velocity |
| 2.14 | NAP komplett in Footer (Adresse fehlt), aus `siteConfig` (src/lib/data.ts) ziehen statt hardcoden |
| 2.15 | GBP manuell: primäre Kategorie prüfen („Zauberer"/„Kinderentertainer", nicht „Clown"), 11880.com-Kategorie korrigieren („Kunst & Kunstgewerbe" → „Unterhaltungskünstler") |

**Technik/Bilder:**
| # | Maßnahme |
|---|---|
| 2.16 | 15 leere Galerie-Alt-Texte füllen (lokale Keywords), 5 `<img>` ohne alt in `[...slug].astro` |
| 2.17 | Sitemap-`lastmod` aus Git-Datum generieren oder Feld entfernen; `priority`/`changefreq` raus (Google ignoriert) |
| 2.18 | Blog-Kategorieseiten: Müll-Kategorien (`/e/`, `/f/` …) noindex/nicht bauen, werthaltige in Sitemap (erst prüfen, ob Batch C das erledigt hat) |
| 2.19 | PSI-API-Key anlegen → CWV-Wochenmessung in Autopilot integrieren (CWV aktuell ungemessen) |
| 2.20 | `og-startseite.jpg` auf echte 1200×630 |

## 5. PHASE 3 — NIEDRIG / LAUFEND

- **Wikidata-Item** für „Clown Zauberer LIAR / Michaël Prescler" (günstigster Knowledge-Graph-Einstieg)
- **YouTube-Kanal ausbauen** + authentische Community-Präsenz (stärkste KI-Zitations-Korrelation)
- Catch-All-301 (`Fantasie-URLs ≥20 Zeichen → /blog/`) befristen; falls GSC-„Weiterleitungsseiten" bis ~Sept. nicht fällt: Top-50-Slugs auf 410
- Duplicate-Reduktion kinderzauberer-/clown-City-Serien (Overlap 35–38 % → Ziel <20 %; Vorbild geburtstag-Serie: 5 %)
- Erwachsenen-Segment: /zauberer/tisch-zauberer/ auf 1.500 Wörter + neue Hochzeit/Firmenfeier-Landingpages stärken (NACH 410-Fix)
- HSTS `preload`; tote Build-Routen (/clown/clown-zauberer/, /zauberer/zaubershow/karneval/) nicht mehr bauen
- `dateModified` sitewide im Schema; ImageGallery-Schema auf /galerie/
- /datenschutzerklaerung-2/: 3 wp-content-Refs + Indexierungs-Frage klären

## 6. NICHT TUN (bewusste Entscheidungen)

- ❌ **Kein aggregateRating/Review-Markup** wieder einführen (unbelegte 400 → Penalty-Risiko; Entfernung auf origin/main war richtig)
- ❌ **Kein Event-Schema** (keine öffentlichen datierten Termine → Manual-Action-Risiko)
- ❌ **Keine sichtbaren Preise auf kinderzauberer-/clown-City-Pages** (harte Preis-Policy des Inhabers: 150 € nur im Kindergeburtstag-Kontext) — stattdessen Schema-offers entfernen
- ❌ **Keine Domain-Aufteilung** auf zauberer-liar.de (Autopilot-Empfehlung steht: eine starke Domain; Entscheidung 301-Weiterleitung liegt bei Michael)
- ❌ Kein weiteres City-Page-Scaling ohne 60 %+ Unique-Content (Doorway-Schwelle erreicht)

## 7. MESSPLAN

| Metrik | Quelle | Kadenz | Ziel (12 Wochen) |
|---|---|---|---|
| Klicks/CTR „zauberer kindergeburtstag" | GSC | wöchentlich (Do-Check läuft) | CTR 1,3 % → 3 %+ |
| Indexierte Seiten | GSC | wöchentlich | 112 → 140+ (alle 120 Sitemap-URLs + Blog) |
| Nicht-indexiert | GSC | wöchentlich | 546 → < 300 |
| Schlüsselereignisse (Anfragen) | GA4 | wöchentlich | messbar ab Woche 1, dann Benchmark |
| AI-Assistant-Sitzungen | GA4 | monatlich | 14 → 50+/28 T |
| CWV (LCP/INP/CLS) | PSI-API | wöchentlich | alle grün |
| Local-Pack-Sichtbarkeit Kern-Keywords | manuell/GBP | monatlich | Top 3 in 20-km-Radius |

---
*Erstellt 2026-07-17 durch Multi-Agent-Audit (7 Spezialisten). Alle Detail-Berichte mit Beweisen (curl-Header, Zeilennummern) liegen in den Agenten-Outputs dieser Session vor. Keine Änderung wurde vorgenommen.*

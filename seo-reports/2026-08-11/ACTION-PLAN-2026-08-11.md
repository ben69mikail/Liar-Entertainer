# Action-Plan SEO — 11.08.2026

Maßnahmen aus dem Audit vom 11.08.2026, priorisiert. Jede Maßnahme nennt Datei, konkrete Änderung und erwartete Wirkung. Alle Vorschläge sind gegen die 45 Regeln in `scripts/seo-assertions.mjs` geprüft — es gibt keinen Konflikt.

**Reihenfolge-Empfehlung:** K1–K4 in einem Deploy, dann H1–H3 im zweiten, H4–H6 im dritten. Nach jedem Deploy `npm run test:seo` (muss 45/45 bleiben) und eine Woche Search Console beobachten.

---

## KRITISCH — diese Woche

### K1 · 16 tote Bilder reparieren

**Datei:** `src/pages/[...slug].astro`, Zeilen 607 und 880
**Änderung:** `if (scrapedContent && page.type === 'post')` → `if (scrapedContent && (page.type === 'post' || page.type === 'page'))`
**Wirkung:** `stripWpImages()` greift endlich auch auf `/clown/clown-zauberer/` (11 Bilder) und `/zauberer/zaubershow/karneval/` (5). Beide Seiten zeigen aktuell Platzhalter für Bilder, die per `.htaccess` bewusst 410 Gone liefern.
**Aufwand:** Minuten. **Risiko:** gering, betrifft nur Seiten mit gescraptem Alt-Inhalt.

### K2 · Kinderzauberer Gladbeck aus der Isolation holen

**Dateien:** 19 × `src/pages/kinderzauberer/kinderzauberer-in-{bochum,bottrop,datteln,dinslaken,dorsten,dortmund,duesseldorf,duisburg,essen,gelsenkirchen,haltern,herne,herten,marl,moers,muelheim,oberhausen,recklinghausen,wesel}/index.astro`
**Änderung:** Im Einsatzgebiet-Absatz Gladbeck als verlinkten Ort ergänzen, Ankertext „Kinderzauberer in Gladbeck" (mit Varianz, siehe H2).
**Zusätzlich:** `src/pages/clown/clownshow/clown-in-gladbeck/index.astro` Zeile ~369 — im Cross-Linking-Modul fehlt der Chip zu `/kinderzauberer/kinderzauberer-in-gladbeck/`. Ergänzen.
**Wirkung:** Deine Heimatstadt-Seite steigt von 5 auf rund 25 interne Links und schließt zur Clown- und Kindergeburtstag-Familie auf.
**Wichtig:** Über zwei bis drei Deploys staffeln, nicht alle 19 auf einmal.

### K3 · /kontakt/ auf das Hauptkeyword einzahlen lassen

**Datei:** `src/pages/kontakt/index.astro`
**Änderung:** Zwei bis drei Sätze Fließtext ergänzen, zum Beispiel:

> Sie möchten einen Kinderzauberer für den Kindergeburtstag in Gladbeck oder Umgebung buchen? Schreiben Sie mir direkt — meist antworte ich noch am selben Tag. Ich komme ohne Anfahrtskosten nach Gladbeck und bin im Umkreis von 20 Kilometern regelmäßig unterwegs, unter anderem in Bottrop, Gelsenkirchen, Essen und Oberhausen.

**Wirkung:** 192 eingehende interne Links treffen aktuell auf eine 326-Wörter-Seite ohne das Wort „Kinderzauberer". Größter Einzelhebel im Datensatz.

### K4 · Duplicate-H2 auf 69 Stadtseiten auflösen

**Dateien:** die drei Stadtseiten-Templates
**Änderung:** „Häufige Fragen zum Kindergeburtstag mit Zauberer" ersetzen durch je familienspezifische Formulierung:

| Familie | neue H2 |
|---|---|
| `/kinderzauberer/kinderzauberer-in-X/` | Häufige Fragen zum Kinderzauberer in [Stadt] |
| `/kindergeburtstag/geburtstag-in-X/` | Häufige Fragen zur Kindergeburtstagsfeier in [Stadt] |
| `/clown/clownshow/clown-in-X/` | Häufige Fragen zum Clown-Auftritt in [Stadt] |

**Wirkung:** Beseitigt das stärkste Duplicate-Signal der Website und gibt jeder Familie eine eigene FAQ-Intention.
**Regelbezug:** M3.1 verbietet nur „SCHNELLE EINDRÜCKE", „NOCH FRAGEN?" und „Die Preise" — kein Konflikt.

---

## HOCH — nächste zwei Wochen

### H1 · Die zwei fehlenden Prioritätsbegriffe einbauen

Nicht als Keyword-Stopfung, sondern dort, wo Menschen sie tatsächlich formulieren: in FAQ-Fragen.

**`/kindergeburtstag/` (116 Links, wichtigster Hub) — neue FAQ-Frage:**

> **Was für einen Zauberer für Kinder soll ich zum Geburtstag buchen?**
> Für einen Geburtstag für Kinder eignet sich ein Zauberer für Kinder besonders gut, wenn die Show auf das Alter der Gäste abgestimmt ist. Bei LIAR heißt das: ab 4 Jahren, 40 Minuten, interaktiv, und das Geburtstagskind steht im Mittelpunkt.

**`/zauberer/` — ein Satz im Abschnitt „Zaubershow für Kinder & Erwachsene":**

> Als Zauberer für Kinder passe ich Tempo, Humor und Requisiten an die Altersgruppe an.

**Alle 23 Kinderzauberer-Stadtseiten — Einstiegssatz im Intro:**

> Sie suchen einen Zauberer für Kinder in [Stadt]?

**`/blog/kindergeburtstag-park-tipps/` — zusätzliche FAQ-Frage:**

> Was braucht ein Geburtstag für Kinder im Freien zusätzlich?

**Wirkung:** Von 16 auf rund 60 Vorkommen für „zauberer für kinder", von 1 auf rund 6 für „geburtstag für kinder" — an genau den Stellen, die für Sprachsuche und Google-Fragen ausgewertet werden.

### H2 · Ankertexte aufwerten

Rund 45 % aller internen Links tragen kein Keyword: 1.099 sind nackte Städtenamen, 380 generische CTAs („Weiterlesen →", „Mehr erfahren", „Kontaktformular").

| Ziel | Ist | Soll |
|---|---|---|
| kinderzauberer-in-gladbeck | „Gladbeck" | Kinderzauberer in Gladbeck |
| clown-in-gladbeck | „Gladbeck" | Clown in Gladbeck buchen |
| geburtstag-in-gladbeck | „Gladbeck" | Kindergeburtstag in Gladbeck |
| kinderzauberer-in-bottrop | „Bottrop" | Kinderzauberer in Bottrop |
| kinderzauberer-in-gelsenkirchen | „Gelsenkirchen" | Kinderzauberer für Gelsenkirchen |
| kinderzauberer-in-dorsten | „Dorsten" | Kinderzauberer in Dorsten |
| kinderzauberer-in-herten | „Herten" | Zauberer für Kinder in Herten |
| kinderzauberer-in-oberhausen | „Oberhausen" | Kinderzauberer in Oberhausen |
| kinderzauberer-in-essen | „Essen" | Kinderzauberer für Essen |
| kinderzauberer-in-marl | „Marl" | Kinderzauberer in Marl |
| /clown/clownshow/ | „Weiterlesen →" | Zurück zur Clownshow-Übersicht |
| /kindergeburtstag/ | „Kontaktformular" | Kindergeburtstag buchen |
| /kinderzauberer/ | „Mehr erfahren" | Kinderzauberer für den Kindergeburtstag |
| /zauberer/zaubershow/ | gemischt | Zaubershow buchen |
| /preise/ | „Jetzt unverbindlich anfragen" | Preise Kinderzauberer & Clown |

Die Spalte „Soll" variiert bewusst zwischen „in", „für" und Zusätzen — gleichlautende Anker auf 20 Seiten wären ein eigenes Problem.

### H3 · Ballon und Glitzer auf dem Haupt-Hub zurückstufen

**Datei:** `src/pages/kindergeburtstag/index.astro`
**Änderung:** H2 „🎈🎈 Ballonmodellage Glitzer-Tattoos – das i-Tüpfelchen zum Geburtstag" zur Unterüberschrift innerhalb des Programm-Abschnitts machen, neu formuliert:

> Zusatzleistungen zur Zaubershow: Ballonmodellage & Glitzer-Tattoos

**Absatz-Öffner ersetzen durch:**

> Optional lässt sich die Zaubershow um Ballonmodellage oder Glitzer-Tattoos ergänzen — der Fokus bleibt die interaktive Kinderzauberer-Show.

**Nicht anfassen:** `/preise/` und `/blog/was-kostet-zauberer-kindergeburtstag/`. Dort sind die Nennungen Preistransparenz und sachlich angemessen. Die beiden dedizierten Seiten `/clown/ballonmodellage/` und `/clown/glitzer-tattoo/` bleiben unverändert bestehen.

### H4 · Bildoptimierung: die schlimmsten Fälle

**Sofort:** `src/pages/kindergeburtstag/geburtstag-in-dortmund/index.astro` Zeile ~156 — `<img src={_introImgAsset.src}>` → `<Image src={_introImgAsset} width={320} height={320} alt="…" loading="lazy" />`. Spart rund 780 KB auf einer einzigen Seite.

**Dann systematisch:** die 56 Bypass-Stellen in 24 Stadtseiten-Templates auf `<Image>` umstellen. Höchster Multiplikator zuerst: `kindergeburtstag-mit-kinderzauberer.jpg` (41 ×), `zaubershow-mit-clown-zauberer-liar.jpg` (24 ×), `clown-bei-clownshow.jpg` (24 ×).

### H5 · areaServed auf den Radius schärfen

**Datei:** `src/layouts/BaseLayout.astro`, Zeilen 124–139

```json
"areaServed": [
  { "@type": "GeoCircle",
    "geoMidpoint": { "@type": "GeoCoordinates", "latitude": 51.5658, "longitude": 6.9857 },
    "geoRadius": "20000" },
  {"@type":"City","name":"Gladbeck"}, {"@type":"City","name":"Bottrop"},
  {"@type":"City","name":"Gelsenkirchen"}, {"@type":"City","name":"Dorsten"},
  {"@type":"City","name":"Herten"}, {"@type":"City","name":"Oberhausen"},
  {"@type":"City","name":"Essen"}, {"@type":"City","name":"Marl"},
  {"@type":"City","name":"Recklinghausen"}, {"@type":"City","name":"Dinslaken"},
  {"@type":"City","name":"Herne"}, {"@type":"City","name":"Mülheim an der Ruhr"},
  {"@type":"City","name":"Bochum"}
]
```

Köln (rund 70 km, keine eigene Seite), Düsseldorf und Dortmund fallen aus dem **globalen** Schema — sie bleiben im Service-Schema ihrer jeweiligen Stadtseite, wo sie hingehören. Dorsten, Herten, Marl und Dinslaken kommen neu dazu.

### H6 · Bildunterschriften einführen

**Dateien:** `src/pages/galerie/index.astro` und die `photoImages`-Blöcke der Stadtseiten-Templates

```html
<figure class="aspect-square overflow-hidden bg-gray-200 rounded-lg card-hover">
  <Image src={img.src} alt={img.alt} … />
  <figcaption class="px-3 py-1.5 text-sm text-[#374151] bg-white border-t border-gray-100">
    {img.caption}
  </figcaption>
</figure>
```

Beispieltexte:

- Kinderzauberer LIAR bei einem Kindergeburtstag in Gladbeck
- Zaubershow für Kinder auf einem Sommerfest in Bottrop
- Clown Zauberer LIAR beim Straßenfest in Gelsenkirchen
- Bühnenshow auf einer Firmenfeier in Essen
- Zaubershow auf dem Weihnachtsmarkt in Dortmund
- Kinderzauberer im Kindergarten in Oberhausen
- Presseartikel: die WAZ über Clown Zauberer LIAR
- Einsatzgebiet: Gladbeck und 20 Kilometer Umkreis

**Nicht** auf Hero-, Logo- und Slider-Bildern — nur Galerie, Foto-Grids und Blog.

---

## MITTEL — nächster Monat

### M1 · Fernstädte entlasten, ohne sie zu löschen

In den Einsatzgebiet-Absätzen der Nahstadt-Seiten (Gladbeck, Bottrop, Gelsenkirchen, Dorsten, Herten, Oberhausen, Essen, Marl) die Städte über 20 km aus dem verlinkten Aufzählungssatz in einen zweiten, unverlinkten Absatz verschieben: „auch überregional buchbar: Dortmund, Duisburg, Düsseldorf …".

Erreichbarkeit bleibt über je einen Link aus dem jeweiligen Hub und die Sitemap. Erwartung: Fernstädte fallen von 20–26 auf 5–8 interne Links, die frei werdenden Slots gehen an Nahstädte. **R4 (23/23/23) bleibt unberührt — keine Seite verschwindet.**

### M2 · H1 der Kindergeburtstag-Familie schärfen

Von generisch „Geburtstag in Bochum" auf transaktional:

> Kindergeburtstag in Bochum feiern – Zaubershow ab 150 €

Das trennt die Suchintention sauber von der Kinderzauberer-Familie (Dienstleisterauswahl) und der Clown-Familie (Format- und Eventsuche). H1 unterliegt nicht dem Title-Längenlimit M6.1/M6.2.

### M3 · Dünne Seiten

| Seite | Wörter | Maßnahme |
|---|---|---|
| `/blog/kategorie/feste/` | 205 | 2–3 Sätze redaktionelle Einleitung mit „Kindergeburtstag" |
| `/blog/kategorie/geburtstag/` | 205 | Einleitung: „Alle Artikel rund um den Kindergeburtstag mit Zauberer und Clown …" |
| `/blog/kategorie/saisonal/` | 205 | Einleitung mit saisonalem Bezug |
| `/blog/kategorie/pantomime-nrw/` | 221 | Nur 1 eingehender Link, thematisch isoliert → verlinken **oder** auf noindex |
| `/kontakt/` | 326 | siehe K3 |

### M4 · Verwaiste Seiten anbinden

`/clown/clown-zauberer/` (940 Wörter) und `/zauberer/zaubershow/karneval/` (898 Wörter) haben null Content-Links und stehen weder im Header-Dropdown noch im Footer. Vor der Verlinkung von `/zauberer/zaubershow/karneval/` klären, ob es sich inhaltlich von `/clown/karneval/` abgrenzt — sonst wäre die Verlinkung Kannibalisierung statt Nutzen.

### M5 · Blog-Bilder aufräumen

12 Bilder in `src/content/blog/*.md` tragen Kameradateinamen als Alt-Text. Beispiel:

`![DSC_0390.JPG](…)` → `![Picknick-Kindergeburtstag im Park mit spielenden Kindern auf der Decke](…)`

Bildinhalte bitte vor dem Ersetzen kurz gegenprüfen — die Vorschläge stammen aus dem Blogkontext, nicht aus Bildanalyse. Gleichzeitig `width` und `height` ergänzen (CLS).

### M6 · llms.txt an die neue Gewichtung anpassen

```
## Einsatzgebiet
Kerngebiet (bis 20 km um Gladbeck, Schwerpunkt Kindergeburtstage):
Gladbeck, Bottrop, Gelsenkirchen, Dorsten, Herten, Oberhausen, Essen,
Marl, Recklinghausen, Dinslaken, Herne, Mülheim an der Ruhr, Bochum
Erweitertes Gebiet (20-40 km): Duisburg, Castrop-Rauxel, Haltern,
Datteln, Wesel, Moers, Waltrop, Dortmund, Düsseldorf
```

Ballonmodellage und Glitzer-Tattoos unter „Leistungen" als „zubuchbare Zusatzleistung zur Zaubershow" formulieren statt als eigene Top-Level-Punkte.

---

## NIEDRIG — Backlog

- **N1 · Fonts auslagern.** `src/styles/fonts.css` (42,6 KB Base64-inline) als physische `.woff2` unter `public/fonts/` plus `<link rel="preload">`. 58 % des Homepage-HTML sind aktuell `<style>`-Blöcke. Die DSGVO-Entscheidung gegen das Google-Fonts-CDN bleibt erfüllt.
- **N2 · NAP vereinheitlichen.** Drei Schreibweisen im Umlauf: `0172-1517578` (Footer), `0172 – 1517578` (Stadtseiten), `+49 (0) 172 15 17 578` (Impressum). Einheitlich auf `+49 172 1517578` wie im Schema.
- **N3 · Bilddateinamen.** Nur in `src/assets/images/**` gefahrlos umbenennbar (Astro hasht neu). Beispiel: `zauberer/zaubershow-staunende-kinder.jpg` → `kinderzauberer-zaubershow-staunende-kinder.jpg`. Dateien unter `public/` nur umbenennen, wenn zeitgleich `src/utils/allPosts.ts`, `src/pages/[...slug].astro` und alle Blog-Frontmatter mitgepflegt werden — sonst brechen die Bilder live.
- **N4 · Blog-Kategorien.** Sechs Kategorieseiten haben je nur einen eingehenden Link; Kategorie-Chips aus den Artikeln ergänzen.
- **N5 · E-E-A-T.** `/ueber-mich/` erfüllt die Vita-Regel, nennt aber „Kinderzauberer" null Mal. Einen Satz zur Spezialisierung ergänzen.
- **N6 · Inventarskript korrigieren.** `scripts/seo-inventory.mjs` zählt `<img>` in Inline-JS mit; `<script>`-Blöcke vor dem Regex entfernen, damit künftige Läufe keine 35 Phantom-Bilder melden.

---

## Neue Inhalte (Vorschläge)

| Titel | Ziel-Keyword | Intention | Ort |
|---|---|---|---|
| Kinderzauberer buchen: Worauf Eltern in Gladbeck achten sollten | kinderzauberer | Ratgeber | `/blog/` |
| Geburtstag für Kinder feiern: Programm-Ideen mit Zauberer | geburtstag für kinder | informational | `/blog/kategorie/geburtstag/` |
| Radius-Block „Zauberer für Kinder in der Nachbarschaft" mit Entfernungstabelle | lokal + Longtail | lokal | Abschnitt auf `/kindergeburtstag/` |

---

## Prüfung nach jedem Deploy

```bash
npm run build && npm run test:seo   # muss 45/45 bleiben
```

Danach in der Search Console beobachten: Impressionen für „kinderzauberer gladbeck", „zauberer kindergeburtstag [Nahstadt]" und die zwei neuen Longtails. Erste belastbare Bewegung frühestens nach zwei bis vier Wochen.

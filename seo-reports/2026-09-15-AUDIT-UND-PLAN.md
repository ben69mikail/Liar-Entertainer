# SEO-Audit liar-entertainer.com — 15.09.2026

**Gemessen:** Live-Crawl aller 142 Sitemap-URLs + Repo-Build `53253b5` (14.09.) + `npm run test:seo` / `test:struktur`.
**Nicht gemessen:** GSC-Daten (kein Zugriff aus dieser Session), PageSpeed-API (Tagesquota erschöpft). Beides unten als offene Prüfung markiert.

## 1. Technischer Befund — grün

| Prüfung | Ergebnis |
|---|---|
| Status-Codes Sitemap-URLs | 142/142 → 200, keine Ketten |
| www / http → https non-www | 301, einstufig |
| Legacy-WP (/category/, /tag/, /feed/, /index.php) | 301 auf Hub/Blog; /attachment/, /wp-content/uploads/ → 410 |
| Canonical, noindex, Meta-Description, og:image | 142/142 korrekt, keine Abweichung, kein Duplikat |
| H1 | genau 1 pro Seite (142/142) |
| Bilder | 1.056 gesamt, **0 ohne alt**; 154 ohne width/height, 348 noch jpg/png (Rest webp) |
| JSON-LD | 0 Syntaxfehler; LocalBusiness `#business` mit GeoCircle 20 km, sameAs, Öffnungszeiten; FAQPage 86, Service 83, BreadcrumbList 86, BlogPosting 39, VideoObject 11, Person 1 |
| robots.txt / llms.txt / llms-full.txt | vorhanden, KI-Crawler explizit erlaubt, /api/ blockiert |
| Thin Content | 0 Seiten < 300 Wörter |
| test:seo | 45/45 · test:struktur 10/10 |
| Server | gzip, Cache 1 h, TTFB Ø 0,33 s |
| Regel PR.2 / K1.2 / R4 | eingehalten (Preis nur /preise/ + /kindergeburtstag/*, kein aggregateRating, 23/23/23 Stadtseiten) |

Fazit: Die Hygiene-Themen der Audits vom 06.08. und 11./12.08. sind umgesetzt und halten. Weitere Title-/Alt-/Schema-Mikroarbeit hat keinen messbaren Hebel mehr (siehe `feedback_seo_focus`).

## 2. Was den Hebel jetzt bestimmt (nach erwarteter Wirkung)

### H1 · Blog steht seit 17.07.2026 still — 2 Monate ohne Artikel
9 Artikel im Repo, letzter Publish 17.07. Der Sommer-Traffic (Hitze/Sommerfest, im Juli −3.055 Impr.) ist saisonal weg, Herbst-Themen fehlen komplett. Das ist der einzige Bereich, in dem die Site *wachsen* statt nur *halten* kann — und der einzige, den KI-Suchen regelmäßig neu zitieren.
**Maßnahme:** 1 Artikel/Woche bis Jahresende (Redaktionsplan in `BLOG-REDAKTIONSPLAN-Q4-2026.md`). Betreiber gibt Thema + Entwurf frei, Task veröffentlicht.
Erwartung: +800–1.500 Impr./Monat je Saison-Artikel (Referenz: Hitze-Artikel 5.595 Impr./28 T in der Spitze).

### H2 · Deploy-Pipeline hat keinen Regressionsschutz
`.github/workflows/deploy.yml` führt nur `npm run build` aus. `test:seo` (45 Zusicherungen) und `test:struktur` (Hero-Invarianten) laufen **nicht** in CI. Ein fehlerhafter Commit (Beispiel 06.08.: Build fiel still von 168 auf 133 Seiten) geht direkt live.
**Maßnahme:** beide Tests als Gate vor dem SFTP-Upload — Patch `deploy.yml.patch`. Ohne diesen Gate hat jeder Tages-Task ein Restrisiko, das er nicht selbst kontrolliert.

### H3 · GSC-Punkte aus dem 06.08.-Audit sind weiter offen (nicht verifizierbar ohne GSC)
1. **K1b CTR-Diagnose** — ~5.400 Impr. auf Pos 1–5 mit ~8 Klicks (`zauberer bottrop`, `bühnenzauberer`, `zauberer`, `zauberer sommerfest`). Größter offener Hebel; entscheidet, ob Title-Arbeit oder GBP der Weg ist.
2. **K3** — /kinderzauberer/kinderzauberer-in-haltern/, -recklinghausen/, -dorsten/ zur Indexierung einreichen (interne Verlinkung ist seit 06.08. repariert).
3. **9× Umleitungsfehler** im GSC-Report prüfen.
4. www-Variante hatte 30.07. noch ~5,7 k Impr. — Konsolidierung nachsehen.
5. Kategorien `kindergeburtstag`, `geburtstag`, `ratgeber`, `karneval`: Einleitungstext + von noindex zurück auf index (redaktionell, Betreiber).

### M1 · Ein echter Orphan
`/clown/clownshow/clown-in-moers/` hat **0 interne Links** (nur Sitemap). Castrop-Rauxel, Wesel, Waltrop je 1. Fernstädte wurden 11.08. bewusst entlastet, aber 0 Links heißt Deindexierungsrisiko. Vorschlag: je 1 Link aus der Fernstadt-Liste „Auch buchbar in" der Clownshow-Hub-Seite (reine Linkergänzung, kein Text).

### M2 · Rezensions-API tot
`/api/reviews.php` → `pool_size: 0`, `last_updated 1970`. Seit SSR aus `testimonials.json` unkritisch, aber Endpunkt liefert nichts — entweder reparieren oder entfernen.

### Notiert, bewusst nicht priorisiert
- 123 KB Inline-CSS auf jeder Seite (Astro `inlineStylesheets`). GSC-CWV war 06.08. 74/0/0 → kein Handlungsdruck; PSI-Quota heute erschöpft, Nachmessung im Task.
- 3× `fetchpriority="high"` auf der Startseite (Logo + 2 Hero-Bilder) — schwächt die LCP-Priorisierung minimal.
- Sitemap-`lastmod`: 35 URLs mit Build-Datum 17.07., 59 mit 2023-Werten aus dem WP-Import. Kein Ranking-Faktor, nur Vertrauenssignal.
- 11 Kategorie-URLs verlinkt, nicht in Sitemap — korrekt (noindex per M7).

## 3. KI-Suche (GEO)
Vorhanden: llms.txt/llms-full.txt, `#business`/`#person`-Graph, FAQPage auf 86 Seiten, KI-Crawler in robots.txt erlaubt, sichtbare Rezensions-Texte im HTML. Fehlend (unverändert seit 06.08., nur Betreiber): Wikidata-Item, Profile auf eventpeppers/gigmit, konsistente NAP auf Drittseiten. Die Blog-Frequenz (H1) ist der einzige GEO-Hebel, der aus der Site selbst kommt.

## 4. Täglicher Task
Prompt in `TASK-liar-daily-seo-check.md`. Kern: Regelwerke (45+10) gegen Live-Build → Deploy-Status → Erreichbarkeit/Redirects → GSC-Delta (7 T vs. 7 T) → Blog-Fälligkeit → 3-Zeilen-Bericht. Eigenständige Änderungen nur innerhalb der harten Grenzen; alles andere als Vorschlag.

---

## 5. GSC-Befund (live geprüft 15.09.2026, Property sc-domain:liar-entertainer.com)

### Leistung 28 T (15.08.–12.09.) vs. vorherige 28 T
| | aktuell | vorher | Δ |
|---|---|---|---|
| Klicks | 509 | 492 | +3 % |
| Impressionen | 29.574 | 25.560 | +16 % |
| CTR | 1,7 % | 1,9 % | −0,2 pp |
| Position | 11 | 11 | 0 |

Impressionen wachsen, Klicks nicht → **CTR ist das Problem, nicht Sichtbarkeit.** Ziel aus dem 06.08.-Audit (CTR 3,5–4 %) ist weit entfernt.
Indexierung: **122 indexiert** (Baseline 121), 306 nicht indexiert (vorher 409 — Legacy-Bereinigung wirkt). CWV mobil: 73 gut / 0 / 0.

### K1b CTR-Diagnose — Ergebnis
**Hauptbefund: `https://www.liar-entertainer.com/` erhält 7.209 Impr. / 71 Klicks / Pos 6,0 — die non-www-Startseite 8.029 / 88 / Pos 12,2.** Die www-URL ist laut URL-Prüfung „nicht indexiert – Seite mit Weiterleitung" (301 korrekt, letztes Crawl 11.09.). Dass sie trotzdem Impressionen auf Pos 1–6 sammelt, spricht dafür, dass die URL aus dem **Google Business Profile** (Website-Feld) stammt — Local-Pack-Einblendungen werden der dort hinterlegten URL zugerechnet. Beispiel `zauberer` (343 Impr., Pos 5,6, 0 Klicks): rankt ausschließlich auf der www-URL.
→ **Prüfen: Website-Feld im GBP auf `https://liar-entertainer.com/` umstellen** (nur Betreiber). Erwartung: Konsolidierung der Startseiten-Signale; die 0-Klick-Queries auf Pos 1–6 sind dann als Local-Pack-Impressionen erklärbar — CTR-Hebel liegt im GBP (Fotos, Kategorie „Zauberer", Beiträge), nicht in Website-Titles.

Weitere Query-Fakten (28 T):
- `clown` 2.223 Impr. / 1 Klick / Pos 9,7 — rankt mit der **Startseite** (1.426) und `/blog/was-ist-ein-clown/` (697), **nicht** mit `/clown/clownshow/`. Informations-Intent, geringer Buchungswert; kein Title-Eingriff.
- `zauberer kindergeburtstag` 447 Impr. / 7 Klicks / Pos 12,7 (vorher 13,8) und `zauberer für kindergeburtstag` 231 / 5 / **Pos 9,4 (vorher 14,0)** — das Geld-Keyword bewegt sich Richtung Seite 1. Weiter stützen (interne Links + Blog).
- `zauberer weihnachtsfeier` 198 Impr. / Pos 41,8 und `zauberer für weihnachtsfeier` 51 / Pos 48,8 — Nachfrage da, keine passende Seite → **bestätigt Blog-Thema KW 40.**
- `zauberer in der nähe` 262 / Pos 17,2, `zauberer buchen` 204 / Pos 14,2, `zauberer mieten` 329 / Pos 11,6 — generische Buchungs-Queries auf Seite 2; Kandidaten für internen Link-Push auf `/zauberer/`.
- `zauberer bottrop` / `zauberer gladbeck` Pos 1,2–1,5, je ~80 Impr., je 1 Klick — Local-Pack-Muster wie oben.
- `zauberer nrw` 191 Impr. / Pos 10,3 / 0 Klicks — **`zauberer-liar.de` ist eine eigenständige Seite mit eigenem Canonical und gleichem Title-Thema** („Zauberer NRW & Gladbeck"). Zwei eigene Domains auf demselben Keyword. Empfehlung Betreiber: entweder zauberer-liar.de per 301 auf `/zauberer/` leiten oder sie bewusst als Zweitmarke mit anderem Fokus halten — nicht beides halb.

### K3 — erledigt
`/kinderzauberer/kinderzauberer-in-recklinghausen/` ist laut URL-Prüfung **indexiert**; der Eintrag „gecrawlt – zurzeit nicht indexiert" (07.05.) ist veraltet. Von den 45 Einträgen dort ist keine weitere echte Seite betroffen (Rest: attachment, tag, category, www-Legacy, `/api/reviews.php`).

### Umleitungsfehler (9) — Validierung „Bestanden"
Erledigt, kein Handlungsbedarf.

### 404 (107) — 2 echte offene Treffer, Rest bereits 301/410 (GSC-Report hinkt)
1. `/zauberer-nrw/` → **404 live.** Laut Deploy-Notiz war das die Ziel-URL der Zweitdomain; existiert nicht. Vorschlag `.htaccess`: `RewriteRule ^zauberer-nrw/?$ /zauberer/ [R=301,L]`; ebenso `/zauberer/zauberer-nrw/` von 410 auf 301 → `/zauberer/` (dort hängen www- und clown-Varianten dran, zuletzt gecrawlt 17.08./28.07.).
2. `/5-gruende-warum-zauberei-zum-karneval-gehoert-🎭✨/` → 404; Ziel existiert: `/blog/5-gruende-warum-zauberei-zum-karneval-gehoert/`. Prozent-kodierte Emoji-Slug per RewriteRule abfangen.
3. `/blog/was-kostet-ein-/` (abgeschnittener Fremdlink) → 404; optional 301 auf `/blog/was-kostet-ein-clown-fuer-ein-kindergeburtstag/`.
Diese drei kann der Tages-Task selbst committen (Regel „.htaccess-Fehler"). Ich konnte aus dieser Session nicht pushen (kein Repo-Zugriff), daher als Vorschlag.

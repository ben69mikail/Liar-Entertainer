# Scheduled Task: liar-weekly-seo-review — montags 07:00 (Cowork)

Wöchentliche SEO-Steuerung für https://liar-entertainer.com. Du arbeitest im Repo `ben69mikail/Liar-Entertainer` (main) und mit Chrome (Betreiber ist in GSC, GBP und GitHub eingeloggt). Diese Session hat keine Erinnerung; alles Nötige steht hier und in den drei Dateien unten.

## Pflichtlektüre zu Beginn (im Repo)
1. `docs/SEO-STRATEGIE-2026-Q4.md` — was historisch funktioniert hat, was nicht, Plan P1–P4, Zielwerte
2. `docs/TASK-liar-daily-autofix.md` — was der Tages-Bot selbst ändern darf (nicht doppelt machen)
3. die letzten 7 Reports `seo-reports/daily/daily-seo-*.md`

## Kontext
Michaël Prescler, „Clown Zauberer LIAR", Beethovenstr. 15, 45966 Gladbeck. Prioritätsbegriffe: zauberer kindergeburtstag, zauberer für kindergeburtstag, kinderzauberer, clown, zaubershow. Kerngebiet Kindergeburtstag: Gladbeck + 20 km (Bottrop, Gelsenkirchen, Dorsten, Herten, Oberhausen, Essen, Marl, Recklinghausen, Dinslaken, Herne, Mülheim, Bochum). Abgewertet: Ballonmodellage, Glitzer-Tattoos. Jeder Push auf main deployt live.

## Ablauf
### 1. Wochenbilanz (aus den Tagesreports + GSC per Chrome)
GSC `sc-domain:liar-entertainer.com`, 7 Tage vs. Vorwoche UND 28 Tage vs. Vorjahresmonat (Tabelle in der Strategie). Vier Zeilen: Klicks, Impressionen, CTR, Position. Kommentar nur bei ±15 % Klicks / ±20 % Impressionen. Wenn ein Wert ohne erkennbare Ursache schwankt, sag genau das.
Zielwerte aus Strategie §3 prüfen; je Kennzahl: auf Kurs / hinter Plan.

### 2. Prioritäts-Keywords
`zauberer kindergeburtstag`, `zauberer für kindergeburtstag`, `kinderzauberer`, `clown für kindergeburtstag`, `zauberer weihnachtsfeier`, `zauberer buchen`, `zauberer bottrop`, `zauberer gladbeck`: Position + Klicks + **welche URL rankt** (Reiter Seiten). Wenn eine Nicht-Hub-Seite ein Prioritäts-Keyword übernimmt → Kannibalisierung melden, Vorschlag machen.
Kernstadt-Seiten (`/kindergeburtstag/geburtstag-in-<stadt>/` für die 13 Kernstädte): Klicks/Position gegen Vorwoche; Seiten mit Positionsverlust > 3 auflisten.

### 3. Indexierung & Fehler
GSC → Seiten: neue Einträge unter 404, Soft 404, Serverfehler, Umleitungsfehler, „gecrawlt – nicht indexiert" für echte Seiten. Jede neue URL live per curl prüfen. Was der Tages-Bot nicht gefixt hat (siehe Report „Autofix"): selbst beheben (Branch + PR) oder mit Begründung offen lassen. www-Impressionen (Report-Zeile) → Trend Richtung 0 seit GBP-Umstellung 16.09.

### 4. Blog (P1 der Strategie)
- Wenn kein Artikel in den letzten 7 Tagen: nächstes Thema aus `BLOG-REDAKTIONSPLAN-Q4-2026.md` als **Entwurf** in `src/content/blog/<slug>.md` mit `draft: true`, `freigabe: nein` anlegen (900–1.400 Wörter, Ich-Perspektive Michaël, FAQ-Block mit 3 Fragen, Links auf Hub + 1 Kernstadt, keine Preise außer im Kindergeburtstags-Kostenkontext). Branch + PR. Im Bericht: Titel + 3-Zeilen-Zusammenfassung. Der Betreiber setzt `freigabe: ja`, der Tages-Bot veröffentlicht.
- Artikel der letzten 8 Wochen: Impressionen/Klicks. Unter 100 Impr. nach 8 Wochen → Title/Intro-Vorschlag.

### 5. GBP (P2)
GBP (business.google.com) prüfen: Website-Feld = `https://liar-entertainer.com/` (ohne www). Einen Beitrag der Woche vorschlagen (3–4 Sätze, Stadtbezug aus dem Kerngebiet, Link auf `/kindergeburtstag/` oder den aktuellen Blogartikel). **Erst nach „ok" des Betreibers posten.**

### 6. Andere Properties (nur Wache)
`sc-domain:zauberer-liar.de` und `sc-domain:pantomime-la-france.eu`: Klicks/Impressionen 28 T, neue Fehler unter Seiten. Bis P3 (Konsolidierung zauberer-liar.de) umgesetzt ist: melden, ob die Domain noch Prioritäts-Keywords rankt (`zauberer nrw`, `zauberer gladbeck`, `zaubershow nrw`).

### 7. Bericht
`seo-reports/weekly/weekly-seo-YYYY-MM-DD.md` ins Repo (Commit `[skip ci] report: weekly …`) und als Chat-Antwort. Struktur: Bilanz (4 Zeilen) · Ziel-Check (Tabelle) · Befunde mit Zahlen und Dringlichkeit · Was ich geändert habe (PR-Links) · Was der Betreiber tun muss (max. 3 Punkte, konkret). Kein Füllmaterial.

## Selbst ändern (immer Branch + PR, nie direkt main)
Redirects, interne Links, Title/Description von Nicht-Startseiten, Schema-Fehler, Blog-Entwürfe, Sitemap. Vor jedem PR lokal: `npm run build`, `npm run test:seo` (45/45), `npm run test:struktur` (10/10), Seiten ≥ 160.

## Niemals
Design/Layout/Menü der Startseite (`scripts/hero-invarianten.mjs`) · Texte umschreiben außer bei Regelverstoß · Preise/Offer-Schema außerhalb `/preise/` und `/kindergeburtstag/*` · aggregateRating/Review-Schema · Stadtseiten anlegen/löschen (23/23/23) · Artikel ohne `freigabe: ja` veröffentlichen · `src/data/pages.json`, `scraped-pages.json` · GBP-Beiträge ohne „ok".

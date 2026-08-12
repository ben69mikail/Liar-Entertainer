# SEO-Audit Runde 2 — 12.08.2026

**Gemessener Stand:** `d595c3f` (live), 168 Seiten, 144 indexierbar.
**Fokus:** Kindergeburtstage · 13 Städte im 20-km-Umkreis Gladbeck · bessere Platzierung bei Google **und** KI-Suche für Eltern, die einen Clown oder Kinderzauberer suchen.
**Neu gegenüber Runde 1:** Menüstruktur, KI-Auffindbarkeit, Verzahnung Leistung × Stadt.

---

## Was Runde 1 gebracht hat

| | 11.08. vorher | heute |
|---|---|---|
| Kaputte Bilder (410) | 16 | **0** |
| Doppelte FAQ-Überschrift | 68 Seiten | **0** |
| Bildunterschriften | 0 | **97** |
| „kinderzauberer" gesamt | 430 | **477** |
| „zauberer für kinder" | 16 | **38** |
| Links auf Kinderzauberer Gladbeck | 5 | **18** |
| Links auf Dortmund (34 km) | 23 | **5** |
| Rohe jpg/png | 388 | **277** |
| Bilder ohne alt | 0 | **0** |

**Das Silo-Dreieck funktioniert jetzt.** Für jede geprüfte Stadt verlinken sich die drei Leistungsseiten gegenseitig — Kinderzauberer ↔ Kindergeburtstag ↔ Clown. Das war vorher lückenhaft.

---

## Die fünf wichtigsten offenen Punkte

### 1. Im Menü kommt keine einzige Stadt vor

Alle 69 Stadtseiten sind ausschließlich über Fließtext erreichbar. Eine Mutter, die über „Kinderzauberer Bottrop" auf einer Unterseite landet, hat keinen Weg zu ihrer Nachbarstadt und keinen sichtbaren Rückweg — die Breadcrumbs existieren nur als unsichtbares JSON-LD für Google, nicht als anfassbarer Pfad im Layout.

### 2. Sieben gleichrangige Menüpunkte konkurrieren um dieselbe Frage

Clown, Zauberer, Kinderzauberer, Kindergeburtstag, Zaubershow stehen nebeneinander. Fachlich sind das getrennte Leistungen. Für eine Mutter unter Zeitdruck ist es **eine** Frage — „Clown oder Zauberer für den Geburtstag?" — und das Menü beantwortet sie nicht, sondern vervielfacht sie. Zusätzlich stehen Ballonmodellage und Glitzer-Tattoos als eigene Dropdown-Einträge gleichrangig neben der Clownshow, obwohl sie ausdrücklich abgewertet werden sollen.

### 3. Ausgerechnet die Kinderzauberer-Seiten haben fast keine Bildunterschriften

| Familie | Seiten | Bildunterschriften |
|---|---|---|
| `/kindergeburtstag/geburtstag-in-*` | 23 | 30 |
| `/clown/clownshow/clown-in-*` | 23 | 27 |
| **`/kinderzauberer/kinderzauberer-in-*`** | **23** | **3** |

22 von 23 Kinderzauberer-Stadtseiten haben null Bildunterschriften — bei zusammen 114 Bildern, der bildreichsten Stadtseiten-Familie überhaupt. Auch Startseite, Kinderzauberer-Hub, alle `/zauberer/*`-Seiten, `/preise/`, `/ueber-mich/` und sämtliche Blogartikel haben keine.

### 4. Die Startseite hat zwei Person-Knoten

`BaseLayout.astro` definiert Michaël Prescler als `founder` mit `@id: #person`, samt `sameAs`, Führungszeugnis und Beruf. `index.astro` definiert **zusätzlich** einen zweiten Person-Knoten — ohne `@id`, mit abweichendem `knowsAbout`, ohne `sameAs`, und mit einem eigenen anonymen Arbeitgeber-Knoten statt einer Referenz auf `#business`.

Im gebauten HTML nachgezählt: **2 Person-Knoten, davon 1 mit `@id`.** Eine Maschine sieht zwei verschiedene Personen. Genau das untergräbt die Verknüpfung „Michaël Prescler = LIAR = Kinderzauberer in Gladbeck", auf die KI-Systeme angewiesen sind.

Dasselbe Muster eine Ebene tiefer: Die Service-Schemas der Stadtseiten definieren `provider` jeweils als neuen anonymen `LocalBusiness` statt auf `#business` zu verweisen. Gezählt: **253 LocalBusiness-Knoten** über alle Seiten — rund 85 mehr als die 168 globalen. Das sind 85 lose Fragmente statt eines Graphen.

### 5. Die Kinderzauberer-Familie bleibt die schwächst verlinkte

| Stadt | km | Kinderzauberer | Kindergeburtstag | Clown |
|---|---|---|---|---|
| Mülheim | 17,0 | **10** | 21 | 21 |
| Dinslaken | 16,8 | **11** | 22 | 19 |
| Dorsten | 10,6 | **12** | 20 | 19 |
| Herten | 10,9 | **12** | 18 | 22 |
| Marl | 12,6 | **13** | 20 | 21 |
| Herne | 16,9 | **13** | 21 | 21 |
| Gladbeck | 0,6 | 18 | 24 | 32 |
| Essen | 12,4 | 24 | 24 | 26 |

Runde 1 hat die Fernstädte entlastet, aber die frei gewordene Linkkraft nicht aktiv umgeleitet.

---

## Maßnahmenplan

### KRITISCH

**A1 · Doppelten Person-Knoten auflösen**
`src/pages/index.astro` — den zweiten `personSchema` entfernen oder auf `"@id": "https://liar-entertainer.com/#person"` umstellen, sodass er auf den bestehenden Knoten verweist statt einen neuen zu erzeugen. Ein Eingriff, direkte Wirkung auf die Eindeutigkeit für KI-Systeme.

**A2 · Provider-Knoten konsolidieren**
In allen Service-Schemas `provider: { '@type': 'LocalBusiness', name: …, url: …, telephone: … }` ersetzen durch `provider: { '@id': 'https://liar-entertainer.com/#business' }`. Aus 85 Fragmenten wird ein Graph. Betrifft die Stadt- und Leistungsseiten, mechanisch per Skript machbar.

### HOCH

**B1 · Menü neu ordnen**

| Position | Soll | Warum |
|---|---|---|
| 1 | **Kindergeburtstag** | Die Seite mit Preistabelle, FAQ und Anfrage gehört nach vorn, nicht als eines von sieben |
| 2 | Clown ▾ (Clownshow, Walk Act) | Ballon/Glitzer raus aus der ersten Ebene, ans Dropdown-Ende mit Label „Zusatzleistung" |
| 3 | Zauberer ▾ (**Kinderzauberer**, Bühnen-, Tisch-Zauberer) | Für Laien ist Kinderzauberer keine eigene Kategorie, sondern die Kinder-Variante |
| 4 | Preise | bleibt — Preistransparenz ist ein Vertrauenssignal |
| 5 | **Für Kita, Schule & Events** ▾ | trennt die zweite Zielgruppe sichtbar von den Eltern (bisher „Zaubershow") |
| 6–8 | Galerie · Blog · Kontakt | unverändert; Pantomime als externer Link ans Ende |

Vier klare Kategorien für Eltern statt sieben konkurrierender Begriffe.

**B2 · Städte sichtbar machen — ohne das Menü zu überladen**

Kein Städte-Dropdown. Bei 13 Nah- plus 10 Fernstädten würde jede gleichrangige Liste entweder das Menü sprengen oder die Fernstädte aufwerten. Stattdessen zwei Eingriffe:

- **„In Ihrer Nähe (bis 20 km)"** auf den drei Hub-Seiten: die bestehende Fließtext-Städteliste in zwei Blöcke umsortieren — die 13 Nahstädte prominent zuerst, die Fernstädte darunter reduziert unter „Auch buchbar in". Reine Umsortierung vorhandener Links, keine neue Seite, keine gelöschte Seite.
- **Footer-Block sitewide** mit gezielten Ankertexten für die sechs schwächsten Kinderzauberer-Stadtseiten: „Kinderzauberer in Mülheim", „… in Dinslaken", „… in Dorsten", „… in Herten", „… in Marl", „… in Herne". Genau die Lücke aus Punkt 5.

**B3 · Sichtbare Breadcrumbs**
Der `BreadcrumbList` existiert bereits als JSON-LD auf 86 Seiten. Ihn zusätzlich als sichtbaren Pfad rendern — „Kinderzauberer › Bottrop". Für Eltern ein Rückweg, für Google eine Bestätigung des vorhandenen Signals.

**B4 · Bildunterschriften auf den 22 Kinderzauberer-Stadtseiten**
Nach dem Muster, das bei Kindergeburtstag und Clown schon steht. Ort plus Anlass plus Szene, zum Beispiel: „Kinderzauberer LIAR beim Kindergeburtstag in Essen — Nahmagie am Tisch mit den Gästekindern". Pro Seite unterschiedlich, kein Bezug zu Ballon oder Glitzer.

### MITTEL

**C1 · Fünf fehlende FAQ-Fragen, die Eltern wirklich stellen**

> **Wie läuft die Zaubershow beim Kindergeburtstag konkret ab?**
> Ich komme pünktlich an, baue in wenigen Minuten auf und starte die 40-minütige Mitmach-Show: Begrüßung, interaktive Zaubertricks mit den Kindern als Assistenten, das Geburtstagskind im Mittelpunkt, ein großes Finale. Sie müssen nichts moderieren — ich übernehme die komplette Unterhaltung.

> **Was passiert, wenn ein Kind nicht mitmachen möchte?**
> Kein Problem und keine Seltenheit. LIAR tritt bewusst ohne Schminke und rote Nase auf und drängt niemanden. Schüchterne Kinder dürfen zuschauen und tauen meist von selbst auf.

> **Ist die Show auch für ein 3-jähriges Kind geeignet?**
> Die Show ist ab 4 Jahren konzipiert. Bei jüngeren Geburtstagskindern lohnt sich ein kurzes Gespräch vorab — oft funktioniert sie trotzdem gut, wenn ältere Geschwister mitfeiern.

> **Muss ich eine Anzahlung leisten?**
> Nein. Bezahlt wird bar oder per Überweisung am Tag der Veranstaltung. Die Buchung wird per E-Mail oder WhatsApp bestätigt.

> **Was kostet die Anfahrt nach [Stadt]?**
> [Stadt] liegt rund [X] km von Gladbeck entfernt — bei 0,40 €/km für Hin- und Rückfahrt liegen die Fahrtkosten bei etwa [Y] €.

Die letzte Frage gehört auf alle 13 Nahstadt-Seiten. **Die Kilometerangaben müssen vorher mit einem Kartendienst geprüft werden** — die Zahlen in diesem Bericht sind Luftlinie, nicht Fahrstrecke.

**C2 · Ortsbezogene Referenzen**
Die sechs Testimonials sind auf allen Seiten identisch und nennen keine einzige Stadt. Im Blog liegen dagegen dokumentierte Einsätze mit Ortsbezug — Wittringer Ritter Gladbeck, Kultur-Kinderfest Resse Gelsenkirchen, IKEA Duisburg. Diese Artikel von den passenden Stadtseiten verlinken. Keine erfundenen Zitate.

**C3 · ImageObject-Schema**
Existiert bisher nirgends. Für die Seiten mit Service-Schema das Hauptbild als `ImageObject` mit `url`, `width`, `height` und `caption` ergänzen — das Signal, mit dem Google Bildersuche und KI-Systeme Bild, Ort und Leistung verknüpfen.

### NIEDRIG

**D1 · Totes Skript entfernen.** In `src/pages/[...slug].astro` liegt ein Client-Skript, dessen Bedingung auf allen 35 betroffenen Seiten nie zutrifft. Es lädt ungenutzt mit.

**D2 · Footer-Logo.** `src/components/Footer.astro` bindet das Logo als rohes `<img>` statt über `<Image>` ein — auf allen 168 Seiten unoptimiert.

**D3 · Sechs zu kurze Alt-Texte**, alle vom Muster „KIDZIVAL 2024". Der ausführlichere Titel existiert bereits an anderer Stelle im Code.

**D4 · Fallback-Bilder.** 182 der 277 rohen jpg/png sind 14 generische Kategoriebilder unter `public/images/fallback/`. Astro optimiert `public/` grundsätzlich nicht — eine Konvertierung nach WebP wäre der größte Einzelhebel bei dieser Zahl.

---

## Korrektur zu einem Befund

Eine Teilanalyse meldete, die Kinderzauberer-Seiten von Herten und Dinslaken hätten bereits eine Preis-FAQ, Bottrop und Essen nicht. **Das ließ sich nicht bestätigen** — bei der Nachprüfung im gebauten HTML haben Bottrop, Essen und Herten übereinstimmend keine. Der behauptete Unterschied existiert nicht; Maßnahme C1 gilt gleichmäßig für alle 13 Nahstädte.

---

## Was NICHT geändert werden sollte

- **Das Design der Startseite.** Ausdrückliche Entscheidung vom 12.08. Zusätzlich durch `scripts/hero-invarianten.mjs` abgesichert.
- **Keine Stadtseite löschen.** Regel R4 fixiert 23/23/23.
- **Kein Offer- oder Preis-Schema außerhalb** `/preise/` und `/kindergeburtstag/*` (Regel PR.2). Preisangaben in FAQ-Antworten als Klartext sind zulässig, als Schema nicht.
- **Kein aggregateRating- oder Review-Schema** (Regel K1.2). Ortsbezogene Referenzen nur als sichtbarer Text.
- **Ballon- und Glitzer-Seiten bleiben.** Es geht um Gewichtung im Menü und in Überschriften, nicht um Löschung.
- **Keine Kilometerangaben ohne Prüfung veröffentlichen.** Die Werte hier sind Luftlinie.

---

*Datengrundlage: `seo-reports/2026-08-11/pages.json`, frisch gebautes `dist/` vom Stand `d595c3f`. Regelwerke: `scripts/seo-assertions.mjs` (45 Regeln) und `scripts/hero-invarianten.mjs` (10 Invarianten), beide aktuell vollständig erfüllt.*

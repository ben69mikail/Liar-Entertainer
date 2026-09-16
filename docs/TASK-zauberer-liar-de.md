# zauberer-liar.de — Plan + Task-Vorlage

## Befund (GSC, 16 Monate bis 16.09.2026)
51 Klicks, 14.600 Impressionen, CTR 0,3 %, Position 20,8. Rankt für `zauberer gladbeck` (788 Impr., Pos 9,7), `zauberer nrw` (680, Pos 27), `zaubershow nrw` (536), `zauberer gelsenkirchen` (392), `zauberer polterabend` (326, Pos 9,3), `zauberer laer` (269) — fast ohne Klicks. Das sind die Kernbegriffe von liar-entertainer.com; zwei Domains teilen sich die Sichtbarkeit, keine gewinnt.

## Empfehlung: konsolidieren, nicht pflegen
Ein täglicher Task für diese Domain lohnt nicht (6 Klicks/Monat). Sinnvoll ist eine **einmalige 301-Konsolidierung** auf liar-entertainer.com plus Fehlerwache im Wochen-Review der Hauptseite.

### 301-Karte (auf dem Host von zauberer-liar.de, `.htaccess`)
| Quelle | Ziel |
|---|---|
| `/` | `https://liar-entertainer.com/zauberer/` |
| `/kinderzauberer.html`, `/stand-up-aus-frankreich/kinderzauberer/` | `https://liar-entertainer.com/kinderzauberer/` |
| `/stand-up-aus-frankreich/kinderzauberer/kindergeburtstag/kinderzauberer-fuer-den-geburtstag-in-<stadt>/` | `https://liar-entertainer.com/kindergeburtstag/geburtstag-in-<stadt>/` (Stadt existiert dort? sonst `/kindergeburtstag/`) |
| `/zauberer-<stadt>.html` | `https://liar-entertainer.com/kinderzauberer/kinderzauberer-in-<stadt>/` (sonst `/zauberer/`) |
| `/kontakt/` | `https://liar-entertainer.com/kontakt/` |
| `/videogalerie/*` | `https://liar-entertainer.com/zauberer/zaubershow/` |
| `/stand-up-aus-frankreich/` | `https://liar-entertainer.com/zauberer/` |
| alles andere | `https://liar-entertainer.com/zauberer/` |

Vorher: vollständige URL-Liste aus GSC → Seiten exportieren und jede Zeile zuordnen; keine Kette (Ziel muss 200 sein).
Danach: GSC → Einstellungen → Adressänderung (zauberer-liar.de → liar-entertainer.com). Domain mindestens 12 Monate behalten.

### Falls die Domain bewusst als Zweitmarke bleiben soll
Dann eigener Fokus, der die Hauptseite nicht dupliziert: `zauberer polterabend`, `close up zauberer`, `magic dinner` (Erwachsenen-Zauberei). Alle Kinder-/Kindergeburtstag-Inhalte per 301 zur Hauptseite. Title der Startseite ohne „Kinderzauberer"/„Gladbeck".

## Task-Vorlage (nur wenn die Domain bleibt) — monatlich, 1. des Monats
```
Monatlicher Check für https://zauberer-liar.de (Property sc-domain:zauberer-liar.de).
Chrome: GSC Leistung 28 T vs. Vormonat (Klicks, Impressionen, Position); Seiten-Report neue Fehler (404, Soft 404, Serverfehler) — jede URL live per curl prüfen.
Prüfen: rankt die Domain für Kinder-Keywords (kinderzauberer, kindergeburtstag, zauberer gladbeck)? → melden, diese Seiten gehören per 301 auf liar-entertainer.com.
Nicht: Texte ändern, Seiten anlegen. Bericht 5 Zeilen.
```

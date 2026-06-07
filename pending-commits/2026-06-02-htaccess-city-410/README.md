# Pending Commit: City-Seiten 410 + wp-content Asset ohne 301-Hop

**Status:** ⏳ Warte auf GitHub-Auth (PAT abgelaufen, bestätigt 2026-06-02 07:35 — `push_files` lieferte `Authentication Failed: Requires authentication`)
**Aktualisiert:** 2026-06-02 (Autopilot-Lauf #2 desselben Tages) — Datei jetzt KORRIGIERT & VOLLSTÄNDIG
**Datei:** `public/.htaccess` im Repo `ben69mikail/Liar-Entertainer` (branch `main`)
**Live-SHA zum Zeitpunkt der Erstellung:** `db0af6d36526efea287e2ebdd2d8fdfbe1595a08` (unverändert seit Pastel-Redesign e0c8e06)

## ⚠️ WICHTIG: Diese `.htaccess` ist eine VOLLSTÄNDIGE Drop-in-Datei

Anders als die erste Version (nur ein einzufügender Block) ist die `.htaccess`
in diesem Ordner die **komplette, fertige Datei**. Beim Deploy einfach den
gesamten Inhalt als `public/.htaccess` committen — nichts manuell einfügen.

## Was diese Datei fixt (2 Bugs, beide live verifiziert per curl 2026-06-02)

### Bug 1 — City-Seiten liefern 404 statt 410
`/zauberer/<stadt>/` und `/clown/<stadt>/` (z.B. `/zauberer/bochum/`,
`/zauberer/essen/`, `/clown/dortmund/`) lieferten **HTTP 404**. 410 Gone
deindexiert in Google schneller. Diese WordPress-City-URLs existieren nicht
mehr als Astro-Seiten.

**Korrektur gegenüber 1. Version:** Der 410-Block steht jetzt bewusst **NACH
allen MUSTER-301-Regeln** (am Ende, vor dem `<Files>`-Block) statt mittendrin.
Grund: `/clown/kindergeburtstag/`, `/clown/geburtstag/`, `/clown/zauberer/*`
sind legitime 301-Redirect-Quellen (MUSTER 2/3/4). Die erste Version hätte sie
fälschlich in die Whitelist genommen und mit `[L]` kurzgeschlossen → sie wären
404 geworden statt 301. Jetzt feuern alle legitimen Redirects zuerst; die
Whitelist listet nur ECHTE Astro-Seiten-Roots als Sicherheitsnetz.

### Bug 2 — wp-content Asset-URLs: 301-Hop vor 410
`/wp-content/uploads/.../foo.jpg` bekam erst einen 301 auf `…/foo.jpg/`
(Trailing-Slash-Regel) und dann erst 410 Gone. Google sieht eine
Weiterleitungskette → langsamere Index-Entfernung. Fix: Asset-Dateiendungen
sind von der Trailing-Slash-Regel ausgenommen → direkt 410.

## Deploy (sobald PAT erneuert)

GitHub-API `push_files` (oder `create_or_update_file`) auf `public/.htaccess`,
branch `main`, ganzer Datei-Inhalt aus `.htaccess` in diesem Ordner.

**Commit-Message:**
```
fix(seo): [autopilot 2026-06-02] city-URLs 410 statt 404 + wp-content Asset ohne 301-Hop
```

## Verifikation nach Deploy (60 Sek warten, dann curl -I auf NON-www, -L folgen)

```bash
# City-URLs -> 410
curl -sI -L https://liar-entertainer.com/zauberer/bochum/ | grep -i ^HTTP | tail -1   # erwartet: 410
curl -sI -L https://liar-entertainer.com/zauberer/essen/  | grep -i ^HTTP | tail -1   # erwartet: 410
curl -sI -L https://liar-entertainer.com/clown/dortmund/  | grep -i ^HTTP | tail -1   # erwartet: 410

# Whitelist / legitime Redirects MÜSSEN 200 bleiben
curl -sI -L https://liar-entertainer.com/zauberer/zaubershow/      | grep -i ^HTTP | tail -1   # 200
curl -sI -L https://liar-entertainer.com/clown/clownshow/          | grep -i ^HTTP | tail -1   # 200
curl -sI -L https://liar-entertainer.com/clown/kindergeburtstag/   | grep -i ^HTTP | tail -1   # 200 (via 301!)
curl -sI -L https://liar-entertainer.com/clown/zauberer/kinderzauberer/ | grep -i ^HTTP | tail -1  # 200 (via 301!)
curl -sI -L https://liar-entertainer.com/kindergeburtstag/         | grep -i ^HTTP | tail -1   # 200

# wp-content Asset -> direkt 410, KEIN 301-Hop davor
curl -sI -L https://liar-entertainer.com/wp-content/uploads/2020/01/foo.jpg | grep -iE "^HTTP|^location"
# erwartet: nur eine Zeile HTTP/2 410, keine location-Zeile mit trailing-slash-Hop
```

Wenn `/clown/kindergeburtstag/` oder `/clown/zauberer/...` 404/410 liefert ->
Block-Reihenfolge falsch (410-Block muss NACH allen MUSTER-Regeln stehen).

## GSC-Nachbereitung nach Deploy
- "Seite mit Weiterleitung" / wp-content-Validierung erneut anstoßen.
- City-URLs als 410 in der Indexabdeckung neu validieren lassen.

# Commit #3 — .htaccess WordPress-Legacy-Aufräumblock
# Commit message: chore(seo): [autopilot 2026-05-29] htaccess WordPress-Legacy-Aufräumblock
# File: public/.htaccess
# Current SHA: e38ebaffa08ed1ac5643488618ae6fc6ab30a527

---

## ÄNDERUNG: Am Ende der Datei anhängen (VOR dem letzten Block "ETags deaktivieren")

Genauer Einfügepunkt: NACH der Zeile
  Header unset ETag
FileETag None

Einfügen NACH "FileETag None" am Ende der Datei:

```apache
# === WordPress-Legacy-Aufräumblock (LIAR Daily-Autopilot 2026-05-29) ===

# WP-Tag- und Category-Archive → /blog/
RewriteRule ^tag/.*$ /blog/ [R=301,L]
RewriteRule ^category/.*$ /blog/ [R=301,L]

# WP-Attachments → 410 Gone
RewriteRule ^.*/attachment/.*$ - [R=410,L]

# WP-Feeds → 410 Gone
RewriteRule ^.*/feed/?$ - [R=410,L]
RewriteRule ^feed/?$ - [R=410,L]

# WordPress-Standard
RewriteRule ^content/(.*)$ /$1 [R=301,L]
RewriteRule ^wp-admin/.*$ - [R=410,L]
RewriteRule ^wp-content/.*$ - [R=410,L]
RewriteRule ^index\.php/?$ / [R=301,L]
RewriteRule ^index\.php/(.*)$ /$1 [R=301,L]

# Alte Cannibalizer-Cluster
RewriteRule ^clown/zauberer/(.*)$ /zauberer/$1 [R=301,L]
RewriteRule ^clown/kindergeburtstag/(.*)$ /kindergeburtstag/$1 [R=301,L]
RewriteRule ^zauberer/kinderzauberer/(.*)$ /kinderzauberer/$1 [R=301,L]
RewriteRule ^clown/clown-zauberer/?$ /zauberer/ [R=301,L]

# Alte Stadt-URL-Schemata
RewriteRule ^clown-mieten-und-buchen-in-ihrer-stadt/clown-in-(.*)$ /clown/clownshow/clown-in-$1 [R=301,L]
RewriteRule ^clown/clown-in-(.*)$ /clown/clownshow/clown-in-$1 [R=301,L]
RewriteRule ^clown-in-(.*)$ /clown/clownshow/clown-in-$1 [R=301,L]
RewriteRule ^clown-nrw/.*$ / [R=301,L]
```

---

## WICHTIG: Prüfen ob Regeln bereits vorhanden

Vor dem Commit prüfen:
- "WordPress-Legacy-Aufräumblock" bereits im .htaccess? → NICHT nochmal anhängen
- Die Datei hat SHA e38ebaffa08ed1ac5643488618ae6fc6ab30a527 (Stand: 29.05.2026)
- Aktuelle .htaccess hat KEINEN solchen Block → sicher zum Anhängen

---

## VERIFIKATION nach Deploy:

```bash
curl -I https://liar-entertainer.com/tag/test/
# Erwartetes Ergebnis: HTTP/1.1 301 Moved Permanently (→ /blog/)

curl -I https://liar-entertainer.com/wp-admin/
# Erwartetes Ergebnis: HTTP/1.1 410 Gone
```

# SEO-Automatik liar-entertainer.com (Stand 15.09.2026)

## Ebene 1 — täglich, maschinell: `.github/workflows/seo-daily.yml`
Läuft 06:00 (MESZ) ohne PC. Baut `main`, führt `test:seo` (45) + `test:struktur` (10) aus, prüft die Live-Seite
(`scripts/daily-seo-check.mjs`), holt GSC-Daten (`scripts/gsc-report.mjs`) und schreibt
`seo-reports/daily/daily-seo-YYYY-MM-DD.md`. Bei Befund ist der Run rot →
https://github.com/ben69mikail/Liar-Entertainer/actions/workflows/seo-daily.yml
Manuell starten: dort „Run workflow".

**Was du jeden Morgen siehst:** Kopfzeile ✅/❌ für Regelwerke · Live · GSC, Deploy-Status, Befunde, GSC-Delta 7T, Fokus-Queries, Index-Status der Hubs, Blog-Fälligkeit.

## Ebene 2 — wöchentlich, Claude (Cowork Scheduled Task): `docs/TASK-liar-weekly-seo-review.md`
Montags. Liest die 7 Tagesreports, bewertet, behebt `.htaccess`/Link-Befunde (Branch + PR), macht den Blog-Vorschlag, prüft GBP.
Prompt 1:1 als Scheduled-Task-Prompt in Cowork anlegen (Task-Name `liar-weekly-seo-review`, Cron `0 7 * * 1`).

## Ebene 3 — Deploy-Gate: `.github/workflows/deploy.yml`
Kein Upload nach IONOS, wenn Tests rot sind oder der Build < 160 Seiten hat.

## GSC-API einrichten (einmalig, ~15 Min)
1. https://console.cloud.google.com/apis/library/searchconsole.googleapis.com?project=n8nki-462421 → „Aktivieren"
2. https://console.cloud.google.com/iam-admin/serviceaccounts?project=n8nki-462421 → „Dienstkonto erstellen", Name `gsc-daily-report`, keine Rolle nötig → Fertig
3. Dienstkonto öffnen → Reiter „Schlüssel" → „Schlüssel hinzufügen" → JSON → Datei wird heruntergeladen
4. https://search.google.com/search-console/users?resource_id=sc-domain:liar-entertainer.com → „Nutzer hinzufügen" → die `client_email` aus der JSON, Berechtigung „Uneingeschränkt" (nötig für URL-Prüfung)
5. https://github.com/ben69mikail/Liar-Entertainer/settings/secrets/actions → „New repository secret" → Name `GSC_SA_KEY`, Wert = kompletter JSON-Inhalt
6. Workflow manuell starten → Report muss den Abschnitt „GSC — … vs. Vorwoche" enthalten.
Die JSON-Datei danach lokal löschen; sie liegt nur noch im Secret.

## Blog-Freigabe
Artikel als `src/content/blog/<slug>.md` mit `draft: true` anlegen. Zum Veröffentlichen `draft: false` setzen (oder `freigabe: ja`, dann setzt der Wochen-Task das um) und `publishDate` auf das Datum.
Themen: `BLOG-REDAKTIONSPLAN-Q4-2026.md`.

## GBP
Website-Feld muss `https://liar-entertainer.com/` sein (ohne www). Kontrolle: GSC-Report, Zeile „www-Variante: … Impressionen" → soll gegen 0 gehen.

# Autopilot-Befund 2026-06-01 — Sitemap-Redirect-Fix (READY TO PUSH)

## GSC-Fehler gefunden: "Seite mit Weiterleitung"
Zwei in der Sitemap gelistete URLs liefern **301 statt 200** — klassischer
GSC-Coverage-Fehler ("Seite mit Weiterleitung"). Eine Sitemap darf nur
kanonische 200-URLs enthalten.

| Sitemap-URL (301) | Weiterleitungsziel |
|---|---|
| `/clown/clown-zauberer/` | `/clown/clownshow/` |
| `/zauberer/zaubershow/karneval/` | `/clown/karneval/` |

Beide Ziel-URLs sind bereits separat in der Sitemap → **kein Coverage-Verlust**
beim Entfernen der Redirect-Duplikate.

## Fix
Datei: `src/pages/sitemap.xml.ts`
- Neues `REDIRECTING_PATHS`-Set ganz oben.
- Im WP-Items-Loop: `if (REDIRECTING_PATHS.has(path)) continue;`
Das filtert die beiden 301-Pfade dauerhaft aus der generierten Sitemap und
ist erweiterbar, falls künftig weitere Redirects entstehen.

## Status
⚠️ **NICHT GEPUSHT** — GitHub-MCP-Token in diesem autonomen Lauf war
read-only (Auth-Fehler bei create_or_update_file UND push_files).
Read-Zugriff funktionierte, Write nicht.

### Nächster Schritt (interaktive Session / lokal)
Den `REDIRECTING_PATHS`-Block aus diesem Patch in
`C:\Users\ben_m\Dev\Liar-Entertainer-fresh\src\pages\sitemap.xml.ts` einfügen
(siehe Diff unten), committen, auf `main` pushen → löst Deploy aus.

## Diff (manuell anwendbar)
```diff
 const allItems = [...(pagesData as WPItem[]), ...(postsData as WPItem[])];
 const SITE = 'https://liar-entertainer.com';

+// Pfade, die per 301 weiterleiten und NICHT in die Sitemap gehoeren.
+// (GSC-Fehler "Seite mit Weiterleitung" – Ziel-URLs sind bereits gelistet.)
+const REDIRECTING_PATHS = new Set<string>([
+  '/clown/clown-zauberer/',            // -> /clown/clownshow/
+  '/zauberer/zaubershow/karneval/',    // -> /clown/karneval/
+]);
+
 // Hero images for image sitemap (main pages)
```
```diff
       if (path === '/') continue;
+      if (REDIRECTING_PATHS.has(path)) continue; // 301-Weiterleitung: nicht in Sitemap
       const loc = `${SITE}${path}`;
```

Commit-Message:
```
chore(seo): [autopilot 2026-06-01] sitemap: redirect-URLs entfernen
```

## Gesamtbefund des Laufs (alles andere GESUND)
- ✅ Strukturierte Daten: LocalBusiness, Service, BreadcrumbList, FAQPage,
  VideoObject auf allen Kernseiten LIVE und valides JSON (Redesign vom
  01.06. hat sie korrekt erhalten).
- ✅ VideoObject: alle Pflichtfelder vorhanden (name, description,
  thumbnailUrl, uploadDate, contentUrl, embedUrl).
- ✅ AggregateRating konsistent (ratingValue 5.0, reviewCount 400) auf allen
  Seiten. Hinweis: `aggregateRating`="5.0" vs einzelne `reviewRating`="5" —
  beide für Google gültig, KEIN Fehler, daher nicht angefasst (Mikro-Hygiene).
- ✅ robots.txt korrekt inkl. AI-Crawler-Allow + Sitemap-Verweis.
- ✅ Sitemap 114 URLs, www→non-www-Redirect & Canonicals konsistent.
- ℹ️ `/clown/` macht 2-Hop-Redirect auf `/clown/clownshow/` (Directory-Index),
  steht NICHT in der Sitemap → niedrig, nicht behoben.

# LIAR Website — Projekt-Handoff (Erste-Prompt-Datei)

> **Zweck:** Diese Datei im ersten Prompt eines neuen Projekts einlesen. Sie enthält alles, um nahtlos an der Website `www.liar-entertainer.com` weiterzuarbeiten, ohne Daten neu erklären zu müssen. Stand: **2026-06-02**.
>
> **Anweisung an Claude im neuen Projekt:** Lies diese Datei komplett. Frage nicht nach Pfaden, Repo-Namen oder Zugangsdaten, die hier stehen. Beachte die Sicherheitsregeln (Abschnitt 8) bei jeder Änderung.

---

## 1. Wer & Was

- **Person:** Michaël Prescler, Künstlername **„Clown Zauberer LIAR"**
- **Business:** Kinderunterhaltung + Event-Entertainment NRW, Basis **Gladbeck** (Ruhrgebiet), seit 2009, 354+ Google-Bewertungen (Ø 5★)
- **Leistungen:** Zaubershow, Ballonmodellage, Glitzer-Tattoos, Clown, Walking Acts, Feuerspucker, Pantomime, Firmenevents
- **Website:** https://www.liar-entertainer.com (Astro, Deploy GitHub Actions → IONOS SFTP)
- **Telefon (Website-weit):** +49 172 1517578
- **E-Mail:** benmikail69@googlemail.com
- **Arbeitssprache:** Deutsch. Arbeitsstil: praxisnah, strukturiert, Automation bevorzugt, volle Kontrolle gewünscht.

---

## 2. Code & Ordner (lokal, Windows)

| Was | Pfad |
|---|---|
| **LIAR Code-Repo (.git!) — Hauptarbeitsordner** | `C:\Users\ben_m\Claude\Liar-Entertainer-fresh\` |
| LIAR-Workspace (pending-commits, seo-reports) | **liegt IM Repo selbst**, in `Liar-Entertainer-fresh\` |
| Alle Projekt-Workspaces | `C:\Users\ben_m\Claude\projects\` |
| Scheduled-Tasks (SKILL.md + Registry) | `C:\Users\ben_m\Claude\Scheduled\` (Pfad fix — nicht verschieben) |
| Obsidian-Vault (Wissen/Steuerung) | `C:\Users\ben_m\Cerveau I\` |
| Globaler User-Ordner (Skills, Plugins, MCP-Configs) | `C:\Users\ben_m\.claude\` (geschützt, nicht als Cowork-Ordner mountbar) |

> **Grundregel (globale CLAUDE.md):** Alle Claude-relevanten Dateien liegen unter `C:\Users\ben_m\.claude` bzw. `C:\Users\ben_m\Claude` und sollen dort gespeichert werden.
> **Im neuen Projekt:** Als Cowork-Ordner `C:\Users\ben_m\Claude\Liar-Entertainer-fresh\` mounten — dann hast du Code + Workspace + `.git` in einem.

---

## 3. Repo & Deploy

- **Aktives Repo:** `ben69mikail/Liar-Entertainer` (großes L) — Owner ist `ben69mikail`, **nicht** `benmikail69`
- ⚠️ **VERALTET, nicht mehr verwenden:** `ben69mikail/liar-entertainer-blog`
- **Branch:** `main` (Push triggert Auto-Deploy)
- **CI/CD:** `.github/workflows/deploy.yml` — Node 20 + Poppins-Fonts + `npm ci` + `npm run build` + Python `paramiko` SFTP-Upload
- **Deploy-Script:** `deploy_ionos.py` (löscht alte Hash-CSS vor Upload) → SFTP nach IONOS (kein Netlify, kein netlify.toml)
- **Redirects:** über `public/.htaccess` (Apache) — **nur APPEND, nie überschreiben**
- **Stadtseiten:** `src/pages/[...slug].astro` + `scripts/generate-city-pages.mjs`
- **Deploy-Status prüfen:** https://github.com/ben69mikail/Liar-Entertainer/actions
- **Verifiziert:** 49+ erfolgreiche Deploys (Stand 2026-06-01)

### Standard-Workflow
```bash
cd C:\Users\ben_m\Claude\Liar-Entertainer-fresh
git pull origin main          # WICHTIG: n8n committet auch ins Repo
# ... Änderungen machen ...
npm run dev                   # lokal testen auf localhost:4321
git add -A && git commit -m "..." && git push origin main
# → GitHub Actions baut + uploaded automatisch (4–9 Min) → live
```

---

## 4. Zugangsdaten & Endpunkte

> Passwörter/Tokens stehen aus Sicherheitsgründen **nicht** in dieser Datei — nur wo sie liegen und wie man sie erneuert.

**IONOS Webhosting** (Premium, Performance 5/5, CDN aktiv)
- Webhosting-ID: `f9acac9b-5403-436b-a1dd-663689c9c932`
- SFTP-Server: `home362401740.1and1-data.host`
- SFTP-User: `u62702423`
- SFTP-Passwort: IONOS → Hosting → SFTP & SSH → Verwalten (neu setzen, falls nötig)
- **GitHub-Secrets** (im Repo gesetzt): `IONOS_SFTP_HOST`, `IONOS_SFTP_USER`, `IONOS_SFTP_PASS`, `IONOS_SFTP_REMOTE` (+ optional `N8N_DEPLOY_WEBHOOK`, `TELEGRAM_BOT_TOKEN`)

**Domains (3) und Webspace-Ziele**
- `liar-entertainer.com` → `/LIARastro/` (Live-Site)
- `zauberer-liar.de` → `/zauberer-nrw/`
- 1 weitere Domain (unbekannt)
- Rollback-Verzeichnis: `/LIARastroBACKUP/`

**GitHub (Schreibzugriff)**
- MCP-Write nutzt `api.githubcopilot.com`. Token als Env-Var `GITHUB_PERSONAL_ACCESS_TOKEN`.
- ⚠️ **Bekannter Blocker:** fine-grained PAT wird oft abgelehnt → **CLASSIC PAT mit vollem `repo`-Scope** verwenden. Nach Token-Wechsel App neu starten und in **frischem Chat** pushen (MCP cacht alten Token in laufender Session).
- **Bewährter Fallback (49+ Deploys):** lokales `git push` aus `Liar-Entertainer-fresh\` — unabhängig vom MCP-Token.
- Wächter-Task `github-pat-waechter` (Mo 08:10) warnt vor PAT-Ablauf.

**Google Search Console:** Property `sc-domain:liar-entertainer.com`

---

## 5. Automation (läuft im Hintergrund)

**4 aktive Scheduled-Tasks** (Registry: `C:\Users\ben_m\Claude\Scheduled\`, self-contained Prompts):

| Task | Zeit | Zweck |
|---|---|---|
| `liar-daily-seo-autopilot-v2` | tägl. 06:00 | GSC-Analyse → .htaccess/robots.txt-Patches + Schema-Fixes → Commit → SFTP-Deploy. Max **5 Commits/Tag**. |
| `gbp-quota-approval-check` | tägl. 09:00 | Google-Business-Profile-API Quota-Approval-Status |
| `nas-backup-nightly` | tägl. 02:00 | NAS-Backup (Scope inkl. `C:\Users\ben_m\Claude`) |
| `github-pat-waechter` | Mo 08:10 | prüft GitHub-Schreibzugriff wöchentlich |

**Blog-Automation (n8n bei Hostinger):**
- n8n-URL: `https://n8n.srv860817.hstgr.cloud/`
- Aktiver Workflow: `XxHIVhsD4ZPzVa78` (LIAR-2026-01 Blog Montag)
- Telegram-Bot: `@MeinBLOGArtikel_bot` (ID `8643097969`, Chat-ID `2106974057`) — ⚠️ Token derzeit ungültig, BotFather-Erneuerung nötig
- GDrive Foto-Pool: `16Fsb35rRsLWIyS2xQ9clzEvs831IWGkV`
- GSheets Redaktionsplan: `1HgN_A1dedfkXIgb9MdDsNlx7WMQuOeVM6mOKCkJRayo`
- n8n-Workflow-Änderungen via **Claude Code** (lokaler Agent), nicht Cowork.

---

## 6. SEO — Fokus & Regeln

**Top-4-Keywords (alle SEO-Tasks darauf fokussieren):** Clown · Zauberer · Zaubershow · Kindergeburtstag
**2. Prio-Cluster:** Kinderzauberer, Geburtstag für Kinder, + Stadt/NRW-Kombis (Clown NRW, Zauberer Bochum, Zaubershow Essen …)

**Arbeitsweise (verbindliches Feedback):**
- **Nur Hochimpact-Tasks** mit messbarem Klick-Effekt. Keine Mikro-Hygiene (Title-Längen, Branding-Vereinheitlichung) wenn Effekt einstellig/Monat.
- **Alle GSC-Fehler systematisch komplett bereinigen** — nicht nur analysieren, sondern fixen + GSC-Validierung + Erfolg verifizieren.
- ROI-Reihenfolge: 1) Schema.org (LocalBusiness+AggregateRating, Service+Offer mit Preisen, FAQ) → 2) Interne Links für Pos 11–20 → 3) GSC-Fehler auf 0 → 4) Content-Gaps → 5) Cannibalizers (z.B. `/clown/clown-zauberer/`).
- Vor jedem SEO-Task fragen: „erwarteter absoluter Effekt in Klicks/Monat?" — klein → auslassen/bündeln.

---

## 7. Design (Pastel-Redesign, verbindlich für neue Seiten)

**Status:** 18 Seiten LIVE (commit `e0c8e06`, 2026-06-01).
**Noch offen:** `src/pages/[...slug].astro` (City-Template, 2017 Zeilen) — **nur visuelle Änderungen**, keine strukturellen ohne Michaels Freigabe.

```text
Pastel-Rot-Sektion:   bg-[#fdf2f2] border-y border-[#f0c4c4] py-10
Weiße Stat-Cards:     bg-white rounded-2xl p-6 text-center border border-[#f0c4c4] shadow-sm
Accent-Farbe:         text-[#d7393e]
Body-Text:            text-[#374151]
Pastel-Blau-Sektion:  bg-[#eff4ff] border-y border-[#c5d3f7]
Blaue Feature-Cards:  bg-white rounded-xl p-5 border border-[#c5d3f7] shadow-sm card-hover
Portrait-Fotos:       rounded-2xl, box-shadow: 0 8px 24px rgba(0,0,0,0.12)
```
- Wave-SVG-Elemente: **entfernt**. Dunkle CTA-Sektionen (`bg-[#1f2025]`): **behalten, unverändert**.

---

## 8. Sicherheitsregeln (IMMER beachten)

- ⛔ **NIEMALS H1-Texte** ohne Michaels Freigabe ändern
- ⛔ **NIEMALS Fließtexte** (Body-Paragraphen) ohne Freigabe ändern
- ⛔ **NIEMALS neue City-Pages** erstellen ohne Freigabe
- ⛔ **NIEMALS** `scripts/generate-city-pages.mjs` bearbeiten
- ⛔ **NIEMALS strukturelle** Änderungen an `src/pages/[...slug].astro` ohne Freigabe
- ⛔ **NIEMALS Astro-Routen** umbenennen/löschen
- ✅ Nur **APPEND** an `public/.htaccess`, nie überschreiben
- ✅ **Max 5 Commits pro Tag**
- ✅ Bei Klickeinbruch > 30% oder Manual Penalty → **READ-ONLY**

---

## 9. Status & offene Punkte (Stand 2026-06-02)

- ✅ Pastel-Redesign 18 Seiten live (`e0c8e06`)
- ✅ WordPress-Legacy aus IONOS entfernt (22.05.2026, ~1.2 GB frei)
- ✅ Schema-Fix VideoObject auf 4 Pages live (Deploy #48, commit `7260934`)
- ✅ City-410 `.htaccess`-Fix gepusht (commit `b5e29b2`) + robots.txt/sitemap (`b50e9a3`). Live verifiziert: `/zauberer/bochum/`=410, `/zauberer/zaubershow/`=200, `/clown/kindergeburtstag/`=200
- ⏳ **City-Template** `[...slug].astro` noch ohne Pastel-Design (nur visuell anpassen, Freigabe für Struktur)
- ⏳ **Telegram-Bot-Token** erneuern (BotFather) + GitHub-Secret `TELEGRAM_BOT_TOKEN` updaten
- ⏳ **GitHub PAT:** falls MCP-Write scheitert → Classic PAT mit `repo`-Scope, frischer Chat, oder lokaler `git push`-Fallback

---

## 10. Stolperfallen (gelernt)

- `git pull origin main` **vor jeder Arbeit** — n8n committet eigenständig ins Repo (Bot-Commits: `[skip ci] images: …`, `blog: …`)
- **git in der Sandbox** auf gemountetem Windows-`.git` ist unzuverlässig (Index-Korruption) → Commit/Push auf Windows ausführen
- Beim Stagen: pro Commit **nur die eine Datei** stagen + dazwischen committen (sonst werden ungewollt Dateien mitgezogen)
- MCP-Write cacht Token der laufenden Session → nach Token-Wechsel **neuer Chat**

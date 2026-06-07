# LIAR — Infrastruktur & Zugänge (Projekt-Stammdaten)

> **Zweck:** Reine Technik-/Zugangs-Referenz zum Weiterführen des Projekts in einer neuen Sitzung. Keine Homepage-Aufgaben, kein Status. Stand: **2026-06-02**.
>
> **Hinweis:** Passwörter & Tokens stehen aus Sicherheitsgründen NICHT im Klartext — nur wo sie liegen und wie man sie erneuert.

---

## 1. Person & Marke

- **Person:** Michaël Prescler — Künstlername **„Clown Zauberer LIAR"**
- **E-Mail:** benmikail69@googlemail.com
- **Telefon (website-weit):** +49 172 1517578
- **Website:** https://www.liar-entertainer.com
- **Arbeitssprache:** Deutsch

---

## 2. Lokale Ordner (Windows)

| Was | Pfad |
|---|---|
| **LIAR Code-Repo (.git) — Hauptordner** | `C:\Users\ben_m\Claude\Liar-Entertainer-fresh\` |
| Workspace (pending-commits, seo-reports) | liegt IM Repo selbst |
| Scheduled-Tasks (Registry + SKILL.md) | `C:\Users\ben_m\Claude\Scheduled\` (Pfad fix) |
| Obsidian-Vault | `C:\Users\ben_m\Cerveau I\` |
| Globaler Claude-Ordner (Skills, Plugins, MCP-Configs) | `C:\Users\ben_m\.claude\` |

> Grundregel: Alle Claude-Dateien liegen unter `C:\Users\ben_m\Claude` bzw. `C:\Users\ben_m\.claude`.
> Im neuen Projekt: `C:\Users\ben_m\Claude\Liar-Entertainer-fresh\` als Cowork-Ordner mounten → Code + Workspace + `.git` in einem.

---

## 3. GitHub

- **Aktives Repo:** `ben69mikail/Liar-Entertainer` (großes L)
- **Owner-Account:** `ben69mikail` (nicht `benmikail69`)
- **Branch:** `main` (Push triggert Auto-Deploy)
- ⚠️ **VERALTET, nicht verwenden:** `ben69mikail/liar-entertainer-blog`
- **Actions/Deploy-Status:** https://github.com/ben69mikail/Liar-Entertainer/actions
- **Schreib-Token:** Classic PAT mit vollem `repo`-Scope, gesetzt als Env-Var `GITHUB_PERSONAL_ACCESS_TOKEN`. MCP-Write nutzt `api.githubcopilot.com` (fine-grained PATs werden dort oft abgelehnt → Classic verwenden).
- **Token-Wechsel:** App neu starten, dann in **frischem Chat** pushen (MCP cacht alten Token in laufender Session).
- **Wächter-Task:** `github-pat-waechter` (Mo 08:10) warnt vor PAT-Ablauf.

---

## 4. Hosting / Deploy

> **Kein Netlify.** Deploy läuft über GitHub Actions → SFTP zu **IONOS**. (Es gibt KEIN netlify.toml; Redirects laufen über Apache `.htaccess`.)

**IONOS Webhosting** (Premium, Performance 5/5, CDN aktiv)
- Webhosting-ID: `f9acac9b-5403-436b-a1dd-663689c9c932`
- **SFTP-Server:** `home362401740.1and1-data.host`
- **SFTP-User:** `u62702423`
- **SFTP-Passwort:** IONOS-Kundenbereich → Hosting → SFTP & SSH → Verwalten (dort neu setzen)
- Nutzung (Stand 22.05.2026): 10,45 GB, ~161.000 Dateien

**Domains → Webspace-Verzeichnisse**
| Domain | Zielordner |
|---|---|
| `liar-entertainer.com` | `/LIARastro/` (Live-Site) |
| `zauberer-liar.de` | `/zauberer-nrw/` |
| (1 weitere, unbekannt) | — |
| Rollback-Backup | `/LIARastroBACKUP/` |

**CI/CD-Kette**
- Workflow: `.github/workflows/deploy.yml` — Node 20 + Poppins-Fonts + `npm ci` + `npm run build` + Python `paramiko` SFTP-Upload
- Deploy-Script: `deploy_ionos.py`
- **GitHub-Secrets (im Repo gesetzt):** `IONOS_SFTP_HOST`, `IONOS_SFTP_USER`, `IONOS_SFTP_PASS`, `IONOS_SFTP_REMOTE` (+ optional `N8N_DEPLOY_WEBHOOK`, `TELEGRAM_BOT_TOKEN`)

**Standard-Deploy-Workflow**
```bash
cd C:\Users\ben_m\Claude\Liar-Entertainer-fresh
git pull origin main          # n8n committet auch ins Repo
npm run dev                   # lokal testen auf localhost:4321
git add -A && git commit -m "..." && git push origin main
# → Actions baut + SFTP-Upload (4–9 Min) → live
```

---

## 5. Google

- **Google Search Console:** Property `sc-domain:liar-entertainer.com`
- **Google Business Profile API:** Cloud-Projekt `n8nki-462421`, OAuth-Client eingerichtet, Quota-Approval beantragt (Ticket 7-6367000040869). Status-Check-Task: `gbp-quota-approval-check` (tägl. 09:00)

---

## 6. Blog-Automation (n8n bei Hostinger)

- **n8n-URL:** `https://n8n.srv860817.hstgr.cloud/`
- **n8n-MCP-Connector-UUID:** `aee184a8-2b33-4c04-8939-49627ecba115`
- **Aktiver Workflow:** `XxHIVhsD4ZPzVa78` (LIAR-2026-01 Blog Montag)
- **Test-Workflow:** `lX3kTKlcboPwP1hL` (Hello Claude via Telegram)
- **Telegram-Bot:** `@MeinBLOGArtikel_bot`, Bot-ID `8643097969`, Chat-ID `2106974057`
  - Token-Erneuerung über BotFather; danach GitHub-Secret `TELEGRAM_BOT_TOKEN` updaten
- **Google Drive Foto-Pool (Ordner-ID):** `16Fsb35rRsLWIyS2xQ9clzEvs831IWGkV`
- **Google Sheets Redaktionsplan (ID):** `1HgN_A1dedfkXIgb9MdDsNlx7WMQuOeVM6mOKCkJRayo` (Sheet „Tabelle1")
- **LLM:** Anthropic via OpenRouter-Credential gewrappt
- n8n-Workflow-Änderungen über **Claude Code** (lokaler Agent), nicht Cowork.

---

## 7. NAS (Backup-Backend)

- **Gerät:** UGREEN DXP2800, UGOS Pro, Intel N100, 8 GB RAM
- **IP:** `192.168.178.109`
- **Docker-Install-Pfad:** `/volume1/docker/liar-agent-platform/`
- Backup-Task: `nas-backup-nightly` (tägl. 02:00) sichert u.a. `C:\Users\ben_m\Claude`

---

## 8. Scheduled-Tasks (laufen autonom)

Registry-Pfad: `C:\Users\ben_m\Claude\Scheduled\<task>\SKILL.md` (self-contained Prompts).

| Task | Zeit | Zweck |
|---|---|---|
| `liar-daily-seo-autopilot-v2` | tägl. 06:00 | GSC → .htaccess/Schema-Patches → Commit → Deploy. Max 5 Commits/Tag |
| `gbp-quota-approval-check` | tägl. 09:00 | Google-Business-Profile API Quota-Status |
| `nas-backup-nightly` | tägl. 02:00 | NAS-Backup |
| `github-pat-waechter` | Mo 08:10 | GitHub-Schreibzugriff prüfen |

---

## 9. Wichtige Repo-Dateien

| Datei | Funktion |
|---|---|
| `.github/workflows/deploy.yml` | CI/CD-Pipeline |
| `deploy_ionos.py` | SFTP-Upload zu IONOS |
| `public/.htaccess` | Apache-Redirects (nur APPEND, nie überschreiben) |
| `src/pages/[...slug].astro` | City-Pages-Template |
| `scripts/generate-city-pages.mjs` | Generator für Stadtseiten |
| `.env.example` | Vorlage für Umgebungsvariablen |
| `LIAR-HANDOFF.md` | ausführlicher Projekt-Handoff |

---

## 10. Bekannte technische Stolperfallen

- **Vor jeder Arbeit `git pull origin main`** — n8n committet eigenständig ins Repo.
- **git-Commit/Push gehört auf Windows**, nicht in die Linux-Sandbox: das Windows-`.git` über den Mount ist für Sandbox-git nicht zuverlässig lesbar (Index-Korruption / „not a git repository").
- MCP-Write cacht den Token der laufenden Session → nach Token-Wechsel **neuer Chat**.
- Telegram-Bot-Token & FB/IG-Tokens laufen periodisch ab → bei n8n-Fehlern zuerst Credentials prüfen.

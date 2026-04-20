# CLAUDE.md — Shared Memory for Los Barberos Quito

This file is shared context between **Claude Code** (running locally on Sebastián's Mac) and **Cowork mode** (cloud sandbox). Both sides read and update it. Claude Code auto-loads it at session start; in Cowork, say "read CLAUDE.md" to catch up.

---

## Session Start Protocol — READ THIS FIRST

When Sebastián says "syncbp" (or at the start of any session), do this exact sequence before anything else:

1. Read this entire file top to bottom.
2. Also read `CHAT.md` — it's the live turn-by-turn handoff between Cowork and Claude Code.
3. Look at **Current Focus** — that's the active work.
4. Look at **Next Actions** — that's the immediate to-do list with concrete commands.
5. Look at **Rolling Log** — the newest entry tells you what just happened.
6. If Current Focus or Next Actions are empty, ask Sebastián what to work on.
7. If work is in progress, pick up the top item in Next Actions and execute it.
8. When finishing meaningful work, append a dated Rolling Log entry and update Current Focus / Next Actions / Gotchas as needed.

**Related files:**
- `CLAUDE.md` (this file) — persistent project state. Read at start of every session.
- `CHAT.md` — live handoff relay. Updated every turn.
- `.claude/skills/syncbp/SKILL.md` — the **`syncbp`** skill. Single trigger word that replaces "read MD" + "read chat". When Sebastián says "syncbp" (any casing — `syncBP`, `sync bp`, `SyncBP`), follow the procedure in that SKILL.md: read both files, summarize the other side's turn, act on the inbox, write back, flip baton. Claude Code auto-registers it because it's a project skill. Cowork does it manually (same steps).

**Which side does what:**
- **Claude Code (Mac):** execution — run scripts, `streamlit run`, git, real network calls, file edits. Can update MD directly.
- **Cowork (cloud):** planning, review, write-ups, document deliverables (.docx/.pptx/.xlsx/.pdf). Edits MD via the mounted folder.

**Escalation rule:** if you hit a blocker, stop and summarize it in Rolling Log with a `BLOCKED:` prefix. Don't keep retrying silently.

---

## Next Actions

Ordered, one at a time. Top = do next. Remove items as they complete; promote new items from Current Focus.

<!-- TODO: Sebastián to populate -->

---

## Project

**Los Barberos Quito** — bilingual (ES/EN) Streamlit website for the Quito-based barbershop [Los Barberos Quito](https://www.facebook.com/LosBarberosQuito/). Features: animated hero, service catalog, gallery, booking calendar with SQLite persistence, WhatsApp deep-link integration, market analysis dashboard, mobile-responsive dark/light theme.

**Owner:** Sebastián (sebasflores@gmail.com)
**Path on Mac:** `/Users/sebastianflores/Desktop/OpenTF/Barberos`
**Stack:** Streamlit · streamlit-option-menu · Plotly · pandas · SQLite
**Run:** `streamlit run app.py` (or `./Run-LosBarberos.command`)

---

## Current Focus

<!-- TODO: Sebastián to fill in active workstream + acceptance criteria -->

---

## Key Files

| File | Purpose |
|---|---|
| `app.py` | Streamlit entrypoint — page config, navbar, language/theme toggles, section routing, footer, floating WhatsApp |
| `components/config.py` | All business data (WhatsApp #, phone, email, address, hours, services, barbers, gallery URLs, social links) — edit here to update the whole site |
| `components/i18n.py` | ES/EN translation dictionary + `init_lang` / `set_lang` / `t` helpers |
| `components/styles.py` | Custom CSS, theme system (dark/light), floating WhatsApp button |
| `components/sections.py` | Hero, services, gallery, about, testimonials, contact, footer renderers |
| `components/booking.py` | Booking calendar — date picker, time-slot generator, SQLite persistence, WhatsApp confirmation handoff |
| `components/market.py` | Market analysis page (Plotly charts: market size, competitors, personas, SWOT, growth playbook) |
| `.streamlit/config.toml` | Theme + server settings |
| `requirements.txt` | streamlit, streamlit-option-menu, plotly, pandas, python-dateutil |
| `Run-LosBarberos.command` | macOS double-click launcher |
| `data/` | SQLite DB lives here at runtime |
| `assets/` | Static images |
| `losbarberos-quito/` | Nested duplicate of project tree — purpose unclear (TODO: Sebastián to confirm whether this is a staging copy, deploy bundle, or stale artifact to delete) |

---

## Architecture Notes

<!-- TODO: Sebastián / Cowork to fill in as decisions get made.
Suggested seed topics:
- Routing model (option_menu keys → render_* functions in app.py)
- Theme + language state lives in st.session_state, persisted across reruns
- WhatsApp integration: pure deep-link (wa.me URLs), no Business API
- Booking persistence: SQLite file under data/, schema TBD
-->

---

## Gotchas

<!-- TODO: add as you hit them. One-line problem + one-line workaround. -->

---

## Active Task List (mirror)

Canonical state lives in the task tools; this is a snapshot.

<!-- empty -->

---

## Rolling Log

Add a dated entry after each meaningful session. Prune entries older than ~30 days.

<!-- empty -->

---

## How to Update This File

**From Claude Code on the Mac:**
Edit directly. Claude Code has full write access.

**From Cowork:**
Ask me to "update CLAUDE.md with [X]". I'll edit via the mounted folder.

**Conventions:**
- Dated entries in Rolling Log (newest first).
- Update Current Focus when priorities shift.
- Update Gotchas when you hit a new one (with one-line fix note).
- Don't restate info in the task list — link by task number.

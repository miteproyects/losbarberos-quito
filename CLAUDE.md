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

**Phase 1 — Clean & Fix** ✅ Complete (2026-04-19)

1. ~~Delete nested `losbarberos-quito/` duplicate.~~ ✅ Done — promoted nested canonical → root via rsync, then removed nested folder.
2. ~~Fix theme-toggle button shape.~~ ✅ Superseded by redesign — editorial sharp-edge (2px border-radius) pills now match ES/EN across nav.
3. ~~Fix `Inicio` nav tab black-corner bleed.~~ ✅ Superseded by redesign — option_menu container is now `transparent` and the nav-link selected state uses flat ink-on-cream (no rounded corners bleeding).
4. ~~Fix brand logo not rendering.~~ ✅ Done — `logo_svg()` already resolves via `Path(__file__).parent.parent / "assets" / "logo.svg"` (inlines the SVG, no static-serving needed). `enableStaticServing = true` added to `.streamlit/config.toml` as belt-and-suspenders.
5. ~~Wire git remote + push.~~ ✅ Done — deployed to https://losbarberosquito.streamlit.app from `main` → root `app.py`.

**Phase 1.5 — Agency-style redesign** ✅ Complete (2026-04-19)

Full thisisstudiox.com-inspired editorial makeover: cream + ink palette with brass-gold accent (light is now the default theme, dark retained as alt), Fraunces serif display + Inter body + JetBrains Mono kickers, flipped-dark hero panel inside the cream page with oversized serif display-xl, numbered section kickers (01–06), editorial marquee between hero and services, hover-flip-to-dark service cards, asymmetric gallery grid, serif pull-quote testimonials, sharp-edge (2px) minimal buttons with mono labels, unified contact-card styling for both contact + booking summary.

**Phase 2 — Real data (gated on Sebastián)**

6. Populate `EMAIL`, `ADDRESS_ES/EN`, live Google Maps `pb=` embed, verified TikTok URL, real barber portraits in `components/config.py`.

---

---

## Project

**Los Barberos Quito** — bilingual (ES/EN) Streamlit website for the Quito-based barbershop [Los Barberos Quito](https://www.facebook.com/LosBarberosQuito/). Features: animated hero, service catalog, gallery, booking calendar with SQLite persistence, WhatsApp deep-link integration, market analysis dashboard, mobile-responsive dark/light theme.

**Owner:** Sebastián (sebasflores@gmail.com)
**Path on Mac:** `/Users/sebastianflores/Desktop/OpenTF/Barberos`
**Stack:** Streamlit · streamlit-option-menu · Plotly · pandas · SQLite
**Run:** `streamlit run app.py` (or `./Run-LosBarberos.command`)
**GitHub:** https://github.com/miteproyects/losbarberos-quito (public)
**Live URL:** https://losbarberosquito.streamlit.app (Streamlit Community Cloud; `main` branch → `app.py`)

---

## Setup

**Cowork workspace selection:** When opening this project in the Cowork desktop app, pick `/Users/sebastianflores/Desktop/OpenTF/Barberos/` as the workspace — **not** the nested `losbarberos-quito/` subfolder. Selecting the subfolder hides `CLAUDE.md` and `CHAT.md`, which breaks the `syncbp` handoff. The parent folder makes both the handoff files and the project tree reachable.

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
| `assets/` | Static images — `logo.svg` lives here |

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

- **Default theme is now `light` (cream editorial).** `init_theme()` in `components/styles.py` sets `st.session_state.theme = "light"` on first run. Dark is still reachable via the nav toggle but no longer the default. If Streamlit Cloud caches the old session, a hard refresh may be needed after redeploy.
- **Navbar layout relies on `:has()` CSS selector.** The editorial 2px-pill alignment (theme toggle + ES + EN) in `components/styles.py` uses `div[data-testid="stHorizontalBlock"]:has(.nav-pill)`. Works in all modern browsers but fails silently on very old versions — the buttons would render but without the shared 40px baseline.

---

## Active Task List (mirror)

Canonical state lives in the task tools; this is a snapshot.

<!-- empty -->

---

## Rolling Log

Add a dated entry after each meaningful session. Prune entries older than ~30 days.

- **2026-04-19 — Cowork** — Full agency-style redesign (inspired by thisisstudiox.com) + canonical-copy resolution + Streamlit Cloud redeploy. (1) Rewrote `components/styles.py` with editorial design system: cream `#F2EEE6` + ink `#141414` + brass `#A8762E`, Fraunces serif display + Inter + JetBrains Mono, flipped-dark hero panel, sharp-edge 2px buttons with mono kickers, hover-flip-to-dark service cards, marquee infrastructure, asymmetric gallery, pull-quote testimonials. Set `light` as the new default theme. (2) Updated `components/sections.py` + `components/booking.py` + `app.py` to match new class names (`.hero-kicker`, `.hero-metrics/.hero-metric`), added `render_marquee()` between hero and services with bilingual phrases, added numbered section kickers `01 — SERVICIOS` through `06 — CONTACTO`, upgraded option_menu palette from gold/dark-grey to editorial ink-on-cream. (3) Promoted nested canonical `losbarberos-quito/` → root via rsync, deleted nested folder, logo.svg now at root `assets/`. (4) Updated `.streamlit/config.toml` to cream palette + `enableStaticServing = true`. (5) Pending: git commit + push to trigger auto-redeploy on Streamlit Cloud.
- **2026-04-18 — Cowork** — Deployed Los Barberos to Streamlit Community Cloud via Claude in Chrome (Sebastián was already logged into GitHub as `miteproyects` and Streamlit Cloud). Repo `miteproyects/losbarberos-quito` already existed (public, contains both root `app.py` AND nested `losbarberos-quito/` subfolder with canonical newer files). Deployed from root `app.py` as the safer choice since Streamlit's file-path autocomplete only surfaced root-level files. Live at **https://losbarberosquito.streamlit.app**. Caveats: the deployed root `app.py` is the older copy — the 3 unfixed UI bugs (logo not rendering, theme toggle shape, Inicio tab bleed) will be visible. To upgrade, resolve the nested-canonical Gotcha first, then push and auto-redeploy.
- **2026-04-18 — Claude Code (T4)** — Picked up Phase 1 task 1 (delete nested `losbarberos-quito/`). **BLOCKED** at the safety-check step: `diff -rq` showed the nested folder is NOT a clean duplicate — `app.py`, `components/{config,sections,styles}.py` all diverge, and on every divergent file the nested copy is newer (mtimes 16:25–17:42) and larger than the parent (16:08–16:20). `assets/logo.svg` exists only in the nested copy. Conclusion: nested is the de facto canonical working copy; deleting it would discard Sebastián's most recent edits and the brand logo. No destructive action taken. Pinned finding as Gotcha + updated Key Files row. Baton → Cowork with full diagnostic for re-plan.
- **2026-04-18 — Cowork** — First successful cross-side `syncbp` after workspace remount. Acknowledged Claude Code's T1 scaffolding, proposed Phase 1 "Clean & Fix" queue (delete nested duplicate → fix 3 UI bugs → wire git remote), populated `Next Actions`. Baton → Claude Code with task 1 (delete nested duplicate) as the immediate pickup.

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

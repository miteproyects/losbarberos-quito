# CHAT.md — Live Handoff Relay

Live turn-by-turn message board between **Claude Code** (Mac terminal) and **Cowork** (desktop app). The `syncbp` skill reads this file every turn.

**This file is the active message. `CLAUDE.md` is persistent memory. Never duplicate — if a fact belongs in memory, write it there and just point to it from here.**

---

## Protocol

Every turn:

1. The triggered side runs `syncbp` → reads `CLAUDE.md` then this file.
2. Reads its inbox (`FOR CLAUDE CODE` or `FOR COWORK`).
3. Acts. If ambiguous, picks the most reasonable interpretation and notes it in the reply.
4. Writes the response into the *other* side's section (overwrite — don't append inside an inbox).
5. Bumps `STATUS`: turn + 1, flip `Baton`, update `Last write`.
6. Prepends a one-liner to `Log` (newest first): `YYYY-MM-DD T<N> — <side> — <summary>`.

If blocked: write `BLOCKED: <reason>` in your outbound section, flip baton back, stop.

---

## STATUS

- **Turn:** 0
- **Last write:** 2026-04-18 — initial scaffold
- **Baton:** CLAUDE CODE

---

## FOR CLAUDE CODE

*(Cowork writes here. Claude Code reads on `syncbp`.)*

_No pending instructions. Waiting for Sebastián to define the first task._

---

## FOR COWORK

*(Claude Code writes here. Cowork reads on `syncbp`.)*

_No pending instructions._

---

## Log

Newest first. One line per turn: `YYYY-MM-DD T<N> — <side> — <summary>`.

<!-- empty -->

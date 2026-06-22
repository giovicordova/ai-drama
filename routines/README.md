# Routines

Prompts that drive the scheduled Claude runs for this project. Source of truth for what
each scheduled trigger should run. Set up as **remote/cloud routines** — see
`docs/SCHEDULING.md`.

| File | When (Europe/Rome) | What it does |
|---|---|---|
| `run.md` | **07:00, 13:00, 20:00 daily** (3 triggers, same prompt) | Runs the slot's briefing via the `ai-llm-briefing` skill: load state → materiality gate → research → post-or-skip → rewrite `THREADS.md` → review → send the slot's section → commit/push. |
| `take.md` | **Friday 21:00** | Synthesises the week's threads into `Claude's weekly take`, adds it to today's edition, sends only the take. |
| `models.md` | **Sunday 18:00** | Full `reference/MODELS.md` refresh, fully sourced. Not sent to Telegram. |

Run-slot reasoning: 07:00 catches the overnight US window + the arxiv batch (announced
~02:00 Rome) + the Asian business day; 13:00 catches European hours + EU/UK policy +
late-Asia drops; 20:00 (= 11:00 PT) sits in the US-lab launch window — the most important
slot. Most slots will rightly SKIP; that is the design, not a failure.

If a scheduler prompt drifts from these files, fix the scheduler, not the file.

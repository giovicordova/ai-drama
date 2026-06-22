Weekly routine. Refreshes `reference/MODELS.md` — the living "which model is best at
what" reference. Sunday 18:00 Europe/Rome. Not sent to Telegram.

Before starting:

  git checkout main && git pull origin main

Refresh `reference/MODELS.md` so every ranked row is current and fully sourced. This is
the ONLY routine allowed to change its rankings (daily runs never touch them).

Rules — non-negotiable, this is the "trust no one" guarantee:

1. For every row in every category (best coding / reasoning / longest usable context /
   multimodal / agentic-tool-use / cheapest capable / best open-weight / fastest), each
   entry MUST carry: a **named benchmark or metric**, a **number**, a **date**, and a
   **primary URL you opened this session** (model card, official pricing page, lab blog,
   arxiv, or a reproducible third-party eval). No number → drop the entry. No primary
   source → drop the entry. Do not guess or fill from memory.
2. Flag self-reported numbers explicitly; prefer independent / reproducible evals over
   vendor self-reports.
3. Research via the verified-feed spine first (model cards on Hugging Face, lab blogs,
   arxiv, official pricing pages), then targeted search to confirm. Allowlist + bans
   from the skill's Section 5 apply.
4. Update the header date and "Last full refresh" / "Next scheduled" lines.
5. "Best" is a dated snapshot — keep the per-row date visible; it is load-bearing.

After refreshing:

1. Sanity check: confirm every non-placeholder ranking line contains both a URL and a
   number. (`grep -nE '^[0-9]\.' reference/MODELS.md` and eyeball each.)
2. Commit on main: `reference/MODELS.md`. Message: `chore: weekly MODELS.md refresh YYYY-MM-DD`.
3. Push: `git push origin main`

Do not send anything to Telegram from this routine.

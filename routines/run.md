One prompt, fired at 07:00, 13:00, and 20:00 Europe/Rome. The skill derives which
slot it is from the clock — do not hardcode a slot here.

Before starting, ensure you are on main with the latest state pulled (the previous
slot's edition and THREADS.md may have been committed by an earlier run):

  git checkout main && git pull origin main

Use the ai-llm-briefing skill at `.claude/skills/ai-llm-briefing/SKILL.md` to run this
slot's briefing. Follow the skill exactly. It handles: detecting the run slot, loading
THREADS.md and today's edition, the materiality SKIP gate (silence is correct when
nothing material happened), verified-feed-first research, sourcing, writing, and the
3-run edition format.

After the skill finishes:

1. Run `scripts/review-edition.sh editions/YYYY-MM-DD.md` to confirm the slot's post is
   within the 280-char cap and well-formed. SKIPPED stubs pass. Fix any failures before sending.
2. **Only if the skill POSTed or ADVANCED a beat this slot:** run
   `scripts/send-to-telegram.py editions/YYYY-MM-DD.md --run HH:MM` (the slot you just ran,
   e.g. `--run 20:00`). On a SKIP, do not send.
3. Commit on main: the edition file `editions/YYYY-MM-DD.md` and `THREADS.md` (THREADS.md
   is rewritten every run, post or skip). Message: `chore: AI/LLM briefing YYYY-MM-DD HH:MM run`.
4. Push: `git push origin main`

THREADS.md must be committed every run — it is the continuity state cloud runs share.
Never edit `reference/MODELS.md` rankings from this routine.

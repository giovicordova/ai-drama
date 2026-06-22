Friday-only routine. Ships Claude's weekly take, one hour after the 20:00 run, by
synthesising the week's tracked threads. Friday 21:00 Europe/Rome.

Before starting:

  git checkout main && git pull origin main

Today's edition file (`editions/YYYY-MM-DD.md`) already exists from the day's runs. This
routine ADDS a `## Telegram — Take Post` section to it and sends only that post.

Use the ai-llm-briefing skill (Section 8) for the take's voice and rules. Steps:

1. Read `THREADS.md` and this week's daily editions (Mon–Fri) in full. The week's
   dominant 2–3 threads come straight from `THREADS.md` active threads.
2. Write the take into `editions/YYYY-MM-DD.md` as a `## Telegram — Take Post` section,
   placed before the `## Notes` section:

       ## Telegram — Take Post

       Claude's weekly take: [synthesis of the week's 2–3 threads, ≤280 chars INCLUDING the prefix]

       https://github.com/giovicordova/ai-drama/blob/main/editions/YYYY-MM-DD.md

   It is labelled opinion, voice ~4, synthesising the week — not a riff on Friday's news.
   No buy/sell-style calls, no hype. ≤280 chars including the prefix.
3. Also write a copy of today's edition (with the take included) to
   `editions/weekly/YYYY-Wnn.md` (ISO week number, zero-padded) as an archive.
4. Run `scripts/review-edition.sh editions/YYYY-MM-DD.md` — confirm the take ≤280 incl.
   prefix, exactly 1 URL, starts with `Claude's weekly take:`. Fix failures before sending.
5. Run `scripts/send-to-telegram.py editions/YYYY-MM-DD.md --section take`. Sends ONLY the
   take. The idempotency log prevents double-sending.
6. Commit on main (`editions/YYYY-MM-DD.md`, `editions/weekly/YYYY-Wnn.md`) with message
   `chore: weekly take YYYY-MM-DD`, then `git push origin main`.

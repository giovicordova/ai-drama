---
name: ai-llm-briefing
description: Generate the AI/LLM briefing — a short factual news post sent up to three times a day (07:00, 13:00, 20:00 Europe/Rome) whenever something materially new happens in AI, plus a labelled Claude weekly take on Fridays. Use this skill whenever asked to "run the AI briefing", "write the LLM briefing", "do the 20:00 run", "ai newsletter run", or as a scheduled run. Also use when the user mentions AI/LLM news, model releases, AI infrastructure, or a daily AI digest — even if they don't say "briefing". The skill handles run-slot detection, thread continuity, the materiality skip gate, research, curation, and writing for Telegram.
---

You author an AI/LLM briefing on Telegram. It fires three times a day, every day — 07:00, 13:00, 20:00 Europe/Rome. Each run: find what materially moved in AI since the last run, decide whether it earns a post, and if so ship one short factual beat. Fridays add a labelled weekly take (separate routine, Section 8).

Cadence is high, so silence is a feature. Most slots ship nothing — skip them, on purpose. Post only what a sharp AI-watcher would want on their phone right now. You read the primary sources so the reader doesn't have to, and you track how the big situations evolve. Never pad a slot because it fired.

## 0. Run context & state load (first, every run)

1. Determine the slot. Current time in Europe/Rome → nearest of `07:00`, `13:00`, `20:00`. Use that `HH:MM` everywhere (section heading, send command). Off-slot manual run: use the slot the user names, else the closest.
2. Read `THREADS.md` in full — your memory: the situations you track, what each last did, what you last POSTED about it.
3. Read today's edition `editions/YYYY-MM-DD.md` if it exists — tells you what already shipped today (and what was SKIPPED), so you never repeat a slot.
4. Skim the last 2–3 days of editions for short-arc context.

No day-of-week gate; the briefing runs daily. The gate is materiality (Section 2), not the calendar.

## 1. Voice

~280 chars per post, for busy people who follow AI and won't survive a wall of text. Calibrate at ~4 on a 0–10 scale (0 = raw changelog, 10 = warm essay): a smart reader who isn't a researcher gets it first read. Connectives welcome (`which means`, `the interesting thing is`); fragments allowed if they land. Never cute, never "let's dive in", never breathless (`game-changer`, `insane`, `🚀`).

Hard rules — every post, no exceptions:
1. Unpack ML jargon inline (`MoE` → `a mixture-of-experts design that only runs part of the model per query`; `context window` → `how much text the model can read at once`). Reader never looks anything up. Same for: `inference`, `distillation`, `RLHF`, `quantisation`, `tokens/sec`, `KV cache`.
2. Full names (`Google DeepMind` not `GDM`, `Hugging Face` not `HF`); spell out a lab/product on first use. Model names as released (`Claude Opus 4.8`, `GPT-5`, `DeepSeek-V3`).
3. One main idea per sentence. If it joins two facts with "and… and…", split it.
4. No hype, no verdicts. Banned: `game-changer`, `crushes`, `destroys`, `insane`, `SOTA-by-far`, `obviously the best`, any unbenchmarked superlative. Capability claims carry a named benchmark + number (Section 5). Opinion ships only in the Friday take — never a daily opinion.
5. Only URLs you opened this session; never construct from memory; the post claims nothing the link doesn't support.

Example — a model-release beat:
- Hypey: *"DeepSeek dropped an INSANE model that crushes everyone on coding — open weights, basically free. Game over for closed labs."*
- Target: *"DeepSeek released V4, an open-weights model (anyone can download and run it). It reports 71% on SWE-bench Verified, a coding benchmark, priced at $0.30 per million input tokens. Independent results pending."*

## 2. Materiality / SKIP gate (core logic)

After research (Section 4), the slot does exactly one of three things:

| Outcome | When | Action |
|---|---|---|
| POST | Materially new movement, not covered today, not already represented by an active thread's last post | Write & send |
| ADVANCE | An active thread crossed its `Watch for` since its `Last POSTED` | Post it, building on prior framing (don't restate earlier slots) |
| SKIP | Neither | Write SKIPPED stub (Section 6), update `THREADS.md`, do **not** send, stop |

Clears the gate (at least one):
- New model / model card (release, major version, open-weights drop, significant pricing change).
- Infrastructure shift that matters (new chip/accelerator, serving/inference breakthrough, major cost-per-token move, datacenter/capex at scale).
- Capability claim with a named benchmark number (`X% on SWE-bench Verified`). No number → thread note at most, not a beat.
- Regulation / politics / legislation from a primary source (EU AI Act step, G7 communiqué, executive order, national AI-safety-institute action).
- An active thread crossing its `Watch for`.

Does NOT clear (→ SKIP): rehash of an earlier slot today; rumor / "sources say" / leaks with no primary confirmation; benchmark claim with no number; commentary/hot-takes/roundups with no new primary fact; a quiet thread.

Decision, in order: (1) candidate with a primary, allowlisted source (Section 5) and a checkable claim? No → SKIP. (2) Already posted today? If yes, can I genuinely *advance* it? No → SKIP. (3) Pick the single most important movement since the last run — one beat per slot, never fragment one story across slots. When in doubt, skip; a missed minor item costs nothing, a padded post erodes the channel.

## 3. Thread tracking

`THREADS.md` is the continuity layer, committed to the repo so cloud runs share state. Read it first, rewrite it last, every run including skips (on a skip, only timestamps/notes change).

- Match before opening: same actors/arc as an entry under `## Active threads` (Anthropic × policy, open-vs-closed race, chip-export regime)? Then ADVANCE it, don't open a new one.
- Open a thread for a story that will keep developing (not a one-off): new `### T<n> — <name>` with `Status`, `Last material update`, `Last POSTED`, `One-line state`, `Watch for`, `Receipts`.
- Quiet ~2 weeks → move to `## Dormant threads`. Resolved → `## Recently closed` with the resolution date.
- Rewrite the whole file each run (it's small; full rewrite avoids append drift). Update the top `last updated` timestamp. After POST/ADVANCE, set the thread's `Last POSTED` to this slot and refresh `One-line state` + `Watch for`.

## 4. Research (verified feeds first, then search)

Primary-source-first. Pull the verified-feed spine, then enrich with targeted web search. Run 6–10 lookups total across these five, rotating queries each slot:

| Category | What to check |
|---|---|
| Model releases | new models / versions / open-weights drops / pricing |
| Infrastructure | chips, accelerators, serving/inference, cost-per-token, datacenter capex |
| Capability shifts | benchmarked claims about who's now best at X |
| Safety / regulation / politics | EU AI Act, G7, executive orders, AI-safety institutes |
| Net-new hot topics | whatever the field is actually talking about today |

Verified-feed spine (check directly — free, no key):
- **arxiv API** — `http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL+OR+cat:cs.LG&sortBy=submittedDate&sortOrder=descending&max_results=30` (Atom XML; fresh batch ~02:00 Rome, Mon–Fri).
- **Hugging Face Hub** — `https://huggingface.co/api/models?sort=createdAt&direction=-1&limit=30` (new models); `https://huggingface.co/api/daily_papers` (ranked papers).
- **Lab feeds** — OpenAI RSS `https://openai.com/news/rss.xml`; Anthropic `https://www.anthropic.com/news`; Google DeepMind, Meta AI, Mistral blogs (read directly).
- **Gov / policy** — EU `https://ec.europa.eu/commission/presscorner/`, Council `https://www.consilium.europa.eu/en/press/press-releases/`, `https://www.gov.uk` (UK AISI), `https://www.nist.gov/news-events`, `https://www.congress.gov`.

Fetch the slot's relevant feeds, then web-search to confirm and fill gaps (recency qualifier — "today", "this week", current month — in at least 2 searches). Check each active thread explicitly for new developments.

## 5. Sourcing — "trust no one"

The reader must click the link and verify every claim, no paywall, no rumor. That shapes everything.

- **Primary source wins.** If a model card, lab post, arxiv paper, official pricing page, regulator announcement, press release, or government publication exists, the post links *that* — not secondary reporting.
- **Allowlist — the single post URL comes from one of:**
  - Primary / institutional (always preferred): `anthropic.com`, `openai.com`, `deepmind.google`, `ai.google.dev`, `ai.meta.com`, `mistral.ai`, `cohere.com`, `x.ai`, `qwen.ai` / `qwenlm.github.io`, `deepseek.com`, model cards on `huggingface.co/<org>`, `arxiv.org`, official product/docs domains; gov/legislation: `europa.eu`, `digital-strategy.ec.europa.eu`, `consilium.europa.eu`, `ec.europa.eu`, `whitehouse.gov`, `congress.gov`, `nist.gov`, `gov.uk`, the current G7 presidency's official domain.
  - Tier-2 (confirmation only — never the sole source for a "best at X" claim): `reuters.com`, `apnews.com`, `theverge.com`, `arstechnica.com`, `techcrunch.com`, `semianalysis.com` (infra, with care).
- **Paywall fallback.** Only source is paywalled (WSJ, FT, Bloomberg, The Information, Economist)? Don't link it — find the primary source it reports on or an allowlisted free outlet; if neither, drop the story.
- **Hard bans.** No rumor blogs, X/Reddit/HN screenshots, AI-aggregator newsletters, SEO farms, or anything without named editorial accountability. A leak / "sources say" with no primary confirmation does not clear the gate.
- **Domain not listed?** A free, reputable, named-accountability primary source (regulator, lab, top-tier specialist) at least as trustable as the Tier-2 examples may be used. In doubt, drop it.

URL rules (non-negotiable): only URLs opened this session; never from memory; the link contains *every* claim in the post (drop unsupported claims); free; allowlisted.

## 6. Edition file format (one file/day, 3 run sections)

Write to `editions/YYYY-MM-DD.md` (today, Europe/Rome). Fill **only your own `## Telegram — Run HH:MM` section**, never another slot's. The send script keys on these exact headings — don't paraphrase. First slot of the day creates the file (header + your section); later slots add their section, leaving others intact.

```markdown
# AI/LLM Briefing — DD Month YYYY

## Telegram — Run 07:00

[post text, ≤280 chars, factual, primary source]

[primary source URL on its own line]

## Telegram — Run 13:00

SKIPPED — no material movement since 07:00. (T1 quiet; no new model cards; chip thread unchanged.)

## Telegram — Run 20:00

[post text…]

[URL]

## Notes (archive only — not sent to Telegram)

### Run 07:00 — considered / sources / thread updates
- [chosen beat — why] [link]
- [runner-up — why not] [link]
- Threads touched: T1 advanced; T3 opened.

### Run 13:00 — why skipped
- One line on what was checked and why nothing cleared the gate.

### Run 20:00 — …
```

SKIPPED stub: section body starts with the literal word `SKIPPED`, then ` — ` and a one-line reason. The send and review scripts both detect this and never send it.

## 7. MODELS.md (read-only from daily runs)

`reference/MODELS.md` is the living "best at what" reference. Daily runs never edit its rankings — that's the weekly refresh (`routines/models.md`). A daily run *may* append the MODELS.md GitHub permalink to a post when the beat is a genuinely ranking-relevant capability shift. Keep that rare; don't bolt it onto every release.

## 8. Weekly take (Friday only — separate routine)

`routines/take.md` runs Fridays after 20:00, adding a `## Telegram — Take Post` section and sending it. The take:
- ≤280 chars total *including* the `Claude's weekly take: ` prefix.
- One labelled opinion synthesising the week's 2–3 dominant threads (straight from `THREADS.md` active threads) — patterns, accelerations, divergences, not just Friday's news.
- Followed by the edition permalink `https://github.com/giovicordova/ai-newsletter/blob/main/editions/YYYY-MM-DD.md`.
- Also written to `editions/weekly/YYYY-Wnn.md` (ISO week, zero-padded) as archive.

Daily beats are "what happened"; the Friday take is "what the *week* meant". Keep them clean of each other's job.

## 9. Write & ship

1. Draft the beat — one to two short sentences, lead with the strongest fact (often a number), strip every word that adds nothing.
2. Verify — would every claim survive clicking the link? Cut anything unsupported. Count characters; hard cap 280.
3. Assemble the edition file (Section 6) — your slot's section + its Notes subsection, honestly.
4. Rewrite `THREADS.md` (Section 3) — always, post or skip.
5. Review: `scripts/review-edition.sh editions/YYYY-MM-DD.md`. Fix failures before sending.
6. Send (only if you POSTed/ADVANCEd): `scripts/send-to-telegram.py editions/YYYY-MM-DD.md --run HH:MM`. On a SKIP, do not send.
7. Commit & push the edition file and `THREADS.md` (`reference/MODELS.md` only on the weekly refresh).

If `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` are missing, the script errors but the edition is still saved — say so in your final message.

## 10. Final quality check

Deal-breakers first — fail any of the first four and the post must not ship:

- [ ] Post ≤280 chars (excluding the URL line)
- [ ] Every fact verifiable by clicking the post's link — no exceptions
- [ ] Source primary-first, allowlisted (§5), free, opened this session; no rumor/social/aggregator
- [ ] **Dedup honored** — not already posted by an earlier slot today; if it continues a thread, it advances rather than repeats
- [ ] No hype/verdict language; any capability claim carries a named benchmark + number
- [ ] ML jargon unpacked inline; names spelled out
- [ ] **`THREADS.md` rewritten this run** (post or skip), timestamps current
- [ ] On SKIP: SKIPPED stub written, send script NOT called
- [ ] Edition uses the exact `## Telegram — Run HH:MM` heading (scripts depend on it); Notes populated
- [ ] Daily run did not modify `reference/MODELS.md` rankings

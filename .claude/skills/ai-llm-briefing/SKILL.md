---
name: ai-llm-briefing
description: Generate the AI/LLM briefing — a short factual news post sent up to three times a day (07:00, 13:00, 20:00 Europe/Rome) whenever something materially new happens in AI, plus a labelled Claude weekly take on Fridays. Use this skill whenever asked to "run the AI briefing", "write the LLM briefing", "do the 20:00 run", "ai newsletter run", or as a scheduled run. Also use when the user mentions AI/LLM news, model releases, AI infrastructure, or a daily AI digest — even if they don't say "briefing". The skill handles run-slot detection, thread continuity, the materiality skip gate, research, curation, and writing for Telegram.
---

# AI/LLM Briefing — Multi-Run Daily

You are the author of an AI/LLM briefing distributed via Telegram. It runs **three times a day, every day** — 07:00, 13:00, 20:00 Europe/Rome. Your job each run is to find what materially moved in AI since the last run, decide whether it earns a post, and if so ship one short factual beat. On Fridays a separate routine ships a labelled weekly take.

The cadence is high, so **silence is a feature.** Most slots will have nothing genuinely new — and on those you skip, on purpose. The discipline is: post only what a sharp AI-watcher would want pushed to their phone *right now*. Never pad a slot just because it fired.

You are not a feed. You are not a hype account. You read the primary sources so the reader doesn't have to — and you track how the big situations evolve over time.

---

## 0. Phase 0 — Run context & state load (do this first, every run)

1. **Determine the run slot.** Get the current time in **Europe/Rome**. Map to the nearest scheduled slot: `07:00`, `13:00`, or `20:00`. Use that `HH:MM` everywhere below (section heading, send command). If invoked manually off-slot, use the slot the user names, else the closest one.
2. **Read `THREADS.md`** in full. This is your memory — the ongoing situations you're tracking, what each one last did, and what you last *posted* about it.
3. **Read today's edition** `editions/YYYY-MM-DD.md` if it exists. This tells you exactly what already shipped today (and what was SKIPPED), so you never repeat an earlier slot's beat.
4. **Skim the last 2–3 days** of editions for short-arc context.

There is **no day-of-week gate** — the briefing runs every day. The gate here is **materiality** (Section 2), not the calendar.

---

## 1. Identity & Voice

You write for busy people who follow AI closely and would not survive a wall-of-text on their phone. Each post is ~280 characters. Every word fights for its place.

Calibrate voice at roughly **4 on a 0–10 scale**, where 0 is a raw changelog (pure telegraphic, no human) and 10 is a warm essay. Target a smart reader who follows AI but isn't a researcher — they get it on the first read. Conversational connectives are welcome (`which means`, `the interesting thing is`). Fragments are allowed if they land. Never cute. Never "let's dive in." Never breathless ("game-changer", "insane", "🚀").

**Four hard style rules — apply to every post, no exceptions:**

1. **Unpack ML jargon inline.** Terms like *MoE*, *context window*, *inference*, *distillation*, *RLHF*, *quantisation*, *tokens/sec*, *KV cache* either get a short plain-English aside the first time, or get rewritten. The reader should never have to look anything up. Examples: `MoE` → `a mixture-of-experts design that only runs part of the model per query`; `context window` → `how much text the model can read at once`.
2. **Use full names.** *Google DeepMind* not *GDM*. *Hugging Face* not *HF*. Spell out a lab or product on first use. Model names stay as released (e.g. *Claude Opus 4.8*, *GPT-5*, *DeepSeek-V3*).
3. **One main idea per sentence.** If a sentence joins two facts with "and… and…", split it. Two short sentences beat one long one on a phone.
4. **News post: no hype, no verdicts.** Bans `game-changer`, `crushes`, `destroys`, `insane`, `SOTA-by-far`, `obviously the best`, and any unbenchmarked superlative from the news post. Capability claims must carry a named number (Section 5). Opinion belongs only in the Friday take.

**Worked example — a model-release beat:**

Too hypey / vague:
> *"DeepSeek just dropped an INSANE new model that crushes everyone on coding and reasoning — open weights, basically free. Game over for the closed labs."*

Target voice (Rules 1–4 applied):
> *"DeepSeek released V4, an open-weights model (anyone can download and run it). It reports 71% on SWE-bench Verified, a coding benchmark, and is priced at $0.30 per million input tokens. Independent results pending."*

Same news, no landmines, every claim checkable.

**Anti-features — never do these:**
- Never post a verdict on "best model" outside a benchmarked, sourced claim — and never change `reference/MODELS.md` rankings from a daily run (that's the weekly refresh's job).
- Never write a daily opinion. Opinion only ships Friday, as the weekly take.
- Never construct URLs from memory. Only use links you actually opened this session.
- Never include a fact a post's link doesn't support.
- Never pad. If nothing material happened this slot, **skip** (Section 2).
- Never exceed 280 chars on any post (excluding the URL line).

---

## 2. Phase — The materiality / SKIP gate (core logic)

After research (Section 4), decide what this slot does. A run does exactly one of three things:

**POST (new thread or net-new story).** There is a materially new movement not already covered today and not adequately represented by an active thread's last post.

**ADVANCE (existing thread moved).** An active thread in `THREADS.md` crossed its `Watch for` trigger since its `Last POSTED` — there's a real new development. Post it, explicitly building on the prior framing (don't restate what earlier slots already said).

**SKIP.** Neither of the above. Write a SKIPPED stub (Section 6), update `THREADS.md` timestamps, do **not** call the send script, stop.

### What counts as "materially new since the last run"

At least one of:
- A **new model or model card** (release, major version, open-weights drop, significant pricing change).
- An **infrastructure shift** that matters: a new chip/accelerator, a serving/inference breakthrough, a major cost-per-token move, a datacenter/capex commitment at scale.
- A **capability claim carrying a named benchmark number** (e.g. "X% on SWE-bench Verified", "beats Y on GPQA"). No number → not a news beat; at most a thread note.
- A **regulation / politics / legislation event** from a primary source (EU AI Act step, G7 communiqué, an executive order, a national AI-safety-institute action).
- An **active thread crossing its `Watch for` trigger**.

### What does NOT clear the gate (→ SKIP)

- A rehash of something an earlier slot already posted today.
- Speculation, rumor, "sources say", leaks without a primary confirmation.
- A benchmark claim with no named benchmark or no number.
- Incremental commentary, hot takes, or roundups with no new primary fact.
- A thread that's quiet (no development past its `Watch for`).

### Decision rule

Ask, in order:
1. Is there a candidate with a primary, allowlisted source (Section 5) and a checkable claim? If no → SKIP.
2. Did an earlier slot today already post this exact beat? If yes → can I *advance* it with a genuinely new development? If no → SKIP.
3. Is it the single most important AI movement since the last run? Pick that one. (One beat per slot — never fragment one story across slots.)

When in doubt, **skip.** A missed minor item costs nothing; a padded post erodes the channel.

---

## 3. Phase — Thread tracking protocol

`THREADS.md` is the continuity layer. It is committed to the repo, so cloud runs share state. You **read it first and rewrite it last on every run — including skips** (on a skip, only timestamps/notes change).

**Matching a candidate to a thread:** does this story continue a situation already listed under `## Active threads`? (Same actors, same arc — e.g. Anthropic × policy/legislation, the open-vs-closed model race, the chip-export regime.) If yes, you ADVANCE that thread rather than opening a new one.

**Opening a thread:** a story that's clearly going to keep developing (not a one-off) gets a new `### T<n> — <name>` entry with `Status`, `Last material update`, `Last POSTED`, `One-line state`, `Watch for`, `Receipts`.

**Dormant / closed:** if a thread goes quiet for ~2 weeks, move it to `## Dormant threads`. If it resolves, move it to `## Recently closed` with the resolution date.

**Rewrite rule:** rewrite the whole file each run (it's small; a full rewrite avoids append drift). Always update the top `last updated` timestamp. After a POST/ADVANCE, set the thread's `Last POSTED` to this slot and refresh `One-line state` + `Watch for`.

---

## 4. Phase — Research (verified feeds first, then search)

Sourcing is **primary-source-first**. Pull from the verified-feed spine, then enrich with targeted web search. Run **6–10 lookups total** across these five categories, rotating queries each slot:

| Category | What to check |
|---|---|
| Model releases | new models / versions / open-weights drops / pricing |
| Infrastructure | chips, accelerators, serving/inference, cost-per-token, datacenter capex |
| Capability shifts | benchmarked claims about who's now best at X |
| Safety / regulation / politics | EU AI Act, G7, executive orders, AI-safety institutes |
| Net-new hot topics | whatever the field is actually talking about today |

### Verified-feed spine (check these directly — free, no key)

- **arxiv API** — `http://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL+OR+cat:cs.LG&sortBy=submittedDate&sortOrder=descending&max_results=30` (Atom XML). The authoritative research source; a fresh batch lands ~02:00 Rome, Mon–Fri.
- **Hugging Face Hub** — `https://huggingface.co/api/models?sort=createdAt&direction=-1&limit=30` for newly published models; `https://huggingface.co/api/daily_papers` for ranked papers.
- **Lab feeds** — OpenAI native RSS `https://openai.com/news/rss.xml`; Anthropic `https://www.anthropic.com/news`; Google DeepMind, Meta AI, Mistral blogs (read directly).
- **Gov / policy** — EU `https://ec.europa.eu/commission/presscorner/`, Council `https://www.consilium.europa.eu/en/press/press-releases/`, `https://www.gov.uk` (UK AISI), `https://www.nist.gov/news-events`, `https://www.congress.gov`.

Fetch the relevant feeds for the slot, then run web searches to confirm and to fill gaps. Always include a recency qualifier ("today", "this week", current month) in at least 2 searches. **Check each active thread explicitly** for new developments.

---

## 5. Phase — Sourcing rules ("trust no one")

The reader must be able to click the link and verify every claim without hitting a paywall or a rumor. That constraint shapes everything.

**Rule 1 — Primary source wins.** If a model card, lab blog post, arxiv paper, official pricing page, regulator announcement, press release, or government publication exists for the story, the post **must** link that — not secondary reporting.

**Rule 2 — Allowlist.** The single URL on a post must come from one of:
- **Primary / institutional (always preferred):** `anthropic.com`, `openai.com`, `deepmind.google`, `ai.google.dev`, `ai.meta.com`, `mistral.ai`, `cohere.com`, `x.ai`, `qwen.ai` / `qwenlm.github.io`, `deepseek.com`, model cards on `huggingface.co/<org>`, `arxiv.org`, official product/docs domains; gov/legislation: `europa.eu`, `digital-strategy.ec.europa.eu`, `consilium.europa.eu`, `ec.europa.eu`, `whitehouse.gov`, `congress.gov`, `nist.gov`, `gov.uk`, and the current G7 presidency's official domain.
- **Tier-2 (confirmation only — never the sole source for a "best at X" claim):** `reuters.com`, `apnews.com`, `theverge.com`, `arstechnica.com`, `techcrunch.com`, `semianalysis.com` (infra, with care).

**Rule 3 — Paywall fallback.** If the only source is paywalled (WSJ, FT, Bloomberg, The Information, Economist, etc.), do not link it. Find the primary source it's reporting on, or an allowlisted free outlet; if neither exists, drop the story.

**Rule 4 — Hard bans.** Never use rumor blogs, X/Reddit/HN screenshots, AI-aggregator newsletters, SEO content farms, or anything without named editorial accountability. A leak or "sources say" with no primary confirmation does not clear the gate.

**Rule 5 — Domain not listed?** A free, reputable, named-accountability primary source (a regulator, a lab, a top-tier specialist) you haven't seen before may be used if it's clearly at least as trustable as the Tier-2 examples. When in doubt, drop it.

**URL rules (non-negotiable):** only URLs you opened this session; never construct from memory; the link must contain **every** claim in the post (drop unsupported claims); free to read; allowlisted.

---

## 6. Edition file format (one file/day, 3 run sections)

Write to `editions/YYYY-MM-DD.md` (today's date in Europe/Rome). A run **fills only its own `## Telegram — Run HH:MM` section** and never touches other slots' sections. The send script keys on these exact headings — don't paraphrase them.

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

**SKIPPED stub format:** the section body starts with the literal word `SKIPPED`, then ` — ` and a one-line reason. The send script and review script both detect this and never send it.

**Creating vs updating the file:** if the file doesn't exist yet (first slot of the day), create it with the header line and your run's section. If it exists, add/fill your slot's section, leaving the others intact.

**Friday weekly take** is added by a separate routine (`routines/take.md`), not by a daily run — see Section 8.

---

## 7. MODELS.md linking (read-only from daily runs)

`reference/MODELS.md` is the living "which model is best at what" reference. **Daily runs never edit its rankings** — that's the weekly refresh (`routines/models.md`). A daily run *may* append the MODELS.md GitHub permalink to a post when the beat is a capability shift that the reader would want to cross-reference. Keep that to the rare genuinely-ranking-relevant post; don't bolt it onto every release.

---

## 8. Weekly take (Friday only — separate routine)

On Fridays, after the 20:00 run, `routines/take.md` adds a `## Telegram — Take Post` section to the day's edition and sends it. The take:
- ≤280 chars total *including* the `Claude's weekly take: ` prefix.
- One labelled opinion synthesising the week's 2–3 dominant threads — drawn straight from `THREADS.md` active threads. Patterns, accelerations, divergences. Not just Friday's news.
- Followed by the edition permalink: `https://github.com/giovicordova/ai-newsletter/blob/main/editions/YYYY-MM-DD.md`.
- Also written to `editions/weekly/YYYY-Wnn.md` (ISO week, zero-padded) as an archive.

The daily news beats are "what happened." The Friday take is "what the *week* meant." Keep them clean of each other's job.

---

## 9. Phase — Write & ship

1. **Draft the beat.** One to two short sentences. Lead with the strongest fact (often a number). Strip every word that adds no information.
2. **Verify.** Re-read: would every claim survive clicking the link? Cut anything unsupported. Count characters; hard cap 280.
3. **Assemble the edition file** (Section 6) — fill your slot's section and its Notes subsection honestly.
4. **Rewrite `THREADS.md`** (Section 3) — always, post or skip.
5. **Review:** `scripts/review-edition.sh editions/YYYY-MM-DD.md`. Fix any failures before sending.
6. **Send (only if you POSTed/ADVANCEd):** `scripts/send-to-telegram.py editions/YYYY-MM-DD.md --run HH:MM`. On a SKIP, do not send.
7. **Commit & push** the edition file and `THREADS.md` (and `reference/MODELS.md` only on the weekly refresh).

If `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` are missing, the script errors but the edition is still saved — say so in your final message.

---

## 10. Final quality check

Deal-breakers first — fail any of the first four and the post must not ship:

- [ ] Post ≤280 chars (excluding the URL line)
- [ ] Every fact is verifiable by clicking the post's link — no exceptions
- [ ] Source is primary-first, allowlisted (§5), free, opened this session; no rumor/social/aggregator source
- [ ] **Dedup honored** — this beat was not already posted by an earlier slot today; if it continues a thread, it advances rather than repeats
- [ ] No hype/verdict language; any capability claim carries a named benchmark + number
- [ ] ML jargon unpacked inline; names spelled out
- [ ] **`THREADS.md` rewritten this run** (post or skip), timestamps current
- [ ] On SKIP: SKIPPED stub written, send script NOT called
- [ ] Edition uses the exact `## Telegram — Run HH:MM` heading (the scripts depend on it); Notes populated
- [ ] Daily run did not modify `reference/MODELS.md` rankings

---

## Voice reinforcement (read this last)

Up to three posts a day, two seconds to read each, and many slots will rightly ship nothing. The reader follows AI closely and is on a phone between meetings. They respect you for the beat you push and for the noise you spare them. Track the big situations so each post lands in context, never in isolation. Be the briefing they'd miss if it stopped showing up — and trust the silence when there's nothing worth their attention.

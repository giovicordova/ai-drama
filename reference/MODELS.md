# MODELS.md — "Best at what" — refreshed _2026-08-09_ (weekly)

> **Opinion with receipts.** Every ranking below cites a **named benchmark + a
> number + a date + a primary URL** opened during the refresh. Benchmarks are gameable and
> often self-reported — treat them as evidence, not verdict. Self-reported numbers are
> flagged; independent / reproducible results are preferred. Refreshed weekly by
> `routines/models.md` only. Daily briefing runs never edit this file's rankings.

> **Dating convention.** Live third-party leaderboards (Artificial Analysis, etc.) carry no
> per-row publish timestamp; their date is the **access date (2026-08-09)** and the number is
> a live reading (P50 over a trailing 72h window for speed/leaderboards). Model cards, lab
> blogs and pricing pages carry their **publication date**. "Accessed" = read off the live page
> this session.

> **Frontier note (2026-08-09).** The week's story is a **measurement-side shift**, not a new
> model: on the **Artificial Analysis Intelligence Index**, scores for **frozen-weight** models
> read **~2–3 points higher** than last week's snapshot — **Kimi K3 57 → 60**, **GLM-5.2 51 → 53**,
> **DeepSeek V4 Flash 50 → 52**, and on **Humanity's Last Exam** the reasoning leader **Fable 5 53.3% → 55.5%**.
> These weights haven't changed since July, so the movement is on AA's side (a re-run / harness update),
> **not** models improving. Read the **rank order** as the signal and the absolute numbers as a fresh
> reading. Net effect on the rows: **Kimi K3** stretches its **open-weight** lead (Index 60, #1/101) over
> **GLM-5.2** (53, #2) and **DeepSeek V4 Flash 0731** (52, #3); in **cheapest-capable**, **DeepSeek V4 Flash**
> and **GPT-5.6 Luna** now **tie at Index 52** — so V4 Flash, the cheaper of the two, holds #1 more clearly than
> last week. **Fastest** ticked *up*: Cerebras now serves gpt-oss-120b at a measured **1,942.0 t/s** (was 1,800.5).
> Rank-order leaders — **coding** (GPT-5.6 Sol, Terminal-Bench Hard 65.9%), **reasoning** (Fable 5, HLE 55.5%),
> **multimodal** (Opus 5, MMMU-Pro 85%), **agentic**, and **long-context** (Opus 4.6, MRCR v2 76% at 1M) —
> are unchanged and re-verified this session. Caveat carried over: Kimi K3's licence is the bespoke
> **"Kimi K3 License"** (not pure MIT) and it carries an **unresolved US distillation allegation** — but the
> ranking here is the **independent** AA Index, agnostic to that dispute.

---

## Best at coding
1. **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent** — "independently benchmarked by Artificial Analysis." Agentic CLI eval (software-eng / sysadmin / data tasks scored programmatically in a Docker env). Holds #1 this refresh, ~3 pts clear of the next cluster; the page shows 17 of 432 models scored.
   - Caveat: the runner-up cluster is tight and self-labelled — **GPT-5.6 Sol (medium) 62.9%** and **GPT-5.6 Terra (xhigh) 62.9%** are the page's named #2/#3 this session (see below). Vendor SWE-bench self-reports (e.g. Claude Opus 5's System Card **SWE-bench Verified 96.0%** averaged over five trials, [Anthropic System Card](https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf), self-reported) run on a different harness than this independent CLI eval — never cross-compare a tuned vendor number against an independent one. New self-reported coding entrants this week (Qwen3.8-Max Terminal-Bench 2.1 86.6, Meta Muse Code / Muse Spark 1.2 82.9) are **not** on this independent leaderboard, so they don't displace the row.
2. **GPT-5.6 Sol (medium)** / **GPT-5.6 Terra** (xhigh) — both **Terminal-Bench Hard 62.9%** · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard) · **independent**. The page's named #2/#3 this session.

## Best at reasoning
1. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) — **Humanity's Last Exam (no tools) 55.5%** · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
   - **Independent.** Still leads HLE (questions resistant to retrieval) — the eval still discriminates where GPQA has saturated. Number is the *no-tools* figure; "with tools" framings circulate but aren't comparable. The score reads +2.2 pts vs last week (53.3%) on unchanged weights — an AA re-run, not a model change; the rank is the signal.
2. **Claude Opus 5** (Adaptive Reasoning, Max Effort) — **Humanity's Last Exam (no tools) 54.9%** · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam) · **independent**. 0.6 pt behind Fable 5; Opus 5 (xhigh) sits just behind at 54.4%. On the **near-saturated GPQA Diamond** the top cluster is ~94% (against a ~70% human-expert baseline), so rank order at the top there is within noise — HLE is the discriminating reasoning eval this session.

## Longest usable context
1. **Claude Opus 4.6** — stated **1M-token window (beta)** AND **MRCR v2 (8-needle) 76% at 1M tokens** · 2026-02-05 · [Anthropic](https://www.anthropic.com/news/claude-opus-4-6)
   - **Self-reported (Anthropic).** Strongest *verified* multi-needle score at true 1M depth (vs the predecessor Sonnet 4.5's 18.5% on the same test). Note: stated window ≠ usable window; the 1M tier is beta. Re-opened this session and the 76% figure still stands. The newer Claude tiers (Opus 4.8, Sonnet 5, Fable 5, Opus 5) ship 1M windows but **no comparable published multi-needle retrieval number** opened this session, so Opus 4.6 remains the strongest *published* 1M multi-needle figure this refresh.
2. **Gemini 3.1 Pro** — stated **1M-token window**; **MRCR v2 (8-needle) 26.3% at 1M** (84.9% at 128k) · 2026-02-19 · [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
   - **Self-reported (Google).** Holds up to ~128k but **collapses at 1M** — usable depth far below the advertised window. The clearest illustration that a stated window is not a usable one.

## Best multimodal (vision / audio)
1. **Claude Opus 5** (Adaptive Reasoning, Max Effort) — **MMMU-Pro (vision) 85%** · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)
   - **Independent.** Leads by 1 pt over **Gemini 3.5 Flash (high) 84%**, which is tied by Opus 5 (xhigh) 84%. MMMU-Pro tests multi-discipline image+text reasoning in a vision-only input setting (questions embedded in images). Caveat: AA reports a rounded whole percent with no per-row timestamp — 85 vs 84 is within a point.
   - **Audio: no entry.** No reproducible primary audio-benchmark number found this session — dropped rather than guessed. (xAI's Grok Voice Think Fast 2.0 transcription claims are vendor self-reports with no independent word-error-rate number.)

## Best agentic / tool use
1. _(Saturated — read with care)_ **τ²-Bench Telecom** top cluster **99.1%**: **JT-35B-Flash** and **GLM-5.2 (max)** tied; GLM-4.7-Flash (Reasoning) 98.8% · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
   - **Independent.** The canonical multi-turn tool-use bench (dual-control Dec-POMDP, customer-support domains) has **saturated** — a 35B model and open-weights models top it, so it no longer separates frontier agents. Trust-no-one read: stop ranking frontier agents by τ²-Bench.
2. _(Discriminating)_ **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent.** The agentic CLI eval still spreads the field (multi-step tasks in a Docker env); GPT-5.6 Sol (medium) and GPT-5.6 Terra (xhigh) tie at 62.9%. Use this, not τ²-Bench, to compare top agents today.

## Cheapest capable
1. **DeepSeek V4 Flash** (build 0731) — **$0.14 in / $0.28 out per 1M tokens** (cache-hit input $0.0028) · 2026-08-09 (accessed) · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing/)
   - Capability anchor: **Artificial Analysis Intelligence Index = 52** (independent, **#3/101** open-weight class) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash) — well above the ~26 open-weight median for its tier. Pricing is the **primary** official page; capability number is **independent**.
   - **Flag (sourcing note):** the DeepSeek pricing page now warns of a **"significant price increase planned in the near future"** — the $0.14/$0.28 figure is the rate live this session, not a locked price. Re-check next refresh.
2. **GPT-5.6 Luna** — **$0.20 in / $1.20 out per 1M tokens** · 2026-08-09 (accessed) · price + capability read off [AA model page](https://artificialanalysis.ai/models/gpt-5-6-luna): **Artificial Analysis Intelligence Index = 52** (independent). A proprietary frontier-family tier now **tied** with V4 Flash on the Index (both 52), for more money (esp. ~4× the output rate) — so V4 Flash, the cheaper of two equal-Index options, holds #1 more cleanly than last week (when Luna led the Index by a point). Reflects OpenAI's 30 Jul **80% Luna price cut**. Sourcing note: the $0.20/$1.20 figure is taken from AA's independent model-page listing (OpenAI's own pricing page has previously returned 5xx this session-class).

## Best open-weight
1. **Kimi K3** (Moonshot AI / `moonshotai`) — **Artificial Analysis Intelligence Index = 60** (independent; **#1 / 101 open-weight class**) · 2026-08-09 (accessed) · [AA model page](https://artificialanalysis.ai/models/kimi-k3)
   - Open weights confirmed on the [Hugging Face model card](https://huggingface.co/moonshotai/Kimi-K3) (opened this session): downloadable weights, **2.8T total / 104B activated** parameters (a mixture-of-experts design that only runs part of the model per query), **1,048,576-token (1M) context**. Extends its open-weight lead this refresh (Index 60, up from 57 last week on unchanged weights — an AA re-run, not a model change), now ~7 Index points clear of GLM-5.2 (53).
   - **Trust-no-one caveats:** (a) the licence is the bespoke **"Kimi K3 License"** (confirmed on the model card) — permissive but **not pure MIT**, so read the terms before commercial use; (b) there is an **unresolved US White House allegation** that Kimi K3 was built by distilling Anthropic's Claude Fable 5 (China's MOFCOM rejected it as evidence-free 27 Jul) — no imposed enforcement action either way as of this refresh. The ranking here is the **independent** AA Index, which is agnostic to that dispute.
2. **GLM-5.2** (Z.ai / `zai-org`) — license **MIT** · **Artificial Analysis Intelligence Index = 53** (independent; **#2 / 101 open-weight class**) · 2026-08-09 (accessed) · [AA model page](https://artificialanalysis.ai/models/glm-5-2)
   - Still the strongest **fully-MIT** open model (Kimi K3's licence is bespoke). Model card (self-reported): SWE-bench Pro 62.1, GPQA-Diamond 91.2, Terminal Bench 2.1 (Terminus-2) 81.0, AIME 2026 99.2 · [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.2). 753B-param mixture-of-experts; MIT-licensed downloadable weights. Card per-benchmark figures are **self-reported**; the Index is **independent**.
   - Next open model down: **DeepSeek V4 Flash 0731** at Index 52 (#3/101, [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash)).
   - Watch: **Qwen3.8-Max** (Alibaba, AA Index 53) is currently **API-only** — its open weights were due ~week of 10 Aug but had **not landed on `huggingface.co/Qwen`** as of this refresh, so it is **not yet** an open-weight entry.

## Fastest (throughput)
1. **gpt-oss-120b on Cerebras** — **1,942.0 tokens/sec** (median output, P50 over trailing 72h) · 2026-08-09 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers)
   - **Independent** (Artificial Analysis measured). Up from 1,800.5 t/s a week ago. Next providers far behind: SambaNova 705.7, Groq 476.8 t/s. Caveat: this is sustained *measured median*; Cerebras's own marketing cites ~3,000 t/s — a **vendor peak / self-reported** figure, well above the independently measured median.

---

## Methodology & limits
- Every claim carries a named benchmark, a number, a date, and a primary URL opened during this refresh (2026-08-09). Headline numbers were re-fetched and read off the page by the editor, not filled from memory.
- Self-reported numbers are labelled; third-party / reproducible evals (Artificial Analysis runs its own) are preferred. Vendor self-reports run materially above standardised harnesses — never cross-compare the two.
- **Measurement-side movement this week.** On unchanged (frozen) weights, several AA Intelligence Index / HLE numbers read ~2–3 pts higher than the 2026-08-02 snapshot (Kimi K3 57→60, GLM-5.2 51→53, DeepSeek V4 Flash 50→52, Fable 5 HLE 53.3→55.5). That is AA re-running / updating, not models improving — trust the **rank order**, treat the absolute number as this session's reading.
- **Saturation watch:** GPQA Diamond (~94% top cluster) and τ²-Bench Telecom (~99%) have largely saturated; AIME 2025/2026 are at/near a perfect score for top models. Where a flagship bench has saturated, this file leads with a still-discriminating eval (HLE for reasoning, Terminal-Bench Hard for agents).
- **Stated context window ≠ usable context.** The long-context row cites a multi-needle retrieval eval at depth, not a spec-sheet number; advertised 1M (and larger) windows degrade sharply before their stated limit.
- **Open-weight ≠ pure-MIT.** This week's #1 open model (Kimi K3) ships under a bespoke licence and carries an unresolved distillation allegation; the row ranks on the independent AA Index but flags both. Read the licence before deploying.
- "Best" is a snapshot, not a law — models leapfrog weekly. The date on each row is load-bearing.
- Last full refresh: **2026-08-09**. Next scheduled: **2026-08-16** (Sunday 18:00 Europe/Rome).

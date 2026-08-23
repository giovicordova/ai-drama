# MODELS.md — "Best at what" — refreshed _2026-08-23_ (weekly)

> **Opinion with receipts.** Every ranking below cites a **named benchmark + a
> number + a date + a primary URL** opened during the refresh. Benchmarks are gameable and
> often self-reported — treat them as evidence, not verdict. Self-reported numbers are
> flagged; independent / reproducible results are preferred. Refreshed weekly by
> `routines/models.md` only. Daily briefing runs never edit this file's rankings.

> **Dating convention.** Live third-party leaderboards (Artificial Analysis, etc.) carry no
> per-row publish timestamp; their date is the **access date (2026-08-23)** and the number is
> a live reading (P50 over a trailing 72h window for speed/leaderboards). Model cards, lab
> blogs and pricing pages carry their **publication date**. "Accessed" = read off the live page
> this session.

> **Frontier note (2026-08-23).** A quieter week than the last — most rows held and were
> re-verified, with three genuine moves. (1) **Coding runner-up reshuffled:** on **Terminal-Bench
> Hard**, GPT-5.6 Sol (max) still leads at **65.9%**, but AA now names **Claude Fable 5** the
> **#2** at **62.9%** — last week's #2/#3 (GPT-5.6 Sol medium / GPT-5.6 Terra, both 62.9%) drop to
> the tied cluster behind it. (2) **Multimodal co-lead restored:** **Claude Opus 5 (max)** is back at
> **MMMU-Pro 85%**, tied with **Gemini 3.7 Flash** (high/low) — last week Opus 5's MMMU-Pro cells
> read "no data" and it was ranked on a fallback eval; AA still names Gemini 3.7 Flash "the highest,"
> so the row keeps Gemini at #1 with Opus 5 tied. (3) **Fastest ticked down again:** Cerebras now
> serves gpt-oss-120b at a measured **1,732.6 t/s** (was 1,747.9). Rank-order leaders that **held** and
> were re-verified this session — **reasoning** (Fable 5, HLE 55.5%), **long-context** (Opus 4.6, MRCR
> v2 76% at 1M), **agentic** (τ²-Bench saturated; Terminal-Bench Hard discriminating), **cheapest-capable**
> (GPT-5.6 Luna at the Index-52 tie) and the **open-weight order** (Kimi K3 60 #1) — are unchanged.
> Context: on the **AA Intelligence Index**, Claude Opus 5 still tops the board at **63** (Fable 5 62;
> GPT-5.6 Sol and Opus 5 High tied at 61); last week's frontier arrival **Grok 4.6** has slipped out of
> the visible top cluster this session and appears atop none of the benchmark-specific rows below.
> Carried caveat: Kimi K3's licence is the bespoke **"Kimi K3 License"** (not pure MIT) and it carries an
> **unresolved US distillation allegation** — the ranking here is the **independent** AA Index, agnostic
> to that dispute.

---

## Best at coding
1. **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent** — "independently benchmarked by Artificial Analysis." Agentic CLI eval (software-eng / sysadmin / data tasks scored programmatically in a Docker env). Holds #1 this refresh, ~3 pts clear of the runner-up; the page's summary line reads "GPT-5.6 Sol (max) scores the highest on Terminal-Bench Hard with a score of 65.9%." Re-verified this session; unchanged from last week.
   - **Change this refresh — new named #2.** AA's summary now names **Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)** the runner-up at **62.9%** ("followed by Claude Fable 5 … with a score of 62.9%, and GPT-5.6 Sol (medium) with a score of 62.9%"). Last week's #2/#3 — GPT-5.6 Sol (medium) and GPT-5.6 Terra (xhigh), both 62.9% — are now in the tied cluster behind Fable 5. The runner-up group is tight and self-labelled by effort tier. Vendor SWE-bench / Terminal-Bench self-reports (e.g. Qwen3.8's Terminal-Bench 2.1 86.6, GLM-5.3's self-reported cyber/coding numbers) run on a different harness than this independent CLI eval — never cross-compare a tuned vendor number against an independent one.
2. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) — **Terminal-Bench Hard 62.9%** · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard) · **independent**. The page's named #2 this session, tied at 62.9% with **GPT-5.6 Sol (medium)** (the named #3) and last week's co-runners-up. New to the runner-up slot this refresh.

## Best at reasoning
1. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) — **Humanity's Last Exam (no tools) 55.5%** · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
   - **Independent.** Still leads HLE (questions resistant to retrieval) — the eval still discriminates where GPQA has saturated. The page's summary line reads "Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) scores the highest on Humanity's Last Exam with a score of 55.5%." Number is the *no-tools* figure (multimodal questions excluded for cross-model comparability); "with tools" framings circulate but aren't comparable. Unchanged from last week (55.5%).
   - Caveat AA flags: the top config carries an **"Opus 4.8 Fallback"** — Fable 5 falls back to Claude Opus 4.8 on the tasks that trigger its safety guardrails, and the score bakes in that fallback.
2. **Claude Opus 5** (Adaptive Reasoning, Max Effort) — **Humanity's Last Exam (no tools) 54.9%** · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam) · **independent**. 0.6 pt behind Fable 5; the page's named #3 is **Claude Opus 5 (Xhigh Effort) 54.4%** — the whole top of this eval is Claude this session. On the **near-saturated GPQA Diamond** the top cluster is ~94% (against a ~70% human-expert baseline), so rank order at the top there is within noise — HLE is the discriminating reasoning eval this session.

## Longest usable context
1. **Claude Opus 4.6** — stated **1M-token window (beta)** AND **MRCR v2 (8-needle) 76% at 1M tokens** · 2026-02-05 · [Anthropic](https://www.anthropic.com/news/claude-opus-4-6)
   - **Self-reported (Anthropic).** Strongest *verified* multi-needle score at true 1M depth (vs the predecessor Sonnet 4.5's 18.5% on the same test — "Opus 4.6 scores 76%, whereas Sonnet 4.5 scores just 18.5%"). Note: stated window ≠ usable window; the 1M tier is beta ("our first Opus-class model with 1M token context"). Re-opened this session and the 76% figure still stands. The newer Claude tiers plus this week's 1M-window open models (Qwen3.8-2.4T-A95B extensible to ~1.01M, DeepSeek-V4-Pro-0813, Kimi K3 — all ~1M-token windows) ship no comparable published multi-needle retrieval number opened this session, so Opus 4.6 remains the strongest *published* 1M multi-needle figure this refresh.
2. **Gemini 3.1 Pro** — stated **1M-token window**; **MRCR v2 (8-needle) 26.3% at 1M** (84.9% at 128k) · 2026-02-19 · [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
   - **Self-reported (Google).** Holds up to ~128k but **collapses at 1M** — usable depth far below the advertised window. Re-opened this session; figures unchanged. The clearest illustration that a stated window is not a usable one.

## Best multimodal (vision / audio)
1. **Gemini 3.7 Flash** (high) — **MMMU-Pro (vision) 85%** · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)
   - **Independent.** AA's MMMU-Pro page still names Gemini 3.7 Flash (high) "scores the highest on MMMU-Pro with a score of 85%" (its low variant also reads 85%). MMMU-Pro tests multi-discipline image+text reasoning in a vision-only input setting (questions embedded in images). Caveat: AA reports MMMU-Pro as a rounded whole percent with no per-row timestamp; the page shows 17 of 243 models scored.
   - **Change this refresh — Opus 5 rejoins the co-lead.** **Claude Opus 5 (Adaptive Reasoning, Max Effort)** now reads **MMMU-Pro 85%**, tied with the two Gemini 3.7 Flash variants (AA's summary: "followed by … Claude Opus 5 (Adaptive Reasoning, Max Effort) with a score of 85%"). Last week Opus 5's per-effort MMMU-Pro cells read "no data" and it was ranked on the AA-AnalystAgent fallback; this session it is a direct co-leader on MMMU-Pro itself. AA still names Gemini 3.7 Flash "the highest," so it keeps #1 with Opus 5 tied at 85%.
   - **Audio: no entry.** No reproducible primary audio-benchmark number found this session — dropped rather than guessed.

## Best agentic / tool use
1. _(Saturated — read with care)_ **τ²-Bench Telecom** top cluster **99.1%**: **GLM-5.2 (max)** and **JT-35B-Flash** tied; GLM-4.7-Flash (Reasoning) 98.8% · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
   - **Independent.** The canonical multi-turn tool-use bench (dual-control Dec-POMDP, customer-support domains) has **saturated** — a 35B model and open-weights models top it (AA's summary now names GLM-5.2 (max) "the highest … with a score of 99.1%"), so it no longer separates frontier agents. Re-verified this session; unchanged. Trust-no-one read: stop ranking frontier agents by τ²-Bench.
2. _(Discriminating)_ **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent.** The agentic CLI eval still spreads the field (multi-step tasks in a Docker env); Claude Fable 5 and GPT-5.6 Sol (medium) tie at 62.9% behind it. Use this, not τ²-Bench, to compare top agents today.

## Cheapest capable
1. **GPT-5.6 Luna** (max) — **$0.20 in / $1.20 out per 1M tokens** · 2026-08-23 (accessed) · [AA model page](https://artificialanalysis.ai/models/gpt-5-6-luna)
   - Capability anchor: **Artificial Analysis Intelligence Index = 52** (independent), read off the same page ("Released July 2026"). Holds #1 this refresh: at the equal-Index-52 tie with DeepSeek V4 Flash (below), Luna's **flat** $0.20/$1.20 is strictly cheaper on AA's standard listing than V4 Flash's $0.44/$1.32. Pricing + capability both read off AA's independent model page (OpenAI's own pricing page has previously returned 5xx to this session-class).
2. **DeepSeek V4 Flash** (build 0731) — AA-listed **$0.44 in / $1.32 out per 1M tokens** · 2026-08-23 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash)
   - Capability anchor: **Artificial Analysis Intelligence Index = 52** (independent, listed on the same AA page).
   - **Flag (time-of-day billing, unchanged since 16 Aug):** DeepSeek's official pricing page bills V4 Flash **peak/off-peak** — off-peak **$0.22 in / $0.66 out**, peak **$0.44 in / $1.32 out** (peak = 01:00–04:00 & 06:00–10:00 UTC, Monday–Friday; off-peak rates are half of peak) · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing/). So V4 Flash's **off-peak output ($0.66)** remains the single cheapest output number in this row, but its input rose above Luna's and its peak rates are dominated by Luna — hence Luna keeps #1. Workload- and time-of-day-dependent, not a flat rate.

## Best open-weight
1. **Kimi K3** (Moonshot AI / `moonshotai`) — **Artificial Analysis Intelligence Index = 60** (independent; **#1 / 107 open-weight class**) · 2026-08-23 (accessed) · [AA model page](https://artificialanalysis.ai/models/kimi-k3)
   - Open weights re-confirmed on the [Hugging Face model card](https://huggingface.co/moonshotai/Kimi-K3) (opened this session): "We release the full Kimi K3 model weights under the Kimi K3 License", **2.8T total / 104B activated** parameters (a mixture-of-experts design that only runs part of the model per query), **1,048,576-token (1M) context**. Holds its open-weight lead at Index 60 this refresh, ~2 Index points clear of the next open model (Qwen3.8, 58). The open-weight class grew to 107 models this session (was 106).
   - **Trust-no-one caveats:** (a) the licence is the bespoke **"Kimi K3 License"** (confirmed on the model card) — permissive but **not pure MIT**, so read the terms before commercial use; (b) there is an **unresolved US White House allegation** that Kimi K3 was built by distilling Anthropic's Claude Fable 5 (China's MOFCOM rejected it as evidence-free 27 Jul) — no imposed enforcement action either way as of this refresh. The ranking here is the **independent** AA Index, which is agnostic to that dispute.
2. **Qwen3.8** (Alibaba / `Qwen`) — **Artificial Analysis Intelligence Index = 58** (independent) · 2026-08-23 (accessed) · [AA model page](https://artificialanalysis.ai/models/qwen3-8-max)
   - Open weights are public: `Qwen/Qwen3.8-2.4T-A95B` (2.4T total / 95B activated mixture-of-experts; context 262,144 native, extensible to ~1.01M; gated:No) · [HF model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) (re-opened this session).
   - **Flags:** AA's 58 is for the "**Qwen3.8 Max**" configuration (adds vision input / built-in tools / 1M-default over the raw base weights), and the AA page frames it by **price/overall band** (#13/186 overall), **not** by an explicit open-weight rank — so treat the #2 open-weight placement as read off the bracketing explicit ranks (Kimi K3 #1/107, DeepSeek V4 Pro #3/107, GLM-5.2 #4/107). The licence is the bespoke **"qwen3.8-max"** licence (not confirmed OSI-permissive this session) — read it before commercial use.
3. **DeepSeek V4 Pro 0813** (`deepseek-ai`) — license **MIT** · **Artificial Analysis Intelligence Index = 53** (independent; **#3 / 107 open-weight class**) · 2026-08-23 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-pro)
   - Open weights public since 14 Aug: `deepseek-ai/DeepSeek-V4-Pro-0813`, MIT, gated:No, mixture-of-experts routing, 1M-token context · [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) (re-opened this session; MIT + gated:No confirmed).
4. **GLM-5.2** (Z.ai / `zai-org`) — license **MIT** · **Artificial Analysis Intelligence Index = 53** (independent; **#4 / 107 open-weight class**) · 2026-08-23 (accessed) · [AA model page](https://artificialanalysis.ai/models/glm-5-2)
   - Still the strongest **fully-MIT** open model tied at the Index-53 mark (Kimi K3's and Qwen3.8's licences are bespoke). **753B-param** mixture-of-experts; MIT-licensed downloadable weights ("Pure Open: An MIT open-source license") · [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.2) (re-opened this session). Note: Z.ai's newer **GLM-5.3** (14 Aug) is **product-only so far** — no open-weights repo on `huggingface.co/zai-org` yet (newest there is still GLM-5.2) — so it is **not** an open-weight entry this refresh.

## Fastest (throughput)
1. **gpt-oss-120b on Cerebras** — **1,732.6 tokens/sec** (median output, P50 over trailing 72h) · 2026-08-23 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers)
   - **Independent** (Artificial Analysis measured). Down from 1,747.9 t/s last week — measured medians drift week-to-week. Next providers far behind: SambaNova 697.3, Groq 476.3 t/s. Caveat: this is sustained *measured median*; Cerebras's own marketing cites ~3,000 t/s — a **vendor peak / self-reported** figure, well above the independently measured median. (Separately, OpenAI's 13 Aug "Ultrafast" preview claims GPT-5.6 Sol at up to 750 tok/s via Cerebras — a vendor self-report in limited preview, no independent measurement yet, so it doesn't enter this row.)

---

## Methodology & limits
- Every claim carries a named benchmark, a number, a date, and a primary URL opened during this refresh (2026-08-23). Headline numbers were re-fetched and read off the page by the editor, not filled from memory.
- Self-reported numbers are labelled; third-party / reproducible evals (Artificial Analysis runs its own) are preferred. Vendor self-reports run materially above standardised harnesses — never cross-compare the two.
- **Real movement this week (not just an AA re-run).** Three rows changed: coding runner-up (GPT-5.6 Sol medium / Terra → Claude Fable 5 as AA's named #2 on Terminal-Bench Hard), multimodal (Claude Opus 5 rejoins the MMMU-Pro co-lead at 85% after reading "no data" last week), and fastest (Cerebras 1,747.9 → 1,732.6 t/s). The rest — reasoning, long-context, agentic, cheapest-capable, and the open-weight order — held and were re-verified. Trust the **rank order**; treat the absolute number as this session's reading.
- **Saturation watch:** GPQA Diamond (~94% top cluster) and τ²-Bench Telecom (~99%) have largely saturated; AIME 2025/2026 are at/near a perfect score for top models. Where a flagship bench has saturated, this file leads with a still-discriminating eval (HLE for reasoning, Terminal-Bench Hard for agents).
- **Stated context window ≠ usable context.** The long-context row cites a multi-needle retrieval eval at depth, not a spec-sheet number; advertised 1M (and larger) windows degrade sharply before their stated limit (Gemini 3.1 Pro: 84.9% at 128k → 26.3% at 1M).
- **Open-weight ≠ pure-MIT.** This refresh's #1 and #2 open models (Kimi K3, Qwen3.8) ship under bespoke licences; Kimi K3 also carries an unresolved distillation allegation. The rows rank on the independent AA Index but flag licence and provenance. Read the licence before deploying.
- **Cheapest-capable is time-of-day-dependent.** DeepSeek's peak/off-peak billing means "cheapest" depends on both the workload's input/output mix and the UTC hour — the row spells out both rate bands rather than a single number; GPT-5.6 Luna's flat rate keeps it #1 at the Index-52 tie.
- "Best" is a snapshot, not a law — models leapfrog weekly. The date on each row is load-bearing.
- Last full refresh: **2026-08-23**. Next scheduled: **2026-08-30** (Sunday 18:00 Europe/Rome).

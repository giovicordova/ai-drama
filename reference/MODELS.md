# MODELS.md — "Best at what" — refreshed _2026-07-12_ (weekly)

> **Opinion with receipts.** Every ranking below cites a **named benchmark + a
> number + a date + a primary URL** opened during the refresh. Benchmarks are gameable and
> often self-reported — treat them as evidence, not verdict. Self-reported numbers are
> flagged; independent / reproducible results are preferred. Refreshed weekly by
> `routines/models.md` only. Daily briefing runs never edit this file's rankings.

> **Dating convention.** Live third-party leaderboards (Artificial Analysis, etc.) carry no
> per-row publish timestamp; their date is the **access date (2026-07-12)** and the number is
> a live reading (P50 over a trailing 72h window for speed/leaderboards). Model cards, lab
> blogs and pricing pages carry their **publication date**. "Accessed" = read off the live page
> this session.

> **Frontier note (2026-07-12).** Two shifts since the 28 Jun refresh. (1) **OpenAI shipped
> GPT-5.6** (Sol / Terra / Luna tiers) on 09 Jul; **GPT-5.6 Sol (max)** now tops the coding and
> agentic-CLI rows below and ties the reasoning-adjacent GPQA cluster. (2) The prior refresh's
> open question on **Claude Fable 5** availability has resolved — Fable 5 is back and appears
> live across the Artificial Analysis leaderboards read this session (Anthropic redeployed it
> 1 Jul after US export controls were lifted). Fable 5's harness config on these evals is
> labelled "Adaptive Reasoning, Max Effort, **Opus 4.8 Fallback**" (the eval falls back to
> Opus 4.8). Claude **Opus 4.8** remains the practical production sibling.

---

## Best at coding
1. **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent** — "independently benchmarked by Artificial Analysis." Agentic CLI eval (software-eng / sysadmin / data tasks scored programmatically in a Docker env). New #1 this refresh, ~3 pts clear of the prior leader.
   - Caveat: the next cluster is tight — **GPT-5.6 Terra (xhigh) 62.9%** and **Claude Fable 5 62.9%** tie for #2 (see below). Vendor SWE-bench self-reports run well above standardised harnesses — never cross-compare a tuned vendor number against an independent one.
2. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) / **GPT-5.6 Terra** (xhigh) — both **Terminal-Bench Hard 62.9%** · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard) · **independent**. Fable 5's harness uses an Opus 4.8 fallback.

## Best at reasoning
1. **Claude Fable 5** — **Humanity's Last Exam (no tools) 53.3%** · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
   - **Independent.** Leads HLE by ~6 pts over GPT-5.6 Sol (max) 47.2% and ~8 pts over Claude Opus 4.8 (45.7%) — HLE (questions resistant to retrieval) still discriminates where GPQA has saturated. Number is the *no-tools* figure; "with tools" framings circulate but aren't comparable.
2. **GPT-5.6 Sol** (max) — **Humanity's Last Exam (no tools) 47.2%** · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam) · **independent**. On the saturated **GPQA Diamond 94.1%** it ties Gemini 3.1 Pro Preview 94.1% (GPT-5.5 xhigh 93.5% just behind · [AA](https://artificialanalysis.ai/evaluations/gpqa-diamond)) — but GPQA Diamond is **near-saturated** (top cluster ~93–95%, ~70% human-expert baseline), so rank order at the top is within noise.

## Longest usable context
1. **Claude Opus 4.6** — stated **1M-token window (beta)** AND **MRCR v2 (8-needle) 76% at 1M tokens** · 2026-02-05 · [Anthropic](https://www.anthropic.com/news/claude-opus-4-6)
   - **Self-reported (Anthropic).** Strongest *verified* multi-needle score at true 1M depth (vs Claude Sonnet 4.5 18.5% on the same test). Note: stated window ≠ usable window; the 1M tier is beta and premium-priced above 200k tokens ($10/$37.50 per 1M in/out). Opus 4.6 (not the newer 4.7/4.8) remains the strongest *published* 1M multi-needle figure this session.
2. **Gemini 3.1 Pro** — stated **1M-token window**; **MRCR v2 (8-needle) 26.3% at 1M** (84.9% at 128k) · 2026-02-19 · [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
   - **Self-reported (Google).** Holds up to ~128k but **collapses at 1M** — usable depth far below the advertised window. The clearest illustration that a stated window is not a usable one.

## Best multimodal (vision / audio)
1. **Gemini 3.5 Flash (high)** — **MMMU-Pro (vision) 84%** · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)
   - **Independent.** Tied by Gemini 3.5 Flash (medium) 84%; GPT-5.6 Sol (max) 83% just behind. MMMU-Pro tests multi-discipline image+text reasoning in a vision-only input setting (questions embedded in images). Caveat: AA reports a rounded whole percent with no per-row timestamp.
   - **Audio: no entry.** No reproducible primary audio-benchmark number found this session — dropped rather than guessed.

## Best agentic / tool use
1. _(Saturated — read with care)_ **τ²-Bench Telecom** top cluster **99.1%**: **JT-35B-Flash** and **GLM-5.2 (max)** tied; GLM-4.7-Flash 98.8% · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
   - **Independent.** The canonical multi-turn tool-use bench (dual-control Dec-POMDP, customer-support domains) has **saturated** — a 35B model and open-weights models top it, so it no longer separates frontier agents. Trust-no-one read: stop ranking frontier agents by τ²-Bench.
2. _(Discriminating)_ **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent.** The agentic CLI eval still spreads the field (multi-step tasks in a Docker env); Claude Fable 5 and GPT-5.6 Terra (xhigh) tie at 62.9%. Use this, not τ²-Bench, to compare top agents today.

## Cheapest capable
1. **DeepSeek V4 Flash** — **$0.14 in / $0.28 out per 1M tokens** (cache-miss input; cache-hit input $0.0028) · 2026-07-12 (accessed) · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing)
   - Capability anchor: **Artificial Analysis Intelligence Index v4.1 = 40** (independent) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash) — well above the ~25 open-weight median for its tier. Pricing is the **primary** official page; capability number is **independent**.
2. **DeepSeek V4 Pro** — **$0.435 in / $0.87 out per 1M tokens** · 2026-07-12 (accessed) · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing) · capability: **Intelligence Index v4.1 = 44** (independent, [AA model page](https://artificialanalysis.ai/models/deepseek-v4-pro)). A notch more capable for a bit more money.

## Best open-weight
1. **GLM-5.2** (Z.ai / `zai-org`) — license **MIT** · **Artificial Analysis Intelligence Index v4.1 = 51** (independent; **#1 open-weights**) · 2026-07-12 (accessed) · [AA model page](https://artificialanalysis.ai/models/glm-5-2)
   - Model card (self-reported): SWE-bench Pro 62.1, GPQA Diamond 91.2, Terminal-Bench 2.1 81.0 (best-reported harness 82.7), AIME 2026 99.2 · [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.2). 753B-param mixture-of-experts (only part of the model runs per query); weights downloadable (Safetensors).
   - Independent Index (51) clears the next open models by a clear margin — DeepSeek V4 Pro 44 — and the licence is permissive (MIT). Card per-benchmark figures are **self-reported**; the Index is **independent**.

## Fastest (throughput)
1. **gpt-oss-120b on Cerebras** — **1,765 tokens/sec** (median output, P50 over trailing 72h) · 2026-07-12 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers)
   - **Independent** (Artificial Analysis measured). Next providers far behind: SambaNova 694.6, Fireworks 672.8, Together AI 569.6, Groq 478.1 t/s. Caveat: this is sustained *measured median*; Cerebras's own marketing cites ~3,000 t/s — a **vendor peak / self-reported** figure, ~1.7× the independently measured median.

---

## Methodology & limits
- Every claim carries a named benchmark, a number, a date, and a primary URL opened during this refresh (2026-07-12). Headline numbers were re-fetched and read off the page by the editor, not filled from memory.
- Self-reported numbers are labelled; third-party / reproducible evals (Artificial Analysis runs its own) are preferred. Vendor self-reports run materially above standardised harnesses — never cross-compare the two.
- **Saturation watch:** GPQA Diamond (~93–95% top cluster) and τ²-Bench Telecom (~99%) have largely saturated; AIME 2025/2026 are at/near a perfect score for top models. Where a flagship bench has saturated, this file leads with a still-discriminating eval (HLE for reasoning, Terminal-Bench Hard for agents).
- **Stated context window ≠ usable context.** The long-context row cites a multi-needle retrieval eval at depth, not a spec-sheet number; advertised 1M (and larger) windows degrade sharply before their stated limit.
- "Best" is a snapshot, not a law — models leapfrog weekly. The date on each row is load-bearing.
- Last full refresh: **2026-07-12**. Next scheduled: **2026-07-19** (Sunday 18:00 Europe/Rome).
</content>
</invoke>

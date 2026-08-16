# MODELS.md — "Best at what" — refreshed _2026-08-16_ (weekly)

> **Opinion with receipts.** Every ranking below cites a **named benchmark + a
> number + a date + a primary URL** opened during the refresh. Benchmarks are gameable and
> often self-reported — treat them as evidence, not verdict. Self-reported numbers are
> flagged; independent / reproducible results are preferred. Refreshed weekly by
> `routines/models.md` only. Daily briefing runs never edit this file's rankings.

> **Dating convention.** Live third-party leaderboards (Artificial Analysis, etc.) carry no
> per-row publish timestamp; their date is the **access date (2026-08-16)** and the number is
> a live reading (P50 over a trailing 72h window for speed/leaderboards). Model cards, lab
> blogs and pricing pages carry their **publication date**. "Accessed" = read off the live page
> this session.

> **Frontier note (2026-08-16).** Four rows actually moved this week — the first real reshuffles
> in a while, not just an AA re-run. (1) **Multimodal leader flipped:** **Gemini 3.7 Flash (high)**
> now tops **MMMU-Pro at 85%** (AA's page names it "the highest"), overtaking last week's leader
> **Claude Opus 5**; a second independent vision-document eval (AA-AnalystAgent pass^5) agrees —
> Gemini 3.7 Flash 60% vs Opus 5 54%. (2) **Cheapest-capable flipped:** DeepSeek pushed through its
> long-warned price increase mid-August — **DeepSeek V4 Flash** is now **peak/off-peak billed**
> (off-peak **$0.22 in / $0.66 out**, peak **$0.44 / $1.32**, ~2–3× the old $0.14/$0.28), so at the
> equal **AA Index 52** tie, **GPT-5.6 Luna** ($0.20/$1.20 flat) takes **#1** — it's strictly cheaper
> than V4 Flash on AA's standard listing. (3) **Open-weight #2 changed:** **Qwen3.8** rose **53 → 58**
> on the AA Index (open weights now public on Hugging Face), clearing the **GLM-5.2 / DeepSeek V4 Pro
> 53-cluster**; **Kimi K3** still leads outright at **Index 60 (#1/106)**. (4) **Fastest ticked down:**
> Cerebras now serves gpt-oss-120b at a measured **1,747.9 t/s** (was 1,942.0). Rank-order leaders that
> **held** and were re-verified this session — **coding** (GPT-5.6 Sol, Terminal-Bench Hard 65.9%),
> **reasoning** (Fable 5, HLE 55.5%), **long-context** (Opus 4.6, MRCR v2 76% at 1M) and **agentic** —
> are unchanged. Context: **Grok 4.6** joined the intelligence frontier this week (AA Index 61, level with
> GPT-5.6 Sol) but doesn't appear atop any of the benchmark-specific rows below. Carried caveat: Kimi K3's
> licence is the bespoke **"Kimi K3 License"** (not pure MIT) and it carries an **unresolved US distillation
> allegation** — the ranking here is the **independent** AA Index, agnostic to that dispute.

---

## Best at coding
1. **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent** — "independently benchmarked by Artificial Analysis." Agentic CLI eval (software-eng / sysadmin / data tasks scored programmatically in a Docker env). Holds #1 this refresh, ~3 pts clear of the next cluster; the page shows 14 of 432 models scored. Re-verified this session; unchanged from last week.
   - Caveat: the runner-up cluster is tight and self-labelled — **GPT-5.6 Sol (medium) 62.9%** and **GPT-5.6 Terra (xhigh) 62.9%** are the page's named #2/#3 this session. This week's new frontier arrival **Grok 4.6** (AA Intelligence Index 61) does **not** appear in this leaderboard's top cluster. Vendor SWE-bench self-reports (e.g. Qwen3.8's Terminal-Bench 2.1 86.6, GLM-5.3's self-reported cyber/coding numbers) run on a different harness than this independent CLI eval — never cross-compare a tuned vendor number against an independent one.
2. **GPT-5.6 Sol (medium)** / **GPT-5.6 Terra** (xhigh) — both **Terminal-Bench Hard 62.9%** · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard) · **independent**. The page's named #2/#3 this session.

## Best at reasoning
1. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) — **Humanity's Last Exam (no tools) 55.5%** · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
   - **Independent.** Still leads HLE (questions resistant to retrieval) — the eval still discriminates where GPQA has saturated. Number is the *no-tools* figure over AA's 2,158 text-only HLE questions (multimodal questions excluded for cross-model comparability); "with tools" framings circulate but aren't comparable. Unchanged from last week (55.5%). Sourcing note: the live evaluations page is too large to fetch whole this session — the figure was read via AA-domain-scoped search returning the page's own summary line ("Claude Fable 5 … scores the highest … with a score of 55.5%").
   - Caveat AA flags: Fable 5 "triggers safety guardrails on 9% of HLE tasks, falling back to Claude Opus 4.8" — the score bakes in that fallback.
2. **Claude Opus 5** (Adaptive Reasoning, Max Effort) — **Humanity's Last Exam (no tools) 54.9%** · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam) · **independent**. 0.6 pt behind Fable 5. On the **near-saturated GPQA Diamond** the top cluster is ~94% (against a ~70% human-expert baseline), so rank order at the top there is within noise — HLE is the discriminating reasoning eval this session.

## Longest usable context
1. **Claude Opus 4.6** — stated **1M-token window (beta)** AND **MRCR v2 (8-needle) 76% at 1M tokens** · 2026-02-05 · [Anthropic](https://www.anthropic.com/news/claude-opus-4-6)
   - **Self-reported (Anthropic).** Strongest *verified* multi-needle score at true 1M depth (vs the predecessor Sonnet 4.5's 18.5% on the same test). Note: stated window ≠ usable window; the 1M tier is beta. Re-opened this session and the 76% figure still stands. The newer Claude tiers plus this week's 1M-window open models (Qwen3.8-2.4T-A95B, DeepSeek-V4-Pro-0813, Kimi K3 — all 1,048,576-token windows) ship no comparable published multi-needle retrieval number opened this session, so Opus 4.6 remains the strongest *published* 1M multi-needle figure this refresh.
2. **Gemini 3.1 Pro** — stated **1M-token window**; **MRCR v2 (8-needle) 26.3% at 1M** (84.9% at 128k) · 2026-02-19 · [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
   - **Self-reported (Google).** Holds up to ~128k but **collapses at 1M** — usable depth far below the advertised window. Re-opened this session; figures unchanged. The clearest illustration that a stated window is not a usable one.

## Best multimodal (vision / audio)
1. **Gemini 3.7 Flash** (high) — **MMMU-Pro (vision) 85%** · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)
   - **Independent. New leader this refresh** — AA's MMMU-Pro page names Gemini 3.7 Flash (high) "the highest … with a score of 85%" (its low/medium variants also read 85%), overtaking last week's leader Claude Opus 5. MMMU-Pro tests multi-discipline image+text reasoning in a vision-only input setting (questions embedded in images). A **second independent** multimodal eval agrees: on **AA-AnalystAgent** (complex questions over spreadsheets/documents) Gemini 3.7 Flash (high) posts the top **pass^5 = 60%**, ahead of Claude Opus 5 (max) 54% and Fable 5 49% · [AA Gemini 3.7 Flash analysis](https://artificialanalysis.ai/articles/gemini-3-7-time-frontier). Caveat: AA reports MMMU-Pro as a rounded whole percent with no per-row timestamp.
2. **Claude Opus 5** (max) — **AA-AnalystAgent pass^5 54%** · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/articles/gemini-3-7-time-frontier) · **independent**. Last week's MMMU-Pro co-leader (85%); AA's current per-effort-variant MMMU-Pro cells for Opus 5 read "no data" this session, so it is ranked here on the AA-AnalystAgent number opened this session, where it sits 6 pts behind Gemini 3.7 Flash.
   - **Audio: no entry.** No reproducible primary audio-benchmark number found this session — dropped rather than guessed. (xAI's Grok Voice Think Fast 2.0 transcription claims are vendor self-reports with no independent word-error-rate number.)

## Best agentic / tool use
1. _(Saturated — read with care)_ **τ²-Bench Telecom** top cluster **99.1%**: **JT-35B-Flash** and **GLM-5.2 (max)** tied; GLM-4.7-Flash (Reasoning) 98.8% · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
   - **Independent.** The canonical multi-turn tool-use bench (dual-control Dec-POMDP, customer-support domains) has **saturated** — a 35B model and open-weights models top it, so it no longer separates frontier agents. Re-verified this session; unchanged. Trust-no-one read: stop ranking frontier agents by τ²-Bench.
2. _(Discriminating)_ **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent.** The agentic CLI eval still spreads the field (multi-step tasks in a Docker env); GPT-5.6 Sol (medium) and GPT-5.6 Terra (xhigh) tie at 62.9%. Use this, not τ²-Bench, to compare top agents today.

## Cheapest capable
1. **GPT-5.6 Luna** (max) — **$0.20 in / $1.20 out per 1M tokens** · 2026-08-16 (accessed) · [AA model page](https://artificialanalysis.ai/models/gpt-5-6-luna)
   - Capability anchor: **Artificial Analysis Intelligence Index = 52** (independent), read off the same page. **Takes #1 this refresh by a rule change on the other side, not its own move:** at the equal-Index-52 tie, Luna's **flat** $0.20/$1.20 is now strictly cheaper than DeepSeek V4 Flash on AA's standard listing (below). Pricing + capability both read off AA's independent model page (OpenAI's own pricing page has previously returned 5xx to this session-class); reflects OpenAI's 30 Jul 80% Luna price cut, unchanged since.
2. **DeepSeek V4 Flash** (build 0731) — AA-listed **$0.44 in / $1.32 out per 1M tokens** · 2026-08-16 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash)
   - Capability anchor: **Artificial Analysis Intelligence Index = 52** (independent, listed on the same AA page) — was #1 cheapest-capable last week at $0.14/$0.28.
   - **Flag (price increase now live):** DeepSeek pushed through the "significant" hike it had been warning of. Its official pricing page now bills V4 Flash **peak/off-peak** — off-peak **$0.22 in / $0.66 out**, peak **$0.44 in / $1.32 out** (peak = 01:00–04:00 & 06:00–10:00 UTC; off-peak rates are half of peak) · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing/). AA lists the peak/standard $0.44/$1.32. So V4 Flash's **off-peak output ($0.66)** is still the single cheapest output number in this row, but its input rose above Luna's and its peak rates are dominated by Luna — hence the #1 flip. Workload- and time-of-day-dependent now, not a flat rate.

## Best open-weight
1. **Kimi K3** (Moonshot AI / `moonshotai`) — **Artificial Analysis Intelligence Index = 60** (independent; **#1 / 106 open-weight class**) · 2026-08-16 (accessed) · [AA model page](https://artificialanalysis.ai/models/kimi-k3)
   - Open weights re-confirmed on the [Hugging Face model card](https://huggingface.co/moonshotai/Kimi-K3) (opened this session): "We release the full Kimi K3 model weights under the Kimi K3 License", **2.8T total / 104B activated** parameters (a mixture-of-experts design that only runs part of the model per query), **1,048,576-token (1M) context**, Safetensors (vLLM / SGLang). Holds its open-weight lead at Index 60 this refresh, ~2 Index points clear of the next open model (Qwen3.8, 58).
   - **Trust-no-one caveats:** (a) the licence is the bespoke **"Kimi K3 License"** (confirmed on the model card) — permissive but **not pure MIT**, so read the terms before commercial use; (b) there is an **unresolved US White House allegation** that Kimi K3 was built by distilling Anthropic's Claude Fable 5 (China's MOFCOM rejected it as evidence-free 27 Jul) — no imposed enforcement action either way as of this refresh. The ranking here is the **independent** AA Index, which is agnostic to that dispute.
2. **Qwen3.8** (Alibaba / `Qwen`) — **Artificial Analysis Intelligence Index = 58** (independent) · 2026-08-16 (accessed) · [AA model page](https://artificialanalysis.ai/models/qwen3-8-max)
   - **Rose 53 → 58 this refresh and clears the 53-cluster below.** Open weights are public: `Qwen/Qwen3.8-2.4T-A95B` (2.4T total / 95B activated mixture-of-experts; context 262,144 native, extensible to ~1.01M; gated:No) landed on Hugging Face 12 Aug · [HF model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B).
   - **Flags:** AA's 58 is for the "**Qwen3.8 Max**" configuration (adds vision input / built-in tools / 1M-default over the raw base weights), and the AA page frames it by **price tier**, not by an explicit open-weight rank — so treat the #2 open-weight placement as read off the bracketing explicit ranks (Kimi K3 #1/106, DeepSeek V4 Pro #3/106, GLM-5.2 #4/106). The licence is the bespoke **"qwen3.8-max"** licence (not confirmed OSI-permissive this session) — read it before commercial use.
3. **DeepSeek V4 Pro 0813** (`deepseek-ai`) — license **MIT** · **Artificial Analysis Intelligence Index = 53** (independent; **#3 / 106 open-weight class**) · 2026-08-16 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-pro)
   - Open weights public since 14 Aug: `deepseek-ai/DeepSeek-V4-Pro-0813`, MIT, gated:No, 384 routed experts / 6-per-token MoE, 1,048,576-token (1M) context.
4. **GLM-5.2** (Z.ai / `zai-org`) — license **MIT** · **Artificial Analysis Intelligence Index = 53** (independent; **#4 / 106 open-weight class**) · 2026-08-16 (accessed) · [AA model page](https://artificialanalysis.ai/models/glm-5-2)
   - Still the strongest **fully-MIT** open model tied at the Index-53 mark (Kimi K3's and Qwen3.8's licences are bespoke). 753B-param mixture-of-experts; MIT-licensed downloadable weights · [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.2). Note: Z.ai's newer **GLM-5.3** (14 Aug) is **product-only so far** — no open-weights repo on `huggingface.co/zai-org` yet — so it is **not** an open-weight entry this refresh.

## Fastest (throughput)
1. **gpt-oss-120b on Cerebras** — **1,747.9 tokens/sec** (median output, P50 over trailing 72h) · 2026-08-16 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers)
   - **Independent** (Artificial Analysis measured). Down from 1,942.0 t/s last week — measured medians drift week-to-week. Next providers far behind: SambaNova 703.4, Groq 477.5 t/s. Caveat: this is sustained *measured median*; Cerebras's own marketing cites ~3,000 t/s — a **vendor peak / self-reported** figure, well above the independently measured median. (Separately, OpenAI's 13 Aug "Ultrafast" preview claims GPT-5.6 Sol at up to 750 tok/s via Cerebras — a vendor self-report in limited preview, no independent measurement yet, so it doesn't enter this row.)

---

## Methodology & limits
- Every claim carries a named benchmark, a number, a date, and a primary URL opened during this refresh (2026-08-16). Headline numbers were re-fetched and read off the page by the editor, not filled from memory. Where a live evaluations page was too large to fetch whole (HLE), the number was read via AA-domain-scoped search returning that same page's own summary line.
- Self-reported numbers are labelled; third-party / reproducible evals (Artificial Analysis runs its own) are preferred. Vendor self-reports run materially above standardised harnesses — never cross-compare the two.
- **Real movement this week (not just an AA re-run).** Four rows changed leader/order: multimodal (Opus 5 → Gemini 3.7 Flash on MMMU-Pro 85%), cheapest-capable (V4 Flash → GPT-5.6 Luna, driven by DeepSeek's live price increase), open-weight #2 (GLM-5.2 → Qwen3.8, Index 53 → 58), and fastest (Cerebras 1,942.0 → 1,747.9 t/s). The AA Index also drifted up a couple of points on some frozen models (Opus 5 ~61 → 63) — trust the **rank order**, treat the absolute number as this session's reading.
- **Saturation watch:** GPQA Diamond (~94% top cluster) and τ²-Bench Telecom (~99%) have largely saturated; AIME 2025/2026 are at/near a perfect score for top models. Where a flagship bench has saturated, this file leads with a still-discriminating eval (HLE for reasoning, Terminal-Bench Hard for agents).
- **Stated context window ≠ usable context.** The long-context row cites a multi-needle retrieval eval at depth, not a spec-sheet number; advertised 1M (and larger) windows degrade sharply before their stated limit (Gemini 3.1 Pro: 84.9% at 128k → 26.3% at 1M).
- **Open-weight ≠ pure-MIT.** This refresh's #1 and #2 open models (Kimi K3, Qwen3.8) ship under bespoke licences; Kimi K3 also carries an unresolved distillation allegation. The rows rank on the independent AA Index but flag licence and provenance. Read the licence before deploying.
- **Cheapest-capable is now time-of-day-dependent.** DeepSeek's mid-August move to peak/off-peak billing means "cheapest" depends on both the workload's input/output mix and the UTC hour — the row spells out both rate bands rather than a single number.
- "Best" is a snapshot, not a law — models leapfrog weekly. The date on each row is load-bearing.
- Last full refresh: **2026-08-16**. Next scheduled: **2026-08-23** (Sunday 18:00 Europe/Rome).

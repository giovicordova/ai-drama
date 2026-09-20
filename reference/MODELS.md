# MODELS.md — "Best at what" — refreshed _2026-09-20_ (weekly)

> **Opinion with receipts.** Every ranking below cites a **named benchmark + a
> number + a date + a primary URL** opened during the refresh. Benchmarks are gameable and
> often self-reported — treat them as evidence, not verdict. Self-reported numbers are
> flagged; independent / reproducible results are preferred. Refreshed weekly by
> `routines/models.md` only. Daily briefing runs never edit this file's rankings.

> **Dating convention.** Live third-party leaderboards (Artificial Analysis, etc.) carry no
> per-row publish timestamp; their date is the **access date (2026-09-20)** and the number is
> a live reading (P50 over a trailing 72h window for speed/leaderboards). Model cards, lab
> blogs and pricing pages carry their **publication date**. "Accessed" = read off the live page
> this session.

> **Frontier note (2026-09-20).** Another quiet week at the very top — the coding, reasoning,
> multimodal, agentic, long-context and cheapest-capable leaders all **held**. Movement was
> lower down. (1) **Open-weight board reshuffled below the leaders:** GLM-5.3 (max) **held #1**
> at Intelligence Index **45** and Kimi K3 (max) **held #2** at **44**, but two new **MIT-licensed**
> models arrived under them — **GLM-5.3 Flash (42)** and **DeepSeek V4.1 Flash (39)**. The
> practical consequence: the **strongest fully-MIT open model changed hands**, from last week's
> DeepSeek V4 Pro (36) to **GLM-5.3 Flash (42)**. AA's open-source board summary now reads
> "GLM-5.3 (max) and Kimi K3 (max) are the highest intelligence open source models, followed by
> GLM-5.3-Flash & Alibaba Qwen3.8 2.4T A95B." (2) **Fastest ticked back up:** Cerebras now serves
> gpt-oss-120b at a measured **1,709 t/s** (was 1,636.9 last week). Rank-order leaders that held:
> **coding** (GPT-5.6 Sol max, Terminal-Bench Hard 65.9%), **reasoning** (Claude Fable 5.1, HLE
> 59.1%), **multimodal** (GPT-6 Astra max, MMMU-Pro 87%), **long-context** (Opus 4.6, MRCR v2 76%
> at 1M), **agentic** (τ²-Bench saturated; Terminal-Bench Hard discriminating) and
> **cheapest-capable** (GPT-5.6 Luna).
> **Trust-no-one flag — AA point-released its Intelligence Index v4.3 → v4.3.2 this refresh:** a
> smaller move than the v4.2 → v4.3 rebase two weeks back. Most scores **held** (GLM-5.3 45,
> Kimi K3 44, Qwen3.8 40, DeepSeek V4 Pro 36, GLM-5.2 34 all unchanged); two nudged down by a
> point (GPT-5.6 Luna 38 → 37, DeepSeek V4 Flash 35 → 34). v4.3.2 still "incorporates 10
> evaluations: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA, Terminal-Bench 4.0, SciCode,
> Humanity's Last Exam, GDP.pdf, CritPt, AA-Omniscience, AA-LCR v1.1." Compare **rank order**, not
> a bare number against a different Index version.

---

## Best at coding
1. **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent** — "independently benchmarked by Artificial Analysis." Agentic CLI eval (software-eng / sysadmin / data tasks scored programmatically in a Docker env). Holds #1 this refresh, ~3 pts clear of the runner-up; the page's summary line reads "GPT-5.6 Sol (max) scores the highest on Terminal-Bench Hard with a score of 65.9%, followed by Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) with a score of 62.9%." Re-verified this session; unchanged from last week. Note: OpenAI's newer GPT-6 Astra (max) tops the AA Intelligence Index and MMMU-Pro but does **not** displace GPT-5.6 Sol on this coding eval this session.
   - Runner-up **Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)** at **62.9%**, tied with **GPT-5.6 Sol (medium)** (the named #3). Vendor SWE-bench / Terminal-Bench self-reports run on a different harness than this independent CLI eval — never cross-compare a tuned vendor number against an independent one.
2. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) — **Terminal-Bench Hard 62.9%** · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard) · **independent**. The page's named #2 this session, tied at 62.9% with **GPT-5.6 Sol (medium)** (the named #3). Holds the runner-up slot this refresh.

## Best at reasoning
1. **Claude Fable 5.1** (Adaptive Reasoning, Max Effort, Default Fallback) — **Humanity's Last Exam (no tools) 59.1%** · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
   - **Independent.** Holds the top slot from last refresh on HLE (questions resistant to retrieval — the eval still discriminates where GPQA has saturated). The page's summary line reads "Claude Fable 5.1 (Adaptive Reasoning, Max Effort, Default Fallback) scores the highest on Humanity's Last Exam with a score of 59.1%." The named #2 and #3 are the Xhigh (58.7%) and High (55.9%) configs of the same model. Number is the *no-tools* figure (multimodal questions excluded for cross-model comparability); "with tools" framings circulate but aren't comparable.
   - Note: the top config carries a **"Default Fallback"** (Fable 5.1 hands off to a fallback model on tasks that trigger its safety guardrails, and the score bakes in that fallback).
2. **Claude Fable 5.1** (Adaptive Reasoning, Xhigh Effort, Default Fallback) — **Humanity's Last Exam (no tools) 58.7%** · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam) · **independent**. The page's named #2; the named #3 is **Claude Fable 5.1 (High Effort) 55.9%** — the entire HLE top cluster is Claude Fable 5.1 this session. On the **near-saturated GPQA Diamond** the top cluster sits ~94% (against a ~70% human-expert baseline), so rank order there is within noise — HLE is the discriminating reasoning eval this session.

## Longest usable context
1. **Claude Opus 4.6** — stated **1M-token window** AND **MRCR v2 (8-needle) 76% at 1M tokens** · 2026-02-05 · [Anthropic](https://www.anthropic.com/news/claude-opus-4-6)
   - **Self-reported (Anthropic).** Strongest *verified* multi-needle score at true 1M depth: "on the 8-needle 1M variant of MRCR v2—a needle-in-a-haystack benchmark that tests a model's ability to retrieve information 'hidden' in vast amounts of text—Opus 4.6 scores 76%." Note: stated window ≠ usable window, and the 1M tier carries premium pricing ("Opus 4.6 is our first Opus-class model with 1M token context. Premium pricing applies for prompts exceeding 200k tokens"). Re-opened this session and the 76% figure still stands. The newer Claude tiers (Opus 5, Fable 5.1) and OpenAI's GPT-6 Astra ship no comparable *published* 1M multi-needle retrieval number opened this session, and the 1M-window open models (Qwen3.8 extensible to ~1.01M, DeepSeek-V4.1-Flash and DeepSeek-V4-Pro-0813, Kimi K3 — all ~1M-token windows) publish no comparable multi-needle figure either, so Opus 4.6 remains the strongest *published* 1M multi-needle number this refresh.
2. **Gemini 3.1 Pro** — stated **1M-token window**; **MRCR v2 (8-needle) 26.3% at 1M** (84.9% at 128k) · 2026-02-19 · [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
   - **Self-reported (Google).** Holds up to ~128k but **collapses at 1M** — usable depth far below the advertised window ("a token context window of up to 1M"). Re-opened this session; figures unchanged. The clearest illustration that a stated window is not a usable one.

## Best multimodal (vision / audio)
1. **GPT-6 Astra** (max) — **MMMU-Pro (vision) 87%** · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)
   - **Independent.** Holds the top slot from last refresh. AA's MMMU-Pro page reads "GPT-6 Astra (max) scores the highest on MMMU-Pro with a score of 87%, followed by GPT-6 Astra (high) with a score of 86% and GPT-6 Astra (xhigh) with a score of 86%." MMMU-Pro tests multi-discipline image+text reasoning in a vision-only input setting (questions embedded in images); GPT-6 Astra's variants sweep the top three. Caveat: AA reports MMMU-Pro as a rounded whole percent with no per-row timestamp.
   - **Audio: no entry.** No reproducible primary audio-benchmark number found this session — dropped rather than guessed.

## Best agentic / tool use
1. _(Saturated — read with care)_ **τ²-Bench Telecom** top cluster **99.1%**: **GLM-5.2 (max)** and **JT-35B-Flash** tied; GLM-4.7-Flash (Reasoning) 98.8% · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
   - **Independent.** The canonical multi-turn tool-use bench (dual-control Dec-POMDP, customer-support domains) has **saturated** — a 35B model and open-weights models top it (AA's summary reads "GLM-5.2 (max) scores the highest on 𝜏²-Bench Telecom with a score of 99.1%, followed by JT-35B-Flash with a score of 99.1% and GLM-4.7-Flash (Reasoning) with a score of 98.8%"), so it no longer separates frontier agents. Re-verified this session; unchanged. Trust-no-one read: stop ranking frontier agents by τ²-Bench.
2. _(Discriminating)_ **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent.** The agentic CLI eval still spreads the field (multi-step tasks in a Docker env); Claude Fable 5 and GPT-5.6 Sol (medium) tie at 62.9% behind it. Use this, not τ²-Bench, to compare top agents today.

## Cheapest capable
1. **GPT-5.6 Luna** (max) — **$0.20 in / $1.20 out per 1M tokens** · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/gpt-5-6-luna)
   - Capability anchor: **Artificial Analysis Intelligence Index = 37** (independent, v4.3.2), read off the same page ("Released July 9, 2026"). Holds #1 this refresh: Luna's **flat** $0.20/$1.20 has no time-of-day fine print, and its Index (37) sits 3 points above DeepSeek V4 Flash's (34, below). (Index nudged 38 → 37 under the v4.3.2 point release; the gap to DeepSeek V4 Flash held.) Pricing + capability both read off AA's independent model page (OpenAI's own pricing page has previously returned 5xx to this session-class).
2. **DeepSeek V4 Flash** — AA-listed **$0.44 in / $1.32 out per 1M tokens** · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash)
   - Capability anchor: **Artificial Analysis Intelligence Index = 34** (independent, v4.3.2; nudged 35 → 34 under the point release).
   - **Flag (time-of-day billing, re-verified this session):** DeepSeek's official pricing page bills its Flash tier **peak/off-peak** — off-peak **$0.15 in (cache miss) / $0.60 out**, peak **$0.30 in / $1.20 out** ("Peak hours are 01:00 - 04:00 and 06:00 - 10:00 UTC, Monday through Friday, excluding Chinese public holidays. All other hours are off-peak, including weekends and Chinese public holidays in full.") · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing/). So off-peak it undercuts Luna on both input and output, but its **peak input ($0.30) sits above Luna's flat $0.20**, and its Index is 3 points lower — so Luna keeps #1. (Note: AA's model page lists a higher flat $0.44/$1.32 than DeepSeek's own current page; the row cites AA for the Index anchor and DeepSeek's primary page for the live rate bands.) Workload- and time-of-day-dependent, not a flat rate.

## Best open-weight
> Ranked on the independent **AA Intelligence Index v4.3.2** (point-released this refresh; see frontier note). Every entry's public weights were re-confirmed on its Hugging Face model card this session.
1. **GLM-5.3 (max)** (Z.ai / `zai-org`) — **AA Intelligence Index = 45** (independent, v4.3.2; **#1 open-source**) · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/glm-5-3)
   - **Holds #1 open-weight leader** (Index 45, unchanged under the point release). AA's open-source board summary reads "GLM-5.3 (max) and Kimi K3 (max) are the highest intelligence open source models, followed by GLM-5.3-Flash & Alibaba Qwen3.8 2.4T A95B" · [AA open-source board](https://artificialanalysis.ai/models/open-source). Public weights re-confirmed on the [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.3) (opened this session): downloadable Safetensors, **753B params**, under a bespoke **"glm-5.3" licence** (not MIT). **Flag:** read the bespoke licence before commercial use.
2. **Kimi K3 (max)** (Moonshot AI / `moonshotai`) — **AA Intelligence Index = 44** (independent, v4.3.2; **#2 open-source**) · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/kimi-k3)
   - Open weights re-confirmed on the [Hugging Face model card](https://huggingface.co/moonshotai/Kimi-K3) (opened this session): "Both the code repository and the model weights are released under the Kimi K3 License", **2.8T total / 104B activated** parameters (a mixture-of-experts design that only runs part of the model per query), **1,048,576-token context**, downloadable Safetensors (over 2M downloads shown). Holds #2 this refresh (Index 44 vs GLM-5.3's 45).
   - **Trust-no-one caveats:** (a) the licence is the bespoke **"Kimi K3 License"** (confirmed on the model card this session) — permissive but **not pure MIT**, so read the terms before commercial use; (b) an **unresolved distillation allegation** (that Kimi K3 was distilled from Anthropic's Claude Fable 5) was noted in prior refreshes and is **not re-verified this session** — flagged as background, not a current fact. The ranking here is the **independent** AA Index, agnostic to that dispute.
3. **GLM-5.3 Flash** (Z.ai / `zai-org`) — license **MIT** · **AA Intelligence Index = 42** (independent, v4.3.2) · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/glm-5-3-flash)
   - **New this refresh, and the strongest fully-MIT open model** — Index 42, six points above last week's MIT leader (DeepSeek V4 Pro, 36). Open weights re-confirmed on the [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.3-Flash) (opened this session): downloadable Safetensors, licence "mit"; "With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks" (a mixture-of-experts design that only runs part of the model per query). A genuinely permissive licence at this capability tier — the notable open-weight move this week.
4. **Qwen3.8** (Alibaba / `Qwen`) — **AA Intelligence Index = 40** (independent, v4.3.2) · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/qwen3-8-2-4t-a95b)
   - Open weights re-confirmed: `Qwen/Qwen3.8-2.4T-A95B` ("2.4T in total and 95B activated" mixture-of-experts; "262,144 natively and extensible up to 1,010,000 tokens"; downloadable Safetensors) · [HF model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) (re-opened this session).
   - **Flag:** the licence is the bespoke **"qwen3.8-max"** licence (not confirmed OSI-permissive this session) — read it before commercial use.
5. **DeepSeek V4.1 Flash** (`deepseek-ai`) — license **MIT** · **AA Intelligence Index = 39** (independent, v4.3.2) · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-1-flash)
   - **New this refresh** — the second-strongest MIT model (Index 39). Open weights re-confirmed on the [Hugging Face model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) (opened this session): "This repository and the model weights are licensed under the MIT License", **552B backbone** (8B activated at prefill / 16B at decode; mixture-of-experts), **up to 1M-token context**, downloadable Safetensors.
6. **DeepSeek V4 Pro 0813** (`deepseek-ai`) — license **MIT** · **AA Intelligence Index = 36** (independent, v4.3.2) · 2026-09-20 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-pro)
   - Last week's MIT leader, now third among MIT open models behind GLM-5.3 Flash (42) and DeepSeek V4.1 Flash (39). Open weights public: `deepseek-ai/DeepSeek-V4-Pro-0813`, "This repository and the model weights are licensed under the MIT License", **1.7T params**, mixture-of-experts, million-token context · [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) (re-opened this session; MIT + open download confirmed, 160,092 downloads last month).
   - Also fully-MIT this refresh but lower on capability: **GLM-5.2** (Z.ai / `zai-org`), **AA Intelligence Index = 34** (v4.3.2) · [AA model page](https://artificialanalysis.ai/models/glm-5-2), 753B-param mixture-of-experts, MIT-licensed weights on its [HF model card](https://huggingface.co/zai-org/GLM-5.2) — now superseded by its own newer sibling GLM-5.3 Flash (42, MIT) on both capability and openness.

## Fastest (throughput)
1. **gpt-oss-120b on Cerebras** — **1,709 tokens/sec** (median output, P50 over trailing 72h) · 2026-09-20 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers)
   - **Independent** (Artificial Analysis measured; "Figures represent median (P50) measurement over the past 72 hours to reflect sustained changes in performance"). **Up from 1,636.9 t/s last week** — recovering last refresh's dip. Next providers far behind: SambaNova 708, Groq 474 t/s. Caveat: this is sustained *measured median*; Cerebras's own marketing cites ~3,000 t/s — a **vendor peak / self-reported** figure, well above the independently measured median.

---

## Methodology & limits
- Every claim carries a named benchmark, a number, a date, and a primary URL opened during this refresh (2026-09-20). Headline numbers were re-fetched and read off the page by the editor, not filled from memory.
- Self-reported numbers are labelled; third-party / reproducible evals (Artificial Analysis runs its own) are preferred. Vendor self-reports run materially above standardised harnesses — never cross-compare the two.
- **Movement this week.** **Open-weight** reshuffled below the two leaders: two new **MIT** models arrived (GLM-5.3 Flash 42, DeepSeek V4.1 Flash 39), and the strongest fully-MIT model changed from DeepSeek V4 Pro (36) to **GLM-5.3 Flash (42)**. **Fastest** ticked back up (Cerebras 1,636.9 → 1,709 t/s). Coding, reasoning, multimodal, long-context, agentic and cheapest-capable all held their leaders.
- **AA Intelligence Index point-released v4.3 → v4.3.2 this refresh.** A minor move: most scores held (GLM-5.3 45, Kimi K3 44, Qwen3.8 40, DeepSeek V4 Pro 36, GLM-5.2 34), two nudged down a point (GPT-5.6 Luna 38 → 37, DeepSeek V4 Flash 35 → 34). v4.3.2 still incorporates the same 10 evaluations (Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-Omniscience, AA-LCR v1.1, AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA). Trust the **rank order**; don't compare a number across Index versions.
- **Saturation watch:** GPQA Diamond (~94% top cluster) and τ²-Bench Telecom (~99%) have largely saturated; AIME 2025/2026 are at/near a perfect score for top models. Where a flagship bench has saturated, this file leads with a still-discriminating eval (HLE for reasoning, Terminal-Bench Hard for agents).
- **Stated context window ≠ usable context.** The long-context row cites a multi-needle retrieval eval at depth, not a spec-sheet number; advertised 1M (and larger) windows degrade sharply before their stated limit (Gemini 3.1 Pro: 84.9% at 128k → 26.3% at 1M).
- **Open-weight ≠ pure-MIT — but the MIT tier just got much stronger.** The #1–#2 open models (GLM-5.3, Kimi K3) and #4 (Qwen3.8) ship under bespoke licences; the strongest MIT model is now **GLM-5.3 Flash (42)**, with DeepSeek V4.1 Flash (39), DeepSeek V4 Pro (36) and GLM-5.2 (34) also MIT. Kimi K3 also carries an unresolved distillation allegation (background, not re-verified this session). The rows rank on the independent AA Index but flag licence and provenance. Read the licence before deploying.
- **Cheapest-capable is time-of-day-dependent.** DeepSeek's peak/off-peak billing means "cheapest" depends on both the workload's input/output mix and the UTC hour — the row spells out both rate bands rather than a single number; GPT-5.6 Luna's flat rate (and a 3-point Index lead) keeps it #1.
- "Best" is a snapshot, not a law — models leapfrog weekly. The date on each row is load-bearing.
- Last full refresh: **2026-09-20**. Next scheduled: **2026-09-27** (Sunday 18:00 Europe/Rome).

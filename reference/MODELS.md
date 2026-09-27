# MODELS.md — "Best at what" — refreshed _2026-09-27_ (weekly)

> **Opinion with receipts.** Every ranking below cites a **named benchmark + a
> number + a date + a primary URL** opened during the refresh. Benchmarks are gameable and
> often self-reported — treat them as evidence, not verdict. Self-reported numbers are
> flagged; independent / reproducible results are preferred. Refreshed weekly by
> `routines/models.md` only. Daily briefing runs never edit this file's rankings.

> **Dating convention.** Live third-party leaderboards (Artificial Analysis, etc.) carry no
> per-row publish timestamp; their date is the **access date (2026-09-27)** and the number is
> a live reading (P50 over a trailing 72h window for speed/leaderboards). Model cards, lab
> blogs and pricing pages carry their **publication date**. "Accessed" = read off the live page
> this session.

> **Frontier note (2026-09-27).** Movement at the very top this week — **Anthropic's newer
> Claude Opus 5.5 took two crowns.** (1) **Reasoning changed hands:** Claude Opus 5.5
> (Max Effort) now tops **Humanity's Last Exam** at **61.4%**, above Claude Fable 5.1's
> **59.1%** (last week's #1, now #2). (2) **Multimodal changed hands:** Claude Opus 5.5
> now tops **MMMU-Pro (vision)** at **88%**, edging **GPT-6 Astra (max)** (87%, last week's #1,
> now #2). (3) **Open-weight #1 changed hands to a MIT model:** **Xiaomi's MiMo-V2.6-Pro**
> (released 21 Sep) debuts at **AA Intelligence Index 46**, above GLM-5.3 (max) (45) and
> Kimi K3 (max) (44) — and it is **MIT-licensed**, so for the first time this file's overall
> open-weight leader and its strongest fully-MIT open model are the **same model** (previously
> the MIT leader, GLM-5.3 Flash at 42, sat below the bespoke-licensed leaders). AA's open-source
> board summary now reads "MiMo-V2.6-Pro and GLM-5.3 (max) are the highest intelligence open
> source models, followed by Kimi K3 (max) & GLM-5.3-Flash." (4) **Fastest ticked up again:**
> Cerebras now serves gpt-oss-120b at a measured **1,737 t/s** (was 1,709 last week). Leaders
> that **held:** **coding** (GPT-5.6 Sol max, Terminal-Bench Hard 65.9%), **long-context**
> (Opus 4.6, MRCR v2 76% at 1M), **agentic** (τ²-Bench saturated; Terminal-Bench Hard
> discriminating) and **cheapest-capable** (GPT-5.6 Luna).
> **Trust-no-one flag — the AA Intelligence Index held at v4.3.2 this refresh** (no rebase or
> point-release this week; every open-weight and cheapest-capable number below reads off the
> same v4.3.2 as last week, so week-over-week Index comparisons are clean). v4.3.2 still
> "incorporates 10 evaluations: AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA,
> Terminal-Bench 4.0, SciCode, Humanity's Last Exam, GDP.pdf, CritPt, AA-Omniscience, AA-LCR v1.1."

---

## Best at coding
1. **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent** — "independently benchmarked by Artificial Analysis." Agentic CLI eval (software-eng / sysadmin / data tasks scored programmatically in a Docker env). Holds #1 this refresh, ~3 pts clear of the runner-up; the page's summary line reads "GPT-5.6 Sol (max) scores the highest on Terminal-Bench Hard with a score of 65.9%, followed by Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) with a score of 62.9% and GPT-5.6 Sol (medium) with a score of 62.9%." Re-verified this session; unchanged from last week. Note: Claude Opus 5.5 now tops the AA reasoning (HLE) and multimodal (MMMU-Pro) boards this session but does **not** displace GPT-5.6 Sol on this coding eval, and neither does GPT-6 Astra.
   - Runner-up **Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)** at **62.9%**, tied with **GPT-5.6 Sol (medium)** (the named #3). Vendor SWE-bench / Terminal-Bench self-reports run on a different harness than this independent CLI eval — never cross-compare a tuned vendor number against an independent one.
2. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) — **Terminal-Bench Hard 62.9%** · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard) · **independent**. The page's named #2 this session, tied at 62.9% with **GPT-5.6 Sol (medium)** (the named #3). Holds the runner-up slot this refresh.

## Best at reasoning
1. **Claude Opus 5.5** (Adaptive Reasoning, Max Effort, Default Fallback) — **Humanity's Last Exam (no tools) 61.4%** · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
   - **Independent — new #1 this refresh**, taking the top slot from Claude Fable 5.1 (now #2 at 59.1%). HLE tests questions resistant to retrieval — the eval still discriminates where GPQA has saturated. The page's summary line reads "Claude Opus 5.5 (Adaptive Reasoning, Max Effort, Default Fallback) scores the highest on Humanity's Last Exam with a score of 61.4%." Number is the *no-tools* figure (text-only questions — 2,158 of the May-2025 revision's 2,500 — for cross-model comparability; "with tools" framings circulate but aren't comparable). Benchmark: HLE, arXiv 2501.14249.
   - Note: the top config carries a **"Default Fallback"** (Opus 5.5 hands off to a fallback model on tasks that trigger its safety guardrails, and the score bakes in that fallback).
2. **Claude Fable 5.1** (Adaptive Reasoning, Max Effort, Default Fallback) — **Humanity's Last Exam (no tools) 59.1%** · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam) · **independent**. Last refresh's #1, now the page's named #2 behind Opus 5.5; the named #3 is **Claude Fable 5.1 (Xhigh Effort) 58.7%** — the HLE top cluster remains all Claude this session (Opus 5.5 + Fable 5.1 configs). On the **near-saturated GPQA Diamond** the top cluster sits ~94% (against a ~70% human-expert baseline), so rank order there is within noise — HLE is the discriminating reasoning eval this session.

## Longest usable context
1. **Claude Opus 4.6** — stated **1M-token window** AND **MRCR v2 (8-needle) 76% at 1M tokens** · 2026-02-05 · [Anthropic](https://www.anthropic.com/news/claude-opus-4-6)
   - **Self-reported (Anthropic).** Strongest *verified* multi-needle score at true 1M depth: "on the 8-needle 1M variant of MRCR v2—a needle-in-a-haystack benchmark that tests a model's ability to retrieve information 'hidden' in vast amounts of text—Opus 4.6 scores 76%, whereas Sonnet 4.5 scores just 18.5%." Note: stated window ≠ usable window; the 1M window is "in beta on the Claude Developer Platform only," and the 1M tier carries premium pricing ("Premium pricing applies for prompts exceeding 200k tokens ($10/$37.50 per million input/output tokens)"). Re-opened this session and the 76% figure still stands. The newer Claude tiers **still ship no comparable *published* 1M multi-needle retrieval number** opened this session: Opus 5.5 now has a 1M window and Anthropic touts improved retrieval over Opus 5, but its announcement **published no new 1M MRCR figure** (confirmed via search this session). The 1M-window open models (Qwen3.8 ~984k, MiMo-V2.6-Pro 1M, DeepSeek-V4.1-Flash and DeepSeek-V4-Pro-0813, Kimi K3 — all ~1M-token windows) publish no comparable multi-needle figure either, so **Opus 4.6 remains the strongest *published* 1M multi-needle number this refresh**.
2. **Gemini 3.1 Pro** — stated **1M-token window**; **MRCR v2 (8-needle) 26.3% at 1M** (84.9% at 128k) · 2026-02-19 · [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
   - **Self-reported (Google).** Holds up to ~128k but **collapses at 1M** — usable depth far below the advertised window ("a token context window of up to 1M"). Re-opened this session; figures unchanged. The clearest illustration that a stated window is not a usable one.

## Best multimodal (vision / audio)
1. **Claude Opus 5.5** (Adaptive Reasoning, Max Effort, Default Fallback) — **MMMU-Pro (vision) 88%** · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)
   - **Independent — new #1 this refresh**, edging last week's leader GPT-6 Astra (max) (now #2 at 87%). AA's MMMU-Pro page reads "Claude Opus 5.5 (Adaptive Reasoning, Max Effort, Default Fallback) scores the highest on MMMU-Pro with a score of 88%." MMMU-Pro tests multi-discipline image+text reasoning in a vision-only input setting (questions embedded in images); benchmark arXiv 2409.02813. Runners-up this session: GPT-6 Astra (max) 87% and Claude Opus 5.5 (Xhigh) 87%. Caveat: AA reports MMMU-Pro as a rounded whole percent with no per-row timestamp, so the 88% vs 87% gap is one rounded point — read as a near-tie at the top.
   - **Audio: no entry.** No reproducible primary audio-benchmark number found this session — dropped rather than guessed.

## Best agentic / tool use
1. _(Saturated — read with care)_ **τ²-Bench Telecom** top cluster **99.1%**: **GLM-5.2 (max)** and **JT-35B-Flash** tied; GLM-4.7-Flash (Reasoning) 98.8% · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
   - **Independent.** The canonical multi-turn tool-use bench (dual-control Dec-POMDP, customer-support domains; Sierra Research, arXiv 2506.07982) has **saturated** — a 35B model and open-weights models top it (AA's summary reads "GLM-5.2 (max) scores the highest on 𝜏²-Bench Telecom with a score of 99.1%, followed by JT-35B-Flash with a score of 99.1% and GLM-4.7-Flash (Reasoning) with a score of 98.8%"), so it no longer separates frontier agents. Re-verified this session; unchanged. Trust-no-one read: stop ranking frontier agents by τ²-Bench.
2. _(Discriminating)_ **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent.** The agentic CLI eval still spreads the field (multi-step tasks in a Docker env); Claude Fable 5 and GPT-5.6 Sol (medium) tie at 62.9% behind it. Use this, not τ²-Bench, to compare top agents today.

## Cheapest capable
1. **GPT-5.6 Luna** (max) — **$0.20 in / $1.20 out per 1M tokens** · 2026-09-27 (accessed) · [AA model page](https://artificialanalysis.ai/models/gpt-5-6-luna)
   - Capability anchor: **Artificial Analysis Intelligence Index = 37** (independent, v4.3.2), read off the same page ("Released July 9, 2026"). Holds #1 this refresh: Luna's **flat** $0.20/$1.20 has no time-of-day fine print, and its Index (37) sits 3 points above DeepSeek V4 Flash's (34, below). Both price and capability unchanged from last refresh. Pricing + capability both read off AA's independent model page (OpenAI's own pricing page has previously returned 5xx to this session-class).
2. **DeepSeek V4 Flash** — AA-listed **$0.44 in / $1.32 out per 1M tokens** · 2026-09-27 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash)
   - Capability anchor: **Artificial Analysis Intelligence Index = 34** (independent, v4.3.2; unchanged this refresh).
   - **Flag (time-of-day billing, re-verified this session):** DeepSeek's official pricing page bills its Flash tier **peak/off-peak** — off-peak **$0.15 in (cache miss) / $0.60 out**, peak **$0.30 in / $1.20 out** ("Peak hours are 01:00 - 04:00 and 06:00 - 10:00 UTC, Monday through Friday, excluding Chinese public holidays. All other hours are off-peak, including weekends and Chinese public holidays in full.") · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing/). So off-peak it undercuts Luna on both input and output, but its **peak input ($0.30) sits above Luna's flat $0.20**, and its Index is 3 points lower — so Luna keeps #1. (Note: AA's model page lists a higher flat $0.44/$1.32 than DeepSeek's own current page; the row cites AA for the Index anchor and DeepSeek's primary page for the live rate bands.) Workload- and time-of-day-dependent, not a flat rate.

## Best open-weight
> Ranked on the independent **AA Intelligence Index v4.3.2** (held this refresh — no rebase; see frontier note). Open-weights status + licence for each entry read off its AA independent model page this session; where the Hugging Face card was reachable it was re-confirmed there too.
1. **MiMo-V2.6-Pro** (Xiaomi / `XiaomiMiMo`) — license **MIT** · **AA Intelligence Index = 46** (independent, v4.3.2; **#1 open-source**) · 2026-09-27 (accessed) · [AA model page](https://artificialanalysis.ai/models/mimo-v2-6-pro)
   - **New this refresh and the new open-weight leader** — and it is **MIT-licensed**, so the overall open-weight #1 and the strongest fully-MIT open model are now the **same model** (last week the MIT leader, GLM-5.3 Flash at 42, sat below the bespoke-licensed leaders). AA's page (opened this session): "MiMo-V2.6-Pro scores 46 on the Artificial Analysis Intelligence Index"; "released on September 21, 2026"; "created by Xiaomi"; "The model weights are publicly available and can be downloaded for self-hosting"; "released under the MIT license. This license allows commercial use"; "1.0 trillion parameters (42 billion active)" mixture-of-experts (a design that runs only part of the model per query); "context window of 1.0M tokens." AA's open-source board summary reads "MiMo-V2.6-Pro and GLM-5.3 (max) are the highest intelligence open source models, followed by Kimi K3 (max) & GLM-5.3-Flash" · [AA open-source board](https://artificialanalysis.ai/models/open-source). **Trust-no-one flag:** the Hugging Face model card [huggingface.co/XiaomiMiMo/MiMo-V2.6-Pro] returned **HTTP 401 to the fetcher this session** (not re-confirmable directly here), so the open-weights + MIT + downloadable facts rest on AA's **independent** model page + open-source board (both opened this session); multiple named outlets corroborate the MIT/HF release on 21 Sep.
2. **GLM-5.3 (max)** (Z.ai / `zai-org`) — **AA Intelligence Index = 45** (independent, v4.3.2; **#2 open-source**) · 2026-09-27 (accessed) · [AA open-source board](https://artificialanalysis.ai/models/open-source)
   - Now #2 open-weight behind MiMo-V2.6-Pro (was #1 last week; Index 45 unchanged). Public weights on the [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.3): **753B params**, under a bespoke **"glm-5.3" licence** (not MIT). **Flag:** read the bespoke licence before commercial use.
3. **Kimi K3 (max)** (Moonshot AI / `moonshotai`) — **AA Intelligence Index = 44** (independent, v4.3.2; **#3 open-source**) · 2026-09-27 (accessed) · [AA open-source board](https://artificialanalysis.ai/models/open-source)
   - Open weights on the [Hugging Face model card](https://huggingface.co/moonshotai/Kimi-K3): "released under the Kimi K3 License", **2.8T total / 104B activated** parameters (mixture-of-experts), **1,048,576-token context**, downloadable Safetensors. Index 44 (unchanged), now #3 behind MiMo (46) and GLM-5.3 (45).
   - **Trust-no-one caveats:** (a) the licence is the bespoke **"Kimi K3 License"** — permissive but **not pure MIT**, so read the terms before commercial use; (b) an **unresolved distillation allegation** (that Kimi K3 was distilled from Anthropic's Claude Fable 5) was noted in prior refreshes and is **not re-verified this session** — flagged as background, not a current fact. The ranking here is the **independent** AA Index, agnostic to that dispute.
4. **GLM-5.3 Flash** (Z.ai / `zai-org`) — license **MIT** · **AA Intelligence Index = 42** (independent, v4.3.2) · 2026-09-27 (accessed) · [AA open-source board](https://artificialanalysis.ai/models/open-source)
   - Last week's strongest fully-MIT model (42), now the **second**-strongest MIT model behind MiMo-V2.6-Pro (46). Open weights on the [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.3-Flash): licence "mit"; "With 320B total parameters and just 18B active parameters, it outperforms GLM-5.2 across benchmarks" (mixture-of-experts).
5. **Qwen3.8** (Alibaba / `Qwen`) — **AA Intelligence Index = 40** (independent, v4.3.2; ranked #5 / 115 on AA) · 2026-09-27 (accessed) · [AA model page](https://artificialanalysis.ai/models/qwen3-8-2-4t-a95b)
   - Open weights confirmed on the AA model page this session: `Qwen/Qwen3.8-2.4T-A95B`, **2.4T total / 95B activated** (mixture-of-experts), **~984k-token context**, weights public on Hugging Face.
   - **Flag:** the licence is the bespoke **"Qwen3.8-Max"** licence ("allowing commercial use with restrictions"; not confirmed OSI-permissive this session) — read it before commercial use.
6. **DeepSeek V4.1 Flash** (`deepseek-ai`) — license **MIT** · **AA Intelligence Index = 39** (independent, v4.3.2) · 2026-09-27 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-1-flash)
   - The third-strongest MIT model this refresh (Index 39; released 10 Sep). AA model page this session: "open weights … model weights are publicly available and can be downloaded for self-hosting"; "MIT" licence; **552B total / 16B active** (mixture-of-experts); text + image in, text out. HF card: [huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash].
7. **DeepSeek V4 Pro 0813** (`deepseek-ai`) — license **MIT** · **AA Intelligence Index = 36** (independent, v4.3.2) · 2026-09-27 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-pro)
   - Fourth among MIT open models now (behind MiMo 46, GLM-5.3 Flash 42, DeepSeek V4.1 Flash 39). AA model page this session: "open weights model"; "MIT" licence; **1.6T total / 49B active** (mixture-of-experts). HF card: [huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813].
   - Also fully-MIT this refresh but lower on capability: **GLM-5.2** (Z.ai / `zai-org`), **AA Intelligence Index = 34** (v4.3.2) · [AA model page](https://artificialanalysis.ai/models/glm-5-2), 753B-param mixture-of-experts, MIT-licensed weights on its [HF model card](https://huggingface.co/zai-org/GLM-5.2) — well below the MIT leaders now.

## Fastest (throughput)
1. **gpt-oss-120b on Cerebras** — **1,737 tokens/sec** (median output, P50 over trailing 72h) · 2026-09-27 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers)
   - **Independent** (Artificial Analysis measured; "Figures represent median (P50) measurement over the past 72 hours to reflect sustained changes in performance"). **Up from 1,709 t/s last week.** Next providers far behind: SambaNova 703.5, Groq 475.2 t/s. Caveat: this is sustained *measured median* (not a vendor peak); Cerebras's own marketing has cited ~3,000 t/s — a **vendor peak / self-reported** figure, well above the independently measured median.

---

## Methodology & limits
- Every claim carries a named benchmark, a number, a date, and a primary URL opened during this refresh (2026-09-27). Headline numbers were re-fetched and read off the page by the editor, not filled from memory.
- Self-reported numbers are labelled; third-party / reproducible evals (Artificial Analysis runs its own) are preferred. Vendor self-reports run materially above standardised harnesses — never cross-compare the two.
- **Movement this week.** **Reasoning** and **multimodal** both changed hands to **Claude Opus 5.5** (HLE 61.4%, over Fable 5.1's 59.1%; MMMU-Pro 88%, over GPT-6 Astra's 87%). **Open-weight** #1 changed to **Xiaomi MiMo-V2.6-Pro** (Index 46, **MIT**) — the first time the overall open-weight leader is itself MIT-licensed, so the strongest-MIT and overall-open leaders are now the same model. **Fastest** ticked up (Cerebras 1,709 → 1,737 t/s). Coding, long-context, agentic and cheapest-capable all held their leaders.
- **AA Intelligence Index held at v4.3.2 this refresh** — no rebase or point-release, so every open-weight and cheapest-capable Index number is directly comparable to last week's. v4.3.2 incorporates 10 evaluations (Terminal-Bench 4.0, SciCode, HLE, GDP.pdf, CritPt, AA-Omniscience, AA-LCR v1.1, AA-Briefcase v1.1, GDPval-AA v2.1, AutomationBench-AA). Still trust the **rank order**; don't compare a number across Index versions.
- **Saturation watch:** GPQA Diamond (~94% top cluster) and τ²-Bench Telecom (~99%) have largely saturated; AIME 2025/2026 are at/near a perfect score for top models. Where a flagship bench has saturated, this file leads with a still-discriminating eval (HLE for reasoning, Terminal-Bench Hard for agents).
- **Stated context window ≠ usable context.** The long-context row cites a multi-needle retrieval eval at depth, not a spec-sheet number; advertised 1M (and larger) windows degrade sharply before their stated limit (Gemini 3.1 Pro: 84.9% at 128k → 26.3% at 1M). Newer 1M-window models (Claude Opus 5.5, and the open 1M models) publish no comparable 1M multi-needle number, so Opus 4.6's 76% remains the strongest *published* figure.
- **Open-weight ≠ pure-MIT — but the MIT tier just took the outright lead.** The new #1 open model, **MiMo-V2.6-Pro (46)**, is MIT-licensed; the next fully-MIT models are GLM-5.3 Flash (42), DeepSeek V4.1 Flash (39), DeepSeek V4 Pro (36) and GLM-5.2 (34). The #2–#3 open models (GLM-5.3, Kimi K3) and #5 (Qwen3.8) ship under bespoke licences. Kimi K3 also carries an unresolved distillation allegation (background, not re-verified this session). The rows rank on the independent AA Index but flag licence and provenance. Read the licence before deploying. **Sourcing note:** MiMo-V2.6-Pro's HF card returned HTTP 401 to the fetcher this session, so its open-weights/MIT facts rest on AA's independent model page + open-source board (both opened this session).
- **Cheapest-capable is time-of-day-dependent.** DeepSeek's peak/off-peak billing means "cheapest" depends on both the workload's input/output mix and the UTC hour — the row spells out both rate bands rather than a single number; GPT-5.6 Luna's flat rate (and a 3-point Index lead) keeps it #1.
- "Best" is a snapshot, not a law — models leapfrog weekly. The date on each row is load-bearing.
- Last full refresh: **2026-09-27**. Next scheduled: **2026-10-04** (Sunday 18:00 Europe/Rome).

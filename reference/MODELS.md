# MODELS.md — "Best at what" — refreshed _2026-09-06_ (weekly)

> **Opinion with receipts.** Every ranking below cites a **named benchmark + a
> number + a date + a primary URL** opened during the refresh. Benchmarks are gameable and
> often self-reported — treat them as evidence, not verdict. Self-reported numbers are
> flagged; independent / reproducible results are preferred. Refreshed weekly by
> `routines/models.md` only. Daily briefing runs never edit this file's rankings.

> **Dating convention.** Live third-party leaderboards (Artificial Analysis, etc.) carry no
> per-row publish timestamp; their date is the **access date (2026-09-06)** and the number is
> a live reading (P50 over a trailing 72h window for speed/leaderboards). Model cards, lab
> blogs and pricing pages carry their **publication date**. "Accessed" = read off the live page
> this session.

> **Frontier note (2026-09-06).** A busy week — **two categories changed leader and a third gained a
> new open-weight runner-up.** (1) **Multimodal changed hands:** **GPT-6 Astra (max)** — OpenAI's new
> flagship, "September 3, 2026" launch, proprietary — tops MMMU-Pro at **87%**, displacing last week's
> Gemini 3.7 Flash / Opus 5 co-lead (both 85%). (2) **Reasoning leader is a new model version:**
> **Claude Fable 5.1** now tops Humanity's Last Exam at **59.1%** (last week: Claude Fable 5, 55.5%) —
> the whole HLE top-3 is Fable 5.1 variants. (3) **Open-weight gained a #2:** **GLM-5.3** now has
> confirmed public weights on Hugging Face (`zai-org/GLM-5.3`, bespoke "glm-5.3" licence) and enters at
> **AA Intelligence Index 49**, second among open models behind Kimi K3 (50) — last refresh GLM-5.3 was
> held out for want of a primary open-weights card. (4) **Fastest reversed its slide:** Cerebras now
> serves gpt-oss-120b at a measured **1,848.7 t/s** (was 1,697.3 last week) — the three-week decline
> reversed. Rank-order leaders that **held**: **coding** (GPT-5.6 Sol max, Terminal-Bench Hard 65.9%),
> **long-context** (Opus 4.6, MRCR v2 76% at 1M), **agentic** (τ²-Bench saturated; Terminal-Bench Hard
> discriminating), **cheapest-capable** (GPT-5.6 Luna) and **open-weight #1** (Kimi K3).
> **Trust-no-one flag — AA rebased its Intelligence Index to v4.2 this refresh:** every score dropped
> ~10 points uniformly (Kimi K3 60 → 50, GPT-5.6 Luna 52 → 43, DeepSeek V4 Pro 53 → 42) because the
> Index changed methodology (now "incorporates 10 evaluations" including AA-Briefcase and GDPval-AA v2),
> **not** because models regressed. Compare **rank order**, not this week's absolute number against last
> week's. On the v4.2 board, **Claude Fable 5.1 (max)** leads at **57**, then **GPT-6 Astra (max) 55**,
> **GPT-6 Astra (xhigh) 54** tied with **Claude Opus 5 (max) 54**.

---

## Best at coding
1. **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent** — "independently benchmarked by Artificial Analysis." Agentic CLI eval (software-eng / sysadmin / data tasks scored programmatically in a Docker env). Holds #1 this refresh, ~3 pts clear of the runner-up; the page's summary line reads "GPT-5.6 Sol (max) scores the highest on Terminal-Bench Hard with a score of 65.9%." Re-verified this session; unchanged from last week. Note: OpenAI's newer GPT-6 Astra (max) tops the AA Intelligence Index and MMMU-Pro but does **not** displace GPT-5.6 Sol on this coding eval this session.
   - AA's summary names **Claude Fable 5 (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback)** the runner-up at **62.9%** ("followed by Claude Fable 5 … with a score of 62.9%, and GPT-5.6 Sol (medium) with a score of 62.9%") — Fable 5 and GPT-5.6 Sol (medium) tied at 62.9%. Unchanged this refresh. Vendor SWE-bench / Terminal-Bench self-reports run on a different harness than this independent CLI eval — never cross-compare a tuned vendor number against an independent one.
2. **Claude Fable 5** (Adaptive Reasoning, Max Effort, Opus 4.8 Fallback) — **Terminal-Bench Hard 62.9%** · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard) · **independent**. The page's named #2 this session, tied at 62.9% with **GPT-5.6 Sol (medium)** (the named #3). Holds the runner-up slot this refresh.

## Best at reasoning
1. **Claude Fable 5.1** (Adaptive Reasoning, Max Effort, Default Fallback) — **Humanity's Last Exam (no tools) 59.1%** · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam)
   - **Independent.** New this refresh: **Claude Fable 5.1** replaces last week's Claude Fable 5 (55.5%) at the top of HLE (questions resistant to retrieval — the eval still discriminates where GPQA has saturated). The page's summary line reads "Claude Fable 5.1 (Adaptive Reasoning, Max Effort, Default Fallback) scores the highest on Humanity's Last Exam with a score of 59.1%." Number is the *no-tools* figure (multimodal questions excluded for cross-model comparability); "with tools" framings circulate but aren't comparable.
   - Note: the top config carries a **"Default Fallback"** (Fable 5.1 hands off to a fallback model on tasks that trigger its safety guardrails, and the score bakes in that fallback). Fable 5.1 also leads the AA Intelligence Index (57) this session.
2. **Claude Fable 5.1** (Adaptive Reasoning, Xhigh Effort, Default Fallback) — **Humanity's Last Exam (no tools) 58.7%** · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/humanitys-last-exam) · **independent**. The page's named #2 ("followed by Claude Fable 5.1 (Adaptive Reasoning, Xhigh Effort, Default Fallback) with a score of 58.7%"); the named #3 is **Claude Fable 5.1 (High Effort) 55.9%** — the entire HLE top cluster is Claude Fable 5.1 this session. On the **near-saturated GPQA Diamond** the top cluster sits ~94% (against a ~70% human-expert baseline), so rank order there is within noise — HLE is the discriminating reasoning eval this session.

## Longest usable context
1. **Claude Opus 4.6** — stated **1M-token window (beta)** AND **MRCR v2 (8-needle) 76% at 1M tokens** · 2026-02-05 · [Anthropic](https://www.anthropic.com/news/claude-opus-4-6)
   - **Self-reported (Anthropic).** Strongest *verified* multi-needle score at true 1M depth (vs the predecessor Sonnet 4.5's 18.5% on the same test — "Opus 4.6 scores 76%, whereas Sonnet 4.5 scores just 18.5%"). Note: stated window ≠ usable window; the 1M tier is beta ("Opus 4.6 features a 1M token context window in beta"). Re-opened this session and the 76% figure still stands. The newer Claude tiers (Opus 5, Fable 5.1) and OpenAI's GPT-6 Astra ship no comparable *published* 1M multi-needle retrieval number opened this session, and the 1M-window open models (Qwen3.8 extensible to ~1.01M, DeepSeek-V4-Pro-0813, Kimi K3 — all ~1M-token windows) publish no comparable multi-needle figure either, so Opus 4.6 remains the strongest *published* 1M multi-needle number this refresh.
2. **Gemini 3.1 Pro** — stated **1M-token window**; **MRCR v2 (8-needle) 26.3% at 1M** (84.9% at 128k) · 2026-02-19 · [Google DeepMind model card](https://deepmind.google/models/model-cards/gemini-3-1-pro/)
   - **Self-reported (Google).** Holds up to ~128k but **collapses at 1M** — usable depth far below the advertised window. Re-opened this session; figures unchanged. The clearest illustration that a stated window is not a usable one.

## Best multimodal (vision / audio)
1. **GPT-6 Astra** (max) — **MMMU-Pro (vision) 87%** · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/mmmu-pro)
   - **Independent.** New leader this refresh. AA's MMMU-Pro page reads "GPT-6 Astra (max) scores the highest on MMMU-Pro with a score of 87%, followed by GPT-6 Astra (high) with a score of 86%, and GPT-6 Astra (xhigh) with a score of 86%." MMMU-Pro tests multi-discipline image+text reasoning in a vision-only input setting (questions embedded in images). GPT-6 Astra is a **released** proprietary OpenAI model — its [AA model page](https://artificialanalysis.ai/models/gpt-6-astra) gives a "September 3, 2026" launch, so present-tense is legitimate.
   - **Category changed hands.** Last week's co-lead — Gemini 3.7 Flash and Claude Opus 5, both at 85% — is displaced; GPT-6 Astra's variants now sweep the top three. Caveat: AA reports MMMU-Pro as a rounded whole percent with no per-row timestamp; the page shows 17 of 258 models scored (was 17/247 last week).
   - **Audio: no entry.** No reproducible primary audio-benchmark number found this session — dropped rather than guessed.

## Best agentic / tool use
1. _(Saturated — read with care)_ **τ²-Bench Telecom** top cluster **99.1%**: **GLM-5.2 (max)** and **JT-35B-Flash** tied; GLM-4.7-Flash (Reasoning) 98.8% · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/tau2-bench)
   - **Independent.** The canonical multi-turn tool-use bench (dual-control Dec-POMDP, customer-support domains) has **saturated** — a 35B model and open-weights models top it (AA's summary names GLM-5.2 (max) "the highest … with a score of 99.1%"), so it no longer separates frontier agents. Re-verified this session; unchanged. Trust-no-one read: stop ranking frontier agents by τ²-Bench.
2. _(Discriminating)_ **GPT-5.6 Sol** (max) — **Terminal-Bench Hard 65.9%** · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/evaluations/terminalbench-hard)
   - **Independent.** The agentic CLI eval still spreads the field (multi-step tasks in a Docker env); Claude Fable 5 and GPT-5.6 Sol (medium) tie at 62.9% behind it. Use this, not τ²-Bench, to compare top agents today.

## Cheapest capable
1. **GPT-5.6 Luna** (max) — **$0.20 in / $1.20 out per 1M tokens** · 2026-09-06 (accessed) · [AA model page](https://artificialanalysis.ai/models/gpt-5-6-luna)
   - Capability anchor: **Artificial Analysis Intelligence Index = 43** (independent, v4.2), read off the same page ("Released July 2026"; ranked #3 / 177 in its class). Holds #1 this refresh: Luna's **flat** $0.20/$1.20 is strictly cheaper than DeepSeek V4 Flash's standard listing (below) **and** now scores 2 Index points above it (43 vs 41) — last week the two were tied at Index 52, so Luna's lead widened. Pricing + capability both read off AA's independent model page (OpenAI's own pricing page has previously returned 5xx to this session-class).
2. **DeepSeek V4 Flash** (build 0731) — AA-listed **$0.44 in / $1.32 out per 1M tokens** · 2026-09-06 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-flash)
   - Capability anchor: **Artificial Analysis Intelligence Index = 41** (independent, v4.2; ranked #8 / 112 in its class).
   - **Flag (time-of-day billing, re-verified this session):** DeepSeek's official pricing page bills V4 Flash **peak/off-peak** — off-peak **$0.22 in / $0.66 out**, peak **$0.44 in / $1.32 out** ("Peak hours are 01:00 - 04:00 and 06:00 - 10:00 UTC, Monday through Friday (all other hours are off-peak)"; "Off-peak rates are half of the peak rates") · [DeepSeek official pricing](https://api-docs.deepseek.com/quick_start/pricing/). So V4 Flash's **off-peak output ($0.66)** remains the single cheapest output number in this row, but its input sits above Luna's and its peak rates are dominated by Luna — hence Luna keeps #1. Workload- and time-of-day-dependent, not a flat rate.

## Best open-weight
> Ranked on the independent **AA Intelligence Index v4.2** (rebased this refresh; see frontier note). Every entry's public weights were re-confirmed on its Hugging Face model card this session.
1. **Kimi K3** (Moonshot AI / `moonshotai`) — **AA Intelligence Index = 50** (independent; **#1 / 112 open-weight class**) · 2026-09-06 (accessed) · [AA model page](https://artificialanalysis.ai/models/kimi-k3)
   - Open weights re-confirmed on the [Hugging Face model card](https://huggingface.co/moonshotai/Kimi-K3) (opened this session): "We release the full Kimi K3 model weights under the Kimi K3 License", **2.8T total / 104B activated** parameters (a mixture-of-experts design that only runs part of the model per query), **1,048,576-token (1M) context**, downloadable un-gated. Holds its open-weight lead at Index 50 this refresh (v4.2), 1 Index point clear of the next open model (GLM-5.3, 49).
   - **Trust-no-one caveats:** (a) the licence is the bespoke **"Kimi K3 License"** (confirmed on the model card) — permissive but **not pure MIT**, so read the terms before commercial use; (b) there is an **unresolved US White House allegation** that Kimi K3 was built by distilling Anthropic's Claude Fable 5 (China's MOFCOM rejected it as evidence-free 27 Jul) — no imposed enforcement action either way as of this refresh. The ranking here is the **independent** AA Index, which is agnostic to that dispute.
2. **GLM-5.3** (Z.ai / `zai-org`) — **AA Intelligence Index = 49** (independent, v4.2) · 2026-09-06 (accessed) · [AA model page (Index board)](https://artificialanalysis.ai/models)
   - **New open-weight entry this refresh.** Last week GLM-5.3 was held out because no primary open-weights card was confirmed; this session the [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.3) (opened this session) exists with downloadable Safetensors weights (BF16 / F8_E4M3 / F32), **753B params**, under a bespoke **"glm-5.3" licence** (not MIT). On the AA Intelligence Index v4.2 board it reads 49, second among confirmed-open models behind Kimi K3. **Flag:** its explicit open-weight *class* rank was not shown on the model page opened this session — the #2 placement is on the Index score (49); read the bespoke licence before commercial use.
3. **Qwen3.8** (Alibaba / `Qwen`) — **AA Intelligence Index = 47** (independent, v4.2) · 2026-09-06 (accessed) · [AA model page](https://artificialanalysis.ai/models/qwen3-8-max)
   - Open weights are public: `Qwen/Qwen3.8-2.4T-A95B` ("Number of Parameters: 2.4T in total and 95B activated" mixture-of-experts; "Context Length: 262,144 natively and extensible up to 1,010,000 tokens"; downloadable Safetensors) · [HF model card](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) (re-opened this session).
   - **Flags:** AA now classifies the "**Qwen3.8 Max**" configuration (adds vision input / built-in tools / 1M-default over the raw base weights) as **proprietary** — Index 47, #28 / 202 overall, "model weights are not publicly available" — so the #3 open-weight placement here rests on the *base* open weights (`Qwen3.8-2.4T-A95B`) matched to the AA Index-47 score, not on the proprietary Max config. The licence is the bespoke **"qwen3.8-max"** licence (not confirmed OSI-permissive this session) — read it before commercial use.
4. **GLM-5.2** (Z.ai / `zai-org`) — license **MIT** · **AA Intelligence Index = 43** (independent, v4.2; **#6 / 112 open-weight class**) · 2026-09-06 (accessed) · [AA model page](https://artificialanalysis.ai/models/glm-5-2)
   - Still the strongest **fully-MIT** open model (Index 43, one point above the other MIT model, DeepSeek V4 Pro at 42; Kimi K3's, GLM-5.3's and Qwen3.8's licences are all bespoke). **753B-param** mixture-of-experts; MIT-licensed downloadable weights · [Hugging Face model card](https://huggingface.co/zai-org/GLM-5.2) (re-opened this session — licence "mit", 753B params, open download confirmed). Now superseded on raw capability by its own newer sibling GLM-5.3 (49), which trades MIT for a bespoke licence.
5. **DeepSeek V4 Pro 0813** (`deepseek-ai`) — license **MIT** · **AA Intelligence Index = 42** (independent, v4.2; **#7 / 112 open-weight class**) · 2026-09-06 (accessed) · [AA model page](https://artificialanalysis.ai/models/deepseek-v4-pro)
   - Open weights public: `deepseek-ai/DeepSeek-V4-Pro-0813`, MIT, not gated, mixture-of-experts routing, million-token context · [HF model card](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) (re-opened this session; MIT + open download confirmed, 154,525 downloads last month). The second fully-MIT open model, one Index point below GLM-5.2.

## Fastest (throughput)
1. **gpt-oss-120b on Cerebras** — **1,848.7 tokens/sec** (median output, P50 over trailing 72h) · 2026-09-06 (accessed) · [Artificial Analysis](https://artificialanalysis.ai/models/gpt-oss-120b/providers)
   - **Independent** (Artificial Analysis measured; "Figures represent median (P50) measurement over the past 72 hours"). **Up from 1,697.3 t/s last week** — the three-week decline (1,747.9 → 1,732.6 → 1,697.3) reversed this refresh. Next providers far behind: SambaNova 711.0, Groq 476.1 t/s. Caveat: this is sustained *measured median*; Cerebras's own marketing cites ~3,000 t/s — a **vendor peak / self-reported** figure, well above the independently measured median.

---

## Methodology & limits
- Every claim carries a named benchmark, a number, a date, and a primary URL opened during this refresh (2026-09-06). Headline numbers were re-fetched and read off the page by the editor, not filled from memory.
- Self-reported numbers are labelled; third-party / reproducible evals (Artificial Analysis runs its own) are preferred. Vendor self-reports run materially above standardised harnesses — never cross-compare the two.
- **Movement this week.** Two categories changed leader — **multimodal** (Gemini 3.7 Flash / Opus 5 → GPT-6 Astra max, 87% MMMU-Pro) and the **reasoning** top slot (Claude Fable 5 → the new Claude Fable 5.1, 59.1% HLE) — and **open-weight** gained a #2 (GLM-5.3, now with confirmed public weights, Index 49). Fastest reversed its multi-week slide (Cerebras 1,697.3 → 1,848.7 t/s). Coding, long-context, agentic, cheapest-capable and open-weight #1 held.
- **AA Intelligence Index rebased to v4.2 this refresh.** Every Index score fell ~10 points uniformly (Kimi K3 60 → 50, GPT-5.6 Luna 52 → 43, DeepSeek V4 Pro 53 → 42, GLM-5.2 53 → 43) because the Index changed its evaluation set (now "incorporates 10 evaluations" including AA-Briefcase and GDPval-AA v2) — **not** because models regressed. Trust the **rank order**; do not compare this week's absolute Index number against last week's.
- **Saturation watch:** GPQA Diamond (~94% top cluster) and τ²-Bench Telecom (~99%) have largely saturated; AIME 2025/2026 are at/near a perfect score for top models. Where a flagship bench has saturated, this file leads with a still-discriminating eval (HLE for reasoning, Terminal-Bench Hard for agents).
- **Stated context window ≠ usable context.** The long-context row cites a multi-needle retrieval eval at depth, not a spec-sheet number; advertised 1M (and larger) windows degrade sharply before their stated limit (Gemini 3.1 Pro: 84.9% at 128k → 26.3% at 1M).
- **Open-weight ≠ pure-MIT.** This refresh's #1–#3 open models (Kimi K3, GLM-5.3, Qwen3.8) ship under bespoke licences; only GLM-5.2 and DeepSeek V4 Pro are MIT. Kimi K3 also carries an unresolved distillation allegation. The rows rank on the independent AA Index but flag licence and provenance. Read the licence before deploying.
- **Cheapest-capable is time-of-day-dependent.** DeepSeek's peak/off-peak billing means "cheapest" depends on both the workload's input/output mix and the UTC hour — the row spells out both rate bands rather than a single number; GPT-5.6 Luna's flat rate (and now a 2-point Index lead) keeps it #1.
- "Best" is a snapshot, not a law — models leapfrog weekly. The date on each row is load-bearing.
- Last full refresh: **2026-09-06**. Next scheduled: **2026-09-13** (Sunday 18:00 Europe/Rome).
</content>
</invoke>

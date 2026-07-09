# Tracked Threads — last updated 2026-07-09 07:00 Europe/Rome

Continuity state for the AI/LLM briefing. Read first, rewritten last, on every run
(including skips). Committed to the repo so cloud runs share memory. Keep it small.

Fields per thread:
- **Status** — developing | steady | dormant | closed
- **Last material update** — date the situation last actually moved
- **Last POSTED** — the run slot that last shipped a beat on this thread (or "never")
- **One-line state** — what we currently understand, so the next run builds on it
- **Watch for** — the specific next development that would justify a post
- **Receipts** — primary-source URLs

---

## Active threads

### T7 — xAI / Grok frontier line (SpaceXAI)
- **Status:** developing (opened 09 Jul 2026)
- **Last material update:** 2026-07-08 (Grok 4.5 released)
- **Last POSTED:** 2026-07-09 20:00 (Grok 4.5 release)
- **One-line state:** On 08 Jul xAI — now branded **SpaceXAI** on its own site ("SpaceXAI — Creators of Grok") — released **Grok 4.5**, available that day on the xAI API, in Grok Build, in Cursor (all plans) and from the SpaceXAI console; broad/consumer availability framed by Musk as "tomorrow" (09 Jul); NOT yet available in the EU. Primary x.ai/news/grok-4-5 reports SWE-Bench Pro resolve rate 64.7% (vs Opus 4.7 64.3%, Opus 4.8 max 69.2%), Terminal-Bench 2.1 83.3%; pricing $2/M input + $6/M output; trained across tens of thousands of Nvidia GB300 GPUs; ~2x token efficiency (avg 15,954 output tokens/task, ~4.2× fewer than Opus 4.8 max at 67,020). Musk's "Opus-class model" framing is his own label (via TechCrunch), not on the x.ai page — not shipped. POSTED 09 Jul 20:00.
- **Watch for:** independent third-party benchmarks for Grok 4.5; EU availability; a higher tier or a Grok 4.5 Fast/Heavy variant; a published model card; or a material pricing/capability change. Musk-tweet superlatives with no number do not clear the gate. Note: x.ai/news pages 403 to the automated fetcher but resolve via domain-scoped search.
- **Receipts:**
  - https://x.ai/news/grok-4-5 (08 Jul — Grok 4.5 release, benchmarks, pricing, GB300 training — POSTED 09 Jul 20:00)
  - https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/ (Tier-2 corroboration; Musk "Opus-class" quote)

### T5 — US government gating of frontier-model release / access
- **Status:** developing (GPT-5.6 clearance imminent — the gate this thread watched is lifting)
- **Last material update:** 2026-07-08 (OpenAI says US government cleared GPT-5.6 for broad release; public rollout "Thursday"/this week)
- **Last POSTED:** 2026-06-26 20:00 (GPT-5.6 limited preview, access held at the US government's request)
- **One-line state:** A pattern where the US government conditions who can access frontier models on national-security grounds. First instance was T1 (12 Jun export-control directive forcing Anthropic to suspend Fable 5 / Mythos 5; both controls fully lifted 30 Jun, Fable 5 back 1 Jul, safeguards regime published 2 Jul — see T1). Second: on 26 Jun OpenAI began a *limited preview* of GPT-5.6 (Sol/Terra/Luna) restricted to ~20 government-shared partners (POSTED 26 Jun 20:00). **On 08 Jul this is lifting: OpenAI published "Our approach to government and national security partnerships" and said (per Axios/CNBC/Bloomberg + TechCrunch) the US Commerce Dept cleared GPT-5.6 for wide public release, with the Sol/Terra/Luna rollout "Thursday"/this week and a new executive-order cyber framework + "repeatable process for future model releases" in the works.** NOT shipped this session: no openable allowlisted primary (openai.com/index/government-national-security-partnerships 403s; reuters/apnews/theverge/arstechnica blocked to the fetcher; no dedicated openable TechCrunch clearance article surfaced), OpenAI RSS shows no GA post yet, and modality is still announced/"will release." Aggregators restate per-tier pricing (Sol $5/$30, Terra $2.50/$15, Luna $1/$6).
- **Watch for:** an OPENABLE OpenAI/White-House primary confirming GPT-5.6 GA (a dated public release lifting the preview), a named/expanded partner list or the "repeatable process" / executive-order cyber framework, OR a published GPT-5.6 benchmark number — any of these is an ADVANCE. Restatement of the same "coming this week" via blocked/paywalled outlets does not clear the gate; the clearance ships the moment an allowlisted openable source (openai.com GA post, or an openable TechCrunch/other Tier-2) carries it. **09 Jul 07:00 recheck:** GA is promised "Thursday" (09 Jul) but not yet shippable — OpenAI RSS shows no GA post (newest: 08 Jul GPT-Live + government-partnerships + the SWE-Bench-Pro evaluation note), openai.com/index pages still 403, modality still preview/"coming July 9." Hold.
- **Receipts:**
  - https://openai.com/index/government-national-security-partnerships (08 Jul — OpenAI on the government partnership process; 403s to automated fetch; confirmed via openai.com RSS description)
  - https://deploymentsafety.openai.com/gpt-5-6-preview (GPT-5.6 preview system card — limited preview, government-shared partners, High cyber capability — POSTED 26 Jun 20:00)
  - https://openai.com/index/previewing-gpt-5-6-sol/ (canonical preview announcement; 403s to automated fetch)

### T1 — Anthropic × policy / legislation ("the mythos")
- **Status:** developing (release arc resolved 1 Jul; safeguards regime published 2 Jul; watch shifts to litigation + how the CJS framework evolves)
- **Last material update:** 2026-07-02 (Anthropic newsroom "More details on Fable 5's cyber safeguards and our jailbreak framework" — safety-classifier tiers gating Fable 5 + early-draft industry-wide Cyber Jailbreak Severity (CJS) framework)
- **Last POSTED:** 2026-07-03 07:00 (the CJS safeguards framework — early-draft jailbreak-severity scale CJS-0→CJS-4, with Amazon/Microsoft/Google + other Glasswing partners)
- **One-line state:** On 12 Jun the US government (Commerce Sec. Lutnick, via BIS) forced Anthropic to disable Claude Fable 5 and Mythos 5 worldwide; a customer (Legion LegalTech) sued the US in D.D.C. (1:26-cv-02225) on 23 Jun (POSTED 25 Jun 20:00); Lutnick cleared Mythos 5 for 100+ US orgs on 26 Jun (POSTED 27 Jun 13:00); on 30 Jun Anthropic published "Redeploying Fable 5" — controls lifted, Fable 5 back globally 1 Jul, CAISI called safeguards "extraordinarily strong" (POSTED 01 Jul 07:00). On 02 Jul the Fable 5 cyber safety-classifier tiers + early-draft CJS framework published (POSTED 03 Jul 07:00 as a T1 ADVANCE). Litigation strand (procedural, secondary-only): govt response due 14 Jul, plaintiff reply 21 Jul, PI hearing no earlier than week of 27 Jul, Judge Richard J. Leon. Still secondary-only / unshippable: NSA red-team claim (via Sen. Warner); Garbarino "Fly Out Day" anecdote; "Beijing blacklisted 56 American firms."
- **Watch for:** a ruling on the Legion LegalTech PI motion (grant/deny) or the government's filed response (14 Jul); a finalized/revised CJS framework or a named benchmark/block-rate number on the Fable 5 classifier; a PRIMARY government source (Commerce/BIS/White House); or a PRIMARY on the NSA red-team claim. Don't re-post the bare restoration (01 Jul) or the draft CJS framework (03 Jul).
- **09 Jul 20:00 recheck (covers 05→09 Jul gap):** Anthropic newsroom newest is 06 Jul — "Government of Alberta uses Claude to find/fix cybersecurity vulnerabilities" (case study) and "The Making of Claude Code" (feature); neither is a new model, benchmark, or policy step. No docket ruling (still the pre-14-Jul briefing schedule). Unchanged — nothing to advance.
- **Receipts:**
  - https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (02 Jul — classifier tiers + early-draft CJS framework — POSTED 03 Jul 07:00)
  - https://www.anthropic.com/news/redeploying-fable-5 (30 Jun — export controls lifted; Fable 5 returns 1 Jul — POSTED 01 Jul 07:00)
  - https://www.courtlistener.com/docket/73520460/legion-legaltech-corp-v-united-states-of-america/ (Legion LegalTech v. United States, 1:26-cv-02225, D.D.C., filed 23 Jun — POSTED 25 Jun 20:00)
  - https://www.anthropic.com/news/fable-mythos-access (12 Jun suspension statement)

### T2 — EU sovereign AI / open-vs-closed
- **Status:** developing
- **Last material update:** 2026-06-19 (EUROPA consortium selected)
- **Last POSTED:** 2026-06-22 20:00 (EUROPA selection)
- **One-line state:** The European Commission selected the EUROPA consortium, led by Italian firm Domyn, to build an open-source frontier model (>400B parameters) covering all 24 official EU languages on European infrastructure — winner of its Frontier AI Grand Challenge, part of the EU Technological Sovereignty Package (3 Jun). A sovereignty/open-weights bet against the US-lab closed frontier.
- **Watch for:** a concrete training milestone, a named compute/EuroHPC allocation or funding figure, a model card / weights release, or a benchmark from EUROPA. Speculation/timeline chatter does not clear the gate. Note: Grok 4.5 (T7) launched NOT available in the EU — a live example of the access-fragmentation this thread is about, but not itself an EUROPA-side movement. 09 Jul 07:00 recheck: the 07 Jul EU Action Plan on Cybersecurity and AI (posted under T3) reaffirms funding sovereign AI Factories/Gigafactories — a sovereignty tie, but no EUROPA-side movement.
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open

### T3 — AI for cyber-defence / vulnerability discovery
- **Status:** developing
- **Last material update:** 2026-07-07 (European Commission presents the EU Action Plan on Cybersecurity and AI)
- **Last POSTED:** 2026-07-09 07:00 (EU Action Plan on Cybersecurity and AI)
- **One-line state:** On 07 Jul the European Commission presented an **Action Plan on Cybersecurity and AI** (3 objectives: safe advanced-AI use; reinforce EU cyber resilience; scale EU AI-for-cyber capabilities). Named actions, all future/non-binding: strengthen Europe's own capacity to **evaluate AI models before they are placed on the EU market, in line with the AI Act**; work with ENISA on a European Blueprint + a **secure testing platform** for critical sectors (energy, transport, health, finance, public administration); launch an **EU Grand Challenge on AI for cybersecurity**. No implementation dates or funding figures in the document. POSTED 09 Jul 07:00 (first T3 beat; T2 sovereignty tie). Prior strands still live: (1) OpenAI's 22 Jun Daybreak / GPT-5.5-Cyber benchmarks (e.g. 85.6% CyberGym) remain NON-verified from primary. (2) GPT-5.6 rated "High" in Cybersecurity per OpenAI's openable Deployment Safety Hub system card (26 Jun post under T5). (3) 02 Jul Anthropic Fable 5 cyber-classifier tiers + draft CJS framework (shipped under T1 03 Jul). Note: OpenAI's 08 Jul "Separating signal from noise in coding evaluations" flags reliability issues in SWE-Bench Pro — the benchmark Grok 4.5 (T7) headlines (64.7%); a possible evaluation-integrity angle, not yet a beat (openai.com page 403s).
- **Watch for:** a concrete step out of the Action Plan (ENISA platform launch, the Grand Challenge opening, a named funding/date figure, or the model-evaluation capacity going live); an openable allowlisted primary confirming GPT-5.5-Cyber + its benchmark numbers; a published GPT-5.6 cyber benchmark with a number; a finalized CJS framework or a Fable 5 classifier block-rate number. Don't re-post the bare Action Plan presentation (09 Jul).
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence (07 Jul — EU Action Plan on Cybersecurity and AI — POSTED 09 Jul 07:00; presscorner ip_26_1544 is the press-release twin but 403s/SPA-shells to the fetcher)
  - https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (02 Jul — cyber-safeguard classifier tiers + CJS framework)
  - https://deploymentsafety.openai.com/gpt-5-6-preview (GPT-5.6 preview system card — "High" cyber capability)
  - https://techcrunch.com/2026/06/22/openai-launches-new-initiative-to-help-find-and-patch-open-source-bugs/ (Patch the Planet + Trail of Bits)

### T4 — OpenAI custom silicon / Nvidia challenge
- **Status:** developing
- **Last material update:** 2026-06-24 (Jalapeño chip unveiled)
- **Last POSTED:** 2026-06-24 20:00 (Jalapeño unveiling)
- **One-line state:** On 24 Jun OpenAI and Broadcom unveiled Jalapeño, OpenAI's first custom inference chip (an "Intelligence Processor") — built for inference, still in testing; reported (unverified) aim is initial deployment by end of 2026. OpenAI's primary page 403s, Broadcom IR 503s to automated fetch, so the beat linked TechCrunch. The "performance-per-watt substantially better" line is unbenchmarked and was not shipped.
- **Watch for:** a confirmed tape-out/manufacturing or first-deployment milestone, named specs or an independent benchmark, a successor chip, or an openable primary carrying specs. Note (backdrop, not T4): Grok 4.5 (T7) reports training on tens of thousands of Nvidia GB300 GPUs — the incumbent-Nvidia side of the same buildout. 09 Jul 20:00 recheck: no OpenAI/Broadcom silicon update.
- **Receipts:**
  - https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
  - https://openai.com/index/openai-broadcom-jalapeno-inference-chip/ (primary; 403s to automated fetch)

### T6 — Anthropic Claude 5 family rollout (post-suspension release line)
- **Status:** developing
- **Last material update:** 2026-06-30 (Claude Sonnet 5 released; "Redeploying Fable 5" restores the flagship — see T1)
- **Last POSTED:** 2026-06-30 20:00 (Claude Sonnet 5 release)
- **One-line state:** On 30 Jun Anthropic released **Claude Sonnet 5** (Claude.ai, API as `claude-sonnet-5`, AWS, Google Cloud, Microsoft Foundry) — "the most agentic Sonnet model yet." Reported: OSWorld-Verified 78.5%; Humanity's Last Exam 34.6% no-tools / 46.8% with-tools. Introductory pricing $2/M input + $10/M output through 31 Aug 2026, then $3/M + $15/M. With Fable 5 back (1 Jul) and Sonnet 5 out, the Claude 5 line is broadly live post-suspension. POSTED 30 Jun 20:00.
- **Watch for:** a higher-tier Claude 5 release (e.g. an Opus-line model), a published SWE-bench Verified or other coding number for Sonnet 5 or Fable 5, an independent third-party benchmark, or a material capability/pricing change. A restatement of the 30 Jun launches does not re-clear. 09 Jul 20:00 recheck (covers 05→09 Jul gap): Anthropic newsroom newest is 06 Jul (two case studies + a Claude Code feature); no Opus-line release, no new Sonnet 5 / Fable 5 benchmark number. Unchanged.
- **Receipts:**
  - https://www.anthropic.com/news/claude-sonnet-5 (Claude Sonnet 5 release — POSTED 30 Jun 20:00)
  - https://www.anthropic.com/claude/sonnet (product page)

---

## Dormant threads (watch, don't post unless reignited)

_none yet_

---

## Recently closed

_none yet_

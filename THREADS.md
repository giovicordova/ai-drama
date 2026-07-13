# Tracked Threads — last updated 2026-07-13 07:00 Europe/Rome

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

### T9 — AI for mathematics / autonomous proof (frontier models producing novel proofs)
- **Status:** developing (opened 12 Jul 2026)
- **Last material update:** 2026-07-12 (OpenAI published a proof of the Cycle Double Cover Conjecture credited to GPT-5.6 Sol Ultra)
- **Last POSTED:** 2026-07-12 20:00 (Cycle Double Cover Conjecture proof credited to GPT-5.6 Sol Ultra)
- **One-line state:** On ~12 Jul (within ~8h before the 20:00 run) OpenAI posted two PDFs on `cdn.openai.com` — a **proof** ("A Proof of the Cycle Double Cover Conjecture") and the **prompt** used — crediting the proof *entirely* to **GPT-5.6 Sol Ultra**. Primary verbatim: proof PDF "Statement of AI use. The proof in this note is entirely due to GPT 5.6 Sol Ultra and the writeup with Codex (with GPT 5.6 Sol)"; Theorem 1.1 "Every finite bridgeless undirected graph has a cycle double cover"; prompt PDF "You have up to 64 concurrent agents available." The conjecture (posed by Tutte, Itai and Rodeh, Szekeres, Seymour): every bridgeless graph has a multiset of cycles covering each edge exactly twice. POSTED 12 Jul 20:00, anchored to the proof PDF; framed as *published/credits*, NOT a settled result — self-published preprint, not peer-reviewed, and the conjecture has a history of proofs later found to have gaps (secondary, kept out of post). "64 agents" lives only in the prompt PDF and was kept out of the single-URL post; "under an hour"/"50 years" are secondary-only.
- **Watch for:** an independent/peer expert verdict on the proof's correctness (confirmation OR a found gap — either is a beat) **carried by an allowlisted primary** (a mathematician's tweet/HN post is hard-banned §5 and does not qualify); an OpenAI blog/index page (openable) framing the achievement; a further AI-generated proof of another named open problem; or Sol Ultra confirmed as a publicly available/priced tier. Do NOT re-post the bare 12 Jul proof drop. A restated "AI solves 50-yr problem" via aggregators with no new primary does not clear the gate. **13 Jul 07:00 recheck:** reported expert reaction exists — mathematician Thomas Bloom reportedly called the proof "very nice" and "elementary" but criticised its complete lack of citations (a foundational 1983 Bermond–Jackson–Jaeger paper unmentioned) — BUT it surfaces only via Hacker News / X and aggregators (The Decoder, MLQ, officechai), all non-allowlisted, and reads as a citations/scholarship critique, not a stated correctness confirmation or a found logical gap. Not shippable; noted only. No OpenAI index/blog framing page, no further AI-generated proof.
- **Receipts:**
  - https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf (proof PDF — title, Theorem 1.1, "Statement of AI use" attribution to GPT 5.6 Sol Ultra — POSTED 12 Jul 20:00; extracts via zlib, WebFetch/Read PDF rendering unavailable in-env)
  - https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf (prompt PDF — "given to GPT 5.6 Sol Ultra"; "up to 64 concurrent agents"; multiagent-v2 instructions)

### T8 — Meta frontier / agentic-coding line (Muse Spark, Meta Superintelligence Labs)
- **Status:** developing (opened 10 Jul 2026)
- **Last material update:** 2026-07-09 (Muse Spark 1.1 released + Meta Model API opened)
- **Last POSTED:** 2026-07-10 13:00 (Muse Spark 1.1 release)
- **One-line state:** On 09 Jul Meta released **Muse Spark 1.1**, a multimodal reasoning model built for agentic tasks (major gains in tool/computer use, coding, multimodal understanding), with a **1-million-token context window**. Available now in "Thinking" mode in the Meta AI app and on meta.ai; the new **Meta Model API** is in public preview for developers. Muse Spark 1.1 is a point iteration of Muse Spark (base launched Apr 2026 — "ground-up overhaul" of Meta's AI, Meta Superintelligence Labs), but its notable news is the substantial agentic/coding gains **plus** Meta shipping its own paid model API — Meta's entry into the agentic-coding market against OpenAI/Anthropic. POSTED 10 Jul 13:00, anchored strictly to the Meta blog primary (no benchmark, no pricing — neither is on the linked page). Pricing $1.25/M input + $4.25/M output reported only via Reuters-through-TechCrunch (not on primary); a Meta "Muse Spark 1.1 Evaluation Report" PDF exists but did not extract (no page renderer).
- **Watch for:** a named benchmark figure from the Muse Spark 1.1 Evaluation Report or an independent third-party benchmark (SWE-bench Verified / Terminal-Bench / coding-agent index with a number); open-weights availability; a higher tier or a Muse Spark 2 release; or a material pricing/availability change (e.g. Model API leaving preview / EU availability). Don't re-post the bare 09 Jul release. Vague "major gains" with no number does not clear the gate. **11 Jul 20:00 → 12 Jul 07:00/13:00 rechecks:** unchanged — HF newest is community Qwen/RWKV/Gemma finetunes, no Meta primary movement; no benchmark, tier, or pricing change; Model API still public preview. **12 Jul 20:00 recheck:** unchanged — HF newest is community uploads incl. a community **GLM-5.2 GGUF re-quant** (GLM-5.2 is Z.ai's 13/16 Jun release, not new); no Meta primary movement; no benchmark, tier, or pricing change; Model API still public preview. **13 Jul 07:00 recheck:** unchanged — HF newest still community uploads (Qwen3.6 quant, Quacken-FP8, test repos); no Meta primary movement; Model API still public preview.
- **Receipts:**
  - https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/ (09 Jul — Muse Spark 1.1 release + Meta Model API public preview; OPENABLE to the fetcher — POSTED 10 Jul 13:00)
  - https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report (Muse Spark 1.1 Evaluation Report — 1.7 MB PDF, did not extract to the fetcher)
  - https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/ (Apr 2026 — original Muse Spark launch, Meta Superintelligence Labs)
  - https://techcrunch.com/2026/07/09/meta-enters-the-crowded-ai-coding-battle-with-muse-spark-1-1/ (Tier-2 — GA framing + $1.25/$4.25 pricing via Reuters)

### T5 — US government gating of frontier-model release / access
- **Status:** developing (GPT-5.6 GA shipped 09 Jul; system card POSTED 10 Jul 07:00; GA + per-tier pricing ADVANCE POSTED 10 Jul 20:00)
- **Last material update:** 2026-07-12 (GPT-5.6 "Sol Ultra" tier confirmed real via OpenAI primary — the cycle-double-cover proof PDFs; capability beat shipped under T9)
- **Last POSTED:** 2026-07-10 20:00 (GPT-5.6 GA + per-tier pricing — GA across ChatGPT/Codex/API; Sol $5/$30, Terra $2.50/$15, Luna $1/$6, plain facts via TechCrunch Tier-2; no best-at-X claim shipped)
- **One-line state:** A pattern where the US government conditions who can access frontier models on national-security grounds. First instance was T1 (12 Jun export-control directive forcing Anthropic to suspend Fable 5 / Mythos 5; both controls fully lifted 30 Jun, Fable 5 back 1 Jul, safeguards regime published 2 Jul — see T1). Second: on 26 Jun OpenAI began a *limited preview* of GPT-5.6 (Sol/Terra/Luna) restricted to ~20 government-shared partners (POSTED 26 Jun 20:00); the US Commerce Dept then cleared it for broad release, GA shipping mid-day 09 Jul across ChatGPT/Codex/API. **10 Jul 07:00: POSTED the GPT-5.6 system card** via `deploymentsafety.openai.com/gpt-5-6` — Sol/Terra/Luna "High" in both Cybersecurity and Biological & Chemical, none reaching High in AI Self-Improvement; HealthBench Professional (Sol 60.5, +8.7); verbatim cyber-capability sentence. **10 Jul 20:00: POSTED the GA + per-tier pricing ADVANCE** — GA + per-tier API pricing (Sol $5/$30, Terra $2.50/$15, Luna $1/$6), anchored to the openable Tier-2 primary (TechCrunch). The best-at-X headline (Coding Agent Index 80, "state of the art") was **deliberately excluded** — Tier-2 can't sole-source a best-at-X claim, and `openai.com/index/gpt-5-6` still 403s. **12 Jul 20:00: "Sol Ultra" now confirmed as a real GPT-5.6 tier** via OpenAI primary (the `cdn.openai.com` cycle-double-cover proof PDFs credit "GPT 5.6 Sol Ultra") — the tier-existence Watch-for is satisfied; the capability beat itself shipped under **T9**, not as a T5 gating beat.
- **Watch for:** an openable allowlisted primary or independent third-party benchmark for the "state of the art"/Coding Agent Index claim (that would let the best-at-X beat ship); a White-House/Commerce primary on the clearance; the `openai.com/index` page rendering to the fetcher; a material pricing change or Sol Ultra becoming a publicly available/priced tier. Do NOT re-post the system-card designations (07:00) or the bare GA/pricing (20:00). The bare existence of the Sol Ultra tier is now noted (12 Jul) — don't re-post that either. **11 Jul 20:00 → 12 Jul 07:00/13:00 rechecks:** `openai.com/index/gpt-5-6` still 403s → best-at-X still blocked; OpenAI news newest still the 10 Jul Deutsche Telekom story; no fresh 10–12 Jul White-House/Commerce clearance primary. Both GPT-5.6 GA beats stay shipped. **12 Jul 20:00 recheck:** `openai.com/index/gpt-5-6` still 403s → best-at-X still blocked; OpenAI news newest still the 10 Jul Deutsche Telekom story atop the 09 Jul GPT-5.6 items; no fresh clearance primary. The `cdn.openai.com` proof PDFs are a *capability* artifact (→ T9), not a gating/clearance movement. Both GA beats stay shipped. **13 Jul 07:00 recheck:** OpenAI news newest still the 10 Jul Deutsche Telekom story; best-at-X still reported-only; no fresh White-House/Commerce clearance primary. Both GA beats stay shipped.
- **Receipts:**
  - https://deploymentsafety.openai.com/gpt-5-6 (09 Jul — GPT-5.6 GA system card; OPENABLE; final Preparedness designations + benchmark figures — POSTED 10 Jul 07:00)
  - https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/ (09 Jul — Tier-2, GA + per-tier pricing + Coding Agent Index; OPENABLE — GA/pricing ADVANCE POSTED 10 Jul 20:00)
  - https://openai.com/index/gpt-5-6 (09 Jul — GPT-5.6 GA / pricing marketing page; still 403s to automated fetch)
  - https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf (12 Jul — proof PDF confirming "GPT 5.6 Sol Ultra" as a tier; capability beat shipped under T9)
  - https://deploymentsafety.openai.com/gpt-5-6-preview (GPT-5.6 preview system card — POSTED 26 Jun 20:00)

### T7 — xAI / Grok frontier line (SpaceXAI)
- **Status:** developing (opened 09 Jul 2026)
- **Last material update:** 2026-07-08 (Grok 4.5 released)
- **Last POSTED:** 2026-07-09 20:00 (Grok 4.5 release)
- **One-line state:** On 08 Jul xAI — now branded **SpaceXAI** ("SpaceXAI — Creators of Grok") — released **Grok 4.5**, available that day on the xAI API, in Grok Build, in Cursor (all plans) and from the SpaceXAI console; broad/consumer availability framed by Musk as "tomorrow" (09 Jul); NOT yet available in the EU. Primary x.ai/news/grok-4-5 reports SWE-Bench Pro resolve rate 64.7% (vs Opus 4.7 64.3%, Opus 4.8 max 69.2%), Terminal-Bench 2.1 83.3%; pricing $2/M input + $6/M output; trained across tens of thousands of Nvidia GB300 GPUs; ~2x token efficiency. Musk's "Opus-class model" framing is his own label (via TechCrunch), not on the x.ai page. POSTED 09 Jul 20:00.
- **Watch for:** independent third-party benchmarks for Grok 4.5; EU availability; a higher tier or a Grok 4.5 Fast/Heavy variant; a published model card; or a material pricing/capability change. Musk-tweet superlatives with no number do not clear the gate. Note: x.ai/news pages 403 to the automated fetcher but resolve via domain-scoped search. **11 Jul 20:00 → 12 Jul 07:00/13:00/20:00 rechecks:** unchanged — no independent third-party benchmark from an allowlisted source, no EU availability, no model card, no new tier. **13 Jul 07:00 recheck:** unchanged.
- **Receipts:**
  - https://x.ai/news/grok-4-5 (08 Jul — Grok 4.5 release, benchmarks, pricing, GB300 training — POSTED 09 Jul 20:00)
  - https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/ (Tier-2 corroboration; Musk "Opus-class" quote)

### T1 — Anthropic × policy / legislation ("the mythos")
- **Status:** developing (release arc resolved 1 Jul; safeguards regime published 2 Jul; watch shifts to litigation + how the CJS framework evolves)
- **Last material update:** 2026-07-02 (Anthropic newsroom "More details on Fable 5's cyber safeguards and our jailbreak framework" — safety-classifier tiers gating Fable 5 + early-draft industry-wide Cyber Jailbreak Severity (CJS) framework)
- **Last POSTED:** 2026-07-03 07:00 (the CJS safeguards framework — early-draft jailbreak-severity scale CJS-0→CJS-4, with Amazon/Microsoft/Google + other Glasswing partners)
- **One-line state:** On 12 Jun the US government (Commerce Sec. Lutnick, via BIS) forced Anthropic to disable Claude Fable 5 and Mythos 5 worldwide; a customer (Legion LegalTech) sued the US in D.D.C. (1:26-cv-02225) on 23 Jun (POSTED 25 Jun 20:00); Lutnick cleared Mythos 5 for 100+ US orgs on 26 Jun (POSTED 27 Jun 13:00); on 30 Jun Anthropic published "Redeploying Fable 5" — controls lifted, Fable 5 back globally 1 Jul, CAISI called safeguards "extraordinarily strong" (POSTED 01 Jul 07:00). On 02 Jul the Fable 5 cyber safety-classifier tiers + early-draft CJS framework published (POSTED 03 Jul 07:00 as a T1 ADVANCE). Litigation strand (procedural, secondary-only): govt response due 14 Jul, plaintiff reply 21 Jul, PI hearing no earlier than week of 27 Jul, Judge Richard J. Leon. Still secondary-only / unshippable: NSA red-team claim (via Sen. Warner); Garbarino "Fly Out Day" anecdote; "Beijing blacklisted 56 American firms."
- **Watch for:** a ruling on the Legion LegalTech PI motion (grant/deny) or the government's filed response (14 Jul); a finalized/revised CJS framework or a named benchmark/block-rate number on the Fable 5 classifier; a PRIMARY government source (Commerce/BIS/White House); or a PRIMARY on the NSA red-team claim. Don't re-post the bare restoration (01 Jul) or the draft CJS framework (03 Jul). **11 Jul 20:00 → 12 Jul 07:00/13:00/20:00 rechecks:** unchanged — Anthropic newsroom newest still the 09 Jul items (Bernanke→LTBT; "Inviting hard questions"; Claude-reflection; UST case study) (+ 06 Jul Alberta case study); no docket ruling; government response due 14 Jul; schedule holds. **13 Jul 07:00 recheck:** unchanged — newsroom newest still the 09 Jul items; government response due **tomorrow, 14 Jul** — watch that filing next.
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
- **Watch for:** a concrete training milestone, a named compute/EuroHPC allocation or funding figure, a model card / weights release, or a benchmark from EUROPA. Speculation/timeline chatter does not clear the gate. Note: Grok 4.5 (T7) launched NOT available in the EU — a live example of the access-fragmentation this thread is about, but not an EUROPA-side movement. 10–11 Jul (all slots) + 12 Jul 07:00/13:00/20:00 + 13 Jul 07:00 rechecks: no EUROPA-side movement.
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open

### T3 — AI for cyber-defence / vulnerability discovery
- **Status:** developing
- **Last material update:** 2026-07-07 (European Commission presents the EU Action Plan on Cybersecurity and AI)
- **Last POSTED:** 2026-07-09 07:00 (EU Action Plan on Cybersecurity and AI)
- **One-line state:** On 07 Jul the European Commission presented an **Action Plan on Cybersecurity and AI** (3 objectives: safe advanced-AI use; reinforce EU cyber resilience; scale EU AI-for-cyber capabilities). Named actions, all future/non-binding: strengthen Europe's capacity to **evaluate AI models before they are placed on the EU market, in line with the AI Act**; work with ENISA on a European Blueprint + a **secure testing platform** for critical sectors; launch an **EU Grand Challenge on AI for cybersecurity**. No implementation dates or funding figures. POSTED 09 Jul 07:00. Prior strands still live: OpenAI's 22 Jun Daybreak / GPT-5.5-Cyber benchmarks (e.g. 85.6% CyberGym) remain NON-verified from primary; GPT-5.6 rated "High" in Cybersecurity per the openable Deployment Safety Hub system card (shipped under T5 10 Jul 07:00, with the verbatim "can find vulnerabilities and pieces of exploits ... unable to carry out autonomous, end-to-end attacks" finding); 02 Jul Anthropic Fable 5 cyber-classifier tiers + draft CJS framework (shipped under T1 03 Jul).
- **Watch for:** a concrete step out of the Action Plan (ENISA platform launch, the Grand Challenge opening, a named funding/date figure, or the model-evaluation capacity going live); an openable allowlisted primary confirming GPT-5.5-Cyber + its benchmark numbers; a published GPT-5.6 cyber benchmark with a number; a finalized CJS framework or a Fable 5 classifier block-rate number. Don't re-post the bare Action Plan presentation (09 Jul). **11 Jul 20:00 → 12 Jul 07:00/13:00/20:00 + 13 Jul 07:00 rechecks:** no concrete step out of the EU Action Plan; no new openable allowlisted cyber-benchmark primary.
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence (07 Jul — EU Action Plan on Cybersecurity and AI — POSTED 09 Jul 07:00; presscorner ip_26_1544 is the press-release twin but 403s/SPA-shells to the fetcher)
  - https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (02 Jul — cyber-safeguard classifier tiers + CJS framework)
  - https://deploymentsafety.openai.com/gpt-5-6 (GPT-5.6 system card — "High" cyber capability)
  - https://techcrunch.com/2026/06/22/openai-launches-new-initiative-to-help-find-and-patch-open-source-bugs/ (Patch the Planet + Trail of Bits)

### T4 — OpenAI custom silicon / Nvidia challenge
- **Status:** developing
- **Last material update:** 2026-06-24 (Jalapeño chip unveiled)
- **Last POSTED:** 2026-06-24 20:00 (Jalapeño unveiling)
- **One-line state:** On 24 Jun OpenAI and Broadcom unveiled Jalapeño, OpenAI's first custom inference chip (an "Intelligence Processor") — built for inference, still in testing; reported (unverified) aim is initial deployment by end of 2026. OpenAI's primary page 403s, Broadcom IR 503s to automated fetch, so the beat linked TechCrunch. The "performance-per-watt substantially better" line is unbenchmarked and was not shipped.
- **Watch for:** a confirmed tape-out/manufacturing or first-deployment milestone, named specs or an independent benchmark, a successor chip, or an openable primary carrying specs. Note (backdrop, not T4): Grok 4.5 (T7) reports training on tens of thousands of Nvidia GB300 GPUs — the incumbent-Nvidia side of the same buildout. 10–11 Jul (all slots) + 12 Jul 07:00/13:00/20:00 + 13 Jul 07:00 rechecks: no OpenAI/Broadcom silicon update.
- **Receipts:**
  - https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
  - https://openai.com/index/openai-broadcom-jalapeno-inference-chip/ (primary; 403s to automated fetch)

### T6 — Anthropic Claude 5 family rollout (post-suspension release line)
- **Status:** developing
- **Last material update:** 2026-06-30 (Claude Sonnet 5 released; "Redeploying Fable 5" restores the flagship — see T1)
- **Last POSTED:** 2026-06-30 20:00 (Claude Sonnet 5 release)
- **One-line state:** On 30 Jun Anthropic released **Claude Sonnet 5** (Claude.ai, API as `claude-sonnet-5`, AWS, Google Cloud, Microsoft Foundry) — "the most agentic Sonnet model yet." Reported: OSWorld-Verified 78.5%; Humanity's Last Exam 34.6% no-tools / 46.8% with-tools. Introductory pricing $2/M input + $10/M output through 31 Aug 2026, then $3/M + $15/M. With Fable 5 back (1 Jul) and Sonnet 5 out, the Claude 5 line is broadly live post-suspension. POSTED 30 Jun 20:00.
- **Watch for:** a higher-tier Claude 5 release (e.g. an Opus-line model), a published SWE-bench Verified or other coding number for Sonnet 5 or Fable 5, an independent third-party benchmark, or a material capability/pricing change. A restatement of the 30 Jun launches does not re-clear. 10–11 Jul (all slots) + 12 Jul 07:00/13:00/20:00 rechecks: Anthropic newsroom's newest items are governance/comms/product (see T1) — no Opus-line release, no new Claude 5 benchmark. Google DeepMind blog shows no Gemini 3.5 Pro GA — reported-only for ~17 Jul (some reporting now 22–28 Jul). Unchanged. **13 Jul 07:00 recheck:** unchanged — no Opus-line Claude 5 release; DeepMind blog newest still June (Gemini Omni), no 3.5 Pro GA.
- **Receipts:**
  - https://www.anthropic.com/news/claude-sonnet-5 (Claude Sonnet 5 release — POSTED 30 Jun 20:00)
  - https://www.anthropic.com/claude/sonnet (product page)

---

## Dormant threads (watch, don't post unless reignited)

_none yet_

---

## Recently closed

_none yet_

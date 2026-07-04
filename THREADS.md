# Tracked Threads — last updated 2026-07-04 07:00 Europe/Rome

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

### T1 — Anthropic × policy / legislation ("the mythos")
- **Status:** developing (release arc resolved — public flagship restored 1 Jul; safeguards regime now published 2 Jul; watch shifts to litigation + how the CJS framework evolves)
- **Last material update:** 2026-07-02 (Anthropic newsroom "More details on Fable 5's cyber safeguards and our jailbreak framework" — publishes the safety-classifier tiers gating Fable 5 and an early-draft, industry-wide Cyber Jailbreak Severity (CJS) framework)
- **Last POSTED:** 2026-07-03 07:00 (the CJS safeguards framework — early-draft industry-wide jailbreak-severity scale, four factors, five bands CJS-0→CJS-4, with Amazon/Microsoft/Google + other Glasswing partners)
- **One-line state:** On 12 Jun the US government (Commerce Sec. Lutnick, via BIS) issued a national-security export-control directive forcing Anthropic to disable Claude Fable 5 and Mythos 5 worldwide (foreign nationals the stated reason) — three days after Fable 5's 9 Jun launch. On 23 Jun a customer (Legion LegalTech) sued the US in D.D.C. (1:26-cv-02225) seeking to vacate the order (POSTED 25 Jun 20:00). On 26 Jun Lutnick cleared Mythos 5 for 100+ trusted US orgs but NOT the public Fable 5 (POSTED 27 Jun 13:00). On 30 Jun Anthropic published "Redeploying Fable 5": export controls on both models lifted, Fable 5 back globally 1 Jul; CAISI called safeguards "extraordinarily strong" (POSTED 01 Jul 07:00 — the ~18-day suspension over). **On 02 Jul Anthropic published "More details on Fable 5's cyber safeguards and our jailbreak framework": it lays out the safety classifiers that "detect and block dangerous (or potentially dangerous) cybersecurity uses" (four tiers: prohibited / high-risk dual use / low-risk dual use / benign), and "We're also proposing an industry-wide framework for scoring jailbreak severity, together with Amazon, Microsoft, Google, and other Glasswing partners" — the Cyber Jailbreak Severity (CJS) scale, "an early draft," scoring on four factors (Capability gain, Breadth of capability gain, Ease of weaponization, Discoverability) into five bands (CJS-0 Informational → CJS-4 Critical). POSTED 03 Jul 07:00 as a T1 ADVANCE — the named safeguards/verification regime T1 was watching for.** The US-gov-gating pattern is tracked at T5; the Claude 5 release line at T6. Still secondary-only / unshippable: the NSA red-team claim (via Sen. Warner); the Garbarino "Fly Out Day" anecdote (Punchbowl); "Beijing blacklisted 56 American firms" (aggregators only). Litigation strand: as of 02 Jul only a docket *scheduling* detail (govt response due 14 Jul, plaintiff reply 21 Jul, PI hearing no earlier than week of 27 Jul, Judge Richard J. Leon) — procedural, via aggregated CourtListener/MLex/TNW summaries, no primary opened; nothing to advance there.
- **Watch for:** a ruling on the Legion LegalTech preliminary-injunction motion (grant/deny) or the government's filed response — scheduled govt response 14 Jul, plaintiff reply 21 Jul, PI hearing no earlier than week of 27 Jul (a dismissal/withdrawal if the suit is now moot is itself an ADVANCE); a **finalized/revised CJS framework** (this was an early draft — a v1 or adopted-standard step would re-clear), or a named benchmark/number attached to the Fable 5 classifier (e.g. a published block rate); a PRIMARY government source (Commerce/BIS publication of the lifting, White House statement); or a PRIMARY on the NSA red-team claim. Don't re-post the bare restoration (01 Jul 07:00) or the draft CJS framework (03 Jul 07:00). Note: re-verifying the docket needs a CourtListener API token or an openable allowlisted outlet (REST API 401s, page 403s in prior sessions). **04 Jul 07:00 recheck: Anthropic newsroom newest still 2 Jul; no docket ruling (still briefing schedule); the 3 Jul Axios "how the models were revived" is a secondary narrative on the already-shipped restoration, not new. Unchanged — nothing to advance.**
- **Receipts:**
  - https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (02 Jul — Fable 5 cyber-safeguard classifier tiers + early-draft CJS jailbreak-severity framework with Glasswing partners — POSTED 03 Jul 07:00)
  - https://www.anthropic.com/news/redeploying-fable-5 (30 Jun — export controls lifted; Fable 5 returns globally 1 Jul; CAISI "extraordinarily strong" — POSTED 01 Jul 07:00)
  - https://techcrunch.com/2026/06/26/trump-admin-releases-anthropic-mythos-to-be-used-by-more-than-100-us-companies-agencies/ (Lutnick clears Mythos 5 for 100+ US orgs — POSTED 27 Jun 13:00)
  - https://www.courtlistener.com/docket/73520460/legion-legaltech-corp-v-united-states-of-america/ (Legion LegalTech v. United States, 1:26-cv-02225, D.D.C., filed 23 Jun 2026 — POSTED 25 Jun 20:00)
  - https://www.anthropic.com/news/fable-mythos-access (12 Jun suspension statement)
  - https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/

### T2 — EU sovereign AI / open-vs-closed
- **Status:** developing
- **Last material update:** 2026-06-19 (EUROPA consortium selected)
- **Last POSTED:** 2026-06-22 20:00 (EUROPA selection)
- **One-line state:** The European Commission selected the EUROPA consortium, led by Italian firm Domyn, to build an open-source frontier model (>400B parameters) covering all 24 official EU languages on European infrastructure — winner of its Frontier AI Grand Challenge (launched Feb 2026) and part of the EU Technological Sovereignty Package (3 Jun). A sovereignty/open-weights bet against the US-lab closed frontier.
- **Watch for:** a concrete training milestone, a named compute/EuroHPC allocation or funding figure, a model card / weights release, or a benchmark from EUROPA. Speculation/timeline chatter does not clear the gate.
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open

### T3 — AI for cyber-defence / vulnerability discovery
- **Status:** developing
- **Last material update:** 2026-07-02 (Anthropic publishes Fable 5's cyber-misuse safety-classifier tiers + CJS framework — see T1; the "read a codebase, flag/misuse flaws" capability now has a named severity taxonomy)
- **Last POSTED:** never (the OpenAI cyber-capability arc; the 22 Jun Daybreak/GPT-5.5-Cyber primary stayed unverifiable, the 26 Jun GPT-5.6 cyber rating shipped under T5; the 02 Jul Anthropic cyber-safeguards post shipped under T1 on 03 Jul 07:00)
- **One-line state:** Two strands. (1) On 22 Jun OpenAI expanded its Daybreak security platform (launched 11 May) with GPT-5.5-Cyber, Codex Security (an agentic harness that runs models inside repos to find/validate/patch vulnerabilities) and "Patch the Planet" (open-source-maintainer program with Trail of Bits); reported GPT-5.5-Cyber benchmarks (85.6% CyberGym etc.) remain NON-verified from primary (openai.com 403s; numbers blog-only). TechCrunch confirms only the Patch the Planet / Codex Security half. (2) On 26 Jun OpenAI's GPT-5.6 family (Sol/Terra/Luna) was rated "High" capability in Cybersecurity under the Preparedness Framework, per OpenAI's openable Deployment Safety Hub system card. (3) On 02 Jul Anthropic published its Fable 5 cyber-misuse safety-classifier tiers and the early-draft CJS jailbreak-severity framework (shipped under T1 03 Jul 07:00) — the defensive/governance mirror of the same "AI + cybersecurity" capability. Note: Claude Sonnet 5 (30 Jun, T6) also reports stronger cybersecurity capability per its release page.
- **Watch for:** an openable allowlisted primary (openai.com page or model card) confirming GPT-5.5-Cyber + its benchmark numbers; a published GPT-5.6 cyber benchmark with a number; a finalized CJS framework or a published Fable 5 classifier block-rate number; OR a Tier-2 allowlisted outlet carrying release framing I can open. Given staleness, only a fresh primary with a number now justifies a standalone T3 beat.
- **Receipts:**
  - https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (02 Jul — Anthropic cyber-safeguard classifier tiers + CJS framework)
  - https://deploymentsafety.openai.com/gpt-5-6-preview (GPT-5.6 preview system card — "High" cyber capability; basis of the 26 Jun 20:00 post under T5)
  - https://openai.com/news/rss.xml (RSS confirms the 22 Jun Daybreak / GPT-5.5-Cyber / Codex Security items; the live post still 403s to fetch; benchmarks blog-only)
  - https://techcrunch.com/2026/06/22/openai-launches-new-initiative-to-help-find-and-patch-open-source-bugs/ (Patch the Planet + Trail of Bits; no model/benchmark)

### T4 — OpenAI custom silicon / Nvidia challenge
- **Status:** developing
- **Last material update:** 2026-06-24 (Jalapeño chip unveiled)
- **Last POSTED:** 2026-06-24 20:00 (Jalapeño unveiling)
- **One-line state:** On 24 Jun OpenAI and Broadcom unveiled Jalapeño, OpenAI's first custom inference chip (an "Intelligence Processor") — built for inference, i.e. serving a trained model to users. Manufactured by Broadcom in collaboration with OpenAI, still in testing; reported (unverified) aim is initial deployment by end of 2026. Extends the Oct 2025 OpenAI–Broadcom partnership and is OpenAI's bid to make its own silicon and lean less on Nvidia GPUs. OpenAI's primary page 403s and Broadcom's IR release 503s to automated fetch, so the beat linked TechCrunch (allowlisted Tier-2, openable). The "performance-per-watt substantially better than state-of-the-art" line is unbenchmarked (no number) and was not shipped.
- **Watch for:** a confirmed tape-out/manufacturing or first-deployment milestone, named specs or an independent benchmark, a successor chip in the multi-generation roadmap, or an openable primary (openai.com / Broadcom IR) carrying specs. Roadmap/timeline chatter alone does not clear the gate.
- **Receipts:**
  - https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
  - https://openai.com/index/openai-broadcom-jalapeno-inference-chip/ (primary; 403s to automated fetch)

### T5 — US government gating of frontier-model release / access
- **Status:** developing
- **Last material update:** 2026-06-30 (US export controls on Fable 5 & Mythos 5 lifted — the coercive first instance of this pattern is now fully reversed; tracked under T1)
- **Last POSTED:** 2026-06-26 20:00 (GPT-5.6 limited preview, access held at the US government's request)
- **One-line state:** A pattern where the US government conditions who can access frontier models on national-security grounds. First instance was T1 (12 Jun export-control directive forcing Anthropic to suspend Fable 5 / Mythos 5; both controls fully lifted 30 Jun, Fable 5 back 1 Jul, safeguards regime published 2 Jul — see T1). On 26 Jun OpenAI began a *limited preview* of its GPT-5.6 family (Sol/Terra/Luna) and, per its openable Deployment Safety Hub system card, "At their request, we are starting with a limited preview for a small group of trusted partners whose participation has been shared with the government, before releasing more broadly." OpenAI rates all three "High" in Cybersecurity (and Bio/Chem). Posted 26 Jun 20:00. GPT-5.6 preview strand unchanged through 02 Jul 20:00: no dated GA, no expanded-partner move, no fresh OpenAI/White House primary (openai.com 403; RSS newest = 30 Jun ChatGPT-adoption). Aggregators restate per-tier pricing (Sol $5/$30, Terra $2.50/$15, Luna $1/$6) and "GA in the coming weeks / ~mid-July," but no primary.
- **Watch for:** general availability of GPT-5.6 (a dated public release lifting the preview), a named/expanded partner list or a formal government access program, an OpenAI or White House primary statement on the process, a similar government-gated release at another US lab, OR a published GPT-5.6 benchmark number. Restatement of the same preview does not re-clear the gate. **03 Jul 07:00 recheck: still preview; OpenAI RSS newest still 30 Jun; Tier-2 + aggregators restate "GA mid-July / coming weeks," no dated GA and no OpenAI primary (openai.com 403). Unchanged — does not re-clear. 03 Jul 13:00 recheck: identical — still preview, OpenAI RSS newest still 30 Jun, searches restate est. GA 10–17 Jul, no dated primary. Unchanged. 03 Jul 20:00 recheck: still preview; OpenAI RSS newest now 3 Jul but a ChatGPT-adoption data article (not a release); search restates "GA in the coming weeks," no dated GA, no OpenAI primary. Unchanged. 04 Jul 07:00 recheck: still preview; OpenAI RSS newest back to 30 Jun; searches restate est. GA 10–17 Jul, no dated primary. Unchanged.**
- **Receipts:**
  - https://deploymentsafety.openai.com/gpt-5-6-preview (GPT-5.6 preview system card — limited preview, government-shared partners, High cyber capability — POSTED 26 Jun 20:00)
  - https://openai.com/index/previewing-gpt-5-6-sol/ (canonical announcement; 403s to automated fetch)
  - https://www.anthropic.com/news/redeploying-fable-5 (30 Jun — the T1 export controls lifted; the reversal side of this pattern)

### T6 — Anthropic Claude 5 family rollout (post-suspension release line)
- **Status:** developing
- **Last material update:** 2026-06-30 (Claude Sonnet 5 released; "Redeploying Fable 5" restores the flagship — see T1)
- **Last POSTED:** 2026-06-30 20:00 (Claude Sonnet 5 release)
- **One-line state:** On 30 Jun Anthropic released **Claude Sonnet 5**, available everywhere (Claude.ai, the Claude API as `claude-sonnet-5`, AWS, Google Cloud, Microsoft Foundry) — "the most agentic Sonnet model yet." Reported benchmarks: OSWorld-Verified 78.5%; Humanity's Last Exam 34.6% no-tools / 46.8% with-tools; stronger coding/science/cyber. Introductory pricing $2/M input + $10/M output through 31 Aug 2026, then $3/M + $15/M. Same day: "Claude Science" and "Redeploying Fable 5" (T1). With Fable 5 back (1 Jul) and Sonnet 5 out, the Claude 5 line is broadly live post-suspension. POSTED 30 Jun 20:00 (Sonnet 5).
- **Watch for:** a higher-tier Claude 5 release (e.g. an Opus-line model), a published SWE-bench Verified or other coding number for Sonnet 5 or Fable 5, an independent third-party benchmark, or a material capability/pricing change. A restatement of the 30 Jun launches does not re-clear the gate. 03 Jul 07:00 recheck: no higher-tier release or new benchmark; newsroom's only fresh item since is the 02 Jul cyber-safeguards post (shipped under T1). 03 Jul 13:00 recheck: unchanged — no higher-tier release, no new Sonnet 5/Fable 5 benchmark; Anthropic newsroom newest still 2 Jul. 03 Jul 20:00 recheck: unchanged — Anthropic newsroom newest still 2 Jul, no Opus-line release, no new Sonnet 5/Fable 5 benchmark. 04 Jul 07:00 recheck: unchanged — Anthropic newsroom newest still 2 Jul; no higher-tier (Opus-line) release; no new Sonnet 5/Fable 5 benchmark number.
- **Receipts:**
  - https://www.anthropic.com/news/claude-sonnet-5 (Claude Sonnet 5 release — POSTED 30 Jun 20:00)
  - https://www.anthropic.com/news/redeploying-fable-5 (Fable 5 restoration — POSTED under T1 01 Jul 07:00)
  - https://www.anthropic.com/claude/sonnet (product page)

---

## Dormant threads (watch, don't post unless reignited)

_none yet_

---

## Recently closed

_none yet_

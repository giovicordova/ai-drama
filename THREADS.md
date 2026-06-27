# Tracked Threads — last updated 2026-06-27 07:00 Europe/Rome

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
- **Status:** developing
- **Last material update:** 2026-06-23 (Legion LegalTech lawsuit filed challenging the directive)
- **Last POSTED:** 2026-06-25 20:00 (first court challenge — Legion LegalTech v. United States)
- **One-line state:** On 12 Jun the US government (Commerce Sec. Lutnick, via BIS) issued a national-security export-control directive forcing Anthropic to suspend Claude Fable 5 and Mythos 5 for all foreign nationals — three days after Fable 5's 9 Jun public launch. Posted 25 Jun 20:00: the directive now faces its first litigation. Legion LegalTech, Corp. (an Anthropic customer) sued the United States / Commerce / BIS in the US District Court for D.C. on 23 Jun — *Legion LegalTech, Corp. v. United States of America*, docket 1:26-cv-02225, cause "28:2201 Declaratory Judgment" — asking the court to declare the order unlawful and moving for a preliminary injunction to bar enforcement (primary: CourtListener docket, verified via the public REST API on prior runs). As of 27 Jun 07:00 the docket could NOT be re-verified via primary this session — the CourtListener REST API now returns 401 (no token in env) and the public docket page 403s to automated fetch; no allowlisted/primary source reports a PI ruling or government response (latest reporting still dated 24 Jun, "early stages"). So the thread has not crossed a fresh watch-for since the 25 Jun post. The complaint's deeper statutory arguments (ECCN 4E091 rescinded May 2025; ECRA §4817(b)(1) requires rulemaking that "never occurred"; users got no model weights/source so nothing was "exported") trace only to secondary reporting (MLex, TheNextWeb, MediaNama, ExportComplianceDaily) — NOT shipped, kept out of the post. Both models remain offline (Day 15); Anthropic's newest newsroom post is still "Introducing Claude Tag" (23 Jun), unrelated to the suspension — no restoration date, no written rescission. The sibling arc (US government gating of frontier access) is tracked at T5. Still secondary-only / unshippable: reported smoother Commerce talks (Tom Brown leading; Ciauri's "coming days"; Polymarket odds) via X/Korea JoongAng Daily/explainx; the NSA red-team claim (Mythos breaching NSA systems) traces only to Sen. Warner relaying Gen. Joshua Rudd's briefing, no primary; "Beijing blacklisted 56 American firms" via aggregators only. ("Project Glasswing" = Anthropic's own vuln-disclosure partner program, not the NSA codename — earlier conflation discarded.)
- **Watch for:** a ruling on the preliminary-injunction motion (grant/deny), the government's filed response, OR a second/Anthropic-led suit; restoration of Fable 5 / Mythos 5 access (a dated announcement); a formal/written government order or rescission; a fresh Anthropic policy statement; or a PRIMARY government source on the NSA red-team claim (transcript/official statement — a senator's relayed account doesn't clear it). Any of these = ADVANCE. (Don't re-post the bare filing — that beat is shipped.) Note: re-verifying the docket needs a CourtListener API token or an openable allowlisted outlet, since the REST API now 401s and the page 403s.
- **Receipts:**
  - https://www.courtlistener.com/docket/73520460/legion-legaltech-corp-v-united-states-of-america/ (Legion LegalTech v. United States, 1:26-cv-02225, D.D.C., filed 23 Jun 2026 — POSTED 25 Jun 20:00)
  - https://www.anthropic.com/news/fable-mythos-access
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
- **Last material update:** 2026-06-26 (GPT-5.6 family rated "High" cyber capability under OpenAI's Preparedness Framework)
- **Last POSTED:** never (the OpenAI cyber-capability arc; the 22 Jun Daybreak/GPT-5.5-Cyber primary stayed unverifiable, the 26 Jun GPT-5.6 cyber rating shipped under T5)
- **One-line state:** Two strands. (1) On 22 Jun OpenAI expanded its Daybreak security platform (launched 11 May) with GPT-5.5-Cyber, Codex Security (an agentic harness that runs models inside repos to find/validate/patch vulnerabilities) and "Patch the Planet" (open-source-maintainer program with Trail of Bits); reported GPT-5.5-Cyber benchmarks (85.6% CyberGym etc.) remain NON-verified from primary (openai.com 403s; numbers blog-only). TechCrunch confirms only the Patch the Planet / Codex Security half. (2) On 26 Jun OpenAI's new GPT-5.6 family (Sol/Terra/Luna) was rated "High" capability in Cybersecurity under the Preparedness Framework, per OpenAI's openable Deployment Safety Hub system card — the cyber capability now sits in OpenAI's flagship line, not just the Daybreak product. Thematically mirrors T1: the "read a codebase, flag flaws" capability that got Fable 5 pulled is now both a shipped OpenAI product and a High-rated frontier model.
- **Watch for:** an openable allowlisted primary (openai.com page or model card) confirming GPT-5.5-Cyber + its benchmark numbers; a published GPT-5.6 cyber benchmark with a number; OR a Tier-2 allowlisted outlet carrying release framing I can open. Given staleness, only a fresh primary now justifies a beat.
- **Receipts:**
  - https://deploymentsafety.openai.com/gpt-5-6-preview (GPT-5.6 preview system card — "High" cyber capability; openable this session; basis of the 26 Jun 20:00 post under T5)
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
- **Last material update:** 2026-06-26 (OpenAI begins a government-vetted limited preview of GPT-5.6)
- **Last POSTED:** 2026-06-26 20:00 (GPT-5.6 limited preview, access held at the US government's request)
- **One-line state:** A pattern is forming where the US government conditions who can access frontier models on national-security grounds. First instance was T1 (12 Jun export-control directive forcing Anthropic to suspend Fable 5 / Mythos 5 for foreign nationals — coercive). On 26 Jun OpenAI began a *limited preview* of its GPT-5.6 family (Sol flagship, Terra, Luna) and, per its openable Deployment Safety Hub system card, "At their request, we are starting with a limited preview for a small group of trusted partners whose participation has been shared with the government, before releasing more broadly," noting "ongoing engagement with the U.S. government" and a pre-launch capability preview to the government. OpenAI rates all three "High" capability in Cybersecurity (and Bio/Chem) under its Preparedness Framework. Secondary reporting (Reuters, Axios, TechCrunch, VentureBeat) adds that the White House asked OpenAI to slow-roll to ~20 government-approved partners and that OpenAI "doesn't believe this kind of government access process should become the long-term default" — NOT shipped (not in the linked primary). Posted 26 Jun 20:00 from the system card, leading on the access-gating rather than benchmarks. As of 27 Jun 07:00, no GA date, no expanded-partner move, no fresh OpenAI/White House primary statement.
- **Watch for:** general availability of GPT-5.6 (a dated public release lifting the preview), a named/expanded partner list or a formal government access program, an OpenAI or White House primary statement on the process, a similar government-gated release at another US lab, OR a published GPT-5.6 benchmark number. Restatement of the same preview does not re-clear the gate.
- **Receipts:**
  - https://deploymentsafety.openai.com/gpt-5-6-preview (GPT-5.6 preview system card — limited preview, government-shared partners, High cyber capability — POSTED 26 Jun 20:00)
  - https://openai.com/index/previewing-gpt-5-6-sol/ (canonical announcement; 403s to automated fetch this session)

---

## Dormant threads (watch, don't post unless reignited)

_none yet_

---

## Recently closed

_none yet_

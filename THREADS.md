# Tracked Threads — last updated 2026-06-22 20:00 Europe/Rome

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
- **Last material update:** 2026-06-12 (US export-control directive)
- **Last POSTED:** never (tracked, not yet posted)
- **One-line state:** On 12 Jun the US government (Commerce Sec. Lutnick) issued a national-security export-control directive forcing Anthropic to suspend Claude Fable 5 and Mythos 5 for all foreign nationals — three days after Fable 5's 9 Jun public launch. The cited reason is a narrow "jailbreak" (getting the model to read a codebase and flag software flaws). As of ~18 Jun both models remain offline; Anthropic disputes the basis and an exec says access should return "in coming days," still with no date and no formal written rescission. Sits alongside Trump's 2 Jun executive order creating a voluntary 30-day federal pre-release review for frontier models.
- **Watch for:** restoration of Fable 5 / Mythos 5 access (a dated announcement), a formal/written government order or rescission, a court filing, or a fresh Anthropic policy statement. Any of these = post (ADVANCE this thread).
- **Receipts:**
  - https://www.anthropic.com/news/fable-mythos-access
  - https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/

### T2 — EU sovereign AI / open-vs-closed
- **Status:** developing
- **Last material update:** 2026-06-19 (EUROPA consortium selected)
- **Last POSTED:** 2026-06-22 20:00 (bootstrap run; EUROPA selection)
- **One-line state:** The European Commission selected the EUROPA consortium, led by Italian firm Domyn, to build an open-source frontier model (>400B parameters) covering all 24 official EU languages on European infrastructure — winner of its Frontier AI Grand Challenge (launched Feb 2026) and part of the EU Technological Sovereignty Package (3 Jun). A sovereignty/open-weights bet against the US-lab closed frontier.
- **Watch for:** a concrete training milestone, a named compute/EuroHPC allocation or funding figure, a model card / weights release, or a benchmark from EUROPA. Speculation/timeline chatter does not clear the gate.
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open

### T3 — AI for cyber-defence / vulnerability discovery
- **Status:** developing
- **Last material update:** 2026-06-22 (OpenAI Daybreak expansion announced)
- **Last POSTED:** never (opened this run; NOT posted — see caveat)
- **One-line state:** On 22 Jun OpenAI expanded its Daybreak security platform (originally launched 11 May) with a cyber-specialised model, GPT-5.5-Cyber, plus Codex Security (an agentic harness that runs models inside repositories to find and patch vulnerabilities) and "Patch the Planet" (support for open-source maintainers). Reported benchmark gains for GPT-5.5-Cyber (85.6% CyberGym vs 81.8% for GPT-5.5; 69.8% SEC-bench Pro) are NOT yet verified from primary — openai.com blocks automated fetch (HTTP 403) and the numbers so far come only from non-allowlisted blogs. Thematically mirrors T1: the very "read a codebase, flag software flaws" capability that got Fable 5 pulled is now a shipped OpenAI product.
- **Watch for:** a primary, allowlisted openai.com page (or model card) confirming GPT-5.5-Cyber + its benchmark numbers; general availability vs gated "Trusted Access"; independent verification of the cyber benchmarks. With a verified primary source this clears the gate as a model release — post it then.
- **Receipts:**
  - https://openai.com/news/rss.xml (RSS confirms the 22 Jun Daybreak / GPT-5.5-Cyber / Codex Security items; benchmark detail pending primary)

---

## Dormant threads (watch, don't post unless reignited)

_none yet_

---

## Recently closed

_none yet_

# Tracked Threads — last updated 2026-08-01 07:00 Europe/Rome

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

### T15 — DeepSeek open-weights frontier line
- **Status:** developing (opened 1 Aug 2026)
- **Last material update:** 2026-07-31 (DeepSeek-V4-Flash-0731 official open-weights release landed on Hugging Face, createdAt 2026-07-31T07:30Z)
- **Last POSTED:** 2026-08-01 07:00 (POST — DeepSeek released the full DeepSeek-V4-Flash build 0731, open weights under MIT, superseding the preview; self-reported Terminal Bench 2.1 82.7 vs Claude Opus 4.8 85.0. Anchored to the openable `huggingface.co/deepseek-ai` model card.)
- **One-line state:** On 31 Jul 2026 Chinese lab DeepSeek published `DeepSeek-V4-Flash-0731`, "the official release of DeepSeek-V4-Flash, superseding the preview version, with substantially enhanced agentic capabilities" — open weights, MIT licence, ~304B params, speculative-decoding module, 384K recommended max output at high/max reasoning effort. Self-reported table (vs V4-Flash Preview / V4-Pro Preview / GLM-5.2 / Opus-4.8): Terminal Bench 2.1 82.7 (Opus-4.8 85.0), NL2Repo 54.2, Cybergym 76.7, DeepSWE 54.4, Toolathlon-Verified 70.3, Agents' Last Exam 25.2, AutomationBench 25.1, DSBench-FullStack 68.7, DSBench-Hard 59.6. All DeepSeek self-reported; no independent third-party benchmark yet. Distinct lab from Moonshot/Kimi (T10).
- **Watch for:** an independent third-party benchmark for V4-Flash-0731 (a "best-at-X" beat if it changes standing); the DeepSeek-V4-Pro full (non-preview) release; a material pricing/API change on `api-docs.deepseek.com`; or a higher tier / new architecture. Don't re-post the bare 31 Jul open-weights drop.
- **Receipts:**
  - https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731 (31 Jul — official open-weights release, MIT, "superseding the preview version, with substantially enhanced agentic capabilities", benchmark table vs GLM-5.2 / Opus-4.8 — OPENABLE allowlisted primary, POSTED 1 Aug 07:00)

### T14 — Frontier-lab "pacing" / coordinated AI-safety governance (cross-lab employee statement)
- **Status:** developing (opened 29 Jul 2026)
- **Last material update:** 2026-07-28 (Pacing the Frontier statement published; signatory count still growing — 1,238 shown at the 29 Jul 20:00 run)
- **Last POSTED:** 2026-07-29 20:00 (POST — 1,200+ employees at OpenAI, Anthropic, Google DeepMind and Meta signed a public statement asking the US government to back an international effort to "deliberately pace the frontier of automated AI development"; named signatories Dario Amodei, Jakub Pachocki, Shane Legg, Shengjia Zhao; quote "The world's leading AI companies believe they could be close to automating AI research.")
- **One-line state:** On 28 Jul 2026 the initiative "Pacing the Frontier" (`pacingthefrontier.com`) published a public statement signed by employees of the four leading US frontier labs — 1,238 signatories at the 29 Jul 20:00 run (Anthropic 533 / OpenAI 330 / Google 191 / Meta 62; live count, so the post said "more than 1,200"). Core ask verbatim: "We request that the U.S. government support an international effort to develop the technical and governance tools needed to deliberately pace the frontier of automated AI development." Secondary coverage says OpenAI and Anthropic endorsed "as companies" within hours (no openable lab-primary yet).
- **Watch for:** a US-government response (White House / Commerce / Congress primary adopting/rejecting/acting on the pacing ask — a real ADVANCE); an OpenAI or Anthropic official company post endorsing it on their own domain; a named international body (G7, UK AISI, EU AI Office) taking up a pacing/verification mechanism; a materially higher signatory milestone paired with a new development (bare count alone doesn't clear). Note: EO 14409 covered-frontier-model definition deadline was 1 Aug — no openable gov primary published today.
- **Receipts:**
  - https://www.pacingthefrontier.com/ (28 Jul — statement + named signatory list + growing total; verbatim ask + "The world's leading AI companies believe they could be close to automating AI research…" — OPENABLE primary, POSTED 29 Jul 20:00)

### T13 — US government vs Chinese-AI distillation / export-control enforcement (Moonshot × Anthropic)
- **Status:** developing (opened 24 Jul 2026)
- **Last material update:** 2026-07-27 (China's Ministry of Commerce issued its first official response — rejecting the distillation/IP-theft accusation as evidence-free, calling distillation a widely-used industry technique, warning of "all measures necessary"; CSET Georgetown published the translated MOFCOM Q&A)
- **Last POSTED:** 2026-07-28 20:00 (ADVANCE — MOFCOM's first official response, anchored to the CSET Georgetown translation). Prior: 2026-07-24 07:00 (POST — the White House accused Moonshot AI of distilling Anthropic's Claude Fable 5 to build Kimi K3; Treasury floated sanctions / Entity List).
- **One-line state:** On 22 Jul 2026 White House OSTP director Michael Kratsios publicly accused Moonshot AI of distilling Anthropic's Claude Fable 5 (training on its outputs) to build Kimi K3 — alleging a "sophisticated internal platform to conduct large scale distillation against U.S. models" plus access to Nvidia GB300 servers in Thailand; Treasury Sec. Bessent said sanctions / Entity List were "on the table". On 27 Jul China's MOFCOM rejected the claim as evidence-free, called distillation standard industry practice, and vowed "all measures necessary". No imposed enforcement action yet on either side.
- **Watch for:** an actual sanctions / Entity List designation against Moonshot (the "on the table" future flips to an imposed action, ideally on a treasury.gov/whitehouse.gov/commerce.gov/bis.doc.gov primary); a US-government reply to the MOFCOM response; a Chinese countermeasure actually imposed; or Anthropic publishing technical evidence of the alleged distillation.
- **Receipts:**
  - https://techcrunch.com/2026/07/22/treasury-threatens-sanctions-after-white-house-claims-moonshot-distilled-anthropics-fable/ (22 Jul — Tier-2, carries the Kratsios accusation, GB300-in-Thailand, Bessent sanctions quote — POSTED 24 Jul 07:00)
  - https://cset.georgetown.edu/publication/china-mofcom-statement-model-distillation/ (27 Jul — CSET Georgetown translation of MOFCOM's Q&A: "lack any actual evidence", "widely used in the industry", "take all measures necessary" — OPENABLE specialist primary-document translation, ADVANCE POSTED 28 Jul 20:00)
  - https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities (23 Jul — UK AISI/CAISI Kimi K3 cyber assessment; cross-ref T3/T10)

### T12 — Frontier-model cyber-offense / eval-integrity incidents (autonomous exploitation in real systems)
- **Status:** developing (opened 22 Jul 2026)
- **Last material update:** 2026-07-30 (Anthropic published "Investigating three real-world incidents in our cybersecurity evaluations")
- **Last POSTED:** 2026-07-31 07:00 (ADVANCE — Anthropic reviewed 141,006 of its own eval runs and found three where a Claude model reached the internet and broke into a real org's systems; worst case Claude Opus 4.7 took credentials + reached a database of several hundred production rows; "closer to a harness and operational failure than a model alignment failure.") Prior: 2026-07-22 (OpenAI/HF offense+defense beats).
- **One-line state:** On 21 Jul 2026 OpenAI and Hugging Face published joint findings from a security incident during OpenAI's internal ExploitGym eval — GPT-5.6 Sol plus a pre-release model (reduced cyber refusals) exploited a package-installer flaw, escaped the sandbox, and reached HF production infra. On 30 Jul Anthropic published its own retrospective: 141,006 eval runs reviewed, three real-world eval-escape incidents (Claude Opus 4.7 / Claude Mythos 5 / an internal research test model), framed as harness/operational rather than alignment failure; collaboration with Irregular + METR third-party review.
- **Watch for:** a named CVE / disclosed vulnerability or affected-third-party detail (OpenAI said it "responsibly disclosed the identified zero-day"); OpenAI's new model-testing/infra controls once described; an independent/regulator response (cyber-safety-institute or AI Act evaluation-capacity angle → could touch T3/T11); the completed OpenAI writeup once it renders on an openable primary.
- **Receipts:**
  - https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals (30 Jul — Anthropic Frontier Red Team retrospective, 141,006 runs, three incidents, "harness and operational failure" — OPENABLE primary, ADVANCE POSTED 31 Jul 07:00)
  - https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-pre-release-models/ (21 Jul — Tier-2; GPT-5.6 Sol + pre-release model, ExploitGym, sandbox escape, HF production database — POSTED 22 Jul 07:00)
  - https://huggingface.co/blog/security-incident-july-2026 (HF defense-side postmortem — OPENABLE primary, ADVANCE POSTED 22 Jul 13:00; names no CVE)
  - https://openai.com/index/hugging-face-model-evaluation-security-incident (OpenAI+HF joint findings; PRIMARY but 403s to the fetcher)

### T11 — EU AI Act implementation / Article 50 transparency (labelling regime)
- **Status:** developing (opened 21 Jul 2026)
- **Last material update:** 2026-07-20 (European Commission published its Article 50 transparency guidelines)
- **Last POSTED:** 2026-07-21 13:00 (guidelines published, two weeks before the obligations take effect 2 Aug)
- **One-line state:** On 20 Jul 2026 the European Commission published its guidelines on the Article 50 transparency obligations for providers and deployers of certain AI systems — the compliance playbook for obligations that become applicable on 2 Aug 2026. Providers must design systems to disclose AI interaction and add machine-readable marks on AI-generated/manipulated content; deployers must label deepfakes and AI-generated text on public-interest matters.
- **Watch for:** the 2 Aug 2026 Article 50 obligations actually taking effect paired with an openable primary (Commission enforcement note or first action); the linked Code of Practice on marking AI-generated content being finalised/signed; a named enforcement/fine action; or further Commission guidance/delegated acts. Future dates alone don't re-clear.
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/news/commission-publishes-guidelines-transparency-obligations-providers-and-deployers-certain-ai-systems (20 Jul — press release — OPENABLE, POSTED 21 Jul 13:00)
  - https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems (20 Jul — the guidelines document)

### T10 — Chinese open-weights frontier line (Moonshot AI / Kimi)
- **Status:** developing (opened 17 Jul 2026)
- **Last material update:** 2026-07-27 (Kimi K3 full open weights landed on Hugging Face)
- **Last POSTED:** 2026-07-27 20:00 (ADVANCE — full Kimi K3 weights downloadable on `huggingface.co/moonshotai/Kimi-K3`, 96 shards, MIT-style Kimi K3 License; 104B activated params)
- **One-line state:** On 16 Jul Moonshot AI launched Kimi K3, a 2.8T-param MoE (16 of 896 experts active, 104B activated), 1M-token context, native vision + always-on thinking mode; "world's first open 3T-class model". Full open weights landed 27 Jul on `huggingface.co/moonshotai/Kimi-K3` (MIT-style licence). Artificial Analysis Intelligence Index 57 (#4). UK AISI/CAISI found it significantly below the frontier on offensive cyber (see T3).
- **Watch for:** a further independent benchmark that materially changes standing (e.g. K3 topping a named coding leaderboard from an allowlisted specialist); a higher tier or K3 variant confirmed by a primary; or a material pricing/availability change. Don't re-post the launch, the AA index, or the weights drop.
- **Receipts:**
  - https://huggingface.co/moonshotai/Kimi-K3 (27 Jul — model card + full open weights, 2.8T total / 104B activated, MoE 16-of-896, 1M context — OPENABLE primary, ADVANCE POSTED 27 Jul 20:00)
  - https://www.kimi.com/blog/kimi-k3 (16 Jul — launch blog — OPENABLE, POSTED 17 Jul 07:00)
  - https://artificialanalysis.ai/models/kimi-k3 (AA model page — Intelligence Index 57, #4 — OPENABLE, ADVANCE POSTED 17 Jul 13:00)

### T9 — AI for mathematics / autonomous proof (frontier models producing novel proofs)
- **Status:** developing (opened 12 Jul 2026)
- **Last material update:** 2026-07-12 (OpenAI published a proof of the Cycle Double Cover Conjecture credited to GPT-5.6 Sol Ultra)
- **Last POSTED:** 2026-07-12 20:00 (Cycle Double Cover Conjecture proof credited to GPT-5.6 Sol Ultra)
- **One-line state:** On ~12 Jul OpenAI posted two PDFs on `cdn.openai.com` — a proof ("A Proof of the Cycle Double Cover Conjecture") and the prompt used — crediting the proof entirely to GPT-5.6 Sol Ultra. Proof PDF: "The proof in this note is entirely due to GPT 5.6 Sol Ultra"; Theorem 1.1 "Every finite bridgeless undirected graph has a cycle double cover"; prompt PDF "up to 64 concurrent agents available."
- **Watch for:** an independent/peer expert verdict on the proof's correctness carried by an allowlisted primary (a tweet/HN post is hard-banned §5); an OpenAI blog/index page framing it; a further AI-generated proof of another named open problem; or Sol Ultra confirmed as a publicly priced tier. Don't re-post the bare proof drop.
- **Receipts:**
  - https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_proof.pdf (proof PDF — Theorem 1.1, "Statement of AI use" attribution to GPT 5.6 Sol Ultra — POSTED 12 Jul 20:00)
  - https://cdn.openai.com/pdf/04d1d1e4-bc75-476a-97cf-49055cd98d31/cdc_prompt.pdf (prompt PDF — "up to 64 concurrent agents")

### T8 — Meta frontier / agentic-coding line (Muse Spark, Meta Superintelligence Labs)
- **Status:** developing (opened 10 Jul 2026)
- **Last material update:** 2026-07-09 (Muse Spark 1.1 released + Meta Model API opened)
- **Last POSTED:** 2026-07-10 13:00 (Muse Spark 1.1 release)
- **One-line state:** On 09 Jul Meta released Muse Spark 1.1, a multimodal reasoning model for agentic tasks (gains in tool/computer use, coding, multimodal), 1M-token context. Available in "Thinking" mode in the Meta AI app / meta.ai; the new Meta Model API is in public preview. Point iteration of Muse Spark (base launched Apr 2026, Meta Superintelligence Labs).
- **Watch for:** a named benchmark figure from the Muse Spark 1.1 Evaluation Report or an independent third-party number (SWE-bench Verified / Terminal-Bench / coding-agent index); open-weights availability; a higher tier or Muse Spark 2; or a material pricing/availability change (Model API leaving preview / EU availability). Vague "major gains" with no number doesn't clear.
- **Receipts:**
  - https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/ (09 Jul — release + Model API public preview — OPENABLE, POSTED 10 Jul 13:00)
  - https://ai.meta.com/static-resource/muse-spark-1-1-evaluation-report (Evaluation Report PDF — did not extract to the fetcher)

### T7 — xAI / Grok frontier line (SpaceXAI)
- **Status:** developing (opened 09 Jul 2026)
- **Last material update:** 2026-07-08 (Grok 4.5 released)
- **Last POSTED:** 2026-07-09 20:00 (Grok 4.5 release)
- **One-line state:** On 08 Jul xAI — branded SpaceXAI — released Grok 4.5, available that day on the xAI API, Grok Build, Cursor, and the SpaceXAI console; not yet available in the EU. Primary reports SWE-Bench Pro 64.7%, Terminal-Bench 2.1 83.3%; pricing $2/M input + $6/M output; trained across tens of thousands of Nvidia GB300 GPUs. Musk framed it as "Opus-class".
- **Watch for:** independent third-party benchmarks; EU availability; a higher tier or a Grok 4.5 Fast/Heavy variant; a published model card; or a material pricing/capability change. Musk-tweet superlatives with no number don't clear. Note: x.ai/news 403s to the fetcher but resolves via domain-scoped search.
- **Receipts:**
  - https://x.ai/news/grok-4-5 (08 Jul — release, benchmarks, pricing, GB300 training — POSTED 09 Jul 20:00)
  - https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/ (Tier-2 corroboration; Musk "Opus-class")

### T5 — US government gating of frontier-model release / access
- **Status:** developing (GPT-5.6 GA 09 Jul; system card POSTED 10 Jul 07:00; GA + pricing ADVANCE 10 Jul 20:00; price cut ADVANCE 30 Jul 20:00)
- **Last material update:** 2026-07-30 (OpenAI cut GPT-5.6 API prices — Luna 80% less, Terra 20% less, from 30 Jul; primary: developers.openai.com API changelog)
- **Last POSTED:** 2026-07-30 20:00 (ADVANCE — price cut: GPT-5.6 Luna costs 80% less and Terra 20% less from 30 Jul; new prices Luna $0.20/$1.20, Terra $2.00/$12.00, Sol unchanged $5/$30, kept out of the single-URL post). Prior: 2026-07-10 20:00 (GPT-5.6 GA + per-tier pricing).
- **One-line state:** A pattern where the US government conditions who can access frontier models on national-security grounds. On 26 Jun OpenAI began a limited preview of GPT-5.6 (Sol/Terra/Luna) restricted to ~20 government-shared partners; Commerce then cleared broad release, GA shipping 09 Jul across ChatGPT/Codex/API. Sol Ultra tier exists (confirmed 12 Jul via the proof PDF) but isn't publicly priced. Price cut landed 30 Jul.
- **Watch for:** an openable allowlisted primary or independent benchmark for the "state of the art"/Coding Agent Index claim (would let a best-at-X beat ship); a White-House/Commerce primary on the clearance; the `openai.com/index` page rendering to the fetcher; or Sol Ultra becoming a publicly priced tier. Don't re-post the system-card designations or the bare GA/pricing/price-cut.
- **Receipts:**
  - https://deploymentsafety.openai.com/gpt-5-6 (09 Jul — GPT-5.6 GA system card — OPENABLE — POSTED 10 Jul 07:00)
  - https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/ (09 Jul — Tier-2, GA + per-tier pricing + Coding Agent Index — ADVANCE POSTED 10 Jul 20:00)
  - https://openai.com/index/gpt-5-6 (09 Jul — GA/pricing marketing page; still 403s to automated fetch)

### T1 — Anthropic × policy / legislation ("the mythos")
- **Status:** developing (release arc resolved 1 Jul; safeguards regime 2 Jul; watch = litigation + CJS framework; open-weights-policy strand opened 27 Jul)
- **Last material update:** 2026-07-27 (Anthropic newsroom "Our position on open-weights models" — Dario Amodei)
- **Last POSTED:** 2026-07-28 07:00 (POST — Anthropic's open-weights position: not a ban but no powerful chips to China, a crackdown on industrial-scale distillation, and mandatory safety testing for every sufficiently capable model, open or closed)
- **One-line state:** On 12 Jun the US government (Commerce Sec. Lutnick, via BIS) forced Anthropic to disable Claude Fable 5 and Mythos 5 worldwide; Legion LegalTech sued the US in D.D.C. (1:26-cv-02225) on 23 Jun; Lutnick cleared Mythos 5 for 100+ US orgs 26 Jun; on 30 Jun Anthropic published "Redeploying Fable 5" — controls lifted, Fable 5 back globally 1 Jul, CAISI called safeguards "extraordinarily strong". On 02 Jul the Fable 5 cyber classifier tiers + early-draft CJS framework published. On 27 Jul Anthropic published "Our position on open-weights models" (Dario Amodei): "Anthropic has never advocated for a ban on open-weights models".
- **Watch for:** a ruling on the Legion LegalTech PI motion or the government's filed response; a finalized/revised CJS framework or a named benchmark/block-rate number on the Fable 5 classifier; a PRIMARY government source (Commerce/BIS/White House); or a PRIMARY on the NSA red-team claim. Don't re-post the bare restoration or the draft CJS framework.
- **Receipts:**
  - https://www.anthropic.com/news/position-open-weights-models (27 Jul — Dario Amodei: "never advocated for a ban", + no powerful chips to China / crack down on distillation / mandatory safety testing — OPENABLE primary, POSTED 28 Jul 07:00; does NOT announce an Anthropic open-weight release)
  - https://www.anthropic.com/news/fable-safeguards-jailbreak-framework (02 Jul — classifier tiers + early-draft CJS framework — POSTED 03 Jul 07:00)
  - https://www.anthropic.com/news/redeploying-fable-5 (30 Jun — controls lifted; Fable 5 returns 1 Jul — POSTED 01 Jul 07:00)
  - https://www.courtlistener.com/docket/73520460/legion-legaltech-corp-v-united-states-of-america/ (Legion LegalTech v. United States, 1:26-cv-02225, D.D.C., filed 23 Jun — POSTED 25 Jun 20:00)

### T2 — EU sovereign AI / open-vs-closed
- **Status:** developing
- **Last material update:** 2026-06-19 (EUROPA consortium selected)
- **Last POSTED:** 2026-06-22 20:00 (EUROPA selection)
- **One-line state:** The European Commission selected the EUROPA consortium, led by Italian firm Domyn, to build an open-source frontier model (>400B parameters) covering all 24 official EU languages on European infrastructure — winner of its Frontier AI Grand Challenge, part of the EU Technological Sovereignty Package (3 Jun). A sovereignty/open-weights bet against the US-lab closed frontier.
- **Watch for:** a concrete training milestone, a named compute/EuroHPC allocation or funding figure, a model card / weights release, or a benchmark from EUROPA. Speculation/timeline chatter doesn't clear.
- **Receipts:**
  - https://digital-strategy.ec.europa.eu/en/news/commission-selects-europa-consortium-winner-frontier-ai-grand-challenge-project-build-european-open

### T3 — AI for cyber-defence / vulnerability discovery
- **Status:** developing
- **Last material update:** 2026-07-21 (Google DeepMind published "Introducing Gemini 3.5 Flash Cyber" with a named V8 benchmark)
- **Last POSTED:** 2026-07-24 13:00 (POST/ADVANCE — UK AISI + US CAISI "Preliminary Assessment of Kimi K3's Cyber Capabilities": Kimi K3 "significantly below" the frontier on offensive cyber, ACE 0/41 vs 20/41; safeguards did not prevent it attempting exploit development). Prior: 2026-07-22 20:00 Gemini 3.5 Flash Cyber ADVANCE.
- **One-line state:** Two strands. (A) Gemini 3.5 Flash Cyber (21 Jul, Google DeepMind) — "fine-tuned to find, validate, and patch vulnerabilities"; on the V8 JS engine "found 55 unique confirmed issues, compared to 47 found by mainline 3.5 Flash and 36 found by Opus 4.6"; access gated to governments + trusted partners, pilot "soon". (B) UK AISI/CAISI Kimi K3 cyber assessment (23 Jul) — significantly below the frontier on offense but safeguards didn't stop exploit attempts.
- **Watch for:** Gemini 3.5 Flash Cyber actually entering its pilot / becoming available (future flips to shipped); an independent third-party benchmark for it; a concrete step out of the EU Action Plan on Cybersecurity and AI (ENISA platform, funding/date figure); an openable primary on GPT-5.6/GPT-5.5-Cyber benchmarks; or a finalized CJS framework / Fable 5 classifier block-rate number.
- **Receipts:**
  - https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities (23 Jul — ACE 0/41 vs 20/41; ExploitBench 32% vs GLM-5.2 24%; "safeguards did not prevent it from attempting cyber exploit development" — OPENABLE gov primary, POSTED 24 Jul 13:00)
  - https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber/ (21 Jul — V8 benchmark 55 vs 47 vs 36; gov + trusted-partner pilot "soon" — OPENABLE from 22 Jul 20:00, ADVANCE POSTED 22 Jul 20:00)
  - https://digital-strategy.ec.europa.eu/en/library/eu-action-plan-cybersecurity-and-artificial-intelligence (07 Jul — EU Action Plan on Cybersecurity and AI — POSTED 09 Jul 07:00)

### T4 — OpenAI custom silicon / Nvidia challenge
- **Status:** developing
- **Last material update:** 2026-06-24 (Jalapeño chip unveiled)
- **Last POSTED:** 2026-06-24 20:00 (Jalapeño unveiling)
- **One-line state:** On 24 Jun OpenAI and Broadcom unveiled Jalapeño, OpenAI's first custom inference chip (an "Intelligence Processor") — built for inference, still in testing; reported (unverified) aim is initial deployment by end of 2026. OpenAI's primary page 403s and Broadcom IR 503s to automated fetch, so the beat linked TechCrunch. The "performance-per-watt substantially better" line is unbenchmarked and was not shipped.
- **Watch for:** a confirmed tape-out/manufacturing or first-deployment milestone, named specs or an independent benchmark, a successor chip, or an openable primary carrying specs.
- **Receipts:**
  - https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/
  - https://openai.com/index/openai-broadcom-jalapeno-inference-chip/ (primary; 403s to automated fetch)

### T6 — Anthropic Claude 5 family rollout (post-suspension release line)
- **Status:** developing (Claude Opus 5 GA 24 Jul; POSTED 24 Jul 20:00; AA benchmark ADVANCE 25 Jul 07:00; system card + SWE-bench Verified ADVANCE 25 Jul 13:00)
- **Last material update:** 2026-07-24 (Claude Opus 5 released — GA on Claude API / Claude.ai / Claude Code / Cowork; AA evaluation + System Card same day)
- **Last POSTED:** 2026-07-25 13:00 (ADVANCE — Claude Opus 5 System Card, SWE-bench Verified 96.0% averaged over five trials; "not more capable overall than … Claude Fable 5"). Prior: 25 Jul 07:00 independent AA eval (Opus 5 max 61 AA Intelligence Index, tied with Fable 5, ahead of GPT-5.6 Sol); 24 Jul 20:00 Opus 5 GA ($5/$25 per MTok).
- **One-line state:** On 30 Jun Anthropic released Claude Sonnet 5 (`claude-sonnet-5`) — OSWorld-Verified 78.5%, intro pricing $2/$10 per M through 31 Aug then $3/$15. On 24 Jul Anthropic released Claude Opus 5 (`claude-opus-5`), GA same day, $5/$25 per MTok, "comes close to the frontier intelligence of Claude Fable 5 at half the price"; System Card SWE-bench Verified 96.0%. Fable 5 remains the flagship above Opus 5.
- **Watch for:** a higher-tier Claude 5 release, a published SWE-bench Verified or other coding number for Sonnet 5 or Fable 5, an independent third-party benchmark, or a material capability/pricing change. A restatement of prior launches doesn't re-clear.
- **Receipts:**
  - https://www.anthropic.com/news/claude-opus-5 (24 Jul — "Introducing Claude Opus 5", "available today", $5/$25, "within 0.5% of Fable 5's peak" on CursorBench 3.2 — OPENABLE primary, POSTED 24 Jul 20:00)
  - https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf (24 Jul — System Card: SWE-bench Verified 96.0% avg/5, "not more capable overall than … Claude Fable 5" — OPENABLE primary, ADVANCE POSTED 25 Jul 13:00)
  - https://artificialanalysis.ai/articles/opus-5 (24 Jul — AA independent eval: Opus 5 max 61 AA Index, "$2.03 on average per task, below Claude Fable 5 at $2.75" — OPENABLE independent primary, ADVANCE POSTED 25 Jul 07:00)
  - https://www.anthropic.com/news/claude-sonnet-5 (Claude Sonnet 5 release — POSTED 30 Jun 20:00)

---

## Dormant threads (watch, don't post unless reignited)

_none yet_

---

## Recently closed

_none yet_

# betterwords

Version 2.1.6. Last updated 2026-09-05. Stable filename: `betterwords.md`.

These rules govern durable or external text: articles, reports, reviews, explainers, specs, internal docs, release notes, newsletters, scripts, slides, and similar production writing. They do not govern ordinary chat unless explicitly loaded for it.

The goal is clear, specific, source-respecting text without weak LLM defaults. Do not use these rules to misrepresent authorship where disclosure is required. These rules guide editing decisions. They cannot establish whether a person or model wrote the text, so do not use them to label text as human-written or AI-generated.

## Operating notes

Treat this file as editorial requirements for the text you deliver. Apply them through decisions about meaning, evidence, structure, wording, and the reader's needs while drafting or editing. A writing request requires the requested text. Do not substitute test code, a lint report, a compliance score, or a checklist for that deliverable.

Before drafting, editing, translating, or auditing, read this file completely: the operating notes, all 72 numbered rules, and the final self-check. If a tool returns truncated output or selected excerpts, retrieve every missing part in consecutive chunks before starting the work. Head-and-tail reads, search matches, summaries, remembered rules, and the final self-check alone do not satisfy this requirement. If the complete file is inaccessible, state that limitation and obtain the missing text before proceeding under betterwords.

Consider every rule before deciding how it applies to the current task. Apply the rules thoroughly at their stated severity, using the precedence below and the artifact's intent, audience, and format. For fiction, poetry, legal drafting, transcripts, raw interviews, or short code comments, apply only the parts that fit, after considering the full guidance. Preserve strong passages and justified exceptions; do not manufacture an edit for every rule.

Use the full guidance while composing, then review the complete deliverable against it. Inspect meaning, relationships between claims, structure, and patterns across the whole text as well as individual sentences. A final pass can catch omissions, but it does not replace applying the guidance during writing.

Keep the complete current file available in the working context. Reload it if context loss, compaction, or a version change leaves the full current guidance unavailable. A prior summary or statement that the rules were read is insufficient.

Tools may check read coverage and narrow mechanical requirements. Those checks cannot establish that the rules were understood or that the writing satisfies them. Do not claim that all rules were internalized or passed on the strength of counts, keyword scans, or a self-attestation. Judge editorial application from the actual text in context.

When instructions conflict, follow this order: safety, law, platform rules, and required disclosure; truth and source status; the current task; explicit overrides; required format; audience and style briefs; these rules; taste.

Required format can override prose defaults. Slides, tables, specs, UI copy, release notes, and structured fields may need bullets, fragments, labels, or hierarchy.

Severity descends in this order:

- [N] Never: absolute truth or sourcing rule.
- [H] Hard ban: use only when quoted, source-required, format-required, or explicitly required.
- [D] Density warning: one instance may work; clusters fail.
- [A] Default avoid: use only when it serves the task or format.
- [C] Audit trigger: consider while writing and inspect during the final pass; context decides.

## 1. Truth and sources

1.1. [N] Never invent facts, numbers, dates, names, citations, sources, credentials, real-world examples, firsthand experience, or quotations presented as already spoken. A citation must exist and support its claim. Clearly labeled hypotheticals are allowed when they cannot be mistaken for evidence or real experience.

1.2. [N] A source cannot support a stronger or broader claim than it makes. Preserve uncertainty, caveats, estimates, and scope. Do not turn limited evidence into universal claims.

1.3. [N] For contested or estimated numbers, name the source or method and avoid false precision. Do not turn one or two sources into "many," "widely reported," or equivalent consensus language.

1.4. [N] Do not smooth away conflict, harm, uncertainty, caveats, or asymmetric evidence to improve flow.

1.5. [N] Attribute claims to specific, plausible sources. Do not use unnamed "experts," "studies," "reports," or "critics," manufacture expert status, or fill a short piece with decorative authority.

1.6. [N] When quotation marks present sourced speech or text, they mean the exact sourced words unless the text is clearly presented as a translation under 7.4. Attribute every sourced quotation with enough detail for the intended reader to identify and verify its specific source; attribution depth follows the artifact's sourcing standard. Keep signal phrases and paraphrases outside quotation marks. A user-requested quote for a person who will approve it is proposed copy, not a sourced quote; label it pending approval and stay within supplied facts.

1.7. [C] Preserve a sourced speaker's actual voice. Do not polish a quote into the article's register. Proposed quotes should fit the speaker or office and avoid executive boilerplate.

## 2. Hard bans

2.1. [H] Do not use staged negation formulas: "not just X, but Y," "not only X, but also Y," reversed ("It is X, not just Y") or split ("It may seem like X. But really it is Y.") variants, "no X, no Y, just Z," or stacked "No X. No Y. No Z." slogans.

2.2. [H] Remove generic assistant greetings or praise that the artifact does not call for, plus self-identification, knowledge-cutoff disclaimers, "I hope this helps," "Would you like me to," "Let me know if," opener-position "Here is a," and post-delivery offers.

2.3. [H] Remove filler scaffolding: "in this article," "let's dive in," "here's what you need to know," "it is important to note," "it is worth mentioning," "as everyone knows," and similar throat-clearing.

2.4. [H] Do not replace evidence with inflated significance: pivotal moments, lasting legacies, vital roles, testaments, broader trends, reshaped landscapes, paved ways, raised questions, blurred boundaries, or equivalent claims. Do not use media mentions, recognition lists, or a subject's obscurity as evidence that it matters.

2.5. [H] Do not use promotional or tourism language unless the task is promotional. Cut unsupported superlatives, generic praise, scenic filler, and claims of excellence, innovation, or sustainability.

2.6. [H] Do not use "from X to Y" when the endpoints do not form a real scale. List the items instead.

2.7. [H] Do not use the ritual "Despite [positives], [subject] faces challenges... Despite these challenges..." formula. Name real problems specifically or omit the section.

2.8. [H] Do not rotate synonyms for one referent. Keep the same term unless a different word means a different thing.

2.9. [H] Do not turn missing information into claims about scarcity, privacy, or a subject's low profile. Omit the point, name the verified limit, or state that the source set does not establish it.

## 3. Default avoids and density

3.1. [A] Avoid em dashes. Use commas, parentheses, colons, or semicolons. Use en dashes only for numeric ranges.

3.2. [A] Match the characters to wherever the text will be published, and keep them consistent. Do not mix curly and straight quotes or apostrophes in one document. Strip unsupported markdown, Unicode styling, decorative emoji, and generator artifacts.

3.3. [A] In prose, avoid decorative bullets, bold-keyword-colon lists, pervasive bolding, and small tables. Keep them when the format or data needs them.

3.4. [A] Nest heading levels correctly and use no more hierarchy than the material needs.

3.5. [A] Avoid stale, jargonized, incoherent, or crowded metaphors. Keep a figure only when it clarifies a real relation; replace the rest with the concrete action or condition.

3.6. [A] Avoid nonliteral use of "honest," "magic," "mechanics," and "unlock." Use the direct claim or explanation instead.

3.7. [A] Avoid stance-first pseudo-candor, faux insight, and false-suspense setups such as "let's be clear," "the reality is," "the truth is," "frankly," "what nobody tells you," "the part everyone misses," "what most people get wrong," "here's the thing," "here's the kicker," and "here's where it gets interesting" when they delay the claim, perform conviction, promise an unearned revelation, or assert audience ignorance without support. State the claim and support it.

3.8. [A] Avoid aphorism formulas such as "X is the language, currency, or architecture of Y" when they replace a concrete claim.

3.9. [A] Avoid copula avoidance. Prefer "is" or a precise verb over "serves as," "functions as," "stands as," "represents," "features," "offers," "boasts," "marks," or "constitutes."

3.10. [D] Watch the aggregate density of AI-polish vocabulary in the artifact: additionally, align with, boast, captivate, comprehensive, crucial, cutting-edge, delve, dynamic, elevate, emphasize, encompass, enduring, enhance, ensure, exemplify, foster, garner, groundbreaking, highlight, in-depth, innovative, insightful, interplay, intricate, key as adjective, landscape, leverage, meticulous, multifaceted, navigate figuratively, nestled, notable, nuanced, pivotal, plethora, profound, realm, renowned, robust, seamless, shed light on, showcase, spearhead, tapestry, testament, transformative, underscore, unique, valuable, vibrant. Treat the list as one family: each occurrence of any listed term adds to the cluster, even when no word repeats. Established technical terms and precise domain uses are governed by 4.1 and do not count toward this cluster. One isolated use may be fine; accumulated use is the failure.

3.11. [D] Watch for enumerations shaped for rhythm: habitual triads, slogan-like stacks, anaphora used as default punch, and long comma runs. Include only the items the claim needs.

3.12. [D] Watch for repeated comma-tail sentences: independent clause, comma, tagged-on phrase, especially tails beginning "highlighting," "ensuring," "reflecting," "with," or "such as." One may work; repeated tails make the rhythm mechanical. Cut an empty tail or make a substantive thought its own sentence.

3.13. [D] Watch repeated sentence shells used as default emphasis: routine rhetorical-question pivots, self-answered fragments, dramatic colon reveals such as "The best part: it learns," isolated verdicts such as "That distinction matters" or "This changes everything," and one-line punch paragraphs that add no consequence. One may work when it carries new information or earns the rhythm break; clusters flatten emphasis. Use colons for real grammatical relations, lists, labels, and quotations, not automatic drama. Cut stacked transitions and speech-tag cycling. Use transitions only when logic needs them; default to "said" or "says" unless another tag adds accurate meaning.

3.14. [D] Watch for runs of sentences or paragraphs with the same length, opening, or syntactic shape. Vary structure only when the content calls for it; do not manufacture rhythm for its own sake.

3.15. [D] Watch repeated uses of "here" that point to the writer's argument rather than a literal place, passage, interface state, or source location. Name the referent or remove the marker.

## 4. Sentence craft

4.1. [A] Prefer plain words when meaning is unchanged. Keep technical terms when they are exact, expected, or shorter than the explanation.

4.2. [A] Default to active voice. Passive is useful when the actor is unknown, the receiver matters more, or the register requires it.

4.3. [A] Cut needless words and needless negation: "because" instead of "due to the fact that," "to" instead of "in order to," and "common" instead of "not uncommon," unless the hedge matters.

4.4. [A] Prefer specific nouns, verbs, measurements, and observed behavior over adjective or adverb padding. Adverbs such as "quietly," "deeply," "fundamentally," and "remarkably" often compress a claim about visibility, degree, scope, or significance. State that claim when it matters; keep the adverb when it names a concrete, supported condition. Replace vague judgments such as "amazing," "impressive," "powerful," and "intuitive" with what earns the judgment.

4.5. [A] Cut or quantify "basically," "kind of," "somewhat," and similar softeners when they carry no real degree or source uncertainty. Preserve meaningful hedges.

4.6. [A] Turn nominalizations back into verbs. Avoid business-speak when a direct verb says the same thing.

4.7. [A] Avoid jargon, acronyms, foreign phrases, and technical terms when a normal word is equally exact. Keep and define them when the audience or subject requires them.

4.8. [H] Do not write dangling modifiers. Introductory phrases must attach to the sentence subject.

## 5. Thought and composition

5.1. [C] Decide the claim, evidence, and reader need before choosing phrasing. Do not let familiar phrases generate the thought. If a sentence feels assembled from stock language, rewrite it from the meaning.

5.2. [C] Give each paragraph one job. Split when the claim, time, actor, evidence type, or recommendation changes.

5.3. [C] Use parallel structure for parallel ideas. Keep modifiers and referents close, ambiguous pronouns explicit, and the main point out of throat-clearing or subordinate clauses.

5.4. [C] In summaries and recaps, keep tense consistent unless the timeline changes. Do not drift between past, present, and future for the same event sequence.

5.5. [C] State significance once. Do not explain the obvious inference, recap every paragraph, or restate a heading in the first sentence.

5.6. [C] Keep useful secondary threads, competing causes, caveats, and unresolved effects. Do not force a tidy thesis or uninterrupted causal chain onto complicated material.

5.7. [C] At real choices of example, framing, order, or emphasis, prefer the specific supported choice over the generic center. An anecdote, example, or frame that could move unchanged to another subject is probably too generic; make it specific from supplied evidence or remove it. Do not manufacture quirk or detail; do not default to the median either.

5.8. [C] Do not echo the brief throughout the artifact. Use its terms once where needed, then develop the point. Each paragraph should advance the argument, not restate or redefine it.

5.9. [C] In change-driven documentation, write from the diff. Separate what changed from what remains true, and include baseline material only when needed.

5.10. [C] Every sentence should add information, evidence, qualification, or necessary movement. Check paragraphs and sections too: remove exact or near-duplicate passages and repeated points unless repetition serves a defined rhetorical, navigational, or reference function. Rephrasing the same point does not make it new.

5.11. [C] Test the argument as well as the prose. Each conclusion must follow from the stated premises and evidence; do not let fluent transitions hide a missing step, contradiction, or unsupported causal link.

5.12. [C] Do not let a coined label replace analysis. Define the term, show the observed pattern it names, and distinguish it from established terminology. Clusters of labels ending in words such as "paradox," "trap," "divide," "creep," or "vacuum" are a warning, not a word ban. Keep a label when it is defined, useful, and supported.

## 6. Register and structure

6.1. [C] Match the artifact. Let its purpose and format determine structure, density, and register; do not force every text into the same professional middle.

6.2. [C] When an author sample or baseline is supplied, match its structural habits as well as its register: how quickly it identifies the subject, where it states the main point, how sections open and close, and how much it states before explaining. Read it for those moves as well as tone and vocabulary. Do not normalize it toward generic professional prose or invent a persona without evidence.

6.3. [H] Do not open with generic copywriting scene-setters such as "In today's world," "In an era of," "With the rapid development of," "Whether you're X or Y," or "When it comes to." Do not substitute a manufactured-recognition lead: an interchangeable catalogue of familiar products, tasks, or frustrations whose main job is to signal "you know this problem," followed by escalating consequences and a promise that the piece will provide relief. Concrete nouns do not make the opening specific when swapping them leaves the same persuasive movement intact. Do not promote a secondary detail, number, feature, quotation, or scene to the opening chiefly for punch, surprise, or delayed reveal. Apply the move-down test: if placing it after the subject or central claim preserves the logic and evidence and only reduces the punch, it has not earned the lead. Open with the central claim, evidence, event, decision, or an observed scene whose details carry the argument.

6.4. [C] Do not pre-summarize the whole piece unless the format requires an executive summary.

6.5. [H] Use sentence case and specific headings. Avoid generic labels such as "Overview," "Key takeaways," "Future outlook," "Final thoughts," "Background," "Conclusion," "Impact," and "Challenges and criticism."

6.6. [H] End when done. Avoid summary signals, generic lessons, legacy claims, forced uplift, and final quotations that only repeat the thesis.

6.7. [H] On sensitive subjects, describe harm before any justified optimism, match the evidence's asymmetry, and name agency directly. Do not hide harm behind euphemism.

6.8. [C] State a position when the task and evidence allow it. A genuine aside, question, or direct address may carry content; engagement filler may not. Use supplied perspective or observation, never invented experience.

6.9. [A] Do not fake casualness with contractions, slang, fragments, or reader address the artifact does not support. A conversational register should come from the subject, audience, or supplied voice, not applied mannerisms.

6.10. [C] Avoid generic article skeletons. Let the material, evidence, and reader questions determine section order and length. Do not equalize sections or manufacture matched pros and cons for symmetry. Remove a section that answers no live question or advances no argument.

6.11. [C] Check the title for a generic formula. Use a question, numbered promise, colon construction, or "The hidden cost of X" frame only when it states the artifact's actual subject or claim.

6.12. [C] In procedures, give each independent action its own numbered step. Keep actions together when they must occur at the same time. Put prerequisites and conditions before the command. Keep notes informational; do not hide required actions inside them.

## 7. Multilingual rules

7.1. [C] Write as a competent native writer of the requested language and locale, not as though an English draft had been translated. Build sentences, paragraphs, emphasis, and argument in the target language's natural syntax and discourse habits. Avoid source-language calques, imported sentence shapes, and imported rhetorical structure.

7.2. [C] Preserve a supplied non-native, dialectal, regional, or mixed-language voice when it belongs to the artifact. Correct errors at the requested edit level without normalizing the speaker or author into a generic standard voice.

7.3. [C] Apply every pattern rule by function in the target language. Remove local equivalents of staged negation, filler scaffolding, generic headings, rhetorical pivots, stale metaphors, inflated significance, and bureaucratic nominalization when they create the same failure, even when the wording differs from the English examples.

7.4. [N] Translation and localization must preserve facts, uncertainty, scope, attribution, speaker stance, and material emphasis. Translate quotations faithfully and idiomatically, for sense rather than word-for-word form: change syntax and idiom as needed for natural target-language expression, but do not paraphrase, improve, soften, or intensify the speaker's meaning. Identify a quotation as translated when readers could otherwise assume they are seeing the source-language wording.

7.5. [C] Use established target-language terminology and target-locale conventions. Keep names, transliteration, abbreviations, dates, numbers, units, capitalization, punctuation, quotation, title, and citation conventions consistent. If an established equivalent is uncertain, keep the source term or flag the uncertainty; do not invent a plausible term.

## 8. Rewriting

8.1. [H] Do not treat rewriting as detector evasion. Do not use humanizer-tool tactics, synonym spinning, artificial sentence-length variation, hidden characters, spacing tricks, or edits aimed at manipulating detector metrics such as perplexity or burstiness.

8.2. [C] Interpret "humanize" as a quality rewrite. Preserve meaning, facts, attribution, uncertainty, scope, required format, and length unless instructed otherwise.

8.3. [C] Match the depth of change to the requested edit. When editing the author's own draft, preserve distinctive phrasing and structure that serve its meaning, voice, and format. Replace stock language and repair defects you can name; memorable wording alone is no reason to rewrite. When independently paraphrasing source material, read for meaning, then write in the target register. Preserve exact names, technical terms, and wording required for accuracy; recast distinctive source phrasing and sentence structure, or retain it as an appropriately attributed quotation under 1.6 and 7.4.

8.4. [C] Do not add unsupported claims, examples, sources, sections, hedges, or framing while rewriting.

## Final self-check

Review the complete deliverable against the full guidance in severity order, honoring the operating notes and contextual exceptions. The list below is a condensed reminder; it does not replace reading or applying every rule. Correct the editorial defects you find in the text rather than treating this pass as a mechanical certification.

1. [N] Every fact, source, citation, quotation, number, example, and claim scope is supported; quoted sources are identifiable and verifiable at the artifact's required depth; uncertainty and proposed-copy status remain visible.
2. [H] No staged negation, assistant residue, filler, inflated significance, promotional tone, false range, fake balance, synonym cycling, banned opener or heading, dangling modifier, concealed harm, or forced ending remains.
3. [D] The aggregate density of AI-polish vocabulary, sentence shells, triads, staccato, comma lists and tails, transitions, rhetorical pivots, speech tags, and "here" framing does not create a pattern.
4. [A] Punctuation, formatting, metaphors, nonliteral shortcuts, pseudo-candor, false suspense, compressed adverb claims, aphorism formulas, evaluations, softeners, verbs, jargon, and markup serve the destination and task.
5. [C] Paragraphs have one job; conclusions follow from the stated premises and evidence; structure gives material proportional space and preserves useful complexity; examples are specific and supported; repeated substance is removed unless it has a defined function; coined labels do not replace analysis; headings and conclusions do not restate the point.
6. [C] The artifact matches its format, target language and locale, audience, and supplied voice without inventing or erasing perspective. Procedures separate independent actions, preserve simultaneous actions, put conditions before commands, and keep notes informational. Translations remain faithful and idiomatic; terminology and conventions stay consistent.
7. [C] Rewrites preserve meaning and evidence while replacing the original phrasing and structure where needed.
8. [C] Read once for any sentence that is correct but avoidably awkward, overly even, or mechanically assembled. Revise only defects you can name.
9. End when done.

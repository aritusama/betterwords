# betterwords

Version 2.0.1. Last updated 2026-07-17. Stable filename: `betterwords.md`.

These rules govern durable or external text: articles, reports, reviews, explainers, specs, internal docs, release notes, newsletters, scripts, slides, and similar production writing. They do not govern ordinary chat unless explicitly loaded for it.

The goal is clear, specific, source-respecting text without weak LLM defaults. Do not use these rules to misrepresent authorship where disclosure is required.

## Operating notes

Apply only the parts that fit fiction, poetry, legal drafting, transcripts, raw interviews, or short code comments.

When instructions conflict, follow this order: safety, law, platform rules, and required disclosure; truth and source status; the current task; explicit overrides; required format; audience and style briefs; these rules; taste.

Required format can override prose defaults. Slides, tables, specs, UI copy, release notes, and structured fields may need bullets, fragments, labels, or hierarchy.

Severity descends in this order:

- [N] Never: absolute truth or sourcing rule.
- [H] Hard ban: use only when quoted, source-required, format-required, or explicitly required.
- [D] Density warning: one instance may work; clusters fail.
- [A] Default avoid: use only when it serves the task or format.
- [C] Audit trigger: inspect during the final pass; context decides.

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

3.5. [A] Avoid stale or jargonized metaphors. Replace them with the concrete action or condition.

3.6. [A] Avoid nonliteral use of "honest," "magic," "mechanics," and "unlock." Use the direct claim or explanation instead.

3.7. [A] Avoid stance-first pseudo-candor such as "let's be clear," "the reality is," "the truth is," "frankly," and "in all honesty" when it delays or performs conviction. State the claim and support it.

3.8. [A] Avoid aphorism formulas such as "X is the language, currency, or architecture of Y" when they replace a concrete claim.

3.9. [A] Avoid copula avoidance. Prefer "is" or a precise verb over "serves as," "functions as," "stands as," "represents," "features," "offers," "boasts," "marks," or "constitutes."

3.10. [D] Watch the aggregate density of AI-polish vocabulary in the artifact: additionally, align with, boast, captivate, comprehensive, crucial, cutting-edge, delve, dynamic, elevate, emphasize, encompass, enduring, enhance, ensure, exemplify, foster, garner, groundbreaking, highlight, in-depth, innovative, insightful, interplay, intricate, key as adjective, landscape, leverage, meticulous, multifaceted, navigate figuratively, nestled, notable, nuanced, pivotal, plethora, profound, realm, renowned, robust, seamless, shed light on, showcase, spearhead, tapestry, testament, transformative, underscore, unique, valuable, vibrant. Treat the list as one family: each occurrence of any listed term adds to the cluster, even when no word repeats. Established technical terms and precise domain uses are governed by 4.1 and do not count toward this cluster. One isolated use may be fine; accumulated use is the failure.

3.11. [D] Watch for triads and rhythmic formulas: three adjectives, three clauses, slogan-like stacked nouns, and anaphora used as default punch. Let the content determine the grouping.

3.12. [D] Watch for repeated comma-tail sentences: independent clause, comma, tagged-on phrase, especially tails beginning "highlighting," "ensuring," "reflecting," "with," or "such as." One may work; repeated tails make the rhythm mechanical. Cut an empty tail or make a substantive thought its own sentence.

3.13. [D] Cut stacked transitions, routine rhetorical-question pivots, fragment punches, and speech-tag cycling. Use transitions only when logic needs them; default to "said" or "says" unless another tag adds accurate meaning.

3.14. [D] Watch for runs of sentences or paragraphs with the same length, opening, or syntactic shape. Vary structure only when the content calls for it; do not manufacture rhythm for its own sake.

## 4. Sentence craft

4.1. [A] Prefer plain words when meaning is unchanged. Keep technical terms when they are exact, expected, or shorter than the explanation.

4.2. [A] Default to active voice. Passive is useful when the actor is unknown, the receiver matters more, or the register requires it.

4.3. [A] Cut needless words and needless negation: "because" instead of "due to the fact that," "to" instead of "in order to," and "common" instead of "not uncommon," unless the hedge matters.

4.4. [A] Prefer specific nouns, verbs, measurements, and observed behavior over adjective or adverb padding. Replace vague judgments such as "amazing," "impressive," "powerful," and "intuitive" with what earns the judgment.

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

5.7. [C] At real choices of example, framing, order, or emphasis, prefer the specific supported choice over the generic center. Do not manufacture quirk; do not default to the median either.

5.8. [C] Do not echo the brief throughout the artifact. Use its terms once where needed, then develop the point. Each paragraph should advance the argument, not restate or redefine it.

5.9. [C] In change-driven documentation, write from the diff. Separate what changed from what remains true, and include baseline material only when needed.

5.10. [C] Every sentence should add information, evidence, qualification, or necessary movement. Cut sentences that only rephrase what the reader already knows.

## 6. Register and structure

6.1. [C] Match the artifact. Let its purpose and format determine structure, density, and register; do not force every text into the same professional middle.

6.2. [C] When an author sample or baseline is supplied, match its register and habits. Do not normalize it toward generic professional prose or invent a persona without evidence.

6.3. [H] Do not open with generic copywriting scene-setters such as "In today's world," "In an era of," "With the rapid development of," "Whether you're X or Y," or "When it comes to." Open with a fact, tension, claim, or scene.

6.4. [C] Do not pre-summarize the whole piece unless the format requires an executive summary.

6.5. [H] Use sentence case and specific headings. Avoid generic labels such as "Overview," "Key takeaways," "Future outlook," "Final thoughts," "Background," "Conclusion," "Impact," and "Challenges and criticism."

6.6. [H] End when done. Avoid summary signals, generic lessons, legacy claims, forced uplift, and final quotations that only repeat the thesis.

6.7. [H] On sensitive subjects, describe harm before any justified optimism, match the evidence's asymmetry, and name agency directly. Do not hide harm behind euphemism.

6.8. [C] State a position when the task and evidence allow it. A genuine aside, question, or direct address may carry content; engagement filler may not. Use supplied perspective or observation, never invented experience.

6.9. [A] Do not fake casualness with contractions, slang, fragments, or reader address the artifact does not support. A conversational register should come from the subject, audience, or supplied voice, not applied mannerisms.

6.10. [C] Avoid generic article skeletons. Let the material and the reader's questions determine section order; remove a section that answers no live question or advances no argument.

6.11. [C] Check the title for a generic formula. Use a question, numbered promise, colon construction, or "The hidden cost of X" frame only when it states the artifact's actual subject or claim.

## 7. Multilingual rules

7.1. [C] Write as a competent native writer of the requested language and locale, not as though an English draft had been translated. Build sentences, paragraphs, emphasis, and argument in the target language's natural syntax and discourse habits. Avoid source-language calques, imported sentence shapes, and imported rhetorical structure.

7.2. [C] Preserve a supplied non-native, dialectal, regional, or mixed-language voice when it belongs to the artifact. Correct errors at the requested edit level without normalizing the speaker or author into a generic standard voice.

7.3. [C] Apply every pattern rule by function in the target language. Remove local equivalents of staged negation, filler scaffolding, generic headings, rhetorical pivots, stale metaphors, inflated significance, and bureaucratic nominalization when they create the same failure, even when the wording differs from the English examples.

7.4. [N] Translation and localization must preserve facts, uncertainty, scope, attribution, speaker stance, and material emphasis. Translate quotations faithfully and idiomatically, for sense rather than word-for-word form: change syntax and idiom as needed for natural target-language expression, but do not paraphrase, improve, soften, or intensify the speaker's meaning. Identify a quotation as translated when readers could otherwise assume they are seeing the source-language wording.

7.5. [C] Use established target-language terminology and target-locale conventions. Keep names, transliteration, abbreviations, dates, numbers, units, capitalization, punctuation, quotation, title, and citation conventions consistent. If an established equivalent is uncertain, keep the source term or flag the uncertainty; do not invent a plausible term.

## 8. Rewriting

8.1. [H] Do not treat rewriting as detector evasion. Do not use humanizer-tool tactics, synonym spinning, artificial sentence-length variation, hidden characters, spacing tricks, or edits aimed at manipulating detector metrics such as perplexity or burstiness.

8.2. [C] Interpret "humanize" as a quality rewrite. Preserve meaning, facts, attribution, uncertainty, scope, required format, and length unless instructed otherwise.

8.3. [C] Do not lightly edit around memorable phrases, stock transitions, paragraph shape, or syntactic formulas. Read for meaning, then rewrite in the target register.

8.4. [C] Do not add unsupported claims, examples, sources, sections, hedges, or framing while rewriting.

## Final self-check

Run checks in severity order:

1. [N] Every fact, source, citation, quotation, number, example, and claim scope is supported; quoted sources are identifiable and verifiable at the artifact's required depth; uncertainty and proposed-copy status remain visible.
2. [H] No staged negation, assistant residue, filler, inflated significance, promotional tone, false range, fake balance, synonym cycling, banned opener or heading, dangling modifier, concealed harm, or forced ending remains.
3. [D] The aggregate density of AI-polish vocabulary, triads, staccato, comma tails, transitions, rhetorical pivots, and speech tags does not create a pattern.
4. [A] Punctuation, formatting, stale metaphors, nonliteral shortcuts, pseudo-candor, aphorism formulas, evaluations, softeners, verbs, jargon, and markup serve the destination and task.
5. [C] Paragraphs have one job; structure preserves useful complexity; headings, examples, and conclusions do not restate the point.
6. [C] The artifact matches its format, target language and locale, audience, and supplied voice without inventing or erasing perspective. Translations remain faithful and idiomatic; terminology and conventions stay consistent.
7. [C] Rewrites preserve meaning and evidence while replacing the original phrasing and structure where needed.
8. [C] Read once for any sentence that is correct but avoidably awkward, overly even, or mechanically assembled. Revise only defects you can name.
9. End when done.

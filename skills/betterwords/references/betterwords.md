# betterwords

Version 1.1.1. Last updated 2026-07-10 15:12 EEST. Stable filename: `betterwords.md`.

These rules govern text artifacts produced for external or durable use: articles, reports, reviews, technical explainers, opinion pieces, user stories, release notes, specs, internal docs, newsletters, scripts, slide text, infographic text, and similar production writing. They do not govern ordinary conversational replies unless explicitly loaded for that purpose.

The goal is clear, specific, source-respecting production text that avoids weak LLM defaults. Do not use these rules to misrepresent authorship where disclosure is required.

## Operating notes

Use these rules for long-form non-fiction and structured professional writing. They are not calibrated for fiction, poetry, legal drafting, transcripts, raw interview text, or short code comments. In those cases, apply only the parts that fit the artifact.

When instructions conflict, follow this order: safety, law, platform rules, and required disclosure; truth, source status, and uncertainty; the user's current task; explicit one-off overrides; artifact format; style, audience, and format briefs; these betterwords rules; taste.

Format can override prose defaults. Slides, infographics, tables, release notes, specs, UI copy, and structured fields may require bullets, fragments, labels, tight hierarchy, or tables. Apply these rules inside the chosen format instead of forcing all output into flowing prose.

Use the severity terms this way. Each rule begins with a one-letter code.

[N] never means an absolute rule that must not be broken; it governs the truth and sourcing rules in section 1.

[H] Hard ban means do not use unless quoted, source-required, format-required, or explicitly required by the user.

[A] Default avoid means avoid unless it genuinely serves the task or format.

[D] Density warning means one instance may be fine; clusters are the failure.

[C] Audit trigger means check during final pass; context decides.

## 1. Truth and source rules

1.1. [N] Never invent facts, numbers, dates, names, quotes, citations, sources, examples, credentials, or firsthand experience.

1.2. [N] Use real perspective only when supplied or source-backed. Do not fabricate lived experience, product testing, interviews, or editorial observation.

1.3. [N] A source cannot support a stronger claim than it makes. If the source says "may," "could," "early evidence," or "limited data," preserve that uncertainty.

1.4. [N] For contested or estimated numbers, name the source or method. Round when precision is false. Do not call one or two sources "several," "many," "widely reported," or "broadly recognized."

1.5. [N] Do not smooth away conflict, caveats, harm, uncertainty, or asymmetry to make the piece read better.

1.6. [N] Do not attribute claims to "experts," "studies," "industry reports," "observers," "critics," or "scholars" unless the source is named.

1.7. [N] Sourcing must be plausible, not merely attributed. Do not populate a short piece with named experts or titled authorities unless real reporting would warrant them. Do not promote ordinary sources to "experts," "analysts," or "Dr. X" for cosmetic authority. If the source, role, and relevance are not real and clear, drop the quote or state the claim directly with evidence.

1.8. [N] Quote literally and attribute specifically. Quotation marks mean the exact words appear in the source.

1.9. [N] Keep quote mechanics clean. Signal phrases stay outside quotation marks; paraphrases do not get quotation marks; direct quotes must be verbatim; when paraphrasing first-person material, adjust pronouns and verbs; use the target language's title and quotation conventions.

1.10. [C] When the user explicitly asks for a quote attributed to a specific person who will review, approve, or sign off on it, such as a CEO quote in a press release, treat the task as copywriting for that speaker. Write the quote in the intended speaker's role and likely register, but do not present it as already said, sourced, or published.

1.11. [C] Quote voice must come from the source, not from the article voice. Do not invent polished quotes or make every speaker sound like the narrator. If a quote is too neat, generic, or vocabulary-matched to the article, verify it, paraphrase without quotation marks, or remove it.

1.12. [C] For approved ghostwritten quotes, avoid generic executive boilerplate. The quote should sound like something that person or office could plausibly approve, not like a summary paragraph with quotation marks.

1.13. [N] A citation must exist and must support the claim attached to it. Do not attach real-looking but unchecked references, do not invent DOIs, ISBNs, or URLs, and do not over-cite to manufacture rigor.

## 2. Hard-banned writing patterns

2.1. [H] Do not use "not just X, but Y," "not only X, but also Y," reversed variants such as "It is X, not just Y," or split variants such as "It may seem like X. But really it is Y."

2.2. [H] Do not use "no X, no Y, just Z" framings. They create the same staged contrast as the main negation cliché.

2.3. [H] Do not use stacked negation slogans such as "No X. No Y. No Z." This is a separate failure from ordinary rule-of-three rhythm. It creates synthetic emphasis by defining the subject through staged denial.

2.4. [H] Do not use conversational AI remnants in production text, including "I hope this helps," "Would you like me to," "Let me know if," "Is there anything else," "Certainly," "Of course," "Great question," "Absolutely," "Here is a," "Here's a breakdown," "as an AI language model," "as of my last update," "as of my knowledge cutoff," and "I cannot browse the internet."

2.5. [H] Do not use filler scaffolding, including "in this article, we will," "it is important to note," "it should be noted," "it is worth mentioning," "it is hard to overestimate," "no discussion would be complete without," "as everyone knows," and "as they say."

2.6. [H] Do not use vague attribution without a named source, including "industry reports suggest," "experts believe," "some critics argue," "many consider," "scholars note," "has been described as," "widely regarded as," and "often considered."

2.7. [H] Do not use inflated significance as a substitute for evidence, including "pivotal moment," "watershed moment," "key turning point," "stands as," "serves as a testament," "plays a vital/significant/crucial role," "leaves a lasting legacy," "indelible mark," "cements its place," "solidifies its position," "reshaping the landscape," "part of a broader trend," "paving the way," "setting the stage," "raises questions about," "sparks debate about," and "blurs the boundaries between."

2.8. [H] Do not use promotional or tourism language unless the task is explicitly promotional, including "rich cultural heritage," "breathtaking natural beauty," "must-see," "must-visit," "dynamic hub," "vibrant community," "in the heart of," "nestled within," "diverse array," "wide range of experiences," and "commitment to excellence/innovation/sustainability."

2.9. [H] Do not use false ranges where endpoints do not form a real scale. "From artistic expression to technological innovation" is not a range. List the items instead.

2.10. [H] Do not use the empty balance formula: "Despite [positives], [subject] faces challenges... Despite these challenges, [subject] continues..." If problems exist, name them specifically. If they do not matter, omit the section.

2.11. [H] Do not rotate synonyms for the same referent. If the text says "system," keep saying "system" unless a different word means a different thing. Do not cycle "smartphone/device/handset/unit" or "company/firm/organization" for variety.

## 3. Default-avoid patterns

3.1. [A] Avoid em dashes. Use commas, parentheses, colons, or semicolons. Use en dashes only for numeric ranges.

3.2. [A] Avoid bullet lists in prose contexts. Use bullets only when the format needs them or when each bullet carries a real argument, recommendation, or data point.

3.3. [A] Do not use the bold-keyword-colon list pattern unless a structured spec requires labels. Do not bold key terms throughout running prose either; bold is for genuine emphasis or required labels.

3.4. [A] Avoid small tables where prose is clearer. Use tables for structured comparisons or data, not for dressing up two facts.

3.5. [A] Avoid title-case headings. Use sentence case. Headings should name the specific section content, not generic labels such as "Overview," "Key takeaways," "Future outlook," or "Final thoughts."

3.6. [A] Avoid stale metaphors, including move the needle, low-hanging fruit, at the end of the day, level the playing field, double-edged sword, tip of the iceberg, game-changer, deep dive, circle back, unpack, on the same page, push the envelope, raise the bar, elephant in the room, perfect storm, think outside the box, bottom line, and boots on the ground.

3.7. [A] Avoid copula avoidance. Do not replace "is" and "are" with "serves as," "stands as," "represents," "features," "boasts," "marks," or "constitutes" unless the verb is precise.

3.8. [A] Match the characters to wherever the text will be published, and keep them consistent. Do not mix curly and straight quotes or apostrophes in one document. Strip generator artifacts: Unicode bold or italic letters, arrows in running prose, Unicode bullet glyphs where the format uses plain text, and decorative emoji, especially in headings.

3.9. [A] Strip markdown the destination will not render. When output goes to email, plain text, or a CMS field, remove leftover hashes, asterisks, and horizontal rules. Leave no markup the target does not parse.

3.10. [A] Keep heading levels properly nested. Do not skip levels (put an H2 under an H1, not an H3), do not start a document below its top level, and do not add headings a short piece does not need. Heading depth should track the actual structure.

## 4. Density warnings

4.1. [D] Watch for clusters of AI-polish vocabulary: additionally, align with, boast, captivate, comprehensive, crucial, cutting-edge, delve, dynamic, elevate, emphasize, encompass, enduring, enhance, ensure, exemplify, foster, garner, groundbreaking, highlight, in-depth, innovative, insightful, interplay, intricate, key as adjective, landscape, leverage, meticulous, multifaceted, navigate figuratively, nestled, notable, nuanced, pivotal, plethora, profound, realm, renowned, robust, seamless, shed light on, showcase, spearhead, tapestry, testament, transformative, underscore, unique, valuable, vibrant. The issue is density, not the existence of one ordinary word. Remove clusters first.

4.2. [D] Watch for triads and rhythmic formulas: three adjectives, three clauses, slogan-like stacked nouns, and anaphora used as default punch. Use two or four items when the content calls for it.

4.3. [D] Watch the broader comma-tail shape: independent clause, comma, tagged-on phrase. The tail does not have to be an "-ing" phrase. One in a paragraph is fine; several in a row make the rhythm mechanical.

4.4. [D] Treat "..., highlighting," "..., ensuring," "..., reflecting," "..., with," and "..., such as" as common comma-tail forms when they append fake depth. If the thought matters, make it a specific sentence. If it does not, cut it.

4.5. [D] Watch for transition stacking: moreover, furthermore, however, in addition, additionally, on the other hand, in contrast. Use them only when the logical relation would otherwise be unclear.

4.6. [D] Default to "said" or "says" for speech tags. Use "argued," "claimed," "conceded," "wrote," or "asked" only when the verb adds accurate information. Do not cycle "explains," "notes," "remarks," "emphasizes," and "concludes" for variety.

## 5. Sentence craft

5.1. [A] Use plain words when they mean the same thing: use not utilize, help not facilitate, show not demonstrate, about not approximately, start not commence, get not obtain, try not endeavor, end not terminate, buy not purchase, need not necessitate, build not construct, enough not sufficient.

5.2. [C] Keep the longer word when it carries a real technical distinction.

5.3. [A] Default to active voice. Passive is fine when the actor is unknown, the receiver matters more, or the register requires it.

5.4. [A] Cut needless words: "because" not "due to the fact that," "to" not "in order to," "now" not "at this point in time," "many" not "a large number of," "if" not "in the event that," "before" not "prior to," and "can" not "has the ability to."

5.5. [A] Use positive form where possible: "common" not "not uncommon," "significant" not "not insignificant," and "similar" not "not dissimilar," unless the partial hedge is genuinely the point.

5.6. [A] Prefer specific nouns and verbs over adjective/adverb padding. "The system handles 10,000 requests per second" beats "the system processes requests quickly."

5.7. [A] Avoid nominalizations and business-speak when the verb is clearer: "decide" instead of "decision-making," "implement" instead of "implementation," and "improve" instead of "enhancement." If the main verb is "is," "has," "involves," "represents," or "constitutes," look for an action noun and turn it back into a verb.

5.8. [A] Avoid jargon, foreign phrases, acronyms, and technical terms when a normal word says the same thing. Keep technical terms when they are exact, expected by the audience, or shorter than the explanation. Define unavoidable jargon on first use unless the audience already knows it.

5.9. [H] Avoid dangling modifiers. Introductory participial phrases must attach to the sentence subject: "After reviewing the logs, the team found the bug," not "After reviewing the logs, the bug was found."

## 6. Thought and composition

6.1. [C] Decide the claim, evidence, and reader need before choosing phrasing. Do not let familiar phrases generate the thought. If a sentence feels assembled from stock language, rewrite it from the meaning.

6.2. [C] Make each paragraph do one job. If a paragraph changes claim, time, actor, evidence type, or recommendation, split it. In analytical prose, the first sentence should usually state the paragraph's point; the rest should support, qualify, or apply it.

6.3. [C] Use parallel structure for parallel ideas. In lists, comparisons, headings, acceptance criteria, and release notes, keep matching items in the same grammatical form unless there is a reason to break the pattern.

6.4. [C] Keep related words close. Put modifiers next to what they modify. Keep subject, verb, and object as close as clarity allows. Avoid unclear "this," "that," "it," and "they" when the referent could be ambiguous.

6.5. [C] Put emphasis where readers feel it, usually at the end of the sentence or paragraph. Do not bury the main point in a subordinate clause, parenthesis, or throat-clearing opener.

6.6. [C] In summaries and recaps, keep tense consistent unless the timeline changes. Do not drift between past, present, and future for the same event sequence.

6.7. [C] Do not restate the significance the evidence already carries. State the point once and let it stand. Spelling out the takeaway right after the example, or telling the reader what to feel about a fact, is over-determination. Trust the reader to make the obvious inference. This includes paragraph-closing recaps: do not end each paragraph by restating what it just said.

6.8. [C] A piece may carry more than one thread. Forcing everything onto a single linear spine, or unifying every part to the thesis with suspiciously perfect tidiness, is a machine default. Secondary threads and complications that enrich the main line are a sign of real authorship. This is compatible with 6.2: each paragraph still does one job; the whole piece need not reduce to one track.

6.9. [C] At each real fork (which example, which framing, which order, which emphasis), the safe central option is the choice most writers and models reach for. Prefer the specific, earned, less generic choice when the material supports it. This is a conception-level decision about substance, not a surface edit, and it is distinct from the detector-metric edits banned in 9.1. Do not manufacture quirk; do not default to the median either.

6.10. [C] Do not echo the brief or prompt back. Repeating the task's key terms throughout, defining them, and restating the question is a strong machine tell; it reads like copy written to define terms rather than writing that uses them and moves on. Use the brief's terms once where needed, then develop the point. Each paragraph should advance the argument, not restate or redefine it.

## 7. Register and structure

7.1. [C] Match the artifact. A technical spec can be dry and structured. A review can include judgment and firsthand details if supplied. A report can use substantive bullets. A release note can be compressed. Do not force every text into the same polished middle register.

7.2. [H] Do not open with "In today's world," "In an era of," "With the rapid development of," or "When it comes to." Instead, open with a concrete fact, tension, claim, or scene.

7.3. [C] Do not pre-summarize the whole piece in the first paragraph unless the format requires an executive summary. Start with something specific. Let the piece unfold instead of handing the reader the entire article in miniature.

7.4. [H] Use sentence case for headings. Avoid generic header templates, including "Overview," "Key takeaways," "Future outlook," "Final thoughts," "Understanding [topic]," "How [topic] works," "Looking ahead," "Background," "Conclusion," "Legacy," "Impact," "Reception," "Significance," and "Challenges and criticism." Headings should name the specific question, claim, or section content.

7.5. [H] End when done. Do not close with "In summary," "Overall," "In conclusion," generic lessons, legacy claims, or forced uplift. A conclusion can offer a practical recommendation, a forward-looking observation, or a hard stop.

7.6. [C] Do not outsource the conclusion to a speaker. A final quote that neatly restates the thesis is a strong AI tell. If a quote belongs at the end, it should add a specific detail, complication, or unresolved question. Otherwise end in the writer's voice or stop when done.

7.7. [H] For sensitive topics, do not pivot to optimism before describing harm. Do not manufacture balance when evidence is asymmetric. Match the seriousness of the subject.

7.8. [H] Do not hide agency or harm behind euphemism. Use direct wording when the source supports it.

7.9. [C] Applying rules with no authorial judgment produces clean-but-flat text. State positions when the task allows and the evidence supports them. Use supplied perspective, source-backed detail, or real observation. Do not invent perspective to solve flatness.

7.10. [A] Do not collapse multiple or competing causes into one tidy chain. Real explanations have contributing factors, partial causes, dead ends, and effects that do not fully resolve. A clean, uninterrupted line from cause to effect is a structural default, not usually the true shape. This extends 1.5 from content to structure.

7.11. [A] Where the artifact allows a voice, a genuine aside, question, or direct address to the reader - use it, provided it carries real content and does not contradict the style. This differs from the conversational filler banned in 2.4: a real aside qualifies, complicates, or adds information; filler greets, pads, or offers help. Do not add engagement for its own sake.

7.12. [C] When a voice sample or author baseline is supplied, match its register and habits; do not normalize toward the generic middle. This applies only when a real baseline exists. Without one, do not invent a persona to fake voice (see 1.2 and 7.9).

## 8. Multilingual rules

8.1. [C] Write as a competent native speaker of the target language, not as a translation from English. Avoid English calques, imported syntax, and target-language equivalents of AI-polish vocabulary.

8.2. [C] Use established target-language terminology unless a foreign term is genuinely standard. Watch for the local version of bureaucratic, nominalization-heavy register. Apply quotation, title, punctuation, and citation conventions for the target language.

## 9. Rewriting existing AI-like text

9.1. [H] Do not treat rewriting as detector evasion. Do not use humanizer-tool tactics, synonym spinning, artificial sentence-length variation, hidden characters, spacing tricks, or edits aimed at manipulating detector metrics such as perplexity or burstiness.

9.2. [C] When asked to humanize, improve, or rewrite existing AI-like text, interpret the task as a quality rewrite. If the user explicitly asks for detector evasion, do not perform that task; offer a quality rewrite instead. Preserve meaning, facts, attribution, uncertainty, scope, and required format.

9.3. [C] Do not lightly edit around the source's memorable phrases, stock transitions, paragraph shape, or syntactic formulas. Those patterns often survive paraphrasing and remain visible to readers and detection tools.

9.4. [C] Read for meaning, then rewrite from scratch in the target register. Preserve length unless instructed otherwise. Do not add hedges, sections, claims, examples, sources, or framing that the source did not support.

## Final self-check

Before delivery, run the checks in severity order, clearing the firmest constraints first.

[N] never, then [H] hard ban:

1. Check for invented or unsupported facts, numbers, quotes, citations, sources, credentials, or experience.
2. Check whether the draft overclaims, hides source uncertainty, uses vague attribution, invents authority, or mishandles quotes.
3. Check for hard-banned patterns including negation cliché, stacked negation slogan, conversational remnant, filler scaffolding, inflated significance, promotional tone, synonym cycling, false range, and fake balance.

[D] density:

4. Check for density problems including clustered AI vocabulary, triads, comma tails, transition stacking, and speech-tag cycling.

[A] default avoid:

5. Check whether any default-avoid pattern appears without a format or task reason, including em dashes, prose bullets, small tables, generic headings, stale metaphors, copula avoidance, mixed quote styles, stray markup, Unicode or emoji artifacts, and skipped heading levels.
6. Check sentence craft for needless words, weak verbs, nominalizations, passive overuse, jargon, and false precision.

[C] audit:

7. Check whether the artifact format justifies bullets, labels, tables, fragments, or hierarchy.
8. Check composition for paragraph unity, related words close, parallel structure, emphasis placement, and tense consistency.
9. Check structure for over-explained significance, over-unification to one thesis, safe-default framing, brief-echoing, and single-track causality.
10. Check voice for specificity, baseline match when a sample is supplied, clean-but-flat wording, fake-casual register, and generic professional middle.
11. Check the finish for generic closing offers or post-delivery suggestions unless they are specifically useful.

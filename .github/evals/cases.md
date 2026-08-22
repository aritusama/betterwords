# betterwords behavioral evaluations

Run these cases manually against Codex, Claude, and Gemini before release. Record the host, model, date, and pass or fail result. Model calls stay out of pull-request CI.

## Case 1: preserve source uncertainty

- User request: "Rewrite this finding for a report."
- Input artifact and sources: Draft: "The pilot may reduce processing time." Source: "Early results suggest the pilot may reduce processing time."
- Expected mode: Rewrite.
- Required invariants: Keep `may` or an equivalent uncertainty marker.
- Prohibited changes: Do not state that the pilot reduces processing time.
- Pass/fail rubric: Pass if the result stays no stronger than the source.

## Case 2: do not invent support

- User request: "Make this product note more persuasive."
- Input artifact and sources: Draft: "The update changes the export screen." No sources or measurements.
- Expected mode: Rewrite.
- Required invariants: Preserve the supplied fact only.
- Prohibited changes: Do not add citations, measurements, customers, experience, or real-world examples.
- Pass/fail rubric: Pass if every factual claim comes from the input.

## Case 3: permit a labeled hypothetical

- User request: "Add one hypothetical example that explains the rule."
- Input artifact and sources: Rule: "Round numbers when precision is false." No source is needed because the example is hypothetical.
- Expected mode: Draft.
- Required invariants: Label the example as hypothetical and use invented values only inside that frame.
- Prohibited changes: Do not imply that the people, event, or measurements are real.
- Pass/fail rubric: Pass if the example is useful and cannot be mistaken for evidence.

## Case 4: label a proposed executive quote

- User request: "Draft a CEO quote for a press release; the CEO will approve it."
- Input artifact and sources: Product facts supplied by the user. No prior CEO quotation.
- Expected mode: Draft.
- Required invariants: Label the text `Proposed quote, awaiting speaker approval` and stay within supplied facts.
- Prohibited changes: Do not call the quote spoken, approved, sourced, or published.
- Pass/fail rubric: Pass if status and approval boundary are explicit.

## Case 5: preserve a sourced quotation

- User request: "Copyedit this paragraph."
- Input artifact and sources: Draft contains `The lead said, "We found three faults."` The source contains those exact words.
- Expected mode: Copyedit.
- Required invariants: Keep the quoted words verbatim and preserve attribution.
- Prohibited changes: Do not polish or expand the quotation.
- Pass/fail rubric: Pass if the quoted string is byte-for-byte unchanged.

## Case 6: keep a copyedit narrow

- User request: "Copyedit for grammar and punctuation only."
- Input artifact and sources: A complete two-paragraph release note with an intentional informal voice.
- Expected mode: Copyedit.
- Required invariants: Correct grammar and punctuation while preserving meaning, order, voice, and paragraph structure.
- Prohibited changes: Do not add headings, rewrite paragraphs, or replace the voice with a generic professional register.
- Pass/fail rubric: Pass if edits are local and every substantive choice remains intact.

## Case 7: audit without rewriting

- User request: "Audit this draft with betterwords."
- Input artifact and sources: Draft includes `Experts believe this pivotal moment will reshape the landscape.` No named source.
- Expected mode: Audit.
- Required invariants: Report findings in severity order with the exact excerpt, rule number, explanation, proposed correction, and confidence status.
- Prohibited changes: Do not return a silently rewritten draft.
- Pass/fail rubric: Pass if the response is a findings report and distinguishes firm violations from judgment calls.

## Case 8: preserve required formats

- User request: "Copyedit these slides, table cells, specification fields, and release-note bullets."
- Input artifact and sources: Structured fragments in all four formats, with labels and bullets required by their destinations.
- Expected mode: Copyedit.
- Required invariants: Keep each format, hierarchy, field name, and concise fragment style.
- Prohibited changes: Do not convert the material into prose paragraphs or remove useful labels and bullets.
- Pass/fail rubric: Pass if format requirements override prose defaults where they conflict.

## Case 9: do not trigger in ordinary chat

- User request: "What time is the meeting?"
- Input artifact and sources: Calendar time supplied in chat; no durable writing artifact requested.
- Expected mode: No betterwords invocation.
- Required invariants: Answer the question directly.
- Prohibited changes: Do not audit or rewrite the user's sentence.
- Pass/fail rubric: Pass if betterwords remains inactive unless explicitly requested.

## Case 10: remove translationese from Ukrainian prose

- User request: "Line edit this Ukrainian article without changing its facts or voice."
- Input artifact and sources: A Ukrainian draft with grammatical sentences but English-shaped syntax, paragraph pivots, and rhetorical structure, including repeated `Що з цього можна взяти?` transitions.
- Expected mode: Line edit.
- Required invariants: Rebuild sentences and paragraph flow in natural Ukrainian while preserving facts, register, and authorial intent.
- Prohibited changes: Do not preserve translationese merely because each sentence is grammatical, and do not translate the article into English.
- Pass/fail rubric: Pass if a competent Ukrainian editor would read the result as original Ukrainian prose rather than an English-shaped translation.

## Case 11: keep literal almost-banned words

- User request: "Copyedit without changing correct wording."
- Input artifact and sources: `John was honest about his skills in magic. The manual explains the game's combat mechanics. Unlock the account with the recovery code.`
- Expected mode: Copyedit.
- Required invariants: Preserve every literal use of `honest`, `magic`, `mechanics`, and `unlock`.
- Prohibited changes: Do not treat any of the words as unconditionally banned.
- Pass/fail rubric: Pass if all three sentences remain unchanged unless an unrelated mechanical correction is required.

## Case 12: revise rhetorical almost-banned words

- User request: "Copyedit these product claims."
- Input artifact and sources: `Here is my honest take. The magic is in the workflow. The mechanics of trust unlock lasting value.`
- Expected mode: Copyedit.
- Required invariants: Replace authenticity claims, vague praise, figurative shorthand, and explanation substitutes with direct wording supported by context.
- Prohibited changes: Do not replace words mechanically or introduce new claims.
- Pass/fail rubric: Pass if each rhetorical shortcut is identified and revised for meaning.

## Case 13: explain structural findings as quality problems

- User request: "Audit this draft."
- Input artifact and sources: The draft repeats the prompt in every paragraph, ends with a quotation that restates the thesis, and lightly swaps synonyms while keeping the source paragraph shape.
- Expected mode: Audit.
- Required invariants: Identify prompt echoing, a redundant final quotation, and shallow paraphrase using rules 5.8, 6.6, and 8.3.
- Prohibited changes: Do not claim to detect authorship or use `machine tell`, `AI tell`, `human marker`, or detector visibility as the rationale.
- Pass/fail rubric: Pass if every explanation names the concrete writing failure and proposes a concise correction.

## Case 14: preserve scope and replace vague evaluation

- User request: "Rewrite this finding for a report."
- Input artifact and sources: Draft: `The pilot always unlocks amazing results. It basically makes processing somewhat faster.` Source: `Early results suggest the pilot may reduce median processing time by 8%.`
- Expected mode: Rewrite.
- Required invariants: Preserve `may`, the 8% result, and its median scope.
- Prohibited changes: Do not keep the universal claim, figurative `unlock`, vague praise, or empty softeners.
- Pass/fail rubric: Pass if the rewrite states the measured result without widening or weakening it.

## Case 15: remove formulaic transitions and aphorisms

- User request: "Copyedit this paragraph without adding claims."
- Input artifact and sources: `Let's be clear: trust is the currency of collaboration. So what does this mean? The result? Better teams. What can we take from this?`
- Expected mode: Copyedit.
- Required invariants: Preserve the supported idea that trust helps teams collaborate.
- Prohibited changes: Do not retain stance-first pseudo-candor, the aphorism formula, or the stack of rhetorical pivots and fragments.
- Pass/fail rubric: Pass if the result states the idea directly in one natural sentence or paragraph.

## Case 16: anchor change documentation to the diff

- User request: "Write a release note for this patch."
- Input artifact and sources: The diff changes timeout handling only. The supplied draft uses an `Overview` heading, repeats that heading in its first sentence, and describes the unchanged request pipeline at length.
- Expected mode: Rewrite.
- Required invariants: Name the timeout-handling change and any supported user effect.
- Prohibited changes: Do not keep the generic heading, restate a heading, or present unchanged baseline behavior as new.
- Pass/fail rubric: Pass if the note is anchored to the actual diff and omits irrelevant baseline description.

## Case 17: translate a quotation faithfully and idiomatically

- User request: "Translate this sourced English quotation for a Ukrainian article."
- Input artifact and sources: An English source quotation with attribution, uncertainty, emphasis, and a colloquial phrase; the article does not otherwise make the translation status obvious.
- Expected mode: Rewrite.
- Required invariants: Preserve meaning, uncertainty, stance, material emphasis, and attribution while using natural Ukrainian syntax and idiom; identify the quotation as translated.
- Prohibited changes: Do not paraphrase, improve, soften, intensify, or back-translate the speaker.
- Pass/fail rubric: Pass if the Ukrainian quotation is faithful in meaning, natural in form, and clearly presented as a translation.

## Case 18: preserve a supplied mixed-language voice

- User request: "Copyedit this interview excerpt for punctuation only."
- Input artifact and sources: A sourced quotation with deliberate regional phrasing and code-switching that identifies the speaker's actual voice.
- Expected mode: Copyedit.
- Required invariants: Correct only punctuation and preserve the speaker's regional and mixed-language choices.
- Prohibited changes: Do not normalize the quotation into generic standard prose or remove intentional code-switching.
- Pass/fail rubric: Pass if the mechanical correction is clean and the speaker still sounds like the source.

## Case 19: keep terminology and locale conventions consistent

- User request: "Line edit this target-language report and keep its established conventions."
- Input artifact and sources: The report and its sources establish terminology, transliteration, abbreviations, dates, decimal notation, numbers, and units.
- Expected mode: Line edit.
- Required invariants: Keep the established target-language terms and locale choices consistent throughout.
- Prohibited changes: Do not switch transliteration systems, mix locale conventions, or invent a plausible equivalent when an established term is uncertain.
- Pass/fail rubric: Pass if terminology and locale conventions remain consistent and uncertain equivalents are retained or flagged rather than invented.

## Case 20: preserve precise technical uses

- User request: "Copyedit this technical report without weakening exact terminology."
- Input artifact and sources: `The model uses robust standard errors and dynamic panel estimation. The draft later calls the workflow a robust, dynamic, comprehensive solution that ensures success.`
- Expected mode: Copyedit.
- Required invariants: Keep `robust standard errors` and `dynamic panel estimation` as established technical terms; treat the later watchlist words as a separate density judgment.
- Prohibited changes: Do not strip precise technical terms or exempt every watchlist word merely because the artifact is technical.
- Pass/fail rubric: Pass if exact terminology remains and generic promotional wording is assessed under rule 3.10.

## Case 21: judge title formulas by function

- User request: "Audit these title options for a report."
- Input artifact and sources: The report measures retry costs in batch exports and answers whether retries increase processing cost. Options: `Batch Exports: Measured Retry Costs`; `Do Retries Increase Processing Cost?`; `The Hidden Cost of Reliability`; `7 Retry Secrets You Need to Know`. The report supports no hidden mechanism, secrets, or seven-item list.
- Expected mode: Audit.
- Required invariants: Apply rule 6.11 contextually; preserve title forms that state the supported subject or question and flag formulas that substitute unsupported framing.
- Prohibited changes: Do not reject a colon, question, or number solely because of its form, and do not retain unsupported hype.
- Pass/fail rubric: Pass if each title is judged against the report's actual subject, claim, and format.

## Case 22: catch an unsupported causal inference

- User request: "Audit this argument without rewriting it."
- Input artifact and sources: The source reports that support tickets fell 12% in the month after a navigation redesign. It does not test causation or retention. Draft: `The redesign caused the 12% decline in support tickets and will improve retention.`
- Expected mode: Audit.
- Required invariants: Preserve the observed sequence and 12% result; identify the missing causal inference and unsupported retention conclusion under rule 5.11.
- Prohibited changes: Do not discard the supported observation, invent an alternative cause, or silently rewrite the draft.
- Pass/fail rubric: Pass if the finding distinguishes the sourced observation from both unsupported conclusions.

## Case 23: reduce repeated argument-pointing words across languages

- User request: "Line edit this Ukrainian article without changing its meaning."
- Input artifact and sources: `Тут важливо врахувати витрати. Тут ми бачимо головний ризик. Тут варто повернутися до даних. Залиште коробки тут.` The first three uses of `тут` point to the argument; the last is a physical-location instruction.
- Expected mode: Line edit.
- Required invariants: Apply rule 3.15 by function under rule 7.3; revise the repeated argument-pointing uses and preserve the literal location.
- Prohibited changes: Do not ban `тут`, remove its literal use, or alter the claims.
- Pass/fail rubric: Pass if the prose no longer repeats `тут` as argumentative scaffolding and the physical-location instruction keeps its meaning.

## Case 24: judge sentence shells by function and density

- User request: "Line edit this analysis without flattening intentional emphasis."
- Input artifact and sources: Source: `The retry limit fell from five to two, and median recovery time fell from 18 seconds to 9.` Draft: `The retry limit fell from five to two. The result? Median recovery time fell from 18 seconds to 9. That distinction matters. This changes everything. The reason? Simpler than it looks.`
- Expected mode: Line edit.
- Required invariants: Preserve both measured changes; allow an isolated self-answered fragment if it carries the supported result; remove or replace empty verdicts and unsupported setup-payoff shells.
- Prohibited changes: Do not ban every short paragraph or rhetorical form, add consequences, or claim that the pattern establishes authorship.
- Pass/fail rubric: Pass if the supported result retains appropriate emphasis without a cluster of reusable sentence shells.

## Case 25: let content determine enumeration length

- User request: "Copyedit this policy note and keep required options."
- Input artifact and sources: The policy permits exactly `email, SMS, voice, or postal notice` and says only that the guide serves `professionals`. Draft: `Notice may arrive by email, SMS, voice, or postal notice. The guide helps writers, editors, designers, coders, teachers, students, founders, managers, consultants, and creators work better.`
- Expected mode: Copyedit.
- Required invariants: Keep all four policy options and preserve the supported audience description.
- Prohibited changes: Do not shorten a content-required list, retain the rhythmic audience inventory, or invent narrower audience categories.
- Pass/fail rubric: Pass if list length follows the supported content rather than a mechanical preference for short or long enumeration.

## Case 26: remove crowded metaphors without weakening facts

- User request: "Rewrite this technical update in direct prose."
- Input artifact and sources: Source: `The queue buffers bursts of up to 100 events. The migration moves 12 services from host A to host B.` Draft: `The queue is our shock absorber. The migration is a bridge, compass, engine, and safety net carrying 12 services into a new home.`
- Expected mode: Rewrite.
- Required invariants: Preserve the queue limit, service count, source host, and destination host.
- Prohibited changes: Do not retain the crowded or incoherent imagery, replace precise technical language mechanically, or add migration benefits.
- Pass/fail rubric: Pass if the result states both operations concretely and every retained figure clarifies a real relation.

## Case 27: replace a portable example only from supplied evidence

- User request: "Rewrite this report example so it supports the finding."
- Input artifact and sources: Source: `On 14 July, the finance team missed the 16:00 export cutoff after a timeout.` Draft: `Many teams discover that change is difficult, but challenges can become opportunities for growth.`
- Expected mode: Rewrite.
- Required invariants: Use the supplied date, team, cutoff, and cause if an example remains.
- Prohibited changes: Do not invent feelings, dialogue, personal experience, consequences, or decorative detail.
- Pass/fail rubric: Pass if the generic portable example is removed or replaced only with the specific supported incident.

## Case 28: give evidence proportional structural space

- User request: "Restructure this assessment around the supplied findings."
- Input artifact and sources: The sources contain six decision-relevant deployment failures and one minor convenience benefit. The draft gives equal-length `Benefits` and `Challenges` sections and adds two unsupported benefits to complete the symmetry.
- Expected mode: Rewrite.
- Required invariants: Preserve all supported findings, remove unsupported benefits, and let decision relevance and evidence determine section order and length.
- Prohibited changes: Do not force equal sections, manufacture a matched pro or con, or hide the evidence's asymmetry.
- Pass/fail rubric: Pass if the structure reflects the supplied evidence and reader decision rather than visual balance.

## Case 29: remove faux insight, false suspense, and dramatic colon reveals by function

- User request: "Line edit this post without flattening its voice."
- Input artifact and sources: Source: `The retry limit fell from five to two, and median recovery time fell from 18 seconds to 9.` Draft: `What nobody tells you about the retry change. Here's the kicker: the best part: median recovery time fell from 18 seconds to 9.`
- Expected mode: Line edit.
- Required invariants: Preserve the measured recovery-time change and the author's direct register.
- Prohibited changes: Do not retain unsupported audience-ignorance framing, false suspense, or automatic colon drama; infer authorship; or rewrite the supported result into generic prose.
- Pass/fail rubric: Pass if the result states the measured change directly, removes the faux-insight setup, false-suspense setup, and dramatic colon reveal, and leaves the supported substance intact.

## Case 30: structure procedure actions by function

- User request: "Copyedit this procedure without changing its operation."
- Input artifact and sources: `1. Press TEST and record the displayed value. 2. Hold CLAMP and press RESET at the same time. Note: If the pressure exceeds 50 psi, close valve V1.` The first step contains sequential actions, the second contains simultaneous actions, and the note contains a required conditional action.
- Expected mode: Copyedit.
- Required invariants: Give the two sequential actions separate numbered steps; keep the simultaneous actions together; move the required action out of the note; put its pressure condition before the command; preserve the controls, threshold, valve identifier, and operation order.
- Prohibited changes: Do not split actions that must occur at the same time, leave a required action inside a note, change the pressure threshold, or invent safety claims.
- Pass/fail rubric: Pass if each independent action is a step, the simultaneous pair remains together, and the conditional command is no longer hidden in a note.

## Case 31: reject a manufactured-recognition lead by function

- User request: "Audit these two opening options with betterwords without rewriting them."
- Input artifact and sources: Source: `Three source systems deliver CSV, JSON, and Parquet files. A missing transformation record prevented the finance team from reproducing the 14 July dashboard.` Option A: `A CSV arrives from one system, JSON from another, Parquet from somewhere else. You know how it goes: soon nobody knows what to trust. This guide will put you back in control.` Option B: `The finance team could not reproduce the 14 July dashboard because its transformation record was missing.`
- Expected mode: Audit.
- Required invariants: Flag Option A under rule 6.3 as a manufactured-recognition lead; explain that its catalogue, presumed shared experience, escalation, and relief promise perform a portable persuasive sequence; preserve Option B as a specific supported incident.
- Prohibited changes: Do not infer human or model authorship, reject every list or problem-led opening, weaken the supported incident, or return silently rewritten options.
- Pass/fail rubric: Pass if the audit identifies Option A's rhetorical function, accepts Option B's evidence-bearing scene, and proposes a concise claim-first correction without adding facts.

## Case 32: judge significance adverbs by function

- User request: "Audit these sentences with betterwords without rewriting them."
- Input artifact and sources: Source packet: `The fan measured 22 dBA. The company removed its price page without a public notice or changelog entry. Two interpretations remain possible; the second accounts for both supplied measurements, while the first accounts for one. No source establishes an industry transformation or broader importance.` Sentences: A: `The policy quietly transformed the industry.` B: `The fan ran quietly at 22 dBA.` C: `The company quietly removed the price page; it issued no notice, and the changelog omitted the change.` D: `The second interpretation is arguably stronger because it accounts for both measurements.` E: `This is arguably a remarkably important development.`
- Expected mode: Audit.
- Required invariants: Flag A and E under rule 4.4 because their adverbs compress unsupported claims; preserve B as measurable manner, C as supported low visibility, and D as a meaningful hedge under rule 4.5.
- Prohibited changes: Do not ban `quietly`, `remarkably`, `arguably`, or adverbs as a class; remove supported uncertainty; infer authorship; or return silently rewritten sentences.
- Pass/fail rubric: Pass if the audit distinguishes unsupported significance from concrete manner, supported visibility, and meaningful epistemic qualification.

## Case 33: distinguish coined labels from useful terms

- User request: "Audit these three explanations for conceptual clarity without rewriting them."
- Input artifact and sources: Source packet: `Approval time rose from two to nine days after a second review step, and queue length doubled. Retry error rates were 2%, 3%, and 4% through the third attempt, then 19% on the fourth. The team defines retry cliff as the measured jump after the third retry. Backpressure describes the system reducing intake when consumer lag exceeds 500 messages.` A: `The approval-latency paradox created a trust vacuum and an execution divide.` B: `We call the measured error-rate jump after the third retry the retry cliff.` C: `Backpressure reduced intake when consumer lag exceeded 500 messages.`
- Expected mode: Audit.
- Required invariants: Flag A under rule 5.12 because its label cluster replaces the observed pattern and mechanism; preserve B because the local term is defined and supported; preserve C as an established technical term used precisely.
- Prohibited changes: Do not ban words ending in `paradox`, `trap`, `divide`, `creep`, or `vacuum`; reject every locally coined term; replace precise terminology with vague plain language; or infer authorship.
- Pass/fail rubric: Pass if the audit judges labels by definition, analytical use, and support rather than vocabulary alone.

## Case 34: remove repeated substance across an artifact

- User request: "Audit this report section for repetition without rewriting it."
- Input artifact and sources: Required format: `Include a one-sentence executive summary.` Source: `In a 30-day comparison, median export time fell from 12 minutes to 7.` Draft: `Executive summary: Median export time fell from 12 minutes to 7. Results: In the 30-day comparison, median export time fell from 12 minutes to 7. Discussion: Exports are now five minutes faster at the median. Conclusion: The migration shortened median export time from 12 minutes to 7.`
- Expected mode: Audit.
- Required invariants: Preserve the required executive summary and one evidence-bearing body statement; flag the discussion and conclusion restatements under rule 5.10 unless they add interpretation, qualification, or consequence.
- Prohibited changes: Do not remove all repetition mechanically, delete required navigation, invent consequences, infer authorship, or return a silently rewritten report.
- Pass/fail rubric: Pass if the audit distinguishes repetition with a defined format function from near-duplicate passages that add no information or movement.

## Case 35: reject historical analogy accumulation as proof

- User request: "Audit the argument in this launch note without rewriting it."
- Input artifact and sources: The supplied source packet supports the three precedent descriptions and states that the current product has 200 beta users, but it contains no adoption forecast or evidence that the products share relevant market conditions. Draft: `AWS began with infrastructure services. Slack grew from an internal tool. Instagram launched with a narrow photo-sharing scope. Our product will follow the same path and become the category standard.`
- Expected mode: Audit.
- Required invariants: Preserve sourced precedent facts as possible illustrations; flag the prediction under rule 5.11 because accumulated analogies do not establish comparable conditions, causation, or inevitability.
- Prohibited changes: Do not treat the number or fame of examples as proof, invent shared conditions, discard every analogy, infer authorship, or silently rewrite the launch note.
- Pass/fail rubric: Pass if the audit separates supported precedent descriptions from the unsupported generalization and predictive conclusion.

## Case 36: match structural habits in a supplied baseline

- User request: "Audit this opening against the supplied author baseline without rewriting it."
- Input artifact and sources: Source: `The Meridian M4 is a 14-inch laptop. In the supplied battery test, it averaged 11 hours.` Baseline A: `The Northstar S2 is a 13-inch laptop for field technicians. Its battery lasted 9 hours in the supplied test.` Baseline B: `The Vector Mini is a compact workstation for video editing. It completed the supplied render in 7 minutes.` Both baseline openings identify the subject in the first sentence and then present the measurement. Draft: `Battery life averaged 11 hours in the supplied test. The Meridian M4 is a 14-inch laptop.`
- Expected mode: Audit.
- Required invariants: Flag the draft under rule 6.2 because it matches the baseline's direct register but reverses its consistent subject-first structural habit; preserve the supplied product description and measurement.
- Prohibited changes: Do not reject evidence-led openings as a class, claim that rule 6.3 independently bans the draft, invent additional baseline habits, infer authorship, or return a silently rewritten opening.
- Pass/fail rubric: Pass if the audit identifies a structural baseline mismatch rather than a tone mismatch and explains that the same opening could be valid without the supplied baseline.

## Case 37: reject a punch-first secondary-detail opening by function

- User request: "Audit these three opening options with betterwords without rewriting them."
- Input artifact and sources: Source: `The Aster 32 monitor replaces the dedicated adaptive-sync module used in the Aster 27 with a standards-based controller, which removes the need for an internal cooling fan. The cable opening in the stand is 6 mm wider. The source gives the wider opening no functional significance.` Option A: `The cable opening is 6 mm wider. It is the first visible difference on this monitor. The monitor is the Aster 32, which replaces its predecessor's dedicated adaptive-sync module with a standards-based controller and no longer needs an internal cooling fan.` Option B: `The Aster 32 replaces its predecessor's dedicated adaptive-sync module with a standards-based controller, removing the need for an internal cooling fan.` Option C: `The Aster 32 has no internal cooling fan because its dedicated adaptive-sync module has been replaced with a standards-based controller.`
- Expected mode: Audit.
- Required invariants: Flag Option A under rule 6.3 because it promotes a supported but secondary measurement chiefly for punch and delayed identification; apply the move-down test and preserve Options B and C because their opening details carry the central supported change.
- Prohibited changes: Do not ban numbers, product details, or detail-led openings as classes; weaken the supported module and fan claims; infer authorship; or return silently rewritten options.
- Pass/fail rubric: Pass if the audit distinguishes a secondary-detail kicker from claim-bearing specificity and permits an earned concrete opening.

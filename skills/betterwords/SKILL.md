---
name: betterwords
description: Apply source-respecting writing and editing rules to durable text artifacts. Use for drafting, rewriting, copyediting, line editing, or auditing articles, reports, reviews, documentation, release notes, specifications, scripts, slide text, and infographic text. Do not use for ordinary conversational replies unless explicitly requested.
---

# betterwords

Load [betterwords](./references/betterwords.md) before working on the artifact. Apply its rules inside production text, not to ordinary conversation around the task.

## Draft or rewrite

- Return the production text first.
- Preserve supplied facts, attribution, uncertainty, scope, and required format.
- Notice the artifact's distinctive vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish. Preserve supported voice signals and leave strong passages alone.
- Add only short notes about material assumptions or unresolved source problems.

## Copyedit or line edit

- Edit at the level requested. Do not silently turn a copyedit into a rewrite.
- Make the minimum effective edit. Leave strong sentences untouched and do not make every paragraph equally tidy.
- Return the edited artifact first.
- Mention only consequential changes, ambiguity, or unresolved source problems.

## Audit

- Do not silently rewrite the artifact unless asked.
- Report findings in severity order.
- For each finding, include the exact excerpt, rule number, explanation, and a concise proposed correction.
- For a grouped rule, name the specific pattern after the rule number.
- Explain findings as writing-quality problems. Do not infer human or model authorship from them.
- Distinguish confirmed violations from judgment calls.

## Verification boundary

When verification and rewriting are both requested, verify claims against the sources and test the argument before polishing the prose. Do not describe an output as fact-checked unless the task included source verification. If verification was required but sources were unavailable, label the factual status as unverified.

# betterwords common instructions

Apply betterwords only when the user asks for durable or external text: articles, reports, reviews, technical explainers, opinion pieces, user stories, release notes, specs, internal docs, newsletters, scripts, slide text, infographic text, and similar production writing.

Do not apply betterwords to ordinary chat unless the user explicitly asks.

Use `betterwords.md` as the rule source. If `betterwords.md` is not available in the current chat, project, Gem, GPT, or repository context, say that the betterwords rule file is missing and ask the user to attach or paste it.

When applying betterwords:

1. Identify whether the user wants drafting, revision, copyediting, line editing, or audit.
2. Read or retrieve the relevant sections of `betterwords.md` before editing. Do not rely on memory of the rules.
3. Preserve supplied facts, attribution, uncertainty, scope, and format requirements.
4. Do not add facts, sources, sourced quotations, numbers, product claims, or firsthand experience. Add a hypothetical example or proposed quote only when the user requests it, the rule file permits it, and its status is explicit.
5. Do not make weak evidence sound stronger than it is.
6. Apply the hard bans, default avoids, density warnings, sentence craft rules, and final self-check in `betterwords.md`.
7. For medium or long outputs, separate the production text from short notes about material assumptions or unresolved source issues.
8. For an audit, report findings in severity order instead of silently rewriting the artifact.
9. For drafting, rewriting, copyediting, or line editing, return the production text first.

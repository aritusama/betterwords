# Changelog

All notable changes to betterwords are documented here. This project follows [Semantic Versioning](https://semver.org) and the [Keep a Changelog](https://keepachangelog.com) format.

## [2.1.0] - 2026-07-21

### Added

- Added an explicit boundary against inferring human or model authorship from writing-quality findings.
- Added density guidance for self-answered fragments, empty importance verdicts, one-line punch paragraphs, and long comma-run enumerations.
- Added checks for incoherent or crowded metaphors, portable generic examples, and section symmetry that ignores evidence or reader need.
- Added five behavioral cases covering sentence-shell density, content-driven enumeration, metaphor coherence, portable examples, and proportional structure.

### Changed

- Expanded the final self-check to name sentence shells and comma lists, inspect metaphor function, require supported specific examples, and give material proportional space.
- Added the authorship boundary to the README and skill audit contract.

### Sources

- [The Rise of Verbal Tics in Large Language Models](https://arxiv.org/abs/2604.19139) informed the aggregate treatment of repetitive formulaic patterns.
- [EQ-Bench Slop Score](https://eqbench.com/slop-score.html) and Hamed Paydarfar's editorial field report, [5 Dead Giveaways You Are Reading AI-Generated Text](https://medium.com/@By.Anchorite/gpt-5-5-update-5-dead-giveaways-you-are-reading-ai-generated-text-c1076073567f), supplied comparison examples. They do not validate authorship classification; betterwords uses them only as prompts for writing-quality review.

## [2.0.3] - 2026-07-21

### Added

- Added rule 3.15, a density warning for repeated argument-pointing uses of `here` and their functional equivalents in other languages while preserving literal uses.
- Added a multilingual behavioral case for repeated Ukrainian `тут` framing.

## [2.0.2] - 2026-07-17

### Added

- Added an argument-validity check for missing steps, contradictions, and unsupported causal links.
- Added a behavioral case that separates a supported observation from unsupported causal and predictive conclusions.

### Changed

- Required verification and argument testing before prose polishing when both verification and rewriting are requested.
- Added argument validity to the final structure self-check.

## [2.0.1] - 2026-07-17

### Added

- Added a contextual audit check for generic title formulas.
- Added behavioral cases for precise technical vocabulary and title-form judgment.

### Changed

- Exempted established technical terms and precise domain uses from the rule 3.10 vocabulary cluster under rule 4.1.
- Required audit findings on grouped rules to name the specific pattern after the rule number.

## [2.0.0] - 2026-07-13

### Added

- Allowed clearly labeled hypothetical examples while continuing to prohibit invented real-world examples.
- Made proposed quotes an explicit truth-tier exception and required clear labeling until speaker approval.
- Required sourced quotations to be identifiable and verifiable at the depth expected by the artifact.
- Added faithful, idiomatic quotation translation while preserving meaning, attribution, stance, uncertainty, and emphasis.
- Added targeted checks for nonliteral `honest`, `magic`, `mechanics`, and `unlock`.
- Added checks for unsupported universal claims, stance-first pseudo-candor, aphorism formulas, vague evaluation, empty softeners, manufactured staccato, heading restatements, and diff-anchored documentation.
- Restored concise checks for knowledge-gap speculation, notability puffing, repeated structural shapes, fake casualness, generic article skeletons, sentence-level informational progress, and avoidably awkward prose.
- Expanded multilingual guidance for translation-shaped prose, supplied non-native or mixed-language voice, functional equivalents of English patterns, and locale consistency.
- Added Codex skill metadata and human-readable behavioral evaluations.
- Documented foundational and later research and comparison influences.

### Changed

- Reorganized and compressed the canonical rules into eight sections, with breaking rule-number changes throughout.
- Defined AI-polish density across the full vocabulary family and restored the complete watchlist.
- Restored the explicit `not only X, but also Y` negation variant and expanded the copula-avoidance examples.
- Split false ranges from fake balance, nominalizations from jargon, format from voice matching, prompt echo from diff anchoring, and triads from comma-tail sentences.
- Kept `End when done` as the final and only severity-free self-check.
- Reframed detector-oriented explanations around concrete writing failures such as redundancy, prompt echoing, shallow paraphrase, and over-tidy structure.
- Tightened draft, rewrite, copyedit, line-edit, audit, and verification output contracts.
- Resolved overlapping severity ownership for headings, vague attribution, copula avoidance, and dangling modifiers.
- Made the `[N]`, `[H]`, `[D]`, `[A]`, `[C]` order explicit and tied post-delivery remnants to rule 2.4.
- Expanded source-strength, filler, stale-metaphor, specificity, structure, and final-audit guidance.
- Updated Codex, Claude, Gemini, Antigravity, ChatGPT, and Copilot installation guidance.
- Moved convenience documentation and infographic assets under `.github/` to keep the repository root focused on `betterwords.md` and required host manifests.

## [1.1.3] - 2026-07-10

### Added

- Added `gemini-extension.json` for Gemini CLI extension discovery.
- Added a root `plugin.json` for Google Antigravity plugin discovery.

### Changed

- Updated Gemini setup docs to lead with native extension and skill installation.
- Kept Gemini web Gems as the fallback setup for hosts without native skill loading.

## [1.1.2] - 2026-07-10

### Added

- Added Claude Code plugin and marketplace manifests under `.claude-plugin/`.

### Changed

- Updated Claude setup docs to lead with native Skill and plugin installation.
- Clarified that Claude Project instructions are fallback setup where custom skills are unavailable.

## [1.1.1] - 2026-07-10

### Changed

- Clarified Codex installation as the primary one-command skill path: `npx skills add aritusama/betterwords`.
- Marked platform setup files as manual fallback adapters for assistants that cannot install Codex skills.

## [1.1.0] - 2026-06-29

Adds a severity code to every rule and a layer of structural and mechanical rules. Earlier versions covered surface style; 1.1.0 extends coverage to discourse-level structure, which survives paraphrasing, and to the character-level and formatting artifacts that mark machine-pasted text. No existing rule was removed or weakened.

### Added

- Severity codes on every rule. Each rule begins with a one-letter code: `[N]` never, `[H]` hard ban, `[A]` default avoid, `[D]` density warning, `[C]` audit trigger. The legend is defined in Operating notes.
- `[N]` tier for the truth and sourcing rules in section 1, marking them as absolute.
- 1.13 `[N]`: a citation must exist and support its claim; no invented DOIs, ISBNs, or URLs; no over-citation.
- 3.8 `[A]`: match characters to the publication target and keep them consistent (no mixed curly and straight quotes, no stray Unicode glyphs or emoji).
- 3.9 `[A]`: strip markdown the target will not render.
- 3.10 `[A]`: keep heading levels properly nested; do not skip levels or start a document below its top level.
- 6.7 `[C]`: do not restate significance the evidence already carries, including paragraph-closing recaps.
- 6.8 `[C]`: a piece may carry more than one thread; do not over-unify everything to a single thesis.
- 6.9 `[C]`: prefer the specific, earned choice over the safe central default at each fork.
- 6.10 `[C]`: do not echo the brief or prompt back.
- 7.10 `[A]`: do not collapse multiple or competing causes into one tidy chain.
- 7.11 `[A]`: genuine reader address can carry real content and is distinct from conversational filler.
- 7.12 `[C]`: match a supplied voice or author baseline; do not invent a persona without one.

### Changed

- The final self-check now runs in severity order, grouped by code: `[N]` and `[H]` first, then `[D]`, then `[A]`, then `[C]`.
- 2.4 extended with AI self-identification and knowledge-cutoff remnants ("as an AI language model," "as of my last update," "I cannot browse the internet").
- 2.7 extended with the vague-impact construction ("raises questions about," "sparks debate about," "blurs the boundaries between").
- 3.3 extended to cover bolding key terms throughout running prose, not only bold-colon lists.
- 7.4 extended with Legacy, Impact, Reception, Significance, and "Challenges and criticism" as generic headers to avoid.

### Sources

The structural rules (6.7 to 6.10, 7.10 to 7.12) were informed by [StoryScope](https://arxiv.org/abs/2604.03136), which studies AI-generated fiction, and Wikipedia's editorial field guide, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing). StoryScope does not by itself validate rules for reports, reviews, journalism, specifications, or other nonfiction, and neither source supports using these patterns as a general-purpose authorship test. The rules use the sources as prompts for writing-quality review; the section 9 ban on detector evasion is unchanged.

## [1.0.0] - 2026-05-20

First public release. Truth and sourcing rules, hard-banned patterns, default-avoid patterns, density warnings, sentence craft, thought and composition, register and structure, multilingual rules, a rewriting section with a hard ban on detector evasion, and a final self-check.

[2.1.0]: https://github.com/aritusama/betterwords/releases/tag/v2.1.0
[2.0.3]: https://github.com/aritusama/betterwords/releases/tag/v2.0.3
[2.0.2]: https://github.com/aritusama/betterwords/releases/tag/v2.0.2
[2.0.1]: https://github.com/aritusama/betterwords/releases/tag/v2.0.1
[2.0.0]: https://github.com/aritusama/betterwords/releases/tag/v2.0.0
[1.1.3]: https://github.com/aritusama/betterwords/releases/tag/v1.1.3
[1.1.2]: https://github.com/aritusama/betterwords/releases/tag/v1.1.2
[1.1.1]: https://github.com/aritusama/betterwords/releases/tag/v1.1.1
[1.1.0]: https://github.com/aritusama/betterwords/releases/tag/v1.1.0
[1.0.0]: https://github.com/aritusama/betterwords/releases/tag/v1.0.0

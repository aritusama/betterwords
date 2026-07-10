# Changelog

All notable changes to betterwords are documented here. This project follows [Semantic Versioning](https://semver.org) and the [Keep a Changelog](https://keepachangelog.com) format.

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
- 7.11 `[A]`: genuine reader address is a human marker, distinct from conversational filler.
- 7.12 `[C]`: match a supplied voice or author baseline; do not invent a persona without one.

### Changed

- The final self-check now runs in severity order, grouped by code: `[N]` and `[H]` first, then `[D]`, then `[A]`, then `[C]`.
- 2.4 extended with AI self-identification and knowledge-cutoff remnants ("as an AI language model," "as of my last update," "I cannot browse the internet").
- 2.7 extended with the vague-impact construction ("raises questions about," "sparks debate about," "blurs the boundaries between").
- 3.3 extended to cover bolding key terms throughout running prose, not only bold-colon lists.
- 7.4 extended with Legacy, Impact, Reception, Significance, and "Challenges and criticism" as generic headers to avoid.

### Sources

The structural rules (6.7 to 6.10, 7.10 to 7.12) draw on StoryScope (Russell et al., arXiv:2604.03136), which finds AI fiction separable by discourse-level structure after style is removed; a CNET piece by Rachel Kane on reading for AI tells; and Wikipedia's Signs of AI writing, which also motivates the mechanical rules (3.8 to 3.10) and several list extensions. These are quality rules; the section 9 ban on detector evasion is unchanged.

## [1.0.0] - 2026-05-20

First public release. Truth and sourcing rules, hard-banned patterns, default-avoid patterns, density warnings, sentence craft, thought and composition, register and structure, multilingual rules, a rewriting section with a hard ban on detector evasion, and a final self-check.

[1.1.3]: https://github.com/aritusama/betterwords/releases/tag/v1.1.3
[1.1.2]: https://github.com/aritusama/betterwords/releases/tag/v1.1.2
[1.1.1]: https://github.com/aritusama/betterwords/releases/tag/v1.1.1
[1.1.0]: https://github.com/aritusama/betterwords/releases/tag/v1.1.0
[1.0.0]: https://github.com/aritusama/betterwords/releases/tag/v1.0.0

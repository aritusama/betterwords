# betterwords

![betterwords 2.0.0 overview](.github/assets/betterwords-2.0.0.png)

Source-respecting rules for drafting, rewriting, copyediting, and auditing durable text.

`betterwords.md` is the product. The skill, plugin manifests, and platform notes are convenience methods for loading that file in different hosts.

## Install the skill

The cross-agent Skills CLI installs betterwords for the current project by default:

```sh
npx skills add aritusama/betterwords
```

Install it for the current user instead:

```sh
npx skills add aritusama/betterwords -g
```

The installer discovers the single skill at `skills/betterwords`.

## Install the Codex plugin

Add this repository as a Codex marketplace:

```sh
codex plugin marketplace add aritusama/betterwords
codex plugin add betterwords@betterwords
```

You can also install `betterwords` from Plugins in the ChatGPT desktop app after adding the marketplace. This repository marketplace is separate from the public Plugins Directory; betterwords does not claim a public directory listing.

## Other hosts

- Claude supports the same skill and a namespaced Claude Code plugin. See [Claude setup](.github/platforms/claude.md).
- Gemini CLI supports extension and standalone-skill installation; Antigravity supports the plugin folder. See [Gemini and Antigravity setup](.github/platforms/gemini.md).
- GitHub Copilot can use repository instructions. See [GitHub Copilot setup](.github/platforms/github-copilot.md).
- Hosts without skill support can use `betterwords.md` with the [short instruction adapter](.github/platforms/common-instructions.md). See [ChatGPT setup](.github/platforms/chatgpt.md) for custom GPT and Project use.

## Use

```text
Use betterwords to copyedit this release note without changing supported facts.
```

```text
Use betterwords to audit this draft for quality.
```

Betterwords is a writing-quality system. It cannot determine whether a person or model wrote a text. Do not use it to label authorship, evade required disclosure, or fabricate sources, quotations, experience, or evidence.

## Sources and influences

betterwords is independently written. These sources shaped named parts of the ruleset:

- William Strunk Jr.'s [The Elements of Style](https://www.gutenberg.org/ebooks/37134), later expanded by E. B. White, established the baseline for active voice, positive form, concrete language, paragraph unity, parallel structure, related words, emphasis, and removing needless words.
- George Orwell's [Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/) informed the meaning-first rule, plain wording, stale-metaphor checks, active voice, and the instruction to cut words that do no work.
- The [Human Detectors paper](https://arxiv.org/abs/2501.15654) and its [annotator data](https://github.com/jenna-russell/human_detectors) informed checks for manufactured sourcing, quotation voice and integration, comma-tailed sentences, speech-tag cycling, generic headings, pre-summarizing introductions, sanitized framing, and nominalization.
- [StoryScope](https://arxiv.org/abs/2604.03136) informed structural checks for over-tidy composition, prompt echo, and loss of useful complications. These checks are applied as writing-quality diagnostics, not as proof of authorship.
- [The Rise of Verbal Tics in Large Language Models](https://arxiv.org/abs/2604.19139) informed the aggregate treatment of repetitive formulaic patterns. [EQ-Bench Slop Score](https://eqbench.com/slop-score.html) and Hamed Paydarfar's editorial field report, [5 Dead Giveaways You Are Reading AI-Generated Text](https://medium.com/@By.Anchorite/gpt-5-5-update-5-dead-giveaways-you-are-reading-ai-generated-text-c1076073567f), supplied comparison examples for contrastive and sentence-shell patterns. These sources do not validate authorship classification; the rules use them only as writing-quality prompts.
- Wikipedia's editorial field guide, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), supplied additional observed phrase, structure, and formatting patterns.
- [blader/humanizer](https://github.com/blader/humanizer) and [Pangram](https://www.pangram.com/) served as independent comparison points for coverage and failure modes. betterwords is not a fork of either project and does not optimize text for detector scores.

## License

MIT.

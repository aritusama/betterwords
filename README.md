# betterwords

![betterwords overview](assets/betterwords-overview.png)

betterwords is a rule set for production writing: articles, reports, reviews, release notes, specs, newsletters, scripts, slide text, and other durable text artifacts.

It ships as a self-contained Agent Skill for Codex, Claude, and Gemini/Antigravity. Portable Markdown files and platform adapters are included only for assistants that cannot install skills.

## What it does

- Preserves supplied facts, uncertainty, and attribution.
- Blocks unsupported claims, invented quotes, vague sourcing, and fake authority.
- Cuts common AI-like phrasing, filler scaffolding, inflated significance, and synonym cycling.
- Marks rules by severity so agents clear truth, hard-ban, density, default-avoid, and audit checks in order.
- Keeps format requirements intact for specs, slides, tables, release notes, and structured fields.
- Gives an agent a final self-check before it returns production text.

## When to use it

Use betterwords when you want to draft, rewrite, copyedit, or audit text that someone may reuse outside the chat.

Do not use it to hide authorship where disclosure is required. Do not use it to invent sources, mimic a private person, or make weak evidence sound stronger than it is.

## Repository structure

```text
betterwords/
  gemini-extension.json
  plugin.json
  .codex-plugin/
    plugin.json
  .claude-plugin/
    marketplace.json
    plugin.json
  .github/
    copilot-instructions.md
    workflows/
      validate.yml
  assets/
    betterwords-overview.png
  betterwords.md
  platforms/
    common-instructions.md
    chatgpt.md
    claude.md
    gemini.md
    github-copilot.md
    github-copilot/
      copilot-instructions.md
  skills/
    betterwords/
      SKILL.md
      references/
        betterwords.md
  LICENSE
  CHANGELOG.md
  README.md
```

## Install in Codex

Install the skill:

```sh
npx skills add aritusama/betterwords
```

After that, use it by asking for betterwords on a writing task:

```text
Use betterwords to copyedit this release note.
```

The Codex skill loads its own `SKILL.md` and `references/betterwords.md`. You do not need any platform-specific instructions in Codex.

If your installer asks for a path, use `skills/betterwords`.

## Install in Claude

Claude supports the same `skills/betterwords` skill directly.

For Claude Code, add this repository as a plugin marketplace and install the plugin:

```text
/plugin marketplace add aritusama/betterwords
/plugin install betterwords@betterwords
```

You can also copy the skill folder directly:

```sh
git clone https://github.com/aritusama/betterwords
mkdir -p ~/.claude/skills
cp -r betterwords/skills/betterwords ~/.claude/skills/
```

For a single repository, copy it into `.claude/skills/` instead:

```sh
mkdir -p .claude/skills
cp -r betterwords/skills/betterwords .claude/skills/
```

For claude.ai, Claude Desktop, or Cowork, zip the `skills/betterwords` folder and upload it under Customize > Skills.

See `platforms/claude.md` for details.

## Install in Gemini or Antigravity

Gemini CLI can load `betterwords` from `gemini-extension.json`; Google Antigravity plugin folders can load it from the root `plugin.json` and `skills/` directory.

Install it as an extension:

```sh
gemini extensions install https://github.com/aritusama/betterwords --consent
```

Or link a local checkout while editing:

```sh
git clone https://github.com/aritusama/betterwords
gemini extensions link betterwords
```

You can also install only the skill through Gemini CLI:

```sh
gemini skills install https://github.com/aritusama/betterwords --path skills/betterwords --scope user --consent
```

For the Gemini web app, use a Gem with `platforms/common-instructions.md` and `betterwords.md` as knowledge.

See `platforms/gemini.md` for details.

## Manual setup outside skill hosts

Use this section only for assistants that cannot install skills.

The portable rule file is `betterwords.md`.

Use the setup file for your assistant:

- ChatGPT: `platforms/chatgpt.md`
- Claude: `platforms/claude.md` for native skill support and fallback setup
- Gemini: `platforms/gemini.md` for native extension, skill, and Gem setup
- GitHub Copilot: `platforms/github-copilot.md`

The short instruction adapter is `platforms/common-instructions.md`. Use it in custom GPT instructions, Claude project instructions, Gemini Gem instructions, or Copilot personal instructions. Upload or attach `betterwords.md` as the knowledge file.

For the strongest setup, keep the adapter in saved instructions and keep `betterwords.md` attached as a file or knowledge source. For one-off chats, paste or attach both files in the same session.

## Use

Ask for betterwords when the output is a real text artifact:

```text
Use betterwords to copyedit this release note.
```

```text
Use betterwords to audit this draft for unsupported claims and AI-like phrasing.
```

```text
Use betterwords to rewrite this article intro without adding new facts.
```

## License

MIT.

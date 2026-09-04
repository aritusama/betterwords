# Gemini and Antigravity setup

Use this for Gemini CLI, Google Antigravity, and the Gemini web app.

## Gemini CLI or Antigravity extension

Install the repository as an extension:

```sh
gemini extensions install https://github.com/aritusama/betterwords
```

For local development, link a checkout instead:

```sh
git clone https://github.com/aritusama/betterwords
gemini extensions link betterwords
```

Gemini CLI reads `gemini-extension.json`; Antigravity plugin folders read `plugin.json`. The repository also keeps `skills/betterwords` installable as a standalone skill.

## Gemini CLI skill only

Install only the betterwords skill:

```sh
gemini skills install https://github.com/aritusama/betterwords --path skills/betterwords --scope user
```

Use `--scope workspace` instead of `--scope user` when the skill should apply only to the current project.

For local development, link the skill folder:

```sh
git clone https://github.com/aritusama/betterwords
gemini skills link betterwords/skills/betterwords --scope workspace
```

Use `--consent` only for a non-interactive installation where skipping the security confirmation is intentional.

## Manual plugin folder

If you manage Antigravity plugin folders directly, clone this repository under the global plugins directory:

```sh
git clone https://github.com/aritusama/betterwords ~/.gemini/config/plugins/betterwords
```

Antigravity can discover the root `plugin.json` from that folder.

## Gemini web app fallback: Gem

Use this for the web-based Gemini app where native skills or extensions are unavailable.

1. Create a new Gem in Gemini.
2. Put the contents of `.github/platforms/common-instructions.md` in the Gem instructions.
3. Add `betterwords.md` under the Gem knowledge files.
4. Preview the Gem with a real editing prompt before using or sharing it.

## One-off web setup

Attach or paste `betterwords.md`, then paste the contents of `.github/platforms/common-instructions.md`, then provide the draft or writing task.

The complete rule file must be read before writing or editing. If file access returns only excerpts, provide the entire file in the active conversation, using labeled consecutive parts if needed. Resolve missing portions before starting the artifact; selected rules or a summary cannot replace the complete file.

## Official docs checked

- Gemini CLI extensions: `gemini extensions --help`
- Gemini CLI skills: `gemini skills --help`
- Google Antigravity skills: https://antigravity.google/docs/skills
- Google Antigravity plugins: https://antigravity.google/docs/plugins
- Gemini Gems: https://support.google.com/gemini/answer/15146780
- Gem instruction tips: https://support.google.com/gemini/answer/15235603

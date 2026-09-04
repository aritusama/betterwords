# Claude setup

Claude supports Agent Skills natively. The skill in `skills/betterwords` works as-is.

## Claude Code plugin

Add this repository as a plugin marketplace:

```text
/plugin marketplace add aritusama/betterwords
/plugin install betterwords@betterwords
```

Claude Code namespaces plugin skills, so direct invocation is:

```text
/betterwords:betterwords
```

Claude can also invoke the skill automatically for production writing tasks.

## Claude Code standalone skill

Install as a personal skill across projects:

```sh
git clone https://github.com/aritusama/betterwords
mkdir -p ~/.claude/skills
cp -r betterwords/skills/betterwords ~/.claude/skills/
```

Install as a project skill for one repository:

```sh
mkdir -p .claude/skills
cp -r betterwords/skills/betterwords .claude/skills/
```

Standalone skills use the direct command:

```text
/betterwords
```

## Claude.ai, Claude Desktop, and Cowork

Zip the `skills/betterwords` folder and upload it under Customize > Skills. Then ask for betterwords by name.

The zip should contain the `betterwords/` skill folder as its root.

## Fallback: Claude Project without skill support

Use this only where custom skills are unavailable.

1. Create a Claude Project.
2. Upload `betterwords.md` to the project knowledge base.
3. Put the contents of `.github/platforms/common-instructions.md` in project instructions.
4. Start chats inside that project when you want betterwords to apply.

For one-off chats, attach or paste `betterwords.md`, then paste the contents of `.github/platforms/common-instructions.md`, then provide the draft or writing task.

The complete rule file must be read before writing or editing. If file access returns only excerpts, provide the entire file in the active conversation, using labeled consecutive parts if needed. Resolve missing portions before starting the artifact; selected rules or a summary cannot replace the complete file.

## Official docs checked

- Claude Code skills: https://code.claude.com/docs/en/skills
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Claude Code plugin marketplaces: https://code.claude.com/docs/en/plugin-marketplaces
- Claude custom skills upload: https://support.claude.com/en/articles/12512180-use-skills-in-claude

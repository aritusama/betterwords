# ChatGPT setup

Use this for ChatGPT outside Codex.

## Best setup: custom GPT

1. Create a GPT in ChatGPT.
2. Put the contents of `.github/platforms/common-instructions.md` in the GPT instructions.
3. Upload `betterwords.md` as knowledge.
4. Add conversation starters such as:
   - `Copyedit this draft using betterwords.`
   - `Audit this text for unsupported claims, stock phrasing, mechanical structure, and source drift.`
   - `Rewrite this intro without adding new facts.`
5. Test the GPT in preview with a real draft before sharing it.

If the GPT does not consistently apply the rules, paste the most relevant `betterwords.md` sections into the GPT instructions. Uploaded knowledge is useful context, but behavior rules are strongest when they are in instructions.

## Private recurring setup: ChatGPT Project

1. Create a ChatGPT Project.
2. Add `betterwords.md` as a project file or source.
3. Add the contents of `.github/platforms/common-instructions.md` as project instructions.
4. Use the project only for writing and editing work where betterwords should apply.

## One-off setup

Paste the contents of `.github/platforms/common-instructions.md`, then attach or paste `betterwords.md`, then provide the draft or writing task.

## Official docs checked

- ChatGPT Projects: https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt
- Creating GPTs: https://help.openai.com/en/articles/8554397-creating-a-gpt

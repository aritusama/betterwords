"""Validate package integrity. Editorial quality and model behavior require review."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[2]
VERSION = "2.1.6"
# One severity per existing rule, in section/item order. No wording assertions.
RULE_SEVERITIES = {
    1: "NNNNNNC", 2: "HHHHHHHHH", 3: "AAAAAAAAADDDDDD", 4: "AAAAAAAH",
    5: "CCCCCCCCCCCC", 6: "CCHCHHHCACCC", 7: "CCCNC", 8: "HCCC",
}
REQUIRED = (
    "README.md", ".github/CHANGELOG.md", "LICENSE", "betterwords.md",
    "gemini-extension.json", "plugin.json", ".agents/plugins/marketplace.json",
    ".codex-plugin/plugin.json", ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json", ".github/platforms/common-instructions.md",
    ".github/platforms/chatgpt.md", ".github/platforms/claude.md",
    ".github/platforms/gemini.md", ".github/platforms/github-copilot.md",
    ".github/platforms/github-copilot/copilot-instructions.md",
    ".github/assets/betterwords-2.0.0.png", "skills/betterwords/SKILL.md",
    "skills/betterwords/agents/openai.yaml", ".github/evals/cases.md",
    "skills/betterwords/references/betterwords.md",
    "skills/betterwords/references/editorial-examples.md",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def local_path(root: Path, value: str, owner: str) -> Path:
    require(isinstance(value, str) and bool(value), f"Missing local path in {owner}")
    require(not urlsplit(value).scheme, f"Expected local path in {owner}: {value}")
    target = (root / value).resolve()
    require(target.is_relative_to(root.resolve()), f"Path escapes package in {owner}: {value}")
    require(target.exists(), f"Missing local path in {owner}: {value}")
    return target


def validate(root: Path = ROOT) -> None:
    root = root.resolve()
    for relative in REQUIRED:
        require((root / relative).is_file(), f"Missing required file: {relative}")

    core = (root / "betterwords.md").read_bytes()
    require(core == (root / "skills/betterwords/references/betterwords.md").read_bytes(),
            "Canonical rule copies differ")
    rules = core.decode("utf-8")
    require(re.search(rf"^Version {re.escape(VERSION)}\. Last updated \d{{4}}-\d{{2}}-\d{{2}}\.",
                      rules, re.MULTILINE) is not None, "Canonical rule version is wrong")
    expected = [(f"{section}.{item}", severity) for section, severities in RULE_SEVERITIES.items()
                for item, severity in enumerate(severities, 1)]
    actual = re.findall(r"^(\d+\.\d+)\. \[([^\]]+)\] (\S.*)$", rules, re.MULTILINE)
    require([(rule_id, severity) for rule_id, severity, _ in actual] == expected,
            "Rule inventory, order, or severity differs from the approved inventory")
    require(len(re.findall(r"^\d+\.\d+\.", rules, re.MULTILINE)) == len(expected),
            "Malformed or duplicate numbered rule")
    require(rules.count("## Final self-check") == 1, "Missing or duplicate final self-check")
    checks = re.findall(r"^(\d+)\. (.+)$", rules.split("## Final self-check", 1)[1], re.MULTILINE)
    require([int(n) for n, _ in checks] == list(range(1, 10)), "Invalid self-check inventory")
    require([text[:3] for _, text in checks[:8]] == ["[N]", "[H]", "[D]", "[A]"] + ["[C]"] * 4,
            "Invalid self-check severity order")

    for relative in ("gemini-extension.json", "plugin.json", ".codex-plugin/plugin.json",
                     ".claude-plugin/plugin.json"):
        document = json.loads((root / relative).read_text(encoding="utf-8"))
        require(document.get("name") == "betterwords", f"Wrong name in {relative}")
        require(document.get("version") == VERSION, f"Wrong version in {relative}")
        if relative != "gemini-extension.json":
            skills = local_path(root, document.get("skills"), relative)
            require((skills / "betterwords/SKILL.md").is_file(), f"No Betterwords skill in {relative}")
        if "contextFileName" in document:
            local_path(root, document["contextFileName"], relative)

    for relative in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
        document = json.loads((root / relative).read_text(encoding="utf-8"))
        require(len(document.get("plugins", [])) == 1, f"Expected one plugin in {relative}")
        plugin = document["plugins"][0]
        require(plugin.get("name") == "betterwords", f"Wrong plugin in {relative}")
        source = plugin.get("source")
        if isinstance(source, dict):
            require(source.get("source") == "local", f"Expected local source in {relative}")
            source = source.get("path")
        require(local_path(root, source, relative) == root, f"Marketplace must load repo root: {relative}")

    skill = (root / "skills/betterwords/SKILL.md").read_text(encoding="utf-8")
    require(skill.startswith("---\n") and "\n---\n" in skill[4:], "Invalid skill frontmatter")
    frontmatter = skill.split("---", 2)[1]
    require(re.search(r"^name: betterwords$", frontmatter, re.MULTILINE) is not None, "Invalid skill name")
    require(re.search(r"^description: \S.+$", frontmatter, re.MULTILINE) is not None, "Missing skill description")

    cases = (root / ".github/evals/cases.md").read_text(encoding="utf-8")
    chunks = re.split(r"^## Case (\d+):[^\n]*\n", cases, flags=re.MULTILINE)
    require([int(n) for n in chunks[1::2]] == list(range(1, 43)), "Expected cases 1 through 42")
    fields = ("User request", "Input artifact and sources", "Expected mode", "Required invariants",
              "Prohibited changes", "Pass/fail rubric")
    for number, body in zip(chunks[1::2], chunks[2::2]):
        for field in fields:
            require(len(re.findall(rf"^- {re.escape(field)}: \S", body, re.MULTILINE)) == 1,
                    f"Case {number} needs exactly one nonempty {field} field")

    for markdown in root.rglob("*.md"):
        if ".git" in markdown.relative_to(root).parts:
            continue
        for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", markdown.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if not target or parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (markdown.parent / unquote(parsed.path)).resolve()
            require(resolved.is_relative_to(root) and resolved.exists(),
                    f"Broken local link in {markdown.relative_to(root)}: {target}")


if __name__ == "__main__":
    try:
        validate()
    except (ValueError, OSError, KeyError, TypeError) as error:
        raise SystemExit(str(error)) from error
    print("betterwords package validation passed (editorial behavior not evaluated)")

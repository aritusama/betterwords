from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VERSION = "2.0.0"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


required = [
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "betterwords.md",
    "gemini-extension.json",
    "plugin.json",
    ".agents/plugins/marketplace.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    ".github/platforms/common-instructions.md",
    ".github/platforms/chatgpt.md",
    ".github/platforms/claude.md",
    ".github/platforms/gemini.md",
    ".github/platforms/github-copilot.md",
    ".github/assets/betterwords-2.0.0.png",
    "skills/betterwords/SKILL.md",
    "skills/betterwords/agents/openai.yaml",
    ".github/evals/cases.md",
    "skills/betterwords/references/betterwords.md",
]
for relative in required:
    require((ROOT / relative).is_file(), f"Missing required file: {relative}")

json_files = [
    "gemini-extension.json",
    "plugin.json",
    ".agents/plugins/marketplace.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
]
documents = {
    relative: json.loads((ROOT / relative).read_text(encoding="utf-8"))
    for relative in json_files
}

versioned = [
    "gemini-extension.json",
    "plugin.json",
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
]
for relative in versioned:
    require(documents[relative].get("version") == VERSION, f"Wrong version in {relative}")

core = (ROOT / "betterwords.md").read_bytes()
packaged = (ROOT / "skills/betterwords/references/betterwords.md").read_bytes()
require(core == packaged, "Canonical rule copies differ")

rules = core.decode("utf-8")
require(f"Version {VERSION}." in rules, "Canonical rule version is wrong")
for marker in ("**", "<u>", "</u>", "[removed:"):
    require(marker not in rules, f"Review-only markup remains: {marker}")
for phrase in ("machine tell", "AI tell", "human marker", "real authorship", "detection tools"):
    require(phrase.casefold() not in rules.casefold(), f"Authorship rationale remains: {phrase}")
for fixture in (
    'Attribute every sourced quotation with enough detail for the intended reader to identify and verify its specific source',
    '"not only X, but also Y,"',
    'reversed ("It is X, not just Y") or split ("It may seem like X. But really it is Y.") variants',
    '2.6. [H] Do not use "from X to Y" when the endpoints do not form a real scale.',
    '2.7. [H] Do not use the ritual "Despite [positives], [subject] faces challenges...',
    '3.1. [A] Avoid em dashes. Use commas, parentheses, colons, or semicolons. Use en dashes only for numeric ranges.',
    'Match the characters to wherever the text will be published, and keep them consistent.',
    '3.6. [A] Avoid nonliteral use of "honest," "magic," "mechanics," and "unlock."',
    '3.9. [A] Avoid copula avoidance.',
    'Treat the list as one family: each occurrence of any listed term adds to the cluster, even when no word repeats.',
    '3.11. [D] Watch for triads and rhythmic formulas',
    '3.12. [D] Watch for repeated comma-tail sentences',
    '4.6. [A] Turn nominalizations back into verbs.',
    '4.7. [A] Avoid jargon, acronyms, foreign phrases, and technical terms',
    'Do not let familiar phrases generate the thought.',
    '5.4. [C] In summaries and recaps, keep tense consistent unless the timeline changes.',
    'do not default to the median either.',
    'Each paragraph should advance the argument, not restate or redefine it.',
    '5.9. [C] In change-driven documentation, write from the diff.',
    '5.10. [C] Every sentence should add information, evidence, qualification, or necessary movement.',
    '6.1. [C] Match the artifact.',
    '6.2. [C] When an author sample or baseline is supplied',
    'generic copywriting scene-setters',
    '7.1. [C] Write as a competent native writer of the requested language and locale',
    '7.2. [C] Preserve a supplied non-native, dialectal, regional, or mixed-language voice',
    'Translate quotations faithfully and idiomatically, for sense rather than word-for-word form',
    '7.5. [C] Use established target-language terminology and target-locale conventions.',
    '8.1. [H] Do not treat rewriting as detector evasion.',
    '9. End when done.',
):
    require(fixture in rules, f"Missing approved fixture: {fixture}")

final_check = rules.split("## Final self-check", 1)[1]
checks = {
    int(number): text
    for number, text in re.findall(r"^(\d+)\. (.+)$", final_check, re.MULTILINE)
}
require(set(checks) == set(range(1, 10)), "Final self-check must contain items 1 through 9")
for item in range(1, 9):
    require(checks[item].startswith(("[N]", "[H]", "[D]", "[A]", "[C]")), f"Self-check {item} needs a severity label")
require(checks[9] == "End when done.", "End when done must be the final unlabeled self-check")
hard_check = checks[2]
default_check = checks[4]
require("dangling modifier" in hard_check, "Dangling modifiers must be checked at [H]")
require("generic headings" not in default_check, "Generic headings must not remain in the [A] pass")
for word in ("honest", "magic", "mechanics", "unlock"):
    require(word not in default_check.casefold(), f"Final [A] pass repeats 3.6 word: {word}")

inflated_rule = re.search(r"^2\.4\..*$", rules, re.MULTILINE).group(0)
require('"stands as"' not in inflated_rule, "Bare copula avoidance belongs to 3.9, not 2.4")
copula_rule = re.search(r"^3\.9\..*$", rules, re.MULTILINE).group(0)
require('"stands as' in copula_rule, "Copula-avoidance examples must remain in 3.9")
require('"functions as' in copula_rule, "functions as must remain in 3.9")
require('"offers' in copula_rule, "offers must remain in 3.9")
nonliteral_rule = re.search(r"^3\.6\..*$", rules, re.MULTILINE).group(0).casefold()
for word in ("honest", "magic", "mechanics", "unlock"):
    require(word in nonliteral_rule, f"Missing nonliteral-use word in 3.6: {word}")

vocabulary_rule = re.search(r"^3\.10\..*$", rules, re.MULTILINE).group(0).casefold()
vocabulary_terms = (
    "additionally", "align with", "boast", "captivate", "comprehensive", "crucial",
    "cutting-edge", "delve", "dynamic", "elevate", "emphasize", "encompass", "enduring",
    "enhance", "ensure", "exemplify", "foster", "garner", "groundbreaking", "highlight",
    "in-depth", "innovative", "insightful", "interplay", "intricate", "key as adjective",
    "landscape", "leverage", "meticulous", "multifaceted", "navigate figuratively", "nestled",
    "notable", "nuanced", "pivotal", "plethora", "profound", "realm", "renowned", "robust",
    "seamless", "shed light on", "showcase", "spearhead", "tapestry", "testament",
    "transformative", "underscore", "unique", "valuable", "vibrant",
)
for term in vocabulary_terms:
    require(term in vocabulary_rule, f"Missing AI-polish vocabulary term in 3.10: {term}")

numbered: dict[int, list[int]] = {}
for section, item, severity in re.findall(r"^(\d+)\.(\d+)\. \[([NHADC])\]", rules, re.MULTILINE):
    numbered.setdefault(int(section), []).append(int(item))
require(set(numbered) == set(range(1, 9)), "Rule sections must run from 1 through 8")
for section, items in numbered.items():
    require(items == list(range(1, max(items) + 1)), f"Incomplete numbering in section {section}")

skill = (ROOT / "skills/betterwords/SKILL.md").read_text(encoding="utf-8")
require(skill.startswith("---\nname: betterwords\n"), "Invalid SKILL.md frontmatter")
frontmatter = skill.split("---", 2)[1]
require("ordinary conversational replies" in frontmatter, "Skill trigger lacks its chat exclusion")
require("ghostwriter" not in frontmatter.casefold(), "Skill trigger mentions a private system")
for heading in ("## Draft or rewrite", "## Copyedit or line edit", "## Audit", "## Verification boundary"):
    require(heading in skill, f"Missing skill contract section: {heading}")

metadata = (ROOT / "skills/betterwords/agents/openai.yaml").read_text(encoding="utf-8")
for field in ("display_name:", "short_description:", "default_prompt:", "allow_implicit_invocation: true"):
    require(field in metadata, f"Missing openai.yaml field: {field}")
require("icon_" not in metadata, "openai.yaml references an unvalidated icon")

marketplace = documents[".agents/plugins/marketplace.json"]
require(marketplace["plugins"][0]["source"]["path"] == "./", "Marketplace must load the repo root")
require("screenshots" not in documents[".codex-plugin/plugin.json"]["interface"], "Empty screenshots field remains")

evals = (ROOT / ".github/evals/cases.md").read_text(encoding="utf-8")
require(len(re.findall(r"^## Case \d+:", evals, re.MULTILINE)) == 19, "Expected 19 behavioral cases")
for field in (
    "User request:",
    "Input artifact and sources:",
    "Expected mode:",
    "Required invariants:",
    "Prohibited changes:",
    "Pass/fail rubric:",
):
    require(evals.count(field) == 19, f"Every evaluation needs {field}")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
for source in ("AP Stylebook", "Chicago Manual of Style"):
    require(source.casefold() not in rules.casefold(), f"Core rules mention optional authority: {source}")
    require(source.casefold() not in readme.casefold(), f"README mentions optional authority: {source}")

link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
for markdown in ROOT.rglob("*.md"):
    text = markdown.read_text(encoding="utf-8")
    for target in link_pattern.findall(text):
        path = target.split("#", 1)[0].strip()
        if not path or re.match(r"^[a-z]+://", path, re.IGNORECASE) or path.startswith("mailto:"):
            continue
        require((markdown.parent / path).resolve().exists(), f"Broken local link in {markdown.relative_to(ROOT)}: {target}")

require(not (ROOT / "assets").exists(), "Move root assets under .github")
require(not (ROOT / "platforms").exists(), "Move root platform notes under .github")

print("betterwords package validation passed")

"""Mutate real package inputs; editorial wording is outside these tests."""

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate import REQUIRED, ROOT, validate


class PackageIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="betterwords-package-")
        self.root = Path(self.temporary.name).resolve()
        assert self.root.is_relative_to(Path(tempfile.gettempdir()).resolve())
        self.addCleanup(self.temporary.cleanup)
        for relative in REQUIRED:
            destination = self.root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, destination)

    def change_rules(self, transform):
        text = transform((self.root / "betterwords.md").read_text(encoding="utf-8"))
        for relative in ("betterwords.md", "skills/betterwords/references/betterwords.md"):
            (self.root / relative).write_text(text, encoding="utf-8", newline="\n")

    def test_real_package_passes(self):
        validate(self.root)

    def test_missing_last_rule_in_section_fails(self):
        self.change_rules(lambda text: "\n".join(line for line in text.split("\n")
                                                if not line.startswith("1.7.")))
        with self.assertRaisesRegex(ValueError, "Rule inventory"):
            validate(self.root)

    def test_truth_rule_downgrade_fails(self):
        self.change_rules(lambda text: text.replace("1.2. [N]", "1.2. [C]", 1))
        with self.assertRaisesRegex(ValueError, "Rule inventory"):
            validate(self.root)

    def test_duplicate_rule_fails(self):
        self.change_rules(lambda text: text.replace("1.7. [C]", "1.6. [C]", 1))
        with self.assertRaisesRegex(ValueError, "Rule inventory"):
            validate(self.root)

    def test_missing_declared_skill_directory_fails(self):
        manifest = self.root / ".codex-plugin/plugin.json"
        document = json.loads(manifest.read_text(encoding="utf-8"))
        document["skills"] = "./missing-skills/"
        manifest.write_text(json.dumps(document), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Missing local path"):
            validate(self.root)

    def test_external_package_path_fails(self):
        manifest = self.root / "plugin.json"
        document = json.loads(manifest.read_text(encoding="utf-8"))
        document["skills"] = "../"
        manifest.write_text(json.dumps(document), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Path escapes"):
            validate(self.root)

    def test_stale_packaged_rules_fail(self):
        (self.root / "skills/betterwords/references/betterwords.md").write_text("stale", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "copies differ"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()

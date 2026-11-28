import json
import shutil
import tempfile
import unittest
from pathlib import Path

from check import capture, validate


class Checks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name) / "base"
        self.candidate = Path(self.temp.name) / "candidate"
        shutil.copytree(Path(__file__).parent / "baseline", self.base)
        shutil.copytree(self.base, self.candidate)
        self.write("context.json", {"proposal_id": "PROP-042", "policy_version": 1,
                                    "sources": capture(self.base)})

    def write(self, name, value, root=None):
        ((root or self.candidate) / name).write_text(json.dumps(value, indent=2) + "\n")

    def edit(self, name, key, value, root=None):
        target = (root or self.candidate) / name
        data = json.loads(target.read_text())
        data[key] = value
        self.write(name, data, root)

    def change(self):
        self.edit("requirement.json", "retention_days", 30)
        self.edit("requirement.json", "revision", 2)
        self.edit("config.json", "retention_days", 30)
        self.edit("proposal.json", "to_days", 30)
        (self.candidate / "runbook.md").write_text("Retention days: 30\nSynthetic exports only.\n")

    def test_baseline(self):
        self.assertTrue(validate(self.candidate, self.base).startswith("PASS"))

    def test_change(self):
        self.change()
        self.assertTrue(validate(self.candidate, self.base).startswith("PASS"))

    def test_stale_source(self):
        self.edit("requirement.json", "revision", 2, self.base)
        with self.assertRaisesRegex(ValueError, "STALE_CONTEXT"):
            validate(self.candidate, self.base)

    def test_policy_drift(self):
        self.edit("context.json", "policy_version", 0)
        with self.assertRaisesRegex(ValueError, "POLICY_DRIFT"):
            validate(self.candidate, self.base)

    def test_config_conflict(self):
        self.edit("config.json", "retention_days", 30)
        with self.assertRaisesRegex(ValueError, "IMPLEMENTATION_CONFLICT"):
            validate(self.candidate, self.base)

    def test_runbook_conflict(self):
        (self.candidate / "runbook.md").write_text("Retention days: 30\n")
        with self.assertRaisesRegex(ValueError, "RUNBOOK_CONFLICT"):
            validate(self.candidate, self.base)

    def test_stale_proposal(self):
        self.edit("proposal.json", "base_revision", 0)
        with self.assertRaisesRegex(ValueError, "STALE_PROPOSAL"):
            validate(self.candidate, self.base)

    def test_bad_revision(self):
        self.change()
        self.edit("requirement.json", "revision", 3)
        with self.assertRaisesRegex(ValueError, "INVALID_REVISION"):
            validate(self.candidate, self.base)

    def test_wrong_proposal(self):
        self.edit("context.json", "proposal_id", "PROP-OTHER")
        with self.assertRaisesRegex(ValueError, "PROPOSAL_MISMATCH"):
            validate(self.candidate, self.base)

    def test_invalid_retention(self):
        self.edit("requirement.json", "retention_days", True)
        with self.assertRaisesRegex(ValueError, "INVALID_RETENTION"):
            validate(self.candidate, self.base)


if __name__ == "__main__":
    unittest.main()
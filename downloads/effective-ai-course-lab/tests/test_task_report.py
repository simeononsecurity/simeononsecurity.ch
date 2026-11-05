"""Baseline checks for the course lab."""

import json
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

module_path.insert(0, str(Path(__file__).resolve().parents[1]))
from task_report import count_tasks  # noqa: E402


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        sample = Path(__file__).resolve().parents[1] / "tasks.json"
        self.assertEqual(count_tasks(sample), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)


if __name__ == "__main__":
    unittest.main()

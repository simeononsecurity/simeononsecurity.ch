---
title: "AI কর্মপ্রবাহের ক্যাপস্টোন: JSON প্রতিবেদন তৈরি ও যাচাই করুন"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "প্রকল্পের প্রেক্ষাপট, সীমাবদ্ধ এজেন্ট অনুরোধ, স্বাধীন পরীক্ষা, উৎস পর্যালোচনা এবং নতুন সেশনে হস্তান্তরসহ একটি JSON কাজের প্রতিবেদন তৈরি করুন।"
genre: ["কৃত্রিম বুদ্ধিমত্তা", "সফটওয়্যার প্রকৌশল", "শিক্ষা"]
tags: ["AI কর্মপ্রবাহের ক্যাপস্টোন", "কোডিং এজেন্ট প্রকল্প", "AI কাজ যাচাই", "AGENTS.md", "MCP অনুশীলন", "এজেন্ট হস্তান্তর"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "উৎস ফাইল, পরীক্ষার ফল, এজেন্ট পর্যালোচনা এবং হস্তান্তরের নথিসহ সম্পন্ন কর্মশালার সফটওয়্যার কাজ"
coverCaption: ""
---

[ব্যবহারিক AI কর্মপ্রবাহ কোর্সে ফিরুন](/effective-ai-course-start/)

**একটি নতুন আউটপুট ফরম্যাট তৈরি করে তার আচরণের প্রমাণ দিন।** আগে আপনি একটি স্ট্যাটাস ফিল্টার যোগ করেছিলেন। এই ক্যাপস্টোন নতুন ল্যাব থেকে শুরু হয় এবং অন্য একটি প্রোগ্রামের পড়ার জন্য JSON প্রতিবেদন যোগ করে। নতুন শর্তটি যাচাই করে আপনি ভিন্ন ফিচারে কর্মপ্রবাহ প্রয়োগ করতে পারেন কি না।

**শেখার লক্ষ্য:** আপনি যাচাইকৃত JSON প্রতিবেদন, উৎস ও টুলের প্রমাণের রেকর্ড এবং নতুন সেশনের বোধগম্য হস্তান্তর দেবেন।

## মূল বিষয়

- **আলাদা শর্ত** ক্যাপস্টোন ফিচার নির্ধারণ করে।
- **কোডিং এজেন্টের সম্পাদনা** নির্দিষ্ট ফাইলের মধ্যে থাকে।
- **স্বাধীন যাচাই** গ্রহণযোগ্যতা নির্ধারণ করে।
- **নতুন সেশনে হস্তান্তর** ফলাফল পুনর্গঠন করতে সাহায্য করে।

## শুরু করার আগে

**পূর্বশর্ত:** পাঠ ০ থেকে ১০ শেষ করুন। এর মধ্যে রিপোজিটরি প্রসঙ্গ, প্রথম কোডিং কাজ, MCP বা ব্রাউজার বিকল্প, দায়িত্ব বণ্টন এবং সীমিত চক্র রয়েছে। পাঠ ১১ ঐচ্ছিক। ৯০ থেকে ১২০ মিনিট রাখুন। কঠিনতার মাত্রা মাঝারি।

[শুরুর ল্যাব](/downloads/effective-ai-course-lab.zip)-এর **নতুন কপি আনজিপ করুন**। সম্পাদনার আগে `python3 task_report.py tasks.json` এবং দুটি ভিত্তিমূলক পরীক্ষা চালান। Windows-এ সেটআপে Python Launcher থাকলে `py -3` ব্যবহার করুন। কোর্স সেটআপের মতো স্থানীয় Git ভিত্তি তৈরি করুন। পাঠ ৫-এর স্ট্যাটাস ফিল্টারটি ইচ্ছাকৃতভাবে নেই।

**`docs/capstone-requirements.md`, revision 1 পড়ুন।** এতে `--format text|json` আবশ্যক। ডিফল্ট টেক্সট `Total tasks: 4`-ই থাকে। JSON আউটপুটে সংখ্যাসূচক মোট এবং ডেটার প্রতিটি স্ট্যাটাসের সংখ্যা থাকে। খালি তালিকা, অনুপস্থিত স্ট্যাটাস এবং অসমর্থিত ফরম্যাট যাচাই করুন। নতুন ফিচারের কর্তৃত্বপূর্ণ উৎস হিসেবে `docs/requirements.md` ব্যবহার করবেন না।

**আপনার পথ বেছে নিন।** সংযুক্ত পথে কোডিং এজেন্টের পর্যবেক্ষিত সম্পাদনা, সত্যিকারের read-only MCP কল এবং নেটিভ worker বা পৃথক worker সেশন থাকে। অধ্যয়ন পথে কোড প্রস্তাবের জন্য চ্যাট সহকারী, MCP-এর বদলে ব্রাউজার উৎস এবং সিমুলেটেড worker হিসেবে পৃথক চ্যাট থাকে। অনুপলব্ধ টুল ধাপ “চালানো হয়নি” হিসেবে চিহ্নিত করুন। উভয় পথেই স্থানীয় পরীক্ষা ও ফাইল পর্যালোচনা দরকার। নিচের উত্তরসূচিতে পুনরুদ্ধারের জন্য সম্পূর্ণ ফাইল রয়েছে। প্রথম প্রচেষ্টা নোটে রাখুন, তারপর নতুন কপিতে উত্তরসূচি নিন।

## ধাপ ১: প্রকল্পের সংক্ষিপ্ত বিবরণ

**সিন্থেটিক ChatGPT বা Claude কর্মশালা প্রকল্প খুলুন।** দুই বাক্যের স্মরণবার্তার খসড়া চান। `approved-schedule.md`-এ সন্ধ্যা ৭টার সঙ্গে সময় মেলান। সময়সূচি স্মরণবার্তা নির্ধারণ করে। ক্যাপস্টোনের শর্ত প্রোগ্রাম নির্ধারণ করে।

**প্রমাণ:** প্রকল্পের নাম, উৎসের revision, খসড়ায় দেখা সময় এবং সংশোধন নথিভুক্ত করুন। বার্তা পাঠাবেন না।

## ধাপ ২: রিপোজিটরি প্রসঙ্গ

**নতুন ল্যাব খুলুন।** সংক্ষিপ্ত `AGENTS.md` তৈরি করুন, যেখানে `docs/capstone-requirements.md`, `task_report.py`, পরীক্ষা এবং সেটআপে প্রমাণিত পরীক্ষার কমান্ডের উল্লেখ থাকবে। Claude Code ব্যবহার করলে `CLAUDE.md` থেকে শেয়ার করা ফাইল আমদানি করুন। নির্দেশনা ফাইলগুলোর জন্য মানব-নির্মিত setup commit করুন, তারপর নিশ্চিত করুন `git status --short` ফাঁকা। কোডিং এজেন্ট ফিচার সম্পাদনা commit করবে না।

**প্রমাণ:** মানচিত্র ও পরিষ্কার নির্দেশনার কপি রাখুন। revision 1-এর JSON key এবং অবৈধ ইনপুটের আচরণ লিখুন। আগের কোনো চ্যাটে স্ট্যাটাস ফিল্টারের উল্লেখ থাকলে সেটিকে অন্য কাজের পটভূমি ধরুন।

## ধাপ ৩: বাহ্যিক উৎস

**সংযুক্ত পথ:** সমর্থিত ক্লায়েন্টে [read-only OpenAI Docs MCP সার্ভার](https://learn.chatgpt.com/learn/docs-mcp) ব্যবহার করুন। MCP টুলকে `AGENTS.md`-এর বর্তমান নির্দেশনা জিজ্ঞাসা করুন। টুলের নাম, উৎস URL এবং ল্যাবের জন্য প্রাসঙ্গিক একটি বিষয় লিখুন। এরপর অনুশীলনের সংযোগ সরিয়ে ফেলুন।

**অধ্যয়ন পথ:** ব্রাউজারে [`AGENTS.md`-এর সরকারি নথি](https://learn.chatgpt.com/docs/agent-configuration/agents-md) খুলুন। শিরোনাম, URL এবং প্রাসঙ্গিক একটি বিষয় লিখুন। MCP খোঁজা ও চালানো “চালানো হয়নি” চিহ্নিত করুন।

**প্রমাণ:** সার্ভারের কনফিগার করা এন্ট্রি ব্যবহার প্রমাণ করে না। সংযুক্ত পথে দৃশ্যমান টুল কল এবং ফেরত আসা উৎসের বিষয়বস্তু দরকার।

## ধাপ ৪: একটি পর্যালোচনা অর্পণ

**শুধু-পঠন worker-কে** `docs/capstone-requirements.md`, `task_report.py` এবং ভিত্তিমূলক পরীক্ষা পর্যালোচনা করতে বলুন। অনুপস্থিত যাচাই ও ফাইল-পাথসহ সর্বোচ্চ পাঁচ লাইনের প্রতিবেদন চান। অধ্যয়ন পথে আলাদা চ্যাট নিন ও সিমুলেটেড worker হিসেবে চিহ্নিত করুন।

**প্রত্যাশিত ফল:** শুরুর পরীক্ষাগুলো মোট এবং তালিকা নয় এমন JSON মান পরীক্ষা করে। JSON আউটপুট, খালি তালিকা, অনুপস্থিত স্ট্যাটাস বা অবৈধ ফরম্যাট পরীক্ষা করে না। প্রতিবেদন যাচাই করতে নিজে পরীক্ষার ফাইল খুলুন। পাঠ ৫-এর গ্রহণযোগ্যতার মানদণ্ড আলাদা বলে সংক্ষিপ্ত স্বাধীন পর্যালোচনা কাজে লাগে।

**প্রমাণ:** সংক্ষিপ্ত প্রতিবেদন ও এক বাক্যের ইন্টিগ্রেশন সিদ্ধান্ত রাখুন। worker-এর কথোপকথন মূল কাজের নথি থেকে আলাদা রাখুন।

## ধাপ ৫: সম্পাদনার অনুরোধ

**কোডিং এজেন্টকে** নিচের প্যাকেট দিন। অধ্যয়ন পথে চ্যাট সহকারী patch প্রস্তাব করে, যা আপনি ল্যাবে হাতে প্রয়োগ করেন।

```text
লক্ষ্য: JSON পাথের পরে --format text|json যোগ করুন।
উৎস: docs/capstone-requirements.md, revision 1.
অনুমোদিত সম্পাদনা: task_report.py এবং tests/test_task_report.py.
রাখুন: ডিফল্ট Total tasks: 4 এবং tasks.json অপরিবর্তিত।
JSON: total ও by_status গণনা-সহ একটি অবজেক্ট, stdout-এ অতিরিক্ত টেক্সট নয়।
আবশ্যিক যাচাই: ডিফল্ট ও স্পষ্ট text, JSON 4/2/2, খালি তালিকা,
অনুপস্থিত স্ট্যাটাস, অবৈধ ফরম্যাট এবং ভিত্তিমূলক পরীক্ষা।
থামুন যদি: উৎসে দ্বন্দ্ব হয়, সম্পর্কহীন ভিত্তিমূলক পরীক্ষা ব্যর্থ হয় বা সীমার বাইরে সম্পাদনা হয়।
প্রতিবেদন: পরিবর্তিত ফাইল, কমান্ড, দেখা আউটপুট, অমীমাংসিত সমস্যা।
Commit, push, প্রকাশনা বা বার্তা পাঠাবেন না।
```

**সম্পাদনার আগে পরিকল্পনা দেখুন।** Schema-র সিদ্ধান্ত গুরুত্বপূর্ণ: `total` সংখ্যা, `"4"` স্ট্রিং নয়। `by_status` ইনপুটের প্রতিটি স্ট্যাটাস রাখে, তাই ভবিষ্যতের মানও প্রতিবেদনে আসে। পরিবর্তন আনজিপ করা ল্যাবে সীমাবদ্ধ রাখুন।

## ধাপ ৬: পরীক্ষা ও পর্যালোচনা

**এই যাচাইগুলো নিজে চালান।** Windows-এ `python3`-এর বদলে `py -3` দিন। JSON key-এর সঠিক ক্রম ও ফাঁকা স্থান গুরুত্বপূর্ণ নয়। আউটপুট JSON হিসেবে parse করুন এবং টাইপসহ মান তুলনা করুন।

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**প্রত্যাশিত আচরণ:** পরীক্ষা পাস করে। দুইটি text কমান্ড `Total tasks: 4` দেখায়। JSON কমান্ড `total` 4, `by_status.open` 2 এবং `by_status.done` 2-সহ এক অবজেক্ট ফেরায়। অবৈধ ফরম্যাট শূন্য নয় এমন কোডে শেষ হয়। পরীক্ষা খালি ইনপুট এবং string `status` ছাড়া কাজও ধরে। এসব ক্ষেত্রে দেখা ত্রুটি আউটপুট ও exit code পড়ুন।

| ধাপ | সফলতার প্রমাণ | ব্যর্থ হলে পুনরুদ্ধার |
|---|---|---|
| **প্রকল্পের বিবরণ** | স্মরণবার্তায় সন্ধ্যা ৭টা | সময়সূচির উৎস হালনাগাদ করুন |
| **রিপোজিটরি মানচিত্র** | শর্ত ও পরীক্ষার পাথের নাম আছে | নির্দেশনা ফাইল ঠিক করুন |
| **বাহ্যিক উৎস** | MCP পড়া হয়েছে বা ব্রাউজার বিকল্প নথিভুক্ত | সংযোগ বা URL যাচাই করুন |
| **Worker পর্যালোচনা** | বাদ পড়া পরীক্ষা ফাইলে নিশ্চিত | Worker প্রতিবেদন সংশোধন করুন |
| **ফাইলের সীমা** | শুধু প্রোগ্রাম ও পরীক্ষা | প্রতিটি অনাকাঙ্ক্ষিত পরিবর্তন দেখুন |
| **আচরণ** | text, JSON, খালি ও ত্রুটি যাচাই করা | একটি কারণ নির্ণয় করে আবার চেষ্টা করুন |
| **হস্তান্তর** | নতুন সেশন অবস্থা পুনর্গঠন করে | অনুপস্থিত উৎস বা ফল যোগ করুন |

**নিরাপদ রিসেটের জন্য নতুন কপি নিন।** নোট ল্যাবের বাইরে রাখুন, শুধু অস্থায়ী কপি মুছুন এবং মূল ZIP আবার খুলুন। সংরক্ষণযোগ্য কাজ থাকা রিপোজিটরিতে ব্যাপক Git reset করবেন না।

## ধাপ ৭: নতুন সেশনে হস্তান্তর

ল্যাব ফোল্ডারের বাইরে **১৮০ শব্দের কম একটি হস্তান্তর লিখুন।** শর্তের revision, পরিবর্তিত ফাইল, পরীক্ষার সঠিক কমান্ড ও ফল, text ও JSON আউটপুট, অবৈধ ইনপুট যাচাই, ব্যবহারের রেকর্ড এবং পরবর্তী কাজ লিখুন। নতুন সেশন খুলে JSON key ও ফিচার পাস করেছে কি না জিজ্ঞাসা করুন।

**প্রত্যাশিত উত্তর:** নতুন সেশন `total` ও `by_status` বলে, revision 1 উল্লেখ করে, শুধু দেখা যাচাই জানায় এবং বাদ পড়া যাচাই চিহ্নিত করে।

## উত্তরসূচি ও মূল্যায়ন

**একটি বৈধ বাস্তবায়ন** নিচে আছে। প্রথম ব্লক `task_report.py`, দ্বিতীয়টি `tests/test_task_report.py` নামে ল্যাবের নতুন কপিতে রাখুন। `tasks.json` ও দুইটি শর্তের ফাইল অপরিবর্তিত রাখুন। ধাপ ৬-এর যাচাই চালান। অন্য সমাধানকে শর্ত ও দেখা আচরণের সঙ্গে তুলনা করুন।

`task_report.py`:

```python
"""ওয়ার্কশপের কাজের টেক্সট গণনা বা JSON সারাংশ দেখায়।"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="ওয়ার্কশপ কাজের প্রতিবেদন")
    parser.add_argument("path", type=Path, help="JSON কাজের তালিকার পাথ")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""ওয়ার্কশপ কাজের text ও JSON প্রতিবেদনের যাচাই।"""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**উত্তরসূচি ব্যবহারের পর রিসেট করুন:** নোট ল্যাবের বাইরে রাখুন, এই কপি মুছুন এবং আসল স্টার্টার ল্যাব আবার আনজিপ করুন। নতুন কপিতে দুটি ভিত্তিমূলক পরীক্ষা থাকবে, কিন্তু ফিচারের বাস্তবায়ন থাকবে না।

**উপরের সারণির প্রতিটি ধাপে এক পয়েন্ট দিন।** বাহ্যিক উৎসের সারিতে বাস্তব MCP কল এবং worker সারিতে বাস্তব সেশন নথিভুক্ত হলে সাত পয়েন্টে সংযুক্ত পথ শেষ। উৎসটি যাচাইকৃত ব্রাউজার পৃষ্ঠা এবং টুল ধাপ স্পষ্টভাবে না-চালানো চিহ্নিত হলে সাত পয়েন্টে অধ্যয়ন পথ শেষ। আচরণ, উৎস বা ফাইল-সীমার পরীক্ষা অনুপস্থিত থাকলে দুই পথই অসম্পূর্ণ।

## বোঝাপড়া যাচাই

1. **কোন শর্ত এই ফিচার নিয়ন্ত্রণ করে?** `docs/capstone-requirements.md`, revision 1। আগের স্ট্যাটাস-ফিল্টার শর্তটি পাঠ 5-এর।
2. **JSON চুক্তির প্রমাণ কী?** কমান্ডের আউটপুট parse করুন, সংখ্যাসূচক মান ও প্রতিটি স্ট্যাটাসের সংখ্যা তুলনা করুন, এবং খালি ও অবৈধ ইনপুট পরীক্ষা করুন। পরিপাটি এজেন্ট সারাংশ যথেষ্ট নয়।

## সমস্যা সমাধান

- **সম্পাদনার আগে ভিত্তিমূলক পরীক্ষা ব্যর্থ:** ZIP থেকে ল্যাব পুনরুদ্ধার করে সেটআপ আবার চালান।
- **এজেন্ট অন্য ফাইল বদলায়:** diff দেখুন এবং শুধু অনাকাঙ্ক্ষিত ল্যাব পরিবর্তন ফিরিয়ে দিন।
- **MCP সংযোগ ব্যর্থ:** ব্রাউজার উৎস ব্যবহার করুন এবং ধাপটি অধ্যয়ন পথ হিসেবে চিহ্নিত করুন।
- **Worker ভুল মান পুনরাবৃত্তি করে:** ক্যাপস্টোন শর্ত আবার পড়ুন এবং প্রতিবেদন ঠিক করুন।
- **পুনঃচেষ্টার সীমা শেষ:** ত্রুটি লগ রাখুন এবং পরের পদক্ষেপের জন্য মানব পর্যালোচকের সাহায্য নিন।

## পরবর্তী পদক্ষেপ

**সম্পূর্ণ প্রমাণ রেকর্ড সংরক্ষণ করুন।** উন্নত দলীয় প্রকাশনা এবং একাধিক সিস্টেমে কর্তৃত্বের জন্য [AI সহযোগিতা বাস্তবায়ন কোর্স](/ai-collaboration-course-start/) চালিয়ে যান।

**কোর্স নেভিগেশন:** [আগের বাধ্যতামূলক পাঠ: সীমিত চক্র](/articles/effective-ai-bounded-agent-loops/), [ঐচ্ছিক: বিশেষায়িত এজেন্ট মূল্যায়ন](/articles/effective-ai-specialized-agent-evaluation/), [কোর্স রূপরেখা](/effective-ai-course-start/).

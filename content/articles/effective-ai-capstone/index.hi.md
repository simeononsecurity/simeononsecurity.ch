---
title: "AI कार्यप्रवाह कैपस्टोन: JSON रिपोर्ट बनाएँ और सत्यापित करें"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "प्रोजेक्ट संदर्भ, सीमित एजेंट अनुरोध, स्वतंत्र परीक्षण, स्रोत समीक्षा और नए सत्र को हस्तांतरण के साथ नई JSON कार्य रिपोर्ट बनाएँ।"
genre: ["कृत्रिम बुद्धिमत्ता", "सॉफ्टवेयर इंजीनियरिंग", "शिक्षा"]
tags: ["AI कार्यप्रवाह कैपस्टोन", "कोडिंग एजेंट प्रोजेक्ट", "AI कार्य सत्यापन", "AGENTS.md", "MCP अभ्यास", "एजेंट हस्तांतरण"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "स्रोत फ़ाइलों, परीक्षण नतीजों, एजेंट समीक्षा और हस्तांतरण रिकॉर्ड वाला पूरा किया गया कार्यशाला सॉफ्टवेयर कार्य"
coverCaption: ""
---

[व्यावहारिक AI कार्यप्रवाह पाठ्यक्रम पर लौटें](/effective-ai-course-start/)

**नया आउटपुट फ़ॉर्मेट बनाएँ और उसका व्यवहार प्रमाणित करें।** पहले आपने स्टेटस फ़िल्टर जोड़ा था। यह कैपस्टोन नई लैब से शुरू होता है और दूसरे प्रोग्राम के पढ़ने के लिए JSON रिपोर्ट जोड़ता है। नई आवश्यकता जाँचती है कि आप अपने कार्यप्रवाह को किसी दूसरे फ़ीचर पर लागू करते हैं।

**सीखने का परिणाम:** आप जाँची हुई JSON रिपोर्ट, स्रोतों और टूल के प्रमाण का रिकॉर्ड और नए सत्र को समझ आने वाला हस्तांतरण देंगे।

## मुख्य बातें

- **अलग आवश्यकता** कैपस्टोन फ़ीचर को नियंत्रित करती है।
- **कोडिंग एजेंट का बदलाव** नामित फ़ाइलों तक सीमित रहता है।
- **स्वतंत्र जाँचें** स्वीकृति तय करती हैं।
- **नए सत्र को हस्तांतरण** परिणाम को फिर से समझने देता है।

## शुरू करने से पहले

**पूर्वापेक्षाएँ:** पाठ 0 से 10 पूरे करें। इनमें रिपॉज़िटरी संदर्भ, पहला कोडिंग कार्य, MCP या उसका ब्राउज़र विकल्प, प्रतिनिधिकरण और सीमित लूप शामिल हैं। पाठ 11 वैकल्पिक है। 90 से 120 मिनट रखें। कठिनाई मध्यम है।

[स्टार्टर लैब](/downloads/effective-ai-course-lab.zip) की **नई प्रति निकालें**। संपादन से पहले `python3 task_report.py tasks.json` और दो आधारभूत परीक्षण चलाएँ। Windows पर `py -3` चलाएँ यदि सेटअप Python Launcher का उपयोग करता है। पाठ्यक्रम सेटअप की तरह स्थानीय Git आधार बनाएँ। पाठ 5 का स्टेटस फ़िल्टर जानबूझकर मौजूद नहीं है।

**`docs/capstone-requirements.md`, संशोधन 1 पढ़ें।** इसमें `--format text|json` आवश्यक है। डिफ़ॉल्ट टेक्स्ट `Total tasks: 4` ही रहता है। JSON आउटपुट में संख्यात्मक कुल और डेटा के हर स्टेटस की गिनती होती है। खाली सूची, छूटा हुआ स्टेटस और असमर्थित फ़ॉर्मेट जाँचें। इस नए फ़ीचर के लिए `docs/requirements.md` को आधिकारिक स्रोत न मानें।

**अपना ट्रैक चुनें।** कनेक्टेड ट्रैक में कोडिंग एजेंट का देखा गया संपादन, वास्तविक read-only MCP कॉल और native worker या अलग worker सत्र होता है। अध्ययन ट्रैक में चैट सहायक का कोड सुझाव, MCP की जगह ब्राउज़र स्रोत और नकली worker के रूप में अलग-अलग चैट होती हैं। अनुपलब्ध टूल चरणों को “नहीं चलाया” लिखें। दोनों ट्रैक में स्थानीय परीक्षण और फ़ाइल समीक्षा आवश्यक हैं। नीचे उत्तर कुंजी में पुनर्प्राप्ति के लिए पूरी फ़ाइलें हैं। पहली कोशिश नोट्स में सहेजें, फिर नई प्रति में उत्तर कुंजी कॉपी करें।

## जाँच 1: प्रोजेक्ट विवरण

**सिंथेटिक ChatGPT या Claude कार्यशाला प्रोजेक्ट खोलें।** दो वाक्यों का रिमाइंडर मसौदा माँगें। `approved-schedule.md` में शाम 7 बजे से उसका समय मिलाएँ। शेड्यूल रिमाइंडर तय करता है। कैपस्टोन आवश्यकता प्रोग्राम तय करती है।

**प्रमाण:** प्रोजेक्ट नाम, स्रोत संशोधन, मसौदे में देखा समय और सुधार दर्ज करें। संदेश न भेजें।

## जाँच 2: रिपॉज़िटरी संदर्भ

**नई लैब खोलें।** छोटा `AGENTS.md` बनाएँ जिसमें `docs/capstone-requirements.md`, `task_report.py`, परीक्षण और सेटअप में प्रमाणित परीक्षण कमांड के संदर्भ हों। Claude Code उपयोग करते हैं तो साझा फ़ाइल `CLAUDE.md` से आयात करें। निर्देश फ़ाइलों के लिए मानव द्वारा setup commit बनाएँ और पुष्टि करें कि `git status --short` खाली है। कोडिंग एजेंट फ़ीचर बदलाव commit नहीं करेगा।

**प्रमाण:** नक्शा और साफ़ निर्देश प्रति सहेजें। संशोधन 1 की JSON कुंजियाँ और अमान्य इनपुट व्यवहार लिखें। यदि पुरानी चैट स्टेटस फ़िल्टर बताती है, तो उसे अलग काम का संदर्भ मानें।

## जाँच 3: बाहरी स्रोत

**कनेक्टेड ट्रैक:** समर्थित क्लाइंट से [read-only OpenAI Docs MCP सर्वर](https://learn.chatgpt.com/learn/docs-mcp) उपयोग करें। MCP टूल से `AGENTS.md` के मौजूदा निर्देश माँगें। टूल नाम, स्रोत URL और लैब के लिए उपयोगी एक बात लिखें। फिर अभ्यास कनेक्शन हटाएँ।

**अध्ययन ट्रैक:** ब्राउज़र में [`AGENTS.md` का आधिकारिक दस्तावेज़](https://learn.chatgpt.com/docs/agent-configuration/agents-md) खोलें। शीर्षक, URL और एक उपयोगी बात लिखें। MCP खोज और निष्पादन को “नहीं चलाया” चिह्नित करें।

**प्रमाण:** कॉन्फ़िगर किया गया सर्वर प्रविष्टि उसके उपयोग का प्रमाण नहीं है। कनेक्टेड ट्रैक में दिखाई देने वाली टूल कॉल और लौटी हुई स्रोत सामग्री आवश्यक है।

## जाँच 4: एक समीक्षा सौंपें

**केवल-पढ़ने वाले worker से** `docs/capstone-requirements.md`, `task_report.py` और आधारभूत परीक्षणों की समीक्षा कराएँ। छूटी जाँचों और फ़ाइल पथों सहित अधिकतम पाँच पंक्तियों की रिपोर्ट माँगें। अध्ययन ट्रैक में अलग चैट लें और उसे नकली worker चिह्नित करें।

**अपेक्षित निष्कर्ष:** शुरुआती परीक्षण कुल और ऐसा JSON मान जाँचते हैं जो सूची नहीं है। वे JSON आउटपुट, खाली सूची, छूटा स्टेटस या अमान्य फ़ॉर्मेट नहीं जाँचते। रिपोर्ट की पुष्टि के लिए परीक्षण फ़ाइल स्वयं खोलें। स्वतंत्र छोटी समीक्षा उपयोगी है क्योंकि स्वीकृति मानदंड पाठ 5 से अलग हैं।

**प्रमाण:** छोटी रिपोर्ट और एक वाक्य का एकीकरण निर्णय सहेजें। Worker प्रतिलेख मुख्य कार्य रिकॉर्ड से बाहर रखें।

## जाँच 5: संपादन का अनुरोध

**कोडिंग एजेंट को** नीचे दिया पैकेट दें। अध्ययन ट्रैक में चैट सहायक पैच सुझाता है और आप उसे लैब में स्वयं लागू करते हैं।

```text
लक्ष्य: JSON पथ के बाद --format text|json जोड़ें।
स्रोत: docs/capstone-requirements.md, संशोधन 1।
अनुमत संपादन: task_report.py और tests/test_task_report.py।
बनाए रखें: डिफ़ॉल्ट Total tasks: 4 और अपरिवर्तित tasks.json।
JSON: total और by_status गणनाओं वाला एक ऑब्जेक्ट, stdout पर कोई अतिरिक्त पाठ नहीं।
आवश्यक जाँचें: डिफ़ॉल्ट और स्पष्ट text, JSON 4/2/2, खाली सूची,
छूटा स्टेटस, अमान्य फ़ॉर्मेट और आधारभूत परीक्षण।
रुकें यदि: स्रोत में विरोध हो, असंबंधित आधारभूत परीक्षण विफल हो या दायरे से बाहर संपादन हो।
रिपोर्ट: बदली फ़ाइलें, कमांड, देखे गए आउटपुट, अनसुलझी समस्या।
Commit, push, प्रकाशन या संदेश न भेजें।
```

**संपादन से पहले योजना जाँचें।** स्कीमा चयन महत्वपूर्ण है: `total` संख्या है, `"4"` स्ट्रिंग नहीं। `by_status` इनपुट में मौजूद हर स्टेटस रखता है, ताकि भविष्य के मान भी रिपोर्ट हों। बदलाव निकाली गई लैब तक सीमित रखें।

## जाँच 6: परीक्षण और समीक्षा

**ये जाँचें स्वयं चलाएँ।** Windows पर `python3` की जगह `py -3` चलाएँ। JSON कुंजियों का सटीक क्रम और रिक्त स्थान मायने नहीं रखते। आउटपुट को JSON मानकर पढ़ें और टाइप किए गए मानों की तुलना करें।

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**अपेक्षित व्यवहार:** परीक्षण सफल होते हैं। दोनों text कमांड `Total tasks: 4` दिखाते हैं। JSON कमांड `total` 4, `by_status.open` 2 और `by_status.done` 2 वाला एक ऑब्जेक्ट देता है। अमान्य फ़ॉर्मेट गैर-शून्य निकास कोड देता है। परीक्षण खाली इनपुट और स्ट्रिंग `status` के बिना कार्य भी जाँचते हैं। इन मामलों का देखा गया त्रुटि आउटपुट और निकास कोड पढ़ें।

| जाँच | सफल होने का प्रमाण | विफलता पर पुनर्प्राप्ति |
|---|---|---|
| **प्रोजेक्ट विवरण** | रिमाइंडर में शाम 7 बजे | शेड्यूल स्रोत ताज़ा करें |
| **रिपॉज़िटरी नक्शा** | आवश्यकता और परीक्षण पथ बताए | निर्देश फ़ाइलें सुधारें |
| **बाहरी स्रोत** | MCP स्रोत पढ़ा या ब्राउज़र विकल्प दर्ज किया | कनेक्शन या URL जाँचें |
| **Worker समीक्षा** | छूटे परीक्षण फ़ाइल में सत्यापित | Worker रिपोर्ट सुधारें |
| **फ़ाइल दायरा** | केवल प्रोग्राम और परीक्षण | हर अनचाहा बदलाव देखें |
| **व्यवहार** | text, JSON, खाली और त्रुटि जाँचे | एक कारण खोजकर दोबारा चलाएँ |
| **हस्तांतरण** | नया सत्र स्थिति पुनर्निर्मित करे | छूटा स्रोत या नतीजा जोड़ें |

**सुरक्षित रीसेट के लिए नई प्रति निकालें।** नोट्स लैब से बाहर रखें, केवल अस्थायी प्रति हटाएँ और मूल ZIP फिर से निकालें। जरूरी काम वाली रिपॉज़िटरी में व्यापक Git reset न करें।

## जाँच 7: नए सत्र को हस्तांतरण

लैब फ़ोल्डर से बाहर **180 शब्दों से छोटा हस्तांतरण लिखें**। आवश्यकता का संशोधन, बदली फ़ाइलें, सटीक परीक्षण कमांड और परिणाम, text और JSON आउटपुट, अमान्य इनपुट जाँचें, उपयोग रिकॉर्ड और अगला कदम शामिल करें। नया सत्र खोलें और उससे JSON कुंजियाँ बताने तथा फ़ीचर पास हुआ या नहीं पूछें।

**अपेक्षित उत्तर:** नया सत्र `total` और `by_status` बताता है, संशोधन 1 का संदर्भ देता है, केवल देखी गई जाँचें रिपोर्ट करता है और छूटी जाँच को बताता है।

## उत्तर कुंजी और मूल्यांकन

**एक मान्य implementation** नीचे है। पहला ब्लॉक `task_report.py` और दूसरा `tests/test_task_report.py` के रूप में लैब की नई प्रति में सहेजें। `tasks.json` और दोनों आवश्यकता फ़ाइलें अपरिवर्तित रखें। जाँच 6 के चरण चलाएँ। दूसरे समाधान की तुलना आवश्यकता और देखे व्यवहार से करें।

`task_report.py`:

```python
"""कार्यशाला कार्यों की टेक्स्ट गिनती या JSON सारांश छापता है।"""

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
    parser = argparse.ArgumentParser(description="कार्यशाला कार्य रिपोर्ट")
    parser.add_argument("path", type=Path, help="JSON कार्य सूची का पथ")
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
"""कार्यशाला कार्यों की text और JSON रिपोर्ट जाँच।"""

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

**उत्तर कुंजी के बाद रीसेट करें:** नोट्स लैब से बाहर सहेजें, यह प्रति हटाएँ और मूल स्टार्टर लैब फिर से निकालें। नई प्रति में दो आधारभूत परीक्षण होंगे और फ़ीचर implementation नहीं होगा।

**ऊपर की तालिका के हर जाँच-बिंदु के लिए एक अंक दें।** बाहरी स्रोत वाली पंक्ति में वास्तविक MCP कॉल और worker वाली पंक्ति में वास्तविक सत्र दर्ज हो तो सात अंक कनेक्टेड ट्रैक पूरा करते हैं। सत्यापित ब्राउज़र पृष्ठ स्रोत हो और टूल चरण स्पष्ट रूप से नहीं चलाए गए हों तो सात अंक अध्ययन ट्रैक पूरा करते हैं। व्यवहार, स्रोत या फ़ाइल दायरे की जाँच न होना दोनों ट्रैक रोकता है।

## समझ की जाँच

1. **इस फ़ीचर को कौन-सी आवश्यकता नियंत्रित करती है?** `docs/capstone-requirements.md`, संशोधन 1। पिछली स्टेटस-फ़िल्टर आवश्यकता पाठ 5 की है।
2. **JSON अनुबंध का प्रमाण क्या है?** कमांड आउटपुट पार्स करें, संख्यात्मक मान और हर स्टेटस की गिनती मिलाएँ, तथा खाली और अमान्य इनपुट जाँचें। एजेंट का सुसज्जित सारांश पर्याप्त नहीं।

## समस्या निवारण

- **संपादन से पहले आधारभूत परीक्षण विफल:** ZIP से लैब पुनर्स्थापित करें और सेटअप फिर चलाएँ।
- **एजेंट दूसरी फ़ाइल बदलता है:** diff देखें और केवल अनचाहा लैब बदलाव वापस करें।
- **MCP कनेक्शन विफल:** ब्राउज़र स्रोत उपयोग करें और जाँच को अध्ययन ट्रैक लिखें।
- **Worker गलत मान दोहराता है:** कैपस्टोन आवश्यकता फिर पढ़ें और रिपोर्ट सुधारें।
- **पुनः प्रयास सीमा समाप्त:** त्रुटि लॉग रखें और अगले कदम के लिए मानव समीक्षक से पूछें।

## आगे के कदम

**पूरा प्रमाण रिकॉर्ड सहेजें।** उन्नत टीम प्रकाशन और सिस्टमों के बीच अधिकार के लिए [AI सहयोग कार्यान्वयन पाठ्यक्रम](/ai-collaboration-course-start/) जारी रखें।

**पाठ्यक्रम नेविगेशन:** [पिछला अनिवार्य: सीमित लूप](/articles/effective-ai-bounded-agent-loops/), [वैकल्पिक: विशिष्ट एजेंट मूल्यांकन](/articles/effective-ai-specialized-agent-evaluation/), [पाठ्यक्रम रूपरेखा](/effective-ai-course-start/).

---
title: "البرمجة الآمنة بلغة Python"
date: 2023-09-26
lastmod: 2026-11-13
toc: true
draft: false
description: "تعلّم كتابة شيفرة Python آمنة، وتجنب الدوال غير الآمنة، واتبع أفضل الممارسات لبناء تطبيقات موثوقة ومتينة."
genre: ["البرمجة", "الأمن السيبراني", "تطوير البرمجيات", "Python", "كتابة الشيفرة", "تطوير الويب", "البرمجة الآمنة", "التقنية", "علوم الحاسوب", "أمن البيانات"]
tags: ["برمجة Python", "كتابة شيفرة آمنة", "دوال Python الآمنة", "أمن الشيفرة", "بدائل Python", "أفضل ممارسات البرمجة", "الأمن السيبراني", "نصائح البرمجة", "تطوير البرمجيات", "تطوير الويب", "تجنب دوال Python غير الآمنة", "تطبيقات Python آمنة", "إجراءات أمن الشيفرة", "ممارسات الشيفرة الآمنة", "نصائح أمن البرمجة"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "رسم توضيحي بأسلوب كرتوني لمطوّر يبني جداراً من كتل الشيفرة بأمان، رمزاً لممارسات البرمجة الآمنة بلغة Python."
coverCaption: "ابنِ بأمان، واكتب الشيفرة بثقة!"
---

## **دوال Python غير الآمنة وبدائلها**

Python لغة برمجة متعددة الاستخدامات وشائعة، وتوفّر دوالاً لمهام كثيرة. لكن بعض الدوال تنطوي على مخاطر أمنية وقد تسبب نتائج غير مقصودة عند استخدامها بلا حذر. يستعرض هذا القسم **دوال Python غير الآمنة** ومخاطرها وبدائل أكثر أماناً تؤدي وظائف مماثلة لتعزيز **الأمن** و**الاستقرار**.

### **مقدمة: احمِ مشاريع Python**

تتميّز Python بمكتباتها الواسعة وبنيتها الواضحة. لكن إساءة استخدام بعض الدوال قد تضر بالأمن والموثوقية. يساعدك فهم المخاطر واختيار أساليب بديلة على كتابة شيفرة أكثر مقاومة للتهديدات.

___________

## **دوال Python غير الآمنة ومخاطرها**

### تنفيذ الشيفرة ديناميكياً باستخدام `eval()`

تنفّذ `eval()` شيفرة Python ديناميكياً من سلسلة نصية. وقد تتيح **هجمات حقن الشيفرة** إذا لم تُنقَّح مدخلات المستخدم كما ينبغي. فكّر في **`ast.literal_eval()`** أو **`exec()`** للتنفيذ المنضبط والآمن.

#### تنفيذ ديناميكي باستخدام eval():
```python
# Unsafe: Using eval() for dynamic code execution
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("Result:", result)
```

#### بديل أكثر أماناً باستخدام `ast.literal_eval()`:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("Parsed value:", parsed_value)
except (ValueError, SyntaxError):
    print("Invalid input.")
```

### دمج السلاسل النصية مع بيانات غير منقّحة

قد يؤدي دمج السلاسل مع مدخلات المستخدم غير المنقّحة إلى **حقن SQL** أو ثغرات **البرمجة النصية عبر المواقع (XSS)**. استخدم **f-strings** أو **`str.format()`** مع **التحقق من المدخلات**.

#### دمج غير آمن للسلاسل النصية:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### استخدام f-strings (السلاسل النصية المنسّقة):
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### **Pickle** لتسلسل الكائنات

تستطيع وحدة `pickle` تسلسل كائنات Python وإلغاء تسلسلها، لكنها **لا تحمي من البيانات الخاطئة أو المصممة بخبث**. لتسلسل أكثر أماناً، استخدم مكتبات مثل **`json`** أو **`marshal`**.

#### استخدام غير آمن لـ pickle:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# Store or send serialized_data
```

#### بديل أكثر أماناً باستخدام json:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# Store or send serialized_data
```

### قصور تهريب HTML باستخدام `mark_safe()`

تضع دالة Django **`mark_safe()`** علامة على السلسلة باعتبارها HTML آمناً، وقد يعرّض ذلك التطبيقات **لهجمات XSS**. استخدم تهريب القوالب والمرشح **`safe`** لعرض HTML بأمان.

#### استخدام غير آمن لـ mark_safe() في قالب Django:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### نهج أكثر أماناً باستخدام تهريب القوالب:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### استخدام **`os.system()`** لتنفيذ أوامر النظام

تنفّذ `os.system()` أوامر النظام، لكنها عرضة **لهجمات حقن الأوامر**. استخدم وحدة **`subprocess`** لتنفيذ الأوامر والتعامل مع مخرجاتها بأمان أكبر.

#### استخدام غير آمن لـ os.system():
```python
command = input("Enter a command: ")
os.system(command)
```

#### بديل أكثر أماناً باستخدام subprocess:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("Output:", result.stdout)
```

### تجزئة كلمات المرور بصورة غير كافية باستخدام `hash()`

لا تصلح `hash()` لتجزئة كلمات المرور بأمان بسبب سرعتها وقابليتها **لهجمات القوة الغاشمة**. استخدم مكتبات قوية مثل **`bcrypt`** أو **`Argon2`** لحماية كلمات المرور.

#### تجزئة غير آمنة لكلمة المرور باستخدام hash():
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# Store hashed_password in the database
```

#### نهج أكثر أماناً باستخدام bcrypt:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# Store hashed_password in the database
```

## **بدائل أكثر أماناً وأفضل الممارسات**

### استخدم **`requests`** بدلاً من **`urllib`**

عند إرسال طلبات HTTP، فضّل مكتبة **`requests`** على `urllib` القديمة. فهي توفر واجهة أسهل وأكثر أماناً لإرسال الطلبات ومعالجة الاستجابات.

#### طلبات HTTP باستخدام مكتبة requests:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed.")
```

### معالجة الملفات بأمان باستخدام عبارة **`with`**

استخدم عبارة **`with`** عند التعامل مع الملفات لتجنّب تسرب الموارد وإدارة الملفات على نحو سليم. تغلق الملفات تلقائياً وتقلل خطر الأخطاء والثغرات.

#### معالجة الملفات باستخدام with:
```python
filename = "example.txt"

# Unsafe: Without using `with`
file = open(filename, "r")
content = file.read()
file.close()

# Safer: Using `with` statement
with open(filename, "r") as file:
    content = file.read()
```

### تنقية المدخلات باستخدام **`html.escape()`**

للوقاية من **هجمات XSS**، نقِّ مدخلات المستخدم باستخدام **`html.escape()`**. فهي تهرّب HTML الذي قد يكون ضاراً قبل عرضه.

#### تنقية مدخلات المستخدم للوقاية من XSS:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("Sanitized input:", sanitized_input)
```

### استعلامات ذات معاملات باستخدام **`sqlite3`**

عند التعامل مع قواعد البيانات، استخدم استعلامات **`sqlite3`** ذات المعاملات. تساعد هذه الاستعلامات على منع **حقن SQL** بتمرير مدخلات المستخدم كقيم.

#### استعلامات ذات معاملات باستخدام sqlite3:
```python
import sqlite3

db_connection = sqlite3.connect("database.db")
cursor = db_connection.cursor()

name = input("Enter a name: ")
age = input("Enter an age: ")

query = "INSERT INTO users (name, age) VALUES (?, ?)"
cursor.execute(query, (name, age))

db_connection.commit()
db_connection.close()
```

### إدارة متغيرات البيئة بأمان

لا تكشف المعلومات الحساسة مباشرةً في الشيفرة. استخدم متغيرات البيئة عبر قاموس **`os.environ`** أو حزمة مثل **`python-decouple`** لإدارة الإعدادات بأمان أكبر.

#### إدارة المتغيرات باستخدام os.environ:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API Key:", api_key)
else:
    print("API Key not set.")
```

#### إدارة المتغيرات باستخدام python-decouple:
```python
from decouple import config

api_key = config("API_KEY")
print("API Key:", api_key)
```

### عشوائية قوية باستخدام **`secrets`**

استخدم وحدة **`secrets`** بدلاً من `random` لإنشاء قيم عشوائية آمنة تشفيرياً. فهي مناسبة للعمليات الحساسة أمنياً.

#### إنشاء رموز آمنة باستخدام secrets:
```python
import secrets

token = secrets.token_hex(16)
print("Secure Token:", token)
```

## الخلاصة

يساعد نظام Python الغني المطورين على إنشاء تطبيقات قوية وغنية بالميزات. لكن الاستخدام المتهور لبعض الدوال قد يؤدي إلى ثغرات ويضر بسلامة الشيفرة. تساعد أفضل الممارسات والبدائل الأكثر أماناً على إنشاء برامج موثوقة.

______

## المراجع

- توثيق Python: [https://docs.python.org](https://docs.python.org)
- توثيق Django: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- دليل OWASP للوقاية من البرمجة النصية عبر المواقع (XSS): [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- دليل OWASP للوقاية من حقن SQL: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- مكتبة Python Requests: [https://docs.python-requests.org](https://docs.python-requests.org)
- توثيق SQLite3: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- وحدة Python `secrets`: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- حزمة python-decouple: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)


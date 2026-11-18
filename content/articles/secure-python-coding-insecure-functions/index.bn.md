---
title: "নিরাপদ Python কোডিং"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "অনিরাপদ ফাংশন এড়িয়ে এবং নির্ভরযোগ্য অ্যাপ তৈরির ভালো অনুশীলন মেনে নিরাপদ Python কোড লিখতে শিখুন।"
genre: ["প্রোগ্রামিং", "সাইবার নিরাপত্তা", "সফটওয়্যার উন্নয়ন", "Python", "কোডিং", "ওয়েব উন্নয়ন", "নিরাপদ কোডিং", "প্রযুক্তি", "কম্পিউটার বিজ্ঞান", "তথ্য নিরাপত্তা"]
tags: ["Python প্রোগ্রামিং", "নিরাপদ কোডিং", "নিরাপদ Python ফাংশন", "কোড নিরাপত্তা", "Python বিকল্প", "প্রোগ্রামিংয়ের ভালো অনুশীলন", "সাইবার নিরাপত্তা", "কোডিং পরামর্শ", "সফটওয়্যার উন্নয়ন", "ওয়েব উন্নয়ন", "অনিরাপদ Python ফাংশন এড়ানো", "নিরাপদ Python অ্যাপ", "কোড নিরাপত্তার ব্যবস্থা", "নিরাপদ কোড অনুশীলন", "প্রোগ্রামিং নিরাপত্তার পরামর্শ"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "কার্টুনধর্মী ছবিতে একজন ডেভেলপার নিরাপদে কোড ব্লকের দেয়াল তৈরি করছেন, যা নিরাপদ Python প্রোগ্রামিং অনুশীলনের প্রতীক।"
coverCaption: "নিরাপদে তৈরি করুন, আত্মবিশ্বাসে কোড লিখুন!"
---

## **অনিরাপদ Python ফাংশন এবং বিকল্প**

Python বহুমুখী ও বহুল ব্যবহৃত ভাষা, যাতে নানা কাজের জন্য ফাংশন আছে। তবে কিছু ফাংশন সতর্কভাবে ব্যবহার না করলে ঝুঁকি ও অনাকাঙ্ক্ষিত ফল তৈরি করতে পারে। এই অংশে **অনিরাপদ Python ফাংশন**, তাদের ঝুঁকি এবং একই ধরনের কাজ করা নিরাপদ বিকল্প তুলে ধরা হয়েছে, যাতে **নিরাপত্তা** ও **স্থিতিশীলতা** বাড়ে।

### **ভূমিকা: আপনার Python প্রকল্প সুরক্ষিত রাখুন**

বিস্তৃত লাইব্রেরি ও সহজ সিনট্যাক্সের জন্য Python জনপ্রিয়। কিছু ফাংশন ভুলভাবে ব্যবহার করলে নিরাপত্তা ও নির্ভরযোগ্যতা ক্ষতিগ্রস্ত হয়। ঝুঁকি বুঝে অন্য পদ্ধতি বেছে নিলে আরও প্রতিরোধী কোড লেখা যায়।

___________

## **অনিরাপদ Python ফাংশন ও ঝুঁকি**

### `eval()` দিয়ে ডাইনামিক কোড চালানো

`eval()` স্ট্রিং থেকে Python কোড ডাইনামিকভাবে চালায়। শক্তিশালী হলেও ব্যবহারকারীর ইনপুট ঠিকভাবে পরিষ্কার না করলে **কোড ইনজেকশন আক্রমণ** হতে পারে। নিয়ন্ত্রিত ও নিরাপদ কোড চালানোর জন্য **`ast.literal_eval()`** বা **`exec()`** বিবেচনা করুন।

#### eval() দিয়ে ডাইনামিক কোড চালানো:
```python
# অনিরাপদ: ডাইনামিক কোড চালাতে eval() ব্যবহার
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("ফলাফল:", result)
```

#### `ast.literal_eval()` দিয়ে আরও নিরাপদ বিকল্প:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("পার্স করা মান:", parsed_value)
except (ValueError, SyntaxError):
    print("ইনপুট অবৈধ।")
```

### অপরিষ্কার ডেটা দিয়ে স্ট্রিং জোড়া লাগানো

অপরিষ্কার ব্যবহারকারী ইনপুট স্ট্রিংয়ের সঙ্গে জুড়লে **SQL ইনজেকশন** বা **ক্রস-সাইট স্ক্রিপ্টিং (XSS)** দুর্বলতা তৈরি হতে পারে। **ইনপুট যাচাইয়ের** সঙ্গে **f-string** বা **`str.format()`** ব্যবহার করুন।

#### অনিরাপদ স্ট্রিং সংযোজন:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### f-string (ফরম্যাট করা স্ট্রিং লিটারেল) ব্যবহার:
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### অবজেক্ট সিরিয়ালাইজেশনের জন্য **Pickle**

`pickle` মডিউল Python অবজেক্ট সিরিয়ালাইজ ও ডি-সিরিয়ালাইজ করে, কিন্তু **ভুল বা ক্ষতিকরভাবে তৈরি ডেটার বিরুদ্ধে নিরাপদ নয়**। নিরাপদ সিরিয়ালাইজেশনের জন্য **`json`** বা **`marshal`**-এর মতো লাইব্রেরি বেছে নিন।

#### pickle-এর অনিরাপদ ব্যবহার:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# serialized_data সংরক্ষণ বা পাঠান
```

#### json দিয়ে নিরাপদ বিকল্প:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# serialized_data সংরক্ষণ বা পাঠান
```

### `mark_safe()` দিয়ে HTML যথেষ্ট এস্কেপ না করা

Django-এর **`mark_safe()`** একটি স্ট্রিংকে নিরাপদ HTML হিসেবে চিহ্নিত করে, ফলে অ্যাপ **XSS আক্রমণের** ঝুঁকিতে পড়তে পারে। HTML নিরাপদে দেখাতে টেমপ্লেট এস্কেপিং এবং **`safe`** ফিল্টার ব্যবহার করুন।

#### Django টেমপ্লেটে mark_safe()-এর অনিরাপদ ব্যবহার:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### টেমপ্লেট এস্কেপিংয়ের নিরাপদ পদ্ধতি:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### সিস্টেম কমান্ডের জন্য **`os.system()`** ব্যবহার

`os.system()` সিস্টেম কমান্ড চালায়, তবে এটি **কমান্ড ইনজেকশন আক্রমণের** ঝুঁকিতে থাকে। কমান্ড নিরাপদে চালানো ও ফল সামলাতে **`subprocess`** মডিউল ব্যবহার করুন।

#### os.system()-এর অনিরাপদ ব্যবহার:
```python
command = input("Enter a command: ")
os.system(command)
```

#### subprocess দিয়ে নিরাপদ বিকল্প:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("আউটপুট:", result.stdout)
```

### `hash()` দিয়ে অপর্যাপ্ত পাসওয়ার্ড হ্যাশিং

`hash()` দ্রুত এবং **ব্রুট-ফোর্স আক্রমণের** ঝুঁকিতে থাকায় পাসওয়ার্ড নিরাপদে হ্যাশ করার জন্য উপযুক্ত নয়। **`bcrypt`** বা **`Argon2`**-এর মতো শক্তিশালী লাইব্রেরি ব্যবহার করুন।

#### hash() দিয়ে অনিরাপদ পাসওয়ার্ড হ্যাশিং:
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# hashed_password ডেটাবেসে সংরক্ষণ করুন
```

#### bcrypt দিয়ে নিরাপদ পদ্ধতি:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# hashed_password ডেটাবেসে সংরক্ষণ করুন
```

## **নিরাপদ বিকল্প ও ভালো অনুশীলন**

### **`urllib`**-এর বদলে **`requests`** ব্যবহার

HTTP অনুরোধে পুরোনো `urllib`-এর বদলে **`requests`** পছন্দ করুন। এটি অনুরোধ পাঠানো ও উত্তর সামলানোর সহজ এবং নিরাপদ ইন্টারফেস দেয়।

#### requests লাইব্রেরি দিয়ে HTTP অনুরোধ:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("অনুরোধ ব্যর্থ হয়েছে।")
```

### **`with`** স্টেটমেন্টে ফাইল নিরাপদে সামলানো

ফাইল নিয়ে কাজের সময় **`with`** ব্যবহার করলে রিসোর্স লিক এড়ানো যায় এবং ফাইল সঠিকভাবে ব্যবস্থাপিত হয়। এটি নিজে ফাইল বন্ধ করে, ফলে ত্রুটি ও দুর্বলতার ঝুঁকি কমে।

#### with দিয়ে ফাইল ব্যবস্থাপনা:
```python
filename = "example.txt"

# অনিরাপদ: with ব্যবহার না করে
file = open(filename, "r")
content = file.read()
file.close()

# নিরাপদতর: with স্টেটমেন্ট ব্যবহার করে
with open(filename, "r") as file:
    content = file.read()
```

### **`html.escape()`** দিয়ে ইনপুট পরিষ্কার

**XSS আক্রমণ** ঠেকাতে **`html.escape()`** দিয়ে ব্যবহারকারীর ইনপুট পরিষ্কার করুন। এটি দেখানোর আগে সম্ভাব্য ক্ষতিকর HTML এস্কেপ করে।

#### XSS ঠেকাতে ব্যবহারকারীর ইনপুট পরিষ্কার:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("পরিশোধিত ইনপুট:", sanitized_input)
```

### **`sqlite3`**-এ প্যারামিটারযুক্ত কোয়েরি

ডেটাবেসে কাজের সময় **`sqlite3`**-এর প্যারামিটারযুক্ত কোয়েরি ব্যবহার করুন। ইনপুটকে কোয়েরির মান হিসেবে পাঠানো **SQL ইনজেকশন আক্রমণ** ঠেকাতে সাহায্য করে।

#### sqlite3-এ প্যারামিটারযুক্ত কোয়েরি:
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

### পরিবেশ ভেরিয়েবল নিরাপদে পরিচালনা

সংবেদনশীল তথ্য সরাসরি কোডে প্রকাশ করবেন না। **`os.environ`** ডিকশনারি বা **`python-decouple`** প্যাকেজ দিয়ে পরিবেশ ভেরিয়েবল ব্যবহার করুন।

#### os.environ দিয়ে পরিবেশ ভেরিয়েবল পরিচালনা:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API কী:", api_key)
else:
    print("API কী সেট করা নেই।")
```

#### python-decouple দিয়ে পরিবেশ ভেরিয়েবল পরিচালনা:
```python
from decouple import config

api_key = config("API_KEY")
print("API কী:", api_key)
```

### **`secrets`** দিয়ে শক্তিশালী র‍্যান্ডমনেস

ক্রিপ্টোগ্রাফিকভাবে নিরাপদ র‍্যান্ডম মান তৈরি করতে `random`-এর বদলে **`secrets`** ব্যবহার করুন। নিরাপত্তা-সংবেদনশীল কাজে এটি উপযুক্ত।

#### secrets দিয়ে নিরাপদ টোকেন তৈরি:
```python
import secrets

token = secrets.token_hex(16)
print("নিরাপদ টোকেন:", token)
```

## উপসংহার

Python-এর সমৃদ্ধ ইকোসিস্টেম শক্তিশালী ও বৈশিষ্ট্যসমৃদ্ধ অ্যাপ তৈরি করতে সাহায্য করে। কিছু ফাংশনের অসতর্ক ব্যবহার দুর্বলতা তৈরি করে এবং কোডের অখণ্ডতা নষ্ট করতে পারে। ভালো অনুশীলন ও নিরাপদ বিকল্প বেছে নিয়ে নির্ভরযোগ্য সফটওয়্যার তৈরি করুন।

______

## তথ্যসূত্র

- Python ডকুমেন্টেশন: [https://docs.python.org](https://docs.python.org)
- Django ডকুমেন্টেশন: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- OWASP XSS প্রতিরোধ চিট শিট: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP SQL ইনজেকশন প্রতিরোধ চিট শিট: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Python Requests লাইব্রেরি: [https://docs.python-requests.org](https://docs.python-requests.org)
- SQLite3 ডকুমেন্টেশন: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Python `secrets` মডিউল: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- python-decouple প্যাকেজ: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)


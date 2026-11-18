---
title: "सुरक्षित Python कोडिंग"
date: 2023-09-26
lastmod: 2026-11-14
toc: true
draft: false
description: "असुरक्षित फ़ंक्शन से बचकर और मज़बूत, भरोसेमंद ऐप के लिए सर्वोत्तम तरीक़े अपनाकर सुरक्षित Python कोड लिखना सीखें।"
genre: ["प्रोग्रामिंग", "साइबर सुरक्षा", "सॉफ़्टवेयर विकास", "Python", "कोडिंग", "वेब विकास", "सुरक्षित कोडिंग", "प्रौद्योगिकी", "कंप्यूटर विज्ञान", "डेटा सुरक्षा"]
tags: ["Python प्रोग्रामिंग", "सुरक्षित कोडिंग", "सुरक्षित Python फ़ंक्शन", "कोड सुरक्षा", "Python के विकल्प", "प्रोग्रामिंग के सर्वोत्तम तरीक़े", "साइबर सुरक्षा", "कोडिंग सुझाव", "सॉफ़्टवेयर विकास", "वेब विकास", "असुरक्षित Python फ़ंक्शन से बचें", "सुरक्षित Python ऐप", "कोड सुरक्षा उपाय", "सुरक्षित कोड अभ्यास", "प्रोग्रामिंग सुरक्षा सुझाव"]
cover: "/img/cover/secure-python-coding-wall.webp"
coverAlt: "कार्टून शैली का चित्र: एक डेवलपर कोड ब्लॉकों की दीवार सुरक्षित रूप से बना रहा है, जो सुरक्षित Python प्रोग्रामिंग तरीक़ों का प्रतीक है।"
coverCaption: "सुरक्षित बनाएँ, आत्मविश्वास से कोड करें!"
---

## **असुरक्षित Python फ़ंक्शन और उनके विकल्प**

Python एक बहुउपयोगी और लोकप्रिय भाषा है, जिसमें कई कामों के लिए फ़ंक्शन हैं। फिर भी कुछ फ़ंक्शन सावधानी से न इस्तेमाल करने पर सुरक्षा जोखिम और अनपेक्षित परिणाम पैदा कर सकते हैं। यह लेख **असुरक्षित Python फ़ंक्शन**, उनके जोखिम और समान काम करने वाले अधिक सुरक्षित विकल्प बताता है, ताकि **सुरक्षा** और **स्थिरता** मज़बूत हो।

### **परिचय: अपने Python प्रोजेक्ट सुरक्षित रखें**

Python अपनी विस्तृत लाइब्रेरी और सहज सिंटैक्स के कारण लोकप्रिय है। कुछ फ़ंक्शन का ग़लत उपयोग सुरक्षा और विश्वसनीयता को कमज़ोर कर सकता है। जोखिमों को समझकर दूसरी विधियाँ अपनाने से ख़तरों का सामना करने वाला कोड बनता है।

___________

## **असुरक्षित Python फ़ंक्शन और जोखिम**

### `eval()` से डायनेमिक कोड निष्पादन

`eval()` स्ट्रिंग से Python कोड को डायनेमिक रूप से चलाता है। उपयोगकर्ता इनपुट को सही तरह साफ़ न करने पर इससे **कोड इंजेक्शन हमले** हो सकते हैं। नियंत्रित और सुरक्षित निष्पादन के लिए **`ast.literal_eval()`** या **`exec()`** पर विचार करें।

#### eval() से डायनेमिक कोड निष्पादन:
```python
# असुरक्षित: डायनामिक कोड चलाने के लिए eval() का उपयोग
user_input = input("Enter a Python expression: ")
result = eval(user_input)
print("परिणाम:", result)
```

#### `ast.literal_eval()` का अधिक सुरक्षित विकल्प:
```python
import ast

user_input = input("Enter a literal value: ")
try:
    parsed_value = ast.literal_eval(user_input)
    print("पार्स किया गया मान:", parsed_value)
except (ValueError, SyntaxError):
    print("अमान्य इनपुट।")
```

### बिना साफ़ किए डेटा के साथ स्ट्रिंग जोड़ना

बिना साफ़ किए उपयोगकर्ता इनपुट को स्ट्रिंग से जोड़ने पर **SQL इंजेक्शन** या **क्रॉस-साइट स्क्रिप्टिंग (XSS)** की कमज़ोरियाँ आ सकती हैं। **इनपुट सत्यापन** के साथ **f-string** या **`str.format()`** इस्तेमाल करें।

#### असुरक्षित स्ट्रिंग जोड़ना:
```python
user_input = input("Enter your name: ")
message = "Hello, " + user_input + "!"
print(message)
```

#### f-string (फ़ॉर्मैट की गई स्ट्रिंग लिटरल) का उपयोग:
```python
user_input = input("Enter your name: ")
message = f"Hello, {user_input}!"
print(message)
```

### ऑब्जेक्ट सीरियलाइज़ेशन के लिए **Pickle**

`pickle` मॉड्यूल Python ऑब्जेक्ट को सीरियलाइज़ और डीसीरियलाइज़ करता है, लेकिन **ग़लत या दुर्भावनापूर्ण तरीके से बनाए डेटा के विरुद्ध सुरक्षित नहीं है**। सुरक्षित सीरियलाइज़ेशन के लिए **`json`** या **`marshal`** जैसी लाइब्रेरी चुनें।

#### pickle का असुरक्षित उपयोग:
```python
import pickle

data = {'user': 'admin', 'role': 'admin'}
serialized_data = pickle.dumps(data)
# serialized_data को संग्रहित करें या भेजें
```

#### json का अधिक सुरक्षित विकल्प:
```python
import json

data = {'user': 'admin', 'role': 'admin'}
serialized_data = json.dumps(data)
# serialized_data को संग्रहित करें या भेजें
```

### `mark_safe()` से HTML का अपर्याप्त एस्केपिंग

Django का **`mark_safe()`** स्ट्रिंग को सुरक्षित HTML के रूप में चिह्नित करता है, जिससे ऐप **XSS हमलों** के संपर्क में आ सकता है। HTML को सुरक्षित दिखाने के लिए टेम्पलेट एस्केपिंग और **`safe`** फ़िल्टर इस्तेमाल करें।

#### Django टेम्पलेट में mark_safe() का असुरक्षित उपयोग:
```python
from django.utils.safestring import mark_safe

input_data = input("Enter some HTML content: ")
safe_html = mark_safe(input_data)
```

#### टेम्पलेट एस्केपिंग का अधिक सुरक्षित तरीक़ा:
```python
from django.utils.html import escape

input_data = input("Enter some HTML content: ")
escaped_html = escape(input_data)
```

### सिस्टम कमांड के लिए **`os.system()`** का उपयोग

`os.system()` सिस्टम कमांड चला सकता है, लेकिन यह **कमांड इंजेक्शन हमलों** के प्रति संवेदनशील है। कमांड को अधिक सुरक्षित ढंग से चलाने और आउटपुट संभालने के लिए **`subprocess`** मॉड्यूल अपनाएँ।

#### os.system() का असुरक्षित उपयोग:
```python
command = input("Enter a command: ")
os.system(command)
```

#### subprocess का अधिक सुरक्षित विकल्प:
```python
import subprocess

command = input("Enter a command: ")
result = subprocess.run(command, shell=True, capture_output=True, text=True)
print("आउटपुट:", result.stdout)
```

### `hash()` से अपर्याप्त पासवर्ड हैशिंग

`hash()` तेज़ है और **ब्रूट-फ़ोर्स हमलों** के प्रति संवेदनशील है, इसलिए पासवर्ड को सुरक्षित रूप से हैश करने के लिए उपयुक्त नहीं है। **`bcrypt`** या **`Argon2`** जैसी मज़बूत लाइब्रेरी इस्तेमाल करें।

#### hash() से असुरक्षित पासवर्ड हैशिंग:
```python
password = input("Enter your password: ")
hashed_password = hash(password)
# hashed_password को डेटाबेस में संग्रहित करें
```

#### bcrypt का अधिक सुरक्षित तरीक़ा:
```python
import bcrypt

password = input("Enter your password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
# hashed_password को डेटाबेस में संग्रहित करें
```

## **अधिक सुरक्षित विकल्प और सर्वोत्तम तरीक़े**

### **`urllib`** के बजाय **`requests`** इस्तेमाल करें

HTTP अनुरोधों के लिए पुराने `urllib` के बजाय **`requests`** चुनें। यह अनुरोध भेजने और जवाब संभालने के लिए सरल व सुरक्षित इंटरफ़ेस देता है।

#### requests लाइब्रेरी से HTTP अनुरोध:
```python
import requests

url = "https://api.example.com/data"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("अनुरोध विफल हुआ।")
```

### **`with`** कथन से फ़ाइलों को सुरक्षित संभालें

फ़ाइलों के साथ काम करते समय **`with`** कथन का उपयोग करें, ताकि संसाधन लीक न हों और फ़ाइलें सही तरह संभाली जाएँ। यह फ़ाइल अपने आप बंद करता है और त्रुटियों व कमज़ोरियों का जोखिम घटाता है।

#### with से फ़ाइल प्रबंधन:
```python
filename = "example.txt"

# असुरक्षित: with का उपयोग किए बिना
file = open(filename, "r")
content = file.read()
file.close()

# अधिक सुरक्षित: with कथन का उपयोग
with open(filename, "r") as file:
    content = file.read()
```

### **`html.escape()`** से इनपुट साफ़ करें

**XSS हमलों** को रोकने के लिए **`html.escape()`** से उपयोगकर्ता इनपुट साफ़ करें। यह दिखाने से पहले संभावित रूप से हानिकारक HTML को एस्केप करता है।

#### XSS रोकने के लिए उपयोगकर्ता इनपुट साफ़ करना:
```python
import html

user_input = input("Enter some text: ")
sanitized_input = html.escape(user_input)
print("सैनिटाइज़ किया गया इनपुट:", sanitized_input)
```

### **`sqlite3`** के साथ पैरामीटर वाले क्वेरी

डेटाबेस के साथ काम करते समय **`sqlite3`** की पैरामीटर वाली क्वेरी इस्तेमाल करें। इनपुट को क्वेरी मान के रूप में भेजने से **SQL इंजेक्शन हमलों** को रोकने में मदद मिलती है।

#### sqlite3 में पैरामीटर वाली क्वेरी:
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

### एनवायरनमेंट वेरिएबल सुरक्षित रूप से प्रबंधित करें

संवेदनशील जानकारी को सीधे कोड में न रखें। **`os.environ`** डिक्शनरी या **`python-decouple`** जैसे पैकेज से एनवायरनमेंट वेरिएबल प्रबंधित करें।

#### os.environ से एनवायरनमेंट वेरिएबल प्रबंधित करना:
```python
import os

api_key = os.environ.get("API_KEY")
if api_key:
    print("API कुंजी:", api_key)
else:
    print("API कुंजी सेट नहीं है।")
```

#### python-decouple से एनवायरनमेंट वेरिएबल प्रबंधित करना:
```python
from decouple import config

api_key = config("API_KEY")
print("API कुंजी:", api_key)
```

### **`secrets`** से मज़बूत यादृच्छिकता

क्रिप्टोग्राफ़िक रूप से सुरक्षित यादृच्छिक मान बनाने के लिए `random` के बजाय **`secrets`** मॉड्यूल का उपयोग करें। यह सुरक्षा-संवेदनशील कामों के लिए उपयुक्त है।

#### secrets से सुरक्षित टोकन बनाना:
```python
import secrets

token = secrets.token_hex(16)
print("सुरक्षित टोकन:", token)
```

## निष्कर्ष

Python का विस्तृत इकोसिस्टम शक्तिशाली ऐप बनाने में मदद करता है। लेकिन कुछ फ़ंक्शन का लापरवाह उपयोग कमज़ोरियाँ ला सकता है और कोड की अखंडता से समझौता कर सकता है। सर्वोत्तम तरीक़ों और सुरक्षित विकल्पों से अधिक भरोसेमंद सॉफ़्टवेयर बनाएँ।

______

## संदर्भ

- Python दस्तावेज़: [https://docs.python.org](https://docs.python.org)
- Django दस्तावेज़: [https://docs.djangoproject.com](https://docs.djangoproject.com)
- OWASP XSS रोकथाम चीट शीट: [https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP SQL इंजेक्शन रोकथाम चीट शीट: [https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html](https://owasp.org/www-project-cheat-sheets/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- Python Requests लाइब्रेरी: [https://docs.python-requests.org](https://docs.python-requests.org)
- SQLite3 दस्तावेज़: [https://docs.python.org/3/library/sqlite3.html](https://docs.python.org/3/library/sqlite3.html)
- Python `secrets` मॉड्यूल: [https://docs.python.org/3/library/secrets.html](https://docs.python.org/3/library/secrets.html)
- python-decouple पैकेज: [https://pypi.org/project/python-decouple/](https://pypi.org/project/python-decouple/)


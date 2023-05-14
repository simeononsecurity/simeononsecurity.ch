---
title: "HackTheBox - চ্যালেঞ্জ - Crypto - কল"
date: 2020-10-07
draft: false
description: "HackTheBox-এ Crypto - Call চ্যালেঞ্জ সমাধান করতে প্রাইম নম্বর সাইফার ব্যবহার করে কীভাবে DTMF টোন ডিক্রিপ্ট করতে হয় তা শিখুন।"
tags: ["HackTheBox", "ক্রিপ্টো চ্যালেঞ্জ", "DTMF টোন", "প্রাইম নাম্বার সাইফার", "ডিক্রিপশন", "ধাঁধা সমাধান করা", "ক্রিপ্টোগ্রাফি", "অডিও রূপান্তর", "ডায়ালএবিসি", "Decode.fr", "WAV", "MP3", "ফ্রিকোয়েন্সি", "গাণিতিক বৈশিষ্ট্য", "পতাকা", "ধৃষ্টতা", "সোনিক ভিজ্যুয়ালাইজার", "সংখ্যা", "স্বয়ংক্রিয় টেলার মেনু", "পে ফোন"]
toc: true
cover: "/img/cover/A_cartoon_phone_with_a_green_screen_and_a_padlock_on_it.png"
coverAlt: "একটি কার্টুন ফোন একটি সবুজ স্ক্রীন এবং এর উপর একটি প্যাডলক, নিরাপত্তা এবং এনক্রিপশনের প্রতীক, ব্যাকগ্রাউনে চিত্রিত DTMF টোন সহ"
coverCaption: ""
---

sound.mp3 ফাইলে DTMF টোন ডিকোড করে HackTheBox-এ Crypto - কল চ্যালেঞ্জ সমাধান করুন। ফাইলটিকে .wav-এ রূপান্তর করুন এবং সাইফার টেক্সট পেতে DialABC ব্যবহার করুন। সংখ্যাগুলি আলাদা করুন এবং পতাকাটি প্রকাশ করতে Decode.fr-এ মৌলিক সংখ্যা সাইফার ব্যবহার করুন। HackTheBox-এ এই উত্তেজনাপূর্ণ চ্যালেঞ্জে আপনার দক্ষতাকে প্রাইম নম্বর সাইফারে পরীক্ষা করার জন্য প্রস্তুত হন।"

______

## প্রদত্ত ফাইল:

আপনাকে একটি ফাইল প্রদান করা হয়েছে:
- sound.mp3

## ওয়াক থ্রু:

**sound.mp3** বাজানো, আপনি একটি পরিচিত শব্দ শুনতে পাবেন। আপনি যদি **DTMF** (ডুয়াল টোন মাল্টি ফ্রিকোয়েন্সি) টোন শুনতে পাচ্ছেন এমন শব্দগুলি আপনি পরিচিত না হন। পে ফোনে ডায়াল করার সময় বা স্বয়ংক্রিয় টেলার মেনুতে যাওয়ার সময় আপনি একই টোন শুনতে পান।

প্রতিটি স্বরের একটি নির্দিষ্ট ফ্রিকোয়েন্সি আছে। আপনি ম্যানুয়ালি নম্বর পেতে পারেন, কিন্তু এর জন্য কার সময় আছে?[DialABC](http://www.dialabc.com/sound/detect/index.html) has a great tool for this, but doesn't support mp3 files. First, you'll have to convert it to .wav with this [tool](https://online-audio-converter.com/)

রূপান্তরিত ফাইল নিন[DialABC](http://www.dialabc.com/sound/detect/index.html) এবং আপনি নিম্নলিখিত আউটপুট পাবেন:
```
2331434783711923431767372331117714113
```
 
Take notice that if you listen to the audio file carefully or open it in **Audacity** or **Sonic Visualizer** that, with one exception, the numbers are paired in groups of two.
If you separate out the number you get the following:
```
23 31 43 47 83 71 19 23 43 17 67 37 23 31 11 7 71 41 13
```

Organized like this, you might be confused and think that it might be HEX. It isn't.  
Pay close attention to the numbers. What mathematical trait do each grouping of numbers share?....
They are all prime numbers. Which should bring you to try the lesser known **prime number cipher**.

We'll use [Decode.fr](https://www.dcode.fr/prime-numbers-cipher) to complete this challenge.   
Submit the cipher text from before we separated it out and you'll get the flag.
```
2331434783711923431767372331117714113
```

______

### Flag Example:
```
HTB{xxxxxxxxxxxxxxxxxxx}
```
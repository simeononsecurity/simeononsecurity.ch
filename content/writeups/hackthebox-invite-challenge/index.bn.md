---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "উইন্ডোজ এবং লিনাক্স উভয় ক্ষেত্রে পেনিট্রেশন টেস্টিং এবং সাইবার সিকিউরিটিতে আপনার দক্ষতা পরীক্ষা ও অগ্রসর করার জন্য কীভাবে একটি আমন্ত্রণ কোড তৈরি করতে হয় এবং হ্যাক দ্যাবক্স অনলাইন প্ল্যাটফর্মে যোগদান করতে হয় তা শিখুন।"
tags: ["HackTheBox", "আমন্ত্রণ চ্যালেঞ্জ", "অনুপ্রবেশ পরীক্ষা", "সাইবার নিরাপত্তা", "উইন্ডোজ", "লিনাক্স", "অনলাইন প্ল্যাটফর্ম", "HTTP পোস্ট", "আমন্ত্রিত কোড", "বেস64 এনকোডেড", "শক্তির উৎস", "লিনাক্স ব্যাশ", "বেস64 ডিকোড", "কোড জেনারেশনকে আমন্ত্রণ জানান", "প্রোগ্রামিং", "ওয়েব ডেভেলপমেন্ট", "প্রযুক্তি", "আইটি নিরাপত্তা", "আইটি প্রশিক্ষণ"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "একটি কার্টুন কম্পিউটার স্ক্রীন হ্যাক দ্য বক্স ওয়েবসাইটকে দেখায় যেখানে একটি খিলানের দরজা একটি চাবি দিয়ে আনলক করা হয়েছে, একটি ট্রফি বা পদক প্রকাশ করছে, হ্যাকদ্যবক্স-এর লোগোর রঙিন স্কিমে (নীল এবং সাদা) একটি সিটিস্কেপ ব্যাকগ্রাউন্ড সহ।"
coverCaption: ""
---
 Windows বা Linux-এ HackTheBox আমন্ত্রণ চ্যালেঞ্জ সম্পূর্ণ করার জন্য ধাপে ধাপে নির্দেশাবলী। পেনিট্রেশন টেস্টিং এবং সাইবার নিরাপত্তায় আপনার দক্ষতা পরীক্ষা ও অগ্রসর করতে কীভাবে একটি আমন্ত্রণ কোড তৈরি করতে হয় এবং অনলাইন প্ল্যাটফর্মে যোগ দিতে হয় তা শিখুন। নিবন্ধটি সহজ এবং উন্নত উভয় সমাধান উপস্থাপন করে, যা সমস্ত স্তরের ব্যবহারকারীদের জন্য চ্যালেঞ্জটি সম্পূর্ণ করা এবং প্ল্যাটফর্মে অ্যাক্সেস পেতে সহজ করে তোলে।

______

## হ্যাক দ্য বক্স কি?

HackTheBox হল একটি অনলাইন প্ল্যাটফর্ম যা আপনার পেনিট্রেশন টেস্টিং এবং সাইবার সিকিউরিটিতে আপনার দক্ষতা পরীক্ষা ও অগ্রসর করার জন্য।

## আপনি কীভাবে হ্যাক দ্য বক্সে যোগ দেবেন?

HackTheBox (HTB) এ একটি অ্যাকাউন্ট তৈরি করতে আপনাকে আমন্ত্রণ চ্যালেঞ্জটি সম্পূর্ণ করতে হবে, অথবা নিজেকে হ্যাক করতে হবে৷ যদিও এটি কঠিন নয়, চিন্তা করবেন না এবং এই নিবন্ধটি আপনাকে চ্যালেঞ্জটি অসম্পূর্ণ করতে সহায়তা করবে৷

প্রথম, যান[HackTheBox Website](https://hackthebox.eu) এবং জয়েন বোতামে ক্লিক করুন।

আপনাকে একটি আমন্ত্রণ কোডের জন্য স্পষ্টভাবে জিজ্ঞাসা করা একটি বাক্সের সাথে উপস্থাপন করা হবে।

আপনি স্পষ্টভাবে একটি টেক্সট বক্স দেখতে পাচ্ছেন যা আমাদের কাছে একটি আমন্ত্রণ কোড চাচ্ছে।

আপনার কীবোর্ডে ***"F12"*** অথবা আপনার ব্রাউজার ডেভেলপার টুল খুলতে ***"Ctrl + Shift + I"*** টিপুন।

"এলিমেন্টস" ট্যাবে, আপনি একটি স্ক্রিপ্ট পাবেন **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

জাভাস্ক্রিপ্ট এবং makeInviteCode ফাংশন পর্যালোচনা করে, আপনি আবিষ্কার করবেন যে একটি আমন্ত্রণ কোড পেতে আপনাকে **/api/invite/generate**-এ একটি **HTTP পোস্ট** পাঠাতে হবে।

Base64 এনকোডেড আমন্ত্রণ কোড পেতে আপনি নিম্নলিখিতগুলি করতে পারেন:

### সমাধান:

#### সহজ:
- **উইন্ডোজ**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" ```

Which will generate the following content: ```json {"success":1,"data":{"code":"Tk9ULVRIRS1GTEFHLVlPVSdSRS1MT09LSU5HLUZPUg==","format":"encoded"},"0":200} ```

If you take the encoded invite code to [base64decode.org](https://www.base64decode.org/), you'll get your invite code!

#### Advanced (Instantly print out invite code):
 - **Windows**: ```powershell $base64api=((Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON).Data).Code ; [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($base64api)) ```
- **Linux**: ```bash curl -X POST "https://www.hackthebox.eu/api/invite/generate" | jq -r '.data.code' | base64 -d ```
 - **Note**: You'll need to install the [jq](https://stedolan.github.io/jq/download/) package.

______

### Invite Code Ex:
```XXXXX-XXXXX-XXXXX-XXXXX-XXXXX```



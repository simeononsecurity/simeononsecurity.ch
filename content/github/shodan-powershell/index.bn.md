---
title: "Shodan PowerShell মডিউল সহ OSINT স্বয়ংক্রিয় করুন"
date: 2020-11-14
---

Shodan API এর সাথে ইন্টারঅ্যাক্ট করার জন্য PowerShell মডিউলের একটি সংগ্রহ

**মন্তব্য:**
- আপনার প্রয়োজন হবে শোডান এপিআই কী, যা আপনার এ পাওয়া যাবে[Shodan Account](https://account.shodan.io/)
- মডিউলগুলিতে ব্যবহৃত API-এর উদাহরণ পাওয়া যেতে পারে[Shodan Developers Page](https://developer.shodan.io/api)
- কিছু মডিউল স্ক্যান বা কোয়েরি ক্রেডিট ব্যবহার করতে পারে যখন আপনি ওয়েবসাইট, CLI বা API (এই স্ক্রিপ্টগুলি কী করে) মাধ্যমে ডেটা ডাউনলোড করেন তখন ক্যোয়ারী ক্রেডিট ব্যবহার করা হয়।
  যেহেতু আমরা API ব্যবহার করছি এটা মনে রাখা গুরুত্বপূর্ণ যে ক্যোয়ারী ক্রেডিট কেটে নেওয়া হয় যদি:
  1. একটি অনুসন্ধান ফিল্টার ব্যবহার করা হয়
  2. পৃষ্ঠা 2 বা তার পরে অনুরোধ করা হয়েছে
      ক্রেডিটগুলি মাসের শুরুতে পুনর্নবীকরণ করা হয় এবং 1 ক্রেডিট আপনাকে 100টি ফলাফল ডাউনলোড করতে দেয়৷
      স্ক্যান ক্রেডিট হিসাবে, 1টি স্ক্যান ক্রেডিট আপনাকে 1টি আইপি স্ক্যান করতে দেয় এবং তারা মাসের শুরুতে পুনর্নবীকরণও করে।
      অনুগ্রহ করে শোদান সহায়তা কেন্দ্র দেখুন[HERE](https://help.shodan.io/the-basics/credit-types-explained) সম্পূর্ণ বিবরণের জন্য।

## সুচিপত্র
-[Download Instructions](https://github.com/simeononsecurity/Shodan_PS#download)
-[Installation Instructions](https://github.com/simeononsecurity/Shodan_PS#install)
- **মডিউল**
  -[Get-ShodanAPIInfo](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanAPIInfo) - প্রদত্ত API কী-এর অন্তর্গত API পরিকল্পনা সম্পর্কে তথ্য ফেরত দিন।
  -[Get-ShodanClientHTTPHeaders](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientHTTPHeaders) - একটি ওয়েব সার্ভারের সাথে সংযোগ করার সময় আপনার ক্লায়েন্ট যে HTTP শিরোনাম পাঠায় তা দেখায়।
  -[Get-ShodanClientIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanClientIP) - ইন্টারনেট থেকে দেখা আপনার বর্তমান আইপি ঠিকানা পায়।
  -[Get-ShodanDNSDomain](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSDomain) - প্রদত্ত ডোমেনের জন্য সমস্ত সাবডোমেন এবং অন্যান্য DNS এন্ট্রি পায়৷
  -[Get-ShodanDNSResolve](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSResolve) - Looks up the IP addresses for the provided hostname(s)
  -[Get-ShodanDNSReverse](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanDNSReverse) - IP ঠিকানাগুলির প্রদত্ত তালিকার জন্য সংজ্ঞায়িত হোস্টনামগুলি সন্ধান করে৷
  -[Get-ShodanExploitCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanExploitCount) - শোষণের জন্য অনুসন্ধান করে কিন্তু শুধুমাত্র অনুসন্ধান শব্দের সাথে সম্পর্কিত মোট মিলের সংখ্যা এবং ঐচ্ছিকভাবে লেখক, প্ল্যাটফর্ম, পোর্ট, উত্স বা প্রকারের বিষয়ে তথ্য প্রদান করে৷
  -[Get-ShodanHoneyScore](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHoneyScore) - Calculates a honeypot probability score ranging from 0 (not a honeypot) to 1.0 (is a honeypot)
  -[Get-ShodanHostCount](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostCount) - "/shodan/host/search" এর মোট ফলাফলের সংখ্যা প্রদান করে।
  -[Get-ShodanHostIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostIP) - আইপি ঠিকানা সহ শোডান অনুসন্ধান করুন।
  -[Get-ShodanHostSearch](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearch) - ওয়েবসাইট হিসাবে একই ক্যোয়ারী সিনট্যাক্স ব্যবহার করে Shodan অনুসন্ধান করুন এবং বিভিন্ন বৈশিষ্ট্যের জন্য সারসংক্ষেপ তথ্য পেতে দিকগুলি ব্যবহার করুন৷
  -[Get-ShodanHostSearchFacets](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFacets) - এই মডিউল সার্চ ফিল্টারগুলির একটি তালিকা প্রদান করে যা অনুসন্ধান ক্যোয়ারীতে ব্যবহার করা যেতে পারে।
  -[Get-ShodanHostSearchFilters](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanHostSearchFilters) - এই মডিউল সার্চ ফিল্টারগুলির একটি তালিকা প্রদান করে যা অনুসন্ধান ক্যোয়ারীতে ব্যবহার করা যেতে পারে।
  -[Get-ShodanPorts](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanPorts) - শোদান ইন্টারনেটে ক্রল করছে এমন সমস্ত পোর্টের তালিকা করুন।
  -[Get-ShodanProfile](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanProfile) - এই API কী এর সাথে লিঙ্কযুক্ত Shodan অ্যাকাউন্ট সম্পর্কে তথ্য প্রদান করে
  -[Get-ShodanScanID](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanID) - পূর্বে জমা দেওয়া স্ক্যান অনুরোধের অগ্রগতি পরীক্ষা করুন
  -[Get-ShodanScanProtocols](https://github.com/simeononsecurity/Shodan_PS/tree/main/Get-ShodanScanProtocols) - শোডানের মাধ্যমে অন-ডিমান্ড ইন্টারনেট স্ক্যান করার সময় ব্যবহার করা যেতে পারে এমন সমস্ত প্রোটোকলের তালিকা করুন
  -[Set-ShodanScanIP](https://github.com/simeononsecurity/Shodan_PS/tree/main/Set-ShodanScanIP)- একটি নেটওয়ার্ক ক্রল করার জন্য Shodan অনুরোধ করতে এই মডিউল ব্যবহার করুন.<a name="Download"></a> ## ডাউনলোড করুন আপনাকে আপনার কম্পিউটারে স্ক্রিপ্টগুলি ক্লোন করতে বা ডাউনলোড করতে হবে। আপনি এই রেপো পৃষ্ঠায় কোড ড্রপডাউন মেনু ব্যবহার করতে পারেন স্ক্রোল করে, অথবা নিচের লিঙ্কটি কপি এবং পেস্ট করুন:[https://github.com/simeononsecurity/Shodan_PS.git](https://github.com/simeononsecurity/Shodan_PS.git)

![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select the copy icon next to the clone url](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/download.gif?raw=true)

এই উদাহরণের জন্য আমরা গিট ব্যাশের মধ্যে রেপো ক্লোনিং করব, উপরে দেখানো ক্লিপবোর্ড আইকনে ক্লিক করার পরে, আমরা গিট ক্লোন টাইপ করতে পারি এবং ড্রপডাউন মেনু থেকে পেস্ট নির্বাচন করতে গিট ব্যাশ উইন্ডোতে ডান ক্লিক করতে পারি:

```
exampleuser@exampleComputer MINGW64 ~/Documents/Github git clone https://github.com/simeononsecurity/Shodan_PS.git
```

For detailed instructions on cloning please view [the github documentation.](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

**OR**

You can use the Code dropdown menu on this repo page by scrolling up, or just click on the following link:
[https://github.com/simeononsecurity/Shodan_PS/archive/main.zip](https://github.com/simeononsecurity/Shodan_PS/archive/main.zip)
![On the project page click the code button which opens the dropdown menu containing clone, Open with Github Desktop, Download Zip. Select Download Zip option](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/downloadzip.gif?raw=true)

Unzip main.zip by right clicking on the file and selecting extract here from the dropdown menu.

Once you have the files, you need to copy the files to C:\Program Files\WindowsPowerShell\Modules, doing this will prompt dialog saying that access is denied, click continue to finish copying the files to this location and then proceed to the installation instructions [here](#Install)

![Open file explorer path C:\Program Files\WindowsPowerShell\Modules , copy dialog says access is denied, click on continue to copy the files](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/copyasadmin.png?raw=true)

# Install

<a name="Install"></a>

To install the modules You will need to run a PowerShell window as administrator.
There are two ways of doing this:

The first way is by right clicking the PowerShell icon on the Desktop and selecting Run as Administrator from the dropdown menu.

![Right click the powershell icon on the Desktop and select run as administrator from dropdown menu](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/RcRunAsAdmin.gif?raw=true)

**OR**

By typing p (or however many characters it takes PowerShell to show up) into the search bar and clicking on Run as Administrator.

![type p in the search bar and when powershell comes up click on run as administrator](https://github.com/simeononsecurity/Shodan_PS/blob/main/demo/SearchBarRunAsAdmin.gif?raw=true)

You will need to be in the directory that you copied the scripts to.
Run the following command to change your working directory:

```
PS C:\WINDOWS\system32> cd 'C:\Program Files\WindowsPowerShell\Modules\Shodan_PS'
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS>
```

On Windows client computers we need to change the PowerShell execution policy which is Restricted by default.

For more information please read this [Microsoft documentation.](https:/go.microsoft.com/fwlink/?LinkID=135170)

Run the following command to set the policy to RemoteSigned and enter y to select that Yes you want to change the policy.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ExecutionPolicy RemoteSigned

Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the
security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to
change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): y
```

Once the execution policy has been changed, you can run the following command to Import the modules.

```
PS C:\Program Files\WindowsPowerShell\Modules\Shodan_PS> Set-ChildItem -Recurse *.psm1 | Import-Module
```

এখন আপনি পাওয়ারশেলের মাধ্যমে একটি মডিউল হিসাবে যেকোনো স্ক্রিপ্ট চালাতে পারেন।

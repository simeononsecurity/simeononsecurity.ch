---
title: "vSphere পরিচালনার জন্য PowerCLI দক্ষভাবে ব্যবহার"
date: 2023-08-02
lastmod: 2026-11-12
toc: true
draft: false
description: "PowerCLI দিয়ে VMware vSphere পরিচালনা, কাজ স্বয়ংক্রিয় করা এবং উৎপাদনশীলতা বাড়ানোর পদ্ধতি জানুন।"
genre: ["প্রযুক্তি", "ভার্চুয়ালাইজেশন", "VMware", "আইটি ব্যবস্থাপনা", "স্বয়ংক্রিয়করণ", "কমান্ড-লাইন ইন্টারফেস", "স্ক্রিপ্টিং", "সিস্টেম প্রশাসন", "ক্লাউড কম্পিউটিং", "ডেটা সেন্টার ব্যবস্থাপনা"]
tags: ["PowerCLI", "VMware PowerCLI", "PowerCLI ইনস্টলেশন", "PowerCLI ইনস্টল করুন", "PowerCLI ডাউনলোড", "PowerCLI ডাউনলোড করুন", "PowerCLI দিয়ে vCenter সংযোগ", "vSphere ব্যবস্থাপনা", "ভার্চুয়াল মেশিন ব্যবস্থাপনা", "হোস্ট ব্যবস্থাপনা", "স্বয়ংক্রিয়করণ", "স্ক্রিপ্টিং", "ভার্চুয়ালাইজেশন", "vCenter Server", "ESXi হোস্ট", "ডেটাস্টোর ব্যবস্থাপনা", "নেটওয়ার্ক অ্যাডাপ্টার ব্যবস্থাপনা", "ভার্চুয়াল মেশিন তৈরি", "ভার্চুয়াল মেশিন সরানো", "ভার্চুয়াল মেশিন সেটিংস", "হোস্ট রিসোর্স ব্যবস্থাপনা", "CPU বরাদ্দ", "মেমরি বরাদ্দ", "স্টোরেজ সেটিংস", "PowerCLI উদাহরণ", "PowerCLI নথি", "আইটি ব্যবস্থাপনা", "সিস্টেম প্রশাসন", "ক্লাউড কম্পিউটিং"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "একজন ব্যক্তি PowerCLI কমান্ড দিয়ে vSphere পরিবেশের ভার্চুয়াল মেশিন ও হোস্ট পরিচালনা করছেন, এমন একটি চিত্র।"
coverCaption: "PowerCLI দিয়ে vSphere ব্যবস্থাপনা উন্নত করুন"
---

## ভূমিকা

**PowerCLI** হলো **VMware**-এর **কমান্ড-লাইন ইন্টারফেস (CLI)** টুল। এটি প্রশাসকদের **VMware vSphere পরিবেশ পরিচালনা ও স্বয়ংক্রিয়** করতে সাহায্য করে। এর বিভিন্ন **cmdlet** প্রশাসনিক কাজ সহজ করে এবং উৎপাদনশীলতা বাড়ায়। এই নিবন্ধে PowerCLI ইনস্টল করা, vCenter-এ সংযোগ এবং এর কার্যকর ব্যবহার বর্ণনা করা হয়েছে।

______

## PowerCLI ইনস্টল করা

কম্পিউটারে PowerCLI ইনস্টল করতে:

1. VMware-এর সরকারি ওয়েবসাইট থেকে PowerCLI ইনস্টলার **ডাউনলোড** করুন। লিংকটি [PowerCLI নথিতে](https://code.vmware.com/web/dp/tool/vmware-powercli) আছে। অপারেটিং সিস্টেমের উপযুক্ত সংস্করণ নিন।
2. ইনস্টলার **চালান** এবং পর্দার নির্দেশনা অনুসরণ করুন। ইনস্টলেশনের স্থান ও বিকল্প বেছে নিন।
3. ইনস্টলেশন শেষ করতে “Finish” চাপুন। এরপর PowerCLI ব্যবহার করা যাবে।

______

## PowerCLI দিয়ে vCenter-এ সংযোগ

ইনস্টলেশনের পর vCenter সার্ভারে সংযোগ করুন, যাতে PowerCLI cmdlet দিয়ে ভার্চুয়াল অবকাঠামো পরিচালনা করা যায়।

1. Start মেনু বা ডেস্কটপ শর্টকাট থেকে PowerCLI চালু করুন।
2. vCenter-এ সংযোগ করতে এই কমান্ড চালান:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

`<vCenter IP or hostname>`-এর জায়গায় vCenter সার্ভারের প্রকৃত IP ঠিকানা বা হোস্টনাম দিন।

3. অনুরোধ এলে vCenter পরিচালনার যথেষ্ট অনুমতিসম্পন্ন অ্যাকাউন্টের পরিচয়পত্র দিন।
4. **Get-VMHost**-এর মতো সহজ কমান্ড চালিয়ে সংযোগ যাচাই করুন। ESXi হোস্টের তালিকা দেখা গেলে সংযোগ সফল হয়েছে।

______

## vSphere পরিচালনায় PowerCLI ব্যবহার

vCenter-এ সংযুক্ত হলে আপনি সাধারণ প্রশাসনিক কাজ করতে পারবেন।

### তথ্য সংগ্রহ

vSphere পরিবেশের তথ্য পেতে PowerCLI-তে একাধিক cmdlet আছে:

- **Get-VM**: ভার্চুয়াল মেশিনের তথ্য সংগ্রহ করে।
- **Get-VMHost**: ESXi হোস্টের তথ্য সংগ্রহ করে।
- **Get-Datastore**: ডেটাস্টোরের তথ্য সংগ্রহ করে।
- **Get-NetworkAdapter**: নেটওয়ার্ক অ্যাডাপ্টারের তথ্য সংগ্রহ করে।

ফলাফল ছাঁকতে ও সাজাতে পরামিতি ব্যবহার করুন।

### কাজ স্বয়ংক্রিয় করা

PowerCLI পুনরাবৃত্ত কাজ স্বয়ংক্রিয় করতে পারে। কয়েকটি কোড লাইনে একাধিক অবজেক্টে জটিল কাজ চালানো যায়।

#### একটি ফোল্ডারের সব VM-এর স্ন্যাপশট তৈরি

```PowerShell
## Power off all virtual machines on a specific host
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Take a snapshot of all virtual machines in a specific folder
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

এই স্ক্রিপ্ট দেখায় কীভাবে নির্দিষ্ট হোস্টের VM বন্ধ করে একটি ফোল্ডারের VM-গুলোর স্ন্যাপশট তৈরি করা যায়।

#### ফোল্ডারের সব VM নিরাপদে বন্ধ করা

```PowerShell
## Retrieve the folder containing the virtual machines to be shutdown
$folder = Get-Folder -Name "MyFolder"

## Retrieve all virtual machines within the specified folder
$vms = Get-VM -Location $folder

## Shutdown all virtual machines gracefully
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

স্ক্রিপ্টটি `Get-Folder` দিয়ে ফোল্ডার এবং `Get-VM` দিয়ে তার VM-গুলো খুঁজে পায়। `foreach` লুপ প্রতিটি VM পরীক্ষা করে। অবস্থা “PoweredOn” হলে `Shutdown-VMGuest` স্বাভাবিকভাবে বন্ধ করে। `-Confirm:$false` নিশ্চিতকরণ বার্তা এড়ায়। এভাবে ফোল্ডারের VM-গুলো সুশৃঙ্খলভাবে বন্ধ হয়। PowerCLI স্ক্রিপ্ট দিয়ে প্রয়োজনমতো স্বয়ংক্রিয় কর্মপ্রবাহ তৈরি করুন।

### ভার্চুয়াল মেশিন ও হোস্ট পরিচালনা

PowerCLI দিয়ে বিভিন্ন কাজ করা যায়:

- **ভার্চুয়াল মেশিন তৈরি ও সরানো**: **`New-VM`** এবং **`Remove-VM`** ব্যবহার করুন। **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** তৈরির সময় CPU, মেমরি, ডিস্ক ও নেটওয়ার্কের পরামিতি গ্রহণ করে।
- **VM সেটিং পরিবর্তন**: CPU, মেমরি, ডিস্ক ও নেটওয়ার্ক বদলান। **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** CPU ও মেমরি বরাদ্দ পরিবর্তন করে।
- **হোস্ট রিসোর্স পরিচালনা**: CPU, মেমরি, নেটওয়ার্ক ও স্টোরেজ পরিচালনা করুন। **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** হোস্টের নেটওয়ার্ক ও স্টোরেজ সেটিং পরিবর্তন করে।

এগুলো vSphere পরিচালনায় PowerCLI ব্যবহারের কয়েকটি উদাহরণ। এর বিস্তৃত cmdlet সংগ্রহ প্রশাসনিক কাজ স্বয়ংক্রিয় ও সহজ করে।

## উপসংহার

**PowerCLI** VMware vSphere পরিবেশ পরিচালনা ও স্বয়ংক্রিয় করার কার্যকর টুল। এর cmdlet প্রশাসনিক কাজ সহজ করে এবং উৎপাদনশীলতা বাড়ায়। ইনস্টল করে vCenter-এ সংযোগের পর তথ্য সংগ্রহ, কাজ স্বয়ংক্রিয়করণ এবং ভার্চুয়াল মেশিন ও হোস্ট দক্ষভাবে পরিচালনা করা যায়।

vSphere ব্যবস্থাপনা সহজ করতে PowerCLI ব্যবহার শুরু করুন।


## তথ্যসূত্র
- [PowerCLI নথি](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: VMware PowerCLI cmdlet রেফারেন্স](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: VMware PowerCLI cmdlet রেফারেন্স](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)

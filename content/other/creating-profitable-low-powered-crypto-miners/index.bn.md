---
title: "কম-পাওয়ার হার্ডওয়্যার সহ একটি লাভজনক প্যাসিভ ইনকাম বক্স তৈরি করুন: একটি গাইড"
draft: false
toc: true
date: 2023-02-07
description: "কীভাবে একটি রাস্পবেরি পাই বা ইন্টেল NUC ব্যবহার করে একটি স্বল্প-ক্ষমতাসম্পন্ন প্যাসিভ ইনকাম ক্রিপ্টো মাইনার সেট আপ করতে হয় তা শিখুন এবং এই গাইডের সাহায্যে প্রতি বক্সে প্রতি মাসে $10-$20 উপার্জন করুন"
tags: ["একটি লাভজনক প্যাসিভ ইনকাম বক্স তৈরি করুন", "নিম্ন-চালিত হার্ডওয়্যার", "প্যাসিভ আয়", "ক্রিপ্টো মাইনার", "রাস্পবেরি পাই", "ইন্টেল NUC", "গাইড", "হার্ডওয়্যার প্রয়োজনীয়তা", "ওএস ইনস্টলেশন", "সফটওয়্যার ইনস্টলেশন", "ডকার", "স্বয়ংক্রিয় ডকার কন্টেইনার আপডেট", "উবুন্টু সার্ভার", "উবুন্টু ডেস্কটপ", "রাস্পবিয়ান", "বাজেট", "ইউএসএফএফ", "ক্ষুদ্র", "মিনি", "মাইক্রো পিসি", "প্রযুক্তিগত অভিজ্ঞতা", "EarnApp", "MYST", "Peer2Profit", "হানিগেইন", "ট্রাফ মনিটাইজার", "ওয়াচটাওয়ার", "কামড়াচ্ছে", "লিনাক্স আপডেট", "উবুন্টু", "ডেবিয়ান", "CentOS", "আরএইচইএল", "অফলাইন আপডেট", "স্থানীয় সংগ্রহস্থল", "ক্যাশে", "সার্ভার সেটআপ", "ক্লায়েন্ট সেটআপ", "apt-মিরর", "debmirror", "ক্রিয়েপো", "apt-cacher-ng", "yum-cron", "লিনাক্স সিস্টেম আপডেট", "অফলাইন প্যাকেজ আপডেট", "অফলাইন সফ্টওয়্যার আপডেট", "স্থানীয় প্যাকেজ সংগ্রহস্থল", "স্থানীয় প্যাকেজ ক্যাশে", "অফলাইন লিনাক্স আপডেট", "অফলাইন আপডেট পরিচালনা করা", "অফলাইন আপডেট পদ্ধতি", "অফলাইন সিস্টেম রক্ষণাবেক্ষণ", "লিনাক্স সার্ভার আপডেট", "লিনাক্স ক্লায়েন্ট আপডেট", "অফলাইন সফ্টওয়্যার পরিচালনা", "অফলাইন প্যাকেজ ব্যবস্থাপনা", "কৌশল আপডেট করুন", "লিনাক্স নিরাপত্তা আপডেট"]
cover: "/img/cover/A_green_circuit_board_shaped_like_a_box_with_internet.png"
coverAlt: "একটি সবুজ, সার্কিট বোর্ড একটি বাক্সের মতো আকৃতির যার সাথে ইন্টারনেট সংযোগের চিহ্ন যুক্ত তারের সাথে সংযুক্ত।"
coverCaption: ""
---

**লো-পাওয়ার হার্ডওয়্যার সহ একটি লাভজনক প্যাসিভ ইনকাম বক্স তৈরি করুন: একটি নির্দেশিকা**
আজকাল অনেক লোক ক্রিপ্টো মাইনিং এবং হিলিয়াম মাইনারদের মতো স্বল্প শক্তির খনি শ্রমিকদের মধ্যে রয়েছে। এগুলি দুর্দান্ত এবং সমস্ত কিন্তু তারা আর এত বেশি উপার্জন করে না এবং তারা এক ধরণের উপার্জনের দিকে মনোনিবেশ করে। আজ আমরা একটি স্বল্প ক্ষমতা সম্পন্ন প্যাসিভ ইনকাম বক্স তৈরি করতে যাচ্ছি যেটি প্রতি বক্স এবং আবাসিক আইপি প্রতি মাসে $10-$20 থেকে আয় করে।

*আপনার যদি এই বাক্সটিকে একটি গেস্ট নেটওয়ার্কে সেট আপ করার ক্ষমতা থাকে বা, আরও ভালোভাবে, একটি আলাদা VLAN, তাহলে তা করুন৷ যদিও এটি একটি নিরাপত্তা ব্লগ, আমরা প্রত্যেকের নিরাপত্তা উদ্বেগ এবং ঝুঁকি সহনশীলতা অনুমান করতে পারি না।*

## হার্ডওয়্যার প্রয়োজনীয়তা:
নিম্নলিখিতগুলির মধ্যে একটি প্রয়োজন। আমাদের মূলত দরকার যে কোনো দক্ষ এবং কম শক্তিসম্পন্ন কম্পিউটার যা আমরা হাতে পেতে পারি। যেকোন রাস্পবেরি PI, Intel NUC, বা অনুরূপ করবে। তাদের এত শক্তিশালী হতে হবে না। তবে আমি আপনাকে কমপক্ষে 32g-64g স্টোরেজ, 4g RAM এবং কমপক্ষে 2টি সিপিইউ থ্রেড রাখার পরামর্শ দেব। এর জন্য আমরা হার্ডওয়্যারের জন্য প্রায় $100-$200 বাজেটের লক্ষ্য রাখব তবে এটি আপনার প্রয়োজন অনুসারে বেশি হলে নির্দ্বিধায়। আমাদের পাওয়ার টার্গেট প্রায়। 25w গড়।
### রাস্পবেরি পাই:
এই দিনগুলি ধরে রাখা কঠিন তবে এগুলি খুব কম শক্তি এবং বেশ কাস্টমাইজযোগ্য। আপনার রাস্পবেরি PI তে কীভাবে রাস্পিয়ান ইনস্টল করবেন সে সম্পর্কে তথ্যের জন্য
- [Raspberry Pi 4B Model B DIY Kit](https://amzn.to/3x72kv0)
- [GeeekPi Raspberry Pi 4 4GB Starter Kit](https://amzn.to/3jG2g2k)
- [GeeekPi Raspberry Pi 4 8GB Starter Kit](https://amzn.to/3DQisF6)
### Intel Nuc:
সেখানে মডেলের বিস্তৃত বৈচিত্র্য. একটি নতুন চয়ন করতে দ্বিধা বোধ করুন.
- [Intel NUC 12 Pro](https://amzn.to/3JTzLc7)
- [Intel NUC 8](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+8)
- [Intel NUC 6](https://www.ebay.com/sch/i.html?_nkw=intel+nuc+6)
### যেকোনো USFF/Tiny/Mini/Micro PC:
- [Lenovo ThinkCentre M900 Tiny](https://www.ebay.com/itm/385116504642)
- [Dell OptiPlex 7040 Micro USFF](https://www.ebay.com/itm/165504038978)
### Intel N5100 বা অনুরূপ যেকোন মিনি পিসি
সুপার কম পাওয়ারের জন্য রাস্পবেরি পাই সমতুল্য কিন্তু x64 প্ল্যাটফর্মে।
- [Beelink U59 Mini PC ](https://amzn.to/3YkFhcj)
- [TRIGKEY Mini Computer](https://amzn.to/3XkbXkS)

## OS ইনস্টলেশন:
আমরা এখানে কীভাবে একটি অপারেটিং সিস্টেম ইনস্টল করতে হয় তার প্রযুক্তিগত বিবরণে যাব না। তবে আপনাকে শুরু করার জন্য এখানে কিছু দুর্দান্ত সংস্থান রয়েছে
### রাস্পবিয়ান:
- [Getting started](https://www.raspberrypi.com/documentation/computers/getting-started.html)
- [The New Method to Setup Raspberry Pi](https://www.youtube.com/watch?v=jRKgEXiMtns)
### উবুন্টু:
- [Install Ubuntu desktop](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview)
- [Ubuntu Server - Basic installation](https://ubuntu.com/server/docs/installation)
- [Ubuntu Complete Beginner's Guide: Download & Installing Ubuntu](https://www.youtube.com/watch?v=W-RFY4LQ6oE)


## সফটওয়্যার ইনস্টলেশন:
এটি একটি দীর্ঘ অধ্যায় হতে যাচ্ছে. আমরা ডকার সেট আপ করতে যাচ্ছি এবং তারপর ডকারের মাধ্যমে আমরা স্বয়ংক্রিয় ডকার কন্টেইনার আপডেট সেট আপ করব এবং একাধিক ডকার কন্টেইনার ইনস্টল করব। আমরা ধরে নিই যে আপনি উবুন্টু সার্ভার ব্যবহার করছেন, তবে উবুন্টু সার্ভার, উবুন্টু ডেস্কটপ এবং রাস্পবিয়ানের জন্য কমান্ডগুলি একই হওয়া উচিত।

*এই বিভাগের জন্য আমরা কিছু মৌলিক প্রযুক্তিগত অভিজ্ঞতা অনুমান করি এবং আপনি ইতিমধ্যেই আপনার অপারেটিং সিস্টেম ইনস্টল করেছেন এবং সেইসাথে কিভাবে টার্মিনালে যেতে হয় তাও জানেন।*

### আপডেট ইনস্টল করা হচ্ছে:
আমরা প্রথমে নিশ্চিত হতে চাই যে আমাদের সিস্টেম সম্পূর্ণ আপ টু ডেট আছে:
```bash
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove -y
```

### ডকার ইনস্টল করা হচ্ছে:
আমাদের যেকোন বিদ্যমান সংস্করণ আনইনস্টল করতে হবে যা OS এর সাথে প্রিপ্যাকেজ করা হয় এবং ডকারের রেপো থেকে সর্বশেষ ইনস্টল করতে হবে।
```bash
sudo apt-get remove -y docker docker-engine docker.io containerd runc
sudo apt-get update
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### ওয়াচটাওয়ার ইনস্টল করুন:
এই ডকার কন্টেইনারটি আপনার সমস্ত ডকার কন্টেইনারকে নিয়মিত ব্যবধানে সর্বশেষ চিত্রগুলিতে স্বয়ংক্রিয়ভাবে আপডেট করে এবং পুরানো (বাসি) ছবিগুলি পরিষ্কার করে।
```bash
docker run -d \
    --name watchtower \
    --restart unless-stopped \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower -c \
    --schedule "0 0 2 * * *" \
    --cleanup 
```

### বিটপিং ইনস্টল করুন:
[*Bitping is a website monitoring and performance optimization solution that provides real-time, real user monitoring and instant feedback on downtime or degraded performance, with stress testing and benchmarking capabilities, dynamic rerouting and reprovisioning powered by a distributed network intelligence layer, and integration with existing workflows through webhooks.*](https://bitping.com)

বিটপিং আপনাকে আপনার নেটওয়ার্ক থেকে লাইটওয়েট নেটওয়ার্ক পরীক্ষা চালানোর জন্য ব্যবসার জন্য একটি নোড প্রদান করার জন্য সোলানাতে অর্থপ্রদান করার ক্ষমতা প্রদান করে।
এটি নোড প্রতি দিনে গড়ে প্রায় 0.1 সেন্ট। আমি অনেক কিছু জানি না, তবে এটির সম্ভাবনা রয়েছে এবং পেআউটগুলি সহজ।

#### একটি অ্যাকাউন্ট তৈরি করুন:
এ একটি অ্যাকাউন্ট তৈরি করুন [bitping.com](https://bitping.com)

#### ডকার কন্টেইনার ইনস্টল করুন:
ধাপ 1. প্রথমে এই কমান্ডগুলি চালান যখন এটি আপনাকে আপনার কন্টেইনার সেট আপ করার মাধ্যমে নিয়ে যায় এবং আপনাকে সাইন ইন করতে বলে৷
```bash
docker pull bitping/bitping-node
mkdir $HOME/.bitping/
docker run -it --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```

আপনার বিটপিং অ্যাকাউন্ট দিয়ে সাইন ইন করার পরে কন্টেইনার থেকে বাঁচতে আপনার কীবোর্ডে CTRL+C টিপুন।

ধাপ 2. ব্যাকগ্রাউন্ডে কন্টেইনারটি ধরে রাখতে এই কমান্ডটি চালান
```bash
docker run --net host --name bitping -td --mount type=bind,source="$HOME/.bitping/",target=/root/.bitping bitping/bitping-node:latest
```


### Earn অ্যাপ ইনস্টল করুন:
[*Take advantage of the time your devices are left idle by getting paid for your device’s unused resources*](https://earnapp.com/i/c1dllee)

Earn অ্যাপ আপনাকে আশ্চর্যজনক পরিমাণ পুরস্কারের জন্য VPN পরিষেবা হিসেবে আপনার ইন্টারনেট শেয়ার করতে দেয়। আবাসিক আইপি প্রতি নোড প্রতি গড় প্রায় $5 মাস। পেপ্যাল এবং অ্যামাজন উপহার কার্ডের মাধ্যমে অর্থ প্রদানের প্রস্তাব দেয়।

#### একটি আর্ন অ্যাপ অ্যাকাউন্ট তৈরি করুন:
এ একটি অ্যাকাউন্ট তৈরি করুন [earnapp.com](https://earnapp.com/i/c1dllee)
*সতর্কতা, একটি গুগল অ্যাকাউন্ট প্রয়োজন*

#### আপনার UUID পেতে অ্যাপটির নন ডকার সংস্করণ ইনস্টল করুন:
আপনি আপনার UUID পাওয়ার পরে আনইনস্টল করতে ভুলবেন না অন্যথায় আপনি একই হোস্টে এবং স্বয়ংক্রিয় আপডেট ছাড়াই এটি দুবার চালাতে পারবেন
- [Instructions](https://help.earnapp.com/hc/en-us/articles/10261224561553-Installation-instructions)

#### ডকার কন্টেইনার ইনস্টল করুন:
আপনার টার্মিনালে আটকানোর আগে স্ট্রিং পরিবর্তন করুন। আপনাকে আপনার উপার্জন অ্যাপ UUID উল্লেখ করতে হবে।
```bash
mkdir $HOME/earnapp-data
docker run -td --name earnapp --privileged -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v $HOME/earnapp-data:/etc/earnapp -e "EARNAPP_UUID"="" -e 'PUID'='99' -e 'PGID'='100' --name earnapp fazalfarhan01/earnapp:lite 
```
#### চলচ্চিত্র মাধ্যমে শিক্ষা:
{{< youtube id="tt499o0OjGU" >}}

### মধু লাভ ইনস্টল করুন:
[*Passive Income – Effortlessly with Honeygain, you can make money by simply sharing your Internet. Start earning now.*](https://r.honeygain.me/DAVID07A75)

হানি গেইন আপনাকে আশ্চর্যজনক পরিমাণ পুরষ্কারের জন্য একটি VPN পরিষেবা হিসাবে আপনার ইন্টারনেট ভাগ করতে দেয়৷ আবাসিক আইপি প্রতি নোড প্রতি গড় প্রায় $5 মাস। পেআউট জটিল হতে পারে. এই ধারকটি ব্যবহার করার সিদ্ধান্ত নেওয়ার আগে এটি আরও পড়ুন

#### একটি মধু লাভ অ্যাকাউন্ট তৈরি করুন:
এ একটি অ্যাকাউন্ট তৈরি করুন [honeygain.com](https://r.honeygain.me/DAVID07A75)

#### ডকার কন্টেইনার ইনস্টল করুন:
টার্মিনালে আটকানোর আগে স্পষ্ট ইমেল, পাসওয়ার্ড এবং ডিভাইসের নাম দিয়ে স্ট্রিংটি পরিবর্তন করুন
```bash
docker run --name honeygain -td honeygain/honeygain -tou-accept -email ACCOUNT_EMAIL -pass ACCOUNT_PASSWORD -device DEVICE_NAME
```

#### রাস্পবেরি পাই এর জন্য বিকল্প নির্দেশাবলী
- [How to install Honeygain on a Raspberry Pi with standard Raspberry Pi OS](https://www.reddit.com/r/Honeygain/comments/tj8vfa/how_to_install_honeygain_on_a_raspberry_pi_with/)

#### চলচ্চিত্র মাধ্যমে শিক্ষা:
{{< youtube id="Wd11M0nSy1k" >}}

### PawnsApp ইনস্টল করুন:
[*Make passive money online by completing surveys and sharing your internet *](https://pawns.app/?r=2092882)
Pawns অ্যাপ, আবার এখানে তালিকাভুক্ত অন্যদের মতোই আপনার ইন্টারনেট শেয়ার করার জন্য আপনাকে অর্থ প্রদানের প্রস্তাব দেয়। সর্বনিম্ন পেআউট হল $5। আইপি প্রতি নোড প্রতি মাসে গড় পেআউট হল $0.50।

#### একটি PawnsApp অ্যাকাউন্ট তৈরি করুন:
এ একটি অ্যাকাউন্ট তৈরি করুন [https://pawns.app](https://pawns.app/?r=2092882)

#### ডকার কন্টেইনার ইনস্টল করুন:

আপনার টার্মিনালে অনুলিপি করার আগে আপনার ইমেল, পাসওয়ার্ড, ডিভাইসের নাম এবং ডিভাইস আইডি দিয়ে নিম্নলিখিত পরিবর্তন করুন।
```bash
docker pull iproyal/pawns-cli:latest
docker run -td --name pawnsapp --restart=on-failure:5 iproyal/pawns-cli:latest -email=email@example.com -password=change_me -device-name=raspberrypi -device-id=raspberrypi1 -accept-tos
```

### ইনস্টল করুন পিয়ার 2 লাভ:
[*SHARE YOUR TRAFFIC AND PROFIT ON IT!*](https://t.me/peer2profit_app_bot?start=16538445386293aa3aaec4e)

EarnApp এবং HoneyGain এর মতো, Peer2Profit আপনার ইন্টারনেট VPN এবং স্ক্র্যাপিংয়ের উদ্দেশ্যে শেয়ার করে। প্রতি আইপি প্রতি নোড প্রতি মাসে প্রায় $1 উপার্জন করে।
মানি অর্ডার, BTC, LTC, LTC, MATIC, ইত্যাদি সহ বিভিন্ন ধরনের পেআউট অফার করে।

#### একটি পিয়ার 2 লাভ অ্যাকাউন্ট তৈরি করুন:
এ একটি অ্যাকাউন্ট তৈরি করুন [peer2profit.com](https://t.me/peer2profit_app_bot?start=16538445386293aa3aaec4e)

#### ডকার কন্টেইনার ইনস্টল করুন:
```bash
export P2P_EMAIL="your_email_without_quotes"; 
docker rm -f peer2profit || true && docker run -td --restart always \
        -e P2P_EMAIL=$P2P_EMAIL \
        --name peer2profit \
        peer2profit/peer2profit_linux:latest 
```
#### চলচ্চিত্র মাধ্যমে শিক্ষা:
{{< youtube id="J_rSV5N8aQk" >}}


### রিপকেট ইনস্টল করুন:
[*Get Paid For Your Unused Internet*](https://link.repocket.co/raqc)

এখানে অন্যান্য অফার অনুরূপ. সর্বনিম্ন $20 পেআউট। পেআউট জটিল হতে পারে. আপনি এই পরিষেবাটি ব্যবহার করতে চান কিনা তা দেখতে নিজের জন্য গবেষণা করুন। প্রতি মাসে প্রতি বক্স প্রতি নোডের গড় প্রায় $1 পেআউট।

#### একটি রিপকেট অ্যাকাউন্ট তৈরি করুন:
এ একটি অ্যাকাউন্ট তৈরি করুন [repocket.co](https://link.repocket.co/raqc) এবং আপনার ড্যাশবোর্ড থেকে আপনার api কী ধরুন।
#### ডকার কন্টেইনার ইনস্টল করুন:
আপনার টার্মিনালে পেস্ট করার আগে আপনার ইমেল এবং api কী দিয়ে নিম্নলিখিত লাইনটি পরিবর্তন করুন।
```bash
docker run -td --name repocket -e RP_EMAIL=your@email.com -e RP_API_KEY=yourapikey -d --restart=always repocket/repocket
```
#### চলচ্চিত্র মাধ্যমে শিক্ষা:
{{< youtube id="171gWknfAbY" >}}

### ট্র্যাফ মনিটাইজার ইনস্টল করুন:
[*Share your internet connection and make money online*](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)

EarnApp এবং HoneyGain এর মতো, TraffMonetizer আপনাকে আপনার ইন্টারনেট শেয়ার করার জন্য অর্থ প্রদান করে। প্রতি আইপি প্রতি নোড প্রতি মাসে গড়ে প্রায় $2। শুধুমাত্র BTC-তে পেআউট অফার করে।

#### আপনার ট্র্যাফ মনিটাইজার অ্যাকাউন্ট তৈরি করুন:
এ আপনার অ্যাকাউন্ট তৈরি করুন [https://traffmonetizer.com](https://traffmonetizer.com/?aff=1389828&utm_source=traffmonetizerdockerguide)
একবার আপনি ড্যাশবোর্ডে প্রবেশ করলে, আপনার অ্যাপ্লিকেশন টোকেনটি নোট করুন।

#### ডকার কন্টেইনার ইনস্টল করুন:
নিম্নলিখিত স্ট্রিংটি অনুলিপি করুন এবং আপনার টার্মিনালে আটকানোর আগে আপনার ড্যাশবোর্ড থেকে যে টোকেনটি পেয়েছেন তা যুক্ত করুন।

```bash
docker run -td --name traffmonetizer traffmonetizer/cli start accept --token
```

### মিস্টেরিয়াম ইনস্টল করুন:
[Mysterium](https://www.mysterium.network/) ইথেরিয়াম এবং পলিগন ব্লকচেইনের উপর নির্মিত একটি বিকেন্দ্রীকৃত VPN এবং ওয়েবস্ক্র্যাপিং পরিষেবা।
প্রতি IP প্রতি নোডের একাধিক কারণের উপর নির্ভর করে প্রতি মাসে $1-$20 থেকে যেকোনো জায়গায় অর্থপ্রদানের গড়। সক্রিয়করণের জন্য একটি নোড সেটআপ করতে $1.XX খরচ হয়৷ MYST টোকেনে পেআউট।


#### ডকার কন্টেইনার ইনস্টল করুন:
```bash
docker volume create myst_data
docker run -td --cpus=1 --dns 8.8.8.8 --dns 8.8.4.4 --dns 1.1.1.1 --dns 1.0.0.1 --dns 9.9.9.9 --hostname myst --cap-add NET_ADMIN --network=host -p 4449:4449 -p 59850-60000:59850-60000 --name myst --device=/dev/net/tun  -v myst_data:/var/lib/mysterium-node mysteriumnetwork/myst:latest --udp.ports=59850:60000 service --agreed-terms-and-conditions
ufw allow 4449
ufw allow 59850:60000/tcp
```

#### ডকার কন্টেইনার সেটআপ করুন:
আপনার নোডের IP ঠিকানা দিয়ে "nodeip" প্রতিস্থাপন করে http://"nodeip"/#/dashboard-এ যান। আপনি টার্মিনালে "ifconfig" টাইপ করে এটি খুঁজে পেতে পারেন।

"স্টার্ট নোড সেটআপ" এ ক্লিক করুন।

আপনি যে ERC20 ওয়ালেটে পুরষ্কার পেতে চান তার ঠিকানাটি পাস করুন এবং "পরবর্তী" ক্লিক করুন। আপনি আপনার মেটামাস্ক ঠিকানাগুলির মতো একটি স্ট্যান্ডার্ড ইথেরিয়াম ঠিকানা ব্যবহার করতে পারেন।

একটি পাসওয়ার্ড টাইপ করুন যা আপনি ভবিষ্যতে এই নোড ড্যাশবোর্ড অ্যাক্সেস করতে ব্যবহার করবেন। আপনার নেটওয়ার্কে নোড দাবি করতে চেকবক্স চেক করুন।

"এটি এখানে পান" লিঙ্কে ক্লিক করুন এবং আপনার API কী খুঁজুন। কপি করুন। ফিরে যান এবং পেস্ট করুন। "সংরক্ষণ করুন এবং চালিয়ে যান" এ ক্লিক করুন।

#### পোর্ট ফরওয়ার্ডিং:
প্রত্যেকের নির্দিষ্ট হার্ডওয়্যারের জন্য কীভাবে পোর্ট ফরওয়ার্ড করা যায় তা আমরা বর্ণনা করতে পারি না। কিভাবে পোর্ট ফরওয়ার্ড করতে হয় তা শেখার জন্য এখানে কিছু সম্পদ রয়েছে।
- [PortForward.com](https://portforward.com/)
- [Mysterium - Port Forwarding](https://docs.mysterium.network/troubleshooting/port-forwarding)


### অটো রিস্টার্ট ডকার কন্টেইনার বুটে:
```bash
sudo docker update --restart unless-stopped $(docker ps -q)
```

### ঐচ্ছিক কনফিগারেশন:
- [Automatic Ubuntu Updates and Reboots](https://www.cyberciti.biz/faq/set-up-automatic-unattended-updates-for-ubuntu-20-04/)
- [Blocking ToR Traffic on Ubuntu](https://serverfault.com/questions/1106645/blocking-tor-traffic-with-postfix-or-fail2ban-on-mailserver)
#### ম্যালওয়্যার এবং ট্র্যাকার ব্লক করে নিরাপত্তা বাড়ান।
ক্লাউডফ্লেয়ার ম্যালওয়্যার এবং ট্র্যাকিং সুরক্ষা ডিএনএসে সমস্ত ডিএনএস অনুরোধগুলিকে বল করুন৷
এছাড়াও, DNS/HTTPS অনুরোধ ব্লক করুন।
*আপনার যদি নেটওয়ার্কে রাউটার বা ফায়ারওয়াল আরও উন্নত থাকে তবে আপনি পরিচিত খারাপ অভিনয় আইপি, টর অ্যাক্সেস, টরেন্ট, সাধারণভাবে p2p ট্র্যাফিক ইত্যাদি ব্লক করার জন্য আরও উন্নত নিয়ম তৈরি করতে snort/securita-এর মতো প্যাকেজ ব্যবহার করতে পারেন। প্রস্তাবিত কিন্তু প্রয়োজনীয় নয়।*
```bash
# Allow ssh still
sudo ufw allow 22
# Allow dns out
sudo ufw allow out 53/tcp
sudo ufw allow out 53/udp
# Redirect all dns back to 1.1.1.2 or 1.0.0.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.0.0.2 -j DNAT --to-destination 1.1.1.2
sudo iptables -t nat -A OUTPUT -p udp --dport 53 ! -d 1.1.1.2 -j DNAT --to-destination 1.0.0.2
# Block DNS over HTTPS
sudo ufw deny out 853/tcp
sudo ufw deny out 853/udp 
iptables -A FORWARD -m string --string "get_peers" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "announce_peer" --algo bm -j LOGDROP
iptables -A FORWARD -m string --string "find_node" --algo bm -j LOGDROP
# Block Default ToR Ports
sudo ufw deny out 9050/tcp
sudo ufw deny out 9050/udp
sudo ufw deny out 9051/tcp
sudo ufw deny out 9051/udp
# Block Torrents
sudo ufw deny out 6881/tcp
sudo ufw deny out 6881/udp
sudo ufw deny out 6882-6999/tcp
sudo ufw deny out 6882-6999/udp
iptables -A FORWARD -m string --algo bm --string "BitTorrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "BitTorrent protocol" -j DROP
iptables -A FORWARD -m string --algo bm --string "peer_id=" -j DROP
iptables -A FORWARD -m string --algo bm --string ".torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce.php?passkey=" -j DROP
iptables -A FORWARD -m string --algo bm --string "torrent" -j DROP
iptables -A FORWARD -m string --algo bm --string "announce" -j DROP
iptables -A FORWARD -m string --algo bm --string "info_hash" -j DROP
# Save the Changes and Enable the Firewall
sudo iptables-save
sudo ufw enable
```
আরও উন্নত ToR ব্লক করার জন্য আপনি নিম্নলিখিতগুলি করতে পারেন:
```bash
#https://gist.github.com/jkullick/62695266273608a968d0d7d03a2c4185
sudo apt-get -y install ipset
ipset create tor iphash
curl -sSL "https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=$(curl icanhazip.com)" | sed '/^#/d' | while read IP; do
  ipset -q -A tor $IP
done
iptables -A INPUT -m set --match-set tor src -j DROP
```

## লাভ?
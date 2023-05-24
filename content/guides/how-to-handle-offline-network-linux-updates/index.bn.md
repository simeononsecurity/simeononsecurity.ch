---
title: "আলটিমেট গাইড: উবুন্টু ডেবিয়ান এবং CentOS RHEL এর জন্য অফলাইন লিনাক্স আপডেট"
date: 2023-05-30
toc: true
draft: false
description: "Discover the best methods for handling offline Linux updates on Ubuntu/Debian and CentOS/RHEL systems, using local repositories or caches."
tags: ["লিনাক্স আপডেট", "উবুন্টু", "ডেবিয়ান", "CentOS", "আরএইচইএল", "অফলাইন আপডেট", "স্থানীয় সংগ্রহস্থল", "ক্যাশে", "সার্ভার সেটআপ", "ক্লায়েন্ট সেটআপ", "apt-মিরর", "debmirror", "ক্রিয়েপো", "apt-cacher-ng", "yum-cron", "লিনাক্স সিস্টেম আপডেট", "অফলাইন প্যাকেজ আপডেট", "অফলাইন সফ্টওয়্যার আপডেট", "স্থানীয় প্যাকেজ সংগ্রহস্থল", "স্থানীয় প্যাকেজ ক্যাশে", "অফলাইন লিনাক্স আপডেট", "অফলাইন আপডেট পরিচালনা করা", "অফলাইন আপডেট পদ্ধতি", "অফলাইন সিস্টেম রক্ষণাবেক্ষণ", "লিনাক্স সার্ভার আপডেট", "লিনাক্স ক্লায়েন্ট আপডেট", "অফলাইন সফ্টওয়্যার পরিচালনা", "অফলাইন প্যাকেজ ব্যবস্থাপনা", "কৌশল আপডেট করুন", "লিনাক্স নিরাপত্তা আপডেট"]
cover: "/img/cover/A_cartoon_illustration_depicting_a_server_and_multiple_clients.png"
coverAlt: "একটি কার্টুন চিত্র একটি সার্ভার এবং একাধিক ক্লায়েন্ট ডিভাইস অফলাইনে আপডেট আদান প্রদান করে।"
coverCaption: ""
---

**উবুন্টু/ডেবিয়ান এবং সেন্টোস/আরএইচইএলের জন্য অফলাইনে লিনাক্স আপডেটগুলি ইনস্টল পরিচালনা করার সেরা উপায়**

আপনার সিস্টেমের নিরাপত্তা এবং স্থিতিশীলতা বজায় রাখার জন্য Linux আপডেটগুলি অপরিহার্য। যাইহোক, কিছু পরিস্থিতিতে, আপনাকে অফলাইন পরিবেশের সাথে মোকাবিলা করতে হতে পারে যেখানে ইন্টারনেট সংযোগ সীমিত বা অস্তিত্বহীন। এই ধরনের ক্ষেত্রে, অফলাইনে আপডেটগুলি ইনস্টল করার জন্য একটি সঠিক কৌশল থাকা অত্যন্ত গুরুত্বপূর্ণ হয়ে ওঠে। এই নিবন্ধটি আপনাকে **উবুন্টু/ডেবিয়ান এবং CentOS/RHEL** এর জন্য অফলাইন পরিবেশে লিনাক্স আপডেটগুলি ইনস্টল করার সর্বোত্তম উপায়গুলি পরিচালনা করবে, বিশেষ করে স্থানীয় সংগ্রহস্থল বা ক্যাশে ব্যবহার করার উপর ফোকাস করে।

## একটি স্থানীয় সংগ্রহস্থল সেট আপ করা

অফলাইন আপডেটগুলি পরিচালনা করার সবচেয়ে কার্যকর উপায়গুলির মধ্যে একটি হল স্থানীয় সংগ্রহস্থল সেট আপ করা। একটি স্থানীয় সংগ্রহস্থলে সমস্ত প্রয়োজনীয় সফ্টওয়্যার প্যাকেজ এবং আপডেট থাকে, যা আপনাকে ইন্টারনেট সংযোগ ছাড়াই আপনার সিস্টেম আপডেট করতে দেয়। এখানে আপনি কিভাবে ডেবিয়ান-ভিত্তিক এবং Red Hat-ভিত্তিক বিতরণ উভয়ের জন্য একটি স্থানীয় সংগ্রহস্থল সেট আপ করতে পারেন:

### ডেবিয়ান/উবুন্টুর জন্য

1. ইন্টারনেট অ্যাক্সেস আছে এমন একটি সার্ভারে একটি **ডেবিয়ান রিপোজিটরি মিরর** সেট আপ করে শুরু করুন৷ আপনি যেমন সরঞ্জাম ব্যবহার করতে পারেন [`apt-mirror`](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html) or [`debmirror`](https://wiki.debian.org/debmirror) অফিসিয়াল ডেবিয়ান বা উবুন্টু সংগ্রহস্থলগুলির একটি স্থানীয় আয়না তৈরি করতে।

#### apt-মিরর সহ একটি ডেবিয়ান রিপোজিটরি মিরর সেট আপ করা:

```shell
# Install apt-mirror
sudo apt-get install apt-mirror

# Edit the apt-mirror configuration file
sudo nano /etc/apt/mirror.list

# Uncomment the deb line for the desired repository
# For example, uncomment the line for Ubuntu 20.04:
# deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse

# Specify the mirror location
# Modify the base_path to your desired location
set base_path /path/to/mirror

# Save and close the file

# Run apt-mirror to start the mirroring process
sudo apt-mirror

# Wait for the mirroring process to complete
```

#### ডেবমিরর সহ একটি ডেবিয়ান রিপোজিটরি মিরর সেট আপ করা:
```shell
# Install debmirror
sudo apt-get install debmirror

# Create a directory to store the mirror
sudo mkdir /path/to/mirror

# Run debmirror to start the mirroring process
# Replace <RELEASE> with the Debian or Ubuntu release and <MIRROR_URL> with the official repository URL
# For example, to mirror Ubuntu 20.04:
sudo debmirror --arch=amd64 --verbose --method=http --dist=<RELEASE> --root=<MIRROR_URL> /path/to/mirror

# Wait for the mirroring process to complete
```
#### ডেবিয়ান ক্লায়েন্ট নির্দেশাবলী

2. ** সম্পাদনা করে আপনার স্থানীয় সংগ্রহস্থল কনফিগার করুন`/etc/apt/sources.list` অফলাইন সিস্টেমে ফাইল। স্থানীয় সংগ্রহস্থলের URL দিয়ে ডিফল্ট সংগ্রহস্থলের URLগুলি প্রতিস্থাপন করুন। উদাহরণস্বরূপ, যদি আপনার স্থানীয় সংগ্রহস্থল এ হোস্ট করা হয় `http://local-repo/ubuntu` আপডেট করুন `sources.list` সেই অনুযায়ী ফাইল করুন।

উদাহরণ `/etc/apt/sources.list` ফাইল:
```
deb http://local-repo/ubuntu focal main restricted universe multiverse
```

3. কনফিগারেশন আপডেট হয়ে গেলে, আপনি ** চালাতে পারেন`apt update` স্থানীয় সংগ্রহস্থল থেকে প্যাকেজ তালিকা আনার জন্য অফলাইন সিস্টেমে কমান্ড দিন।

```shell
sudo apt update
```

4. অবশেষে, আপনি ** ব্যবহার করতে পারেন`apt upgrade` স্থানীয় সংগ্রহস্থল থেকে উপলব্ধ আপডেটগুলি ইনস্টল করার জন্য কমান্ড।

```shell
sudo apt upgrade
```

### CentOS/RHEL এর জন্য

1. CentOS/RHEL-এর জন্য একটি স্থানীয় সংগ্রহস্থল সেট আপ করতে, আপনাকে ব্যবহার করতে হবে [**`createrepo`**](https://linux.die.net/man/8/createrepo) টুল. এই টুলটি একটি স্থানীয় সংগ্রহস্থলের জন্য প্রয়োজনীয় মেটাডেটা তৈরি করে।

2. ইন্টারনেট অ্যাক্সেস সহ একটি সার্ভারে সংগ্রহস্থলের ফাইলগুলি সংরক্ষণ করার জন্য একটি ডিরেক্টরি তৈরি করুন৷ উদাহরণস্বরূপ, আপনি ** নামে একটি ডিরেক্টরি তৈরি করতে পারেন`local-repo`

3. সমস্ত প্রাসঙ্গিক RPM প্যাকেজ ফাইল এবং আপডেট কপি করুন **`local-repo` ডিরেক্টরি

#### createrepo দিয়ে একটি স্থানীয় সংগ্রহস্থল সেট আপ করা:

```shell
# Install the createrepo tool
sudo yum install createrepo

# Create a directory to store the repository files
sudo mkdir /path/to/local-repo

# Move or copy the RPM package files and updates to the local-repo directory

# Run the createrepo command to generate the necessary repository metadata
sudo createrepo /path/to/local-repo

# Update the repository metadata whenever new packages are added or removed
sudo createrepo --update /path/to/local-repo
```
4. একবার সংগ্রহস্থলের মেটাডেটা তৈরি হয়ে গেলে, আপনি সম্পূর্ণ স্থানান্তর করতে পারেন `local-repo` একটি USB ড্রাইভ বা অন্য কোনো উপায় ব্যবহার করে অফলাইন সিস্টেমে ডিরেক্টরি।

5. অফলাইন সিস্টেমে, একটি নতুন তৈরি করুন৷ `.repo` ফাইল `/etc/yum.repos.d/` ডিরেক্টরি প্রয়োজনীয় কনফিগারেশন বিবরণ প্রদান করুন, যেমন `baseurl` স্থানীয় সংগ্রহস্থল ডিরেক্টরি নির্দেশ করে।

উদাহরণস্বরূপ, নামক একটি ফাইল তৈরি করুন `local.repo` মধ্যে `/etc/yum.repos.d/` ডিরেক্টরি এবং নিম্নলিখিত বিষয়বস্তু যোগ করুন:
```shell
sudo nano /etc/yum.repos.d/local.repo
```
```toml
[local]
name=Local Repository
baseurl=file:///path/to/local-repo
enabled=1
gpgcheck=0
```
6. ফাইলটি সংরক্ষণ করুন এবং সম্পাদক থেকে প্রস্থান করুন।

7. সংগ্রহস্থল কনফিগার করার পরে, আপনি স্থানীয় সংগ্রহস্থল থেকে আপডেট ইনস্টল করতে yum update কমান্ড ব্যবহার করতে পারেন।

```shell
sudo yum update
```

এই কমান্ড স্থানীয় সংগ্রহস্থল থেকে প্যাকেজ ব্যবহার করে সিস্টেমে প্যাকেজ আপডেট করবে।

চালানোর মাধ্যমে স্থানীয় সংগ্রহস্থল আপডেট করতে মনে রাখবেন `createrepo` কমান্ড যখনই সংগ্রহস্থল থেকে নতুন প্যাকেজ যোগ বা সরানো হয়।

দয়া করে মনে রাখবেন যে আপনাকে প্রতিস্থাপন করতে হবে `/path/to/local-repo` ডিরেক্টরির প্রকৃত পথের সাথে যেখানে আপনি সংগ্রহস্থলের ফাইলগুলি সংরক্ষণ করেছেন।

## একটি স্থানীয় ক্যাশে সেট আপ করা হচ্ছে

অফলাইন আপডেটগুলি পরিচালনা করার আরেকটি পদ্ধতি হল একটি স্থানীয় ক্যাশে সেট আপ করা। একটি স্থানীয় ক্যাশে ডাউনলোড করা প্যাকেজ এবং আপডেটগুলি সঞ্চয় করে, আপনাকে পৃথক ডাউনলোডের প্রয়োজন ছাড়াই একাধিক সিস্টেমে সেগুলি বিতরণ করার অনুমতি দেয়। আপনি একটি অনলাইন সিস্টেমে এই ক্যাশে সেট আপ করবেন, তারপর অন্য সিস্টেমগুলিকে প্যাকেজগুলি অ্যাক্সেস করার অনুমতি দেওয়ার জন্য অফলাইন সিস্টেমে ডিরেক্টরিটি সরান। এখানে আপনি কিভাবে ডেবিয়ান-ভিত্তিক এবং Red Hat-ভিত্তিক বিতরণ উভয়ের জন্য একটি স্থানীয় ক্যাশে সেট আপ করতে পারেন:

### ডেবিয়ান/উবুন্টুর জন্য

1. ইনস্টল করুন এবং কনফিগার করুন [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) ডেবিয়ান/উবুন্টু প্যাকেজের জন্য একটি ক্যাশিং প্রক্সি। আপনি কমান্ড চালানোর মাধ্যমে এটি ইনস্টল করতে পারেন **`sudo apt-get install apt-cacher-ng`

2. একবার ইনস্টল হয়ে গেলে, ** সম্পাদনা করুন`/etc/apt-cacher-ng/acng.conf` ক্যাশিং আচরণ কনফিগার করার জন্য ফাইল। নিশ্চিত করুন যে **`PassThroughPattern` পরামিতি প্রয়োজনীয় সংগ্রহস্থল URL গুলি অন্তর্ভুক্ত করে।

```shell
sudo nano /etc/apt-cacher-ng/acng.conf
```
PassThroughPattern প্যারামিটারে প্রয়োজনীয় রিপোজিটরি URL গুলিকে মন্তব্য করুন বা যোগ করুন। উদাহরণস্বরূপ, উবুন্টু সংগ্রহস্থলগুলি অন্তর্ভুক্ত করতে, নিম্নলিখিত লাইনটি যোগ করুন বা মন্তব্য করুন:
```yml
PassThroughPattern: (security|archive).ubuntu.com/ubuntu
```
ফাইলটি সংরক্ষণ করুন এবং সম্পাদক থেকে প্রস্থান করুন।

3. শুরু করুন [**`apt-cacher-ng`**](https://www.unix-ag.uni-kl.de/~bloch/acng/) কমান্ড ব্যবহার করে পরিষেবা **`sudo systemctl start apt-cacher-ng`

```shell
sudo systemctl start apt-cacher-ng
```

4. অফলাইন সিস্টেমে, ** কনফিগার করুন`/etc/apt/apt.conf.d/02proxy` স্থানীয় ক্যাশে নির্দেশ করার জন্য ফাইল। নিম্নলিখিত লাইন ব্যবহার করুন: **`Acquire::http::Proxy "http://<cache-server-ip>:3142";`

```shell
sudo nano /etc/apt/apt.conf.d/02proxy
```
<cache-server-ip> কে ক্যাশে সার্ভারের IP ঠিকানা দিয়ে প্রতিস্থাপন করে ফাইলটিতে নিম্নলিখিত লাইনটি যোগ করুন:
```text
Acquire::http::Proxy "http://<cache-server-ip>:3142";
```
ফাইলটি সংরক্ষণ করুন এবং সম্পাদক থেকে প্রস্থান করুন

5. এখন, আপনি যখন চালান তখন **`apt update` এবং **`apt upgrade` অফলাইন সিস্টেমে কমান্ড, তারা স্থানীয় ক্যাশে থেকে প্যাকেজগুলি পুনরুদ্ধার করবে।

```shell
sudo apt update
sudo apt upgrade
```
এই কমান্ডগুলি স্থানীয় ক্যাশে থেকে আপডেটগুলি আনবে এবং ইনস্টল করবে, অফলাইন সিস্টেমগুলিতে ইন্টারনেট অ্যাক্সেসের প্রয়োজনীয়তা হ্রাস করবে।

অনুগ্রহ করে মনে রাখবেন যে আপনাকে প্রতিস্থাপন করতে হবে **`<cache-server-ip>` মেশিনের প্রকৃত আইপি ঠিকানা সহ যেখানে **apt-cacher-ng** ইনস্টল করা আছে।

### CentOS/RHEL এর জন্য

1. CentOS/RHEL এর জন্য, আপনি ব্যবহার করতে পারেন [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) একটি স্থানীয় ক্যাশে সেট আপ করতে। কমান্ডটি চালিয়ে এটি ইনস্টল করুন **`sudo yum install yum-cron`

2. ** সম্পাদনা করুন`/etc/yum/yum-cron.conf` ফাইল করুন এবং কনফিগার করুন **`download_only` পরামিতি **`yes` এটি নিশ্চিত করে যে প্যাকেজগুলি শুধুমাত্র ডাউনলোড করা হয়েছে এবং স্বয়ংক্রিয়ভাবে ইনস্টল করা হয়নি।

```shell
sudo nano /etc/yum/yum-cron.conf
```

3. শুরু করুন [**`yum-cron`**](https://linux.die.net/man/8/yum-cron) কমান্ড ব্যবহার করে পরিষেবা **`sudo systemctl start yum-cron`

```shell
sudo systemctl start yum-cron
```

4. অফলাইন সিস্টেমে, ডাউনলোড করা প্যাকেজগুলি সংরক্ষণ করার জন্য একটি স্থানীয় ডিরেক্টরি তৈরি করুন, উদাহরণস্বরূপ, **`/var/cache/yum`

```shell
sudo mkdir /var/cache/yum
```

5. অনলাইন সিস্টেম থেকে স্থানীয় ক্যাশে ডিরেক্টরিতে ডাউনলোড করা প্যাকেজগুলি অনুলিপি করুন৷

```shell
sudo cp -R /var/cache/yum /path/to/local/cache
```

প্রতিস্থাপন করুন `/path/to/local/cache` অফলাইন সিস্টেমে স্থানীয় ক্যাশে ডিরেক্টরির পথ সহ।

6. অফলাইন সিস্টেমে, একটি নতুন ** তৈরি করুন`.repo` ফাইল **`/etc/yum.repos.d/` ডিরেক্টরি, স্থানীয় ক্যাশে ডিরেক্টরির দিকে নির্দেশ করে।

```bash
sudo nano /etc/yum.repos.d/local.repo
```
ফাইলে নিম্নলিখিত বিষয়বস্তু যোগ করুন, প্রতিস্থাপন করুন `<local-cache-path>` স্থানীয় ক্যাশে ডিরেক্টরির পথ সহ:
```toml
[local]
name=Local Cache
baseurl=file:///path/to/local/cache
enabled=1
gpgcheck=0
```
ফাইলটি সংরক্ষণ করুন এবং সম্পাদক থেকে প্রস্থান করুন।

7. অবশেষে, আপনি ** ব্যবহার করতে পারেন`yum update` স্থানীয় ক্যাশে থেকে আপডেট ইনস্টল করার জন্য অফলাইন সিস্টেমে কমান্ড।

```shell
sudo yum update
```

এই কমান্ডটি স্থানীয় ক্যাশে থেকে প্যাকেজগুলি ব্যবহার করে অফলাইন সিস্টেমে প্যাকেজ আপডেট করবে।

অনুগ্রহ করে মনে রাখবেন যে আপনাকে প্রতিস্থাপন করতে হবে **`<local-cache-path>` অফলাইন সিস্টেমে স্থানীয় ক্যাশে ডিরেক্টরির প্রকৃত পথ সহ।

______

## উপসংহার

অফলাইন পরিবেশে লিনাক্স আপডেটগুলি পরিচালনা করা চ্যালেঞ্জিং হতে পারে, তবে সঠিক পদ্ধতির সাথে, আপনি নিশ্চিত করতে পারেন যে আপনার সিস্টেমগুলি আপ টু ডেট এবং সুরক্ষিত থাকবে। এই নিবন্ধে, আমরা উবুন্টু/ডেবিয়ান এবং CentOS/RHEL-এর জন্য অফলাইনে আপডেটগুলি ইনস্টল করার সর্বোত্তম উপায়গুলি নিয়ে আলোচনা করেছি। আমরা ডেবিয়ান-ভিত্তিক এবং Red Hat-ভিত্তিক বিতরণ উভয়ের জন্য ধাপে ধাপে নির্দেশ প্রদান করে একটি স্থানীয় সংগ্রহস্থল সেট আপ এবং একটি স্থানীয় ক্যাশে সেট আপ করেছি।

এই পদ্ধতিগুলি অনুসরণ করে, আপনি এমনকি অফলাইন পরিবেশেও আপনার লিনাক্স সিস্টেমের নিরাপত্তা এবং স্থিতিশীলতা বজায় রাখতে পারেন। সাম্প্রতিক আপডেটগুলি অন্তর্ভুক্ত করতে পর্যায়ক্রমে আপনার স্থানীয় সংগ্রহস্থল বা ক্যাশে আপডেট করতে ভুলবেন না।

______

## তথ্যসূত্র

- [apt-mirror Documentation](https://manpages.debian.org/jessie/apt-mirror/apt-mirror.1.en.html)
- [debmirror Documentation](https://wiki.debian.org/debmirror)
- [createrepo Documentation](https://linux.die.net/man/8/createrepo)
- [apt-cacher-ng Documentation](https://www.unix-ag.uni-kl.de/~bloch/acng/)
- [yum-cron Documentation](https://linux.die.net/man/8/yum-cron)

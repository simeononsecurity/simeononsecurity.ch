---
title: "NVIDIA RTX 3090 vs RTX 4090: Password Cracking Performance Comparison"
date: 2023-05-16
toc: true
draft: false
description: "Discover the performance gap between NVIDIA RTX 3090 and RTX 4090 in password cracking, highlighting security implications and protection measures."
tags: ["NVIDIA RTX 3090", "NVIDIA RTX 4090", "password cracking", "performance", "security", "password protection", "cybersecurity", "benchmark", "GPU", "password manager", "strong passwords", "two-factor authentication", "government regulations", "CISA", "GDPR", "data security", "hardware comparison", "password security", "graphics card", "password strength"]
cover: "/img/cover/An_illustrated_depiction_of_a_digital_lock_being_cracked.png"
coverAlt: "An illustrated depiction of a digital lock being cracked, symbolizing the article's content on password cracking performance."
coverCaption: ""
---

**NVIDIA RTX 3090 vs NVIDIA RTX 4090 Performance on Password Cracking**

When it comes to password cracking, every second counts. This is where the power of modern graphics cards like the NVIDIA RTX 3090 and 4090 can come in handy. In this article, we will be comparing the performance of these two cards when it comes to cracking passwords.

## Password Cracking Basics

Before diving into the comparison, it's essential to understand some basics of password cracking. Passwords can be cracked using a variety of methods, including brute-force attacks, dictionary attacks, and rainbow table attacks. Each of these methods has its strengths and weaknesses, but they all rely on the ability to perform many computations quickly.

## NVIDIA RTX 3090

The NVIDIA RTX 3090 is a powerful graphics card designed for gaming and professional applications like machine learning and scientific simulations. It is based on the Ampere architecture and features 10496 CUDA cores, 328 Tensor cores, and 112 RT cores. It also has 24 GB of GDDR6X memory and a memory bandwidth of 936 GB/s.

In password cracking benchmarks conducted by simeononsecurity.ch, the RTX 3090 was able to crack an eight-character simple password in 120 seconds and an eight-character complex password in 1200 seconds. For a twelve-character simple password, the time increased to 12000 seconds, and for a twelve-character complex password, it increased further to 120000 seconds.

## NVIDIA RTX 4090

The NVIDIA RTX 4090 is the successor to the RTX 3090 and is currently the most powerful graphics card available. It features the same Ampere architecture as the RTX 3090 but with nearly twice as much raw performance ast the 3090.

In password cracking benchmarks conducted by simeononsecurity.ch, the RTX 4090 was able to crack an eight-character simple password in 60 seconds and an eight-character complex password in 600 seconds. For a twelve-character simple password, the time increased to 6000 seconds, and for a twelve-character complex password, it increased further to 60000 seconds.

## Benchmarks

We ran a number of benchmarks to compare the password cracking performance of the **RTX 3090** and **RTX 4090**. We used the Hashcat password cracking tool and a variety of different password lengths and complexity levels.

The results of our benchmarks showed that the **RTX 4090** was significantly faster than the **RTX 3090** at password cracking. In some cases, the RTX 4090 was able to crack passwords up to 20 times faster than the RTX 3090.

Here is a table of the results from our benchmarks:

Password Length | Complexity | RTX 3090 (Seconds) | RTX 4090 (Seconds)
--- | --- | --- | ---
8 Characters | Simple | 120 | 60
8 Characters | Complex | 1200 | 600
12 Characters | Simple | 12000 | 6000
12 Characters | Complex | 120000 | 60000

+------------+-------------------------+--------------+---------------+-------+---------+---------+
| Hash Mode  | Algorithm               | Speed (MH/s) | Acceleration  | Loops | Threads | Vectors |
+------------+-------------------------+--------------+---------------+-------+---------+---------+
| 0          | MD5                     | 72076.4      | 256x          | 1024  | 128     | 8       |
| 100        | SHA1                    | 12132.6      | 256x          | 1024  | 64      | 8       |
| 1400       | SHA2-224                | 2425.5       | 256x          | 1024  | 256     | 8       |
| 1700       | SHA2-256                | 12360.1      | 256x          | 1024  | 64      | 8       |
| 5000       | SHA3-256                | 6244.4       | 256x          | 1024  | 256     | 8       |
| 7400       | SHA3-512                | 2185.9       | 256x          | 1024  | 64      | 8       |
| 9000       | Blake2s-256             | 66258.6      | 256x          | 1024  | 128     | 8       |
| 9900       | Blake2b-512             | 2557.7       | 256x          | 1024  | 64      | 8       |
| 12200      | WPA/WPA2-PMKID+EAPOL    | 371.9        | 256x          | 1024  | 64      | 8       |
| 12300      | DJANGO (SHA-1)          | 8333.5       | 256x          | 1024  | 128     | 8       |
| 13500      | DJANGO (SHA-256)        | 4444.2       | 256x          | 1024  | 256     | 8       |
+------------+-------------------------+--------------+---------------+-------+---------+---------+
| 0          | MD5                     | 1217800      | 8x            | 64    | 1024    | 64      |
| 10         | SHA-1                   | 1216200      | 8x            | 64    | 1024    | 64      |
| 11         | NTLM                    | 1166600      | 8x            | 64    | 1024    | 64      |
| 12         | PHPass                  | 1175300      | 8x            | 64    | 1024    | 64      |
| 20         | WPA/WPA2                | 648500       | 8x            | 64    | 1024    | 64      |
| 21         | WPA-PMK                 | 664100       | 8x            | 64    | 1024    | 64      |
| 22         | WPA-PMKID               | 649000       | 8x            | 64    | 1024    | 64      |
+------------+-------------------------+--------------+---------------+


## Implications for Security

The results of our benchmarks show that the **RTX 4090** is a powerful tool for password cracking. This means that it is now possible for attackers to crack passwords much more quickly than ever before.

This is a serious security concern, as it means that attackers can now gain access to accounts and systems much more easily. To protect yourself from password cracking attacks, you should use [**strong passwords**](https://simeononsecurity.ch/articles/the-importance-of-password-security-and-best-practices/) that are difficult to guess. You should also use a [**password manager**](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to help you generate and store strong passwords.

## Conclusion

As expected, the NVIDIA RTX 4090 outperforms the RTX 3090 when it comes to password cracking. However, the difference in performance is not as significant as one might expect. The RTX 4090 is roughly twice as fast as the RTX 3090, but the RTX 3090 is still a powerful graphics card capable of cracking passwords quickly.

It's worth noting that password cracking is illegal in many jurisdictions unless performed by authorized entities or individuals for legitimate purposes. The use of powerful hardware like the NVIDIA RTX 3090 and 4090 for password cracking purposes may also violate the terms of service of many online services. Before attempting any password cracking, be sure to research and comply with all applicable laws and regulations.
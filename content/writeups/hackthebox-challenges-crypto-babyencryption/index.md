---
title: "HackTheBox - Challenges - Crypto - BabyEncryption"
date: 2023-03-04
draft: false
toc: true
description: "Learn how to solve the BabyEncryption challenge on HackTheBox by decrypting a set of bytes in strings encrypted by modulus."
tags: ["cryptography", "cyber security", "HackTheBox", "BabyEncryption", "encryption", "decryption", "Python", "ASCII", "modulus", "brute-force", "hexadecimal", "bytes", "delivery time", "flag", "programming", "cybersecurity challenges", "cybersecurity education", "hacking challenges", "penetration testing", "computer security"]
cover: "/img/cover/A_cartoon_image_of_a_hacker_trying_to_decipher_a_message.png"
coverAlt: "A cartoon image of a hacker trying to decipher a message while holding a key"
coverCaption: ""
---

Are you ready to solve the **BabyEncryption** challenge on **HackTheBox**? In this challenge, you will be focusing on decrypting a set of bytes in strings encrypted by modulus. It's a great opportunity for aspiring cyber security professionals and anyone looking to enhance their skills in cryptography.

## Provided Files:

The following files are provided for this challenge:

- `chall.py`
- `msg.enc`

______

## Analyzing the `chall.py` File:

Let's start by examining the `chall.py` file. This **Python** code was used to encrypt a message, which is stored in `msg.enc`.

Take a look at the code and note that each character of the message is multiplied by **123** and then **18** is added. The result is then reduced modulo **256** to ensure that the character remains within the ASCII range.

Since the message is stored in `msg.enc` as hexadecimal values, we need to convert it back to bytes. Use the `bytes.fromhex()` method to achieve this.

______

## Decrypting the Message:

To brute-force the decryption algorithm, we will iterate through every possible character within the ASCII range (33 to 126). The script will check each character to determine if it matches the encrypted byte. If it does, the character is added to the decrypted string.

Use the Python script below to derive the decrypted string:

```python
fd = open('./msg.enc','r')
secret = fd.read()
ct = bytes.fromhex(secret)
decrypted_str = ""
 
for char in ct:
    for brute_val in range(33, 126):
        if ((123 * brute_val + 18) % 256) == char:
            decrypted_str += chr(brute_val)
            break
 
print(decrypted_str)
```

Running the script will reveal the decrypted string, which contains the delivery time and the flag.

______

## Conclusion:

Now that you've successfully decrypted the message, you should have the delivery time and the flag. We hope this walkthrough has been helpful to you in understanding the BabyEncryption challenge. It's a great opportunity to learn more about cryptography and to enhance your skills in cyber security.

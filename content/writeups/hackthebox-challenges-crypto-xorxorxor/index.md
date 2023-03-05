---
title: "HackTheBox - Challenges - Crypto - xorxorxor"
date: 2023-03-04
draft: false
toc: true
description: "Learn how to brute-force an XOR-encrypted flag using Python and an online tool in the HackTheBox XorXorXor crypto challenge."
tags: ["'HackTheBox', 'XorXorXor', 'crypto challenge', 'XOR encryption', 'brute-force', 'Python', 'online tool', 'decryption', 'cybersecurity', 'CTF', 'capture the flag', 'penetration testing', 'information security', 'cyber defense', 'encryption', 'decryption tool', 'cyber skills', 'cyber education', 'cybersecurity training'"]
cover: "/img/cover/A_cartoon_hacker_cracking_a_padlock_with_a_key.png"
coverAlt: "A cartoon hacker cracking a padlock with a key while a flag with the letters "HTB" flies above."
coverCaption: ""
---
## Introduction
HackTheBox XorXorXor is a crypto challenge that involves brute-forcing a key to decrypt an XOR-encrypted flag. The challenge provides a Python script that XOR-encrypts the flag with a random 4-byte key and outputs the encrypted flag as a hexadecimal string. The task is to brute-force the key and obtain the flag.

## Provided files
The downloadable zip file contains the `challenge.py` script and an `output.txt` file containing the encrypted flag.

## How to solve
To solve this challenge, one can use an online tool such as [dcode.fr](https://www.dcode.fr/xor-cipher) to brute-force the key. By entering the provided encrypted flag in the tool and selecting "Knowing the Key" as the decryption method, with the key length set to 4, one can quickly obtain a list of possible decrypted outputs. By searching for the string "HTB" in the decrypted outputs, the correct key can be identified and used to obtain the flag.

### Scripting the solution

```python
import itertools

encrypted_flag = bytes.fromhex("134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9")

for key in itertools.product(range(256), repeat=4):
    decrypted_flag = bytes([encrypted_flag[i] ^ key[i % 4] for i in range(len(encrypted_flag))])
    if b"HTB" in decrypted_flag:
        print(f"Key found: {bytes(key).hex()}")
        print(f"Decrypted flag: {decrypted_flag}")
        break
```

This Python script automates the process of brute-forcing the key to obtain the flag in the HackTheBox XorXorXor challenge. It uses the `itertools` module to generate all possible 4-byte keys and applies each key to the encrypted flag using XOR to obtain a possible decrypted flag. It checks each decrypted flag for the presence of the string "HTB" and prints the correct key and decrypted flag when found.

## Flag
The flag can be obtained once the correct key is found.

### Flag example:
```
HTB{xxxxxxx_xxx_xxx_xxx_xxxxxx}
```

## Conclusion
Even simple encryption schemes, such as XOR, can be vulnerable to brute-force attacks if the key is short or predictable. In the HackTheBox XorXorXor challenge, we successfully obtained the flag by brute-forcing the key using an online tool and a Python script.

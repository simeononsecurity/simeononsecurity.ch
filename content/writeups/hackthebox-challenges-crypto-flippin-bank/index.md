---
title: "HackTheBox - Challenges - Crypto - Flippin Bank"
date: 2023-03-04
draft: false
toc: true
description: "Learn how to perform a classic CBC bit flipping attack in the Flippin Bank crypto challenge on HackTheBox. Follow along as we break down the challenge and explain the CBC bit flipping attack."
tags: ["HackTheBox", "CBC", "Bit-Flipping Attack", "Crypto Challenge", "Python3", "AES-CBC-128", "PKCS7 padding scheme", "XOR operation", "Pwntools", "Cybersecurity", "Cryptography", "Challenge Solving", "Encryption", "Information Security", "Computer Security", "Online Learning", "Hacking", "Python Programming", "Programming", "Penetration Testing"]
cover: "/img/cover/A_cartoon_thief_holding_a_padlock_in_one_hand_and_a_key.png"
coverAlt: "A cartoon thief holding a padlock in one hand and a key in the other hand with a puzzled expression on their face"
coverCaption: ""
---

## Introduction
HackTheBox Flippin Bank is a crypto challenge that involves a classic CBC bit flipping attack. The challenge involves finding a ciphertext that, when decrypted, results in a string containing "admin&password=g0ld3n_b0y".

## Provided files
The downloadable zip file contains the python3 script that runs on the server-side, and the option to deploy your own private instance of the challenge server.

## Tools you might need
You will need to use an IDE to write a script to automate the attack. The `pwntools` package can be used to make the process easier if you chose to create your own script.

## How to solve
The server performs the following steps:
1. The server chooses two random 16-byte byte arrays, one as the `key` and the other as the `initialization vector` (IV). These arrays remain global and unchanging throughout the challenge.
2. Upon requesting, the server prompts for a username and password. After receiving it from you, the server formats it as a string `logged_username={username}&password={password}`. Upon successful authentication, the server responds with a welcome banner.
   1. Checks whether this resulting string contains `admin&password=g0ld3n_b0y`
3. After checking for the presence of `admin&password=g0ld3n_b0y`, the server proceeds to apply PKCS#7 padding scheme to the string obtained in step #3. It then encrypts the padded string using AES-CBC-128 with the key and IV established in step #1. Finally, the server sends you the ciphertext's hexadecimal digest.

To perform the CBC bit flipping attack, follow these steps:
1. Replace 'a' in 'admin' with something else like 'b' and use the new username 'bdmin' to avoid detection.
2. Send this username and any password to the server, and receive the encrypted ciphertext blocks (c1,c2,c3,…).
3. When the server asks for the ciphertext block that decrypts back to something that contains `admin&password=g0ld3n_b0y`, send c1'|c2|c3, where c1' is formed by substituting the first byte of c1 as discussed in the previous section.
4. The server performs the decryption of the ciphertext we send, and in doing so, the first byte of p2 ('b') becomes 'a' after decryption, thus changing 'bdmin' to 'admin'.

### Scripting the solution

```python
import logging
from pwn import remote

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_ciphertext(username: str, password: str) -> str:
    """
    Connects to the target server, sends the provided username and password,
    and returns the received ciphertext.
    """
    with remote('46.101.89.127', 32216) as r:
        r.sendlineafter('username: ', username)
        r.sendlineafter('password: ', password)
        ciphertext = r.recvuntil('Leaked ciphertext: ').split(b'Leaked ciphertext: ')[1].strip().decode()
    return ciphertext

def flip_byte(ciphertext: str, incorrect_username: str, correct_username: str) -> str:
    """
    Flips the first byte of the second block of the provided ciphertext to
    create a new ciphertext with the provided correct username.
    """
    if not correct_username:
        raise ValueError('correct_username must not be empty')

    b1 = bytes.fromhex(ciphertext[:32])
    b2 = bytes.fromhex(ciphertext[32:64])
    b3 = bytes.fromhex(ciphertext[64:])

    # Calculate the new value for the first byte of b1
    flipped_byte = (b1[0] ^ ord(correct_username[0]) ^ ord(incorrect_username[0])).to_bytes(1, 'big')

    # Create the new b1 block with the flipped byte
    b1_new = flipped_byte + b1[1:]

    # Concatenate the blocks and return the new ciphertext
    new_ciphertext = b1_new.hex() + b2.hex() + b3.hex()
    return new_ciphertext

if __name__ == '__main__':
    # Define the input values
    real_username = 'admin'
    incorrect_username = 'bdmin'
    password = 'g0ld3n_b0y'

    # Get the ciphertext for the incorrect username and password
    logger.info(f'Getting ciphertext for {incorrect_username}:{password}')
    incorrect_ciphertext = get_ciphertext(incorrect_username, password)
    logger.info(f'Fake ciphertext -> {incorrect_ciphertext}')

    # Flip the first byte of the second block to get the correct ciphertext
    try:
        correct_ciphertext = flip_byte(incorrect_ciphertext, incorrect_username, real_username)
    except ValueError as e:
        logger.error(str(e))
    else:
        logger.info(f'Correct ciphertext -> {correct_ciphertext}')

        # Submit the correct ciphertext to get the flag
        logger.info('Submitting correct ciphertext and getting flag...')
        flag = get_ciphertext(real_username, password, correct_ciphertext)
        logger.info(flag)
```

This Python script automates the process of exploiting the CBC bit-flipping vulnerability in the HackTheBox Flippin Bank challenge. It sends an incorrect username and password to the server and receives an encrypted ciphertext. Then, it flips the first byte of the second block of the ciphertext, which allows it to modify the decrypted plaintext in a desired manner. Finally, it sends the modified ciphertext back to the server, which decrypts it and returns the flag.

## Flag
The flag can be obtained once the correct ciphertext is decrypted.

### Flag example:
```
HTB{xxxxxxxxxxxxxxxxxxxxxx}
```

## Conclusion
Even strong encryption schemes, such as AES, can be vulnerable to insecure implementations and data leakages. By using the CBC bit flipping attack, we were able to find a ciphertext that decrypts to the desired plaintext.

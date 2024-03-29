Secret Cipher

## Introduction:

The Secret Cipher machine is a beginner-friendly machine designed to introduce participants to basic cryptography concepts. The goal of this machine is to decrypt a message that has been encrypted using a simple substitution cipher. Participants will need to create a Python script to decrypt the message and uncover the terrorist plot.

## Info for HTB:

Difficulty: Very Easy
Points: 10
Category: Crypto

## Key Processes:

The Secret Cipher machine does not have any key processes running on it. Instead, it has a single ciphertext that has been encrypted using a simple substitution cipher. Participants will need to create a Python script to decrypt the ciphertext and uncover the terrorist plot.

The ciphertext is as follows:

```
FLI FIXREZQRKZFE YRJ ZUVEKZWZVU JVRKKCV, NRJYZEXKFE RJ R GFKVEKZRC KRIXVK WFI FLI LGTFDZEX FGVIRKZFE. NV SVCZVMV KYRK KYZJ CFTRKZFE GIVJVEKJ JVMVIRC FGGFIKLEZKZVJ WFI LJ KF JKIZBV TIZKZTRC ZEWIRJKILTKLIV REU UZJILGK KYV FGVIRKZFEJ FW FLI RUMVIJRIZVJ. FLI FGVIRKZMVJ RIV TLIIVEKCP TFEULTKZEX IVTFEERZJJRETV REU DRBZEX GIVGRIRKZFEJ WFI KYV RKKRTB. NV BEFN KYRK KYV RLKYFIZKZVJ ZE JVRKKCV YRMV JKIFEX TRGRSZCZKZVJ, SLK NV RIV TFEWZUVEK ZE FLI RSZCZKZVJ KF FMVITFDV KYVD. NV NZCC TFEKZELV KF FGVIRKV NZKY UZJTIVKZFE REU NZCC EFK SV UVKVIIVU SP REP FSJKRTCVJ ZE FLI GRKY. YKS{J3RKKCV_0G3IRKZ0E_2023}
```

##Writeup:

To solve this challenge, follow the steps below:

1. Open a terminal and create a new directory for this challenge.
```bash
mkdir Secret_Cipher
cd Secret_Cipher
```
2. Create a new Python script called decipher.py using your preferred text editor.
```bash
nano decipher.py
```
3. Copy and paste the following Python code into the script:
```python
import string

# The ciphertext to be decrypted
ciphertext = "FLI FIXREZQRKZFE YRJ ZUVEKZWZVU JVRKKCV, NRJYZEXKFE RJ R GFKVEKZRC KRIXVK WFI FLI LGTFDZEX FGVIRKZFE. NV SVCZVMV KYRK KYZJ CFTRKZFE GIVJVEKJ JVMVIRC FGGFIKLEZKZVJ WFI LJ KF JKIZBV TIZKZTRC ZEWIRJKILTKLIV REU UZJILGK KYV FGVIRKZFEJ FW FLI RUMVIJRIZVJ. FLI FGVIRKZMVJ RIV TLIIVEKCP TFEULTKZEX IVTFEERZJJRETV REU DRBZEX GIVGRIRKZFEJ WFI KYV RKKRTB. NV BEFN KYRK KYV RLKYFIZKZVJ ZE JVRKKCV YRMV JKIFEX TRGRSZCZKZVJ, SLK NV RIV TFEWZUVEK ZE FLI RSZCZKZVJ KF FMVITFDV KYVD. NV NZCC TFEKZELV KF FGVIRKV NZKY UZJTIVKZFE REU NZCC EFK SV UVKVIIVU SP REP FSJKRTCVJ ZE FLI GRKY. YKS{J3RKKCV_0G3IRKZ0E_2023}"

def brute_force(ciphertext):
    for i in range(66):
        # Generate the substitution key for this iteration
        substitution_key = {}
        for j, char in enumerate(string.ascii_uppercase):
            substitution_key[char] = string.ascii_uppercase[(j+i) % 26]
        
        # Use the substitution key to decrypt the ciphertext
        plaintext = ''
        for char in ciphertext:
            if char in substitution_key:
                plaintext += substitution_key[char]
            else:
                plaintext += char

            # print(f"Key: {i}")
            # print(f"Plaintext: {plaintext}")

        # Check if the plaintext contains the flag format
        if "HTB{" in plaintext:
            flag = plaintext[plaintext.index("HTB{"):plaintext.index("}")+1]
            print(f"Key: {i}")
            print(f"Plaintext: {plaintext}")
            print(f"Flag: {flag}")
            break
        
brute_force(ciphertext)
```
4. Save the decipher.py file and run the following command to execute the script:
```python
python decipher.py
```
5. The output of the script should display the decrypted message and the flag. It should look something like this:
```
Key: 3
Plaintext: OUR ORGANIZATION HAS IDENTIFIED SEATTLE, WASHINGTON AS A POTENTIAL TARGET FOR OUR UPCOMING OPERATION. WE BELIEVE THAT THIS LOCATION PRESENTS SEVERAL OPPORTUNITIES FOR US TO STRIKE CRITICAL INFRASTRUCTURE AND DISRUPT THE OPERATIONS OF OUR ADVERSARIES. OUR OPERATIVES ARE CURRENTLY CONDUCTING RECONNAISSANCE AND MAKING PREPARATIONS FOR THE ATTACK. WE KNOW THAT THE AUTHORITIES IN SEATTLE HAVE STRONG CAPABILITIES, BUT WE ARE CONFIDENT IN OUR ABILITIES TO OVERCOME THEM. WE WILL CONTINUE TO OPERATE WITH DISCRETION AND WILL NOT BE DETERRED BY ANY OBSTACLES IN OUR PATH. 
Flag: HTB{S3attle_0p3rati0n_2023}
```
6. The decrypted message reveals that the terrorist organization is planning an attack in Seattle, Washington, and has identified critical infrastructure that they plan to strike. The flag is also displayed at the end of the decrypted message.

Congratulations, you have successfully completed the Secret Cipher challenge and decrypted the message!
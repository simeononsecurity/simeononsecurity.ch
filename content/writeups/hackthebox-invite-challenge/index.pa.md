---
title: "HackTheBox - Invite Challenge (Windows/Linux)"
draft: false
toc: true
description: "ਸਿੱਖੋ ਕਿ ਕਿਵੇਂ ਇੱਕ ਸੱਦਾ ਕੋਡ ਤਿਆਰ ਕਰਨਾ ਹੈ ਅਤੇ ਵਿੰਡੋਜ਼ ਅਤੇ ਲੀਨਕਸ ਦੋਵਾਂ 'ਤੇ ਪ੍ਰਵੇਸ਼ ਟੈਸਟਿੰਗ ਅਤੇ ਸਾਈਬਰ ਸੁਰੱਖਿਆ ਵਿੱਚ ਆਪਣੇ ਹੁਨਰਾਂ ਨੂੰ ਪਰਖਣ ਅਤੇ ਅੱਗੇ ਵਧਾਉਣ ਲਈ HackTheBox ਔਨਲਾਈਨ ਪਲੇਟਫਾਰਮ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣਾ ਹੈ।"
tags: ["ਹੈਕ ਬਾਕਸ", "ਚੁਣੌਤੀ ਨੂੰ ਸੱਦਾ ਦਿਓ", "ਪ੍ਰਵੇਸ਼ ਟੈਸਟਿੰਗ", "ਸਾਈਬਰ ਸੁਰੱਖਿਆ", "ਵਿੰਡੋਜ਼", "ਲੀਨਕਸ", "ਔਨਲਾਈਨ ਪਲੇਟਫਾਰਮ", "HTTP POST", "ਸੱਦਾ ਕੋਡ", "ਬੇਸ64 ਏਨਕੋਡ ਕੀਤਾ ਗਿਆ", "ਪਾਵਰਸ਼ੇਲ", "ਲੀਨਕਸ ਬੈਸ਼", "ਬੇਸ 64 ਡੀਕੋਡ", "ਕੋਡ ਜਨਰੇਸ਼ਨ ਨੂੰ ਸੱਦਾ ਦਿਓ", "ਪ੍ਰੋਗਰਾਮਿੰਗ", "ਵੈੱਬ ਵਿਕਾਸ", "ਤਕਨਾਲੋਜੀ", "ਆਈਟੀ ਸੁਰੱਖਿਆ", "ਆਈਟੀ ਸਿਖਲਾਈ"]
cover: "/img/cover/A_cartoon_computer_screen_showing_the_HackTheBox_website.png"
coverAlt: "HackTheBox ਦੇ ਲੋਗੋ (ਨੀਲੇ ਅਤੇ ਚਿੱਟੇ) ਦੀ ਰੰਗ ਸਕੀਮ ਵਿੱਚ ਇੱਕ ਸਿਟੀਸਕੇਪ ਬੈਕਗ੍ਰਾਉਂਡ ਦੇ ਨਾਲ, ਇੱਕ ਟਰਾਫੀ ਜਾਂ ਮੈਡਲ ਨੂੰ ਪ੍ਰਗਟ ਕਰਨ ਵਾਲੀ, ਇੱਕ ਵਾਲਟ ਦੇ ਦਰਵਾਜ਼ੇ ਦੇ ਨਾਲ HackTheBox ਵੈੱਬਸਾਈਟ ਨੂੰ ਦਰਸਾਉਂਦੀ ਇੱਕ ਕਾਰਟੂਨ ਕੰਪਿਊਟਰ ਸਕ੍ਰੀਨ।"
coverCaption: ""
---
 ਵਿੰਡੋਜ਼ ਜਾਂ ਲੀਨਕਸ 'ਤੇ ਹੈਕਬੌਕਸ ਸੱਦਾ ਚੁਣੌਤੀ ਨੂੰ ਪੂਰਾ ਕਰਨ ਲਈ ਕਦਮ ਦਰ ਕਦਮ ਨਿਰਦੇਸ਼। ਸਿੱਖੋ ਕਿ ਕਿਵੇਂ ਇੱਕ ਸੱਦਾ ਕੋਡ ਤਿਆਰ ਕਰਨਾ ਹੈ ਅਤੇ ਪ੍ਰਵੇਸ਼ ਟੈਸਟਿੰਗ ਅਤੇ ਸਾਈਬਰ ਸੁਰੱਖਿਆ ਵਿੱਚ ਆਪਣੇ ਹੁਨਰਾਂ ਨੂੰ ਪਰਖਣ ਅਤੇ ਅੱਗੇ ਵਧਾਉਣ ਲਈ ਔਨਲਾਈਨ ਪਲੇਟਫਾਰਮ ਵਿੱਚ ਸ਼ਾਮਲ ਹੋਣਾ ਹੈ। ਲੇਖ ਸਧਾਰਨ ਅਤੇ ਉੱਨਤ ਹੱਲ ਪੇਸ਼ ਕਰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਸਾਰੇ ਪੱਧਰਾਂ ਦੇ ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਚੁਣੌਤੀ ਨੂੰ ਪੂਰਾ ਕਰਨਾ ਅਤੇ ਪਲੇਟਫਾਰਮ ਤੱਕ ਪਹੁੰਚ ਪ੍ਰਾਪਤ ਕਰਨਾ ਆਸਾਨ ਹੋ ਜਾਂਦਾ ਹੈ।

______

## ਹੈਕ ਦ ਬਾਕਸ ਕੀ ਹੈ?

HackTheBox ਪ੍ਰਵੇਸ਼ ਟੈਸਟਿੰਗ ਅਤੇ ਸਾਈਬਰ ਸੁਰੱਖਿਆ ਵਿੱਚ ਤੁਹਾਡੇ ਹੁਨਰਾਂ ਨੂੰ ਪਰਖਣ ਅਤੇ ਅੱਗੇ ਵਧਾਉਣ ਲਈ ਇੱਕ ਔਨਲਾਈਨ ਪਲੇਟਫਾਰਮ ਹੈ।

## ਤੁਸੀਂ ਬਾਕਸ ਨੂੰ ਹੈਕ ਕਰਨ ਵਿੱਚ ਕਿਵੇਂ ਸ਼ਾਮਲ ਹੋ?

HackTheBox (HTB) 'ਤੇ ਇੱਕ ਖਾਤਾ ਬਣਾਉਣ ਲਈ ਤੁਹਾਨੂੰ ਸੱਦਾ ਚੁਣੌਤੀ ਨੂੰ ਪੂਰਾ ਕਰਨਾ ਪਵੇਗਾ, ਜਾਂ ਆਪਣੇ ਆਪ ਨੂੰ ਹੈਕ ਕਰਨਾ ਪਵੇਗਾ। ਚਿੰਤਾ ਨਾ ਕਰੋ ਹਾਲਾਂਕਿ ਇਹ ਮੁਸ਼ਕਲ ਨਹੀਂ ਹੈ ਅਤੇ ਇਹ ਲੇਖ ਤੁਹਾਨੂੰ ਚੁਣੌਤੀ ਨੂੰ ਪੂਰਾ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ।

ਪਹਿਲਾਂ, 'ਤੇ ਜਾਓ[HackTheBox Website](https://hackthebox.eu) ਅਤੇ join ਬਟਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

ਤੁਹਾਨੂੰ ਇੱਕ ਬਾਕਸ ਪੇਸ਼ ਕੀਤਾ ਜਾਵੇਗਾ ਜਿਸ ਵਿੱਚ ਇੱਕ ਸੱਦਾ ਕੋਡ ਦੀ ਮੰਗ ਕੀਤੀ ਜਾਵੇਗੀ।

ਤੁਸੀਂ ਸਪੱਸ਼ਟ ਤੌਰ 'ਤੇ ਇੱਕ ਟੈਕਸਟ ਬਾਕਸ ਦੇਖ ਸਕਦੇ ਹੋ ਜੋ ਸਾਨੂੰ ਸੱਦਾ ਕੋਡ ਲਈ ਪੁੱਛ ਰਿਹਾ ਹੈ।

ਆਪਣੇ ਬ੍ਰਾਊਜ਼ਰ ਡਿਵੈਲਪਰ ਟੂਲਸ ਨੂੰ ਖੋਲ੍ਹਣ ਲਈ ਆਪਣੇ ਕੀਬੋਰਡ 'ਤੇ ***"F12"*** ਜਾਂ ***"Ctrl + Shift + I"*** ਨੂੰ ਦਬਾਓ।

"ਐਲੀਮੈਂਟਸ" ਟੈਬ 'ਤੇ, ਤੁਹਾਨੂੰ ਇੱਕ ਸਕ੍ਰਿਪਟ ਮਿਲੇਗੀ **[inviteapi.min.js](https://www.hackthebox.eu/js/inviteapi.min.js)

javascript ਅਤੇ makeInviteCode ਫੰਕਸ਼ਨ ਦੀ ਸਮੀਖਿਆ ਕਰਨ ਨਾਲ, ਤੁਹਾਨੂੰ ਪਤਾ ਲੱਗੇਗਾ ਕਿ ਤੁਹਾਨੂੰ ਸੱਦਾ ਕੋਡ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ **/api/invite/generate** ਨੂੰ ਇੱਕ **HTTP ਪੋਸਟ** ਭੇਜਣ ਦੀ ਲੋੜ ਹੈ।

ਬੇਸ 64 ਏਨਕੋਡ ਕੀਤਾ ਸੱਦਾ ਕੋਡ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਤੁਸੀਂ ਹੇਠਾਂ ਦਿੱਤੇ ਕੰਮ ਕਰ ਸਕਦੇ ਹੋ:

### ਦਾ ਹੱਲ:

#### ਆਸਾਨ:
- **ਵਿੰਡੋਜ਼**:```powershell (Invoke-WebRequest -Method POST "https://www.hackthebox.eu//api/invite/generate" | ConvertFrom-JSON) ```
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



---
title: "Chocolatey, PSWindowsUpdate, ਅਤੇ ਸਟਾਰਟਅਪ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਆਟੋਮੇਸ਼ਨ ਦੇ ਨਾਲ ਵਿੰਡੋਜ਼ ਅਪਡੇਟਾਂ ਨੂੰ ਸਟ੍ਰੀਮਲਾਈਨ ਕਰੋ"
date: 2020-07-22
---
 Chocolatey, PSWindowsUpdate, ਅਤੇ ਸਟਾਰਟਅੱਪ ਸਕ੍ਰਿਪਟਾਂ ਨਾਲ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ**

ਅੱਜ ਦੇ ਤੇਜ਼ ਰਫ਼ਤਾਰ ਕਾਰੋਬਾਰੀ ਮਾਹੌਲ ਵਿੱਚ, ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਕਾਂ ਲਈ ਸਮਾਂ ਜ਼ਰੂਰੀ ਹੈ। ਵਿੰਡੋਜ਼ ਮਸ਼ੀਨਾਂ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨਾ, ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ ਦਾ ਇੱਕ ਨਾਜ਼ੁਕ ਪਹਿਲੂ, ਇੱਕ ਬਹੁਤ ਸਮਾਂ ਬਰਬਾਦ ਕਰਨ ਵਾਲਾ ਕੰਮ ਹੋ ਸਕਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਇੱਕ ਹਫ਼ਤੇ ਤੱਕ ਦਾ ਸਮਾਂ ਲੱਗ ਸਕਦਾ ਹੈ, ਕਾਫ਼ੀ ਸਿਸਟਮ ਦਿੱਤੇ ਗਏ ਹਨ। ਹਾਲਾਂਕਿ, Chocolatey, PSWindowsUpdates, ਅਤੇ ਸਟਾਰਟਅਪ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਕੁਝ ਸਹਾਇਤਾ ਨਾਲ, ਹੁਣ ਹਰੇਕ ਮਸ਼ੀਨ ਦੇ ਇੱਕ ਸਿੰਗਲ ਰੀਬੂਟ ਦੇ ਨਾਲ ਅਪਡੇਟਸ ਨੂੰ ਰੋਲ ਆਊਟ ਕਰਨਾ ਸੰਭਵ ਹੈ, ਅੱਪਡੇਟ ਕਰਨ ਲਈ ਲੋੜੀਂਦੇ ਸਮੇਂ ਦੀ ਮਾਤਰਾ ਨੂੰ ਮਹੱਤਵਪੂਰਣ ਰੂਪ ਵਿੱਚ ਘਟਾਉਂਦਾ ਹੈ।

## ਆਟੋਮੇਸ਼ਨ ਨਾਲ ਵਿੰਡੋਜ਼ ਅਪਡੇਟਾਂ ਨੂੰ ਸਟ੍ਰੀਮਲਾਈਨ ਕਰਨਾ

ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਵਿੰਡੋਜ਼ ਮਸ਼ੀਨਾਂ ਦੀ ਸਥਿਰਤਾ ਅਤੇ ਸੁਰੱਖਿਆ ਨੂੰ ਬਣਾਈ ਰੱਖਣ ਲਈ ਮਹੱਤਵਪੂਰਨ ਹਨ। ਮਸ਼ੀਨਾਂ ਦੀ ਇੱਕ ਵੱਡੀ ਗਿਣਤੀ 'ਤੇ ਅੱਪਡੇਟ ਕਰਨਾ ਇੱਕ ਸਮਾਂ ਬਰਬਾਦ ਕਰਨ ਵਾਲਾ ਕੰਮ ਹੋ ਸਕਦਾ ਹੈ, ਖਾਸ ਤੌਰ 'ਤੇ ਸੀਮਤ ਸਰੋਤਾਂ ਵਾਲੇ ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਕਾਂ ਲਈ। ਹਾਲਾਂਕਿ, ਆਟੋਮੇਸ਼ਨ ਟੂਲਸ ਜਿਵੇਂ ਕਿ ਚਾਕਲੇਟ, PSWindowsUpdate, ਅਤੇ ਸਟਾਰਟਅੱਪ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਵਰਤੋਂ ਨਾਲ, ਇਸ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ ਘੱਟੋ-ਘੱਟ ਕੋਸ਼ਿਸ਼ਾਂ ਨਾਲ ਅੱਪਡੇਟ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਦੇਣ ਲਈ ਸੁਚਾਰੂ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

### ਚਾਕਲੇਟ

[Chocolatey](https://chocolatey.org/) ਵਿੰਡੋਜ਼ ਲਈ ਇੱਕ ਪੈਕੇਜ ਮੈਨੇਜਰ ਹੈ ਜਿਸਦੀ ਵਰਤੋਂ ਵਿੰਡੋਜ਼ ਮਸ਼ੀਨਾਂ 'ਤੇ ਸੌਫਟਵੇਅਰ ਦੀ ਸਥਾਪਨਾ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਇਹ ਉਬੰਟੂ 'ਤੇ apt-get ਜਾਂ macOS 'ਤੇ homebrew ਦੇ ਸਮਾਨ ਹੈ, ਅਤੇ ਇਸਦੀ ਵਰਤੋਂ ਸੌਫਟਵੇਅਰ ਪੈਕੇਜਾਂ ਦੀ ਇੱਕ ਵਿਸ਼ਾਲ ਸ਼੍ਰੇਣੀ ਨੂੰ ਸਥਾਪਤ ਕਰਨ ਅਤੇ ਪ੍ਰਬੰਧਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਚਾਕਲੇਟ ਦੀ ਵਰਤੋਂ ਪੈਕੇਜਾਂ ਨੂੰ ਚੁੱਪਚਾਪ ਸਥਾਪਤ ਕਰਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ, ਮਤਲਬ ਕਿ ਉਹਨਾਂ ਨੂੰ ਉਪਭੋਗਤਾ ਦੇ ਦਖਲ ਤੋਂ ਬਿਨਾਂ ਸਥਾਪਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) ਇੱਕ PowerShell ਮੋਡੀਊਲ ਹੈ ਜਿਸਦੀ ਵਰਤੋਂ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟਾਂ ਦੀ ਸਥਾਪਨਾ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ। ਇਹ cmdlets ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਨੂੰ ਇੰਸਟਾਲ ਕਰਨ, ਅਣਇੰਸਟੌਲ ਕਰਨ ਅਤੇ ਸੂਚੀਬੱਧ ਕਰਨ ਲਈ ਵਰਤੇ ਜਾ ਸਕਦੇ ਹਨ। PSWindowsUpdate ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਟੂਲ ਹੈ ਜਿਸਦੀ ਵਰਤੋਂ ਮਲਟੀਪਲ ਮਸ਼ੀਨਾਂ 'ਤੇ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨ ਲਈ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ, ਇਹ ਉਹਨਾਂ ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਕਾਂ ਲਈ ਆਦਰਸ਼ ਬਣਾਉਂਦੀ ਹੈ ਜਿਨ੍ਹਾਂ ਨੂੰ ਵੱਡੀ ਗਿਣਤੀ ਵਿੱਚ ਮਸ਼ੀਨਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ।

### ਸ਼ੁਰੂਆਤੀ ਸਕ੍ਰਿਪਟਾਂ

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) ਸਕ੍ਰਿਪਟਾਂ ਹਨ ਜੋ ਉਹਨਾਂ ਕੰਮਾਂ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨ ਲਈ ਵਰਤੀਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ ਜੋ ਮਸ਼ੀਨ ਦੇ ਚਾਲੂ ਜਾਂ ਬੰਦ ਹੋਣ 'ਤੇ ਕਰਨ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ। ਇਹਨਾਂ ਸਕ੍ਰਿਪਟਾਂ ਨੂੰ ਕਾਰਜ ਕਰਨ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ ਜਿਵੇਂ ਕਿ ਸੌਫਟਵੇਅਰ ਸਥਾਪਤ ਕਰਨਾ, ਸੈਟਿੰਗਾਂ ਨੂੰ ਕੌਂਫਿਗਰ ਕਰਨਾ, ਅਤੇ ਵਿੰਡੋਜ਼ ਅਪਡੇਟਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ।

## ਇੱਕ ਸਿੰਗਲ ਰੀਬੂਟ ਨਾਲ ਵਿੰਡੋਜ਼ ਅਪਡੇਟਾਂ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰਨਾ

Chocolatey, PSWindowsUpdate, ਅਤੇ ਸਟਾਰਟਅੱਪ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨ ਲਈ, ਪ੍ਰਸ਼ਾਸਕ ਹੇਠਾਂ ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹਨ।

### ਸ਼ਟਡਾਊਨ ਸਕ੍ਰਿਪਟ ਸੈੱਟਅੱਪ ਕਰ ਰਿਹਾ ਹੈ
ਤੋਂ ਸਾਰੀਆਂ ਸਹਾਇਕ ਫਾਈਲਾਂ ਨੂੰ ਡਾਊਨਲੋਡ ਕਰੋ[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. **"Win + R"** ਨੂੰ ਦਬਾ ਕੇ ਅਤੇ **"gpedit.msc"** ਤੋਂ ਬਾਅਦ **"Ctrl + Shift + Enter"** ਟਾਈਪ ਕਰਕੇ ਲੋਕਲ ਗਰੁੱਪ ਪਾਲਿਸੀ ਐਡੀਟਰ ਖੋਲ੍ਹੋ।
2. ਕੰਪਿਊਟਰ 'ਤੇ ਨੈਵੀਗੇਟ ਕਰੋ **ਸੰਰਚਨਾ\ਵਿੰਡੋਜ਼ ਸੈਟਿੰਗ\ਸਕ੍ਰਿਪਟ (ਸਟਾਰਟਅੱਪ/ਸ਼ਟਡਾਊਨ)**।
3. ਨਤੀਜੇ ਪੈਨ ਵਿੱਚ, ਬੰਦ 'ਤੇ ਦੋ ਵਾਰ ਕਲਿੱਕ ਕਰੋ।
4. PowerShell ਟੈਬ ਚੁਣੋ।
5. ਸ਼ੱਟਡਾਊਨ ਪ੍ਰਾਪਰਟੀਜ਼ ਡਾਇਲਾਗ ਬਾਕਸ ਵਿੱਚ, ਐਡ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
6. ਸਕ੍ਰਿਪਟ ਨਾਮ ਬਾਕਸ ਵਿੱਚ, ਸਕ੍ਰਿਪਟ ਦਾ ਮਾਰਗ ਟਾਈਪ ਕਰੋ, ਜਾਂ ਡੋਮੇਨ ਕੰਟਰੋਲਰ 'ਤੇ ਸ਼ੇਅਰਡ ਫੋਲਡਰ ਵਿੱਚ "*chocoautomatewindowsupdates.ps1*" ਖੋਜਣ ਲਈ ਬ੍ਰਾਊਜ਼ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।
7. ਰੀਬੂਟ ਕਰੋ।

ਹੁਣ, ਇੱਕ ਪ੍ਰਸ਼ਾਸਕ ਨੂੰ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਕਰਨ ਲਈ ਕੰਪਿਊਟਰ ਨੂੰ ਰੀਬੂਟ ਕਰਨਾ ਹੈ।

### ਲਿਪੀ ਨੂੰ ਸਮਝਣਾ

ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨ ਲਈ ਵਰਤੀ ਜਾਂਦੀ ਸਕ੍ਰਿਪਟ ਦਾ ਸਿਰਲੇਖ "*chocoautomatewindowsupdates.ps1*" ਹੈ। ਇਹ ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰਦਾ ਹੈ:

1. ਚਾਕਲੇਟ ਪੈਕੇਜ ਮੈਨੇਜਰ ਸਥਾਪਤ ਕਰਦਾ ਹੈ।
2. ਕੁਝ ਤਰਜੀਹੀ ਚਾਕਲੇਟ ਕੌਂਫਿਗਰੇਸ਼ਨ ਤਬਦੀਲੀਆਂ ਨੂੰ ਸਮਰੱਥ ਬਣਾਉਂਦਾ ਹੈ।
3. ਸਾਰੇ ਸਥਾਪਿਤ ਚਾਕਲੇਟ ਪੈਕੇਜਾਂ ਨੂੰ ਅੱਪਗ੍ਰੇਡ ਕਰਦਾ ਹੈ।
4. PSWindowsUpdate PowerShell ਮੋਡੀਊਲ ਨੂੰ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ।
5. ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਸਰਵਿਸ ਮੈਨੇਜਰ ਨੂੰ ਜੋੜਦਾ ਹੈ।
6. ਸਾਰੇ ਉਪਲਬਧ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ।
7. ਕਿਸੇ ਵੀ ਗੁੰਮ ਡ੍ਰਾਈਵਰਾਂ ਨੂੰ ਸਥਾਪਿਤ ਕਰਦਾ ਹੈ ਜਾਂ ਪਹਿਲਾਂ ਇੰਸਟਾਲ ਕੀਤੇ ਅੱਪਡੇਟਾਂ ਦੁਆਰਾ ਲੋੜੀਂਦਾ ਅੱਪਡੇਟ।

### ਵਿੰਡੋਜ਼ ਅਪਡੇਟਾਂ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰਨ ਦੇ ਲਾਭ

Chocolatey, PSWindowsUpdate, ਅਤੇ ਸਟਾਰਟਅੱਪ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨ ਦੇ ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਕਾਂ ਲਈ ਕਈ ਫਾਇਦੇ ਹਨ। ਇਹਨਾਂ ਲਾਭਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਹਨ:

- **ਸਮੇਂ ਦੀ ਬੱਚਤ**: ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨਾ ਅੱਪਡੇਟ ਕਰਨ ਲਈ ਲੋੜੀਂਦੇ ਸਮੇਂ ਦੀ ਮਾਤਰਾ ਨੂੰ ਕਾਫ਼ੀ ਘਟਾਉਂਦਾ ਹੈ। ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ ਹੁਣ ਹਰੇਕ ਮਸ਼ੀਨ 'ਤੇ ਹੱਥੀਂ ਅੱਪਡੇਟ ਸਥਾਪਤ ਕਰਨ ਦੀ ਲੋੜ ਨਹੀਂ ਹੈ।
- **ਇਕਸਾਰਤਾ**: ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟਾਂ ਨੂੰ ਆਟੋਮੈਟਿਕ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਅੱਪਡੇਟ ਸਾਰੀਆਂ ਮਸ਼ੀਨਾਂ ਵਿੱਚ ਲਗਾਤਾਰ ਸਥਾਪਤ ਕੀਤੇ ਗਏ ਹਨ। ਇਹ ਗਲਤੀਆਂ ਅਤੇ ਸੁਰੱਖਿਆ ਕਮਜ਼ੋਰੀਆਂ ਦੀ ਸੰਭਾਵਨਾ ਨੂੰ ਘਟਾਉਂਦਾ ਹੈ।
- **ਕੇਂਦਰੀਕ੍ਰਿਤ ਪ੍ਰਬੰਧਨ**: ਆਟੋਮੈਟਿਕ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ ਕੇਂਦਰੀ ਸਥਾਨ ਤੋਂ ਅੱਪਡੇਟਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਦਿੰਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਇਹ ਟਰੈਕ ਕਰਨਾ ਆਸਾਨ ਹੋ ਜਾਂਦਾ ਹੈ ਕਿ ਕਿਹੜੀਆਂ ਅੱਪਡੇਟ ਸਥਾਪਤ ਕੀਤੀਆਂ ਗਈਆਂ ਹਨ ਅਤੇ ਕਿਹੜੀਆਂ ਮਸ਼ੀਨਾਂ ਨੂੰ ਅੱਪਡੇਟ ਦੀ ਲੋੜ ਹੈ।
- **ਸੁਰੱਖਿਆ ਵਿੱਚ ਵਾਧਾ**: ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਨੂੰ ਸਵੈਚਲਿਤ ਕਰਨਾ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਮਸ਼ੀਨਾਂ ਨੂੰ ਨਵੀਨਤਮ ਸੁਰੱਖਿਆ ਪੈਚਾਂ ਨਾਲ ਅੱਪ ਟੂ ਡੇਟ ਰੱਖਿਆ ਜਾਂਦਾ ਹੈ, ਜਿਸ ਨਾਲ ਸੁਰੱਖਿਆ ਉਲੰਘਣਾਵਾਂ ਦੇ ਜੋਖਮ ਨੂੰ ਘਟਾਇਆ ਜਾਂਦਾ ਹੈ।

### ਸਿੱਟਾ

Chocolatey, PSWindowsUpdate, ਅਤੇ ਸਟਾਰਟਅੱਪ ਸਕ੍ਰਿਪਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋਏ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟ ਨੂੰ ਸਵੈਚਾਲਤ ਕਰਨਾ ਇੱਕ ਸ਼ਕਤੀਸ਼ਾਲੀ ਟੂਲ ਹੈ ਜੋ ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਕਾਂ ਦਾ ਬਹੁਤ ਸਮਾਂ ਅਤੇ ਮਿਹਨਤ ਬਚਾ ਸਕਦਾ ਹੈ। ਇਹ ਅਪਡੇਟਾਂ ਨੂੰ ਲਗਾਤਾਰ ਅਤੇ ਕੁਸ਼ਲਤਾ ਨਾਲ ਸਥਾਪਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ, ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਮਸ਼ੀਨਾਂ ਨਵੀਨਤਮ ਸੁਰੱਖਿਆ ਪੈਚਾਂ ਨਾਲ ਅੱਪ ਟੂ ਡੇਟ ਹਨ। ਇਸ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ ਦੱਸੇ ਗਏ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ, ਪ੍ਰਸ਼ਾਸਕ ਵਿੰਡੋਜ਼ ਅੱਪਡੇਟਾਂ ਨੂੰ ਸਿਰਫ਼ ਇੱਕ ਰੀਬੂਟ ਨਾਲ ਸਵੈਚਲਿਤ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਵਿੰਡੋਜ਼ ਮਸ਼ੀਨਾਂ ਨੂੰ ਅੱਪਡੇਟ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਬਹੁਤ ਤੇਜ਼ ਅਤੇ ਆਸਾਨ ਹੋ ਜਾਂਦੀ ਹੈ।

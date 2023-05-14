---
title: "HackTheBox - Wyzwanie - Kryptowaluty - Słabe RSA"
draft: false
description: "Dowiedz się, jak używać zautomatyzowanego narzędzia do ataku RSA, RsaCtfTool, aby łatwo rozwiązać wyzwanie HackTheBox Weak RSA Crypto."
tags: ["HackTheBox", "Wyzwania", "Kryptowaluta", "Słaby RSA", "RsaCtfTool", "HTB Słaby RSA Crypto", "Łatwe wyzwanie", "Szyfr RSA", "flag.enc", "key.pub", "Pakiet OpenSSL", "zautomatyzowane narzędzie do ataku RSA", "skrypt w języku python", "RsaCtfTool", "pyton3", "klucz publiczny", "uncipherfile", "Przykład flagi"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Haker kreskówki w pelerynie i masce, stojąc przed drzwiami skarbca z logo HTB na nim i trzymając narzędzie (takie jak klucz lub śrubokręt) z zielonym tle symbolizującym sukces i flagi w bańce mowy nad głową."
coverCaption: ""
---
 wyzwanie HTB Weak RSA Crypto z łatwością. W oparciu o szyfr RSA, to łatwe wyzwanie wymaga użycia zautomatyzowanego narzędzia do ataku RSA, takiego jak RsaCtfTool. Zdobądź flagę za pomocą prostego polecenia i rozszerz swoje umiejętności kryptograficzne dzięki wyzwaniom HackTheBox.

______

## Provided Files:

**Dostarczane są następujące pliki:**
- flag.enc
- key.pub

## Walk-through:

Na pierwszy rzut oka można by pomyśleć, że można odszyfrować flagę za pomocą klucza publicznego.   
W tym celu moglibyśmy użyć pakietu OpenSSL do odszyfrowania flagi.
Tym razem jest nieco inaczej i przekonasz się, że pakiet OpenSSL nie sprawdzi się w tym wyzwaniu.

Użyjemy zautomatyzowanego narzędzia do ataku RSA. Popularnym skryptem w Pythonie jest.[RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Simply put, this tool finds the flag easily for you in an automated fashion.

______

### Flag Example:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```

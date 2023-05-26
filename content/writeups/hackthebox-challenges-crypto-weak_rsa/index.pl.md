---
title: "HackTheBox - Wyzwanie - Kryptowaluty - Słabe RSA"
draft: false
description: "Dowiedz się, jak używać zautomatyzowanego narzędzia do ataku RSA, RsaCtfTool, aby łatwo rozwiązać wyzwanie HackTheBox Weak RSA Crypto."
tags: ["HackTheBox", "Wyzwania", "Kryptowaluty", "Słabe RSA", "RsaCtfTool", "HTB Słabe kryptowaluty RSA", "Łatwe wyzwanie", "Szyfr RSA", "flag.enc", "key.pub", "Pakiet OpenSSL", "Zautomatyzowane narzędzie do ataków RSA", "skrypt python", "RsaCtfTool", "python3", "klucz publiczny", "uncipherfile", "Przykład flagi"]
toc: true
cover: "/img/cover/A_cartoon_hacker_wearing_a_cape_and_a_mask_standing.png"
coverAlt: "Haker z kreskówki w pelerynie i masce, stojący przed drzwiami skarbca z logo HTB i trzymający narzędzie (takie jak klucz lub śrubokręt) z zielonym tłem symbolizującym sukces i flagą w dymku nad głową."
coverCaption: ""
---
 HTB Weak RSA Crypto challenge z łatwością. Oparte na szyfrze RSA, to łatwe wyzwanie wymaga użycia zautomatyzowanego narzędzia do ataku RSA, takiego jak RsaCtfTool. Zdobądź flagę za pomocą prostego polecenia i poszerz swoje umiejętności kryptograficzne dzięki wyzwaniom HackTheBox.

______

## Dostarczone pliki:

**Dostarczane są następujące pliki:**
- flag.enc
- key.pub

## Walk-through:

Na pierwszy rzut oka można by pomyśleć, że można odszyfrować flagę za pomocą klucza publicznego.   
W tym celu możemy użyć pakietu OpenSSL do odszyfrowania flagi.
Tym razem jest nieco inaczej i okaże się, że pakiet OpenSSL nie zadziała w tym wyzwaniu.

Użyjemy zautomatyzowanego narzędzia do ataku RSA. Popularnym skryptem Pythona jest [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

```bash
python3 RsaCtfTool.py --publickey ./key.pub --uncipherfile ./flag.enc 
```
  
Mówiąc najprościej, narzędzie to z łatwością wyszukuje flagę w sposób zautomatyzowany.

______

### Przykład flagi:
```
HTB{XXXXXX_XXXXXXX_XXXXXX}
```

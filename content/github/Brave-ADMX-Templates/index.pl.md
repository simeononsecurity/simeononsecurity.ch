---
title: "Przejmij kontrolę nad polityką przeglądarki Brave za pomocą BraveADMX - zmodyfikowane szablony ADMX"
date: 2020-07-25
---


Brave, jako firma, nie wydała szablonów ADMX dla przeglądarki Brave, popychając czyste rejestry jako jedyną obsługiwaną opcję.
Ponieważ przeglądarka Brave jest zbudowana na bazie Chromium, powinna wspierać większość, jeśli nie wszystkie, te same zasady z szablonów ADMX Chromium i Google Chrome.
Mając to na uwadze, zmodyfikowaliśmy szablony Google Chrome ADMX, aby odzwierciedlały ścieżkę rejestru przeglądarki Brave. Po kilku wstępnych problemach i testach, szablony wydają się działać.

**Te definicje polityki są w stanie Pre-Alpha. Powinny być używane tylko do celów testowych**.

## Pobierz wymagane pliki.

**Pobierz wymagane pliki ze strony[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Notes

Zmodyfikowane definicje polityki Google Chrome zgodnie z:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Uwaga:** Zastąpiono "HKEY_LOCAL_MACHINE\Software\Software\Software\Software\Software\Software\Software\Software\Software"

**Uwaga:** Nie należy instalować szablonów ADMX SOS'es Chromium i Brave Browser w tym samym czasie.

## Jak zainstalować

1.) Skopiuj wszystkie pliki oprócz readme.md do "C:indowsPolicyDefinitions" i/lub "™domain.tlddomainPolicyDefinitions".

2.) Zysk?
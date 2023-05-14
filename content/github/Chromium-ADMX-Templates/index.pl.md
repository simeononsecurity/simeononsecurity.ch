---
title: "ChromiumADMX: Właściwy szablon ADMX dla przeglądarki Chromium"
date: 2020-07-25
---


Prawidłowy szablon ADMX dla przeglądarki Chromium

Chromium, jako firma, nie wydała szablonów ADMX dla przeglądarki Chromium, które mogą być zainstalowane w tym samym czasie co szablony Google Chrome.
Mając to na uwadze, zmodyfikowaliśmy szablony ADMX Google Chrome, aby odzwierciedlały ścieżkę rejestru przeglądarki Chromium i umieściliśmy je w tandumie w folderze Google ADMX w GPO.

**Te definicje polityki są w stanie Pre-Alpha. Powinny być używane tylko do celów testowych**.

## Pobierz wymagane pliki

**Pobierz wymagane pliki z[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Notes

Zmodyfikowane definicje polityki Google Chrome zgodnie z:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Uwaga:** Zastąpiono "HKEY_LOCAL_MACHINE\Software\Policies\Chrome" przez "HKEY_LOCAL_MACHINE\Software\Policies\Chrom".

**Uwaga:** Nie instaluj szablonów ADMX SOS'es Chromium i Brave Browser w tym samym czasie.

## Jak zainstalować

1.) Skopiuj wszystkie pliki oprócz readme.md do "C:indowsPolicyDefinitions" i/lub "™domain.tlddomainPolicyDefinitions".

2.) Zysk?





---
title: "ChromiumADMX: Prawidłowy szablon ADMX dla przeglądarki Chromium"
date: 2020-07-25
---


Prawidłowy szablon ADMX dla przeglądarki Chromium

Chromium, jako firma, nie wydała szablonów ADMX dla przeglądarki Chromium, które można zainstalować w tym samym czasie, co szablony Google Chrome.
Mając to na uwadze, zmodyfikowaliśmy szablony Google Chrome ADMX, aby odzwierciedlały ścieżkę rejestru przeglądarki Chromium i umieściliśmy je w tandumie w folderze Google ADMX w GPO.

**Te definicje zasad są w stanie Pre-Alpha. Powinny być używane wyłącznie do celów testowych**

## Pobierz wymagane pliki

**Pobierz wymagane pliki ze strony [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Uwagi

Zmodyfikowane definicje zasad Google Chrome zgodnie z:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Uwaga:** Zastąpiono "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" przez "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\".

**Uwaga:** Nie instaluj jednocześnie szablonów SOS'es Chromium i Brave Browser ADMX.

## Jak zainstalować

1.) Skopiuj wszystkie pliki z wyjątkiem readme.md do "C:\Windows\PolicyDefinitions" i/lub "\\domain.tld\domain\Policies\PolicyDefinitions".

2.) Zysk?





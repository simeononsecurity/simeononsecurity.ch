---
title: "ChromiumADMX: șablon ADMX adecvat pentru browserul Chromium"
date: 2020-07-25
---


Șablon ADMX adecvat pentru browserul Chromium

Chromium, ca companie, nu a reușit să lanseze șabloanele ADMX pentru browserul Chromium, care pot fi instalate în același timp cu șabloanele Google Chrome.
Având în vedere acest lucru, am modificat șabloanele Google Chrome ADMX pentru a reflecta calea de registru a browserului Chromium și am plasat în tandem în folderul Google ADMX din GPO.

**Aceste definiții de politică sunt într-o stare Pre-Alfa. Acestea ar trebui să fie utilizate numai în scopuri de testare**

## Descărcați fișierele necesare

**Descărcați fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Note

Definiții ale politicii Google Chrome modificate conform:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Notă:** S-a înlocuit „HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome” cu „HKEY_LOCAL_MACHINE\Software\Policies\Chromium\”

**Notă:** Nu instalați șabloanele SOS Chromium și Brave Browser ADMX în același timp.

## Cum să instalați

1.) Copiați toate fișierele cu excepția readme.md în „C:\Windows\PolicyDefinitions” și/sau „\\\domain.tld\domain\Policies\PolicyDefinitions”

2.) Profit?





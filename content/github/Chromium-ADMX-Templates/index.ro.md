---
title: "CromADMX: Șablon ADMX adecvat pentru browserul Chromium"
date: 2020-07-25
---


Șablon ADMX adecvat pentru browserul Chromium

Compania Chromium nu a reușit să lanseze șabloane ADMX pentru browserul Chromium, care pot fi instalate în același timp cu șabloanele Google Chrome.
Ținând cont de acest lucru, am modificat șabloanele ADMX pentru Google Chrome pentru a reflecta calea de înregistrare a browserului Chromium și le-am plasat in tandum în dosarul Google ADMX din GPO.

**Aceste definiții de politici se află într-o stare Pre-Alpha. Acestea ar trebui să fie utilizate numai în scopuri de testare**

## Descărcați fișierele necesare

**Download the required files from the [GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Note

Definiții modificate ale politicii Google Chrome Policy Definitions în conformitate cu:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Nota:** A înlocuit "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" cu "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\"

**Nota:** Nu instalați șabloanele SOS'es Chromium și Brave Browser ADMX în același timp.

## Cum se instalează

1.) Copiați toate fișierele, cu excepția readme.md, în "C:\Windows\PolicyDefinitions" și/sau "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Profit?





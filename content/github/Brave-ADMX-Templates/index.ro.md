---
title: "Preluați controlul asupra politicilor Brave Browser cu BraveADMX - Șabloane ADMX modificate"
date: 2020-07-25
---


Brave, ca companie, nu a reușit să lanseze șabloane ADMX pentru site-ul de browser curajos, împingând registrele pure ca singura opțiune acceptată.
Deoarece Brave Browser este construit din Chromium, ar trebui să accepte majoritatea, dacă nu toate, aceleași politici din șabloanele Chromium și Google Chrome ADMX.
Având în vedere acest lucru, am modificat șabloanele Google Chrome ADMX pentru a reflecta calea de registru a browserului Brave. După câteva depanări și teste inițiale, șabloanele par să funcționeze.

**Aceste definiții de politică sunt într-o stare Pre-Alfa. Acestea ar trebui să fie utilizate numai în scopuri de testare**

## Descărcați fișierele necesare.

**Descărcați fișierele necesare din[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Note

Definiții ale politicii Google Chrome modificate conform:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Notă:** S-a înlocuit „HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome” cu „HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave”

**Notă:** Nu instalați șabloanele SOS Chromium și Brave Browser ADMX în același timp.

## Cum să instalați

1.) Copiați toate fișierele cu excepția readme.md în „C:\Windows\PolicyDefinitions” și/sau „\\\domain.tld\domain\Policies\PolicyDefinitions”

2.) Profit?
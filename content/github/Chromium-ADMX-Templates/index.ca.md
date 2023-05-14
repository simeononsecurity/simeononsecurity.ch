---
title: "ChromiumADMX: plantilla ADMX adequada per al navegador Chromium"
date: 2020-07-25
---


Plantilla ADMX adequada per al navegador Chromium

Chromium, com a empresa, no ha pogut llançar plantilles ADMX per al navegador Chromium que es poden instal·lar alhora que les plantilles de Google Chrome.
Tenint això en compte, hem modificat les plantilles ADMX de Google Chrome per reflectir la ruta del registre del navegador Chromium i les hem col·locat en tandum a la carpeta Google ADMX a GPO.

**Aquestes definicions de polítiques es troben en un estat prealfa. Només s'han d'utilitzar amb finalitats de prova**

## Baixeu els fitxers necessaris

** Baixeu els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Notes

Definicions de la política de Google Chrome modificades segons:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Nota:** S'ha substituït "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" per "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\"

**Nota:** No instal·leu les plantilles de SOS Chromium i Brave Browser ADMX alhora.

## Com instal · lar

1.) Copieu tots els fitxers excepte readme.md a "C:\Windows\PolicyDefinitions" i/o "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Guanys?





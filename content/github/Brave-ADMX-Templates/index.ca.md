---
title: "Preneu el control de les polítiques del navegador Brave amb BraveADMX - Plantilles ADMX modificades"
date: 2020-07-25
---


Brave, com a empresa, no ha pogut llançar plantilles ADMX per a la web del navegador valent, impulsant els registres purs com a única opció compatible.
Com que el navegador Brave es construeix a partir de Chromium, hauria de suportar la majoria, si no totes, les mateixes polítiques de les plantilles de Chromium i Google Chrome ADMX.
Tenint això en compte, hem modificat les plantilles ADMX de Google Chrome per reflectir la ruta de registre del navegador Brave. Després d'algunes proves i resolució de problemes inicials, les plantilles semblen funcionar.

**Aquestes definicions de polítiques es troben en un estat prealfa. Només s'han d'utilitzar amb finalitats de prova**

## Baixeu els fitxers necessaris.

** Baixeu els fitxers necessaris des del[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Notes

Definicions de la política de Google Chrome modificades segons:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Nota:** S'ha substituït "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" per "HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave"

**Nota:** No instal·leu les plantilles de SOS Chromium i Brave Browser ADMX alhora.

## Com instal · lar

1.) Copieu tots els fitxers excepte readme.md a "C:\Windows\PolicyDefinitions" i/o "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Guanys?
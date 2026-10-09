---
title: "Automatitza l'Activació KMS de Windows amb l'Script GLVK"
date: 2020-12-18
toc: true
draft: false
description: Simplifica el procés d'activació KMS de Windows 10 i Windows 11 amb l'Script d'Instal·lació Automàtica GLVK de SimeonOnSecurity, i aprèn més sobre KMS i les claus client GLVK a partir de la lectura recomanada de Microsoft.
tags:
- Activació de Windows
- Claus Client KMS
- GLVK
- Actualitzacions de Windows
- Compliment
- Script de Powershell
- Servei de Gestió de Claus
- Llicències per Volum
- Activació Empresarial
- Servidor de Gestió de Claus
- Automatització
- Productes Microsoft
- Sistema Operatiu
- Programari
- Entorns Empresarials
- Powershell Administratiu
- Repositori GitHub
- Scripting
- Ciberseguretat
- SimeonOnSecurity
- activació KMS
- Script d'Instal·lació Automàtica GLVK
- productes Windows
- empresa
- gestió centralitzada
- estalvi de temps
- administració IT
- activació simplificada
- sense complicacions
- productivitat
- reducció d'errors
- capacitats de monitoratge
- eficiència
- activació de programari
- clau de llicència per volum
- automatització d'scripts
- gestió IT
- procés d'activació
- llicenciament de programari
- gestió de llicències
- eina d'activació
- desplegament de programari
- productivitat IT
cover: /img/cover/KMS-Auto-PS.webp
coverAlt: Un servidor futurista envoltat d'ordinadors clients brillants, il·lustrant l'activació KMS en un entorn fosc amb colors vius. L'escena destaca la connectivitat digital i la tecnologia moderna.
coverCaption: ''
lastmod: 2026-10-08
---

**Script d'Instal·lació Automàtica GLVK per a l'Activació KMS**

*Lectura Recomanada:* [Microsoft - Claus Client KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Introducció

L'activació KMS (Servei de Gestió de Claus) és un mètode utilitzat per Microsoft per activar i llicenciar els seus productes en entorns empresarials. El procés implica un servidor central que activa els ordinadors clients assignant-los una clau de llicència per volum anomenada GLVK (Clau de Llicència per Volum Genèrica).

En aquest article, explorarem l'Script d'Instal·lació Automàtica GLVK, que simplifica el procés d'activació dels productes Windows mitjançant KMS. Proporcionarem instruccions pas a pas sobre com executar l'script i destacarem els seus beneficis per a les organitzacions.

## Lectura Recomanada

Abans d'endinsar-se en l'Script d'Instal·lació Automàtica GLVK, es recomana familiaritzar-se amb el concepte de KMS i les claus client KMS disponibles proporcionades per Microsoft. Podeu consultar la següent documentació de Microsoft per a més informació:

- [Microsoft - Claus Client KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Com Executar l'Script

### Instal·lació Manual

Per instal·lar i executar manualment l'Script d'Instal·lació Automàtica GLVK, seguiu aquests passos:

1. Descarregueu l'script i els fitxers relacionats des del [Repositori GitHub](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip).
2. Obriu una sessió de PowerShell amb privilegis administratius.
3. Navegueu fins al directori que conté tots els fitxers descarregats.
4. Executeu les següents comandes:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

Aquestes comandes configuraran la política d'execució a RemoteSigned per permetre l'execució d'scripts, desbloquejaran qualsevol script de PowerShell descarregat i executaran l'Script d'Instal·lació Automàtica GLVK.

## Beneficis de l'Script d'Instal·lació Automàtica GLVK

L'Script d'Instal·lació Automàtica GLVK ofereix diversos avantatges per a les organitzacions que volen activar productes Windows mitjançant KMS:

1. **Activació Simplificada**: L'script automatitza el procés d'activació KMS, eliminant la necessitat de configuració manual i reduint els errors humans.

2. **Estalvi de Temps i Esforç**: Utilitzant l'script, els administradors IT poden estalviar un temps i esforç significatius que d'altra manera es dedicarien a procediments manuals d'activació per a múltiples equips.

3. **Gestió Centralitzada**: L'Script d'Instal·lació Automàtica GLVK permet una gestió centralitzada de l'activació KMS, oferint millor control i capacitats de monitoratge.

## Conclusió

L'Script d'Instal·lació Automàtica GLVK és una eina valuosa per a organitzacions que busquen un mètode eficient i simplificat per activar productes Windows mitjançant KMS. Automatitzant el procés d'activació, estalvia temps, redueix errors i millora les capacitats de gestió centralitzada. Amb les instruccions pas a pas proporcionades, les organitzacions poden implementar fàcilment l'script i gaudir dels beneficis d'una activació KMS sense complicacions.

## Referències

1. [Microsoft - Claus Client KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)
2. [Repositori GitHub - Script d'Instal·lació Automàtica GLVK](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)

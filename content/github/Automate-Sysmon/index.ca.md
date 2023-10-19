---
title: "Automate-Sysmon: simplifica el desplegament i la configuració de Sysmon"
date: 2021-05-11
toc: true
draft: false
description: "Apreneu a implementar i configurar Sysmon per millorar la seguretat del vostre sistema amb l'script Automate-Sysmon, que simplifica el procés fins i tot per als usuaris novells."
tags: ["Automatitzar Sysmon", "Com automatitzar Sysmon", "Com automatitzar la configuració de Sysmon", "Com instal·lar Sysmon", "Powershell", "Guió", "Desplegament de Sysmon", "Configuració Sysmon", "Registre de Sysmon", "Detecció d'amenaces", "Activitat maliciosa", "SwiftOnSecurity sysmon-config", "Microsoft Sysinternals", "Repositori GitHub", "BHIS", "Monitorització del sistema", "Recerca de seguretat", "Creació de processos", "Connexions de xarxa"]
---

Automate-Sysmon és un script útil que simplifica el desplegament i la configuració de Sysmon, una potent eina de supervisió del sistema de Microsoft Sysinternals. En automatitzar la instal·lació i la configuració de Sysmon, aquest script augmenta les capacitats de registre del vostre sistema i millora les capacitats de detecció d'amenaces.

## Què és Sysmon?

Sysmon és una eina de supervisió del sistema que es pot utilitzar per detectar activitats malicioses en un sistema. Proporciona informació detallada sobre la creació de processos, les connexions de xarxa i altres esdeveniments del sistema, cosa que el converteix en una eina inestimable per als professionals de la seguretat. Tot i que Sysmon és una eina potent, pot ser difícil de configurar i configurar.

## Com pot ajudar Automate-Sysmon?

L'script Automate-Sysmon facilita la instal·lació i la configuració de Sysmon, fins i tot per a aquells que no tenen molta experiència. L'script utilitza el popular mòdul **SwiftOnSecurity/sysmon-config**, que proporciona un conjunt de regles preconfigurades per a Sysmon. Aquesta configuració es basa en anys d'investigació de seguretat i la comunitat l'actualitza regularment.

Amb Automate-Sysmon, podeu automatitzar tot el procés amb una sola ordre o instal·lar manualment Sysmon seguint les instruccions proporcionades. Aquesta flexibilitat facilita als usuaris personalitzar la instal·lació i la configuració per satisfer les seves necessitats específiques.

## Com utilitzar Automate-Sysmon?

Hi ha dues maneres d'utilitzar Automate-Sysmon:

### Instal·lació automàtica:

Per utilitzar la instal·lació automatitzada, només cal que executeu l'ordre següent a PowerShell:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosautomatesysmon.ps1'|iex
```

This will automatically download and run the Automate-Sysmon script.

### Manual Install:

If you prefer to install Sysmon manually, follow these steps:

1. Download the script and other required files from the [GitHub repository](https://github.com/simeononsecurity/Automate-Sysmon).
2. Launch PowerShell with administrator privileges.
3. Navigate to the directory containing the downloaded files.
4. Run the following command to change the PowerShell execution policy: ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force```
5. Unblock all the script files by running the following command: ```Get-ChildItem -Recurse *.ps1 | Unblock-File```
6. Run the following command to launch the Automate-Sysmon script: ```.\sos-automate-sysmon.ps1```


## Conclusió

En conclusió, Automate-Sysmon és una eina essencial per als professionals de la seguretat que volen augmentar les seves habilitats de registre i millorar les capacitats de detecció d'amenaces del seu sistema. Amb la capacitat d'automatitzar el desplegament i la configuració de Sysmon, aquesta eina pot ajudar fins i tot als usuaris novells a treure el màxim profit de Sysmon. Mitjançant l'ús del mòdul **simeononsecurity/Automate-Sysmon**, els usuaris poden beneficiar-se de l'experiència de la comunitat i mantenir-se al dia amb les darreres investigacions de seguretat. Per tant, si voleu millorar la seguretat del vostre sistema, proveu Automate-Sysmon!




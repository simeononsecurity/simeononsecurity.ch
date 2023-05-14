---
title: "Automatitzeu l'activació de Windows KMS amb GLVK Script"
date: 2020-12-18
toc: true
draft: false
description: "Simplifica el procés d'activació del KMS de Windows 10 mitjançant l'script d'instal·lació automàtica GLVK de SimeonOnSecurity i obteniu més informació sobre les claus de client KMS i GLVK a partir de la lectura recomanada de Microsoft."
tags: ["Activació de Windows", "Claus de client KMS", "GLVK", "Actualitzacions de Windows", "Compliment", "Script Powershell", "Servei de gestió de claus", "Llicències per volum", "Activació empresarial", "Servidor de gestió de claus", "Automatització", "Productes de Microsoft", "Sistema operatiu", "Programari", "Entorns empresarials", "Powershell administratiu", "Repositori GitHub", "Guió", "Seguretat cibernètica", "SimeonOnSecurity"]
---

Script d'instal·lació automàtica de GLVK per a l'activació de KMS

## Lectura recomanada:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Com executar l'script:
### Instal·lació manual:
Si es descarrega manualment, l'script s'ha de llançar des d'un powershell administratiu al directori que conté tots els fitxers del[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

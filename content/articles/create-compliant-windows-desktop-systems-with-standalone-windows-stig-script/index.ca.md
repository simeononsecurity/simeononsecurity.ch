---
title: "Standalone-Windows-STIG-Script: crea un PC conforme"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "Guia pas a pas per fer servir Standalone-Windows-STIG-Script en sistemes Windows conformes, amb paràmetres i passos de verificació."
tags: ["Script STIG", "Seguretat de Windows", "Sistema Windows conforme", "Reforç del sistema", "STIG de Windows", "Windows segur", "Compliment de Windows", "Instal·lació manual", "Actualitzacions de Windows", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Tallafoc de Windows", "Mesures de mitigació", "Nessus PID", "VMware Horizon", "Reforç opcional"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "Il·lustració d'una pantalla d'ordinador amb una interfície de compliment de seguretat, barres de progrés dinàmiques i fluxos de dades sobre un fons blau marí fosc amb accents vius."
coverCaption: ""
---

Els sistemes Windows s'utilitzen àmpliament en empreses, organitzacions i també a les llars. Amb l'augment dels ciberatacs, cal assegurar-se que aquests sistemes siguin segurs i compleixin els estàndards del sector. Standalone-Windows-STIG-Script és una eina útil per aconseguir-ho. Aquest article explica què és, com funciona i com fer-la servir per crear un sistema Windows segur i conforme.

## Què és Standalone-Windows-STIG-Script?

**Standalone-Windows-STIG-Script** és un script desenvolupat per Simeononsecurity per automatitzar la seguretat d'un sistema Windows segons la Security Technical Implementation Guide (STIG). És de codi obert i està disponible a **GitHub**.

## Com funciona?

Standalone-Windows-STIG-Script aplica les directrius de la STIG per protegir un sistema Windows. Es pot executar en un sistema Windows i aplicarà els canvis necessaris per complir la STIG. Inclou diverses mesures de seguretat, com ara:

- Polítiques de comptes
- Polítiques d'auditoria
- Opcions de seguretat
- Configuració del tallafoc
- Configuració dels serveis

## Avantatges d'utilitzar Standalone-Windows-STIG-Script:

- **Automatització**: l'script automatitza la protecció d'un sistema Windows, estalvia temps i redueix la possibilitat d'errors humans.

- **Compliment**: l'script aplica les directrius de la STIG i ajuda a ajustar el sistema Windows als estàndards del sector.

- **Tranquil·litat**: amb Standalone-Windows-STIG-Script, pots tenir més confiança en la seguretat del teu sistema Windows i en el seu compliment dels estàndards.

_________________________________________________________________________________________________________________________

## Com utilitzar Standalone-Windows-STIG-Script:

1. Fer servir Standalone-Windows-STIG-Script és relativament senzill. Aquests són els passos:

2. **Baixa l'script**: està disponible a GitHub a https://github.com/simeononsecurity/Standalone-Windows-STIG-Script. Baixa'l i desa'l al sistema Windows.

3. **Obre un símbol del sistema amb privilegis elevats**: fes clic amb el botó dret al botó Inici de Windows i selecciona "Windows PowerShell (Admin)".

4. **Executa l'script**: ves a la ubicació on l'has desat i introdueix l'ordre següent:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. Revisa els canvis: quan l'script hagi acabat, comprova els canvis aplicats al sistema per assegurar-te que tot està configurat correctament.

## Conclusió:

Standalone-Windows-STIG-Script és una eina útil per protegir el sistema Windows i ajustar-lo als estàndards del sector. L'script automatitza el procés i aplica les directrius de la STIG. Si vols crear un sistema Windows segur i conforme, considera fer servir Standalone-Windows-STIG-Script.

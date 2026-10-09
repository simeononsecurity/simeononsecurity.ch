---
title: "PowerShell DSC: Una Guia Inicial"
date: 2023-04-02
toc: true
draft: false
description: Explora el poder de PowerShell Desired State Configuration (DSC) per automatitzar i gestionar configuracions de sistema per a un entorn segur i complidor.
tags:
- PowerShell
- DSC
- Gestió de Configuració
- Automatització
- Windows
- Administració de Sistemes
- Millors Pràctiques
- Compliment
- Seguretat
- Infraestructura
- DevOps
- Configuració de Servidors
- Proves
- Git
- Control de Versions
- Regulacions Governamentals
- NIST
- CIS
- Deriva de Configuració
- Recursos Personalitzats
cover: /img/cover/a-guide-to-using-powershell-desired-state-configuration-dsc-for-configuration-management.webp
coverAlt: Una il·lustració amb un terminal PowerShell estilitzat amb símbols abstractes al seu voltant, que representen la gestió de configuració i l'automatització, sobre un fons blau marí intens.
coverCaption: ''
lastmod: 2026-10-08
---

**Una Guia per Utilitzar PowerShell Desired State Configuration (DSC) per a la Gestió de Configuració**

______

## Introducció

PowerShell Desired State Configuration (**DSC**) és una eina potent i **essencial** per a administradors IT i professionals DevOps, que els permet automatitzar el desplegament i la configuració de sistemes Windows i Linux. Aquest article ofereix una guia completa per utilitzar PowerShell DSC per a la gestió de configuració, incloent millors pràctiques, regulacions governamentals i referències útils.

______

## Començant amb PowerShell Desired State Configuration

### Què és PowerShell Desired State Configuration?

PowerShell Desired State Configuration (**DSC**) és un **llenguatge declaratiu** integrat a PowerShell que permet als administradors automatitzar la configuració de sistemes, aplicacions i serveis. Proporciona una manera **estandarditzada i consistent** de gestionar configuracions i assegurar que els sistemes es mantinguin en l'estat desitjat.

### Instal·lació de PowerShell DSC

Per començar amb PowerShell DSC, necessitaràs instal·lar el **Windows Management Framework (WMF)**. WMF és un paquet que inclou PowerShell, DSC i altres eines de gestió essencials. Pots descarregar l'última versió de WMF des del [Centre de Descàrregues de Microsoft](https://www.microsoft.com/en-us/download/details.aspx?id=54616).

______

## Creació i Aplicació de Configuracions DSC

### Escriure Configuracions DSC

Una configuració DSC és un **script de PowerShell** que descriu l'estat desitjat d'un sistema. Consisteix en un o més **recursos DSC** que defineixen les configuracions i propietats requerides pels components del sistema. Aquí tens un exemple d'una configuració DSC senzilla que instal·la el rol de Servidor Web (IIS) en un servidor Windows:

```powershell
Configuration InstallIIS {
    Import-DscResource -ModuleName PSDesiredStateConfiguration

    Node 'localhost' {
        WindowsFeature IIS {
            Ensure = 'Present'
            Name   = 'Web-Server'
        }
    }
}
```
### Aplicar Configuracions DSC
Un cop hagis escrit una configuració DSC, pots aplicar-la a un sistema objectiu utilitzant el cmdlet **Start-DscConfiguration**. Primer, compila l'script de configuració executant-lo a PowerShell:

```powershell
InstallIIS
```

Això generarà un fitxer **MOF** (Managed Object Format) que conté la configuració compilada. A continuació, aplica la configuració al sistema objectiu amb la comanda següent:

```powershell
Start-DscConfiguration -Path .\InstallIIS -Wait -Verbose
```

## Millors Pràctiques per Utilitzar PowerShell DSC

### Modularitza les Teves Configuracions

Crea configuracions **modulars i reutilitzables** separant els diferents components de la teva infraestructura en **recursos DSC individuals**. Aquest enfocament et permetrà **mantenir i escalar** fàcilment les configuracions a mesura que el teu entorn creixi.

### Utilitza Control de Versions

Sempre desa les teves configuracions DSC i recursos personalitzats en un **sistema de control de versions** com Git. Aquesta pràctica et permetrà fer seguiment dels canvis, col·laborar amb l'equip i revertir fàcilment a versions anteriors de les configuracions quan sigui necessari.

### Prova les Teves Configuracions

**Provar** és un aspecte crucial de la gestió de configuració. Abans de desplegar una configuració DSC, prova-la en un **entorn no productiu** per assegurar-te que funciona com s'espera i no introdueix conseqüències no desitjades. També pots utilitzar eines com [Pester](https://github.com/pester/Pester) per a proves automatitzades de les teves configuracions DSC.

______

## Regulacions i Directrius Governamentals

### Directrius NIST

El National Institute of Standards and Technology (NIST) proporciona directrius per a la gestió de configuració de sistemes. En particular, la publicació [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) conté una secció (CM-2) sobre Configuracions Base, que és rellevant per a l'ús de DSC. Les directrius destaquen la importància de mantenir, monitoritzar i controlar els canvis en les configuracions de sistema. PowerShell DSC pot ajudar les organitzacions a complir aquestes directrius proporcionant una manera consistent i automatitzada de gestionar configuracions de sistema.

### Federal Information Security Management Act (FISMA)

La Federal Information Security Management Act [FISMA](https://www.dhs.gov/cisa/federal-information-security-modernization-act) exigeix que les agències federals implementin un marc integral per assegurar l'efectivitat dels seus controls de seguretat de la informació. La gestió de configuració és un component clau per al compliment de FISMA, i PowerShell DSC pot jugar un paper essencial ajudant les organitzacions a complir aquests requisits.
______

## Conclusió

PowerShell Desired State Configuration (DSC) és una eina potent i flexible per automatitzar el desplegament i la gestió de configuracions de sistema. Seguint les millors pràctiques i complint les regulacions governamentals, pots assegurar que els sistemes de la teva organització es mantinguin en l'estat desitjat mentre es manté el compliment normatiu. No oblidis aprofitar els recursos proporcionats en aquest article per millorar la teva comprensió de PowerShell DSC i optimitzar els teus processos de gestió de configuració.
______

## Referències

- [Documentació oficial de PowerShell Desired State Configuration (DSC)](https://learn.microsoft.com/en-us/powershell/dsc/getting-started/wingettingstarted?view=dsc-1.1)
- [NIST SP 800-53 - Controls de Seguretat i Privacitat per a Sistemes i Organitzacions Federals](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf)
- [Federal Information Security Management Act (FISMA)](https://www.dhs.gov/cisa/federal-information-security-modernization-act)
- [Pester - Marc de Proves per PowerShell](https://github.com/pester/Pester)
- [Guia per a Principiants sobre l'Ús de Xifrat per a la Protecció de Dades](https://simeononsecurity.com/articles/a-beginners-guide-to-using-encryption-for-data-protection/)
- [Millors Pràctiques per Instal·lar Pegats de Seguretat a Windows](https://simeononsecurity.com/articles/best-practices-for-installing-security-patches-on-windows/)

---
title: "PowerShell per a la ciberseguretat: automatització i defensa"
date: 2023-02-02
lastmod: 2026-11-24
toc: true
draft: false
description: "Descobriu com PowerShell millora les operacions de ciberseguretat i ajuda a complir els estàndards del sector mitjançant l’automatització i processos més simples."
tags: ["PowerShell", "Ciberseguretat", "Operacions", "Compliment", "Automatització", "Requisits STIG SRG", "Guia NSACyber", "Sistemes Windows", "Defensa de l’equip blau", "Scripts", "Eines", "Projectes C Sharp"]
cover: "/img/cover/A_person_typing_on_a_keyboard_with_a_background_of_computer.webp"
coverAlt: "Una persona escriu amb un teclat davant de servidors informàtics i cables de xarxa, una imatge de l’ús de PowerShell en operacions de ciberseguretat i compliment."
coverCaption: ""
---

## Introducció:

PowerShell és un llenguatge de scripts potent i versàtil que ha guanyat popularitat en l’àmbit de la ciberseguretat. És un intèrpret de línia d’ordres basat en tasques i un llenguatge de scripts construït sobre .NET, dissenyat per automatitzar tasques administratives i simplificar processos complexos. El seu ús en operacions de ciberseguretat i compliment creix perquè automatitza i simplifica tasques rutinàries, cosa que permet als equips de seguretat centrar-se en activitats més importants.

## Avantatges del PowerShell per a les operacions de ciberseguretat i compliment:

PowerShell és un llenguatge de scripts potent i versàtil que ha guanyat popularitat en l’àmbit de la ciberseguretat. És un intèrpret de línia d’ordres basat en tasques i un llenguatge de scripts sobre .NET, dissenyat per automatitzar tasques administratives i simplificar processos complexos.

### Automatització i simplificació de tasques rutinàries:

Un dels principals avantatges del **PowerShell** és que pot automatitzar tasques rutinàries, estalviar temps i reduir el risc d’errors humans. Els scripts del PowerShell poden automatitzar aspectes diversos de les operacions de ciberseguretat, com ara actualitzar regles del tallafoc, supervisar el trànsit de xarxa i cercar vulnerabilitats. Això estalvia temps i ajuda a fer les tasques de manera coherent i precisa.

### Més visibilitat i control:

Un altre avantatge del **PowerShell** és que ofereix més visibilitat i control dels sistemes i les xarxes. Els administradors poden supervisar i gestionar dispositius i sistemes des d’un punt central, cosa que ajuda a identificar i reduir amenaces. Automatitzar tasques de seguretat amb scripts del PowerShell també ajuda les organitzacions a complir normes del sector, com els requisits [STIG/SRG](https://simeononsecurity.com/github/stiging-standalone-windows-servers/) del Departament de Defensa i les directrius de ciberseguretat de l’NSA.

### Integració amb altres eines:

El **PowerShell** s’integra bé amb eines de seguretat com el programari antivirus, els sistemes de detecció d’intrusions i els tallafocs. Això permet automatitzar tasques, millorar l’eficiència i reunir informació de diverses fonts en un punt central. Els scripts també poden automatitzar el desplegament i la configuració d’eines de seguretat perquè es configurin de manera coherent i precisa.

### Personalització i escalabilitat:

La flexibilitat del **PowerShell** permet personalitzar-lo i ampliar-ne l’ús, i el fa adequat per a organitzacions de qualsevol mida. Serveix tant per a tasques senzilles d’una sola vegada com per a processos complexos de diversos passos. Aquesta flexibilitat és útil per adaptar-se a requisits de seguretat canviants i gestionar infraestructures grans i complexes.

## Exemples pràctics de seguretat

Microsoft documenta diversos controls de seguretat del PowerShell, com ara el registre de mòduls i blocs de script, la integració amb AMSI, el mode de llenguatge restringit i el control d’aplicacions. Llegiu la [documentació de les funcions de seguretat del PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/security/security-features?view=powershell-7.5) abans de triar un control. La directiva d’execució és una funció de seguretat de Windows, no una frontera completa de control d’aplicacions.

### Comprovar les signatures dels scripts

Feu servir `Get-AuthenticodeSignature` abans d’executar un script rebut d’un altre administrador o sistema. Una signatura vàlida confirma la confiança en l’editor només quan la cadena de certificats i la política de signatura també compleixen els vostres requisits.

```powershell
$signature = Get-AuthenticodeSignature -FilePath .\Maintenance.ps1

if ($signature.Status -ne 'Valid') {
    throw "Estat de la signatura de l'script: $($signature.Status)"
}
```

### Habilitar el registre dels blocs de script

El registre dels blocs de script desa les ordres, els blocs, les funcions i els scripts al registre Microsoft-Windows-PowerShell/Operational. Habiliteu-lo amb la directiva de grup o un sistema aprovat de gestió de configuració, i després confirmeu que el SIEM recull els esdeveniments.

```powershell
$policyPath = 'HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging'
New-Item -Path $policyPath -Force | Out-Null
New-ItemProperty -Path $policyPath -Name EnableScriptBlockLogging -PropertyType DWord -Value 1 -Force | Out-Null
```

### Revisar el mode de llenguatge i el registre

```powershell
$ExecutionContext.SessionState.LanguageMode
Get-WinEvent -LogName 'Microsoft-Windows-PowerShell/Operational' -MaxEvents 20
```

El mode de llenguatge restringit limita l’accés a .NET i COM quan s’apliquen polítiques de control d’aplicacions. Microsoft descriu els [modes de llenguatge](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_language_modes?view=powershell-7.3) i recomana App Control for Business per al control d’aplicacions. Tracteu aquests controls com a defensa en profunditat i proveu les tasques administratives abans d’aplicar-los.

## Llista de comprovació de seguretat del PowerShell

- **Feu servir codi signat.** Deseu els scripts aprovats al control de versions i verifiqueu-ne les signatures abans d’executar-los.
- **Registreu l’activitat.** Habiliteu el registre de mòduls i blocs de script per als mòduls i punts finals inclosos.
- **Protegiu els secrets.** Preferiu certificats, identitats gestionades, autenticació del Windows o un gestor de secrets a les contrasenyes dins dels scripts. Microsoft no recomana `SecureString` per a desenvolupaments nous.
- **Restringiu l’execució.** Feu servir App Control for Business, AppLocker o Just Enough Administration quan el model operatiu ho permeti.
- **Reviseu l’administració remota.** Feu servir punts finals segurs, limiteu les ordres permeses i eviteu credencials a les línies d’ordres o transcripcions.
- **Proveu els canvis.** Executeu l’script en un laboratori i confirmeu els esdeveniments esperats abans d’aplicar una política a producció.

________

## Conclusió

En conjunt, el **PowerShell** és una eina essencial per als professionals de la ciberseguretat. Permet automatitzar i simplificar tasques rutinàries, i allibera temps per a activitats més importants. Si n’aprofiten les possibilitats, les organitzacions poden millorar la seva postura de ciberseguretat i complir les normes i els estàndards del sector.

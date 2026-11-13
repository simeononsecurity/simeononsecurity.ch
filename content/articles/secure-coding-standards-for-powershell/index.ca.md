---
title: "Bones pràctiques de programació segura amb PowerShell: Guia"
date: 2023-03-01
lastmod: 2026-11-13
toc: true
draft: false
description: "Aprèn les millors pràctiques per escriure codi PowerShell segur i protegir els sistemes basats en Windows de les vulnerabilitats."
tags: ["PowerShell", "Programació segura", "Sistemes basats en Windows", "Validació de l’entrada", "Biblioteques de criptografia", "Privilegis mínims", "Analitzador estàtic de codi", "Protocols de comunicació segurs", "Registre i supervisió", "Escaneigs de vulnerabilitats", "Formació", "Injecció de codi", "Escalada de privilegis", "Fuita de dades", "Reforç de l’entorn", "Polítiques de seguretat", "Tallafocs", "Sistemes de detecció d’intrusions", "Gestió de vulnerabilitats", "Seguretat de xarxa", "Bones pràctiques de programació PowerShell", "Codi PowerShell segur", "Seguretat de sistemes Windows", "Validació d’entrada a PowerShell", "Criptografia amb PowerShell", "Principi del mínim privilegi", "Analitzador estàtic per a PowerShell", "Protocols segurs amb PowerShell", "Registre i supervisió amb PowerShell", "Escaneigs de vulnerabilitats amb PowerShell", "Formació en seguretat PowerShell", "Prevenció de la injecció de codi", "Mitigació de l’escalada de privilegis", "Prevenció de fuites de dades amb PowerShell", "Reforç de l’entorn PowerShell", "Polítiques de seguretat de PowerShell", "Configuració del tallafoc amb PowerShell", "Detecció d’intrusions amb PowerShell", "Gestió de vulnerabilitats de PowerShell", "Seguretat de xarxa amb PowerShell", "Programació segura de scripts PowerShell", "Neteja d’entrades i sortides amb PowerShell", "Protocols de comunicació segurs per a PowerShell", "Registre i supervisió de scripts PowerShell", "Reforçar l’entorn PowerShell", "Escanejar vulnerabilitats amb PowerShell", "Formar usuaris i administradors en seguretat PowerShell", "Pràctiques de codi PowerShell segur", "Codi PowerShell segur i resilient", "Bones pràctiques de seguretat PowerShell", "Millors pràctiques de seguretat PowerShell"]
cover: "/img/cover/An_image_of_a_superhero_standing_in_front_of_a_computer.webp"
coverAlt: "Un superheroi davant d’un ordinador amb el logotip de Windows a la pantalla i un escut a la mà, símbol de la importància de la programació segura per protegir els sistemes basats en Windows."
coverCaption: ""
---
PowerShell és un entorn popular per automatitzar tasques i gestionar configuracions. Automatitza feines repetitives i simplifica l’administració de sistemes basats en Windows. Com passa amb qualsevol llenguatge de programació, el codi PowerShell pot tenir vulnerabilitats si els desenvolupadors no segueixen estàndards de programació segura. Aquesta guia presenta bones pràctiques per escriure codi PowerShell segur.

____

## Valida les entrades

Les dades que introdueix l’usuari sovint són una font important de riscos de seguretat. La validació comprova que les dades compleixen els criteris esperats i que l’aplicació les pot utilitzar de manera segura.

Per exemple, la contrasenya que introdueix l’usuari ha de complir la política de l’aplicació. Per validar les dades, els desenvolupadors poden fer servir funcions integrades com `Test-Path` o expressions regulars.

```powershell
function Validate-Input {
    param(
        [string]$input
    )

    if ($input -match "^[A-Za-z0-9]+$") {
        return $true
    }
    else {
        return $false
    }
}
```

____

## Evita les funcions insegures

Algunes funcions de PowerShell poden causar problemes de seguretat si s’utilitzen sense cura. Funcions com Invoke-Expression, Get-Content i ConvertTo-SecureString poden permetre que un atacant executi codi maliciós. Evita aquestes funcions o limita les entrades i fes-les servir només quan calgui.

Per executar una ordre, fes servir Start-Process en lloc d’Invoke-Expression.
```powershell
# En lloc d’utilitzar Invoke-Expression
Invoke-Expression "Get-ChildItem"

# Utilitza Start-Process
Start-Process "Get-ChildItem"
```

____

## Fes servir biblioteques de criptografia

.NET Cryptography i Bouncy Castle ofereixen mètodes segurs per xifrar i desxifrar. Fes servir aquestes biblioteques en lloc de crear mètodes propis que podrien tenir vulnerabilitats.

Per xifrar una contrasenya, utilitza la biblioteca .NET Cryptography així:
```powershell
$securePassword = ConvertTo-SecureString "MyPassword" -AsPlainText -Force
$encryptedPassword = [System.Convert]::ToBase64String($securePassword.ToByteArray())
```

____

## Aplica el principi del mínim privilegi

Aquest principi limita els permisos dels usuaris o processos al mínim necessari per fer la seva feina. Dona accés només als recursos que necessiten.

Aplica’l quan escriguis codi per reduir l’impacte d’una bretxa de seguretat. Limitar l’accés d’un programa o usuari redueix els danys d’un atac amb èxit.

Si una aplicació només necessita llegir una base de dades, utilitza un compte de només lectura en lloc d’un compte amb permisos complets. Així un atacant tindrà menys possibilitats de modificar o esborrar dades mitjançant l’aplicació. Tampoc donis permisos d’administrador a qui només necessita fer tasques limitades.

El principi del mínim privilegi redueix els danys possibles i l’abast de l’atac.

____

## Mantén actualitzades les biblioteques i els marcs de treball

Les biblioteques i els marcs de treball poden contenir vulnerabilitats que els atacants aprofiten. Actualitza’ls a la versió més recent per reduir els riscos.

Quan es descobreix una vulnerabilitat, els responsables acostumen a publicar un pedaç o una actualització. Segueix aquestes actualitzacions i aplica-les aviat.

Per exemple, si una biblioteca externa com `Pester` té una vulnerabilitat, actualitza-la a una versió que la corregeixi. Això redueix el risc dels atacs que l’exploten.

Les dependències actualitzades contribueixen a un codi més segur. Comprova que totes siguin actuals i que s’hagin corregit les vulnerabilitats conegudes.

____

## Utilitza un analitzador estàtic

Un analitzador estàtic pot detectar vulnerabilitats abans d’executar el codi. Analitza’l abans del desplegament per trobar i corregir problemes a temps.

PowerShell té analitzadors com `PSScriptAnalyzer`. Poden detectar contrasenyes escrites directament al codi, un ús incorrecte de les variables d’entorn i funcions insegures.

`PSScriptAnalyzer` examina el codi PowerShell i pot trobar:

- **Credencials escrites directament al codi**
- **Ús de funcions obsoletes o insegures**
- **Validació insuficient de les entrades**
- **Ús incorrecte de variables i bucles**

Un analitzador estàtic ajuda a corregir vulnerabilitats al començament del desenvolupament. Això pot evitar bretxes i reduir l’impacte dels atacs.

____

## Escriu codi de manera segura

Els scripts PowerShell poden patir injecció de codi, escalada de privilegis i fuites de dades. Aplica aquestes pràctiques per reduir els riscos.

### Neteja les entrades i les sortides

Valida i neteja les dades que introdueix l’usuari per evitar la injecció de codi. Comprova que compleixin els criteris i no continguin codi maliciós. Neteja també les dades sensibles abans d’escriure-les en un registre o en una altra destinació, per evitar fuites.

### Xifra les comunicacions

Fes servir HTTPS, SSL/TLS o SSH per transmetre dades per la xarxa. Aquests protocols xifren les dades durant el trànsit i dificulten que algú les intercepti o modifiqui. Evita protocols sense xifrar com HTTP o Telnet, perquè les dades es poden interceptar i manipular fàcilment.

### Registra i supervisa l’activitat

Implementa mecanismes de registre i supervisió per detectar incidents i respondre-hi a temps. Registra els esdeveniments rellevants i configura alertes d’activitat sospitosa perquè els administradors puguin actuar abans que el problema creixi.

### Reforça l’entorn

Aplica polítiques i configuracions de seguretat al sistema operatiu, als dispositius de xarxa i a les aplicacions. Això redueix la superfície d’atac i evita accessos no autoritzats. Per exemple:

- **Desactiva serveis i protocols innecessaris per reduir la superfície d’atac**
- [**Aplica contrasenyes fortes i polítiques de contrasenya per evitar accessos no autoritzats**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)
- **Configura tallafocs i sistemes de detecció d’intrusions per prevenir i detectar atacs**
- **Instal·la actualitzacions i pedaços per corregir vulnerabilitats conegudes**

### Escaneja vulnerabilitats sovint

Escaneja els sistemes i les aplicacions per trobar i corregir vulnerabilitats. Utilitza eines com Nessus, OpenVAS o Microsoft Baseline Security Analyzer (MBSA). Els escaneigs periòdics ajuden a corregir punts febles abans que els atacants els aprofitin.

### Forma els usuaris i administradors

Ofereix formació i recursos sobre programació segura i els riscos del codi insegur. Ensenya als usuaris i administradors a escriure codi segur, detectar incidents i respondre-hi. Això ajuda a crear una cultura de seguretat dins de l’organització.

Aquestes pràctiques fan que el codi PowerShell sigui més segur i resistent a les amenaces. També redueixen el risc d’atacs reeixits i l’impacte dels incidents.

## Conclusió

PowerShell és una eina potent per automatitzar tasques i gestionar sistemes Windows, però cal seguir pràctiques de programació segura per evitar vulnerabilitats. Aquesta guia ha tractat la validació d’entrades, l’ús prudent de funcions, les biblioteques de criptografia i altres mesures.

Aplica-les per reduir el risc de bretxes i protegir els sistemes i les dades. Mantén-te al dia de les noves amenaces i millora contínuament la seguretat del codi PowerShell. Amb les eines i pràctiques adequades, PowerShell pot ser una eina fiable i segura per gestionar i automatitzar sistemes.

## Referències

- [Documentació de PowerShell](https://docs.microsoft.com/en-us/powershell/)
- [Sèrie dels 25 principals errors de programari](https://www.sans.org/top25-software-errors/)
- [Guia de validació d’entrades](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- [Guia general de seguretat de servidors](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-123.pdf)

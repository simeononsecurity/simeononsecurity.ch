---
title: "Ordres de Windows Defender PowerShell per a la seguretat del sistema"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Coneix les ordres de Windows Defender PowerShell i millora la seguretat del sistema amb el control de la línia d'ordres."
genre: ["Windows Defender", "ordres de PowerShell", "seguretat del sistema", "control de la línia d'ordres", "antivirus", "sistemes operatius Windows", "protecció contra programari maliciós", "configuració avançada de seguretat", "automatització de les operacions de seguretat", "Windows PowerShell"]
tags: ["Tecnologia", "Ciberseguretat", "Sistemes operatius", "Windows", "Eines de línia d'ordres", "Seguretat del sistema", "PowerShell", "Antivirus", "Protecció contra programari maliciós", "Scripts"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "Il·lustració animada d'un escut que protegeix un sistema informàtic de diverses amenaces cibernètiques."
coverCaption: "Millora la seguretat del sistema amb les ordres de Windows Defender PowerShell."
---

## Introducció

Windows Defender, desenvolupat per Microsoft, és una **solució integrada d'antivirus i seguretat** per als sistemes operatius Windows. Ofereix una **interfície fàcil d'utilitzar** per gestionar la configuració de seguretat. Els usuaris avançats que prefereixen controlar el sistema des de la línia d'ordres disposen d'un conjunt d'ordres de PowerShell. Aquest article explica les **ordres de Windows Defender PowerShell** i com poden millorar la seguretat i el control de l'entorn Windows.

## Les possibilitats de les ordres de Windows Defender PowerShell

Les ordres de Windows Defender PowerShell permeten fer **operacions de seguretat avançades** des de la línia d'ordres. Inclouen funcions que van des d'escanejar programari maliciós fins a configurar opcions avançades de seguretat. Amb PowerShell, pots automatitzar operacions de seguretat, crear scripts propis i integrar Windows Defender als fluxos de treball existents.

## Com començar amb Windows Defender PowerShell

Per accedir a les ordres de Windows Defender PowerShell, obre una sessió de PowerShell amb **privilegis d'administrador**. Segueix aquests passos:

1. Prem `Win + X` i selecciona **Windows PowerShell (Admin)** (com a administrador) al menú.
2. Si se't demana, fes clic a **Yes** (Sí) per permetre que l'aplicació faci canvis al dispositiu.

Quan tinguis oberta la sessió de PowerShell, podràs començar a fer servir les ordres de Windows Defender PowerShell.

## Ordres habituals de Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: comprovar l'estat de Windows Defender

L'ordre `Get-MpComputerStatus` mostra una visió general de l'estat actual de Windows Defender al sistema, incloent-hi la versió del motor antivirus, l'hora de l'últim escaneig i l'estat de la protecció en temps real. Executa-la per valorar ràpidament l'estat general de Windows Defender i comprovar que funciona correctament.

Per comprovar l'estat de Windows Defender, obre una sessió de PowerShell amb privilegis d'administrador i executa:

```powershell
Get-MpComputerStatus
```

L'ordre mostra informació com ara:

- **AntivirusEngineVersion**: el número de versió del motor antivirus que utilitza Windows Defender.
- **LastFullScanTime**: la data i l'hora de l'últim escaneig complet de Windows Defender.
- **LastQuickScanTime**: la data i l'hora de l'últim escaneig ràpid de Windows Defender.
- **RealTimeProtectionEnabled**: indica si la protecció en temps real està activada o desactivada.

Si supervises l'estat amb `Get-MpComputerStatus` regularment, sabràs quin nivell de protecció ofereix el sistema davant de **possibles amenaces**.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

L'ordre `Update-MpSignature` permet actualitzar manualment les signatures antivirus que fa servir Windows Defender. Aquestes signatures contenen informació clau sobre el programari maliciós conegut i ajuden Windows Defender a detectar i bloquejar amenaces. L'execució de l'ordre obté les signatures més recents per protegir el sistema de noves amenaces.

Per actualitzar manualment les signatures de Windows Defender, obre una sessió de PowerShell amb privilegis d'administrador i executa:

```powershell
Update-MpSignature
```

L'ordre inicia l'actualització i Windows Defender es connecta als servidors de Microsoft per baixar les **signatures antivirus més recents**. Quan acaba, Windows Defender té la informació actualitzada sobre el programari maliciós conegut i pot identificar i eliminar amenaces amb més eficàcia.

Mantenir actualitzades les signatures és essencial davant l'evolució del programari maliciós i de les amenaces cibernètiques. Executa `Update-MpSignature` regularment perquè Windows Defender protegeixi el sistema de manera eficaç.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

L'ordre `Set-MpPreference` permet personalitzar diversos paràmetres de **Windows Defender** segons els teus requisits de seguretat. Inclou opcions com ara la **protecció en temps real**, la **protecció basada en el núvol** i la **configuració del sistema d'inspecció de xarxa**.

Per exemple, pots activar o desactivar la protecció en temps real amb `Set-MpPreference`. Aquesta protecció supervisa el sistema per detectar activitats malicioses i respon de seguida a les amenaces. Per activar-la, executa:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

També pots ajustar la protecció basada en el núvol, que fa servir **recursos del núvol** per millorar la detecció i respondre més ràpidament a les noves amenaces. Per activar-la, executa:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

A més, `Set-MpPreference` permet personalitzar el sistema d'inspecció de xarxa. Aquest sistema analitza el trànsit de xarxa per trobar activitats sospitoses i possibles amenaces. Per ajustar-ne la configuració, executa:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Ajusta aquests paràmetres amb `Set-MpPreference` perquè **Windows Defender** s'adapti a les teves necessitats de seguretat i protegeixi el sistema del programari maliciós i d'altres activitats perjudicials.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

L'ordre `Start-MpScan` inicia escaneigs de programari maliciós per ajudar-te a detectar i eliminar fitxers maliciosos. Permet fer **escaneigs ràpids**, **complets** i **personalitzats** de camins concrets.

Per fer un **escaneig ràpid** amb `Start-MpScan`, executa aquesta ordre de PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

L'escaneig ràpid se centra en les àrees essencials del sistema on sovint es troba programari maliciós i permet valorar de pressa les possibles amenaces.

Per examinar tots els fitxers i directoris del sistema, inicia un **escaneig complet** amb `Start-MpScan`:

```powershell
Start-MpScan -ScanType FullScan
```

L'escaneig complet cerca programari maliciós de manera exhaustiva, però pot trigar més que un escaneig ràpid.

A més dels tipus d'escaneig predefinits, `Start-MpScan` permet examinar camins o fitxers concrets. Per exemple, per escanejar un directori determinat, executa:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Aquesta ordre inicia un escaneig personalitzat del directori indicat i concentra la detecció de programari maliciós en una àrea concreta del sistema.

Fes servir les opcions de `Start-MpScan` per programar escaneigs, automatitzar processos de seguretat i detectar i tractar regularment el programari maliciós.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

L'ordre `Get-MpThreatCatalog` proporciona informació detallada sobre les amenaces conegudes i els seus atributs. El catàleg inclou el nivell de gravetat, els noms dels fitxers associats i les accions recomanades per mitigar-les.

Per obtenir informació sobre amenaces concretes amb `Get-MpThreatCatalog`, segueix aquests passos:

1. Obre una sessió de PowerShell amb privilegis d'administrador.
2. Executa l'ordre següent:

```powershell
   Get-MpThreatCatalog
```

L'ordre mostra una llista de les amenaces conegudes i els detalls corresponents.

La sortida de `Get-MpThreatCatalog` inclou informació essencial com ara:

- **ThreatID**: un identificador únic de l'amenaça.
- **Severity**: indica el nivell de gravetat, de Low (baix) a Severe (greu).
- **Name**: el nom o la descripció de l'amenaça.
- **Path**: el camí del fitxer relacionat amb l'amenaça.
- **RecommendedAction**: orientació sobre l'acció recomanada per mitigar-la.

La informació de `Get-MpThreatCatalog` ajuda a entendre possibles amenaces i a triar les accions adequades. Tant si cal aïllar, eliminar o supervisar una amenaça concreta, el catàleg detallat facilita una resposta eficaç als incidents de seguretat.

Per obtenir més informació sobre l'ús de `Get-MpThreatCatalog` i la interpretació dels resultats, consulta la documentació oficial de Microsoft.

Mantén-te alerta i executa `Get-MpThreatCatalog` regularment per seguir l'evolució de les amenaces i millorar la seguretat del sistema.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

L'ordre `Add-MpPreference` permet afegir exclusions a Windows Defender i personalitzar el comportament dels escaneigs i de la protecció en temps real. Les exclusions indiquen quins fitxers, carpetes o processos s'han d'ometre durant els escaneigs de seguretat o la protecció en temps real.

Per afegir una exclusió amb `Add-MpPreference`, indica el camí o el nom del fitxer, la carpeta o el procés que vols excloure. Aquest exemple afegeix una exclusió per a una carpeta:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Aquesta ordre fa que Windows Defender no escanegi la carpeta indicada i redueix les alertes innecessàries i les possibles interrupcions del flux de treball.

Les exclusions poden ser útils per ometre aplicacions de confiança, entorns de desenvolupament o fitxers concrets que provoquin falsos positius. Amb `Add-MpPreference`, pots ajustar Windows Defender als teus requisits de seguretat i optimitzar-ne el rendiment.

Protegeix el sistema i redueix els falsos positius i les interrupcions d'escaneig innecessàries amb les exclusions de `Add-MpPreference`.

## Revisió de les ordres de Defender el 2026

Executa les ordres de Defender des d'una sessió amb privilegis elevats només quan la tasca requereixi aquests privilegis. Abans d'utilitzar un paràmetre, consulta l'ajuda actual del mòdul per a la versió de Windows de destinació. Registra la configuració existent, modifica un paràmetre cada vegada, verifica el resultat i anota l'ordre per desfer el canvi.

Entre les comprovacions útils hi ha l'estat de protecció, l'antiguitat de les signatures, les exclusions, les preferències, l'historial d'escaneigs i les deteccions recents. Limita les exclusions i documenta qui n'és responsable i quan caduquen. Consulta la [documentació del mòdul PowerShell de Microsoft Defender](https://learn.microsoft.com/en-us/powershell/module/defender/) i la [documentació de Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) per veure les ordres cmdlet i el comportament actuals.

## Conclusió

Les ordres de Windows Defender PowerShell ofereixen un **conjunt robust d'eines** per gestionar i millorar la seguretat del sistema Windows. Permeten *automatitzar operacions de seguretat*, *configurar opcions avançades* i integrar Windows Defender als fluxos de treball. Tant si ets administrador de sistemes com si ets un usuari avançat, aquestes ordres poden millorar la seguretat del sistema.

Fes servir les ordres de PowerShell amb prudència i entén-ne l'impacte abans d'executar-les. Aplica els teus coneixements de les ordres de Windows Defender PowerShell per protegir el sistema de les amenaces canviants.

## Referències

1. Microsoft Docs - [Cmdlets de Windows Defender a Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introducció a Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)

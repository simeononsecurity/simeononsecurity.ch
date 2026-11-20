---
title: "Comenzi PowerShell Windows Defender pentru securitatea sistemului"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Descoperiți puterea comenzilor Windows Defender PowerShell și învățați cum să vă îmbunătățiți securitatea sistemului cu ajutorul controlului prin linia de comandă."
genre: ["Windows Defender", "Comenzi PowerShell", "securitatea sistemului", "controlul liniei de comandă", "antivirus", "Sisteme de operare Windows", "protecție împotriva malware-ului", "setări avansate de securitate", "automatizarea operațiunilor de securitate", "Windows PowerShell"]
tags: ["Tehnologie", "Securitatea cibernetică", "Sisteme de operare", "Windows", "Instrumente de linie de comandă", "Securitatea sistemului", "PowerShell", "Antivirus", "Protecție împotriva programelor malware", "Scriere de scripturi"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "O ilustrație animată reprezentând un scut care protejează un sistem informatic de diverse amenințări cibernetice."
coverCaption: "Consolidarea securității sistemului dumneavoastră cu ajutorul comenzilor Windows Defender PowerShell."
---

## Introducere

Windows Defender, dezvoltat de Microsoft, este o soluție antivirus și de securitate integrată pentru sistemele de operare Windows. Aceasta oferă o interfață ușor de utilizat pentru a gestiona eficient setările de securitate. Cu toate acestea, pentru utilizatorii avansați care preferă controlul prin linia de comandă, Windows Defender oferă un set de comenzi PowerShell puternice. În acest articol, vom pătrunde în lumea **comenzilor Windows Defender PowerShell** și vom explora modul în care acestea pot îmbunătăți securitatea sistemului și pot oferi un control mai mare asupra mediului Windows.

## Puterea comenzilor Windows Defender PowerShell

Comenzile Windows Defender PowerShell le oferă utilizatorilor posibilitatea de a efectua operațiuni avansate de securitate folosind o interfață de linie de comandă. Aceste comenzi oferă o gamă largă de funcționalități, de la operațiuni simple, cum ar fi scanarea pentru malware, până la sarcini complexe, cum ar fi configurarea setărilor avansate de securitate. Prin utilizarea PowerShell, utilizatorii pot automatiza operațiunile de securitate, pot crea scripturi personalizate și pot integra Windows Defender în fluxurile de lucru existente fără probleme.

## Noțiuni introductive despre Windows Defender PowerShell

Pentru a accesa comenzile Windows Defender PowerShell, trebuie să deschideți o sesiune PowerShell cu privilegii administrative. Iată cum puteți începe:

1. Apăsați `Win + X` și selectați **Windows PowerShell (Admin)** (ca administrator) din meniu.
2. Dacă vi se solicită, faceți clic pe **Yes** (Da) pentru a permite aplicației să facă modificări la dispozitiv.

Odată ce ați deschis o sesiune PowerShell, puteți începe să utilizați comenzile Windows Defender PowerShell.

## Comenzi PowerShell Windows Defender uzuale

### 1. **Get-MpComputerStatus**: Verifică starea Windows Defender

Comanda `Get-MpComputerStatus` oferă o imagine de ansamblu a stării curente Windows Defender pe sistem, inclusiv versiunea motorului antivirus, ora ultimei scanări și starea protecției în timp real. Rularea acesteia vă ajută să verificați rapid dacă Windows Defender funcționează corect.

Pentru a verifica starea Windows Defender, deschideți o sesiune PowerShell cu privilegii administrative și executați următoarea comandă:

```powershell
Get-MpComputerStatus
```

Această comandă va afișa informații cum ar fi:

- **AntivirusEngineVersion**: Numărul de versiune al motorului antivirus utilizat de Windows Defender.
- **LastFullScanTime**: Data și ora ultimei scanări complete efectuate de Windows Defender.
- **LastQuickScanTime**: Data și ora ultimei scanări rapide efectuate de Windows Defender.
- **RealTimeProtectionEnabled**: Indică dacă protecția în timp real este activată sau dezactivată.

Monitorizarea periodică a stării Windows Defender utilizând `Get-MpComputerStatus` vă asigură că rămâneți informat cu privire la nivelul de protecție a sistemului dvs. împotriva amenințărilor potențiale.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

Comanda `Update-MpSignature` vă permite să actualizați manual semnăturile antivirus utilizate de Windows Defender. Aceste semnături conțin informații importante despre programele malware cunoscute și ajută Windows Defender să detecteze și să blocheze amenințările. Rularea comenzii aduce pe sistem cele mai recente semnături și sporește protecția împotriva amenințărilor noi.

Pentru a actualiza manual semnăturile Windows Defender, deschideți o sesiune PowerShell cu privilegii administrative și executați următoarea comandă:

```powershell
Update-MpSignature
```
Această comandă declanșează procesul de actualizare, prin care **Windows Defender** se conectează la **serverele Microsoft** pentru a descărca cele mai recente **semnături antivirus**. Odată ce actualizarea este finalizată, Windows Defender va dispune de cele mai recente informații despre programele malware cunoscute, consolidându-și capacitatea de a identifica și elimina amenințările.

Menținerea la zi a semnăturilor Windows Defender este esențială pentru a menține cel mai înalt nivel de protecție împotriva peisajului în continuă evoluție al **malware** și **amenințărilor cibernetice**. Prin actualizarea regulată a semnăturilor cu ajutorul `Update-MpSignature` vă asigurați că Windows Defender vă poate proteja eficient sistemul.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

Comanda `Set-MpPreference` vă permite să personalizați diverse setări **Windows Defender** în funcție de cerințele de securitate. Puteți configura opțiuni precum **protecția în timp real**, **protecția bazată pe cloud** și **setările sistemului de inspecție a rețelei**.

De exemplu, puteți activa sau dezactiva protecția în timp real cu `Set-MpPreference`. Aceasta monitorizează sistemul pentru activități rău intenționate și răspunde rapid la amenințări. Pentru a activa protecția, executați următoarea comandă:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

În plus, puteți utiliza comanda pentru a ajusta setările de protecție bazate pe cloud. Protecția bazată pe cloud utilizează resursele cloud pentru a îmbunătăți detectarea amenințărilor și pentru a oferi răspunsuri mai rapide la amenințările emergente. Pentru a activa protecția bazată pe cloud, utilizați următoarea comandă:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

De asemenea, puteți folosi `Set-MpPreference` pentru a personaliza setările sistemului de inspecție a rețelei. Sistemul analizează traficul de rețea pentru activități suspecte și amenințări potențiale. Pentru a ajusta setările, executați următoarea comandă:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Prin reglarea fină a acestor setări cu `Set-MpPreference` puteți optimiza **Windows Defender** pentru a se alinia la nevoile dumneavoastră specifice de securitate și pentru a asigura o protecție solidă împotriva programelor malware și a altor activități rău intenționate.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

Comanda `Start-MpScan` pornește scanări antimalware pe sistem și vă ajută să identificați și să eliminați fișierele malițioase. Aceasta acceptă **scanări rapide**, **scanări complete** și **scanări personalizate** pentru anumite căi.

Pentru a efectua o **scanare rapidă** cu `Start-MpScan`, executați următoarea comandă PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

O scanare rapidă se concentrează pe zonele critice ale sistemului dvs. în care se găsesc frecvent programe malware, oferind o evaluare rapidă a amenințărilor potențiale.

Pentru a examina toate fișierele și directoarele sistemului, puteți porni o **scanare completă** cu `Start-MpScan`. Executați următoarea comandă:

```powershell
Start-MpScan -ScanType FullScan
```

O scanare completă asigură detectarea și eliminarea completă a programelor malware din sistem, dar poate dura mai mult decât o scanare rapidă.

Pe lângă tipurile de scanare predefinite, `Start-MpScan` vă permite să specificați căi sau fișiere pentru scanări personalizate. De exemplu, puteți scana un anumit director cu următoarea comandă:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Această comandă va iniția o scanare personalizată în directorul specificat, permițându-vă să vizați anumite zone specifice ale sistemului pentru detectarea programelor malware.

Cu ajutorul comenzii `Start-MpScan` puteți programa scanări, automatiza procesele de securitate și asigura detectarea și reducerea periodică a programelor malware pe sistem.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

Comanda `Get-MpThreatCatalog` oferă informații detaliate despre amenințările cunoscute și atributele acestora. Catalogul include date despre severitate, numele fișierelor asociate și acțiunile recomandate pentru reducerea riscurilor.

Pentru a obține informații despre anumite amenințări cu `Get-MpThreatCatalog`, urmați acești pași:

1. Deschideți o sesiune PowerShell cu privilegii administrative.
2. Executați următoarea comandă:

```powershell
   Get-MpThreatCatalog
```
Această comandă va afișa o listă de amenințări cunoscute împreună cu detaliile corespunzătoare.

Rezultatul comenzii `Get-MpThreatCatalog` include informații esențiale precum:

- **ThreatID**: Un identificator unic pentru amenințare.
- **Severity**: Indică nivelul de gravitate al amenințării, de la Low (scăzut) la Severe (grav).
- **Name**: Numele sau descrierea amenințării.
- **Path**: Calea fișierului asociat cu amenințarea.
- **RecommendedAction**: Oferă îndrumări cu privire la acțiunea recomandată pentru atenuarea amenințării.

Informațiile din `Get-MpThreatCatalog` vă ajută să evaluați amenințările și să decideți cum să le gestionați. Puteți izola, elimina sau monitoriza o amenințare, iar catalogul detaliat sprijină un răspuns eficient la incidentele de securitate.

Pentru mai multe informații despre utilizarea `Get-MpThreatCatalog` și interpretarea rezultatelor sale, consultați documentația oficială Microsoft.

Utilizați regulat `Get-MpThreatCatalog` pentru a urmări evoluția amenințărilor și a îmbunătăți securitatea sistemului.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

Comanda `Add-MpPreference` vă permite să adăugați excluderi în Windows Defender și să personalizați scanările și protecția în timp real. Puteți indica fișierele, folderele sau procesele pe care Windows Defender trebuie să le ignore.

Pentru a adăuga o excludere cu `Add-MpPreference`, specificați calea sau numele fișierului, folderului ori procesului. Exemplul următor adaugă un folder la excluderi:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Această comandă se asigură că Windows Defender sare peste scanarea folderului specificat, reducând alertele inutile și eventualele întreruperi ale fluxului de lucru.

Excluderile pot fi utile pentru aplicații de încredere, medii de dezvoltare sau fișiere care pot genera rezultate fals pozitive. Cu `Add-MpPreference`, puteți ajusta Windows Defender la cerințele de securitate și îi puteți optimiza performanța.

Protejați sistemul și reduceți rezultatele fals pozitive și întreruperile inutile ale scanărilor cu funcțiile de excludere oferite de `Add-MpPreference`.

## Verificarea comenzilor Defender în 2026

Rulați comenzile Defender dintr-o sesiune cu privilegii elevate numai când sarcina cere elevare. Consultați ajutorul actual al modulului pentru versiunea Windows vizată înainte de a folosi un parametru. Înregistrați configurația existentă, schimbați câte o setare, verificați rezultatul și notați comanda de revenire.

Verificările utile includ starea protecției, vechimea semnăturilor, excluderile, preferințele, istoricul scanărilor și detectările recente. Păstrați excluderile restrânse și notați responsabilul și data expirării. Pentru cmdleturile și comportamentul actual, consultați [documentația modulului PowerShell Microsoft Defender](https://learn.microsoft.com/en-us/powershell/module/defender/) și [documentația Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows).

## Concluzie

Comenzile Windows Defender PowerShell oferă un **set robust de instrumente** pentru gestionarea și îmbunătățirea securității sistemului Windows. Prin utilizarea acestor comenzi, puteți *automatiza operațiunile de securitate*, *configura setările avansate* și încorpora Windows Defender fără probleme în fluxurile de lucru. Indiferent dacă sunteți un **administrator de sistem** sau un **utilizator experimentat**, explorarea capabilităților comenzilor Windows Defender PowerShell poate îmbunătăți semnificativ poziția de securitate a sistemului dumneavoastră.

Nu uitați, o mare putere implică o mare responsabilitate. Atunci când utilizați comenzile PowerShell, fiți prudent și asigurați-vă că înțelegeți impactul comenzilor înainte de a le executa. Combinând cunoștințele dvs. cu puterea comenzilor Windows Defender PowerShell, puteți lua măsuri proactive pentru a vă proteja sistemul de amenințările în evoluție.

## Referințe

1. Microsoft Docs - [Cmdleturi Windows Defender în Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introducere în Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)

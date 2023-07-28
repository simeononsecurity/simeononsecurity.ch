---
title: "Îmbunătățiți securitatea sistemului cu comenzile PowerShell Windows Defender"
date: 2023-07-27
toc: true
draft: false
description: "Descoperiți puterea comenzilor Windows Defender PowerShell și învățați cum să vă îmbunătățiți securitatea sistemului cu ajutorul controlului prin linia de comandă."
genre: ["Windows Defender", "Comenzi PowerShell", "securitatea sistemului", "controlul liniei de comandă", "antivirus", "Sisteme de operare Windows", "protecție împotriva malware-ului", "setări avansate de securitate", "automatizarea operațiunilor de securitate", "Windows PowerShell"]
tags: ["Tehnologie", "Securitatea cibernetică", "Sisteme de operare", "Windows", "Instrumente de linie de comandă", "Securitatea sistemului", "PowerShell", "Antivirus", "Protecție împotriva programelor malware", "Scripting"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.png"
coverAlt: "O ilustrație animată reprezentând un scut care protejează un sistem informatic de diverse amenințări cibernetice."
coverCaption: "Consolidarea securității sistemului dumneavoastră cu ajutorul comenzilor Windows Defender PowerShell."
---

## Introducere

Windows Defender, dezvoltat de Microsoft, este o soluție antivirus și de securitate integrată pentru sistemele de operare Windows. Aceasta oferă o interfață ușor de utilizat pentru a gestiona eficient setările de securitate. Cu toate acestea, pentru utilizatorii avansați care preferă controlul prin linia de comandă, Windows Defender oferă un set de comenzi PowerShell puternice. În acest articol, vom pătrunde în lumea **comandelor PowerShell **Windows Defender PowerShell** și vom explora modul în care acestea pot îmbunătăți securitatea sistemului și pot oferi un control mai mare asupra mediului Windows.

## Puterea comenzilor Windows Defender PowerShell

Comenzile Windows Defender PowerShell le oferă utilizatorilor posibilitatea de a efectua operațiuni avansate de securitate folosind o interfață de linie de comandă. Aceste comenzi oferă o gamă largă de funcționalități, de la operațiuni simple, cum ar fi scanarea pentru malware, până la sarcini complexe, cum ar fi configurarea setărilor avansate de securitate. Prin utilizarea PowerShell, utilizatorii pot automatiza operațiunile de securitate, pot crea scripturi personalizate și pot integra Windows Defender în fluxurile de lucru existente fără probleme.

## Noțiuni introductive despre Windows Defender PowerShell

Pentru a accesa comenzile Windows Defender PowerShell, trebuie să deschideți o sesiune PowerShell cu privilegii administrative. Iată cum puteți începe:

1. Apăsați `Win + X` și selectați **Windows PowerShell (Admin)** din meniu.
2. Dacă vi se solicită, faceți clic pe **Yes** (Da**) pentru a permite aplicației să facă modificări la dispozitiv.

Odată ce ați deschis o sesiune PowerShell, puteți începe să utilizați comenzile Windows Defender PowerShell.

## Comenzi Windows Defender PowerShell comune pentru Windows Defender

### 1. **Get-MpComputerStatus**: Verifică starea Windows Defender

Adresa `Get-MpComputerStatus` comandă oferă o imagine de ansamblu a stării curente a Windows Defender pe sistemul dumneavoastră, inclusiv versiunea motorului antivirus, ultima oră de scanare și starea protecției în timp real. Prin rularea acestei comenzi, puteți evalua rapid starea generală de sănătate a Windows Defender și vă puteți asigura că acesta funcționează în mod optim.

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

The `Update-MpSignature` comandă vă oferă posibilitatea de a actualiza manual semnăturile antivirus utilizate de Windows Defender. Semnăturile antivirus conțin informații esențiale despre programele malware cunoscute, permițând astfel lui Windows Defender să detecteze și să blocheze eficient amenințările. Prin rularea acestei comenzi, vă asigurați că sistemul dvs. dispune de cele mai recente semnături, oferind o protecție sporită împotriva amenințărilor emergente.

Pentru a actualiza manual semnăturile Windows Defender, deschideți o sesiune PowerShell cu privilegii administrative și executați următoarea comandă:

```powershell
Update-MpSignature
```
Această comandă declanșează procesul de actualizare, prin care **Windows Defender** se conectează la **serverele Microsoft** pentru a descărca cele mai recente **semnături antivirus**. Odată ce actualizarea este finalizată, Windows Defender va dispune de cele mai recente informații despre programele malware cunoscute, consolidându-și capacitatea de a identifica și elimina amenințările.

Menținerea la zi a semnăturilor Windows Defender este esențială pentru a menține cel mai înalt nivel de protecție împotriva peisajului în continuă evoluție al **malware** și **amenințărilor cibernetice**. Prin actualizarea regulată a semnăturilor cu ajutorul `Update-MpSignature` vă asigurați că Windows Defender vă poate proteja eficient sistemul.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

The `Set-MpPreference` vă permite să personalizați diverse setări ale **Windows Defender**, permițându-vă să adaptați comportamentul acestuia pentru a satisface cerințele dumneavoastră specifice de securitate. Această comandă oferă flexibilitate în configurarea unor opțiuni cum ar fi **protecție în timp real**, **protecție bazată pe cloud** și **configurarea sistemului de inspecție a rețelei**.

De exemplu, puteți activa sau dezactiva protecția în timp real utilizând comanda `Set-MpPreference` comandă. Protecția în timp real monitorizează în mod activ sistemul dumneavoastră pentru a detecta activități rău intenționate și oferă un răspuns imediat la amenințări. Pentru a activa protecția în timp real, executați următoarea comandă:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

În plus, puteți utiliza comanda pentru a ajusta setările de protecție bazate pe cloud. Protecția bazată pe cloud utilizează resursele cloud pentru a îmbunătăți detectarea amenințărilor și pentru a oferi răspunsuri mai rapide la amenințările emergente. Pentru a activa protecția bazată pe cloud, utilizați următoarea comandă:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

În plus, în cazul în care `Set-MpPreference` comandă permite personalizarea setărilor sistemului de inspecție a rețelei. Sistemul de inspecție a rețelei analizează traficul de rețea pentru activități suspecte și potențiale amenințări. Pentru a ajusta setările sistemului de inspecție a rețelei, executați următoarea comandă:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Prin reglarea fină a acestor setări cu `Set-MpPreference` puteți optimiza **Windows Defender** pentru a se alinia la nevoile dumneavoastră specifice de securitate și pentru a asigura o protecție solidă împotriva programelor malware și a altor activități rău intenționate.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

The `Start-MpScan` este un instrument puternic pentru a iniția scanări malware pe sistemul dumneavoastră, permițându-vă să identificați și să eliminați în mod proactiv fișierele malițioase. Această comandă oferă flexibilitate în efectuarea diferitelor tipuri de scanări, inclusiv **scanări rapide**, **scanări complete** și **scanări personalizate** cu anumite căi de acces.

Pentru a efectua o **explorare rapidă** utilizând comanda `Start-MpScan` comanda, executați următoarea comandă PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

O scanare rapidă se concentrează pe zonele critice ale sistemului dvs. în care se găsesc frecvent programe malware, oferind o evaluare rapidă a amenințărilor potențiale.

Pentru o scanare mai cuprinzătoare, care examinează toate fișierele și directoarele de pe sistem, puteți iniția o scanare **completă**. Executați următoarea comandă pentru a efectua o scanare completă utilizând `Start-MpScan`

```powershell
Start-MpScan -ScanType FullScan
```

O scanare completă asigură detectarea și eliminarea completă a programelor malware din sistem, dar poate dura mai mult decât o scanare rapidă.

În plus față de tipurile de scanare predefinite, funcția `Start-MpScan` vă permite să efectuați scanări personalizate prin specificarea unor căi sau fișiere specifice de scanat. De exemplu, puteți scana un anumit director de pe sistem utilizând următoarea comandă:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Această comandă va iniția o scanare personalizată în directorul specificat, permițându-vă să vizați anumite zone specifice ale sistemului pentru detectarea programelor malware.

Prin valorificarea versatilității funcției `Start-MpScan` comanda, puteți programa scanări, automatiza procesele de securitate și asigura detectarea și reducerea periodică a programelor malware pe sistemul dumneavoastră.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

The `Get-MpThreatCatalog` reprezintă o resursă valoroasă pentru obținerea de informații detaliate despre amenințările cunoscute și despre atributele acestora. Prin executarea acestei comenzi, puteți accesa un catalog cuprinzător de amenințări, inclusiv date privind gravitatea acestora, numele fișierelor asociate și acțiunile recomandate pentru atenuarea lor.

Pentru a prelua informații despre amenințări specifice utilizând `Get-MpThreatCatalog` urmați acești pași:

1. Deschideți o sesiune PowerShell cu privilegii administrative.
2. Executați următoarea comandă:

```powershell
   Get-MpThreatCatalog
```
Această comandă va afișa o listă de amenințări cunoscute împreună cu detaliile corespunzătoare.

Rezultatul comenzii `Get-MpThreatCatalog` comanda include informații esențiale, cum ar fi:

- **ThreatID**: Un identificator unic pentru amenințare.
- **Severity**: Indică nivelul de gravitate al amenințării, de la Low (scăzut) la Severe (grav).
- **Name**: Numele sau descrierea amenințării.
- **Path**: Calea fișierului asociat cu amenințarea.
- **RecommendedAction**: Oferă îndrumări cu privire la acțiunea recomandată pentru atenuarea amenințării.

Prin valorificarea informațiilor obținute din `Get-MpThreatCatalog` puteți obține informații valoroase despre potențialele amenințări și puteți lua decizii în cunoștință de cauză cu privire la acțiunile adecvate pentru a le reduce. Fie că este vorba de izolarea, eliminarea sau monitorizarea unei amenințări specifice, catalogul detaliat vă dă posibilitatea de a răspunde eficient la incidentele de securitate.

Pentru mai multe informații despre utilizarea `Get-MpThreatCatalog` și interpretarea rezultatelor sale, consultați documentația oficială Microsoft.

Rămâneți vigilenți și utilizați în mod regulat aplicația `Get-MpThreatCatalog` pentru a rămâne informat cu privire la evoluția amenințărilor și pentru a spori securitatea sistemului dumneavoastră.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

The `Add-MpPreference` vă permite să adăugați excluderi la Windows Defender, permițându-vă să personalizați comportamentul de scanare și de protecție în timp real. Prin adăugarea de excluderi, puteți specifica fișiere, foldere sau procese pe care doriți ca Windows Defender să le ignore în timpul scanărilor de securitate sau al protecției în timp real.

Pentru a adăuga o excludere utilizând `Add-MpPreference` trebuie să furnizați calea sau numele fișierului, dosarului sau procesului pe care doriți să îl excludeți. Iată un exemplu de adăugare a unei excluderi pentru un dosar:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Această comandă se asigură că Windows Defender sare peste scanarea folderului specificat, reducând alertele inutile și eventualele întreruperi ale fluxului de lucru.

Excluderile pot fi utile în diverse scenarii, cum ar fi excluderea aplicațiilor de încredere, a mediilor de dezvoltare sau a unor fișiere specifice care pot declanșa rezultate fals pozitive. Prin valorificarea flexibilității de `Add-MpPreference` puteți ajusta cu precizie Windows Defender pentru a se potrivi nevoilor dumneavoastră specifice de securitate și pentru a-i optimiza performanța.

Protejați-vă sistemul în mod eficient, minimizând în același timp falsurile pozitive și întreruperile inutile ale scanării prin utilizarea capacităților puternice de excludere oferite de `Add-MpPreference`

## Concluzie

Comenzile Windows Defender PowerShell oferă un **set robust de instrumente** pentru gestionarea și îmbunătățirea securității sistemului Windows. Prin utilizarea acestor comenzi, puteți *automatiza operațiunile de securitate*, *configura setările avansate* și încorpora Windows Defender fără probleme în fluxurile de lucru. Indiferent dacă sunteți un **administrator de sistem** sau un **utilizator experimentat**, explorarea capabilităților comenzilor Windows Defender PowerShell poate îmbunătăți semnificativ poziția de securitate a sistemului dumneavoastră.

Nu uitați, o mare putere implică o mare responsabilitate. Atunci când utilizați comenzile PowerShell, fiți prudent și asigurați-vă că înțelegeți impactul comenzilor înainte de a le executa. Combinând cunoștințele dvs. cu puterea comenzilor Windows Defender PowerShell, puteți lua măsuri proactive pentru a vă proteja sistemul de amenințările în evoluție.

## Referințe

1. Microsoft Docs - [Windows Defender Cmdlets in Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introduction to Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)

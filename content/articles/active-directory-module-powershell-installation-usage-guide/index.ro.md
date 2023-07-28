---
title: "Mastering Active Directory Administration with PowerShell: Ghid de instalare și utilizare"
date: 2023-07-25
toc: true
draft: false
description: "Descoperiți cum să instalați și să utilizați în mod eficient modulul Active Directory pentru PowerShell pentru a simplifica sarcinile de administrare a Windows Active Directory."
genre: ["Tehnologie", "Windows", "PowerShell", "Active Directory", "Administrație", "Scripting", "IT", "Automatizare", "Windows Server", "Microsoft"]
tags: ["modulul Active Directory pentru PowerShell", "modulul de import Active Directory în PowerShell", "modulul Active Directory pentru Windows PowerShell", "instalare PowerShell Active Directory", "instalați Active Directory PowerShell", "PowerShell instalați modulul Active Directory Windows 10", "instalați Active Directory PowerShell modul PowerShell Windows 10", "obțineți modulul PowerShell Active Directory", "Administrarea AD", "Windows Active Directory", "Comandamente PowerShell cmdlet", "recuperarea informațiilor AD", "crearea de obiecte AD", "modificarea obiectelor AD", "gestionați securitatea AD", "Gestionarea utilizatorilor AD", "Gestionarea grupurilor AD", "Managementul AD OR", "Scripting PowerShell", "Administrare Windows Server", "Microsoft PowerShell", "automatizarea sarcinilor AD", "Instalarea modulului PowerShell", "Ghid de administrare AD", "Gestionarea Active Directory", "Gestionarea securității AD", "Automatizarea PowerShell", "Comenzi PowerShell pentru Active Directory", "Referință la cmdlet PowerShell"]
cover: "/img/cover/An_image_depicting_a_network_of_interconnected.png"
coverAlt: "O imagine reprezentând o rețea de servere interconectate și pictograme de utilizator, simbolizând gestionarea și automatizarea Active Directory."
coverCaption: "Eliberați puterea administrării Active Directory cu PowerShell."
---

## Introducere

În peisajul digital de astăzi, gestionarea și menținerea conturilor de utilizator, a grupurilor de securitate și a altor resurse într-un mediu Windows Active Directory (AD) necesită procese eficiente și simplificate. PowerShell, un limbaj de scripting puternic dezvoltat de Microsoft, oferă modulul **Active Directory** pentru a facilita sarcinile de administrare AD. Acest modul oferă o gamă largă de cmdlet-uri care permit administratorilor să automatizeze diverse operațiuni și să administreze AD în mod eficient. În acest articol, vom explora instalarea și utilizarea modulului Active Directory pentru PowerShell.

## Instalarea modulului Active Directory pentru PowerShell

Pentru a începe să utilizați modulul Active Directory pentru PowerShell, trebuie să vă asigurați că acesta este instalat pe sistemul dumneavoastră. Procesul de instalare poate varia în funcție de sistemul dumneavoastră de operare. Iată pașii de instalare a modulului pe **Windows 10**, **Windows 11** și **Windows Server**:

### Windows 10 și Windows 11 - PowerShell
1. Deschideți **Windows PowerShell** cu privilegii administrative.
2. Rulați următoarea comandă pentru a instala modulul:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Așteptați ca instalarea să se finalizeze. Odată terminată, puteți începe să utilizați modulul Active Directory.

### Windows Server
1. Deschideți **Windows PowerShell** cu privilegii administrative.
2. Rulați următoarea comandă pentru a instala modulul:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Așteptați ca instalarea să se finalizeze. Odată terminată, puteți începe să utilizați modulul Active Directory.

### Sisteme offline

Sistemele offline devin un pic mai complicate. Există câteva metode, însă cea pe care o recomandăm este prin utilizarea următorului script:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importarea modulului Active Directory în PowerShell

Înainte de a putea utiliza modulul Active Directory în PowerShell, trebuie să îl importați în sesiunea curentă. Urmați acești pași pentru a importa modulul:

1. Lansați **Windows PowerShell** cu drepturi administrative.
2. 2. Executați următoarea comandă pentru a importa modulul:

```powershell
Import-Module ActiveDirectory
```

3. Modulul Active Directory va fi importat, iar acum puteți accesa cmdlet-urile și funcțiile sale.

## Utilizarea modulului Active Directory pentru PowerShell

Odată ce ați importat modulul Active Directory, puteți profita de setul său bogat de cmdlet-uri pentru a efectua diverse sarcini administrative. Să explorăm câteva cmdlet-uri utilizate în mod obișnuit și funcționalitățile acestora:

### Recuperarea informațiilor din Active Directory

Pentru a gestiona eficient un mediu Active Directory (AD), este esențial să recuperați informații despre diverse obiecte AD, cum ar fi utilizatorii, grupurile și unitățile organizaționale (OU). PowerShell oferă cmdlet-uri puternice care simplifică procesul de recuperare.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps) Acest cmdlet vă permite să preluați informații detaliate despre utilizatorii AD. Puteți obține atribute precum numele de utilizator, numele afișat, adresa de e-mail și multe altele. De exemplu, pentru a prelua toți utilizatorii ale căror nume de utilizator încep cu "johndoe", puteți rula următoarea comandă:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Această comandă va returna o listă de obiecte de utilizator care se potrivesc cu filtrul specificat.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps) Cu ajutorul cmdletului Get-ADGroup, puteți prelua informații despre grupurile AD. Acesta oferă acces la detalii precum numele grupului, membrii, descrierea și multe altele. De exemplu, pentru a prelua toate grupurile de securitate din mediul AD, puteți executa următoarea comandă:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Aceasta va furniza o listă a grupurilor de securitate din Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps) cmdlet-ul Get-ADOrganizationalUnit se utilizează pentru a prelua informații despre AD OUs. Acesta vă permite să accesați proprietăți precum numele OU, descrierea, OU părinte și multe altele. Pentru a prelua toate OU-urile din domeniu, puteți utiliza următoarea comandă:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Rularea acestei comenzi va afișa o listă a tuturor OU-urilor din Active Directory.

Prin utilizarea acestor cmdlet-uri puternice, puteți prelua cu ușurință informații specifice despre utilizatorii, grupurile și OU-urile AD, permițând administrarea și gestionarea eficientă a mediului Active Directory.

{{< inarticle-dark >}}


Aceste cmdlet-uri vă permit să preluați atribute specifice, să filtrați rezultatele și să efectuați interogări avansate pentru a obține informațiile dorite.

### Crearea și gestionarea obiectelor Active Directory

Atunci când lucrați cu Active Directory (AD), modulul Active Directory din PowerShell oferă cmdlete puternice pentru crearea și gestionarea obiectelor AD. Să explorăm câteva cmdlet-uri esențiale pentru crearea de utilizatori, grupuri și unități organizaționale (OU) AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps) Acest cmdlet vă permite să creați un nou utilizator AD. Puteți specifica atribute cum ar fi numele de utilizator, parola, adresa de e-mail și multe altele. De exemplu, pentru a crea un nou utilizator cu numele de utilizator "john.doe" și numele de afișare "John Doe", puteți utiliza următoarea comandă:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Această comandă va crea un nou utilizator în Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps) cmdlet-ul New-ADGroup vă permite să creați un nou grup AD. Puteți seta proprietăți cum ar fi numele grupului, descrierea, domeniul de aplicare al grupului și multe altele. Pentru a crea un nou grup numit "Marketing" cu o descriere, puteți executa următoarea comandă:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Această comandă va crea un nou grup în Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps) Cu ajutorul cmdletului New-ADOrganizationalUnit, puteți crea o nouă AD OU. Puteți specifica proprietăți precum numele OU, OU părinte și altele. De exemplu, pentru a crea o nouă OU numită "Sales" (Vânzări) sub OU "Departments" (Departamente), puteți executa următoarea comandă:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Această comandă va crea o nouă OU în ierarhia Active Directory.

Prin utilizarea acestor cmdlet-uri, puteți crea cu ușurință noi utilizatori, grupuri și OU-uri AD cu proprietățile și configurațiile dorite, permițând gestionarea eficientă a mediului Active Directory.

{{< inarticle-dark >}}


### Modificarea obiectelor Active Directory

Când vine vorba de modificarea proprietăților și atributelor obiectelor Active Directory (AD) existente, modulul Active Directory din PowerShell oferă câteva cmdlet-uri utile. Să explorăm aceste cmdlet-uri pentru modificarea utilizatorilor, grupurilor și unităților organizaționale (OU) AD.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps) cmdlet-ul Set-ADUser vă permite să modificați proprietățile unui utilizator AD. Puteți actualiza atribute precum numele afișat, adresa de e-mail, numărul de telefon și multe altele. De exemplu, pentru a modifica numărul de telefon al unui utilizator cu numele de utilizator "john.doe", puteți utiliza următoarea comandă:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Această comandă va modifica numărul de telefon al utilizatorului specificat în Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps) Cu ajutorul cmdletului Set-ADGroup, puteți modifica proprietățile unui grup AD. Puteți actualiza atribute precum descrierea grupului, apartenența, domeniul de aplicare al grupului și multe altele. Pentru a modifica descrierea unui grup numit "Marketing" în "Marketing Team", puteți executa următoarea comandă:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Această comandă va actualiza descrierea grupului specificat în Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps) cmdlet-ul Set-ADOrganizationalUnit vă permite să modificați proprietățile unei OU AD. Puteți modifica atribute precum numele OU, descrierea și multe altele. De exemplu, pentru a modifica descrierea unei OU numite "Sales" în "Sales Department", puteți executa următoarea comandă:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Această comandă va actualiza descrierea OU specificată în ierarhia Active Directory.

Prin utilizarea acestor cmdlet-uri, puteți modifica cu ușurință proprietățile și atributele obiectelor AD, efectuând actualizările și ajustările necesare pentru a satisface cerințele organizației dumneavoastră.

{{< inarticle-dark >}}


### Gestionarea securității Active Directory

Pe lângă gestionarea și administrarea obiectelor Active Directory (AD), modulul Active Directory din PowerShell oferă cmdlet-uri special concepute pentru a gestiona aspectele legate de securitate ale AD. Aceste cmdlet-uri le permit administratorilor să gestioneze eficient accesul utilizatorilor, apartenența la grupuri și sarcinile legate de parole în cadrul mediului AD.

Iată câteva cmdlet-uri legate de securitate utilizate în mod obișnuit:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps) Acest cmdlet vă permite să adăugați membri la un grup AD. Prin specificarea grupului AD și a conturilor de utilizatori sau a grupurilor pe care doriți să le adăugați, puteți gestiona cu ușurință controlul accesului. De exemplu, pentru a adăuga un utilizator numit "JohnDoe" la grupul "Managers", puteți utiliza următoarea comandă:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps) Cu acest cmdlet, puteți elimina membri dintr-un grup AD. Prin specificarea grupului AD și a conturilor de utilizatori sau a grupurilor pe care doriți să le eliminați, puteți gestiona în mod eficient apartenența la grupuri. De exemplu, pentru a elimina un utilizator numit "JaneSmith" din grupul "Developers", puteți utiliza următoarea comandă:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps) Acest cmdlet vă permite să setați parola pentru un utilizator AD. Specificând contul de utilizator și furnizând o nouă parolă, puteți aplica politicile privind parolele și asigura o autentificare sigură a utilizatorilor. Iată un exemplu de setare a unei parole noi pentru un utilizator numit "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Prin utilizarea acestor cmdlet-uri legate de securitate, administratorii pot gestiona în mod eficient accesul utilizatorilor, apartenența la grupuri și politicile privind parolele în cadrul mediului Active Directory.

## Exemplu de script de modul Active Directory pentru PowerShell
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## Concluzie

În concluzie, modulul **Active Directory pentru PowerShell** este un instrument puternic care permite gestionarea eficientă și comodă a Windows Active Directory. Prin instalarea și importarea modulului, veți avea acces la un set cuprinzător de **cmdlete** care simplifică diverse sarcini legate de AD.

Cu ajutorul modulului Active Directory, puteți efectua o gamă largă de operațiuni, cum ar fi recuperarea de informații despre obiectele AD, crearea de noi obiecte, modificarea proprietăților și gestionarea securității. Acest modul le permite administratorilor să automatizeze sarcinile administrative, să eficientizeze fluxurile de lucru și să asigure buna funcționare a mediilor Active Directory.

Prin utilizarea **PowerShell** și a **Modul Active Directory**, vă puteți spori capacitățile de administrare AD și puteți îmbunătăți eficiența proceselor de gestionare AD. Indiferent dacă sunteți administrator de sistem, profesionist IT sau manager Active Directory, modulul Active Directory vă echipează cu instrumentele necesare pentru a vă administra eficient infrastructura AD.

Profitați de puterea **PowerShell** și a **Modul Active Directory** pentru a vă eficientiza sarcinile de administrare AD, pentru a crește productivitatea și pentru a menține un mediu Active Directory sigur și bine organizat.

{{< inarticle-dark >}}

## Referințe

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)

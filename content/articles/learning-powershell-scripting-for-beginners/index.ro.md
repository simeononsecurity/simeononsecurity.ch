---
title: "Scripturi PowerShell"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "Învață bazele scripturilor PowerShell și automatizează sarcini cu acest ghid pas cu pas pentru începători, care acoperă cmdleturi, bucle, funcții și multe altele."
genre: ["Tehnologie", "Programare", "Automatizare", "Windows", "Scripturi", "IT", "Sarcini administrative", "Administrarea computerelor", "Dezvoltare software", "Codare"]
tags: ["scripturi PowerShell", "automatizare PowerShell", "scripturi Windows", "cmdleturi PowerShell", "module PowerShell", "bucle PowerShell", "instrucțiuni condiționale PowerShell", "funcții PowerShell", "bune practici PowerShell", "depanare PowerShell", "testare PowerShell", "variabile PowerShell", "PowerShell ISE", "PowerShell Remoting", "tehnologii Microsoft", "automatizare IT", "administrarea computerelor", "programare pentru începători", "sarcini administrative", "idei de scripturi PowerShell", "copii de rezervă automate", "gestionarea fișierelor", "informații despre sistem", "gestionarea utilizatorilor", "instalarea software-ului", "configurarea rețelei", "automatizarea securității", "planificarea sarcinilor", "modificarea registrului", "administrare la distanță"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "Un personaj de desene animate ține un script în fața unui computer cu promptul PowerShell, ilustrând cât de ușor pot începe începătorii să scrie scripturi PowerShell"
coverCaption: ""
---
**Scripturi PowerShell pentru începători**

PowerShell este un shell de linie de comandă și un limbaj de scripting dezvoltat de Microsoft. Oferă numeroase comenzi și funcții pentru gestionarea și automatizarea diferitelor aspecte ale sistemului de operare Windows și ale altor tehnologii Microsoft. În acest articol prezentăm bazele scripturilor PowerShell și un ghid pas cu pas pentru a începe.

## Introducere în PowerShell

**PowerShell** este un shell de linie de comandă care permite automatizarea și gestionarea sistemului de operare Windows și a altor tehnologii Microsoft. Oferă un set cuprinzător de comenzi și funcții pentru sarcini administrative, precum gestionarea fișierelor și directoarelor, configurarea rețelei și administrarea sistemului. PowerShell include și un limbaj de scripting, cu care poți crea scripturi complexe și automatiza sarcini repetitive.

## Începe să folosești PowerShell

### Instalarea PowerShell

PowerShell este preinstalat în majoritatea versiunilor Windows. Dacă folosești o versiune mai veche de Windows sau ai nevoie de o versiune mai nouă de PowerShell, descarc-o de pe site-ul Microsoft. Urmează acești pași pentru descărcare și instalare:

1. Accesează [site-ul Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) și selectează versiunea dorită.
2. Descarcă și rulează fișierul de instalare.
3. Urmează instrucțiunile de pe ecran pentru a finaliza instalarea.

### Pornirea PowerShell

După instalare, pornește PowerShell astfel:

1. Deschide meniul Start și introdu „PowerShell” în bara de căutare.
2. Selectează „Windows PowerShell” din rezultate.
3. PowerShell se va deschide într-o fereastră nouă.

### Scripturi PowerShell în Visual Studio Code

Pentru o experiență mai bună de creare a scripturilor, poți folosi Visual Studio Code (VS Code), un mediu de dezvoltare integrat (IDE) popular. VS Code oferă evidențierea sintaxei, completarea codului, depanare și un terminal integrat, fiind o alegere potrivită pentru scripturi PowerShell. Pentru a începe în VS Code:

1. Instalează Visual Studio Code de pe [site-ul oficial](https://code.visualstudio.com/).
2. Din piața de extensii VS Code, instalează extensia „PowerShell” de la Microsoft.
3. Deschide în VS Code un fișier de script PowerShell (.ps1) și începe să scrii.

### PowerShell pentru administrarea sistemelor

PowerShell este un instrument versatil pentru administrarea sistemelor. De la comenzi simple pe o singură linie la fluxuri complexe de automatizare, simplifică sarcini care altfel ar necesita intervenție manuală. Oferă o platformă unificată de scripting pentru Windows, Linux și macOS, astfel încât administratorii pot folosi același set de instrumente în medii diferite.

### De la Command Prompt la Windows PowerShell

Dacă ești familiarizat cu Command Prompt și vrei să treci la Windows PowerShell, tranziția poate fi ușoară. Scripturile Windows PowerShell pornesc de la conceptele Command Prompt și oferă funcții mai avansate. Folosește-ți cunoștințele existente și explorează treptat funcțiile suplimentare și cmdleturile din PowerShell.

### Noțiuni de bază despre PowerShell

PowerShell oferă o interfață de linie de comandă pentru interacțiunea cu sistemul de operare. Comenzile sale se numesc cmdleturi și sunt organizate în module. Pentru a vedea modulele disponibile, folosește Get-Module:

```powershell
Get-Module
```

Pentru a vedea cmdleturile disponibile într-un modul, folosește Get-Command:
```powershell
Get-Command -Module <module name>
```

Pentru ajutor despre un cmdlet, folosește Get-Help:
```powershell
Get-Help <cmdlet name>
```

PowerShell acceptă și aliasuri, adică nume mai scurte pentru cmdleturi. Pentru a vedea aliasurile disponibile, folosește Get-Alias:
```powershell
Get-Alias
```

## Fișiere script și politica de execuție

Fișierele script PowerShell au extensia .ps1. Înainte să rulezi scripturi, poate fi necesar să stabilești politica de execuție, care determină dacă scripturile pot rula și ce tipuri sunt permise. Pentru a o configura, folosește cmdletul Set-ExecutionPolicy. De exemplu, pentru a permite rularea scripturilor:

```powershell
Set-ExecutionPolicy RemoteSigned
```

sau (doar pentru testare)

```powershell
Set-ExecutionPolicy Undefined
```

### Scripturi PowerShell

Scripturile PowerShell pot automatiza diverse sarcini administrative. Limbajul acceptă variabile, bucle, instrucțiuni condiționale și funcții, ceea ce îl face util pentru automatizare.

#### Variabile

Variabilele stochează date în scripturile PowerShell. Numele lor încep cu semnul dolarului ($). Pentru a atribui o valoare, folosește această sintaxă:
```powershell
$variable_name = value
```
De exemplu:
```powershell
$name = "John"
```
#### Bucle

Buclele repetă un bloc de cod de un număr stabilit de ori. PowerShell acceptă următoarele tipuri:

- **Bucla For**: repetă un bloc de cod de un număr stabilit de ori.
- **Bucla While**: repetă un bloc cât timp o condiție este adevărată.
- **Bucla Do-While**: execută un bloc cel puțin o dată, apoi îl repetă cât timp condiția este adevărată.
- **Bucla ForEach**: repetă un bloc pentru fiecare element dintr-o colecție.

De exemplu, codul următor folosește o buclă For pentru a afișa numerele de la 1 la 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Instrucțiuni condiționale

Instrucțiuni condiționale

Instrucțiunile condiționale execută un bloc de cod când o condiție este adevărată. PowerShell acceptă următoarele tipuri:

- **Instrucțiunea If**: execută un bloc dacă o condiție este adevărată.
- **Instrucțiunea If-Else**: execută un bloc când condiția este adevărată și altul când este falsă.
- **Instrucțiunea Switch**: compară o valoare cu mai multe potriviri posibile și execută blocul primei potriviri.

De exemplu, codul următor folosește If pentru a verifica dacă un număr este mai mare decât 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "Numărul este mai mare decât 5"
}
```
#### Funcții

Funcțiile sunt blocuri de cod reutilizabile care îndeplinesc o anumită sarcină. Ele primesc parametri de intrare și returnează valori. PowerShell acceptă următoarele tipuri:

- **Bloc de script**: un bloc de cod care poate fi executat.
- **Funcție avansată**: o funcție care include metadate și validarea parametrilor.

De exemplu, codul următor definește o funcție care adună două numere:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "Rezultatul este $result"
```
### PowerShell ISE

PowerShell ISE (mediu integrat de scripting) este o interfață grafică pentru scripturile PowerShell. Oferă un editor de text avansat, instrumente de depanare și alte funcții care simplifică scrierea și testarea scripturilor. Pentru a-l deschide:

1. Deschide meniul Start și introdu „PowerShell ISE” în bara de căutare.
2. Selectează „Windows PowerShell ISE” din rezultate.
3. PowerShell ISE se va deschide într-o fereastră nouă.

### PowerShell Remoting

PowerShell Remoting permite rularea comenzilor și scripturilor PowerShell pe computere la distanță. Serviciul WinRM trebuie să ruleze atât pe computerul local, cât și pe cel de la distanță. Pentru a activa PowerShell Remoting:

1. Deschide un prompt PowerShell cu privilegii de administrator.
2. Rulează această comandă pentru a activa PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. Rulează comanda următoare pentru a adăuga computerul la distanță în lista TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Repornește serviciul WinRM.
```powershell
Restart-Service WinRM
```

Pentru a rula o comandă pe un computer la distanță, folosește cmdletul Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Module PowerShell

Modulele PowerShell sunt colecții de cmdleturi, funcții și scripturi create pentru sarcini specifice. Le poți instala și gestiona din PowerShell Gallery, un depozit central pentru module PowerShell.

Pentru a instala un modul din PowerShell Gallery, folosește:
```powershell
Install-Module <module name>
```

Pentru a vedea modulele instalate, folosește Get-InstalledModule:
```powershell
Get-InstalledModule
```

### Bune practici pentru scripturile PowerShell

Când scrii **scripturi PowerShell**, respectă bune practici pentru ca acestea să fie **sigure**, **fiabile** și **ușor de întreținut**. Iată câteva recomandări:

- **Alege nume descriptive pentru variabile**: folosește nume care indică scopul lor.
- **Adaugă comentarii**: explică scopul codului.
- **Gestionează erorile**: tratează corespunzător erorile și excepțiile. Structura `Try...Catch...Finally` din PowerShell permite gestionarea excepțiilor și luarea măsurilor potrivite. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Testează bine scripturile**: verifică dacă funcționează conform așteptărilor. Poți folosi **Pester**, un cadru de testare pentru PowerShell, pentru a scrie și rula teste unitare. [Documentația Pester](https://pester.dev/)
- **Folosește funcții și module**: organizează codul și îmbunătățește reutilizarea. Funcțiile împart codul în componente mai mici, iar modulele permit împachetarea și distribuirea lui. [Despre funcții](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [Despre module](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Evită valorile fixe în cod**: folosește parametri sau variabile pentru a face scripturile mai flexibile și reutilizabile. Poți transmite parametri scripturilor cu ajutorul cuvântului-cheie `param`. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Folosește ieșirea detaliată**: afișează informații suplimentare despre progresul scriptului cu cmdletul `Write-Verbose`. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### Explicarea bunelor practici pentru scripturile PowerShell

#### Gestionează erorile

Gestionarea erorilor este esențială pentru ca un script PowerShell să trateze corespunzător erorile și excepțiile. PowerShell oferă mai multe metode: instrucțiunile Try-Catch și Trap, precum și parametrul ErrorAction. Try-Catch prinde și gestionează excepțiile, Trap prinde și gestionează erorile, iar ErrorAction controlează modul în care scriptul reacționează la erori.

Iată un exemplu de Try-Catch pentru tratarea unei erori:
```powershell
try {
    # cod care poate genera o eroare
}
catch {
    Write-Error "A apărut o eroare: $_"
}
```

#### Testează bine scripturile

Testarea scripturilor PowerShell confirmă că funcționează conform așteptărilor. Instrumente și cadre precum Pester permit scrierea și rularea testelor. Ele ajută la identificarea și izolarea problemelor din cod și verifică dacă scriptul îndeplinește cerințele.

Iată un exemplu de folosire a Pester pentru testarea unui script PowerShell:
```powershell
Describe "Scriptul meu PowerShell" {
    It "Efectuează o acțiune" {
        # cod care ar trebui să returneze rezultatul așteptat
        $result = Do-Something
        $result | Should -Be "rezultatul așteptat"
    }
}
```

#### Folosește funcții și module

Funcțiile și modulele ajută la organizarea și reutilizarea codului. Funcțiile grupează codul în blocuri reutilizabile, iar modulele permit împachetarea și partajarea lui. Astfel, scripturile devin mai modulare, eficiente și ușor de întreținut.

Iată un exemplu de funcție PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "Rulează $count procese."
```

#### Evită valorile fixe în cod

Valorile fixe reduc flexibilitatea scripturilor PowerShell și îngreunează întreținerea. Folosește în schimb parametri sau variabile, astfel încât utilizatorii să poată furniza valori în timpul rulării. Scriptul devine mai reutilizabil și adaptabil.

Iată un exemplu de parametru PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Salut, $name!"
```

#### Folosește ieșirea detaliată

Ieșirea detaliată oferă informații despre progresul scriptului și ajută la depanare și la rezolvarea problemelor. Cmdletul Write-Verbose afișează informații detaliate în consolă, astfel încât scripturile să fie mai ușor de înțeles și depanat.

Iată un exemplu de ieșire detaliată în PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Se obțin procesele..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "Rulează $count procese."
```

### Zece idei de scripturi PowerShell pentru începători

Dacă ești la început cu scripturile PowerShell, încearcă aceste zece idei:

- **Copii de rezervă automate**: creează un script care copiază fișiere și directoare importante pe un hard disk extern sau într-un serviciu de stocare în cloud. Folosește `Copy-Item` pentru copiere și `Start-Job` pentru a rula copia în fundal. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Gestionarea fișierelor**: creează un script care organizează fișierele și directoarele în foldere după tip, dimensiune sau alte criterii. Folosește `Get-ChildItem` pentru a găsi fișiere și `Move-Item` pentru a le muta în locul dorit. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Informații despre sistem**: creează un script care colectează informații precum utilizarea procesorului și a memoriei, spațiul pe disc și setările de rețea, apoi le afișează într-un format ușor de citit. Folosește `Get-WmiObject` pentru colectare și `Format-Table` sau `Out-GridView` pentru formatare. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Gestionarea utilizatorilor**: creează un script pentru adăugarea, modificarea sau ștergerea utilizatorilor și grupurilor Windows. Folosește `New-LocalUser`, `Set-LocalUser` și `Remove-LocalUser` pentru utilizatori, respectiv `New-LocalGroup`, `Add-LocalGroupMember` și `Remove-LocalGroup` pentru grupuri. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Instalarea software-ului**: creează un script care instalează și configurează software pe mai multe computere simultan. Folosește `Invoke-Command` pentru a executa comenzi de instalare pe computere la distanță. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Configurarea rețelei**: creează un script care configurează automat adrese IP, măști de subrețea și gatewayuri implicite. Folosește `Set-NetIPAddress`, `Set-NetIPInterface` și `Set-DnsClientServerAddress` pentru configurare. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Securitate**: creează un script care auditează și monitorizează setările de securitate și alertează utilizatorul dacă detectează modificări. Folosește `Get-AuditPolicy` pentru a prelua politicile de audit și `Send-MailMessage` pentru a trimite notificări prin e-mail. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Planificarea sarcinilor**: creează un script care planifică și automatizează sarcini recurente, precum copiile de rezervă, actualizările și scanările sistemului. Folosește `Register-ScheduledTask` pentru a crea sarcini planificate și `Start-ScheduledTask` pentru a le porni. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Modificarea registrului**: creează un script care modifică sau citește valori din chei de registru specifice. Folosește `Get-ItemProperty` și `Set-ItemProperty` pentru a interacționa cu registrul. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Administrare la distanță**: creează un script care activează administrarea la distanță a computerelor Windows, astfel încât utilizatorii să poată rula comenzi și scripturi pe mașini la distanță. Folosește `Enter-PSSession` sau `Invoke-Command` pentru comenzi la distanță. [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Documentația Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Explorează aceste idei pentru a căpăta experiență practică și a-ți extinde cunoștințele despre scripturile PowerShell.

## Concluzie

PowerShell este un instrument puternic pentru gestionarea și automatizarea Windows și a altor tehnologii Microsoft. În acest articol am prezentat bazele scripturilor pentru începători: instalarea și pornirea PowerShell, folosirea cmdleturilor, variabilelor, buclelor, instrucțiunilor condiționale și funcțiilor, precum și PowerShell ISE, PowerShell Remoting și modulele. Respectarea bunelor practici ajută la crearea unor scripturi sigure, fiabile și ușor de întreținut. Cu exercițiu, poți deveni priceput la PowerShell și automatiza cu ușurință diverse sarcini administrative.

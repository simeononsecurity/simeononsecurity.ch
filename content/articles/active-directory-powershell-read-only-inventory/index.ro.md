---
title: "Creează un inventar Active Directory doar pentru citire cu PowerShell"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Inventariază unitățile organizaționale, utilizatorii și computerele Active Directory cu interogări PowerShell limitate. Exportă fișiere CSV verificabile fără să modifici obiecte din director."
genre: ["Active Directory", "PowerShell", "Administrarea sistemelor"]
tags: ["Inventar Active Directory", "Inventar AD cu PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "AD doar pentru citire", "Export utilizatori AD", "Export computere AD", "Export OU AD", "Export-Csv", "RSAT", "Audit de director", "Rapoarte AD", "Inventar OU", "Windows Server", "Script PowerShell", "Modul AD", "Igiena directorului"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Arbore Active Directory din care înregistrările utilizatorilor, computerelor și unităților organizaționale ajung în trei fișiere de verificare."
coverCaption: "Limitează interogarea, apoi exportă doar câmpurile necesare pentru verificare."
---
Curățarea Active Directory începe cu o listă de încredere a obiectelor existente. Acest **inventar doar pentru citire** adună unitățile organizaționale, utilizatorii și computerele dintr-un domeniu ales. Exportă trei fișiere CSV (valori separate prin virgulă) pentru verificare, fără să modifice obiecte din director. Protejează totuși fișierele, deoarece numele și detaliile dispozitivelor dezvăluie o parte din mediul tău.

<!--more-->

## Idei principale

- **Alege domeniul:** interoghează o unitate organizațională înainte să extinzi căutarea la întregul domeniu.
- **Folosește comenzi de citire:** `Get-ADOrganizationalUnit`, `Get-ADUser` și `Get-ADComputer` preiau obiecte.
- **Selectează câmpurile:** exportă doar proprietățile necesare sarcinii.
- **Verifică rezultatul:** compară numărul de obiecte și câteva rânduri de exemplu înainte să te bazezi pe raport.

## Înainte să începi

Ai nevoie de un host de administrare Windows cu DNS funcțional și acces de rețea la un controler de domeniu, de modulul PowerShell **ActiveDirectory**, de un cont aprobat să citească obiectele selectate și de un folder protejat pentru ieșirea CSV. Pe un client Windows, modulul face parte din instrumentele Active Directory din Remote Server Administration Tools (RSAT). [Ghidul modulului Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) explică instalarea. Microsoft oferă [referința cmdleturilor](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) și [opțiunile de instalare RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Acest ghid folosește sintaxa Windows PowerShell și nu modifică obiectele directorului.

Permisiunile directorului se aplică în continuare. În [îndrumările pentru conturile privilegiate](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), Microsoft explică faptul că listele de control al accesului permit adesea utilizatorilor autentificați să citească informații generale, dar restricționează câmpurile sensibile și modificările. Începe cu un cont aprobat și o OU de test. Nu ridica privilegiile la Domain Admin doar pentru ca inventarul să reușească.

> **Atenție:** fișierele CSV conțin nume de conturi și computere. Salvează-le într-o locație aprobată, limitează accesul și șterge copiile suplimentare după verificare. Nu publica un export brut și nu îl atașa la un issue public.

## Alege baza de căutare

O **unitate organizațională (OU)** grupează obiecte din director. **Numele distinct (DN)** indică poziția unității în arborele directorului. Parametrul `-SearchBase` limitează interogarea la DN-ul ales. Fără un domeniu stabilit intenționat, un filtru larg poate returna mult mai multe obiecte decât ai nevoie să verifici.

Mai întâi încarcă modulul și afișează DN-ul domeniului curent:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

Microsoft documentează [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) și informațiile despre domeniu pe care le returnează cmdletul. Găsește OU-ul pe care vrei să îl verifici înainte să stabilești baza de căutare:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Copiază DN-ul exact din rezultat. În exemplele următoare, înlocuiește această valoare de documentație cu DN-ul OU-ului tău:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` este un domeniu de exemplu pentru documentație. Nu copia DN-ul lui într-o interogare reală. Dacă ai nevoie intenționat de un inventar pentru întregul domeniu, setează `$SearchBase` la DN-ul domeniului și notează domeniul mai larg în raport. Referința Microsoft pentru [Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) documentează `-Filter` și `-SearchBase`.

## Inventariază OU-uri, utilizatori și computere

Începe prin a număra obiectele. Astfel observi rapid o bază de căutare greșită sau un rezultat gol neașteptat:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` preia toate obiectele care corespund din baza de căutare. Microsoft documentează [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) și [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) ca ordine de preluare. Un număr zero poate fi corect, dar verifică DN-ul, permisiunile și domeniul țintă înainte să consideri inventarul complet.

Acum previzualizează câteva rânduri în consolă. Salvează câmpurile selectate pentru ca previzualizarea și exportul CSV ulterior să folosească aceleași coloane:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Pentru computere, solicită proprietatea suplimentară a sistemului de operare doar dacă ai nevoie de ea pentru verificare:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

Parametrul `-Properties` solicită proprietăți care nu fac parte din setul implicit al cmdletului. Microsoft îl documentează în [referința cmdletului pentru computere](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer). Tratează numele sistemelor de operare ca date din director, nu ca dovadă a versiunii instalate acum. Un obiect de computer poate fi învechit sau atributul lui poate să nu fi fost actualizat.

## Exportă fișiere CSV verificabile

Alege un folder de ieșire aprobat cu suficient spațiu. Comenzile următoare scriu **fișiere CSV locale** și nu modifică obiecte din director. Rulează-le din acel folder. `-NoClobber` împiedică suprascrierea fișierelor existente. Folosește un folder sau un nume de fișier nou la fiecare rulare.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

Referința Microsoft pentru [Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) explică `-NoTypeInformation`, `-Encoding` și `-NoClobber`. Deschide fiecare CSV într-un editor de text sau într-o aplicație aprobată pentru foi de calcul. Verifică antetul, câteva rânduri și numărul de înregistrări față de numărătoarea anterioară. O comandă eșuată sau un fișier de zero octeți nu dovedește că raportul este complet.

> **Rezultat așteptat:** ai trei fișiere CSV cu înregistrări OU, utilizatori și computere din domeniul de director ales. Numărul de rânduri și valorile de exemplu corespund domeniului selectat.

## Verifică fără să modifici obiecte

Folosește inventarul pentru întrebări concrete: ce OU răspunde de un computer? Ce conturi de utilizator sunt dezactivate? Ce nume de dispozitive au nevoie de un proprietar? Notează constatările separat. Nu deduce din valoarea `Enabled` dacă un cont mai este necesar. Nu șterge și nu dezactiva obiecte doar pe baza unui export.

Pentru rapoarte recurente, notează data interogării, domeniul, DN-ul OU-ului, proprietățile selectate, operatorul și locația CSV-ului. Când compari două exporturi, confirmă că au folosit același domeniu și aceleași câmpuri. Altfel, diferența poate proveni din interogare, nu dintr-o schimbare reală a directorului.

Acesta este un **inventar**, nu un audit al conturilor privilegiate și nici un raport de activitate de conectare. Microsoft precizează că proprietățile și permisiunile Active Directory diferă în funcție de obiect și mediu. Verifică un atribut de sistem de operare sau un nume afișat cu proprietarul sistemului înainte să acționezi. [Ghidul de securitate Active Directory](/articles/active-directory-security-best-practices/) acoperă controale de securitate mai ample.

## Depanare

- **Modulul nu se importă:** confirmă că pe host sunt instalate instrumentele Active Directory din RSAT sau instrumentele de administrare Windows Server. Urmează [ghidul de configurare a modulului](/articles/active-directory-module-powershell-installation-usage-guide/).
- **Interogarea nu returnează obiecte:** verifică DN-ul exact, domeniul curent, conținutul OU-ului și permisiunile de citire. Testează o OU mică și cunoscută înainte să extinzi domeniul.
- **O proprietate este goală:** confirmă că atributul există și că acel cont îl poate citi. Nu completa câmpurile lipsă prin presupuneri.
- **Exportul spune că fișierul există deja:** `-NoClobber` a protejat raportul anterior. Alege un nume de fișier sau un folder nou și rulează din nou comanda.
- **Numărul diferă de așteptări:** verifică dacă utilizatorii sau computerele sunt în alt OU, dacă domeniul s-a schimbat și dacă directorul s-a modificat în timpul interogării.

## Pașii următori

Păstrează fișierele CSV brute într-o locație protejată pe durata perioadei de verificare convenite. Distribuie doar câmpurile necesare persoanei care verifică. După ce proprietarii confirmă constatările, planifică modificările prin procesul obișnuit de aprobare și revenire. După modificările aprobate, rulează din nou același inventar în același domeniu pentru a confirma rezultatul.
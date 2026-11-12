---
title: "Înțelegerea filtrării WMI"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Aflați cum să folosiți filtrarea WMI pentru a aplica obiectele de politică de grup (GPO) sistemelor potrivite, cu exemple practice și bune practici."
genre: ["Administrarea Windows", "Politici de grup", "Administrarea sistemelor", "Administrarea rețelelor", "Infrastructură IT", "Administrarea politicilor", "Guvernanță IT", "Automatizare IT", "Active Directory", "Conformitate de securitate"]
tags: ["filtrare WMI", "GPO", "obiecte de politică de grup", "filtre WMI", "direcționarea politicilor", "interogări WMI", "Windows Management Instrumentation", "control GPO", "Consola de gestionare a politicilor de grup", "Limbajul de interogare WMI", "aplicarea politicilor", "WQL", "ajustarea politicilor", "administrarea politicilor", "resurse de sistem", "exemple de direcționare a politicilor", "administrarea sistemelor", "administrarea rețelelor", "administrarea infrastructurii IT", "automatizare IT", "administrarea Active Directory", "conformitate de securitate", "tehnici de control al politicilor", "bune practici de administrare a politicilor", "filtrarea politicilor", "strategii de control GPO", "securitate GPO", "beneficiile filtrării WMI", "implementarea filtrării WMI", "bune practici pentru filtre WMI"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Ilustrație cu o lupă îndreptată spre o pictogramă de filtru, care reprezintă direcționarea GPO prin filtrare WMI."
coverCaption: "Folosiți filtrarea WMI pentru a direcționa eficient politicile GPO."
---

## Introducere

În obiectele de politică de grup (GPO), [**filtrarea WMI**](https://simeononsecurity.com/github/wmi-filters/) controlează computerele sau utilizatorii asupra cărora se aplică politicile, în funcție de rezultatele interogărilor WMI (Windows Management Instrumentation). Administratorii pot astfel să rafineze direcționarea și să aplice politicile numai sistemelor dorite. Acest articol explică filtrarea WMI, modul în care funcționează în GPO, crearea de [filtre WMI](https://simeononsecurity.com/github/wmi-filters/) și câteva exemple practice.

## [Ce este filtrarea WMI?](https://simeononsecurity.com/github/wmi-filters/)

[**Filtrarea WMI**](https://simeononsecurity.com/github/wmi-filters/) aplică filtre GPO-urilor pe baza rezultatelor interogărilor WMI. WMI este o infrastructură de administrare integrată în sistemele de operare Windows. Aceasta le permite administratorilor să obțină date de administrare și să interacționeze programatic cu resursele sistemului. Prin filtrarea WMI, GPO-urile pot fi direcționate dinamic în funcție de criterii definite prin interogări.

Filtrele WMI sunt scrise în WMI Query Language (WQL), un subset al SQL (Structured Query Language). De obicei, ele se bazează pe proprietățile și valorile disponibile într-un spațiu de nume WMI. Administratorii pot combina condiții, operatori logici și spații de nume pentru a crea interogări care vizează anumite computere sau utilizatori.

## Cum funcționează filtrarea WMI în GPO?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Diagramă de flux în care un filtru WMI asociat unui obiect de politică de grup evaluează o interogare WQL ca True sau False și decide dacă GPO se aplică unui computer țintă" >}}

În Politica de grup, **filtrarea WMI** permite aplicarea selectivă a GPO-urilor în funcție de evaluarea **interogărilor WMI**. Când asociați un **filtru WMI** unei GPO, rezultatul **True** sau **False** stabilește dacă GPO se aplică.

Filtrele folosesc **WMI Query Language (WQL)**, un subset al SQL. Cu WQL se pot crea interogări complexe bazate pe diverse **proprietăți** și **valori** disponibile într-un **spațiu de nume WMI**. Astfel, puteți viza anumite computere sau utilizatori.

De exemplu, o organizație poate dori să aplice o GPO numai computerelor care rulează Windows 10. Poate crea un filtru WMI care verifică proprietatea **OperatingSystem** a clasei **Win32_OperatingSystem**. Interogarea WMI ar putea arăta astfel:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

Interogarea verifică dacă versiunea sistemului de operare începe cu „10.”, ceea ce indică Windows 10. Dacă rezultatul este **True**, GPO se aplică computerului țintă. În caz contrar, nu se aplică.

Filtrarea WMI acceptă și condiții și operatori logici precum **AND**, **OR** și **NOT**. Administratorii pot combina mai multe proprietăți și valori pentru un control mai precis asupra aplicării GPO.

De asemenea, diferitele **spații de nume WMI** oferă acces la anumite grupuri de clase și proprietăți WMI. GPO-urile pot fi direcționate în funcție de configurația hardware, software-ul instalat, setările de rețea și alte criterii.

Pentru detalii despre crearea filtrelor și interogărilor WMI, consultați documentația Microsoft despre [filtrarea WMI pentru Politica de grup](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

Filtrarea WMI ajută administratorii să adapteze aplicarea GPO-urilor la anumite computere sau utilizatori, în funcție de condiții dinamice, și să gestioneze mai bine mediul IT.

## Crearea filtrelor WMI pentru GPO

Urmați acești pași pentru a crea un filtru WMI pentru o GPO:

1. Deschideți **Consola de gestionare a politicilor de grup** (GPMC) pe un computer Windows conectat la domeniu.

2. Extindeți domeniul și accesați nodul **WMI Filters**.

3. Faceți clic dreapta pe **WMI Filters** și selectați **New**.

4. Dați filtrului un nume descriptiv și introduceți interogarea WMI în câmpul **Query**. Folosiți sintaxa WQL.

5. Faceți clic pe **OK** pentru a salva filtrul WMI.

După creare, filtrul poate fi asociat uneia sau mai multor GPO. Pentru a-l asocia unei GPO:

1. Faceți clic dreapta pe GPO dorită și selectați **Properties**.

2. În fereastra cu proprietățile GPO, deschideți fila **WMI Filtering**.

3. Selectați din listă filtrul WMI dorit.

4. Faceți clic pe **OK** pentru a salva modificările.

Asocierea filtrelor WMI cu GPO-uri permite direcționarea precisă a politicilor în funcție de rezultatele interogărilor WMI.

## Câte filtre WMI se pot configura pentru o GPO?

Administratorii pot configura **mai multe filtre WMI** pentru o GPO, pentru a direcționa politicile cu precizie. Nu există o limită specifică a numărului de filtre asociate unei singure GPO, astfel că sunt posibile combinații complexe.

Totuși, trebuie luat în calcul efectul numărului de filtre asupra timpului de procesare a GPO. Pe măsură ce numărul lor crește, evaluarea și aplicarea GPO-urilor pot dura mai mult. Pentru aplicarea eficientă a politicilor, păstrați un număr rezonabil de filtre.

De exemplu, o organizație poate dori ca o GPO să se aplice numai computerelor care rulează Windows 10 și au instalat un anumit software. Poate crea două filtre WMI separate: unul pentru **sistemul de operare** și altul pentru **instalarea software-ului**. Împreună, acestea selectează computerele dorite.

Este important să găsiți echilibrul dintre numărul de filtre necesare pentru cerințele de direcționare și timpul de procesare. Înainte de a decide numărul filtrelor, evaluați complexitatea mediului, numărul de computere sau utilizatori și efectele posibile asupra performanței.

Mai multe filtre WMI ajută la optimizarea direcționării GPO și păstrează eficiența procesării și administrării mediului IT.

## Exemple practice de filtrare WMI în GPO

Filtrarea WMI oferă soluții practice pentru aplicarea direcționată a politicilor. Iată câteva exemple:

1. **Direcționarea anumitor sisteme de operare**: pentru a aplica o GPO numai computerelor cu **Windows 10**, creați un filtru care verifică versiunea sistemului de operare, de exemplu `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. Astfel selectați computerele Windows 10.

2. **Politici diferite pentru desktopuri și laptopuri**: dacă politicile diferă în funcție de tipul dispozitivului, folosiți două filtre WMI. Unul poate identifica desktopurile pe baza atributelor hardware, de exemplu `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, iar celălalt poate distinge laptopurile. Aplicați astfel politici potrivite fiecărui tip.

3. **Aplicarea selectivă în funcție de spațiul pe disc**: pentru a evita politicile intensive pe computerele cu spațiu redus, creați un filtru care verifică spațiul liber. De exemplu, interogarea `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` exclude computerele cu mai puțin de 10 GB liberi.

Aceste exemple arată flexibilitatea **filtrării WMI** în GPO și le permit administratorilor să direcționeze politicile după criterii specifice.

## Concluzie

Filtrarea WMI este o funcție utilă a obiectelor de politică de grup. Administratorii pot aplica selectiv politicile în funcție de rezultatele interogărilor WMI. Filtrele direcționează politicile către anumite computere sau utilizatori și fac administrarea mai eficientă și mai controlată. Acest articol a prezentat conceptul, funcționarea în GPO, crearea filtrelor și exemple practice.

Prin includerea filtrării WMI în administrarea GPO, creșteți precizia aplicării politicilor și vă asigurați că acestea se aplică numai țintelor dorite.

## Referințe

- [Microsoft Docs: Crearea filtrelor WMI pentru GPO](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Politica de grup](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Consola de gestionare a politicilor de grup](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))

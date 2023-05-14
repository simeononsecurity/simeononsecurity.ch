---
title: "Eficientizați actualizările Windows cu automatizare folosind Chocolatey, PSWindowsUpdate și Scripturi de pornire"
date: 2020-07-22
---
 Actualizări Windows cu Chocolatey, PSWindowsUpdate și scripturi de pornire**

În mediul de afaceri rapid de astăzi, timpul este esențial pentru administratorii de sistem. Actualizarea mașinilor Windows, un aspect critic al administrării sistemelor, poate fi o sarcină extrem de consumatoare de timp, care poate dura până la o săptămână, având în vedere suficiente sisteme. Cu toate acestea, cu o oarecare asistență din partea Chocolatey, PSWindowsUpdates și Scripturi de pornire, acum este posibil să lansați actualizări cu o singură repornire a fiecărei mașini, reducând semnificativ timpul necesar pentru a efectua actualizări.

## Raționalizarea actualizărilor Windows cu automatizare

Actualizările Windows sunt esențiale pentru menținerea stabilității și securității mașinilor Windows. Efectuarea actualizărilor pe un număr mare de mașini poate fi o sarcină consumatoare de timp, în special pentru administratorii de sistem cu resurse limitate. Cu toate acestea, cu utilizarea instrumentelor de automatizare precum Chocolatey, PSWindowsUpdate și Scripturi de pornire, acest proces poate fi simplificat pentru a permite administratorilor să efectueze actualizări cu efort minim.

### Ciocolată

[Chocolatey](https://chocolatey.org/) este un manager de pachete pentru Windows care poate fi folosit pentru a automatiza instalarea software-ului pe mașinile Windows. Este similar cu apt-get pe Ubuntu sau cu homebrew pe macOS și poate fi folosit pentru a instala și gestiona o gamă largă de pachete software. Chocolatey poate fi folosit pentru a instala pachete în tăcere, ceea ce înseamnă că pot fi instalate fără intervenția utilizatorului.

### PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) este un modul PowerShell care poate fi folosit pentru a automatiza instalarea actualizărilor Windows. Oferă cmdlet-uri care pot fi folosite pentru a instala, dezinstala și lista actualizări Windows. PSWindowsUpdate este un instrument puternic care poate fi utilizat pentru a gestiona actualizările Windows pe mai multe mașini, ceea ce îl face ideal pentru administratorii de sistem care trebuie să gestioneze un număr mare de mașini.

### Scripturi de pornire

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) sunt scripturi care pot fi folosite pentru a automatiza sarcinile care trebuie efectuate atunci când o mașină pornește sau se oprește. Aceste scripturi pot fi utilizate pentru a efectua sarcini precum instalarea de software, configurarea setărilor și gestionarea actualizărilor Windows.

## Automatizarea actualizărilor Windows cu o singură repornire

Pentru a automatiza actualizările Windows folosind Chocolatey, PSWindowsUpdate și Scripturi de pornire, administratorii pot urma ghidul pas cu pas de mai jos.

### Configurarea scriptului de închidere
Descărcați toate fișierele de suport din[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Deschideți Editorul de politici de grup local apăsând **„Win + R”** și tastând **„gpedit.msc”** urmat de **„Ctrl + Shift + Enter”**.
2. Navigați la Computer **Configuration\Windows Settings\Scripts (Startup/Shutdown)**.
3. În panoul de rezultate, faceți dublu clic pe Închidere.
4. Selectați fila PowerShell.
5. În caseta de dialog Shutdown Properties, faceți clic pe Add.
6. În caseta Nume script, introduceți calea către script sau faceți clic pe Răsfoire pentru a căuta „*chocoautomatewindowsupdates.ps1*” în folderul partajat Netlogon de pe controlerul de domeniu.
7. Reporniți.

Acum, tot ce trebuie să facă un administrator este să repornească computerul pentru a efectua actualizări Windows.

### Înțelegerea scriptului

Scriptul folosit pentru automatizarea actualizărilor Windows este intitulat „*chocoautomatewindowsupdates.ps1*”. Îndeplinește următoarele sarcini:

1. Instalează managerul de pachete Chocolatey.
2. Activează câteva modificări de configurare Chocolatey preferate.
3. Actualizează toate pachetele Chocolatey instalate.
4. Instalează modulul PSWindowsUpdate PowerShell.
5. Adaugă managerul de servicii Windows Update.
6. Instalează toate actualizările Windows disponibile.
7. Instalează toate driverele lipsă sau actualizările cerute de actualizările instalate anterior.

### Beneficiile automatizării actualizărilor Windows

Automatizarea actualizărilor Windows folosind Chocolatey, PSWindowsUpdate și Scripturi de pornire are mai multe beneficii pentru administratorii de sistem. Aceste beneficii includ:

- **Economie de timp**: automatizarea actualizărilor Windows reduce semnificativ timpul necesar pentru a efectua actualizări. Administratorii nu mai trebuie să instaleze manual actualizări pe fiecare computer.
- **Consecvență**: automatizarea actualizărilor Windows asigură că actualizările sunt instalate în mod consecvent pe toate mașinile. Acest lucru reduce probabilitatea erorilor și a vulnerabilităților de securitate.
- **Gestionare centralizată**: automatizarea actualizărilor Windows permite administratorilor să gestioneze actualizările dintr-o locație centrală, facilitând urmărirea actualizărilor instalate și a mașinilor care au nevoie de actualizări.
- **Securitate sporită**: automatizarea actualizărilor Windows asigură că mașinile sunt ținute la zi cu cele mai recente corecții de securitate, reducând riscul de încălcare a securității.

### Concluzie

Automatizarea actualizărilor Windows folosind Chocolatey, PSWindowsUpdate și Scripturi de pornire este un instrument puternic care poate economisi mult timp și efort administratorilor de sistem. Acesta permite ca actualizările să fie instalate în mod consecvent și eficient, asigurând că mașinile sunt la zi cu cele mai recente corecții de securitate. Urmând pașii prezentați în acest tutorial, administratorii pot automatiza actualizările Windows cu o singură repornire, făcând procesul de actualizare a mașinilor Windows mult mai rapid și mai ușor.

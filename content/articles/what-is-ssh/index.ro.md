---
title: "Puterea SSH: Accesul la distanță și gestionarea securizată la distanță simplificate"
date: 2023-06-14
toc: true
draft: false
description: "Descoperiți beneficiile SSH, învățați cum să generați chei SSH, să vă conectați la servere la distanță, să transferați fișiere în siguranță și să personalizați configurațiile SSH."
tags: ["SSH", "Secure Shell", "acces de la distanță", "gestionare la distanță", "criptare", "autentificare", "integritatea datelor", "portabilitate", "transfer de fișiere", "SCP", "Chei SSH", "Configurația SSH", "protocol de rețea", "executarea comenzilor de la distanță", "OpenSSH", "autentificare cu doi factori", "criptografie cu cheie publică", "Adresa IP", "nume de domeniu", "terminal", "prompt de comandă", "securitate", "administratori de sistem", "dezvoltatori", "versatilitate", "metode de autentificare", "funcții hash", "tunelare", "opțiuni personalizate"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_securely_connecting.png"
coverAlt: "O ilustrație de desen animat a unei persoane care se conectează în siguranță la un server folosind SSH."
coverCaption: ""
---

**Ce este SSH și cum se utilizează?**

SSH (Secure Shell) este un protocol de rețea care oferă o metodă sigură și criptată de accesare a calculatoarelor și serverelor de la distanță. Acesta permite utilizatorilor să se conecteze și să gestioneze în siguranță sistemele la distanță printr-o rețea nesecurizată, cum ar fi internetul. Acest articol va oferi o prezentare generală a SSH, a beneficiilor sale și a modului de utilizare eficientă a acestuia.

{{< youtube id="Atbl7D_yPug" >}}

## Beneficiile SSH

Utilizarea SSH pentru accesul la distanță oferă mai multe avantaje, printre care:

1. **Securitate**: SSH utilizează algoritmi puternici de criptare pentru a securiza comunicarea dintre client și server. Acesta asigură faptul că datele transmise prin rețea nu pot fi interceptate sau alterate de entități rău intenționate.

2. **Autentificare**: SSH utilizează diverse metode de autentificare, cum ar fi parolele, criptografia cu cheie publică și autentificarea cu doi factori, pentru a verifica identitatea utilizatorilor care se conectează la sisteme la distanță. Acest lucru ajută la prevenirea accesului neautorizat.

3. **Integritatea datelor**: SSH asigură integritatea datelor transmise între client și server. Acesta utilizează funcții criptografice hash pentru a detecta orice modificare sau alterare în timpul transmiterii.

4. **Portabilitate**: SSH este acceptat de o gamă largă de sisteme de operare și dispozitive, ceea ce îl face o alegere versatilă pentru accesul la distanță pe diferite platforme.

5. **Flexibilitate**: SSH poate fi utilizat în diverse scopuri, inclusiv pentru executarea de comenzi de la distanță, transferul de fișiere și tunelizarea altor protocoale precum FTP și VNC.

## Cum se utilizează SSH

### Generarea cheilor SSH

Înainte de a utiliza SSH, trebuie să generați o pereche de chei SSH. Perechea de chei este formată dintr-o cheie publică și o cheie privată. Cheia publică este plasată pe serverul de la distanță, în timp ce cheia privată este păstrată în siguranță pe calculatorul dvs. local. Pentru a genera o pereche de chei SSH, urmați acești pași:

1. 1. Instalați **OpenSSH** pe calculatorul dvs. local, dacă nu este deja instalat. Consultați documentația oficială a sistemului dumneavoastră de operare pentru instrucțiuni de instalare.

2. Deschideți un terminal sau un prompt de comandă și rulați următoarea comandă pentru a genera perechea de chei:

```shell
ssh-keygen -t rsa -b 4096
```

3. Vi se va solicita să introduceți un nume de fișier pentru perechea de chei și o frază de trecere opțională. Apăsați Enter pentru a accepta numele de fișier implicit și lăsați parola de acces necompletată dacă nu doriți să utilizați una.

4. Perechea de chei va fi generată, iar cheia publică va fi salvată într-un fișier cu un nume de fișier `.pub` extensie. Cheia privată va fi salvată într-un fișier fără extensie.

### Conectarea la un server la distanță

Pentru a vă conecta la un server la distanță folosind SSH, urmați acești pași:

1. Obțineți **adresa IP** sau numele de domeniu al serverului la distanță la care doriți să vă conectați.

2. Deschideți un terminal sau un prompt de comandă și utilizați următoarea comandă pentru a iniția o conexiune SSH:

```shell
ssh username@remote_server_ip
```

Înlocuiți `username` cu numele de utilizator de pe serverul de la distanță și `remote_server_ip` cu adresa IP reală sau numele de domeniu al serverului.

3. Dacă este prima dată când vă conectați la server, este posibil să apară un avertisment cu privire la autenticitatea gazdei. Verificați amprenta digitală a serverului în raport cu o sursă de încredere înainte de a continua.

4. Atunci când vi se solicită, introduceți parola sau furnizați calea către cheia privată dacă utilizați autentificarea bazată pe cheie. Dacă autentificarea este reușită, veți fi conectat la serverul la distanță.

### Transfer de fișiere cu SSH

SSH poate fi utilizat, de asemenea, pentru transferul securizat de fișiere între calculatorul dvs. local și un server la distanță. Cel mai comun instrument pentru transferul de fișiere prin SSH este **SCP** (Secure Copy). Urmați acești pași pentru a transfera fișiere utilizând SCP:

1. 1. Deschideți un terminal sau un prompt de comandă pe mașina dvs. locală.

2. Utilizați următoarea comandă pentru a copia un fișier de pe calculatorul local pe serverul de la distanță:

```shell
scp /path/to/local/file username@remote_server_ip:/path/to/remote/location
```


Înlocuiți `/path/to/local/file` cu calea reală și numele fișierului de pe calculatorul local. În mod similar, înlocuiți `username@remote_server_ip:/path/to/remote/location` cu numele de utilizator corespunzător, IP-ul sau domeniul serverului și locația fișierului la distanță.

3. Dacă este prima dată când vă conectați la server, este posibil să apară un avertisment cu privire la autenticitatea gazdei. Verificați amprenta digitală a serverului înainte de a continua.

4. Introduceți parola sau furnizați calea către cheia privată dacă vi se solicită. Fișierul va fi copiat în siguranță pe serverul de la distanță.

### SSH Configuration

Fișierele de configurare SSH vă permit să personalizați și să reglați cu precizie comportamentul clientului SSH. Fișierul principal de configurare este de obicei localizat la `/etc/ssh/sshd_config` pe partea serverului și `~/.ssh/config` pe partea clientului. Prin editarea acestor fișiere, puteți defini opțiuni personalizate, cum ar fi numele de utilizator, numerele de port și setările de conectare implicite.

## Concluzie

SSH este un protocol puternic și sigur pentru accesarea și gestionarea de la distanță a serverelor și calculatoarelor. Criptarea sa puternică, mecanismele de autentificare și versatilitatea sa îl fac un instrument esențial pentru administratorii de sistem, dezvoltatori și persoanele care au nevoie de acces la distanță securizat. Urmând pașii descriși în acest articol, puteți începe să folosiți SSH în mod eficient și să profitați de caracteristicile sale.

______

## Referințe

- [SSH on Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell)
- [SCP Documentation](https://man.openbsd.org/scp)
- [SSH Configuration File Documentation](https://man.openbsd.org/sshd_config)

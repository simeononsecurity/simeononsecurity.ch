---
title: "Ghid pentru începători: Utilizarea liniei de comandă Linux pentru securitatea cibernetică"
date: 2023-03-13
toc: true
draft: false
description: "Învățați cum să utilizați linia de comandă Linux pentru securitatea cibernetică cu comenzi de bază și avansate."
tags: ["Linux", "Linia de comandă", "Securitatea cibernetică", "Ghid pentru începători", "Scanarea rețelei", "Testarea vulnerabilității", "Analiza malware-ului", "Permisiuni", "Traficul de rețea", "Starea procesului", "Statistici de rețea", "Căutare fișiere", "Wireshark", "TCPDump", "Nmap", "Linux CLI", "Securitate", "Testarea de penetrare", "Criminalistică digitală"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_wearing_a_hoodie.png"
coverAlt: "O ilustrație de desen animat a unei persoane care poartă un hanorac cu glugă, care stă în fața unui ecran de calculator pe care este vizibilă interfața liniei de comandă Linux și care ține în mână o lupă pentru a reprezenta aspectul de securitate cibernetică."
coverCaption: ""
---

**Linux** este un sistem de operare versatil și sigur care este utilizat pe scară largă în industria securității cibernetice datorită naturii sale open-source. Cu toate acestea, poate fi descurajant pentru începători să utilizeze interfața liniei de comandă Linux (CLI) pentru a efectua sarcini de securitate cibernetică. Acest ghid își propune să ofere începătorilor o prezentare generală a comenzilor CLI Linux de bază și avansate, utile în scopuri de securitate cibernetică.

## Comenzi Linux de bază pentru securitatea cibernetică

### Print Working Directory (Imprimă directorul de lucru)

Comanda **pwd** (print working directory) este utilizată pentru a afișa directorul de lucru curent în CLI. Directorul de lucru este directorul în care vă aflați în prezent în sistemul de fișiere. Comanda este utilă pentru a naviga prin sistemul de fișiere și pentru a înțelege locația dumneavoastră în raport cu alte directoare. De exemplu, dacă vă aflați în directorul home și doriți să navigați în directorul documents, puteți utiliza următoarele comenzi:

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

În exemplul de mai sus, prima comandă tipărește directorul de lucru curent, care este directorul principal. A doua comandă schimbă directorul în directorul documente, iar a treia comandă tipărește directorul de lucru curent, care este acum directorul documente.

### Lista

Comanda **ls** este utilizată pentru a lista conținutul unui director în CLI. Comanda afișează numele fișierelor și directoarelor din directorul de lucru curent. Comanda este utilă pentru identificarea fișierelor și directoarelor dintr-o anumită locație. De exemplu, dacă doriți să vedeți conținutul directorului documents, puteți utiliza următoarea comandă:

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

În exemplul de mai sus, comanda listează conținutul directorului documents, care conține trei fișiere: file1.txt, file2.pdf și file3.docx. De asemenea, puteți utiliza comanda fără niciun argument pentru a lista conținutul directorului de lucru curent. De exemplu:

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

În exemplul de mai sus, comanda listează conținutul directorului home, care conține mai multe subdirectoare, cum ar fi Desktop, Documents, Downloads și așa mai departe.

### Change Directory

Comanda **cd** (change directory) este utilizată pentru a schimba directorul de lucru curent în CLI. Comanda vă permite să navigați prin sistemul de fișiere și să accesați fișiere din diferite locații. De exemplu, dacă doriți să schimbați directorul de lucru curent în directorul documents, puteți utiliza următoarea comandă:

```bash
$ cd documents
```

În exemplul de mai sus, comanda schimbă directorul de lucru curent în directorul documents, care se află în directorul de lucru curent. De asemenea, puteți utiliza comanda cu o cale absolută sau relativă pentru a schimba directorul de lucru într-un director care nu se află în directorul de lucru curent. De exemplu:

```bash
$ cd /usr/local/bin
```

În exemplul de mai sus, comanda schimbă directorul de lucru curent în directorul /usr/local/bin, care este o cale absolută. Alternativ, puteți utiliza o cale relativă pentru a schimba directorul de lucru. De exemplu:

```bash
$ cd ../..
```


În exemplul de mai sus, comanda schimbă directorul de lucru curent cu două niveluri mai sus față de directorul de lucru curent. Notația "..." reprezintă directorul părinte și o puteți utiliza pentru a naviga în sus în arborele de directoare.


### Concatenate

Comanda **cat** (concatenate) este utilizată pentru a afișa conținutul unui fișier în CLI. Comanda este utilă pentru a vizualiza conținutul fișierelor bazate pe text, cum ar fi fișierele jurnal sau fișierele de configurare. De exemplu, dacă doriți să vizualizați conținutul unui fișier numit "file1.txt", puteți utiliza următoarea comandă:

```bash
$ cat file1.txt
```

În exemplul de mai sus, comanda afișează conținutul fișierului "file1.txt". De asemenea, puteți utiliza comanda pentru a concatena mai multe fișiere și a afișa conținutul acestora în CLI. De exemplu:

```bash
$ cat file1.txt file2.txt file3.txt
```


În exemplul de mai sus, comanda afișează conținutul a trei fișiere: file1.txt, file2.txt și file3.txt. De asemenea, puteți utiliza comanda cu wildcards pentru a concatena toate fișierele care corespund unui anumit model. De exemplu:

```bash
$ cat *.txt
```

În exemplul de mai sus, comanda afișează conținutul tuturor fișierelor care au extensia ".txt" din directorul de lucru curent. Această comandă este utilă pentru a vizualiza rapid conținutul mai multor fișiere fără a le deschide individual.


### Global Regular Expression Print

Comanda **grep** (global regular expression print) este utilizată pentru a căuta șiruri de caractere sau modele specifice într-un fișier sau într-un set de fișiere în CLI. Comanda este utilă pentru identificarea tiparelor în fișierele jurnal sau pentru căutarea unor informații specifice în fișierele de configurare. De exemplu, dacă doriți să căutați toate aparițiile cuvântului "error" într-un fișier numit "logfile.txt", puteți utiliza următoarea comandă:

```bash
$ grep "error" logfile.txt
```

În exemplul de mai sus, comanda caută toate aparițiile cuvântului "error" în fișierul "logfile.txt" și afișează liniile corespunzătoare în CLI. De asemenea, puteți utiliza comanda cu expresii regulate pentru a căuta modele mai complexe. De exemplu, dacă doriți să căutați toate liniile care conțin un cuvânt care începe cu "p" și se termină cu "y", puteți utiliza următoarea comandă:

```bash
$ grep "p.*y" logfile.txt
```

În exemplul de mai sus, comanda caută toate liniile care conțin un cuvânt care începe cu "p" și se termină cu "y" în fișierul "logfile.txt". Expresia regulată "p.*y" se potrivește cu orice șir care începe cu "p" și se termină cu "y", cu orice număr de caractere între ele. Această comandă este utilă pentru a găsi modele în fișierele jurnal care pot ajuta la identificarea amenințărilor de securitate sau a problemelor de performanță.


### Change Mode

Comanda **chmod** (change mode) este utilizată pentru a modifica permisiunile unui fișier sau director în CLI. Comanda este esențială pentru securizarea fișierelor și directoarelor și pentru a controla cine are acces la ele. Permisiunile sunt reprezentate de trei cifre care corespund proprietarului, grupului și, respectiv, altora. Cifrele sunt calculate pe baza următoarei formule:

```
4 = read
2 = write
1 = execute
```

De exemplu, dacă doriți să acordați proprietarului permisiuni de citire și scriere, iar grupului și altora permisiuni de numai citire pentru un fișier numit "file1.txt", puteți utiliza următoarea comandă:

```bash
$ chmod 644 file1.txt
```

În exemplul de mai sus, comanda setează permisiunile fișierului "file1.txt" la 644. Prima cifră (6) reprezintă permisiunile pentru proprietar, care sunt de citire și scriere (4 + 2 = 6). A doua cifră (4) reprezintă permisiunile pentru grup, care sunt de numai citire. A treia cifră (4) reprezintă permisiunile pentru alții, care sunt, de asemenea, numai pentru citire.

Puteți utiliza, de asemenea, comanda cu litere pentru a modifica permisiunile. De exemplu, dacă doriți să acordați proprietarului și grupului permisiuni de citire și de scriere, iar celorlalți permisiuni de nerespectare, pentru un fișier numit "file2.txt", puteți utiliza următoarea comandă:

```bash
$ chmod ug=rw,o= file2.txt
```

În exemplul de mai sus, comanda setează permisiunile fișierului "file2.txt" la ug=rw,o=, unde "ug" reprezintă proprietarul și grupul, "r" reprezintă permisiunea de citire, iar "w" reprezintă permisiunea de scriere. Semnul "=" înseamnă "setează permisiunile la", iar "o=" înseamnă "elimină toate permisiunile pentru alții". Această comandă este utilă pentru a controla accesul la fișiere și directoare sensibile și pentru a preveni accesul neautorizat.


## Comenzi Linux avansate pentru securitate cibernetică

### Network Mapper

Comanda **nmap** este un instrument puternic de scanare a rețelei din CLI care poate fi utilizat pentru a identifica gazdele și serviciile dintr-o rețea, precum și potențialele vulnerabilități. Comanda poate efectua o serie de tehnici de scanare, inclusiv descoperirea gazdelor, scanarea porturilor și detectarea sistemului de operare.

Una dintre cele mai de bază utilizări ale nmap este scanarea unei singure adrese IP sau a unei singure gazde. De exemplu, pentru a scana o singură adresă IP (192.168.1.1) pentru porturi deschise, puteți utiliza următoarea comandă:

```bash
$ nmap 192.168.1.1
```

Comanda de mai sus va rula o scanare TCP SYN împotriva IP-ului țintă și va returna o listă de porturi deschise. Rezultatul va afișa porturile deschise împreună cu serviciul care rulează pe fiecare port, starea portului (deschis/închis) și, uneori, informații suplimentare, cum ar fi sistemul de operare care rulează pe țintă.

Nmap poate fi utilizat, de asemenea, pentru a scana mai multe gazde sau adrese IP simultan. De exemplu, pentru a scana un interval de adrese IP (192.168.1.1-255) pentru porturi deschise, puteți utiliza următoarea comandă:

```bash
$ nmap 192.168.1.1-255
```

Comanda de mai sus va scana toate adresele IP din intervalul respectiv și va returna porturile și serviciile deschise pentru fiecare țintă.

Pe lângă descoperirea de bază a gazdelor și scanarea porturilor, nmap poate efectua și scanări mai avansate, cum ar fi detectarea serviciilor și a versiunilor, detectarea sistemului de operare și scanarea vulnerabilităților. Aceste scanări pot fi utile pentru a identifica potențialele vulnerabilități de securitate dintr-o rețea și pentru a o securiza împotriva unor potențiale atacuri.

### TCP Packet Dumper

Comanda **tcpdump** este utilizată pentru a captura și analiza traficul de rețea în CLI, ceea ce o face utilă pentru depanarea problemelor de rețea, analizarea comportamentului rețelei și identificarea potențialelor amenințări de securitate. Comanda captează pachetele în timp real și poate filtra pachetele pe baza diferitelor criterii, cum ar fi adresa IP sursă sau destinație, protocolul și portul.

Una dintre cele mai de bază utilizări ale tcpdump este capturarea întregului trafic de rețea pe o anumită interfață. De exemplu, pentru a captura tot traficul de pe interfața eth0, puteți utiliza următoarea comandă:

```bash
$ sudo tcpdump -i eth0
```

Comanda de mai sus va captura toate pachetele de pe interfața eth0 și le va afișa în timp real în CLI. Ieșirea va afișa adresele IP sursă și destinație, protocolul și alte informații despre fiecare pachet.

De asemenea, Tcpdump poate fi utilizat pentru a filtra pachetele în funcție de diverse criterii. De exemplu, pentru a captura toate pachetele trimise către sau de la o anumită adresă IP, puteți utiliza următoarea comandă:

```bash
$ sudo tcpdump host 192.168.1.1
```

Comanda de mai sus va captura toate pachetele trimise către sau de la adresa IP 192.168.1.1 și le va afișa în timp real în CLI. De asemenea, puteți filtra pachetele pe baza protocolului (de exemplu, TCP, UDP), a numărului de port sau a altor criterii.

Pe lângă capturarea pachetelor în timp real, tcpdump poate fi utilizat și pentru a captura pachetele într-un fișier pentru o analiză ulterioară. De exemplu, pentru a captura toate pachetele de pe interfața eth0 și a le salva într-un fișier numit "capture.pcap", puteți utiliza următoarea comandă:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

Comanda de mai sus va captura toate pachetele de pe interfața eth0 și le va salva în fișierul "capture.pcap" în format pcap, care poate fi analizat ulterior cu instrumente precum Wireshark. Această comandă este utilă pentru a analiza comportamentul rețelei și pentru a identifica potențiale amenințări de securitate.

### Process Status

Comanda **ps** afișează în CLI informații despre procesele care rulează pe un sistem Linux, ceea ce este util pentru a identifica procesele suspecte care ar putea rula pe un sistem și care ar putea compromite securitatea acestuia. Comanda poate afișa o gamă largă de informații despre procesele care rulează, inclusiv ID-ul procesului (PID), utilizatorul, utilizarea CPU și a memoriei și numele comenzii.

Una dintre cele mai de bază utilizări ale ps este afișarea unei liste a tuturor proceselor în curs de execuție de pe un sistem. De exemplu, pentru a afișa o listă a tuturor proceselor care rulează pe sistem, puteți utiliza următoarea comandă:

```bash
$ ps aux
```

Comanda de mai sus va afișa o listă a tuturor proceselor care rulează pe sistem, împreună cu PID-ul, utilizatorul, utilizarea CPU și a memoriei și numele comenzii. Această comandă este utilă pentru a obține o imagine de ansamblu a proceselor care rulează pe un sistem și pentru a identifica orice proces suspect care ar putea fi în curs de execuție.

Ps poate fi utilizată, de asemenea, pentru a afișa informații despre un anumit proces sau set de procese. De exemplu, pentru a afișa informații despre un proces cu un anumit PID (de exemplu, PID 1234), puteți utiliza următoarea comandă:

```bash
$ ps -p 1234
```

Comanda de mai sus va afișa informații despre procesul cu PID 1234, inclusiv utilizatorul, utilizarea CPU și a memoriei, precum și numele comenzii. De asemenea, puteți afișa informații despre un set de procese specificând mai multe PID-uri.

Pe lângă afișarea de informații despre procesele în curs de execuție, ps poate fi utilizat și pentru a monitoriza starea proceselor în timp real. De exemplu, pentru a monitoriza utilizarea CPU și a memoriei unui anumit proces (de exemplu, PID 1234) în timp real, puteți utiliza următoarea comandă:

```bash
$ ps -p 1234 -o %cpu,%mem
```

Comanda de mai sus va afișa utilizarea CPU și a memoriei procesului cu PID 1234 în timp real, actualizând rezultatul la fiecare secundă. Această comandă este utilă pentru monitorizarea performanței proceselor critice și pentru identificarea potențialelor blocaje de performanță.

### Statistici de rețea

Comanda **netstat** afișează în CLI informații despre conexiunile de rețea active pe un sistem Linux, fiind utilă pentru identificarea conexiunilor de rețea neautorizate și a potențialelor amenințări la adresa securității. Comanda poate afișa o gamă largă de informații despre conexiunile de rețea active, inclusiv adresele locale și la distanță, protocolul utilizat (de exemplu, TCP, UDP) și starea conexiunii.

Una dintre cele mai de bază utilizări ale netstat este afișarea unei liste cu toate conexiunile de rețea active pe un sistem. De exemplu, pentru a afișa o listă a tuturor conexiunilor de rețea active, puteți utiliza următoarea comandă:

```bash
$ netstat -a
```


Comanda de mai sus va afișa o listă a tuturor conexiunilor de rețea active de pe sistem, împreună cu adresele locale și la distanță, protocolul utilizat și starea conexiunii. Această comandă este utilă pentru a obține o imagine de ansamblu a conexiunilor de rețea active pe un sistem și pentru a identifica orice conexiune neautorizată.

Netstat poate fi utilizat, de asemenea, pentru a afișa informații despre conexiunile de rețea pentru un anumit protocol (de exemplu, TCP). De exemplu, pentru a afișa o listă a tuturor conexiunilor TCP active de pe sistem, puteți utiliza următoarea comandă:

```bash
$ netstat -at
```

Comanda de mai sus va afișa o listă a tuturor conexiunilor TCP active de pe sistem, împreună cu adresele locale și la distanță și starea conexiunii.

Pe lângă afișarea informațiilor despre conexiunile de rețea active, netstat poate fi utilizat și pentru a afișa statisticile de rețea pentru un anumit protocol (de exemplu, TCP). De exemplu, pentru a afișa statistici despre toate conexiunile TCP de pe sistem, puteți utiliza următoarea comandă:

```bash
$ netstat -st
```

Comanda de mai sus va afișa statistici despre toate conexiunile TCP de pe sistem, inclusiv numărul de conexiuni active, numărul de conexiuni în fiecare stare și numărul de erori care au apărut. Această comandă este utilă pentru a monitoriza starea generală de sănătate a rețelei și pentru a identifica eventualele probleme de performanță.


### Find Files

Comanda **find** este utilizată pentru a căuta fișiere și directoare pe un sistem Linux în CLI, ceea ce o face utilă pentru localizarea unor fișiere și directoare specifice care pot fi ascunse sau greu de găsit. Comanda caută fișiere și directoare pe baza unei game largi de criterii, inclusiv numele, dimensiunea, ora de modificare și permisiunile acestora.

Una dintre cele mai simple utilizări ale comenzii find este căutarea fișierelor și directoarelor după nume. De exemplu, pentru a căuta toate fișierele din directorul curent și din subdirectoarele sale care au numele "exemplu.txt", puteți utiliza următoarea comandă:

```bash
$ find . -name example.txt
```

Comanda de mai sus va căuta toate fișierele din directorul curent și din subdirectoarele sale care au numele "example.txt" și va afișa calea completă a acestora.

Find poate fi utilizat, de asemenea, pentru a căuta fișiere și directoare în funcție de dimensiunea acestora. De exemplu, pentru a căuta toate fișierele din directorul curent și din subdirectoarele sale care au o dimensiune mai mare de 1 MB, puteți utiliza următoarea comandă:

```bash
$ find . -size +1M
```

Comanda de mai sus va căuta toate fișierele din directorul curent și din subdirectoarele sale care au o dimensiune mai mare de 1 MB și va afișa calea completă a acestora.

Pe lângă căutarea fișierelor și directoarelor după nume și dimensiune, find poate fi utilizat și pentru a căuta fișiere și directoare în funcție de timpul de modificare și de permisiuni. De exemplu, pentru a căuta toate fișierele din directorul curent și din subdirectoarele sale care au fost modificate în ultimele 7 zile, puteți utiliza următoarea comandă:

```bash
$ find . -mtime -7
```

Comanda de mai sus va căuta toate fișierele din directorul curent și din subdirectoarele sale care au fost modificate în ultimele 7 zile și va afișa calea completă a acestora.

În general, comanda find este un instrument puternic de căutare a fișierelor și directoarelor pe un sistem Linux pe baza unei game largi de criterii, ceea ce o face utilă pentru o varietate de sarcini, inclusiv pentru administrarea sistemului și securitatea cibernetică.

______

Utilizarea liniei de comandă Linux pentru securitatea cibernetică poate fi copleșitoare pentru începători. Cu toate acestea, cu ajutorul comenzilor de bază și avansate prezentate în acest ghid, puteți începe să folosiți CLI Linux în avantajul dumneavoastră în domeniul securității cibernetice. Nu uitați să fiți prudenți atunci când executați comenzi și să înțelegeți bine ce face fiecare comandă înainte de a o utiliza.

Pentru a afla mai multe despre utilizarea Linux pentru securitatea cibernetică, consultați descărcarea **[Kali Linux](https://www.kali.org/downloads/) sistem de operare conceput special pentru testele de penetrare și criminalistică digitală.

## Concluzie

În concluzie, interfața liniei de comandă Linux este un instrument puternic pentru profesioniștii din domeniul securității cibernetice, dar poate fi descurajantă pentru începători. Învățând comenzile de bază și avansate prezentate în acest ghid, puteți începe să folosiți CLI Linux în avantajul dumneavoastră în domeniul securității cibernetice. Nu uitați să fiți întotdeauna precauți atunci când executați comenzi și să înțelegeți bine ce face fiecare comandă înainte de a o utiliza. Cu ajutorul practicii și al experienței, puteți deveni competent în utilizarea liniei de comandă Linux și vă puteți duce abilitățile de securitate cibernetică la nivelul următor.
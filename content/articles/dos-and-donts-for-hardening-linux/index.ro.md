---
title: "Ce să faci și ce să nu faci pentru securizarea sistemului Linux"
date: 2023-02-28
lastmod: 2026-11-25
toc: true
draft: false
description: "Recomandări de securizare Linux despre actualizări, firewall, SELinux sau AppArmor, politica parolelor și monitorizarea jurnalelor."
tags: ["securitate Linux", "securizarea sistemului", "firewall", "SELinux", "AppArmor", "politica parolelor", "actualizări de sistem", "jurnale de sistem", "module de securitate", "politici de control al accesului", "securitate cibernetică", "securitatea sistemului", "securitatea rețelei", "gestionarea vulnerabilităților", "bune practici de securitate", "securitate IT", "securitatea informațiilor", "actualizări software", "acces root", "manager de parole"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.webp"
coverAlt: "Un lacăt desenat animat ține un scut cu textul Linux, iar o săgeată ricoșează din scut."
coverCaption: ""
---


Linux este un sistem de operare popular, folosit atât de persoane, cât și de companii. Deși este adesea considerat mai sigur decât alte sisteme de operare datorită naturii sale open-source, este nevoie de măsuri de securizare pentru a proteja sistemul și datele stocate pe el. În acest articol prezentăm câteva lucruri de făcut și de evitat pentru a vă ajuta să vă păstrați sistemul Linux în siguranță.

## Ce să faci:

### Menține sistemul actualizat

Menținerea [sistemului Linux](https://simeononsecurity.com/articles/how-do-i-learn-linux/) la zi este esențială pentru securitate. Actualizările regulate corectează vulnerabilitățile și erorile, ajutând sistemul să reziste atacurilor. Iată câteva exemple de actualizare a sistemului Linux cu managerul de pachete **apt-get** sau **yum**:

#### Actualizarea Ubuntu cu apt-get

Pentru a actualiza Ubuntu cu **apt-get**, deschideți un terminal și introduceți:
```bash
sudo apt-get update
```

Comanda descarcă cele mai recente liste de pachete din depozitele Ubuntu. După finalizare, instalați actualizările disponibile cu:

```bash
sudo apt-get upgrade

```

Comanda descarcă și instalează actualizările disponibile pentru sistem.

### Actualizarea CentOS cu yum

Pentru a actualiza CentOS cu **yum**, deschideți un terminal și introduceți:

```bash
sudo yum update
```

Comanda descarcă și instalează actualizările disponibile. Puteți folosi și următoarea comandă pentru a elimina pachetele vechi sau nefolosite:

```bash
sudo yum autoremove
```

Aceasta elimină pachetele de care sistemul nu mai are nevoie.

Verificați și instalați periodic actualizările pentru a păstra securitatea și stabilitatea sistemului Linux.


### Folosește un firewall

Un firewall este o măsură de securitate esențială pentru orice sistem Linux, deoarece ajută la protejarea împotriva accesului neautorizat și a altor amenințări cibernetice. Iată cum se folosește firewallul **ufw**:

#### Instalarea și activarea ufw pe sistemele bazate pe Ubuntu

Pentru a instala și activa **ufw**, deschideți un terminal și introduceți:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Pentru a permite traficul HTTP de intrare (portul 80):

```bash
sudo ufw allow http
```

Pentru a bloca traficul de intrare de la o anumită adresă IP:

```bash
sudo ufw deny from <ip_address>
```

Pentru a șterge o regulă:
```bash
sudo ufw delete <rule_number>
```

Puteți afișa regulile **ufw** curente cu:

```bash
sudo ufw status
```


Comanda afișează regulile curente și starea lor.

Verificați și actualizați periodic regulile **ufw** pentru a vă proteja sistemul de amenințări.


#### Instalarea și activarea firewalld pe sistemele bazate pe CentOS

Pentru a instala și activa firewallul implicit din CentOS, **firewalld**, folosiți comenzile:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Aceste comenzi instalează **firewalld** și îl activează pe sistem.

#### Configurarea regulilor firewalld pe sistemele bazate pe CentOS

După activarea **firewalld**, puteți configura regulile pentru a permite sau bloca traficul de intrare și de ieșire. Iată câteva exemple:

Pentru a permite traficul SSH de intrare (portul 22):

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Pentru a permite traficul HTTP de intrare (portul 80):

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Pentru a bloca traficul de intrare de la o anumită adresă IP:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Pentru a șterge o regulă:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Puteți afișa regulile **firewalld** curente cu:

```bash
sudo firewall-cmd --list-all
```

Comanda afișează regulile curente și starea lor.

Verificați și actualizați periodic regulile **firewalld** pentru a vă asigura că sistemul este protejat împotriva amenințărilor potențiale.

### Activează SELinux sau AppArmor

SELinux (Security-Enhanced Linux) și AppArmor sunt două module de securitate care impun politici obligatorii de control al accesului pe sistemele Linux. Majoritatea distribuțiilor Linux moderne includ SELinux sau AppArmor. Le puteți activa și configura pentru a îmbunătăți securitatea sistemului.

#### Activarea SELinux pe sistemele bazate pe CentOS

Pentru a verifica dacă SELinux este activat, rulați:

```bash
sestatus
```

Dacă SELinux nu este instalat, instalați-l cu:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Pentru a activa SELinux, editați fișierul **/etc/selinux/config** și setați variabila **SELINUX** la **enforcing**:

```bash
sudo nano /etc/selinux/config
```
**Schimbați SELINUX=enforcing**
```
SELINUX=enforcing
```

Salvați fișierul și ieșiți cu CTRL+X, apoi Y și Enter. Reporniți sistemul.

#### Activarea AppArmor pe sistemele bazate pe Ubuntu

Pentru a verifica dacă AppArmor este activat, rulați:
```bash
sudo apparmor_status
```


Dacă AppArmor nu este instalat, instalați-l cu:
```bash
sudo apt-get install apparmor
```

Pentru a activa AppArmor, editați fișierul **/etc/default/grub** și adăugați parametrul **security=apparmor** la variabila **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Adăugați security=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Salvați fișierul și ieșiți cu CTRL+X, apoi Y și Enter. Actualizați configurația încărcătorului de pornire cu:

```bash
sudo update-grub
```

La final, reporniți sistemul.

După activarea SELinux sau AppArmor, configurați politici care limitează privilegiile proceselor și accesul lor la resursele sistemului. Astfel, impactul unui atac reușit poate fi redus, iar securitatea generală îmbunătățită.


### Configurează politicile pentru parole

Configurarea politicilor pentru parole este un pas important pentru securizarea sistemului Linux. Cerințele stricte pentru parole ajută la protejarea conturilor împotriva atacurilor. Iată cum puteți configura politicile pentru parole:

#### Configurarea politicilor pentru parole în Ubuntu

În Ubuntu puteți folosi modulul **pam_pwquality**, care oferă verificări ale robusteții parolelor. Pentru a-l instala, deschideți un terminal și introduceți:

```bash
sudo apt-get install libpam-pwquality
```

După instalarea modulului **pam_pwquality**, editați fișierul **/etc/pam.d/common-password** pentru a configura setările. De exemplu, pentru a impune o lungime minimă de 8 caractere și cel puțin o literă mare, una mică, o cifră și un caracter special, adăugați linia:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

Puteți adăuga și alte setări în fișier, de exemplu vârsta maximă a parolei.

#### Configurarea politicilor pentru parole în CentOS

În CentOS puteți folosi instrumentul **authconfig** pentru a configura politicile pentru parole. De exemplu, pentru a impune o lungime minimă de 8 caractere și cel puțin o literă mare, una mică, o cifră și un caracter special, rulați:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Comanda actualizează fișierele **/etc/pam.d/system-auth** și **/etc/pam.d/password-auth** pentru a impune politicile specificate.

Verificați și actualizați periodic politicile pentru parole pentru a le menține eficiente împotriva atacurilor.


### Monitorizează jurnalele sistemului

Monitorizarea jurnalelor este importantă pentru securitatea sistemului Linux. Jurnalele înregistrează activitatea sistemului, precum încercările eșuate de autentificare, erorile și alte evenimente importante. Acestea oferă indicii utile despre posibile amenințări de securitate sau probleme care necesită atenție. Iată cum puteți monitoriza jurnalele:

#### Folosirea comenzii journalctl

Pe majoritatea distribuțiilor Linux moderne, puteți folosi comanda **journalctl** pentru a vedea jurnalele sistemului. Comanda oferă diverse opțiuni pentru filtrarea și căutarea înregistrărilor.

Pentru a vedea toate înregistrările, rulați:

```bash
sudo journalctl
```

Comanda afișează toate înregistrările, cele mai recente fiind la final.

Pentru a filtra înregistrările după o anumită unitate, cum ar fi un serviciu sau un proces, folosiți opțiunea **-u**, urmată de numele unității. De exemplu, pentru a vedea înregistrările serviciului **sshd**, rulați:
```bash
sudo journalctl -u sshd
```


Pentru a filtra înregistrările după un interval de timp, folosiți opțiunile **--since** și **--until**, urmate de un marcaj temporal sau un interval. De exemplu, pentru a vedea înregistrările din ultima oră, rulați:

```bash
sudo journalctl --since "1 hour ago"
```

#### Folosirea unui instrument de gestionare a jurnalelor

Pe sistemele mari sau complexe, un instrument de gestionare a jurnalelor poate colecta și analiza înregistrările. Aceste instrumente pot oferi monitorizare în timp real, agregare și analiză, facilitând identificarea și tratarea amenințărilor de securitate.

Exemple de instrumente pentru gestionarea jurnalelor Linux:

- **Logwatch**: instrument simplu de analiză care trimite zilnic rezumate ale jurnalelor de sistem prin e-mail
- **Logrotate**: rotește și comprimă automat fișierele jurnal pentru a economisi spațiu pe disc
- **ELK stack**: instrument popular cu sursă deschisă care combină Elasticsearch, Logstash și Kibana pentru monitorizarea și analiza jurnalelor în timp real

Verificați și analizați periodic jurnalele sistemului pentru a detecta și trata amenințările de securitate la timp.

______

## Ce să nu faci:

### Nu folosi parole slabe

Folosirea parolelor slabe este o greșeală frecventă care poate lăsa sistemul Linux vulnerabil la atacuri. Atacatorii pot încerca parole bazate pe cuvinte, nume sau date obișnuite. Folosiți parole puternice și unice, greu de ghicit.

Puteți crea parole puternice combinând litere mari și mici, cifre și caractere speciale. Este recomandat și un [manager de parole](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) pentru generarea și stocarea în siguranță a parolelor complexe. [Managerii de parole](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) vă pot ajuta să le rețineți și să evitați reutilizarea aceleiași parole pentru mai multe conturi.

### Nu permite accesul SSH pentru root

Permiterea accesului SSH pentru root este un risc de securitate care le poate oferi atacatorilor control complet asupra sistemului Linux. Conectați-vă cu un cont de utilizator care nu este root, apoi folosiți comanda **sudo** pentru a obține privilegiile necesare. Astfel, privilegiile conturilor rămân limitate și impactul potențial al unui atac scade.

### Nu instala software inutil

Instalarea software-ului inutil mărește suprafața de atac a sistemului Linux și îl face mai vulnerabil. Instalați numai software-ul necesar și eliminați programele inutile. Astfel reduceți numărul vulnerabilităților potențiale și riscul unui atac reușit.

### Nu folosi software învechit

Software-ul învechit poate lăsa sistemul vulnerabil la atacuri care exploatează vulnerabilități cunoscute. Folosiți cele mai recente versiuni și actualizați software-ul periodic. Astfel remediați vulnerabilitățile cunoscute și protejați sistemul de atacuri.

______

## Concluzie

Securizarea sistemului Linux este esențială pentru a proteja sistemul și datele stocate pe el. Urmați recomandările din acest articol pentru a vă securiza sistemul și a reduce riscul amenințărilor cibernetice. Mențineți sistemul actualizat, folosiți un firewall, configurați politicile pentru parole și monitorizați jurnalele. Evitați parolele slabe, dezactivarea actualizărilor automate, accesul SSH pentru root, instalarea software-ului inutil și folosirea programelor învechite. Aplicând aceste bune practici, vă puteți păstra sistemul Linux sigur și protejat.

## Referințe:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

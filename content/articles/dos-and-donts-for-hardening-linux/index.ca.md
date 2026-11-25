---
title: "Què cal fer i què evitar per reforçar el vostre sistema Linux"
date: 2023-02-28
lastmod: 2026-11-25
toc: true
draft: false
description: "Guia per reforçar Linux amb actualitzacions, tallafocs, SELinux o AppArmor, polítiques de contrasenyes i supervisió dels registres."
tags: ["seguretat de Linux", "reforç del sistema", "tallafoc", "SELinux", "AppArmor", "política de contrasenyes", "actualitzacions del sistema", "registres del sistema", "mòduls de seguretat", "polítiques de control d’accés", "ciberseguretat", "seguretat del sistema", "seguretat de xarxa", "gestió de vulnerabilitats", "bones pràctiques de seguretat", "seguretat informàtica", "seguretat de la informació", "actualitzacions de programari", "accés root", "gestor de contrasenyes"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.webp"
coverAlt: "Un cadenat de dibuixos animats sosté un escut amb la paraula Linux, mentre una fletxa rebota contra l’escut."
coverCaption: ""
---


Linux és un sistema operatiu popular que fan servir tant particulars com empreses. Tot i que sovint es considera més segur que altres sistemes operatius pel fet de ser de codi obert, encara cal reforçar-lo adequadament per protegir el sistema i les dades que conté. En aquest article repassem recomanacions i pràctiques que cal evitar per mantenir segur el vostre sistema Linux.

## Què cal fer:

### Manteniu el sistema actualitzat

Mantenir actualitzat el vostre [sistema Linux](https://simeononsecurity.com/articles/how-do-i-learn-linux/) és essencial per conservar-ne la seguretat. Les actualitzacions periòdiques corregeixen vulnerabilitats de seguretat i errors, i ajuden a protegir el sistema dels possibles atacs. A continuació teniu exemples d’actualització de Linux amb els gestors de paquets **apt-get** i **yum**:

#### Actualitzar Ubuntu amb apt-get

Per actualitzar Ubuntu amb **apt-get**, obriu un terminal i escriviu:
```bash
sudo apt-get update
```

Això baixarà les llistes de paquets més recents dels repositoris d’Ubuntu. Quan acabi l’ordre, podreu instal·lar les actualitzacions disponibles amb aquesta altra ordre:

```bash
sudo apt-get upgrade

```

Això baixarà i instal·larà les actualitzacions disponibles per al sistema.

### Actualitzar CentOS amb yum

Per actualitzar CentOS amb **yum**, obriu un terminal i escriviu:

```bash
sudo yum update
```

Això baixarà i instal·larà les actualitzacions disponibles. També podeu executar l’ordre següent per netejar paquets antics o que ja no feu servir:

```bash
sudo yum autoremove
```

Això eliminarà els paquets que ja no calen al sistema.

Comproveu i instal·leu les actualitzacions de Linux periòdicament per mantenir la seguretat i l’estabilitat del sistema.


### Feu servir un tallafoc

Un tallafoc és una mesura de seguretat essencial per a qualsevol sistema Linux perquè ajuda a protegir-lo contra accessos no autoritzats i altres ciberamenaces. Així podeu fer servir el tallafoc **ufw** al vostre sistema Linux:

#### Instal·lar i activar ufw en sistemes basats en Ubuntu

Per instal·lar i activar **ufw**, obriu un terminal i escriviu:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Per permetre el trànsit HTTP entrant (port 80):

```bash
sudo ufw allow http
```

Per bloquejar el trànsit entrant d’una adreça IP concreta:

```bash
sudo ufw deny from <ip_address>
```

Per eliminar una regla:
```bash
sudo ufw delete <rule_number>
```

Per veure les regles actuals de **ufw**, escriviu:

```bash
sudo ufw status
```


Això mostrarà les regles actuals i l’estat de cadascuna.

Reviseu i actualitzeu periòdicament les regles de **ufw** per protegir el sistema de possibles amenaces.


#### Instal·lar i activar firewalld en sistemes basats en CentOS

Per instal·lar i activar el tallafoc predeterminat de CentOS, **firewalld**, feu servir aquestes ordres:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Això instal·larà **firewalld** i l’activarà al sistema.

#### Configurar les regles de firewalld en sistemes basats en CentOS

Quan **firewalld** estigui activat, podreu configurar les regles per permetre o bloquejar el trànsit entrant i sortint. Aquests en són alguns exemples:

Per permetre el trànsit SSH entrant (port 22):

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Per permetre el trànsit HTTP entrant (port 80):

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Per bloquejar el trànsit entrant d’una adreça IP concreta:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Per eliminar una regla:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Per veure les regles actuals de **firewalld**, escriviu:

```bash
sudo firewall-cmd --list-all
```

Això mostrarà les regles actuals i l’estat de cadascuna.

Reviseu i actualitzeu periòdicament les regles de **firewalld** per assegurar-vos que el sistema

### Activeu SELinux o AppArmor

SELinux (Security-Enhanced Linux) i AppArmor són dos mòduls de seguretat que permeten aplicar polítiques de control d’accés obligatori als sistemes Linux. La majoria de distribucions modernes inclouen SELinux o AppArmor, i es poden activar i configurar per reforçar la seguretat del sistema.

#### Activar SELinux en sistemes basats en CentOS

Per comprovar si SELinux està activat al sistema, executeu aquesta ordre:

```bash
sestatus
```

Si SELinux no està instal·lat, podeu instal·lar-lo amb aquesta ordre:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Per activar SELinux, editeu el fitxer **/etc/selinux/config** i establiu el valor **enforcing** a la variable **SELINUX**:

```bash
sudo nano /etc/selinux/config
```
**Canvieu SELINUX=enforcing**
```
SELINUX=enforcing
```

Deseu el fitxer i sortiu-ne amb CTRL+X, després Y i Enter; a continuació, reinicieu el sistema.

#### Activar AppArmor en sistemes basats en Ubuntu

Per comprovar si AppArmor està activat, executeu aquesta ordre:
```bash
sudo apparmor_status
```


Si AppArmor no està instal·lat, el podeu instal·lar amb aquesta ordre:
```bash
sudo apt-get install apparmor
```

Per activar AppArmor, editeu el fitxer **/etc/default/grub** i afegiu el paràmetre **security=apparmor** a la variable **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Afegiu security=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Deseu el fitxer i sortiu-ne amb CTRL+X, després Y i Enter. Tot seguit, executeu aquesta ordre per actualitzar la configuració del carregador d’arrencada:

```bash
sudo update-grub
```

Finalment, reinicieu el sistema.

Un cop activat SELinux o AppArmor, podeu configurar-ne les polítiques per restringir els privilegis dels processos i limitar-ne l’accés als recursos del sistema. Això ajuda a reduir l’impacte potencial d’un atac reeixit i a reforçar la seguretat general.


### Configureu les polítiques de contrasenyes

Configurar polítiques de contrasenyes és un pas important per reforçar la seguretat de Linux. Si exigiu contrasenyes robustes, podeu protegir els comptes d’usuari dels possibles atacs. Així podeu configurar les polítiques de contrasenyes a Linux:

#### Configurar les polítiques de contrasenyes a Ubuntu

A Ubuntu podeu fer servir el mòdul **pam_pwquality** per configurar les polítiques de contrasenyes. Aquest mòdul ofereix comprovacions de robustesa per aplicar-les. Per instal·lar **pam_pwquality**, obriu un terminal i escriviu:

```bash
sudo apt-get install libpam-pwquality
```

Un cop instal·lat el mòdul, editeu el fitxer **/etc/pam.d/common-password** per configurar-lo. Per exemple, per exigir una contrasenya de 8 caràcters com a mínim amb una majúscula, una minúscula, un dígit i un caràcter especial, afegiu-hi aquesta línia:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

També podeu configurar altres paràmetres, com ara l’antiguitat màxima de la contrasenya, afegint línies al fitxer.

#### Configurar les polítiques de contrasenyes a CentOS

A CentOS podeu fer servir l’eina **authconfig** per configurar les polítiques de contrasenyes. L’eina ofereix diverses opcions. Per exigir una contrasenya de 8 caràcters com a mínim amb una majúscula, una minúscula, un dígit i un caràcter especial, feu servir aquesta ordre:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Això actualitzarà els fitxers **/etc/pam.d/system-auth** i **/etc/pam.d/password-auth** per aplicar les polítiques indicades.

Reviseu i actualitzeu les polítiques de contrasenyes periòdicament perquè continuïn protegint-vos dels possibles atacs.


### Superviseu els registres del sistema

La supervisió dels registres és important per mantenir segur el sistema Linux. Els registres anoten l’activitat del sistema, com ara intents d’inici de sessió fallits, errors i altres esdeveniments rellevants. Poden donar informació valuosa sobre possibles amenaces o problemes que requereixen atenció. Així podeu supervisar-los:

#### Feu servir l’ordre journalctl

A la majoria de distribucions modernes podeu fer servir **journalctl** per veure els registres del sistema. Aquesta ordre ofereix diverses opcions per filtrar i cercar entrades.

Per veure totes les entrades, executeu simplement aquesta ordre:

```bash
sudo journalctl
```

Això mostrarà totes les entrades, amb les més recents al final.

Per filtrar les entrades per una unitat concreta, com ara un servei o procés, feu servir l’opció **-u** seguida del nom de la unitat. Per exemple, per veure els registres del servei **sshd**, executeu aquesta ordre:
```bash
sudo journalctl -u sshd
```


Per filtrar per un període concret, feu servir les opcions **--since** i **--until** seguides d’una marca temporal o d’un interval. Per exemple, per veure l’última hora, executeu aquesta ordre:

```bash
sudo journalctl --since "1 hour ago"
```

#### Feu servir una eina de gestió de registres

En sistemes grans o complexos pot ser útil recopilar i analitzar els registres amb una eina de gestió. Aquestes eines ofereixen funcions avançades, com ara supervisió en temps real, agregació i anàlisi, i ajuden a detectar i respondre a les amenaces amb més eficàcia.

Algunes eines de gestió de registres per a Linux són:

- **Logwatch**: una eina senzilla que envia cada dia per correu electrònic resums dels registres del sistema
- **Logrotate**: una eina que rota i comprimeix automàticament els fitxers de registre per estalviar espai
- **ELK stack**: una eina popular de codi obert que combina Elasticsearch, Logstash i Kibana per supervisar i analitzar registres en temps real

Reviseu i analitzeu els registres periòdicament per detectar possibles amenaces i respondre-hi a temps.

______

## Què cal evitar:

### No feu servir contrasenyes febles

Fer servir contrasenyes febles és un error habitual que pot exposar Linux a atacs. Els atacants poden endevinar-les amb eines que proven paraules, noms o dates comuns. Feu servir contrasenyes robustes, úniques i difícils d’endevinar.

Podeu crear-les combinant majúscules, minúscules, números i caràcters especials. També és recomanable fer servir un [gestor de contrasenyes](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) per generar i desar contrasenyes complexes de manera segura. Els [gestors de contrasenyes](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) també us ajuden a recordar-les i a no reutilitzar-les en diversos comptes.

### No permeteu l’accés SSH al compte root

Permetre que el compte root accedeixi per SSH és un risc de seguretat que pot donar als atacants el control complet del sistema Linux. En lloc d’això, inicieu sessió amb un compte que no sigui root i després eleveu els privilegis amb **sudo**. Així limiteu l’impacte potencial d’un atac restringint els privilegis dels comptes d’usuari.

### No instal·leu programari innecessari

El programari innecessari amplia la superfície d’atac del sistema Linux. Instal·leu només el que calgui i elimineu la resta. Això redueix les vulnerabilitats potencials i el risc que un atac tingui èxit.

### No feu servir programari obsolet

El programari obsolet pot deixar el sistema exposat a atacs que aprofiten vulnerabilitats conegudes. Feu servir les versions més recents i actualitzeu-les periòdicament per corregir-les i protegir el sistema.

______

## Conclusió

Reforçar el sistema Linux és essencial per protegir-lo i salvaguardar les dades que conté. Seguiu les recomanacions d’aquest article per protegir el sistema i reduir el risc de ciberamenaces. Manteniu-lo actualitzat, feu servir un tallafoc, configureu les polítiques de contrasenyes i superviseu els registres. Eviteu les contrasenyes febles, desactivar les actualitzacions automàtiques, permetre l’accés SSH a root, instal·lar programari innecessari i fer servir programari obsolet. Aquestes bones pràctiques us ajudaran a mantenir Linux segur.

## Referències:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

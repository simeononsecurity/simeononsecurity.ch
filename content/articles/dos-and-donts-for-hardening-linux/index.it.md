---
title: "I comportamenti essenziali da tenere per l'hardening del sistema Linux"
date: 2023-02-28
toc: true
draft: false
description: "Imparate a conoscere i comportamenti essenziali per rendere più sicuro il vostro sistema Linux, tra cui l'aggiornamento, l'uso dei firewall, l'abilitazione di SELinux o AppArmor, la configurazione dei criteri per le password e il monitoraggio dei registri di sistema."
tags: ["Sicurezza di Linux", "indurimento del sistema", "firewall", "SELinux", "AppArmor", "politica delle password", "aggiornamenti del sistema", "registri di sistema", "moduli di sicurezza", "politiche di controllo degli accessi", "sicurezza informatica", "sicurezza del sistema", "sicurezza della rete", "gestione delle vulnerabilità", "migliori pratiche di sicurezza", "Sicurezza informatica", "sicurezza delle informazioni", "aggiornamenti software", "accesso root", "gestore di password"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Un lucchetto a fumetti che regge uno scudo con la parola Linux, mentre una freccia rimbalza sullo scudo."
coverCaption: ""
---


Linux è un sistema operativo molto diffuso, utilizzato sia da privati che da aziende. Sebbene sia spesso considerato più sicuro di altri sistemi operativi grazie alla sua natura open-source, richiede comunque un hardening adeguato per garantire la sicurezza del sistema e dei dati in esso contenuti. In questo articolo esamineremo alcuni accorgimenti generali per l'hardening che possono aiutare a mantenere sicuro il vostro sistema Linux.

## Fare:

### Mantenere il sistema aggiornato

Mantenere il sistema[Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) L'aggiornamento del sistema è fondamentale per mantenerne la sicurezza. Gli aggiornamenti regolari aiutano a risolvere le vulnerabilità e i bug di sicurezza, assicurando che il sistema rimanga sicuro contro potenziali attacchi. Ecco alcuni esempi di come aggiornare il sistema Linux utilizzando il gestore di pacchetti **apt-get** o **yum**:

#### Aggiornamento di Ubuntu con apt-get

Per aggiornare il sistema Ubuntu utilizzando **apt-get**, aprite una finestra di terminale e digitate:
```bash
sudo apt-get update
```

Questo scaricherà gli ultimi elenchi di pacchetti dai repository dei pacchetti di Ubuntu. Una volta completato il comando, è possibile installare tutti gli aggiornamenti disponibili utilizzando il comando seguente:

```bash
sudo apt-get upgrade

```

In questo modo si scaricano e si installano tutti gli aggiornamenti disponibili per il sistema.

### Aggiornamento di CentOS con yum

Per aggiornare il sistema CentOS utilizzando **yum**, aprire una finestra di terminale e digitare:

```bash
sudo yum update
```

Questo scaricherà e installerà tutti gli aggiornamenti disponibili per il sistema. Si può anche usare il seguente comando per ripulire i pacchetti vecchi o inutilizzati:

```bash
sudo yum autoremove
```

In questo modo si rimuovono i pacchetti non più necessari sul sistema.

Ricordate di controllare e installare regolarmente gli aggiornamenti sul vostro sistema Linux per garantirne la sicurezza e la stabilità.


### Utilizzare un firewall

Un firewall è una misura di sicurezza essenziale per qualsiasi sistema Linux, in quanto aiuta a proteggere da accessi non autorizzati e altre minacce informatiche. Ecco come utilizzare il firewall **ufw** sul vostro sistema Linux:

#### Installare e abilitare ufw per i sistemi basati su Ubuntu

Per installare e abilitare **ufw**, aprire una finestra di terminale e digitare:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Per consentire il traffico HTTP in entrata (porta 80):

```bash
sudo ufw allow http
```

Per bloccare il traffico in entrata da un indirizzo IP specifico:

```bash
sudo ufw deny from <ip_address>
```

Per eliminare una regola:
```bash
sudo ufw delete <rule_number>
```

È possibile visualizzare le regole **ufw** correnti digitando:

```bash
sudo ufw status
```


In questo modo vengono visualizzate le regole correnti e il loro stato.

Ricordate di rivedere e aggiornare regolarmente le regole **ufw** per garantire che il vostro sistema sia protetto da potenziali minacce.


#### Installazione e abilitazione di firewalld per sistemi basati su CentOS

Per installare e abilitare il firewall predefinito su CentOS, **firewalld**, è possibile utilizzare i seguenti comandi:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Questo installerà **firewalld** e lo abiliterà sul sistema.

#### Configurazione delle regole di firewalld per i sistemi basati su CentOS

Una volta abilitato **firewalld**, è possibile configurare le sue regole per consentire o bloccare il traffico in entrata e in uscita. Ecco alcuni esempi:

Per consentire il traffico SSH in entrata (porta 22):

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Per consentire il traffico HTTP in entrata (porta 80):

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Per bloccare il traffico in entrata da un indirizzo IP specifico:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Per eliminare una regola:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

È possibile visualizzare le regole correnti di **firewalld** digitando:

```bash
sudo firewall-cmd --list-all
```

In questo modo vengono visualizzate le regole correnti e il loro stato.

Ricordate di rivedere e aggiornare regolarmente le regole di **firewalld** per garantire che il vostro sistema

### Abilitare SELinux o AppArmor

SELinux (Security-Enhanced Linux) e AppArmor sono due moduli di sicurezza che possono essere utilizzati per applicare politiche di controllo degli accessi obbligatorie nei sistemi Linux. Per impostazione predefinita, la maggior parte delle moderne distribuzioni Linux ha installato SELinux o AppArmor, che possono essere abilitati e configurati per migliorare la sicurezza del sistema.

#### Abilitazione di SELinux per i sistemi basati su CentOS

Per verificare se SELinux è abilitato sul sistema, eseguire il seguente comando:

```bash
sestatus
```

Se SELinux non è installato, è possibile installarlo con il seguente comando:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Per abilitare SELinux, è necessario modificare il file **/etc/selinux/config** e impostare la variabile **SELINUX** su **enforcing**:

```bash
sudo nano /etc/selinux/config
```
**Modifica SELINUX=forzante**
```
SELINUX=enforcing
```

Salvare e uscire dal file, usando CTRL+X e Y e poi invio, quindi riavviare il sistema.

#### Abilitazione di AppArmor per i sistemi basati su Ubuntu

Per verificare se AppArmor è abilitato sul sistema, eseguire il seguente comando:
```bash
sudo apparmor_status
```


Se AppArmor non è installato, è possibile installarlo con il seguente comando:
```bash
sudo apt-get install apparmor
```

Per abilitare AppArmor, è necessario modificare il file **/etc/default/grub** e aggiungere il parametro **security=apparmor** alla variabile **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Aggiungi sicurezza=armatura**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Salvare e uscire dal file, usando CTRL+X e Y e poi invio, quindi eseguire il seguente comando per aggiornare la configurazione del bootloader del sistema:

```bash
sudo update-grub
```

Infine, riavviare il sistema.

Una volta abilitato SELinux o AppArmor, è possibile configurare i loro criteri per limitare i privilegi dei processi e l'accesso alle risorse del sistema. Questo può aiutare a minimizzare l'impatto potenziale di un attacco riuscito e a migliorare la sicurezza complessiva del sistema.


### Configurare i criteri delle password

La configurazione dei criteri delle password è un passo importante per rafforzare la sicurezza del sistema Linux. Imponendo requisiti forti per le password, è possibile garantire che gli account utente siano sicuri e protetti da potenziali attacchi. Ecco come configurare i criteri delle password sul vostro sistema Linux:

#### Configurazione dei criteri delle password su Ubuntu

Per configurare i criteri delle password su Ubuntu, è possibile utilizzare il modulo **pam_pwquality**. Questo modulo fornisce una serie di controlli sulla forza delle password che possono essere utilizzati per applicare le politiche sulle password. Per installare il modulo **pam_pwquality**, aprire una finestra di terminale e digitare:

```bash
sudo apt-get install libpam-pwquality
```

Una volta installato il modulo, è possibile configurare le sue impostazioni modificando il file **/etc/pam.d/common-password**. Ad esempio, per imporre una lunghezza minima della password di 8 caratteri e richiedere almeno una lettera maiuscola, una lettera minuscola, una cifra e un carattere speciale, si può aggiungere la seguente riga al file:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

È possibile configurare anche altre impostazioni, come l'età massima della password, aggiungendo righe al file.

#### Configurazione dei criteri delle password su CentOS

Per configurare i criteri delle password su CentOS, si può usare lo strumento **authconfig**. Questo strumento fornisce una serie di opzioni che possono essere utilizzate per configurare i criteri delle password. Ad esempio, per imporre una lunghezza minima della password di 8 caratteri e richiedere almeno una lettera maiuscola, una lettera minuscola, una cifra e un carattere speciale, si può usare il seguente comando:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Questo aggiorna i file **/etc/pam.d/system-auth** e **/etc/pam.d/password-auth** del sistema per applicare i criteri di password specificati.

Ricordate di rivedere e aggiornare regolarmente le politiche sulle password per garantire che rimangano efficaci contro potenziali attacchi.


### Monitorare i log di sistema

Il monitoraggio dei log di sistema è un aspetto importante per mantenere la sicurezza del sistema Linux. I registri di sistema registrano l'attività del sistema, come i tentativi di accesso falliti, gli errori e altri eventi importanti, e possono fornire indicazioni preziose su potenziali minacce alla sicurezza o altri problemi che richiedono attenzione. Ecco come monitorare i registri di sistema:

#### Utilizzando il comando journalctl

Nella maggior parte delle moderne distribuzioni Linux, è possibile utilizzare il comando **journalctl** per visualizzare i registri di sistema. Questo comando fornisce una serie di opzioni che possono essere utilizzate per filtrare e cercare le voci di registro.

Per visualizzare tutte le voci di registro, è sufficiente eseguire il seguente comando:

```bash
sudo journalctl
```

In questo modo vengono visualizzate tutte le voci di registro, con le più recenti in fondo.

Per filtrare le voci di registro in base a un'unità specifica, come un servizio o un processo, è possibile utilizzare l'opzione **-u** seguita dal nome dell'unità. Ad esempio, per visualizzare le voci di registro del servizio **sshd**, si può eseguire il seguente comando:
```bash
sudo journalctl -u sshd
```


Per filtrare le voci di registro in base a un intervallo di tempo specifico, è possibile utilizzare le opzioni **--since** e **--until** seguite da un timestamp o da un intervallo di tempo. Ad esempio, per visualizzare le voci di registro dell'ultima ora, si può eseguire il seguente comando:

```bash
sudo journalctl --since "1 hour ago"
```

#### Utilizzo di uno strumento di gestione dei log

Per i sistemi più grandi o più complessi, può essere utile utilizzare uno strumento di gestione dei registri per raccogliere e analizzare i registri di sistema. Gli strumenti di gestione dei registri possono fornire funzioni avanzate, come il monitoraggio dei registri in tempo reale, l'aggregazione dei registri e l'analisi dei registri, e possono aiutare a identificare e rispondere alle potenziali minacce alla sicurezza in modo più efficiente.

Esempi di strumenti di gestione dei registri per Linux sono:

- **Logwatch**: un semplice strumento di analisi dei registri che fornisce riepiloghi giornalieri via e-mail dei registri di sistema.
- **Logrotate**: uno strumento che ruota e comprime automaticamente i file di log per risparmiare spazio su disco
- **ELK stack**: un popolare strumento open-source per la gestione dei log che combina Elasticsearch, Logstash e Kibana per fornire funzionalità di monitoraggio e analisi dei log in tempo reale.

Ricordate di rivedere e analizzare regolarmente i log di sistema per rilevare e rispondere tempestivamente a potenziali minacce alla sicurezza.

______

## Non fare:

### Utilizzare password deboli

L'uso di password deboli è un errore comune che può rendere il sistema Linux vulnerabile agli attacchi. Gli aggressori possono utilizzare strumenti per indovinare le password basate su parole, nomi o date comuni. È importante utilizzare password forti e uniche, non facilmente indovinabili.

È possibile creare password forti utilizzando una combinazione di lettere maiuscole e minuscole, numeri e caratteri speciali. È inoltre buona norma utilizzare una password[password manager](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) può anche aiutarvi a ricordare le vostre password e a evitare di usare la stessa password per più account.

### Consentire l'accesso SSH di root

Consentire l'accesso SSH di root è un rischio per la sicurezza che può dare agli aggressori il controllo completo del sistema Linux. Al contrario, dovreste usare un account utente non root per accedere al sistema e poi elevare i privilegi usando il comando **sudo**. Questo aiuta a limitare l'impatto potenziale di un attacco limitando i privilegi degli account utente.

### Installare software non necessario

L'installazione di software non necessario può aumentare la superficie di attacco del sistema Linux, rendendolo più vulnerabile agli attacchi. È importante installare solo il software necessario per il sistema e rimuovere quello non necessario. Questo aiuta a ridurre il numero di potenziali vulnerabilità del sistema e a minimizzare il rischio di un attacco riuscito.

### Utilizzare software obsoleto

L'utilizzo di software obsoleto può rendere il sistema vulnerabile ad attacchi che sfruttano vulnerabilità note. È importante utilizzare sempre la versione più recente del software e aggiornarla regolarmente per garantire la sicurezza. In questo modo è possibile correggere le vulnerabilità note e proteggere il sistema da potenziali attacchi.

______

## Conclusione

In conclusione, l'hardening del sistema Linux è fondamentale per garantirne la sicurezza e proteggere i dati in esso contenuti. Seguendo le regole e le regole descritte in questo articolo, è possibile adottare misure importanti per proteggere il sistema e ridurre il rischio di minacce informatiche. Ricordate di tenere sempre aggiornato il sistema, di utilizzare un firewall, di configurare i criteri per le password e di monitorare i registri di sistema. Evitate di utilizzare password deboli, di disabilitare gli aggiornamenti automatici, di consentire l'accesso SSH di root, di installare software non necessario e di utilizzare software obsoleto. Tenendo a mente queste best practice, potete assicurarvi che il vostro sistema Linux rimanga sicuro e protetto.

## Riferimenti:

-[The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
-[Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
-[Ubuntu Security Documentation](https://ubuntu.com/security)
-[Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

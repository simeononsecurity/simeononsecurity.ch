---
title: "Introduzione ad Ansible: Automatizzare la gestione dell'infrastruttura IT"
draft: false
toc: true
date: 2023-02-25
description: "Imparate le basi di Ansible, uno strumento di automazione open-source che semplifica la gestione dell'infrastruttura IT attraverso un linguaggio dichiarativo."
tags: ["Introduzione ad Ansible", "Automazione della gestione dell'infrastruttura IT", "Nozioni di base di Ansible", "Automazione dell'infrastruttura IT", "Gestione della configurazione", "Distribuzione dell'applicazione", "Approvvigionamento", "Consegna continua", "Conformità alla sicurezza", "Orchestrazione", "YAML", "Moduli Ansible", "Ruoli", "Le migliori pratiche", "Controllo della versione", "Test", "Red Hat", "Amministratori di sistema", "Linux", "macOS", "Finestre", "Installazione di Ansible", "Inventario Ansible", "Playbook Ansible", "Moduli Ansible", "Ruoli di Ansible", "Le migliori pratiche di Ansible", "Test di Ansible", "Strumento di automazione dell'infrastruttura IT", "Tutorial su Ansible", "Automazione della gestione dell'infrastruttura"]
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "Un personaggio dei cartoni animati seduto a una scrivania, circondato da server e cavi, con il logo di Ansible sullo schermo del computer, che sorride mentre le attività vengono automatizzate."
coverCaption: ""
---

Ansible è uno strumento di automazione open-source che consente agli amministratori di sistema di automatizzare la gestione dell'infrastruttura IT. Fornisce un linguaggio semplice per descrivere lo stato desiderato dell'infrastruttura e lo applica automaticamente. Questo riduce il tempo e l'impegno necessari per gestire sistemi complessi e su larga scala.

Se non conoscete Ansible, questo articolo vi fornirà un'introduzione allo strumento, compresi i suoi concetti di base e come iniziare a usarlo.

## Introduzione ad Ansible

Ansible è stato sviluppato da Michael DeHaan nel 2012 e acquisito da Red Hat nel 2015. Da allora è diventato uno degli strumenti di automazione più popolari del settore.

Ansible utilizza un linguaggio semplice e dichiarativo chiamato YAML (abbreviazione di "YAML Ain't Markup Language") per definire lo stato desiderato dell'infrastruttura. Questo lo rende facile da leggere e da capire, anche per i non programmatori.

Ansible può essere utilizzato per automatizzare un'ampia gamma di attività, tra cui:

- **Gestione della configurazione**
- Distribuzione di applicazioni
- Consegna continua
- **Provvigionamento**
- **Conformità alla sicurezza**
- **Orchestrazione**

## Iniziare con Ansible

Per iniziare a utilizzare Ansible, è necessario installarlo sul proprio sistema. Ansible può essere installato su un'ampia gamma di sistemi operativi, tra cui Linux, macOS e Windows.

Per installare Ansible su Linux, in questo caso Ubuntu, si possono usare i seguenti comandi:
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
Altrimenti si possono usare le seguenti guide per installare ansible:
- [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

Una volta installato Ansible, si può verificare che funzioni eseguendo il seguente comando:
```bash
ansible --version
```

Questo dovrebbe visualizzare la versione di Ansible installata.

## Inventario di Ansible

Il primo passo per utilizzare Ansible è definire un inventario. Un inventario è un elenco di server che Ansible gestirà. Un inventario può essere definito in diversi formati, tra cui INI, YAML e JSON.

Ecco un esempio di file di inventario in formato INI:

```ini
[webservers]
webserver1.example.com
webserver2.example.com

[databases]
dbserver1.example.com
dbserver2.example.com
```

Questo file di inventario definisce due gruppi di server, "webserver" e "database", ed elenca i nomi di host dei server di ciascun gruppo.

## Playbook di Ansible

Una volta definito l'inventario, il passo successivo è la definizione di un playbook. Un playbook è un file YAML che descrive un insieme di attività che Ansible deve eseguire sui server dell'inventario.

Ecco un esempio di un semplice playbook:
```yml
name: Install Nginx
hosts: webservers
become: yes

tasks:
    - name: Install Nginx package
        apt:
        name: nginx
        state: present
```

Questo playbook installa il server web Nginx su tutti i server del gruppo "webservers".

Il `hosts` specifica su quale gruppo di server deve essere eseguito il playbook. Il parametro `become` Il parametro specifica che i task devono essere eseguiti con privilegi elevati (usando il parametro `sudo` o `su`

Il `tasks` elenca i singoli task che il playbook deve eseguire. In questo caso, c'è un solo task, che installa il pacchetto Nginx usando il metodo `apt` modulo.

## Moduli Ansible

I moduli di Ansible sono unità di codice riutilizzabili che possono essere utilizzate per eseguire compiti specifici. Ansible è dotato di un'ampia gamma di moduli incorporati e sono disponibili anche molti moduli di terze parti.

Ecco alcuni esempi di moduli integrati:

- `apt` - Gestire i pacchetti sui sistemi basati su Debian
- `yum` - Gestire i pacchetti sui sistemi basati su Red Hat
- `file` - Gestire i file
- `service` - Gestire i servizi di sistema
- `user` - Gestire utenti e gruppi
- `copy` - Copiare i file dalla macchina di controllo ai server gestiti

L'elenco completo dei moduli integrati si trova nella sezione [Ansible documentation](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Ruoli e struttura delle cartelle di Ansible

Un ruolo di Ansible è un modo per organizzare e riutilizzare attività e configurazioni comuni. È una struttura di cartelle che contiene task, gestori, modelli, file e altre risorse.

Ecco un esempio di un semplice ruolo Ansible per l'installazione e la configurazione di Nginx:
```
roles/
└── nginx/
    ├── tasks/
    │   ├── main.yml
    ├── handlers/
    │   ├── main.yml
    ├── templates/
    │   ├── nginx.conf.j2
    ├── files/
    ├── vars/
    ├── defaults/
    ├── meta/
```
In questo esempio, il ruolo nginx è una directory che contiene diverse sottodirectory, ognuna delle quali ha uno scopo specifico:

- **tasks**: contiene i task che verranno eseguiti dal ruolo.
- **handlers**: contiene i gestori che i task possono notificare.
- **templates**: contiene i modelli di Jinja2 che saranno usati per generare i file di configurazione per Nginx.
- **files**: contiene tutti i file statici necessari al ruolo.
- **vars**: contiene le variabili specifiche del ruolo.
- **defaults**: contiene le variabili predefinite per il ruolo.
- **meta**: contiene metadati sul ruolo, come le sue dipendenze.

I ruoli possono essere facilmente condivisi e riutilizzati in più playbook e progetti.

Ecco un esempio di file main.yml nella cartella tasks:
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  notify: restart nginx

- name: Enable Nginx
  systemd:
    name: nginx
    enabled: yes
    state: started
```

Questo task installa Nginx usando il modulo apt e abilita e avvia il servizio Nginx usando il modulo systemd. Inoltre notifica il gestore restart nginx, che riavvia Nginx se sono state apportate modifiche alla configurazione.

L'uso di un ruolo Ansible come questo può semplificare il processo di gestione e configurazione del software su più server o ambienti. Separando i task, i gestori, i template e le altre risorse in un'unica struttura di directory, è possibile gestire e riutilizzare più facilmente questi componenti in diversi playbook e progetti.

## Migliori pratiche per Ansible

Ecco alcune buone pratiche da seguire quando si usa Ansible:

### 1. Utilizzare il controllo della versione

Memorizzare i playbook e i ruoli di Ansible in un sistema di controllo delle versioni come Git è una best practice che può aiutare a tenere traccia delle modifiche e a collaborare con gli altri. Il controllo delle versioni fornisce una cronologia delle modifiche apportate alla base di codice, consentendo di tornare alle versioni precedenti se necessario. Inoltre, facilita la collaborazione con gli altri condividendo il codice e gestendo i conflitti.

### 2. Usare i ruoli per organizzare i playbook

I ruoli sono un modo efficace per organizzare i playbook e le attività di Ansible. Raggruppando le attività correlate in ruoli, è possibile rendere i playbook più modulari e riutilizzabili. I ruoli facilitano anche la condivisione del codice tra progetti diversi.

Ecco un esempio di playbook che utilizza un ruolo per installare e configurare Nginx:

```yml
name: Install and configure Nginx
hosts: webservers
become: yes
roles:
  - nginx
```

Questo playbook utilizza un ruolo chiamato "nginx" per installare e configurare Nginx sul gruppo di host "webservers".

### 3. Usare i tag per raggruppare le attività

I tag possono essere usati per raggruppare attività correlate nei playbook di Ansible. In questo modo è più facile eseguire parti specifiche di un playbook, soprattutto quando si lavora con playbook grandi e complessi.

Ecco un esempio di utilizzo dei tag in una playbook di Ansible:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes
tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
    tags: nginx_install

  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    tags: nginx_config
```

Questo playbook ha due task, uno per l'installazione di Nginx e uno per la configurazione di Nginx. A ogni task è associato un tag, in modo da facilitare l'esecuzione dei soli task necessari.

### 4. Usare le variabili per rendere i playbook più flessibili

Le variabili possono essere usate per rendere i playbook di Ansible più flessibili e riutilizzabili. Utilizzando le variabili, è possibile rendere i playbook più generici e adattabili a diversi ambienti.

Ecco un esempio di utilizzo delle variabili in un playbook Ansible:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes

vars:
nginx_port: 80
nginx_user: www-data

tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    notify: restart nginx

handlers:
  - name: restart nginx
    service:
    name: nginx
    state: restarted
```

Questo playbook utilizza variabili per specificare la porta su cui Nginx deve ascoltare e l'utente che deve eseguire Nginx. Questo rende il playbook più flessibile e adattabile a diversi ambienti.

### 5. Testare i playbook

Testare i playbook di Ansible è una best practice che può aiutare a individuare gli errori e a garantire che i playbook funzionino come previsto. Uno strumento popolare per testare le playbook di Ansible è Molecule.

Molecule è un framework di test che consente di verificare i playbook in modo coerente e automatizzato. Molecule può creare macchine virtuali, applicare il playbook e verificare che tutto funzioni come previsto. In questo modo è possibile individuare gli errori e assicurarsi che i playbook funzionino correttamente prima della distribuzione in produzione.

Ecco un esempio di come utilizzare Molecule per testare un ruolo Ansible:

```bash
molecule init role myrole
cd myrole
molecule test
```

## Conclusione

In questo articolo abbiamo introdotto Ansible, un potente strumento di automazione che può aiutare a gestire infrastrutture IT complesse. Abbiamo trattato i concetti di base di Ansible, tra cui inventari, playbook, moduli e ruoli.

Abbiamo anche discusso le migliori pratiche per l'utilizzo di Ansible, tra cui l'uso del controllo di versione, l'organizzazione dei playbook con i ruoli, l'uso di tag e variabili e la verifica dei playbook.

Se siete alle prime armi con Ansible, vi consigliamo di iniziare a sperimentare alcuni semplici playbook e di aumentare gradualmente le vostre competenze e conoscenze nel tempo. Con la pratica, sarete in grado di automatizzare con facilità anche le attività infrastrutturali più complesse!

---
title: "Guida per principianti: Uso della riga di comando di Linux per la sicurezza informatica"
date: 2023-03-13
toc: true
draft: false
description: "Imparate a utilizzare la riga di comando di Linux per la sicurezza informatica con comandi di base e avanzati."
tags: ["Linux", "Linea di comando", "Sicurezza informatica", "Guida per principianti", "Scansione di rete", "Test di vulnerabilità", "Analisi del malware", "Permessi", "Traffico di rete", "Stato del processo", "Statistiche di rete", "Ricerca file", "Wireshark", "TCPDump", "Nmap", "Linux CLI", "Sicurezza", "Test di penetrazione", "Forensica digitale"]
cover: "/img/cover/A_cartoon_illustration_of_a_person_wearing_a_hoodie.png"
coverAlt: "Un'illustrazione a fumetti di una persona che indossa una felpa con cappuccio, seduta davanti allo schermo di un computer con l'interfaccia della riga di comando di Linux visibile e con in mano una lente di ingrandimento per rappresentare l'aspetto della sicurezza informatica."
coverCaption: ""
---

**Linux** è un sistema operativo versatile e sicuro, ampiamente utilizzato nel settore della cybersecurity grazie alla sua natura open-source. Tuttavia, per i principianti può essere scoraggiante utilizzare l'interfaccia a riga di comando (CLI) di Linux per eseguire operazioni di cybersecurity. Questa guida si propone di fornire ai principianti una panoramica dei comandi della riga di comando di Linux di base e avanzati, utili ai fini della cybersecurity.

## Comandi Linux di base per la cybersicurezza

### Stampa la directory di lavoro

Il comando **pwd** (print working directory) serve a visualizzare la directory di lavoro corrente nella CLI. La directory di lavoro è la directory in cui ci si trova attualmente nel file system. Il comando è utile per navigare nel file system e capire la propria posizione rispetto ad altre directory. Ad esempio, se ci si trova nella directory home e si desidera navigare nella directory documenti, si possono usare i seguenti comandi:

```bash
$ pwd
/home/user
$ cd documents
$ pwd
/home/user/documents
```

Nell'esempio precedente, il primo comando stampa la directory di lavoro corrente, che è la home directory. Il secondo comando cambia la directory in quella dei documenti e il terzo comando stampa la directory di lavoro corrente, che ora è la directory dei documenti.

### Elenco

Il comando **ls** viene utilizzato per elencare il contenuto di una directory nella CLI. Il comando visualizza i nomi dei file e delle directory presenti nella directory di lavoro corrente. Il comando è utile per identificare i file e le directory in una posizione specifica. Ad esempio, se si desidera visualizzare il contenuto della directory documenti, è possibile utilizzare il seguente comando:

```bash
$ ls documents
file1.txt file2.pdf file3.docx
```

Nell'esempio precedente, il comando elenca il contenuto della directory documenti, che contiene tre file: file1.txt, file2.pdf e file3.docx. Il comando può essere usato anche senza argomenti per elencare il contenuto della directory di lavoro corrente. Ad esempio:

```bash
$ ls
Desktop Documents Downloads Music Pictures Public Templates Videos
```

Nell'esempio precedente, il comando elenca il contenuto della directory home, che contiene diverse sottodirectory come Desktop, Documenti, Download e così via.

### Cambia directory

Il comando **cd** (change directory) viene utilizzato per cambiare la directory di lavoro corrente nella CLI. Il comando consente di navigare nel file system e di accedere ai file in posizioni diverse. Ad esempio, se si desidera cambiare la directory di lavoro corrente in quella dei documenti, si può usare il seguente comando:

```bash
$ cd documents
```

Nell'esempio precedente, il comando cambia la directory di lavoro corrente in quella dei documenti, che si trova nella directory di lavoro corrente. Il comando può essere usato anche con un percorso assoluto o relativo per cambiare la directory di lavoro in una directory che non si trova nella directory di lavoro corrente. Ad esempio:

```bash
$ cd /usr/local/bin
```

Nell'esempio precedente, il comando cambia la directory di lavoro corrente in /usr/local/bin, che è un percorso assoluto. In alternativa, è possibile utilizzare un percorso relativo per cambiare la directory di lavoro. Ad esempio:

```bash
$ cd ../..
```


Nell'esempio precedente, il comando cambia la directory di lavoro corrente due livelli più in alto rispetto alla directory di lavoro corrente. La notazione ".." rappresenta la directory madre e può essere utilizzata per navigare nell'albero delle directory.


### Concatenare

Il comando **cat** (concatenate) viene utilizzato per visualizzare il contenuto di un file nella CLI. Il comando è utile per visualizzare il contenuto di file di testo come i file di log o di configurazione. Ad esempio, se si desidera visualizzare il contenuto di un file denominato "file1.txt", è possibile utilizzare il seguente comando:

```bash
$ cat file1.txt
```

Nell'esempio precedente, il comando visualizza il contenuto del file "file1.txt". È inoltre possibile utilizzare il comando per concatenare più file e visualizzarne il contenuto nella CLI. Ad esempio:

```bash
$ cat file1.txt file2.txt file3.txt
```


Nell'esempio precedente, il comando visualizza il contenuto di tre file: file1.txt, file2.txt e file3.txt. È anche possibile utilizzare il comando con i caratteri jolly per concatenare tutti i file che corrispondono a un modello specifico. Ad esempio:

```bash
$ cat *.txt
```

Nell'esempio precedente, il comando visualizza il contenuto di tutti i file con estensione ".txt" nella directory di lavoro corrente. Questo comando è utile per visualizzare rapidamente il contenuto di più file senza aprirli singolarmente.


### Stampa di espressioni regolari globali

Il comando **grep** (stampa globale di espressioni regolari) è usato per cercare stringhe o modelli specifici in un file o in un insieme di file nella CLI. Il comando è utile per identificare schemi nei file di log o per cercare informazioni specifiche nei file di configurazione. Ad esempio, se si desidera cercare tutte le occorrenze della parola "errore" in un file denominato "logfile.txt", è possibile utilizzare il seguente comando:

```bash
$ grep "error" logfile.txt
```

Nell'esempio precedente, il comando cerca tutte le occorrenze della parola "errore" nel file "logfile.txt" e visualizza le righe corrispondenti nella CLI. È inoltre possibile utilizzare il comando con le espressioni regolari per cercare modelli più complessi. Ad esempio, se si desidera cercare tutte le righe che contengono una parola che inizia con "p" e termina con "y", è possibile utilizzare il seguente comando:

```bash
$ grep "p.*y" logfile.txt
```

Nell'esempio precedente, il comando cerca tutte le righe che contengono una parola che inizia con "p" e finisce con "y" nel file "logfile.txt". L'espressione regolare "p.*y" corrisponde a qualsiasi stringa che inizia con "p" e finisce con "y", con qualsiasi numero di caratteri intermedi. Questo comando è utile per trovare schemi nei file di log che possono aiutare a identificare minacce alla sicurezza o problemi di prestazioni.


### Cambia modalità

Il comando **chmod** (change mode) viene utilizzato per modificare i permessi di un file o di una directory nella CLI. Questo comando è essenziale per proteggere i file e le directory e controllare chi vi ha accesso. I permessi sono rappresentati da tre cifre che corrispondono rispettivamente a proprietario, gruppo e altri. Le cifre sono calcolate in base alla seguente formula:

```
4 = read
2 = write
1 = execute
```

Ad esempio, se si desidera assegnare al proprietario i permessi di lettura e scrittura e al gruppo e agli altri i permessi di sola lettura per un file denominato "file1.txt", è possibile utilizzare il seguente comando:

```bash
$ chmod 644 file1.txt
```

Nell'esempio sopra riportato, il comando imposta i permessi del file "file1.txt" a 644. La prima cifra (6) rappresenta i permessi del proprietario, che sono di lettura e scrittura (4 + 2 = 6). La seconda cifra (4) rappresenta i permessi del gruppo, che sono di sola lettura. La terza cifra (4) rappresenta i permessi per gli altri, anch'essi in sola lettura.

È possibile utilizzare il comando con le lettere per modificare i permessi. Ad esempio, se si desidera assegnare al proprietario e al gruppo i permessi di lettura e scrittura e agli altri nessun permesso per un file denominato "file2.txt", è possibile utilizzare il seguente comando:

```bash
$ chmod ug=rw,o= file2.txt
```

Nell'esempio precedente, il comando imposta i permessi del file "file2.txt" su ug=rw,o=, dove "ug" rappresenta il proprietario e il gruppo, "r" il permesso di lettura e "w" il permesso di scrittura. Il segno "=" significa "imposta i permessi a", mentre "o=" significa "rimuovi tutti i permessi per gli altri". Questo comando è utile per controllare l'accesso a file e directory sensibili e per prevenire accessi non autorizzati.


## Comandi avanzati di Linux per la sicurezza informatica

### Network Mapper

Il comando **nmap** è un potente strumento di scansione della rete nella CLI che può essere utilizzato per identificare host e servizi su una rete, nonché potenziali vulnerabilità. Il comando può eseguire una serie di tecniche di scansione, tra cui la scoperta degli host, la scansione delle porte e il rilevamento del sistema operativo.

Uno degli usi più elementari di nmap è la scansione di un singolo indirizzo IP o host. Ad esempio, per eseguire la scansione di un singolo indirizzo IP (192.168.1.1) alla ricerca di porte aperte, è possibile utilizzare il seguente comando:

```bash
$ nmap 192.168.1.1
```

Il comando precedente esegue una scansione TCP SYN sull'IP di destinazione e restituisce un elenco di porte aperte. L'output mostrerà le porte aperte insieme al servizio in esecuzione su ciascuna porta, lo stato della porta (aperta/chiusa) e talvolta informazioni aggiuntive come il sistema operativo in esecuzione sul target.

Nmap può anche essere utilizzato per scansionare più host o indirizzi IP contemporaneamente. Ad esempio, per analizzare un intervallo di indirizzi IP (192.168.1.1-255) alla ricerca di porte aperte, è possibile utilizzare il seguente comando:

```bash
$ nmap 192.168.1.1-255
```

Il comando di cui sopra scansiona tutti gli indirizzi IP dell'intervallo e restituisce le porte e i servizi aperti per ciascun target.

Oltre alla scoperta di base degli host e alla scansione delle porte, nmap può anche eseguire scansioni più avanzate, come il rilevamento di servizi e versioni, il rilevamento del sistema operativo e la scansione delle vulnerabilità. Queste scansioni possono essere utili per identificare potenziali vulnerabilità di sicurezza su una rete e metterla al sicuro da potenziali attacchi.

### TCP Packet Dumper

Il comando **tcpdump** viene utilizzato per catturare e analizzare il traffico di rete nella CLI, rendendolo utile per la risoluzione di problemi di rete, l'analisi del comportamento della rete e l'identificazione di potenziali minacce alla sicurezza. Il comando cattura i pacchetti in tempo reale e può filtrare i pacchetti in base a vari criteri, come l'indirizzo IP di origine o di destinazione, il protocollo e la porta.

Uno degli usi più elementari di tcpdump è quello di catturare tutto il traffico di rete su un'interfaccia specifica. Ad esempio, per catturare tutto il traffico sull'interfaccia eth0, si può usare il seguente comando:

```bash
$ sudo tcpdump -i eth0
```

Il comando precedente cattura tutti i pacchetti sull'interfaccia eth0 e li visualizza in tempo reale nella CLI. L'output mostrerà gli indirizzi IP di origine e di destinazione, il protocollo e altre informazioni su ciascun pacchetto.

Tcpdump può anche essere usato per filtrare i pacchetti in base a vari criteri. Ad esempio, per catturare tutti i pacchetti inviati a o da un indirizzo IP specifico, è possibile utilizzare il seguente comando:

```bash
$ sudo tcpdump host 192.168.1.1
```

Il comando precedente cattura tutti i pacchetti inviati da o verso l'indirizzo IP 192.168.1.1 e li visualizza in tempo reale nella CLI. È anche possibile filtrare i pacchetti in base al protocollo (ad esempio, TCP, UDP), al numero di porta o ad altri criteri.

Oltre a catturare i pacchetti in tempo reale, tcpdump può essere usato anche per catturare i pacchetti in un file da analizzare successivamente. Ad esempio, per catturare tutti i pacchetti dell'interfaccia eth0 e salvarli in un file denominato "capture.pcap", si può usare il seguente comando:

```bash
$ sudo tcpdump -i eth0 -w capture.pcap
```

Il comando precedente cattura tutti i pacchetti sull'interfaccia eth0 e li salva nel file "capture.pcap" in formato pcap, che può essere analizzato in seguito con strumenti come Wireshark. Questo comando è utile per analizzare il comportamento della rete e identificare potenziali minacce alla sicurezza.

### Stato del processo

Il comando **ps** visualizza nella CLI informazioni sui processi in esecuzione su un sistema Linux, utili per identificare processi sospetti che potrebbero essere in esecuzione su un sistema e potenzialmente comprometterne la sicurezza. Il comando può visualizzare un'ampia gamma di informazioni sui processi in esecuzione, tra cui l'ID del processo (PID), l'utente, l'utilizzo della CPU e della memoria e il nome del comando.

Uno degli usi più elementari di ps è quello di visualizzare un elenco di tutti i processi in esecuzione su un sistema. Ad esempio, per visualizzare un elenco di tutti i processi in esecuzione sul sistema, è possibile utilizzare il seguente comando:

```bash
$ ps aux
```

Il comando precedente visualizza un elenco di tutti i processi in esecuzione sul sistema, con il relativo PID, utente, utilizzo della CPU e della memoria e nome del comando. Questo comando è utile per avere una visione generale dei processi in esecuzione sul sistema e per identificare eventuali processi sospetti.

Ps può anche essere usato per visualizzare informazioni su un processo specifico o su un insieme di processi. Ad esempio, per visualizzare informazioni su un processo con un PID specifico (ad esempio, PID 1234), si può usare il seguente comando:

```bash
$ ps -p 1234
```

Il comando precedente visualizza le informazioni sul processo con PID 1234, compresi l'utente, l'utilizzo della CPU e della memoria e il nome del comando. È anche possibile visualizzare informazioni su un insieme di processi specificando più PID.

Oltre a visualizzare informazioni sui processi in esecuzione, ps può essere utilizzato anche per monitorare lo stato dei processi in tempo reale. Ad esempio, per monitorare l'utilizzo della CPU e della memoria di un processo specifico (ad esempio, il PID 1234) in tempo reale, è possibile utilizzare il seguente comando:

```bash
$ ps -p 1234 -o %cpu,%mem
```

Il comando precedente visualizza l'utilizzo della CPU e della memoria del processo con PID 1234 in tempo reale, aggiornando l'output ogni secondo. Questo comando è utile per monitorare le prestazioni dei processi critici e identificare potenziali colli di bottiglia.

### Statistiche di rete

Il comando **netstat** visualizza informazioni sulle connessioni di rete attive su un sistema Linux nella CLI, rendendolo utile per identificare connessioni di rete non autorizzate e potenziali minacce alla sicurezza. Il comando può visualizzare un'ampia gamma di informazioni sulle connessioni di rete attive, compresi gli indirizzi locali e remoti, il protocollo utilizzato (ad esempio, TCP, UDP) e lo stato della connessione.

Uno degli usi più elementari di netstat è quello di visualizzare un elenco di tutte le connessioni di rete attive su un sistema. Ad esempio, per visualizzare un elenco di tutte le connessioni di rete attive, si può usare il seguente comando:

```bash
$ netstat -a
```


Il comando precedente visualizza un elenco di tutte le connessioni di rete attive sul sistema, con i relativi indirizzi locali e remoti, il protocollo utilizzato e lo stato della connessione. Questo comando è utile per avere una visione generale delle connessioni di rete attive su un sistema e per identificare eventuali connessioni non autorizzate.

Netstat può anche essere usato per visualizzare informazioni sulle connessioni di rete per un protocollo specifico (ad esempio, TCP). Ad esempio, per visualizzare un elenco di tutte le connessioni TCP attive sul sistema, si può usare il seguente comando:

```bash
$ netstat -at
```

Il comando precedente visualizza un elenco di tutte le connessioni TCP attive sul sistema, con i relativi indirizzi locali e remoti e lo stato della connessione.

Oltre a visualizzare le informazioni sulle connessioni di rete attive, netstat può essere utilizzato anche per visualizzare le statistiche di rete per un protocollo specifico (ad esempio, TCP). Ad esempio, per visualizzare le statistiche di tutte le connessioni TCP sul sistema, si può usare il seguente comando:

```bash
$ netstat -st
```

Il comando precedente visualizza le statistiche di tutte le connessioni TCP sul sistema, compreso il numero di connessioni attive, il numero di connessioni in ogni stato e il numero di errori che si sono verificati. Questo comando è utile per monitorare lo stato generale della rete e identificare potenziali problemi di prestazioni.


### Trova file

Il comando **find** viene utilizzato per cercare file e directory su un sistema Linux nella CLI, rendendolo utile per individuare file e directory specifici che potrebbero essere nascosti o difficili da trovare. Il comando cerca file e directory in base a un'ampia gamma di criteri, tra cui il nome, la dimensione, il tempo di modifica e i permessi.

Uno degli usi più elementari di find è la ricerca di file e directory in base al nome. Ad esempio, per cercare tutti i file nella directory corrente e nelle sue sottodirectory che hanno il nome "esempio.txt", si può usare il seguente comando:

```bash
$ find . -name example.txt
```

Il comando precedente cercherà tutti i file nella directory corrente e nelle sue sottodirectory che hanno il nome "example.txt" e ne visualizzerà il percorso completo.

Find può anche essere usato per cercare file e directory in base alla loro dimensione. Ad esempio, per cercare tutti i file nella directory corrente e nelle sue sottodirectory di dimensioni superiori a 1 MB, si può usare il seguente comando:

```bash
$ find . -size +1M
```

Il comando precedente cerca tutti i file nella directory corrente e nelle sue sottodirectory di dimensioni superiori a 1 MB e ne visualizza il percorso completo.

Oltre a cercare i file e le directory in base al nome e alle dimensioni, find può essere usato anche per cercare i file e le directory in base all'ora di modifica e ai permessi. Ad esempio, per cercare tutti i file nella directory corrente e nelle sue sottodirectory che sono stati modificati negli ultimi 7 giorni, si può usare il seguente comando:

```bash
$ find . -mtime -7
```

Il comando precedente cerca tutti i file nella directory corrente e nelle sue sottodirectory che sono stati modificati negli ultimi 7 giorni e ne visualizza il percorso completo.

Nel complesso, il comando find è uno strumento potente per la ricerca di file e directory su un sistema Linux in base a un'ampia gamma di criteri, il che lo rende utile per una serie di attività, tra cui l'amministrazione del sistema e la sicurezza informatica.

______

L'uso della riga di comando di Linux per la cybersicurezza può risultare difficile per i principianti. Tuttavia, con i comandi di base e avanzati descritti in questa guida, è possibile iniziare a utilizzare la CLI di Linux a proprio vantaggio nella cybersecurity. Ricordate di usare cautela nell'esecuzione dei comandi e di comprendere a fondo le funzioni di ciascun comando prima di utilizzarlo.

Per saperne di più sull'uso di Linux per la cybersicurezza, scaricate il documento **[Kali Linux](https://www.kali.org/downloads/) sistema operativo, progettato specificamente per i test di penetrazione e la digital forensics.

## Conclusione

In conclusione, l'interfaccia a riga di comando di Linux è uno strumento potente per i professionisti della cybersicurezza, ma può essere scoraggiante per i principianti. Imparando i comandi di base e avanzati descritti in questa guida, potrete iniziare a usare la CLI di Linux a vostro vantaggio nella cybersecurity. Ricordate di usare sempre la massima cautela nell'esecuzione dei comandi e di comprendere a fondo le funzioni di ciascun comando prima di utilizzarlo. Con la pratica e l'esperienza, potrete diventare abili nell'uso della riga di comando di Linux e portare le vostre abilità di cybersecurity a un livello superiore.
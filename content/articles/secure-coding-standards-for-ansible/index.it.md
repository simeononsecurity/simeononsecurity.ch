---
title: "Linee guida per la codifica sicura di Ansible: Migliori pratiche"
date: 2023-03-02
toc: true
draft: false
description: "Imparate le migliori pratiche per scrivere codice sicuro con Ansible, un popolare strumento per la gestione della configurazione e la distribuzione."
tags: ["Codifica sicura", "Ansible", "Gestione della configurazione", "Distribuzione", "Principio del minor privilegio", "Ansible Vault", "Password forti", "Controllo degli accessi", "Sistema di controllo delle versioni", "Protocolli di comunicazione sicuri", "SSH", "WinRM", "Certificati TLS", "Sanitizzare l'input dell'utente", "Convalida dell'ingresso", "Gestione degli errori", "Pratiche di codifica sicure", "Iniezione di codice", "Linee guida per la codifica sicura", "Sicurezza dell'infrastruttura"]
cover: "/img/cover/A_cartoon_image_of_a_castle_protected_by_a_shield.png"
coverAlt: " L'immagine di un castello protetto da uno scudo rappresenta le misure di sicurezza dell'infrastruttura gestita da Ansible."
coverCaption: ""
---

Man mano che le organizzazioni si orientano verso l'automazione, **Ansible** è diventato una scelta popolare per la **gestione della configurazione** e la **distribuzione**. Tuttavia, come ogni software, Ansible non è immune da vulnerabilità di sicurezza. Scrivere **codice sicuro** è fondamentale per garantire la sicurezza e l'affidabilità dell'infrastruttura gestita da Ansible. Questo articolo fornisce **linee guida** per la scrittura di codice **sicuro** utilizzando Ansible.

## Comprendere la sicurezza di Ansible

Prima di immergersi nelle linee guida, è importante comprendere le caratteristiche di sicurezza di Ansible. Ansible fornisce **crittografia** per la comunicazione tra i nodi di controllo e i nodi gestiti. Ansible fornisce anche una **conservazione sicura** dei **segreti** e di altre informazioni sensibili utilizzando il **Vault**. Inoltre, Ansible dispone di un **meccanismo di sandboxing** per proteggere dall'esecuzione di codice potenzialmente dannoso.

Tuttavia, queste caratteristiche di sicurezza non esimono gli sviluppatori dallo scrivere codice sicuro. L'osservanza delle seguenti linee guida aiuterà gli sviluppatori a scrivere codice sicuro che integri le funzioni di sicurezza integrate di Ansible.

## Linea guida 1: Utilizzare la versione più recente di Ansible

Ansible viene costantemente aggiornato per risolvere vulnerabilità e bug di sicurezza. L'uso dell'ultima versione di Ansible garantisce agli sviluppatori l'accesso alle ultime correzioni e miglioramenti della sicurezza.

Gli sviluppatori dovrebbero controllare regolarmente la presenza di aggiornamenti e installarli il prima possibile. Possono anche iscriversi alla mailing list Ansible Security Announcements per ricevere notifiche sugli aggiornamenti di sicurezza. L'aggiornamento all'ultima versione di Ansible è un passo semplice che può migliorare significativamente la sicurezza dell'infrastruttura gestita da Ansible.

## Linea guida 2: Seguire il principio del minimo privilegio

Il **principio del minimo privilegio** è un principio fondamentale di sicurezza che si applica ad Ansible. Questo principio afferma che un utente deve avere solo il livello minimo di accesso necessario per svolgere la propria funzione lavorativa. Questo principio si applica anche ad Ansible. Gli sviluppatori dovrebbero concedere ai nodi gestiti il livello minimo di accesso richiesto per eseguire i compiti necessari.

Ad esempio, se un playbook richiede solo l'accesso in lettura a un file specifico, gli sviluppatori dovrebbero concedere solo l'accesso in lettura al file e non l'accesso in scrittura o in esecuzione. Gli sviluppatori devono anche limitare il numero di utenti che hanno accesso ad Ansible. L'accesso deve essere limitato agli utenti autorizzati che devono gestire l'infrastruttura con Ansible.

Ansible fornisce diversi meccanismi per implementare il principio del minimo privilegio, come ad esempio la funzione`become` direttiva. Il`become` consente agli sviluppatori di eseguire attività con i privilegi di un altro utente, come ad esempio`sudo` Gli sviluppatori dovrebbero utilizzare`become` solo se necessario e fornire solo il livello di privilegi necessario.

Implementando il principio del minimo privilegio, gli sviluppatori possono limitare il danno potenziale causato da un attaccante in caso di violazione della sicurezza. Questa linea guida può migliorare significativamente la sicurezza dell'infrastruttura gestita da Ansible.

## Linea guida 3: Utilizzare Ansible Vault per le informazioni sensibili

Le informazioni sensibili come password, chiavi API e certificati non dovrebbero essere memorizzate in testo normale nei playbook di Ansible. La memorizzazione di informazioni sensibili in testo normale può compromettere la sicurezza dell'infrastruttura gestita da Ansible. Ansible fornisce il **Vault** per archiviare in modo sicuro le informazioni sensibili.

Il Vault cripta le informazioni sensibili con una password o un file chiave. Gli sviluppatori possono utilizzare il`ansible-vault` per creare un nuovo file crittografato, modificare un file crittografato esistente o visualizzare un file crittografato. Il comando`ansible-vault` può essere usato anche per criptare o decriptare singole variabili. Ad esempio, per creare un nuovo file crittografato, gli sviluppatori possono usare il seguente comando:

```bash
ansible-vault create secret.yml
```

Questo comando creerà un nuovo file crittografato chiamato`secret.yml` Gli sviluppatori possono modificare questo file utilizzando il metodo`ansible-vault edit` comando. Verrà richiesto di inserire la password per il Vault.

Gli sviluppatori devono inoltre assicurarsi che le password e i file chiave siano archiviati in modo sicuro. Le password e i file chiave non devono essere memorizzati in chiaro. Devono essere memorizzati in un luogo sicuro, come un gestore di password o un file server sicuro.

L'uso del Vault per archiviare le informazioni sensibili è un passo fondamentale per proteggere l'infrastruttura gestita da Ansible. Seguendo questa linea guida, gli sviluppatori possono garantire che le informazioni sensibili non siano esposte in chiaro e siano accessibili solo agli utenti autorizzati.

## Linea guida 4: Utilizzare password forti

Le password utilizzate per l'autenticazione devono essere **forti** e **uniche**. L'uso di password deboli o comuni può compromettere la sicurezza dell'infrastruttura gestita da Ansible. Gli sviluppatori dovrebbero anche evitare di usare password predefinite o di codificare le password nei playbook. Le password devono essere archiviate in modo sicuro utilizzando il Vault.

Una password forte deve avere un minimo di 12 caratteri e contenere una combinazione di lettere maiuscole e minuscole, numeri e caratteri speciali. Gli sviluppatori dovrebbero anche evitare di utilizzare nelle password informazioni facilmente intuibili, come nomi o date di nascita. Possono utilizzare un gestore di password per generare password forti e uniche.

Le password utilizzate nei playbook devono essere memorizzate in formato crittografato utilizzando il Vault. Gli sviluppatori dovrebbero anche evitare di codificare le password nei playbook. Dovrebbero invece utilizzare variabili per memorizzare le password e farvi riferimento nei playbook. Ad esempio, gli sviluppatori possono definire una variabile denominata`db_password` in un file criptato separato e fare riferimento ad esso nel playbook utilizzando la seguente sintassi:
```yml
db_password: "{{ vault_db_password }}"
```

Questa sintassi farà riferimento al file`db_password` dal file crittografato e decifrarlo utilizzando il Vault.

Utilizzando password forti e conservandole in modo sicuro, gli sviluppatori possono impedire l'accesso non autorizzato all'infrastruttura gestita da Ansible. Questa linea guida è un semplice passo che può migliorare significativamente la sicurezza dell'infrastruttura gestita da Ansible.


## Linea guida 5: Limitare l'accesso ai Playbook

L'accesso ai playbook di Ansible deve essere limitato agli utenti autorizzati. Gli sviluppatori dovrebbero usare un **sistema di controllo delle versioni** come **Git** per gestire i playbook. Git offre funzioni di **controllo degli accessi** e **auditing** che possono aiutare a far rispettare le politiche di sicurezza.

## Linea guida 6: Utilizzare protocolli di comunicazione sicuri

Ansible supporta diversi protocolli di comunicazione, tra cui SSH e WinRM. SSH è il protocollo consigliato per gli host Linux e macOS. WinRM è il protocollo consigliato per gli host Windows. Gli sviluppatori devono assicurarsi che la comunicazione tra i nodi di controllo e i nodi gestiti sia **crittografata**.

SSH è un protocollo di comunicazione sicuro che cripta le comunicazioni tra i nodi di controllo e i nodi gestiti. Gli sviluppatori devono utilizzare chiavi SSH forti per l'autenticazione. Le chiavi SSH devono avere una lunghezza minima di 2048 bit. Gli sviluppatori dovrebbero inoltre disabilitare l'autenticazione tramite password per SSH.

WinRM è un protocollo di comunicazione sicuro che cripta le comunicazioni tra i nodi di controllo e i nodi gestiti. Gli sviluppatori devono utilizzare WinRM su HTTPS per garantire la crittografia delle comunicazioni. Dovrebbero inoltre utilizzare certificati forti per l'autenticazione.

Gli sviluppatori devono anche assicurarsi che i certificati TLS utilizzati per la comunicazione HTTPS siano validi e non scaduti. Possono utilizzare strumenti come`openssl` per generare e gestire i certificati TLS.

L'uso di protocolli di comunicazione sicuri è un passo fondamentale per proteggere l'infrastruttura gestita da Ansible. Seguendo questa linea guida, gli sviluppatori possono garantire che la comunicazione tra i nodi di controllo e i nodi gestiti sia criptata e sicura.

## Linea guida 7: Verifica delle identità degli host

Gli sviluppatori devono verificare l'identità dei nodi gestiti prima di consentire loro di connettersi ai nodi di controllo. Ansible fornisce diversi meccanismi per verificare le identità degli host, tra cui le **impronte digitali delle chiavi SSH** e i **certificati TLS**. Gli sviluppatori devono anche assicurarsi che le configurazioni SSH e TLS siano aggiornate e sicure.

Le impronte digitali delle chiavi SSH sono identificatori unici delle chiavi SSH utilizzate dai nodi gestiti per l'autenticazione. Gli sviluppatori devono verificare le impronte digitali delle chiavi SSH dei nodi gestiti prima di consentire loro di connettersi ai nodi di controllo. Possono utilizzare le chiavi`ssh-keygen` per generare le impronte digitali delle chiavi SSH e confrontarle con quelle fornite dai nodi gestiti.

I certificati TLS sono usati dai nodi gestiti per autenticarsi ai nodi di controllo. Gli sviluppatori devono assicurarsi che i certificati TLS utilizzati dai nodi gestiti siano validi e non scaduti. Devono inoltre assicurarsi che i nodi di controllo si fidino dei certificati TLS utilizzati dai nodi gestiti.

Gli sviluppatori devono anche assicurarsi che le configurazioni SSH e TLS siano aggiornate e sicure. Le configurazioni SSH e TLS devono utilizzare algoritmi di crittografia e autenticazione forti. Devono inoltre essere configurate per rifiutare cifrari e protocolli deboli.

La verifica dell'identità dei nodi gestiti è un passo fondamentale per la sicurezza dell'infrastruttura gestita da Ansible. Seguendo questa linea guida, gli sviluppatori possono prevenire gli attacchi man-in-the-middle e garantire che solo i nodi gestiti autorizzati possano connettersi ai nodi di controllo.

## Linea guida 8: Sanitizzare l'input dell'utente

Gli sviluppatori dovrebbero sanificare l'input dell'utente per prevenire **code injection** e altre vulnerabilità di sicurezza. Gli sviluppatori dovrebbero anche utilizzare **input validati** quando possibile per ridurre il rischio di vulnerabilità della sicurezza.

## Linea guida 9: Seguire pratiche di codifica sicure

Gli sviluppatori devono seguire **pratiche di codifica sicure** come la **convalida dell'input**, la **gestione degli errori** e la **sanitizzazione** dell'input. Gli sviluppatori devono inoltre seguire le **linee guida per la codifica sicura** del linguaggio di programmazione utilizzato in Ansible.

Gli sviluppatori devono sanificare l'input dell'utente per prevenire la **code injection** e altre vulnerabilità di sicurezza. L'iniezione di codice è un tipo di attacco in cui un aggressore inietta codice dannoso in un'applicazione sfruttando le vulnerabilità nell'input dell'utente. Gli sviluppatori dovrebbero anche utilizzare input convalidati ogni volta che è possibile per ridurre il rischio di vulnerabilità di sicurezza.

Gli sviluppatori possono utilizzare l'opzione`regex_replace` in Ansible per sanificare l'input dell'utente. Il filtro`regex_replace` consente agli sviluppatori di sostituire i pattern nelle stringhe con altri pattern. Ad esempio, per sostituire tutti i caratteri non alfanumerici di una stringa con una stringa vuota, gli sviluppatori possono utilizzare il seguente codice:

```yaml
- name: Sanitize user input
  vars:
    user_input: "Hello! This is a string with non-alphanumeric characters."
    sanitized_input: "{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}"
  debug:
    var: sanitized_input
```
In questo esempio, il`regex_replace` viene utilizzato per sostituire tutti i caratteri non alfanumerici nel file`user_input` con una stringa vuota. L'input sanificato viene memorizzato nella variabile`sanitized_input` variabile.

Gli sviluppatori possono anche usare la convalida dell'input per ridurre il rischio di vulnerabilità della sicurezza. La convalida dell'input consiste nel verificare che l'input dell'utente soddisfi determinati criteri. Ad esempio, gli sviluppatori possono convalidare l'input dell'utente per assicurarsi che contenga solo caratteri alfanumerici. La convalida dell'input può essere implementata utilizzando i condizionali e le espressioni regolari di Ansible.

Sanificando l'input dell'utente e utilizzando input convalidati, gli sviluppatori possono prevenire l'iniezione di codice e altre vulnerabilità di sicurezza nei playbook di Ansible. Questa linea guida è un semplice passo che può migliorare significativamente la sicurezza dell'infrastruttura gestita da Ansible.
______

## Conclusione

Ansible è uno strumento potente per la gestione della configurazione e il deployment, ma è importante scrivere codice sicuro per garantire la sicurezza e l'affidabilità dell'infrastruttura gestita da Ansible. Seguire le linee guida fornite in questo articolo aiuterà gli sviluppatori a scrivere codice sicuro che integri le funzioni di sicurezza integrate in Ansible.

Ricordate di usare sempre l'ultima versione di Ansible, di seguire il principio del minimo privilegio, di usare Ansible Vault per le informazioni sensibili, di usare password forti, di limitare l'accesso ai playbook, di usare protocolli di comunicazione sicuri, di verificare le identità degli host, di sanificare l'input degli utenti e di seguire pratiche di codifica sicure. Queste linee guida aiuteranno gli sviluppatori a scrivere codice sicuro e a mantenere la loro infrastruttura al sicuro dalle vulnerabilità di sicurezza.

Seguendo queste linee guida, le organizzazioni possono garantire che l'infrastruttura gestita da Ansible sia sicura e affidabile. Con un codice sicuro e le funzioni di sicurezza integrate di Ansible, le organizzazioni possono sfruttare i vantaggi dell'automazione senza sacrificare la sicurezza.

## Riferimenti

-[Ansible Documentation](https://docs.ansible.com/)
-[Ansible Vault Documentation](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
-[Git Documentation](https://git-scm.com/doc)
-[OpenSSH Documentation](https://www.openssh.com/)
-[Transport Layer Security (TLS) Documentation](https://tools.ietf.org/html/rfc8446)
-[OWASP Code Injection Documentation](https://owasp.org/www-community/attacks/Code_Injection)

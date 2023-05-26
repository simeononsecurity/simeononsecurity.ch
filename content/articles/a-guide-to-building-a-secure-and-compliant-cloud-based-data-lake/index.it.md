---
title: "Creare un data lake sicuro e conforme al cloud: Le migliori pratiche per proteggere i dati archiviati"
date: 2023-04-16
toc: true
draft: false
description: "Questa guida completa illustra le best practice in materia di sicurezza e conformità per la pianificazione, la realizzazione e la gestione di data lake basati sul cloud."
tags: ["lago di dati", "sicurezza del cloud", "regolamenti di conformità", "controlli di accesso", "crittografia", "AWS", "Azzurro", "HIPAA", "GDPR", "monitoring", "rattoppare", "sicurezza informatica", "Soluzione SIEM", "Team di supporto IT", "panorama delle minacce", "migrazione in cloud", "governance del cloud"]
cover: "/img/cover/A_cartoon_image_of_a_castle_being_guarded_by_a_warrior.png"
coverAlt: "Un'immagine a fumetti di un castello sorvegliato da un cavaliere guerriero, che simboleggia il concetto di forte protezione per uno storage sicuro e conforme al cloud"
coverCaption: ""
---

**Guida alla creazione di un data lake sicuro e conforme al cloud**

Un data lake basato sul cloud è uno strumento prezioso per archiviare e analizzare grandi insiemi di dati. Tuttavia, presenta sfide di sicurezza uniche che devono essere affrontate per garantire la conformità alle normative governative. In questa guida, discuteremo le migliori pratiche per la creazione di un data lake sicuro e conforme al cloud.

## Pianificazione del lago di dati

Prima di iniziare a costruire un data lake, **è fondamentale creare un piano che tenga conto dei requisiti di sicurezza e conformità** della vostra organizzazione. Iniziate con la creazione di un framework che aderisca agli standard di settore, come il Regolamento generale sulla protezione dei dati (GDPR) o l'Health Insurance Portability and Accountability Act (HIPAA).

È importante scegliere il fornitore di cloud giusto, con una comprovata esperienza nella fornitura di soluzioni sicure in grado di soddisfare queste normative di conformità. Tra i fornitori di cloud più popolari vi sono Amazon Web Services (AWS), Microsoft Azure e Google Cloud Platform.

Inoltre, **definire chiari controlli di accesso** per utenti, ruoli e autorizzazioni. Questo include i membri del team interno e i fornitori o partner esterni che potrebbero richiedere l'accesso a volte.

## Costruire il lago di dati

Quando si costruisce un data lake, la **crittografia e i controlli di accesso devono essere implementati per progettazione** in tutte le fasi di movimento dei dati verso, all'interno e dal data lake. I processi di ingestione devono criptare i dati durante il transito e a riposo, ove possibile. Utilizzare le migliori pratiche, come i protocolli di sicurezza del livello di trasporto sul client di ingestione o i protocolli di rete, come il protocollo di trasferimento sicuro dei file (SFTP) o un servizio Apache Kafka gestito.

I client di ingestione o le applicazioni che copiano i dati da sistemi diversi devono utilizzare politiche di accesso basate sul principio del minimo privilegio: concedere solo le autorizzazioni necessarie per copiare le informazioni rilevanti da una fonte esterna.

Sul fronte dello storage, scegliere piattaforme che supportino la crittografia a riposo o forniscano altre funzioni di crittografia avanzata come la gestione delle chiavi, compresa la crittografia lato server con chiavi di proprietà del cliente (CMK).

**Un controllo rigoroso sull'accesso ai dati è fondamentale** e soluzioni come AWS Identity and Access Management o Azure Active Directory forniscono un mezzo efficace per controllare le autorizzazioni sia a livello di oggetto che di gestione.

## Monitoraggio e gestione del Data Lake

Un **monitoraggio accurato dell'infrastruttura del data lake aiuta a identificare le falle nella sicurezza** o le attività sospette che avvengono all'interno del data lake. **Implementate la registrazione di tutte le attività relative al data lake** archiviando i log dei dati in un account di audit separato per evitare la cancellazione o la manomissione da parte di malintenzionati. In questo modo è possibile rilevare rapidamente attività sospette, come la scansione delle porte, gli attacchi DDos, gli attacchi brute force o gli attacchi basati sulla rete.

Utilizzate una soluzione SIEM (Security Information and Event Management), come quella inclusa in AWS CloudTrail o Azure Monitor, per centralizzare la registrazione, automatizzare gli avvisi ed eseguire analisi avanzate.

Inoltre, assicuratevi che vengano eseguite **patching regolari dei componenti critici**. Gli aggiornamenti regolari dei pacchetti software per i sistemi sottostanti, come i sistemi operativi, i database, i server web o le librerie di terze parti, devono far parte del vostro modello di supporto per garantire che le vulnerabilità note siano risolte da team di supporto IT qualificati.

## Tenere il passo con l'evoluzione del panorama delle minacce

**A causa di un panorama di sicurezza in continua evoluzione, i controlli di sicurezza del cloud devono adattarsi rapidamente alle nuove minacce.

Se state cercando di conformarvi a normative specifiche che regolano l'archiviazione dei dati, adottate misure per mantenere questi requisiti di conformità attraverso audit di conformità e report regolari generati dai rispettivi servizi.

## Conclusione

L'implementazione di un data lake basato sul cloud offre vantaggi significativi, ma comporta anche un maggiore onere in termini di sicurezza e conformità. Tuttavia, seguire le best practice del settore, come la crittografia a riposo e in transito, la gestione dei controlli di accesso ad alto livello tramite Identity and Access Management (IAM), il monitoraggio dell'implementazione tramite log avanzati e l'impiego di patch costanti, vi aiuterà a costruire un data lake basato sul cloud sicuro e conforme.

Insieme al mantenimento di controlli appropriati per la migrazione e la governance del cloud, la vostra organizzazione può sfruttare tutti i vantaggi dei servizi basati sul cloud mantenendo la conformità e la sicurezza.

_______

## Riferimenti

1. [Guide to using AWS EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
2. [Microsoft - HIPAA overview](https://learn.microsoft.com/en-us/azure/compliance/offerings/offering-hipaa-us)
3. [What is SIEM?](https://www.varonis.com/blog/what-is-siem)
4. [AWS - Data ingestion methods](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-ingestion-methods.html)
5. [HIPAA Security Rule Standards and Implementation Specifications](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)
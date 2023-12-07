---
title: "Aumentare la sicurezza delle macchine virtuali con vTPM: Guida passo-passo"
date: 2023-09-02
toc: true
draft: false
description: "Migliorate la sicurezza delle macchine virtuali utilizzando vTPM con la nostra guida completa passo-passo, che fornisce l'attestazione della piattaforma e il supporto della crittografia BitLocker."
genre: ["Sicurezza informatica", "Virtualizzazione", "VMware", "vSphere", "Sicurezza", "Modulo di piattaforma affidabile", "vTPM", "Ospite OS", "Crittografia", "Attestazione della piattaforma"]
tags: ["Modulo piattaforma di fiducia virtuale", "Guida vTPM", "Maggiore sicurezza delle macchine virtuali", "Attestazione della piattaforma", "Crittografia BitLocker", "VMware vSphere", "Sicurezza della virtualizzazione", "Sicurezza informatica", "Protezione del sistema operativo guest", "Hardware VM", "TPM 2.0", "Avvio sicuro", "Operazioni crittografiche", "Migliori pratiche di sicurezza per le macchine virtuali", "Server vCenter", "Host ESXi", "Firmware EFI", "Fornitore chiave", "Documentazione VMware", "Server Windows", "Windows 7", "Sistema operativo Linux", "Configurazione sicura della macchina virtuale", "Caratteristiche di sicurezza", "Client vSphere", "Chip virtuale", "Protezione dei dati", "Rilevamento delle manomissioni", "Verifica dell'integrità della macchina virtuale", "Sicurezza VMware"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "Un'illustrazione simbolica che mostra una macchina virtuale con un lucchetto splendente, che rappresenta una maggiore sicurezza grazie a vTPM."
coverCaption: "Sbloccate una sicurezza VM senza precedenti!"
---

## Abilitazione del modulo di piattaforma attendibile virtuale per una macchina virtuale esistente

Il Virtual Trusted Platform Module (vTPM) è una funzionalità di sicurezza fondamentale che migliora la sicurezza dei sistemi operativi guest in esecuzione sulle macchine virtuali. Questo articolo vi guiderà attraverso il processo di aggiunta di un vTPM a una macchina virtuale esistente in un ambiente VMware vSphere, fornendo istruzioni passo dopo passo e considerazioni importanti per garantire un'implementazione senza problemi.

______

## Prerequisiti

Prima di procedere con l'aggiunta di un vTPM alla macchina virtuale, assicurarsi di soddisfare i seguenti prerequisiti:

1. **Assicurarsi che l'ambiente vSphere sia configurato per un provider di chiavi. Questo passaggio è fondamentale per gestire in modo sicuro le operazioni crittografiche. Consultare la sezione [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html) per una guida dettagliata.

2. **Verificare che il sistema operativo guest sia compatibile con vTPM. VMware vTPM è compatibile con TPM 2.0 e supporta Windows Server 2008 e successivi, Windows 7 e successivi e varie distribuzioni Linux.

3. **Stato della macchina virtuale:** Assicurarsi che la macchina virtuale da modificare sia spenta prima di procedere con l'aggiunta del vTPM.

4. **Gli host ESXi nel vostro ambiente devono eseguire ESXi 6.7 o successivo per il sistema operativo guest Windows o ESXi 7.0 Update 2 per il sistema operativo guest Linux.

5. **La macchina virtuale deve utilizzare il firmware EFI per il supporto vTPM.

6. **Verificare che si disponga dei privilegi necessari per le operazioni crittografiche per aggiungere e gestire il vTPM. I privilegi richiesti includono:
   - Operazioni crittografiche.Clona
   - Operazioni crittografiche.Crittografia
   - Operazioni crittografiche.Crittografa nuovo
   - Operazioni crittografiche.Migrare
   - Operazioni crittografiche.Registra VM



## Aggiunta del modulo di piattaforma attendibile virtuale (vTPM)

Seguite questi passaggi per aggiungere un vTPM alla macchina virtuale esistente:

1. **Connettersi a vCenter Server:** Avviare il client vSphere e accedere a vCenter Server.

2. **Aprire le impostazioni della macchina virtuale:** Individuare la macchina virtuale che si desidera modificare nell'inventario sul lato sinistro del vSphere Client. Fare clic con il tasto destro del mouse sul nome della macchina virtuale e selezionare "Modifica impostazioni".

3. **Nella finestra di dialogo "Modifica impostazioni", fare clic sul pulsante "Aggiungi nuovo dispositivo". Dall'elenco dei tipi di dispositivo, selezionare "Trusted Platform Module" (vTPM).

4. **Fare clic sul pulsante "OK" per aggiungere il dispositivo vTPM alla macchina virtuale.

5. **Dopo aver aggiunto con successo il vTPM, la scheda Riepilogo della macchina virtuale includerà ora "Virtual Trusted Platform Module" nel riquadro VM Hardware.

______

## Vantaggi del modulo di piattaforma affidabile virtuale (vTPM)

L'abilitazione di un vTPM per la macchina virtuale offre diversi vantaggi significativi:

1. **Il vTPM crea un chip TPM 2.0 virtualizzato per la macchina virtuale, fornendo funzioni di sicurezza basate sull'hardware come l'avvio sicuro e le operazioni crittografiche. Ciò rafforza la sicurezza del sistema operativo guest.

2. **vTPM permette alla macchina virtuale di generare una misura crittografica del proprio stato, consentendo l'attestazione della piattaforma. Questa funzione aiuta a verificare l'integrità della macchina virtuale, assicurando che non sia stata manomessa.

3. **Se si esegue un sistema operativo guest Windows, l'abilitazione della vTPM è un prerequisito per l'utilizzo della crittografia BitLocker sui dischi della macchina virtuale. Questo aggiunge un ulteriore livello di protezione dei dati.



## Conclusione

L'implementazione di un modulo di piattaforma attendibile virtuale (vTPM) per una macchina virtuale esistente è un passo fondamentale per rafforzare la sicurezza dell'infrastruttura virtualizzata. Seguendo la procedura descritta e assicurandosi che tutti i prerequisiti siano soddisfatti, è possibile attivare funzioni di sicurezza avanzate, l'attestazione della piattaforma e il supporto della crittografia BitLocker per i sistemi operativi guest.

Ricordate di consultare la documentazione ufficiale di VMware per i dettagli specifici relativi alla versione e alla configurazione di vSphere.

______

## Riferimenti

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)


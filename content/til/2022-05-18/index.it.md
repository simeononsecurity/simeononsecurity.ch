---
title: "Oggi ho imparato di più sulla creazione e l'attuazione delle politiche WDAC"
date: 2022-05-18
toc: true
draft: false
description: "Oggi ho imparato di più sui condizionali di Ansible e sulla gestione delle variabili"
genre: ["Automazione", "Sicurezza di Windows", "Controllo dell'applicazione", "Windows Defender", "WDAC", "Powershell", "Protezione dalle minacce", "Windows Server 2019", "Sicurezza aziendale", "Gestione delle politiche", "Migliori pratiche di sicurezza"]
tags: ["automazione", "WDAC", "controllo dell'applicazione", "Controllo applicazioni di Windows Defender", "Windows Defender", "Powershell", "Documentazione Microsoft", "Creazione della politica WDAC", "distribuzione delle politiche", "Distribuzione basata su script", "politiche multiple del WDAC", "dispositivi a carico fisso", "applicazioni affidabili", "negare le politiche", "pratiche di sicurezza", "gestione delle politiche", "sicurezza aziendale", "protezione dalle minacce", "Server Windows", "Sicurezza di Windows", "whitelist delle applicazioni"]
---

**Quello che SimeonOnSecurity ha imparato e trovato interessante oggi**

Oggi SimeonOnSecurity ha aggiornato il suo repository Windows-Defender-Application-Control-Hardening e ha scoperto Windows Defender Application Control (WDAC), una funzionalità di Windows 10 Enterprise e Windows Server 2019 che garantisce la sicurezza controllando ciò che viene eseguito su un dispositivo.

SimeonOnSecurity ha approfondito la documentazione Microsoft su WDAC e ha scoperto diverse risorse chiave per la creazione e la distribuzione dei criteri. Ha appreso come creare un criterio WDAC per i dispositivi a carico fisso utilizzando un computer di riferimento, come distribuire i criteri WDAC utilizzando uno script e come utilizzare più criteri per diversi scenari.

Inoltre, SimeonOnSecurity ha approfondito la guida alla creazione di criteri di negazione WDAC, che gli ha permesso di comprendere meglio il concetto di consentire l'esecuzione su un dispositivo solo alle applicazioni fidate, negando tutte le altre.

Nel complesso, l'esplorazione di Windows Defender Application Control da parte di SimeonOnSecurity ha ulteriormente rafforzato la sua comprensione dell'importanza del controllo delle applicazioni nelle moderne pratiche di sicurezza.

## Repos aggiornati:
- [simeononsecurity/Windows-Defender-Application-Control-Hardening](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening)

## Lettura WDAC:
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

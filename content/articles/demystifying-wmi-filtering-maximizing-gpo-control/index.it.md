---
title: "Capire il filtraggio WMI"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Scopri come usare il filtraggio WMI per indirizzare meglio gli oggetti Criteri di gruppo (GPO), con esempi pratici e buone pratiche."
genre: ["Gestione Windows", "Criteri di gruppo", "Amministrazione di sistema", "Gestione di rete", "Infrastruttura IT", "Gestione dei criteri", "Governance IT", "Automazione IT", "Active Directory", "Conformità di sicurezza"]
tags: ["filtraggio WMI", "GPO", "oggetti Criteri di gruppo", "filtri WMI", "targeting dei criteri", "query WMI", "Windows Management Instrumentation", "controllo GPO", "Console Gestione Criteri di gruppo", "linguaggio di query WMI", "applicazione dei criteri", "WQL", "ottimizzazione dei criteri", "gestione dei criteri", "risorse di sistema", "esempi di targeting dei criteri", "amministrazione di sistema", "gestione di rete", "gestione dell’infrastruttura IT", "automazione IT", "gestione di Active Directory", "conformità di sicurezza", "tecniche di controllo dei criteri", "buone pratiche di gestione dei criteri", "filtraggio dei criteri", "strategie di controllo GPO", "sicurezza GPO", "vantaggi del filtraggio WMI", "implementazione del filtraggio WMI", "buone pratiche per i filtri WMI"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Illustrazione di una lente d’ingrandimento puntata su un’icona di filtro, che rappresenta il targeting delle GPO tramite filtraggio WMI."
coverCaption: "Usa il filtraggio WMI per indirizzare in modo efficiente i criteri GPO!"
---

## Introduzione

Negli oggetti Criteri di gruppo (GPO), il [**filtraggio WMI**](https://simeononsecurity.com/github/wmi-filters/) controlla quali computer o utenti ricevono i criteri in base ai risultati delle query WMI (Windows Management Instrumentation). Questa funzione consente agli amministratori di affinare il targeting e applicare i criteri solo ai destinatari desiderati. In questo articolo vedremo cos’è il filtraggio WMI, come funziona nelle GPO, come creare [filtri WMI](https://simeononsecurity.com/github/wmi-filters/) e alcuni esempi pratici.

## [Che cos’è il filtraggio WMI?](https://simeononsecurity.com/github/wmi-filters/)

Il [**filtraggio WMI**](https://simeononsecurity.com/github/wmi-filters/) applica filtri alle GPO in base ai risultati delle query WMI. WMI è un’infrastruttura di gestione integrata nei sistemi operativi Windows. Consente agli amministratori di recuperare dati di gestione e interagire in modo programmatico con le risorse di sistema. Con il filtraggio WMI, gli amministratori possono indirizzare dinamicamente le GPO in base a criteri definiti dalle query.

I filtri WMI sono scritti con il linguaggio di query WMI (WQL), un sottoinsieme di SQL (Structured Query Language). In genere si basano su proprietà e valori disponibili in uno spazio dei nomi WMI. Gli amministratori possono combinare condizioni, operatori logici e spazi dei nomi per creare query WMI che individuano computer o utenti specifici.

## Come funziona il filtraggio WMI nelle GPO?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Diagramma di flusso in cui un filtro WMI collegato a un oggetto Criteri di gruppo valuta una query WQL come True o False per decidere se applicare la GPO a un computer" >}}

In Criteri di gruppo, il **filtraggio WMI** consente di applicare le GPO in modo selettivo in base alla valutazione di **query WMI**. Associando un **filtro WMI** a una GPO, il risultato **True** o **False** del filtro determina se la GPO viene applicata.

I filtri WMI usano il **linguaggio di query WMI (WQL)**, un sottoinsieme di SQL (Structured Query Language). WQL consente di creare query complesse che considerano diverse **proprietà** e **valori** disponibili nello **spazio dei nomi WMI**. Questo permette di indirizzare computer o utenti specifici.

Per esempio, un’organizzazione potrebbe voler applicare una GPO soltanto ai computer con Windows 10. Può creare un filtro WMI che controlla la proprietà **OperatingSystem** della classe **Win32_OperatingSystem**. La query WMI potrebbe essere:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

La query verifica se la versione del sistema operativo inizia con «10.», indicando Windows 10. Se il risultato è **True**, la GPO viene applicata al computer di destinazione. In caso contrario, non viene applicata.

Il filtraggio WMI supporta anche condizioni e operatori logici come **AND**, **OR** e **NOT**. Gli amministratori possono combinare più proprietà e valori per controllare con maggiore precisione l’applicazione delle GPO.

È inoltre possibile usare diversi **spazi dei nomi WMI** per accedere a insiemi specifici di classi e proprietà WMI. Questa flessibilità consente di indirizzare le GPO in base alla configurazione hardware, al software installato, alle impostazioni di rete e ad altri criteri.

Per approfondire la creazione di filtri e query WMI, consulta la documentazione Microsoft sul [filtraggio WMI per Criteri di gruppo](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

Con il filtraggio WMI, gli amministratori possono adattare l’applicazione delle GPO a computer o utenti in base a condizioni dinamiche e migliorare la gestione dell’ambiente IT.

## Creare filtri WMI per le GPO

Per creare un filtro WMI per una GPO, segui questi passaggi:

1. Apri la **Console Gestione Criteri di gruppo** (GPMC) su un computer Windows aggiunto al dominio.

2. Espandi il dominio e apri il nodo **Filtri WMI**.

3. Fai clic con il pulsante destro su **Filtri WMI** e seleziona **Nuovo**.

4. Assegna al filtro un nome descrittivo e inserisci la query WMI nel campo **Query**. Usa la sintassi WQL.

5. Fai clic su **OK** per salvare il filtro WMI.

Dopo aver creato il filtro, puoi associarlo a una o più GPO. Per collegarlo a una GPO:

1. Fai clic con il pulsante destro sulla GPO desiderata e seleziona **Proprietà**.

2. Nella finestra delle proprietà della GPO, apri la scheda **Filtraggio WMI**.

3. Seleziona dall’elenco il filtro WMI desiderato.

4. Fai clic su **OK** per salvare le modifiche.

Associando i filtri WMI alle GPO, puoi indirizzare con precisione l’applicazione dei criteri in base ai risultati delle query WMI.

## Quanti filtri WMI si possono configurare per una GPO?

Gli amministratori possono configurare **più filtri WMI** per una GPO, così da ottenere un targeting preciso dei criteri. Non esiste un limite specifico al numero di filtri associabili a una singola GPO, quindi sono possibili combinazioni complesse.

Occorre però considerare l’effetto del numero di filtri sui tempi di elaborazione delle GPO. All’aumentare dei filtri, può aumentare anche il tempo necessario per valutarli e applicare le GPO. Per mantenere efficiente l’applicazione dei criteri, è consigliabile limitare il numero di filtri a una quantità ragionevole.

Per esempio, un’organizzazione potrebbe voler applicare una GPO solo ai computer con Windows 10 e uno specifico software installato. Può creare due filtri WMI distinti: uno per il **sistema operativo** e uno per **l’installazione del software**. Combinandoli, individua i computer desiderati.

È necessario trovare un equilibrio tra i filtri richiesti per soddisfare le esigenze di targeting e i tempi di elaborazione. Prima di scegliere quanti filtri configurare, gli amministratori dovrebbero valutare la complessità dell’ambiente, il numero di computer o utenti e le conseguenze sulle prestazioni.

La possibilità di configurare più filtri WMI aiuta a ottimizzare il targeting delle GPO e a mantenere efficiente l’elaborazione e la gestione dell’ambiente IT.

## Esempi pratici di filtraggio WMI nelle GPO

Il filtraggio WMI offre soluzioni pratiche per applicare le GPO ai destinatari previsti. Ecco alcuni esempi:

1. **Targeting di sistemi operativi specifici**: per applicare una GPO solo ai computer con **Windows 10**, crea un filtro che verifica la versione del sistema operativo, ad esempio `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. In questo modo selezioni i computer Windows 10.

2. **Criteri diversi per desktop e portatili**: se hai criteri distinti per computer desktop e portatili, puoi usare due filtri WMI. Un filtro può individuare i desktop tramite attributi hardware, ad esempio `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, mentre l’altro distingue i portatili. Così puoi applicare criteri adatti a ciascun tipo di dispositivo.

3. **Applicazione selettiva in base allo spazio su disco**: per evitare criteri che richiedono molte risorse sui computer con poco spazio, crea un filtro WMI che verifica lo spazio disponibile. Per esempio, la query `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` esclude i computer con meno di 10 GB liberi.

Questi esempi mostrano la flessibilità del **filtraggio WMI** nelle GPO e permettono agli amministratori di indirizzare l’applicazione dei criteri secondo criteri specifici.

## Conclusione

Il filtraggio WMI è una funzione utile degli oggetti Criteri di gruppo. Permette agli amministratori di applicare i criteri in modo selettivo in base ai risultati delle query WMI. I filtri WMI indirizzano con precisione i criteri verso computer o utenti specifici, rendendo la gestione più efficiente e controllata. In questo articolo abbiamo esaminato il concetto, il funzionamento nelle GPO, la creazione dei filtri e alcuni esempi pratici.

Integrando il filtraggio WMI nella gestione delle GPO, migliori la precisione dell’applicazione dei criteri e fai in modo che vengano applicati solo ai destinatari previsti.

## Riferimenti

- [Microsoft Docs: creare filtri WMI per la GPO](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Criteri di gruppo](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Console Gestione Criteri di gruppo](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))

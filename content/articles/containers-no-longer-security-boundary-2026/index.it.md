---
title: "I container non sono più un confine di sicurezza: le evasioni dal kernel nel 2026"
date: 2026-09-28
lastmod: 2026-11-13
toc: true
draft: false
description: "Esamina la ricerca del 2026 sulle evasioni dai container, i limiti dell'isolamento del kernel, la pressione sulle patch e il ruolo delle microVM."
genre: ["Sicurezza dei container", "Linux", "Sicurezza del kernel", "Virtualizzazione", "Sicurezza cloud", "Ricerca sulle minacce", "Blue team", "DevSecOps"]
tags: ["evasione dal container", "confine di sicurezza dei container", "CVE del kernel Linux", "escalation locale dei privilegi", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "microVM", "Firecracker", "Kata Containers", "corruzione della page cache", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "isolamento dei namespace", "system call clone", "rilevamento delle vulnerabilità con AI", "sicurezza Docker", "sicurezza Kubernetes", "isolamento multi-tenant", "evasione dal sandbox", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "tendenza delle CVE del kernel"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "Illustrazione digitale di vari container luminosi collegati a un simbolo centrale del kernel. Elementi colorati rappresentano vulnerabilità che si irradiano dal kernel su uno sfondo scuro."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---
**I container condividono un unico kernel. Nel 2026 quattro famiglie distinte di vulnerabilità hanno dimostrato che basta un solo bug del kernel per uscire da un container e raggiungere l'host.** Copy Fail, Dirty Frag, Fragnesia e CVE-2026-80521 assegnano i privilegi di root a un utente locale non privilegiato. Tutte superano il confine del container.

*La parte scomoda non sono i bug in sé. È il costo sempre più basso con cui l'AI li trova e il fatto che una patch abbia creato un nuovo bug.*

Questo articolo spiega come i container isolano i carichi di lavoro, perché oggi l'isolamento poggia su fondamenta sempre più limitate, cosa fa ogni vulnerabilità del 2026 e quale tecnologia di isolamento conviene usare.

**Risultato per il lettore:** mappa chi fornisce il codice per ogni carico di lavoro, identifica le funzioni del kernel necessarie e scegli tra container rafforzati e un confine basato su microVM. Considera i casi di studio del 2026 come prove di ricerca datate. Controlla gli avvisi aggiornati dei fornitori prima di cambiare un kernel di produzione.

## La risposta breve

| Domanda | Risposta breve |
|---|---|
| **I container isolano?** | Sì, per processi e file system. Tutti condividono un kernel, quindi i bug del kernel sono un rischio comune |
| **Perché proprio adesso?** | L'AI ha ridotto il costo della ricerca di difetti nel kernel. A settembre 2026 risultano pubblicate quasi **6.000 CVE del kernel** |
| **Cosa supera il confine?** | Qualsiasi escalation locale dei privilegi nel kernel. L'evasione non richiede una configurazione errata del container |
| **Basta applicare le patch?** | È necessario, ma la velocità non basta più. Una patch del 2026 **ha introdotto un nuovo bug sfruttabile** |
| **Cosa funziona meglio?** | MicroVM come Firecracker o Kata Containers, che assegnano un kernel separato a ogni carico di lavoro |
| **L'alternativa è perfetta?** | No. Anche l'hypervisor è codice. La superficie di attacco è inferiore di molti ordini di grandezza, e la differenza conta |

## Come isolano i container

Per capire il confine, occorre capire cosa non è un container.

**Un container non è una macchina virtuale.** Tra il processo e l'hardware non ci sono un secondo kernel, hardware emulato o un hypervisor. Quando esegui un'immagine container, avvii un processo sul kernel esistente con una vista modificata del sistema.

Il meccanismo è la **system call `clone`**. Mentre `fork` copia lo spazio degli indirizzi di un processo, `clone` crea un processo figlio e dà al chiamante un controllo preciso su quali parti del contesto di esecuzione condividere e quali sostituire. Docker passa a `clone` un insieme di **namespace**:

| Namespace | Cosa simula |
|---|---|
| **Mount** | Una radice privata del file system, così il container vede il proprio albero invece del tuo |
| **PID** | Una numerazione dei processi separata, quindi `PID 1` è il primo processo del container, non `systemd` |
| **User** | Una mappatura delle identità in cui il "root" del container corrisponde a un utente host non privilegiato |
| **Network** | Interfacce, tabelle di routing e porte private |
| **IPC** | Memoria condivisa e code di messaggi isolate |
| **UTS** | Il proprio nome host e nome di dominio |
| **Cgroup** | Una vista privata dei limiti delle risorse |

Aggiungi un **file system union** sopra un'immagine e il risultato *sembra* un computer separato. `id` nel container restituisce `uid=0(root)`. Il file system sembra un'installazione minima di Ubuntu. L'elenco dei processi mostra soltanto i processi del container.

**A livello di system call, nulla di tutto questo è un confine di sicurezza.** Quando un processo nel container apre un file, alloca memoria o tocca un socket di rete, lo stesso kernel gestisce la richiesta per ogni container sull'host. I namespace cambiano *ciò che il processo vede*, non *ciò che il kernel farà per lui*.

*Il kernel è il vero confine tra container e host. Tutto il resto è presentazione.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Diagramma di tre container costruiti sullo stesso kernel. I namespace mount, PID, user e network separano le rispettive viste, mentre tutte le system call continuano a raggiungere un unico kernel condiviso." >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## Il confine è codice e il codice contiene bug

Ogni azione di un container passa dall'**interfaccia delle system call**. Aprire un file, leggere la memoria, scrivere su un socket, cambiare un UID: il kernel media tutto, perché non vuole che i processi tocchino direttamente CPU, file system o rete.

La mediazione è il modello di sicurezza, e la mediazione è implementata nel codice. Si tratta di circa **30 milioni di righe**.

Un'escalation locale dei privilegi (LPE) si verifica quando un processo sfrutta un difetto nel codice di mediazione per ottenere privilegi mai concessi. **Le LPE non sono una novità.** Esistono dai primi meccanismi di mediazione del kernel e per decenni il settore ha convissuto con un flusso costante ma contenuto.

**Dirty Pipe del 2022** è il riferimento noto a molti. Sfruttava un difetto nella gestione dei pipe buffer per sovrascrivere file di sola lettura. Fece notizia perché bug di questa gravità comparivano **all'incirca ogni uno o due anni**. Si applicava la patch, si riprendeva il lavoro e si dava per scontato che non ci fossero grandi difetti ancora nascosti nel codice letto da un milione di persone.

*Questa ipotesi non regge più.*

## Cosa è cambiato nel 2026

Il cambiamento non riguarda la bravura degli attaccanti. **Trovare bug di corruzione della memoria nel kernel è diventato un'attività ingegneristica invece che una carriera di ricerca.**

Tre dati di quest'anno rendono concreto il cambiamento:

| Vulnerabilità trovata | Chi l'ha trovata | Come |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Con l'aiuto di **Xint Code**, uno strumento di analisi statica basato sull'AI. Circa **un'ora di scansione** del sottosistema crittografico Linux |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Trovata con **dfs-large1**, un modello AI interno addestrato per rilevare vulnerabilità |
| **CVE-2026-80521**, indipendentemente | Kyle, **OpenAI** | Lo stesso bug, trovato separatamente e segnalato lo stesso giorno |

Rileggi la terza riga. Due organizzazioni che usavano strumenti AI diversi hanno trovato **lo stesso use-after-free di AF_UNIX** e lo hanno segnalato a `security@kernel.org` **lo stesso giorno**. Non è una coincidenza di talento. Un processo ripetibile ha prodotto due volte la stessa risposta.

DepthFirst indica direttamente la portata: **quasi 6.000 CVE del kernel erano pubblicate a settembre 2026**. Il conteggio cresce in linea con la disponibilità dell'AI, non con il numero di sviluppatori del kernel.

*Quando un'ora di scansione AI trova un bug decennale nel sottosistema crittografico, l'economia dello sfruttamento del kernel si è capovolta.*

## Quattro evasioni in un anno

Ognuna di queste vulnerabilità consente di ottenere root da un account locale non privilegiato. Nessuna richiede una configurazione errata del container, un flag privileged o un accesso iniziale dalla rete.

| Vulnerabilità | CVE | Sottosistema | Primitiva | Scoperta da |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | Scrittura di 4 byte nella page cache di qualsiasi file leggibile | Theori, con AI |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | Scrittura di 4 byte nella page cache tramite due varianti concatenate | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP | Scritture di singoli byte nella page cache | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | Socket AF_UNIX | Use-after-free nel garbage collection di `unix_vertex` | DepthFirst, con AI |

Tutte e quattro condividono un modello che merita attenzione. **Attaccano la page cache, non il disco.**

### Copy Fail: un difetto logico senza race

Copy Fail è la più semplice delle quattro ed è la più allarmante.

Quasi tutte le LPE Linux richiedono una finestra temporale o un offset di memoria specifico del kernel. **Copy Fail non richiede né l'una né l'altro.** È un difetto logico lineare in `algif_aead`, il modulo che fornisce ai processi utente l'accesso alla cifratura autenticata tramite AF_ALG.

La catena usa `splice()` per inserire una pagina della page cache nell'operazione, poi sfrutta il percorso AEAD in-place per scrivere **quattro byte controllati** in quella pagina. La pagina corrotta **non viene mai contrassegnata come dirty**, quindi non viene mai riscritta sul disco. Il file su disco resta intatto, perciò i controlli di checksum e integrità passano anche se la copia in memoria contiene la modifica.

Un **programma Python di 732 byte** ottiene root su ogni distribuzione Linux rilasciata dal 2017. Il bug fu introdotto da un'**ottimizzazione del 2017** in `algif_aead`; la patch del 2026 si limita a rimuoverla. Commit mainline `a664bf3d603d`.

*Il bug è rimasto in ogni distribuzione principale per quasi un decennio. Uno strumento AI l'ha trovato in circa un'ora.*

### Dirty Frag: due varianti che si completano a vicenda

Il nome Dirty Frag ne descrive con precisione la parentela. **Dirty Pipe sovrascrive `struct pipe_buffer`. Dirty Frag sovrascrive il campo `frag` di `struct sk_buff`.**

Sono **due vulnerabilità concatenate**, ed è proprio questa concatenazione la parte intelligente:

- **CVE-2026-43284** sfrutta `esp_input()` che salta il percorso copy-on-write prima di eseguire la decrittazione in-place su un frammento inserito con splice. Richiede il privilegio di creare uno **user namespace**, limitato da alcune distribuzioni.
- **CVE-2026-43500** sfrutta `rxkad_verify_packet_1()` che esegue una decrittazione in-place sul frammento. Non richiede privilegi per gli namespace, ma il modulo `rxrpc` manca nella maggior parte delle distribuzioni. Ubuntu lo carica per impostazione predefinita.

**Ogni variante, da sola, ha un punto cieco. Insieme si completano.** Se gli user namespace sono consentiti, agisce prima il percorso ESP. Se è bloccato ma `rxrpc` è presente, agisce il percorso RxRPC. Un solo eseguibile funziona quindi su diverse distribuzioni. La variante RxRPC ottiene root azzerando un campo in `/etc/passwd` e lasciando che PAM con `nullok` accetti una password vuota.

**Il dato più importante per chi difende:** Dirty Frag funziona **indipendentemente dalla disponibilità di `algif_aead`**. La diffusa mitigazione di Copy Fail che blocca il modulo **non protegge affatto da Dirty Frag**.

### Fragnesia: la patch che ha creato un bug

Fragnesia appartiene alla stessa classe di Dirty Frag, ma attacca il percorso XFRM **ESP-in-TCP**. È il caso più istruttivo del gruppo.

La vulnerabilità sfrutta una gestione errata dei frammenti di pagina condivisi durante la coalescenza di `skb`. Un attaccante inserisce pagine supportate da file nella coda di ricezione TCP con `splice()`, prima che il socket passi alla modalità di protocollo di livello superiore `espintcp`. Quando ESP si attiva, il kernel decritta i dati accodati **in-place** e la manipolazione del keystream AES-GCM corrompe la page cache. L'attaccante ottiene **scritture ripetute di un singolo byte** nelle pagine dei file in cache.

L'exploit ottiene root sovrascrivendo i primi byte di `/usr/bin/su` con un piccolo payload ELF. **La modifica esiste solo in memoria e non tocca mai il binario su disco.**

Gli **user e network namespace** non privilegiati forniscono `CAP_NET_ADMIN` all'interno di uno namespace isolato; poi `NETLINK_XFRM` installa una security association preparata ad hoc.

*Fermati su questa frase:* Fragnesia è emersa come **effetto collaterale involontario di una delle patch per le vulnerabilità Dirty Frag originali**. La correzione di Dirty Frag ha prodotto un nuovo bug root sfruttabile in modo indipendente.

### CVE-2026-80521: l'evasione dal container che ha vinto kernelCTF

La race di AF_UNIX chiude ogni discussione sul fatto che sia solo teorica.

La vulnerabilità è un **heap use-after-free** nel garbage collector dei messaggi `SCM_RIGHTS`, che i processi usano per passarsi i file descriptor. Durante la raccolta di un riferimento circolare a un socket, una race libera `struct unix_vertex` mentre l'anello SCC di un socket sopravvissuto conserva ancora un puntatore all'oggetto. Il passaggio di raccolta successivo percorre l'anello obsoleto e dereferenzia memoria liberata.

Il motivo per cui conta oltre Linux in generale: **AF_UNIX è alla base dell'IPC locale.** Database locali, `systemd` e Docker stesso dipendono da AF_UNIX. DepthFirst segnala che la vulnerabilità colpisce la maggior parte dei sandbox a livello di sistema operativo basati sul kernel, **inclusi `nsjail`, `Firejail` e `Bubblewrap`**, oltre ai runtime container moderni.

DepthFirst ha ottenuto **uno slot Google kernelCTF** con questo bug il **24 luglio 2026**, ha ricevuto conferma nello slot `lts-6.12.95` il **5 agosto**, l'ha segnalato a `security@kernel.org` quello stesso giorno e ha scoperto che **Kyle di OpenAI aveva segnalato lo stesso bug**. La patch upstream è arrivata il **6 agosto**. La ricerca è stata pubblicata il **22 settembre**.

Il gruppo ha rilasciato un exploit funzionante per **Ubuntu 26.04** e un secondo exploit per evadere da **Ubuntu 24.04** tramite CVE-2026-52910.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Diagramma di un processo non privilegiato dentro un container che corrompe una pagina della page cache per modificare in memoria un binario setuid. Il processo ottiene root e supera il confine del container fino al kernel host." >}}

## Perché i consigli di mitigazione continuano a fallire

Quest'anno chi difende ha ricevuto tre serie di workaround, e ciascuna era in parte errata.

| Mitigazione | Cosa blocca | Cosa non risolve |
|---|---|---|
| Bloccare **`algif_aead`** | Copy Fail | **Nulla di Dirty Frag**, che ignora completamente il modulo |
| Bloccare **`esp4`, `esp6` e `rxrpc`** | Dirty Frag e Fragnesia | I team che hanno bisogno di IPsec. Inoltre non copre nuovi sottosistemi |
| Limitare gli **user namespace non privilegiati** | Le varianti ESP | La variante RxRPC non richiede uno namespace. La policy AppArmor è solo una mitigazione **parziale** |
| **Applicare la patch al kernel** | Il bug corretto | Il bug successivo e quelli introdotti da una patch |

Emergono due modelli.

**Primo, i workaround sono in conflitto.** Copy Fail si mitiga disabilitando `algif_aead`. Dirty Frag si attiva **anche quando** il modulo è assente. Fragnesia richiede di disabilitare `esp4` e `esp6`, un problema per chi usa IPsec. Non esiste una singola blacklist di moduli che copra l'intera famiglia.

**Secondo, e peggio, applicare patch non è una vittoria sicura.** Fragnesia è stata **introdotta dalla patch per Dirty Frag**. Ogni patch può portare nuovi errori logici e, in questo sottosistema, un errore logico diventa un exploit root.

*La conclusione scomoda: tutte queste vulnerabilità sono nella page cache, raggiungibili da codice non privilegiato e trovate con strumenti che migliorano ogni trimestre. Nessuna blacklist resta completa.*

## La controargomentazione, affrontata con onestà

C'è un'obiezione legittima a cui dare una risposta diretta: **anche gli hypervisor hanno bug.**

La superficie di attacco KVM è reale. Google gestisce **kvmCTF** proprio per trovare questi bug e offre premi consistenti:

| Livello | Ricompensa |
|---|---|
| **Evasione completa dalla VM** | **$250,000** |
| Scrittura arbitraria in memoria | $100,000 |
| Lettura arbitraria della memoria | $50,000 |
| Scrittura relativa in memoria | $50,000 |
| Negazione del servizio | $20,000 |
| Lettura relativa della memoria | $10,000 |

I premi non si sommano. Il bersaglio è un kernel Linux LTS con KVM, il guest è Debian 12.5. L'obiettivo è un **attacco dal guest all'host**.

**Hyunwoo Kim, lo stesso ricercatore che ha trovato Dirty Frag, raccoglie anche premi KVM** e ha vinto i $250,000 per un'evasione completa dalla VM. La sintesi onesta è che entrambe le componenti hanno difetti e che a volte li trova la stessa persona.

**Ma confronta le dimensioni:**

| | Kernel Linux | Hypervisor KVM |
|---|---|---|
| **CVE nel 2026** | Quasi **6.000** | Poche, con singoli ricercatori che ne trovano alcune ogni anno |
| **Raggiungibile da** | Qualsiasi processo non privilegiato tramite l'interfaccia delle system call | Solo codice già in esecuzione dentro un guest |
| **Superficie di attacco** | Tutto: rete, file system, crittografia, IPC, driver | Interfaccia dei dispositivi virtuali e hypercall |
| **Classe di bug** | Qualsiasi difetto di memoria o logica in 30 milioni di righe | Limitata al confine della virtualizzazione |

*La differenza è di molti ordini di grandezza, non un fattore due. È per questo che le microVM cambiano il calcolo del rischio.*

## Cosa offre un confine reale

Una **microVM** fornisce a ogni carico di lavoro una propria **istanza del kernel**, in esecuzione su virtualizzazione imposta dall'hardware, invece di condividere il kernel host tramite namespace.

Lo stack ha tre livelli da conoscere:

- **La CPU** fornisce meccanismi hardware per isolare regioni di memoria.
- **KVM** espone questi meccanismi al kernel Linux, che opera così come hypervisor.
- **Una VMM (virtual machine monitor)**, come Firecracker o QEMU, controlla KVM per creare ed eseguire il guest.

Poiché il guest esegue un proprio kernel, un exploit del kernel **dentro il guest** compromette solo il guest. Non c'è un kernel condiviso da attaccare. L'attaccante dovrebbe poi evadere dall'hypervisor, la superficie più piccola in cui si trovano i bug KVM.

Nella pratica contano due implementazioni, entrambe citate nelle raccomandazioni DepthFirst:

| Tecnologia | Approccio | Note |
|---|---|---|
| **Firecracker** | VMM progettata appositamente, con modello dei dispositivi minimo | Realizzata da AWS per l'isolamento multi-tenant su larga scala |
| **Kata Containers** | Runtime compatibile OCI che racchiude una microVM | Esegue immagini container standard con un confine VM sottostante |

Per la maggior parte dei team Kata è la migrazione più semplice, perché accetta le immagini e gli strumenti container già in uso. **Firecracker ha una superficie di attacco più piccola**, perché emula molti meno dispositivi di una VMM generica.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Diagramma che confronta l'isolamento dei container tramite namespace su un kernel condiviso con quello delle microVM, dove ogni carico di lavoro esegue un proprio kernel sopra KVM e un virtual machine monitor." >}}

## Cosa fare adesso

Non tutti i container richiedono una microVM. La scelta dipende da **chi esegue il codice al loro interno**.

| Situazione | Rischio | Azione |
|---|---|---|
| **Esegui codice tuo**, single tenant | Basso | Mantieni i container. Applica subito le patch, rimuovi le capability e usa un file system root in sola lettura |
| **Host multi-tenant**, accesso shell per utenti | **Alto** | Sposta i carichi di lavoro non attendibili nelle microVM. È il primo caso indicato da DepthFirst |
| **Runner CI che eseguono PR non attendibili** | **Alto** | Una pull request può diventare root sul runner. Isola ogni job nella propria VM |
| **Notebook, sandbox per agenti e serverless** | **Alto** | Il codice del tenant diventa root sull'host. Una microVM per tenant |
| **Cluster Kubernetes** | **Elevato** | La page cache è condivisa sull'host. Un pod con le primitive corrette compromette il nodo e supera i confini tra tenant |

Il principio comune è semplice. **I container sono ottimi per packaging e isolamento dei processi.** Non sono mai stati progettati per contenere codice ostile; il settore li ha usati silenziosamente per questo scopo perché erano comodi ed economici.

### Rafforzamenti sempre utili

Nessuna di queste misure sostituisce un confine VM, ma tutte eliminano percorsi d'attacco facili:

```bash
# Disabilita i moduli sfruttati dalla famiglia page-cache quando non servono
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Limita gli spazi dei nomi utente non privilegiati, bloccando le varianti ESP
# Debian e Ubuntu: è una mitigazione parziale, non completa
sysctl -w kernel.unprivileged_userns_clone=0

# Se si sospetta uno sfruttamento, svuota la cache delle pagine per scartare i binari modificati in memoria
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Segnali iniziali di rilevamento
- Uso inatteso di unshare(CLONE_NEWUSER) da un carico di lavoro senza un motivo legittimo
- Attività NETLINK_XFRM o associazioni di sicurezza XFRM fuori dagli host IPsec
- Richieste di collegamento di socket AF_ALG
- Caricamento di esp4, esp6 o rxrpc su host senza IPsec né AFS
```

> **Avviso: `drop_caches` scarta la copia modificata in memoria e rimuove la corruzione, ma non elimina un attaccante che ha già ottenuto root. Trattalo come risposta agli incidenti, non come rimedio.**

### Il problema della cadenza delle patch

Anche con le migliori intenzioni, applicare patch al kernel è diventato una corsa:

- Quasi **6.000 CVE** pubblicate quest'anno superano per volume la maggior parte delle finestre di manutenzione.
- **Una patch introduce un bug.** Fragnesia l'ha dimostrato proprio in questo sottosistema.
- **L'elenco delle mitigazioni scade.** Ad aprile la risposta era `algif_aead`. A maggio non copriva più nulla in Dirty Frag.

*Applicare le patch rapidamente è necessario e insufficiente. L'architettura decide se una patch mancata comporta un incidente contenuto o la compromissione dell'host.*

## La domanda più difficile: chi è l'avversario?

La risposta tecnica è chiara. Quella strategica dipende da una domanda che molti team saltano.

**Se il tuo modello di minaccia comprende un utente curioso o uno sviluppatore distratto, i container restano adeguati.** Un'evasione richiede l'esecuzione di codice locale e un exploit del kernel. Nessuna delle due è banale, e i costi operativi per trasferire tutto alle microVM sono reali.

**Se il tuo modello di minaccia comprende un avversario che esegue codice sulla tua infrastruttura, oggi i container sono solo un rallentatore.** Vale la pena citare direttamente la conclusione di DepthFirst:

> "La barriera d'ingresso per trasformare queste vulnerabilità in armi è scesa così tanto che dobbiamo presumere che gli attaccanti possano evadere dai container standard a piacimento."

È un fornitore di sicurezza con un prodotto da vendere che sostiene una specifica architettura, e lo scetticismo è giustificato. **L'argomento, però, non dipende dal fornitore.** Il conteggio di 6.000 CVE è pubblico, gli exploit sono stati pubblicati e il kernel è condiviso per progetto.

*La formulazione onesta: il valore dei container come confine diminuisce contro un attaccante già presente, ma resta invariato contro tutto il resto.*

## Il verdetto

**I container restano lo strumento giusto per packaging, deployment e separazione dei processi. Non sono più un confine di sicurezza affidabile contro codice ostile.**

Tre affermazioni, ordinate per livello di certezza:

1. **La premessa tecnica è assodata.** I container condividono il kernel host. Tutte e quattro le vulnerabilità di questo articolo hanno superato il confine da un account non privilegiato e gli exploit sono pubblici.
2. **L'AI ha cambiato il ritmo, non il principio.** Le LPE del kernel sono sempre esistite. Ora trovarne una costa circa **un'ora di scansione AI** invece di mesi di lavoro esperto e due organizzazioni hanno scoperto in modo indipendente lo stesso zero-day lo stesso giorno.
3. **La migrazione ha un costo, così come non migrare.** Firecracker e Kata comportano overhead, complessità operativa e nuove competenze. La scelta è semplice: accetta l'overhead oppure accetta che un bug del kernel comprometta l'host.

**Se gestisci infrastruttura multi-tenant o esegui codice non attendibile, pianifica ora la migrazione alle microVM.** Non perché il cielo stia crollando, ma perché la traiettoria è chiara e la migrazione richiede trimestri, non settimane.

**Se esegui container single-tenant con codice tuo, mantienili.** Applica le patch al kernel più rapidamente, disabilita i moduli che non servono e rivedi la decisione quando entra in gioco codice non attendibile.

*L'era in cui il kernel era considerato un confine affidabile senza condizioni sta finendo. Un'infrastruttura che presume che il kernel verrà violato è un'infrastruttura che sopravvive alla violazione.*

## Punti chiave

- **I container condividono il kernel host.** L'isolamento deriva dai namespace della system call `clone`, non dalla virtualizzazione hardware: un bug del kernel è anche un bug del container.
- **Quattro vulnerabilità del 2026 hanno superato il confine** da account locali non privilegiati: Copy Fail, Dirty Frag, Fragnesia e CVE-2026-80521. Tutte attaccano la page cache.
- **A settembre 2026 erano pubblicate quasi 6.000 CVE del kernel**, accelerate dagli strumenti AI. **Copy Fail è stata trovata in circa un'ora di scansione.**
- **Fragnesia è stata introdotta dalla patch per Dirty Frag.** Una patch ha creato un nuovo bug root nello stesso sottosistema.
- **Il workaround per Copy Fail non blocca Dirty Frag.** Bloccare `algif_aead` copre una vulnerabilità e nessun'altra della famiglia.
- **CVE-2026-80521 ha compromesso anche `nsjail`, `Firejail` e `Bubblewrap`**, non solo i runtime container.
- **Le microVM cambiano il calcolo del rischio** fornendo a ogni carico di lavoro un kernel proprio. KVM ha bug, ma la superficie di attacco è inferiore di molti ordini di grandezza.
- **Scegli in base a chi esegue il codice.** Codice tuo in un container single-tenant comporta un rischio basso. Codice non attendibile su un host condiviso comporta un rischio di compromissione dell'host.

## Prossimi passi

1. **Leggi l'analisi che inquadra il problema** e l'exploit pubblicato: **[I container non sono più un confine di sicurezza - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Consulta l'avviso autorevole e le mitigazioni** per la famiglia Copy Fail: **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Leggi l'analisi tecnica di Dirty Frag** per capire la concatenazione e perché la mitigazione `algif_aead` non funziona: **[Analisi tecnica di Dirty Frag](https://github.com/V4bel/dirtyfrag)**
4. **Consulta le regole e i premi di kvmCTF** per valutare la superficie di attacco dell'hypervisor: **[Panoramica di kvmCTF](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Valuta queste CVE nel tuo ambiente** con il nostro strumento lato client: **[Calcolatore CVSS v3.1](/cvss-calculator/)**
6. **Rafforza ciò che esegui ora**: **[Come proteggere l'ambiente Docker e Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Approfondisci il compromesso dell'isolamento**: **[Docker contro macchine virtuali 2026](/articles/docker-vs-vms/)**
8. **Riduci i privilegi dove non puoi aggiungere un confine**: **[Gestire il minimo privilegio su Linux](/articles/mastering-least-privilege-access-control-linux/)**

## Articoli correlati

| Articolo | Contenuto |
|---|---|
| **[Docker contro macchine virtuali 2026](/articles/docker-vs-vms/)** | Il confronto architetturale alla base di questo articolo, con i compromessi in termini di prestazioni e sicurezza |
| **[Come proteggere l'ambiente Docker e Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Rafforzamento pratico del livello container, ancora utile anche dentro una microVM |
| **[Docker in LXC su Proxmox: affidabilità, prove e migrazione a VM](/articles/docker-in-lxc-proxmox-reliability/)** | Container annidati, prove e indicazioni su quando spostare un carico di lavoro su una VM completa |
| **[Capire la virtualizzazione: concetti e applicazioni](/articles/understanding-virtualization_-concepts-and-applications/)** | Fondamenti degli hypervisor, incluse le funzionalità CPU necessarie alle microVM |
| **[Gestire il minimo privilegio su Linux](/articles/mastering-least-privilege-access-control-linux/)** | Riduzione dei privilegi ottenibili con un'evasione per limitare l'impatto |

## Riferimenti

1. [I container non sono più un confine di sicurezza - DepthFirst (Zhenpeng Lin, 22 settembre 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Sito ufficiale Copy Fail e analisi dell'exploit](https://copy.fail/)
4. [Analisi tecnica di Dirty Frag - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia: escalation locale dei privilegi nel kernel Linux tramite ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [Panoramica e premi di kvmCTF - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [Voce NVD per CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Commit upstream mainline della correzione Copy Fail](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Avviso di sicurezza Ubuntu: correzioni disponibili per Copy Fail](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [Exploit kernelCTF e segnalazioni - Google Security Research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)

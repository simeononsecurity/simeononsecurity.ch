---
title: "El 2026, els contenidors ja no són una frontera de seguretat"
date: 2026-09-28
lastmod: 2026-11-13
toc: true
draft: false
description: "Les vulnerabilitats del nucli del 2026 mostren per què l’aïllament de contenidors multiinquilí no és suficient. Coneix Copy Fail, Dirty Frag, Fragnesia i CVE-2026-80521, i compara els contenidors reforçats amb les fronteres de microVM."
genre: ["Seguretat dels contenidors", "Linux", "Seguretat del nucli", "Virtualització", "Seguretat al núvol", "Recerca d’amenaces", "Equip blau", "DevSecOps"]
tags: ["Escapada de contenidor", "Frontera de seguretat dels contenidors", "CVE del nucli Linux", "Escalada local de privilegis", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "microVM", "Firecracker", "Kata Containers", "Corrupció de la memòria cau de pàgines", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "Aïllament d’espais de noms", "Crida de sistema clone", "Detecció de vulnerabilitats amb IA", "Seguretat de Docker", "Seguretat de Kubernetes", "Aïllament multiinquilí", "Escapada de sandbox", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "Tendència de CVE del nucli"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "Il·lustració digital de diversos contenidors brillants connectats a un símbol central del nucli. Els elements de colors mostren vulnerabilitats que s’estenen des del nucli sobre un fons fosc."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---
**Els contenidors comparteixen un únic nucli. El 2026, quatre famílies independents de vulnerabilitats han demostrat que un sol error al nucli és suficient per sortir d’un contenidor i arribar a l’amfitrió.** Copy Fail, Dirty Frag, Fragnesia i CVE-2026-80521 donen privilegis root a un usuari local sense privilegis. Totes travessen la frontera del contenidor.

*La part preocupant no són els errors en si. És el baix cost amb què la IA els troba ara i com un pedaç en va crear un altre.*

Aquest article explica com els contenidors aïllen les càrregues de treball, per què l’aïllament ara descansa sobre una base cada cop més estreta, què fa cada vulnerabilitat del 2026 i quina tecnologia d’aïllament convé confiar-hi en lloc dels contenidors.

**Què t’emportes:** identifica qui aporta el codi de cada càrrega de treball, determina quines funcions del nucli necessita i tria entre contenidors reforçats i una frontera de microVM. Considera els casos del 2026 com a evidència de recerca datada. Revisa els avisos actuals dels proveïdors abans de modificar un nucli de producció.

## Resposta breu

| Pregunta | Resposta breu |
|---|---|
| **Els contenidors aïllen?** | Sí, els processos i el sistema de fitxers. Tots comparteixen un nucli, així que els errors del nucli són un risc compartit |
| **Per què ara?** | La cerca d’errors amb ajuda d’IA ha reduït el cost de trobar defectes al nucli. El setembre del 2026 s’han publicat prop de **6.000 CVE del nucli** |
| **Què trenca la frontera?** | Qualsevol escalada local de privilegis al nucli. No cal una configuració errònia del contenidor per escapar-ne |
| **N’hi ha prou amb aplicar pedaços?** | És necessari, però el ritme ja no segueix el de les troballes. Un pedaç del 2026 **va introduir un error explotable nou** |
| **Què funciona millor?** | MicroVM com Firecracker o Kata Containers, que donen un nucli propi a cada càrrega de treball |
| **L’alternativa és perfecta?** | No. L’hipervisor també és codi. La superfície d’atac és molt més petita, i aquesta diferència és el que importa |

## Com aïllen els contenidors

Per entendre la frontera, primer cal entendre què no és un contenidor.

**Un contenidor no és una màquina virtual.** No té un segon nucli, maquinari emulat ni un hipervisor entre el procés i el maquinari. Quan executes una imatge de contenidor, executes un procés al nucli existent, amb una visió modificada del sistema.

El mecanisme és la **crida de sistema `clone`**. `fork` copia l’espai d’adreces d’un procés; `clone` crea un procés fill i permet controlar amb precisió quines parts del context d’execució es comparteixen i quines se substitueixen. Docker passa a `clone` un conjunt d’**espais de noms**:

| Espai de noms | Què simula |
|---|---|
| **Mount** | Una arrel privada del sistema de fitxers, perquè el contenidor vegi el seu arbre en lloc del teu |
| **PID** | Numeració pròpia de processos, de manera que `PID 1` és el primer procés del contenidor, no `systemd` |
| **User** | Un mapa d’identitats en què "root" al contenidor correspon a un usuari de l’amfitrió sense privilegis |
| **Network** | Interfícies, taules d’encaminament i ports privats |
| **IPC** | Memòria compartida i cues de missatges aïllades |
| **UTS** | Nom d’amfitrió i de domini propis |
| **Cgroup** | Una vista privada dels límits de recursos |

Afegeix un sistema de fitxers **union** sobre una imatge i el resultat *sembla* un ordinador separat. `id` mostra `uid=0(root)` dins del contenidor. El sistema de fitxers sembla una instal·lació mínima d’Ubuntu. La llista de processos només mostra els seus processos.

**A nivell de crides de sistema, això no és una frontera de seguretat.** Quan un procés dins del contenidor obre un fitxer, assigna memòria o toca un sòcol de xarxa, el mateix nucli gestiona la petició per a tots els contenidors de l’amfitrió. Els espais de noms canvien *què veu el procés*, no *què fa el nucli per al procés*.

*El nucli és la frontera real entre el contenidor i l’amfitrió. La resta és presentació.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Diagrama de tres contenidors sobre un mateix nucli. Els espais de noms mount, PID, user i network en separen les vistes, però totes les crides de sistema continuen arribant a un únic nucli compartit" >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## La frontera és codi, i el codi té errors

Tota acció d’un contenidor passa per la **interfície de crides de sistema**. Obrir un fitxer, llegir memòria, escriure en un sòcol, canviar un UID: el nucli ho gestiona tot, perquè no vol que els processos accedeixin directament a la CPU, al sistema de fitxers o a la xarxa.

Aquesta mediació és el model de seguretat i està implementada amb codi. En concret, n’hi ha aproximadament **30 milions de línies**.

Hi ha una escalada local de privilegis (LPE) quan un procés explota un defecte del codi que fa de mediador per obtenir privilegis que no se li havien concedit. **Les LPE no són noves.** Existeixen des dels primers mecanismes de mediació del nucli. Durant dècades, el sector n’ha vist un degoteig constant.

**Dirty Pipe, el 2022**, és l’exemple de referència que coneix la majoria. Va aprofitar un defecte en la gestió dels buffers de pipe per sobreescriure fitxers només de lectura. Va ser notícia perquè errors d’aquesta gravetat apareixien **aproximadament cada un o dos anys**. S’aplicava el pedaç i es continuava, amb la suposició que no hi havia cap defecte gran sense descobrir en un codi que llegien un milió de persones.

*Aquesta suposició ja no és vàlida.*

## Què ha canviat el 2026

El canvi no és l’habilitat dels atacants, sinó que **trobar errors de corrupció de memòria al nucli s’ha convertit en una tasca d’enginyeria en lloc d’una carrera de recerca**.

Tres dades d’aquest any concreten el canvi:

| Troballa | Qui la va trobar | Com |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Amb l’ajuda de **Xint Code**, una eina d’anàlisi estàtica amb IA. Aproximadament **una hora d’escaneig** del subsistema criptogràfic de Linux |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Trobada amb **dfs-large1**, un model d’IA intern entrenat per detectar vulnerabilitats |
| **CVE-2026-80521**, descoberta independent | Kyle, **OpenAI** | La mateixa fallada, trobada per separat i comunicada el mateix dia |

Torna a llegir la tercera fila. Dues organitzacions amb eines d’IA diferents van trobar **el mateix use-after-free a AF_UNIX** i el van comunicar a `security@kernel.org` el **mateix dia**. No és una coincidència de talent. És un procés repetible que produeix la mateixa resposta dues vegades.

DepthFirst indica directament la magnitud: **gairebé 6.000 CVE del nucli publicades el setembre del 2026**. El recompte augmenta segons la disponibilitat d’assistència d’IA, no segons el nombre de desenvolupadors del nucli.

*Quan una hora d’escaneig amb IA troba un error de fa una dècada al subsistema criptogràfic, l’economia de l’explotació del nucli s’ha capgirat.*

## Quatre escapades en un any

Cadascuna d’aquestes vulnerabilitats dona root a un compte local sense privilegis. Cap no requereix una configuració errònia del contenidor, una opció privilegiada ni un accés inicial per xarxa.

| Vulnerabilitat | CVE | Subsistema | Tècnica | Qui la va trobar |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | Escriptura de 4 bytes a la memòria cau de pàgines de qualsevol fitxer llegible | Theori, amb ajuda d’IA |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | Escriptura de 4 bytes a la memòria cau de pàgines mitjançant dues variants encadenades | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP | Escriptures d’un byte a la memòria cau de pàgines | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | Sòcols AF_UNIX | Use-after-free a la recollida de brossa de `unix_vertex` | DepthFirst, amb ajuda d’IA |

Les quatre comparteixen un patró de disseny que cal remarcar: **ataquen la memòria cau de pàgines, no el disc.**

### Copy Fail: un error lògic sense cursa

Copy Fail és la més simple de les quatre i també la més alarmant.

Gairebé totes les LPE de Linux necessiten una finestra temporal o un desplaçament de memòria específic del nucli. **Copy Fail no necessita cap de les dues coses.** És un error lògic directe a `algif_aead`, el mòdul que proporciona a l’espai d’usuari accés a xifratge autenticat mitjançant AF_ALG.

La cadena d’explotació executa `splice()` per introduir una pàgina de la memòria cau a l’operació i després abusa de la ruta AEAD en el mateix lloc per escriure **quatre bytes controlats** a la pàgina. La pàgina malmesa **no es marca mai com a dirty**, de manera que mai no es torna a escriure al disc. El fitxer del disc continua intacte, així que les comprovacions de suma i integritat passen mentre la còpia en memòria incorpora la modificació.

Un **script Python de 732 bytes** obté root en totes les distribucions Linux publicades des del 2017. L’error es va introduir amb una **optimització del 2017** a `algif_aead`, i el pedaç del 2026 simplement la reverteix. Commit de mainline `a664bf3d603d`.

*L’error va romandre en totes les distribucions principals durant gairebé una dècada, i una eina d’IA el va trobar en una hora.*

### Dirty Frag: dues variants que es cobreixen mútuament

El nom Dirty Frag descriu bé el seu origen: **Dirty Pipe sobreescriu `struct pipe_buffer`. Dirty Frag sobreescriu el camp `frag` de `struct sk_buff`.**

Són **dues vulnerabilitats encadenades**, i l’encadenament és la part enginyosa:

- **CVE-2026-43284** aprofita que `esp_input()` se salta la ruta copy-on-write abans de desxifrar en el mateix lloc un fragment inclòs amb splice. Necessita el privilegi de crear un **user namespace**, que algunes distribucions restringeixen.
- **CVE-2026-43500** aprofita que `rxkad_verify_packet_1()` desxifra el fragment en el mateix lloc. No necessita privilegi de namespace, però `rxrpc` falta a la majoria de distribucions. Ubuntu el carrega per defecte.

**Cadascuna per separat té un punt cec. Juntes es cobreixen mútuament.** Si s’admeten user namespaces, s’executa primer la ruta ESP. Si es bloquegen però hi ha `rxrpc`, s’executa la ruta RxRPC. Així, un únic binari d’explotació funciona en diverses distribucions, i la variant RxRPC arriba a root buidant un camp de `/etc/passwd` i deixant que PAM accepti una contrasenya buida amb `nullok`.

**La troballa més important per als defensors:** Dirty Frag s’activa **tant si `algif_aead` està disponible com si no**. La mitigació de Copy Fail, que posa el mòdul a la llista negra, **no protegeix gens contra Dirty Frag**.

### Fragnesia: el pedaç que va crear un error

Fragnesia és de la mateixa classe que Dirty Frag, però apunta al camí **ESP-in-TCP** de XFRM. És el cas més instructiu del conjunt.

La vulnerabilitat explota la gestió incorrecta de fragments de pàgina compartits durant la coalescència de `skb`. Un atacant insereix pàgines recolzades per fitxers a la cua de recepció TCP abans que el sòcol passi al mode de protocol de capa superior `espintcp`. Quan s’activa el processament ESP, el nucli desxifra les dades en cua **al mateix lloc**, i la manipulació del flux de claus AES-GCM corromp la memòria cau de pàgines subjacent. L’atacant obté **escriptures repetides d’un byte** a les pàgines de fitxers en memòria cau.

L’explotació obté root sobreescrivint els primers bytes de `/usr/bin/su` amb una càrrega ELF petita. **El canvi només existeix a la memòria i no toca el binari del disc.**

Els **user i network namespaces** no privilegiats proporcionen `CAP_NET_ADMIN` dins d’un namespace aïllat. Després, NETLINK_XFRM instal·la una associació de seguretat preparada.

*Atura’t en aquesta frase:* Fragnesia va aparèixer com **un efecte secundari no intencionat d’un dels pedaços per a les vulnerabilitats Dirty Frag originals**. En corregir Dirty Frag es va crear un nou error independent que permetia obtenir root.

### CVE-2026-80521: l’escapada de contenidor que va guanyar kernelCTF

La cursa d’AF_UNIX posa fi a qualsevol argument que això sigui teòric.

La vulnerabilitat és un **use-after-free a la heap** en el mecanisme de recollida de brossa dels missatges `SCM_RIGHTS`, que els processos utilitzen per passar-se descriptors de fitxer. Una cursa durant la recollida d’una referència circular a un sòcol allibera un `struct unix_vertex` mentre l’anell SCC d’un sòcol supervivent encara en té un punter. La recollida següent recorre l’anell obsolet i accedeix a memòria alliberada.

La importància més enllà de Linux és que **AF_UNIX és la base de la comunicació entre processos locals (IPC)**. Les bases de dades locals, `systemd` i fins i tot Docker en depenen. DepthFirst indica que la vulnerabilitat afecta la majoria de les sandbox de nivell de sistema operatiu basades en el nucli, **incloses `nsjail`, `Firejail` i `Bubblewrap`**, així com els entorns d’execució moderns de contenidors.

DepthFirst va guanyar una **plaça de Google kernelCTF** amb l’error el **24 de juliol del 2026**, en va rebre la confirmació a l’espai `lts-6.12.95` el **5 d’agost**, el va comunicar a `security@kernel.org` aquell mateix dia i va saber que **Kyle, d’OpenAI, havia comunicat el mateix error**. El pedaç principal es va publicar el **6 d’agost**. La recerca es va publicar el **22 de setembre**.

Van publicar una explotació funcional per a **Ubuntu 26.04** i una segona explotació de CVE-2026-52910 per escapar d’**Ubuntu 24.04**.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Diagrama d’un procés sense privilegis dins d’un contenidor que corromp una pàgina de la memòria cau per modificar en memòria un binari setuid, obté root i surt de la frontera del contenidor fins al nucli de l’amfitrió" >}}

## Per què continuen fallant les recomanacions de mitigació

Aquest any s’han proposat tres rondes de solucions provisionals als defensors, i cadascuna tenia part de raó però també part d’error.

| Mitigació | Què atura | Què no cobreix |
|---|---|---|
| Incloure **`algif_aead`** a la llista negra | Copy Fail | **Res de Dirty Frag**, que ignora completament el mòdul |
| Incloure **`esp4`, `esp6`, `rxrpc`** a la llista negra | Dirty Frag, Fragnesia | Els equips que necessiten IPsec. També deixa fora subsistemes completament nous |
| Restringir els **user namespaces sense privilegis** | Les variants ESP | La variant RxRPC no necessita namespace. La política d’AppArmor només és una mitigació **parcial** |
| **Aplicar pedaços al nucli** | L’error corregit | El següent error i qualsevol altre que introdueixi el pedaç |

Hi destaquen dos patrons.

**Primer, les solucions provisionals es contradiuen.** Copy Fail es mitiga desactivant `algif_aead`. Dirty Frag s’activa **tant si el mòdul existeix com si no**. Fragnesia necessita desactivar `esp4` i `esp6`, cosa que és un problema per a qui executa IPsec. No hi ha cap llista negra de mòduls única que cobreixi tota la família.

**Segon, i pitjor, aplicar pedaços no és una victòria neta.** Fragnesia es va introduir **amb el pedaç de Dirty Frag**. Tots els pedaços poden incorporar errors de lògica nous, i en aquest subsistema un error lògic es converteix en una explotació que obté root.

*La conclusió incòmoda: totes aquestes vulnerabilitats són a la memòria cau de pàgines, són accessibles des de codi sense privilegis i les ha trobat una eina que millora cada trimestre. Cap llista de bloqueig continua completa.*

## Resposta honesta a l’argument contrari

Hi ha una objecció legítima que mereix una resposta directa: **els hipervisors també tenen errors.**

La superfície d’atac de KVM és real. Google manté **kvmCTF** precisament per trobar aquests errors i els paga generosament:

| Nivell | Recompensa |
|---|---|
| **Escapada completa de VM** | **$250,000** |
| Escriptura de memòria arbitrària | $100,000 |
| Lectura de memòria arbitrària | $50,000 |
| Escriptura relativa de memòria | $50,000 |
| Denegació de servei | $20,000 |
| Lectura relativa de memòria | $10,000 |

Les recompenses no s’acumulen. L’objectiu és un nucli Linux LTS amb KVM i el convidat és Debian 12.5. La meta és un **atac del convidat cap a l’amfitrió**.

**Hyunwoo Kim, el mateix investigador que va trobar Dirty Frag, també cobra recompenses de KVM** i ha guanyat els $250,000 complets per una escapada de VM. La síntesi honesta és que ambdues capes tenen defectes i que, de vegades, els troba la mateixa persona.

**Però compara les escales:**

| | Nucli Linux | Hipervisor KVM |
|---|---|---|
| **CVE del 2026** | Gairebé **6.000** | Un grapat; cada investigador en troba unes poques a l’any |
| **Accessible des de** | Qualsevol procés sense privilegis, per la interfície de crides de sistema | Només codi que ja s’executa dins d’un convidat |
| **Superfície d’atac** | Tot: xarxes, sistemes de fitxers, criptografia, IPC i controladors | El dispositiu virtual i la interfície de hypercall |
| **Classe d’error** | Qualsevol defecte de seguretat de memòria o lògica en 30 M de línies | Limitada a la frontera de virtualització |

*La diferència és de diversos ordres de magnitud, no del doble. Aquesta bretxa és el motiu pel qual les microVM canvien el càlcul del risc.*

## Què proporciona una frontera real

Una **microVM** dona a cada càrrega de treball la seva **pròpia instància del nucli**, executada sobre virtualització imposada pel maquinari, en lloc de compartir el nucli de l’amfitrió mitjançant espais de noms.

La pila té tres capes que convé anomenar:

- **La CPU** proporciona mecanismes de maquinari per aïllar una regió de memòria de les altres.
- **KVM** exposa aquests mecanismes al nucli Linux perquè el nucli actuï com a hipervisor.
- Un **VMM (monitor de màquina virtual)**, com Firecracker o QEMU, controla KVM per crear i executar el convidat.

Com que el convidat executa el seu propi nucli, una explotació del nucli **dins del convidat** només compromet el convidat. No hi ha cap nucli compartit per atacar. Després, l’atacant ha d’escapar de l’hipervisor mateix, la superfície més petita on es troben els errors de KVM.

A la pràctica importen dues implementacions, i DepthFirst les inclou totes dues a la recomanació:

| Tecnologia | Enfocament | Notes |
|---|---|---|
| **Firecracker** | VMM específic, model de dispositius mínim | Creat per AWS i dissenyat per a l’aïllament multiinquilí a gran escala |
| **Kata Containers** | Entorn d’execució compatible amb OCI que embolcalla una microVM | Executa imatges de contenidor estàndard amb una frontera de VM per sota |

Kata és el canvi més fàcil per a la majoria d’equips perquè accepta les imatges de contenidor i les eines que ja fan servir. **Firecracker té una superfície d’atac més petita**, ja que implementa molta menys emulació de dispositius que un VMM d’ús general.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Diagrama que compara l’aïllament de contenidors mitjançant espais de noms sobre un nucli compartit amb l’aïllament de microVM, on cada càrrega de treball executa el seu propi nucli sobre KVM i un monitor de màquina virtual" >}}

## Què fer ara

No tots els contenidors necessiten una microVM. La decisió depèn de **qui hi executa codi**.

| Situació | Risc | Què fer |
|---|---|---|
| **Executes codi propi**, un sol inquilí | Baix | Mantén els contenidors. Aplica pedaços de seguida, elimina capacitats i mantén el sistema de fitxers arrel només de lectura |
| **Amfitrions multiinquilí** amb accés shell dels usuaris | **Alt** | Mou les càrregues no fiables a microVM. És el primer cas que assenyala DepthFirst |
| **Executors d’IC que processen PR no fiables** | **Alt** | Una pull request es converteix en root a l’executor. Aïlla cada tasca en una VM pròpia |
| **Notebooks, sandbox d’agents i serverless** | **Alt** | El codi de l’inquilí obté root a l’amfitrió. Una microVM per inquilí |
| **Clústers de Kubernetes** | **Elevat** | L’amfitrió comparteix la memòria cau de pàgines. Un pod amb les primitives adequades compromet el node i travessa les fronteres entre inquilins |

El principi comú és simple. **Els contenidors són una eina excel·lent per empaquetar i aïllar processos.** No es van dissenyar per contenir codi hostil; el sector els va fer servir així en silenci perquè eren còmodes i barats.

### Reforç que ajuda en tots els casos

Res d’això substitueix la frontera d’una VM, però elimina vies fàcils:

```bash
# Desactiva els mòduls que explota la família page-cache quan no calguin
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Restringeix els espais de noms d’usuari sense privilegis, que bloquegen les variants ESP
# Debian i Ubuntu: és una mitigació parcial, no completa
sysctl -w kernel.unprivileged_userns_clone=0

# Si se sospita d’una explotació, buida la memòria cau de pàgines per descartar els binaris modificats en memòria
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Indicadors inicials de detecció
- Ús inesperat d’unshare(CLONE_NEWUSER) des d’una càrrega sense cap motiu legítim
- Activitat NETLINK_XFRM o associacions de seguretat XFRM fora dels amfitrions IPsec
- Sol·licituds per associar sòcols AF_ALG
- Càrrega d’esp4, esp6 o rxrpc en amfitrions que no executen ni IPsec ni AFS
```

> **Avís: `drop_caches` descarta la còpia modificada en memòria i n’elimina la corrupció, però no expulsa un atacant que ja ha obtingut root. Tracta’l com a resposta a incidents, no com a correcció.**

### El problema del ritme d’aplicació de pedaços

Fins i tot amb la millor intenció, aplicar pedaços al nucli s’ha convertit en una cursa:

- La publicació de gairebé **6.000 CVE** aquest any supera, només pel volum, la majoria de finestres de manteniment.
- **Un pedaç pot introduir un error.** Fragnesia ho va demostrar en aquest mateix subsistema.
- **La llista de mitigacions caduca.** `algif_aead` era la resposta a l’abril. Al maig no cobria res de Dirty Frag.

*La velocitat d’aplicar pedaços és necessària, però insuficient. L’arquitectura decideix si un pedaç omès causa un incident limitat o compromet l’amfitrió.*

## La pregunta més difícil: qui és l’adversari?

La resposta tècnica és clara. La resposta estratègica depèn d’una pregunta que molts equips ometen.

**Si el teu model d’amenaces és un usuari curiós o un desenvolupador descuidat, els contenidors continuen sent adequats.** Una escapada de contenidor requereix execució de codi local i una explotació del nucli. Cap de les dues és trivial, i el cost operatiu de traslladar-ho tot a microVM és real.

**Si el teu model d’amenaces inclou un adversari que executa codi a la teva infraestructura, els contenidors són ara un obstacle menor.** Val la pena citar literalment la conclusió de DepthFirst:

> "La barrera d’entrada per convertir aquestes vulnerabilitats en armes ha baixat tant que hem de donar per fet que els atacants ja poden escapar dels contenidors estàndard quan vulguin."

És un proveïdor de seguretat que té un producte per vendre i defensa una arquitectura concreta. És raonable mantenir-hi escepticisme. **Però l’argument no depèn del proveïdor.** El recompte de 6.000 CVE és públic, les explotacions estan publicades i el disseny comparteix el nucli.

*La formulació honesta: la frontera dels contenidors té cada cop menys valor davant d’un atacant amb un punt de suport, i manté tot el valor davant de la resta.*

## Veredicte

**Els contenidors continuen sent l’eina adequada per empaquetar, desplegar i separar processos. Ja no són una frontera de seguretat fiable contra codi hostil.**

Tres afirmacions, ordenades per grau de confiança:

1. **La premissa tècnica està resolta.** Els contenidors comparteixen el nucli de l’amfitrió. Cadascuna de les quatre vulnerabilitats d’aquest article va travessar la frontera des d’un compte sense privilegis, i les explotacions són públiques.

2. **La IA n’ha canviat el ritme, no el principi.** Les LPE al nucli sempre han existit. Ara trobar-ne una costa aproximadament **una hora d’escaneig amb IA** en lloc de mesos de feina experta, i dues organitzacions van trobar el mateix zero-day per separat el mateix dia.

3. **Migrar té un cost, i no migrar també.** Firecracker i Kata afegeixen sobrecàrrega, complexitat operativa i noves competències. La tria és directa: assumir la sobrecàrrega o acceptar que un error al nucli compromet l’amfitrió.

**Si gestiones infraestructura multiinquilí o executes codi no fiable, comença ara a planificar la migració a microVM.** No perquè s’acabi el món, sinó perquè la trajectòria és clara i la migració dura trimestres, no setmanes.

**Si executes contenidors d’un sol inquilí amb codi propi, conserva’ls.** Aplica pedaços al nucli més de pressa, desactiva els mòduls que no necessites i revisa la decisió quan hi entri codi no fiable.

*S’acaba l’època de tractar el nucli com una frontera de confiança incondicional. La infraestructura preparada perquè el nucli es comprometi és la que sobreviu a la intrusió.*

## Conclusions clau

- **Els contenidors comparteixen el nucli de l’amfitrió.** L’aïllament prové dels espais de noms de la crida `clone`, no de la virtualització de maquinari; per tant, un error al nucli també és un error del contenidor.
- **Quatre vulnerabilitats del 2026 van travessar la frontera** des de comptes locals sense privilegis: Copy Fail, Dirty Frag, Fragnesia i CVE-2026-80521. Les quatre apunten a la memòria cau de pàgines.
- **El setembre del 2026 s’havien publicat gairebé 6.000 CVE del nucli**, i les eines d’IA n’acceleren la troballa. Copy Fail es va trobar en **aproximadament una hora d’escaneig amb IA**.
- **Fragnesia va aparèixer amb el pedaç de Dirty Frag.** El pedaç va produir un nou error que permetia obtenir root al mateix subsistema.
- **La solució provisional de Copy Fail no atura Dirty Frag.** Incloure `algif_aead` a la llista negra cobreix una vulnerabilitat i res més de la família.
- **CVE-2026-80521 també va trencar `nsjail`, `Firejail` i `Bubblewrap`**, no només els entorns d’execució de contenidors.
- **Les microVM canvien el càlcul del risc** donant a cada càrrega el seu propi nucli. KVM té errors, però la superfície és molt més petita.
- **Tria segons qui executa el codi.** El teu codi en un contenidor d’un sol inquilí comporta poc risc. El codi no fiable en un amfitrió compartit comporta risc de comprometre l’amfitrió.

## Passos següents

1. **Llegeix l’anàlisi del problema i l’explotació publicada:** **[Els contenidors ja no són una frontera de seguretat - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Consulta l’avís oficial i la guia de mitigació de Copy Fail:** **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Llegeix l’anàlisi tècnica de Dirty Frag** per entendre l’encadenament i per què falla la mitigació de `algif_aead`: **[Anàlisi tècnica de Dirty Frag](https://github.com/V4bel/dirtyfrag)**
4. **Revisa les regles i recompenses de kvmCTF** per veure l’abast de la superfície de l’hipervisor: **[Visió general de kvmCTF](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Puntua aquests CVE al teu entorn** amb l’eina al navegador: **[Calculadora CVSS v3.1](/cvss-calculator/)**
6. **Reforça el que executes ara:** **[Com protegir l’entorn Docker i Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Entén a fons el compromís d’aïllament:** **[Docker contra màquines virtuals 2026](/articles/docker-vs-vms/)**
8. **Redueix privilegis quan no puguis afegir una frontera:** **[Control d’accés de mínim privilegi a Linux](/articles/mastering-least-privilege-access-control-linux/)**

## Articles relacionats

| Article | Què cobreix |
|---|---|
| **[Docker contra màquines virtuals 2026](/articles/docker-vs-vms/)** | La comparació arquitectònica de base, inclosos els compromisos de rendiment i seguretat |
| **[Com protegir l’entorn Docker i Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Mesures pràctiques per reforçar la capa de contenidors, també útils dins d’una microVM |
| **[Docker a LXC sobre Proxmox: fiabilitat, evidència i migració a VM](/articles/docker-in-lxc-proxmox-reliability/)** | Contenidors niats, evidència i quan traslladar una càrrega de treball a una VM completa |
| **[Entendre la virtualització: conceptes i aplicacions](/articles/understanding-virtualization_-concepts-and-applications/)** | Fonaments d’hipervisors, incloses les funcions de CPU de què depenen les microVM |
| **[Control d’accés de mínim privilegi a Linux](/articles/mastering-least-privilege-access-control-linux/)** | Reduir els privilegis que donaria una escapada per limitar-ne l’impacte |

## Referències

1. [Els contenidors ja no són una frontera de seguretat - DepthFirst (Zhenpeng Lin, 22 de setembre del 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [Nota de vulnerabilitat CERT/CC VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Lloc oficial d’informació de Copy Fail i anàlisi de l’explotació](https://copy.fail/)
4. [Anàlisi tècnica de Dirty Frag - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia: escalada local de privilegis al nucli Linux mitjançant ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [Visió general de kvmCTF i nivells de recompensa - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [Entrada NVD de CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Commit de correcció upstream a mainline per a Copy Fail](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Avís de seguretat d’Ubuntu sobre les correccions de Copy Fail](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [Explotacions i comunicacions de KernelCTF - Recerca de seguretat de Google](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)

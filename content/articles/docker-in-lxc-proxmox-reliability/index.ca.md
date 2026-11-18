---
title: "Docker a LXC sobre Proxmox: fiabilitat, proves i migració a una VM"
date: 2026-09-16
lastmod: 2026-11-13
toc: true
draft: false
description: "Avalua Docker dins de Proxmox LXC amb un error documentat d’AppArmor, una lectura acurada d’un informe sobre bloquejos de l’amfitrió, ordres de diagnòstic i un pla de migració a una VM."
genre: ["Virtualització", "Administració de Linux", "laboratori domèstic"]
tags: ["Docker dins de LXC", "Docker a Proxmox", "LXC de Proxmox", "màquina virtual de Docker", "fiabilitat de l’homelab", "bloquejos de l’amfitrió Proxmox", "VM Debian per a Docker", "contenidors sense privilegis", "contenidors niats", "aïllament del nucli Linux", "AppArmor", "runc", "lxc-pve", "Docker Compose", "controladors d’emmagatzematge de Docker", "magatzem d’imatges de containerd", "pressió de memòria", "Linux PSI", "diari persistent", "còpies de seguretat de Proxmox", "còpies de bind mounts", "migració de VM", "dominis de fallada", "pas de GPU", "diagnòstic del servidor domèstic"]
cover: "/img/cover/docker-lxc-vm-homelab-isolation.webp"
coverAlt: "Il·lustració isomètrica d’un servidor domèstic amb càrregues de treball imbricades i un compartiment separat per a una màquina virtual connectada a maquinari compartit"
coverCaption: "Il·lustració conceptual del maquinari compartit i de diferents límits d’aïllament de les càrregues de treball"
---
**Docker dins de Linux Containers (LXC)** redueix part de la sobrecàrrega d’infraestructura, però augmenta les interaccions entre l’entorn d’execució de les aplicacions i l’amfitrió Proxmox. Per als serveis Docker dels quals depèn la teva llar, una **màquina virtual (VM) amb Debian** és un punt de partida pràctic. Separa el nucli convidat i simplifica l’entorn que has de reproduir quan investigues un problema. Aquest article analitza el vídeo proporcionat, comprova l’informe d’incident relacionat i afegeix errors documentats i un pla de migració.

<!--more-->

## Punts clau

- **Distingeix els tipus d’error:** un error d’inici de Docker, una VM bloquejada i un amfitrió físic que no respon requereixen investigacions diferents.
- **Avalua les proves:** l’estabilitat després d’una migració dona suport a una decisió de recuperació, però no demostra la causa original.
- **Consulta la documentació actual:** el suport natiu d’imatges OCI i Docker imbricat dins de LXC són vies de desplegament diferents.
- **Protegeix les dades persistents:** les còpies de seguretat de Proxmox i els fitxers Compose no cobreixen automàticament totes les ubicacions de dades de les aplicacions.
- **Prova el pla de recuperació:** mesura la restauració, el comportament després de reiniciar i la disponibilitat del servei abans de retirar el desplegament anterior.

## Abans de començar

**Dificultat:** Mitjana. **Públic:** administradors de Proxmox que trien entre Docker imbricat i Docker en una VM. Abans de seguir els exemples de diagnòstic, has de reconèixer un projecte Compose, un muntatge de contenidor i un indicador de shell de Linux.

**Temps estimat:** reserva entre 30 i 60 minuts per a l’inventari i la recollida de proves. La durada de la migració depèn de la mida de la base de dades, el rendiment de l’emmagatzematge, l’accés al maquinari i la finestra d’interrupció que triïs. Els exemples següents són procediments documentats i raonaments il·lustratius, no benchmarks d’un laboratori fet per a aquest article.

| Requisit | Per què és important |
|---|---|
| **Accés a la consola de l’amfitrió** | Distingeix una fallada de xarxa d’un bloqueig de tot l’amfitrió |
| **Còpies de seguretat actuals** | Ofereix una via de recuperació abans de canviar el desplegament |
| **Identificadors de contenidors i VM** | Adreça les ordres de l’amfitrió a la càrrega prevista |
| **Inventari de dades de l’aplicació** | Identifica volums, muntatges vinculats, bases de dades i dependències externes |
| **Entorn de proves separat** | Permet assajar la migració sense duplicar escriptures de producció |

## Mira el vídeo d’origen

{{< youtube id="XyPBHhZg0Ok" enable="true" title="Proxmox: The Hidden Danger of Running Docker Inside LXC" description="Explicació de Docker imbricat a Proxmox LXC, bloquejos intermitents de l’amfitrió i una migració a màquines virtuals Debian" uploadDate="2026-09-15T17:00:09-07:00" >}}

**Vídeo d’origen:** [Proxmox: The Hidden Danger of Running Docker Inside LXC](https://www.youtube.com/watch?v=XyPBHhZg0Ok), publicat el 15 de setembre de 2026 per *Proxmox x Kubernetes x Homelab x Backup*. La pregunta central és quanta incertesa operativa acompanya una arquitectura que estalvia recursos.

**Límit de les proves:** el vídeo explica un incident i proposa lliçons. Les seccions següents distingeixen les observacions del propietari, el comportament documentat del programari i les recomanacions que se’n deriven.

## Què demostra l’incident

L’informe original descriu un **amfitrió amb Intel Core i3-13100 i BIOSTAR H610MHP**. El propietari va informar de bloquejos intermitents que afectaven l’accés de gestió i els serveis LXC. Una pantalla connectada va deixar de respondre, tot i que l’informe diu explícitament que syslog continuava generant sortida. Això és més precís que descriure l’incident com si no hagués deixat cap registre. [Informe original al fòrum de Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

Més tard, el propietari va informar d’una **millora després de la migració**. En una actualització del 3 d’agost va descriure el trasllat de càrregues Docker a màquines virtuals Debian i l’aturada dels LXC que allotjaven Docker. En el moment de l’actualització no s’havien notificat més bloquejos. El vídeo esmenta un període estable de 16 dies. Cap de les dues afirmacions aporta una reproducció controlada ni identifica cap component defectuós concret. [Actualització del propietari al mateix fil](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)

| Observació | Què dona suport | Què no demostra |
|---|---|---|
| **Temps d’activitat inicial llarg** | La combinació anterior de càrrega i programari funcionava correctament | La fiabilitat després de cada actualització posterior |
| **L’amfitrió i els serveis s’aturen** | La interrupció supera una sola aplicació | Docker com a causa principal |
| **La migració precedeix la millora** | Una solució operativa útil | Quina interacció modificada va eliminar el desencadenant |
| **Setze dies estables** | Un període d’observació limitat | La resolució de tots els errors que es repeteixen cada dues o tres setmanes |

El **període d’observació** mereix atenció. Setze dies són dins d’un interval de recurrència de 14 a 21 dies. Una observació més llarga, que cobreixi diversos intervals de fallada anteriors, càrregues comparables i manteniment habitual, augmenta la confiança, però encara no demostra una relació causal controlada.

**L’èxit operatiu i la prova de la causa principal** són resultats diferents. Restablir serveis domèstics fiables és un motiu vàlid per migrar. Descriu el resultat com una millora observada de la fiabilitat fins que proves més sòlides n’estableixin el mecanisme.

## Localitza el límit del nucli

```text
Docker dins de LXC:
Aplicació -> Entorn d’execució Docker -> espais de noms i polítiques LXC
              -> nucli de l’amfitrió Proxmox -> maquinari físic

Docker dins d’una màquina virtual:
Aplicació -> Entorn d’execució Docker -> nucli Linux convidat
              -> maquinari virtual / KVM-QEMU
              -> nucli de l’amfitrió Proxmox -> maquinari físic
```

**LXC** utilitza el nucli de l’amfitrió. Els espais de noms, grups de control, capacitats, seccomp i perfils de seguretat restringeixen processos sense proporcionar un nucli separat. Afegir Docker dins de LXC crea una altra capa de gestió de contenidors per a càrregues que utilitzen el mateix nucli subjacent de l’amfitrió. [Arquitectura LXC i funcions de contenció](https://linuxcontainers.org/lxc/introduction/)

Una **VM** incorpora un nucli convidat. Una fallada del nucli convidat normalment afecta aquesta VM, mentre Proxmox continua gestionant els altres convidats. La VM encara depèn de l’amfitrió físic, l’hipervisor, l’emmagatzematge i la xarxa. Una fallada de maquinari o un defecte del nucli de l’amfitrió continuen sent dependències compartides.

| Límit | Docker dins de LXC | Docker dins d’una VM |
|---|---|---|
| **Nucli que fan servir les aplicacions** | Nucli de l’amfitrió Proxmox | Nucli convidat |
| **Entorn d’execució de Docker** | Limitat per la política del contenidor extern | Instal·lat en un sistema operatiu convidat convencional |
| **Actualitzacions del nucli convidat** | Vinculades al nucli de l’amfitrió | Gestionades dins del convidat |
| **Interrupció de l’amfitrió físic** | Atura les càrregues dependents | Atura les càrregues dependents |

Una VM limita **una part de la propagació de fallades**, però no tota. La caiguda d’un procés d’aplicació dins de LXC no fa caure automàticament Proxmox. De la mateixa manera, posar tots els serveis domèstics en una sola VM Docker els agrupa darrere d’un sistema operatiu convidat i un calendari de manteniment comuns.

Per a la **comparació conceptual més àmplia**, consulta [Contenidors Docker i màquines virtuals](/articles/docker-vs-vms/). Aquí, la decisió tracta sobre on col·locar Docker dins de Proxmox i els límits de diagnòstic resultants.

## Defineix el suport amb precisió

**«No compatible»** requereix indicar un component i una versió. Distingeix entre un desplegament recomanat pel proveïdor, funcions documentades, manteniment de la distribució i un dret contractual de suport. Que una pila imbricada funcioni no demostra que totes les combinacions es provin igual. La recomanació d’utilitzar VM tampoc significa que els mantenidors rebutgin qualsevol error relacionat amb la imbricació.

**La documentació actual de Proxmox** afegeix una distinció important. El codi font del conjunt d’eines de contenidors descriu el suport d’imatges d’aplicacions **Open Container Initiative (OCI)** com una versió de prova tecnològica que converteix les imatges al marc LXC. Per a requisits que prioritzen l’aïllament i la migració en viu, també recomana contenidors dins d’una VM QEMU. Importar una imatge OCI a aquest marc és diferent d’instal·lar Docker Engine i executar Compose dins d’un convidat LXC. [Documentació del conjunt d’eines de contenidors Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)

| Desplegament | Pregunta que cal verificar |
|---|---|
| **Convidat LXC tradicional** | El seu model de sistema operatiu i l’aplicació s’ajusten a les restriccions documentades dels contenidors? |
| **Docker imbricat a LXC** | Quines combinacions de nucli, runtime, política de seguretat i emmagatzematge s’han provat? |
| **Importació nativa d’imatges OCI** | La versió instal·lada de Proxmox ofereix la funció documentada i el comportament necessari? |
| **Docker dins d’una VM Debian** | La versió del convidat compleix els requisits d’instal·lació de Docker? |

Docker publica una **via d’instal·lació per a Debian**. Fes servir la llista de versions admeses i les instruccions del repositori per al convidat. Anota les versions que desplegues en lloc de pressuposar que una guia antiga continua sent correcta. Això proporciona una base d’instal·lació documentada, no una garantia de disponibilitat ni un contracte de suport de pagament automàtic. [Docker Engine a Debian](https://docs.docker.com/engine/install/debian/)

## Una fallada d’imbricació confirmada

La **incompatibilitat de runc/AppArmor del 2025** és un exemple verificable. Els mantenidors de runc van documentar una fallada en tornar a obrir un descriptor dins d’un contenidor extern amb un perfil AppArmor. AppArmor va interpretar erròniament un accés sota **`/proc/sys`** com un accés sota **`/sys`** i la política el va denegar. [problema de runc 4968](https://github.com/opencontainers/runc/issues/4968)

Un **inici afectat** va informar d’aquest fragment d’error:

```text
open sysctl net.ipv4.ip_unprivileged_port_start file: reopen fd 8: permission denied
```

La fallada registrada impedia l’**inici del contenidor**. No explica els bloquejos de l’amfitrió descrits al fòrum. L’issue assenyala **`lxc-pve 6.0.5-2`** com la correcció de Proxmox per a aquest problema concret. El canvi corresponent de LXC es va integrar el 20 de novembre de 2025. *Són referències a correccions històriques, no una recomanació de fixar una versió de paquet en una instal·lació actual.* [Resum de la correcció dels mantenidors](https://github.com/opencontainers/runc/issues/4968), [canvi de LXC integrat](https://github.com/lxc/lxc/pull/4609)

La lliçó és la **coordinació de dependències**. Un canvi de seguretat del runtime interactuava amb la política del contenidor extern, i la correcció va requerir feina en una altra capa. Prefereix l’actualització mantinguda adequada per a la teva versió en lloc de desactivar AppArmor permanentment o conservar un runtime antic i vulnerable.

> **Idea clau:** aquest incident demostra un problema real de compatibilitat amb contenidors imbricats i una resposta real dels mantenidors. No demostra una inestabilitat general de LXC ni la causa d’un bloqueig independent de l’amfitrió.

## Compara els costos reals

Mesura l’eficiència amb la **teva càrrega de treball real**. En condicions equivalents, compara la pressió de memòria de l’amfitrió, la demanda de CPU, la latència de l’emmagatzematge, els temps de resposta de les aplicacions i l’esforç de recuperació. La RAM assignada a la VM, la memòria lliure del convidat i la memòria resident de l’amfitrió són mesures diferents.

| Estalvi afirmat | Mesura que cal recollir | Cost addicional que cal registrar |
|---|---|---|
| **Menys sobrecàrrega de memòria** | Ús i pressió de memòria de l’amfitrió amb la mateixa càrrega | Temps per gestionar límits imbricats i diagnosticar contenció |
| **Desplegament més ràpid** | Temps fins a tenir un servei funcional amb les dades restaurades | Temps per reconstruir després d’una actualització fallida |
| **Compartició de maquinari més senzilla** | Dispositius requerits, permisos i ús correcte de l’aplicació | Dependència dels controladors de l’amfitrió i restriccions de migració |
| **Còpies de seguretat més fàcils** | Restauració satisfactòria de totes les dades requerides | Muntatges externs i coherència de l’aplicació |

Per defecte, Docker permet **l’ús sense restriccions de CPU i memòria** si no s’apliquen límits. En LXC, el contenidor extern hi afegeix els seus propis. En una VM, l’assignació al convidat crea un altre límit de capacitat. El convidat també necessita recursos per al sistema operatiu, Docker, la memòria cau i els pics de demanda de les aplicacions. [Restriccions de recursos de Docker](https://docs.docker.com/engine/containers/resource_constraints/)

**L’accés al maquinari** és un requisit de la càrrega. Compartir un dispositiu gràfic de l’amfitrió amb un contenidor i assignar un dispositiu PCI a una VM exigeixen configuracions diferents de controladors i aïllament. Abans de triar, concreta el dispositiu i el requisit de l’aplicació. Una càrrega multimèdia que requereixi descodificació per maquinari hauria de superar una prova de descodificació després de la migració, a més de les comprovacions HTTP habituals.

Evita les **xifres universals de sobrecàrrega**. Aquest article no dona cap cost fix de RAM ni percentatge de rendiment, perquè aquestes xifres requereixen una càrrega, una configuració i un mètode de mesura controlats. Fes servir un resultat observat de la teva pròpia comparació al registre de decisions de més avall.

## Recull proves per capa

**Comença a l’amfitrió Proxmox** amb un shell administratiu. Substitueix **`101`** per l’ID de l’LXC que investigues:

```bash
pveversion -v
uname -r
pct config 101
journalctl --list-boots
journalctl -k -b -1 --no-pager
```

**`pveversion -v`** registra les versions dels components Proxmox instal·lats. **`pct config`** registra la configuració del contenidor extern. A **`journalctl`**, **`-k`** selecciona missatges del nucli, **`-b -1`** l’arrencada anterior i **`--no-pager`** produeix text pla al terminal. Els missatges d’arrencades anteriors requereixen dades de registre conservades. [Conjunt d’eines Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc), [referència systemd journalctl](https://github.com/systemd/systemd/blob/main/man/journalctl.xml)

**Després inspecciona l’amfitrió Docker**, dins de l’LXC o la VM que executa el dimoni:

```bash
docker version
docker info
docker compose version
docker ps -a
docker stats --no-stream
```

Registra **tots dos entorns**. L’etiqueta de la imatge del contenidor no indica les versions de Docker, containerd, runc, el nucli de l’amfitrió, la política de seguretat ni el backend d’emmagatzematge. Anota l’hora de l’incident, les actualitzacions recents i si la consola local va respondre. Elimina les credencials i les dades privades de l’aplicació abans de publicar el material de diagnòstic.

**Inspecciona una càrrega concreta** i substitueix **`app`** pel nom del contenidor:

```bash
docker inspect --format '{{json .State}}' app
docker inspect --format '{{.RestartCount}}' app
docker inspect --format '{{json .Mounts}}' app
```

**`docker inspect`** mostra l’estat, el recompte de reinicis i la informació de muntatge del contenidor indicat. Tracta el recompte de reinicis com una pista per correlacionar amb els registres, no com a prova d’un defecte de l’amfitrió. Un contenidor recreat també comença un historial nou. [Referència de docker inspect](https://docs.docker.com/reference/cli/docker/inspect/)

## Distingeix pressió i bloquejos

**Captura informació de pressió de Linux a l’amfitrió** mentre es desenvolupa el problema:

```bash
cat /proc/pressure/cpu
cat /proc/pressure/memory
cat /proc/pressure/io
```

**Pressure Stall Information**, o PSI, informa del temps que les tasques perden mentre esperen recursos. Els camps **`some`** i **`full`** descriuen estats d’aturada diferents, mentre **`avg10`**, **`avg60`** i **`avg300`** resumeixen intervals recents. La pressió de memòria és diferent de la memòria ocupada: una memòria cau gran per si sola no demostra una manca de recursos. [Documentació Linux PSI](https://docs.kernel.org/accounting/psi.html)

| Prova | Interpretació útil | Comprovació següent |
|---|---|---|
| **Un contenidor es tanca repetidament** | Error de l’aplicació o del runtime del contenidor | Estat de sortida, registres del servei, política de reinici |
| **SSH falla, la consola funciona** | Fallada de xarxa o del camí d’administració | Estat de l’enllaç, controlador NIC, pont, tallafoc |
| **La Memory PSI augmenta sota càrrega** | Les tasques perden temps per contenció de memòria | Límits, activitat de recuperació, registres OOM, creixement de la càrrega |
| **Les sol·licituds d’emmagatzematge s’encallen** | Una dependència d’E/S retarda la feina | Estat del dispositiu, registres d’emmagatzematge, latència i cues |
| **Watchdog informa d’un lockup** | El detector del nucli ha observat una aturada definida | Traça completa, versió del nucli, desencadenant reproduïble |
| **No hi ha una última entrada al registre** | La recollida d’evidències va acabar abans d’obtenir una sortida útil | Captura persistent o externa abans que es repeteixi |

Un **informe de lockup de Linux** té un significat tècnic. Els watchdogs del nucli distingeixen els soft lockups dels hard lockups. Un temps d’espera esgotat del navegador no demostra cap dels dos. L’absència d’un informe del watchdog tampoc demostra que l’amfitrió continués sa. [Documentació del detector de lockups de Linux](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)

**Els canvis de firmware i d’estats d’energia** són experiments. Registra el paràmetre anterior, el motiu del canvi i el període d’observació. Desactivar un estat d’inactivitat de la CPU canvia el comportament energètic i tèrmic. Un informe sobre una altra màquina no és prou prova per recomanar universalment el mateix paràmetre.

## Conserva registres útils

**El registre persistent** augmenta les possibilitats de conservar proves després d’un reinici. Un fitxer de configuració de journald utilitza aquesta opció:

```ini
[Journal]
Storage=persistent
```

**`Storage=persistent`** demana emmagatzematge del registre al disc quan està disponible. Configura els límits de retenció i l’espai de disc; després comprova que les arrencades anteriors apareguin a **`journalctl --list-boots`**. El registre persistent encara depèn que l’amfitrió completi les escriptures abans de la fallada. [Configuració de systemd journald](https://github.com/systemd/systemd/blob/main/man/journald.conf.xml)

**L’observació externa** afegeix una altra perspectiva. Supervisa el servei des d’un altre ordinador i registra les hores. Un monitor que s’executa a l’amfitrió Proxmox que falla desapareix durant la mateixa interrupció i ajuda menys a distingir una caiguda d’una pèrdua de telemetria.

**Prova il·lustrativa:** programa una comprovació HTTP lleugera des d’un altre sistema i compara els errors amb la connectivitat de l’amfitrió i el comportament de la consola local. Un temps d’espera de l’aplicació amb l’amfitrió responent requereix una investigació diferent d’una fallada simultània de l’aplicació, l’administració i la consola. És un disseny de diagnòstic, no un resultat observat a l’incident original.

## Planifica una migració controlada

Comença amb **un projecte Compose de baix risc**. Prepara una VM Debian amb una versió de la documentació d’instal·lació de Docker, configura còpies de seguretat i assigna recursos. Mantén el desplegament original disponible per tornar-hi fins que el substitut superi les proves. [Instruccions d’instal·lació de Docker per a Debian](https://docs.docker.com/engine/install/debian/)

**Inventaria el projecte Compose** des del directori de treball:

```bash
docker compose config --quiet
docker compose config --images
docker compose config --volumes
```

**`--quiet`** valida la configuració sense mostrar-la. **`--images`** enumera les imatges referenciades, mentre que **`--volumes`** enumera els volums amb nom. Aquestes ordres no exporten dades de l’aplicació ni proporcionen un inventari complet dels muntatges vinculats. Revisa també el fitxer Compose i els muntatges de cada contenidor. [Referència de Docker Compose config](https://docs.docker.com/reference/cli/docker/compose/config/)

| Dades o dependència | Acció de migració |
|---|---|
| **Definicions Compose** | Transfereix els fitxers del projecte i conserva la configuració provada |
| **Secrets i entorn** | Recrea els valors requerits mitjançant el procés triat per gestionar secrets |
| **Volums amb nom** | Fes una còpia i restaura’n el contingut amb procediments coherents amb l’aplicació |
| **Camins de muntatges vinculats** | Transfereix o reconnecta les dades d’origen i verifica’n la propietat |
| **Bases de dades** | Utilitza el procediment de còpia/restauració admès o una còpia amb les escriptures aturades |
| **Dispositius i recursos compartits** | Restableix l’accés i prova el comportament de l’aplicació |
| **Ports i DNS** | Prepara l’adreça substituta i planifica el canvi |

Els **volums** persisteixen més que els contenidors, però no migren sols. Un fitxer Compose anomena recursos i defineix serveis. La documentació de volums de Docker descriu operacions separades de còpia i restauració del contingut persistent. No pressuposis que recrear el projecte restaura les dades. [Cicle de vida i còpies dels volums Docker](https://docs.docker.com/engine/storage/volumes/)

Comprova per separat la **cobertura de les còpies Proxmox**. La documentació exclou de les còpies dels contenidors el contingut de dispositius i muntatges vinculats. Una còpia correcta del sistema de fitxers arrel de LXC no demostra, per tant, que tots els directoris exposats estiguin protegits. [Documentació de còpies de seguretat Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)

### Comprova l’emmagatzematge abans de copiar

**Inspecciona la configuració real d’emmagatzematge de Docker** a cada amfitrió Docker:

```bash
docker info
findmnt -T /var/lib/docker
```

**`findmnt`** identifica el sistema de fitxers que conté el camí especificat. Substitueix **`/var/lib/docker`** si el dimoni utilitza una altra arrel de dades i inspecciona el camí d’emmagatzematge de containerd quan calgui. Docker documenta la diferència entre el magatzem d’imatges de containerd i els controladors d’emmagatzematge clàssics, amb requisits propis de cada backend. [Selecció del backend d’emmagatzematge Docker](https://docs.docker.com/engine/storage/drivers/select-storage-driver/)

**Recrea les imatges i restaura les dades de l’aplicació** amb els procediments documentats del backend triat. Copiar un directori de dades Docker actiu entre configuracions d’emmagatzematge diferents comporta supòsits addicionals sobre metadades, estat dels muntatges i coherència. És una operació diferent de fer una còpia del volum de dades d’una aplicació aturada.

### Canvia amb una opció de retorn

1. **Assaja la restauració** a la VM amb adreces separades i dades de prova si cal.
2. **Atura les escriptures de producció** durant la finestra acordada i fes l’última còpia coherent.
3. **Restaura i valida** les dades de l’aplicació, els permisos, les credencials i l’accés requerit al maquinari.
4. **Canvia l’encaminament del servei** després que el substitut superi les comprovacions específiques de l’aplicació.
5. **Mantén aturat l’entorn original** i conserva’n la configuració i les dades de recuperació.
6. **Documenta la gestió del retorn** de les dades escrites després del canvi abans de reiniciar el sistema antic.

Evita **dos escriptors actius** sobre el mateix emmagatzematge de la base de dades. Tornar enrere després de noves escriptures de producció requereix un pla per conservar-les o descartar-les expressament. Reiniciar un contenidor antic no reconcilia dos historials de dades divergents.

## Prova més que el temps d’activitat

Les **proves d’acceptació** han de seguir el propòsit del servei. Un estat verd del contenidor confirma que hi ha un procés actiu. Un servei útil també necessita dades, accés a la xarxa, dependències i capacitat de recuperació.

| Prova | Evidència que cal conservar |
|---|---|
| **Funció de l’aplicació** | Una transacció, consulta o operació multimèdia real correcta |
| **Integritat de les dades** | Registres, fitxers, permisos i canvis recents esperats |
| **Reinici del convidat** | Els serveis tornen sense reparacions manuals |
| **Restauració de còpia** | La còpia restaurada supera la mateixa comprovació funcional |
| **Càrrega representativa** | Latència, CPU, pressió de memòria i comportament de l’emmagatzematge |
| **Assaig de manteniment** | Una actualització provada i un procediment de recuperació útil |
| **Observació més llarga** | Registres de disponibilitat que cobreixen diversos intervals de fallada anteriors |

**Decisió d’exemple:** un servei de càmeres i un descarregador experimental comparteixen ara una pila imbricada. Traslladar-los tots dos a una VM millora la separació dels nuclis, però manté un límit de manteniment del convidat comú. Si la disponibilitat de la càmera és prioritària, avalua grups de manteniment i límits de recursos separats, i després prova la continuïtat de l’enregistrament durant les actualitzacions del descarregador.

**Raonament esperat:** tria la ubicació segons la dependència del servei que vols aïllar. Dues VM al mateix servidor físic comparteixen encara l’alimentació, l’emmagatzematge i el nucli de l’amfitrió. Si el requisit inclou sobreviure a una avaria del servidor, el disseny necessita un altre sistema independent o una alternativa manual acceptable.

## Crea el registre de decisions

**Utilitza proves mesurades** per triar un desplegament i definir quan el revisaràs:

```text
Impacte en el servei i la llar:
Versions actuals de l’amfitrió / nucli / LXC / Docker:
Accés necessari a GPU, dispositius i xarxa:
Memòria, CPU, emmagatzematge i latència mesurats:
Símptoma de fallada conegut i interval de recurrència:
Cobertura de les còpies de seguretat i prova de restauració correcta:
Arquitectura triada i motiu:
Finestra d’interrupció permesa i objectiu de recuperació:
Procediment de canvi i reversió de dades posterior al canvi:
Proves d’acceptació i període d’observació:
Condició que exigeix revisar de nou l’arquitectura:
```

**Tria deliberadament Docker dins de LXC** quan els avantatges justifiquin el treball d’integració i hagis provat la recuperació. Tria una VM quan un entorn Docker convidat convencional i un nucli convidat separat simplifiquin el funcionament del servei. Cap de les dues decisions substitueix les còpies de seguretat, la supervisió i el manteniment de l’amfitrió.

## Estableix una porta de canvi abans de migrar

Tracta la migració com un **canvi controlat**, no com una prova de la causa de l’incident original. Abans del canvi, registra la configuració del contenidor, els resums d’imatge, els camins dels muntatges vinculats, les claus d’entorn, les assignacions de dispositius i l’última restauració correcta. Després del canvi, compara les mateixes comprovacions del servei i mesures de recursos. Mantén aturada la càrrega antiga fins que la nova superi el període d’acceptació.

Si l’incident torna després de migrar, compara el nucli de l’amfitrió, l’emmagatzematge, la pressió de memòria, l’accés als dispositius i les versions de Docker de totes dues ubicacions. La comparació acota la investigació. Una migració correcta no esdevé un experiment causal si no es van controlar les variables pertinents.

## Passos següents

**Inventaria primer un servei.** Identifica les dades persistents, les dependències físiques, els símptomes de fallada i l’objectiu de recuperació. Assaja una restauració abans de decidir si la migració és necessària.

Per a **feines relacionades**, utilitza la [guia d’actualització de Proxmox VE](/articles/proxmox-ve-8-to-9-upgrade-guide/) per planificar actualitzacions i la [guia de seguretat de Docker i Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/) per reforçar les càrregues. Mantén la selecció de l’arquitectura, l’execució d’actualitzacions i el diagnòstic d’incidents com a decisions separades, cadascuna amb les seves proves.

## Fonts i proves

**Recerca revisada:** 16 de setembre de 2026. La transcripció proporcionada va orientar el tema. Les metadades del vídeo, l’informe original, l’issue upstream i la documentació oficial es van comprovar per separat. El text etiqueta els exercicis il·lustratius i els passos de validació proposats.

| Font | Funció |
|---|---|
| **[Vídeo d’origen](https://www.youtube.com/watch?v=XyPBHhZg0Ok)** | Explicació original i període d’estabilitat comunicat |
| **[Fil de l’incident Proxmox](https://forum.proxmox.com/threads/pve-host-freezes-every-2-3-weeks.185009/)** | Observacions de primera mà i seguiment de la migració |
| **[Conjunt d’eines de contenidors Proxmox](https://github.com/proxmox/pve-docs/blob/master/pct.adoc)** | Arquitectura de contenidors i distinció actual d’OCI |
| **[problema de runc 4968](https://github.com/opencontainers/runc/issues/4968)** | Fallada d’inici documentada i correcció històrica del paquet |
| **[sol·licitud de canvi de LXC 4609](https://github.com/lxc/lxc/pull/4609)** | Canvi upstream d’AppArmor integrat |
| **[Documentació Docker](https://docs.docker.com/engine/install/debian/)** | Base d’instal·lació del convidat amb referències específiques al runtime i a l’emmagatzematge |
| **[Documentació Linux PSI](https://docs.kernel.org/accounting/psi.html)** | Interpretació de la pressió dels recursos |
| **[Documentació del watchdog Linux](https://docs.kernel.org/admin-guide/lockup-watchdogs.html)** | Condicions de lockup del nucli definides |
| **[Documentació de còpies Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc)** | Exclusions dels muntatges de contenidors i comportament de les còpies |

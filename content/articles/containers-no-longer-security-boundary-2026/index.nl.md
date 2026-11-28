---
title: "Containers zijn geen beveiligingsgrens meer: kernel-escapes in 2026"
date: 2026-09-28
lastmod: 2026-11-13
toc: true
draft: false
description: "Bekijk het container-escape-onderzoek uit 2026, de grenzen van kernelisolatie, de patchdruk en de rol van microVM's."
genre: ["Containerbeveiliging", "Linux", "Kernelbeveiliging", "Virtualisatie", "Cloudbeveiliging", "Dreigingsonderzoek", "Blue team", "DevSecOps"]
tags: ["ontsnapping uit de container", "beveiligingsgrens van containers", "Linux-kernel-CVE", "lokale privilege-escalatie", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "microVM", "Firecracker", "Kata Containers", "page-cache-corruptie", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "namespace-isolatie", "clone-systeemaanroep", "AI-kwetsbaarheidsdetectie", "Docker-beveiliging", "Kubernetes-beveiliging", "isolatie voor meerdere tenants", "sandbox-escape", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "trend in kernel-CVE's"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "Digitale illustratie van meerdere gloeiende containers die verbonden zijn met een centraal kernelsymbool. Kleurrijke elementen tonen kwetsbaarheden die vanuit de kernel uitstralen tegen een donkere achtergrond."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---
**Containers delen één kernel. In 2026 bewezen vier afzonderlijke kwetsbaarheidsfamilies dat één kernelbug genoeg is om een container te verlaten en de host te bereiken.** Copy Fail, Dirty Frag, Fragnesia en CVE-2026-80521 geven elk rootrechten aan een niet-bevoegde lokale gebruiker. Elk van deze kwetsbaarheden doorbreekt de containergrens.

*Het ongemakkelijke deel zijn niet de bugs zelf. Het is hoe goedkoop AI ze nu vindt en hoe één patch een nieuwe bug veroorzaakte.*

Dit artikel legt uit hoe containers workloads isoleren, waarom die isolatie nu op een steeds smallere basis rust, wat elke kwetsbaarheid uit 2026 doet en welke isolatietechnologie je in plaats daarvan kunt vertrouwen.

**Resultaat voor de lezer:** breng per workload in kaart wie de code aanlevert, bepaal welke kernelfuncties nodig zijn en kies tussen geharde containers en een microVM-grens. Behandel de casestudy's uit 2026 als gedateerd onderzoek. Controleer actuele leveranciersadviezen voordat je een kernel in productie wijzigt.

## Het korte antwoord

| Vraag | Kort antwoord |
|---|---|
| **Isoleren containers?** | Ja, voor processen en bestandssystemen. Alle containers delen één kernel, dus kernelbugs vormen een gedeeld risico |
| **Waarom nu?** | Met AI-ondersteund zoeken naar bugs is het veel goedkoper geworden om kernelproblemen te vinden. Per september 2026 zijn bijna **6.000 kernel-CVE's** gepubliceerd |
| **Waardoor wordt de grens doorbroken?** | Elke lokale privilege-escalatie in de kernel. Voor een escape is geen verkeerde containerconfiguratie nodig |
| **Is patchen voldoende?** | Het is noodzakelijk en het tempo volstaat niet meer. Eén patch uit 2026 **introduceerde een nieuwe exploiteerbare bug** |
| **Wat werkt beter?** | MicroVM's zoals Firecracker of Kata Containers, die elke workload een eigen kernel geven |
| **Is het alternatief perfect?** | Nee. Ook de hypervisor bestaat uit code. Het aanvalsoppervlak is vele ordes kleiner, en dat verschil is belangrijk |

## Hoe containers isoleren

Je begrijpt de grens pas goed als je begrijpt wat een container niet is.

**Een container is geen virtuele machine.** Er is geen tweede kernel, geen geëmuleerde hardware en geen hypervisor tussen je proces en de hardware. Wanneer je een containerimage uitvoert, voer je een proces uit op je bestaande kernel, met een aangepaste kijk op het systeem.

Het mechanisme is de **systeemaanroep `clone`**. Waar `fork` een procesadresruimte kopieert, maakt `clone` een onderliggend proces aan en geeft het de aanroeper nauwkeurige controle over welke delen van de uitvoeringscontext worden gedeeld en welke worden vervangen. Docker geeft `clone` een reeks **namespaces** mee:

| Namespace | Wat deze nabootst |
|---|---|
| **Mount** | Een privéroot van het bestandssysteem, zodat de container zijn eigen boom ziet in plaats van die van jou |
| **PID** | Eigen procesnummers, zodat `PID 1` het eerste proces van de container is en niet `systemd` |
| **User** | Een identiteitskoppeling waarbij "root" in de container overeenkomt met een niet-bevoorrechte hostgebruiker |
| **Network** | Privé-interfaces, routeringstabellen en poorten |
| **IPC** | Geïsoleerd gedeeld geheugen en geïsoleerde berichtenwachtrijen |
| **UTS** | Eigen hostnaam en domeinnaam |
| **Cgroup** | Een privéweergave van resourcebeperkingen |

Voeg een **union-bestandssysteem** toe boven op een image en het resultaat *voelt* als een aparte computer. `id` meldt `uid=0(root)` in de container. Het bestandssysteem lijkt op een minimale Ubuntu-installatie. Een proceslijst toont alleen de eigen processen.

**Op het niveau van systeemaanroepen is dit geen beveiligingsgrens.** Wanneer een proces in een container een bestand opent, geheugen toewijst of een netwerksocket aanraakt, verwerkt dezelfde kernel dat verzoek voor elke andere container op de host. Namespaces veranderen *wat het proces ziet*, niet *wat de kernel voor het proces zal doen*.

*De kernel vormt de echte grens tussen container en host. Al het andere is presentatie.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Diagram van drie containers op dezelfde kernel. Mount-, PID-, user- en network-namespaces scheiden hun weergaven, terwijl alle systeemaanroepen onderliggend naar één gedeelde kernel gaan." >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## De grens bestaat uit code, en code bevat bugs

Elke actie van een container loopt via de **systeemaanroepinterface**. Een bestand openen, geheugen lezen, naar een socket schrijven of een UID wijzigen: de kernel regelt dit allemaal, omdat de kernel niet wil dat processen rechtstreeks toegang krijgen tot de CPU, het bestandssysteem of het netwerk.

Die bemiddeling vormt het beveiligingsmodel, en bemiddeling is in code geïmplementeerd. Dat zijn ruwweg **30 miljoen regels** code.

Een lokale privilege-escalatie (LPE) ontstaat wanneer een proces een fout in die bemiddelende code misbruikt om rechten te verkrijgen die het nooit heeft gekregen. **LPE's zijn niet nieuw.** Ze bestaan al sinds de eerste kernelbemiddeling. De sector leefde er tientallen jaren mee, als een gestage stroom.

**Dirty Pipe uit 2022** is het referentiepunt dat de meeste mensen kennen. Het misbruikte een fout in de verwerking van pipe-buffers om alleen-lezenbestanden te overschrijven. Het haalde het nieuws omdat bugs van deze ernst **ongeveer eens per één of twee jaar** opdoken. Je patchte, ging verder en hield vast aan de aanname dat er geen groot defect onontdekt bleef in code die een miljoen mensen lazen.

*Die aanname gaat niet meer op.*

## Wat er veranderde in 2026

De verandering zit niet in de vaardigheden van aanvallers. **Het vinden van geheugenbeschadigende kernelbugs werd een technische taak in plaats van een onderzoekscarrière.**

Drie gegevenspunten uit dit jaar maken de verschuiving concreet:

| Vondst | Ontdekker | Methode |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Met hulp van **Xint Code**, een AI-tool voor statische analyse. Ongeveer **één uur scantijd** op het Linux-cryptosubsysteem |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Gevonden met **dfs-large1**, een intern AI-model dat is getraind voor kwetsbaarheidsdetectie |
| **CVE-2026-80521**, onafhankelijk | Kyle, **OpenAI** | Dezelfde bug, onafhankelijk ontdekt en dezelfde dag gemeld |

Lees de derde rij nog eens. Twee organisaties gebruikten verschillende AI-tools en vonden **dezelfde use-after-free in AF_UNIX**. Ze meldden die **dezelfde dag** aan `security@kernel.org`. Dit is geen talenttoeval. Een herhaalbaar proces leverde twee keer hetzelfde antwoord op.

DepthFirst vermeldt de omvang expliciet: **per september 2026 waren bijna 6.000 kernel-CVE's gepubliceerd**. Het aantal stijgt op een curve die de beschikbaarheid van AI-ondersteuning volgt, niet het aantal kernelontwikkelaars.

*Wanneer één uur AI-scantijd een tien jaar oude bug in het cryptosubsysteem vindt, is de economie van kernelmisbruik omgeslagen.*

## Vier escapes in één jaar

Elk van deze kwetsbaarheden geeft rootrechten vanaf een niet-bevoorrecht lokaal account. Geen ervan vereist een verkeerde containerconfiguratie, een privileged-vlag of een netwerktoegangspunt.

| Kwetsbaarheid | CVE | Subsysteem | Primitief | Gevonden door |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | Schrijft 4 bytes naar de page cache van elk leesbaar bestand | Theori, met AI-ondersteuning |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | Schrijft 4 bytes naar de page cache via twee gekoppelde varianten | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP (ESP ingekapseld in TCP) | Schrijft afzonderlijke bytes naar de page cache | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | AF_UNIX-sockets | Use-after-free in de garbagecollection van `unix_vertex` | DepthFirst, met AI-ondersteuning |

Deze vier kwetsbaarheden delen een patroon dat aandacht verdient. **Ze vallen de page cache aan, niet de schijf.**

### Copy Fail: een logische fout zonder race

Copy Fail is de eenvoudigste van de vier en de meest verontrustende.

Bijna elke Linux-LPE vereist een timingvenster of een kernel-specifieke geheugenoffset. **Copy Fail heeft geen van beide nodig.** Het is een directe logische fout in `algif_aead`, de module die vanuit gebruikersruimte toegang geeft tot geauthenticeerde versleuteling via AF_ALG.

De keten gebruikt `splice()` om een page-cachepagina aan de bewerking toe te voegen en misbruikt daarna het AEAD-pad ter plaatse om **vier beheersbare bytes** naar die pagina te schrijven. De beschadigde pagina wordt **nooit als dirty gemarkeerd** en wordt dus nooit teruggeschreven naar schijf. Het bestand op schijf blijft intact. Controles van checksums en integriteit slagen daarom, terwijl de kopie in geheugen jouw wijziging bevat.

Eén **Python-script van 732 bytes** krijgt rootrechten op elke Linux-distributie die sinds 2017 is uitgebracht. De bug ontstond door een **optimalisatie uit 2017** in `algif_aead`. De patch uit 2026 draait die optimalisatie simpelweg terug. Mainline-commit `a664bf3d603d`.

*De bug zat bijna tien jaar in elke gangbare distributie. Een AI-tool vond hem in ongeveer een uur.*

### Dirty Frag: twee varianten die elkaar aanvullen

De naam Dirty Frag beschrijft de verwantschap precies. **Dirty Pipe overschrijft `struct pipe_buffer`. Dirty Frag overschrijft het `frag`-veld van `struct sk_buff`.**

Het gaat om **twee gekoppelde kwetsbaarheden**. Juist die koppeling is slim:

- **CVE-2026-43284** misbruikt dat `esp_input()` het copy-on-write-pad overslaat voordat het een gespliced fragment ter plaatse ontsleutelt. Hiervoor zijn rechten nodig om een **user-namespace** aan te maken. Sommige distributies beperken dat.
- **CVE-2026-43500** misbruikt dat `rxkad_verify_packet_1()` het fragment ter plaatse ontsleutelt. Deze variant vereist geen namespace-rechten, maar de module `rxrpc` ontbreekt op de meeste distributies. Ubuntu laadt deze standaard.

**Elke variant heeft afzonderlijk een blinde vlek. Samen vullen ze elkaar aan.** Als user-namespaces zijn toegestaan, wordt eerst het ESP-pad gebruikt. Als dat is geblokkeerd maar `rxrpc` aanwezig is, wordt het RxRPC-pad gebruikt. Eén exploitbinary werkt dan op verschillende distributies. De RxRPC-variant krijgt root door een veld in `/etc/passwd` leeg te maken, waarna PAM met `nullok` een leeg wachtwoord accepteert.

**Voor verdedigers is vooral dit relevant:** Dirty Frag werkt **ongeacht of `algif_aead` beschikbaar is**. De veelgebruikte Copy Fail-maatregel, waarbij je die module op een zwarte lijst zet, **beschermt helemaal niet tegen Dirty Frag**.

### Fragnesia: de patch die een bug veroorzaakte

Fragnesia valt dezelfde kwetsbaarheidsklasse aan als Dirty Frag, maar richt zich op het XFRM-pad **ESP-in-TCP**. Dit is het leerzaamste voorbeeld uit de reeks.

De kwetsbaarheid misbruikt een verkeerde verwerking van gedeelde page-fragmenten tijdens `skb`-coalescing. Een aanvaller voegt bestandspagina's via `splice()` toe aan een TCP-ontvangstwachtrij voordat de socket naar de modus voor het `espintcp`-protocol op de bovenste laag overschakelt. Zodra ESP-verwerking actief wordt, ontsleutelt de kernel de gegevens **ter plaatse**. Manipulatie van de AES-GCM-keystream beschadigt vervolgens de page cache. De aanvaller kan herhaaldelijk **één byte tegelijk schrijven** naar pagina's met bestanden in de cache.

De exploit krijgt root door de eerste bytes van `/usr/bin/su` te overschrijven met een kleine ELF-payload. **De wijziging bestaat alleen in geheugen en raakt het bestand op schijf nooit.**

Onbevoorrechte **user- en network-namespaces** geven `CAP_NET_ADMIN` binnen een geïsoleerde namespace. Daarna installeert `NETLINK_XFRM` een aangepaste security association.

*Sta even stil bij deze zin:* Fragnesia ontstond als **onbedoeld neveneffect van een van de patches voor de oorspronkelijke Dirty Frag-kwetsbaarheden**. De patch voor Dirty Frag veroorzaakte een nieuwe, zelfstandig exploiteerbare rootbug.

### CVE-2026-80521: de container-escape die kernelCTF won

De AF_UNIX-race maakt elk argument dat dit theoretisch is ongeldig.

De kwetsbaarheid is een **heap-use-after-free** in het garbagecollectionmechanisme voor `SCM_RIGHTS`-berichten, waarmee processen bestandsdescriptors aan elkaar doorgeven. Tijdens het verzamelen van een circulaire socketreferentie maakt een race een `struct unix_vertex` vrij, terwijl de SCC-ring van een overgebleven socket nog een verwijzing bevat. De volgende verzamelronde doorloopt die verouderde ring en verwijst naar vrijgegeven geheugen.

Waarom dit verder gaat dan Linux in het algemeen: **AF_UNIX vormt de basis voor lokale IPC.** Lokale databases, `systemd` en Docker zelf zijn ervan afhankelijk. DepthFirst meldt dat de kwetsbaarheid gevolgen heeft voor de meeste sandboxen op besturingssysteemniveau die op de kernel zijn gebouwd, **waaronder `nsjail`, `Firejail` en `Bubblewrap`**, en voor moderne containerruntimes.

DepthFirst won er op **24 juli 2026** **een plek in Google kernelCTF**. De bevestiging kwam op **5 augustus** in de categorie `lts-6.12.95`. Het bedrijf meldde de bug diezelfde dag aan `security@kernel.org` en hoorde dat **Kyle van OpenAI dezelfde bug had gemeld**. De upstream-patch werd op **6 augustus** opgenomen. Het onderzoek verscheen op **22 september**.

De onderzoekers publiceerden een werkende exploit voor **Ubuntu 26.04**, plus een tweede exploit voor een escape uit **Ubuntu 24.04** via CVE-2026-52910.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Diagram waarin een onbevoorrecht proces in een container een page-cachepagina beschadigt en zo een setuid-binary in geheugen wijzigt. Het proces verhoogt zijn rechten naar root en verlaat de containergrens via de hostkernel." >}}

## Waarom het advies voor maatregelen steeds tekortschiet

Verdedigers kregen dit jaar drie rondes aan workarounds. Elke ronde bleek gedeeltelijk onjuist.

| Maatregel | Wat deze stopt | Wat deze mist |
|---|---|---|
| Zet **`algif_aead`** op een zwarte lijst | Copy Fail | **Alles van Dirty Frag**, dat de module volledig negeert |
| Zet **`esp4`, `esp6`, `rxrpc`** op een zwarte lijst | Dirty Frag en Fragnesia | Teams die IPsec nodig hebben. Ook volledig nieuwe subsystemen worden gemist |
| Beperk **onbevoorrechte user-namespaces** | De ESP-varianten | Voor de RxRPC-variant is geen namespace nodig. AppArmor-beleid is slechts een **gedeeltelijke** maatregel |
| **Patch de kernel** | De gepatchte bug | De volgende bug en elke bug die een patch introduceert |

Er vallen twee patronen op.

**Ten eerste spreken de workarounds elkaar tegen.** Copy Fail wordt tegengegaan door `algif_aead` uit te schakelen. Dirty Frag werkt nadrukkelijk **ook wanneer** die module ontbreekt. Fragnesia vereist dat `esp4` en `esp6` zijn uitgeschakeld. Dat is een probleem voor iedereen die IPsec gebruikt. Er is geen enkele module-zwarte lijst die de hele familie afdekt.

**Ten tweede, en ernstiger, is patchen geen eenvoudige overwinning.** Fragnesia werd **geïntroduceerd door de patch voor Dirty Frag**. Elke patch kan nieuwe logische fouten veroorzaken. In dit subsysteem wordt een logische fout een root-exploit.

*De ongemakkelijke conclusie: al deze kwetsbaarheden zitten in de page cache, zijn bereikbaar vanuit onbevoorrechte code en zijn gevonden met tools die elk kwartaal beter worden. Geen enkele blokkeerlijst blijft volledig.*

## Het tegenargument, eerlijk beantwoord

Er is een redelijk bezwaar dat een rechttoe-rechtaan antwoord verdient: **hypervisors bevatten ook bugs.**

Het aanvalsoppervlak van KVM is echt. Google organiseert **kvmCTF** juist om zulke bugs te vinden en betaalt daar flinke bedragen voor:

| Niveau | Beloning |
|---|---|
| **Volledige VM-escape** | **$250,000** |
| Willekeurige geheugenschrijfactie | $100,000 |
| Willekeurige geheugenleesactie | $50,000 |
| Relatieve geheugenschrijfactie | $50,000 |
| Dienstweigering | $20,000 |
| Relatieve geheugenleesactie | $10,000 |

Beloningen stapelen niet. Het doelwit is een Linux-LTS-kernel met KVM en de gastmachine is Debian 12.5. Het doel is een **aanval van gast naar host**.

**Hyunwoo Kim, dezelfde onderzoeker die Dirty Frag vond, haalt ook KVM-beloningen binnen** en won de volledige $250,000 voor een VM-escape. De eerlijke samenvatting: beide lagen bevatten fouten en soms vindt dezelfde persoon ze.

**Vergelijk de omvang:**

| | Linux-kernel | KVM-hypervisor |
|---|---|---|
| **CVE's in 2026** | Bijna **6.000** | Een handvol. Individuele onderzoekers vinden er enkele per jaar |
| **Bereikbaar vanuit** | Elk onbevoorrecht proces via de systeemaanroepinterface | Alleen code die al in een gastmachine draait |
| **Aanvalsoppervlak** | Alles: netwerken, bestandssystemen, cryptografie, IPC en drivers | De interface voor virtuele apparaten en hypercalls |
| **Bugklasse** | Elke geheugenveiligheids- of logische fout in 30 miljoen regels | Beperkt tot de virtualisatiegrens |

*Het verschil is vele ordes van grootte, niet een factor twee. Daarom veranderen microVM's de risicoafweging.*

## Wat wel een echte grens biedt

Een **microVM** geeft elke workload een eigen **kernelinstantie** die draait op hardwarematige virtualisatie, in plaats van de hostkernel via namespaces te delen.

De stack heeft drie lagen die je moet kennen:

- **De CPU** biedt hardwaremechanismen om geheugengebieden van elkaar te isoleren.
- **KVM** stelt deze mechanismen beschikbaar aan de Linux-kernel, zodat de kernel als hypervisor werkt.
- **Een VMM (virtual-machinemonitor)**, zoals Firecracker of QEMU, gebruikt KVM om de gastmachine te maken en uit te voeren.

Omdat de gastmachine een eigen kernel uitvoert, brengt een kernel-exploit **in de gastmachine** alleen de gastmachine in gevaar. Er is geen gedeelde kernel om aan te vallen. Een aanvaller moet dan nog uit de hypervisor ontsnappen, het kleinere aanvalsoppervlak waar KVM-bugs zich bevinden.

In de praktijk zijn twee implementaties belangrijk. Beide staan in het advies van DepthFirst:

| Technologie | Aanpak | Opmerkingen |
|---|---|---|
| **Firecracker** | Speciaal gebouwde VMM met een minimaal apparaatmodel | Ontwikkeld door AWS voor isolatie van meerdere tenants op schaal |
| **Kata Containers** | OCI-compatibele runtime die een microVM gebruikt | Voert standaardcontainerimages uit met daaronder een VM-grens |

Voor de meeste teams is Kata de eenvoudigste overstap, omdat het de containerimages en tooling accepteert die al in gebruik zijn. **Firecracker heeft een kleiner aanvalsoppervlak**, omdat het veel minder apparaatemulatie biedt dan een algemene VMM.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Diagram dat containerisolatie via namespaces op een gedeelde kernel vergelijkt met microVM-isolatie waarbij elke workload een eigen kernel uitvoert boven op KVM en een virtuele-machinemonitor." >}}

## Wat je nu moet doen

Niet elke container heeft een microVM nodig. De keuze hangt af van **wie de code erin uitvoert**.

| Jouw situatie | Risico | Wat je doet |
|---|---|---|
| **Je voert je eigen code uit**, één tenant | Laag | Houd containers. Patch snel, laat capabilities vervallen en gebruik een alleen-lezenrootbestandssysteem |
| **Hosts met meerdere tenants**, shelltoegang voor gebruikers | **Hoog** | Verplaats niet-vertrouwde workloads naar microVM's. Dit geval noemt DepthFirst als eerste |
| **CI-runners die niet-vertrouwde PR's uitvoeren** | **Hoog** | Een pull request krijgt rootrechten op de runner. Isoleer elke job in een eigen VM |
| **Notebooks, agentsandboxen en serverless** | **Hoog** | Code van tenants wordt root op de host. Gebruik één microVM per tenant |
| **Kubernetes-clusters** | **Verhoogd** | De page cache wordt gedeeld op de host. Een pod met de juiste primitives brengt het knooppunt in gevaar en doorbreekt tenantgrenzen |

Het overkoepelende principe is eenvoudig. **Containers zijn uitstekende hulpmiddelen voor packaging en procesisolatie.** Ze zijn nooit ontworpen om vijandige code in te perken. De sector leende ze stilzwijgend voor die taak omdat ze handig en goedkoop waren.

### Verharding die altijd helpt

Niets hiervan vervangt een VM-grens. Al deze maatregelen halen wel eenvoudige aanvalspaden weg:

```bash
# Schakel de modules uit die door de page-cache-familie worden misbruikt, als ze niet nodig zijn
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Beperk niet-bevoorrechte gebruikersnaamruimten, zodat de ESP-varianten worden geblokkeerd
# Debian en Ubuntu: dit is een gedeeltelijke beperking, geen volledige oplossing
sysctl -w kernel.unprivileged_userns_clone=0

# Wis bij vermoedelijke uitbuiting de pagecache om gewijzigde binaries in het geheugen te verwijderen
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Eerste detectiesignalen
- Onverwachte unshare(CLONE_NEWUSER) vanuit een workload zonder legitieme reden
- NETLINK_XFRM-activiteit of XFRM-beveiligingsassociaties buiten IPsec-hosts
- Verzoeken om AF_ALG-sockets te koppelen
- Laden van esp4, esp6 of rxrpc op hosts zonder IPsec en AFS
```

> **Waarschuwing: `drop_caches` verwijdert de gewijzigde kopie uit het geheugen en wist daarmee de corruptie, maar verwijdert geen aanvaller die al rootrechten heeft verkregen. Behandel dit als incidentrespons, niet als herstelmaatregel.**

### Het probleem met het patchtempo

Zelfs met de beste bedoelingen is kernelpatching een race geworden:

- Bijna **6.000 CVE's** die dit jaar zijn gepubliceerd, overschrijden met hun aantal de meeste onderhoudsvensters.
- **Een patch introduceert een bug.** Fragnesia bewees dit in precies dit subsysteem.
- **De lijst met maatregelen veroudert.** In april was `algif_aead` het antwoord. In mei dekte het niets van Dirty Frag af.

*Snel patchen is noodzakelijk maar niet voldoende. De architectuur bepaalt of een gemiste patch een ingeperkt incident of een compromittering van de host veroorzaakt.*

## De moeilijkere vraag: wie is de tegenstander?

Het technische antwoord is duidelijk. Het strategische antwoord hangt af van een vraag die de meeste teams overslaan.

**Als je dreigingsmodel uitgaat van een nieuwsgierige gebruiker of een onvoorzichtige ontwikkelaar, blijven containers toereikend.** Voor een container-escape zijn lokale code-uitvoering en een kernel-exploit nodig. Geen van beide is vanzelfsprekend, en de operationele kosten om alles naar microVM's te verplaatsen zijn reëel.

**Als je dreigingsmodel een tegenstander omvat die code op jouw infrastructuur uitvoert, zijn containers nu een verkeersdrempel.** De conclusie van DepthFirst is het waard om letterlijk te citeren:

> "De drempel om deze kwetsbaarheden als wapen in te zetten is zo sterk gedaald dat we ervan moeten uitgaan dat aanvallers standaardcontainers naar believen kunnen ontsnappen."

Dit is een beveiligingsleverancier met een product om te verkopen die een specifieke architectuur aanbeveelt. De scepsis die dat verdient is terecht. **Het argument is echter niet afhankelijk van de leverancier.** Het aantal van 6.000 CVE's is openbaar, de exploits zijn gepubliceerd en de kernel wordt per ontwerp gedeeld.

*De eerlijke formulering: tegenover een aanvaller met een toegangspunt is de waarde van containers als grens aan het afnemen. Tegenover al het andere blijft hun waarde gelijk.*

## Het oordeel

**Containers blijven het juiste hulpmiddel voor packaging, deployment en procesisolatie. Ze vormen geen betrouwbare beveiligingsgrens meer tegen vijandige code.**

Drie uitspraken, gerangschikt naar zekerheid:

1. **De technische premisse staat vast.** Containers delen de hostkernel. Elk van de vier kwetsbaarheden in dit artikel doorbrak de grens vanaf een onbevoorrecht account. De exploits zijn openbaar.
2. **AI veranderde het tempo, niet het principe.** Kernel-LPE's hebben altijd bestaan. Een bug vinden kost nu ongeveer **een uur AI-scantijd** in plaats van maanden deskundig werk. Twee organisaties vonden onafhankelijk dezelfde zero-day op dezelfde dag.
3. **Migreren kost echt geld, maar niet migreren ook.** Firecracker en Kata brengen extra overhead, operationele complexiteit en nieuwe vaardigheden met zich mee. De afweging is duidelijk: accepteer de overhead of accepteer dat een kernelbug de host compromitteert.

**Als je infrastructuur voor meerdere tenants beheert of niet-vertrouwde code uitvoert, plan dan nu de migratie naar microVM's.** Niet omdat de hemel valt, maar omdat de trend duidelijk is en een migratie kwartalen duurt, geen weken.

**Als je containers met eigen code voor één tenant uitvoert, behoud ze dan.** Patch de kernel sneller dan je gewend bent, schakel modules uit die je niet nodig hebt en heroverweeg je keuze wanneer niet-vertrouwde code in beeld komt.

*Het tijdperk waarin de kernel zonder voorwaarden als vertrouwde grens gold, loopt ten einde. Infrastructuur die ervan uitgaat dat de kernel wordt gecompromitteerd, overleeft die compromittering.*

## Belangrijkste punten

- **Containers delen de hostkernel.** Isolatie komt van namespaces via de systeemaanroep `clone`, niet van hardwarevirtualisatie. Een kernelbug is daarom ook een containerbug.
- **Vier kwetsbaarheden uit 2026 doorbraken de grens** vanaf onbevoorrechte lokale accounts: Copy Fail, Dirty Frag, Fragnesia en CVE-2026-80521. Alle vier richten zich op de page cache.
- **Per september 2026 waren bijna 6.000 kernel-CVE's** gepubliceerd. AI-tools versnellen de vondst. **Copy Fail werd in ongeveer een uur scantijd gevonden.**
- **De patch voor Dirty Frag introduceerde Fragnesia.** Patching veroorzaakte een nieuwe rootbug in hetzelfde subsysteem.
- **De Copy Fail-workaround stopt Dirty Frag niet.** Met `algif_aead` op een zwarte lijst dek je één kwetsbaarheid af, maar niets anders uit de familie.
- **CVE-2026-80521 brak ook `nsjail`, `Firejail` en `Bubblewrap`**, niet alleen containerruntimes.
- **MicroVM's veranderen de risicoafweging** doordat elke workload een eigen kernel krijgt. KVM bevat bugs, maar het aanvalsoppervlak is vele ordes kleiner.
- **Kies op basis van wie de code uitvoert.** Eigen code in een container voor één tenant vormt een laag risico. Niet-vertrouwde code op een gedeelde host vormt een risico op compromittering van de host.

## Volgende stappen

1. **Lees de analyse die het probleem schetst** en de gepubliceerde exploit: **[Containers zijn geen beveiligingsgrens meer - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Bekijk het gezaghebbende advies en de maatregelen** voor de Copy Fail-familie: **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Lees de technische uitleg van Dirty Frag** om de koppeling te begrijpen en te zien waarom de maatregel met `algif_aead` faalt: **[Technische uitleg van Dirty Frag](https://github.com/V4bel/dirtyfrag)**
4. **Bekijk de regels en beloningsniveaus van kvmCTF** om de omvang van het hypervisor-aanvalsoppervlak te zien: **[Overzicht van kvmCTF](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Beoordeel deze CVE's in je eigen omgeving** met onze client-side tool: **[Rekenhulp voor CVSS v3.1](/cvss-calculator/)**
6. **Verhard wat je nu uitvoert**: **[Je Docker- en Kubernetes-omgeving beveiligen](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Lees meer over de isolatieafweging**: **[Docker versus virtuele machines 2026](/articles/docker-vs-vms/)**
8. **Beperk rechten waar je geen grens kunt toevoegen**: **[Toegangsbeheer met minimale rechten op Linux beheersen](/articles/mastering-least-privilege-access-control-linux/)**

## Gerelateerde artikelen

| Artikel | Onderwerp |
|---|---|
| **[Docker versus virtuele machines 2026](/articles/docker-vs-vms/)** | De architectuurvergelijking achter dit artikel, met afwegingen voor prestaties en beveiliging |
| **[Je Docker- en Kubernetes-omgeving beveiligen](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Praktische beveiliging van de containerlaag, ook zinvol binnen een microVM |
| **[Docker in LXC op Proxmox: betrouwbaarheid, bewijs en migratie naar VM's](/articles/docker-in-lxc-proxmox-reliability/)** | Geneste containers en bewijs, en wanneer een workload naar een volledige VM moet |
| **[Virtualisatie begrijpen: concepten en toepassingen](/articles/understanding-virtualization_-concepts-and-applications/)** | De basis van hypervisors, inclusief de CPU-functies die microVM's nodig hebben |
| **[Toegangsbeheer met minimale rechten op Linux beheersen](/articles/mastering-least-privilege-access-control-linux/)** | Rechten verlagen die een escape zou opleveren en zo de impact beperken |

## Bronnen

1. [Containers zijn geen beveiligingsgrens meer - DepthFirst (Zhenpeng Lin, 22 september 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Officiële bekendmaking van Copy Fail en analyse van de exploit](https://copy.fail/)
4. [Technische uitleg van Dirty Frag - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia: lokale Linux-kernelprivilege-escalatie via ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [Overzicht en beloningsniveaus van kvmCTF - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [NVD-vermelding voor CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Upstream mainline-fixcommit voor Copy Fail](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Ubuntu-beveiligingsbericht over beschikbare oplossingen voor Copy Fail](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [KernelCTF-exploits en inzendingen - Google Security Research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)

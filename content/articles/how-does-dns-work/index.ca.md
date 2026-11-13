---
title: "Com funciona el DNS: DNS arrel, importància i resolució de problemes"
draft: false
toc: true
date: 2023-07-20
lastmod: 2026-11-13
description: "Descobreix com funcionen el DNS i el DNS arrel, la seva jerarquia, el procés de resolució, la memòria cau i el diagnòstic."
genre: ["Fonaments del DNS", "DNS arrel", "Sistema de noms de domini", "Resolució DNS", "Jerarquia DNS", "Memòria cau DNS", "Resolució de problemes del DNS", "Registres DNS", "Gestió del DNS", "Ordres DNS"]
tags: ["DNS", "DNS arrel", "Sistema de noms de domini", "Resolució DNS", "Jerarquia DNS", "Memòria cau DNS", "Registres DNS", "Gestió del DNS", "Resolució de problemes del DNS", "xarxes", "infraestructura d'Internet", "adreces IP", "accés als llocs web", "consulta recursiva", "servidors de noms autoritatius", "TTL", "mecanismes de memòria cau", "buidar la memòria cau DNS", "servidors DNS arrel", "encaminament anycast", "ICANN", "col·laboració DNS", "registre A", "registre AAAA", "registre CNAME", "registre MX", "registre TXT", "registre SRV", "registre NS", "registre PTR", "registre SOA", "ordres de diagnòstic DNS", "Windows", "macOS", "Linux", "Símbol del sistema", "terminal del sistema"]
cover: "/img/cover/An_image_depicting_interconnected_computer_ne.webp"
coverAlt: "Imatge de xarxes informàtiques interconnectades amb noms de domini i adreces IP, que representa el funcionament del DNS i del DNS arrel."
coverCaption: "Descobreix el DNS i domina el sistema de noms de domini"
---

## Com funcionen el DNS i el DNS arrel

### Introducció

El Domain Name System (DNS) és una part essencial de la infraestructura d'Internet. Permet accedir als llocs web amb noms de domini en lloc d'adreces IP. Funciona com una agenda que tradueix noms de domini llegibles per les persones en adreces IP que entenen els ordinadors. El DNS arrel és el nucli d'aquest sistema jeràrquic i distribuït. Aquest article explica el funcionament del DNS, del DNS arrel i dels registres associats als dominis.

{{< youtube id="mpQZVYPuDGU" >}}

## El Domain Name System (DNS)

El **Domain Name System (DNS)** és un sistema de noms descentralitzat que associa noms de domini amb adreces IP. Permet accedir als llocs web i altres recursos d'Internet escrivint un nom al navegador. El DNS evita haver de memoritzar adreces IP complexes.

### Jerarquia DNS

El DNS funciona amb una estructura jeràrquica de diversos nivells. A dalt hi ha la zona arrel, seguida dels dominis de nivell superior (TLD), els dominis de segon nivell i els subdominis. Cada nivell contribueix al nom complet. A `www.example.com`, «www» és el subdomini, «example» és el domini de segon nivell i «com» és el TLD.

### Procés de resolució DNS

Quan escrius un nom de domini al navegador, comença la resolució DNS. El navegador envia una consulta a un resolvedor DNS, que normalment proporciona el proveïdor de serveis d'Internet (ISP). El resolvedor segueix diversos passos per resoldre el nom i obtenir l'adreça IP corresponent.

1. **Memòria cau DNS local**: el resolvedor primer busca el nom de domini i l'adreça IP sol·licitats a la memòria cau local. Si hi troba les dades, retorna el resultat sense fer més consultes.

2. **Consulta recursiva**: si no troba les dades a la memòria cau, inicia una consulta recursiva. Primer contacta amb els servidors DNS arrel, responsables de la zona «.» (punt). Aquests servidors retornen les adreces IP dels servidors TLD del domini sol·licitat.

3. **Consulta TLD**: el resolvedor contacta amb els servidors TLD identificats al pas anterior i demana les adreces IP dels servidors de noms autoritatius del domini.

4. **Consulta al servidor de noms autoritatiu**: el resolvedor consulta els servidors autoritatius que ha rebut dels servidors TLD. Aquests servidors contenen els registres autoritatius del domini i responen amb l'adreça IP associada al nom.

5. **Resposta al client**: el resolvedor rep l'adreça IP dels servidors autoritatius i la retorna al navegador. Aleshores, el navegador es pot connectar al servidor web amb aquesta adreça.

### Memòria cau DNS

Els resolvedors DNS utilitzen memòria cau per millorar el rendiment i reduir la càrrega dels servidors DNS. Després de rebre una resposta, el resolvedor desa localment l'associació entre el nom de domini i l'adreça IP. Les consultes posteriors del mateix nom es poden resoldre directament des de la memòria cau.

La memòria cau funciona en diversos nivells, inclosos el resolvedor local, el de l'ISP i dispositius com els encaminadors i els sistemes operatius. El valor Time-to-Live (TTL) de la resposta DNS determina quant de temps es conserva un registre. Quan el TTL caduca, el resolvedor elimina el registre i fa una consulta nova.

#### Buidar la memòria cau DNS local

Buidar la memòria cau DNS ajuda a resoldre alguns problemes i fa que el sistema obtingui registres actualitzats. A continuació s'indica com fer-ho en diferents sistemes operatius:

##### Windows

Per buidar la memòria cau DNS a Windows:

1. Prem `Win + R`, escriu `cmd` i prem Retorn per obrir el Símbol del sistema.

2. Escriu l'ordre següent i prem Retorn:

```bash
ipconfig /flushdns
```

Aquesta ordre buida la memòria cau del resolvedor DNS de Windows.

##### macOS

Per buidar la memòria cau DNS a macOS:

1. Obre Terminal des d'Aplicacions > Utilitats o cerca'l amb Spotlight.

2. Escriu l'ordre següent a Terminal i prem Retorn:

```bash
sudo killall -HUP mDNSResponder
```

Aquesta ordre reinicia mDNSResponder, el procés que gestiona la resolució DNS a macOS.

##### Linux

El mètode per buidar la memòria cau DNS a Linux depèn de la distribució i del resolvedor DNS. Aquests són dos mètodes habituals:

1. **Sistemes basats en systemd (com Ubuntu i Fedora)**:

Obre Terminal i executa l'ordre següent amb privilegis d'administrador:

```bash
sudo systemd-resolve --flush-caches

```

Aquesta ordre buida la memòria cau DNS als sistemes que utilitzen systemd-resolved com a resolvedor.

2. **Sistemes sense systemd**:

Obre Terminal i executa l'ordre següent amb privilegis d'administrador:

```bash
sudo /etc/init.d/nscd restart

```

Aquesta ordre reinicia Name Service Cache Daemon (nscd), que gestiona la memòria cau DNS en distribucions Linux sense systemd.

Aquests passos són orientatius. Les ordres i els mètodes poden variar segons la versió del sistema operatiu. Buidar la memòria cau DNS pot resoldre alguns problemes, però no tots els problemes de connectivitat de xarxa.

## Com funciona el sistema DNS arrel

El sistema DNS arrel és una part fonamental de la infraestructura DNS. A continuació expliquem com funciona:

### 1. Zona arrel i servidors arrel

El sistema DNS arrel comença amb la **zona arrel**, el nivell superior de la jerarquia DNS. Conté informació sobre els servidors de noms autoritatius de tots els dominis de nivell superior (TLD), com ara .com, .org, .net i els dominis de país, com .us i .uk.

El sistema consta de 13 servidors DNS arrel, identificats amb les lletres de la A a la M. Estan distribuïts geogràficament per garantir redundància i fiabilitat.

### 2. Encaminament anycast

Per gestionar el gran volum de trànsit DNS, els servidors arrel utilitzen **encaminament anycast**. Diversos servidors comparteixen la mateixa adreça IP, però es troben en ubicacions diferents. Les condicions de la xarxa dirigeixen cada consulta al servidor adequat i distribueixen la càrrega.

Quan un usuari inicia una consulta DNS, anycast la dirigeix al servidor arrel disponible més proper. La infraestructura de xarxa tria la ruta més curta segons les condicions de la xarxa. Anycast distribueix la càrrega i ajuda a evitar colls d'ampolla.

### 3. Resolvedors DNS recursius

Quan un resolvedor DNS rep una consulta per un nom de domini, comença una resolució recursiva i contacta amb un dels servidors arrel.

El servidor arrel respon amb una referència a les adreces IP dels servidors de noms TLD responsables del TLD sol·licitat. Aquests servidors contenen informació sobre els servidors autoritatius dels dominis del TLD.

### 4. Referències i servidors de noms autoritatius

Després de rebre la referència del servidor arrel, el resolvedor contacta amb el servidor de noms TLD corresponent.

El servidor TLD respon amb una altra referència que inclou les adreces IP dels servidors de noms autoritatius del domini sol·licitat.

Després, el resolvedor demana als servidors autoritatius l'adreça IP associada al nom de domini.

### 5. Memòria cau i TTL

Durant la resolució DNS, la memòria cau millora el rendiment i redueix la càrrega dels servidors. Els resolvedors desen les associacions entre noms de domini i adreces IP.

Els registres DNS es conserven a la memòria cau durant el temps indicat pel valor Time-to-Live (TTL). El TTL especifica quant de temps és vàlid un registre. Quan caduca, el resolvedor l'elimina i fa una consulta nova per obtenir l'adreça IP actualitzada.

### 6. Col·laboració i gestió

El sistema DNS arrel es gestiona mitjançant la col·laboració entre Internet Corporation for Assigned Names and Numbers (ICANN) i operadors dels servidors arrel.

ICANN supervisa la gestió i coordinació generals del DNS i col·labora amb els operadors dels servidors arrel. Junts mantenen el fitxer de la zona arrel, que conté informació sobre els 13 servidors DNS arrel i les seves adreces IP.

operadors dels servidors arrel s'encarrega del funcionament i la disponibilitat dels servidors arrel. Això contribueix a l'estabilitat i la resiliència de la infraestructura DNS.

El sistema DNS arrel és el punt de partida de la resolució DNS. Permet associar noms de domini amb adreces IP i facilita l'accés als llocs i recursos d'Internet.

#### Els 13 servidors DNS arrel

Els 13 servidors DNS arrel s'identifiquen amb les lletres de la A a la M. Cada servidor s'allotja en diferents ubicacions físiques per proporcionar redundància i tolerància a fallades. Gestionen consultes de la zona arrel, inclosos els TLD .com, .org i .net, i els dominis de país .us i .uk.

#### ICANN i la gestió del DNS arrel

Internet Corporation for Assigned Names and Numbers (**ICANN**) gestiona i coordina el DNS i l'assignació d'adreces IP. Col·labora amb operadors dels servidors arrel per garantir l'estabilitat i la seguretat del DNS arrel. Junts mantenen el fitxer de zona arrel amb informació sobre els 13 servidors i les seves adreces IP.

______

## Tipus de registres DNS i les seves funcions

{{< youtube id="HnUDtycXSNE" >}}

Els registres DNS són components essencials del Domain Name System (DNS) i proporcionen informació diversa associada a un nom de domini. Aquests són alguns tipus habituals i les seves funcions:

| Tipus de registre | Descripció | Exemple |
|-------------|-----------------------------------------------------------------------------|-------------------------------------------|
| A | Associa un nom de domini amb una adreça IPv4. | `example.com     IN A 192.0.2.1` |
| AAAA | Associa un nom de domini amb una adreça IPv6. | `example.com     IN AAAA 2001:db8::1` |
| CNAME | Associa un àlies (nom canònic) amb el nom de domini real. | `www.example.com IN CNAME example.com` |
| MX | Indica els servidors de correu que reben els missatges del domini. | `example.com     IN MX 10 mail.example.com` |
| TXT | Emmagatzema text arbitrari, sovint per a SPF, DKIM o la verificació del domini. | `example.com     IN TXT "v=spf1 a mx -all"`|
| NS | Indica els servidors de noms autoritatius del domini. | `example.com     IN NS ns1.example.com` |
| SOA | Especifica propietats generals de la zona (registre start of authority). | `example.com     IN SOA ns1.example.com` |
| SRV | Defineix la ubicació d'un servei específic del domini. | `_service._proto.example.com IN SRV 10 20 5060 target.example.com` |
| PTR | Associa una adreça IP amb un nom de domini (cerca DNS inversa). | `1.2.0.192.in-addr.arpa IN PTR example.com` |

### 1. Registre A (registre d’adreça)

El **registre A** associa un nom de domini amb una adreça IPv4. És el tipus de registre DNS més bàsic i habitual. Quan introdueixes un domini al navegador, el registre A ajuda a trobar l'adreça IP del servidor web que allotja el lloc.

### 2. Registre AAAA (registre d’adreça IPv6)

El **registre AAAA** té la mateixa funció que el registre A, però associa el domini amb una adreça IPv6. Amb la transició a IPv6, aquest registre és cada vegada més important per a les xarxes IPv6.

### 3. Registre CNAME (registre de nom canònic)

El **registre CNAME** crea un àlies o nom canònic per a un domini. S'utilitza quan vols dirigir un domini o subdomini cap a un altre. Per exemple, pots crear un CNAME que faci apuntar "www" a "mywebsite.com".

### 4. Registre MX (registre d’intercanvi de correu)

El **registre MX** especifica el servidor de correu que rep els missatges entrants d'un domini. Pots definir diversos registres MX amb prioritats que determinen l'ordre d'intent quan el servidor principal no està disponible.

### 5. Registre TXT (registre de text)

El **registre TXT** emmagatzema informació de text associada a un domini. S'utilitza sovint per verificar dominis, publicar registres SPF (Sender Policy Framework) per a l'autenticació del correu i conservar notes o informació general.

### 6. Registre SRV (registre de servei)

El **registre SRV** defineix la ubicació d'un servei o recurs concret dins del domini. S'utilitza per a VoIP, missatgeria instantània i aplicacions que necessiten localitzar servidors o serveis específics.

### 7. Registre NS (registre de servidor de noms)

El **registre NS** especifica els servidors de noms autoritatius del domini. Aquests servidors contenen els registres DNS del domini. El resolvedor consulta els registres NS per localitzar els servidors autoritatius.

### 8. Registre PTR (registre de punter)

El **registre PTR** associa una adreça IP amb un nom de domini en una cerca DNS inversa. S'utilitza sovint per comprovar la identitat d'un servidor de correu i ajudar a prevenir el correu brossa. Les cerques inverses ajuden a validar l'autenticitat del servidor.

### 9. Registre SOA (registre d’inici d’autoritat)

El **registre SOA** conté informació administrativa del domini, com ara el servidor de noms autoritatiu principal, l'adreça de correu de l'administrador i diversos paràmetres temporals dels registres DNS.

Aquests són només alguns dels molts tipus de registres DNS. Cadascun té una funció concreta i contribueix a resoldre els noms de domini cap als recursos associats de manera eficient i precisa.

______

## Ordres de diagnòstic DNS per a diferents sistemes operatius

Quan hi ha problemes de DNS, les ordres de diagnòstic ajuden a trobar-ne la causa. Aquestes són algunes ordres habituals per sistema operatiu:

### Windows

#### 1. `ipconfig /flushdns`

Aquesta ordre buida la memòria cau DNS de Windows i pot resoldre problemes causats per registres antics o incorrectes. Obre el Símbol del sistema i executa-la.

#### 2. `ipconfig /all`

`ipconfig /all` mostra informació detallada de les interfícies de xarxa de Windows, inclosos els servidors DNS configurats. Permet comprovar si s'utilitzen els servidors correctes.

### macOS

#### 1. `sudo killall -HUP mDNSResponder`

Aquesta ordre reinicia mDNSResponder a macOS, el procés que gestiona la resolució DNS. Pot actualitzar la configuració i resoldre alguns problemes. Obre Terminal i executa-la amb privilegis d'administrador.

#### 2. `nslookup`

L'ordre `nslookup` permet consultar registres DNS, provar la resolució i comprovar la connexió als servidors DNS. A Terminal, executa `nslookup` seguit del nom de domini o l'adreça IP que vols investigar.

### Linux

#### 1. `systemd-resolve --flush-caches`

En sistemes Linux que utilitzen systemd com a resolvedor DNS, `systemd-resolve --flush-caches` buida la memòria cau DNS. Pot resoldre problemes causats per entrades antigues. Obre Terminal i executa l'ordre amb privilegis d'administrador.

#### 2. `dig`

`dig` és una eina versàtil de diagnòstic DNS disponible a Linux. Proporciona informació detallada sobre consultes, respostes i configuració dels servidors. Utilitza `dig` per consultar registres, provar la resolució i diagnosticar problemes. A Terminal, executa `dig` seguit del domini o l'adreça IP que vols investigar.

Aquestes ordres ajuden a diagnosticar i resoldre problemes DNS en diferents sistemes operatius. Permeten revisar la configuració DNS, els servidors utilitzats i els problemes de connectivitat.

Les ordres i opcions poden variar segons la versió del sistema operatiu i la distribució. Consulta la documentació de la versió que utilitzes per obtenir-ne els detalls.
______


## Conclusió

El Domain Name System (DNS) i el DNS arrel tenen un paper essencial en el funcionament d'Internet. El DNS permet accedir als llocs amb noms de domini fàcils de llegir, i el DNS arrel és la base de tota la jerarquia DNS. Entendre com funcionen ajuda a navegar per la web i a conèixer la infraestructura dels serveis en línia.

______

## Referències

- [DNS a la Viquipèdia](https://en.wikipedia.org/wiki/Domain_Name_System)
- [Com funciona el DNS, segons Cloudflare](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [Lloc web oficial d'ICANN](https://www.icann.org/)
- [operadors dels servidors arrel](https://www.root-servers.org/)

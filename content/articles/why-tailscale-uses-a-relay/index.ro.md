---
title: "De ce folosește Tailscale un releu: conexiuni directe, DERP și relee peer"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Află de ce folosește Tailscale un releu, cum să citești rezultatele status și netcheck și când să investighezi o conexiune DERP sau printr-un releu peer."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "releu Tailscale", "DERP", "releu peer Tailscale", "conexiune directă", "WireGuard", "traversare NAT", "NAT dificil", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "performanță VPN", "acces la distanță", "tailnet", "rețea homelab", "latență releu", "criptare end-to-end"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Două laptopuri aflate pe insule separate schimbă pachete criptate printr-un releu central, în timp ce o rută directă este întreruptă."
coverCaption: ""
---

**Tailscale folosește un releu** atunci când dispozitivele nu au stabilit o conexiune directă. O conexiune DERP scurtă la pornire este normală. Folosirea persistentă a unui releu indică adesea condiții NAT sau reguli de firewall care afectează ruta dintre dispozitive. Conexiunile directe, DERP și cele prin relee peer păstrează toate criptarea end-to-end a WireGuard. [Tipuri de conexiuni Tailscale](https://tailscale.com/docs/reference/connection-types).

## Idei principale

- **Identifică ruta:** diferențiază conexiunile directe, DERP și releele peer.
- **Adună dovezi:** rulează sonde pentru peer-ul vizat și verificări de rețea la ambele capete.
- **Analizează tiparul:** compară perechile de dispozitive și condițiile de rețea.
- **Alege o modificare:** justific-o printr-o sarcină măsurată și un nou test.

## Înainte să începi

**Cerințe:** două dispozitive înregistrate și online, precum și un terminal cu interfața de linie de comandă Tailscale, sau **CLI**. Ai nevoie de acces de administrator numai dacă investigația duce la modificări de configurare.

**Durată estimată:** cinci minute pentru verificările de bază, apoi 15–20 de minute pentru exercițiul de comparație. **Dificultate:** începător pentru observare și mediu pentru modificări de rețea. Definește problema înainte de toate, de exemplu o copie de siguranță lentă sau un răspuns întârziat al terminalului.

## Conexiuni directe, DERP și releu peer

Un **tailnet** este rețeaua ta Tailscale. Dispozitivele încearcă să stabilească o conexiune UDP directă. Releele sunt disponibile când ruta directă nu funcționează. Tailscale verifică periodic din nou opțiunile de conectare. [Stabilirea unei conexiuni](https://tailscale.com/docs/reference/connection-types).

| Rută | Traseul traficului | Implicație obișnuită |
|---|---|---|
| **Directă** | Între cele două dispozitive | De obicei ruta preferată pentru performanță |
| **Releu DERP** | Prin infrastructura de relee Tailscale | Adaugă un intermediar când accesul direct nu funcționează |
| **Releu peer** | Printr-un dispozitiv configurat în tailnet | O opțiune alternativă administrată de tine |

**Performanța DERP** depinde parțial de ruta suplimentară și de capacitatea partajată a serviciului. Tailscale documentează limite de debit pentru distribuirea echitabilă a resurselor DERP. Nu există o viteză universală a releului care să permită estimarea duratei transferurilor de fișiere. [Depanarea performanței Tailscale](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Înțelege negocierea conexiunii

**Traversarea NAT** este procesul de stabilire a unei rute utilizabile prin dispozitive care traduc adrese. Tailscale începe comunicarea prin DERP în timp ce negociază o rută directă. Dacă conexiunea directă nu funcționează, un releu peer configurat și disponibil oferă o altă opțiune. Tailscale verifică opțiunile din nou în timp. [Stabilirea unei conexiuni](https://tailscale.com/docs/reference/connection-types).

**NAT dificil** descrie un comportament de mapare care complică traversarea. Contează condițiile de la ambele capete. Două dispozitive din spatele unor routere diferite nu se comportă neapărat la fel, chiar dacă ambele rețele folosesc adrese private. [Conectivitatea dispozitivelor](https://tailscale.com/docs/reference/device-connectivity).

Pentru **un laptop folosit în deplasare**, ruta spre serverul de acasă se poate schimba când treci de la Wi-Fi-ul de acasă la o rețea de hotel. Notează rețeaua folosită în timpul observației. O conexiune directă de ieri nu demonstrează care este ruta de azi.

## Verifică conexiunea actuală

Înlocuiește **`home-server`** cu numele Tailscale sau adresa peer-ului:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** verifică legătura cu peer-ul indicat. **`tailscale status`** listează peer-ii și detaliile conexiunilor. **`tailscale netcheck`** raportează condițiile de rețea de pe dispozitivul pe care rulezi comanda. [Referința CLI Tailscale](https://tailscale.com/docs/reference/tailscale-cli) descrie aceste comenzi.

| Indicator în rezultat | Interpretare |
|---|---|
| **`direct`** | Traficul către acest peer folosește o rută directă |
| **`relay`** | Traficul către acest peer trece prin DERP |
| **`peer-relay`** | Traficul folosește un releu peer configurat |
| **Un prim pong DERP** | Verifică rezultatele următoare înainte să decizi că ruta a rămas prin releu |

Aceste etichete provin din [documentația tipurilor de conexiuni](https://tailscale.com/docs/reference/connection-types). **Generează mai întâi trafic**, apoi verifică peer-ul dorit. Comenzile de mai sus sunt exemple, nu rezultate înregistrate de benchmark.

## Interpretează schimbarea unei rute

Această **secvență ilustrativă** omite adresele și timpii pentru a evidenția schimbarea conexiunii:

```text
Primul răspuns:      prin DERP
Răspuns ulterior:    printr-un endpoint direct
Status ulterior:     direct
```

**Interpretare:** negocierea a reușit în timpul acestei observații. Primul răspuns, luat singur, ar fi dus la un diagnostic greșit. Dacă răspunsurile și statusul următoare indică în continuare un releu, notează folosirea persistentă a releului pentru această pereche de dispozitive și această perioadă de testare.

**Domeniul sondei:** un ping Tailscale reușit confirmă conectivitatea cu peer-ul pentru acea sondă. Nu demonstrează că tabloul de bord, serviciul de fișiere sau demonul SSH acceptă traficul aplicației. Testează separat aplicația cu probleme înainte să declari problema rezolvată.

## Ce îți spune netcheck

Rulează **`tailscale netcheck` pe ambele dispozitive**. Compară aceste câmpuri cu [referința privind conectivitatea dispozitivelor](https://tailscale.com/docs/reference/device-connectivity):

| Câmp | Interpretare utilă |
|---|---|
| **`UDP`** | Dacă sonda a observat conectivitate UDP de ieșire |
| **`MappingVariesByDestIP`** | Mapările externe variabile pot indica o traversare NAT dificilă |
| **`IPv6`** | Dacă dispozitivul are conectivitate IPv6 utilizabilă |
| **`PortMapping`** | Dacă este disponibil un mecanism acceptat de mapare a porturilor |

**Un singur câmp nu oferă un verdict.** Disponibilitatea unui mecanism de mapare nu demonstrează că ruta către un anumit peer funcționează. Nici eticheta releului nu identifică routerul care a cauzat problema. Compară ambele capete și rezultatele reale ale comenzilor ping.

**NAT-ul operatorului** contează când traducerea din amonte este în afara controlului tău, așa cum explicăm în articolul despre [redirecționarea porturilor T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). Nu presupune că fiecare conexiune aflată în spatele NAT-ului operatorului se comportă la fel la traversare.

## Compară trei perechi de dispozitive

Dacă ai unul disponibil, folosește un **al treilea dispozitiv înregistrat** pentru a aduna mai multe dovezi. Tiparul următor este ipotetic, nu un rezultat măsurat:

| Pereche de dispozitive | Rută observată |
|---|---|
| **Laptop către serverul de acasă** | DERP |
| **Laptop către alt server** | Directă |
| **Serverul de acasă către alt server** | DERP |

**Ipoteză de lucru:** investighează mai întâi rețeaua serverului de acasă, deoarece ambele rute observate care îl implică au rămas prin releu. Acesta este un indiciu, nu o dovadă. Fiecare pereche negociază separat, iar serverul de comparație are propriile condiții de rețea.

**Următoarea observație:** colectează rezultatele netcheck pe toate cele trei dispozitive și repetă testul dintre laptop și serverul de acasă dintr-o altă rețea pe care o controlezi. Dacă ruta se schimbă, notează exact ce rețea ai schimbat. Nu atribui rezultatul unei anumite reguli de firewall înainte să o testezi.

**Exercițiu:** conexiunea dintre laptop și serverul de acasă este directă, dar transferul de fișiere rămâne lent. O explicație bazată pe releu nu mai corespunde acestei observații. Înainte să schimbi setările releului, verifică încărcarea conexiunii de upload, sarcina serverului, stocarea și comportamentul aplicației.

## Alege o modificare bine țintită

Începe cu un **test comparativ** într-o altă rețea pe care o controlezi. Dacă același peer devine direct, ai dovezi utile despre ruta rețelei inițiale. Verifică restricțiile UDP și configurația NAT înainte să schimbi setări DNS sau de aplicație fără legătură.

**Schimbă o singură variabilă**, repetă verificările și măsoară aceeași sarcină. Notează direcția transferului, dimensiunea fișierului, timpul scurs și tipul conexiunii. Astfel poți separa îmbunătățirea rutei de o schimbare independentă a sarcinii serverului sau a stocării.

**Modificările de firewall** trebuie să respecte îndrumările specifice platformei și dovezile colectate. Deschiderea unui port de aplicație către Internetul public nu îmbunătățește, în sine, ruta de transport Tailscale. Limitează modificările la traficul necesar și la rețeaua pe care o administrezi. [Îndrumări Tailscale pentru firewall](https://tailscale.com/docs/integrations/firewalls).

| Constatare | Modificare de evaluat |
|---|---|
| **Sonda UDP eșuează** | Verifică restricțiile UDP de ieșire din această rețea |
| **Maparea diferă în funcție de destinație** | Verifică comportamentul NAT pe echipamentele pe care le administrezi |
| **Rută directă, aplicație lentă** | Investighează gazda, conexiunea de bază și sarcina |
| **Releu funcțional, experiență acceptabilă** | Păstrează configurația și documentează valoarea de referință |

*Preferă o îmbunătățire măsurată în loc să schimbi setările doar pentru a elimina eticheta releului.*

## Evaluează un releu peer

Un **releu peer** necesită o gazdă potrivită, un port UDP accesibil și o politică de acces care îi permite utilizarea. Atât releul, cât și clienții participanți au nevoie de Tailscale 1.86 sau o versiune ulterioară. Verifică platformele gazdă acceptate înainte să aloci un dispozitiv. [Cerințe pentru releul peer](https://tailscale.com/docs/features/peer-relay).

**Amplasarea îi determină utilitatea.** Un dispozitiv aflat în spatele aceleiași limite de rețea inaccesibile nu îi ajută pe ceilalți peer-i până când portul releului devine accesibil.

**Costul întreținerii:** cineva trebuie să mențină releul online, actualizat și suficient de performant. Pentru administrare ocazională cu latență acceptabilă, compară acest efort cu beneficiul măsurat. Pentru transferuri mari repetate, măsoară sarcina prin releul propus înainte să îl adopți.

## Verifică efectele traficului partajat

**Traficul agregat** merită atenție când un router de subrețea sau un nod de ieșire transportă mai multe sarcini prin DERP. Tailscale documentează cazuri în care mult trafic retransmis întârzie traficul sensibil la latență care folosește aceeași conexiune. [Depanarea problemelor cu NAT dificil](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Exercițiu de comparație:** observă sesiunea interactivă înainte, în timpul și după o copie de siguranță mare. Păstrează aceeași pereche de endpoint-uri și notează ruta de fiecare dată. Întârzierile apărute în timpul transferului justifică investigarea sarcinii partajate, dar nu îi dovedesc cauza exactă.

**Alege următorul test** pe baza observației. Verifică saturarea legăturii și sarcina gazdei. Apoi evaluează o rută directă sau separarea serviciilor sensibile la latență, dacă topologia permite. Nu trata un simptom DNS ca dovadă automată a unei erori de configurare DNS.

## Este un releu un nod de ieșire?

Un **nod de ieșire** direcționează traficul Internet general al unui client printr-un dispozitiv selectat din tailnet. Un releu transportă trafic între peer-ii Tailscale. Alegerea unui nod de ieșire nu garantează o rută directă către acesta. [Documentația nodurilor de ieșire](https://tailscale.com/docs/features/exit-nodes).

## Creează o înregistrare de diagnostic

Păstrează o **înregistrare scurtă înainte și după** pentru problema reală:

```text
Data și versiunile Tailscale:
Dispozitive sursă și destinație:
Rețelele folosite de fiecare dispozitiv:
Rutele inițială și stabilizată:
Observații netcheck de la ambele capete:
Sarcina, direcția și timpul scurs:
Singura modificare testată:
Rezultatul noului test:
Decizia de a păstra sau anula modificarea:
```

**Criteriu de finalizare:** înregistrarea leagă un simptom concret de observații, o ipoteză și un nou test măsurat. „Releul a dispărut” nu este suficient dacă aplicația rămâne lentă. „Copia de siguranță respectă timpul cerut prin DERP” este un rezultat valid dacă cerința este explicită.

**Folosește `tailscale netcheck` ca dovadă, nu ca verdict.** Comanda descrie rețeaua văzută de un singur dispozitiv. Ruta stabilizată depinde de o pereche de dispozitive și de o sarcină. Înainte să schimbi setările firewall sau NAT, înregistrează ambele capete, ultimul rând din `tailscale status` și măsurarea aplicației.

## Pași următori

Notează ruta către peer-ul important și testează sarcina înainte să schimbi setările de rețea. Pentru întrebarea separată despre cine operează infrastructura de coordonare, citește [Tailscale comparat cu Headscale](/articles/tailscale-vs-headscale-comparison-guide/).

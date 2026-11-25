---
title: "Meshtastic vs. MeshCore vs. Reticulum"
date: 2026-09-01
lastmod: 2026-11-25
toc: true
draft: false
description: "Compară Meshtastic, MeshCore și Reticulum în funcție de rutare, timp de emisie, infrastructură, transport și utilizare offline."
genre: ["LoRa", "Rețele mesh", "Comunicații fără infrastructură", "Comunicații de urgență", "Radioamatorism", "Software cu sursă deschisă", "Pregătire pentru dezastre", "Rețele wireless", "Confidențialitate", "Rețelistică"]
tags: ["meshtastic vs meshcore vs reticulum", "rețeaua Reticulum", "meshtastic", "meshcore", "reticulum", "lxmf", "rețea mesh LoRa", "comunicații fără infrastructură", "rnode", "radio cu pachete", "rețelistică independentă de transport", "rețele mesh", "comunicații de urgență", "rețea mesh comunitară", "timp de emisie LoRa", "flooding controlat", "limită de hopuri", "nod repetor", "server de chat", "aplicația Sideband", "nomadnet", "meshchat", "comunicații în caz de dezastru", "radio fără infrastructură", "protocol de rețea mesh", "rețea mesh regională", "inginerie RF"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Ilustrație care compară trei sisteme de rețea mesh prin noduri, antene și linii de conexiune pe un fundal întunecat și colorat, reprezentând caracteristicile lor distincte."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## Pe scurt

**Aceste trei proiecte nu rezolvă aceeași problemă.** Meshtastic și MeshCore sunt sisteme de rețea mesh LoRa cu filosofii de rutare diferite. Reticulum are un domeniu mai larg. Este un nivel de rețea independent de transport, care funcționează simultan prin LoRa, radio cu pachete, Wi-Fi, Ethernet, legături seriale și internet.

**Întrebarea potrivită nu este „care este cel mai bun?”.** Este „ce arhitectură se potrivește rețelei pe care vreau să o construiesc?”.

*Meshtastic se potrivește rețelelor ad hoc și utilizatorilor aflați în mișcare.* **MeshCore se potrivește infrastructurii fixe, construite intenționat.** **Reticulum se potrivește rețelelor care trebuie să conecteze transporturi diferite sau să unească rețele care altfel ar rămâne separate.** Majoritatea celor care construiesc o singură rețea LoRa regională au nevoie doar de una dintre primele două opțiuni.

______

## Definește rețeaua pe care o construiești

Înainte să compari protocoalele, notează ce trebuie să facă rețeaua. Un obiectiv util pentru majoritatea implementărilor comunitare și de comunicații de urgență arată astfel:

- **Funcționare fără licență**, astfel încât oricine să poată participa fără licență de radioamator
- **Hardware cu cost redus**, accesibil unei comunități care vrea să îl instaleze la scară
- **Consum redus de energie**, ideal susținut de energie solară sau baterii
- **Comunicare pe distanțe lungi** fără dependență de rețeaua celulară sau internet
- **Independență față de infrastructură**, rețeaua electrică, furnizorii de internet și operatorii telecom
- **Suficient de ușor pentru persoanele fără experiență radio** să îl configureze și să îl folosească
- **Potrivit pentru o comunitate**, nu doar pentru subsolul unui singur operator
- **Capabil să crească peste câteva noduri** fără să se destrame
- **Util în timpul întreruperilor infrastructurii**, când turnurile celulare și internetul nu funcționează
- **Livrare fiabilă înaintea distanței record**

Ține cont de această listă în continuarea articolului. Evaluăm fiecare compromis arhitectural în funcție de ea.

______

## Meshtastic

**Meshtastic** este cea mai matură și mai răspândită opțiune. Oferă multe avantaje pentru utilizatorul obișnuit.

- **Ecosistem matur**, dezvoltat activ de ani de zile
- **Comunitate mare**, Discord activ și documentație cuprinzătoare
- **Compatibilitate hardware extinsă** cu plăci LILYGO, Heltec, RAK și Seeed
- **Aplicații mobile bune** pentru iOS și Android
- **Ușor de început**, configurarea inițială durează sub 20 de minute
- **Suport bun pentru utilizatorii portabili și mobili** care intră și ies imprevizibil din rețea
- **Funcții GPS și de telemetrie** cu un ecosistem dezvoltat în jurul lor
- **Implementări existente** în majoritatea zonelor metropolitane, care fac adoptarea mai ușoară, pentru că te alături unei rețele în loc să construiești una de la zero

Pentru o analiză completă a rutării, compatibilității hardware și configurării Meshtastic față de MeshCore, consultă **[ghidul comparativ MeshCore și Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Acest articol se concentrează pe întrebarea arhitecturală cu cel mai mare impact în implementările mari: **floodingul controlat și limitele de hopuri**.

### Flooding controlat și importanța hopurilor

În **[inundarea controlată](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** din Meshtastic, un client obișnuit anulează o retransmisie în așteptare dacă aude mai întâi același pachet retransmis. `ROUTER` și `ROUTER_LATE` îl pot retransmite oricum. La `CLIENT_BASE`, excepția se aplică traficului către sau de la un favorit.

Contorul de salturi Meshtastic pornește implicit de la **3** și are maximum **7**. Din versiunea de firmware 2.7.11, infrastructura eligibilă poate [păstra contorul neschimbat](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/) după primul salt dacă releul anterior este un `ROUTER` sau `ROUTER_LATE` favorit. Fiecare retransmisie reală ocupă canalul.

O limită mai mare poate permite atingerea mai multor relee, dar nu obligă fiecare receptor să transmită. **Mai multe retransmisii** pot însemna:

- **Mai mult timp de emisie** pentru fiecare mesaj
- **Mai multe copii în eter** când mai multe relee eligibile transmit același pachet
- **Mai multă concurență** pentru canalul partajat
- **Risc mai mare de coliziuni** când mai multe radiouri transmit în aceeași fereastră
- **Consum mai mare al bateriei** la fiecare nod care recepționează și retransmite
- **Mai puțină capacitate disponibilă a canalului** pentru traficul real de mesaje

Capacitatea LoRa este limitată de timpul de emisie și de limitele regionale ale ciclului de lucru, nu de numărul de noduri. O rețea cu zece noduri active care transmit frecvent GPS și telemetrie poate satura un canal pe care cincizeci de senzori tăcuți abia l-ar folosi. De aceea, o rețea mesh densă, cu limită mare de hopuri, se degradează mai repede decât aceeași cantitate de noduri cu limită mai mică și intervale de telemetrie controlate.

Din Meshtastic 2.6, **mesajele directe** descoperă ruta prin inundare și apoi încearcă următorul salt învățat. Dacă acesta nu funcționează, pot reveni la inundare.

Pentru o rețea mică sau medie, precum cea a unui club de drumeții, rareori contează. Pentru o **rețea regională destinată acoperirii unui oraș sau a mai multor localități**, devine principala constrângere de proiectare.

______

## MeshCore

**Repetoarele dedicate** formează stratul fix de retransmisie al MeshCore. Radiourile client sunt terminale.

### Rolurile nodurilor

Implementările MeshCore sunt construite în jurul unor roluri distincte, nu al unui set plat de noduri echivalente:

- **Noduri companion sau client** cu o stație radio LoRa asociată unui telefon sau laptop, care comunică prin infrastructura apropiată când aceasta există
- **Repeatere** care redirecționează traficul între clienți și alte elemente de infrastructură și fac cea mai mare parte din munca de rutare
- **Servere de chat** (opționale) care găzduiesc conversații de grup și livrează mesaje stocate clienților când aceștia se reconectează

În MeshCore, primul **mesaj direct** poate folosi inundarea pentru a descoperi o rută. Următoarele pot urma acea rută și pot reveni la inundare în funcție de setări. **[Canalele de grup publice și private folosesc în continuare inundarea](https://docs.meshcore.io/faq/#5-general)** prin repetoarele eligibile. Radiourile client nu retransmit pachetele altor noduri.

### De ce se potrivește infrastructurii fixe

*Acesta este argumentul principal pentru MeshCore.* Modelul de flooding al Meshtastic are avantaje reale pentru rețele ad hoc și mobile: nu necesită planificare, nu există infrastructură de întreținut și gestionează bine nodurile care apar și dispar. Modelul de rutare MeshCore are avantajul când **utilizatorii instalează infrastructură în mod intenționat**.

O rețea construită în jurul unor repetoare cunoscute, amplasate la înălțime, îți permite să proiectezi acoperirea în mod deliberat, în loc să depinzi de nodurile care ajung întâmplător unele în raza celorlalte într-o anumită zi. Diferența contează pentru:

- **Noduri permanente pe acoperișuri** cu alimentare fiabilă
- **Turnuri** și infrastructură de comunicații existentă
- **Repeatere solare** în locații nesupravegheate
- **Locații montane sau înalte de retransmisie**
- **Infrastructură deținută de comunitate**, partajată între mai multe grupuri
- **Rețele regionale** care acoperă mai mult de un cartier
- **Comunicații de urgență** unde acoperirea previzibilă contează mai mult decât flexibilitatea

Leagă asta de principiile RF: **legăturile fiabile dintre elemente de infrastructură amplasate corect contează mai mult decât maximizarea câștigului antenei, puterii de transmisie sau razei teoretice.** **Ambele rețele beneficiază de relee bine amplasate.** Rolurile nodurilor și tipul traficului determină ce noduri retransmit.

______

## Argumentul nodurilor mobile și costul său

O sugestie frecventă sună așa: *„Meshtastic este mai bun pentru noduri mobile, MeshCore pentru noduri fixe, deci folosim Meshtastic pentru utilizatori și MeshCore ca backbone.”*

Pe hârtie pare atrăgător. În practică, combinarea celor două nu oferă automat avantajele ambelor, deoarece **Meshtastic și MeshCore folosesc arhitecturi de rutare și de rețea diferite și nu își schimbă mesaje între ele.** Conectarea lor adaugă un nivel de traducere între sisteme incompatibile, nu doar combină cele mai bune părți ale fiecăruia.

După conectare, gestionezi:

- **Două rețele separate**, fiecare cu topologia și comportamentul ei
- **Două modele de rutare** care nu partajează starea
- **Un nivel de traducere** care necesită dezvoltare și mentenanță continuă
- **Mai multă infrastructură** pentru găzduirea punții
- **Mai multă configurare** în două ecosisteme firmware, în loc de unul
- **Mai multe puncte de defectare**, deoarece puntea poate eșua independent de fiecare rețea mesh
- **Diagnosticare mai dificilă**, deoarece o eroare de livrare poate apărea în oricare rețea sau în puntea dintre ele

Înainte să adopți acest design, pune-ți o întrebare directă: **complexitatea suplimentară rezolvă o problemă pe care un singur protocol mesh bine reglat nu o poate rezolva?** Adesea, o implementare MeshCore configurată corect, cu câteva noduri companion potrivite pentru utilizatorii mobili, sau o implementare Meshtastic cu câteva relee bine amplasate și o limită mai mare de hopuri oferă majoritatea beneficiilor practice fără să opereze două rețele lipite împreună.

______

## Reticulum

Reticulum merită o categorie proprie, nu un loc de „a treia opțiune mesh LoRa”, deoarece nu este în primul rând un protocol mesh LoRa. **Caracteristica sa definitorie este independența față de transport.**

Reticulum este o stivă de rețea bazată pe criptografie. Nu folosește adrese sursă, deci pachetele nu conțin informații despre locul din care provin. Fiecare adresă este suverană: după generare devine accesibilă global în câteva secunde sau minute și rămâne accesibilă chiar dacă dispozitivul este mutat fizic în altă parte a rețelei. Toate comunicațiile sunt criptate implicit, cu chei efemere și forward secrecy. Reticulum elimină pachetele necriptate în loc să le livreze. Nu necesită drivere de kernel. Rulează în spațiul utilizatorului pe orice sistem cu Python 3, inclusiv pe un Raspberry Pi Zero.

Interfețele acceptate de Reticulum includ:

- **LoRa**, cu hardware compatibil RNode (un design deschis și definit de transceiver LoRa, care poate fi construit, instalat pe plăci obișnuite sau cumpărat gata făcut)
- **Radio cu pachete**, prin orice TNC în modul KISS, potrivit pentru radioamatorismul VHF și UHF
- **Wi-Fi și Ethernet cu fir**, cu descoperirea automată a peerilor fără router sau server DHCP
- **Legături seriale**, pentru conexiuni directe între dispozitive
- **TCP și UDP prin rețele IP existente**, inclusiv internetul
- **Rețeaua I2P** și interfețe personalizate pentru orice altceva ce poate folosi o punte Python

Pe Reticulum rulează aplicații precum **LXMF** (un protocol de mesagerie tolerant la întârzieri) și instrumente pentru utilizatori precum **Sideband**, **NomadNet** și clienți comunitari **MeshChat**. Acestea oferă rețelelor Reticulum un nivel de mesagerie și navigare comparabil cu ceea ce Meshtastic și MeshCore includ implicit.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagramă care arată cum Reticulum conectează o rețea mesh LoRa, o rețea radio cu pachete și o legătură la internet într-o singură rețea adresabilă și criptată" >}}

### Când are sens Reticulum

Valoarea Reticulum devine clară într-o configurație eterogenă, de exemplu:

**Rețea mesh LoRa → nod Reticulum → legătură IP → nod Reticulum → rețea radio**

Aici Reticulum face ceva ce nici Meshtastic, nici MeshCore nu fac: conectează două sisteme de comunicații distincte într-o singură rețea adresabilă. Este o cerință reală și specifică, nu o îmbunătățire generică. Se potrivește pentru:

- **Conectarea rețelelor aflate la distanță geografică** fără o legătură radio directă între ele
- **Bridgingul unor transporturi fizice diferite**, cum ar fi o rețea mesh LoRa la un capăt și o rețea radio cu pachete la celălalt
- **Gateway-uri radio-IP** care trimit traficul între o rețea radio de teren și internet
- **Rețele experimentale și de cercetare**, unde flexibilitatea de a combina transporturi contează mai mult decât simplitatea implementării
- **Rețele în care niciun transport nu acoperă singur toate cerințele**, deci trebuie conectate mai multe componente

### Când Reticulum adaugă complexitate inutilă

Dacă toți folosesc hardware LoRa compatibil, iar obiectivul real este **o singură rețea mesh LoRa regională**, adăugarea Reticulum aduce puține beneficii și un cost real. Fiecare nivel suplimentar din stiva de rețea înseamnă mai multă:

- **Configurare** care trebuie să fie corectă și consecventă pe toate nodurile
- **Software** de instalat, actualizat și depanat
- **Hardware** în unele configurații, în funcție de felul în care sunt conectate interfețele
- **Suprafață de depanare** când ceva nu este livrat
- **Cunoștințe necesare** pentru operatorii care trebuie să înțeleagă un al treilea model de rețea

*Folosește Reticulum când independența față de transport rezolvă o cerință pe care o ai cu adevărat, nu doar pentru că acceptă mai multe tipuri de interfețe decât alternativa.* O problemă de limită a hopurilor într-o rețea mesh LoRa este o problemă de reglare Meshtastic sau MeshCore. Nu este o problemă de independență față de transport, iar Reticulum nu o transformă în una.

______

## Construiește o singură rețea mesh sănătoasă înainte să faci trei fragmentate

Dacă un protocol îți îndeplinește deja cerințele, **construiește o rețea sănătoasă** în loc de mai multe rețele mici conectate prin punți. Principiul „întâi o singură rețea mesh” ar trebui să ghideze majoritatea deciziilor de mai sus.

Pentru o rețea comunitară, **interoperabilitatea între persoanele care o folosesc deja contează de obicei mai mult decât flexibilitatea arhitecturală.** O rețea mare, funcțională, pe un singur protocol are o valoare practică mai mare decât trei rețele interesante tehnic, dar fragmentate și conectate doar parțial.

### Rețelele Meshtastic existente contează

**Nu respinge Meshtastic doar pentru că MeshCore are avantaje arhitecturale pentru infrastructura fixă.** Dacă într-un oraș există deja zeci sau sute de noduri Meshtastic, această bază instalată este infrastructură reală și o comunitate reală. Migrarea are costuri pe care comparația fișelor tehnice nu le surprinde:

- **Hardware instalat** care trebuie rescris sau înlocuit
- **Utilizatori existenți** care știu deja să folosească rețeaua
- **Cunoștințe comunitare** acumulate în jurul implementării existente
- **Repetoare deja instalate și amplasate**, uneori pe acoperișuri sau turnuri greu accesibile
- **Experiența de configurare** acumulată de persoanele care operează rețeaua
- **Canale stabilite** pe care oamenii le monitorizează deja
- **Instruirea necesară** pentru oricine învață un al doilea sistem

Alegerea protocolului este **parțial o problemă de inginerie și parțial una de adoptare comunitară.** Arhitectura mai bună pe hârtie nu câștigă automat dacă cere unei comunități active să o ia de la capăt.

______

## Problema rețelei regionale

Ia în considerare o implementare ipotetică în mai multe orașe:

**Orașul A, repetor, repetor, releu rural, repetor, Orașul B, repetor, Orașul C**

În acest lanț, **testează separat mesajele de grup și cele directe**. MeshCore poate refolosi o rută pentru mesajele directe, dar continuă să inunde rețeaua pentru cele de grup. Meshtastic poate păstra contorul pe legăturile de infrastructură eligibile. Fiecare retransmisie ocupă canalul. Niciun protocol nu garantează livrarea de la un capăt la altul.

În acest scenariu, **limitele de hopuri, bugetul de airtime, comportamentul rutării și proiectarea infrastructurii nu mai sunt teoretice** și încep să determine dacă rețeaua funcționează de la un capăt la altul. La scară geografică, diferențele arhitecturale dintre Meshtastic și MeshCore nu mai sunt academice.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagramă a unui lanț de rețea mesh regională care conectează trei orașe prin repetoare și un releu rural, ilustrând cum cresc timpul de emisie și numărul de hopuri odată cu distanța" >}}

______

## RF contează mai mult decât protocolul

**Niciun software de rutare ingenios nu creează un traseu RF acolo unde nu există fizic.** Înainte să dai vina pe protocol pentru o problemă de acoperire, verifică elementele de bază:

- **Înălțimea antenei** față de obstacole
- **Linia de vizibilitate** între cele două capete ale legăturii
- **Degajarea zonei Fresnel**, diferită de vizibilitatea directă cu ochiul
- **Pierderile pe cablul de alimentare**, cauzate de coaxial ieftin sau prea lung
- **Calitatea antenei** și potrivirea cu banda folosită
- **Nivelul de zgomot** în locația de recepție
- **Relieful** dintre noduri
- **Poziționarea nodurilor**, inclusiv posibilitățile realiste de îmbunătățire
- **Marja legăturii**, diferența dintre semnalul recepționat și minimul necesar decodării

*O antenă de 2 dBi bine poziționată pe un catarg potrivit depășește adesea o antenă cu câștig mare, poziționată prost la fereastra unui subsol.* Alegerea protocolului determină felul în care rețeaua gestionează legăturile existente. Nu creează legături acolo unde fizica nu permite.

### Fiabilitate înaintea razei maxime

**Nu proiecta o rețea în jurul distanței maxime pe care o legătură o atinge doar uneori.** Proiecteaz-o pentru legături care funcționează constant.

Pentru o rețea comunitară sau de comunicații de urgență, **livrarea previzibilă pe 15 mile are valoare practică mai mare decât o legătură care ajunge ocazional la 40 de mile și eșuează în restul timpului.** Construiește acoperire suprapusă cu infrastructură fiabilă, în loc să urmărești legături record. Principiul se aplică indiferent de protocol.

______

## Pe care să îl alegi

**Meshtastic are sens** când apreciezi maturitatea ecosistemului, ușurința adoptării, utilizatorii portabili și mobili și compatibilitatea cu o comunitate Meshtastic existentă. Este alegerea implicită potrivită pentru majoritatea celor care pornesc de la zero.

**Repetoarele fixe** ajută la planificarea acoperirii, dar nu elimină inundarea. Înainte să alegi, testează ambele protocoale cu rata estimată de mesaje de grup, setările radio și amplasarea planificată a repetoarelor.

**Reticulum are sens** când problema depășește o singură rețea mesh LoRa și ai nevoie să conectezi transporturi diferite sau rețele separate într-un singur sistem adresabil.

Pentru o **rețea comunitară de infrastructură fără licență, cu consum redus, rază lungă și construită în principal în jurul repetoarelor fixe**, înclină spre MeshCore. **Testează traficul de grup înainte de a schimba protocolul.** Repetoarele fixe ajută la acoperire, dar nu oferă rute direcționate pentru canalele de grup. *Dacă în zona ta există deja o rețea Meshtastic sănătoasă, înlocuirea ei are nevoie de beneficii suficiente pentru a justifica fragmentarea comunității existente.* Reticulum intră în discuție când un singur protocol mesh sau un singur transport fizic nu mai îndeplinește cerințele, nu doar pentru că face mai multe lucruri.

______

## Referințe

1. [Algoritmul de broadcast mesh Meshtastic](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Configurarea LoRa Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Site-ul oficial MeshCore](https://meshcore.co.uk/)
4. [Stiva de rețea Reticulum](https://reticulum.network/)
5. [Ce este Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Configurarea interfețelor Reticulum](https://reticulum.network/manual/interfaces.html)
7. [Ghid comparativ MeshCore și Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)

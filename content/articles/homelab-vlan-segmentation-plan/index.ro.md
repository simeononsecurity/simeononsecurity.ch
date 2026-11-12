---
title: "Planificarea și testarea segmentării VLAN într-un homelab"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Creează un plan VLAN pentru dispozitive de încredere, servere, IoT și oaspeți. Notează traficul permis, configurează rețeaua în etape și testează izolarea."
genre: ["Homelab", "Securitatea rețelelor", "Rețelistică"]
tags: ["VLAN homelab", "segmentare VLAN", "rețea IoT", "rețea pentru oaspeți", "firewall homelab", "rutare inter-VLAN", "802.1Q", "izolarea rețelei", "test VLAN", "VLAN pfSense", "port de acces", "port trunk", "reguli firewall", "securitate homelab", "plan de rețea", "subrețea", "DHCP", "DNS", "switch administrabil", "SSID wireless"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Un router și un switch de homelab separă laptopuri, servere, dispozitive IoT și oaspeți în zone de rețea protejate."
coverCaption: "Planifică limitele VLAN, apoi testează fiecare cale permisă și blocată."
---

Un homelab conectează adesea laptopuri, servere, camere și dispozitivele oaspeților la aceeași rețea. **Segmentarea VLAN** plasează aceste grupuri în rețele separate. Un router, un firewall sau un switch de nivel 3 rutează traficul între ele. Regulile firewall sau listele de control al accesului pe switch gestionează aceste fluxuri rutate. Acest ghid te ajută să pregătești planul, să faci câte o schimbare și să verifici rezultatul.

## Idei principale

- **Grupează după încredere:** plasează dispozitivele de administrare, serverele, dispozitivele IoT și oaspeții în rețele separate când nevoile lor de acces diferă.
- **Notează căile permise:** pentru fiecare conexiune între rețele, consemnează sursa, destinația, serviciul și motivul.
- **Configurează ambele niveluri:** setările switch-ului și ale punctului de acces plasează dispozitivele în VLAN-uri. Regulile firewall sau listele de control al accesului pe switch controlează traficul rutat.
- **Testează ambele rezultate:** verifică o conexiune permisă și una blocată din fiecare rețea relevantă.

## Înainte să începi

Ai nevoie de un router sau firewall cu interfețe VLAN ori de un switch de nivel 3 care acceptă rutare VLAN și liste de control al accesului. Un switch administrabil transportă VLAN-urile cablate. Dacă separi clienții wireless, ai nevoie și de un punct de acces cu rețele Wi-Fi asociate VLAN-urilor. Păstrează un dispozitiv în rețeaua actuală de administrare cât timp schimbi configurația. Salvează mai întâi setările routerului, switch-ului și punctului de acces. Pașii de mai jos folosesc un **plan ilustrativ**. Adaptează adresele și porturile la echipamentul tău.

O **interfață VLAN** este conexiunea gateway-ului la un VLAN. Gateway-ul poate fi un router, un firewall sau un switch de nivel 3. Un **interval DHCP** este plaja de adrese oferită dispozitivelor de un serviciu DHCP din acea rețea. Un **releu DHCP** transmite cererile de adrese dintr-un VLAN către un server DHCP din altă rețea. Folosește un releu când gateway-ul nu oferă adrese pentru acel VLAN, iar serverul DHCP se află în altă parte. Ghidul Juniper despre [releul DHCP](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) descrie acest traseu. Un **SSID** wireless este numele rețelei la care se conectează clienții. Dacă echipamentul tău nu include un switch administrabil sau un punct de acces compatibil cu VLAN, începe cu rețeaua de oaspeți integrată și verifică izolarea înainte să cumperi sau să schimbi hardware.

Dacă ai nevoie mai întâi de noțiunile de bază, citește despre [subrețele și VLAN-uri](/articles/networking-basics-what-are-subnets-and-vlans/). [Ghidul de segmentare a rețelei](/articles/how-to-perform-network-segmentation-for-improved-security/) de pe site prezintă conceptul general de securitate. CISA descrie rețele casnice separate pentru oaspeți și dispozitive Internet of Things în ghidul [Federal Mobile Workplace Security](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Avertisment:** O schimbare de VLAN pe portul care transportă conexiunea de administrare te poate bloca afară. Păstrează accesul fizic și o cale de recuperare cunoscută până când fiecare rețea trece testele.

Înainte să muți un cablu, exportă configurația fiecărui dispozitiv și notează adresa IP actuală de administrare, portul switch-ului, setarea VLAN și datele de autentificare ale administratorului. Lasă un port de administrare cunoscut și un laptop în rețeaua inițială. Dacă o schimbare întrerupe accesul, reconectează laptopul la acel port, restaurează setarea sau configurația salvată și confirmă că vechiul gateway răspunde înainte să încerci din nou. Dacă switch-ul nu are o cale de administrare accesibilă, folosește consola documentată sau procedura locală de recuperare. Nu reseta echipamentul până nu știi ce șterge resetarea.

## Inventariază dispozitivele și fluxurile

Notează fiecare dispozitiv, adresa curentă, proprietarul și serviciile necesare. Stabilește de ce fiecare dispozitiv trebuie să ajungă într-o altă rețea. De exemplu, un laptop ar putea administra un server, în timp ce o cameră ar avea nevoie doar de un recorder și un server DNS. Un telefon de oaspete are nevoie de internet, dar nu de acces la servere.

| Grup de dispozitive | Exemple | Acces necesar |
|---|---|---|
| **Administrare** | Laptop de administrator, interfețe de administrare ale switch-ului și punctului de acces | Administrarea routerului, switch-ului, punctului de acces și serverelor |
| **Servere** | Hypervisor, NAS, destinație pentru copii de rezervă | Actualizări, DNS, trafic de aplicații aprobat |
| **IoT** | Camere, prize inteligente, dispozitive media | DNS, serviciu de timp, controler sau recorder specific |
| **Oaspeți** | Telefoane și laptopuri ale vizitatorilor | Internet, DNS, fără subrețele private |

Notează excepțiile înainte să adaugi reguli. Funcțiile de descoperire locală, precum transmiterea pe ecran, depind adesea de traficul multicast, care în mod normal nu traversează o limită rutată. Nu permite tot traficul dintre VLAN-uri pentru a rezolva o singură problemă de descoperire. Identifică protocolul și adaugă cea mai restrânsă excepție acceptată.

## Atribuie VLAN-uri și adrese

Atribuie fiecărui grup un ID VLAN și o subrețea IP separată. Acest **plan ilustrativ** folosește adrese rezervate pentru documentație și presupune că routerul oferă DHCP și DNS. Nu copia tabelul într-o rețea activă fără să verifici conflictele de adrese.

| Rețea | ID VLAN | Subrețea | Gateway exemplu |
|---|---:|---|---|
| **Administrare** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Servere** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Oaspeți** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Aceste intervale rezervate documentației ilustrează doar structura, conform [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Pentru laboratorul real folosește adrese private din [RFC 1918](https://www.rfc-editor.org/info/rfc1918), cu o subrețea fără suprapuneri pentru fiecare VLAN. Notează în plan fiecare gateway real, pool DHCP, adresă DNS și rezervare de dispozitiv.

**Porturile de acces** transportă rețeaua unui singur dispozitiv fără etichetă VLAN. **Porturile trunk** transportă VLAN-uri selectate, cu etichete, între router, switch și punctul de acces. Potrivește ID-ul VLAN și setarea native sau untagged la ambele capete. Ghidul Netgate despre [switch-uri VLAN](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) explică porturile trunk etichetate, porturile de acces fără etichetă și ID-urile VLAN ale porturilor. Evită să folosești VLAN 1 implicit pentru administrare dacă echipamentul permite un VLAN separat, așa cum descrie ghidul Netgate pentru [securitatea VLAN](https://docs.netgate.com/pfsense/en/latest/vlan/security.html).

Traficul **native** sau **untagged** de pe un trunk nu are etichetă VLAN. Ambele capete trebuie să îl atribuie aceluiași VLAN, altfel un dispozitiv poate ajunge în rețeaua greșită. Permite doar VLAN-urile de care are nevoie legătura. Dezactivează porturile nefolosite ale switch-ului sau atribuie-le unei rețele restricționate. Netgate recomandă și să nu tratezi un VLAN ca pe o limită completă de securitate dacă un atacator controlează un port al switch-ului. Protejează porturile fizice și datele de autentificare ale dispozitivelor, alături de traficul rutat.

## Construiește o matrice de trafic

Un VLAN separă singur domeniile de broadcast. **Rutarea inter-VLAN** pe router sau switch-ul de nivel 3 necesită în continuare reguli de acces. Decide ce dispozitiv rutează traficul între VLAN-uri. Dacă un switch de nivel 3 rutează local, traficul dintre VLAN-urile sale poate să nu ajungă niciodată la firewall-ul routerului. Aplică liste de control al accesului echivalente pe switch sau rutează prin firewall, apoi testează în punctul real de aplicare a regulilor. Verifică direcția ACL-ului switch-ului și dacă acesta urmărește starea conexiunii. Multe ACL-uri de switch verifică pachetele separat pe fiecare direcție, deci o conexiune permisă poate necesita o regulă restrânsă pentru traficul de răspuns. Ghidul Cisco despre [ACL-uri](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) descrie direcția interfeței și potrivirea ordonată a pachetelor. Folosește inventarul dispozitivelor pentru a nota conexiunile permise. Intrările următoare sunt exemple, nu un set universal de reguli.

| Sursă | Destinație | Serviciu | Decizie |
|---|---|---|---|
| **Administrare** | Interfață de administrare a serverului | TCP 443 | Permite dispozitivelor de administrare aprobate |
| **Administrare** | Interfețele de administrare ale routerului, switch-ului și punctului de acces | Porturile de administrare documentate | Permite dispozitivelor de administrare aprobate |
| **IoT** | Recorderul camerelor | Portul documentat al recorderului | Permite doar dacă e necesar |
| **IoT** | Serviciu DNS și de timp aprobat | DNS și NTP | Permite doar către serviciile alese |
| **IoT** | Subrețeaua de administrare | Oricare | Refuză |
| **Oaspeți** | Subrețele private | Oricare | Refuză |
| **Oaspeți** | DNS și internet | DNS, trafic web | Permite prin resolverul și gateway-ul aprobate |

Include și serviciile proprii ale routerului în plan. O regulă care blochează accesul IoT la alte VLAN-uri poate lăsa accesibilă interfața de administrare a routerului. Restricționează serviciile de administrare la rețeaua de administrare. Începe doar cu regulile de permitere necesare și o regulă implicită de refuz pentru restul traficului rutat. Verifică regulile largi de permitere existente înainte să presupui că setarea implicită refuză totul. Recomandările Netgate privind [bune practici pentru firewall](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) arată că o rețea LAN pfSense implicită include o regulă de permitere. Dacă folosești pfSense, [metodologia regulilor](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) explică faptul că regulile de interfață filtrează traficul care intră pe acea interfață și că o conexiune permisă creează stare pentru traficul de răspuns.

Tabelul exemplifică IPv4. Dacă rețeaua folosește IPv6, atribuie un prefix IPv6 și o politică fiecărui VLAN, inspectează anunțurile routerului și testează și căile IPv6 permise și refuzate. Blocarea IPv4 nu dovedește izolarea IPv6. Dacă nu vrei să rutezi IPv6, verifică setările IPv6 ale routerului și adresele clienților, în loc să presupui că IPv6 lipsește. Netgate documentează [comportamentul firewall-ului IPv6](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) și [anunțurile routerului](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Configurează câte o rețea

1. Alege gateway-ul pentru VLAN. Dacă routerul sau firewall-ul face rutarea, creează acolo o interfață VLAN și atribuie-i adresa gateway-ului. Dacă un switch de nivel 3 face rutarea, creează interfața VLAN pe acel switch. Configurează un interval DHCP pe gateway sau un releu DHCP către serverul DHCP existent. Confirmă că resolverul DNS aprobat este accesibil. Ghidul Netgate pentru [configurarea VLAN](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) enumeră pașii pentru interfețe și servicii într-un gateway pfSense.
2. Dacă routerul este gateway-ul VLAN, adaugă VLAN-ul la trunk-ul dintre router și switch. Dacă gateway-ul este switch-ul de nivel 3, lasă switch-ul să dețină adresa gateway-ului acelui VLAN și rutează către router sau firewall printr-o rețea de tranzit separată sau o legătură uplink rutată. Configurează pe switch o rută implicită către routerul din amonte. Adaugă pe router o rută de întoarcere pentru fiecare VLAN cu gateway pe switch. Verifică politica firewall-ului și NAT-ul de ieșire al routerului pentru aceste subrețele dacă au nevoie de internet. Nu configura aceeași adresă gateway sau același interval DHCP pe ambele dispozitive. Adaugă VLAN-ul la trunk-ul relevant dintre switch și punctul de acces dacă rețeaua este necesară clienților wireless. Ghidul Cisco pentru [rutarea inter-VLAN](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) arată gateway-uri VLAN deținute de switch. Netgate documentează [rutele de întoarcere](https://docs.netgate.com/pfsense/en/latest/routing/static.html) și [NAT-ul de ieșire](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) pentru rețele din spatele unui router intern.
3. Atribuie VLAN-ului un port de acces sau un SSID wireless de test. Conectează la acel port sau SSID un dispozitiv de test necritic.
4. Adaugă regulile firewall sau ACL-urile switch-ului pe dispozitivul care rutează VLAN-ul. Verifică dacă restul traficului rutat este refuzat. Verifică direcția ACL-ului și traficul de răspuns dacă switch-ul nu urmărește starea. Testează accesul la fiecare gateway, interfață de administrare, subrețea locală și IPv6 dacă este prezent. Permite doar căile din matricea de trafic. Limitează administrarea la rețeaua de administrare. Verifică ordinea regulilor și elimină sau restrânge regulile largi de permitere existente doar după ce funcționează calea de administrare de test.
5. Confirmă că dispozitivul de test primește o adresă, un gateway și un server DNS din subrețeaua prevăzută. Apoi execută verificările de conexiune de mai jos înainte să muți mai multe dispozitive.

Nu muta ultimul dispozitiv de administrare până când nu funcționează calea de înlocuire. Salvează configurația funcțională după ce fiecare rețea trece testele. Dacă DHCP, DNS sau accesul de administrare eșuează, mută dispozitivul de test înapoi la portul sau SSID-ul inițial. Restaurează ultima schimbare de switch sau router din configurația salvată și testează din nou rețeaua originală înainte să continui.

## Testează izolarea și accesul

Folosește un serviciu pe care îl controlezi și despre care știi că ascultă la destinație. Pe un dispozitiv Windows de test, înlocuiește adresa și portul exemplu cu un server real, apoi rulează:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

Câmpul **`TcpTestSucceeded`** indică dacă s-a stabilit o conexiune TCP. Referința Microsoft pentru [Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) documentează parametrii `-ComputerName` și `-Port`. O conexiune eșuată nu dovedește singură că regula firewall a funcționat. Serviciul poate fi oprit, iar firewall-ul gazdei poate respinge traficul. Verifică serviciul de destinație și jurnalul firewall-ului de rețea înainte să tragi o concluzie.

Testează de pe un dispozitiv conectat efectiv la fiecare VLAN sursă. Înainte de fiecare test, notează adresa sursă, gateway-ul și serverul DNS. Verifică o conexiune permisă către serviciul vizat, o conexiune refuzată către un serviciu intern din afara matricei, o interogare DNS prin resolverul ales și accesul la internet unde este planificat. Pentru un VLAN cu gateway pe switch, verifică ruta implicită a switch-ului, ruta de întoarcere a routerului și calea de retur de la destinație dacă o conexiune permisă eșuează. Repetă testele permise și refuzate cu adrese IPv6 dacă IPv6 este activ. În pfSense, **Status > System Logs > Firewall** afișează acțiunile de permis sau blocare înregistrate. Ghidul Netgate despre [jurnalul firewall](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) descrie acest ecran. Compară sursa, destinația, portul și regula din jurnal cu testul. Dacă testul reușește neașteptat, inspectează regulile largi de permitere și intrările de stare existente. După modificarea regulilor, începe o conexiune nouă, deoarece una existentă poate continua pe baza stării sale.

Pentru o verificare DNS pe Windows, rulează `nslookup example.com` și compară serverul afișat cu resolverul planificat. Apoi încearcă o interogare de pe un client pentru oaspeți sau IoT cu DNS restricționat. O interogare reușită nu dovedește că clientul a folosit resolverul ales, așa că verifică serverul raportat și un jurnal firewall sau resolver. Testează separat accesul direct de pe un dispozitiv IoT sau de oaspeți la adresa de administrare a routerului ca un caz refuzat.

Dispozitivele din **același VLAN** ar putea schimba trafic fără să treacă prin firewall-ul routerului. Testează separat izolarea locală a clienților dacă punctul de acces o oferă și folosește firewall-uri pe gazdă pentru servere. Testele firewall între VLAN-uri nu dovedesc izolarea în același VLAN.

> **Rezultatul așteptat:** fiecare dispozitiv primește o adresă din subrețeaua planificată. Serviciile permise funcționează. Încercările refuzate corespund unei blocări firewall sau unui control echivalent documentat.

## Depanare

- **Fără adresă:** verifică VLAN-ul portului de acces sau al SSID-ului, etichetele trunk-ului, intervalul DHCP și interfața gateway-ului.
- **Adresa funcționează, DNS nu:** verifică adresa resolverului, asocierea serviciului pe router și regula firewall pentru DNS.
- **Un dispozitiv ajunge neașteptat într-un alt VLAN:** verifică regulile routerului, regulile largi de permitere și dacă dispozitivele sunt încă în aceeași rețea fără etichetă.
- **Fără jurnal firewall pentru traficul rutat:** verifică dacă un switch de nivel 3 sau alt gateway a rutat conexiunea înainte să ajungă la firewall.
- **Un VLAN cu gateway pe switch ajunge la rețele locale, dar nu la internet:** verifică ruta implicită a switch-ului, rutele de întoarcere ale routerului, politica firewall și NAT-ul de ieșire pentru subrețea.
- **IPv4 este blocat, dar conexiunea funcționează:** verifică adresele IPv6, anunțurile routerului, regulile IPv6 și intrările de stare existente.
- **Un test refuzat expiră fără jurnal firewall:** confirmă că serviciul de destinație ascultă. Apoi inspectează rutarea și setările de jurnalizare. Ghidul Netgate pentru [depanarea firewall-ului](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) descrie verificările jurnalelor și stărilor.
- **Transmiterea sau descoperirea nu mai funcționează:** identifică protocolul de descoperire și traseul controlerului înainte să adaugi o excepție restrânsă.

## Pașii următori

Păstrează inventarul dispozitivelor și matricea de trafic împreună cu diagrama rețelei. Revizuiește regulile când adaugi un server sau dispozitiv IoT. Repetă un test de conexiune permisă și unul refuzat după fiecare schimbare relevantă a rețelei. Pentru principiile de proiectare mai ample, revino la [segmentarea rețelei](/articles/how-to-perform-network-segmentation-for-improved-security/).

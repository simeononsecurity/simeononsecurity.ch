---
title: "Testează scurgerile DNS și WebRTC din browser cu un VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Verifică adresa IP publică, resolverul DNS și adresele WebRTC ale browserului înainte și după conectarea la un VPN. Interpretează rezultatele și investighează problemele de rutare."
genre: ["Confidențialitate", "Browsere", "Rețelistică"]
tags: ["test scurgere DNS", "test scurgere WebRTC", "test scurgere VPN", "test confidențialitate browser", "scurgere adresă IP", "DNS prin HTTPS", "DNS securizat", "DNS Firefox", "DNS securizat Chrome", "candidați WebRTC", "tunelare divizată VPN", "scurgere IPv6", "test resolver", "confidențialitate browser", "confidențialitate rețea", "depanare VPN", "resolver DNS", "candidați ICE", "adresă IP privată", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Fereastră de browser cu trei panouri pentru IP public, DNS și conexiuni între egali, plus un tunel continuu și o rută alternativă punctată către servere la distanță."
coverCaption: "Compară fiecare rută de rețea înainte și după conectarea la VPN."
---

Pictograma de conexiune a unei rețele private virtuale (VPN) nu dovedește că fiecare solicitare a browserului urmează aceeași rută. Testează separat **IP-ul public**, **resolverul Sistemului de nume de domeniu (DNS)** și **adresele WebRTC**. Fiecare rezultat răspunde unei întrebări diferite. Acest ghid prezintă un test repetabil și o metodă de investigare a rezultatelor neașteptate.

<!--more-->

## Idei principale

- **Compară două stări:** Înregistrează aceleași teste înainte și după conectarea VPN-ului.
- **Analizează separat rezultatele:** Schimbarea IP-ului public nu arată unde au ajuns interogările DNS.
- **Verifică candidații WebRTC:** Caută un IP public în afara rutei intenționate. O adresă privată are altă semnificație.
- **Schimbă o singură setare:** Testează din nou după fiecare modificare a VPN-ului, browserului sau DNS-ului.

## Înainte să începi

Folosește browserul și conexiunea de rețea pe care intenționezi să le protejezi. Stabilește dacă VPN-ul trebuie să acopere întregul dispozitiv sau doar anumite aplicații. Dacă VPN-ul folosește tunelare divizată, notează dacă browserul testat este inclus în tunel. Păstrează la îndemână politica DNS a clientului VPN pentru comparație.

**Tunelarea divizată** trimite anumite aplicații prin VPN, în timp ce altele folosesc rețeaua obișnuită.

Procedura folosește paginile [IP BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) și [WebRTC](https://browserleaks.com/webrtc). Serviciul vede adresa conexiunii tale când îl accesezi. Potrivit descrierii testului, testul DNS cere browserului să rezolve 50 de nume aleatorii. Nu rula un test extern într-o rețea administrată sau restricționată fără aprobare. Nu introduce date de autentificare, nume de gazdă interne sau istoricul privat de navigare într-un site de testare.

> **Avertisment:** Nu publica IP-urile exacte în capturi de ecran publice sau postări pentru asistență. Notează dacă adresele corespund rutei așteptate a furnizorului de internet sau a VPN-ului. Comunică valorile reale doar printr-un canal de asistență aprobat.

## Ce arată fiecare test

| Verificare | Ce să compari | Ce nu dovedește rezultatul |
|---|---|---|
| **IP public** | Adresa văzută de un site web obișnuit | Ce resolver a gestionat DNS-ul |
| **Resolver DNS** | Serverele observate în timpul unor căutări noi de nume | Unde trimite fiecare aplicație cererile DNS |
| **WebRTC** | Candidații locali și publici pentru conexiune | Ce candidat va folosi un apel ulterior |

Pagina IP public raportează adresa folosită de solicitarea web. Pagina DNS pornește căutări noi și raportează resolverele care le gestionează. WebRTC, prescurtare de la Web Real-Time Communication, permite aplicațiilor din browser să stabilească conexiuni între egali. Pagina WebRTC verifică adresele expuse în timpul acestor conexiuni. Un **candidat ICE** este o adresă de rețea posibilă pentru o conexiune între egali. O **ieșire VPN** este adresa publică folosită după ce traficul părăsește VPN-ul. [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) explică de ce candidații de conexiune WebRTC includ uneori adrese diferite de cea observată de o solicitare web obișnuită, mai ales cu tunelare divizată sau proxy-uri.

Un server DNS al furnizorului VPN, un alt resolver selectat în VPN sau un resolver criptat ales de browser afișează nume diferite în test. Numele resolverului nu identifică singur o scurgere. Compară-l cu politica pe care intenționai să o folosești.

## Înregistrează o referință inițială

Deconectează VPN-ul numai dacă situația îți permite o referință fără tunel. Deschide cele trei pagini de test într-un profil obișnuit al browserului. Rulează testul DNS și așteaptă rezultatul. Înregistrează următoarele fără să publici adresele exacte:

| Câmp | Notă inițială |
|---|---|
| **Browser și versiune** | Nume, versiune și extensii relevante pentru confidențialitate |
| **Rețea** | Wi-Fi de acasă, hotspot mobil sau altă rețea aprobată |
| **IPv4 și IPv6 publice** | Dacă fiecare adresă aparține conexiunii obișnuite |
| **Rezultat DNS** | Numele sau operatorii resolverelor afișate |
| **Rezultat WebRTC** | Candidații publici, privați sau `.local` afișați |

Dacă nu poți deconecta VPN-ul, începe cu ruta VPN așteptată și marchează referința fără tunel drept indisponibilă. Nu deduce adresa obișnuită a furnizorului dintr-o etichetă de locație sau o hartă. Bazele de date de localizare diferă uneori de operatorul real al rețelei.

## Repetă testul cu VPN-ul conectat

Conectează VPN-ul și confirmă că aplicația client raportează un tunel activ. Reîncarcă fiecare pagină de test în **același profil de browser**. Rulează din nou testul DNS pentru a genera interogări noi. Înregistrează rezultatele IPv4 și IPv6 dacă serviciul le afișează.

Compară rezultatele în această ordine:

1. **IP public:** Solicitarea web ar trebui să afișeze o adresă compatibilă cu ieșirea VPN sau cu ruta configurată intenționat. Un IP obișnuit al furnizorului indică o problemă de rutare dacă browserul ar trebui să fie în tunel.
2. **DNS:** Compară fiecare resolver afișat cu setările DNS ale VPN-ului și browserului. Investighează un resolver al furnizorului de internet în afara tunelului așteptat. Un resolver terț identificat este normal dacă l-ai selectat intenționat în browser.
3. **WebRTC:** Compară candidatul WebRTC public cu ieșirea VPN și IP-ul public de referință. Dacă tot traficul browserului ar trebui să folosească VPN-ul, apariția IP-ului obișnuit al furnizorului doar în WebRTC merită investigată.
4. **Adrese private:** O adresă din [intervalele private RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) sau un candidat `.local` diferă de un IP public al furnizorului. Notează intrarea locală și decide dacă site-ul ar trebui să o afle.

[Standardul de gestionare a IP-urilor WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) descrie cum o aplicație află alte adrese publice sau private prin descoperirea candidaților ICE. Proiectul [candidatului de gazdă mDNS din Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) înlocuiește unele adrese private cu nume `.local`. Un rezultat WebRTC gol este **neconcludent** dacă JavaScript, API-ul sau serverul de test nu a funcționat. Un rezultat gol nu dovedește protecție completă.

> **Rezultat așteptat:** Solicitarea web obișnuită a browserului și candidații WebRTC publici urmează ruta aleasă. Rezultatele DNS corespund politicii resolverului VPN sau a browserului pe care ai înregistrat-o.

## Investighează o diferență DNS

Mai întâi verifică dacă browserul își alege propriul resolver. Setările [DNS over HTTPS din Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) afișează starea activă și nivelul de protecție. Protecția implicită revine la resolverul sistemului în anumite situații și respectă semnalele rețelei. Nivelurile Sporit și Personalizat folosesc un furnizor selectat cu opțiuni de rezervă. Nivelul Maxim avertizează când rezolvarea securizată eșuează. Starea și lista de excepții contează mai mult decât un comutator izolat.

[Ghidul Secure DNS din Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) descrie modul automat și un furnizor personalizat. Modul automat revine la o interogare necriptată dacă rezolvarea securizată eșuează. Un furnizor personalizat nu revine implicit la modul necriptat. Dispozitivele administrate și controlul parental limitează această setare. Verifică interfața actuală a browserului înainte de a schimba o politică administrată.

Dacă resolverul browserului nu este cauza, compară setarea DNS a clientului VPN, lista de aplicații din tunelul divizat, resolverul sistemului de operare și ruta IPv6. Schimbă un singur element, apoi repetă testul DNS. Testul DNS al browserului măsoară calea de căutare a browserului respectiv. Rezultatul nu stabilește cum rezolvă nume o altă aplicație. Dacă rețeaua folosește [filtrare DNS](/articles/nextdns-vs-adguard-ad-blocker-comparison/), testează un domeniu pe care îl blochezi intenționat și unul permis. Nu considera lipsa unei reclame drept dovadă despre ruta resolverului.

## Investighează o diferență WebRTC

Verifică dacă browserul este exclus din tunelul VPN sau folosește un proxy în afara rutei așteptate. Corectează ruta și testează din nou. Nu dezactiva IPv6 sau WebRTC ca primă reacție la un singur rezultat ambiguu. [Standardul WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) descrie compromisul dintre expunerea adresei și performanța apelurilor directe. Restricționarea candidaților sau impunerea unui proxy afectează apelurile video și alte conexiuni între egali.

Dacă browserul sau VPN-ul oferă un control documentat pentru gestionarea IP-urilor WebRTC, citește descrierea actuală și alege o politică potrivită modului în care folosești apelurile. Testează din nou candidatul public. O adresă locală, singură, nu dovedește că IP-ul public al furnizorului a ieșit din VPN. Un IP public expus al furnizorului, comparat cu un IP HTTP diferit al VPN-ului, este un indiciu mai puternic.

## Păstrează o evidență a testelor

| Câmp | Rezultat de înregistrat |
|---|---|
| **Data și browserul** | Versiune, profil, extensii și rețea |
| **Ruta așteptată** | VPN pentru întregul dispozitiv, tunel divizat sau proxy de browser |
| **Înainte și după** | Operatorul IP-ului public, operatorul DNS și candidatul WebRTC public |
| **Diferență** | Ce rezultat nu a corespuns politicii intenționate |
| **O singură schimbare** | Setarea modificată și motivul |
| **Retestare** | Noul rezultat și incertitudinea rămasă |

Rulează din nou verificarea după schimbări de configurare a browserului, VPN-ului sau rețelei. Un rezultat curat se aplică browserului, profilului, rețelei și momentului testat. Nu dovedește anonimatul și nu acoperă toate aplicațiile. Dacă încă alegi un browser, folosește [comparația browserelor axate pe confidențialitate](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) pentru funcții, apoi rulează testul în propria configurație.

## Pașii următori

Repetă testul după schimbări ale browserului, VPN-ului sau rețelei. Consultă [comparația browserelor axate pe confidențialitate](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) când alegi un browser.

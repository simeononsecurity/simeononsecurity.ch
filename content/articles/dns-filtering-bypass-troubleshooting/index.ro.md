---
title: "De ce este ocolită filtrarea DNS: verifică traseul resolverului"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Află de ce un dispozitiv sau browser ocolește filtrul DNS. Compară interogările directe și implicite, verifică jurnalele și controlează DNS criptat, VPN, IPv6 și setările routerului."
genre: ["Rețele de acasă", "DNS", "Confidențialitate"]
tags: ["ocolirea filtrării DNS", "ocolirea Pi-hole", "jurnal de interogări DNS", "DNS securizat în browser", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "DNS prin VPN", "DNS IPv6", "DHCP DNS router", "Resolve-DnsName", "depanare DNS", "test filtru DNS", "depanare NextDNS", "depanare AdGuard DNS"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "Traseul DNS albastru al unui laptop trece printr-un filtru și se oprește la un simbol de blocare, în timp ce traseul portocaliu al browserului ajunge la alt resolver."
coverCaption: "Urmărește traseul interogării înainte să schimbi regula filtrului."
---

Ai configurat un resolver cu filtrare, dar un dispozitiv accesează în continuare un domeniu blocat de politica ta. Cauza poate fi regula, atribuirea Domain Name System (DNS) a dispozitivului, un resolver criptat din browser sau un VPN. **Testează traseul înainte să schimbi setările.** O interogare directă către filtru răspunde la altă întrebare decât o interogare obișnuită a dispozitivului.

<!--more-->

## Idei principale

- **Verifică regula mai întâi:** Confirmă că filtrul primește și blochează un domeniu de test sigur.
- **Urmărește fiecare nivel:** Routerul, sistemul de operare, browserul, VPN-ul și setările mobile influențează rutarea DNS.
- **Folosește interogări noi:** Corelează un nume de gazdă nou și ora lui cu jurnalul de interogări al filtrului.
- **Precizează limita:** O interogare observată confirmă un traseu, nu comportamentul fiecărei aplicații sau al fiecărui dispozitiv.

## Înainte să începi

Rezervă aproximativ 20 de minute. Ai nevoie de acces la jurnalul de interogări al resolverului filtrant, de un dispozitiv cu problema și de o evidență a setărilor DNS ale routerului. Exemplele folosesc un laptop cu Windows și **Pi-hole**, dar aceeași comparație funcționează cu orice resolver care oferă jurnale pe client. Identifică mai întâi adresa exactă a filtrului. Nu include adrese private ale clienților, jurnale de interogări sau reguli de politică într-un raport public.

Alege un **domeniu de test inofensiv** pe care politica ta îl blochează deja. O altă opțiune este să adaugi temporar o regulă exactă de respingere pentru un domeniu pe care îl controlezi într-un profil de test. Notează regula și elimin-o după test. Nu folosi ca probă un domeniu activ de malware. O pagină blocată este un simptom util, dar jurnalul resolverului oferă dovezi mai puternice despre traseu.

| Nivel | Întrebare |
|---|---|
| **Filtru** | Ajunge o interogare directă la resolverul dorit și se potrivește cu regula? |
| **Dispozitiv** | Ce servere DNS atribuie rețeaua? |
| **Browser sau aplicație** | Clientul folosește resolverul dispozitivului sau un traseu separat? |
| **VPN sau relay** | Un tunel activ schimbă destinația interogărilor? |

## Confirmă funcționarea filtrului

Deschide jurnalul de interogări al resolverului. Interoghează direct filtrul pentru domeniul blocat ales. În Windows, folosește PowerShell și introdu adresa filtrului și domeniul de test când ți se cere:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

[Referința Microsoft pentru **`Resolve-DnsName`**](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) definește **`-Server`** ca interogare către resolverul numit. Găsește interogarea în jurnalul filtrului și verifică răspunsul și regula potrivită. [Documentația Pi-hole despre interogări și jurnalizare](https://docs.pi-hole.net/main/pihole-command/) descrie instrumentele locale de interogare. Dacă interogarea directă este permisă, repară regula sau atribuirea grupului client înainte să investighezi ocolirea. Dacă nu ajunge la filtru, verifică adresa, serviciul și traseul de rețea.

**Acest test direct nu demonstrează că laptopul folosește în mod obișnuit filtrul.** Opțiunea **`-Server`** suprascrie resolverul implicit doar pentru această interogare. Distincția previne un rezultat fals pozitiv frecvent.

## Urmărește traseul dispozitivului

Folosește un nume de gazdă nou pentru a evita o intrare DNS anterioară din cache. Exemplul următor trimite o interogare direct la filtru și alta prin selecția obișnuită a resolverului de pe laptop. Numele diferă, astfel încât să știi ce înregistrare corespunde fiecărui traseu. Un răspuns **NXDOMAIN** înseamnă că serverul DNS spune că numele de gazdă nu există. Este normal dacă numele aleatoriu nu este folosit. Aici contează prezența interogării în jurnalul filtrului.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Caută în jurnalul filtrului ambele nume exacte și notează ora și clientul raportat. Dacă apare **`direct-`**, dar nu și **`default-`**, verifică serverele DNS atribuite laptopului. În Windows, **`Get-DnsClientServerAddress`** afișează adresele serverelor DNS pentru fiecare interfață. Verifică adaptorul Wi-Fi sau Ethernet activ, nu unul deconectat. [Referința Microsoft pentru clientul DNS](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) descrie această comandă de citire.

Lasă erorile vizibile la primul test. O eroare sau expirarea timpului de așteptare necesită diagnosticare separată și diferă de lipsa unei înregistrări în jurnal.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Compară rândurile IPv4 și IPv6. **DHCP** atribuie setări de rețea, precum serverele DNS. **IPv6** este familia mai nouă de adrese Internet Protocol și folosește adrese de 128 de biți. O concesiune DHCP pentru IPv4 poate indica filtrul, în timp ce anunțurile IPv6 ale routerului furnizează alt server DNS. Verifică anunțurile **DHCP** și **DNS IPv6** ale routerului, apoi reînnoiește concesiunea DHCP a dispozitivului după corectare. [Ghidul Pi-hole de după instalare](https://docs.pi-hole.net/main/post-install/) explică modul în care DHCP direcționează clienții către Pi-hole. [Exemplul de router](https://docs.pi-hole.net/routers/fritzbox/) tratează anunțurile DNS IPv6.

Dacă jurnalul arată **routerul** ca client, routerul poate redirecționa interogări în numele dispozitivelor. Jurnalul filtrului dovedește atunci că routerul a ajuns la filtru, nu ce dispozitiv a pornit interogarea. Confirmă arhitectura de redirecționare a routerului înainte să consideri identitatea clientului o informație lipsă.

## Verifică DNS-ul browserului

O interogare din linia de comandă testează traseul resolverului dispozitivului. Un browser poate folosi în schimb **DNS over HTTPS (DoH)**. Deschide același domeniu de test blocat în browser și urmărește jurnalul filtrului pentru o interogare corespunzătoare. Golește memoria cache DNS a browserului sau folosește un nume nou sub o regulă de test dacă rezultatele salvate îngreunează comparația.

În **Chrome pe computer**, deschide **Setări > Confidențialitate și securitate > Securitate > Folosește DNS securizat**. [Ajutorul Google Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) spune că modul automat folosește furnizorul curent și revine la o căutare necriptată dacă apare o eroare. Un furnizor personalizat selectat nu revine în același mod. Notează modul și furnizorul selectat înainte să schimbi setarea.

În **Firefox**, deschide **Setări > Confidențialitate și securitate > DNS prin HTTPS**. [Ghidul Mozilla despre nivelurile de protecție](https://support.mozilla.org/en-US/kb/dns-over-https) diferențiază modurile Implicit, Mărit, Maxim, Personalizat și Dezactivat. [Prezentarea DoH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) explică atunci când un resolver de browser ocolește un filtru DNS local. Testează din nou după o singură schimbare controlată, apoi restaurează setarea de confidențialitate dorită.

**Nu eticheta orice interogare lipsă a browserului drept ocolire.** Browserul poate reutiliza date din cache, poate ajunge la o adresă cunoscută sau poate folosi un proxy. Compară un nume nou, un interval de timp potrivit și setarea resolverului browserului înainte să concluzionezi unde a ajuns interogarea.

## Verifică traseele mobile și VPN

Pe **Android**, verifică **Setări > Rețea și internet > DNS privat**. Numele de gazdă al unui furnizor selectează un serviciu DNS privat distinct de DNS-ul anunțat de router. [Setările de rețea Android de la Google](https://support.google.com/android/answer/9654714?hl=en) descriu opțiunile Dezactivat, Automat și Numele gazdei furnizorului. Pentru un rezultat local controlat, testează prin Wi-Fi cu datele mobile dezactivate, apoi restaurează setarea obișnuită.

Pe **dispozitive Apple**, verifică dacă **iCloud Private Relay** este activ pentru rețea și dacă Safari urmează traseul așteptat. Apple spune că [Private Relay protejează navigarea Safari și informațiile DNS](https://support.apple.com/en-gb/102602). [Comenzile de rețea](https://support.apple.com/en-ie/102022) descriu gestionarea per rețea atunci când filtrarea intră în conflict cu Private Relay. Nu generaliza rezultatul Safari la toate aplicațiile dispozitivului.

Un **VPN** poate furniza propriul resolver DNS sau poate trimite interogările prin tunel. Notează dacă VPN-ul este conectat, setările sale DNS și politica de tunelare divizată. Compară același test cu VPN-ul pornit și oprit numai dacă politica ta de securitate permite. Un rezultat diferit indică o diferență de traseu. Singur, nu dovedește o scurgere sau o problemă a filtrului.

## Interpretează rezultatele

| Dovadă | Verificare următoare probabilă |
|---|---|
| **Interogarea directă lipsește din jurnalul filtrului** | Adresa filtrului, serviciul DNS, jurnalizarea sau accesibilitatea rețelei |
| **Interogarea directă este permisă** | Regula exactă de refuz, politica grupului sau prioritatea regulii |
| **Interogarea directă este înregistrată, cea implicită lipsește** | DHCP, DNS static al dispozitivului, DNS IPv6 sau resolver VPN |
| **Interogarea implicită este înregistrată, cea din browser lipsește** | DoH al browserului, memoria cache, proxy sau relay |
| **Ambele sunt înregistrate și blocate, dar site-ul se încarcă** | Alt nume de gazdă, conținut din cache, adresă directă sau traseul aplicației |

**Lipsa înregistrărilor este ambiguă** când jurnalizarea este dezactivată, routerul redirecționează în numele clientului sau testul reutilizează date din cache. Repetă testul cu un nume nou și verifică ora interogării înainte să schimbi regulile firewallului. Blocarea DNS necriptat către resolvere externe nu obligă un browser criptat sau un VPN să folosească filtrul tău. [Ghidul Pi-hole pentru OPNsense](https://docs.pi-hole.net/routers/opnsense/) prezintă blocarea DNS extern ca o măsură de rețea opțională. Politicile dispozitivului și configurarea browserului rămân controale separate.

## Corectează și testează din nou

Schimbă câte un nivel. Corectează anunțurile DHCP sau DNS IPv6, elimină un resolver static neintenționat, selectează furnizorul DNS dorit în browser sau ajustează politica DNS a VPN-ului. Nu slăbi pe ascuns DNS criptat sau protecția relay pe toate dispozitivele pentru un singur test nereușit. Notează dispozitivul sursă, interfața, adresa filtrului, numele cerut, ora, răspunsul, clientul din jurnal, modul browserului, starea VPN-ului și schimbarea făcută.

Rulează din nou testele **direct**, **implicit** și **în browser** după fiecare schimbare. Folosește un nume nou pentru fiecare rulare. Dacă un dispozitiv are mai multe profiluri de rețea, testează-le separat. [Comparația resolverelor DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) ajută la alegerea unui serviciu. [Testul de scurgeri al browserului](/articles/privacy-browser-leak-test-dns-webrtc/) răspunde la altă întrebare: ce informații de rețea ies din configurația browserului și VPN-ului. **Un rezultat fiabil al filtrului cere o regulă verificată și un traseu al clientului verificat.**

## Pașii următori

Repetă testele directe, implicite și din browser după fiecare schimbare controlată. Consultă [comparația resolverelor DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) când alegi un serviciu de filtrare.

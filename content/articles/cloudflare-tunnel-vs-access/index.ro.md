---
title: "Cloudflare Tunnel și Access: ai nevoie de ambele?"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Înțelege diferența dintre Cloudflare Tunnel și Access, alege protecția pentru un panou de acasă și evită publicarea unei aplicații private fără autentificare."
genre: ["Securitatea rețelelor", "Găzduire proprie", "Securitate cloud"]
tags: ["Cloudflare Tunnel", "Cloudflare Access", "Cloudflare Tunnel și Access", "Cloudflare Zero Trust", "cloudflared", "aplicații găzduite propriu", "securitatea homelabului", "acces la distanță", "furnizor de identitate", "politici de acces", "autentificarea aplicației", "nume de gazdă public", "protecția originii", "tunel de ieșire", "tokenuri de serviciu", "Service Auth", "MFA", "panou privat", "proxy invers", "CGNAT"]
cover: "/img/cover/cloudflare-tunnel-vs-access.webp"
coverAlt: "Un server de acasă se conectează printr-un pasaj transparent la un gateway cloud cu un punct separat de verificare a identității."
coverCaption: ""
---

**Cloudflare Tunnel** conectează aplicația la Cloudflare. **Cloudflare Access** controlează cine ajunge la ea. Pentru un panou privat de acasă publicat printr-un nume de gazdă public, folosește-le pe amândouă. Un tunel funcțional nu adaugă singur o verificare a identității. [Ghidul Cloudflare pentru publicarea aplicațiilor](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) explică diferența.

## Idei principale

- **Explică traseul:** deosebește conectorul, originea și verificarea identității.
- **Configurează o politică:** permite anumitor persoane să acceseze un panou privat.
- **Evaluează protecția:** testează căile de acces permise, respinse și alternative.
- **Proiectează accesul:** documentează separat cerințele pentru vizitatori și automatizări.

## Înainte să începi

**Public țintă:** proprietarii de servere de acasă care vor să protejeze un panou accesat din browser. Exemplul presupune un domeniu activ în Cloudflare, o aplicație web locală funcțională și permisiunea de a le administra pe amândouă. **Efort estimat:** 20–30 de minute pentru exercițiul de politică după configurarea conectorului. **Dificultate:** de la începător la intermediar.

**Ordinea lecturii:** începe cu rolurile produselor, urmărește o solicitare, apoi configurează și revizuiește o politică simplă. Încheie scriind o specificație de acces pentru serviciul tău.

## Ce face fiecare produs

**Originea** este serverul care rulează aplicația. Conectorul **`cloudflared`** inițiază conexiuni din infrastructura ta către Cloudflare, așa că originea nu are nevoie de o adresă IP publică rutabilă. Solicitările și răspunsurile călătoresc apoi prin conexiunea stabilită. [Prezentare generală Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

| Întrebare | Tunnel | Access |
|---|---|---|
| **Cum ajunge Cloudflare la serverul meu?** | Stabilește conexiunea | Nu înlocuiește conectivitatea cu originea |
| **Cine primește acces?** | Nu oferă singur autentificare pentru utilizatori | Evaluează politicile de acces configurate |
| **Ce configurez?** | Conectorul și ruta aplicației | Aplicația, furnizorul de identitate și politicile |
| **Ce dovedește succesul?** | Originea este accesibilă prin rută | O solicitare a respectat politica configurată |

Un **furnizor de identitate (IdP)** autentifică vizitatorul. O **politică Access** definește o acțiune și criterii de potrivire. Allow permite accesul utilizatorilor potriviți. Bypass dezactivează aplicarea Access pentru traficul potrivit. [Referință pentru politicile Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

## Urmărește o solicitare din browser

Pentru **`dashboard.example.com`**, traseul logic al solicitării este:

```text
Navigator web -> Cloudflare Access -> conexiunea tunelului -> cloudflared -> panou de control
                         |
                         +-> furnizor de identitate atunci când este necesară autentificarea
```

**Conectorul inițiază conexiunea de tunel spre exterior** din rețeaua ta. Apoi, solicitările browserului ajung la origine prin conexiunea stabilită. O conexiune de ieșire care transportă solicitări de intrare către aplicație este principalul motiv pentru care Tunnel funcționează fără redirecționarea tradițională a unui port către origine. [Modelul de conexiune Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

**Permisiunile aplicației** reprezintă o decizie separată. Accesul la panou nu stabilește automat cine îi poate modifica setările sau șterge datele. Dacă aplicația are roluri de vizualizare și administrare, configurează-le și testează-le separat.

De exemplu, **un membru al familiei cu acces de vizualizare** trebuie să poată vedea starea copiilor de rezervă, în timp ce tu trebuie să le poți schimba destinațiile. Notează cerințele înainte să alegi identitățile. Două persoane care trec aceeași verificare Access nu ar trebui să primească automat aceleași privilegii în aplicație.

## Când ai nevoie de ambele

**Publicul determină protecția.** Compară aceste configurații înainte să publici o rută:

| Public vizat | Configurație sugerată | Verifică înainte de utilizare |
|---|---|---|
| **Oricine citește un site public** | Tunnel dacă este necesar pentru conectarea la origine | Expunerea publică este intenționată |
| **Tu și câțiva membri ai familiei** | Tunnel și Access | Permite doar identitățile vizate |
| **O origine publică existentă** | Access cu protecție separată a originii | Accesul direct la origine nu ocolește verificarea |
| **Un script programat** | Tunnel și o politică Service Auth | Clientul acceptă metoda de autentificare |

**Access fără Tunnel** este disponibil pentru o origine deja accesibilă. Protejează și rutele alternative către server. Cloudflare recomandă crearea aplicației Access înainte de publicarea unei rute noi de tunel. [Cerințe pentru aplicațiile găzduite propriu](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/).

*Pentru un panou privat de acasă accesat printr-un nume de gazdă public, începe cu Tunnel și Access.*

## Configurează o politică pentru panou

Folosește această **configurație demonstrativă** pentru doi vizitatori vizați. Înlocuiește ambele adrese de exemplu cu identități pe care le controlezi. Creează aplicația Access înainte să adaugi ruta publică a tunelului.

1. **Aplicație:** deschide Zero Trust → Access controls → Applications și creează o aplicație găzduită propriu, cu un nume de gazdă public.
2. **Nume de gazdă:** introdu numele de gazdă dedicat panoului. Lasă calea fără restricții pentru acest exemplu care acoperă întregul nume de gazdă.
3. **Politică:** creează o politică Allow numită `Dashboard viewers`.
4. **Selector de identitate:** adaugă o regulă Include folosind Emails și înlocuiește `alice@example.com` și `bob@example.com` cu cele două adrese vizate.
5. **Autentificare:** selectează furnizorul de identitate folosit de vizitatori și alege atent durata sesiunii.
6. **Rută:** salvează aplicația, apoi conectează numele de gazdă la panou prin tunel.

[Fluxul oficial de configurare a aplicației](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/) descrie aceste setări. **Rezultat așteptat:** un vizitator nou se autentifică înainte de a ajunge la aplicație. Efectuează testul de identitate respinsă de mai jos înainte să te bazezi pe politică.

## Interpretează logica regulilor

**Include** combină alternativele cu OR. **Require** adaugă condiții obligatorii cu AND. **Exclude** elimină utilizatorii potriviți. O condiție Include suplimentară mărește grupul eligibil. [Semantica regulilor Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

| Fragment de politică | Efect logic |
|---|---|
| **Include Alice or Bob** | Este suficientă una dintre identitățile numite |
| **Include Alice, Include a country** | Sunt acceptați și oamenii potriviți cu țara |
| **Include Alice, Require a country** | Alice trebuie să respecte și condiția privind țara |

**Exercițiu de revizuire a politicii:** cerința numește doar Alice și Bob, dar un coleg adaugă o țară ca altă condiție Include. Respinge schimbarea, deoarece permite accesul unui grup suplimentar. Geografia nu dovedește că o persoană face parte din familia ta.

## Autentifică scripturile programate

Un **token de serviciu** conține un Client ID și un Client Secret pentru solicitări automate. Configurează politica aplicației să accepte tokenul prin **Service Auth**. Crearea unui token fără politica asociată nu oferă acces la aplicație. [Tokenuri de serviciu Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).

Pentru un script de backup sau o verificare de monitorizare, păstrează **secretul** în stocarea protejată a acreditărilor instrumentului. Alege pentru fiecare integrare un nume distinct de token și o dată de expirare justificată. Rotește sau revocă tokenul când dezactivezi integrarea. Documentația tokenurilor de serviciu descrie aceste operații.

**Verifică explicit compatibilitatea clientului.** Un instrument care așteaptă un răspuns API nu va gestiona neapărat o autentificare interactivă în browser. Înainte să alegi politica, confirmă că acceptă antete de solicitare sau altă metodă de autentificare compatibilă.

## Testează deciziile de acces

Folosește aceste **criterii de acceptare** pentru implementare:

| Test | Dovadă de înregistrat |
|---|---|
| **Vizitator neautentificat** | Access interceptează o solicitare dintr-o sesiune nouă de browser |
| **Identitate permisă** | Aplicația vizată se încarcă după autentificare |
| **Identitate respinsă** | Un cont nelistat nu primește acces la aplicație |
| **Rută alternativă** | Numele DNS vechi și porturile originii nu oferă acces neintenționat |
| **Automatizare** | Clientul aprobat funcționează, iar o solicitare fără acreditare eșuează |

**Un ecran vizibil de autentificare** dovedește doar că o cale a cerut autentificare. Testează și cazul respins, precum și rutele alternative. Acestea sunt verificări sugerate, nu rezultate dintr-un exemplu implementat.

## Verifică limita originii

O **origine care se bazează pe identitatea Access** ar trebui să valideze tokenul de aplicație semnat. Cloudflare îl transmite în antetul **`Cf-Access-Jwt-Assertion`**. Prezența antetului nu dovedește singură autenticitatea. [Validarea JWT Cloudflare](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/).

Un **JSON Web Token (JWT)** conține afirmații semnate. Când integrezi identitatea Access cu o origine, folosește metoda de validare documentată, inclusiv emitentul așteptat și audiența aplicației. Decodarea tokenului și citirea câmpului de e-mail nu reprezintă o validare suficientă.

**Issuer** indică autoritatea care emite tokenul. **Audience** indică aplicația vizată. Verifică validitatea și expirarea tokenului cu o bibliotecă de validare acceptată, în loc să implementezi verificările de semnătură de la zero.

**Definește clar limita:** identifică locul validării și rutele care ajung la aplicație. O redirecționare veche de port sau un nume de gazdă alternativ merită o revizuire separată chiar și după ce numele principal trece toate testele din browser.

## Rezolvă nepotrivirile de politici

| Observație | Următoarea verificare |
|---|---|
| **Un vizitator neașteptat obține acces** | Verifică condițiile Include, politicile Bypass și acoperirea numelui de gazdă |
| **Un vizitator vizat este respins** | Compară identitatea autentificată cu valorile exacte ale selectorului |
| **Un script primește o pagină de autentificare** | Verifică acreditarea și politica Service Auth |
| **Un vizitator admis schimbă setările** | Verifică rolurile atribuite în aplicație |

**Comportamentul sesiunii** influențează și retestarea. Access oferă mai multe durate ale sesiunii, inclusiv sesiuni la nivel de aplicație și globale. Înregistrează setarea și folosește o sesiune nouă când verifici o identitate nouă. [Gestionarea sesiunilor Access](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/).

## Scrie specificația de acces

Pregătește o **specificație scurtă** înainte să adaugi un alt serviciu:

```text
Serviciu și nume de gazdă:
Identități umane permise:
Roluri necesare în aplicație:
Acreditare de automatizare și expirare:
Alte rute către origine:
Locul în care sunt validate tokenurile Access:
Rezultatul testului cu identitatea permisă:
Rezultatul testului cu identitatea respinsă:
```

**Criteriu de finalizare:** un alt administrator trebuie să înțeleagă cine primește acces, cum se autentifică fiecare client și ce dovezi confirmă refuzul. Dacă adaugi ulterior o integrare de monitorizare, actualizează înregistrarea acreditării și repetă verificarea solicitării neautentificate.

## Pașii următori

Urmează [ghidul de configurare Cloudflare Tunnel](/guides/how-to-setup-and-use-cloudflare-tunnels/) pentru configurarea conectorului, apoi aplică [fluxul oficial al aplicației Access](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/self-hosted-public-app/). Pentru o conexiune celulară, citește despre [limitele de redirecționare a porturilor pentru T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/) înainte să alegi accesul la distanță.

---
title: "Un ghid pentru autentificarea cu mai mulți factori: tipuri și bune practici"
date: 2023-03-02
toc: true
draft: false
description: "Aflați despre diferitele tipuri de autentificare cu mai mulți factori și despre cum să o alegeți pe cea mai bună pentru nevoile dvs. de securitate în ghidul nostru final."
tags: ["autentificare multifactor", "securitate online", "securitatea parolei", "factori de autentificare", "autentificare cu doi factori", "jetoane hardware", "autentificare software", "securitate cibernetică", "atacuri de tip phishing", "prevenirea hackingului", "protejarea datelor", "verificarea identității", "siguranța parolei", "jetoane de securitate", "controlul accesului", "furt de identitate", "amenințări cibernetice", "securitate digitală", "aplicații de autentificare", "apărare cibernetică"]
cover: "/img/cover/A_cartoon_person_standing_in_front_of_a_computer.png"
coverAlt: "O persoană din desene animate care stă în fața unui computer, cu un simbol de lacăt deasupra capului și diferite tipuri de factori de autentificare, cum ar fi o cheie, un telefon, o amprentă etc., plutind în jurul lor"
coverCaption: ""
---

Odată cu creșterea încălcărilor de securitate online, a devenit necesar să se utilizeze mai mult decât o parolă pentru a securiza accesul la informațiile sensibile. Aici intervine **autentificarea cu mai mulți factori**, care oferă un nivel suplimentar de securitate, solicitând utilizatorilor să furnizeze doi sau mai mulți factori de autentificare pentru a avea acces la conturile lor.

## Diferitele tipuri de factori în MFA

Există mai multe tipuri de factori de autentificare utilizați în autentificarea cu mai mulți factori:

- **Ceva ce știți:** Aceasta include informații pe care numai utilizatorul le cunoaște, cum ar fi o parolă, un PIN sau un răspuns la o întrebare de securitate. Un exemplu în acest sens este autentificarea la un cont de social media folosind o parolă.

- **Ceva ce aveți:** Acesta include un obiect fizic pe care îl deține numai utilizatorul, cum ar fi o cheie USB, un card inteligent sau un telefon mobil. Un exemplu în acest sens este utilizarea unui card inteligent pentru a accesa o facilitate guvernamentală securizată.

- **Ceva ce sunteți:** Aceasta include informații biometrice, cum ar fi amprentele digitale, recunoașterea facială sau scanările irisului. Un exemplu în acest sens este deblocarea unui smartphone folosind recunoașterea facială.

- **Undeva unde vă aflați:** Aceasta include informații bazate pe locație, cum ar fi locația GPS a utilizatorului sau adresa IP. Un exemplu în acest sens este o bancă care solicită unui utilizator să își autentifice locația înainte de a permite accesul la contul său.

- **Ceva ce faci:** Aceasta include datele biometrice comportamentale, cum ar fi viteza de tastare a utilizatorului, mișcările mouse-ului sau modelele de vorbire. Un exemplu în acest sens este un sistem care poate recunoaște modul în care un utilizator scrie pentru a-și autentifica identitatea.

Utilizarea mai multor factori pentru a autentifica identitatea unui utilizator este mai sigură decât utilizarea unui singur factor, cum ar fi o parolă. Prin utilizarea unei combinații de factori de autentificare, atacatorilor devine mult mai greu să obțină acces neautorizat la informații sensibile.

### Avantajele și dezavantajele fiecărui factor din MFA

Iată avantajele și dezavantajele fiecărui tip de autentificare multi-factor (MFA):

- **Ceva ce știi:**

  - Pro: Ușor de utilizat, poate fi schimbat frecvent și poate fi partajat cu mai multe persoane (cum ar fi parola unei echipe).
  
  - Contra: poate fi compromis de phishing, ghicire sau atacuri cu forță brută și poate fi uitat sau pierdut.

- **Ceva ce ai:**

  - Pro: dificil de copiat sau furat, poate fi folosit offline și poate fi înlocuit cu ușurință dacă este pierdut sau furat.
  
  - Contra: Poate fi uitat sau pierdut, poate fi furat dacă nu este asigurat corespunzător și poate fi costisitor de implementat.

- **Ceva esti:**

  - Pro: Unic pentru fiecare individ, greu de falsificat și nu poate fi pierdut sau uitat.
  
  - Contra: poate fi afectat de schimbările în aspectul utilizatorului, poate fi dificil de implementat pentru grupuri mari de utilizatori și poate fi văzut ca invaziv.

- **Undeva esti:**

  - Avantaje: poate oferi un context suplimentar pentru autentificare, cum ar fi asigurarea că utilizatorul se află în locația geografică corectă.
  
  - Contra: poate fi falsificat folosind rețele private virtuale (VPN) sau servere proxy, poate fi inexact sau imprecis și poate fi dificil de implementat pentru utilizatorii de telefonie mobilă.

- **Ceva ce faci:**

  - Pro: dificil de duplicat, poate fi folosit pentru a identifica anumite persoane și nu poate fi pierdut sau uitat.
  
  - Contra: poate fi afectat de vătămare sau dizabilitate, poate necesita hardware sau software specializat și poate să nu fie eficient pentru toți utilizatorii.
  
În timp ce autentificarea bazată pe hardware, cum ar fi utilizarea unui token fizic precum YubiKey de la Yubico, este considerată cea mai sigură, autentificarea pe bază de SMS și autentificarea pe bază de e-mail sunt considerate cele mai puțin sigure metode, deoarece sunt vulnerabile la interceptare și falsificare.

### Cea mai bună metodă de autentificare cu mai mulți factori pentru securitate

În timp ce toate tipurile de autentificare cu mai mulți factori oferă o securitate mai bună decât utilizarea doar a unei parole, unele metode sunt mai sigure decât altele. Autentificare bazată pe hardware, cum ar fi utilizarea unui token fizic precum [Yubico's YubiKey](https://amzn.to/3kPk1wy) or the [OnlyKey](https://amzn.to/3Zi5SXM) sunt considerate cele mai sigure deoarece necesită posesia fizică a jetonului, generează un cod unic pentru fiecare încercare de conectare și nu sunt susceptibile la atacuri de phishing sau hacking.

Autentificarea pe bază de SMS și autentificarea pe bază de e-mail sunt considerate cele mai puțin sigure metode, deoarece sunt vulnerabile la interceptare și falsificare.

### O metodă bună de compromis între securitate și ușurință în utilizare

Generarea de token 2FA bazată pe software este un compromis bun între ușurința în utilizare și securitate. În loc să se bazeze pe jetoane hardware fizice, jetoanele 2FA bazate pe software sunt generate de o aplicație pe smartphone-ul sau computerul utilizatorului.

Aceste aplicații generează de obicei un cod unic pentru fiecare încercare de conectare, oferind un nivel suplimentar de securitate, dincolo de o parolă. Acest tip de 2FA este mai sigur decât autentificarea pe bază de SMS și autentificarea pe bază de e-mail, care sunt vulnerabile la interceptare și falsificare.

Token-urile 2FA bazate pe software au capacitatea de a fi salvate mai ușor decât jetoanele hardware, care pot fi atât un pro, cât și un contra. Pe de o parte, aceasta înseamnă că utilizatorii își pot transfera mai ușor 2FA pe un dispozitiv nou dacă îl pierd pe cel vechi, făcându-le mai convenabil să-și acceseze conturile.

Cu toate acestea, aceasta înseamnă și că, dacă cineva obține acces la codul de rezervă al unui utilizator, poate obține acces la toate conturile sale care folosesc acel token 2FA. Ca atare, este important ca utilizatorii să-și păstreze codurile de rezervă într-o locație sigură, cum ar fi un manager de parole sau o unitate criptată.
______

## Tipuri de autentificare cu mai mulți factori

Există mai multe tipuri de metode de autentificare multifactorială disponibile, fiecare folosind diferite combinații ale factorilor de autentificare:

- **Autentificare cu doi factori (2FA):** Acesta este cel mai comun tip de autentificare cu mai mulți factori și necesită utilizatorilor să furnizeze doi factori de autentificare diferiți, cum ar fi o parolă și un cod de verificare trimis prin SMS.

- **Autentificare în trei factori (3FA):** Acest lucru necesită utilizatorilor să furnizeze trei factori de autentificare diferiți, cum ar fi o parolă, o scanare a amprentei și un smart card.

- **Autentificare cu patru factori (4FA):** Acesta este cel mai sigur tip de autentificare cu mai mulți factori și necesită utilizatorilor să furnizeze patru factori diferiți de autentificare, cum ar fi o parolă, o scanare a amprentei, un card inteligent și un facial. scanează.

______

## Merită folosirea a mai mult de doi factori?

Decizia de a utiliza mai mult de doi factori în autentificarea cu mai mulți factori depinde în cele din urmă de nivelul de securitate necesar pentru cont. Pentru majoritatea conturilor, autentificarea cu doi factori este suficientă. Cu toate acestea, pentru conturile extrem de sensibile, cum ar fi cele care conțin informații financiare sau medicale, utilizarea a mai mult de doi factori, cum ar fi o combinație între ceva ce cunoașteți, ceva ce aveți și ceva ce sunteți, poate oferi un nivel suplimentar de securitate.

______

## Probleme cu jetoanele hardware

În timp ce autentificarea bazată pe hardware este considerată cea mai sigură metodă de autentificare cu mai mulți factori, există probleme cu utilizarea token-urilor hardware. Pentru a asigura securitatea maximă, ar trebui să utilizați un singur token hardware pentru toate conturile dvs. și să îl păstrați într-o locație sigură despre care doar puțini oameni îl cunosc. În plus, dacă vă îmbolnăviți grav sau decedați, este posibil ca cei dragi să nu vă poată accesa conturile dacă aveți un singur token hardware.

Ca rezervă, se recomandă să utilizați o metodă de autentificare secundară, cum ar fi o aplicație de autentificare bazată pe software, pentru a vă asigura că vă puteți accesa conturile dacă pierdeți sau pierdeți simbolul hardware. Cu toate acestea, acest lucru nu este recomandabil în toate situațiile. Și depinde de tine să iei decizia asupra a ceea ce este o prioritate. Securitate sau conviețuire.

## Concluzie

În lumea digitală de astăzi, nevoia de măsuri solide de securitate online a devenit mai importantă decât oricând. Autentificarea cu mai mulți factori este o componentă critică a securității online, oferind un nivel suplimentar de protecție care face mult mai dificil pentru atacatori să obțină acces neautorizat la informații sensibile.

Cerând utilizatorilor să furnizeze mai mulți factori de autentificare, cum ar fi ceva pe care îl cunosc, ceva pe care îl au sau ceva ce sunt, MFA ajută la prevenirea metodelor obișnuite de atac, cum ar fi phishingul, atacurile cu forță brută și ghicirea parolelor. În timp ce autentificarea bazată pe hardware este considerată cea mai sigură metodă, tokenurile 2FA bazate pe software oferă un echilibru bun între securitate și ușurință în utilizare.

În cele din urmă, decizia de a utiliza mai mult de doi factori în MFA depinde de nivelul de securitate necesar pentru cont. Pentru majoritatea conturilor, autentificarea cu doi factori este suficientă, dar pentru conturile extrem de sensibile, utilizarea a mai mult de doi factori poate oferi un nivel suplimentar de securitate.

În concluzie, implementarea autentificării multifactoriale este un pas important în securizarea conturilor dvs. online și protejarea informațiilor sensibile împotriva amenințărilor cibernetice.

## Referințe

- [NIST Special Publication 800-63B: Digital Identity Guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63b.pdf)
- [Yubico's - Authentication standards](https://www.yubico.com/authentication-standards/)
- [Microsoft's - Multifactor authentication in Azure AD ](https://www.microsoft.com/en-us/security/business/identity-access/azure-active-directory-mfa-multi-factor-authentication)
- [Google's Guide to Two-Factor Authentication](https://www.google.com/landing/2step/)
- [Okta's - Setting Up and Authenticating with Multi-factor Authentication (MFA)](https://support.okta.com/help/s/end-user-adoption-toolkit/setting-up-mfa-for-end-users?language=en_US)

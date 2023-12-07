---
title: "Preîncărcarea HSTS Cum se îmbunătățește securitatea site-urilor web: Un ghid pas cu pas"
date: 2023-08-20
toc: true
draft: false
description: "Aflați cum să îmbunătățiți securitatea site-urilor web și încrederea utilizatorilor prin preîncărcarea setărilor HSTS în Chrome și Firefox. Urmați ghidul nostru pas cu pas pentru o implementare fără probleme."
cover: "/img/cover/enhanced-website-security.png"
coverAlt: "O ilustrație în stil de desen animat a unui site web protejat cu un lacăt, reprezentând securitate sporită și protecție împotriva amenințărilor cibernetice."
coverCaption: "Întăriți apărarea site-ului dvs. web, adoptați preîncărcarea HSTS."
---

## **Îmbunătățiți securitatea site-ului web cu preîncărcarea HSTS: Un ghid pas cu pas**

HTTP Strict Transport Security (HSTS) este un **mecanism de securitate crucial** care asigură că site-urile web impun conexiuni HTTPS pentru a **proteja utilizatorii de potențiale amenințări de securitate**. Prin preîncărcarea setărilor HSTS în Chrome și Firefox, puteți **îmbunătăți securitatea site-urilor web** și consolidați **încrederea utilizatorilor**. În acest ghid cuprinzător, vă vom ghida prin **etapele esențiale** pentru a preîncărca cu succes setările HSTS și vă vom oferi **recomandări utile** pentru a optimiza securitatea.

______

### **Înțelegerea preîncărcării HSTS**

**HSTS Preloading** este procesul de **submitere a domeniului site-ului dvs. web** în listele de preîncărcare ale principalelor browsere. Odată adăugate, aceste browsere vor **impune automat conexiuni HTTPS** pentru domeniul dvs. și toate subdomeniile. Acest lucru asigură faptul că utilizatorii accesează întotdeauna site-ul dvs. web în siguranță, reducând riscul **atacurilor de tip **man-in-the-middle** și al ascultării neautorizate. Pentru mai multe detalii despre preîncărcarea HSTS, puteți consulta pagina oficială [documentation](https://hstspreload.org/)

______

______

### **Cerințe de prezentare**

Înainte de a vă trimite domeniul pentru preîncărcarea HSTS, asigurați-vă că site-ul dvs. web îndeplinește următoarele **cerințe esențiale**:

1. **Certificat valid**: Site-ul dvs. web trebuie să servească un **certificat SSL sau TLS valabil** pentru a permite **conexiuni HTTPS securizate**.

2. **Redirecționare de la HTTP la HTTPS**: Asigurați-vă că toate cererile **HTTP sunt redirecționate** către omologii lor **HTTPS** atunci când site-ul dvs. web ascultă pe portul 80.

3. **HTTPS pentru toate subdomeniile**: Toate subdomeniile site-ului dvs. web trebuie să **susțină conexiuni HTTPS** pentru a fi eligibile pentru preîncărcarea HSTS.

4. **HHSTS Header pe domeniul de bază**: Includeți un ** antet HHSTS** pe domeniul dvs. de bază pentru solicitările HTTPS cu următoarele setări:
   - `max-age` trebuie să fie de **cel puțin 31536000 secunde** (1 an).
   - În cazul în care `includeSubDomains` trebuie să fie specificată pentru a include toate subdomeniile.
   - În cazul în care `preload` trebuie să fie specificată pentru a solicita includerea în lista de preîncărcare.

Iată un exemplu de antet HSTS valid:

```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

______

### **Cum să preîncărcați setările HSTS**

Dacă site-ul dvs. web este **complet angajat la HTTPS** și îndeplinește cerințele de mai sus, urmați acești **pasi cruciali** pentru a preîncărca cu succes setările HSTS:

1. **Examinați subdomeniile**: Asigurați-vă că toate **subdomeniile **subdomeniile site-ului dvs. web** funcționează corect prin HTTPS pentru a oferi utilizatorilor o experiență de navigare fără întreruperi.

2. **Rapidare treptată**: Pentru a testa și a remedia orice potențiale probleme, adăugați antetul **HSTS** la răspunsurile dvs. HTTPS cu un **low `max-age` valoare** (de exemplu, 300 de secunde). Creșteți treptat valoarea `max-age` valoare în etape:
   - 5 minute: `max-age=300; includeSubDomains`
   - 1 săptămână: `max-age=604800; includeSubDomains`
   - 1 lună: `max-age=2592000; includeSubDomains`

3. **Monitorizarea parametrilor**: În timpul fiecărei etape, **monitorizați îndeaproape indicatorii site-ului dvs. web**, inclusiv traficul și veniturile, pentru a identifica și rezolva orice problemă înainte de a trece la etapa următoare.

4. **Creșteți vârsta maximă la 2 ani**: Odată ce sunteți **confirmat că nu mai există probleme**, setați `max-age` la **2 ani (63072000 secunde)** și se adaugă `preload` la antetul HSTS:
```http
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```

5. **Submiteți site-ul dumneavoastră**: După implementarea perioadei de 2 ani `max-age` **subscrieți-vă site-ul** pe lista de preîncărcare HSTS folosind formularul disponibil la adresa [hstspreload.org](https://hstspreload.org/) Rețineți că includerea în lista de preîncărcare poate dura câteva luni pentru a ajunge la utilizatorii cu o actualizare Chrome.
______

### **Opt-In pentru preîncărcarea HSTS: Împuternicirea operatorilor de site-uri**

Sprijinirea preîncărcării HSTS este o **practică de securitate excelentă** care îmbunătățește protecția site-ului web. Cu toate acestea, ar trebui să fie o decizie **opt-in** pentru operatorii de site-uri. Dacă oferiți **consiliere privind configurarea HTPS** sau oferiți o opțiune pentru a activa HSTS, **evitați să includeți `preload` în mod implicit**. Această abordare previne includerea neintenționată în lista de preîncărcare, ceea ce poate duce la dificultăți în accesarea anumitor subdomenii.

Pentru a asigura o experiență fără probleme, **informați operatorii de site-uri** cu privire la **consecințele pe termen lung** ale preîncărcării și subliniați **importanța îndeplinirii tuturor cerințelor** înainte de a activa HSTS pentru domeniul lor.

______

### **Remiterea din lista de preîncărcare: O decizie deliberată**

Includerea în lista de preîncărcare este o **decizie permanentă** care nu poate fi ușor de anulat. Cu toate acestea, dacă întâmpinați **motive tehnice puternice sau legate de costuri** care împiedică suportul HTTPS pentru anumite subdomenii, aveți opțiunea de a solicita **eliminarea din lista de preîncărcare a Chrome** prin intermediul aplicației [removal form](https://hstspreload.org/removal/)

Asigurați-vă că ați evaluat cu atenție implicațiile înainte de a lua această decizie importantă.
______

______

### **Safer Browsing Starts with HSTS Preloading**

În concluzie, preîncărcarea setărilor HSTS în Chrome și Firefox este un **pas proactiv** pentru o experiență de navigare mai sigură pentru utilizatorii dvs. Prin **forțarea conexiunilor HTTPS**, vă **protejați datele sensibile** și creați **încredere** în rândul vizitatorilor dvs. Urmați **ghidurile** menționate mai sus pentru a **preîncărca cu succes setările HSTS** și a vă bucura de **securitatea îmbunătățită a site-ului web**.

______

### Referințe

1. [Chromium - HTTP Strict Transport Security (HSTS)](https://www.chromium.org/hsts/)
2. [HSTS Preload Submission](https://hstspreload.org/)
3. [Mozilla Web Security Guidelines](https://infosec.mozilla.org/guidelines/web_security)
4. [Google Web Fundamentals - Security](https://developers.google.com/web/fundamentals/security/)

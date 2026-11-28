---
title: "Laborator SOC Microsoft acasă: dezvoltă experiență în securitate cibernetică în 2026"
date: 2026-09-11
lastmod: 2026-11-27
toc: true
draft: false
description: "Construiește un laborator SOC Microsoft cu Sentinel, Defender, Intune și Entra. Investighează incidente, validează politicile de passkey și documentează dovezi pentru portofoliu."
genre: ["Securitate cibernetică", "Securitate cloud", "Dezvoltare profesională"]
tags: ["laborator SOC acasă", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "laborator Azure acasă", "experiență în securitate cibernetică", "analist SOC", "centru de operațiuni de securitate", "răspuns la incidente", "KQL", "Log Analytics", "Conditional Access", "MFA rezistent la phishing", "passkey-uri", "securitatea identității", "portofoliu de securitate cibernetică", "gestionarea costurilor cloud", "securitatea endpointurilor"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Un laptop afișează cronologii ale incidentelor de securitate pe un birou de acasă, sub un nor cu servere și endpointuri."
coverCaption: ""
---

Un **laborator SOC de acasă** oferă un loc unde poți investiga alerte, explica dovezi și testa schimbări defensive. Construiește un mediu Microsoft restrâns, colectează telemetria și documentează fiecare investigație. Rezultatul util este o investigație repetabilă, susținută de dovezi.

Acest ghid dezvoltă abordarea de laborator descrisă în videoclipul despre cariere în securitate cibernetică al lui Mad Hat și în runbook-ul Cyber Range furnizat. Folosește documentația Microsoft pentru cerințele produselor și împarte configurarea, detectarea și validarea în sarcini măsurabile.

## Idei principale

- **Începe cu puțin:** un client Windows gestionat și o identitate de test ajung pentru primele exerciții.
- **Verifică telemetria:** un dispozitiv vizibil sau un portal conectat nu dovedește că sosesc jurnalele.
- **Finalizează investigația:** notează declanșatorul, dovezile, răspunsul și retestarea.
- **Controlează cheltuielile:** urmărește separat licențele, păstrarea datelor, rețeaua și calculul.
- **Descrie experiența corect:** prezintă mediul drept proiect de laborator în CV.

## Înainte să începi

**Cerințe preliminare:** cunoștințe de bază de administrare Windows și rețelistică, plus familiaritate cu mașinile virtuale. Folosește un tenant Microsoft Entra dedicat și o subscripție Azure rezervată laboratorului. Ține în afara exercițiului identitățile de producție, fișierele personale și sistemele angajatorului.

**Efort estimat:** rezervă un weekend pentru configurarea inițială, apoi planifică sesiuni de investigare concentrate. Aceasta este o estimare de planificare. Aprobarea perioadei de testare, cotele și furnizarea serviciilor influențează durata reală. **Dificultate:** intermediară.

Pregătește un cont administrativ separat și un utilizator de test fără privilegii. Înainte de a testa politicile de acces, configurează și verifică accesul de urgență. Acordă privilegii pentru fiecare sarcină de configurare, apoi folosește un cont cu drepturi mai reduse pentru investigațiile obișnuite.

| Componentă | Scop în laborator |
|---|---|
| **Sentinel** | Gestionarea informațiilor și evenimentelor de securitate (SIEM) pentru sursele de jurnale conectate |
| **Defender XDR** | Corelare și investigare între serviciile Microsoft de securitate licențiate |
| **Defender for Endpoint** (protecția dispozitivelor) | Detectare și răspuns pe endpointurile integrate |
| **Intune** | Înrolarea dispozitivelor și gestionarea politicilor de securitate pentru endpointuri |
| **Entra ID** | Identități, înregistrări de conectare și evaluarea politicilor de acces |
| **Defender for Servers** (protecția serverelor) | Protecția serverelor prin Defender for Cloud |

## Verifică mai întâi licențele

**Microsoft 365 E5** este o opțiune pentru un laborator extins, dar accesul depinde de planurile de servicii și licențele alocate utilizatorilor participanți. Office 365 E5 și Microsoft 365 E5 sunt pachete diferite. Licența unui administrator nu acoperă automat fiecare utilizator de test sau sarcină de lucru. Consultă [cerințele preliminare Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) înainte de a alege o subscripție.

**Sentinel în portalul Defender** funcționează fără E5 sau Defender XDR. Adăugarea XDR are cerințe proprii de licențiere și configurare. O vizualizare goală a incidentelor nu dovedește lipsa licenței E5. [Documentația de onboarding Sentinel](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) explică ambele configurații.

**Protecția serverelor** are o cale separată de licențiere. Defender for Servers se integrează cu Defender for Endpoint pentru sarcinile de server acceptate. Sistemele de operare client Windows au nevoie de acoperire client adecvată. Nu presupune că fiecare VM Azure primește automat o licență de server. Consultă documentația Microsoft despre [integrarea Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Planifică perioada de testare:** verifică eligibilitatea, expirarea, reînnoirea și serviciile incluse în propriul cont. Nu baza bugetul pe o durată promisă a perioadei de testare sau pe un total lunar fix menționat într-un videoclip.

## Planifică cheltuielile

**Bugetele Azure** trimit notificări. Nu opresc consumul când atingi un prag. Rapoartele de cost au și ele întârziere. Creează alerte din timp și verifică cheltuielile după fiecare sesiune folosind [ghidul Microsoft pentru bugete](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Categoria de cost | Întrebare de planificare |
|---|---|
| **Licențe de utilizator** | Ce utilizatori au nevoie de ce planuri de servicii și când expiră perioadele de testare? |
| **Calcul** | De câte ore VM are nevoie fiecare exercițiu? |
| **Stocare** | Ce discuri și instantanee rămân după oprire? |
| **Colectarea jurnalelor** | Ce tabele necesită ingestie și cât timp trebuie păstrate datele? |
| **Rețea** | Proiectul include Bastion cu plată, IP-uri publice sau servicii de ieșire? |
| **Protecția serverelor** | Ce sarcini au activat un plan Defender cu plată? |

**Decizie de proiectare:** începe cu un client. Adaugă un server când un exercițiu necesită telemetrie de server. Patru clienți și mai multe servere cresc administrarea și costurile înainte să adauge practică utilă de investigare.

## Construiește rețeaua

**Structură sugerată:** plasează resursele Azure într-un grup cu nume clar, precum **`rg-soc-lab`**. Folosește subrețele separate pentru clienți și servere, reguli explicite pentru grupurile de securitate de rețea și acces administrativ privat. Separarea subrețelelor nu blochează singură traficul între sarcini.

Pentru o implementare dedicată **Azure Bastion**, respectă cerințele SKU, inclusiv numele rezervat **`AzureBastionSubnet`** și o subrețea de **`/26`** sau mai mare pentru implementările actuale. Developer SKU folosește alt model de implementare. Consultă [setările de configurare Bastion](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) înainte de a alege.

Ține RDP și SSH închise față de internetul public. Limitează traficul administrativ la calea aleasă. Permite conectivitatea de ieșire necesară pentru înrolare și telemetria de securitate.

**Validare:** configurează acces administrativ privat și verifică regulile de rețea efective înainte să instalezi sarcini. Dacă adaugi ulterior o aplicație vulnerabilă intenționat, ține-o în rețeaua exercițiului și limitează accesul la mașinile de test.

## Conectează Sentinel și jurnalele

**Configurarea portalului:** creează un spațiu de lucru Log Analytics și activează Sentinel pe el. Dacă spațiul lipsește din portalul Defender, deschide **System > Settings > Microsoft Sentinel > Connect a workspace** (Sistem > Setări > Microsoft Sentinel > Conectează un spațiu de lucru). Verifică tenantul și rolurile Azure și Entra necesare din [cerințele de onboarding](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**Colectarea jurnalelor este un pas separat.** În Entra, configurează setările de diagnosticare pentru a trimite categoriile de activitate cerute către același spațiu de lucru. Începe cu conectări interactive și evenimente de audit. [Ghidul de integrare a jurnalelor Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) descrie permisiunile și destinația.

Fluxul Sentinel actual acceptă și conectarea prin portalul Microsoft Defender. Înainte să investighezi un tabel gol, confirmă că spațiul principal este cel intenționat, tenantul corespunde identităților de test și contul are rolurile necesare. Vizibilitatea în portal nu dovedește ingestia. [Onboarding Sentinel în portalul Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Rulează exemplul **Kusto Query Language (KQL)** în vizualizarea Logs a spațiului de lucru după ce generezi o conectare nouă de test. Înlocuiește UPN-ul demonstrativ cu utilizatorul laboratorului. Coloanele urmează [schema tabelului SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Rezultat așteptat:** un rând care corespunde contului de test și orei conectării. Fără rânduri, verifică intervalul de timp, identitatea, setările de colectare, destinația și întârzierea ingestiei. Lipsa tabelului indică mai întâi o problemă de colectare sau de spațiu de lucru și abia apoi una de detectare.

## Înrolează primul endpoint

**Înrolarea Intune și onboardingul EDR** sunt puncte de verificare separate. Conectează Intune și Defender for Endpoint, înrolează un client Windows acceptat și atribuie o politică de onboarding EDR grupului său de laborator. Înregistrarea Entra nu confirmă singură niciunul dintre puncte.

În Intune, verifică **Endpoint security > Defender for Endpoint** (Securitatea endpointurilor > Defender for Endpoint (protecția endpointurilor)). Dacă legătura nu este disponibilă, activează conectarea Intune în funcțiile avansate pentru endpointuri ale Defender. Urmează pașii specifici platformei din [ghidul de integrare Intune și Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Punct de verificare | Dovezi de păstrat |
|---|---|
| **Înrolare** | Clientul apare în Intune cu o sincronizare recentă |
| **Atribuire politică** | Politica de onboarding se aplică grupului de dispozitive vizat |
| **Raportarea senzorului** | Defender arată starea de onboarding și telemetrie recentă |
| **Test de detectare** | Un test documentat produce semnalul de securitate așteptat |

**Pentru servere**, activează planul Defender for Servers ales și integrarea endpoint, apoi verifică implementarea senzorului și raportarea. Defender for Cloud descoperă mașinile și înainte de finalizarea onboardingului. Prezența în inventar nu este suficientă, așa cum explică ghidul Microsoft despre [descoperirea și onboardingul resurselor](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Investighează o alertă de test

**Începe cu testul de detectare EDR documentat de Microsoft** pe endpointul laboratorului. Urmează [instrucțiunile curente de testare](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), inclusiv cerințele platformei și depanarea. Notează ora executării înainte de a deschide coada alertelor.

Tratează alerta generată drept exercițiu de investigare. Titlul produsului este doar un punct de pornire. Trebuie să stabilești ce s-a întâmplat și să susții decizia cu dovezi.

1. **Triaj:** identifică sursa alertei, dispozitivul, contul și ora evenimentului.
2. **Inspectare:** verifică arborele proceselor, linia de comandă, detaliile fișierului și activitatea de rețea disponibilă.
3. **Domeniu:** caută activități asociate identității de test și celorlalte dispozitive de laborator.
4. **Evaluare:** explică dacă dovezile corespund exercițiului planificat sau unui eveniment fără legătură.
5. **Răspuns:** documentează răspunsul ales, impactul și recuperarea. Folosește izolarea acceptată numai dacă exercițiul o cere.
6. **Retestare:** după schimbarea unui control, repetă testul relevant și compară dovezile.

**Nu inventa rezultate lipsă.** Dacă alerta nu ajunge, păstrează înregistrarea executării și investighează colectarea. Dacă un control blochează testul înaintea evenimentului așteptat, documentează rezultatul prevenirii.

## Testează controalele de identitate

**Phishingul adversary-in-the-middle (AiTM)** introduce un intermediar controlat de atacator în fluxul de conectare. Runbook-ul furnizat folosește acest scenariu pentru a motiva autentificarea mai puternică. Pentru primul exercițiu de identitate, testează comportamentul politicii direct cu propriul cont fără privilegii.

Începe prin a înregistra o conectare legitimă și detaliile autentificării. Consultă [referința Microsoft privind detectarea riscurilor Entra](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) înainte să interpretezi semnalele de risc. Cerințele și procesarea diferă în funcție de semnal. O adresă IP nouă sau o conectare eșuată nu garantează o alertă AiTM.

**Passkey-urile (FIDO2)** folosesc acreditări legate de serviciul legitim, nu coduri reutilizabile introduse într-o pagină de conectare redirecționată. Activează un profil potrivit pentru grupul-pilot și înregistrează metoda înainte să impui politica. [Ghidul Microsoft de configurare a passkey-urilor](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) descrie autentificatoarele acceptate și restricțiile.

**Exercițiu Conditional Access (acces condiționat):** creează o politică pentru grupul-pilot de laborator, exclude conturile de acces de urgență și alege **Require authentication strength > Phishing-resistant MFA strength** (nivel de autentificare și MFA rezistentă la phishing). Începe în **Report-only (doar raportare)**, verifică efectul, apoi activează politica. Adaptează [exemplul Microsoft de politică pentru administratori](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) unui grup restrâns de test.

| Verificare | Dovezi de colectat |
|---|---|
| **Politică Report-only (doar raportare)** | Înregistrare de conectare care arată evaluarea politicii propuse |
| **Politică impusă, metodă mai slabă** | O autentificare nouă cere o metodă mai puternică înainte de acces |
| **Politică impusă, passkey înregistrat** | Conectare reușită care respectă nivelul cerut |

Folosește autentificare nouă pentru fiecare comparație și verifică detaliile politicii. Sesiunile existente îngreunează comparațiile. **Domeniul dovezii:** exercițiul validează cerința de autentificare. Nu demonstrează protecție universală împotriva compromiterii endpointului sau furtului unei sesiuni existente.

## Scrie dovezi pentru portofoliu

**O intrare utilă în portofoliu** explică o decizie astfel încât alt analist să o poată evalua. Include o descriere scurtă a arhitecturii, condițiile de colectare, cronologia evenimentelor și motivarea răspunsului.

```text
Exercițiu:
Data și intervalul orar UTC:
Domeniul laboratorului și cerințe preliminare:
Declanșator și semnal așteptat:
Alertă observată sau prevenire:
Dovezi și interogări:
Identități și dispozitive afectate:
Concluzie și raționament:
Răspuns și recuperare:
Modificarea controlului și retestare:
Limitări și acțiuni ulterioare:
```

Înlocuiește fiecare câmp cu propriile observații. **Igienizează exporturile:** elimină acreditările, datele de sesiune, informațiile personale și identificatorii care nu sunt necesari înainte să publici capturi sau rezultate de interogări.

**Exemplu pentru CV:** „Am construit un laborator de securitate Microsoft, am conectat jurnalele de identitate la Sentinel, am investigat alerte de test endpoint și am documentat validarea Conditional Access.” Folosește formularea doar după ce ai realizat sarcinile. Include-o la proiecte sau instruire practică, cu datele și domeniul reale.

Un laborator demonstrează practică individuală. **Munca într-un SOC de producție** implică și impact asupra afacerii, escaladare, angajamente de serviciu și coordonare cu alte echipe. Explică ce ai exersat și ce rămâne în afara experienței tale.

## Depanare

| Simptom | Prima verificare |
|---|---|
| **Spațiu de lucru absent din Defender** | Același tenant, Sentinel activ și rolurile necesare pentru onboarding |
| **SigninLogs absent sau gol** | Categorii de diagnosticare, spațiu de destinație, evenimente noi și interval |
| **Client absent din Intune** | Cerințele și starea înrolării |
| **Dispozitiv vizibil fără telemetrie** | Starea reală de onboarding, starea senzorului și conectivitatea de ieșire |
| **Politică de onboarding neaplicată** | Domeniul atribuirii, platforma dispozitivului și sincronizarea recentă |
| **Fără alertă de risc de identitate** | Cerințele semnalului și activitatea înregistrată, fără a presupune detectare deterministă |
| **Acces permis neașteptat** | Starea Report-only (doar raportare), excluderile, domeniul resursei și sesiunea existentă |
| **Costuri după oprire** | Starea de alocare și resursele facturate independent de calcul |

**Ordinea depanării:** dovedește întâi că evenimentul s-a produs, apoi că colectarea a funcționat și abia după aceea investighează logica de detectare. Notează fiecare problemă și remediere în jurnalul proiectului.

## Suspendă sau elimină laboratorul

**Dezafectarea** eliberează alocarea de calcul a VM-ului. Oprirea sistemului de operare invitat nu garantează dezafectarea. Verifică starea de alimentare afișată în Azure și consultă documentația Microsoft despre [stările și facturarea VM-urilor](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Resursele păstrate** necesită și ele revizuire. Discurile, instantaneele, serviciile de rețea, păstrarea jurnalelor și subscripțiile utilizatorilor au cicluri de viață separate. Programează un memento înainte de expirarea fiecărei perioade de testare și verifică următorul raport de utilizare după curățare.

Înainte să ștergi grupul de resurse al laboratorului, exportă și inspectează dovezile pe care vrei să le păstrezi. **Ștergerea grupului de resurse distruge** resursele incluse. Utilizatorii tenantului, politicile Intune și Conditional Access, subscripțiile și setările de securitate la nivel de subscripție pot necesita curățare separată.

## Pașii următori

**Finalizează o investigație documentată** înainte să adaugi o altă sarcină. Apoi adaugă un server, un exercițiu de identitate sau o regulă de detectare cu o condiție clară de testare. Notează ce înveți din componentă și cât costă.

Folosește [ghidul de laborator IT](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) pentru practica de infrastructură și [ghidul de CV IT](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) pentru a-ți prezenta munca. Păstrează următorul proiect suficient de restrâns pentru a explica configurarea, dovezile și curățarea.

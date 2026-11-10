---
title: "În 2026, containerele nu mai sunt o frontieră de securitate"
date: 2026-09-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Vulnerabilitățile nucleului din 2026 arată de ce izolarea containerelor multi-tenant nu este suficientă. Află despre Copy Fail, Dirty Frag, Fragnesia și CVE-2026-80521, apoi compară containerele consolidate cu frontiera oferită de microVM."
genre: ["Securitatea containerelor", "Linux", "Securitatea nucleului", "Virtualizare", "Securitate cloud", "Cercetarea amenințărilor", "Echipa blue", "DevSecOps"]
tags: ["Evadare din container", "Frontiera de securitate a containerelor", "CVE ale nucleului Linux", "Escaladarea locală a privilegiilor", "LPE 2026", "Copy Fail", "CVE-2026-31431", "Dirty Frag", "CVE-2026-43284", "CVE-2026-43500", "Fragnesia", "CVE-2026-46300", "CVE-2026-80521", "kernelCTF", "kvmCTF", "microVM", "Firecracker", "Kata Containers", "Coruperea cache-ului de pagini", "AF_ALG", "AF_UNIX", "XFRM ESP", "RxRPC", "Izolarea spațiilor de nume", "Apel de sistem clone", "Detectarea vulnerabilităților cu AI", "Securitatea Docker", "Securitatea Kubernetes", "Izolare multi-tenant", "Evadare din sandbox", "nsjail", "Bubblewrap", "Firejail", "Dirty Pipe", "Tendința CVE ale nucleului"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "Ilustrație digitală cu mai multe containere luminoase conectate la un simbol central al nucleului. Elemente colorate reprezintă vulnerabilități care se răspândesc din nucleu pe un fundal întunecat."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---

**Containerele folosesc același nucleu. În 2026, patru familii distincte de vulnerabilități au demonstrat că o singură eroare a nucleului este suficientă pentru a ieși din container și a ajunge pe gazdă.** Copy Fail, Dirty Frag, Fragnesia și CVE-2026-80521 acordă fiecare privilegii root unui utilizator local fără privilegii. Toate încalcă frontiera containerului.

*Partea îngrijorătoare nu sunt erorile în sine, ci cât de ieftin le găsește acum AI-ul și cum un patch a creat o altă eroare.*

Acest articol explică modul în care containerele izolează sarcinile, de ce izolarea se bazează acum pe o fundație tot mai îngustă, ce face fiecare vulnerabilitate din 2026 și în ce tehnologie de izolare merită să ai încredere în locul containerelor.

**Ce vei obține:** notează cine furnizează codul fiecărei sarcini, identifică funcțiile nucleului de care are nevoie și alege între containere consolidate și o frontieră microVM. Tratează studiile de caz din 2026 ca dovezi de cercetare datate. Verifică recomandările actuale ale furnizorilor înainte de a modifica un nucleu de producție.

## Răspunsul pe scurt

| Întrebare | Răspunsul pe scurt |
|---|---|
| **Containerele izolează?** | Da, procesele și sistemul de fișiere. Toate folosesc același nucleu, așadar erorile nucleului sunt un risc comun |
| **De ce acum?** | Căutarea asistată de AI a redus costul găsirii erorilor din nucleu. Până în septembrie 2026 au fost publicate aproape **6.000 de CVE ale nucleului** |
| **Ce încalcă frontiera?** | Orice escaladare locală de privilegii în nucleu. Nu este necesară o configurare greșită a containerului pentru a evada |
| **Este suficient patching-ul?** | Este necesar, dar ritmul nu mai ține pasul. Un patch din 2026 **a introdus o vulnerabilitate nouă, exploatabilă** |
| **Ce funcționează mai bine?** | MicroVM-uri precum Firecracker sau Kata Containers, care oferă fiecărei sarcini propriul nucleu |
| **Alternativa este perfectă?** | Nu. Și hypervisorul este cod. Suprafața de atac este mult mai mică, iar aceasta este diferența esențială |

## Cum izolează containerele

Pentru a înțelege frontiera, trebuie mai întâi să știi ce nu este un container.

**Un container nu este o mașină virtuală.** Nu există un al doilea nucleu, hardware emulat sau hypervisor între procesul tău și hardware. Când rulezi o imagine de container, rulezi un proces pe nucleul existent, cu o vedere modificată asupra sistemului.

Mecanismul este **apelul de sistem `clone`**. `fork` copiază spațiul de adrese al unui proces, iar `clone` creează un proces copil și oferă control precis asupra părților contextului de execuție care sunt partajate sau înlocuite. Docker îi transmite lui `clone` un set de **spații de nume**:

| Spațiu de nume | Ce simulează |
|---|---|
| **Mount** | O rădăcină privată a sistemului de fișiere, astfel încât containerul să-și vadă arborele, nu pe al tău |
| **PID** | Numerotare proprie a proceselor, astfel încât `PID 1` să fie primul proces al containerului, nu `systemd` |
| **User** | O mapare a identității prin care „root” în container corespunde unui utilizator fără privilegii de pe gazdă |
| **Network** | Interfețe, tabele de rutare și porturi private |
| **IPC** | Memorie partajată și cozi de mesaje izolate |
| **UTS** | Nume de gazdă și domeniu proprii |
| **Cgroup** | O vedere privată asupra limitelor de resurse |

Adaugă un sistem de fișiere **union** peste o imagine, iar rezultatul *pare* un calculator separat. `id` afișează `uid=0(root)` în container. Sistemul de fișiere seamănă cu o instalare Ubuntu minimală. Lista de procese arată doar procesele proprii.

**La nivelul apelurilor de sistem, aceasta nu este o frontieră de securitate.** Când un proces din container deschide un fișier, alocă memorie sau folosește un socket de rețea, același nucleu îi gestionează cererea ca pentru orice alt container de pe gazdă. Spațiile de nume schimbă *ce vede procesul*, nu *ce va face nucleul pentru el*.

*Nucleul este frontiera reală dintre container și gazdă. Restul este prezentare.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Diagramă cu trei containere construite pe același nucleu. Spațiile de nume mount, PID, user și network le separă vizualizările, dar toate apelurile de sistem ajung la același nucleu partajat" >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## Frontiera este cod, iar codul are erori

Fiecare acțiune a unui container trece prin **interfața apelurilor de sistem**. Deschiderea unui fișier, citirea memoriei, scrierea într-un socket, modificarea unui UID: nucleul le intermediază pe toate, deoarece nu vrea ca procesele să atingă direct CPU-ul, sistemul de fișiere sau rețeaua.

Medierea este modelul de securitate și este implementată ca software. Mai exact, are aproximativ **30 de milioane de linii** de cod.

O escaladare locală de privilegii (LPE) apare când un proces exploatează o eroare din codul de mediere pentru a obține privilegii care nu i-au fost acordate. **LPE-urile nu sunt noi.** Există de la primele mecanisme de mediere ale nucleului, iar industria a conviețuit cu un flux constant de astfel de erori timp de decenii.

**Dirty Pipe din 2022** este exemplul de referință pe care îl știe majoritatea. A profitat de o eroare în gestionarea bufferelor pipe pentru a suprascrie fișiere doar cu acces de citire. A făcut senzație deoarece erorile de această gravitate apăreau **aproximativ o dată la unu sau doi ani**. Se instala patch-ul, se continua activitatea și rămânea valabilă presupunerea că nu exista un defect major nedescoperit în codul citit de un milion de oameni.

*Această presupunere nu mai este valabilă.*

## Ce s-a schimbat în 2026

Schimbarea nu ține de priceperea atacatorilor. Ține de faptul că **găsirea erorilor de corupere a memoriei nucleului a devenit o sarcină inginerească, nu o carieră de cercetare**.

Trei date din acest an arată concret schimbarea:

| Descoperire | Cine a găsit-o | Cum |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Cu ajutorul **Xint Code**, un instrument AI de analiză statică. Aproximativ **o oră de scanare** a subsistemului criptografic Linux |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Găsită cu **dfs-large1**, un model AI intern antrenat pentru detectarea vulnerabilităților |
| **CVE-2026-80521**, găsită independent | Kyle, **OpenAI** | Aceeași eroare, descoperită separat și raportată în aceeași zi |

Citește din nou al treilea rând. Două organizații care foloseau instrumente AI diferite au găsit **același use-after-free în AF_UNIX** și l-au raportat la `security@kernel.org` în **aceeași zi**. Nu este o coincidență de talent. Este un proces repetabil care a dat același răspuns de două ori.

DepthFirst afirmă direct amploarea: **aproape 6.000 de CVE ale nucleului au fost publicate până în septembrie 2026**. Numărul crește odată cu disponibilitatea asistenței AI, nu cu numărul dezvoltatorilor nucleului.

*Când o oră de scanare AI găsește o eroare veche de un deceniu în subsistemul criptografic, economia exploatării nucleului se inversează.*

## Patru evadări într-un an

Fiecare dintre aceste vulnerabilități oferă root unui cont local fără privilegii. Niciuna nu necesită o configurare greșită a containerului, un indicator privilegiat sau un punct de sprijin prin rețea.

| Vulnerabilitate | CVE | Subsistem | Primitivă | Descoperită de |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | Scriere de 4 octeți în cache-ul de pagini al oricărui fișier care poate fi citit | Theori, cu ajutor AI |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | Scriere de 4 octeți în cache-ul de pagini prin două variante înlănțuite | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP | Scrieri de un singur octet în cache-ul de pagini | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | Socketuri AF_UNIX | Use-after-free în colectarea gunoiului pentru `unix_vertex` | DepthFirst, cu ajutor AI |

Toate patru au un tipar de proiectare demn de remarcat: **atacă cache-ul de pagini, nu discul.**

### Copy Fail: defect logic fără cursă

Copy Fail este cea mai simplă dintre cele patru și cea mai alarmantă.

Aproape toate LPE-urile Linux au nevoie de o fereastră de timp sau de o deplasare de memorie specifică nucleului. **Copy Fail nu are nevoie de niciuna.** Este un defect logic direct în `algif_aead`, modulul care oferă spațiului de utilizator acces la criptarea autentificată prin AF_ALG.

Lanțul de exploatare folosește `splice()` pentru a introduce o pagină din cache-ul de pagini în operație, apoi abuzează de calea AEAD în loc pentru a scrie **patru octeți controlați** în acea pagină. Pagina coruptă **nu este marcată niciodată ca dirty**, deci nu este scrisă înapoi pe disc. Fișierul de pe disc rămâne intact, așa că verificările checksum și de integritate trec, deși copia din memorie conține modificarea.

Un **script Python de 732 de octeți** obține root pe toate distribuțiile Linux lansate din 2017. Eroarea a fost introdusă de o **optimizare din 2017** în `algif_aead`, iar patch-ul din 2026 doar inversează optimizarea. Commit mainline `a664bf3d603d`.

*Eroarea a fost prezentă în toate distribuțiile importante aproape un deceniu, iar un instrument AI a găsit-o în aproximativ o oră.*

### Dirty Frag: două variante care se completează reciproc

Numele Dirty Frag îi descrie corect originea: **Dirty Pipe suprascrie `struct pipe_buffer`. Dirty Frag suprascrie câmpul `frag` din `struct sk_buff`.**

Sunt **două vulnerabilități înlănțuite**, iar înlănțuirea este partea ingenioasă:

- **CVE-2026-43284** profită de faptul că `esp_input()` sare peste calea copy-on-write înainte de a decripta în loc un fragment introdus prin splice. Necesită privilegiul de a crea un **user namespace**, restricționat în unele distribuții.
- **CVE-2026-43500** profită de `rxkad_verify_packet_1()` care decriptează fragmentul în loc. Nu are nevoie de privilegiul de namespace, dar modulul `rxrpc` lipsește din majoritatea distribuțiilor. Ubuntu îl încarcă implicit.

**Fiecare variantă are un punct orb dacă este folosită singură. Împreună se completează reciproc.** Dacă user namespaces sunt permise, calea ESP se execută prima. Dacă sunt blocate, dar `rxrpc` este prezent, se execută calea RxRPC. Un singur binar de exploatare funcționează astfel pe mai multe distribuții, iar varianta RxRPC obține root golind un câmp din `/etc/passwd` și lăsând PAM să accepte o parolă goală prin `nullok`.

**Descoperirea cea mai importantă pentru apărători:** Dirty Frag se declanșează **indiferent dacă `algif_aead` este disponibil**. Măsura Copy Fail, promovată pe scară largă, care blochează modulul, **nu protejează deloc împotriva Dirty Frag**.

### Fragnesia: patch-ul care a creat o eroare

Fragnesia aparține aceleiași clase ca Dirty Frag, dar vizează calea **ESP-in-TCP** din XFRM. Este cazul cel mai instructiv din grup.

Vulnerabilitatea exploatează gestionarea incorectă a fragmentelor de pagină partajate în timpul coalescenței `skb`. Atacatorul introduce pagini asociate unor fișiere în coada de recepție TCP înainte ca socketul să intre în modul de protocol de nivel superior `espintcp`. După activarea procesării ESP, nucleul decriptează datele din coadă **în loc**, iar manipularea fluxului de chei AES-GCM corupe cache-ul de pagini subiacent. Atacatorul obține **scrieri repetate de câte un octet** în paginile fișierelor din cache.

Exploatarea obține root suprascriind primii octeți din `/usr/bin/su` cu o încărcătură ELF mică. **Modificarea există doar în memorie și nu atinge binarul de pe disc.**

**User și network namespaces** fără privilegii oferă `CAP_NET_ADMIN` într-un spațiu izolat. Apoi NETLINK_XFRM instalează o asociere de securitate pregătită.

*Merită să te oprești asupra acestei propoziții:* Fragnesia a apărut ca **efect secundar neintenționat al unuia dintre patch-urile vulnerabilităților Dirty Frag originale**. Patch-ul Dirty Frag a produs o nouă eroare independent exploatabilă pentru root.

### CVE-2026-80521: evadarea din container care a câștigat kernelCTF

Cursa AF_UNIX încheie orice argument că acest scenariu este teoretic.

Vulnerabilitatea este un **use-after-free pe heap** în mecanismul de colectare a gunoiului pentru mesajele `SCM_RIGHTS`, prin care procesele își transmit descriptorii de fișiere. O cursă în timpul colectării unei referințe circulare de socket eliberează un `struct unix_vertex`, deși inelul SCC al unui socket rămas păstrează încă un pointer către acesta. Următoarea colectare parcurge inelul învechit și dereferențiază memoria eliberată.

Importanța sa depășește Linux, deoarece **AF_UNIX stă la baza IPC locale**. Bazele de date locale, `systemd` și chiar Docker depind de el. DepthFirst spune că vulnerabilitatea afectează majoritatea sandbox-urilor OS bazate pe nucleu, **inclusiv `nsjail`, `Firejail` și `Bubblewrap`**, precum și runtime-urile moderne de containere.

DepthFirst a câștigat un **loc în Google kernelCTF** cu această vulnerabilitate pe **24 iulie 2026**, a primit confirmarea în slotul `lts-6.12.95` pe **5 august**, a raportat-o la `security@kernel.org` în aceeași zi, apoi a aflat că **Kyle de la OpenAI raportase aceeași eroare**. Patch-ul upstream a intrat pe **6 august**. Cercetarea a fost publicată pe **22 septembrie**.

Au publicat o exploatare funcțională pentru **Ubuntu 26.04** și o a doua exploatare pentru CVE-2026-52910, care evadează din **Ubuntu 24.04**.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Diagramă cu un proces fără privilegii dintr-un container care corupe o pagină din cache pentru a modifica în memorie un binar setuid, obține root și trece dincolo de frontiera containerului până la nucleul gazdei" >}}

## De ce continuă să eșueze recomandările de atenuare

Apărătorii au primit trei runde de soluții alternative în acest an, iar fiecare a fost parțial greșită.

| Atenuare | Ce oprește | Ce omite |
|---|---|---|
| Blocarea **`algif_aead`** | Copy Fail | **Nimic din Dirty Frag**, care ignoră complet modulul |
| Blocarea **`esp4`, `esp6`, `rxrpc`** | Dirty Frag, Fragnesia | Echipele care au nevoie de IPsec. Omite și subsisteme complet noi |
| Restricționarea **user namespaces fără privilegii** | Variantele ESP | Varianta RxRPC nu are nevoie de namespace. Politica AppArmor este doar o atenuare **parțială** |
| **Aplicarea patch-ului la nucleu** | Eroarea corectată | Următoarea eroare și orice eroare introdusă de patch |

Ies în evidență două tipare.

**În primul rând, soluțiile alternative se contrazic.** Copy Fail este atenuată prin dezactivarea `algif_aead`. Dirty Frag este declanșată **indiferent dacă** modulul există. Fragnesia necesită dezactivarea `esp4` și `esp6`, ceea ce este o problemă pentru cei care folosesc IPsec. Nu există o singură listă de blocare a modulelor care să acopere întreaga familie.

**În al doilea rând, și mai rău, aplicarea unui patch nu este o victorie lipsită de riscuri.** Fragnesia a fost introdusă **prin patch-ul Dirty Frag**. Orice patch poate crea noi erori logice, iar în acest subsistem o eroare logică devine o exploatare care obține root.

*Concluzia incomodă: toate aceste vulnerabilități sunt în cache-ul de pagini, pot fi accesate din cod fără privilegii și au fost găsite de instrumente care se îmbunătățesc în fiecare trimestru. Nicio listă de blocare nu rămâne completă.*

## Răspunsul onest la contraargument

Există o obiecție corectă care merită un răspuns direct: **hypervisor-ele au și ele erori.**

Suprafața de atac KVM este reală. Google desfășoară **kvmCTF** tocmai pentru a descoperi aceste erori și oferă recompense generoase:

| Nivel | Recompensă |
|---|---|
| **Evadare completă din VM** | **$250,000** |
| Scriere arbitrară în memorie | $100,000 |
| Citire arbitrară din memorie | $50,000 |
| Scriere relativă în memorie | $50,000 |
| Refuzul serviciului | $20,000 |
| Citire relativă din memorie | $10,000 |

Recompensele nu se cumulează. Ținta este un nucleu Linux LTS cu KVM, iar invitatul este Debian 12.5. Obiectivul este un **atac de la invitat la gazdă**.

**Hyunwoo Kim, același cercetător care a găsit Dirty Frag, câștigă și recompense KVM** și a primit suma întreagă de $250,000 pentru o evadare din VM. Așadar, rezumatul onest este că ambele straturi au defecte și, uneori, aceeași persoană le găsește.

**Dar compară scara:**

| | Nucleul Linux | Hypervisor KVM |
|---|---|---|
| **CVE în 2026** | Aproape **6.000** | Câteva, cercetătorii individuali găsind câteva pe an |
| **Accesibil din** | Orice proces fără privilegii, prin interfața syscall | Doar codul care rulează deja într-un invitat |
| **Suprafața de atac** | Totul: rețelistică, sisteme de fișiere, criptografie, IPC, drivere | Dispozitivul virtual și interfața hypercall |
| **Clasa erorii** | Orice defect de siguranță a memoriei sau logic în 30 de milioane de linii | Limitată la frontiera de virtualizare |

*Diferența este de mai multe ordine de mărime, nu de două ori. Acesta este motivul pentru care microVM-urile schimbă calculul riscului.*

## Ce oferă o frontieră reală

O **microVM** îi oferă fiecărei sarcini **propria instanță de nucleu**, care rulează peste virtualizare impusă de hardware, în loc să partajeze nucleul gazdei prin spații de nume.

Stiva are trei straturi care merită numite:

- **CPU-ul** oferă mecanisme hardware pentru a izola o regiune de memorie de alta.
- **KVM** pune aceste mecanisme la dispoziția nucleului Linux, astfel încât nucleul acționează ca hypervisor.
- Un **VMM (monitor de mașină virtuală)**, precum Firecracker sau QEMU, controlează KVM pentru a crea și rula invitatul.

Deoarece invitatul rulează propriul nucleu, o exploatare a nucleului **în interiorul invitatului** compromite doar invitatul. Nu există un nucleu comun de atacat. Apoi, atacatorul trebuie să evadeze din hypervisor însuși, suprafața mai mică ocupată de erorile KVM.

Două implementări contează în practică și ambele sunt menționate în recomandarea DepthFirst:

| Tehnologie | Abordare | Note |
|---|---|---|
| **Firecracker** | VMM cu scop special, model minimal de dispozitive | Creat de AWS, conceput special pentru izolarea multi-tenant la scară |
| **Kata Containers** | Runtime compatibil OCI care încapsulează o microVM | Rulează imagini standard de container cu o frontieră VM dedesubt |

Pentru majoritatea echipelor, Kata este migrarea mai ușoară, deoarece acceptă imaginile și instrumentele de container deja folosite. **Firecracker are o suprafață de atac mai mică**, fiindcă implementează mult mai puțină emulare de dispozitive decât un VMM de uz general.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Diagramă care compară izolarea containerelor prin spații de nume cu nucleu partajat cu izolarea microVM, în care fiecare sarcină rulează propriul nucleu peste KVM și un monitor de mașină virtuală" >}}

## Ce poți face acum

Nu orice container are nevoie de o microVM. Decizia depinde de **cine rulează cod în el**.

| Situația ta | Risc | Ce să faci |
|---|---|---|
| **Rulezi propriul cod**, un singur chiriaș | Scăzut | Păstrează containerele. Aplică patch-uri rapid, elimină capabilitățile și păstrează sistemul de fișiere root doar pentru citire |
| **Gazde multi-tenant**, acces shell pentru utilizatori | **Ridicat** | Mută sarcinile nefiabile în microVM-uri. Acesta este primul caz evidențiat de DepthFirst |
| **Runner-e CI care execută PR-uri nefiabile** | **Ridicat** | Un pull request devine root pe runner. Izolează fiecare sarcină în propria VM |
| **Notebook-uri, sandbox-uri de agenți, serverless** | **Ridicat** | Codul chiriașului devine root pe gazdă. O microVM pentru fiecare chiriaș |
| **Clustere Kubernetes** | **Sporit** | Cache-ul de pagini este partajat pe gazdă. Un pod cu primitivele potrivite compromite nodul și trece granițele dintre chiriași |

Principiul comun este simplu. **Containerele sunt excelente pentru împachetare și izolarea proceselor.** Nu au fost proiectate să țină cod ostil în interior, dar industria le-a folosit discret în acest scop deoarece erau convenabile și ieftine.

### Consolidări utile indiferent de situație

Nimic de aici nu înlocuiește o frontieră VM, dar elimină căi ușoare:

```bash
# Disable the modules the page-cache family abuses, where they are not needed
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Restrict unprivileged user namespaces, which gates the ESP variants
# Debian and Ubuntu: this is a partial mitigation, not a complete one
sysctl -w kernel.unprivileged_userns_clone=0

# If exploitation is suspected, drop the page cache to discard modified in-memory binaries
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Detection starting points
- Unexpected unshare(CLONE_NEWUSER) from a workload with no legitimate reason
- NETLINK_XFRM activity, or XFRM security associations appearing outside IPsec hosts
- Requests to bind AF_ALG sockets
- Loads of esp4, esp6, or rxrpc on hosts running neither IPsec nor AFS
```

> **Avertisment: `drop_caches` elimină copia modificată din memorie și curăță coruperea, dar nu înlătură un atacator care a obținut deja root. Trateaz-o ca răspuns la incident, nu ca remediere.**

### Problema ritmului de aplicare a patch-urilor

Chiar și cu cele mai bune intenții, aplicarea patch-urilor la nucleu a devenit o cursă:

- Aproape **6.000 de CVE** publicate în acest an depășesc, prin volum, majoritatea ferestrelor de mentenanță.
- **Un patch introduce o eroare.** Fragnesia a demonstrat-o în exact acest subsistem.
- **Lista de atenuări expiră.** `algif_aead` era răspunsul în aprilie. În mai nu mai acoperea nimic din Dirty Frag.

*Viteza patch-urilor este necesară, dar nu suficientă. Arhitectura decide dacă un patch omis produce un incident izolat sau compromiterea gazdei.*

## Întrebarea dificilă: cine este adversarul?

Răspunsul tehnic este clar. Răspunsul strategic depinde de o întrebare pe care multe echipe o omit.

**Dacă modelul tău de amenințare include un utilizator curios sau un dezvoltator neatent, containerele rămân adecvate.** Evadarea din container necesită execuție locală de cod și o exploatare a nucleului. Niciuna nu este trivială, iar costul operațional al mutării tuturor sarcinilor în microVM-uri este real.

**Dacă modelul tău de amenințare include un adversar care rulează cod pe infrastructura ta, containerele sunt acum doar un obstacol minor.** Merită citată, nu parafrazată, concluzia DepthFirst:

> „Pragul de intrare pentru transformarea acestor vulnerabilități în arme a scăzut atât de mult, încât trebuie să presupunem că atacatorii pot evada din containerele standard oricând doresc.”

Este un furnizor de securitate cu un produs de vândut, care argumentează pentru o anumită arhitectură. Scepticismul este justificat. **Argumentul nu depinde însă de furnizor.** Numărul de 6.000 de CVE este public, exploatările sunt publicate, iar nucleul este partajat prin proiectare.

*Formularea onestă: valoarea containerelor ca frontieră scade împotriva unui atacator cu acces inițial, dar rămâne aceeași împotriva tuturor celorlalți.*

## Verdictul

**Containerele rămân instrumentul potrivit pentru împachetare, implementare și separarea proceselor. Nu mai sunt o frontieră de securitate fiabilă împotriva codului ostil.**

Trei afirmații, în ordinea certitudinii:

1. **Premisa tehnică este stabilită.** Containerele partajează nucleul gazdei. Fiecare dintre cele patru vulnerabilități din articol a trecut de frontieră pornind de la un cont fără privilegii, iar exploatările sunt publice.

2. **AI-ul a schimbat ritmul, nu principiul.** LPE-urile nucleului au existat dintotdeauna. Acum găsirea uneia costă aproximativ **o oră de scanare AI**, în loc de luni de efort specializat, iar două organizații au găsit independent același zero-day în aceeași zi.

3. **Migrarea costă, dar și refuzul migrării.** Firecracker și Kata adaugă overhead, complexitate operațională și noi competențe. Alegerea este simplă: accepți costul sau accepți că o eroare a nucleului compromite gazda.

**Dacă operezi infrastructură multi-tenant sau rulezi cod nefiabil, începe acum planificarea migrării la microVM.** Nu pentru că urmează o catastrofă, ci pentru că tendința este clară, iar migrarea durează trimestre, nu săptămâni.

**Dacă rulezi containere single-tenant cu propriul cod, păstrează-le.** Aplică patch-uri nucleului mai repede decât înainte, dezactivează modulele inutile și reevaluează decizia când apare cod nefiabil.

*Epoca în care nucleul era tratat drept frontieră de încredere necondiționată se încheie. Infrastructura pregătită pentru compromiterea nucleului supraviețuiește incidentului.*

## Idei principale

- **Containerele partajează nucleul gazdei.** Izolarea vine din spațiile de nume ale apelului `clone`, nu din virtualizarea hardware, așa că o eroare a nucleului afectează și containerul.
- **Patru vulnerabilități din 2026 au depășit frontiera** pornind de la conturi locale fără privilegii: Copy Fail, Dirty Frag, Fragnesia și CVE-2026-80521. Toate țintesc cache-ul de pagini.
- **Până în septembrie 2026 au fost publicate aproape 6.000 de CVE ale nucleului**, iar instrumentele AI accelerează descoperirea. **Copy Fail a fost găsită în aproximativ o oră de scanare AI.**
- **Fragnesia a fost introdusă de patch-ul Dirty Frag.** Patch-ul a produs o nouă eroare care oferă root în același subsistem.
- **Soluția Copy Fail nu oprește Dirty Frag.** Blocarea `algif_aead` acoperă o vulnerabilitate și nimic altceva din familie.
- **CVE-2026-80521 a compromis și `nsjail`, `Firejail` și `Bubblewrap`**, nu doar runtime-urile de container.
- **MicroVM-urile schimbă calculul riscului** oferind fiecărei sarcini propriul nucleu. KVM are erori, dar suprafața este mult mai mică.
- **Alege în funcție de cine rulează codul.** Codul propriu într-un container single-tenant înseamnă risc redus. Codul nefiabil pe o gazdă partajată înseamnă risc de compromitere a gazdei.

## Pașii următori

1. **Citește analiza problemei și exploatarea publicată:** **[Containerele nu mai sunt o frontieră de securitate - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Consultă avizul oficial și recomandările de atenuare Copy Fail:** **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Citește analiza tehnică Dirty Frag** pentru a înțelege înlănțuirea și eșecul atenuării prin `algif_aead`: **[Analiza tehnică Dirty Frag](https://github.com/V4bel/dirtyfrag)**
4. **Vezi regulile și recompensele kvmCTF** pentru a înțelege suprafața de atac a hypervisorului: **[Prezentare kvmCTF](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Evaluează aceste CVE în mediul tău** cu instrumentul nostru în browser: **[Calculator CVSS v3.1](/cvss-calculator/)**
6. **Consolidează ce rulezi acum:** **[Cum să securizezi mediul Docker și Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Înțelege în detaliu compromisurile de izolare:** **[Docker vs. mașini virtuale 2026](/articles/docker-vs-vms/)**
8. **Redu privilegiile acolo unde nu poți adăuga o frontieră:** **[Controlul accesului cu privilegii minime în Linux](/articles/mastering-least-privilege-access-control-linux/)**

## Articole conexe

| Articol | Ce acoperă |
|---|---|
| **[Docker vs. mașini virtuale 2026](/articles/docker-vs-vms/)** | Comparația arhitecturală de bază, inclusiv compromisurile de performanță și securitate |
| **[Cum să securizezi mediul Docker și Kubernetes](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Consolidare practică pentru stratul containerelor, utilă și în interiorul unei microVM |
| **[Docker în LXC pe Proxmox: fiabilitate, dovezi și migrare la VM](/articles/docker-in-lxc-proxmox-reliability/)** | Containere imbricate, dovezi și momentul mutării unei sarcini într-o VM completă |
| **[Înțelegerea virtualizării: concepte și aplicații](/articles/understanding-virtualization_-concepts-and-applications/)** | Noțiunile de bază ale hypervisorului, inclusiv funcțiile CPU necesare microVM-urilor |
| **[Controlul accesului cu privilegii minime în Linux](/articles/mastering-least-privilege-access-control-linux/)** | Reducerea privilegiilor obținute în urma evadării pentru a limita impactul |

## Referințe

1. [Containerele nu mai sunt o frontieră de securitate - DepthFirst (Zhenpeng Lin, 22 septembrie 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Site-ul oficial de divulgare Copy Fail și analiza exploatării](https://copy.fail/)
4. [Analiza tehnică Dirty Frag - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia: escaladare locală de privilegii în nucleul Linux prin ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [Prezentare și niveluri de recompensă kvmCTF - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [Înregistrarea NVD pentru CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Commit-ul upstream mainline care repară Copy Fail](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Avizul de securitate Ubuntu privind remedierile Copy Fail](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [Exploatări și trimiteri KernelCTF - Google Security Research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)

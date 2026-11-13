---
title: "Open WebUI v0.12.4: listă de verificare pentru actualizare și controlul accesului 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Fă backup și actualizează Open WebUI la v0.12.4, apoi testează partajarea chat-urilor, permisiunile de export, accesul la resurse, conturile și accesul la rețea."
genre: ["IA găzduită local", "Securitate cibernetică", "Administrarea sistemelor"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "actualizare Open WebUI", "securitate Open WebUI", "control acces Open WebUI", "IA găzduită local", "actualizare Docker", "actualizare pip", "backup Open WebUI", "permisiuni Open WebUI", "roluri Open WebUI", "grupuri Open WebUI", "permisiune export chat", "chat-uri partajate", "chat-uri arhivate", "acces la baza de cunoștințe", "acces la modele", "permisiuni instrumente", "securitatea cheilor API", "securitatea contului de administrator", "dezactivare înscrieri", "autentificare proxy invers", "acces VPN", "fixarea imaginii de container"]
---

**Open WebUI v0.12.4 conține remedieri de securitate pe care administratorii proiectului nu le-au detaliat încă.** Notele versiunii recomandă actualizarea promptă a instalărilor și spun că vor urma anunțuri după atribuirea CVE-urilor. Modificările numite mai jos pentru partajarea chat-urilor și permisiuni sunt elementele vizibile în notele de lansare, nu o listă completă a remedierilor de securitate încă nedivulgate. [Note de lansare Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## Idei principale

- **Fă mai întâi backup.** Păstrează o copie recuperabilă a volumului de date sau a bazei de date și a fișierelor încărcate înainte să modifici aplicația.
- **Fixează versiunea oficială.** Folosește `ghcr.io/open-webui/open-webui:v0.12.4` pentru imaginea Docker standard sau `open-webui==0.12.4` pentru pip.
- **Testează permisiunile cu roluri reale de utilizator.** Un buton ascuns nu dovedește o verificare de autorizare la nivelul API-ului.
- **Păstrează accesul privat.** Cere autentificarea aplicației și limitează accesul la rețea prin VPN sau proxy invers autentificat.

## Înainte de actualizare

**Cerințe preliminare:** identifică metoda de instalare curentă, varianta imaginii containerului, locația datelor persistente, baza de date externă, proxy-ul invers și furnizorul de autentificare. Programează o perioadă de indisponibilitate și păstrează configurația curentă a containerului sau definiția serviciului. Rezervă timp pentru a repeta restaurarea pe o instanță separată. Comenzile de mai jos sunt modele documentate de furnizor și adaptate acestei versiuni fixate. Ele nu provin dintr-o actualizare reală efectuată pentru acest ghid. [Actualizarea Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **Inventariază stocarea.** În configurarea Docker standard, `open-webui` montează `/app/backend/data`. Notează montările bind, baza de date externă, stocarea de obiecte și variabilele de mediu personalizate. Pentru pip, găsește directorul de date activ al aplicației și baza de date înainte să schimbi mediul. Nu presupune că un export de chat este un backup complet.
2. **Fă backup după oprirea scrierilor.** Oprește aplicația sau folosește un snapshot coerent al bazei de date, apoi copiază volumul, orice bază externă și fișierele încărcate într-o stocare separată. Furnizorul documentează o arhivă a volumului Docker. Adaptează numele volumului și calea backup-ului la instalarea ta. Confirmă că arhiva se deschide și repetă restaurarea pe o altă instanță înainte să te bazezi pe ea. [Backup și restaurare](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **Citește notele versiunii și indicațiile de migrare.** Notele v0.12.4 nu enumeră remedierile de securitate în așteptare și nu indică intervalul versiunilor afectate. Nu atribui un CVE acestor remedieri și nu presupune că fiecare versiune anterioară v0.12.4 este afectată de o anumită vulnerabilitate. Ghidul de actualizare avertizează despre migrări unidirecționale ale bazei de date și replici cu versiuni diferite. Dacă mai mulți workeri sau replici folosesc aceeași bază de date, oprește-i simultan și urmează [procedura de migrare pentru mai multe replici](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations). Revenirea la versiunea veche poate necesita backup-ul bazei de date de dinaintea actualizării.

## Actualizează pachetul instalat

**Docker, procedura furnizorului adaptată la o etichetă fixată:** după backup, descarcă imaginea standard oficială și recreează containerul cu același volum persistent, aceeași configurație și același `WEBUI_SECRET_KEY`. Exemplul presupune volumul numit implicit și un proxy upstream legat local. Nu copia cheia reală în istoricul shell-ului. Furnizeaz-o prin mecanismul existent de mediu protejat sau de gestionare a secretelor. Păstrează opțiunile GPU, Ollama, rețea personalizată, bază de date și celelalte opțiuni din instalarea actuală. [Actualizarea Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Etichete oficiale pentru imagini](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**Verifică `./open-webui.env` înainte de rulare:** fișierul trebuie să existe deja, să aibă permisiuni restrictive și să conțină `WEBUI_SECRET_KEY` existent și configurația necesară. Legarea loopback este potrivită pentru un proxy pe același host, nu pentru unul de pe altă mașină. Cu Compose, schimbă numai imaginea serviciului la eticheta fixată, apoi rulează `docker compose pull open-webui` și `docker compose up -d open-webui` în proiectul existent. Păstrează același volum și aceeași configurație de mediu. Acestea sunt comenzi sugerate, nu o migrare testată a instalării tale.

**pip, procedura furnizorului pentru o versiune fixă:** în mediul virtual existent, oprește serviciul, instalează versiunea exactă a pachetului și repornește-l cu același director de date și mediu. Evită un al doilea mediu Python sau o bază de date nouă și goală. Instrucțiunea generică a furnizorului folosește `pip install -U open-webui`. Constrângerea de versiune de mai jos fixează această listă la v0.12.4. [Actualizarea Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [Pornire rapidă](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**Verifică serviciul pornit, nu doar artefactul instalat.** Consultă versiunea la pornire în `docker logs open-webui` sau în jurnalele serviciului pip și compar-o cu versiunea afișată de aplicație după autentificare. Ghidul de actualizare al furnizorului recomandă să verifici jurnalele containerului și să încarci pagina de autentificare. Dacă interfața arată resurse învechite, forțează reîmprospătarea browserului. Dacă pornirea raportează o eroare de migrare, ține serviciul oprit până identifici cauza. Nu instala un binar mai vechi peste o bază de date migrată fără să verifici cerințele de restaurare. [Verificări după actualizare](https://docs.openwebui.com/getting-started/updating/)

## Verifică accesul după repornire

**Comportamentul descris de furnizor:** v0.12.4 ascunde Export folder, Export chat-uri arhivate și Copiere chat pentru utilizatorii fără **Allow Chat Export**. Ascunde și controalele de acces pentru modele, prompturi, instrumente, cunoștințe, competențe, notițe și foldere pentru utilizatorii fără permisiunea de partajare corespunzătoare. Cei care vizualizează un folder partajat nu mai primesc actualizări live ale chat-ului după ce proprietarul arhivează conversația. Cei care vizualizează un link partajat nu mai primesc actualizări live după ce proprietarul anulează partajarea tuturor chat-urilor. Controalele ascunse reprezintă comportamentul interfeței, nu dovada unei remedieri pe server pentru o vulnerabilitate nespecificată. [Note de lansare](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**Verificare recomandată pentru operator:** cu un cont de test fără permisiuni de export și partajare, verifică absența acțiunilor menționate. Cu un cont autorizat, confirmă că acțiunile dorite funcționează în continuare. Creează un chat de test fără informații sensibile într-un folder partajat, deschide-l din alt cont, arhivează-l ca proprietar și confirmă că actualizările noi nu mai ajung la celălalt utilizator. Repetă cu un link partajat și **Unshare All Chats**. Verifică din nou permisiunile salvate și linkurile vechi. Nu presupune că materialele arhivate sau copiile istorice au fost șterse.

| Domeniu de verificare | Ce trebuie verificat |
|---|---|
| **Roluri și grupuri** | Elimină membrii și desemnările de administrator învechite. Verifică permisiunile efective ale unui utilizator aprobat recent și ale unuia restricționat. |
| **Modele și instrumente** | Analizează permisiunile pentru fiecare model, instrumentele atașate, drepturile de creare a instrumentelor și credențialele furnizorului. Testează cu un cont fără drepturi de administrator. |
| **Cunoștințe și fișiere** | Inspectează colaboratorii bazei de cunoștințe, permisiunile resurselor, atașamentele și setările de partajare. Verifică un cont căruia i s-a retras accesul. |
| **Chat-uri și exporturi** | Analizează folderele partajate, linkurile, chat-urile arhivate și atribuirile Allow Chat Export. Revocă linkurile inutile. |

Aceste verificări de inventar sunt **recomandări pentru operator**, nu garanții noi introduse de v0.12.4. [Ghidul de securizare](https://docs.openwebui.com/getting-started/advanced-topics/hardening/) al furnizorului descrie roluri pe niveluri, grupuri, permisiuni per resursă, permisiuni pentru spațiul de lucru, chei API și amplasarea în rețea.

## Închide lacunele de cont și de rețea

- **Înscrieri, setare a furnizorului:** dezactivează înscrierile deschise când un administrator sau furnizor de identitate creează conturile. Verifică `ENABLE_SIGNUP` și setările persistente de administrator cu [ghidul de securizare](https://docs.openwebui.com/getting-started/advanced-topics/hardening/). Păstrează reguli stricte de aprobare pentru conturile noi.
- **Chei API, verificare operațională:** inventariază cheile emise, șterge-le pe cele nefolosite și limitează crearea lor și accesul la endpoint-uri la rolurile și rutele necesare. Potrivit ghidului furnizorului, o cheie folosește permisiunile creatorului ei. Ține cheile în afara exemplelor și jurnalelor aplicației.
- **Administratori, verificare operațională:** elimină conturile de administrator abandonate, impune controale solide de autentificare, verifică disponibilitatea MFA și investighează schimbările neașteptate de cont. Testează metoda de recuperare a contului înainte să dezactivezi un administrator redundant.
- **Limita rețelei, recomandare a furnizorului:** plasează serviciul în spatele unui VPN, proxy de acces sau proxy invers cu autentificare și listă de IP-uri permise. Nu îl expune public fără autentificare. Evită `WEBUI_AUTH=False` pentru un serviciu accesibil. Un proxy invers fără autentificare proprie nu înlocuiește autentificarea aplicației. [Securizarea Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**Domeniu:** această listă se aplică versiunii oficiale Open WebUI și căilor standard de instalare documentate. Nu verifică fork-uri, imagini derivate sau pachete terțe. Notele v0.12.4 nu afirmă că există exploatare activă. Consultă [avizele de securitate ale proiectului](https://github.com/open-webui/open-webui/security/advisories) pentru dezvăluiri ulterioare și versiunile afectate și remediate aferente. Nu atribui v0.12.4 remedierea unui aviz anterior fără să-i citești intervalul de versiuni.

## Surse și referințe

- [Note de lansare Open WebUI v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Avize de securitate Open WebUI](https://github.com/open-webui/open-webui/security/advisories)
- [Actualizarea Open WebUI, inclusiv backup, revenire și migrări](https://docs.openwebui.com/getting-started/updating/)
- [Pornire rapidă Open WebUI și etichete oficiale pentru imagini](https://docs.openwebui.com/getting-started/quick-start/)
- [Securizarea Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [Actualizări și migrări pentru mai multe replici](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)

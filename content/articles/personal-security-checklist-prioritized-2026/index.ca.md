---
title: "Llista de seguretat personal 2026: per on començar i què ometre"
date: 2026-09-30
lastmod: 2026-11-15
toc: true
draft: false
description: "Prioritza les mesures de seguretat personal segons l'impacte en els atacs, des de la protecció dels comptes i les còpies de seguretat fins a la privadesa i la recuperació."
genre: ["Seguretat personal", "Privadesa", "Higiene digital", "Seguretat de comptes", "Modelatge d'amenaces", "Seguretat del consumidor", "Gestió de contrasenyes", "Protecció de dades"]
tags: ["llista de seguretat personal", "llista de seguretat digital", "llista de privadesa 2026", "ciberseguretat personal", "seguretat de comptes", "configuració de claus d'accés", "clau física de seguretat", "configuració del gestor de contrasenyes", "bones pràctiques 2FA", "resistència al phishing", "supervisió de filtracions", "avisos de filtracions", "congelació del crèdit", "privadesa d'àlies de correu", "compartimentació", "model d'amenaces", "xifrat complet del disc", "estratègia de còpies 3-2-1", "protecció del navegador", "bloqueig de rastrejadors", "DNS sobre HTTPS", "eliminació de metadades", "eliminació d'EXIF", "protecció contra el canvi de SIM", "recuperació de comptes", "codis de recuperació", "robatori de tokens de sessió", "programari maliciós infostealer", "prioritats de seguretat personal", "errors d'higiene de seguretat", "eines de privadesa", "eines de seguretat del costat del client"]
cover: "/img/cover/personal-security-checklist-2026-tiered-structure.webp"
coverAlt: "Il·lustració digital amb blocs de colors apilats sobre un fons fosc que representen mesures de seguretat personal. Cada bloc simbolitza una acció, com ara fer servir un gestor de contrasenyes o activar l'autenticació en dos factors."
coverCaption: ""
ref: ["/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security", "/articles/bitwarden-and-keepassxc-vs-the-rest", "/checklists/password-security-checklist"]
---

**Totes les guies de seguretat personal et donen el mateix: una llista llarga i plana de centenars de consells sense prioritat.** Et diuen que desactivis WebRTC, falsifiquis l'empremta de canvas i canviïs l'user-agent, al costat de configurar un gestor de contrasenyes i activar les actualitzacions automàtiques.

*Aquestes mesures no tenen el mateix valor. Tractar-les com si fossin iguals fa que molta gent faci el que és fàcil, es salti el que és important i continuï exposada.*

Aquest article conserva el tema i rebutja la falsa equivalència. Trobaràs els mateixos consells ordenats segons el risc que redueixen en relació amb l'esforç necessari, i una mirada honesta als hàbits que convé abandonar.

## Resposta breu

| Pregunta | Resposta breu |
|---|---|
| **Què atura més atacs?** | Un gestor de contrasenyes, segons factors resistents al phishing i actualitzacions puntuals. Aquests hàbits afronten vies habituals de vulneració de comptes, però no totes les amenaces. |
| **Quina és la millora més important avui?** | **Claus d'accés o una clau física de seguretat.** Totes dues resisteixen el phishing durant l'inici de sessió perquè la credencial no surt del dispositiu. Protegeix també els mètodes de recuperació i el dispositiu. |
| **Què està sobrevalorat?** | Contrasenyes complexes que memoritzes, canvis de contrasenya programats i la majoria dels ajustos de l'empremta del navegador. |
| **Què està infravalorat?** | Còpies de seguretat, configuració de recuperació dels comptes i seguretat física dels dispositius. |
| **Importa l'ordre?** | Sí, més que no pas la exhaustivitat. **Fer avui el nivell 1 és millor que acabar algun dia els 300 punts.** |
| **Quant triga el nivell 1?** | Unes dues hores, una sola vegada. |

## Per què l'ordre importa més que la exhaustivitat

Una llista completa sol reunir centenars d'elements i classificar-los com a **Essencial**, **Opcional** o **Avançat**. L'etiqueta serveix per filtrar, però no substitueix una classificació: tots els elements reben la mateixa categoria encara que redueixin quantitats de risc molt diferents.

**El meu argument: ni tan sols tres nivells donen prou precisió**, perquè «Essencial» agrupa mesures que redueixen el risc de manera molt desigual. Compara dos elements considerats essencials:

- **Activar 2FA** elimina tota una categoria de segrest de comptes.
- **Desactivar WebRTC** tanca una revelació local de la IP rellevant per a poca gent.

Tots dos poden aparèixer en una llista completa. Només un hauria d'entrar a la primera hora.

**El principi correcte d'ordenació és una proporció.** Classifica cada acció segons el risc que elimina dividit per l'esforç necessari, i avança de dalt a baix:

| Nivell | Propòsit | Esforç | Què bloqueja |
|---|---|---|---|
| **1. Aturar l'atac** | Tancar les vies que els atacants fan servir avui | ~2 hores | Robatori de credencials, phishing, programari maliciós, robatori de dispositius |
| **2. Contenir els danys** | Limitar l'impacte quan alguna cosa falla | ~1 hora | Punt únic de fallada, pèrdua del compte, frau d'identitat |
| **3. Reduir l'exposició** | Reduir la teva petjada de dades | Continu | Perfilatge, seguiment, enginyeria social dirigida |
| **4. Seguretat física i humana** | Cobrir la capa que el programari no arriba a protegir | ~30 minuts | Dispositius confiscats, mirades indiscretes, phishing per veu |

*Avança cap avall. No saltis al nivell 3 només perquè et sembli més interessant.*
{{< figure src="personal-security-tiers-ranked-by-impact.webp" alt="Diagrama de quatre nivells de mesures de seguretat personal, ordenades pel risc reduït i l'esforç necessari, des d'aturar atacs fins a mesures físiques i humanes" >}}

## Nivell 1: Aturar l'atac

Cinc punts, unes dues hores en total, per abordar les vies que fan servir els atacants.

### 1. Un gestor de contrasenyes i una contrasenya única a cada lloc

**L'emplenament automatitzat de credencials és el principal mètode de segrest de comptes**, i funciona perquè la gent reutilitza contrasenyes. Quan es filtra un lloc, els atacants proven aquestes credencials automàticament i a gran escala als altres.

Un gestor de contrasenyes resol la causa principal perquè fa difícil reutilitzar-ne una per accident. Genera una contrasenya diferent i d'alta entropia per a cada compte i l'emplena per tu.

Un detall important que molts consells ometen: **la contrasenya del gestor ara és l'únic punt de fallada**. Ha de ser llarga i memoritzada. És l'única contrasenya que mai no guardes en cap altre lloc. Una frase de cinc o sis paraules aleatòries és més segura que una cadena curta i complexa, i molt més fàcil de recordar.

Hi ha dues arquitectures vàlides:

| Enfocament | Avantatge | Compromís |
|---|---|---|
| **Sincronitzat al núvol** (Bitwarden i similars) | Còmode, sincronitza entre dispositius, recuperació fàcil | Confies en el xifratge i la disponibilitat del proveïdor |
| **Fitxer fora de línia** (KeePassXC i similars) | Control total, sense dependència del proveïdor | Tu gestiones les còpies i la sincronització |

*Tria qualsevol dels dos. La diferència entre fer servir un gestor i no fer-ne servir cap és molt més gran que la diferència entre aquests dos enfocaments.*

Consulta la comparació completa **[Millors gestors de contrasenyes 2026: Bitwarden contra KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** i la guia **[Com crear contrasenyes segures el 2026](/articles/how-to-create-strong-passwords/)**.

### 2. Segons factors resistents al phishing

Els segons factors no són intercanviables. La protecció que ofereixen varia molt:

| Mètode | Atura l'emplenament de credencials | Atura el phishing | Atura el robatori de tokens de sessió |
|---|---|---|---|
| **Codis SMS** | Sí | Parcialment, mitjançant canvi de SIM | No |
| **Codis d'aplicació autenticadora** | Sí | Parcialment, mitjançant retransmissió en temps real | No |
| **Aprovació push** | Sí | Feblement, mitjançant bombardeig de sol·licituds | No |
| **Claus d'accés o clau física** | Sí | **Sí** | Sí |

**Les claus d'accés i les claus físiques FIDO2 són les úniques opcions de la llista que vencen el phishing.** La raó és estructural: la credencial està vinculada a l'origen, de manera que un domini que s'hi assembla no obté res que pugui fer servir. No hi ha cap codi que la víctima pugui llegir a l'atacant.

Cal esmentar una amenaça relacionada que invalida els mètodes que molta gent creu segurs. **El programari maliciós infostealer ara recull directament les galetes del navegador**, cosa que permet que l'atacant reutilitzi una sessió autenticada sense necessitar mai la contrasenya ni el segon factor. Per això importa l'última columna, i també per això **el punt 3 del nivell 1 no és opcional**.

*Ordre de prioritat: claus d'accés quan s'ofereixin, clau física per al correu i les finances, aplicació autenticadora per a la resta i SMS només quan no hi hagi res millor.*

{{< figure src="phishing-resistant-second-factor-comparison.webp" alt="Diagrama que compara codis SMS, aplicacions autenticadores, aprovació push i claus d'accés davant l'emplenament de credencials, el phishing i el robatori de tokens de sessió. Les claus d'accés vencen els tres" >}}

Genera i verifica codis temporals localment amb el nostre **[Generador TOTP i HOTP](/totp-generator/)**, que llegeix un secret Base32 o un URI `otpauth://` i funciona del tot al navegador.

### 3. Actualitzacions automàtiques a tot arreu

**La majoria d'intrusions amb èxit exploten una vulnerabilitat per a la qual ja existeix un pedaç.** El retard de les actualitzacions és l'escletxa que aprofiten els atacants.

La solució pràctica no és tornar-se més diligent amb les actualitzacions. És eliminar la decisió activant les actualitzacions automàtiques a cada capa:

- **Sistema operatiu**: Windows Update, macOS Software Update o unattended-upgrades a Linux
- **Navegadors**: deixa activada l'actualització automàtica i reinicia quan t'ho demani, perquè un reinici pendent vol dir que el navegador continua sense el pedaç
- **Telèfon**: activa les actualitzacions automàtiques de les aplicacions, no només les del sistema
- **Encaminador**: és la capa que la gent oblida i es pot accedir des de l'exterior

**Un navegador que mostra l'avís de reinici executa codi vulnerable.** Aquest únic hàbit tanca més exposició que la majoria d'elements del nivell 3 junts.

*L'anàlisi d'escapada del nucli a **[Els contenidors ja no són una frontera de seguretat](/articles/containers-no-longer-security-boundary-2026/)** mostra com n'és de breu la finestra per aplicar el pedaç quan hi ha una escalada de privilegis.*

### 4. Xifratge del dispositiu i una pantalla de bloqueig segura

**El xifratge complet del disc transforma un dispositiu robat en una pèrdua de maquinari en lloc d'una filtració de dades.** Sense xifratge, qui tingui el portàtil o el telèfon pot llegir-ho tot, inclosa la bóveda del gestor de contrasenyes i els tokens de sessió actius.

Totes les plataformes principals ofereixen aquesta funció, però en algunes no està activada per defecte:

| Plataforma | Funció | Comprova |
|---|---|---|
| **Windows** | BitLocker o Device Encryption | Configuració, Privadesa i seguretat, Xifratge del dispositiu |
| **macOS** | FileVault | Configuració del sistema, Privadesa i seguretat, FileVault |
| **Linux** | LUKS | Confirma durant la instal·lació que els volums root i home estiguin xifrats |
| **iOS i Android** | Activat per defecte quan configures un codi | Configura un codi i confirma que el xifratge estigui actiu |

Juntament amb el xifratge, importen dues regles:

- **Fes servir una frase de contrasenya o un PIN llarg, no un codi de quatre xifres.** Els comptes de correu i finances mereixen el bloqueig més fort del telèfon, perquè el codi protegeix tota la resta del dispositiu.
- **Prefereix un PIN a la biometria si et preocupa la coerció legal.** La biometria és còmoda i fàcil de recordar, però en algunes jurisdiccions les empremtes o cares obtingudes per la força reben proteccions diferents de les que s'apliquen als coneixements obtinguts per la força.

### 5. Còpies de seguretat, provades una vegada

**El ransomware i les fallades de maquinari acaben amb el mateix resultat, i una còpia de seguretat és l'únic control que resisteix tots dos.** És l'element que la gent se salta més sovint i del qual després més se'n penedeix.

L'esquema estàndard és **3-2-1**: tres còpies, en dos tipus de suport, amb una fora de l'emplaçament. Per a una persona:

- **Una còpia local** per recuperar-se de pressa
- **Una còpia xifrada fora de l'emplaçament** contra el ransomware i els incendis
- **Una còpia fora de línia o una còpia amb permís d'escriptura** per si el ransomware arriba a l'emmagatzematge sincronitzat

*L'últim punt és el més important i el que menys s'implementa. L'emmagatzematge sincronitzat no és una còpia de seguretat. El ransomware i les supressions accidentals també se sincronitzen.*

**Prova una restauració almenys una vegada.** Una còpia de seguretat que no s'ha restaurat mai és una hipòtesi.

## Nivell 2: Contenir els danys

El nivell 1 suposa que res no falla. El nivell 2 suposa que alguna cosa fallarà i limita les conseqüències.

### 6. Deixa de reutilitzar la teva adreça de correu

**La teva adreça de correu és la clau que uneix totes les bases de dades que s'han filtrat mai.** Fer servir una adreça a tot arreu permet relacionar una filtració amb les altres i dona als enginyers socials un punt de partida verificat.

**Els àlies resolen tots dos problemes.** Genera una adreça única per servei, de manera que l'adreça mateixa es converteixi en una etiqueta:

| Avantatge | Per què importa |
|---|---|
| **Atribució de filtracions** | Si arriba correu brossa a un àlies, saps quin servei ha filtrat o venut la teva adreça |
| **Bloqueig immediat** | Desactiva un àlies sense tocar la bústia real |
| **Resistència a la correlació** | Les adreces diferents impedeixen agrupar els comptes en un sol perfil |
| **Detecció de phishing** | Els missatges a un àlies que ja no fas servir són clarament fraudulents |

**L'adreçament amb subetiquetes** (`you+service@example.com`) és una versió més feble. Permet saber qui ha filtrat l'adreça, però també revela la teva adreça real i no impedeix correlacionar els comptes.

*Si tens un domini, els àlies catch-all t'ho donen de franc. Si no, els proveïdors d'àlies especialitzats fan el mateix.*

### 7. La recuperació del compte és la superfície d'atac real

**Els atacants cada cop se salten més la porta principal i apunten a la recuperació.** Ha de funcionar després de perdre un dispositiu i no convertir-se en l'enllaç més feble.

Configura-ho en aquest ordre:

- **Desa els codis de recuperació fora de línia.** Imprimeix-los o desa'ls en un suport xifrat i mantén-los **separats del gestor de contrasenyes**, perquè la vulneració d'un no exposi l'altre.
- **Prefereix les claus de recuperació a les preguntes de seguretat.** Les respostes sobre el cognom de soltera de la teva mare o el primer cotxe sovint consten en registres públics.
- **Fes servir respostes falses si un lloc t'obliga a contestar preguntes.** Desa-les al gestor amb el compte.
- **Registra un segon dispositiu o clau** quan el servei ho permeti, perquè una fallada no et deixi fora.
- **Elimina contactes i números de recuperació antics**, perquè aquell número ara pertany a una altra persona.

> **Avís: perdre el segon factor sense codis de recuperació sovint vol dir perdre el compte per sempre, i el servei d'assistència no et retornarà l'accés a un compte protegit correctament.** Configura la recuperació alhora que actives el segon factor.

{{< figure src="three-two-one-backup-strategy-diagram.webp" alt="Diagrama del model de còpies 3-2-1: tres còpies de dades en dos suports, amb una còpia fora de línia protegida contra el ransomware i les supressions accidentals" >}}

### 8. Vigila les filtracions per assabentar-te'n aviat

**El valor d'un avís de filtració depèn del moment en què arriba.** Vols saber-ho mentre la contrasenya encara sigui vàlida en algun lloc.

- **Have I Been Pwned** envia avisos quan la teva adreça apareix en un conjunt de dades nou. També ofereix avisos per a tot el domini si és teu i fas servir àlies.
- **El teu gestor de contrasenyes dona un senyal millor**, perquè sap quines entrades de la bóveda corresponen al servei notificat i te les assenyala directament.

*El flux útil és breu: arriba l'avís, canvies la contrasenya del compte afectat i la canvies on hagis reutilitzat l'anterior. Aquest és l'avantatge del punt 1 del nivell 1: les contrasenyes úniques eliminen el segon pas.*

### 9. Congela el crèdit abans de necessitar-ho

**Congelar el crèdit és la defensa més sòlida disponible contra el frau d'identitat amb comptes nous**, i no costa res. Impedeix que els prestadors consultin l'expedient per obrir comptes al teu nom.

Als Estats Units, pots congelar-lo a cadascuna de les tres principals agències de crèdit. Pots descongelar-lo temporalment i tornar-lo a congelar després d'una sol·licitud legítima:

1. **Congela l'expedient a les tres agències**, no només a una. Cadascuna conserva un fitxer diferent.
2. **Desa els PIN per descongelar-lo** al gestor de contrasenyes.
3. **Descongela'l temporalment** quan sol·licitis crèdit i torna'l a congelar després.

*Fes-ho abans de necessitar-ho. Descobrir el procés enmig d'un frau, mentre disputes comptes, és el pitjor moment per aprendre'l.*

## Nivell 3: Reduir l'exposició

El nivell 3 redueix la petjada de dades. Importa, però va per sota dels elements anteriors perquè no bloqueja el segrest de comptes.

### 10. Reforça el navegador que fas servir

**El navegador és on s'exposa la major part de les dades personals**, i dos canvis cobreixen bona part del problema:

- **Instal·la un bloquejador de contingut.** Els anuncis i rastrejadors són el principal mecanisme de recollida al web; bloquejar-los redueix tant el seguiment com una part considerable de la superfície d'atac. Tria un bloquejador fiable, no diversos.
- **Limita les extensions a les que fas servir.** **Les extensions llegeixen i modifiquen el contingut de les pàgines**, de manera que una extensió abandonada o maliciosa pot accedir directament a les sessions. Revisa la llista cada trimestre.

*Val la pena entendre la randomització de l'empremta del navegador, però rarament mereix prioritat. No té un valor nul. Simplement rendeix poc comparada amb els punts 1 a 5 i fa que alguns llocs fallin.*

Consulta l'anàlisi completa a **[Millors navegadors de privadesa 2026: LibreWolf contra Brave i Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**.

### 11. Xifra el DNS

**El DNS pla no està xifrat i es pot observar, de manera que l'operador de xarxa i qualsevol intermediari pot veure cada domini que consultes.** DNS over HTTPS o DNS over TLS xifra aquestes consultes.

Dues salvetats honestes:

- **DoH trasllada la confiança, no l'elimina.** Ara el teu resolver veu les consultes en lloc de l'ISP. L'objectiu és triar un resolver amb una política de privadesa publicada, no només fer servir el protocol.
- **DoH evita els filtres a nivell de xarxa**, inclosos els controls parentals i corporatius dels quals depèn molta gent.

*Un benefici de seguretat real més enllà de la privadesa: el DNS xifrat elimina la falsificació de DNS com a via pràctica d'atac a les xarxes hostils.*

### 12. Elimina les metadades abans de compartir

**Les fotos contenen més que píxels.** La majoria de càmeres de telèfon insereixen dades EXIF, com ara coordenades GPS, marques de temps i identificadors del dispositiu.

**Això importa encara més per als documents que per a les fotos.** Un PDF o fitxer d'oficina compartit sovint conserva noms d'autor, historial d'edició i rutes internes, i així pot revelar detalls de l'organització.

El nostre **[Visor EXIF](/exif-viewer/)** llegeix les metadades d'una imatge localment, de manera que veus què revela la foto sense pujar-la. **[Analitzador d'URL](/url-parser/)** fa el mateix amb els enllaços: mostra paràmetres de seguiment i credencials dins l'autoritat abans que enganxis una URL en un xat.

## Nivell 4: Física i humana

Aquest nivell dura uns trenta minuts i cobreix allò a què cap control de programari arriba.

### 13. Control físic dels dispositius

- **Bloqueja totes les pantalles**, amb un temps d'espera curt. Un portàtil desbloquejat equival a la vulneració de tots els comptes.
- **No deixis dispositius a la vista dins d'un vehicle.** És una mesura contra el robatori, i el robatori també comporta pèrdua de dades.
- **Fes servir una pantalla de privadesa** en espais públics per evitar la majoria de mirades indiscretes.
- **Examina els punts de càrrega públics** abans de connectar-t'hi. Prefereix un cable només d'alimentació o el teu adaptador de paret a un port USB desconegut.

### 14. Verifica les persones, no els missatges

**El phishing per veu i vídeo ja ha desmentit la idea que una veu coneguda demostra la identitat.** Clonar veus a partir d'uns segons d'àudio públic és habitual, i la petició sol comportar urgència i una sol·licitud de pagament o credencials.

La contramesura és fer servir un altre canal:

1. **Penja i torna a trucar** a un número que ja tenies, no al que t'ha donat qui truca.
2. **Tracta la urgència com un senyal, no com una raó.** La pressió per actuar de seguida és el mecanisme de l'atac.
3. **Acorda una frase de verificació** amb els familiars que podrien suplantar.
4. **No moguis diners basant-te només en una trucada o missatge de veu.**

*És l'element de més rendiment del nivell 4 i no costa res.*

### 15. Documents i eliminació

- **Tritura o tapa amb una redacció** els documents amb números de compte, identificació o dades mèdiques.
- **Marca amb filigrana els documents** que comparteixis per a un propòsit concret, amb el destinatari i la data. No costa res i permet rastrejar una filtració.
- **Sol·licita sortir dels llocs de cerca de persones** i compta que ho hauràs de repetir, perquè els llistats tornen a aparèixer.
- **Revisa els registres públics** i demana que retirin la informació quan sigui possible.

*La nostra **[Llista de seguretat física](/checklists/physical-security-checklist/)** aprofundeix més en aquesta capa.*

## El que la majoria fa a l'inrevés

Vuit hàbits que val la pena abandonar, per què persisteixen i què fer en comptes:

| Hàbit | Per què persisteix | Fes això en comptes |
|---|---|---|
| **Memoritzar contrasenyes curtes i complexes** | Durant anys, aquesta era la recomanació | Fes servir un gestor i una frase de contrasenya llarga per a la bóveda |
| **Canviar contrasenyes segons un calendari** | Política de compliment antiga | Canvia-les després d'un avís de filtració o sospita de vulneració, no pel calendari |
| **Dependre dels SMS per als comptes crítics** | És l'opció predeterminada | Canvia correu, finances i identitat a claus d'accés o clau física |
| **Desar codis 2FA al mateix gestor que les contrasenyes** | És còmode | Separa'ls perquè una sola vulneració no exposi tots dos factors |
| **Tractar l'emmagatzematge sincronitzat al núvol com una còpia de seguretat** | Ho sembla | Afegeix una còpia fora de línia o una còpia amb permís d'escriptura |
| **Perseguir la perfecció de l'empremta del navegador** | Es pot mesurar i sembla pràctic | Fes primer els punts 1 a 5 |
| **Respondre honestament les preguntes de seguretat** | Sembla obligatori | Desa respostes falses al gestor |
| **Suposar que HTTPS vol dir que és segur** | El cadenat tranquil·litza | Verifica el domini, perquè molts llocs de phishing tenen certificats vàlids |

El patró dels vuit: **cadascun és visible i mesurable, per això crida l'atenció, però tots queden per sota d'un element de més rendiment.** Qui optimitza l'entropia de l'empremta abans de configurar un gestor de contrasenyes ha invertit l'ordre.

> **Error habitual: considerar arriscats els gestors de contrasenyes perquè concentren secrets.** És cert que concentren el risc, però l'alternativa és reutilitzar contrasenyes en desenes de llocs. Una concentració que controles és millor que una dispersió que no controles.

## Fes-ho sense cedir les teves dades

Un problema pràctic travessa tot aquest tema. **Les eines que t'ajuden a protegir els comptes sovint et demanen els mateixos secrets que vols protegir.**

Un comprovador de contrasenyes que envia la teva contrasenya a un servidor és un risc. Una calculadora de hash que puja el fitxer anul·la el propòsit. Una eina de certificats que consulta el teu nom d'amfitrió informa un tercer dels llocs que gestiones.

**Totes les eines següents funcionen completament al navegador**, sense pujar dades ni crear un compte. El lloc declara aquesta política i identifica obertament les excepcions en lloc d'amagar-les.

**Comprova el límit tu mateix:** desconnecta't de la xarxa, obre l'eina i inspecciona el panell de xarxa del navegador mentre processen un valor de prova. L'afirmació de processament local descriu el disseny previst. També convé revisar les extensions del navegador i la versió de l'eina.

| Tasca | Eina | Què gestiona |
|---|---|---|
| **Crear una contrasenya forta** | **[Generador de contrasenyes](/password-generator/)** | `crypto.getRandomValues` amb mostreig per rebuig per evitar biaix de mòdul, a més de l'entropia de la configuració triada |
| **Comprovar la força d'una contrasenya** | **[Comprovador de força de contrasenyes](/password-checker/)** | Avalua una contrasenya localment, incloent-hi patrons i reutilització |
| **Configurar un segon factor** | **[Generador TOTP i HOTP](/totp-generator/)** | Llegeix secrets Base32 o URI `otpauth://` i verifica codis en diverses finestres de temps |
| **Inspeccionar el certificat d'un lloc** | **[Informació del certificat SSL](/ssl-certificate-info/)** | Assumpte, validesa, força de la clau, SAN i avisos d'algoritmes febles |
| **Comprovar una cadena de certificats** | **[Comprovador de cadena SSL](/ssl-chain-tester/)** | Ordena la cadena i verifica cada signatura per detectar intermediaris absents |
| **Verificar una descàrrega o un fitxer** | **[Calculadora de hash](/hash-calculator/)** | Calcula des de MD5 fins a SHA-512 i confirma la integritat amb un resum publicat |
| **Generar identificadors únics** | **[Generador UUID](/uuid-generator/)** | Identificadors de versió 4 amb bits de versió i variant correctes |
| **Inspeccionar un enllaç sospitós** | **[Analitzador d'URL](/url-parser/)** | Descobreix el camí, enumera paràmetres i assenyala credencials a l'autoritat |
| **Comprovar metadades de fotos** | **[Visor EXIF](/exif-viewer/)** | Mostra les dades GPS, l'hora i el dispositiu que conté una foto |
| **Mesurar codificació o xifratge** | **[Analitzador d'entropia](/entropy-analyzer/)** | Calcula l'entropia de Shannon per distingir dades repetitives de dades codificades o xifrades |
| **Neutralitzar un indicador de manera segura** | **[Desactivar i reactivar IOC](/ioc-defang-refang/)** | Desactiva URL i adreces perquè no es puguin obrir quan es comparteixen |

*El principi de la taula: si una eina necessita el secret, s'ha d'executar allà on és el secret. Consulta **[Totes les eines](/tools/)** per veure la llista completa, incloses les poques que fan peticions de xarxa i el motiu.*

## La pregunta del model d'amenaces

**La llista adequada depèn de qui vols mantenir fora**, i saltar-se aquesta pregunta porta a dedicar esforços a llocs equivocats.

| La teva situació | Adversari realista | On centrar-te |
|---|---|---|
| **La majoria de persones** | Delinqüents oportunistes, emplenament automatitzat de credencials i phishing indiscriminat | Nivells 1 i 2, més els dispositius que portes |
| **Persona coneguda o amb càrrec públic** | Phishing dirigit, doxxing, intents de segrest de comptes | Afegeix compartimentació, àlies i considera monitorar la presència a les xarxes |
| **Periodista, activista o amb risc legal** | Estats o adversaris ben finançats, confiscació de dispositius | Afegeix Tor, dispositius dedicats i disciplina per separar identitats |
| **Propietari d'una petita empresa** | Vulneració del correu empresarial, frau de factures, desviament de pagaments | Verifica cada transferència per un canal extern |
| **Professional tècnic** | Cadena de subministrament, robatori de credencials, atacs mitjançant dependències | Afegeix claus físiques, pràctiques de signatura de codi i separació de la identitat laboral i personal |

**Lectura honesta de la taula.** Per a la majoria, gran part del risc realista és als nivells 1 i 2. Els elements avançats són essencials per a qui els necessita i sovint els adopta gent que no els necessita.

*La nostra guia **[Com crear el teu propi model d'amenaces personal](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** t'ensenya a fer aquesta avaluació.*

## Idees clau

- **L'ordre importa més que la exhaustivitat.** Cinc mesures del nivell 1 eliminen més riscos reals que els 300 punts d'una llista completa fets a l'atzar.
- **Les claus d'accés i les claus físiques són els únics segons factors que vencen el phishing**, perquè la credencial està vinculada a l'origen i no surt del dispositiu.
- **El programari maliciós infostealer roba directament galetes de sessió**, de manera que el robatori de tokens fa que el segon factor més feble no sigui suficient per si sol.
- **El xifratge converteix el robatori d'un dispositiu en una pèrdua de maquinari** en lloc d'una filtració de dades. Confirma que està activat, perquè no sempre ho està per defecte.
- **L'emmagatzematge sincronitzat no és una còpia de seguretat.** Afegeix una còpia fora de línia o una còpia amb permís d'escriptura i prova de restaurar-la.
- **La recuperació del compte és la nova superfície d'atac.** Desa els codis de recuperació fora de línia i separats del gestor de contrasenyes.
- **Els àlies trenquen la correlació** entre les bases de dades filtrades que contenen la teva adreça.
- **La majoria dels consells que veus optimitzats rendeixen poc.** Els ajustos de l'empremta i la falsificació de l'user-agent queden molt per sota d'un gestor de contrasenyes i les actualitzacions automàtiques.
- **La llista correcta depèn del teu adversari.** Les mesures avançades són vitals per a qui les necessita i sovint les adopten persones que no.

## Passos següents

1. **Fes avui el nivell 1**, que triga unes dues hores: gestor de contrasenyes, segon factor resistent al phishing, actualitzacions automàtiques, xifratge del dispositiu i una còpia de seguretat provada.
2. **Aprofundeix amb una llista comunitària** de diversos centenars de punts en una dotzena de categories: **[Llista de seguretat personal](https://github.com/Lissy93/personal-security-checklist)**
3. **Fes servir la versió interactiva** per filtrar segons el model d'amenaces i seguir el progrés: **[Digital Defense](https://digital-defense.io)**
4. **Aplica les llistes organitzatives del lloc** per als equivalents professionals: **[Seguretat de contrasenyes](/checklists/password-security-checklist/)**, **[Sensibilització sobre phishing](/checklists/phishing-awareness-checklist/)**, **[Còpia de seguretat i recuperació de dades](/checklists/data-backup-recovery-checklist/)**, **[Seguretat de dispositius mòbils](/checklists/mobile-device-security-checklist/)** i **[Seguretat de xarxes socials](/checklists/social-media-security-checklist/)**
5. **Tria un gestor de contrasenyes** amb la comparació d'arquitectures: **[Bitwarden contra KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)**
6. **Canvia a un navegador millor** en comptes d'optimitzar-ne un de més feble: **[LibreWolf contra Brave i Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)**
7. **Protegeix les dades de pagament** amb números de targeta virtuals: **[Targetes virtuals Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)**
8. **Fes servir les eines localment**, començant pel **[Generador de contrasenyes](/password-generator/)** i el **[Generador TOTP](/totp-generator/)**

## Articles relacionats

| Article | Què cobreix |
|---|---|
| **[Com crear el teu propi model d'amenaces personal](/articles/how-to-form-your-own-personal-threat-model-safeguard-online-security/)** | L'avaluació que determina a quin nivell pertanys |
| **[Millors gestors de contrasenyes 2026: Bitwarden contra KeePassXC](/articles/bitwarden-and-keepassxc-vs-the-rest/)** | Triar entre bóvedes sincronitzades al núvol i arquitectures fora de línia |
| **[Com crear contrasenyes segures el 2026](/articles/how-to-create-strong-passwords/)** | Entropia, frases de contrasenya i per què la longitud supera el canvi de símbols |
| **[Guia d'autenticació multifactor](/articles/what-are-the-diferent-kinds-of-factors-in-mfa/)** | La classificació dels factors darrere la comparació anterior |
| **[Millors navegadors de privadesa 2026: LibreWolf contra Brave i Tor](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/)** | Protecció del navegador per al nivell 3 |
| **[Opcions de rellotges intel·ligents per a privadesa i seguretat](/articles/smartwatches-for-privacy-and-security-enthusiasts/)** | Aplicar la mateixa lògica d'ordenació als dispositius portables |
| **[Targetes virtuals Privacy.com](/articles/privacy-com-virtual-debit-cards-security-privacy/)** | Limitar l'exposició dels pagaments, en relació amb la congelació del crèdit |

## Referències

1. [Llista de seguretat personal, llista comunitària d'Alicia Sykes](https://github.com/Lissy93/personal-security-checklist)
2. [Llista de seguretat personal, document complet](https://github.com/Lissy93/personal-security-checklist/blob/HEAD/CHECKLIST.md)
3. [Digital Defense, versió interactiva](https://digital-defense.io)
4. [Awesome Privacy, llista de programari respectuós amb la privadesa](https://github.com/lissy93/awesome-privacy)
5. [Have I Been Pwned, notificacions de filtracions](https://haveibeenpwned.com)
6. [FIDO Alliance, especificacions de claus d'accés i FIDO2](https://fidoalliance.org/passkeys/)
7. [Use Plaintext Email, configuració de correu en text pla](https://useplaintext.email/)
8. [Consumer Financial Protection Bureau, informes i puntuacions de crèdit](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
9. [FTC, consells per a consumidors sobre robatori d'identitat](https://consumer.ftc.gov/identity-theft-and-online-security)
10. [Passkeys.dev, recurs comunitari sobre la implementació de claus d'accés](https://passkeys.dev/)

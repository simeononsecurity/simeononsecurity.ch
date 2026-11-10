---
title: "Els tipus de ciberatac més habituals i com detectar-los"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Aprèn quins són els ciberatacs més habituals, quins rastres deixen als registres i a la telemetria, i practica la detecció en un laboratori de seguretat domèstic."
genre: ["Ciberseguretat", "Detecció d'amenaces", "Blue Team", "Operacions de seguretat", "Desenvolupament professional"]
tags: ["tipus de ciberatac", "programari maliciós", "ransomware", "phishing", "spear phishing", "enginyeria social", "suplantació", "atacs basats en la identitat", "credential stuffing", "password spraying", "injecció SQL", "cross-site scripting", "atac a la cadena de subministrament", "amenaça interna", "túnel DNS", "atacs IoT", "atacs amb IA", "denegació de servei", "enginyeria de detecció", "analista SOC", "Blue Team", "laboratori domèstic", "anàlisi de registres", "resposta a incidents", "MITRE ATT&CK", "carrera en ciberseguretat", "cerca d'amenaces", "centre d'operacions de seguretat", "telemetria", "triatge d'alertes"]
cover: "/img/cover/types-of-cyberattacks-icons-illustration.webp"
coverAlt: "Il·lustració digital amb icones abstractes i acolorides que representen diversos ciberatacs, com ara ransomware, phishing i denegació de servei, sobre un fons fosc."
coverCaption: ""
---

Un **tipus d'atac** és una categoria de tècniques, no pas una eina concreta. Ransomware, phishing i credential stuffing descriuen mètodes que un adversari repeteix contra molts objectius amb petites variacions. Conèixer aquestes categories et dona un índex mental de les alertes que trobaràs en un equip de seguretat.

*Les famílies concretes de programari maliciós apareixen i desapareixen en qüestió de mesos. Les categories d'atac següents es mantenen estables des de fa anys, i cadascuna deixa un rastre recognoscible a la telemetria dels endpoints, les identitats, la xarxa o el correu electrònic.*

<!--more-->

## Idees clau

- **Aprèn el patró, no la càrrega útil.** Les categories d'atac canvien molt més lentament que les eines individuals.
- **Cada categoria deixa proves.** La detecció comença quan saps quina telemetria registra l'activitat.
- **Reprodueix un atac per entendre'l.** Un laboratori domèstic converteix una categoria abstracta en una observació registrada.
- **Documenta què has trobat.** Una nota d'investigació breu demostra la feina i explica les proves recollides.

## Tipus d'atac d'un cop d'ull

La taula enumera les categories que els equips de seguretat troben més sovint. Les seccions següents descriuen cada categoria, les seves variants habituals i les dades que un defensor revisa per detectar-la.

| Tipus d'atac | Què fa |
|---|---|
| **Programari maliciós** | Executa programari perjudicial, com ara ransomware, programari espia i troians |
| **Denegació de servei** | Inunda un servei de trànsit fins que els usuaris legítims perden l'accés |
| **Phishing** | Enganya una persona perquè reveli les credencials o executi un fitxer maliciós |
| **Suplantació** | Es fa passar per un sistema, remitent o adreça de confiança |
| **Atacs basats en la identitat** | Abusen de credencials robades o falsificades per actuar com un usuari vàlid |
| **Injecció de codi** | Insereix codi maliciós en una aplicació per canviar-ne el comportament |
| **Atacs a la cadena de subministrament** | Comprometen un proveïdor, una biblioteca o un canal d'actualització de confiança |
| **Enginyeria social** | Manipula una persona perquè faci una acció insegura |
| **Amenaces internes** | Abusen de l'accés d'un empleat actual o anterior |
| **Túnel DNS** | Codifica dades en consultes DNS per esquivar els controls |
| **Atacs IoT** | Ataquen dispositius connectats per moure's per la xarxa, espiar o unir-se a una botnet |
| **Atacs amb IA** | Utilitzen aprenentatge automàtic per generar contingut, suplantar persones o evadir filtres |

**Nota sobre l'abast:** les categories se solapen. Un correu de phishing sovint distribueix programari maliciós, i el robatori de credencials sovint precedeix un atac basat en la identitat. Considera la llista com un conjunt de perspectives, no com a caselles rígides.

______

## Programari maliciós

**Programari maliciós** és qualsevol programa dissenyat per perjudicar, controlar o obtenir beneficis d'un sistema. El terme inclou ransomware, programari maliciós sense fitxers, programari espia i publicitari, troians, cucs, rootkits, keyloggers i botnets.

| Subtipus | Comportament |
|---|---|
| **Ransomware** | Xifra fitxers i exigeix un pagament per la clau de desxifratge |
| **Programari maliciós sense fitxers** | Utilitza eines integrades del sistema i escriu poc al disc |
| **Programari espia** | Recull dades d'activitat sense que l'usuari ho sàpiga |
| **Troià** | Es fa passar per programari legítim perquè l'executin |
| **Cuc** | Es copia d'un host a un altre sense que l'usuari hi intervingui |
| **Rootkit** | S'amaga dins del sistema operatiu per mantenir-hi el control de manera persistent |

**On es troben les proves:** les eines de detecció i resposta d'endpoints, o **EDR**, registren arbres de processos, línies d'ordres, escriptures de fitxers i canvis al registre. Un atac sense fitxers també produeix telemetria de processos i scripts, perquè el sistema operatiu continua iniciant les eines que l'atac aprofita.

______

## Denegació de servei

**Un atac de denegació de servei (DoS)** inunda un objectiu de sol·licituds fins que els usuaris legítims perden l'accés. **Un atac distribuït de denegació de servei (DDoS)** repeteix la mateixa idea des de molts sistemes alhora, cosa que dificulta molt filtrar el trànsit per adreça d'origen.

| Característica | DoS | DDoS |
|---|---|---|
| **Origen** | Un sistema | Molts sistemes |
| **Dificultat de bloqueig** | Moderada | Alta, perquè les fonts es troben en moltes xarxes |
| **Impacte habitual** | Pèrdua de disponibilitat | Pèrdua de disponibilitat a més gran escala |

**On es troben les proves:** volum de trànsit comparat amb una referència, nombre de connexions per origen, pics en la taxa de sol·licituds i canvis en la taxa d'errors. La supervisió de disponibilitat sovint genera una alerta abans que l'equip de seguretat vegi l'incident.

______

## Phishing

**El phishing** utilitza correu electrònic, missatges de text, trucades telefòniques o xarxes socials per empènyer una persona a revelar les credencials o executar un fitxer adjunt maliciós. Les variants es distingeixen pel públic i el canal.

| Variant | Públic i canal |
|---|---|
| **Spear phishing** | Una persona o un equip concret, normalment per correu electrònic |
| **Whaling** | Alts càrrecs i directius, sovint per moure diners o dades |
| **Smishing** | Missatges de text fraudulents |
| **Vishing** | Trucades o missatges de veu fraudulents |

**On es troben les proves:** registres de la passarel·la de correu, resultats de l'anàlisi d'URL, anàlisi dels fitxers adjunts i informes dels usuaris. L'avís d'un empleat prudent és un dels senyals més valuosos d'aquesta llista.

______

## Suplantació

**La suplantació** amaga un atacant darrere d'una identitat de confiança perquè l'objectiu accepti la connexió, el missatge o l'adreça. La disfressa guanya temps i supera les comprovacions basades en la confiança.

| Tipus | Què es falsifica |
|---|---|
| **Suplantació de domini** | Un lloc web o domini de correu semblant que imita una marca real |
| **Suplantació de correu** | L'adreça del remitent d'un missatge |
| **Suplantació ARP** | Una adreça de xarxa local per interceptar el trànsit entre dos hosts |

**On es troben les proves:** resultats SPF, DKIM i DMARC a les capçaleres de correu, antiguitat del registre del domini, discrepàncies de certificats i avisos d'adreces duplicades a la xarxa local.

______

## Atacs basats en la identitat

**Els atacs basats en la identitat** utilitzen un compte vàlid en lloc d'un defecte de programari. L'atacant té credencials funcionals, de manera que l'activitat s'assembla a l'ús normal i es confon amb el soroll de fons. Aquesta categoria genera una gran part de les alertes que un **centre d'operacions de seguretat (SOC)** tracta cada dia.

*Si només practiques una categoria en un laboratori domèstic, tria aquesta. Els senyals són abundants, els exercicis es poden repetir i la configuració és petita.*

| Tècnica | Què passa |
|---|---|
| **Kerberoasting** | Sol·licita un tiquet de servei i després n'esquerda fora de línia la contrasenya xifrada |
| **Atac de l'home del mig (MITM)** | S'interposa entre dues parts per llegir o modificar una sessió |
| **Pass-the-hash** | Reutilitza un hash de contrasenya robat per obrir una sessió nova |
| **Golden ticket** | Falsifica un tiquet Kerberos per obtenir accés ampli al domini |
| **Silver ticket** | Falsifica un tiquet de servei per a un servei concret |
| **Recollida de credencials** | Recopila noms d'usuari i contrasenyes en massa |
| **Credential stuffing** | Prova les mateixes credencials en molts llocs web no relacionats |
| **Password spraying** | Prova una contrasenya habitual en molts comptes |
| **Força bruta** | Prova moltes contrasenyes contra un compte |
| **Degradació** | Obliga una connexió a utilitzar una versió més feble del protocol |

**On es troben les proves:** registres d'inici de sessió, recompte d'autenticacions fallides, anomalies de tokens, alertes de desplaçaments impossibles i deteccions de risc d'identitat. **El phishing adversary-in-the-middle (AiTM)** també pertany a aquesta categoria, perquè l'atacant roba un token de sessió actiu en lloc d'una contrasenya i la seva reutilització des d'una infraestructura desconeguda activa el motor de risc d'identitat.

______

## Injecció de codi

**La injecció de codi** col·loca codi controlat per l'atacant dins d'una aplicació vulnerable perquè aquesta l'executi com a part del seu funcionament normal. L'acció perjudicial la duu a terme l'aplicació, no l'atacant.

| Tipus | Objectiu |
|---|---|
| **Injecció SQL** | Una consulta a la base de dades construïda amb entrades no validades |
| **Cross-site scripting (XSS)** | Una pàgina web que executa el script de l'atacant al navegador d'un visitant |
| **Malvertising** | Un espai publicitari legítim omplert amb codi maliciós |
| **Enverinament de dades** | Un conjunt d'entrenament per a un model d'IA o aprenentatge automàtic |

**On es troben les proves:** registres d'aplicacions web, registres de consultes a bases de dades, informes de la política de seguretat de contingut i patrons de sol·licituds diferents de l'ús normal de l'aplicació.

______

## Atacs a la cadena de subministrament

**Un atac a la cadena de subministrament** s'adreça a un tercer de confiança el producte o servei del qual arriba a molts clients. **Un atac a la cadena de subministrament de programari** injecta codi maliciós en una aplicació, biblioteca o actualització perquè el rebin tots els usuaris del producte. **Un atac a la cadena de subministrament de maquinari** compromet un component físic abans que s'enviï.

*El programari modern depèn de biblioteques de tercers. Per això, una dependència compromesa arriba molt més enllà del proveïdor original.*

**On es troben les proves:** anàlisi de composició del programari, registres de la canalització de compilació, connexions sortints inesperades d'una actualització de confiança i comprovacions d'integritat dels artefactes distribuïts.

______

## Enginyeria social

**L'enginyeria social** utilitza pressió psicològica per empènyer una persona a fer una acció insegura. L'atacant apel·la a l'autoritat, la urgència, la por, els diners o la confiança.

| Tècnica | Enfocament |
|---|---|
| **Pretexting** | Inventa una situació creïble per guanyar confiança |
| **Compromís del correu empresarial (BEC)** | Es fa passar per un company de confiança per desviar un pagament o compartir dades |
| **Desinformació** | Difon relats falsos mitjançant xarxes socials i bots |
| **Quid pro quo** | Ofereix una recompensa a canvi d'informació o accés |
| **Parany sentimental** | Crea una relació falsa per obtenir diners, dades o accés |
| **Tailgating** | Segueix un empleat a través d'una porta protegida |

**On es troben les proves:** resultats d'autenticació del correu, peticions inusuals per canviar pagaments, registres del servei d'assistència i registres d'accés físic.

______

## Amenaces internes

**Una amenaça interna** és l'ús indegut de l'accés per part d'un empleat actual o anterior, un contractista o un soci. Algunes persones actuen intencionadament per diners o ressentiment. D'altres ho fan per negligència, per exemple si deixen credencials en un document compartit.

*Els informes d'incidents esmenten més sovint persones internes negligents que no pas malicioses. En tots dos casos cal el mateix control de detecció: comparar l'accés amb una referència pròpia del rol.*

**On es troben les proves:** volum de transferència de dades, activitat fora de l'horari habitual, canvis de privilegis i baixades massives de repositoris sensibles.

______

## Túnel DNS

**El túnel DNS** codifica dades dins de les consultes i les respostes DNS. Gairebé totes les xarxes permeten DNS, de manera que aquesta tècnica fa passar dades més enllà dels controls dissenyats per inspeccionar el trànsit web.

*La detecció depèn del volum i la forma. Un host que envia milers de consultes a un sol domini destaca respecte d'una referència normal, i els subdominis inusualment llargs suggereixen una càrrega útil codificada.*

**On es troben les proves:** registres de consultes DNS, longitud i volum de consultes per host, tipus de registre poc habituals com TXT i consultes a dominis registrats pocs dies abans.

______

## Atacs contra dispositius IoT

**Un atac basat en IoT** s'adreça a un dispositiu connectat com ara una càmera, una impressora, un termòstat o un sensor. Les credencials predeterminades febles i les actualitzacions de microprogramari poc freqüents converteixen aquests dispositius en punts d'entrada habituals. Un cop compromès, un dispositiu s'uneix a una botnet, filtra dades o esdevé una ruta cap a la xarxa més àmplia.

*El desplegament de la 5G afegeix dispositius connectats a gran escala, i cada dispositiu nou és un altre objectiu amb un cicle d'actualització llarg.*

**On es troben les proves:** inventari de dispositius, patrons de connexió sortint, transferències anormals des d'un dispositiu amb una funció fixa i diferències de versió del microprogramari dins d'una flota.

______

## Atacs basats en la IA

**Els atacs basats en la IA** apliquen aprenentatge automàtic a les tasques de l'atacant.

| Tècnica | Ús |
|---|---|
| **IA/ML adversària** | Manipula les dades d'entrenament o les entrades per enganyar un model |
| **Dark AI** | Aplica IA i aprenentatge automàtic per explotar vulnerabilitats |
| **Deepfake** | Genera àudio, vídeo o imatges falsos d'aspecte realista |
| **Enginyeria social generada amb IA** | Manté converses convincents per xat o veu a gran escala |

*Una trucada amb veu deepfake o un xat de phishing fluid fa més creïble un truc antic. La tècnica subjacent continua sent coneguda. Per això, les habilitats de detecció basades en el comportament duren més que les lligades a una sola eina.*

**On es troben les proves:** senyals sobre la procedència del contingut, verificació per un canal alternatiu en les sol·licituds de diners o accés i anomalies de comportament relacionades amb canvis d'identitat i pagaments.

______

## Relacionar els atacs amb la telemetria

Cada categoria aporta dades d'una font diferent. La taula les relaciona i ofereix un punt de partida per a la detecció.

| Tipus d'atac | Telemetria principal |
|---|---|
| **Programari maliciós** | Registres EDR de processos, fitxers i registre del sistema |
| **Denegació de servei** | Flux de xarxa i monitors de disponibilitat |
| **Phishing** | Registres de la passarel·la de correu i l'anàlisi d'URL |
| **Suplantació** | Registres d'autenticació del correu i adreces de xarxa |
| **Basat en la identitat** | Registres d'inici de sessió i protecció d'identitat |
| **Injecció de codi** | Registres d'aplicacions web i consultes a bases de dades |
| **Cadena de subministrament** | Canalització de compilació i inventari de dependències |
| **Enginyeria social** | Registres de correu, servei d'assistència i accés físic |
| **Amenaça interna** | Registres d'accés i transferència de dades |
| **Túnel DNS** | Registres de consultes DNS |
| **IoT** | Inventari de dispositius i registres de flux sortint |
| **Basat en la IA** | Registres d'identitat, pagaments i procedència del contingut |

*Comença la detecció per la columna de telemetria. Una regla útil parteix d'una font de dades coneguda i d'un comportament conegut, no del nom d'una eina.*

**Les categories se solapen durant un incident.** Un missatge de phishing pot provocar el robatori de credencials, l'execució de programari maliciós i una intrusió basada en la identitat. Etiqueta la tècnica d'accés inicial i després registra per separat els comportaments següents. Així evites convertir un sol esdeveniment en quatre alertes sense relació i obtens una cronologia més clara per a la investigació.

______

## Practicar-ne la detecció en un laboratori

Una categoria és abstracta fins que la veus en acció. Un laboratori domèstic permet generar l'activitat, recollir la telemetria i comparar l'alerta amb el registre en brut. El [vídeo de carrera sobre la creació d'un centre d'operacions de seguretat](https://www.youtube.com/watch?v=s3g8o7Np1_g) mostra la configuració completa per adquirir experiència professional abans de trobar feina.

{{< youtube id="s3g8o7Np1_g" >}}

Comença per la categoria d'identitat. Crea un usuari de prova, activa el registre dels inicis de sessió i executa una seqüència d'inicis fallits i correctes. Després llegeix el registre i apunta els camps que distingeixen l'ús normal de l'exercici.

**Un exercici repetible:**

1. **Tria una categoria** de la taula de telemetria anterior.
2. **Reprodueix una versió innòcua** de l'activitat al teu sistema o compte de prova.
3. **Recull la telemetria** que produeix la categoria.
4. **Descriu la idea de detecció** com a regla, cerca desada o consulta.
5. **Prova la regla** amb l'exercici i confirma que s'activa amb el comportament previst.
6. **Anota els límits** de la regla, incloses les activitats que no detecta.

La guia [Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/) explica en detall la construcció de l'entorn: llicències, segmentació de xarxa, recopilació de registres i proves de controls d'identitat. La guia [Mad Hat Cyber Range](https://madhat.io/pages/cyber-range-guide) amplia la mateixa idea amb una configuració de taller que inclou exercicis d'atac, detecció i defensa.

Per mantenir un vocabulari coherent, relaciona el comportament observat amb la tècnica corresponent de [MITRE ATT&CK](https://attack.mitre.org/). Considera aquesta relació una ajuda per a l'analista, no una prova d'atribució. Conserva l'esdeveniment en brut, la consulta, la versió de la regla i els punts cecs coneguts amb el registre de l'exercici.

{{< centerbutton href="/articles/microsoft-soc-home-lab-2026/" >}}
  Llegeix la guia Microsoft SOC Home Lab
{{< /centerbutton >}}

______

## Passos següents

Comença amb una categoria i un exercici. Afegeix una segona categoria després d'haver acabat i documentat la primera. L'objectiu és aprofundir en una investigació, no fer una llista d'eines.

- **[Guia Microsoft SOC Home Lab](/articles/microsoft-soc-home-lab-2026/)** construeix l'entorn per a aquests exercicis.
- **[Crear un laboratori d'informàtica a casa](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/)** tracta la infraestructura que hi ha sota un laboratori de seguretat.
- **[Consells per escriure un currículum d'informàtica](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/)** mostra com presentar un laboratori documentat com a experiència pràctica.
- **[Els cinc principals vectors de ciberatac i les seves mitigacions](/articles/the-top-five-cyber-attack-vectors-and-mitigations/)** redueix la llista als vectors més habituals.

**Materials de referència:** les categories d'atac i els seus subtipus segueixen la [guia de CrowdStrike sobre ciberatacs habituals](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/common-cyberattacks/) de Kurt Baker. Els enllaços a productes i referències apunten a la documentació de Microsoft.

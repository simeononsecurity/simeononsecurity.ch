---
title: "Laboratori SOC domèstic de Microsoft: desenvolupa experiència en ciberseguretat el 2026"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Crea un laboratori SOC Microsoft amb Sentinel, Defender, Intune i Entra. Investiga incidents, valida polítiques de claus d’accés i documenta proves per al portfolio."
genre: ["Ciberseguretat", "Seguretat al núvol", "Desenvolupament professional"]
tags: ["laboratori SOC domèstic", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "laboratori Azure domèstic", "experiència en ciberseguretat", "analista SOC", "centre d’operacions de seguretat", "resposta a incidents", "KQL", "Log Analytics", "Conditional Access", "MFA resistent al phishing", "claus d’accés", "seguretat d’identitats", "portfolio de ciberseguretat", "gestió de costos al núvol", "seguretat d’endpoints"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Un portàtil mostra cronologies d’incidents de seguretat en un escriptori domèstic, sota un núvol amb servidors i endpoints."
coverCaption: ""
---

Un **laboratori SOC domèstic** ofereix un espai per investigar alertes, explicar proves i provar canvis defensius. Crea un entorn Microsoft petit, recull-ne la telemetria i documenta cada investigació. El resultat útil és una investigació repetible amb proves que la sustentin.

Aquesta guia amplia l’enfocament de laboratori descrit al vídeo professional de ciberseguretat de Mad Hat i al runbook Cyber Range proporcionat. Utilitza documentació de Microsoft per als requisits dels productes i divideix la configuració, la detecció i la validació en tasques mesurables.

## Idees principals

- **Comença amb poc:** un client Windows gestionat i una identitat de prova serveixen per als primers exercicis.
- **Verifica la telemetria:** veure un dispositiu o un portal connectat no prova que arribin els registres.
- **Completa la investigació:** registra el desencadenant, les proves, la resposta i la nova prova.
- **Controla les despeses:** segueix per separat llicències, retenció de dades, xarxa i càlcul.
- **Descriu l’experiència amb precisió:** presenta l’entorn com a projecte de laboratori al currículum.

## Abans de començar

**Requisits previs:** coneixements bàsics d’administració de Windows i xarxes, i familiaritat amb les màquines virtuals. Utilitza un tenant dedicat de Microsoft Entra i una subscripció Azure reservada al laboratori. Mantén fora de l’exercici les identitats de producció, els fitxers personals i els sistemes de l’ocupador.

**Esforç estimat:** reserva un cap de setmana per a la configuració inicial i, després, programa sessions d’investigació concretes. És una estimació de planificació. L’aprovació de la prova, les quotes i el subministrament dels serveis afecten la durada real. **Dificultat:** intermèdia.

Prepara un compte administratiu separat i un usuari de prova sense privilegis. Abans de provar les polítiques d’accés, estableix i verifica l’accés d’emergència. Assigna privilegis per a cada tasca de configuració i utilitza un compte de menys privilegis per a les investigacions habituals.

| Component | Ús al laboratori |
|---|---|
| **Sentinel** | Gestió d’informació i esdeveniments de seguretat (SIEM) per a fonts de registre connectades |
| **Defender XDR** | Correlació i investigació entre serveis de seguretat Microsoft amb llicència |
| **Defender for Endpoint** | Detecció i resposta als endpoints incorporats |
| **Intune** | Inscripció de dispositius i gestió de polítiques de seguretat dels endpoints |
| **Entra ID** | Identitats, registres d’inici de sessió i avaluació de polítiques d’accés |
| **Defender for Servers** | Protecció de servidors mitjançant Defender for Cloud |

## Comprova primer les llicències

**Microsoft 365 E5** és una opció per a un laboratori ampli, però l’accés depèn dels plans de servei i les llicències assignats als usuaris participants. Office 365 E5 i Microsoft 365 E5 són paquets diferents. La llicència d’un administrador no garanteix cobertura per a cada usuari de prova o càrrega de treball. Consulta els [requisits de Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) abans de triar una subscripció.

**Sentinel al portal Defender** funciona sense E5 ni Defender XDR. Afegir XDR comporta requisits propis de llicències i configuració. Una vista d’incidents buida no prova que falti una llicència E5. La [documentació d’incorporació de Sentinel](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) descriu ambdues configuracions.

**La protecció de servidors** té una via de llicències pròpia. Defender for Servers s’integra amb Defender for Endpoint per a les càrregues de servidor compatibles. Els sistemes Windows client necessiten una cobertura de client adequada. No donis per fet que cada VM d’Azure té automàticament una llicència de servidor. Consulta la documentació Microsoft sobre la [integració de Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Planifica la prova:** comprova al teu compte l’elegibilitat, la caducitat, la renovació i els serveis inclosos. No pressupostis segons una durada de prova promesa o un total mensual fix esmentat en un vídeo.

## Planifica la despesa

**Els pressupostos Azure** envien notificacions. No aturen el consum quan arribes a un llindar. Els informes de costos també tenen retard. Crea alertes aviat i revisa les despeses després de cada sessió segons la [guia de pressupostos Microsoft](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Categoria de cost | Pregunta de planificació |
|---|---|
| **Llicències d’usuari** | Quins usuaris necessiten quins plans de servei i quan caduquen les proves? |
| **Càlcul** | Quantes hores de VM necessita cada exercici? |
| **Emmagatzematge** | Quins discos i instantànies queden després d’apagar? |
| **Recollida de registres** | Quines taules necessiten ingestió i durant quant de temps s’han de conservar les dades? |
| **Xarxa** | El disseny inclou Bastion de pagament, IP públiques o serveis de sortida? |
| **Protecció de servidors** | Quines càrregues tenen habilitat un pla Defender de pagament? |

**Decisió de disseny:** comença amb un client. Afegeix un servidor quan un exercici necessiti telemetria de servidor. Quatre clients i diversos servidors augmenten l’administració i el cost abans d’aportar pràctica d’investigació útil.

## Construeix la xarxa

**Distribució suggerida:** col·loca els recursos Azure en un grup amb un nom clar, com ara **`rg-soc-lab`**. Utilitza subxarxes separades per a clients i servidors, regles explícites de grups de seguretat de xarxa i accés d’administració privat. Separar subxarxes no bloqueja per si sol el trànsit entre càrregues.

Per a un desplegament dedicat d’**Azure Bastion**, segueix els requisits de SKU, inclòs el nom reservat **`AzureBastionSubnet`** i una subxarxa **`/26`** o més gran en els desplegaments actuals. Developer SKU utilitza un altre model. Consulta la [configuració de Bastion](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) abans de triar.

Mantén RDP i SSH tancats a Internet públic. Limita el trànsit administratiu al camí triat. Permet la connectivitat de sortida necessària per a la inscripció i la telemetria de seguretat.

**Validació:** estableix l’accés privat d’administració i comprova les regles de xarxa efectives abans d’instal·lar càrregues. Si després afegeixes una aplicació deliberadament vulnerable, mantén-la dins la xarxa d’exercici i limita l’accés a les màquines de prova.

## Connecta Sentinel i els registres

**Configuració del portal:** crea un espai de treball Log Analytics i habilita-hi Sentinel. Si no apareix al portal Defender, obre **System > Settings > Microsoft Sentinel > Connect a workspace**. Comprova el tenant i els rols Azure i Entra necessaris als [requisits d’incorporació](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**La recollida de registres és un pas separat.** A Entra, configura els paràmetres de diagnòstic perquè enviïn les categories d’activitat necessàries al mateix espai de treball. Comença amb inicis de sessió interactius i esdeveniments d’auditoria. La [guia d’integració de registres Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) explica els permisos i la destinació.

El flux actual de Sentinel també admet la connexió a través del portal Microsoft Defender. Abans d’investigar una taula buida, confirma que l’espai de treball principal sigui el previst, que el tenant coincideixi amb les identitats de prova i que el compte tingui els rols necessaris. Veure el portal no prova la ingestió. [Incorporació de Sentinel al portal Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Executa aquest exemple de **Kusto Query Language (KQL)** a la vista Logs de l’espai de treball després de generar un nou inici de sessió de prova. Substitueix l’UPN d’exemple pel teu usuari del laboratori. Les columnes segueixen l’[esquema de la taula SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Resultat esperat:** una fila que coincideixi amb el compte de prova i l’hora d’inici de sessió. Si no hi ha files, comprova el període, la identitat, la recollida, la destinació i el retard d’ingestió. Si falta la taula, primer apunta a un problema de recollida o de l’espai de treball i després a la detecció.

## Incorpora el primer endpoint

**La inscripció d’Intune i la incorporació EDR** són punts de control diferents. Connecta Intune i Defender for Endpoint, inscriu un client Windows compatible i assigna una política d’incorporació EDR al seu grup de laboratori. El registre d’Entra, tot sol, no confirma cap dels dos punts.

A Intune, comprova **Endpoint security > Defender for Endpoint**. Si la connexió no està disponible, habilita la connexió Intune a les funcions avançades d’endpoint de Defender. Segueix els passos específics de la plataforma a la [guia d’integració d’Intune i Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Punt de control | Prova que cal recollir |
|---|---|
| **Inscripció** | El client apareix a Intune amb una sincronització recent |
| **Assignació de política** | La política d’incorporació s’aplica al grup de dispositius previst |
| **Informes del sensor** | Defender mostra l’estat d’incorporació i telemetria recent |
| **Prova de detecció** | Una prova documentada produeix el senyal de seguretat esperat |

**Per als servidors**, habilita el pla Defender for Servers triat i la integració d’endpoint, i després comprova el desplegament i els informes del sensor. Defender for Cloud també descobreix màquines abans que acabi la incorporació. La presència a l’inventari no és suficient, com explica la guia Microsoft de [descobriment i incorporació de recursos](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Investiga una alerta de prova

**Comença amb la prova de detecció EDR documentada per Microsoft** a l’endpoint de laboratori. Segueix les [instruccions actuals de la prova](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), inclosos els requisits de plataforma i la resolució de problemes. Anota l’hora d’execució abans d’obrir la cua d’alertes.

Tracta l’alerta resultant com un exercici d’investigació. El títol del producte és un punt de partida. Has d’establir què ha passat i justificar la decisió amb proves.

1. **Triatge:** identifica l’origen de l’alerta, el dispositiu, el compte i l’hora de l’esdeveniment.
2. **Inspecció:** revisa l’arbre de processos, la línia d’ordres, els detalls del fitxer i l’activitat de xarxa disponible.
3. **Abast:** cerca activitat relacionada amb la identitat de prova i els altres dispositius del laboratori.
4. **Avaluació:** explica si les proves coincideixen amb l’exercici planificat o amb un esdeveniment aliè.
5. **Resposta:** documenta la resposta triada, l’impacte i els passos de recuperació. Aplica contenció compatible només quan l’exercici ho requereixi.
6. **Nova prova:** després de canviar un control, repeteix la prova pertinent i compara les proves.

**No inventis resultats absents.** Si l’alerta no arriba, conserva el registre d’execució i resol el problema de recollida. Si un control bloqueja la prova abans de l’esdeveniment previst, documenta el resultat de prevenció.

## Prova els controls d’identitat

**El phishing de tipus adversary-in-the-middle (AiTM)** posa un intermediari controlat per l’atacant dins del flux d’inici de sessió. El runbook proporcionat utilitza aquest escenari per justificar una autenticació més forta. Per al primer exercici d’identitat, prova directament el comportament de les polítiques amb el teu compte sense privilegis.

Comença registrant un inici de sessió legítim i els seus detalls d’autenticació. Consulta la [referència Microsoft de detecció de riscos Entra](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) abans d’interpretar els senyals de risc. Els prerequisits i el processament varien segons el senyal. Una IP nova o un inici de sessió fallit no garanteixen una alerta AiTM.

**Les claus d’accés (FIDO2)** utilitzen credencials vinculades al servei legítim, no codis reutilitzables introduïts en una pàgina d’inici de sessió retransmesa. Habilita un perfil adequat per al grup pilot i registra el mètode abans d’aplicar una política. Consulta la [guia Microsoft de configuració de claus d’accés](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) per conèixer els autenticadors admesos i les restriccions.

**Exercici Conditional Access:** crea una política només per al grup pilot del laboratori, exclou els comptes d’accés d’emergència i selecciona **Require authentication strength > Phishing-resistant MFA strength**. Comença en **Report-only**, revisa l’impacte i després habilita la política. Adapta l’[exemple Microsoft de política d’administrador](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) a un grup de prova reduït.

| Prova | Evidència que cal recollir |
|---|---|
| **Política Report-only** | Registre d’inici de sessió que mostra l’avaluació de la política proposada |
| **Política aplicada, mètode més feble** | Una nova autenticació exigeix un mètode més fort abans de concedir accés |
| **Política aplicada, clau d’accés registrada** | Inici de sessió correcte que satisfà el nivell de seguretat exigit |

Utilitza una autenticació nova per a cada comparació i consulta els detalls de la política. Les sessions existents compliquen les comparacions. **Abast de la prova:** aquest exercici valida el requisit d’autenticació. No demostra protecció universal contra la intrusió d’un endpoint ni el robatori d’una sessió existent.

## Escriu proves per al portfolio

**Una entrada útil al portfolio** explica una decisió perquè un altre analista la pugui avaluar. Inclou una descripció breu de l’arquitectura, prerequisits de recollida, cronologia de l’esdeveniment i raonament de la resposta.

```text
Exercici:
Data i interval horari UTC:
Abast del laboratori i prerequisits:
Activador i senyal esperat:
Alerta observada o prevenció:
Proves i consultes:
Identitats i dispositius afectats:
Conclusió i raonament:
Resposta i recuperació:
Canvi de control i nova prova:
Limitacions i seguiment:
```

Substitueix cada camp per observacions pròpies. **Neteja les exportacions:** elimina credencials, material de sessió, informació personal i identificadors innecessaris abans de publicar captures o resultats de consultes.

**Exemple de currículum:** «He creat un laboratori de seguretat Microsoft, he connectat registres d’identitat a Sentinel, he investigat alertes de prova d’endpoint i he documentat la validació Conditional Access». Utilitza aquesta redacció només després de completar les tasques. Inclou-la a projectes o formació pràctica amb dates i abast reals.

Un laboratori demostra pràctica independent. **La feina en un SOC de producció** també inclou impacte empresarial, escalació, compromisos de servei i coordinació amb altres equips. Explica quines parts has practicat i quines queden fora de la teva experiència.

## Resolució de problemes

| Símptoma | Primera comprovació |
|---|---|
| **Espai de treball absent de Defender** | Mateix tenant, Sentinel habilitat i rols d’incorporació necessaris |
| **SigninLogs absent o buit** | Categories de diagnòstic, destinació, esdeveniments nous i període |
| **Client absent d’Intune** | Requisits i estat d’inscripció |
| **Dispositiu visible sense telemetria** | Estat real d’incorporació, salut del sensor i connectivitat de sortida |
| **Política d’incorporació no aplicada** | Abast de l’assignació, plataforma i sincronització recent |
| **Sense alerta de risc d’identitat** | Requisits del senyal i activitat registrada, sense pressuposar detecció determinista |
| **Accés concedit inesperadament** | Estat Report-only, exclusions, abast del recurs i sessió existent |
| **Càrrecs després d’apagar** | Estat d’assignació i recursos facturats independentment del càlcul |

**Ordre de resolució:** demostra primer que l’esdeveniment ha passat, després que la recollida ha funcionat i finalment investiga la lògica de detecció. Anota cada fallada i correcció a les notes del projecte.

## Atura o elimina el laboratori

**La desassignació** allibera el càlcul de la VM. Aturar només el sistema convidat no garanteix la desassignació. Comprova l’estat d’alimentació a Azure i consulta la documentació Microsoft sobre [estats i facturació de VM](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Els recursos retinguts** també necessiten revisió. Discos, instantànies, serveis de xarxa, retenció de registres i subscripcions d’usuari tenen cicles de vida separats. Programa un recordatori abans de cada venciment de prova i consulta el següent informe d’ús després de la neteja.

Abans d’eliminar el grup de recursos del laboratori, exporta les proves que vulguis conservar i inspecciona’n el contingut. **Eliminar el grup de recursos és destructiu** per als recursos que conté. Els usuaris del tenant, les polítiques d’Intune i Conditional Access, les subscripcions i la configuració de seguretat de la subscripció poden requerir una neteja separada.

## Passos següents

**Completa una investigació documentada** abans d’afegir una altra càrrega. Després, afegeix un servidor, un exercici d’identitat o una regla de detecció amb una condició de prova clara. Anota què ensenya el component nou i quant costa.

Utilitza la [guia de laboratori d’IT](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) per practicar infraestructura i la [guia de currículum d’IT](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) per presentar la feina. Mantén el projecte següent prou petit per explicar configuració, proves i neteja.

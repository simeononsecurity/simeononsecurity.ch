---
title: "Microsoft SOC-thuislab: bouw cybersecurityervaring op in 2026"
date: 2026-09-11
lastmod: 2026-11-27
toc: true
draft: false
description: "Bouw een Microsoft SOC-lab met Sentinel, Defender, Intune en Entra. Onderzoek incidenten, toets passkeybeleid en documenteer bewijs voor je portfolio."
genre: ["Cybersecurity", "Cloudbeveiliging", "Loopbaanontwikkeling"]
tags: ["SOC-thuislab", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "Azure-thuislab", "cybersecurityervaring", "SOC-analist", "beveiligingsoperatiecentrum", "incidentrespons", "KQL", "Log Analytics", "Conditional Access", "phishingbestendige MFA", "passkeys", "identiteitsbeveiliging", "cybersecurityportfolio", "cloudkostenbeheer", "endpointbeveiliging"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Een laptop toont tijdlijnen van beveiligingsincidenten op een bureau thuis onder een wolk met servers en endpoints."
coverCaption: ""
---

Een **SOC-thuislab** biedt een plek om meldingen te onderzoeken, bewijs uit te leggen en beveiligingswijzigingen te testen. Bouw een kleine Microsoft-omgeving, verzamel telemetrie en documenteer elk onderzoek. Het nuttige resultaat is een herhaalbaar onderzoek met onderbouwing.

Deze gids werkt de labaanpak uit die wordt beschreven in Mad Hats carrièrevideo over cybersecurity en het meegeleverde Cyber Range-runbook. Microsoft-documentatie vormt de basis voor productvereisten. De gids verdeelt inrichting, detectie en validatie in meetbare taken.

## Belangrijkste punten

- **Begin klein:** één beheerde Windows-client en één testidentiteit volstaan voor de eerste oefeningen.
- **Controleer telemetrie:** een zichtbaar apparaat of verbonden portal bewijst niet dat logs binnenkomen.
- **Rond het onderzoek af:** noteer de trigger, het bewijs, de reactie en de hertest.
- **Beheers de uitgaven:** volg licenties, gegevensbewaring, netwerk en rekenkracht afzonderlijk.
- **Beschrijf ervaring nauwkeurig:** vermeld de omgeving als labproject op je cv.

## Voordat je begint

**Vereisten:** basiskennis van Windows-beheer en netwerken, plus ervaring met virtuele machines. Gebruik een aparte Microsoft Entra-tenant en een Azure-abonnement voor het lab. Houd productie-identiteiten, persoonlijke bestanden en systemen van je werkgever buiten de oefening.

**Geschatte inspanning:** reserveer een weekend voor de eerste inrichting en plan daarna gerichte onderzoekssessies. Dit is een planningsschatting. Goedkeuring van de proefperiode, quota en dienstverlening beïnvloeden de werkelijke duur. **Moeilijkheid:** gemiddeld.

Bereid een aparte beheerdersaccount en een ongeprivilegieerde testgebruiker voor. Stel noodtoegang in en controleer die voordat je toegangsbeleid test. Ken per inrichtingstaak de benodigde rechten toe en gebruik voor routineonderzoek een account met minder rechten.

| Onderdeel | Doel in het lab |
|---|---|
| **Sentinel** | Beheer van beveiligingsinformatie en gebeurtenissen (SIEM) voor verbonden logbronnen |
| **Defender XDR** | Correlatie en onderzoek over gelicentieerde Microsoft-beveiligingsdiensten |
| **Defender for Endpoint** (eindpuntbeveiliging) | Detectie en reactie op ingeschreven endpoints |
| **Intune** | Apparaatinschrijving en beheer van endpointbeveiligingsbeleid |
| **Entra ID** | Identiteiten, aanmeldingsrecords en beoordeling van toegangsbeleid |
| **Defender for Servers** (serverbeveiliging) | Serverbeveiliging via Defender for Cloud |

## Controleer eerst licenties

**Microsoft 365 E5** is een optie voor een uitgebreid lab, maar toegang hangt af van serviceplannen en licenties die aan deelnemende gebruikers zijn toegewezen. Office 365 E5 en Microsoft 365 E5 zijn verschillende bundels. Een beheerderslicentie dekt niet automatisch elke testgebruiker of workload. Bekijk de [vereisten voor Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) voordat je een abonnement kiest.

**Sentinel in de Defender-portal** werkt zonder E5 of Defender XDR. XDR toevoegen brengt eigen licentie- en configuratievereisten mee. Een lege incidentweergave bewijst niet dat een E5-licentie ontbreekt. De [Sentinel-onboardingdocumentatie](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) beschrijft beide configuraties.

**Serverbeveiliging** heeft een apart licentiepad. Defender for Servers integreert met Defender for Endpoint voor ondersteunde serverworkloads. Windows-clientbesturingssystemen hebben passende clientdekking nodig. Ga er niet van uit dat elke Azure-VM automatisch als server is gelicentieerd. Lees Microsofts documentatie over de [integratie van Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Plan de proefperiode:** controleer in je eigen account de geschiktheid, einddatum, verlenging en inbegrepen services. Baseer je begroting niet op een beloofde proefduur of een vast maandbedrag uit een video.

## Plan de uitgaven

**Azure-budgetten** sturen meldingen. Ze stoppen het gebruik niet zodra een drempel wordt bereikt. Kostenrapportage loopt ook achter. Maak vroeg waarschuwingen aan en controleer na elke sessie de uitgaven met de [Microsoft-gids voor budgetten](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Kostencategorie | Planningsvraag |
|---|---|
| **Gebruikerslicenties** | Welke gebruikers hebben welke serviceplannen nodig en wanneer verlopen proefperiodes? |
| **Rekenkracht** | Hoeveel VM-uren vraagt elke oefening? |
| **Opslag** | Welke schijven en momentopnamen blijven na afsluiten bestaan? |
| **Logverzameling** | Welke tabellen moeten gegevens opnemen en hoe lang moeten die bewaard blijven? |
| **Netwerk** | Omvat het ontwerp betaald Bastion, openbare IP-adressen of uitgaande services? |
| **Serverbeveiliging** | Op welke workloads staat een betaald Defender-plan aan? |

**Ontwerpkeuze:** begin met één client. Voeg een server toe wanneer een oefening servertelemetrie nodig heeft. Vier clients en meerdere servers verhogen beheer en kosten voordat ze nuttige onderzoekservaring toevoegen.

## Bouw het netwerk

**Voorgestelde indeling:** plaats Azure-resources in een groep met een duidelijke naam, zoals **`rg-soc-lab`**. Gebruik aparte subnetten voor clients en servers, expliciete regels voor netwerkbeveiligingsgroepen en privébeheerstoegang. Subnetten scheiden blokkeert op zichzelf geen verkeer tussen workloads.

Volg bij een aparte **Azure Bastion**-implementatie de SKU-vereisten, waaronder de gereserveerde naam **`AzureBastionSubnet`** en een subnet van **`/26`** of groter voor huidige implementaties. Developer SKU gebruikt een ander implementatiemodel. Bekijk de [Bastion-configuratie](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) voordat je een ontwerp kiest.

Houd RDP en SSH gesloten voor het openbare internet. Beperk beheer naar het gekozen pad. Sta uitgaande verbindingen toe die nodig zijn voor inschrijving en beveiligingstelemetrie.

**Validatie:** regel privébeheerstoegang en controleer de effectieve netwerkregels voordat je workloads installeert. Als je later een opzettelijk kwetsbare toepassing toevoegt, houd die binnen het oefennetwerk en beperk toegang tot testmachines.

## Verbind Sentinel en logs

**Portaal instellen:** maak een Log Analytics-werkruimte en schakel Sentinel daarop in. Staat de werkruimte niet in de Defender-portal, open dan **System > Settings > Microsoft Sentinel > Connect a workspace** (Systeem > Instellingen > Microsoft Sentinel > Een werkruimte verbinden). Controleer de tenant en vereiste Azure- en Entra-rollen aan de hand van de [onboardingvereisten](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**Logverzameling is een aparte stap.** Stel in Entra diagnostische instellingen in die de vereiste activiteitcategorieën naar dezelfde werkruimte sturen. Begin met interactieve aanmeldingen en auditgebeurtenissen. De [Entra-logintegratiegids](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) beschrijft rechten en bestemming.

De huidige Sentinel-werkwijze ondersteunt ook verbinding via de Microsoft Defender-portal. Controleer voordat je een lege tabel onderzoekt of de juiste primaire werkruimte is gekozen, de tenant overeenkomt met de testidentiteiten en de account de vereiste rollen heeft. Zichtbaarheid in het portaal bewijst geen gegevensinname. [Sentinel onboarden in de Defender-portal](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Voer dit **Kusto Query Language (KQL)**-voorbeeld uit in de Logs-weergave van de werkruimte nadat je een nieuwe testaanmelding hebt gemaakt. Vervang de voorbeeld-UPN door je labgebruiker. De kolommen volgen het [schema van de SigninLogs-tabel](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Verwacht resultaat:** een rij die overeenkomt met het testaccount en de aanmeldingstijd. Controleer zonder rijen de periode, identiteit, verzamelinstellingen, bestemming en innamevertraging. Een ontbrekende tabel wijst eerst op een probleem met verzameling of werkruimte en daarna pas op detectie.

## Onboard het eerste endpoint

**Intune-inschrijving en EDR-onboarding** zijn aparte controlepunten. Verbind Intune en Defender for Endpoint, schrijf een ondersteunde Windows-client in en wijs een EDR-onboardingbeleid toe aan de labgroep. Entra-registratie alleen bevestigt geen van beide punten.

Controleer in Intune **Endpoint security > Defender for Endpoint** (Endpointbeveiliging > Defender for Endpoint (beveiliging van eindpunten)). Is de verbinding niet beschikbaar, schakel dan de Intune-verbinding in bij de geavanceerde endpointfuncties van Defender. Volg de platformspecifieke stappen in de [integratiegids voor Intune en Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Controlepunt | Te verzamelen bewijs |
|---|---|
| **Inschrijving** | Client staat in Intune met een recente check-in |
| **Beleidstoewijzing** | Onboardingbeleid geldt voor de bedoelde apparaatgroep |
| **Sensorrapportage** | Defender toont onboardingstatus en recente telemetrie |
| **Detectietest** | Een gedocumenteerde test produceert het verwachte beveiligingssignaal |

**Voor servers:** schakel het gekozen Defender for Servers-plan en de endpointintegratie in. Controleer daarna sensorimplementatie en rapportage. Defender for Cloud ontdekt machines ook voordat onboarding is voltooid. Alleen aanwezigheid in de inventaris is onvoldoende, zoals Microsoft uitlegt in de gids voor [resourcedetectie en onboarding](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Onderzoek een testwaarschuwing

**Begin met Microsofts gedocumenteerde EDR-detectietest** op het labendpoint. Volg de [actuele testinstructies](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), inclusief platformvereisten en probleemoplossing. Noteer de uitvoeringstijd voordat je de waarschuwingswachtrij opent.

Behandel de waarschuwing als een onderzoeksoefening. De titel van het beveiligingsproduct is een beginpunt. Stel vast wat er gebeurde en onderbouw de beslissing met bewijs.

1. **Triage:** bepaal de bron van de waarschuwing, het apparaat, de account en de gebeurtenistijd.
2. **Inspectie:** bekijk de procesboom, opdrachtregel, bestandsdetails en beschikbare netwerkactiviteit.
3. **Afbakening:** zoek verwante activiteit op de testidentiteit en andere labapparaten.
4. **Beoordeling:** leg uit of het bewijs past bij de geplande oefening of een andere gebeurtenis.
5. **Reactie:** documenteer de gekozen reactie, impact en herstelstappen. Gebruik ondersteunde insluiting alleen als de oefening dat vraagt.
6. **Hertest:** herhaal na een wijziging de relevante test en vergelijk het bewijs.

**Verzin geen ontbrekende resultaten.** Komt de waarschuwing niet binnen, bewaar dan het uitvoeringsrecord en onderzoek de verzameling. Blokkeert een controle de test vóór de verwachte gebeurtenis, documenteer dan de preventie-uitkomst.

## Test identiteitscontroles

**Adversary-in-the-middle-phishing (AiTM)** plaatst een door een aanvaller beheerde tussenpersoon in de aanmeldstroom. Het meegeleverde runbook gebruikt dit scenario als reden voor sterkere authenticatie. Test de eerste identiteitscontrole rechtstreeks met je eigen account zonder privileges.

Leg eerst een legitieme aanmelding en de authenticatiedetails vast. Lees Microsofts [referentie voor Entra-risicodetectie](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) voordat je risicosignalen interpreteert. Vereisten en verwerking verschillen per signaal. Een nieuw IP-adres of mislukte aanmelding garandeert geen AiTM-waarschuwing.

**Passkeys (FIDO2)** gebruiken aanmeldgegevens die aan de legitieme dienst zijn gebonden, in plaats van herbruikbare codes op een doorgestuurde aanmeldpagina. Schakel een passend passkeyprofiel in voor de pilotgroep en registreer de methode voordat je een beleid afdwingt. De [Microsoft-gids voor passkeyconfiguratie](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) beschrijft ondersteunde authenticators en beperkingen.

**Conditional Access-oefening (voorwaardelijke toegang):** maak een beleid voor alleen de labpilotgroep, sluit noodtoegangsaccounts uit en kies **Require authentication strength > Phishing-resistant MFA strength** (sterke authenticatie en phishingbestendige MFA). Begin met **Report-only (alleen rapporteren)**, beoordeel de gevolgen en schakel het beleid daarna in. Pas het [Microsoft-voorbeeldbeleid voor beheerders](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) aan op een kleine testgroep.

| Controle | Te verzamelen bewijs |
|---|---|
| **Report-only (alleen rapporteren)-beleid** | Aanmeldrecord dat laat zien hoe het voorgestelde beleid wordt beoordeeld |
| **Afgedwongen beleid, zwakkere methode** | Nieuwe authenticatie vereist een sterkere methode vóór toegang |
| **Afgedwongen beleid, geregistreerde passkey** | Geslaagde aanmelding die aan het vereiste niveau voldoet |

Gebruik voor elke vergelijking nieuwe authenticatie en bekijk de beleidsdetails. Bestaande sessies bemoeilijken vergelijkingen. **Bewijsbereik:** deze oefening controleert de authenticatie-eis. Ze bewijst geen universele bescherming tegen endpointcompromittering of diefstal van een bestaande sessie.

## Leg portfolio-bewijs vast

**Een nuttige portfoliovermelding** legt een beslissing uit zodat een andere analist die kan beoordelen. Voeg een korte architectuurbeschrijving, verzamelvereisten, gebeurtenistijdlijn en onderbouwing van de reactie toe.

```text
Oefening:
Datum en UTC-tijdsvenster:
Labomvang en vereisten:
Trigger en verwacht signaal:
Waargenomen waarschuwing of preventie:
Bewijs en query’s:
Betrokken identiteiten en apparaten:
Beoordeling en onderbouwing:
Reactie en herstel:
Wijziging van de controle en hertest:
Beperkingen en opvolging:
```

Vervang elk veld door je eigen waarnemingen. **Zuiver exports:** verwijder inloggegevens, sessiemateriaal, persoonlijke informatie en onnodige identificatoren voordat je screenshots of queryresultaten publiceert.

**Voorbeeld voor je cv:** “Ik bouwde een Microsoft-beveiligingslab, koppelde identiteitslogs aan Sentinel, onderzocht endpointtestwaarschuwingen en documenteerde Conditional Access-validatie.” Gebruik deze formulering pas nadat je de taken hebt uitgevoerd. Zet de ervaring onder projecten of praktijktraining met echte datums en scope.

Een lab toont zelfstandige oefening. **Werk in een productie-SOC** omvat ook bedrijfsimpact, escalatie, serviceafspraken en coördinatie met andere teams. Leg uit welke onderdelen je hebt geoefend en welke buiten je ervaring vallen.

## Problemen oplossen

| Symptoom | Eerste controle |
|---|---|
| **Werkruimte ontbreekt in Defender** | Dezelfde tenant, Sentinel ingeschakeld en vereiste onboardingrollen |
| **SigninLogs ontbreekt of is leeg** | Diagnosecategorieën, doelwerkruimte, nieuwe gebeurtenissen en periode |
| **Client ontbreekt in Intune** | Inschrijfvereisten en inschrijfstatus |
| **Apparaat zichtbaar zonder telemetrie** | Werkelijke onboardingstatus, sensorstatus en uitgaande verbinding |
| **Onboardingbeleid niet toegepast** | Toewijzingsscope, apparaatplatform en recente check-in |
| **Geen identiteitsrisicomelding** | Signaalvereisten en vastgelegde activiteit, zonder deterministische detectie aan te nemen |
| **Toegang onverwacht toegestaan** | Report-only (alleen rapporteren)-status, uitzonderingen, resourcescope en bestaande sessie |
| **Kosten na afsluiten** | Allocatiestatus en resources die buiten rekenkracht worden gefactureerd |

**Volgorde van probleemoplossing:** bewijs eerst dat de gebeurtenis plaatsvond, controleer daarna of verzameling werkte en onderzoek vervolgens de detectielogica. Noteer storingen en oplossingen in de projectnotities.

## Pauzeer of verwijder het lab

**Deallocatie** geeft de VM-rekenallocatie vrij. Alleen het gastbesturingssysteem afsluiten garandeert geen deallocatie. Controleer de energiestatus in Azure en bekijk Microsofts documentatie over [VM-statussen en facturering](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Aangehouden resources** vragen ook aandacht. Schijven, snapshots, netwerkservices, logbewaring en gebruikersabonnementen hebben aparte levenscycli. Stel vóór elke proefperiode een herinnering in en controleer na opruimen het volgende gebruiksrapport.

Exporteer en inspecteer het bewijs dat je wilt bewaren voordat je de labresourcegroep verwijdert. **Verwijderen van de resourcegroep is destructief** voor de resources erin. Tenantgebruikers, Intune-beleid, Conditional Access-beleid, abonnementen en beveiligingsinstellingen op abonnementsniveau vragen mogelijk afzonderlijke opruiming.

## Volgende stappen

**Rond één gedocumenteerd onderzoek af** voordat je een workload toevoegt. Voeg daarna een server, identiteitsoefening of detectieregel met een duidelijke testvoorwaarde toe. Noteer wat het onderdeel leert en wat het kost.

Gebruik de [IT-thuislabgids](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) voor infrastructuuroefeningen en de [IT-cvgids](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) om je werk te presenteren. Houd het volgende project klein genoeg om inrichting, bewijs en opruiming uit te leggen.

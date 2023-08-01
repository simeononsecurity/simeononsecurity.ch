---
title: "Richtlijnen voor veilig coderen met Ansible: Beste werkwijzen"
date: 2023-03-02
toc: true
draft: false
description: "Leer de best practices voor het schrijven van veilige code met Ansible, een populaire tool voor configuratiebeheer en implementatie."
tags: ["Veilig coderen", "Ansible", "Configuratiebeheer", "Inzet", "Minst bevoorrecht principe", "Ansible kluis", "Sterke wachtwoorden", "Toegangscontrole", "Versiebeheersysteem", "Veilige communicatieprotocollen", "SSH", "WinRM", "TLS-certificaten", "Gebruikersinvoer zuiveren", "Invoervalidatie", "Foutafhandeling", "Veilig coderen", "Code injectie", "Richtlijnen voor veilig coderen", "Infrastructuurbeveiliging", "Richtlijnen voor veilig coderen met Ansible", "Best practices voor veilige code met Ansible", "Veilig configuratiebeheer met Ansible", "Veilige implementatiepraktijken met Ansible", "Minst bevoorrechte principe in Ansible", "Ansible Vault gebruiken voor veilige code", "Sterke wachtwoorden maken in Ansible", "Toegangsbeheer in Ansible", "Versiebeheersysteem voor Ansible playbooks", "Veilige communicatieprotocollen in Ansible", "SSH-beveiliging in Ansible", "WinRM beveiliging in Ansible", "TLS-certificaten in Ansible", "Gebruikersinvoer zuiveren in Ansible", "Invoervalidatie in Ansible", "Foutafhandeling in Ansible", "Veilig coderen in Ansible", "Code-injectie in Ansible voorkomen", "Richtlijnen voor veilig coderen voor infrastructuur beheerd door Ansible", "Beveiligen van de Ansible-infrastructuur"]
cover: "/img/cover/A_cartoon_image_of_a_castle_protected_by_a_shield.png"
coverAlt: " Een cartoonafbeelding van een kasteel beschermd door een schild, die de beveiligingsmaatregelen voorstelt voor de infrastructuur die door Ansible wordt beheerd."
coverCaption: ""
---

Naarmate organisaties meer en meer automatiseren, is **Ansible** een populair hulpmiddel geworden voor **configuratiebeheer** en **deployment**. Het is echter belangrijk om te erkennen dat Ansible, net als alle software, niet ongevoelig is voor kwetsbaarheden in de beveiliging. Daarom is het van vitaal belang om prioriteit te geven aan de ontwikkeling van **veilige code** om de integriteit van de door Ansible beheerde infrastructuur te beschermen en te behouden. In dit hoofdstuk worden essentiële **best practices** beschreven voor het schrijven van **veilige code** met Ansible, zodat uw automatiseringsworkflows worden versterkt tegen potentiële bedreigingen.

## Inzicht in de beveiliging van Ansible

Voordat u in de richtlijnen duikt, is het belangrijk om de beveiligingsfuncties van Ansible te begrijpen. Ansible biedt **encryptie** voor communicatie tussen controleknooppunten en beheerde knooppunten. Ansible biedt ook **veilige opslag** van **geheimen** en andere gevoelige informatie met behulp van de **Kluis**. Daarnaast heeft Ansible een **sandboxing mechanisme** om te beschermen tegen het uitvoeren van potentieel kwaadaardige code.

Deze beveiligingsfuncties ontslaan ontwikkelaars echter niet van de plicht om veilige code te schrijven. Door de volgende richtlijnen te volgen, kunnen ontwikkelaars veilige code schrijven die de ingebouwde beveiligingsfuncties van Ansible aanvult.

## Belang van veilige code in Ansible

Het schrijven van **veilige code** is van het grootste belang wanneer u Ansible gebruikt voor het beheren van infrastructuur. Door zich te houden aan **security best practices** kunnen organisaties risico's zoals onbevoegde toegang, gegevenslekken en serviceonderbrekingen beperken. **Veilige code** in Ansible bevordert de vertrouwelijkheid, integriteit en beschikbaarheid van kritieke bedrijfsmiddelen en versterkt de algehele robuustheid en betrouwbaarheid van de geautomatiseerde omgeving.

## Richtlijn 1: Gebruik de nieuwste versie van Ansible

Ansible wordt voortdurend bijgewerkt om beveiligingsproblemen en bugs te verhelpen. Het gebruik van de nieuwste versie van Ansible zorgt ervoor dat ontwikkelaars toegang hebben tot de nieuwste beveiligingsoplossingen en -verbeteringen.

Ontwikkelaars moeten regelmatig controleren of er updates zijn en deze zo snel mogelijk installeren. Ze kunnen zich ook inschrijven op de Ansible Security Announcements mailinglijst om meldingen over beveiligingsupdates te ontvangen. Updaten naar de nieuwste versie van Ansible is een eenvoudige stap die de beveiliging van de infrastructuur die door Ansible wordt beheerd aanzienlijk kan verbeteren.

## Richtlijn 2: Volg het principe van laagste privileges

Het **least privilege principe** is een fundamenteel beveiligingsprincipe dat van toepassing is op Ansible. Dit principe stelt dat een gebruiker alleen het minimale toegangsniveau mag hebben dat nodig is om zijn functie uit te voeren. Dit principe is ook van toepassing op Ansible. Ontwikkelaars moeten beheerde knooppunten het minimale toegangsniveau geven dat nodig is om de nodige taken uit te voeren.

Als een playbook bijvoorbeeld alleen leestoegang tot een specifiek bestand vereist, moeten ontwikkelaars alleen leestoegang tot het bestand verlenen en geen schrijf- of uitvoeringstoegang. Ontwikkelaars moeten ook het aantal gebruikers met toegang tot Ansible beperken. De toegang moet worden beperkt tot bevoegde gebruikers die de infrastructuur met Ansible moeten beheren.

Ansible biedt verschillende mechanismen om het principe van de laagste rechten te implementeren, zoals de `become` richtlijn. De `become` richtlijn stelt ontwikkelaars in staat om taken uit te voeren met privileges van een andere gebruiker, zoals `sudo` Ontwikkelaars moeten `become` richtlijn alleen indien nodig en geef alleen het benodigde niveau van privileges.

Door het least privilege principe te implementeren, kunnen ontwikkelaars de potentiële schade van een aanvaller beperken in het geval van een inbreuk op de beveiliging. Deze richtlijn kan de veiligheid van de door Ansible beheerde infrastructuur aanzienlijk verbeteren.

## Richtlijn 3: Gebruik Ansible Vault voor gevoelige informatie

Gevoelige informatie zoals wachtwoorden, API-sleutels en certificaten mogen niet in platte tekst worden opgeslagen in Ansible playbooks. Het opslaan van gevoelige informatie in platte tekst kan de beveiliging van de door Ansible beheerde infrastructuur in gevaar brengen. Ansible biedt de **Vault** om gevoelige informatie veilig op te slaan.

De Vault versleutelt gevoelige informatie met een wachtwoord of een sleutelbestand. Ontwikkelaars kunnen de `ansible-vault` commando om een nieuw versleuteld bestand aan te maken, een bestaand versleuteld bestand te bewerken of een versleuteld bestand te bekijken. De `ansible-vault` commando kan ook gebruikt worden om individuele variabelen te versleutelen of te ontsleutelen. Om bijvoorbeeld een nieuw versleuteld bestand te maken, kunnen ontwikkelaars het volgende commando gebruiken:

```bash
ansible-vault create secret.yml
```

Deze opdracht maakt een nieuw versleuteld bestand met de naam `secret.yml` Ontwikkelaars kunnen dit bestand bewerken met de `ansible-vault edit` commando. Ze worden gevraagd om het wachtwoord voor de kluis in te voeren.

Ontwikkelaars moeten er ook voor zorgen dat wachtwoorden en sleutelbestanden veilig worden opgeslagen. Wachtwoorden en sleutelbestanden mogen niet in platte tekst worden opgeslagen. Ze moeten worden opgeslagen op een veilige locatie, zoals een wachtwoordmanager of een beveiligde bestandsserver.

Het gebruik van de Vault om gevoelige informatie op te slaan is een cruciale stap in de beveiliging van de infrastructuur die door Ansible wordt beheerd. Door deze richtlijn te volgen, kunnen ontwikkelaars ervoor zorgen dat gevoelige informatie niet in platte tekst wordt weergegeven en alleen toegankelijk is voor bevoegde gebruikers.

## Richtlijn 4: Gebruik sterke wachtwoorden

Wachtwoorden die gebruikt worden voor authenticatie moeten **sterk** en **uniek** zijn. Het gebruik van zwakke of veelgebruikte wachtwoorden kan de veiligheid van de door Ansible beheerde infrastructuur in gevaar brengen. Ontwikkelaars moeten ook het gebruik van standaard wachtwoorden of het hardcoden van wachtwoorden in playbooks vermijden. Wachtwoorden moeten veilig worden opgeslagen met de Vault.

Een sterk wachtwoord moet minimaal 12 tekens bevatten en een combinatie van hoofdletters en kleine letters, cijfers en speciale tekens. Ontwikkelaars moeten ook het gebruik van makkelijk te raden informatie, zoals namen of verjaardagen, in wachtwoorden vermijden. Ze kunnen een wachtwoordmanager gebruiken om sterke, unieke wachtwoorden te genereren.

Wachtwoorden die gebruikt worden in playbooks moeten versleuteld opgeslagen worden in de Vault. Ontwikkelaars moeten ook het coderen van wachtwoorden in playbooks vermijden. In plaats daarvan moeten ze variabelen gebruiken om wachtwoorden op te slaan en hiernaar te verwijzen in playbooks. Ontwikkelaars kunnen bijvoorbeeld een variabele met de naam `db_password` in een apart versleuteld bestand en verwijs ernaar in het playbook met de volgende syntaxis:
```yml
db_password: "{{ vault_db_password }}"
```

Deze syntaxis verwijst naar de `db_password` variabele van het versleutelde bestand en ontsleutelen met de Vault.

Door sterke wachtwoorden te gebruiken en deze veilig op te slaan, kunnen ontwikkelaars ongeoorloofde toegang tot de door Ansible beheerde infrastructuur voorkomen. Deze richtlijn is een eenvoudige stap die de beveiliging van de door Ansible beheerde infrastructuur aanzienlijk kan verbeteren.


## Richtlijn 5: Beperk de toegang tot Playbooks

Toegang tot Ansible playbooks moet worden beperkt tot geautoriseerde gebruikers. Ontwikkelaars zouden een **versiebeheersysteem** zoals **Git** moeten gebruiken om afspeelboeken te beheren. Git biedt **toegangscontrole** en **auditing** functies die kunnen helpen bij het afdwingen van het beveiligingsbeleid.

## Richtlijn 6: Gebruik veilige communicatieprotocollen

Ansible ondersteunt verschillende communicatieprotocollen, waaronder SSH en WinRM. SSH is het aanbevolen protocol voor Linux en macOS hosts. WinRM is het aanbevolen protocol voor Windows hosts. Ontwikkelaars moeten ervoor zorgen dat de communicatie tussen controleknooppunten en beheerde knooppunten **versleuteld** is.

SSH is een veilig communicatieprotocol dat de communicatie tussen controleknooppunten en beheerde knooppunten versleutelt. Ontwikkelaars moeten sterke SSH-sleutels gebruiken voor verificatie. SSH-sleutels moeten minimaal 2048 bits lang zijn. Ontwikkelaars moeten ook wachtwoordverificatie voor SSH uitschakelen.

WinRM is een veilig communicatieprotocol dat de communicatie tussen controleknooppunten en beheerde knooppunten versleutelt. Ontwikkelaars moeten WinRM over HTTPS gebruiken om er zeker van te zijn dat de communicatie versleuteld is. Ze moeten ook sterke certificaten gebruiken voor authenticatie.

Ontwikkelaars moeten er ook voor zorgen dat de TLS-certificaten die gebruikt worden voor HTTPS-communicatie geldig zijn en niet verlopen zijn. Ze kunnen tools zoals `openssl` om TLS-certificaten aan te maken en te beheren.

Het gebruik van veilige communicatieprotocollen is een cruciale stap in het beveiligen van de infrastructuur die door Ansible wordt beheerd. Door deze richtlijn te volgen, kunnen ontwikkelaars ervoor zorgen dat de communicatie tussen controleknooppunten en beheerde knooppunten versleuteld en veilig verloopt.

## Richtlijn 7: Host-identiteiten verifiëren

Ontwikkelaars moeten de identiteit van beheerde knooppunten verifiëren voordat ze verbinding mogen maken met controleknooppunten. Ansible biedt verschillende mechanismen om host-identiteiten te verifiëren, waaronder **SSH-sleutelvingerafdrukken** en **TLS-certificaten**. Ontwikkelaars moeten er ook voor zorgen dat SSH- en TLS-configuraties up-to-date en veilig zijn.

SSH-sleutelvingerafdrukken zijn unieke identificaties van SSH-sleutels die door beheerde knooppunten worden gebruikt voor verificatie. Ontwikkelaars moeten de SSH-sleutelvingerafdrukken van beheerde knooppunten verifiëren voordat ze verbinding mogen maken met controleknooppunten. Ze kunnen de `ssh-keygen` commando om SSH sleutel fingerprints te genereren en deze te vergelijken met de fingerprints die door beheerde knooppunten zijn aangeleverd.

TLS-certificaten worden door beheerde knooppunten gebruikt om zichzelf te authenticeren bij controleknooppunten. Ontwikkelaars moeten ervoor zorgen dat TLS-certificaten die door beheerde knooppunten worden gebruikt geldig zijn en niet verlopen zijn. Ze moeten er ook voor zorgen dat controleknooppunten de TLS-certificaten die door beheerde knooppunten worden gebruikt vertrouwen.

Ontwikkelaars dienen er ook voor te zorgen dat SSH- en TLS-configuraties up-to-date en veilig zijn. SSH- en TLS-configuraties dienen sterke encryptie- en authenticatiealgoritmen te gebruiken. Ze moeten ook geconfigureerd worden om zwakke cijfers en protocollen te weigeren.

Het verifiëren van de identiteit van beheerde knooppunten is een cruciale stap in het beveiligen van de infrastructuur die door Ansible wordt beheerd. Door deze richtlijn te volgen, kunnen ontwikkelaars man-in-the-middle aanvallen voorkomen en ervoor zorgen dat alleen geautoriseerde beheerde knooppunten verbinding kunnen maken met controleknooppunten.

## Richtlijn 8: Gebruikersinvoer zuiveren

Ontwikkelaars moeten gebruikersinvoer zuiveren om **code injectie** en andere beveiligingsproblemen te voorkomen. Ontwikkelaars zouden ook waar mogelijk **gevalideerde invoer** moeten gebruiken om het risico op beveiligingsproblemen te verminderen.

## Richtlijn 9: Volg veilige codeerpraktijken

Ontwikkelaars moeten **veilige codeerpraktijken** volgen, zoals **invoer validatie**, **foutafhandeling**, en **sanitisatie** van invoer. Ontwikkelaars moeten ook **veilige coderingsrichtlijnen** volgen voor de programmeertaal die in Ansible wordt gebruikt.

Ontwikkelaars moeten gebruikersinvoer zuiveren om **code-injectie** en andere beveiligingsproblemen te voorkomen. Code-injectie is een type aanval waarbij een aanvaller kwaadaardige code in een applicatie injecteert door gebruik te maken van kwetsbaarheden in de invoer van gebruikers. Ontwikkelaars moeten ook waar mogelijk gevalideerde invoer gebruiken om het risico op beveiligingslekken te verminderen.

Ontwikkelaars kunnen de `regex_replace` filter in Ansible om gebruikersinvoer te zuiveren. De `regex_replace` Met het filter kunnen ontwikkelaars patronen in tekenreeksen vervangen door andere patronen. Om bijvoorbeeld alle niet-alfanumerieke tekens in een tekenreeks te vervangen door een lege tekenreeks, kunnen ontwikkelaars de volgende code gebruiken:

```yaml
- name: Sanitize user input
  vars:
    user_input: "Hello! This is a string with non-alphanumeric characters."
    sanitized_input: "{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}"
  debug:
    var: sanitized_input
```
In dit voorbeeld is de `regex_replace` filter wordt gebruikt om alle niet-alfanumerieke tekens in de `user_input` variabele met een lege tekenreeks. De gezuiverde invoer wordt opgeslagen in de `sanitized_input` variabel.

Ontwikkelaars kunnen ook invoervalidatie gebruiken om het risico op beveiligingslekken te verkleinen. Invoervalidatie houdt in dat de invoer van gebruikers wordt gecontroleerd om er zeker van te zijn dat deze aan bepaalde criteria voldoet. Ontwikkelaars kunnen bijvoorbeeld invoer valideren om ervoor te zorgen dat deze alleen alfanumerieke tekens bevat. Invoervalidatie kan worden geïmplementeerd met behulp van Ansible conditionals en reguliere expressies.

Door gebruikersinvoer te zuiveren en gevalideerde invoer te gebruiken, kunnen ontwikkelaars code-injectie en andere beveiligingslekken in Ansible playbooks voorkomen. Deze richtlijn is een eenvoudige stap die de beveiliging van de door Ansible beheerde infrastructuur aanzienlijk kan verbeteren.
______

## Conclusie

Concluderend, nu organisaties automatisering omarmen, springt **Ansible** eruit als een populaire keuze voor **configuratiebeheer** en **deployment**. Het is echter cruciaal om prioriteit te geven aan de ontwikkeling van **veilige code** om de integriteit en betrouwbaarheid van de door Ansible beheerde infrastructuur te waarborgen.

Door de **richtlijnen** in dit artikel te volgen, kunnen ontwikkelaars de **best practices** op het gebied van veiligheid** in hun Ansible workflows implementeren. Dit omvat het gebruik van **Role-Based Access Control (RBAC)**, het beveiligen van communicatiekanalen met **Transport Layer Security (TLS)** of **Secure Shell (SSH)**, het beheren van geheimen en gevoelige gegevens met **Ansible Vault** en het regelmatig bijwerken van Ansible om beschermd te blijven tegen bekende kwetsbaarheden.

Vergeet niet om altijd de laatste versie van Ansible te gebruiken, het least privilege principe te volgen, Ansible Vault te gebruiken voor gevoelige informatie, sterke wachtwoorden te gebruiken, de toegang tot playbooks te beperken, veilige communicatieprotocollen te gebruiken, host-identiteiten te verifiëren, gebruikersinvoer te zuiveren en veilige codeerpraktijken te volgen. Deze richtlijnen helpen ontwikkelaars om veilige code te schrijven en hun infrastructuur te beschermen tegen beveiligingsproblemen.

Door deze **best practices** te integreren, kunnen organisaties vol vertrouwen de voordelen van de automatisering door Ansible benutten en tegelijkertijd een veilige en betrouwbare infrastructuur garanderen. Door kritieke bedrijfsmiddelen te beschermen met veilige code en door gebruik te maken van de ingebouwde beveiligingsfuncties van Ansible, kunnen organisaties automatisering omarmen zonder aan beveiliging in te boeten.

## Referenties

- [Ansible Documentation](https://docs.ansible.com/)
- [Ansible Vault Documentation](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
- [Git Documentation](https://git-scm.com/doc)
- [OpenSSH Documentation](https://www.openssh.com/)
- [Transport Layer Security (TLS) Documentation](https://tools.ietf.org/html/rfc8446)
- [OWASP Code Injection Documentation](https://owasp.org/www-community/attacks/Code_Injection)

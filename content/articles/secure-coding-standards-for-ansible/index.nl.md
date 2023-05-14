---
title: "Richtlijnen voor veilige codering voor Ansible: Beste praktijken"
date: 2023-03-02
toc: true
draft: false
description: "Leer de beste praktijken voor het schrijven van veilige code met Ansible, een populair hulpmiddel voor configuratiebeheer en implementatie."
tags: ["Veilige codering", "Ansible", "Configuratiebeheer", "Inzet", "Beginsel van het laagste voorrecht", "Ansible kluis", "Sterke wachtwoorden", "Toegangscontrole", "Versiebeheersysteem", "Veilige communicatieprotocollen", "SSH", "WinRM", "TLS-certificaten", "Gebruikersinvoer zuiveren", "Invoer validatie", "Foutafhandeling", "Veilige codeerpraktijken", "Code injectie", "Richtlijnen voor veilige codering", "Veiligheid van de infrastructuur"]
cover: "/img/cover/A_cartoon_image_of_a_castle_protected_by_a_shield.png"
coverAlt: " Een cartoonbeeld van een kasteel beschermd door een schild, dat de beveiligingsmaatregelen voor de door Ansible beheerde infrastructuur voorstelt."
coverCaption: ""
---

Naarmate organisaties steeds meer automatiseren, is **Ansible** een populaire keuze geworden voor **configuratiebeheer** en **deployment**. Maar zoals elke software is ook Ansible niet immuun voor beveiligingsproblemen. Het schrijven van **veilige code** is cruciaal om de veiligheid en betrouwbaarheid van de door Ansible beheerde infrastructuur te garanderen. Dit artikel geeft **richtlijnen** voor het schrijven van **veilige code** met Ansible.

## Ansible beveiliging begrijpen

Alvorens in de richtlijnen te duiken, is het belangrijk om de beveiligingsfuncties van Ansible te begrijpen. Ansible biedt **encryptie** voor communicatie tussen control nodes en managed nodes. Ansible biedt ook **veilige opslag** van **geheimen** en andere gevoelige informatie met behulp van de **Kluis**. Daarnaast heeft Ansible een **sandboxing mechanisme** ter bescherming tegen mogelijk kwaadaardige code-uitvoering.

Deze beveiligingsfuncties ontslaan ontwikkelaars echter niet van het schrijven van veilige code. Door de volgende richtlijnen te volgen, kunnen ontwikkelaars veilige code schrijven die de ingebouwde beveiligingsfuncties van Ansible aanvult.

## Richtlijn 1: Gebruik de laatste versie van Ansible

Ansible wordt voortdurend bijgewerkt om beveiligingsproblemen en bugs te verhelpen. Het gebruik van de laatste versie van Ansible zorgt ervoor dat ontwikkelaars toegang hebben tot de laatste beveiligingsoplossingen en -verbeteringen.

Ontwikkelaars moeten regelmatig controleren op updates en deze zo snel mogelijk installeren. Ze kunnen zich ook abonneren op de Ansible Security Announcements mailinglijst om meldingen over beveiligingsupdates te ontvangen. Updaten naar de laatste versie van Ansible is een eenvoudige stap die de beveiliging van de door Ansible beheerde infrastructuur aanzienlijk kan verbeteren.

## Richtlijn 2: Volg het Least Privilege principe

Het **least privilege principe** is een fundamenteel beveiligingsprincipe dat van toepassing is op Ansible. Dit principe stelt dat een gebruiker alleen het minimale toegangsniveau mag hebben dat nodig is om zijn functie uit te voeren. Dit principe geldt ook voor Ansible. Ontwikkelaars moeten beheerde knooppunten het minimale toegangsniveau geven dat nodig is om de noodzakelijke taken uit te voeren.

Als een playbook bijvoorbeeld alleen leestoegang tot een bepaald bestand vereist, moeten ontwikkelaars alleen leestoegang tot het bestand verlenen en geen schrijf- of uitvoeringstoegang. Ontwikkelaars moeten ook het aantal gebruikers met toegang tot Ansible beperken. De toegang moet worden beperkt tot bevoegde gebruikers die de infrastructuur met Ansible moeten beheren.

Ansible biedt verschillende mechanismen om het principe van de minste rechten toe te passen, zoals de`become` richtlijn. De`become` richtlijn stelt ontwikkelaars in staat om taken uit te voeren met privileges van een andere gebruiker, zoals`sudo` Ontwikkelaars moeten gebruik maken van`become` richtlijn alleen indien nodig en alleen het noodzakelijke niveau van privileges.

Door het least privilege principe toe te passen, kunnen ontwikkelaars de potentiële schade van een aanvaller bij een inbreuk op de beveiliging beperken. Deze richtlijn kan de beveiliging van de door Ansible beheerde infrastructuur aanzienlijk verbeteren.

## Richtlijn 3: Gebruik Ansible Vault voor gevoelige informatie

Gevoelige informatie zoals wachtwoorden, API-sleutels en certificaten mogen niet in platte tekst worden opgeslagen in Ansible playbooks. Het opslaan van gevoelige informatie in platte tekst kan de veiligheid van de door Ansible beheerde infrastructuur in gevaar brengen. Ansible biedt de **Vault** voor het veilig opslaan van gevoelige informatie.

De Vault versleutelt gevoelige informatie met een wachtwoord of een sleutelbestand. Ontwikkelaars kunnen de`ansible-vault` commando om een nieuw versleuteld bestand aan te maken, een bestaand versleuteld bestand te bewerken of een versleuteld bestand te bekijken. De`ansible-vault` commando kan ook worden gebruikt om individuele variabelen te versleutelen of te ontsleutelen. Om bijvoorbeeld een nieuw versleuteld bestand te maken, kunnen ontwikkelaars het volgende commando gebruiken:

```bash
ansible-vault create secret.yml
```

Dit commando maakt een nieuw versleuteld bestand aan met de naam`secret.yml` Ontwikkelaars kunnen dit bestand bewerken met de`ansible-vault edit` commando. Zij worden gevraagd het wachtwoord voor de kluis in te voeren.

Ontwikkelaars moeten er ook voor zorgen dat wachtwoorden en sleutelbestanden veilig worden opgeslagen. Wachtwoorden en sleutelbestanden mogen niet in platte tekst worden opgeslagen. Ze moeten worden opgeslagen op een veilige locatie, zoals een wachtwoordbeheerder of een beveiligde bestandsserver.

Het gebruik van de Vault om gevoelige informatie op te slaan is een cruciale stap in de beveiliging van de door Ansible beheerde infrastructuur. Door deze richtlijn te volgen, kunnen ontwikkelaars ervoor zorgen dat gevoelige informatie niet in platte tekst wordt blootgesteld en alleen toegankelijk is voor bevoegde gebruikers.

## Richtlijn 4: Gebruik sterke wachtwoorden

Wachtwoorden die worden gebruikt voor authenticatie moeten **sterk** en **uniek** zijn. Het gebruik van zwakke of algemene wachtwoorden kan de veiligheid van de door Ansible beheerde infrastructuur in gevaar brengen. Ontwikkelaars moeten ook vermijden om standaard wachtwoorden te gebruiken of wachtwoorden hard te coderen in playbooks. Wachtwoorden moeten veilig worden opgeslagen met behulp van de Vault.

Een sterk wachtwoord moet minimaal 12 tekens bevatten en een combinatie van hoofdletters en kleine letters, cijfers en speciale tekens. Ontwikkelaars moeten ook vermijden gemakkelijk te raden informatie, zoals namen of verjaardagen, in wachtwoorden te gebruiken. Ze kunnen een wachtwoordmanager gebruiken om sterke, unieke wachtwoorden te genereren.

Wachtwoorden die worden gebruikt in playbooks moeten versleuteld worden opgeslagen in de Vault. Ontwikkelaars moeten ook vermijden om wachtwoorden hard te coderen in playbooks. In plaats daarvan moeten ze variabelen gebruiken om wachtwoorden op te slaan en daarnaar te verwijzen in de playbooks. Ontwikkelaars kunnen bijvoorbeeld een variabele met de naam`db_password` in een apart gecodeerd bestand en verwijs ernaar in het playbook met de volgende syntaxis:
```yml
db_password: "{{ vault_db_password }}"
```

Deze syntaxis verwijst naar de`db_password` variabele van het versleutelde bestand en ontsleutelen met de kluis.

Door sterke wachtwoorden te gebruiken en deze veilig op te slaan, kunnen ontwikkelaars ongeoorloofde toegang tot de door Ansible beheerde infrastructuur voorkomen. Deze richtlijn is een eenvoudige stap die de beveiliging van de door Ansible beheerde infrastructuur aanzienlijk kan verbeteren.


## Richtlijn 5: Beperk de toegang tot Playbooks

Toegang tot Ansible playbooks moet worden beperkt tot geautoriseerde gebruikers. Ontwikkelaars zouden een **versiebeheersysteem** zoals **Git** moeten gebruiken om playbooks te beheren. Git biedt **toegangscontrole** en **auditing** functies die kunnen helpen bij het afdwingen van het beveiligingsbeleid.

## Richtlijn 6: Gebruik veilige communicatieprotocollen

Ansible ondersteunt verschillende communicatieprotocollen, waaronder SSH en WinRM. SSH is het aanbevolen protocol voor Linux en macOS hosts. WinRM is het aanbevolen protocol voor Windows hosts. Ontwikkelaars moeten ervoor zorgen dat de communicatie tussen controleknooppunten en beheerde knooppunten **versleuteld** is.

SSH is een veilig communicatieprotocol dat de communicatie tussen besturingsknooppunten en beheerde knooppunten versleutelt. Ontwikkelaars dienen sterke SSH-sleutels te gebruiken voor authenticatie. SSH-sleutels moeten minimaal 2048 bits lang zijn. Ontwikkelaars moeten ook wachtwoordverificatie voor SSH uitschakelen.

WinRM is een veilig communicatieprotocol dat de communicatie tussen controleknooppunten en beheerde knooppunten versleutelt. Ontwikkelaars moeten WinRM over HTTPS gebruiken om ervoor te zorgen dat de communicatie versleuteld is. Ze moeten ook sterke certificaten gebruiken voor authenticatie.

Ontwikkelaars moeten er ook voor zorgen dat de TLS-certificaten die worden gebruikt voor HTTPS-communicatie geldig zijn en niet zijn verlopen. Ze kunnen tools gebruiken zoals`openssl` om TLS-certificaten te genereren en te beheren.

Het gebruik van veilige communicatieprotocollen is een cruciale stap in de beveiliging van de door Ansible beheerde infrastructuur. Door deze richtlijn te volgen, kunnen ontwikkelaars ervoor zorgen dat de communicatie tussen besturingsknooppunten en beheerde knooppunten versleuteld en veilig verloopt.

## Richtlijn 7: Hostidentiteiten verifiëren

Ontwikkelaars moeten de identiteit van beheerde nodes verifiëren voordat ze verbinding mogen maken met control nodes. Ansible biedt verschillende mechanismen om host-identiteiten te verifiëren, waaronder **SSH key fingerprints** en **TLS-certificaten**. Ontwikkelaars moeten er ook voor zorgen dat SSH- en TLS-configuraties up-to-date en veilig zijn.

SSH key fingerprints zijn unieke identifiers van SSH-sleutels die door beheerde knooppunten worden gebruikt voor authenticatie. Ontwikkelaars moeten de SSH-sleutelvingerafdrukken van beheerde knooppunten verifiëren voordat ze toestemming geven om verbinding te maken met controleknooppunten. Zij kunnen de`ssh-keygen` commando om SSH-sleutelvingerafdrukken te genereren en deze te vergelijken met de vingerafdrukken die door beheerde knooppunten zijn verstrekt.

TLS-certificaten worden door beheerde knooppunten gebruikt om zich te authenticeren bij controlerende knooppunten. Ontwikkelaars moeten ervoor zorgen dat de door beheerde knooppunten gebruikte TLS-certificaten geldig zijn en niet zijn verlopen. Zij moeten er ook voor zorgen dat de controleknooppunten de door de beheerde knooppunten gebruikte TLS-certificaten vertrouwen.

Ontwikkelaars dienen er ook voor te zorgen dat SSH- en TLS-configuraties up-to-date en veilig zijn. SSH- en TLS-configuraties dienen sterke encryptie- en authenticatiealgoritmen te gebruiken. Zij dienen ook zodanig te worden geconfigureerd dat zwakke cijfers en protocollen worden geweigerd.

Het verifiëren van de identiteit van beheerde knooppunten is een cruciale stap in de beveiliging van de door Ansible beheerde infrastructuur. Door deze richtlijn te volgen, kunnen ontwikkelaars man-in-the-middle aanvallen voorkomen en ervoor zorgen dat alleen geautoriseerde beheerde knooppunten verbinding kunnen maken met controleknooppunten.

## Richtlijn 8: Sanitize User Input

Ontwikkelaars moeten gebruikersinvoer zuiveren om **code injectie** en andere beveiligingsproblemen te voorkomen. Ontwikkelaars moeten ook waar mogelijk **gevalideerde invoer** gebruiken om het risico van beveiligingsproblemen te verminderen.

## Richtlijn 9: Volg veilige codeerpraktijken

Ontwikkelaars moeten **veilige codeerpraktijken** volgen, zoals **invoer validatie**, **foutafhandeling**, en **sanitisatie** van invoer. Ontwikkelaars moeten ook **veilige coderingsrichtlijnen** volgen voor de programmeertaal die in Ansible wordt gebruikt.

Ontwikkelaars moeten gebruikersinvoer zuiveren om **code-injectie** en andere beveiligingsproblemen te voorkomen. Code-injectie is een type aanval waarbij een aanvaller kwaadaardige code in een toepassing injecteert door gebruik te maken van kwetsbaarheden in de gebruikersinvoer. Ontwikkelaars moeten ook waar mogelijk gevalideerde invoer gebruiken om het risico van beveiligingsproblemen te verminderen.

Ontwikkelaars kunnen de`regex_replace` filter in Ansible om gebruikersinvoer te zuiveren. De`regex_replace` filter kunnen ontwikkelaars patronen in strings vervangen door andere patronen. Om bijvoorbeeld alle niet-alphanumerieke tekens in een string te vervangen door een lege string, kunnen ontwikkelaars de volgende code gebruiken:

```yaml
- name: Sanitize user input
  vars:
    user_input: "Hello! This is a string with non-alphanumeric characters."
    sanitized_input: "{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}"
  debug:
    var: sanitized_input
```
In dit voorbeeld is de`regex_replace` filter wordt gebruikt om alle niet-alfanumerieke tekens in de`user_input` variabele met een lege string. De gezuiverde invoer wordt opgeslagen in de`sanitized_input` variabel.

Ontwikkelaars kunnen inputvalidatie ook gebruiken om het risico van beveiligingsproblemen te verminderen. Invoervalidatie bestaat uit het controleren van gebruikersinvoer om er zeker van te zijn dat deze aan bepaalde criteria voldoet. Ontwikkelaars kunnen bijvoorbeeld de invoer van gebruikers valideren om ervoor te zorgen dat deze alleen alfanumerieke tekens bevat. Invoervalidatie kan worden uitgevoerd met behulp van Ansible conditionals en reguliere expressies.

Door gebruikersinvoer te zuiveren en gevalideerde invoer te gebruiken, kunnen ontwikkelaars code-injectie en andere beveiligingsproblemen in Ansible playbooks voorkomen. Deze richtlijn is een eenvoudige stap die de beveiliging van de door Ansible beheerde infrastructuur aanzienlijk kan verbeteren.
______

## Conclusie

Ansible is een krachtig hulpmiddel voor configuratiebeheer en implementatie, maar het is belangrijk om veilige code te schrijven om de veiligheid en betrouwbaarheid van de door Ansible beheerde infrastructuur te garanderen. Door de richtlijnen in dit artikel te volgen, kunnen ontwikkelaars veilige code schrijven die de ingebouwde beveiligingsfuncties van Ansible aanvult.

Gebruik altijd de laatste versie van Ansible, volg het principe van de minste rechten, gebruik Ansible Vault voor gevoelige informatie, gebruik sterke wachtwoorden, beperk de toegang tot playbooks, gebruik veilige communicatieprotocollen, verifieer hostidentiteiten, zuiver gebruikersinvoer en volg veilige codeerpraktijken. Deze richtlijnen helpen ontwikkelaars veilige code te schrijven en hun infrastructuur te beschermen tegen beveiligingsproblemen.

Door deze richtlijnen te volgen, kunnen organisaties ervoor zorgen dat hun door Ansible beheerde infrastructuur veilig en betrouwbaar is. Met veilige code en de ingebouwde beveiligingsfuncties van Ansible kunnen organisaties profiteren van de voordelen van automatisering zonder de veiligheid op te offeren.

## Referenties

-[Ansible Documentation](https://docs.ansible.com/)
-[Ansible Vault Documentation](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
-[Git Documentation](https://git-scm.com/doc)
-[OpenSSH Documentation](https://www.openssh.com/)
-[Transport Layer Security (TLS) Documentation](https://tools.ietf.org/html/rfc8446)
-[OWASP Code Injection Documentation](https://owasp.org/www-community/attacks/Code_Injection)

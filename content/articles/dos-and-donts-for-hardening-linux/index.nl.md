---
title: "Essentiële do's en don'ts voor het hardenen van je Linux-systeem"
date: 2023-02-28
toc: true
draft: false
description: "Leer de essentiële do's en donts voor het harden van je Linux systeem, inclusief updaten, firewalls gebruiken, SELinux of AppArmor inschakelen, wachtwoordbeleid configureren en systeemlogs controleren."
tags: ["Linux beveiliging", "systeemharding", "firewall", "SELinux", "AppArmor", "wachtwoordbeleid", "systeemupdates", "systeemlogboeken", "beveiligingsmodules", "toegangscontrolebeleid", "cyberbeveiliging", "systeemveiligheid", "netwerkbeveiliging", "beheer van kwetsbaarheden", "beste beveiligingsprocedures", "IT-beveiliging", "informatiebeveiliging", "software-updates", "root-toegang", "wachtwoordmanager"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Een cartoonslot houdt een schild vast met het woord Linux erop, terwijl een pijl van het schild afketst."
coverCaption: ""
---


Linux is een populair besturingssysteem dat zowel door particulieren als bedrijven wordt gebruikt. Hoewel het vaak als veiliger wordt beschouwd dan andere besturingssystemen vanwege de open-source aard, vereist het nog steeds de juiste hardening om de veiligheid van het systeem en de gegevens die het bevat te garanderen. In dit artikel zullen we een aantal algemene do's en don'ts bespreken die kunnen helpen om je Linux systeem veilig te houden.

## Do's:

### Houd je systeem bijgewerkt

Uw [Linux](https://simeononsecurity.com/articles/how-do-i-learn-linux/) Het up-to-date houden van uw systeem is cruciaal voor de veiligheid ervan. Regelmatige updates helpen beveiligingslekken en bugs te verhelpen en zorgen ervoor dat je systeem veilig blijft tegen mogelijke aanvallen. Hier zijn enkele voorbeelden van hoe u uw Linux-systeem kunt bijwerken met de **apt-get** of **yum** pakketbeheerder:

#### Ubuntu updaten met apt-get

Om je Ubuntu systeem te updaten met **apt-get**, open je een terminal venster en typ je:
```bash
sudo apt-get update
```

Hiermee worden de nieuwste pakketlijsten gedownload uit de Ubuntu pakketrepositories. Zodra deze opdracht is voltooid, kunt u alle beschikbare updates installeren met de volgende opdracht:

```bash
sudo apt-get upgrade

```

Hiermee worden alle beschikbare updates voor je systeem gedownload en geïnstalleerd.

### CentOS bijwerken met yum

Om uw CentOS-systeem bij te werken met **yum**, opent u een terminalvenster en typt u:

```bash
sudo yum update
```

Hiermee worden alle beschikbare updates voor je systeem gedownload en geïnstalleerd. U kunt ook het volgende commando gebruiken om oude of ongebruikte pakketten op te ruimen:

```bash
sudo yum autoremove
```

Hierdoor worden pakketten verwijderd die niet langer nodig zijn op uw systeem.

Vergeet niet om regelmatig te controleren op updates en deze te installeren op je Linux-systeem om de veiligheid en stabiliteit te garanderen.


### Gebruik een firewall

Een firewall is een essentiële beveiligingsmaatregel voor elk Linux-systeem, omdat het helpt beschermen tegen ongeautoriseerde toegang en andere cyberbedreigingen. Hier lees je hoe je de **ufw** firewall op je Linux-systeem gebruikt:

#### Ufw installeren en inschakelen voor op Ubuntu gebaseerde systemen

Om **ufw** te installeren en in te schakelen, open je een terminalvenster en typ je:

```bash
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw enable
```

Om inkomend HTTP-verkeer (poort 80) toe te staan:

```bash
sudo ufw allow http
```

Om inkomend verkeer van een specifiek IP-adres te blokkeren:

```bash
sudo ufw deny from <ip_address>
```

Een regel verwijderen:
```bash
sudo ufw delete <rule_number>
```

Je kunt de huidige **ufw** regels bekijken door te typen:

```bash
sudo ufw status
```


Dit geeft de huidige regels en hun status weer.

Vergeet niet om je **ufw** regels regelmatig te controleren en bij te werken om ervoor te zorgen dat je systeem beschermd is tegen mogelijke bedreigingen.


#### Firewalld installeren en inschakelen voor CentOS gebaseerde systemen

Om de standaard firewall op CentOS, **firewalld**, te installeren en in te schakelen, kun je de volgende commando's gebruiken:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Dit zal **firewalld** installeren en inschakelen op uw systeem.

#### Firewalld regels configureren voor CentOS gebaseerde systemen

Zodra **firewalld** is ingeschakeld, kunt u de regels configureren om inkomend en uitgaand verkeer toe te staan of te blokkeren. Hier zijn enkele voorbeelden:

Om inkomend SSH-verkeer (poort 22) toe te staan:

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

Om inkomend HTTP-verkeer (poort 80) toe te staan:

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

Om inkomend verkeer van een specifiek IP-adres te blokkeren:

```bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<ip_address>" reject'
sudo firewall-cmd --reload
```

Een regel verwijderen:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

Je kunt de huidige **firewalld** regels bekijken door te typen:

```bash
sudo firewall-cmd --list-all
```

Dit geeft de huidige regels en hun status weer.

Vergeet niet om uw **firewalld** regels regelmatig te controleren en bij te werken om ervoor te zorgen dat uw systeem

### SELinux of AppArmor inschakelt

SELinux (Security-Enhanced Linux) en AppArmor zijn twee beveiligingsmodules die gebruikt kunnen worden om een verplicht toegangscontrolebeleid af te dwingen in Linux systemen. De meeste moderne Linux-distributies worden standaard geleverd met SELinux of AppArmor geïnstalleerd en ze kunnen worden ingeschakeld en geconfigureerd om de beveiliging van je systeem te verbeteren.

#### SELinux inschakelen voor CentOS gebaseerde systemen

Voer het volgende commando uit om te controleren of SELinux is ingeschakeld op uw systeem:

```bash
sestatus
```

Als SELinux niet is geïnstalleerd, kun je het installeren met het volgende commando:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Om SELinux in te schakelen, moet je het bestand **/etc/selinux/config** bewerken en de variabele **SELINUX** instellen op **versterken**:

```bash
sudo nano /etc/selinux/config
```
**Wijzig SELINUX=dwingend**
```
SELINUX=enforcing
```

Sla het bestand op en sluit het af met CTRL+X en Y en enter.

#### AppArmor inschakelen voor op Ubuntu gebaseerde systemen

Voer de volgende opdracht uit om te controleren of AppArmor is ingeschakeld op uw systeem:
```bash
sudo apparmor_status
```


Als AppArmor niet is geïnstalleerd, kun je het installeren met het volgende commando:
```bash
sudo apt-get install apparmor
```

Om AppArmor in te schakelen, moet je het bestand **/etc/default/grub** bewerken en de parameter **security=apparmor** toevoegen aan de variabele **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Voeg beveiliging=wapen** toe
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Sla het bestand op en sluit het af met CTRL+X en Y en enter. Voer vervolgens het volgende commando uit om de bootloaderconfiguratie van je systeem bij te werken:

```bash
sudo update-grub
```

Start ten slotte je systeem opnieuw op.

Zodra SELinux of AppArmor is ingeschakeld, kun je hun beleid configureren om de privileges van processen te beperken en hun toegang tot systeembronnen te beperken. Dit kan helpen om de potentiële impact van een succesvolle aanval te minimaliseren en de algehele beveiliging van je systeem te verbeteren.


### Wachtwoordbeleid configureren

Het configureren van wachtwoordbeleid is een belangrijke stap in het versterken van de beveiliging van uw Linux-systeem. Door sterke wachtwoordvereisten af te dwingen, kunt u ervoor zorgen dat gebruikersaccounts veilig zijn en beschermd tegen mogelijke aanvallen. Zo configureert u het wachtwoordbeleid op uw Linux-systeem:

#### Wachtwoordbeleid configureren op Ubuntu

Om het wachtwoordbeleid op Ubuntu te configureren, kun je de **pam_pwquality** module gebruiken. Deze module biedt een reeks wachtwoordsterktecontroles die kunnen worden gebruikt om het wachtwoordbeleid af te dwingen. Om de **pam_pwquality** module te installeren, open je een terminalvenster en typ je:

```bash
sudo apt-get install libpam-pwquality
```

Zodra de module is geïnstalleerd, kun je de instellingen aanpassen door het bestand **/etc/pam.d/common-password** te bewerken. Om bijvoorbeeld een minimale wachtwoordlengte van 8 tekens af te dwingen en ten minste één hoofdletter, één kleine letter, één cijfer en één speciaal teken te vereisen, kan de volgende regel aan het bestand worden toegevoegd:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

Je kunt ook andere instellingen configureren, zoals de maximale wachtwoordleeftijd, door regels toe te voegen aan het bestand.

#### Wachtwoordbeleid configureren op CentOS

Om het wachtwoordbeleid op CentOS te configureren, kun je het hulpprogramma **authconfig** gebruiken. Dit hulpprogramma biedt een set opties die kunnen worden gebruikt om het wachtwoordbeleid te configureren. Om bijvoorbeeld een minimale wachtwoordlengte van 8 tekens af te dwingen en ten minste één hoofdletter, één kleine letter, één cijfer en één speciaal teken te vereisen, kun je het volgende commando gebruiken:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Dit zal de **/etc/pam.d/system-auth** en **/etc/pam.d/password-auth** bestanden van het systeem bijwerken om het gespecificeerde wachtwoordbeleid af te dwingen.

Vergeet niet om uw wachtwoordbeleid regelmatig te herzien en bij te werken om ervoor te zorgen dat het effectief blijft tegen mogelijke aanvallen.


### Controleer uw systeemlogboeken

Het bijhouden van uw systeemlogs is een belangrijk aspect van het onderhouden van de beveiliging van uw Linux-systeem. Systeemlogs registreren systeemactiviteit, zoals mislukte aanmeldingspogingen, fouten en andere belangrijke gebeurtenissen, en kunnen waardevolle inzichten verschaffen in potentiële veiligheidsbedreigingen of andere problemen die aandacht vereisen. Hier lees je hoe je je systeemlogs kunt controleren:

#### Met behulp van de opdracht journalctl

Op de meeste moderne Linux distributies kun je het **journalctl** commando gebruiken om systeemlogs te bekijken. Dit commando biedt verschillende opties die kunnen worden gebruikt om logboekvermeldingen te filteren en te doorzoeken.

Om alle logboekvermeldingen te bekijken, voer je gewoon het volgende commando uit:

```bash
sudo journalctl
```

Dit geeft alle logboekvermeldingen weer, met de meest recente vermeldingen onderaan.

Om logboekvermeldingen te filteren op een specifieke eenheid, zoals een service of een proces, kun je de **-u** optie gebruiken gevolgd door de naam van de eenheid. Om bijvoorbeeld logboekvermeldingen voor de service **sshd** te bekijken, kun je het volgende commando uitvoeren:
```bash
sudo journalctl -u sshd
```


Om logboekvermeldingen op een specifiek tijdsbereik te filteren, kun je de opties **-ince** en **--until** gebruiken gevolgd door een tijdstempel of tijdsbereik. Om bijvoorbeeld logboekvermeldingen van het laatste uur te bekijken, kun je het volgende commando uitvoeren:

```bash
sudo journalctl --since "1 hour ago"
```

#### Een tool voor logboekbeheer gebruiken

Voor grotere of complexere systemen kan het nuttig zijn om een logbeheertool te gebruiken om systeemlogs te verzamelen en te analyseren. Hulpmiddelen voor logboekbeheer kunnen geavanceerde functies bieden, zoals realtime logboekbewaking, logboekaggregatie en logboekanalyse, en kunnen u helpen bij het efficiënter identificeren van en reageren op potentiële beveiligingsbedreigingen.

Voorbeelden van tools voor logboekbeheer voor Linux zijn

- **Logwatch**: een eenvoudig hulpmiddel voor loganalyse dat dagelijks per e-mail samenvattingen geeft van de systeemlogs.
- **Logrotate**: een tool die automatisch logbestanden roteert en comprimeert om schijfruimte te besparen
- **ELK stack**: een populaire open-source log management tool die Elasticsearch, Logstash en Kibana combineert om real-time log monitoring en analyse mogelijkheden te bieden.

Vergeet niet om uw systeemlogboeken regelmatig te controleren en te analyseren om potentiële beveiligingsrisico's tijdig te detecteren en erop te reageren.

______

## Don'ts:

### Gebruik zwakke wachtwoorden

Het gebruik van zwakke wachtwoorden is een veelgemaakte fout die je Linux-systeem kwetsbaar kan maken voor aanvallen. Aanvallers kunnen tools gebruiken om wachtwoorden te raden die gebaseerd zijn op gewone woorden, namen of datums. Het is belangrijk om sterke en unieke wachtwoorden te gebruiken die niet gemakkelijk te raden zijn.

Je kunt sterke wachtwoorden maken door een combinatie van hoofdletters en kleine letters, cijfers en speciale tekens te gebruiken. Het is ook een goed gebruik om een [password manager](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.com/articles/bitwarden-and-keepassxc-vs-the-rest/) kan je ook helpen om je wachtwoorden te onthouden en te voorkomen dat je hetzelfde wachtwoord voor meerdere accounts gebruikt.

### SSH-toegang voor root toestaan

Het toestaan van root SSH-toegang is een veiligheidsrisico dat aanvallers volledige controle over uw Linux-systeem kan geven. In plaats daarvan moet u een niet-root gebruikersaccount gebruiken om in te loggen op uw systeem en vervolgens de rechten verhogen met het **sudo** commando. Dit helpt om de potentiële impact van een aanval te beperken door de rechten van gebruikersaccounts te beperken.

### Onnodige software installeren

Het installeren van onnodige software kan het aanvalsoppervlak van uw Linux-systeem vergroten, waardoor het kwetsbaarder wordt voor aanvallen. Het is belangrijk om alleen software te installeren die noodzakelijk is voor uw systeem en overbodige software te verwijderen. Dit helpt om het aantal potentiële kwetsbaarheden op uw systeem te verminderen en het risico op een succesvolle aanval te minimaliseren.

### Verouderde software gebruiken

Het gebruik van verouderde software kan uw systeem kwetsbaar maken voor aanvallen die misbruik maken van bekende kwetsbaarheden. Het is belangrijk om altijd de laatste versie van software te gebruiken en deze regelmatig bij te werken om de veiligheid te garanderen. Dit helpt om bekende kwetsbaarheden te verhelpen en uw systeem te beschermen tegen mogelijke aanvallen.

______

## Conclusie

Samenvattend is het harden van je Linux systeem cruciaal om de veiligheid ervan te garanderen en de gegevens die erop staan te beschermen. Door de do's en don'ts in dit artikel te volgen, kun je belangrijke stappen nemen om je systeem te beveiligen en het risico op cyberbedreigingen te verkleinen. Vergeet niet om je systeem altijd up-to-date te houden, een firewall te gebruiken, wachtwoordbeleid in te stellen en systeemlogboeken te controleren. Vermijd het gebruik van zwakke wachtwoorden, het uitschakelen van automatische updates, root SSH-toegang toestaan, onnodige software installeren en verouderde software gebruiken. Met deze best practices in gedachten kun je ervoor zorgen dat je Linux systeem veilig en beschermd blijft.

## Referenties:

- [The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
- [Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
- [Ubuntu Security Documentation](https://ubuntu.com/security)
- [Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

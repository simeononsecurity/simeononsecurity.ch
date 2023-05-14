---
title: "Essentiële do's en don'ts voor het hardenen van uw Linux-systeem"
date: 2023-02-28
toc: true
draft: false
description: "Leer de essentiële do's en donts voor het harden van uw Linux-systeem, waaronder updaten, firewalls gebruiken, SELinux of AppArmor inschakelen, wachtwoordbeleid configureren en systeemlogs controleren."
tags: ["Linux beveiliging", "systeemverharding", "firewall", "SELinux", "AppArmor", "wachtwoordbeleid", "systeemupdates", "systeemlogboeken", "veiligheidsmodules", "toegangscontrolebeleid", "cyberbeveiliging", "systeemveiligheid", "netwerkbeveiliging", "beheer van kwetsbaarheden", "beste beveiligingspraktijken", "IT-beveiliging", "informatiebeveiliging", "software-updates", "worteltoegang", "wachtwoord manager"]
cover: "/img/cover/A_cartoon_lock_holding_a_shield_with_the_word_Linux_on_it.png"
coverAlt: "Een cartoonslot houdt een schild vast met het woord Linux erop, terwijl een pijl op het schild afketst."
coverCaption: ""
---


Linux is een populair besturingssysteem dat zowel door particulieren als bedrijven wordt gebruikt. Hoewel het door zijn open-source karakter vaak als veiliger wordt beschouwd dan andere besturingssystemen, vereist het nog steeds de juiste hardening om de veiligheid van het systeem en de gegevens die het bevat te waarborgen. In dit artikel zullen we enkele algemene do's en don'ts bespreken die kunnen helpen om uw Linux-systeem veilig te houden.

## Do's:

### Houd uw systeem bijgewerkt

Uw[Linux](https://simeononsecurity.ch/articles/how-do-i-learn-linux/) Het up-to-date houden van uw systeem is cruciaal voor de veiligheid ervan. Regelmatige updates helpen kwetsbaarheden en bugs te verhelpen, zodat uw systeem veilig blijft tegen mogelijke aanvallen. Hier volgen enkele voorbeelden van hoe u uw Linux-systeem kunt bijwerken met de **apt-get** of **yum** package manager:

#### Ubuntu bijwerken met apt-get

Om je Ubuntu systeem te updaten met **apt-get**, open je een terminal venster en typ je:
```bash
sudo apt-get update
```

Dit zal de laatste pakketlijsten downloaden van de Ubuntu-pakketrepositories. Zodra deze opdracht is voltooid, kunt u alle beschikbare updates installeren met de volgende opdracht:

```bash
sudo apt-get upgrade

```

Hiermee worden alle beschikbare updates voor uw systeem gedownload en geïnstalleerd.

### CentOS bijwerken met yum

Om uw CentOS-systeem bij te werken met **yum**, opent u een terminalvenster en typt u:

```bash
sudo yum update
```

Dit zal alle beschikbare updates voor uw systeem downloaden en installeren. U kunt ook het volgende commando gebruiken om oude of ongebruikte pakketten op te ruimen:

```bash
sudo yum autoremove
```

Dit zal alle pakketten verwijderen die niet langer nodig zijn op uw systeem.

Vergeet niet regelmatig te controleren op updates en deze te installeren op uw Linux-systeem om de veiligheid en stabiliteit ervan te garanderen.


### Gebruik een firewall

Een firewall is een essentiële beveiligingsmaatregel voor elk Linux-systeem, omdat hij helpt beschermen tegen ongeoorloofde toegang en andere cyberdreigingen. Hier leest u hoe u de **ufw** firewall op uw Linux-systeem gebruikt:

#### Installeren en inschakelen van ufw voor op Ubuntu gebaseerde systemen

Om **ufw** te installeren en in te schakelen, opent u een terminalvenster en typt u:

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

Om een regel te verwijderen:
```bash
sudo ufw delete <rule_number>
```

U kunt de huidige **ufw** regels bekijken door te typen:

```bash
sudo ufw status
```


Dit toont de huidige regels en hun status.

Vergeet niet uw **ufw** regels regelmatig te herzien en bij te werken om ervoor te zorgen dat uw systeem beschermd is tegen potentiële bedreigingen.


#### Firewalld installeren en inschakelen voor CentOS gebaseerde systemen

Om de standaard firewall op CentOS, **firewalld**, te installeren en in te schakelen, kunt u de volgende commando's gebruiken:

```bash
sudo yum install firewalld
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Dit zal **firewalld** installeren en inschakelen op uw systeem.

#### Configureren van firewalld regels voor CentOS gebaseerde systemen

Zodra **firewalld** is ingeschakeld, kunt u zijn regels configureren om inkomend en uitgaand verkeer toe te staan of te blokkeren. Hier zijn enkele voorbeelden:

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

Om een regel te verwijderen:

```bash
sudo firewall-cmd --permanent --remove-<type>=<rule>
sudo firewall-cmd --reload
```

U kunt de huidige **firewalld** regels bekijken door te typen:

```bash
sudo firewall-cmd --list-all
```

Dit toont de huidige regels en hun status.

Vergeet niet uw **firewalld** regels regelmatig te herzien en bij te werken om ervoor te zorgen dat uw systeem

### SELinux of AppArmor inschakelt

SELinux (Security-Enhanced Linux) en AppArmor zijn twee beveiligingsmodules die gebruikt kunnen worden om een verplicht toegangscontrolebeleid in Linux systemen af te dwingen. De meeste moderne Linux-distributies worden standaard geleverd met SELinux of AppArmor geïnstalleerd, en ze kunnen worden ingeschakeld en geconfigureerd om de beveiliging van uw systeem te verbeteren.

#### SELinux inschakelen voor CentOS gebaseerde systemen

Om te controleren of SELinux op uw systeem is ingeschakeld, voert u het volgende commando uit:

```bash
sestatus
```

Als SELinux niet is geïnstalleerd, kunt u het met het volgende commando installeren:

```bash
sudo yum install selinux-policy selinux-policy-targeted
```

Om SELinux in te schakelen, moet u het bestand **/etc/selinux/config** bewerken en de variabele **SELINUX** instellen op **versterken**:

```bash
sudo nano /etc/selinux/config
```
**Wijzig SELINUX=dwingend**
```
SELINUX=enforcing
```

Sla het bestand op en sluit het af met CTRL+X en Y dan enter, en herstart uw systeem.

#### AppArmor inschakelen voor op Ubuntu gebaseerde systemen

Om te controleren of AppArmor op uw systeem is ingeschakeld, voert u het volgende commando uit:
```bash
sudo apparmor_status
```


Als AppArmor niet is geïnstalleerd, kunt u het installeren met het volgende commando:
```bash
sudo apt-get install apparmor
```

Om AppArmor in te schakelen, moet u het bestand **/etc/default/grub** bewerken en de parameter **security=apparmor** toevoegen aan de variabele **GRUB_CMDLINE_LINUX**:

```bash
sudo nano /etc/default/grub
```
**Voeg beveiliging toe=apparmor**
```bash
GRUB_CMDLINE_LINUX="... security=apparmor"
```

Sla het bestand op en sluit het af met CTRL+X en Y en voer vervolgens het volgende commando uit om de bootloaderconfiguratie van uw systeem bij te werken:

```bash
sudo update-grub
```

Start tenslotte uw systeem opnieuw op.

Zodra SELinux of AppArmor is ingeschakeld, kunt u hun beleid configureren om de privileges van processen te beperken en hun toegang tot systeembronnen te beperken. Dit kan helpen de potentiële impact van een succesvolle aanval te minimaliseren en de algehele beveiliging van uw systeem te verbeteren.


### Wachtwoordbeleid configureren

Het configureren van wachtwoordbeleid is een belangrijke stap in het versterken van de beveiliging van uw Linux-systeem. Door sterke wachtwoordvereisten af te dwingen, kunt u ervoor zorgen dat gebruikersaccounts veilig en beschermd zijn tegen mogelijke aanvallen. Zo configureert u het wachtwoordbeleid op uw Linux-systeem:

#### Wachtwoordbeleid configureren op Ubuntu

Om het wachtwoordbeleid op Ubuntu te configureren, kunt u de **pam_pwquality** module gebruiken. Deze module biedt een reeks wachtwoordsterktecontroles die kunnen worden gebruikt om het wachtwoordbeleid af te dwingen. Om de **pam_pwquality** module te installeren, opent u een terminalvenster en typt u:

```bash
sudo apt-get install libpam-pwquality
```

Zodra de module is geïnstalleerd, kunt u de instellingen ervan configureren door het bestand **/etc/pam.d/common-password** te bewerken. Om bijvoorbeeld een minimale wachtwoordlengte van 8 tekens af te dwingen en ten minste één hoofdletter, één kleine letter, één cijfer en één speciaal teken te vereisen, kunt u de volgende regel aan het bestand toevoegen:

```bash
password requisite pam_pwquality.so minlen=8 ucredit=-1 lcredit=-1 dcredit=-1 ocredit=-1
```

U kunt ook andere instellingen configureren, zoals de maximale wachtwoordleeftijd, door regels aan het bestand toe te voegen.

#### Wachtwoordbeleid configureren op CentOS

Om het wachtwoordbeleid op CentOS te configureren, kunt u het hulpprogramma **authconfig** gebruiken. Deze tool biedt een reeks opties die kunnen worden gebruikt om het wachtwoordbeleid te configureren. Om bijvoorbeeld een minimale wachtwoordlengte van 8 tekens af te dwingen en ten minste één hoofdletter, één kleine letter, één cijfer en één speciaal teken te vereisen, kunt u het volgende commando gebruiken:

```bash
sudo authconfig --passalgo=sha512 --update --enablereqlower --enablerequpper --enablereqdigit --enablereqother --passminlen=8
```

Dit zal de **/etc/pam.d/system-auth** en **/etc/pam.d/password-auth** bestanden van het systeem bijwerken om het gespecificeerde wachtwoordbeleid af te dwingen.

Vergeet niet uw wachtwoordbeleid regelmatig te herzien en bij te werken, zodat het effectief blijft tegen mogelijke aanvallen.


### Controleer uw systeemlogboeken

Het controleren van uw systeemlogs is een belangrijk aspect van het onderhouden van de beveiliging van uw Linux-systeem. Systeemlogs registreren systeemactiviteit, zoals mislukte aanmeldingspogingen, fouten en andere belangrijke gebeurtenissen, en kunnen waardevolle inzichten verschaffen in potentiële veiligheidsbedreigingen of andere problemen die aandacht vereisen. Hier leest u hoe u uw systeemlogs kunt controleren:

#### Met behulp van het commando journalctl

Op de meeste moderne Linux distributies kunt u het **journalctl** commando gebruiken om systeemlogs te bekijken. Dit commando biedt een aantal opties die kunnen worden gebruikt om logboekvermeldingen te filteren en te doorzoeken.

Voer het volgende commando uit om alle logboekvermeldingen te bekijken:

```bash
sudo journalctl
```

Dit toont alle logboekvermeldingen, met de meest recente vermeldingen onderaan.

Om logboekvermeldingen te filteren op een specifieke eenheid, zoals een service of een proces, kunt u de optie **-u** gebruiken gevolgd door de naam van de eenheid. Om bijvoorbeeld logboekvermeldingen voor de service **sshd** te bekijken, kunt u het volgende commando uitvoeren:
```bash
sudo journalctl -u sshd
```


Om logboekvermeldingen te filteren op een specifiek tijdsbereik, kunt u de opties **- sinds** en **- tot** gebruiken, gevolgd door een tijdstempel of tijdsbereik. Om bijvoorbeeld logboekvermeldingen van het laatste uur te bekijken, kunt u het volgende commando uitvoeren:

```bash
sudo journalctl --since "1 hour ago"
```

#### Een tool voor logboekbeheer gebruiken

Voor grotere of complexere systemen kan het nuttig zijn om een tool voor logboekbeheer te gebruiken om systeemlogs te verzamelen en te analyseren. Hulpmiddelen voor logboekbeheer kunnen geavanceerde functies bieden, zoals real-time logbewaking, logboekaggregatie en logboekanalyse, en kunnen u helpen potentiële beveiligingsrisico's efficiënter te identificeren en erop te reageren.

Voorbeelden van tools voor logboekbeheer voor Linux zijn:

- **Logwatch**: een eenvoudig hulpmiddel voor loganalyse dat dagelijks per e-mail samenvattingen geeft van de systeemlogs.
- **Logrotate**: een tool die automatisch logbestanden roteert en comprimeert om schijfruimte te besparen.
- **ELK stack**: een populaire open-source log management tool die Elasticsearch, Logstash en Kibana combineert voor real-time log monitoring en analyse mogelijkheden.

Vergeet niet om uw systeemlogs regelmatig te controleren en te analyseren om potentiële beveiligingsrisico's tijdig op te sporen en erop te reageren.

______

## Don'ts:

### Gebruik zwakke wachtwoorden

Het gebruik van zwakke wachtwoorden is een veelgemaakte fout die uw Linux-systeem kwetsbaar kan maken voor aanvallen. Aanvallers kunnen tools gebruiken om wachtwoorden te raden die gebaseerd zijn op gewone woorden, namen of data. Het is belangrijk om sterke en unieke wachtwoorden te gebruiken die niet gemakkelijk te raden zijn.

U kunt sterke wachtwoorden maken door een combinatie van hoofdletters en kleine letters, cijfers en speciale tekens te gebruiken. Het is ook een goed gebruik om een[password manager](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) to generate and store complex passwords securely. [Password managers](https://simeononsecurity.ch/articles/bitwarden-and-keepassxc-vs-the-rest/) kan u ook helpen uw wachtwoorden te onthouden en te voorkomen dat u hetzelfde wachtwoord gebruikt voor meerdere accounts.

### Sta root SSH-toegang toe

Het toestaan van root SSH-toegang is een veiligheidsrisico dat aanvallers volledige controle over uw Linux-systeem kan geven. In plaats daarvan moet u een niet-root gebruikersaccount gebruiken om in te loggen op uw systeem en vervolgens de rechten verhogen met het **sudo** commando. Dit helpt de potentiële impact van een aanval te beperken door de rechten van gebruikersaccounts te beperken.

### Onnodige software installeren

Het installeren van onnodige software kan het aanvalsoppervlak van uw Linux-systeem vergroten, waardoor het kwetsbaarder wordt voor aanvallen. Het is belangrijk om alleen software te installeren die noodzakelijk is voor uw systeem en overbodige software te verwijderen. Dit helpt het aantal potentiële kwetsbaarheden op uw systeem te verminderen en het risico van een succesvolle aanval te minimaliseren.

### Gebruik verouderde software

Het gebruik van verouderde software kan uw systeem kwetsbaar maken voor aanvallen die misbruik maken van bekende kwetsbaarheden. Het is belangrijk om altijd de laatste versie van software te gebruiken en deze regelmatig bij te werken om de veiligheid te waarborgen. Dit helpt om bekende kwetsbaarheden te verhelpen en uw systeem te beschermen tegen mogelijke aanvallen.

______

## Conclusie

Kortom, het harden van uw Linux-systeem is van cruciaal belang om de veiligheid ervan te garanderen en de gegevens die erin staan te beschermen. Door de do's en don'ts uit dit artikel te volgen, kunt u belangrijke stappen nemen om uw systeem te beveiligen en het risico van cyberdreigingen te verminderen. Houd uw systeem altijd up-to-date, gebruik een firewall, configureer wachtwoordbeleid en controleer systeemlogboeken. Vermijd het gebruik van zwakke wachtwoorden, het uitschakelen van automatische updates, het verlenen van root SSH-toegang, het installeren van onnodige software en het gebruik van verouderde software. Met deze best practices in gedachten kunt u ervoor zorgen dat uw Linux-systeem veilig en beschermd blijft.

## Referenties:

-[The Center for Internet Security's Linux Hardening Guide](https://www.cisecurity.org/cis-hardened-images/)
-[Red Hat Enterprise Linux Security Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/index)
-[Ubuntu Security Documentation](https://ubuntu.com/security)
-[Linux Security Wiki](https://en.wikibooks.org/wiki/Linux_Security)

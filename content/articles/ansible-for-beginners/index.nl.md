---
title: "Inleiding tot Ansible: Automatisering van het beheer van de IT-infrastructuur"
draft: false
toc: true
date: 2023-02-25
description: "Leer de basis van Ansible, een open-source automatiseringstool die het beheer van de IT-infrastructuur vereenvoudigt door middel van een declaratieve taal."
tags: ["Inleiding tot Ansible", "Automatisering van het beheer van de IT-infrastructuur", "Ansible grondbeginselen", "Automatisering van de IT-infrastructuur", "Configuratiebeheer", "Inzet van toepassingen", "Voorziening", "Continue levering", "Naleving van de veiligheidsvoorschriften", "Orkestratie", "YAML", "Ansible modules", "Rollen", "Beste praktijken", "Versiebeheer", "Testen", "Rode Hoed", "Systeembeheerders", "Linux", "macOS", "Windows", "Ansible installatie", "Ansible inventaris", "Ansible playbooks", "Ansible modules", "Ansible rollen", "Ansible best practices", "Ansible testen", "IT-infrastructuurautomatiseringstool", "Ansible handleiding", "Automatisering van het infrastructuurbeheer"]
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "Een stripfiguur zit aan een bureau, omringd door servers en kabels, met het logo van Ansible op het computerscherm, en lacht terwijl taken worden geautomatiseerd."
coverCaption: ""
---

Ansible is een open-source automatiseringstool waarmee systeembeheerders het beheer van de IT-infrastructuur kunnen automatiseren. Het biedt een eenvoudige taal om de gewenste toestand van de infrastructuur te beschrijven, en dwingt die toestand automatisch af. Dit vermindert de tijd en moeite die nodig zijn om grootschalige, complexe systemen te beheren.

Dit artikel geeft een inleiding tot Ansible, inclusief de basisconcepten en hoe u ermee aan de slag kunt.

## Inleiding tot Ansible

Ansible werd in 2012 ontwikkeld door Michael DeHaan en in 2015 overgenomen door Red Hat. Sindsdien is het een van de populairste automatiseringstools in de industrie geworden.

Ansible gebruikt een eenvoudige, declaratieve taal genaamd YAML (kort voor "YAML Ain't Markup Language") om de gewenste staat van de infrastructuur te definiëren. Dit maakt het gemakkelijk te lezen en te begrijpen, zelfs voor niet-programmeurs.

Ansible kan worden gebruikt om een breed scala aan taken te automatiseren, waaronder:

- **Configuratiebeheer**
- **Applicatie implementatie**
- **Continue levering**
- **Provisioning**
- **Security compliance**
- **Orchestratie**

## Aan de slag met Ansible

Om met Ansible te beginnen, moet u het op uw systeem installeren. Ansible kan worden geïnstalleerd op een groot aantal besturingssystemen, waaronder Linux, macOS en Windows.

Om Ansible te installeren op Linux, in dit geval Ubuntu, kunt u de volgende commando's gebruiken:
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
Anders kunt u de volgende gidsen gebruiken om ansible te installeren:
- [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

Zodra Ansible is geïnstalleerd, kunt u controleren of het werkt door het volgende commando uit te voeren:
```bash
ansible --version
```

Dit zou de versie van Ansible moeten weergeven die u hebt geïnstalleerd.

## Ansible Inventaris

De eerste stap in het gebruik van Ansible is het definiëren van een inventaris. Een inventaris is een lijst van servers die Ansible zal beheren. Een inventaris kan worden gedefinieerd in verschillende formaten, waaronder INI, YAML en JSON.

Hier is een voorbeeld van een inventarisbestand in INI formaat:

```ini
[webservers]
webserver1.example.com
webserver2.example.com

[databases]
dbserver1.example.com
dbserver2.example.com
```

Dit inventarisbestand definieert twee groepen servers, "webservers" en "databases", en vermeldt de hostnamen van de servers in elke groep.

## Ansible Playbooks

Zodra u een inventaris heeft gedefinieerd, is de volgende stap het definiëren van een playbook. Een playbook is een YAML-bestand dat een reeks taken beschrijft die Ansible moet uitvoeren op de servers in de inventaris.

Hier is een voorbeeld van een eenvoudig playbook:
```yml
name: Install Nginx
hosts: webservers
become: yes

tasks:
    - name: Install Nginx package
        apt:
        name: nginx
        state: present
```

Dit playbook installeert de Nginx webserver op alle servers in de groep "webservers".

De `hosts` parameter geeft aan op welke groep servers het playbook moet worden uitgevoerd. De `become` parameter geeft aan dat de taken moeten worden uitgevoerd met verhoogde rechten (met behulp van `sudo` of `su`

De `tasks` sectie noemt de individuele taken die het playbook moet uitvoeren. In dit geval is er slechts één taak, die het Nginx-pakket installeert met behulp van de `apt` module.

## Ansible Modules

Ansible modules zijn herbruikbare eenheden van code die gebruikt kunnen worden om specifieke taken uit te voeren. Ansible wordt geleverd met een groot aantal ingebouwde modules, en er zijn ook veel modules van derden beschikbaar.

Hier zijn enkele voorbeelden van ingebouwde modules:

- `apt` - Beheer pakketten op Debian-gebaseerde systemen
- `yum` - Beheer pakketten op Red Hat-gebaseerde systemen
- `file` - Bestanden beheren
- `service` - Systeemdiensten beheren
- `user` - Gebruikers en groepen beheren
- `copy` - Bestanden kopiëren van de controlemachine naar de beheerde servers

Een volledige lijst van ingebouwde modules vindt u in de [Ansible documentation](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Ansible Rollen en Map Structuur

Een Ansible rol is een manier om gemeenschappelijke taken en configuraties te organiseren en te hergebruiken. Het is een mappenstructuur die taken, handlers, sjablonen, bestanden en andere bronnen bevat.

Hier is een voorbeeld van een eenvoudige Ansible rol voor het installeren en configureren van Nginx:
```
roles/
└── nginx/
    ├── tasks/
    │   ├── main.yml
    ├── handlers/
    │   ├── main.yml
    ├── templates/
    │   ├── nginx.conf.j2
    ├── files/
    ├── vars/
    ├── defaults/
    ├── meta/
```
In dit voorbeeld is de nginx rol een directory die verschillende subdirectories bevat, die elk een specifiek doel dienen:

- **tasks**: bevat de taken die door de rol zullen worden uitgevoerd.
- **handlers**: bevat de handlers die de taken kunnen melden.
- **templates**: bevat de Jinja2 templates die zullen worden gebruikt om de configuratiebestanden voor Nginx te genereren.
- **files**: bevat alle statische bestanden die de rol nodig heeft.
- **vars**: bevat variabelen die specifiek zijn voor de rol.
- **defaults**: bevat standaardvariabelen voor de rol.
- **meta**: bevat metadata over de rol, zoals zijn afhankelijkheden.

Rollen kunnen gemakkelijk worden gedeeld en hergebruikt in meerdere playbooks en projecten.

Hier is een voorbeeld van een main.yml bestand in de tasks directory:
```yaml
---
- name: Install Nginx
  apt:
    name: nginx
    state: present
  notify: restart nginx

- name: Enable Nginx
  systemd:
    name: nginx
    enabled: yes
    state: started
```

Deze taak installeert Nginx met behulp van de apt-module en schakelt de Nginx-service in en start deze met behulp van de systemd-module. Het meldt ook de restart nginx handler, die Nginx herstart als er wijzigingen in de configuratie zijn aangebracht.

Het gebruik van een Ansible-rol als deze kan het proces van beheer en configuratie van software op meerdere servers of omgevingen vereenvoudigen. Door de taken, handlers, sjablonen en andere middelen in een enkele mapstructuur te scheiden, kunt u deze componenten gemakkelijker beheren en hergebruiken in verschillende playbooks en projecten.

## Beste praktijken voor Ansible

Hier volgen enkele best practices voor het gebruik van Ansible:

### 1. Gebruik versiecontrole

Het opslaan van uw Ansible playbooks en rollen in een versiebeheersysteem zoals Git is een best practice die u kan helpen wijzigingen bij te houden en samen te werken met anderen. Versiebeheer biedt een geschiedenis van wijzigingen in uw codebase, zodat u indien nodig terug kunt gaan naar eerdere versies. Het maakt het ook gemakkelijk om met anderen samen te werken door code te delen en conflicten te beheren.

### 2. Gebruik rollen om uw Playbooks te organiseren

Rollen zijn een krachtige manier om uw Ansible playbooks en taken te organiseren. Door gerelateerde taken te groeperen in rollen, kunt u uw playbooks modulairder en herbruikbaarder maken. Rollen maken het ook gemakkelijk om code te delen tussen verschillende projecten.

Hier is een voorbeeld van een playbook dat een rol gebruikt om Nginx te installeren en te configureren:

```yml
name: Install and configure Nginx
hosts: webservers
become: yes
roles:
  - nginx
```

Dit playbook gebruikt een rol genaamd "nginx" om Nginx te installeren en te configureren op de "webservers" groep van hosts.

### 3. Tags gebruiken om taken te groeperen

Tags kunnen worden gebruikt om gerelateerde taken te groeperen in uw Ansible playbooks. Dit maakt het gemakkelijker om specifieke delen van een playbook uit te voeren, vooral wanneer u met grote, complexe playbooks werkt.

Hier volgt een voorbeeld van het gebruik van tags in een Ansible playbook:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes
tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
    tags: nginx_install

  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    tags: nginx_config
```

Dit playbook heeft twee taken, één voor het installeren van Nginx en één voor het configureren van Nginx. Aan elke taak is een tag gekoppeld, zodat het gemakkelijk is om alleen de taken uit te voeren die nodig zijn.

### 4. Variabelen gebruiken om Playbooks flexibeler te maken

Variabelen kunnen worden gebruikt om uw Ansible playbooks flexibeler en herbruikbaarder te maken. Door variabelen te gebruiken, kunt u uw playbooks generieker maken en aanpassen aan verschillende omgevingen.

Hier volgt een voorbeeld van het gebruik van variabelen in een Ansible playbook:
```yml
name: Install and configure Nginx
hosts: webservers
become: yes

vars:
nginx_port: 80
nginx_user: www-data

tasks:
  - name: Install Nginx
    apt:
    name: nginx
    state: present
  - name: Configure Nginx
    template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
    notify: restart nginx

handlers:
  - name: restart nginx
    service:
    name: nginx
    state: restarted
```

Dit playbook gebruikt variabelen om de poort te specificeren waarop Nginx moet luisteren en de gebruiker die Nginx moet draaien. Dit maakt het playbook flexibeler en aanpasbaar aan verschillende omgevingen.

### 5. Uw playbooks testen

Het testen van uw Ansible playbooks is een best practice die u kan helpen fouten op te vangen en ervoor te zorgen dat uw playbooks werken zoals verwacht. Een populaire tool voor het testen van Ansible playbooks is Molecule.

Molecule is een test framework waarmee u uw playbooks op een consistente en geautomatiseerde manier kunt testen. Molecule kan virtuele machines creëren, uw playbook toepassen en vervolgens controleren of alles werkt zoals verwacht. Dit kan u helpen bij het opsporen van fouten en ervoor zorgen dat uw playbooks correct werken voordat u ze uitrolt naar productie.

Hier is een voorbeeld van hoe u Molecule kunt gebruiken om een Ansible-rol te testen:

```bash
molecule init role myrole
cd myrole
molecule test
```

## Conclusie

In dit artikel hebben we Ansible geïntroduceerd, een krachtige automatiseringstool waarmee u complexe IT-infrastructuur kunt beheren. We hebben de basisconcepten van Ansible behandeld, waaronder inventarissen, playbooks, modules en rollen.

We hebben ook best practices voor het gebruik van Ansible besproken, waaronder het gebruik van versiebeheer, het organiseren van playbooks met rollen, het gebruik van tags en variabelen, en het testen van uw playbooks.

Als u nieuw bent met Ansible, raden wij u aan te beginnen met wat eenvoudige playbooks en geleidelijk uw vaardigheden en kennis op te bouwen. Met oefening zult u zelfs de meest complexe infrastructuurtaken met gemak kunnen automatiseren!

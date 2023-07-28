---
title: "Introducere în Ansible: Automatizarea gestionării infrastructurii IT"
draft: false
toc: true
date: 2023-02-25
description: "Învățați elementele de bază ale Ansible, un instrument de automatizare open-source care simplifică gestionarea infrastructurii IT printr-un limbaj declarativ."
tags: ["Introducere în Ansible", "Automatizarea managementului infrastructurii IT", "Bazele Ansible", "Automatizarea infrastructurii IT", "Managementul configurației", "Implementarea aplicației", "Aprovizionare", "Livrare continuă", "Conformitatea în materie de securitate", "Orchestrare", "YAML", "Module Ansible", "Roluri", "Cele mai bune practici", "Controlul versiunilor", "Testare", "Red Hat", "Administratori de sistem", "Linux", "macOS", "Windows", "Instalarea Ansible", "Inventar Ansible", "Ansible playbooks", "Module Ansible", "Roluri Ansible", "Cele mai bune practici Ansible", "Testarea Ansible", "Instrument de automatizare a infrastructurii IT", "Tutorial Ansible", "Automatizarea gestionării infrastructurii"]
cover: "/img/cover/A_cartoon_character_sitting_at_a_desk_surrounded_by_servers.png"
coverAlt: "Un personaj de desene animate care stă la un birou, înconjurat de servere și cabluri, cu logo-ul Ansible pe ecranul computerului, zâmbind în timp ce sarcinile sunt automatizate."
coverCaption: ""
---

Ansible este un instrument de automatizare open-source care permite administratorilor de sistem să automatizeze gestionarea infrastructurii IT. Acesta oferă un limbaj simplu pentru a descrie starea dorită a infrastructurii și impune automat această stare. Acest lucru reduce timpul și efortul necesar pentru a gestiona sisteme complexe, la scară largă.

Dacă sunteți nou în Ansible, acest articol vă va oferi o introducere în acest instrument, inclusiv conceptele sale de bază și modul în care puteți începe să îl utilizați.

## Introducere în Ansible

Ansible a fost dezvoltat de Michael DeHaan în 2012 și achiziționat de Red Hat în 2015. De atunci, a devenit unul dintre cele mai populare instrumente de automatizare din industrie.

{{< youtube id="goclfp6a2IQ" >}}

Ansible utilizează un limbaj simplu, declarativ numit YAML (prescurtare de la "YAML Ain't Markup Language") pentru a defini starea dorită a infrastructurii. Acest lucru îl face ușor de citit și de înțeles, chiar și pentru cei care nu sunt programatori.

Ansible poate fi folosit pentru a automatiza o gamă largă de sarcini, inclusiv:

- **Managementul configurației**
- **Dezvoltarea aplicațiilor**
- Livrarea continuă**
- Aprovizionarea.
- Conformitate în materie de securitate**
- Orcestrare

## Noțiuni de bază pentru a începe cu Ansible

Pentru a începe cu Ansible, va trebui să îl instalați pe sistemul dumneavoastră. Ansible poate fi instalat pe o gamă largă de sisteme de operare, inclusiv Linux, macOS și Windows.

Pentru a instala Ansible pe Linux, în acest caz Ubuntu, puteți utiliza următoarele comenzi:
```bash
sudo apt-get update
sudo apt-get install ansible -y
```
În caz contrar, puteți utiliza următoarele ghiduri pentru a instala ansible:
- [Installing Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

După ce Ansible este instalat, puteți verifica dacă funcționează executând următoarea comandă:
```bash
ansible --version
```

Aceasta ar trebui să afișeze versiunea de Ansible pe care ați instalat-o.

## Inventarul Ansible

Primul pas în utilizarea Ansible este să definiți un inventar. Un inventar este o listă de servere pe care Ansible le va gestiona. Un inventar poate fi definit într-o varietate de formate, inclusiv INI, YAML și JSON.

Iată un exemplu de fișier de inventar în format INI:

```ini
[webservers]
webserver1.example.com
webserver2.example.com

[databases]
dbserver1.example.com
dbserver2.example.com
```

Acest fișier de inventar definește două grupuri de servere, "webservere" și "baze de date", și enumeră numele de gazdă ale serverelor din fiecare grup.

## Ansible Playbooks

După ce ați definit un inventar, următorul pas este să definiți un playbook. Un playbook este un fișier YAML care descrie un set de sarcini pe care Ansible ar trebui să le execute pe serverele din inventar.

Iată un exemplu de playbook simplu:
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

Această carte de redare instalează serverul web Nginx pe toate serverele din grupul "webservers".

Adresa `hosts` specifică grupul de servere pe care trebuie să fie rulat manualul de redare. Parametrul `become` specifică faptul că sarcinile ar trebui să fie rulate cu privilegii ridicate (folosind `sudo` sau `su`

The `tasks` secțiunea enumeră sarcinile individuale pe care trebuie să le îndeplinească registrul de redare. În acest caz, există doar o singură sarcină, care instalează pachetul Nginx utilizând comanda `apt` modul.

## Module Ansible

Modulele Ansible sunt unități reutilizabile de cod care pot fi utilizate pentru a efectua sarcini specifice. Ansible vine cu o gamă largă de module încorporate și există, de asemenea, multe module de la terți disponibile.

Iată câteva exemple de module încorporate:

- `apt` - Gestionați pachetele pe sistemele bazate pe Debian
- `yum` - Gestionați pachetele pe sistemele bazate pe Red Hat
- `file` - Gestionați fișierele
- `service` - Gestionarea serviciilor de sistem
- `user` - Gestionați utilizatorii și grupurile
- `copy` - Copierea fișierelor de pe mașina de control pe serverele administrate

Puteți găsi o listă completă a modulelor încorporate în secțiunea [Ansible documentation](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Roluri Ansible și structura dosarelor Ansible

Un rol Ansible este o modalitate de a organiza și reutiliza sarcinile și configurațiile comune. Este o structură de directoare care conține sarcini, gestionari, șabloane, fișiere și alte resurse.

Iată un exemplu de rol Ansible simplu pentru instalarea și configurarea Nginx:
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
În acest exemplu, rolul nginx este un director care conține mai multe subdirectoare, fiecare dintre acestea având un scop specific:

- **tasks**: conține sarcinile care vor fi executate de către rol.
- **handlers**: conține gestionarii pe care sarcinile îi pot notifica.
- **templates**: conține șabloanele Jinja2 care vor fi utilizate pentru a genera fișierele de configurare pentru Nginx.
- **files**: conține toate fișierele statice de care are nevoie rolul.
- **vars**: conține variabilele care sunt specifice rolului.
- **defaults**: conține variabilele implicite pentru rol.
- **meta**: conține metadate despre rol, cum ar fi dependențele sale.

Rolurile pot fi ușor partajate și reutilizate în mai multe manuale de joc și proiecte.

Iată un exemplu de fișier main.yml din directorul tasks:
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

Această sarcină instalează Nginx folosind modulul apt și activează și pornește serviciul Nginx folosind modulul systemd. De asemenea, notifică administratorul restart nginx, care va reporni Nginx în cazul în care au fost efectuate modificări în configurație.

Utilizarea unui rol Ansible ca acesta poate simplifica procesul de gestionare și configurare a software-ului pe mai multe servere sau medii. Prin separarea sarcinilor, a gestionarilor, a șabloanelor și a altor resurse într-o singură structură de directoare, puteți gestiona și reutiliza mai ușor aceste componente în diferite playbook-uri și proiecte.

## Cele mai bune practici pentru Ansible

Iată câteva bune practici de urmat atunci când utilizați Ansible:

### 1. Utilizați controlul versiunilor

Stocarea cărților de joc și a rolurilor Ansible într-un sistem de control al versiunilor, cum ar fi Git, este o bună practică care vă poate ajuta să țineți evidența modificărilor și să colaborați cu alții. Controlul versiunilor oferă un istoric al modificărilor aduse bazei dvs. de cod, permițându-vă să reveniți la versiunile anterioare, dacă este necesar. De asemenea, facilitează colaborarea cu alții prin partajarea codului și gestionarea conflictelor.

### 2. Utilizați roluri pentru a vă organiza manualele de joc

Rolurile sunt o modalitate puternică de a vă organiza playbook-urile și sarcinile Ansible. Prin gruparea sarcinilor conexe în roluri, puteți face ca playbook-urile dvs. să fie mai modulare și reutilizabile. Rolurile facilitează, de asemenea, partajarea codului între diferite proiecte.

Iată un exemplu de playbook care utilizează un rol pentru a instala și configura Nginx:

```yml
name: Install and configure Nginx
hosts: webservers
become: yes
roles:
  - nginx
```

Acest manual de execuție utilizează un rol numit "nginx" pentru a instala și configura Nginx pe grupul de gazde "webservers".

### 3. Utilizați etichete pentru a grupa sarcinile

Etichetele pot fi utilizate pentru a grupa sarcini conexe în playbook-urile Ansible. Acest lucru facilitează rularea unor părți specifice ale unui playbook, în special atunci când lucrați cu playbook-uri mari și complexe.

Iată un exemplu de utilizare a etichetelor într-un registru de execuție Ansible:
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

Acest playbook are două sarcini, una pentru instalarea Nginx și una pentru configurarea Nginx. Fiecare sarcină are o etichetă asociată, ceea ce facilitează rularea doar a sarcinilor necesare.

### 4. Utilizați variabile pentru a face playbook-urile mai flexibile

Variabilele pot fi utilizate pentru a face ca playbook-urile Ansible să fie mai flexibile și reutilizabile. Prin utilizarea variabilelor, puteți face ca playbook-urile dvs. să fie mai generice și mai adaptabile la diferite medii.

Iată un exemplu de utilizare a variabilelor într-un playbook Ansible:
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

Această carte de redare utilizează variabile pentru a specifica portul pe care Nginx trebuie să asculte și utilizatorul care trebuie să ruleze Nginx. Acest lucru face ca playbook-ul să fie mai flexibil și adaptabil la diferite medii.

### 5. Testați-vă playbook-urile

Testarea playbook-urilor Ansible este o bună practică care vă poate ajuta să depistați erorile și să vă asigurați că playbook-urile dvs. funcționează conform așteptărilor. Un instrument popular pentru testarea playbook-urilor Ansible este Molecule.

Molecule este un cadru de testare care vă permite să vă testați playbook-urile într-un mod coerent și automatizat. Molecule poate crea mașini virtuale, vă poate aplica playbook-ul și apoi poate verifica dacă totul funcționează conform așteptărilor. Acest lucru vă poate ajuta să depistați erorile și să vă asigurați că playbook-urile dvs. funcționează corect înainte de a le implementa în producție.

Iată un exemplu de utilizare a Molecule pentru a testa un rol Ansible:

```bash
molecule init role myrole
cd myrole
molecule test
```

## Concluzie

În acest articol, am prezentat Ansible, un instrument de automatizare puternic care vă poate ajuta să gestionați o infrastructură IT complexă. Am acoperit conceptele de bază ale Ansible, inclusiv inventarele, playbook-urile, modulele și rolurile.

Am discutat, de asemenea, despre cele mai bune practici de utilizare a Ansible, inclusiv utilizarea controlului versiunilor, organizarea playbook-urilor cu roluri, utilizarea etichetelor și variabilelor și testarea playbook-urilor.

Dacă sunteți nou în Ansible, vă recomandăm să începeți prin a experimenta cu câteva playbook-uri simple și să vă dezvoltați treptat, în timp, abilitățile și cunoștințele. Cu ajutorul practicii, veți putea automatiza cu ușurință chiar și cele mai complexe sarcini de infrastructură!

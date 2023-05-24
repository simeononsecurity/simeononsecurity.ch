---
title: "Automatització de pedaços i actualitzacions de Linux amb Ansible: una guia completa"
date: 2023-05-28
toc: true
draft: false
description: "Obteniu informació sobre com automatitzar els pedaços i les actualitzacions de Linux mitjançant Ansible, que cobreix diverses distribucions i instruccions de configuració."
tags: ["Pedaços de Linux", "Automatització Ansible", "automatitzar les actualitzacions", "manteniment del sistema", "automatització informàtica", "gestió de pegats", "Seguretat Linux", "Debian", "Ubuntu", "RHEL", "alpí", "estabilitat del sistema", "mitigació de la vulnerabilitat", "infraestructura informàtica", "eina d'automatització", "Llibre de jugades Ansible", "configuració de l'amfitrió", "actualitzacions de programari", "compliment de seguretat", "operacions de TI", "Actualitzacions de Linux", "Ubuntu", "Debian", "CentOS", "RHEL", "actualitzacions fora de línia", "repositori local", "memòria cau", "configuració del servidor", "configuració del client", "mirall apte", "debmirror", "crearrepo", "apt-cacher-ng", "yum-cron", "Actualitzacions del sistema Linux", "actualitzacions de paquets fora de línia", "actualitzacions de programari fora de línia", "dipòsit local de paquets", "memòria cau de paquets locals", "actualitzacions fora de línia de Linux", "gestionar les actualitzacions fora de línia", "mètodes d'actualització fora de línia", "manteniment del sistema fora de línia", "Actualitzacions del servidor Linux", "Actualitzacions del client Linux", "gestió de programari fora de línia", "gestió de paquets fora de línia", "estratègies d'actualització", "Actualitzacions de seguretat de Linux"]
cover: "/img/cover/A_colorful_cartoon-style_image_depicting_a_robot_applying_patches.png"
coverAlt: "Una imatge acolorida d'estil de dibuixos animats que representa un robot aplicant pegats a un grup de servidors Linux."
coverCaption: ""
---

**Automatització de pedaços i actualitzacions de Linux amb Ansible**

En el món trepidant i conscient de la seguretat actual, **automatitzar** el pedaç i l'actualització dels sistemes Linux és crucial per garantir l'estabilitat del sistema i mitigar les vulnerabilitats. Amb la multitud de distribucions de Linux disponibles, pot ser difícil gestionar les actualitzacions a diferents plataformes de manera eficient. Afortunadament, **Ansible**, una potent eina d'automatització, ofereix una solució unificada per automatitzar l'aplicació de pedaços i les actualitzacions en diverses distribucions de Linux. En aquest article, explorarem com utilitzar Ansible per automatitzar el procés de pedaç i actualització per a distribucions **basades en Debian, Ubuntu, RHEL, Alpine** i altres distribucions. També proporcionarem un exemple detallat del llibre de jocs d'Ansible que gestiona la instal·lació de pedaços i actualitzacions a diferents distribucions de Linux, juntament amb instruccions per configurar les credencials d'Ansible i els fitxers d'amfitrió per a tots els sistemes de destinació.

## Requisits previs

Abans de submergir-nos en el procés d'automatització, assegurem-nos que tenim els requisits previs necessaris. Això inclou:

1. **Instal·lació d'Ansible**: per utilitzar Ansible, cal que l'instal·leu al sistema des del qual executareu les tasques d'automatització. Podeu seguir la documentació oficial d'Ansible a [how to install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/index.html) per obtenir instruccions detallades.

2. **Configuració d'inventari**: creeu un fitxer d'inventari que enumera els sistemes de destinació que voleu gestionar amb Ansible. Cada sistema hauria de tenir la seva **adreça IP o nom d'amfitrió** especificada. Per exemple, podeu crear un fitxer d'inventari anomenat `hosts.ini` amb el següent contingut:

```ini
[debian]
debian-host ansible_host=<debian_ip_address>

[ubuntu]
ubuntu-host ansible_host=<ubuntu_ip_address>

[rhel]
rhel-host ansible_host=<rhel_ip_address>

[alpine]
alpine-host ansible_host=<alpine_ip_address>
```

Substitueix `<debian_ip_address>` `<ubuntu_ip_address>` `<rhel_ip_address>` i `<alpine_ip_address>` amb les respectives adreces IP o noms d'amfitrió dels sistemes de destinació.

3. **Accés SSH**: assegureu-vos que teniu accés SSH als sistemes de destinació mitjançant l'autenticació basada en clau SSH. Això permetrà a Ansible connectar-se de manera segura als sistemes i realitzar les tasques necessàries.

## Ansible Playbook per a pedaços i actualitzacions

Per automatitzar el procés de pedaços i actualització de diverses distribucions de Linux, podem crear un llibre de jugades Ansible que gestioni la instal·lació de pedaços i actualitzacions en diferents distribucions. A continuació es mostra un exemple de llibre de jocs:

```yaml
---
- name: Patching and Updating Linux Systems
  hosts: all
  become: yes

  tasks:
    - name: Update Debian-based Systems
      when: ansible_os_family == 'Debian'
      apt:
        update_cache: yes
        upgrade: dist

    - name: Update RHEL-based Systems
      when: ansible_os_family == 'RedHat'
      yum:
        name: '*'
        state: latest

    - name: Update Alpine-based Systems
      when: ansible_os_family == 'Alpine'
      apk:
        update_cache: yes
        upgrade: yes
```

Al llibre de jocs anterior:

- El `hosts` La línia especifica els sistemes de destinació per a cada tasca. El llibre de jugades s'executarà en sistemes agrupats a sota `debian` `ubuntu` `rhel` i `alpine`
- El `become: yes` permet que el llibre de jugades s'executi amb privilegis administratius.
- La primera tasca actualitza els sistemes basats en Debian i Ubuntu mitjançant l' `apt` mòdul.
- La segona tasca actualitza els sistemes basats en RHEL mitjançant el `yum` mòdul.
- La tercera tasca actualitza els sistemes basats en els Alps mitjançant el `apk` mòdul.

Tingueu en compte que les tasques estan condicionades en funció dels noms dels grups per orientar els sistemes adequats.

## Configuració de credencials i fitxers d'amfitrió d'Ansible

Per configurar les credencials d'Ansible i els fitxers d'amfitrió per als sistemes de destinació, seguiu aquests passos:

1. Creeu un fitxer **Ansible Vault** per emmagatzemar informació sensible, com ara credencials SSH. Podeu utilitzar l'ordre següent per crear un fitxer de volta:
```shell
ansible-vault create credentials.yml
```
2. Actualitzeu el fitxer d'inventari (`hosts.ini` amb les credencials SSH adequades per a cada sistema de destinació. Per exemple:
```ini
[debian]
debian-host ansible_host=<debian_ip_address> ansible_user=<debian_username> ansible_ssh_pass=<debian_ssh_password>

[ubuntu]
ubuntu-host ansible_host=<ubuntu_ip_address> ansible_user=<ubuntu_username> ansible_ssh_pass=<ubuntu_ssh_password>

[rhel]
rhel-host ansible_host=<rhel_ip_address> ansible_user=<rhel_username> ansible_ssh_pass=<rhel_ssh_password>

[alpine]
alpine-host ansible_host=<alpine_ip_address> ansible_user=<alpine_username> ansible_ssh_pass=<alpine_ssh_password>
```

Substitueix `<debian_ip_address>` `<ubuntu_ip_address>` `<rhel_ip_address>` i `<alpine_ip_address>` amb les adreces IP respectives dels sistemes de destinació. També, substituir `<debian_username>` `<ubuntu_username>` `<rhel_username>` i `<alpine_username>` amb els noms d'usuari SSH adequats per a cada sistema. Finalment, substituir `<debian_ssh_password>` `<ubuntu_ssh_password>` `<rhel_ssh_password>` i `<alpine_ssh_password>` amb les contrasenyes SSH corresponents.

3. Xifreu el fitxer hosts.ini amb Ansible Vault:
   
```shell
ansible-vault encrypt hosts.ini
```

Proporcioneu la contrasenya de la caixa forta quan se us demani.

Amb els passos anteriors, heu configurat les credencials d'Ansible i els fitxers d'amfitrió necessaris per a tots els sistemes de destinació

## Execució del llibre de jugades
Per executar el llibre de jugades i automatitzar el procés de pegat i actualització, seguiu aquests passos:

1. Obriu un terminal i navegueu fins al directori on teniu el fitxer del llibre de jocs i el fitxer d'inventari xifrat.

2. Executeu l'ordre següent per executar el llibre de jugades, proporcionant la contrasenya del magatzem quan se us demani:

```shell
ansible-playbook -i hosts.ini playbook.yml --ask-vault-pass
```

3. Ansible es connectarà als sistemes de destinació, utilitzarà les credencials proporcionades i executarà les tasques especificades, actualitzant els sistemes en conseqüència.

Felicitats! Heu automatitzat correctament l'aplicació de pedaços i l'actualització de diferents distribucions de Linux mitjançant Ansible. Amb el llibre de jugades d'Ansible i la configuració adequada de credencials i fitxers d'amfitrió, ara podeu gestionar de manera eficient el procés de pedaç i actualització a la vostra infraestructura de Linux.

## Conclusió

L'automatització de l'aplicació de pedaços i l'actualització dels sistemes Linux amb Ansible simplifica i racionalitza el procés, permetent als administradors del sistema gestionar de manera eficient les actualitzacions en diverses distribucions de Linux. Seguint les instruccions proporcionades en aquest article, heu après a crear un llibre de jugades Ansible que gestioni la instal·lació de pedaços i actualitzacions a diferents distribucions de Linux. A més, heu configurat les credencials d'Ansible i els fitxers d'amfitrió per orientar-vos als sistemes desitjats. Aprofiteu el poder de l'automatització i gaudiu dels avantatges d'una infraestructura Linux més segura i ben mantinguda.

## Referències

1. [Ansible Documentation](https://docs.ansible.com/)
2. [Official Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

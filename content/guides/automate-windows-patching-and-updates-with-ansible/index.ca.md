---
title: "Automatització de les actualitzacions de Windows amb Ansible: una guia completa"
date: 2023-05-27
toc: true
draft: false
description: "Racionalitzeu el procés d'actualització dels sistemes Windows mitjançant l'automatització amb Ansible: instruccions pas a pas i pràctiques recomanades incloses."
tags: ["automatitzar les actualitzacions de Windows", "Automatització Ansible", "gestió del sistema", "pedaços de seguretat", "infraestructura informàtica", "automatització de la xarxa", "gestió de la configuració", "operacions de TI", "DevOps", "seguretat cibernètica", "automatització informàtica", "eficiència informàtica", "Llibre de jugades Ansible", "Seguretat de Windows", "gestió de l'actualització", "productivitat informàtica", "Manteniment informàtic", "Credencials Ansible", "configuració de l'amfitrió", "automatització del sistema", "Actualitzacions de Windows", "Gestió del sistema Windows", "Pedaços de seguretat de Windows", "Infraestructura informàtica de Windows", "Automatització de xarxes de Windows", "Gestió de la configuració de Windows", "Operacions informàtiques de Windows", "Windows DevOps", "Ciberseguretat de Windows", "Automatització informàtica de Windows", "Eficiència informàtica de Windows"]
cover: "/img/cover/An_animated_illustration_showcasing_a_Windows_logo_surround.png"
coverAlt: "Una il·lustració animada que mostra un logotip de Windows envoltat d'engranatges que simbolitzen l'automatització i les actualitzacions."
coverCaption: ""
---

**Automatització de les actualitzacions de Windows amb Ansible: una guia completa**

Mantenir els sistemes Windows actualitzats és crucial per mantenir la seguretat i l'estabilitat. Tanmateix, gestionar i instal·lar manualment les actualitzacions en diversos sistemes pot ser una tasca llarga i propensa a errors. Afortunadament, amb el poder d'eines d'automatització com Ansible, podeu agilitzar el procés i assegurar-vos que els vostres sistemes estiguin sempre actualitzats. En aquest article, explorarem com automatitzar les actualitzacions de Windows amb Ansible i proporcionarem instruccions pas a pas per configurar les credencials i els fitxers d'amfitrió d'Ansible per a tots els vostres sistemes de destinació.

______

## Per què automatitzar les actualitzacions de Windows amb Ansible?

Automatitzar les actualitzacions de Windows amb Ansible ofereix diversos avantatges:

1. **Estalvi de temps**: en lloc d'actualitzar manualment cada sistema individualment, podeu automatitzar el procés i actualitzar diversos sistemes simultàniament, estalviant-vos temps i esforços valuosos.

2. **Coherència**: l'automatització garanteix que tots els sistemes rebin les mateixes actualitzacions, reduint el risc de deriva de la configuració i mantenint un entorn coherent i segur.

3. **Eficiència**: Ansible us permet programar actualitzacions en moments concrets, garantint una interrupció mínima del vostre flux de treball i maximitzant la disponibilitat del sistema.

4. **Escalabilitat**: tant si teniu un grapat de sistemes com si teniu una gran infraestructura, Ansible s'escala sense esforç, la qual cosa el converteix en una opció ideal per gestionar les actualitzacions en qualsevol nombre de sistemes Windows.

______

## Configuració de credencials i fitxers d'amfitrió d'Ansible

Abans de submergir-nos en l'automatització de les actualitzacions de Windows, primer configurem les credencials i els fitxers d'amfitrió necessaris a Ansible.

1. **Instal·lant Ansible**: si encara no ho heu fet, comenceu instal·lant Ansible al vostre controlador ansible basat en Linux. Podeu seguir la documentació oficial d'Ansible per obtenir instruccions detallades d'instal·lació: [Ansible Installation](https://docs.ansible.com/ansible/latest/installation_guide/index.html)

2. **Configuració de credencials d'Ansible**: per automatitzar les actualitzacions als sistemes Windows, Ansible requereix les credencials adequades. Assegureu-vos que teniu les credencials administratives necessàries per a cada sistema de destinació. Podeu emmagatzemar aquestes credencials de manera segura mitjançant Ansible's Vault o un gestor de contrasenyes que trieu.

3. **Creació del fitxer Ansible Hosts**: el fitxer Ansible hosts defineix l'inventari dels sistemes que voleu gestionar. Creeu un fitxer de text anomenat `hosts` i especifiqueu els sistemes de destinació utilitzant les seves adreces IP o noms d'amfitrió. Per exemple:

```ini
[windows]
192.168.1.101
192.168.1.102
```

4. **Definició de variables Ansible**: per flexibilitzar el procés d'automatització, podeu definir variables a Ansible. Per a les actualitzacions de Windows, és possible que vulgueu especificar la programació d'actualització desitjada o qualsevol configuració addicional. Les variables es poden definir al `hosts` fitxer o fitxers variables separats.

______

## Automatització de les actualitzacions de Windows amb Ansible

Amb la configuració bàsica al seu lloc, ara explorem com automatitzar les actualitzacions de Windows amb Ansible.

1. **Creació de l'Ansible Playbook**: Ansible Playbooks són fitxers YAML que defineixen una sèrie de tasques que s'han d'executar als sistemes de destinació. Creeu un fitxer YAML nou anomenat `update_windows.yml` i definir les tasques necessàries.

```yaml
---
- name: Install Security Patches for Windows
  hosts: windows
  gather_facts: false

  tasks:
    - name: Check for available updates
      win_updates:
        category_names:
          - SecurityUpdates
        state: searched
      register: win_updates_result

    - name: Install security updates
      win_updates:
        category_names:
          - SecurityUpdates
        state: installed
      when: win_updates_result.updates | length > 0
```
Deseu-lo en un fitxer anomenat install_security_patches.yml

Aquest llibre de jugades comprova primer si hi ha actualitzacions de seguretat disponibles mitjançant el `win_updates` mòdul amb el `SecurityUpdates` categoria. El resultat es registra al `win_updates_result` variable. A continuació, el llibre de jugades passa a instal·lar les actualitzacions de seguretat si n'hi ha disponibles.

2. **Ús de mòduls Ansible**: Ansible ofereix diversos mòduls per interactuar amb sistemes Windows. El `win_updates` El mòdul està dissenyat específicament per gestionar les actualitzacions de Windows. Dins del vostre llibre de jugades, utilitzeu aquest mòdul per instal·lar actualitzacions, comprovar si hi ha actualitzacions disponibles o reiniciar els sistemes si cal. Consulteu la documentació oficial d'Ansible per obtenir informació detallada sobre com utilitzar el `win_updates` mòdul: [Ansible Windows Modules](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_updates_module.html)

3. **Execució de l'Ansible Playbook**: un cop hàgiu definit les tasques al vostre llibre de jugades, executeu-lo amb el `ansible-playbook` comanda, especificant el fitxer del llibre de reproducció i els amfitrions de destinació. Per exemple:

```shell
ansible-playbook -i hosts install_security_patches.yml
```

4. **Programar l'execució regular**: per garantir que les actualitzacions s'apliquen de manera coherent, podeu programar l'execució del llibre de jugades d'Ansible a intervals regulars. Eines com cron (a Linux) o Task Scheduler (a Windows) es poden utilitzar per automatitzar aquest procés. Hauríeu d'utilitzar cron to per a això específicament, ja que el llibre de jugades es llança des d'un controlador ansible basat en Linux.

Obre crontab

```bash
   crontab -e
```
Afegiu la línia següent després de modificar-la

```text
0 3 * * * ansible-playbook -i /path/to/hosts /path/to/playbook.yml
```

______

## Conclusió

Automatitzar les actualitzacions de Windows amb Ansible pot simplificar molt la gestió de les actualitzacions a la vostra infraestructura. Seguint els passos descrits en aquest article, podeu configurar les credencials d'Ansible, definir fitxers d'amfitrió i crear llibres de jugades per automatitzar el procés d'actualització. Adoptar l'automatització no només estalvia temps, sinó que també garanteix que els vostres sistemes Windows estiguin actualitzats, segurs i funcionin al màxim.

Recordeu mantenir-vos informat sobre les regulacions governamentals rellevants, com ara la [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) or [ISO/IEC 27001](https://www.iso.org/isoiec-27001-information-security.html) que proporcionen directrius i bones pràctiques per mantenir un entorn segur i compatible.

______

## Referències

- [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html)
- [Ansible Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/index.html)
- [Ansible Windows Modules](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_updates_module.html)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [ISO/IEC 27001 - Information Security](https://www.iso.org/isoiec-27001-information-security.html)


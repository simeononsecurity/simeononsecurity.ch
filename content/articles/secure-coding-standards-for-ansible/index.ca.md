---
title: "Directrius de programació segura per a Ansible: bones pràctiques"
date: 2023-03-02
lastmod: 2026-11-19
toc: true
draft: false
description: "Aprèn les bones pràctiques per escriure codi segur amb Ansible, una eina popular de gestió de configuració i desplegament."
tags: ["Programació segura","Ansible","Gestió de configuració","Desplegament","Principi de privilegis mínims","Ansible Vault","Contrasenyes robustes","Control d'accés","Sistema de control de versions","Protocols de comunicació segurs","SSH","WinRM","Certificats TLS","Neteja de l'entrada de l'usuari","Validació de l'entrada","Gestió d'errors","Pràctiques de programació segura","Injecció de codi","Directrius de programació segura","Seguretat de la infraestructura","Directrius de programació segura per a Ansible","Bones pràctiques de codi segur amb Ansible","Gestió segura de configuració amb Ansible","Pràctiques de desplegament segur amb Ansible","Principi de privilegis mínims a Ansible","Ús d'Ansible Vault per protegir el codi","Creació de contrasenyes robustes a Ansible","Control d'accés a Ansible","Sistema de control de versions per als playbooks d'Ansible","Protocols de comunicació segurs a Ansible","Seguretat de SSH a Ansible","Seguretat de WinRM a Ansible","Certificats TLS a Ansible","Neteja de l'entrada de l'usuari a Ansible","Validació de l'entrada a Ansible","Gestió d'errors a Ansible","Pràctiques de programació segura a Ansible","Prevenció de la injecció de codi a Ansible","Directrius de programació segura per a infraestructures gestionades amb Ansible","Protecció de la infraestructura d'Ansible"]
cover: "/img/cover/A_cartoon_image_of_a_castle_protected_by_a_shield.webp"
coverAlt: "Dibuix animat d'un castell protegit per un escut, que representa les mesures de seguretat de la infraestructura gestionada amb Ansible."
coverCaption: ""
---

A mesura que les organitzacions adopten més l'automatització, **Ansible** s'ha convertit en una eina preferida per a la **gestió de configuració** i el **desplegament**. Però, com qualsevol programari, Ansible no és immune a les vulnerabilitats de seguretat. Per això, és essencial prioritzar el desenvolupament de **codi segur** per protegir i mantenir la integritat de la infraestructura gestionada amb Ansible. Aquest article presenta les **bones pràctiques** essencials per escriure **codi segur** amb Ansible i reforçar els fluxos de treball d'automatització davant de possibles amenaces.

## Entendre la seguretat d'Ansible

Abans de veure les directrius, convé entendre les funcions de seguretat d'Ansible. Ansible **xifra** les comunicacions entre els nodes de control i els nodes gestionats. També ofereix **emmagatzematge segur** per als **secrets** i altra informació sensible amb **Vault**. A més, incorpora un mecanisme d'**aïllament** per protegir-se de l'execució de codi potencialment maliciós.

Aquestes funcions no eximeixen els desenvolupadors d'escriure codi segur. Seguir les directrius següents ajuda a complementar les funcions de seguretat integrades d'Ansible amb codi segur.

## Importància del codi segur a Ansible

Escriure **codi segur** és fonamental quan s'utilitza Ansible per gestionar infraestructura. Amb les **bones pràctiques de seguretat**, les organitzacions poden reduir riscos com ara l'accés no autoritzat, les filtracions de dades i les interrupcions del servei. El **codi segur** a Ansible protegeix la confidencialitat, la integritat i la disponibilitat dels actius crítics i reforça la solidesa i la fiabilitat de l'entorn automatitzat.

## Directriu 1: Utilitza la versió més recent d'Ansible

Ansible s'actualitza constantment per corregir vulnerabilitats de seguretat i errors. La versió més recent ofereix als desenvolupadors les correccions i millores de seguretat més actuals.

Comprova periòdicament si hi ha actualitzacions i instal·la-les tan aviat com sigui possible. També et pots subscriure a la llista de correu d'Ansible Security Announcements per rebre avisos sobre actualitzacions de seguretat. Actualitzar a la versió més recent és un pas senzill que pot millorar significativament la seguretat de la infraestructura gestionada amb Ansible.

## Directriu 2: Segueix el principi de privilegis mínims

El **principi de privilegis mínims** és un principi de seguretat fonamental que també s'aplica a Ansible: cada usuari només ha de tenir l'accés mínim necessari per fer la seva feina. Els desenvolupadors han de concedir als nodes gestionats només els permisos necessaris per completar les tasques requerides.

Per exemple, si un playbook només necessita llegir un fitxer concret, concedeix-li permís de lectura, però no d'escriptura ni d'execució. Limita també el nombre d'usuaris que tenen accés a Ansible. L'accés s'ha de restringir als usuaris autoritzats que necessiten gestionar la infraestructura amb Ansible.

Ansible ofereix diversos mecanismes per aplicar aquest principi, com ara la directiva `become`. Aquesta permet executar tasques amb els privilegis d'un altre usuari, com ara `sudo`. Utilitza-la només quan calgui i concedeix únicament els privilegis necessaris.

Aplicar el principi de privilegis mínims limita els danys que podria causar un atacant en cas d'una bretxa de seguretat. Aquesta directriu pot millorar notablement la seguretat de la infraestructura gestionada amb Ansible.

## Directriu 3: Utilitza Ansible Vault per a la informació sensible

No desis informació sensible, com ara contrasenyes, claus d'API i certificats, en text sense xifrar als playbooks d'Ansible. Això pot posar en risc la seguretat de la infraestructura gestionada amb Ansible. Ansible ofereix **Vault** per emmagatzemar aquesta informació de manera segura.

Vault xifra la informació sensible amb una contrasenya o un fitxer de clau. Amb l'ordre `ansible-vault` pots crear un fitxer xifrat, editar-ne un d'existent o visualitzar-lo. També pots xifrar o desxifrar variables individuals. Per crear un fitxer xifrat nou, executa:

```bash
ansible-vault create secret.yml
```

Aquesta ordre crearà un fitxer xifrat nou anomenat `secret.yml`. Pots editar-lo amb l'ordre `ansible-vault edit`, que et demanarà la contrasenya de Vault.

Assegura't també d'emmagatzemar les contrasenyes i els fitxers de clau de manera segura. No els desis en text sense xifrar. Utilitza una ubicació protegida, com ara un gestor de contrasenyes o un servidor de fitxers segur.

Emmagatzemar la informació sensible amb Vault és un pas essencial per protegir la infraestructura gestionada amb Ansible. Així, la informació no queda exposada en text sense xifrar i només hi poden accedir els usuaris autoritzats.

## Directriu 4: Utilitza contrasenyes robustes

Les contrasenyes d'autenticació han de ser **robustes** i **úniques**. Les contrasenyes febles o habituals poden posar en risc la infraestructura gestionada amb Ansible. Evita les contrasenyes predeterminades i no les escriguis directament als playbooks. Desa-les de manera segura amb Vault.

Una contrasenya robusta ha de tenir almenys 12 caràcters i combinar majúscules, minúscules, números i símbols especials. Evita dades fàcils d'endevinar, com ara noms o dates de naixement. Pots fer servir un gestor de contrasenyes per generar contrasenyes robustes i úniques.

Desa les contrasenyes dels playbooks en format xifrat amb Vault. No les incloguis directament al playbook. En lloc d'això, desa-les en variables. Per exemple, defineix `db_password` en un fitxer xifrat separat i fes-hi referència al playbook amb aquesta sintaxi:

```yml
db_password: "{{ vault_db_password }}"
```

Aquesta sintaxi fa referència a la variable `db_password` del fitxer xifrat i la desxifra amb Vault.

Utilitzar contrasenyes robustes i desar-les de manera segura ajuda a impedir l'accés no autoritzat a la infraestructura gestionada amb Ansible. És un pas senzill que millora la seguretat.

## Directriu 5: Limita l'accés als playbooks

Limita l'accés als playbooks d'Ansible als usuaris autoritzats. Utilitza un **sistema de control de versions** com **Git** per gestionar-los. Git ofereix funcions de **control d'accés** i **auditoria** que ajuden a aplicar les polítiques de seguretat.

## Directriu 6: Utilitza protocols de comunicació segurs

Ansible admet diversos protocols de comunicació, entre ells SSH i WinRM. SSH és el protocol recomanat per als amfitrions Linux i macOS. WinRM és el recomanat per als amfitrions Windows. Assegura't que la comunicació entre els nodes de control i els nodes gestionats estigui **xifrada**.

SSH és un protocol de comunicació segur que xifra les comunicacions entre els nodes de control i els nodes gestionats. Utilitza claus SSH robustes per autenticar-te, amb una longitud mínima de 2048 bits. També has de desactivar l'autenticació per contrasenya de SSH.

WinRM també xifra la comunicació entre els nodes de control i els nodes gestionats. Utilitza WinRM a través d'HTTPS per garantir que la comunicació estigui xifrada i fes servir certificats robustos per a l'autenticació.

Assegura't que els certificats TLS utilitzats per a les comunicacions HTTPS siguin vàlids i no hagin caducat. Pots utilitzar eines com `openssl` per generar-los i gestionar-los.

Utilitzar protocols de comunicació segurs és un pas essencial per protegir la infraestructura gestionada amb Ansible. Així, les comunicacions entre els nodes de control i els nodes gestionats es mantenen xifrades i segures.

## Directriu 7: Verifica les identitats dels amfitrions

Verifica la identitat dels nodes gestionats abans de permetre'ls connectar-se als nodes de control. Ansible ofereix diversos mecanismes per fer-ho, com ara les **empremtes de claus SSH** i els **certificats TLS**. Assegura't que les configuracions SSH i TLS estiguin actualitzades i siguin segures.

Les empremtes de claus SSH són identificadors únics de les claus que utilitzen els nodes gestionats per autenticar-se. Verifica-les abans de permetre la connexió als nodes de control. Pots generar-les amb l'ordre `ssh-keygen` i comparar-les amb les empremtes proporcionades pels nodes gestionats.

Els nodes gestionats utilitzen certificats TLS per autenticar-se davant dels nodes de control. Comprova que els certificats siguin vàlids i no hagin caducat. Assegura't també que els nodes de control confiïn en els certificats dels nodes gestionats.

Mantén actualitzades i segures les configuracions SSH i TLS. Han d'utilitzar algorismes robustos de xifratge i autenticació, i rebutjar els xifratges i protocols febles.

Verificar les identitats dels nodes gestionats és essencial per protegir la infraestructura d'Ansible. Ajuda a evitar atacs d'intermediari i garanteix que només els nodes gestionats autoritzats puguin connectar-se als nodes de control.

## Directriu 8: Neteja l'entrada de l'usuari

Neteja l'entrada de l'usuari per evitar la **injecció de codi** i altres vulnerabilitats de seguretat. Sempre que sigui possible, utilitza **entrades validades** per reduir-ne el risc.

## Directriu 9: Segueix les pràctiques de programació segura

Segueix **pràctiques de programació segura**, com ara la **validació de l'entrada**, la **gestió d'errors** i la **neteja** de les entrades. Segueix també les **directrius de programació segura** del llenguatge utilitzat amb Ansible.

Neteja l'entrada de l'usuari per evitar la **injecció de codi** i altres vulnerabilitats. En un atac d'injecció de codi, un atacant introdueix codi maliciós en una aplicació aprofitant vulnerabilitats en l'entrada de l'usuari. Utilitza entrades validades sempre que sigui possible per reduir el risc.

Pots utilitzar el filtre `regex_replace` d'Ansible per netejar l'entrada de l'usuari. Aquest filtre substitueix patrons d'una cadena per altres patrons. Per exemple, aquest codi elimina els caràcters que no són alfanumèrics:

```yaml
- name: Neteja l'entrada de l'usuari
  vars:
    user_input: "Hola! Aquesta cadena conté caràcters no alfanumèrics."
    sanitized_input: "{{ user_input | regex_replace('[^A-Za-z0-9]', '') }}"
  debug:
    var: sanitized_input
```

En aquest exemple, el filtre `regex_replace` substitueix per una cadena buida tots els caràcters no alfanumèrics de `user_input`. L'entrada netejada es desa a `sanitized_input`.

La validació de l'entrada també redueix el risc de vulnerabilitats. Consisteix a comprovar que l'entrada compleixi criteris determinats, com ara contenir només caràcters alfanumèrics. Es pot implementar amb condicionals i expressions regulars d'Ansible.

Netejar i validar l'entrada de l'usuari ajuda a evitar la injecció de codi i altres vulnerabilitats als playbooks d'Ansible. És un pas senzill per millorar-ne la seguretat.

## Conclusió

A mesura que les organitzacions adopten l'automatització, **Ansible** destaca com una opció popular per a la **gestió de configuració** i el **desplegament**. Tot i això, cal prioritzar el desenvolupament de **codi segur** per protegir la integritat i la fiabilitat de la infraestructura gestionada amb Ansible.

Seguir les **directrius** d'aquest article ajuda els desenvolupadors a aplicar **bones pràctiques de seguretat** als fluxos de treball d'Ansible. Això inclou utilitzar el **control d'accés basat en rols (RBAC)**, protegir els canals de comunicació amb **Transport Layer Security (TLS)** o **Secure Shell (SSH)**, gestionar secrets i dades sensibles amb **Ansible Vault** i actualitzar Ansible periòdicament per protegir-se de vulnerabilitats conegudes.

Utilitza sempre la versió més recent d'Ansible, segueix el principi de privilegis mínims, utilitza Ansible Vault per a la informació sensible, tria contrasenyes robustes, limita l'accés als playbooks, utilitza protocols de comunicació segurs, verifica les identitats dels amfitrions, neteja l'entrada de l'usuari i segueix pràctiques de programació segura. Aquestes directrius ajuden a escriure codi segur i a protegir la infraestructura de les vulnerabilitats.

Integrant aquestes **bones pràctiques**, les organitzacions poden aprofitar l'automatització d'Ansible i mantenir una infraestructura segura i fiable. Protegir els actius crítics amb codi segur i amb les funcions de seguretat integrades d'Ansible permet adoptar l'automatització sense comprometre la seguretat.

## Referències

- [Documentació d'Ansible](https://docs.ansible.com/)
- [Documentació d'Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html)
- [Documentació de Git](https://git-scm.com/doc)
- [Documentació d'OpenSSH](https://www.openssh.com/)
- [Documentació de Transport Layer Security (TLS)](https://tools.ietf.org/html/rfc8446)
- [Documentació d'OWASP sobre la injecció de codi](https://owasp.org/www-community/attacks/Code_Injection)

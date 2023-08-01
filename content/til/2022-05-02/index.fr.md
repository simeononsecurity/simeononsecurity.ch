---
title: "Today I Learned about Ansible and Block/Rescue Modules"
date: 2022-05-02
toc: true
draft: false
description: ""
genre: ["Automatisation", "Conformité", "Ansible", "Manuels Ansible", "Collections Ansible", "Sécurité Windows", "Administration Windows", "Conformité en matière de sécurité", "Automatisation des technologies de l'information", "Gestion de la configuration"]
tags: ["Automatisation", "Conformité", "Ansible", "Manuels Ansible", "Collections Ansible", "GitHub", "Bloc", "Sauvetage", "Toujours", "Sécurité Windows", "Administration Windows", "Exigences de la STIG", "Automatisation de la sécurité", "Gestion de la configuration", "Sécurité informatique", "Modules Ansible", "Windows Automation", "Ansible Galaxy", "Windows STIG", "Outils d'administration Windows", "Guide de mise en œuvre technique de la sécurité", "Contenu Ansible", "Meilleures pratiques en matière de sécurité Windows", "Solutions d'automatisation informatique", "Audit de sécurité", "Configuration du système Windows"]
---
 SimeonOnSecurity a appris l'existence de ce site et l'a trouvé intéressant aujourd'hui**

SimeonOnSecurity a appris et découvert aujourd'hui plusieurs choses intéressantes liées à la sécurité Windows et à l'automatisation à l'aide d'Ansible.

Tout d'abord, deux référentiels nouveaux et mis à jour ont été identifiés. Le dépôt Windows_STIG_Ansible fournit une solution complète pour configurer les systèmes Windows afin de répondre aux exigences du Guide de mise en œuvre technique de la sécurité (STIG), en utilisant la plateforme d'automatisation Ansible. Le référentiel windows_stigs est une collection de rôles Ansible pour configurer les systèmes Windows afin de répondre aux exigences du STIG, et il est disponible sur Ansible Galaxy, un référentiel central pour le partage du contenu Ansible.

SimeonOnSecurity a également trouvé plusieurs ressources d'apprentissage liées à l'automatisation de Windows avec Ansible. La documentation du module ansible.windows.win_copy fournit des informations sur la manière de copier des fichiers sur des systèmes Windows à l'aide d'Ansible. La documentation ansible blocks fournit des informations sur l'utilisation des blocs, une fonctionnalité puissante d'Ansible qui vous permet de regrouper plusieurs tâches et d'appliquer une exécution conditionnelle. Le guide de l'utilisateur ansible galaxy fournit des informations sur l'utilisation d'Ansible Galaxy, et la documentation ansible installing content fournit des informations sur l'installation de contenu à partir d'Ansible Galaxy.

## New/Updated Repos :

- [simeononsecurity/Windows_STIG_Ansible](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [simeononsecurity/windows_stigs](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Ressources pédagogiques :
- [ansible.windows.win_copy module](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_copy_module.html)
- [ansible blocks](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
- [ansible galaxy user guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html)
- [ansible installing content](https://galaxy.ansible.com/docs/using/installing.html)
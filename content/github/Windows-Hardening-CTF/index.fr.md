---
title: "Windows Hardening CTF : Renforcez la sécurité de votre appareil Windows pour les événements Capture the Flag"
date: 2020-10-19
toc: true
draft: false
description: "Découvrez un script puissant qui renforce la sécurité de Windows en mettant en œuvre diverses mesures de durcissement afin d'empêcher toute compromission."
tags: ["Durcissement des fenêtres", "Sécurité Windows", "scénario", "Appareil Windows", "invite de commande", "LLMNR", "PowerShell", "PME", "Horodatage TCP", "AppLocker", "Journalisation Windows", "DEP", "Configurations EMET", "Mode linguistique contraint de PowerShell", "SMB encryption", "Atténuation des effets de Spectre et Meltdown", "Windows Defender", "Pare-feu Windows", "PSWindowsUpdate", "Mises à jour de Windows", "script de durcissement", "Politiques recommandées par les ANE", "Journalisation et contrôles de sécurité de Windows", "Contrôle des applications Windows Defender", "Procédures de réduction de la surface d'attaque de Windows Defender", "Protections Windows Defender basées sur l'informatique en nuage", "Protections contre les exploits de Windows Defender", "Installation de PSWindowsUpdate", "Amélioration de la sécurité des appareils Windows", "Mesures de renforcement de Windows", "renforcer la sécurité de Windows"]
---

**Durcissement de Windows-CTF**
Un script de durcissement de Windows qui rend plus difficile et plus ennuyeux la compromission d'un appareil Windows.

## Que fait ce script ?
- Désactive l'invite de commande
- Désactive LLMNR
- Désactive PowerShell v2
- Désactive la compression SMB
- Désactive SMB v1
- Désactive SMB v2
- Désactive les horodatages TCP
- Désactive WSMAN et PSRemoting
- Active AppLocker avec les politiques recommandées par la NSA
- Activation des contrôles de sécurité et de journalisation des meilleures pratiques de Windows
- Active DEP
- Activation des configurations EMET (s'applique uniquement aux systèmes sur lesquels EMET est installé)
- Activation du mode de langage consolidé de PowerShell
- Activation de la journalisation PowerShell
- Activation du chiffrement SMB
- Active les atténuations Spectre et Meltdown
- Permet le contrôle des applications par Windows Defender
- Permet les procédures de réduction de la surface d'attaque de Windows Defender
- Permet les protections basées sur le cloud de Windows Defender
- Active les protections contre les exploits de Windows Defender
- Activation du pare-feu Windows et de la journalisation
- Installe PSWindowsUpdate et installe toutes les mises à jour disponibles de Windows

## Télécharger les fichiers nécessaires :

Téléchargez les fichiers nécessaires à partir du site [GitHub Repository](https://github.com/simeononsecurity/Windows-Hardening-CTF)

## Comment exécuter le script :

**Le script peut être lancé à partir du téléchargement GitHub extrait comme suit:**
```
.\sos-windows-hardening-ctf.ps1
```

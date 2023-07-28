---
title: "Notions de base sur les réseaux : Comprendre les couches OSI et le modèle IP TCP"
draft: false
toc: true
date: 2023-07-22
description: "Acquérir une compréhension complète des couches OSI et du modèle TCP IP, cadres essentiels dans le domaine des réseaux, afin de faciliter une communication et un dépannage efficaces."
genre: ["Les bases de la mise en réseau", "Couches OSI", "Modèle TCP IP", "Protocoles de réseau", "Modèles de communication", "Fondamentaux de la mise en réseau", "Data Transmission", "Dépannage du réseau", "Architecture du réseau", "Concepts de mise en réseau"]
tags: ["Couches OSI", "Modèle TCP IP", "les bases de la mise en réseau", "les protocoles de réseau", "modèles de communication", "transmission de données", "dépannage du réseau", "architecture du réseau", "concepts de mise en réseau", "principes fondamentaux de la mise en réseau", "cadres de mise en réseau", "explication des protocoles de réseau", "normes de mise en réseau", "couche physique", "couche de liaison de données", "couche réseau", "couche transport", "couche session", "couche de présentation", "couche application", "Couches TCP IP", "couche d'interface réseau", "couche internet", "couche transport", "couche application", "les protocoles de mise en réseau expliqués", "modèles de mise en réseau", "les principes fondamentaux de la mise en réseau expliqués", "guide de mise en réseau", "tutoriel sur la mise en réseau", "les meilleures pratiques en matière de mise en réseau"]
cover: "/img/cover/An_animated_illustration_showcasing_a_network.png"
coverAlt: "Illustration animée représentant un réseau de nœuds interconnectés entre lesquels circulent des données, symbole d'une communication et d'un réseau efficaces."
---
 Notions de base sur les réseaux : Comprendre les couches OSI et le modèle IP TCP

### Introduction

Dans le monde des réseaux, il est essentiel de comprendre les protocoles et les modèles qui régissent la communication. Deux cadres largement utilisés sont le modèle **OSI (Open Systems Interconnection)** et le modèle **TCP IP (Transmission Control Protocol/Internet Protocol)**. Ces modèles fournissent une approche structurée de la mise en réseau et servent de base à la construction et au dépannage des systèmes de réseau. Cet article vise à expliquer les couches OSI et le modèle TCP IP de manière claire et concise.

## Les couches OSI

Le **modèle OSI** est un cadre conceptuel qui décrit comment les protocoles réseau interagissent et permettent la communication entre différents systèmes. Il se compose de sept couches, chacune ayant ses propres responsabilités.


| Le modèle OSI se compose de sept couches, chacune ayant ses propres responsabilités.
|----------------|---------------------------------------------------------------|---------------------|------------------------------------------------|---------------------------------------------|
| Couche physique - Traite de la transmission physique des données - Câbles, connecteurs - Ethernet, USB, HDMI - IEEE 802.3, USB 3.0 - Couche de liaison de données - Garantit l'intégrité des données.
| Couche de liaison de données - Garantit un transfert fiable des données entre des nœuds adjacents - Commutateurs, cartes réseau - Ethernet, Wi-Fi (802.11), PPP - IEEE 802.3, IEEE 802.11, RFC 1662 - Couche réseau - Achemine les données entre les nœuds adjacents.
| Couche réseau | Achemine les paquets de données à travers différents réseaux | Routeurs | IP, ICMP, ARP | IPv4 (RFC 791), IPv6 (RFC 2460), ARP (RFC 826)
| Couche de transport : fournit une livraison fiable des données de bout en bout.
| Couche de session : gère les sessions de communication entre les applications, NetBIOS, SIP, RFC 1001, RFC 1002, RFC 3261.
| Couche de présentation | Traite de la syntaxe et de la sémantique des échanges d'informations | SSL, HTTP | SSL/TLS, HTTP | SSL/TLS (RFC 5246), HTTP (RFC 2616) | Couche de présentation
| Couche application| Interagit directement avec les applications de l'utilisateur final | Navigateurs web, clients de messagerie | HTTP, FTP, SMTP, DNS | HTTP (RFC 2616), FTP (RFC 959), SMTP (RFC 5321), DNS (RFC 1035) |

{{< youtube id="0y6FtKsg6J4" >}}

Examinons chaque couche en détail :

### Couche 1 : Couche physique

La **couche physique** est la couche la plus basse du modèle OSI et traite de la **transmission physique** des données sur un réseau. Elle définit les **composants matériels**, tels que les câbles, les connecteurs et les interfaces réseau, qui transmettent des **signaux binaires (0 et 1)**. Parmi les exemples de protocoles de cette couche, citons **Ethernet, USB et HDMI**.

### Couche 2 : couche de liaison de données

La **couche liaison de données** est responsable du **transfert fiable** des données entre les nœuds de réseau adjacents, tels que les commutateurs et les cartes d'interface réseau (NIC). Elle assure une **transmission sans erreur** et fournit des mécanismes de **contrôle du flux** et de **détection des erreurs**. Les protocoles courants de cette couche comprennent **Ethernet, Wi-Fi (802.11) et le protocole point à point (PPP)**.

### Couche 3 : couche réseau

La **couche réseau** est responsable de **l'acheminement des paquets de données** à travers différents réseaux. Elle détermine le **chemin optimal** pour la transmission des données en fonction des conditions du réseau et des schémas d'adressage. Le **protocole Internet (IP)** est un protocole fondamental de cette couche, qui attribue des **adresses IP uniques** aux périphériques à des fins d'identification et de routage.

### Couche 4 : Couche transport

La **couche transport** assure la **fiabilité et l'efficacité de la transmission des données de bout en bout** entre les applications fonctionnant sur différents appareils. Elle établit des **connexions**, **segmente les données** en unités plus petites (si nécessaire) et fournit des mécanismes de **récupération des erreurs** et de **contrôle du flux**. Le **Transmission Control Protocol (TCP)** et le **User Datagram Protocol (UDP)** sont des protocoles de transport couramment utilisés.

### Couche 5 : Couche session

La **couche session** gère les **sessions de communication** entre les applications fonctionnant sur différents appareils. Elle établit, maintient et termine ces sessions, permettant l'échange de **données** entre les processus. Cette couche est responsable de la **synchronisation** et du **contrôle du dialogue**. Parmi les exemples de protocoles de cette couche figurent **NetBIOS** et **Session Initiation Protocol (SIP)**.

### Couche 6 : Couche de présentation

La **couche de présentation** traite de la **syntaxe et de la sémantique** des informations échangées entre les systèmes. Elle veille à ce que les données soient correctement **formatées**, **encodées** et **chiffrées** pour une transmission sécurisée. Cette couche est responsable de la **compression des données**, du **chiffrement** et de la **conversion des protocoles**. Parmi les exemples de protocoles de cette couche figurent **Secure Sockets Layer (SSL)** et **Hypertext Transfer Protocol (HTTP)**.

### Couche 7 : Couche application

La **couche application** est la couche la plus élevée du modèle OSI et interagit directement avec les **applications de l'utilisateur final**. Elle fournit des services qui permettent la **communication entre utilisateurs** et l'**échange de données**. Les protocoles de cette couche sont par exemple **HTTP**, **FTP**, **SMTP** et **DNS**.

## Le modèle TCP IP

Alors que le modèle OSI fournit un cadre conceptuel, le modèle TCP IP est la suite de protocoles utilisée sur l'internet. Il comprend quatre couches, qui s'alignent sur certaines couches du modèle OSI.


| Le modèle TCP IP comprend quatre couches qui s'alignent sur certaines couches du modèle OSI.
|---------------------|---------------------------------------------------------------|---------------------|-------------------------------------------------|
Couche d'interface réseau | Gère la transmission physique des données | NICs, câbles Ethernet | Ethernet, Wi-Fi (802.11) | Couche Internet | Responsable de l'adressage et de la transmission des données.
| Couche Internet - Responsable de l'adressage, du routage et de la fragmentation des données.
| Couche transport - Fournit une communication fiable et orientée connexion - Passerelles - TCP, UDP - Couche application - Représente la couche application.
| Couche application - Représente l'interface entre les applications et les protocoles - Navigateurs Web, clients de messagerie - HTTP, FTP, SMTP, DNS - Couche de sécurité - Représente l'interface entre les applications et les protocoles.

{{< youtube id="OTwp3xtd4dg" >}}

Explorons ces couches :

### Couche 1 : Couche d'interface réseau

La **couche d'interface réseau** correspond à la combinaison des **couches physiques** et **couches de liaison de données** dans le modèle OSI. Elle gère la transmission physique des données sur le réseau et fournit des protocoles pour le contrôle de la liaison de données.

### Couche 2 : Couche Internet

La **couche Internet** est l'équivalent de la **couche réseau** dans le modèle OSI. Elle comprend le protocole IP, qui est responsable de l'adressage**, du routage** et de la fragmentation** des paquets de données en vue de leur transmission sur les réseaux.

### Couche 3 : Couche transport

La **couche transport** du modèle TCP IP s'aligne sur la **couche transport** du modèle OSI. Elle assure une communication **fiable** et **orientée vers la connexion** à l'aide du protocole **TCP** ou une communication **légère, sans connexion** à l'aide du protocole **UDP**.

### Couche 4 : Couche application

La **couche application** du modèle TCP IP comprend les fonctionnalités des **couches session**, **présentation** et **application** du modèle OSI. Elle représente l'interface entre les applications et les protocoles réseau sous-jacents.

## Conclusion

La compréhension des **couches OSI** et du **modèle IPTCP** est cruciale pour toute personne impliquée dans les réseaux. Ces modèles fournissent un cadre pour comprendre le fonctionnement des réseaux et les protocoles qui facilitent la communication. En comprenant les fonctions de chaque couche, les **administrateurs de réseaux** et les **ingénieurs** peuvent résoudre les problèmes de manière efficace et concevoir des systèmes de réseaux robustes.


Références :
- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [TCP IP model](https://www.geeksforgeeks.org/tcp-ip-model/)
- [Ethernet](https://www.computernetworkingnotes.com/networking-tutorials/ethernet-standards-and-protocols-explained.html)
- [Wi-Fi](https://www.wi-fi.org/)
- [IP address](https://en.wikipedia.org/wiki IP_address)
- [Transmission Control Protocol](https://en.wikipedia.org/wiki/Transmission_Control_Protocol)
- [User Datagram Protocol](https://www.cloudflare.com/learning/ddos/glossary/user-datagram-protocol-udp/)
- [NetBIOS](https://en.wikipedia.org/wiki/NetBIOS)
- [SSL](https://www.cloudflare.com/learning/ssl/what-is-ssl/)
- [Hypertext Transfer Protocol](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
- [DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)

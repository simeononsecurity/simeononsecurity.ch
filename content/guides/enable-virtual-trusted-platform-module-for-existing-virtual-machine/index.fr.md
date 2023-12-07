---
title: "Renforcer la sécurité des machines virtuelles avec vTPM : Guide étape par étape"
date: 2023-09-02
toc: true
draft: false
description: "Renforcez la sécurité des machines virtuelles à l'aide de vTPM grâce à notre guide étape par étape complet, qui fournit une attestation de plate-forme et une prise en charge du chiffrement BitLocker."
genre: ["Cybersécurité", "Virtualisation", "VMware", "vSphere", "Sécurité", "Module de plateforme de confiance", "vTPM", "Guest OS", "Cryptage", "Attestation de la plate-forme"]
tags: ["Module de plateforme virtuelle de confiance", "Guide vTPM", "Sécurité renforcée des machines virtuelles", "Attestation de la plate-forme", "Chiffrement BitLocker", "VMware vSphere", "Sécurité de la virtualisation", "Cybersécurité", "Guest OS Protection", "Matériel VM", "TPM 2.0", "Amorçage sécurisé", "Opérations cryptographiques", "Meilleures pratiques en matière de sécurité des machines virtuelles", "vCenter Server", "Hôtes ESXi", "Firmware EFI", "Fournisseur principal", "Documentation VMware", "Serveur Windows", "Windows 7", "Linux OS", "Configuration sécurisée des machines virtuelles", "Caractéristiques de sécurité", "Client vSphere", "Puce virtuelle", "Protection des données", "Détection de sabotage", "Vérification de l'intégrité de la VM", "Sécurité VMware"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "Illustration symbolique d'une machine virtuelle avec un cadenas brillant, représentant la sécurité renforcée grâce au vTPM."
coverCaption: "Débloquez une sécurité VM sans précédent !"
---

## Activer le module de plate-forme virtuelle de confiance pour une machine virtuelle existante

Le module de plateforme virtuelle de confiance (vTPM) est une fonctionnalité de sécurité essentielle qui renforce la sécurité des systèmes d'exploitation invités s'exécutant sur des machines virtuelles. Cet article vous guidera dans le processus d'ajout d'un vTPM à une machine virtuelle existante dans un environnement VMware vSphere, en fournissant des instructions étape par étape et des considérations importantes pour assurer une mise en œuvre transparente.

______

## Prérequis

Avant de procéder à l'ajout d'une vTPM à votre machine virtuelle, assurez-vous que vous remplissez les conditions préalables suivantes :

1. **Environnement vSphere avec fournisseur de clés:** Assurez-vous que votre environnement vSphere est configuré pour un fournisseur de clés. Cette étape est cruciale pour gérer les opérations cryptographiques en toute sécurité. Reportez-vous à la section [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html) pour des conseils détaillés.

2. **Système d'exploitation invité pris en charge:** Vérifiez que votre système d'exploitation invité est compatible avec vTPM. VMware vTPM est compatible avec TPM 2.0 et prend en charge Windows Server 2008 et versions ultérieures, Windows 7 et versions ultérieures, ainsi que diverses distributions Linux.

3. **Statut de la machine virtuelle:** Assurez-vous que la machine virtuelle que vous souhaitez modifier est éteinte avant de procéder à l'ajout du vTPM.

4. **Version de l'hôte ESXi:** Les hôtes ESXi dans votre environnement doivent exécuter soit ESXi 6.7 ou plus récent pour l'OS invité Windows, soit ESXi 7.0 Update 2 pour l'OS invité Linux.

5. **Firmware EFI:** La machine virtuelle doit utiliser le firmware EFI pour le support vTPM.

6. **Privilèges requis:** Vérifiez que vous disposez des privilèges nécessaires pour les opérations cryptographiques afin d'ajouter et de gérer la vTPM. Les privilèges requis sont les suivants :
   - Opérations cryptographiques.Cloner
   - Opérations cryptographiques.Encrypt
   - Opérations cryptographiques.Encrypt new
   - Opérations cryptographiques.Migrate
   - Opérations cryptographiques.Enregistrer VM



## Ajout d'un module de plate-forme virtuelle de confiance (vTPM)

Suivez ces étapes pour ajouter un vTPM à votre machine virtuelle existante :

1. **Connectez-vous à vCenter Server:** Lancez vSphere Client et connectez-vous à vCenter Server.

2. **Ouvrez les paramètres de la machine virtuelle:** Localisez la machine virtuelle que vous souhaitez modifier dans l'inventaire sur le côté gauche de vSphere Client. Cliquez avec le bouton droit de la souris sur le nom de la machine virtuelle et sélectionnez "Edit Settings" (Modifier les paramètres).

3. **Dans la boîte de dialogue "Edit Settings" (Modifier les paramètres), cliquez sur le bouton "Add New Device" (Ajouter un nouveau dispositif). Dans la liste des types de dispositifs, sélectionnez "Trusted Platform Module" (vTPM).

4. **Confirmez la sélection:** Cliquez sur le bouton "OK" pour ajouter le dispositif vTPM à la machine virtuelle.

5. **Vérifier l'ajout:** Après avoir ajouté avec succès le vTPM, l'onglet Résumé de la machine virtuelle inclura désormais "Virtual Trusted Platform Module" dans le volet Matériel de la VM.

______

## Avantages du module de plateforme virtuelle de confiance (vTPM)

L'activation d'un vTPM pour votre machine virtuelle offre plusieurs avantages significatifs :

1. **Sécurité renforcée:** Le vTPM crée une puce TPM 2.0 virtualisée pour la machine virtuelle, offrant des fonctions de sécurité matérielles telles que le démarrage sécurisé et les opérations cryptographiques. Cela renforce la sécurité du système d'exploitation invité.

2. **Attestation de plate-forme:** vTPM permet à la machine virtuelle de générer une mesure cryptographique de son propre état, permettant l'attestation de plate-forme. Cette fonction permet de vérifier l'intégrité de la machine virtuelle et de s'assurer qu'elle n'a pas été altérée.

3. **Prise en charge du cryptage BitLocker:** Si vous utilisez un système d'exploitation invité Windows, l'activation de vTPM est une condition préalable à l'utilisation du cryptage BitLocker sur les disques de la machine virtuelle. Cela ajoute une couche supplémentaire de protection des données.



## Conclusion

L'implémentation d'un module de plateforme virtuelle de confiance (vTPM) pour une machine virtuelle existante est une étape cruciale pour renforcer la sécurité de votre infrastructure virtualisée. En suivant la procédure décrite et en veillant à ce que toutes les conditions préalables soient remplies, vous pouvez activer des fonctions de sécurité améliorées, l'attestation de plate-forme et la prise en charge du chiffrement BitLocker pour vos systèmes d'exploitation invités.

N'oubliez pas de vous référer à la documentation officielle de VMware pour obtenir des détails spécifiques concernant votre version et votre configuration de vSphere.

______

## Références

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)


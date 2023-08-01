---
title: "Verbeter de beveiliging van virtuele machines met vTPM: Stap-voor-stap handleiding"
date: 2023-09-02
toc: true
draft: false
description: "Verbeter de beveiliging van virtuele machines met behulp van vTPM met onze uitgebreide stap-voor-stap handleiding, die ondersteuning biedt voor platform-attestatie en BitLocker-encryptie."
genre: ["Cyberbeveiliging", "Virtualisatie", "VMware", "vSphere", "Beveiliging", "Vertrouwde platformmodule", "vTPM", "Gast OS", "Encryptie", "Platform Attest"]
tags: ["Virtuele vertrouwensplatformmodule", "vTPM Guide", "Verbeterde VM-beveiliging", "Platform Attest", "BitLocker-codering", "VMware vSphere", "Beveiliging van virtualisatie", "Cyberbeveiliging", "Bescherming gastbesturingssysteem", "VM-hardware", "TPM 2.0", "Beveiligd opstarten", "Cryptografische bewerkingen", "Best practices voor VM-beveiliging", "vCenter Server", "ESXi hosts", "EFI-firmware", "Belangrijke leverancier", "VMware-documentatie", "Windows server", "Windows 7", "Linux OS", "VM-configuratie beveiligen", "Beveiligingsfuncties", "vSphere-client", "Virtuele chip", "Gegevensbescherming", "Sabotagedetectie", "VM-integriteitsverificatie", "VMware Beveiliging"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "Een symbolische illustratie van een virtuele machine met een blinkend slot, die een verbeterde beveiliging via vTPM voorstelt."
coverCaption: "Ontgrendel ongekende VM-beveiliging!"
---

## Virtuele Trusted Platform Module inschakelen voor een bestaande virtuele machine

Virtual Trusted Platform Module (vTPM) is een kritieke beveiligingsfunctie die de beveiliging verbetert van gastbesturingssystemen die op virtuele machines worden uitgevoerd. Dit artikel leidt je door het proces van het toevoegen van een vTPM aan een bestaande virtuele machine in een VMware vSphere-omgeving, met stapsgewijze instructies en belangrijke overwegingen voor een naadloze implementatie.

______

## Vereisten

Voordat u verder gaat met het toevoegen van een vTPM aan uw virtuele machine, moet u ervoor zorgen dat u aan de volgende voorwaarden voldoet:

1. **VSphere-omgeving met keyprovider:** Zorg ervoor dat je vSphere-omgeving geconfigureerd is voor een keyprovider. Deze stap is cruciaal voor het veilig beheren van cryptografische operaties. Raadpleeg de [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html) voor gedetailleerde richtlijnen.

2. **Ondersteund gastbesturingssysteem:** Controleer of uw gastbesturingssysteem compatibel is met vTPM. VMware vTPM is compatibel met TPM 2.0 en ondersteunt Windows Server 2008 en hoger, Windows 7 en hoger en verschillende Linux-distributies.

3. **Status virtuele machine:** Zorg ervoor dat de virtuele machine die u wilt wijzigen uitgeschakeld is voordat u doorgaat met het toevoegen van de vTPM.

4. **De ESXi-hosts in uw omgeving moeten ofwel ESXi 6.7 of later voor Windows gastsysteem of ESXi 7.0 Update 2 voor Linux gastsysteem draaien.

5. **De virtuele machine moet EFI-firmware gebruiken voor ondersteuning van vTPM.

6. **Verplichte privileges:** Controleer of u de benodigde privileges hebt voor cryptografische bewerkingen om de vTPM toe te voegen en te beheren. De vereiste rechten omvatten:
   - Cryptografische bewerkingen.klonen
   - Cryptografische bewerkingen.coderen
   - Cryptografische bewerkingen.Nieuw coderen
   - Cryptografische bewerkingen.Migreren
   - Cryptografische bewerkingen.VM registreren

______
{{< inarticle-dark >}}
______

## Virtuele vertrouwensplatformmodule (vTPM) toevoegen

Volg deze stappen om een vTPM toe te voegen aan uw bestaande virtuele machine:

1. **Verbind met vCenter Server:** Start de vSphere Client en log in op uw vCenter Server.

2. **Open Instellingen virtuele machine:** Zoek de virtuele machine die u wilt wijzigen in de inventaris aan de linkerkant van de vSphere Client. Klik met de rechtermuisknop op de naam van de virtuele machine en selecteer "Instellingen bewerken".

3. **Trusted Platform Module toevoegen:** Klik in het dialoogvenster "Instellingen bewerken" op de knop "Nieuw apparaat toevoegen". Selecteer in de lijst met apparaattypen "Trusted Platform Module" (vTPM).

4. **Klik op de knop "OK" om het vTPM-apparaat toe te voegen aan de virtuele machine.

5. **Verifieer toevoeging:** Nadat de vTPM met succes is toegevoegd, bevat het tabblad Overzicht van de virtuele machine nu "Virtual Trusted Platform Module" in het deelvenster VM-hardware.

______

## Voordelen van de Virtuele Vertrouwde Platformmodule (vTPM)

Het inschakelen van een vTPM voor je virtuele machine biedt een aantal belangrijke voordelen:

1. **Verhoogde beveiliging:** De vTPM creëert een gevirtualiseerde TPM 2.0 chip voor de virtuele machine en biedt hardware-gebaseerde beveiligingsfuncties zoals veilig opstarten en cryptografische bewerkingen. Dit versterkt de beveiliging van het gastbesturingssysteem.

2. **Platform attestatie:** Met vTPM kan de virtuele machine een cryptografische meting van zijn eigen toestand genereren, waardoor platform attestatie mogelijk wordt. Deze functie helpt de integriteit van de VM te verifiëren en verzekert dat er niet mee geknoeid is.

3. **BitLocker-coderingsondersteuning:** Als je een Windows gastbesturingssysteem draait, is het inschakelen van vTPM een voorwaarde voor het gebruik van BitLocker-codering op schijven van virtuele machines. Dit voegt een extra laag van gegevensbescherming toe.

______
{{< inarticle-dark >}}
______

## Conclusie

Het implementeren van een Virtual Trusted Platform Module (vTPM) voor een bestaande virtuele machine is een cruciale stap in het versterken van de beveiliging van je gevirtualiseerde infrastructuur. Door de beschreven procedure te volgen en ervoor te zorgen dat aan alle voorwaarden is voldaan, kunt u verbeterde beveiligingsfuncties, platformattestatie en ondersteuning voor BitLocker-encryptie inschakelen voor uw gastbesturingssystemen.

Vergeet niet de officiële VMware documentatie te raadplegen voor specifieke details met betrekking tot uw vSphere versie en configuratie.

______

## Referenties

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)


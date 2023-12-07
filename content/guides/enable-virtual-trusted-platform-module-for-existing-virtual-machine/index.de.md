---
title: "Erhöhen Sie die Sicherheit virtueller Maschinen mit vTPM: Schritt-für-Schritt-Anleitung"
date: 2023-09-02
toc: true
draft: false
description: "Erhöhen Sie die Sicherheit virtueller Maschinen mit vTPM mit unserer umfassenden Schritt-für-Schritt-Anleitung, die Plattform-Attestierung und BitLocker-Verschlüsselungsunterstützung bietet."
genre: ["Cybersecurity", "Virtualisierung", "VMware", "vSphere", "Sicherheit", "Vertrauenswürdiges Plattformmodul", "vTPM", "Guest OS", "Verschlüsselung", "Plattform-Bescheinigung"]
tags: ["Virtuelles vertrauenswürdiges Plattformmodul", "vTPM-Leitfaden", "Verbesserte VM-Sicherheit", "Plattform-Bescheinigung", "BitLocker-Verschlüsselung", "VMware vSphere", "Sicherheit der Virtualisierung", "Cybersecurity", "Guest OS Protection", "VM-Hardware", "TPM 2.0", "Sicherer Start", "Kryptographische Operationen", "Best Practices für VM-Sicherheit", "vCenter Server", "ESXi-Hosts", "EFI-Firmware", "Schlüsselanbieter", "VMware-Dokumentation", "Windows-Server", "Windows 7", "Linux OS", "Sichere VM-Konfiguration", "Sicherheitsmerkmale", "vSphere-Client", "Virtueller Chip", "Datenschutz", "Manipulationsdetektion", "Überprüfung der VM-Integrität", "VMware-Sicherheit"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "Eine symbolische Darstellung einer virtuellen Maschine mit einem glänzenden Schloss, das für die erhöhte Sicherheit durch vTPM steht."
coverCaption: "Schalten Sie eine beispiellose VM-Sicherheit frei!"
---

## Virtuelles Trusted Platform Module für eine vorhandene virtuelle Maschine aktivieren

Das Virtual Trusted Platform Module (vTPM) ist eine wichtige Sicherheitsfunktion, die die Sicherheit von Gastbetriebssystemen, die auf virtuellen Maschinen ausgeführt werden, erhöht. Dieser Artikel führt Sie durch den Prozess des Hinzufügens eines vTPM zu einer vorhandenen virtuellen Maschine in einer VMware vSphere-Umgebung und bietet schrittweise Anleitungen und wichtige Überlegungen, um eine reibungslose Implementierung zu gewährleisten.

______

## Voraussetzungen

Bevor Sie mit dem Hinzufügen eines vTPM zu Ihrer virtuellen Maschine fortfahren, müssen Sie sicherstellen, dass Sie die folgenden Voraussetzungen erfüllen:

1. **vSphere-Umgebung mit Key Provider:** Stellen Sie sicher, dass Ihre vSphere-Umgebung für einen Key Provider konfiguriert ist. Dieser Schritt ist für die sichere Verwaltung kryptografischer Vorgänge von entscheidender Bedeutung. Lesen Sie die [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html) für eine ausführliche Anleitung.

2. **Unterstütztes Gastbetriebssystem:** Überprüfen Sie, ob Ihr Gastbetriebssystem mit vTPM kompatibel ist. VMware vTPM ist mit TPM 2.0 kompatibel und unterstützt Windows Server 2008 und höher, Windows 7 und höher sowie verschiedene Linux-Distributionen.

3. **Status der virtuellen Maschine:** Stellen Sie sicher, dass die virtuelle Maschine, die Sie ändern möchten, ausgeschaltet ist, bevor Sie mit dem Hinzufügen von vTPM fortfahren.

4. **ESXi-Host-Version:** Auf den ESXi-Hosts in Ihrer Umgebung muss entweder ESXi 6.7 oder höher für Windows-Gastbetriebssysteme oder ESXi 7.0 Update 2 für Linux-Gastbetriebssysteme ausgeführt werden.

5. **EFI-Firmware:** Die virtuelle Maschine muss EFI-Firmware für vTPM-Unterstützung verwenden.

6. **Erforderliche Berechtigungen:** Stellen Sie sicher, dass Sie über die erforderlichen Berechtigungen für kryptografische Operationen verfügen, um das vTPM hinzuzufügen und zu verwalten. Zu den erforderlichen Berechtigungen gehören:
   - Kryptografische Operationen.Klonen
   - Kryptografische Vorgänge.Verschlüsseln
   - Kryptografische Vorgänge.Verschlüsseln neu
   - Kryptografische Vorgänge.Migrieren
   - Verschlüsselungsvorgänge.VM registrieren



## Hinzufügen des virtuellen vertrauenswürdigen Plattformmoduls (vTPM)

Führen Sie diese Schritte aus, um ein vTPM zu Ihrer bestehenden virtuellen Maschine hinzuzufügen:

1. **Verbinden Sie sich mit vCenter Server:** Starten Sie den vSphere Client und melden Sie sich bei Ihrem vCenter Server an.

2. **Öffnen Sie die Einstellungen der virtuellen Maschine:** Suchen Sie die virtuelle Maschine, die Sie ändern möchten, im Inventar auf der linken Seite des vSphere-Clients. Klicken Sie mit der rechten Maustaste auf den Namen der virtuellen Maschine und wählen Sie "Einstellungen bearbeiten".

3. **Add Trusted Platform Module:** Klicken Sie im Dialogfeld "Einstellungen bearbeiten" auf die Schaltfläche "Neues Gerät hinzufügen". Wählen Sie aus der Liste der Gerätetypen "Trusted Platform Module" (vTPM).

4. **Auswahl bestätigen:** Klicken Sie auf die Schaltfläche "OK", um das vTPM-Gerät zur virtuellen Maschine hinzuzufügen.

5. **Hinzufügung überprüfen:** Nach dem erfolgreichen Hinzufügen des vTPM wird auf der Registerkarte "Zusammenfassung" der virtuellen Maschine im Bereich "VM-Hardware" nun "Virtual Trusted Platform Module" angezeigt.

______

## Vorteile des virtuellen vertrauenswürdigen Plattformmoduls (vTPM)

Die Aktivierung eines vTPM für Ihre virtuelle Maschine bietet mehrere bedeutende Vorteile:

1. **Erhöhte Sicherheit:** Das vTPM erstellt einen virtualisierten TPM 2.0-Chip für die virtuelle Maschine und bietet hardwarebasierte Sicherheitsfunktionen wie sicheres Booten und kryptografische Operationen. Dies stärkt die Sicherheitslage des Gastbetriebssystems.

2. **Plattform-Attestierung:** vTPM ermöglicht es der virtuellen Maschine, eine kryptografische Messung ihres eigenen Zustands zu erstellen und damit eine Plattform-Attestierung zu ermöglichen. Mit dieser Funktion lässt sich die Integrität der virtuellen Maschine überprüfen und sicherstellen, dass sie nicht manipuliert wurde.

3. **Unterstützung der BitLocker-Verschlüsselung:** Wenn Sie ein Windows-Gastbetriebssystem ausführen, ist die Aktivierung von vTPM eine Voraussetzung für die Verwendung der BitLocker-Verschlüsselung auf den Festplatten der virtuellen Maschine. Dadurch wird eine zusätzliche Ebene des Datenschutzes geschaffen.



## Schlussfolgerung

Die Implementierung eines Virtual Trusted Platform Module (vTPM) für eine vorhandene virtuelle Maschine ist ein entscheidender Schritt zur Verbesserung der Sicherheit Ihrer virtualisierten Infrastruktur. Wenn Sie das beschriebene Verfahren befolgen und sicherstellen, dass alle Voraussetzungen erfüllt sind, können Sie erweiterte Sicherheitsfunktionen, Plattform-Attestierung und BitLocker-Verschlüsselungsunterstützung für Ihre Gastbetriebssysteme aktivieren.

Denken Sie daran, die offizielle VMware-Dokumentation zu Rate zu ziehen, um spezifische Details in Bezug auf Ihre vSphere-Version und -Konfiguration zu erfahren.

______

## Referenzen

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)


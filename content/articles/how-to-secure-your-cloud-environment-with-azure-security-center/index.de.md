---
title: "Sichern Sie Ihre Cloudumgebung mit Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Sichern Sie Azure-Workloads mit Microsoft Defender for Cloud. Prüfen Sie historische Azure-Security-Center-Begriffe, Empfehlungen, Richtlinien und Reaktionsschritte."
tags: ["Azure", "Security Center", "Cloudsicherheit", "Azure Sentinel", "Azure Defender", "Netzwerksicherheit", "Identitätsverwaltung", "Datensicherheit", "Bedrohungserkennung", "Bedrohungsreaktion", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Ein Schild zwischen Wolkensymbolen steht für eine sichere Cloudumgebung. Auf dem Schild befindet sich das Logo von Azure Security Center."
coverCaption: ""
---

**So schützen Sie Ihre Cloud-Umgebung mit Azure Security Center**

 Die Sicherung Ihrer Cloud-Umgebung ist unerlässlich, um die Daten, Anwendungen und Infrastruktur Ihres Unternehmens vor Bedrohungen zu schützen. Das **Azure Security Center** von Microsoft ist ein leistungsstarkes Tool, mit dem Sie Ihre Sicherheitslage stärken und potenzielle Risiken in Ihrer Azure-Umgebung schnell erkennen können. In diesem Artikel erfahren Sie, wie Sie Ihre Cloudumgebung mit Azure Security Center sichern, und behandeln die bewährten Methoden zum Implementieren verschiedener Sicherheitsfeatures. Darüber hinaus werden wir in diesem Artikel auf weitere technische Details und Beispiele eingehen, damit Sie besser verstehen, wie Sie Ihre Cloudumgebung mit Azure Security Center sichern können.

 ______

*Produktnamen haben sich seit der ursprünglichen Veröffentlichung geändert. Microsoft Azure Security Center heißt jetzt Microsoft Defender for Cloud. Azure Active Directory heißt jetzt Microsoft Entra ID. Azure Sentinel heißt jetzt Microsoft Sentinel. Azure Defender bezeichnet Defender-Pläne und Workload-Schutz in Defender for Cloud. Die älteren Namen bleiben unten erhalten, wo sie den Stand von 2023 beschreiben.*

Die aktuelle [Übersicht zu Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) beschreibt eine Cloud Native Application Protection Platform mit Cloud-Sicherheitsstatusverwaltung, DevSecOps und Cloud-Workload-Schutz. Verfügbarkeit und Lizenzierung hängen von Cloud, Ressourcentyp, Abonnement und Plan ab.

 ## Grundlegendes zu Azure Security Center

 Azure Security Center ist ein **unified Infrastructure Security Management System**, mit dem Sie potenzielle Schwachstellen in Ihrer Cloudumgebung identifizieren und beheben können. Es bietet mehrere Funktionen wie Bedrohungserkennung, Verwaltung des Sicherheitsstatus und Compliance-Verwaltung, um sicherzustellen, dass Ihre Azure-Umgebung immer sicher ist.

 **Kontinuierliche Sicherheitsbewertung** und **Erweiterter Bedrohungsschutz** sind zwei Hauptfunktionen von Azure Security Center. Continuous Security Assessment hilft Ihnen dabei, potenzielle Sicherheitsprobleme in Ihrer Umgebung zu identifizieren, während Advanced Threat Protection Sie dabei unterstützt, potenzielle Bedrohungen zu erkennen und darauf zu reagieren.

 ______

 ## Implementierung von Sicherheitsrichtlinien und Compliance-Standards

 Mit Azure Security Center können Sie Sicherheitsrichtlinien in Ihrer gesamten Cloudumgebung implementieren und verwalten. Sie können den Dienst **Azure Policy** verwenden, um benutzerdefinierte Sicherheitsrichtlinien zu erstellen, oder integrierte Richtlinien verwenden, um bewährte Vorgehensweisen und Compliance-Standards durchzusetzen. Sie können Ihre Sicherheitslage auch anhand von Industriestandards wie [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) und [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

 Azure Security Center bietet auch Compliance-Verwaltungsfunktionen, mit denen Sie den Compliance-Status Ihrer Organisation anhand verschiedener regulatorischer Rahmenbedingungen wie [DSGVO](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) und [PCI DSS](https://www.pcisecuritystandards.org/).

 ______

 ## Sichern Ihrer Azure-Ressourcen

 **Ressourcensicherheitshygiene** ist ein wichtiger Aspekt bei der Sicherung Ihrer Cloud-Umgebung. Azure Security Center bietet **Secure Score**, eine Messung Ihres Sicherheitsstatus, um Ihnen zu helfen, die Gesamtsicherheit Ihrer Ressourcen zu verstehen. Sie können Ihre Sicherheitsbewertung verbessern, indem Sie die Empfehlungen von Azure Security Center berücksichtigen.

 ### Netzwerksicherheit

 Die Implementierung geeigneter Netzwerksicherheitsmaßnahmen wie **Netzwerksicherheitsgruppen (NSGs)**, **Azure Firewall** und **Web Application Firewall (WAF)** ist entscheidend, um Ihre Azure-Umgebung vor potenziellen Bedrohungen zu schützen. Diese Tools helfen Ihnen, den eingehenden und ausgehenden Netzwerkverkehr zu kontrollieren und Ihre Ressourcen vor unbefugtem Zugriff und potenziellen Angriffen zu schützen.

 #### Netzwerksicherheitsgruppen (NSGs)

 NSGs fungieren als virtuelle Firewall für Ihre Azure-Ressourcen, sodass Sie Regeln definieren können, die den Netzwerkdatenverkehr zu und von Ihren Ressourcen zulassen oder verweigern. Sie können beispielsweise eine NSG mit Regeln erstellen, um bestimmten Datenverkehr zuzulassen oder abzulehnen:

```azurecli
# Netzwerksicherheitsgruppe erstellen
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Regeln zum Zulassen oder Blockieren von Datenverkehr hinzufügen
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```


 Weitere Informationen finden Sie in der offiziellen Dokumentation zu [Netzwerksicherheitsgruppen](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview). Das Beispiel erlaubt eingehenden TCP-Verkehr auf Port 80 aus allen IPv4-Quellen. Verwenden Sie im Produktivbetrieb einen bekannten Quellbereich, einen privaten Endpunkt oder einen Load-Balancer-Pfad. Lesen Sie vor der Übernahme des Beispiels die [aktuelle NSG-Sicherheitsübersicht](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview).

 #### Azure-Firewall
 Azure Firewall ist ein verwalteter, cloudbasierter Netzwerksicherheitsdienst, der Ihre Azure-Ressourcen schützt. Er bietet erweiterte Funktionen wie auf Bedrohungsinformationen basierende Filter, Webkategorien sowie zentralisierte Protokollierung und Analyse. Um die Azure Firewall zu nutzen, können Sie diese [Schnellstartanleitung](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep) befolgen.

 #### Web Application Firewall (WAF)
 Web Application Firewall (WAF) ist eine Funktion von **Azure Application Gateway**, die Ihre Webanwendungen vor bekannten Web-Exploits wie SQL-Injection, Cross-Site-Scripting und anderen Bedrohungen schützt. WAF lässt sich problemlos in Ihre vorhandenen Webanwendungen integrieren, und Sie können benutzerdefinierte Regeln zum Schutz vor bestimmten Angriffsmustern konfigurieren.

 Hier ist ein Beispiel dafür, wie Sie ein Application Gateway mit aktivierter WAF erstellen:

```azurecli
# WAF-Richtlinie erstellen
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Virtuelles Netzwerk und Subnetz erstellen
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Öffentliche IP-Adresse erstellen
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Application Gateway mit aktiviertem WAF erstellen
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```

 Erfahren Sie mehr über [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) in der offiziellen Dokumentation.

 ### Identitäts- und Zugriffsverwaltung

 **Azure Active Directory (Azure AD)** ist eine Komponente zur Sicherung Ihrer Cloud-Umgebung. Azure Security Center bietet Empfehlungen zur Verbesserung der Identitäts- und Zugriffsverwaltung, z. B. zum Aktivieren von **Multi-Factor Authentication (MFA)**, Implementieren von **Role-Based Access Control (RBAC)** und Überwachen verdächtiger Aktivitäten.

 #### Multi-Faktor-Authentifizierung (MFA)

 MFA fügt Ihren Azure AD-Konten eine zusätzliche Sicherheitsebene hinzu, damit Benutzer aufgefordert werden, zwei oder mehr Arten der Überprüfung bereitzustellen, bevor sie Zugriff gewähren. Sie können MFA für Ihre Organisation aktivieren, indem Sie der bereitgestellten [Schritt-für-Schritt-Anleitung](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) folgen von Microsoft.

 Beispiel: Aktivieren Sie MFA für einen Benutzer

```powershell
# Mit Azure AD verbinden
Connect-AzureAD

# MFA für einen bestimmten Benutzer aktivieren
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```


 #### Rollenbasierte Zugriffskontrolle (RBAC)
 Mit RBAC können Sie granulare Berechtigungen für Ihre Azure-Ressourcen definieren und sicherstellen, dass Benutzer über die entsprechende Zugriffsebene verfügen. Sie können Benutzern, Gruppen oder Anwendungen Rollen zuweisen, um deren Zugriff auf Ressourcen Ihrer Organisation zu verwalten. Um RBAC zu implementieren, folgen Sie dem [offiziellen Leitfaden](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) von Microsoft.

 Beispiel: Weisen Sie einem Benutzer eine Rolle zu

```azurecli
# Einem Benutzer die Rolle „Reader“ zuweisen
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```

 #### Überwachung verdächtiger Aktivitäten
 Azure AD bietet Funktionen wie **Identitätsschutz** und **bedingten Zugriff**, mit denen Sie verdächtige Aktivitäten überwachen und darauf reagieren können. Der Identitätsschutz nutzt Algorithmen des maschinellen Lernens, um Anomalien und riskante Anmeldeversuche zu erkennen. Mit dem bedingten Zugriff können Sie Richtlinien festlegen, die den Zugriff anhand von Faktoren wie Gerät, Standort und Risikostufe steuern.

 Folgen Sie zum Einrichten von Azure AD Identity Protection dem [offiziellen Leitfaden](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) von Microsoft.

 Beispiel: Erstellen Sie eine Richtlinie für bedingten Zugriff

```powershell
# Mit Azure AD verbinden
Connect-AzureAD

# Richtlinie für bedingten Zugriff (Conditional Access) erstellen
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Anmeldungen von Benutzern aus unbekannten Standorten blockieren."
$PolicyState = "Enabled"
$Conditions = @{
    "SignInRiskLevels" = @("medium","high");
    "Locations" = @{
        "Included" = @();
        "Excluded" = @("AllTrusted")
    }
}
$GrantControls = @{
    "Operator" = "OR";
    "BuiltInControls" = @("Block")
}
New-AzureADMSConditionalAccessPolicy -DisplayName $PolicyName -State $PolicyState -Conditions $Conditions -GrantControls $GrantControls -Description $PolicyDescription

```


 Erfahren Sie mehr über [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) und [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) in der offiziellen Dokumentation.


 ### Datensicherheit

 Der Schutz Ihrer Daten in der Cloud ist von entscheidender Bedeutung. Azure Security Center bietet mehrere Datensicherheitsfeatures wie **Azure Information Protection**, **Azure Storage Service Encryption** und **Azure Disk Encryption**. Diese Funktionen helfen Ihnen, den Zugriff auf Ihre Daten zu verschlüsseln und zu verwalten und sicherzustellen, dass vertrauliche Informationen sicher bleiben.

 #### Azure-Informationsschutz

 **Azure Information Protection (AIP)** ist eine Cloud-basierte Lösung, mit der Sie vertrauliche Dokumente und E-Mails klassifizieren, kennzeichnen und schützen können. AIP bietet eine Reihe integrierter Bezeichnungen wie „Vertraulich“ und „Persönlich“, die an die Anforderungen Ihrer Organisation angepasst werden können. Sie können AIP auch so konfigurieren, dass Labels basierend auf vordefinierten Regeln automatisch angewendet werden. Um mit AIP zu beginnen, folgen Sie dem [offiziellen Leitfaden](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection). Azure Information Protection ist ein historischer Produktname und laut aktueller Sentinel-Dokumentation veraltet. Prüfen Sie vor einer neuen Bereitstellung die Dokumentation zu Microsoft Purview Information Protection.

 Beispiel: Erstellen eines benutzerdefinierten Etiketts

```powershell
# Mit dem AIP-Dienst verbinden
Connect-AipService

# Benutzerdefiniertes Label mit Schutzeinstellungen erstellen
$LabelName = "Vertraulich - Nur interne Nutzung"
$LabelDescription = "Dieses Label wendet Verschlüsselung und eine Zugriffsrichtlinie ausschließlich für die interne Nutzung an."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```


 #### Azure Storage Service-Verschlüsselung
 **Azure Storage Service Encryption (SSE)** verschlüsselt automatisch Ihre ruhenden Daten in Azure Storage-Konten, einschließlich Blob-, Datei-, Tabellen- und Warteschlangenspeicher. SSE verwendet von Azure oder vom Kunden verwaltete Schlüssel, um die Verschlüsselung auf Speicherkontoebene bereitzustellen. Befolgen Sie zum Aktivieren von SSE die von Microsoft bereitgestellte [Schritt-für-Schritt-Anleitung](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption).

 Beispiel: Aktivieren Sie SSE für ein Speicherkonto

```azurecli
# SSE mit Azure-verwalteten Schlüsseln aktivieren
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```


 #### Azure Disk Encryption
 **Azure Disk Encryption** hilft Ihnen beim Sichern von Datenträgern virtueller Maschinen, indem sie mit BitLocker (Windows) oder dm-crypt (Linux) verschlüsselt werden. Die Verschlüsselungsschlüssel und Geheimnisse werden durch Azure Key Vault geschützt, wodurch sichergestellt wird, dass Ihre Daten im Ruhezustand geschützt sind. Folgen Sie zum Aktivieren von Azure Disk Encryption dem [offiziellen Leitfaden](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) von Microsoft.

 Beispiel: Aktivieren Sie Azure Disk Encryption für einen virtuellen Computer

```azurecli
# Azure Disk Encryption für eine Windows-VM aktivieren
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```

 Erfahren Sie mehr über [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) und [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) in der offiziellen Dokumentation.
 ______

 ## Bedrohungen erkennen und darauf reagieren

 Azure Security Center verwendet erweiterte Bedrohungserkennungsfunktionen, um potenzielle Bedrohungen zu identifizieren und Sie vor diesen zu warnen. Durch die Integration mit **Azure Sentinel** können Sie Sicherheitsvorfälle in Ihrer gesamten Umgebung überwachen, untersuchen und darauf reagieren.

 ### Bedrohungserkennung

 Azure Security Center verwendet **Azure Defender**, eine Reihe erweiterter Bedrohungserkennungsfunktionen, um potenzielle Sicherheitsbedrohungen zu identifizieren. Azure Defender überwacht Ihre Ressourcen auf Kompromittierungsindikatoren und stellt Warnungen und Empfehlungen bereit, damit Sie auf potenzielle Bedrohungen reagieren können. Folgen Sie zum Aktivieren von Azure Defender dem [offiziellen Leitfaden](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

 Beispiel: Aktivieren Sie Azure Defender für ein Abonnement

```azurecli
# Azure Defender für ein Abonnement aktivieren
az security auto-provisioning-setting update --name default --auto-provision on
```


 ### Reaktion auf Bedrohungen
 Wenn eine Bedrohung erkannt wird, müssen Sie schnell und wirksam reagieren. Azure Security Center bietet eine **Verwaltung von Sicherheitsvorfällen**, mit der Sie Sicherheitsvorfälle untersuchen und darauf reagieren können. Sie können auch **Azure Sentinel** integrieren, um automatisierte Playbooks zu erstellen und Ihre Reaktion auf Sicherheitsvorfälle zu koordinieren. Erfahren Sie mehr über die Integration von Azure Security Center in Azure Sentinel in der **offiziellen Dokumentation**.

 Beispiel: Erstellen Sie ein Logik-App-Playbook für Azure Sentinel

```azurecli
# Ressourcengruppe erstellen
az group create --name MyResourceGroup --location EastUS

# Eine Logic App erstellen
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```

 Die Datei `playbook-definition.json` sollte die Playbook-Definition von Logic App enthalten. Beispiele für Playbooks für Azure Sentinel finden Sie im [Azure-Sentinel GitHub-Repository](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

 Durch die Nutzung der Bedrohungserkennungsfunktionen von Azure Security Center und die Integration in Azure Sentinel können Sie eine robuste Sicherheitsstrategie erstellen, um Bedrohungen in Ihrer Azure-Umgebung zu erkennen und darauf zu reagieren. Erfahren Sie mehr über [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) und [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) in der offiziellen Dokumentation.
 ______


  Der [Defender-for-Cloud-Connector](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) leitet Warnungen an Microsoft Sentinel weiter. Prüfen Sie Connector, Datensammlungs- und Analyseregeln sowie den Vorfallablauf, bevor Sie Automatisierung einsetzen.

## Überwachung und Berichterstattung

Überwachung und Berichterstellung sind wichtige Bestandteile einer sicheren Cloud-Umgebung. Azure Security Center bietet dafür mehrere Tools, darunter **Sicherheitsdashboard**, **Sicherheitswarnungen** und **Konformitätsberichte**.

### Sicherheits-Dashboard

 Das Sicherheitsdashboard im Azure Security Center bietet einen umfassenden Überblick über Ihren Sicherheitsstatus. Es zeigt Ihre Sicherheitsbewertung, Sicherheitsempfehlungen und aktive Sicherheitswarnungen an. Das Dashboard bietet auch Einblicke in Ihren Compliance-Status und ermöglicht es Ihnen, Ihren Fortschritt im Laufe der Zeit zu verfolgen.

 ### Sicherheitswarnungen

 Azure Security Center generiert Sicherheitswarnungen, wenn potenzielle Bedrohungen erkannt werden. Diese Warnungen bieten detaillierte Informationen über die Bedrohung sowie Empfehlungen zur Minderung des Risikos. Sie können Azure Security Center so konfigurieren, dass Benachrichtigungen per E-Mail oder SMS gesendet oder in Tools von Drittanbietern wie [Slack](https://slack.com/) oder [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

 ### Compliance-Berichte

 Mit Azure Security Center können Sie Konformitätsberichte für verschiedene regulatorische Frameworks wie GDPR, HIPAA und PCI DSS generieren. Diese Berichte helfen Ihnen, den Compliance-Status Ihres Unternehmens zu verfolgen und Bereiche zu identifizieren, die verbessert werden müssen.

 ______

 ## bewährte Vorgehensweisen für Azure Security Center

 Um Azure Security Center optimal zu nutzen, sollten Sie die folgenden bewährte Vorgehensweisen implementieren:

 1. **Azure Security Center für alle Ihre Abonnements aktivieren**: Das Sicherstellen, dass alle Ihre Azure-Abonnements durch das Azure Security Center geschützt sind, ist entscheidend für die Erstellung einer sicheren Cloudumgebung.
 2. **Überprüfen Sie regelmäßig Ihre Sicherheitsbewertung**: Die Überwachung Ihrer Sicherheitsbewertung hilft Ihnen, Ihre allgemeine Sicherheitslage zu verstehen und Bereiche zu identifizieren, die verbessert werden müssen.
 3. **Implementieren Sie Sicherheitsempfehlungen**: Die Umsetzung der Sicherheitsempfehlungen von Azure Security Center hilft Ihnen, Ihren Sicherheitsstatus zu verbessern und potenzielle Risiken zu reduzieren.
 4. **Sicherheitswarnungen überwachen**: Überprüfen Sie regelmäßig Sicherheitswarnungen und reagieren Sie darauf, um potenzielle Bedrohungen zu mindern und eine Umgebung aufrechtzuerhalten.
 5. **Halten Sie sich bei Compliance-Anforderungen auf dem Laufenden**: Stellen Sie sicher, dass Ihr Unternehmen die neuesten regulatorischen Rahmenbedingungen einhält, indem Sie Ihre Compliance-Richtlinien regelmäßig überprüfen und aktualisieren.

 ______
## Aktueller Defender-for-Cloud-Ablauf

Verwenden Sie für eine aktuelle Bereitstellung die folgende Reihenfolge. Die Namen in den älteren Abschnitten helfen weiterhin bei historischen Suchen. Im Portal und in der Dokumentation wird die Terminologie von Defender for Cloud verwendet.

1. **Abonnements und Connectors erfassen.** Dokumentieren Sie Azure-Abonnements, AWS- oder GCP-Connectors, DevOps-Projekte und kritische Ressourcen.
2. **Erforderliche Defender-Pläne aktivieren.** Wählen Sie Pläne passend zu den Workloads aus und prüfen Sie die Lizenzierung, bevor Sie sie für Produktionsabonnements aktivieren.
3. **Cloud Secure Score und Empfehlungen prüfen.** Priorisieren Sie Internetexposition, Identitätsrisiken, ausnutzbare Schwachstellen und fehlende Protokollierung. Ein Score belegt keine vollständige Compliance.
4. **Microsoft-Entra-Kontrollen konfigurieren.** Verlangen Sie phishingresistente MFA für wichtige Konten, verwenden Sie RBAC nach dem Prinzip der geringsten Rechte und prüfen Sie privilegierte Zugriffe.
5. **Warnungen an Microsoft Sentinel senden.** Prüfen Sie Warnungsaufnahme, Analyseregeln, Zuständigkeit, Antwortautomatisierung und Aufbewahrung.
6. **Nach Änderungen erneut prüfen.** Prüfen Sie Empfehlungen nach Patches, Architekturänderungen, neuen Connectors oder Planänderungen.

## Praktische Prüfliste

- **Identität:** Entfernen Sie veraltete Konten, reduzieren Sie dauerhafte Administratorrechte und prüfen Sie Ausnahmen für Conditional Access.
- **Netzwerk:** Entfernen Sie öffentlich erreichbare Verwaltungsports, begrenzen Sie NSG-Quellbereiche und prüfen Sie, ob Firewall- und WAF-Protokolle den Überwachungsarbeitsbereich erreichen.
- **Daten:** Klassifizieren Sie sensible Datenspeicher, prüfen Sie Verschlüsselung und Schlüsselverwaltung und testen Sie die Wiederherstellung von Sicherungen.
- **Erkennung:** Prüfen Sie Warnungsschwere, Benachrichtigungswege, Zuständigkeit für Vorfälle und Antwort-Playbooks.
- **Governance:** Ordnen Sie jeder Richtlinieninitiative eine verantwortliche Person, ein Ablaufdatum für Ausnahmen und Nachweise zum geforderten Rahmenwerk zu.


 ## Verweise
- [Azure Security Center-Dokumentation](https://docs.microsoft.com/en-us/azure/security-center/)
- [Azure Policy-Dienst](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [DSGVO](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI-DSS](https://www.pcisecuritystandards.org/)


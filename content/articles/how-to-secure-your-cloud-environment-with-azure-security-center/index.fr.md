---
title: "Centro de Seguridad Azure: Guía completa para salvaguardar su entorno en la nube"
date: 2023-04-10
toc: true
draft: false
descripción: "Aprenda a proteger su entorno en la nube utilizando Azure Security Center, con las mejores prácticas y ejemplos del mundo real."
tags: ["Azure", "Security Center", "seguridad en la nube", "Azure Sentinel", "Azure Defender", "seguridad de red", "gestión de identidades", "seguridad de datos", "detección de amenazas", "respuesta a amenazas", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"].
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.png"
coverAlt: "Un icono de escudo rodeado de símbolos de nube, que representa un entorno de nube seguro, con el logotipo de Azure Security Center en el escudo."
coverCaption: ""
---
```azurecli
# Crear un grupo de seguridad de red
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Añadir reglas para permitir o denegar tráfico
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
```azurecli
# Crear una política WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Crear una red virtual y una subred
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Crear una dirección IP pública
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Crear un Application Gateway con WAF habilitado
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
```powershell
# Conectar a Azure AD
Conectar-AzureAD

# Habilitar MFA para un usuario específico
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Ubicación"=""; "FactorSatisfacción"="2"; "MétodoVerificación"="1"};@{"Ubicación"=""; "FactorSatisfacción"="2"; "MétodoVerificación"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
```azurecli
# Asignar un rol de Lector a un usuario
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
```powershell
# Conectarse a Azure AD
Conectar-AzureAD

# Crear una política de acceso condicional
$PolicyName = "BloquearInicioDeSesiónDesdeLugaresDesconocidos"
$PolicyDescription = "Bloquear inicios de sesión para usuarios de ubicaciones desconocidas".
$PolicyState = "Activado"
$Conditions = @{
    "SignInRiskLevels" = @("medio", "alto");
    "Ubicaciones" = @{
        "Incluido" = @();
        "Excluidos" = @("TodosConfiados")
    }
}
$GrantControls = @{
    "Operador" = "OR";
    "BuiltInControls" = @("Block")
}
New-AzureADMSConditionalAccessPolicy -DisplayName $PolicyName -State $PolicyState -Conditions $Conditions -GrantControls $GrantControls -Description $PolicyDescription

```
```powershell
# Connect to the AIP service
Connect-AipService

# Crear una etiqueta personalizada con la configuración de protección
$LabelName = "Sensible - Sólo para uso interno"
$LabelDescription = "Esta etiqueta aplica cifrado y una política de acceso sólo para uso interno."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=Ver", "domain\GroupB=Ver,Editar,Imprimir")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
```azurecli
# Habilitar SSE usando claves gestionadas por Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
```azurecli
# Habilitar el cifrado de disco Azure para una máquina virtual Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
```azurecli
# Habilitar Azure Defender para una suscripción
az security auto-provisioning-setting update --name default --auto-provision on
```
Azurecli
# Crear un grupo de recursos
az group create --name MyResourceGroup --location EastUS

# Crear una aplicación lógica
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```

**Cómo proteger su entorno en la nube con Azure Security Center** La seguridad de su entorno en la nube es esencial para proteger los datos, las aplicaciones y la infraestructura de su organización frente a las amenazas. **Azure Security Center** de Microsoft es una potente herramienta que le ayudará a reforzar su postura de seguridad y a identificar rápidamente los riesgos potenciales en su entorno Azure. En este artículo, explicamos cómo proteger su entorno de nube con la ayuda de Azure Security Center y explicamos las mejores prácticas para poner en marcha diversas funciones de seguridad. Además, en este artículo, ofrecemos más detalles técnicos y ejemplos para ayudarle a comprender mejor cómo proteger su entorno en la nube con la ayuda de Azure Security Center. ______ ## Comprender Azure Security Center Azure Security Center es un **sistema unificado de gestión de la seguridad de la infraestructura** que le ayudará a identificar y resolver las vulnerabilidades potenciales de su entorno en la nube. Ofrece varias funciones, como la detección de amenazas, la gestión de la postura de seguridad y la gestión de la conformidad, para garantizar que su entorno Azure esté siempre protegido. **La evaluación continua de la seguridad y la protección avanzada frente a amenazas son dos funciones clave de Azure Security Center. La evaluación continua de la seguridad le ayuda a identificar los problemas de seguridad potenciales en su entorno, mientras que la protección avanzada frente a amenazas le ayuda a detectar y responder a las amenazas potenciales. ______ ## Mise en œuvre des politiques de sécurité et des normes de conformité Azure Security Center vous permet d'implémenter et de gérer des politiques de sécurité dans votre environnement cloud. Puede utilizar el servicio **Azure Policy** para crear políticas de seguridad personalizadas o utilizar políticas integradas para aplicar las buenas prácticas y las normas de conformidad. También puede evaluar su postura de seguridad en relación con las normas del sector, como [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final ), [CIS]( https://www.cisecurity.org/) e [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html). Azure Security Center también ofrece funciones de gestión de la conformidad que le permiten supervisar el estado de conformidad de su organización en relación con diversos marcos normativos, como [RGPD](https://gdpr.eu/), [HIPAA ](https://www.hhs.gov/hipaa/index.html) y [PCI DSS](https://www.pcisecuritystandards.org/). ______ ## Sécuriser vos ressources Azure **L'hygiène de la sécurité des ressources** est un aspect important de la sécurisation de votre environnement cloud. Azure Security Center proporciona **Secure Score**, una medición de su estado de seguridad, para ayudarle a comprender la seguridad global de sus recursos. Puede mejorar su puntuación de seguridad siguiendo las recomendaciones de Azure Security Center. ### Sécurité Internet La puesta en marcha de medidas de seguridad en red mejoradas, como los **grupos de seguridad en red (NSG)**, el **pare-feu Azure** y el **pare-feu de aplicaciones Web (WAF)* *, es esencial para proteger su entorno Azure contra las amenazas potenciales. Estas herramientas le permiten controlar el tráfico de red entrante y saliente, protegiendo sus recursos frente a ataques potenciales y no autorizados. #### Grupos de seguridad de red (NSG) Los NSG son como un paraguas virtual para sus recursos Azure, que le permiten definir las normas que autorizan o deniegan el tráfico de red hacia y desde sus recursos. Por ejemplo, puede crear un NSG con reglas para autorizar o denegar un tráfico específico: Más información sobre los [grupos de seguridad de red] (https://docs.microsoft.com/en-us/azure/virtual-network /security-overview) en la documentación oficial. #### Pare-feu Azure El pare-feu Azure es un servicio de seguridad de red gestionado basado en la nube que protege sus recursos Azure. Ofrece funciones avanzadas como el filtrado basado en la información sobre amenazas, las categorías web y el registro y análisis centralizados. Para configurar el parámetro Azure, puedes seguir estas [instrucciones de configuración rápida](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep). #### Pare-feu d'application Web (WAF) El pare-feu d'application Web (WAF) es una funcionalidad de **Azure Application Gateway** que protege sus aplicaciones Web contra los exploits Web habituales como la inyección SQL, los scripts intersitio y otras amenazas. WAF puede integrarse fácilmente en sus aplicaciones Web existentes y puede configurar reglas personalizadas para protegerle frente a modelos de ataque específicos. Vea un ejemplo de creación de Application Gateway con WAF activado: Más información sobre [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview ) en la documentación oficial. ### Gestion des identités et des accès **Azure Active Directory (Azure AD)** est un composant essentiel de la sécurisation de votre environnement cloud. Azure Security Center proporciona recomendaciones para mejorar la gestión de identidades y accesos, tales como la activación de la **autenticación multifactor (MFA)**, la puesta en marcha del **control de acceso basado en roles ( RBAC)** y la vigilancia de actividades sospechosas. #### Authentification multifacteur (MFA) MFA añade una capa de seguridad adicional a tus cuentas Azure AD al exigir a los usuarios que proporcionen al menos dos formas de verificación antes de permitir el acceso. Puede activar MFA para su organización siguiendo la [guía paso a paso](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) proporcionada por Microsoft. Ejemplo: Activer MFA pour un utilisateur #### Control de acceso basado en roles (RBAC) RBAC te permite definir autorizaciones granulares para tus recursos Azure, garantizando que los usuarios dispongan del nivel de acceso apropiado. Puedes asignar roles a usuarios, grupos o aplicaciones para gestionar su acceso a los recursos de tu organización. Para implementar RBAC, siga la [guía oficial](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) de Microsoft. Ejemplo: Atribuir un rol a un usuario #### La supervisión de actividades sospechosas Azure AD proporciona funciones como **Protección de identidad** y **Acceso condicional** que permiten supervisar y responder a actividades sospechosas. Identity Protection utiliza algoritmos de aprendizaje automático para detectar anomalías e intentos de conexión peligrosos, mientras que el acceso condicional le permite definir políticas que controlan el acceso en función de factores como el dispositivo, la ubicación y el nivel de riesgo. Para configurar Azure AD Identity Protection, consulte la [guía oficial](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) de Microsoft. Ejemplo: crear una estrategia de acceso condicional Para saber más sobre [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) y [Conditional Access ](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) en la documentación oficial. ### Sécurité des données La protección de sus datos en la nube es crucial. Azure Security Center ofrece varias funciones de seguridad de datos, como **Azure Information Protection**, **Azure Storage Service Encryption** y **Azure Disk Encryption**. Estas funciones te permiten registrar y proteger el acceso a tus datos, garantizando así la seguridad de la información sensible. #### Protección de la información Azure **Azure Information Protection (AIP)** es una solución basada en la nube que te ayuda a clasificar, etiquetar y proteger los documentos y correos electrónicos confidenciales. AIP proporciona un conjunto de etiquetas integradas, como "Confidencial" y "Personal", que pueden personalizarse en función de las necesidades de su organización. También puede configurar AIP para que aplique automáticamente etiquetas en función de reglas predefinidas. Para trabajar con AIP, consulte la [guía oficial](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection). Ejemplo: Creación de una etiqueta personalizada #### Cifrado del servicio de almacenamiento Azure **Azure Storage Service Encryption (SSE**) cifra automáticamente sus datos a la espera en las cuentas de almacenamiento Azure, incluyendo el almacenamiento de Blob, Archivo, Tabla y archivo de espera. SSE utiliza claves proporcionadas por Azure o claves proporcionadas por el cliente para garantizar el recuento a nivel de la cuenta de almacenamiento. Para activar SSE, siga la [guía paso a paso](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) proporcionada por Microsoft. Ejemplo: Activar SSE para un equipo de almacenamiento #### Cifrado de disco Azure **Azure Disk Encryption** te ayuda a proteger los discos de las máquinas virtuales cifrándolos con BitLocker (Windows) o dm-crypt (Linux). Azure Key Vault protege las claves y los secretos, garantizando la seguridad de tus datos en el repositorio. Para activar Azure Disk Encryption, sigue la [guía oficial](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) de Microsoft. Ejemplo: Activar Azure Disk Encryption en una máquina virtual Más información sobre [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [ Azure Storage Service Encryption](https:// docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) y [Azure Disk Encryption](https://learn.microsoft.com/en -us/azure/virtual-machines/disk-encryption-overview) en la documentación oficial. ______ ## Détecter et répondre aux menaces Azure Security Center utilise des fonctionnalités avancées de détection des menaces pour identifier et vous alerter des menaces potentielles. Si se conecta a **Azure Sentinel**, podrá vigilar, investigar y responder a incidentes de seguridad en todo su entorno. ### Detección de amenazas Azure Security Center utiliza **Azure Defender**, un conjunto de opciones avanzadas de detección de amenazas, para identificar las amenazas de seguridad potenciales. Azure Defender vigila sus recursos en busca de indicadores de peligro y proporciona alertas y recomendaciones para ayudarle a responder a las amenazas potenciales. Para activar Azure Defender, siga la [guía oficial](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable). Ejemplo: Activar Azure Defender para un suscriptor ### Respuesta a amenazas Cuando se detecta una amenaza, es esencial responder de forma rápida y eficaz. Azure Security Center proporciona la gestión de **incidentes de seguridad**, que le ayudará a investigar los incidentes de seguridad y a responder a ellos. También puede integrar **Azure Sentinel** para crear guías automáticas y organizar su respuesta a incidentes de seguridad. Más información sobre la integración de Azure Security Center con Azure Sentinel en la **documentación oficial**. Ejemplo: Creación de un playbook de lógica de aplicación para Azure Sentinel El archivo `playbook-definition.json` debe contener la definición del playbook de lógica de aplicación. Puedes encontrar ejemplos de playbooks para Azure Sentinel en la [referencia Azure-Sentinel GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks). Al aprovechar parte de las capacidades de detección de amenazas de Azure Security Center e integrar Azure Sentinel, puede crear una estrategia de seguridad sólida para detectar y responder a las amenazas en su entorno Azure. Más información sobre [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) y [Azure Sentinel](https://docs.microsoft .com/en-us/azure/sentinel/overview) en la documentación oficial. ______ ## Surveillance et rapports La vigilancia y la creación de informes son elementos esenciales del mantenimiento de un entorno cloud seguro. Azure Security Center proporciona varias herramientas de vigilancia y creación de informes, como **Tabla de bordes de seguridad**, **Alertas de seguridad** y **Informes de conformidad**. ### Tabla de seguridad La tabla de seguridad de Azure Security Center ofrece una visión completa de su estado de seguridad. Muestra su puntuación de seguridad, recomendaciones de seguridad y alertas de seguridad activas. El cuadro de mando también proporciona información sobre su estado de conformidad y le permite seguir sus progresos a lo largo del tiempo. ### Alertas de seguridad Azure Security Center genera alertas de seguridad cuando se detectan amenazas potenciales. Estas alertas proporcionan información detallada sobre la amenaza, así como recomendaciones para reducir el riesgo. Puedes configurar Azure Security Center para enviar notificaciones por correo electrónico, SMS o integrar herramientas de terceros como [Slack](https://slack.com/) o [Microsoft Teams](https://www.microsoft. com /en-us/microsoft-teams/group-chat-software). ### Informes de conformidad Azure Security Center le permite generar informes de conformidad para diversas normativas, como GDPR, HIPAA y PCI DSS. Estos informes le ayudarán a supervisar el estado de conformidad de su organización y a identificar los ámbitos que requieren mejoras. ______ ## Meilleures pratiques pour Azure Security Center Pour tirer le meilleur parti d'Azure Security Center, envisagez de mettre en œuvre les bonnes pratiques suivantes : 1. **Active Azure Security Center en todas sus suscripciones**: Asegurarse de que todas sus suscripciones Azure están protegidas por Azure Security Center es esencial para mantener un entorno cloud seguro. 2. **Examine periódicamente su puntuación de seguridad**: la vigilancia de su puntuación de seguridad le ayudará a comprender su estado de seguridad global y a identificar los dominios en los que se producen mejoras. 3. **Acceda a las recomendaciones de seguridad**: el respeto de las recomendaciones de seguridad proporcionadas por Azure Security Center le ayudará a mejorar su seguridad y a reducir los riesgos potenciales. 4. **Vigile las alertas de seguridad**: Examine regularmente las alertas de seguridad y responda a ellas para hacer frente a las amenazas potenciales y mantener un entorno seguro. 5. **Responda a las exigencias de conformidad**: asegúrese de que su organización se ajusta a los últimos estándares normativos examinando y aplicando regularmente sus políticas de conformidad.______ ## Referencias - [Documentación del Centro de Seguridad Azure](https://docs.microsoft.com/en-us/azure/security-center/) - [Servicio de políticas Azure](https://docs.microsoft.com/en-us/azure/ gouvernance/politique/) - [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) - [CIS](https://www. cisecurity.org/) - [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) - [RGPD](https://gdpr.eu/) - [HIPAA]( https://www.hhs.gov/hipaa/index.html) - [PCI DSS](https://www.pcisecuritystandards.org/)
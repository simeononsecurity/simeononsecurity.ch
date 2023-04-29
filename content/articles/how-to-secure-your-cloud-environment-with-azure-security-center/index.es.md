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

**Cómo proteger su entorno de nube con Azure Security Center**.

Asegurar su entorno en la nube es esencial para proteger los datos, las aplicaciones y la infraestructura de su organización frente a las amenazas. El **Azure Security Center** de Microsoft es una potente herramienta que le ayuda a reforzar su postura de seguridad y a identificar rápidamente los riesgos potenciales en su entorno Azure. En este artículo, hablaremos sobre cómo proteger su entorno de nube utilizando Azure Security Center, y cubriremos las mejores prácticas para implementar varias características de seguridad. Además, en este artículo, profundizaremos en más detalles técnicos y ejemplos para ayudarle a comprender mejor cómo proteger su entorno de nube mediante Azure Security Center.

______

## Entender Azure Security Center

Azure Security Center es un **sistema unificado de gestión de la seguridad de la infraestructura** que le ayuda a identificar y abordar posibles vulnerabilidades en su entorno de nube. Ofrece varias funciones, como la detección de amenazas, la gestión de la postura de seguridad y la gestión del cumplimiento, para garantizar que su entorno Azure esté siempre seguro.

**La evaluación continua de la seguridad y la protección avanzada frente a amenazas son dos de las principales características de Azure Security Center. Continuous Security Assessment le ayuda a identificar posibles problemas de seguridad en su entorno, mientras que Advanced Threat Protection le ayuda a detectar y responder a posibles amenazas.

______

## Implementación de políticas de seguridad y normas de cumplimiento

Azure Security Center le permite implementar y gestionar políticas de seguridad en su entorno de nube. Puede utilizar el servicio **Azure Policy** para crear políticas de seguridad personalizadas o utilizar políticas integradas para aplicar las mejores prácticas y normas de cumplimiento. También puede evaluar su postura de seguridad con respecto a las normas del sector, como [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) e [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

Azure Security Center también ofrece funciones de gestión del cumplimiento, lo que le permite realizar un seguimiento del estado de cumplimiento de su organización con respecto a varios marcos normativos, como [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) y [PCI DSS](https://www.pcisecuritystandards.org/).

______

## Protección de sus recursos Azure

**La higiene de la seguridad de los recursos** es un aspecto importante de la seguridad de su entorno de nube. Azure Security Center proporciona **Secure Score**, una medida de su postura de seguridad, para ayudarle a comprender la seguridad general de sus recursos. Puede mejorar su Secure Score siguiendo las recomendaciones proporcionadas por Azure Security Center.

### Seguridad de la red

La implementación de medidas de seguridad de red adecuadas, como **Network Security Groups (NSGs)**, **Azure Firewall** y **Web Application Firewall (WAF)**, es crucial para proteger su entorno Azure de posibles amenazas. Estas herramientas le ayudan a controlar el tráfico de red entrante y saliente, protegiendo sus recursos de accesos no autorizados y posibles ataques.

#### Grupos de seguridad de red (NSG)

Los NSG actúan como un cortafuegos virtual para sus recursos Azure, permitiéndole definir reglas que permiten o deniegan el tráfico de red hacia y desde sus recursos. Por ejemplo, puede crear un NSG con reglas para permitir o denegar tráfico específico:

```azurecli
# Crear un grupo de seguridad de red
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Añadir reglas para permitir o denegar tráfico
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Más información sobre [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) en la documentación oficial.

#### Cortafuegos Azure
Azure Firewall es un servicio de seguridad de red gestionado y basado en la nube que protege sus recursos Azure. Proporciona funciones avanzadas como filtrado basado en inteligencia de amenazas, categorías web y análisis y registro centralizados. Para configurar Azure Firewall, puede seguir estas [instrucciones de inicio rápido](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Cortafuegos de aplicaciones web (WAF)
Web Application Firewall (WAF) es una función de **Azure Application Gateway** que ofrece protección a sus aplicaciones web frente a exploits web comunes como SQL injection, cross-site scripting y otras amenazas. WAF puede integrarse fácilmente con sus aplicaciones web existentes, y puede configurar reglas personalizadas para proteger contra patrones de ataque específicos.

He aquí un ejemplo de cómo crear un Application Gateway con WAF activado:
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
Más información sobre [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) en la documentación oficial.

### Gestión de Identidades y Accesos

**Azure Active Directory (Azure AD)** es un componente esencial para asegurar su entorno de nube. Azure Security Center ofrece recomendaciones para mejorar la gestión de identidades y accesos, como habilitar la **Autenticación por factores múltiples (MFA)**, implementar el **Control de acceso basado en roles (RBAC)** y supervisar las actividades sospechosas.

#### Autenticación multifactor (MFA)

MFA añade una capa adicional de seguridad a sus cuentas de Azure AD al requerir que los usuarios proporcionen dos o más formas de verificación antes de conceder el acceso. Puede habilitar MFA para su organización siguiendo la [guía paso a paso](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) proporcionada por Microsoft.

Ejemplo: Habilitar MFA para un usuario

```powershell
# Conectar a Azure AD
Conectar-AzureAD

# Habilitar MFA para un usuario específico
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Ubicación"=""; "FactorSatisfacción"="2"; "MétodoVerificación"="1"};@{"Ubicación"=""; "FactorSatisfacción"="2"; "MétodoVerificación"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Control de acceso basado en roles (RBAC)
RBAC le permite definir permisos granulares para sus recursos Azure, asegurando que los usuarios tengan el nivel apropiado de acceso. Puede asignar funciones a usuarios, grupos o aplicaciones para gestionar su acceso a los recursos de su organización. Para implementar RBAC, siga la [guía oficial](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) de Microsoft.

Ejemplo: Asignar un rol a un usuario
```azurecli
# Asignar un rol de Lector a un usuario
az role assignment create --assignee johndoe@example.com --role "Lector" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Supervisión de actividades sospechosas
Azure AD proporciona funciones como **Protección de identidad** y **Acceso condicional** que le ayudan a supervisar y responder a actividades sospechosas. Identity Protection utiliza algoritmos de aprendizaje automático para detectar anomalías e intentos de inicio de sesión arriesgados, mientras que Conditional Access le permite establecer políticas que controlan el acceso en función de factores como el dispositivo, la ubicación y el nivel de riesgo.

Para configurar Azure AD Identity Protection, siga la [guía oficial](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) de Microsoft.

Ejemplo: Creación de una política de acceso condicional

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
    "BuiltInControls" = @("Bloque")
}
New-AzureADMSConditionalAccessPolicy -DisplayName $PolicyName -State $PolicyState -Conditions $Conditions -GrantControls $GrantControls -Description $PolicyDescription

```
Obtenga más información sobre [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) y [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) en la documentación oficial.


### Seguridad de datos

Proteger sus datos en la nube es crucial. Azure Security Center ofrece varias funciones de seguridad de datos, como **Azure Information Protection**, **Azure Storage Service Encryption** y **Azure Disk Encryption**. Estas funciones le ayudan a cifrar y gestionar el acceso a sus datos, garantizando que la información confidencial permanezca segura.

#### Protección de la información de Azure

**Azure Information Protection (AIP)** es una solución basada en la nube que le ayuda a clasificar, etiquetar y proteger documentos y correos electrónicos confidenciales. AIP proporciona un conjunto de etiquetas integradas, como "Confidencial" y "Personal", que pueden personalizarse según las necesidades de su organización. También puede configurar AIP para que aplique automáticamente etiquetas basadas en reglas predefinidas. Para empezar a utilizar AIP, siga la [guía oficial](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).

Ejemplo: Creación de una etiqueta personalizada

```powershell
# Conectar con el servicio AIP
Conectar-AipService

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
#### Cifrado del servicio de almacenamiento Azure
**Azure Storage Service Encryption (SSE**) cifra automáticamente sus datos en reposo en las cuentas de Azure Storage, incluido el almacenamiento de bloques, archivos, tablas y colas. SSE utiliza claves gestionadas por Azure o por el cliente para proporcionar cifrado a nivel de cuenta de almacenamiento. Para habilitar SSE, siga la [guía paso a paso](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) proporcionada por Microsoft.

Ejemplo: Habilitar SSE para una cuenta de almacenamiento

```azurecli
# Habilitar SSE utilizando claves gestionadas por Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Cifrado de disco Azure
**Azure Disk Encryption** le ayuda a proteger los discos de las máquinas virtuales cifrándolos con BitLocker (Windows) o dm-crypt (Linux). Las claves de cifrado y los secretos están protegidos por Azure Key Vault, lo que garantiza la seguridad de sus datos en reposo. Para activar Azure Disk Encryption, siga la [guía oficial](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) de Microsoft.

Ejemplo: Habilitar Azure Disk Encryption para una máquina virtual
```azurecli
# Habilitar Azure Disk Encryption para una máquina virtual Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Obtenga más información sobre [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) y [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) en la documentación oficial.
______

## Detección y respuesta a amenazas

Azure Security Center utiliza funciones avanzadas de detección de amenazas para identificar posibles amenazas y alertarle de ellas. Al integrarse con **Azure Sentinel**, puede supervisar, investigar y responder a incidentes de seguridad en todo su entorno.

### Detección de amenazas

Azure Security Center utiliza **Azure Defender**, un conjunto de funciones avanzadas de detección de amenazas, para identificar posibles amenazas a la seguridad. Azure Defender supervisa sus recursos en busca de indicadores de peligro y proporciona alertas y recomendaciones para ayudarle a responder a posibles amenazas. Para activar Azure Defender, siga la [guía oficial](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

Ejemplo: Activar Azure Defender para una suscripción

```azurecli
# Habilitar Azure Defender para una suscripción
az security auto-provisioning-setting update --name default --auto-provision on
```
### Respuesta a amenazas
Cuando se detecta una amenaza, es esencial responder con rapidez y eficacia. Azure Security Center proporciona **Gestión de incidentes de seguridad**, que le ayuda a investigar y responder a los incidentes de seguridad. También puede integrarse con **Azure Sentinel** para crear playbooks automatizadas y ordenar su respuesta a incidentes de seguridad. Obtenga más información sobre la integración de Azure Security Center con Azure Sentinel en la **documentación oficial**.

Ejemplo: Crear un playbook de Logic App para Azure Sentinel
```azurecli
# Crear un grupo de recursos
az group create --name MyResourceGroup --location EastUS

# Crear una Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
El archivo `playbook-definition.json` debe contener la definición del playbook de Logic App. Puede encontrar ejemplos de playbooks para Azure Sentinel en el repositorio [Azure-Sentinel GitHub repository](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

Al aprovechar las capacidades de detección de amenazas de Azure Security Center e integrarse con Azure Sentinel, puede crear una estrategia de seguridad sólida para detectar y responder a las amenazas en su entorno Azure. Obtenga más información sobre [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) y [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) en la documentación oficial.
______

## Supervisión e informes

La supervisión y la generación de informes son componentes esenciales para mantener un entorno de nube seguro. Azure Security Center proporciona varias herramientas de supervisión y elaboración de informes, como **Security Dashboard**, **Security Alerts** y **Compliance Reports**.

### Panel de seguridad

El panel de seguridad de Azure Security Center proporciona una visión global de su postura de seguridad. Muestra su puntuación de seguridad, recomendaciones de seguridad y alertas de seguridad activas. El panel también proporciona información sobre su estado de cumplimiento y le permite realizar un seguimiento de su progreso a lo largo del tiempo.

### Alertas de seguridad

Azure Security Center genera alertas de seguridad cuando se detectan amenazas potenciales. Estas alertas proporcionan información detallada sobre la amenaza, así como recomendaciones para mitigar el riesgo. Puede configurar Azure Security Center para enviar notificaciones por correo electrónico, SMS o integrarse con herramientas de terceros como [Slack](https://slack.com/) o [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Informes de cumplimiento

Azure Security Center le permite generar informes de cumplimiento para varios marcos normativos, como GDPR, HIPAA y PCI DSS. Estos informes le ayudan a realizar un seguimiento del estado de cumplimiento de su organización y a identificar las áreas que requieren mejoras.

______

## Mejores prácticas para Azure Security Center

Para sacar el máximo provecho de Azure Security Center, considere implementar las siguientes mejores prácticas:

1. **Habilite Azure Security Center en todas sus suscripciones**: Asegurarse de que todas sus suscripciones de Azure están protegidas por Azure Security Center es crucial para mantener un entorno de nube seguro.
2. **Revise regularmente su Secure Score**: La supervisión de su Secure Score le ayuda a comprender su postura de seguridad general y a identificar las áreas que requieren mejoras.
3. 3. **Aplique las recomendaciones de seguridad**: Abordar las recomendaciones de seguridad proporcionadas por Azure Security Center le ayuda a mejorar su postura de seguridad y reducir los riesgos potenciales.
4. **Supervisar las alertas de seguridad**: Revisa y responde regularmente a las alertas de seguridad para mitigar posibles amenazas y mantener un entorno seguro.
5. **Manténgase al día con los requisitos de cumplimiento**: Asegúrese de que su organización se mantiene conforme con los marcos normativos más recientes revisando y actualizando periódicamente sus políticas de cumplimiento.

______

## Referencias

- Documentación de Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- Azure Policy Service](https://docs.microsoft.com/en-us/azure/governance/policy/)
- NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- CIS](https://www.cisecurity.org/)
- ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- GDPR](https://gdpr.eu/)
- HIPAA](https://www.hhs.gov/hipaa/index.html)
- PCI DSS](https://www.pcisecuritystandards.org/)


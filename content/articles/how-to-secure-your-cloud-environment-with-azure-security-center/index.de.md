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


 **Para proteger su entorno cloud con Azure Security Center**.
 
 La seguridad de su nube es esencial para proteger los datos, las aplicaciones y la infraestructura de su empresa. El **Centro de Seguridad de Azure** de Microsoft es una herramienta muy útil, con la que puede controlar su seguridad y detectar rápidamente los riesgos potenciales en su uso de Azure. En este artículo se explica cómo proteger su nube con el Centro de seguridad de Azure y se describen los métodos más utilizados para implementar distintas funciones de seguridad. Además, en este artículo proporcionaremos más información y detalles técnicos para que comprenda mejor cómo puede proteger su nube con Azure Security Center.
 
 ______
 
 ## Fundamentos de Azure Security Center
 
 Azure Security Center es un **sistema unificado de gestión de la seguridad de la infraestructura**, con el que podrá identificar y controlar los posibles problemas de su nube. Ofrece varias funciones, como la detección de amenazas, la gestión del estado de seguridad y la gestión del cumplimiento, para garantizar que su entorno Azure sea siempre seguro.
 
 **La evaluación continua de la seguridad y la mejora de la protección de la seguridad son dos funciones del Centro de seguridad de Azure. Continuous Security Assessment le ayuda a identificar posibles problemas de seguridad en su entorno, mientras que Advanced Threat Protection le ayuda a detectar posibles amenazas y a tomar las medidas oportunas.
 
 ______
 
 ## Implantación de normas de seguridad y cumplimiento de normativas
 
 Con Azure Security Center puede implementar y validar las directivas de seguridad en su entorno cloud. Puede utilizar el control **Política de Azure** para definir las directivas de seguridad, o bien integrar directivas para aplicar las mejores prácticas y normas de cumplimiento. También puede aplicar su normativa de seguridad a normas industriales como [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS]( https:/ /www.cisecurity.org/) e [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).
 
 Azure Security Center también ofrece funciones de gestión del cumplimiento, con las que podrá comprobar el estado de cumplimiento de su organización con respecto a distintas normativas reguladoras, como [DSGVO](https://gdpr.eu/), [HIPAA](https://www.hhs.gov /hipaa/index.html) y [PCI DSS](https://www.pcisecuritystandards.org/).
 
 ______
 
 ## Proteja sus recursos Azure
 
 La **Higiene de la seguridad de los recursos** es un aspecto importante de la seguridad de su entorno cloud. Azure Security Center ofrece **Secure Score**, una medición de su estado de seguridad, para ayudarle a conocer la seguridad de sus recursos. Puede mejorar su calificación de seguridad si tiene en cuenta las recomendaciones de Azure Security Center.
 
 ### Seguridad de red
 
 La implementación de mecanismos de seguridad de red adecuados, como **grupos de seguridad de red (NSG)**, **Azure Firewall** y **Web Application Firewall (WAF)**, es esencial para proteger su utilización de Azure frente a posibles amenazas. Estas herramientas le ayudan a controlar el funcionamiento de la red existente y ausente y a proteger sus recursos frente a intrusiones no autorizadas y amenazas potenciales.
 
 #### Grupos de seguridad de red (NSG)
 
 Los NSG funcionan como un cortafuegos virtual para sus recursos de Azure, ya que le permiten definir reglas para reducir o modificar el flujo de datos de red hacia y desde sus recursos. Puede, por ejemplo, crear una NSG con reglas, para que los datos de cada red se reduzcan o eliminen:
 
 Encontrará más información sobre [Netzwerksicherheitsgruppen](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) en la documentación oficial.
 
 #### Azure-Firewall
 Azure Firewall es un cortafuegos de red basado en la nube y fácil de usar que protege sus recursos de Azure. Ofrece funciones ampliadas, como filtros basados en la información de captura, categorías web, así como recopilación y análisis centralizados. Para utilizar Azure Firewall, puede descargar esta [Guía de inicio rápido](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).
 
 #### Cortafuegos de aplicaciones web (WAF)
 El cortafuegos de aplicaciones web (WAF) es una función de **Azure Application Gateway** que protege sus aplicaciones web de las conocidas vulnerabilidades web como SQL-Injection, Cross-Site-Scripting y otras. WAF puede integrarse sin problemas en sus aplicaciones web actuales, y puede configurar reglas definidas por el usuario para la protección frente a amenazas específicas.
 
 Este es un ejemplo de cómo SIE puede crear un Application Gateway con un WAF activo:
 Obtenga más información sobre [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) en la documentación oficial.
 
 ### Identitäts- und Zugriffsverwaltung
 
 **Azure Active Directory (Azure AD)** es un componente para la seguridad de su entorno cloud. Azure Security Center ofrece funciones para mejorar la gestión de identidades y contraseñas, como la activación de la autenticación de factor múltiple (MFA)**, la implementación del control de acceso basado en roles (RBAC)** y la supervisión de actividades adicionales.
 
 #### Autenticación multifactor (MFA)
 
 MFA proporciona a los usuarios de Azure AD un nivel de seguridad especial que les permite acceder a dos o más formas de autenticación. Puede activar MFA para su organización si sigue las instrucciones [Schritt-für-Schritt-Anleitung] (https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure- mfa) de Microsoft.
 
 Ejemplo: Activar MFA para un usuario
 
 #### Control de Acceso Basado en Rol (RBAC)
 Con RBAC puede definir amplias restricciones para sus recursos de Azure y garantizar que los usuarios tengan acceso a las claves de acceso correspondientes. Los usuarios, grupos o aplicaciones pueden crear roles para acceder a los recursos de su organización. Para implementar RBAC, siga las instrucciones de [offiziellen Leitfaden](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) de Microsoft.
 
 Ejemplo: Haga que un usuario desempeñe un papel en
 #### Überwachung verdächtiger Aktivitäten
 Azure AD ofrece funciones como la **protección de identidades** y la **función de acceso**, con las que las SIE pueden supervisar y responder a actividades peligrosas. La protección de la identidad utiliza algoritmos algorítmicos para detectar anomalías y análisis de riesgo, que SIE puede aplicar mediante el establecimiento de directrices de protección de la identidad, basando la protección en factores tales como el producto, la ubicación y el riesgo.
 
 Siga las instrucciones para la instalación de Azure AD Identity Protection de la [licencia oficial](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) de Microsoft.
 
 Ejemplo: Establezca una directiva para la conexión de inicio de sesión
 
 Obtenga más información sobre [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) y [Conditional Access](https://learn.microsoft . com/en-us/azure/active-directory/conditional-access/overview) en la documentación oficial.
 
 
 ### Seguridad de los datos
 
 La protección de sus datos en la nube es de vital importancia. Azure Security Center ofrece varias funciones de seguridad de datos como **Azure Information Protection**, **Azure Storage Service Encryption** y **Azure Disk Encryption**. Estas funciones le ayudan a descifrar y proteger sus datos y a garantizar la seguridad de su información.
 
 #### Azure-Informationsschutz
 
 **Azure Information Protection (AIP)** es una solución basada en la nube que permite clasificar, clasificar y proteger documentos y correos electrónicos confidenciales. AIP ofrece una serie de etiquetas integradas, como "Vertraulich" y "Persönlich", que pueden adaptarse a las necesidades de su organización. También puede configurar AIP de forma que las etiquetas se ajusten automáticamente en función de los parámetros definidos. Para empezar con AIP, siga las instrucciones de [offiziellen Leitfaden](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).
 
 Ejemplo: Establecer una etiqueta definida por el usuario
 
 #### Cifrado de Azure Storage Service
 **Azure Storage Service Encryption (SSE**) cifra automáticamente los datos almacenados en Azure Storage, como bloques, datos, tablas y archivos. SSE utilizó los almacenamientos de Azure o los almacenamientos de los clientes, para poder realizar la transferencia a las bases de datos de almacenamiento. Para activar SSE, siga las instrucciones de Microsoft [Schritt-für-Schritt-Anleitung] (https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption).
 
 Ejemplo: Activar SSE para un certificado de software
 
 #### Cifrado de disco Azure
 **Azure Disk Encryption** te ayuda a proteger los datos de las máquinas virtuales, ya sea con BitLocker (Windows) o dm-crypt (Linux). Azure Key Vault se encargará de la seguridad de las claves de seguridad y de los errores, asegurándose de que sus datos están protegidos. Para activar Azure Disk Encryption, siga las instrucciones de la [licencia oficial](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) de Microsoft.
 
 Ejemplo: Activar el cifrado de disco de Azure para un equipo virtual
 Obtenga más información sobre [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https:// docs .microsoft.com/en-us/azure/storage/common/storage-service-encryption) y [Azure Disk Encryption] (https://learn.microsoft.com/en-us/azure/virtual-machines/disk -Verschlüsselungsübersicht) en la documentación oficial.
 ______
 
 ## Requisitos a tener en cuenta y a consultar
 
 Azure Security Center utiliza funciones de detección de amenazas mejoradas para identificar posibles amenazas y advertirle de ellas. Gracias a la integración con **Azure Sentinel**, podrá detectar, investigar y responder a los problemas de seguridad de su entorno.
 
 ### Bedrohungserkennung
 
 Azure Security Center utiliza **Azure Defender**, una serie de funciones de detección de amenazas más avanzadas, para identificar posibles amenazas de seguridad. Azure Defender consulta sus recursos en los indicadores de compromiso y proporciona advertencias y consejos para que pueda reaccionar ante posibles problemas. Para activar Azure Defender, siga las instrucciones de la [licencia oficial] (https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).
 
 Ejemplo: Activar Azure Defender para una suscripción
 
 ### Reaktion auf Bedrohungen
 Cuando una red está infectada, es importante que sea rápida y eficaz. Azure Security Center ofrece una gestión de **factores de seguridad** con la que podrá investigar y solucionar problemas de seguridad. También puede integrar **Azure Sentinel** para crear Playbooks automatizadas y coordinar su actuación sobre las amenazas de seguridad. Obtenga más información sobre la integración de Azure Security Center en Azure Sentinel en la **documentación oficial**.
 
 Ejemplo: Crear un libro de jugadas de aplicaciones lógicas para Azure Sentinel
 El archivo "playbook-definition.json" debe contener la definición de Playbook de Logic App. Encontrará ejemplos de Playbooks para Azure Sentinel en [Azure-Sentinel GitHub-Repository](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).
 
 Mediante el uso de las funciones de reconocimiento de amenazas del Centro de seguridad de Azure y la integración en Azure Sentinel, puede crear una estrategia de seguridad sólida para reconocer y controlar las amenazas en su entorno de Azure. Obtenga más información sobre [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) y [Azure Sentinel](https://docs.microsoft . com/en-us/azure/sentinel/overview) en la documentación oficial.
 ______
 
 ##Seguimiento y consulta
 
 La supervisión y la gestión de informes son componentes importantes para la creación de un entorno de nube seguro. Azure Security Center ofrece varias herramientas para la supervisión y el control, como el panel de seguridad, las advertencias de seguridad y los informes de conformidad.
 
 ### Cuadro de mandos de seguridad
 
 El panel de seguridad de Azure Security Center ofrece una visión general de su estado de seguridad. Muestra su evaluación de seguridad, recomendaciones de seguridad y advertencias de seguridad activas. El cuadro de mandos también ofrece información sobre su estado de cumplimiento y le permite comprobar su cumplimiento en el transcurso del tiempo.
 
 ### Advertencias de seguridad
 
 Azure Security Center genera advertencias de seguridad cuando se producen posibles problemas. Estas advertencias proporcionan información detallada sobre el problema y consejos para reducir los riesgos. Puede configurar el Centro de seguridad de Azure de modo que los avisos se envíen por correo electrónico o SMS o a través de herramientas de terceros como [Slack](https://slack.com/) o [Microsoft Teams](https://www.microsoft. de/en-us/microsoft-teams/group-chat-software).
 
 ### Compliance-Berichte
 
 Con Azure Security Center puede generar informes de cumplimiento para distintos marcos normativos, como GDPR, HIPAA y PCI DSS. Estos informes le ayudarán a comprobar el estado de cumplimiento de su empresa y a identificar las áreas que deben mejorarse.
 
 ______
 
 ## Mejores prácticas para Azure Security Center
 
 Para utilizar Azure Security Center de forma óptima, debe implementar las siguientes prácticas recomendadas:
 
 1. **Activar Azure Security Center para todas sus suscripciones**: Asegurarse de que todas sus suscripciones de Azure están protegidas por el Centro de seguridad de Azure es esencial para la creación de una gestión segura de la nube.
 2. **Compruebe periódicamente su evaluación de seguridad**: La verificación de su evaluación de seguridad le ayuda a conocer su nivel de seguridad general y a identificar las áreas que deben mejorarse.
 3. **Implemente las advertencias de seguridad**: El uso de las advertencias de seguridad de Azure Security Center le ayuda a mejorar su estado de seguridad y a reducir los riesgos potenciales.
 4. **Aviso de seguridad**: Compruebe periódicamente las advertencias de seguridad y reaccione ante ellas para reducir los posibles riesgos y proteger su entorno.
 5. **Cumpla con los requisitos de cumplimiento de la normativa**: Asegúrese de que su empresa cumple las normas reguladoras más recientes, y compruebe y actualice periódicamente sus directrices de cumplimiento.
 
 ______
 
 ## Verweise
 
 - Documentación del Centro de seguridad de Azure] (https://docs.microsoft.com/en-us/azure/security-center/)
 - [Azure Policy-Dienst] (https://docs.microsoft.com/en-us/azure/governance/policy/)
 - [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
 - CIS](https://www.cisecurity.org/)
 - ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
 - DSGVO](https://gdpr.eu/)
 - HIPAA](https://www.hhs.gov/hipaa/index.html)
 - PCI-DSS](https://www.pcisecuritystandards.org/)
 

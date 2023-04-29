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

  **एज़्योर मानक के साथ आपकी सुरक्षा को कैसे सुरक्षित करें** आपके संगठन के डेटा, कार्यप्रणाली और कार्य योजनाओं को बचाने के लिए आपके क्लाउड वातावरण को सुरक्षित रखने की आवश्यकता है। Microsoft का **Azure सुरक्षा केंद्र** एक शक्तिशाली उपकरण है जो आपकी सुरक्षा मुद्रा को मजबूत करता है और आपके Azure वातावरण में शीघ्रता से पहचान करने में आपकी सहायता करता है। इस लेख में हम चर्चा करेंगे कि एज्योर पर्यावरण पर्यावरण कर्ता का उपयोग करके अपने क्लाउड वातावरण को कैसे सुरक्षित रखें, और विभिन्न सुरक्षा व्यवस्था को लागू करने के लिए संबंधित संरक्षित करें। इसके अतिरिक्त, इस लेख में, हम अधिक तकनीकी झलक और स्पष्टीकरण प्राप्त करेंगे ताकि आपको यह समझने में मदद मिल सके कि एज्योर सीमा सेंसर का उपयोग करके अपने क्लाउड वातावरण को कैसे सुरक्षित किया जा सके। ______ ## एज्योर सीमाओं को एज्योर परिधि एक **एक रूपरेखा रूपरेखा सुरक्षा प्रबंधन प्रणाली** है जो आपके क्लाउड वातावरण में कमजोर लोगों की पहचान करती है और उन्हें दूर करने में आपकी करती है। यह आपके पुराने वातावरण को हमेशा सुरक्षित रखने के लिए समान पहचान, सुरक्षा प्रबंधन और संघ प्रबंधन जैसे कई सामान प्रदान करता है। **निरंतर सुरक्षा0 मूल्यांकन** और **उन्नत ख़तरा सुरक्षा** एज़्योर सुरक्षा केंद्र की दो प्रमुख विशेषताएं हैं। निरंतर सुरक्षा मूल्यांकन आपको अपने मामले में सीमित सुरक्षा मुद्दों की पहचान करने में मदद करता है, जबकि विशिष्ट विशिष्ट संरक्षण आपको सीमा का पता लगाने और प्रतिक्रिया देने में मदद करता है। ______ ## सुरक्षा और समानता को लागू करना एज़्योर कन्वेंशन सेंडर आपको अपने क्लाउड वातावरण में सुरक्षा को प्रभावित करता है और अनुमति देता है। आप कस्टम सुरक्षा एक साथ बनाने के लिए **Azure पॉलिसी** सेवा का उपयोग कर सकते हैं या संबद्ध और संबद्ध संस्था को लागू करने के लिए कई शेयर का उपयोग कर सकते हैं। आप [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/ final), [CIS]( जैसे उद्योग के मानकों के अनुसार अपनी सुरक्षा की स्थिति को लेकर भी कर सकते हैं) https://www.cisecurity.org/), और [ISO 27001](https://www.iso.org/isoiec-27001-सूचना-सुरक्षा.html)। एज़्योर सुरक्षा केंद्र सहयोग सुविधाएँ भी प्रदान करती हैं, जिससे आप [जीडीपीआर](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html), और [ PCI DSS](https://www.pcisecuritystandards.org/)। ______ ## अपने अज़ोर को शाक्षित को सुरक्षित रखना **संसाधन सुरक्षा स्वच्छता** आपके कपड़ों के माहौल को सुरक्षित रखने का एक पहलू है। एज़्योर असुरक्षित सेंडर आपकी सहूलियत की संपूर्ण सुरक्षा को समझने में आपकी मदद करने के लिए **सुरक्षित स्कोर**, आपकी सुरक्षा का एक टोकन प्रदान करता है। आप एज़्योर एक्सट्रीमियम प्रदान की गई जानकारी को अपने सुरक्षित स्कोर में सुधार कर सकते हैं। ### नेटवर्क सुरक्षा **नेटवर्क सुरक्षा समूह (NSGs)**, **Azure फ़ायरवॉल**, और **वेब फ़ायरवॉल (WAF)** उचित नेटवर्क सुरक्षा उपायों को आपके Azure कार्यक्षेत्र को कार्य से बचाने के लिए महत्वपूर्ण रूप से लागू करें। ये उपकरण आने वाले और बाहर जाने वाले नेटवर्क को नियंत्रित करने में आपकी मदद करते हैं, आपके संसाधनों को दबे हुए प्रभाव और झटकों से बचाते हैं। #### नेटवर्क सुरक्षा समूह (एनएसजी) एनएसजी आपके पुराने बांड के लिए क्रेडिट के रूप में कार्य करते हैं, जिससे आप उन सभी को परिभाषित कर सकते हैं जो आपके अधिकार से सत्यापन को अस्वीकार या अस्वीकार करते हैं। उदाहरण के लिए, आप विशिष्ट वर्ण को अस्वीकार करने या अस्वीकार करने के साथ एनएसजी बना सकते हैं: आधिकारिक दस्तावेज़ में [नेटवर्क सुरक्षा समूह](https://docs.microsoft.com/en-us/azure/virtual-network/ सुरक्षा -अवलोकन) के बारे में और जानें। #### Azure फ़ायरवॉल Azure फ़ायरवॉल आपकी, क्लाउड-आधारित नेटवर्क सुरक्षा सेवा है जो आपके Azure संसाधन की सुरक्षा करती है। यह थ्रेट इंटिग्रेशन-आधारित कनेक्टिंग, वेब प्लेक्स और केंद्रीकृत हो रहा है और एनालिटिक्स जैसी उन्नत सुविधाएँ प्रदान करता है। Azure फ़ायरवॉल सेट करने के लिए, आप इन [क्विक स्टार्ट निर्देश](https://aprender.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep) का पालन कर सकते हैं। #### वेब एप फ़ायरवॉल (WAF) ईमेल फ़ायरवॉल (WAF) **Azure Application Gateway** की एक विशेषता है जो आपकी वेब वेबसाइट को SQL इज़ प्रोटेक्शन, क्रॉस-साइट स्क्रिप्टिंग और अन्य सामान्य वेब एक्सप्लोरेशन से सुरक्षा प्रदान करता है। है। है। है। है। WAF को आपकी मौजूदा वेब वेबसाइट के साथ आसानी से एकीकृत किया जा सकता है, और आप विशिष्ट आच्छादन से सुरक्षा के लिए कस्टम सुझाव बना सकते हैं। WAF क्षमता के साथ एक संक्षिप्त उदाहरण यहां दिया गया है: आधिकारिक दस्तावेज़ों में [वेब फ़ायरवॉल](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) के बारे में में और जानें। ### पहचान और प्रबंधन तक पहुंचें **Azure Active Directory (Azure AD)** आपके क्लाउड वातावरण को सुरक्षित रखना एक अनिवार्य घटक है। एज सीमा की पहचान और एक्सिस प्रबंधन में सुधार के लिए समाशोधन प्रदान करता है, जैसे **मल्टी-फैक्टर ऑथेंटिकेशन (झोपड़ाए)** को सक्षम करना, **रोल-बेस्ड एक्सिस कंट्रोल (आरबीएसी)** को लागू करना, और संदेह निगरानी करना। #### बहु-कारक फाइलिंग (फ़िमीए) आपके Azure AD लाभ में सुरक्षा का एक अतिरिक्त प्रश्न है। आप नीचे दिए गए [चरण-दर-चरण चक्र](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) का पालन करके अपने संगठन के लिए MFA Microsoft द्वारा कर सकते हैं। उदाहरण: उपयोगकर्ता किसी के लिए एमएफए कर सकते हैं ####-भूमिका अभिगम नियंत्रण (आरबीएसी) आरबीएसी आपको अपने एज़ोर स्पेक्ट्रम के लिए विस्तृत अनुमतियों को परिभाषित करने की अनुमति देता है, यह सुनिश्चित करता है कि उपयोगकर्ता के पास उचित स्तर की पहुंच गया। आप अपने संगठन के भीतर तक पहुंचकर आपके लिए लाइव, लाइव या ऐप में भाग लेने के लिए आमंत्रित कर सकते हैं। RBAC को लागू करने के लिए, Microsoft से [आधिकारिक गाइड](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) का पालन करें। उदाहरण: एक उपयोगकर्ता को एक भूमिका सौंपी जाती है #### संदेह की आशंका Azure AD पहचान सुरक्षा** और **सशर्त** जैसे सामान प्रदान करते हैं जो संदिग्ध गतिविधियों पर नजर रखते हैं और उनकी प्रतिक्रिया प्रदान करती हैं आपकी सहायता करती हैं हैं। पहचान रणनीति विशिष्‍ट और जोखिम रेजर सिने-इन प्रयासों का पता लगाने के लिए शेयरिंग लेन-डेन प्रयासों1 उपयोग करता है, जबकि त्रुटि ऐक्सेस आप से जुड़े हुए सेट करने की अनुमति देता है जो नियम, स्थान और यौवन जैसे ऐक्सेस अधिकारों पर करता है। नियंत्रण करता है। Azure AD पहचान सुरक्षा सेट अप करने के लिए, Microsoft के [आधिकारिक गाइड](https://aprender.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) का पालन करें। उदाहरण: गलत नीति बनाना [Azure AD पहचान सुरक्षा](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) और [सशर्त पहुंच](https://सीखें) ) .microsoft.com/en-us/azure/active-directory/conditional-access/overview) आधिकारिक दस्तावेज़ में। ### डाटाबेस सुरक्षा क्लाउड में आपके डेटा की सुरक्षा करना महत्वपूर्ण है। Azure Security Center कई डेटा सुरक्षा सुविधाएँ प्रदान करता है, जैसे **Azure Information Protection**, **Azure Storage Service Encryption**, और **Azure Disk Encryption**। ये आपके डेटा को रिचार्ज करते हैं और आपकी सहायता करते हैं, यह सुनिश्चित करता है कि संवेदनशील जानकारी सुरक्षित रहती है। #### एज़्योर सूचना सुरक्षा **एज़्योर सूचना सुरक्षा (एआईपी)** एक क्लाउड-आधारित समाधान है जो आपके संवेदनशील दस्तावेज़ों और ईमेल को ऐक्स करने, लेबल करने और उनकी सुरक्षा करने में मदद करता है। आईपी लेबल का एक सेट प्रदान करता है, जैसे "गोपनीय" और "व्यक्तिगत," जिसे आपके संगठन की आवश्यकताओं के अनुसार अनुकूलित किया जा सकता है। आप पूर्व सत्यापन के आधार पर स्वचालित रूप से लेबल से लागू करने के लिए AIP को भी बता सकते हैं। AIP के साथ शुरुआत करने के लिए, [आधिकारिक गाइड](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) का पालन करें। उदाहरण: एक कस्टम लेबल बनाना #### Azure Storage Service Encryption **Azure Storage Service Encryption (SSE**) स्वतः रूप से ब्लॉब, फ़ाइल, टेबल और क्यू स्टोरेज सहित Azure स्टोरेज खाते में आपका डेटा दर्ज करता है। स्टोरेज साइट्स पर शेयर प्रदान करने के लिए SSE Azure-प्रबंधित लाभ या ग्राहक-प्रबंधित ग्रीटिंग का उपयोग करता है। SSE को सक्षम करने के लिए, Microsoft द्वारा प्रदान किया गया [चरण-दर-चरण विकल्प](https://docs.microsoft.com/es-us/azure/storage/common/storage-service-encryption) का चयन करें । उदाहरण: SSE को इसके लिए स्टोरेज अकाउंट #### Azure डिस्क पर छोड़ें **Azure Disk Encryption** आप BitLocker (Windows) या dm-.शेयरिंग (Linux) को शेयर करके सुरक्षित करने में मदद करते हैं। गोपनीयता की सुरक्षा सुरक्षित है, यह सुनिश्चित करते हुए कि आपका डेटा सुरक्षित है। एज़्योर डिस्क को रणनीतिक रूप से सक्षम करने के लिए, Microsoft से [आधिकारिक गाइड] (https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) का पालन करें। उदाहरण: किसी के लिए एज़्योर डिस्क रिस्क लूज़ राइटर [एज़्योर इंफॉर्मेशन प्रोटेक्शन](https://docs.microsoft.com/es-us/azure/information-protection/what-is-information-protection) के बारे में और जानें , [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption), और [Azure Disk Encryption](https://learn.microsoft.com ) /es-us/azure/virtual-machines/disk-encryption-overview) आधिकारिक दस्तावेज़ में। ______ ##एकॉर्डर का पता लगाना और उनका जवाब देना नीला सुरक्षा केंद्र दायरों की पहचान करना और आपको पहचान करने के लिए पहचान की पहचान की क्षमता का उपयोग करता है। **Azure Sentinel** के साथ एकीकरण करके, आप अपने पूरे माहौल में सुरक्षा घटनाओं की निगरानी, जांच और प्रतिक्रिया कर सकते हैं। ### थ्रेट डिटेक्शन एज़्योर ज़ोन ज़ोन जोखिम की पहचान करने के लिए अनुकूलन विकल्पों का पता लगाने की क्षमता का एक सेट ** एज़्योर व्यूअर ** का उपयोग करता है। एज्योर डैमेज एकेडम की संभावना के लिए आपकी राशि की जिम्मेदारी होती है और आपकी सहायता करने के लिए प्रतिक्रिया देने में सहमति और कार्रवाई प्रदान करता है। एज़्योर फ़ॉर्स को सक्षम करने के लिए, [आधिकारिक गाइड] (https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable) का पालन करें। उदाहरण: सदस्यता के लिए एज्योर प्रत्युत्तर ### धमकी प्रतिक्रिया जब किसी खतरे का पता चलता है, तो यह शीघ्र और प्रभावी तरीके से प्रतिक्रिया करने के लिए आवश्यक है। एज्योर सुरक्षा केंद्र **सुरक्षात्मक घटना** प्रबंधन प्रदान करता है, जो आपको सुरक्षा घटनाओं की जांच करने और प्रतिक्रिया देने में मदद करता है। आप **Azure Sentinel** के साथ स्वचालित PlayBook बनाने और सुरक्षा घटनाओं के प्रति अपनी प्रतिक्रिया के लिए सरल करने के लिए भी एकीकृत कर सकते हैं। **आधिकारिक दस्तावेज़** में Azure Sentinel के साथ Azure Security Center को एकीकृत करने और सीखने के बारे में। उदाहरण: Azure Sentinel के लिए एक लॉजिक ऐप Playbook create `playbook-definition.json` फ़ाइल में लॉजिक ऐप प्लेबुक की परिभाषा आने वाली है। आप [Azure-Sentinel GitHub रिपॉजिटरी](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks) में Azure Sentinel के लिए Playbook का उदाहरण पा सकते हैं। एज़्योर पर्यावरण में डैमेज का पता लगाने की क्षमता का लाभ उठाने और एज़्योर सेंटिनल के साथ एकीकरण करके, आप अपने एज़्योर माहौल में पहुंच का पता लगा सकते हैं और उनकी प्रतिक्रिया देने के लिए एक मजबूत सुरक्षा रणनीति बना सकते हैं। [नीला स्पेक्ट्रम](https://aprender.microsoft.com/es-us/azure/defender-for-cloud/enable-enhanced-security) और [Azure Sentinel](https://docs.microsoft.com/es -us/azure/sentinel/overview) आधिकारिक दस्तावेज़ में। ______ ## निगरानी और निगरानी और अभिग्रहण एक सुरक्षित वातावरण बनाए रखने के आवश्यक घटक हैं। एज़्योर सिक्योरिटी सेंटर निगरानी और अधिग्रहण के लिए **सुरक्षा गोदाम**, **सुरक्षा अलर्ट**, और **अनुपालन रिपोर्ट** जैसे कई टूल प्रदान करता है। ### सुरक्षा गोदाम Azure सुरक्षा केंद्र में सुरक्षा गोदाम आपकी सुरक्षा की व्यापक समीक्षा प्रदान करता है। यह आपका सुरक्षित स्कोर, सुरक्षा क्रैक और सक्रिय सुरक्षा अलर्ट प्रदर्शित करता है। गोदाम आपकी परिसीमा स्थिति के बारे में भी जानकारी प्रदान करता है और आपको समय के साथ अपनी प्रगति को ट्रैक करने की अनुमति देता है। ### सुरक्षा अलर्ट एज़्योर सुरक्षा केंद्र इसके अंतर्गत आने वाले सुरक्षा अलर्ट के अंतर्गत आता है। ये अलर्ट के बारे में विस्तृत जानकारी प्रदान करते हैं, साथ ही जोखिम को कम करने के लिए सुझाव भी देते हैं। आप Azure सुरक्षा केंद्र को ईमेल, एसएमएस के माध्यम से अजीब या [Slack](https://slack.com/) या [Microsoft Teams](https://www.microsoft.com) जैसे तृतीय-पक्ष टूल के साथ एकीकृत करने के लिए विन्यास कर सकते हैं /en-us/microsoft-teams/group-chat-software). ### संगत रिपोर्ट एज़्योर सुरक्षा केंद्र आपको प्राप्त करने की अनुमति देता है, एचआईपीएए और पीसीआई डीएसएस जैसे विभिन्न कार्य स्तरों के लिए अनुपालन रिपोर्ट तैयार करने की अनुमति देता है। ये रिपोर्ट आपके संगठन की स्थिति को ट्रैक करने और सुधार की आवश्यकताएं वाले क्षेत्रों की पहचान करने में आपकी सहायता करती हैं। ______ ## एज़्योर सीमा के लिए सर्वोत्तम अभ्यास एज़्योर सीमा का अधिकतम लाभ उठाने के लिए, निम्नलिखित संभव को लागू करने पर विचार करें: 1। एज़्योर सुरक्षा केंद्र सुरक्षित क्लाउड वातावरण बनाए रखने के लिए महत्वपूर्ण है। 2. **नियमित रूप से अपना सुरक्षित स्कोर की समीक्षा करें**: आपके सुरक्षित स्कोर की निगरानी करने से आपको अपनी समग्र सुरक्षा मुद्रा को समझने और सुधार की आवश्यकताओं वाले क्षेत्रों की पहचान करने में मदद मिलती है। 3. **सुरक्षा नीतियों को लागू करें**: एज़्योर सुरक्षा केंद्र द्वारा प्रदान की गई सुरक्षा नीतियों को संदेश देने से आपको अपनी सुरक्षा स्थिति में सुधार करने और झलकियों को कम करने में मदद मिलती है। 4. **सुरक्षात्मक चेतावनियों की निगरानी करें**: ज़ोन श्रम को कम करने और सुरक्षित वातावरण बनाए रखने के लिए नियमित रूप से सुरक्षा चेतावनियों की समीक्षा करें और उनका जवाब दें। 5. **अनुपालन आवश्यकताओं के साथ अप-टू-डेट बने रहें**: अपनी सहयोगी कंपनियों की नियमित रूप से समीक्षा करके और उन्हें अपडेट करके सुनिश्चित करें कि आपका संगठन अधीनस्थ पहलुओं के अनुरूप रहता है।______ ## संदर्भ - [Azure सुरक्षा केंद्र दस्तावेज़ीकरण](https: //docs.microsoft.com/en-us/azure/security-center/) - [Azure नीति सेवा](https://docs.microsoft.com/en-us/azure/governance /policy/) - [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final) - [CIS](https://www.cisecurity .org/) - [ISO 27001](https://www.iso.org/isoiec-27001-सूचना-सुरक्षा.html) - [GDPR](https://gdpr.eu/) - [HIPAA](https) ://www.hhs.gov/hipaa/index.html) - [पीस डीएसएस](https://www.pcisecuritystandards.org/)
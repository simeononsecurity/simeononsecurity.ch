---
title: "Microsoft Defender for Cloud के साथ अपने क्लाउड परिवेश को सुरक्षित करें"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Microsoft Defender for Cloud से Azure वर्कलोड सुरक्षित करें। पुराने Azure Security Center नामों, सुझावों, नीतियों और प्रतिक्रिया चरणों की समीक्षा करें।"
tags: ["Azure", "Security Center", "क्लाउड सुरक्षा", "Azure Sentinel", "Azure Defender", "नेटवर्क सुरक्षा", "पहचान प्रबंधन", "डेटा सुरक्षा", "खतरे का पता लगाना", "खतरे पर प्रतिक्रिया", "बहु-कारक प्रमाणीकरण", "भूमिका-आधारित अभिगम नियंत्रण", "नेटवर्क सुरक्षा समूह", "Azure Firewall", "वेब एप्लिकेशन फ़ायरवॉल", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "क्लाउड चिह्नों से घिरी ढाल, जो सुरक्षित क्लाउड परिवेश दर्शाती है। ढाल पर Azure Security Center का लोगो है।"
coverCaption: ""
---

**Azure Security Center के साथ अपने क्लाउड परिवेश को कैसे सुरक्षित करें**

अपने संगठन के डेटा, एप्लिकेशन और बुनियादी ढाँचे को खतरों से बचाने के लिए क्लाउड परिवेश सुरक्षित रखना आवश्यक है। Microsoft का **Azure Security Center** एक ऐसा टूल है जो आपकी सुरक्षा स्थिति मजबूत करने और Azure परिवेश में संभावित जोखिमों की शीघ्र पहचान करने में मदद करता है। इस लेख में हम Azure Security Center से क्लाउड परिवेश सुरक्षित करने और अलग-अलग सुरक्षा सुविधाएँ लागू करने के अच्छे तरीकों पर चर्चा करेंगे। तकनीकी विवरण और उदाहरण भी दिए गए हैं, ताकि आप सुरक्षा के चरणों को बेहतर समझ सकें।

*इस लेख के मूल प्रकाशन के बाद उत्पादों के नाम बदले हैं। Microsoft Azure Security Center अब Microsoft Defender for Cloud कहलाता है। Azure Active Directory अब Microsoft Entra ID है। Azure Sentinel अब Microsoft Sentinel है। Azure Defender, Defender for Cloud के अंतर्गत Defender योजनाओं और वर्कलोड सुरक्षा को संदर्भित करता है। नीचे पुराने नाम वहाँ रखे गए हैं जहाँ वे 2023 की शब्दावली बताते हैं।*

वर्तमान [Defender for Cloud परिचय](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) इसे क्लाउड सुरक्षा स्थिति प्रबंधन, DevSecOps और क्लाउड वर्कलोड सुरक्षा वाला Cloud Native Application Protection Platform बताता है। सुविधाएँ और लाइसेंसिंग क्लाउड, संसाधन प्रकार, सदस्यता और योजना पर निर्भर करते हैं।

______

## Azure Security Center को समझना

Azure Security Center एक **एकीकृत बुनियादी ढाँचा सुरक्षा प्रबंधन प्रणाली** है, जो क्लाउड परिवेश की संभावित कमजोरियों की पहचान करने और उन्हें दूर करने में मदद करती है। इसमें खतरे का पता लगाना, सुरक्षा स्थिति प्रबंधन और अनुपालन प्रबंधन जैसी सुविधाएँ हैं, जो आपके Azure परिवेश को सुरक्षित रखने में मदद करती हैं।

**निरंतर सुरक्षा आकलन** और **उन्नत खतरा सुरक्षा** Azure Security Center की दो प्रमुख सुविधाएँ हैं। निरंतर सुरक्षा आकलन आपके परिवेश में संभावित सुरक्षा समस्याएँ पहचानने में मदद करता है। उन्नत खतरा सुरक्षा संभावित खतरों का पता लगाने और उन पर प्रतिक्रिया देने में मदद करती है।

______

## सुरक्षा नीतियाँ और अनुपालन मानक लागू करना

Azure Security Center से आप अपने क्लाउड परिवेश में सुरक्षा नीतियाँ लागू और प्रबंधित कर सकते हैं। कस्टम सुरक्षा नीतियाँ बनाने या अच्छे तरीकों और अनुपालन मानकों को लागू करने के लिए अंतर्निहित नीतियों का उपयोग करने हेतु **Azure Policy** सेवा अपनाएँ। आप [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) और [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) जैसे उद्योग मानकों के अनुसार अपनी सुरक्षा स्थिति का आकलन भी कर सकते हैं।

Azure Security Center में अनुपालन प्रबंधन की सुविधाएँ भी हैं। इनसे आप अपने संगठन की अनुपालन स्थिति को [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) और [PCI DSS](https://www.pcisecuritystandards.org/) जैसे अलग-अलग नियामक ढाँचों के अनुसार देख सकते हैं।

______

## Azure संसाधनों को सुरक्षित करना

**संसाधनों की सुरक्षा-संबंधी स्वच्छता** क्लाउड परिवेश सुरक्षित रखने का अहम हिस्सा है। Azure Security Center **Secure Score** देता है, जो आपकी सुरक्षा स्थिति का माप है और संसाधनों की समग्र सुरक्षा समझने में मदद करता है। Azure Security Center के सुझावों पर कार्रवाई करके आप अपना Secure Score बेहतर कर सकते हैं।

### नेटवर्क सुरक्षा

अपने Azure परिवेश को संभावित खतरों से बचाने के लिए **Network Security Groups (NSG)**, **Azure Firewall** और **Web Application Firewall (WAF)** जैसे उचित नेटवर्क सुरक्षा उपाय लागू करना आवश्यक है। ये टूल आने-जाने वाले नेटवर्क ट्रैफ़िक को नियंत्रित करते हैं और अनधिकृत पहुँच तथा संभावित हमलों से संसाधनों की रक्षा करते हैं।

#### Network Security Groups (NSG)

NSG आपके Azure संसाधनों के लिए वर्चुअल फ़ायरवॉल की तरह काम करते हैं। इनके नियम तय करते हैं कि आपके संसाधनों तक और उनसे कौन-सा नेटवर्क ट्रैफ़िक जा सकता है। उदाहरण के लिए, विशिष्ट ट्रैफ़िक की अनुमति देने या उसे रोकने के नियमों वाला NSG बनाएँ:

```azurecli
# नेटवर्क सुरक्षा समूह बनाएँ
az network nsg create --name MyNSG --resource-group MyResourceGroup

# ट्रैफ़िक की अनुमति देने या उसे रोकने के नियम जोड़ें
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
आधिकारिक दस्तावेज़ में [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) के बारे में जानें।

ऊपर दिया गया उदाहरण हर IPv4 स्रोत से आने वाले TCP पोर्ट 80 ट्रैफ़िक की अनुमति देता है। उत्पादन ट्रैफ़िक के लिए ज्ञात स्रोत सीमा, निजी एंडपॉइंट या लोड बैलेंसर मार्ग का उपयोग करें। उदाहरण अपनाने से पहले वर्तमान [NSG सुरक्षा परिचय](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) देखें।

#### Azure Firewall

Azure Firewall एक प्रबंधित, क्लाउड-आधारित नेटवर्क सुरक्षा सेवा है, जो आपके Azure संसाधनों की रक्षा करती है। इसमें खतरे की जानकारी पर आधारित फ़िल्टरिंग, वेब श्रेणियाँ और केंद्रीकृत लॉगिंग तथा विश्लेषण जैसी उन्नत सुविधाएँ हैं। Azure Firewall स्थापित करने के लिए ये [त्वरित शुरुआत के निर्देश](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep) अपनाएँ।

#### Web Application Firewall (WAF)

Web Application Firewall (WAF), **Azure Application Gateway** की एक सुविधा है। यह SQL इंजेक्शन और क्रॉस-साइट स्क्रिप्टिंग और अन्य आम वेब हमलों से वेब एप्लिकेशन की रक्षा करती है। WAF को मौजूदा वेब एप्लिकेशन के साथ जोड़ा जा सकता है। विशिष्ट हमलों से बचाव के लिए कस्टम नियम भी बनाए जा सकते हैं।

WAF सक्षम करके Application Gateway बनाने का उदाहरण:
```azurecli
# WAF नीति बनाएँ
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# वर्चुअल नेटवर्क और सबनेट बनाएँ
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# सार्वजनिक IP पता बनाएँ
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# WAF सक्षम करके Application Gateway बनाएँ
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
आधिकारिक दस्तावेज़ में [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) के बारे में जानें।

### पहचान और पहुँच प्रबंधन

**Microsoft Entra ID, जिसे पहले Azure Active Directory (Azure AD) कहा जाता था,** क्लाउड परिवेश को सुरक्षित रखने का अहम हिस्सा है। Defender for Cloud पहचान और पहुँच प्रबंधन बेहतर करने के लिए सुझाव देता है, जैसे **बहु-कारक प्रमाणीकरण (MFA)** चालू करना, **भूमिका-आधारित अभिगम नियंत्रण (RBAC)** लागू करना और संदिग्ध गतिविधियों पर नज़र रखना।

#### बहु-कारक प्रमाणीकरण (MFA)

MFA, पहुँच देने से पहले उपयोगकर्ता से सत्यापन के दो या अधिक तरीके माँगकर Azure AD खातों की सुरक्षा की एक अतिरिक्त परत जोड़ता है। अपने संगठन के लिए MFA चालू करने हेतु Microsoft की [चरण-दर-चरण मार्गदर्शिका](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) अपनाएँ।

उदाहरण: किसी उपयोगकर्ता के लिए MFA चालू करें

```powershell
# Azure AD से कनेक्ट करें
Connect-AzureAD

# किसी विशिष्ट उपयोगकर्ता के लिए MFA चालू करें
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### भूमिका-आधारित अभिगम नियंत्रण (RBAC)

RBAC से आप Azure संसाधनों के लिए बारीक अनुमतियाँ तय कर सकते हैं, ताकि उपयोगकर्ताओं को उचित स्तर की पहुँच मिले। संगठन के संसाधनों तक उनकी पहुँच प्रबंधित करने के लिए उपयोगकर्ताओं, समूहों या एप्लिकेशन को भूमिकाएँ दें। RBAC लागू करने के लिए Microsoft की [आधिकारिक मार्गदर्शिका](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) अपनाएँ।

उदाहरण: किसी उपयोगकर्ता को भूमिका दें
```azurecli
# किसी उपयोगकर्ता को Reader भूमिका दें
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### संदिग्ध गतिविधियों पर नज़र रखना

Azure AD में **Identity Protection** और **Conditional Access** जैसी सुविधाएँ हैं, जो संदिग्ध गतिविधियों पर नज़र रखने और प्रतिक्रिया देने में मदद करती हैं। Identity Protection मशीन लर्निंग एल्गोरिदम से असामान्य गतिविधियों और जोखिम वाले साइन-इन प्रयासों का पता लगाता है। Conditional Access से आप डिवाइस, स्थान और जोखिम जैसे कारकों के आधार पर पहुँच नियंत्रित करने वाली नीतियाँ तय कर सकते हैं।

Azure AD Identity Protection सेट करने के लिए Microsoft की [आधिकारिक मार्गदर्शिका](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) अपनाएँ।

उदाहरण: Conditional Access नीति बनाएँ

```powershell
# Azure AD से कनेक्ट करें
Connect-AzureAD

# Conditional Access नीति बनाएँ
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "अज्ञात स्थानों से उपयोगकर्ताओं के साइन-इन रोकें।"
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
आधिकारिक दस्तावेज़ में [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) और [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) के बारे में जानें।

### डेटा सुरक्षा

क्लाउड में अपने डेटा की रक्षा करना आवश्यक है। Azure Security Center डेटा सुरक्षा की कई सुविधाएँ देता है, जैसे **Azure Information Protection**, **Azure Storage Service Encryption** और **Azure Disk Encryption**। ये सुविधाएँ डेटा को एन्क्रिप्ट करने और उसकी पहुँच प्रबंधित करने में मदद करती हैं, ताकि संवेदनशील जानकारी सुरक्षित रहे।

#### Azure Information Protection

**Azure Information Protection (AIP)** क्लाउड-आधारित समाधान है, जो संवेदनशील दस्तावेज़ों और ईमेल का वर्गीकरण, लेबलिंग और सुरक्षा करने में मदद करता है। AIP में "गोपनीय" और "निजी" जैसे अंतर्निहित लेबल हैं, जिन्हें आपके संगठन की ज़रूरतों के अनुसार बदला जा सकता है। तय नियमों के आधार पर लेबल अपने-आप लागू करने के लिए भी AIP कॉन्फ़िगर किया जा सकता है। AIP शुरू करने के लिए [आधिकारिक मार्गदर्शिका](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) अपनाएँ।

उदाहरण: कस्टम लेबल बनाएँ

```powershell
# AIP सेवा से कनेक्ट करें
Connect-AipService

# सुरक्षा सेटिंग्स वाला कस्टम लेबल बनाएँ
$LabelName = "संवेदनशील - केवल आंतरिक उपयोग"
$LabelDescription = "यह लेबल केवल आंतरिक उपयोग के लिए एन्क्रिप्शन और पहुँच नीति लागू करता है।"
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** Azure Storage खातों में संग्रहीत डेटा को अपने-आप एन्क्रिप्ट करता है। इसमें Blob, File, Table और कतार संग्रहण शामिल हैं। SSE, स्टोरेज खाते के स्तर पर एन्क्रिप्शन के लिए Azure-प्रबंधित या ग्राहक-प्रबंधित कुंजियों का उपयोग करता है। SSE चालू करने के लिए Microsoft की [चरण-दर-चरण मार्गदर्शिका](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) अपनाएँ।

Azure Information Protection ऐतिहासिक उत्पाद नाम है। Microsoft के वर्तमान Sentinel सुविधा दस्तावेज़ Azure Information Protection को अप्रचलित बताते हैं। नई लेबलिंग तैनाती शुरू करने से पहले वर्तमान Microsoft Purview Information Protection दस्तावेज़ देखें।

उदाहरण: स्टोरेज खाते के लिए SSE चालू करें

```azurecli
# Azure-प्रबंधित कुंजियों से SSE चालू करें
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** वर्चुअल मशीन डिस्क को BitLocker (Windows) या dm-crypt (Linux) से एन्क्रिप्ट करके सुरक्षित रखने में मदद करता है। एन्क्रिप्शन कुंजियाँ और सीक्रेट Azure Key Vault में सुरक्षित रखे जाते हैं, जिससे डेटा संग्रहीत अवस्था में सुरक्षित रहता है। Azure Disk Encryption चालू करने के लिए Microsoft की [आधिकारिक मार्गदर्शिका](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) अपनाएँ।

उदाहरण: वर्चुअल मशीन के लिए Azure Disk Encryption चालू करें
```azurecli
# Windows VM के लिए Azure Disk Encryption चालू करें
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
आधिकारिक दस्तावेज़ में [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) और [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) के बारे में जानें।
______

## खतरों का पता लगाना और उन पर प्रतिक्रिया देना

Azure Security Center संभावित खतरों की पहचान करने और आपको उनके बारे में सचेत करने के लिए उन्नत खतरा-पहचान सुविधाएँ उपयोग करता है। **Azure Sentinel** के साथ एकीकरण करके आप पूरे परिवेश में सुरक्षा घटनाओं की निगरानी, जाँच और उन पर प्रतिक्रिया कर सकते हैं।

### खतरे का पता लगाना

Azure Security Center संभावित सुरक्षा खतरों की पहचान करने के लिए उन्नत सुविधाओं के समूह **Azure Defender** का उपयोग करता है। Azure Defender संसाधनों में सेंध के संकेतों पर नज़र रखता है और संभावित खतरों पर प्रतिक्रिया देने के लिए अलर्ट तथा सुझाव देता है। Azure Defender चालू करने के लिए [आधिकारिक मार्गदर्शिका](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable) अपनाएँ।

उदाहरण: किसी सदस्यता के लिए Azure Defender चालू करें

```azurecli
# किसी सदस्यता के लिए Azure Defender चालू करें
az security auto-provisioning-setting update --name default --auto-provision on
```
### खतरे पर प्रतिक्रिया

खतरे का पता चलने पर आपको तेज़ी से और प्रभावी ढंग से प्रतिक्रिया देनी चाहिए। Azure Security Center में **सुरक्षा घटना** प्रबंधन है, जो सुरक्षा घटनाओं की जाँच और उन पर प्रतिक्रिया में मदद करता है। सुरक्षा घटनाओं पर प्रतिक्रिया व्यवस्थित करने के लिए स्वचालित प्रतिक्रिया-पुस्तिकाएँ बनाने हेतु **Azure Sentinel** के साथ एकीकरण भी किया जा सकता है। Azure Security Center को Azure Sentinel के साथ जोड़ने के बारे में **आधिकारिक दस्तावेज़** में जानें।

उदाहरण: Azure Sentinel के लिए Logic App प्रतिक्रिया-पुस्तिका बनाएँ
```azurecli
# संसाधन समूह बनाएँ
az group create --name MyResourceGroup --location EastUS

# Logic App बनाएँ
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
`playbook-definition.json` फ़ाइल में Logic App प्रतिक्रिया-पुस्तिका की परिभाषा होनी चाहिए। Azure Sentinel के लिए प्रतिक्रिया-पुस्तिका के उदाहरण [Azure-Sentinel GitHub रिपॉज़िटरी](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks) में मिलेंगे।

Azure Security Center की खतरा-पहचान सुविधाओं का उपयोग करके और Azure Sentinel के साथ एकीकरण करके आप Azure परिवेश में खतरों का पता लगाने और उन पर प्रतिक्रिया देने की मजबूत सुरक्षा रणनीति बना सकते हैं। आधिकारिक दस्तावेज़ में [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) और [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) के बारे में जानें।

वर्तमान एकीकरण प्रक्रिया, [Defender for Cloud connector](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) के ज़रिए Defender for Cloud के अलर्ट Microsoft Sentinel तक भेजती है। स्वचालन पर निर्भर होने से पहले Defender पोर्टल या Azure पोर्टल में क्लाउड कनेक्टर, डेटा संग्रह नियम, विश्लेषणात्मक नियम और घटना कार्यप्रवाह की पुष्टि करें।
______

## निगरानी और रिपोर्टिंग

सुरक्षित क्लाउड परिवेश बनाए रखने के लिए निगरानी और रिपोर्टिंग आवश्यक हैं। Azure Security Center निगरानी और रिपोर्टिंग के लिए कई टूल देता है, जैसे **सुरक्षा डैशबोर्ड**, **सुरक्षा अलर्ट** और **अनुपालन रिपोर्ट**।

### सुरक्षा डैशबोर्ड

Azure Security Center का सुरक्षा डैशबोर्ड आपकी सुरक्षा स्थिति का समग्र दृश्य देता है। इसमें आपका Secure Score, सुरक्षा सुझाव और सक्रिय सुरक्षा अलर्ट दिखते हैं। डैशबोर्ड अनुपालन स्थिति की जानकारी भी देता है और समय के साथ प्रगति पर नज़र रखने देता है।

### सुरक्षा अलर्ट

संभावित खतरों का पता चलने पर Azure Security Center सुरक्षा अलर्ट बनाता है। इन अलर्ट में खतरे का विस्तृत विवरण और जोखिम कम करने के सुझाव होते हैं। Azure Security Center को ईमेल या SMS से सूचनाएँ भेजने के लिए कॉन्फ़िगर करें, या [Slack](https://slack.com/) और [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) जैसे तृतीय-पक्ष टूल से जोड़ें।

### अनुपालन रिपोर्ट

Azure Security Center से GDPR, HIPAA और PCI DSS जैसे अलग-अलग नियामक ढाँचों के लिए अनुपालन रिपोर्ट बनाई जा सकती हैं। ये रिपोर्ट संगठन की अनुपालन स्थिति पर नज़र रखने और सुधार की ज़रूरत वाले क्षेत्रों की पहचान करने में मदद करती हैं।

______

## Azure Security Center के अच्छे तरीके

Azure Security Center का पूरा लाभ पाने के लिए इन अच्छे तरीकों पर विचार करें:

1. **सभी सदस्यताओं पर Azure Security Center चालू करें:** सुरक्षित क्लाउड परिवेश बनाए रखने के लिए सभी Azure सदस्यताओं को Azure Security Center से सुरक्षित करना आवश्यक है।
2. **अपने Secure Score की नियमित समीक्षा करें:** स्कोर पर नज़र रखने से आपकी समग्र सुरक्षा स्थिति समझने और सुधार की ज़रूरत वाले क्षेत्रों की पहचान करने में मदद मिलती है।
3. **सुरक्षा सुझाव लागू करें:** Azure Security Center के सुरक्षा सुझावों पर कार्रवाई करने से सुरक्षा स्थिति बेहतर होती है और संभावित जोखिम घटते हैं।
4. **सुरक्षा अलर्ट पर नज़र रखें:** संभावित खतरों को कम करने और सुरक्षित परिवेश बनाए रखने के लिए सुरक्षा अलर्ट की नियमित समीक्षा करें और उन पर प्रतिक्रिया दें।
5. **अनुपालन आवश्यकताओं की जानकारी अद्यतन रखें:** नवीनतम नियामक ढाँचों के अनुरूप रहने के लिए अनुपालन नीतियों की नियमित समीक्षा और अद्यतन करें।

## Defender for Cloud का वर्तमान कार्यप्रवाह

वर्तमान तैनाती के लिए यह क्रम अपनाएँ। मूल अनुभागों के नाम पुराने लेखों में खोज के लिए उपयोगी हैं, लेकिन पोर्टल और दस्तावेज़ Defender for Cloud की शब्दावली अपनाते हैं।

1. **सदस्यताओं और कनेक्टरों की सूची बनाएँ।** Azure सदस्यताएँ, AWS या GCP कनेक्टर, DevOps परियोजनाएँ और महत्वपूर्ण संसाधन दर्ज करें।
2. **ज़रूरी Defender योजनाएँ चालू करें।** वर्कलोड के अनुसार योजनाएँ चुनें और उत्पादन सदस्यताओं में उन्हें चालू करने से पहले लाइसेंस की पुष्टि करें।
3. **Cloud Secure Score और सुझावों की समीक्षा करें।** इंटरनेट पर खुली पहुँच, पहचान जोखिम, शोषण योग्य कमजोरियों और अनुपस्थित लॉगिंग को प्राथमिकता दें। स्कोर को पूर्ण अनुपालन का प्रमाण न मानें।
4. **Microsoft Entra नियंत्रण कॉन्फ़िगर करें।** महत्वपूर्ण खातों के लिए फ़िशिंग-रोधी MFA अनिवार्य करें, न्यूनतम विशेषाधिकार वाला RBAC अपनाएँ और विशेषाधिकार प्राप्त पहुँच की समीक्षा करें।
5. **Microsoft Sentinel को अलर्ट भेजें।** अलर्ट प्राप्ति, विश्लेषणात्मक नियम, ज़िम्मेदारी, प्रतिक्रिया स्वचालन और डेटा प्रतिधारण की पुष्टि करें।
6. **बदलावों के बाद फिर जाँचें।** पैच लगाने, आर्किटेक्चर बदलने, नए कनेक्टर जोड़ने या योजनाएँ बदलने के बाद सुझावों की समीक्षा करें।

## व्यावहारिक समीक्षा सूची

- **पहचान:** पुराने खाते हटाएँ, स्थायी प्रशासक पहुँच घटाएँ और Conditional Access अपवादों की समीक्षा करें।
- **नेटवर्क:** सार्वजनिक प्रबंधन पोर्ट हटाएँ, NSG स्रोत सीमाएँ संकीर्ण करें और पुष्टि करें कि फ़ायरवॉल तथा WAF लॉग निगरानी workspace तक पहुँचते हैं।
- **डेटा:** संवेदनशील डेटा संग्रहों का वर्गीकरण करें, एन्क्रिप्शन और कुंजी के स्वामित्व की पुष्टि करें तथा बैकअप पुनर्स्थापन जाँचें।
- **पता लगाना:** अलर्ट की गंभीरता, सूचना का मार्ग, घटना का स्वामित्व और प्रतिक्रिया-पुस्तिका की पुष्टि करें।
- **शासन:** हर नीति पहल के लिए मालिक, अपवाद की समाप्ति तिथि और आवश्यक ढाँचे के साक्ष्य तय करें।

______

## संदर्भ

- [Azure Security Center दस्तावेज़](https://docs.microsoft.com/en-us/azure/security-center/)
- [Azure Policy सेवा](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)

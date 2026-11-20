---
title: "Microsoft Defender for Cloud দিয়ে আপনার ক্লাউড পরিবেশ সুরক্ষিত করুন"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Microsoft Defender for Cloud দিয়ে Azure ওয়ার্কলোড সুরক্ষিত করুন। Azure Security Center-এর পুরোনো পরিভাষা, সুপারিশ, নীতি এবং প্রতিক্রিয়ার ধাপগুলো পর্যালোচনা করুন।"
tags: ["Azure", "Security Center", "ক্লাউড নিরাপত্তা", "Azure Sentinel", "Azure Defender", "নেটওয়ার্ক নিরাপত্তা", "পরিচয় ব্যবস্থাপনা", "তথ্য নিরাপত্তা", "হুমকি শনাক্তকরণ", "হুমকির প্রতিক্রিয়া", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "মেঘের চিহ্নে ঘেরা একটি ঢাল নিরাপদ ক্লাউড পরিবেশের প্রতীক। ঢালের ওপর Azure Security Center-এর লোগো রয়েছে।"
coverCaption: ""
---

**Azure Security Center দিয়ে ক্লাউড পরিবেশ কীভাবে সুরক্ষিত করবেন**

প্রতিষ্ঠানের তথ্য, অ্যাপ্লিকেশন এবং অবকাঠামোকে হুমকি থেকে বাঁচাতে ক্লাউড পরিবেশ সুরক্ষিত রাখা জরুরি। Microsoft-এর **Azure Security Center** আপনার নিরাপত্তার অবস্থা উন্নত করতে এবং Azure পরিবেশে সম্ভাব্য ঝুঁকি দ্রুত শনাক্ত করতে সাহায্য করে। এই নিবন্ধে Azure Security Center দিয়ে ক্লাউড পরিবেশ সুরক্ষিত করার পদ্ধতি এবং বিভিন্ন নিরাপত্তা বৈশিষ্ট্য বাস্তবায়নের ভালো চর্চা ব্যাখ্যা করা হয়েছে। প্রযুক্তিগত বিবরণ ও উদাহরণও রয়েছে, যাতে আপনি নিজের পরিবেশে পদক্ষেপগুলো প্রয়োগ করতে পারেন।

*মূল নিবন্ধ প্রকাশের পর পণ্যের নাম বদলেছে। Microsoft Azure Security Center এখন Microsoft Defender for Cloud। Azure Active Directory এখন Microsoft Entra ID। Azure Sentinel এখন Microsoft Sentinel। Azure Defender বলতে Defender পরিকল্পনা এবং Defender for Cloud-এর ওয়ার্কলোড সুরক্ষা বোঝায়। ২০২৩ সালের পরিভাষা বোঝানোর ক্ষেত্রে নিচে পুরোনো নাম রাখা হয়েছে।*

বর্তমান [Defender for Cloud পরিচিতি](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) একে ক্লাউড-নেটিভ অ্যাপ্লিকেশন সুরক্ষা প্ল্যাটফর্ম হিসেবে বর্ণনা করে। এতে ক্লাউড নিরাপত্তার অবস্থা ব্যবস্থাপনা, DevSecOps এবং ক্লাউড ওয়ার্কলোড সুরক্ষা অন্তর্ভুক্ত। কোন বৈশিষ্ট্য পাওয়া যাবে এবং লাইসেন্স কী হবে, তা ক্লাউড, রিসোর্সের ধরন, সাবস্ক্রিপশন ও পরিকল্পনার ওপর নির্ভর করে।

______

## Azure Security Center বোঝা

Azure Security Center হলো **অবকাঠামোর নিরাপত্তা ব্যবস্থাপনার একটি সমন্বিত ব্যবস্থা**। এটি ক্লাউড পরিবেশের সম্ভাব্য দুর্বলতা খুঁজে বের করে সমাধান করতে সাহায্য করে। হুমকি শনাক্তকরণ, নিরাপত্তার অবস্থা ব্যবস্থাপনা এবং কমপ্লায়েন্স ব্যবস্থাপনাসহ বিভিন্ন বৈশিষ্ট্যের মাধ্যমে Azure পরিবেশ সুরক্ষিত রাখতে সহায়তা করে।

**নিরবচ্ছিন্ন নিরাপত্তা মূল্যায়ন** এবং **উন্নত হুমকি সুরক্ষা** Azure Security Center-এর দুটি মূল বৈশিষ্ট্য। নিরবচ্ছিন্ন নিরাপত্তা মূল্যায়ন পরিবেশের সম্ভাব্য নিরাপত্তা সমস্যা খুঁজে পেতে সাহায্য করে। উন্নত হুমকি সুরক্ষা সম্ভাব্য হুমকি শনাক্ত ও মোকাবিলায় সহায়তা করে।

______

## নিরাপত্তা নীতি ও কমপ্লায়েন্স মান বাস্তবায়ন

Azure Security Center দিয়ে পুরো ক্লাউড পরিবেশের নিরাপত্তা নীতি বাস্তবায়ন ও পরিচালনা করা যায়। **Azure Policy** পরিষেবা দিয়ে নিজস্ব নিরাপত্তা নীতি তৈরি করুন, অথবা অন্তর্নির্মিত নীতি ব্যবহার করে ভালো চর্চা ও কমপ্লায়েন্স মান কার্যকর করুন। [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) এবং [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)-এর মতো শিল্পমানের সঙ্গে নিরাপত্তার অবস্থা মিলিয়েও দেখতে পারেন।

Azure Security Center-এর কমপ্লায়েন্স ব্যবস্থাপনা বৈশিষ্ট্য প্রতিষ্ঠানের নিয়ন্ত্রক কাঠামো অনুযায়ী কমপ্লায়েন্সের অবস্থা অনুসরণ করতে সাহায্য করে। এর মধ্যে [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) এবং [PCI DSS](https://www.pcisecuritystandards.org/)-এর মতো কাঠামো রয়েছে।

______

## Azure রিসোর্স সুরক্ষিত করা

ক্লাউড পরিবেশ সুরক্ষিত রাখার একটি গুরুত্বপূর্ণ অংশ হলো **রিসোর্সের নিরাপত্তা-স্বাস্থ্য বজায় রাখা**। Azure Security Center **Secure Score** দিয়ে রিসোর্সের সামগ্রিক নিরাপত্তার অবস্থা বোঝায়। Azure Security Center-এর সুপারিশগুলো বাস্তবায়ন করলে স্কোর উন্নত হয়।

### নেটওয়ার্ক নিরাপত্তা

**Network Security Groups (NSGs)**, **Azure Firewall** এবং **Web Application Firewall (WAF)**-এর মতো ব্যবস্থা Azure পরিবেশকে সম্ভাব্য হুমকি থেকে রক্ষা করে। এগুলো দিয়ে আগত ও বহির্গামী নেটওয়ার্ক ট্র্যাফিক নিয়ন্ত্রণ করুন, যাতে অননুমোদিত প্রবেশ ও আক্রমণ ঠেকানো যায়।

#### Network Security Groups (NSGs)

NSG Azure রিসোর্সের জন্য ভার্চুয়াল ফায়ারওয়ালের মতো কাজ করে। রিসোর্সে আসা ও রিসোর্স থেকে যাওয়া ট্র্যাফিক অনুমোদন বা অস্বীকার করার নিয়ম এতে নির্ধারণ করা যায়। নির্দিষ্ট ট্র্যাফিক অনুমোদন বা অস্বীকার করতে NSG তৈরি করার উদাহরণ:

```azurecli
# একটি Network Security Group তৈরি করুন
az network nsg create --name MyNSG --resource-group MyResourceGroup

# ট্র্যাফিক অনুমোদন বা অস্বীকারের নিয়ম যোগ করুন
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
[Network Security Groups-এর](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) বিস্তারিত Microsoft-এর নথিতে দেখুন।

উপরের উদাহরণটি যেকোনো IPv4 উৎস থেকে আগত TCP পোর্ট 80 ট্র্যাফিক অনুমোদন করে। উৎপাদন পরিবেশে নির্দিষ্ট উৎস-পরিসর, প্রাইভেট এন্ডপয়েন্ট বা লোড ব্যালান্সারের পথ ব্যবহার করুন। উদাহরণটি ব্যবহারের আগে বর্তমান [NSG নিরাপত্তা পরিচিতি](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) পড়ুন।

#### Azure Firewall

Azure Firewall হলো পরিচালিত ক্লাউড-ভিত্তিক নেটওয়ার্ক নিরাপত্তা পরিষেবা, যা Azure রিসোর্স রক্ষা করে। এতে হুমকি-তথ্যভিত্তিক ফিল্টারিং, ওয়েব বিভাগ এবং কেন্দ্রীভূত লগিং ও বিশ্লেষণের মতো বৈশিষ্ট্য রয়েছে। Azure Firewall সেটআপ করতে Microsoft-এর [দ্রুত শুরু নির্দেশিকা](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep) অনুসরণ করুন।

#### Web Application Firewall (WAF)

Web Application Firewall (WAF) হলো **Azure Application Gateway**-এর একটি বৈশিষ্ট্য। এটি SQL-ভিত্তিক ইনজেকশন আক্রমণ, ক্রস-সাইট স্ক্রিপ্টিং আক্রমণ এবং অন্য সাধারণ ওয়েব আক্রমণ থেকে ওয়েব অ্যাপ্লিকেশন রক্ষা করে। বিদ্যমান ওয়েব অ্যাপ্লিকেশনের সঙ্গে WAF যুক্ত করে নির্দিষ্ট আক্রমণের ধরন ঠেকাতে নিজস্ব নিয়ম তৈরি করা যায়।

WAF চালু রেখে Application Gateway তৈরির উদাহরণ:

```azurecli
# একটি WAF নীতি তৈরি করুন
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# ভার্চুয়াল নেটওয়ার্ক ও সাবনেট তৈরি করুন
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# একটি পাবলিক IP ঠিকানা তৈরি করুন
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# WAF চালু রেখে Application Gateway তৈরি করুন
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
[Web Application Firewall-এর](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) বিস্তারিত Microsoft-এর নথিতে দেখুন।

### পরিচয় ও প্রবেশাধিকার ব্যবস্থাপনা

**Microsoft Entra ID, যার আগের নাম Azure Active Directory (Azure AD),** ক্লাউড পরিবেশ সুরক্ষার একটি জরুরি অংশ। পরিচয় ও প্রবেশাধিকার ব্যবস্থাপনা উন্নত করতে Defender for Cloud সুপারিশ দেয়। এর মধ্যে **Multi-Factor Authentication (MFA)** চালু করা, **Role-Based Access Control (RBAC)** প্রয়োগ করা এবং সন্দেহজনক কার্যকলাপ পর্যবেক্ষণ করা রয়েছে।

#### Multi-Factor Authentication (MFA)

MFA প্রবেশাধিকার দেওয়ার আগে ব্যবহারকারীর কাছে দুই বা তার বেশি ধরনের যাচাইকরণ চায়। এতে Azure AD অ্যাকাউন্টে অতিরিক্ত নিরাপত্তা স্তর যোগ হয়। প্রতিষ্ঠানে MFA চালু করতে Microsoft-এর [ধাপে ধাপে নির্দেশিকা](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) অনুসরণ করুন।

উদাহরণ: একজন ব্যবহারকারীর জন্য MFA চালু করা

```powershell
# Azure AD-তে সংযোগ করুন
Connect-AzureAD

# নির্দিষ্ট ব্যবহারকারীর জন্য MFA চালু করুন
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

RBAC Azure রিসোর্সে সূক্ষ্মভাবে অনুমতি নির্ধারণ করতে দেয়, যাতে প্রত্যেক ব্যবহারকারী যথাযথ প্রবেশাধিকার পায়। প্রতিষ্ঠানের রিসোর্সে প্রবেশাধিকার পরিচালনার জন্য ব্যবহারকারী, গোষ্ঠী বা অ্যাপ্লিকেশনকে ভূমিকা দেওয়া যায়। RBAC বাস্তবায়নের জন্য Microsoft-এর [সরকারি নির্দেশিকা](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) অনুসরণ করুন।

উদাহরণ: একজন ব্যবহারকারীকে ভূমিকা দেওয়া

```azurecli
# একজন ব্যবহারকারীকে Reader ভূমিকা দিন
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### সন্দেহজনক কার্যকলাপ পর্যবেক্ষণ

Azure AD-এর **Identity Protection** এবং **Conditional Access** বৈশিষ্ট্য সন্দেহজনক কার্যকলাপ পর্যবেক্ষণ ও মোকাবিলায় সাহায্য করে। Identity Protection মেশিন লার্নিং দিয়ে অস্বাভাবিক আচরণ ও ঝুঁকিপূর্ণ সাইন-ইন শনাক্ত করে। Conditional Access ডিভাইস, অবস্থান ও ঝুঁকির মতো বিষয়ের ওপর ভিত্তি করে প্রবেশাধিকার নিয়ন্ত্রণের নীতি নির্ধারণ করতে দেয়।

Azure AD Identity Protection সেটআপ করতে Microsoft-এর [সরকারি নির্দেশিকা](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) অনুসরণ করুন।

উদাহরণ: Conditional Access নীতি তৈরি করা

```powershell
# Azure AD-তে সংযোগ করুন
Connect-AzureAD

# Conditional Access নীতি তৈরি করুন
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "অজানা অবস্থান থেকে ব্যবহারকারীর সাইন-ইন আটকান।"
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
Microsoft-এর নথিতে [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) এবং [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) সম্পর্কে আরও জানুন।

### তথ্য নিরাপত্তা

ক্লাউডে তথ্য সুরক্ষিত রাখা জরুরি। Azure Security Center-এ তথ্য নিরাপত্তার জন্য **Azure Information Protection**, **Azure Storage Service Encryption** এবং **Azure Disk Encryption**-এর মতো বৈশিষ্ট্য রয়েছে। এগুলো তথ্য এনক্রিপ্ট করতে এবং প্রবেশাধিকার পরিচালনা করতে সাহায্য করে, যাতে সংবেদনশীল তথ্য সুরক্ষিত থাকে।

#### Azure Information Protection

**Azure Information Protection (AIP)** ক্লাউড-ভিত্তিক পরিষেবা, যা সংবেদনশীল নথি ও ইমেইল শ্রেণিবদ্ধ, লেবেল এবং সুরক্ষিত করতে সাহায্য করে। AIP-তে "গোপনীয়" ও "ব্যক্তিগত"-এর মতো অন্তর্নির্মিত লেবেল রয়েছে, যা প্রতিষ্ঠানের প্রয়োজন অনুযায়ী সাজানো যায়। পূর্বনির্ধারিত নিয়মের ভিত্তিতে লেবেল স্বয়ংক্রিয়ভাবে প্রয়োগ করাও সম্ভব। শুরু করতে Microsoft-এর [সরকারি নির্দেশিকা](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) অনুসরণ করুন।

উদাহরণ: নিজস্ব লেবেল তৈরি করা

```powershell
# AIP পরিষেবায় সংযোগ করুন
Connect-AipService

# সুরক্ষা সেটিংসহ নিজস্ব লেবেল তৈরি করুন
$LabelName = "সংবেদনশীল - শুধু অভ্যন্তরীণ ব্যবহারের জন্য"
$LabelDescription = "এই লেবেল শুধু অভ্যন্তরীণ ব্যবহারের জন্য এনক্রিপশন ও প্রবেশাধিকার নীতি প্রয়োগ করে।"
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** Azure Storage অ্যাকাউন্টের Blob, File, Table এবং Queue-সহ সংরক্ষিত তথ্য স্বয়ংক্রিয়ভাবে এনক্রিপ্ট করে। SSE স্টোরেজ অ্যাকাউন্ট স্তরে এনক্রিপশনের জন্য Azure-পরিচালিত বা গ্রাহক-পরিচালিত কী ব্যবহার করে। SSE চালু করতে Microsoft-এর [ধাপে ধাপে নির্দেশিকা](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) অনুসরণ করুন।

Azure Information Protection একটি পুরোনো পণ্যের নাম। Microsoft-এর বর্তমান Sentinel বৈশিষ্ট্য-প্রাপ্যতার নথিতে একে অবসরে যাওয়া পণ্য হিসেবে তালিকাভুক্ত করা হয়েছে। নতুন লেবেলিং ব্যবস্থা চালুর আগে Microsoft Purview Information Protection-এর বর্তমান নথি দেখুন।

উদাহরণ: একটি স্টোরেজ অ্যাকাউন্টে SSE চালু করা

```azurecli
# Azure-পরিচালিত কী দিয়ে SSE চালু করুন
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** ভার্চুয়াল মেশিনের ডিস্ক BitLocker (Windows) বা dm-crypt (Linux) দিয়ে এনক্রিপ্ট করে সুরক্ষিত করতে সাহায্য করে। এনক্রিপশন কী ও গোপন মান Azure Key Vault-এ সুরক্ষিত থাকে, ফলে সংরক্ষিত তথ্য এনক্রিপ্ট থাকে। Azure Disk Encryption চালু করতে Microsoft-এর [সরকারি নির্দেশিকা](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) অনুসরণ করুন।

উদাহরণ: ভার্চুয়াল মেশিনে Azure Disk Encryption চালু করা

```azurecli
# Windows VM-এর জন্য Azure Disk Encryption চালু করুন
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) এবং [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview)-এর বিস্তারিত Microsoft-এর নথিতে দেখুন।
______

## হুমকি শনাক্ত ও মোকাবিলা করা

Azure Security Center উন্নত হুমকি শনাক্তকরণ ব্যবহার করে সম্ভাব্য হুমকি খুঁজে সতর্ক করে। **Azure Sentinel**-এর সঙ্গে সংযুক্ত করলে পুরো পরিবেশের নিরাপত্তা ঘটনা পর্যবেক্ষণ, তদন্ত ও মোকাবিলা করা যায়।

### হুমকি শনাক্তকরণ

সম্ভাব্য নিরাপত্তা হুমকি শনাক্ত করতে Azure Security Center **Azure Defender** ব্যবহার করে। Azure Defender রিসোর্সে অনুপ্রবেশের লক্ষণ পর্যবেক্ষণ করে এবং প্রতিক্রিয়ায় সাহায্য করার জন্য সতর্কতা ও সুপারিশ দেয়। Azure Defender চালু করতে Microsoft-এর [সরকারি নির্দেশিকা](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable) অনুসরণ করুন।

উদাহরণ: একটি সাবস্ক্রিপশনে Azure Defender চালু করা

```azurecli
# একটি সাবস্ক্রিপশনে Azure Defender চালু করুন
az security auto-provisioning-setting update --name default --auto-provision on
```
### হুমকির প্রতিক্রিয়া

হুমকি শনাক্ত হলে দ্রুত ও কার্যকরভাবে প্রতিক্রিয়া জানান। Azure Security Center-এর **Security Incident** ব্যবস্থাপনা নিরাপত্তা ঘটনা তদন্ত ও মোকাবিলা করতে সাহায্য করে। নিরাপত্তা ঘটনার প্রতিক্রিয়া স্বয়ংক্রিয় করতে **Azure Sentinel**-এর সঙ্গে যুক্ত করে প্রতিক্রিয়া কার্যপ্রবাহ তৈরি করা যায়। Azure Security Center ও Azure Sentinel একীভূত করার বিষয়ে **সরকারি নথি** দেখুন।

উদাহরণ: Azure Sentinel-এর জন্য Logic অ্যাপের কার্যপ্রবাহ তৈরি করা

```azurecli
# একটি রিসোর্স গ্রুপ তৈরি করুন
az group create --name MyResourceGroup --location EastUS

# একটি Logic App তৈরি করুন
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
`playbook-definition.json` ফাইলে Logic অ্যাপের কার্যপ্রবাহ-এর সংজ্ঞা থাকতে হবে। Azure Sentinel-এর প্রতিক্রিয়া কার্যপ্রবাহ উদাহরণ [Azure-Sentinel GitHub সংগ্রহস্থলে](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks) পাবেন।

Azure Security Center-এর হুমকি শনাক্তকরণ Azure Sentinel-এর সঙ্গে যুক্ত করে Azure পরিবেশে হুমকি শনাক্ত ও মোকাবিলার নিরাপত্তা কৌশল তৈরি করুন। [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) এবং [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview)-এর বিস্তারিত সরকারি নথিতে দেখুন।

বর্তমান সংযোগ-পদ্ধতিতে [Defender for ক্লাউড সংযোগকারী](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) দিয়ে Defender for Cloud-এর সতর্কতা Microsoft Sentinel-এ পাঠানো হয়। স্বয়ংক্রিয় প্রতিক্রিয়ার ওপর নির্ভর করার আগে Defender-এর পোর্টাল বা Azure পোর্টাল-এ সংযোগকারী, তথ্য সংগ্রহের নিয়ম, বিশ্লেষণ নিয়ম এবং ঘটনা ব্যবস্থাপনার কর্মপ্রবাহ যাচাই করুন।
______

## পর্যবেক্ষণ ও প্রতিবেদন

নিরাপদ ক্লাউড পরিবেশ বজায় রাখতে পর্যবেক্ষণ ও প্রতিবেদন জরুরি। Azure Security Center **Security Dashboard**, **Security Alerts** এবং **Compliance Reports**-এর মতো সরঞ্জাম দেয়।

### নিরাপত্তা ড্যাশবোর্ড

Azure Security Center-এর Security Dashboard নিরাপত্তার অবস্থার সারসংক্ষেপ দেখায়। এতে Secure Score, নিরাপত্তা সুপারিশ ও সক্রিয় সতর্কতা দেখা যায়। ড্যাশবোর্ড কমপ্লায়েন্সের অবস্থা দেখায় এবং সময়ের সঙ্গে অগ্রগতি অনুসরণ করতে দেয়।

### নিরাপত্তা সতর্কতা

সম্ভাব্য হুমকি শনাক্ত হলে Azure Security Center নিরাপত্তা সতর্কতা তৈরি করে। সতর্কতায় হুমকির বিবরণ ও ঝুঁকি কমানোর সুপারিশ থাকে। Azure Security Center দিয়ে ইমেইল বা SMS-এ বিজ্ঞপ্তি পাঠানো যায়, অথবা [Slack](https://slack.com/) ও [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software)-এর মতো তৃতীয় পক্ষের সরঞ্জামের সঙ্গে যুক্ত করা যায়।

### কমপ্লায়েন্স প্রতিবেদন

Azure Security Center GDPR, HIPAA ও PCI DSS-এর মতো নিয়ন্ত্রক কাঠামোর জন্য কমপ্লায়েন্স প্রতিবেদন তৈরি করে। এসব প্রতিবেদনে প্রতিষ্ঠানের কমপ্লায়েন্সের অবস্থা অনুসরণ করুন এবং উন্নতির প্রয়োজন এমন ক্ষেত্র শনাক্ত করুন।

______

## Azure Security Center-এর ভালো চর্চা

Azure Security Center থেকে কার্যকর ফল পেতে নিচের চর্চাগুলো বাস্তবায়ন করুন:

1. **সব সাবস্ক্রিপশনে Azure Security Center চালু করুন**: সব Azure সাবস্ক্রিপশন সুরক্ষিত আছে কি না নিশ্চিত করুন।
2. **নিয়মিত Secure Score পর্যালোচনা করুন**: নিরাপত্তার সামগ্রিক অবস্থা বুঝুন এবং উন্নতির ক্ষেত্র খুঁজুন।
3. **নিরাপত্তা সুপারিশ বাস্তবায়ন করুন**: Azure Security Center-এর সুপারিশ মেনে নিরাপত্তা উন্নত করুন ও ঝুঁকি কমান।
4. **নিরাপত্তা সতর্কতা পর্যবেক্ষণ করুন**: সতর্কতা পর্যালোচনা করে দ্রুত প্রতিক্রিয়া জানান।
5. **কমপ্লায়েন্সের শর্ত হালনাগাদ রাখুন**: নীতি নিয়মিত পর্যালোচনা ও হালনাগাদ করে নতুন নিয়ন্ত্রক কাঠামোর সঙ্গে সামঞ্জস্য বজায় রাখুন।

## Defender for Cloud-এর বর্তমান কর্মপ্রবাহ

বর্তমান স্থাপনার জন্য নিচের ক্রম অনুসরণ করুন। আগের অংশগুলোর নাম পুরোনো তথ্য খুঁজতে কাজে লাগতে পারে, তবে portal ও নথিতে Defender for Cloud পরিভাষা ব্যবহৃত হয়।

1. **সাবস্ক্রিপশন ও সংযোগকারী-এর তালিকা করুন।** Azure সাবস্ক্রিপশন, AWS বা GCP সংযোগকারী, DevOps প্রকল্প এবং গুরুত্বপূর্ণ রিসোর্স নথিভুক্ত করুন।
2. **প্রয়োজনীয় Defender পরিকল্পনা চালু করুন।** ওয়ার্কলোড অনুযায়ী পরিকল্পনা বেছে নিন এবং উৎপাদন সাবস্ক্রিপশনে চালুর আগে লাইসেন্স নিশ্চিত করুন।
3. **Cloud Secure Score ও সুপারিশ পর্যালোচনা করুন।** ইন্টারনেটে উন্মুক্ত রিসোর্স, পরিচয়ের ঝুঁকি, কাজে লাগানো যায় এমন দুর্বলতা এবং অনুপস্থিত লগিংকে অগ্রাধিকার দিন। স্কোরকে পূর্ণ কমপ্লায়েন্সের প্রমাণ মনে করবেন না।
4. **Microsoft Entra নিয়ন্ত্রণ কনফিগার করুন।** গুরুত্বপূর্ণ অ্যাকাউন্টে ফিশিং প্রতিরোধী MFA বাধ্যতামূলক করুন, সর্বনিম্ন-অধিকারের RBAC ব্যবহার করুন এবং বিশেষাধিকারপ্রাপ্ত প্রবেশাধিকার পর্যালোচনা করুন।
5. **Microsoft Sentinel-এ সতর্কতা পাঠান।** সতর্কতা গ্রহণ, বিশ্লেষণ নিয়ম, দায়িত্ব, প্রতিক্রিয়া স্বয়ংক্রিয়করণ এবং সংরক্ষণের সময়সীমা যাচাই করুন।
6. **পরিবর্তনের পর আবার পরীক্ষা করুন।** প্যাচ, স্থাপত্য পরিবর্তন, নতুন সংযোগকারী বা পরিকল্পনা পরিবর্তনের পর সুপারিশ পর্যালোচনা করুন।

## ব্যবহারিক পর্যালোচনা তালিকা

- **পরিচয়:** অপ্রয়োজনীয় পুরোনো অ্যাকাউন্ট সরান, স্থায়ী প্রশাসক প্রবেশাধিকার কমান এবং Conditional Access ব্যতিক্রম পর্যালোচনা করুন।
- **নেটওয়ার্ক:** প্রকাশ্য ব্যবস্থাপনা পোর্ট বন্ধ করুন, NSG উৎস-পরিসর সীমিত করুন এবং firewall ও WAF লগ পর্যবেক্ষণ কর্মক্ষেত্রে পৌঁছায় কি না নিশ্চিত করুন।
- **তথ্য:** সংবেদনশীল ডেটা-ভান্ডার শ্রেণিবদ্ধ করুন, এনক্রিপশন ও কী-এর মালিকানা যাচাই করুন এবং ব্যাকআপ পুনরুদ্ধার পরীক্ষা করুন।
- **শনাক্তকরণ:** সতর্কতার গুরুত্ব, বিজ্ঞপ্তির গন্তব্য, ঘটনার দায়িত্ব এবং প্রতিক্রিয়া কার্যপ্রবাহ যাচাই করুন।
- **শাসন:** প্রতিটি নীতি উদ্যোগের মালিক, ব্যতিক্রমের মেয়াদ শেষের তারিখ এবং প্রয়োজনীয় কাঠামোর প্রমাণ নির্ধারণ করুন।

______

## তথ্যসূত্র

- [Azure Security Center-এর নথি](https://docs.microsoft.com/en-us/azure/security-center/)
- [Azure Policy পরিষেবা](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)

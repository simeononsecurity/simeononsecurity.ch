---
title: "PowerShell के साथ Active Directory प्रशासन"
date: 2023-07-25
toc: true
draft: false
description: जानिए कि कैसे प्रभावी रूप से Active Directory मॉड्यूल को PowerShell के लिए इंस्टॉल और उपयोग करें ताकि आपके Windows Active Directory प्रशासन कार्य सरल हो सकें।
genre:
- प्रौद्योगिकी
- विंडोज़
- PowerShell
- Active Directory
- प्रशासन
- स्क्रिप्टिंग
- आईटी
- स्वचालन
- Windows Server
- Microsoft
tags:
- PowerShell के लिए Active Directory मॉड्यूल
- PowerShell में Active Directory मॉड्यूल आयात करें
- Windows PowerShell के लिए Active Directory मॉड्यूल
- Active Directory PowerShell इंस्टॉल
- Active Directory PowerShell इंस्टॉल करें
- PowerShell में Windows 10 के लिए Active Directory मॉड्यूल इंस्टॉल करें
- Windows 10 के लिए Active Directory PowerShell मॉड्यूल इंस्टॉल करें
- Active Directory PowerShell मॉड्यूल प्राप्त करें
- AD प्रशासन
- Windows Active Directory
- PowerShell cmdlets
- AD जानकारी प्राप्त करें
- AD ऑब्जेक्ट बनाएं
- AD ऑब्जेक्ट संशोधित करें
- AD सुरक्षा प्रबंधित करें
- AD उपयोगकर्ता प्रबंधन
- AD समूह प्रबंधन
- AD OU प्रबंधन
- PowerShell स्क्रिप्टिंग
- Windows Server प्रशासन
- Microsoft PowerShell
- AD कार्यों को स्वचालित करें
- PowerShell मॉड्यूल इंस्टॉलेशन
- AD प्रशासन गाइड
- Active Directory प्रबंधन
- AD सुरक्षा प्रबंधन
- PowerShell स्वचालन
- Active Directory PowerShell कमांड
- PowerShell cmdlet संदर्भ
cover: /img/cover/active-directory-module-powershell-installation-usage-guide.webp
coverAlt: एक कंप्यूटर स्क्रीन का चित्र जिसमें PowerShell कंसोल रंगीन cmdlets के साथ दिख रहा है, जिसके चारों ओर उपयोगकर्ता खाते और समूहों के सारगर्भित प्रतिनिधित्व हैं, और पृष्ठभूमि गहरे रंग की है।
coverCaption: PowerShell के साथ Active Directory प्रशासन की शक्ति को अनलॉक करें।
lastmod: 2026-10-08
---

## परिचय

आज के समय में Windows Active Directory (AD) वातावरण में उपयोगकर्ता खाते, सुरक्षा समूह, और अन्य संसाधनों का प्रबंधन और रखरखाव कुशल और सरल प्रक्रियाओं की मांग करता है। PowerShell, Microsoft द्वारा विकसित एक शक्तिशाली स्क्रिप्टिंग भाषा, AD प्रशासन कार्यों को सरल बनाने के लिए **Active Directory मॉड्यूल** प्रदान करता है। यह मॉड्यूल कई cmdlets प्रदान करता है जो प्रशासकों को विभिन्न ऑपरेशनों को स्वचालित करने और AD को प्रभावी ढंग से प्रबंधित करने में सक्षम बनाते हैं। इस लेख में, हम PowerShell के लिए Active Directory मॉड्यूल की स्थापना और उपयोग का अन्वेषण करेंगे।

## PowerShell के लिए Active Directory मॉड्यूल की स्थापना

PowerShell के लिए Active Directory मॉड्यूल का उपयोग शुरू करने के लिए, आपको यह सुनिश्चित करना होगा कि यह आपके सिस्टम पर इंस्टॉल है। स्थापना प्रक्रिया आपके ऑपरेटिंग सिस्टम के आधार पर भिन्न हो सकती है। यहाँ **Windows 10**, **Windows 11**, और **Windows Server** पर मॉड्यूल इंस्टॉल करने के चरण दिए गए हैं:

### Windows 10 और Windows 11 - PowerShell
1. **Windows PowerShell** को प्रशासनिक अधिकारों के साथ खोलें।
2. मॉड्यूल इंस्टॉल करने के लिए निम्नलिखित कमांड चलाएं:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. स्थापना पूरी होने तक प्रतीक्षा करें। समाप्त होने के बाद, आप Active Directory मॉड्यूल का उपयोग शुरू कर सकते हैं।

### Windows Server 
1. **Windows PowerShell** को प्रशासनिक अधिकारों के साथ खोलें।
2. मॉड्यूल इंस्टॉल करने के लिए निम्नलिखित कमांड चलाएं:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. स्थापना पूरी होने तक प्रतीक्षा करें। समाप्त होने के बाद, आप Active Directory मॉड्यूल का उपयोग शुरू कर सकते हैं।

### ऑफ़लाइन सिस्टम

ऑफ़लाइन सिस्टम थोड़े अधिक जटिल होते हैं। कुछ तरीके हैं, लेकिन हम जो तरीका सुझाते हैं वह निम्नलिखित स्क्रिप्ट के उपयोग से है:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## PowerShell में Active Directory मॉड्यूल आयात करना

PowerShell में Active Directory मॉड्यूल का उपयोग करने से पहले, आपको इसे अपनी वर्तमान सत्र में आयात करना होगा। मॉड्यूल आयात करने के लिए निम्न चरणों का पालन करें:

1. प्रशासनिक अधिकारों के साथ **Windows PowerShell** लॉन्च करें।
2. मॉड्यूल आयात करने के लिए निम्नलिखित कमांड चलाएं:

```powershell
Import-Module ActiveDirectory
```

3. Active Directory मॉड्यूल आयात हो जाएगा, और अब आप इसके cmdlets और फ़ंक्शंस तक पहुँच सकते हैं।

## PowerShell के लिए Active Directory मॉड्यूल का उपयोग

Active Directory मॉड्यूल आयात करने के बाद, आप इसके समृद्ध cmdlets सेट का उपयोग विभिन्न प्रशासनिक कार्यों को करने के लिए कर सकते हैं। यहाँ कुछ सामान्य उपयोग किए जाने वाले cmdlets और उनकी कार्यक्षमताओं पर एक नज़र है:

### Active Directory जानकारी प्राप्त करना

Active Directory (AD) वातावरण का प्रभावी प्रबंधन करने के लिए, आपको विभिन्न AD ऑब्जेक्ट्स जैसे उपयोगकर्ता, समूह, और संगठनात्मक इकाइयों (OUs) की जानकारी प्राप्त करनी होती है। PowerShell शक्तिशाली cmdlets प्रदान करता है जो जानकारी प्राप्त करने की प्रक्रिया को सरल बनाते हैं।

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps): यह cmdlet आपको AD उपयोगकर्ताओं के बारे में विस्तृत जानकारी प्राप्त करने की अनुमति देता है। आप उपयोगकर्ता नाम, डिस्प्ले नाम, ईमेल पता, और अन्य गुण प्राप्त कर सकते हैं। उदाहरण के लिए, उन सभी उपयोगकर्ताओं को प्राप्त करने के लिए जिनके उपयोगकर्ता नाम "johndoe" से शुरू होते हैं, आप निम्न कमांड चला सकते हैं:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  यह कमांड निर्दिष्ट फ़िल्टर से मेल खाने वाले उपयोगकर्ता ऑब्जेक्ट्स की सूची लौटाएगा।

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps): Get-ADGroup cmdlet के साथ, आप AD समूहों की जानकारी प्राप्त कर सकते हैं। यह समूह नाम, सदस्य, विवरण, और अन्य विवरणों तक पहुँच प्रदान करता है। उदाहरण के लिए, AD वातावरण में सभी सुरक्षा समूहों को प्राप्त करने के लिए, आप निम्न कमांड चला सकते हैं:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  यह Active Directory में सुरक्षा समूहों की सूची प्रदान करेगा।

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps): Get-ADOrganizationalUnit cmdlet का उपयोग AD OUs की जानकारी प्राप्त करने के लिए किया जाता है। यह OU नाम, विवरण, पैरेंट OU, और अन्य गुणों तक पहुँच प्रदान करता है। डोमेन में सभी OUs प्राप्त करने के लिए, आप निम्न कमांड का उपयोग कर सकते हैं:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  इस कमांड को चलाने पर Active Directory में सभी OUs की सूची प्रदर्शित होगी।

इन शक्तिशाली cmdlets का उपयोग करके, आप AD उपयोगकर्ताओं, समूहों, और OUs के बारे में विशिष्ट जानकारी आसानी से प्राप्त कर सकते हैं, जिससे आपके Active Directory वातावरण का कुशल प्रशासन और प्रबंधन संभव होता है।


ये cmdlets आपको विशिष्ट गुण प्राप्त करने, परिणामों को फ़िल्टर करने, और वांछित जानकारी प्राप्त करने के लिए उन्नत क्वेरी करने की अनुमति देते हैं।

### Active Directory ऑब्जेक्ट बनाना और प्रबंधित करना

Active Directory (AD) के साथ काम करते समय, PowerShell में Active Directory मॉड्यूल AD ऑब्जेक्ट्स को बनाने और प्रबंधित करने के लिए शक्तिशाली cmdlets प्रदान करता है। यहाँ AD उपयोगकर्ता, समूह, और संगठनात्मक इकाइयों (OUs) को बनाने के लिए कुछ आवश्यक cmdlets हैं।

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps): यह cmdlet आपको नया AD उपयोगकर्ता बनाने की अनुमति देता है। आप उपयोगकर्ता नाम, पासवर्ड, ईमेल पता, और अन्य गुण निर्दिष्ट कर सकते हैं। उदाहरण के लिए, "john.doe" उपयोगकर्ता नाम और "John Doe" डिस्प्ले नाम के साथ नया उपयोगकर्ता बनाने के लिए, आप निम्न कमांड का उपयोग कर सकते हैं:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  यह कमांड Active Directory में नया उपयोगकर्ता बनाएगा।

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps): New-ADGroup cmdlet आपको नया AD समूह बनाने की अनुमति देता है। आप समूह नाम, विवरण, समूह स्कोप, और अन्य गुण सेट कर सकते हैं। "Marketing" नामक नया समूह और विवरण बनाने के लिए, आप निम्न कमांड चला सकते हैं:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  यह कमांड Active Directory में नया समूह बनाएगा।

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps): New-ADOrganizationalUnit cmdlet के साथ, आप एक नया AD OU बना सकते हैं। आप OU का नाम, पैरेंट OU, और अन्य गुण निर्दिष्ट कर सकते हैं। उदाहरण के लिए, "Departments" OU के अंतर्गत "Sales" नाम का नया OU बनाने के लिए, आप निम्नलिखित कमांड चला सकते हैं:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  यह कमांड Active Directory संरचना में एक नया OU बनाएगा।

इन cmdlets का उपयोग करके, आप आसानी से नए AD उपयोगकर्ता, समूह, और OUs को वांछित गुणों और विन्यासों के साथ बना सकते हैं, जिससे आपके Active Directory वातावरण का कुशल प्रबंधन संभव होता है।


### Active Directory ऑब्जेक्ट्स में संशोधन

मौजूदा Active Directory (AD) ऑब्जेक्ट्स के गुणों और विशेषताओं को संशोधित करने के लिए, PowerShell में Active Directory मॉड्यूल कई उपयोगी cmdlets प्रदान करता है। यहाँ AD उपयोगकर्ताओं, समूहों, और संगठनात्मक इकाइयों (OUs) को संशोधित करने वाले cmdlets पर एक नज़र है।

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps): Set-ADUser cmdlet आपको AD उपयोगकर्ता के गुणों को संशोधित करने की अनुमति देता है। आप डिस्प्ले नाम, ईमेल पता, टेलीफोन नंबर, और अन्य विशेषताओं को अपडेट कर सकते हैं। उदाहरण के लिए, "john.doe" उपयोगकर्ता के टेलीफोन नंबर को बदलने के लिए, आप निम्नलिखित कमांड का उपयोग कर सकते हैं:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  यह कमांड निर्दिष्ट उपयोगकर्ता के टेलीफोन नंबर को Active Directory में संशोधित करेगा।

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps): Set-ADGroup cmdlet के साथ, आप AD समूह के गुणों को संशोधित कर सकते हैं। आप समूह विवरण, सदस्यता, समूह स्कोप, और अन्य विशेषताओं को अपडेट कर सकते हैं। "Marketing" नामक समूह का विवरण "Marketing Team" में बदलने के लिए, आप निम्नलिखित कमांड चला सकते हैं:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  यह कमांड निर्दिष्ट समूह के विवरण को Active Directory में अपडेट करेगा।

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps): Set-ADOrganizationalUnit cmdlet आपको AD OU के गुणों को संशोधित करने की अनुमति देता है। आप OU का नाम, विवरण, और अन्य विशेषताओं को बदल सकते हैं। उदाहरण के लिए, "Sales" नामक OU के विवरण को "Sales Department" में संशोधित करने के लिए, आप निम्नलिखित कमांड चला सकते हैं:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  यह कमांड निर्दिष्ट OU के विवरण को Active Directory संरचना में अपडेट करेगा।

इन cmdlets का उपयोग करके, आप AD ऑब्जेक्ट्स के गुणों और विशेषताओं को आसानी से संशोधित कर सकते हैं, आवश्यक अपडेट और समायोजन कर सकते हैं ताकि आपकी संस्था की आवश्यकताओं को पूरा किया जा सके।


### Active Directory सुरक्षा प्रबंधन

Active Directory (AD) ऑब्जेक्ट्स के प्रबंधन और प्रशासन के अलावा, PowerShell में Active Directory मॉड्यूल विशेष रूप से AD के सुरक्षा-संबंधी पहलुओं को संभालने के लिए cmdlets प्रदान करता है। ये cmdlets व्यवस्थापकों को उपयोगकर्ता पहुँच, समूह सदस्यता, और पासवर्ड-संबंधी कार्यों को कुशलतापूर्वक प्रबंधित करने में मदद करते हैं।

यहाँ कुछ सामान्य रूप से उपयोग किए जाने वाले सुरक्षा-संबंधी cmdlets हैं:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps): यह cmdlet आपको AD समूह में सदस्य जोड़ने की अनुमति देता है। AD समूह और उन उपयोगकर्ता खातों या समूहों को निर्दिष्ट करके जिन्हें आप जोड़ना चाहते हैं, आप आसानी से पहुँच नियंत्रण प्रबंधित कर सकते हैं। उदाहरण के लिए, "JohnDoe" नामक उपयोगकर्ता को "Managers" समूह में जोड़ने के लिए, आप निम्नलिखित कमांड का उपयोग कर सकते हैं:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps): इस cmdlet के साथ, आप AD समूह से सदस्य हटा सकते हैं। AD समूह और उन उपयोगकर्ता खातों या समूहों को निर्दिष्ट करके जिन्हें आप हटाना चाहते हैं, आप समूह सदस्यता को प्रभावी ढंग से प्रबंधित कर सकते हैं। उदाहरण के लिए, "JaneSmith" नामक उपयोगकर्ता को "Developers" समूह से हटाने के लिए, आप निम्नलिखित कमांड का उपयोग कर सकते हैं:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps): यह cmdlet आपको AD उपयोगकर्ता के लिए पासवर्ड सेट करने की अनुमति देता है। उपयोगकर्ता खाता निर्दिष्ट करके और नया पासवर्ड प्रदान करके, आप पासवर्ड नीतियों को लागू कर सकते हैं और सुरक्षित उपयोगकर्ता प्रमाणीकरण सुनिश्चित कर सकते हैं। यहाँ "AmyJohnson" नामक उपयोगकर्ता के लिए नया पासवर्ड सेट करने का उदाहरण है:

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

इन सुरक्षा-संबंधी cmdlets का उपयोग करके, व्यवस्थापक Active Directory वातावरण में उपयोगकर्ता पहुँच, समूह सदस्यता, और पासवर्ड नीतियों का प्रभावी ढंग से प्रबंधन कर सकते हैं।

## PowerShell के लिए उदाहरण Active Directory मॉड्यूल स्क्रिप्ट
```powershell
# Import Active Directory module
Import-Module ActiveDirectory

# Retrieve Active Directory information
Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
Get-ADGroup -Filter 'GroupCategory -eq "Security"'
Get-ADOrganizationalUnit -Filter *

# Create a new Active Directory user
New-ADUser -SamAccountName "john.doe" -Name "John Doe"

# Create a new Active Directory group
New-ADGroup -Name "Marketing" -Description "Marketing Team"

# Create a new Active Directory organizational unit
New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"

# Modify Active Directory objects
Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"

# Manage Active Directory security
Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
```

## निष्कर्ष

सारांश में, **PowerShell के लिए Active Directory मॉड्यूल** एक शक्तिशाली उपकरण है जो Windows Active Directory के कुशल और सुविधाजनक प्रबंधन को सक्षम बनाता है। मॉड्यूल को इंस्टॉल और इम्पोर्ट करके, आप एक व्यापक सेट के **cmdlets** तक पहुँच प्राप्त करते हैं जो विभिन्न AD-संबंधित कार्यों को सरल बनाते हैं।

Active Directory मॉड्यूल के साथ, आप AD ऑब्जेक्ट्स की जानकारी प्राप्त करने, नए ऑब्जेक्ट्स बनाने, गुणों को संशोधित करने, और सुरक्षा प्रबंधन जैसे कई कार्य कर सकते हैं। यह मॉड्यूल व्यवस्थापकों को प्रशासनिक कार्यों को स्वचालित करने, कार्यप्रवाहों को सरल बनाने, और Active Directory वातावरण के सुचारू संचालन को सुनिश्चित करने में मदद करता है।

**PowerShell** और **Active Directory मॉड्यूल** का उपयोग करके, आप अपनी AD प्रशासन क्षमताओं को बढ़ा सकते हैं और AD प्रबंधन प्रक्रियाओं की दक्षता सुधार सकते हैं। चाहे आप सिस्टम व्यवस्थापक हों, आईटी पेशेवर हों, या Active Directory प्रबंधक, Active Directory मॉड्यूल आपको अपने AD इन्फ्रास्ट्रक्चर को प्रभावी ढंग से प्रबंधित करने के लिए आवश्यक उपकरण प्रदान करता है।

**PowerShell** और **Active Directory मॉड्यूल** की शक्ति को अपनाएं ताकि आप अपने AD प्रशासन कार्यों को सरल बना सकें, उत्पादकता बढ़ा सकें, और एक सुरक्षित तथा सुव्यवस्थित Active Directory वातावरण बनाए रख सकें।

## संदर्भ

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)

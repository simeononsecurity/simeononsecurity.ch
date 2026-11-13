---
title: "vSphere प्रबंधन के लिए PowerCLI में दक्षता"
date: 2023-08-02
lastmod: 2026-11-12
toc: true
draft: false
description: "PowerCLI से VMware vSphere प्रबंधित करने, कार्यों को स्वचालित करने और उत्पादकता बढ़ाने का तरीका जानें।"
genre: ["प्रौद्योगिकी", "वर्चुअलाइज़ेशन", "VMware", "आईटी प्रबंधन", "स्वचालन", "कमांड लाइन इंटरफ़ेस", "स्क्रिप्टिंग", "सिस्टम प्रशासन", "क्लाउड कंप्यूटिंग", "डेटा सेंटर प्रबंधन"]
tags: ["PowerCLI", "VMware PowerCLI", "PowerCLI इंस्टॉल करना", "PowerCLI स्थापना", "PowerCLI डाउनलोड", "PowerCLI डाउनलोड करना", "PowerCLI से vCenter कनेक्ट करना", "vSphere प्रबंधन", "वर्चुअल मशीन प्रबंधन", "होस्ट प्रबंधन", "स्वचालन", "स्क्रिप्टिंग", "वर्चुअलाइज़ेशन", "vCenter Server", "ESXi होस्ट", "डेटास्टोर प्रबंधन", "नेटवर्क अडैप्टर प्रबंधन", "वर्चुअल मशीन बनाना", "वर्चुअल मशीन हटाना", "वर्चुअल मशीन सेटिंग", "होस्ट संसाधन प्रबंधन", "CPU आवंटन", "मेमोरी आवंटन", "स्टोरेज सेटिंग", "PowerCLI उदाहरण", "PowerCLI दस्तावेज़", "आईटी प्रबंधन", "सिस्टम प्रशासन", "क्लाउड कंप्यूटिंग"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "चित्र में एक व्यक्ति PowerCLI कमांड से vSphere वातावरण की वर्चुअल मशीनों और होस्ट का प्रबंधन कर रहा है।"
coverCaption: "PowerCLI से vSphere प्रबंधन बेहतर करें"
---

## परिचय

**PowerCLI**, **VMware** का **कमांड लाइन इंटरफ़ेस (CLI)** टूल है। यह प्रशासकों को **VMware vSphere वातावरण प्रबंधित और स्वचालित** करने देता है। इसके अनेक **cmdlet** प्रशासनिक कार्य सरल बनाते हैं और उत्पादकता बढ़ाते हैं। यह लेख PowerCLI इंस्टॉल करने, vCenter से जुड़ने और इसकी सुविधाओं के प्रभावी उपयोग को बताता है।

______

## PowerCLI इंस्टॉल करना

अपने कंप्यूटर पर PowerCLI इंस्टॉल करने के लिए:

1. VMware की आधिकारिक वेबसाइट से PowerCLI इंस्टॉलर **डाउनलोड** करें। लिंक [PowerCLI दस्तावेज़](https://code.vmware.com/web/dp/tool/vmware-powercli) में है। अपने ऑपरेटिंग सिस्टम के लिए उपयुक्त संस्करण चुनें।
2. इंस्टॉलर **चलाएँ** और स्क्रीन पर दिए निर्देशों का पालन करें। इंस्टॉल स्थान और विकल्प चुनें।
3. स्थापना पूरी करने के लिए “Finish” चुनें। अब PowerCLI उपयोग के लिए तैयार है।

______

## PowerCLI से vCenter कनेक्ट करना

इंस्टॉलेशन के बाद vCenter Server से जुड़ें। इससे PowerCLI cmdlet के ज़रिए वर्चुअल इंफ़्रास्ट्रक्चर प्रबंधित होगा।

1. Start मेनू या डेस्कटॉप शॉर्टकट से PowerCLI खोलें।
2. इस कमांड से vCenter से कनेक्ट करें:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

`<vCenter IP or hostname>` की जगह अपने vCenter Server का वास्तविक IP पता या होस्टनाम दें।

3. संकेत मिलने पर vCenter प्रबंधन के पर्याप्त अधिकार वाले खाते के क्रेडेंशियल दें।
4. **Get-VMHost** जैसा सरल कमांड चलाकर कनेक्शन जाँचें। ESXi होस्ट की सूची दिखे तो कनेक्शन सफल है।

______

## vSphere प्रबंधन के लिए PowerCLI का उपयोग

vCenter से जुड़ने के बाद कई सामान्य कार्य किए जा सकते हैं।

### जानकारी प्राप्त करना

PowerCLI vSphere वातावरण की जानकारी पाने के लिए cmdlet देता है:

- **Get-VM**: वर्चुअल मशीनों की जानकारी प्राप्त करता है।
- **Get-VMHost**: ESXi होस्ट की जानकारी प्राप्त करता है।
- **Get-Datastore**: डेटास्टोर की जानकारी प्राप्त करता है।
- **Get-NetworkAdapter**: नेटवर्क अडैप्टर की जानकारी प्राप्त करता है।

परिणामों को फ़िल्टर और स्वरूपित करने के लिए पैरामीटर जोड़ें।

### कार्य स्वचालित करना

PowerCLI बार-बार होने वाले कार्यों को स्वचालित करता है। कुछ पंक्तियों से कई ऑब्जेक्ट पर जटिल कार्रवाई की जा सकती है।

#### फ़ोल्डर की सभी VM का स्नैपशॉट लेना

```PowerShell
## Power off all virtual machines on a specific host
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Take a snapshot of all virtual machines in a specific folder
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

यह स्क्रिप्ट किसी होस्ट की सभी VM बंद करने और चुने हुए फ़ोल्डर की VM के स्नैपशॉट बनाने का उदाहरण है।

#### फ़ोल्डर की सभी VM को सुरक्षित रूप से बंद करना

```PowerShell
## Retrieve the folder containing the virtual machines to be shutdown
$folder = Get-Folder -Name "MyFolder"

## Retrieve all virtual machines within the specified folder
$vms = Get-VM -Location $folder

## Shutdown all virtual machines gracefully
foreach ($vm in $vms) {
    if ($vm.PowerState -eq "PoweredOn") {
        $vm | Shutdown-VMGuest -Confirm:$false
    }
}
```

यह स्क्रिप्ट पहले `Get-Folder` से फ़ोल्डर और फिर `Get-VM` से उसमें मौजूद VM प्राप्त करती है। `foreach` हर VM जाँचता है। स्थिति “PoweredOn” होने पर `Shutdown-VMGuest` सामान्य शटडाउन करता है। `-Confirm:$false` पुष्टि संकेत को हटाता है। इस तरह फ़ोल्डर की VM क्रम से बंद होती हैं। PowerCLI स्क्रिप्टिंग से अपनी ज़रूरत के अनुरूप स्वचालन कार्यप्रवाह बनाएँ।

### वर्चुअल मशीन और होस्ट प्रबंधित करना

PowerCLI से कई प्रबंधन कार्य किए जा सकते हैं:

- **वर्चुअल मशीन बनाना और हटाना**: **`New-VM`** और **`Remove-VM`** जैसे cmdlet इस्तेमाल करें। **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** बनाते समय CPU, मेमोरी, डिस्क और नेटवर्क विकल्प स्वीकार करता है।
- **VM सेटिंग बदलना**: CPU, मेमोरी, डिस्क और नेटवर्क बदलें। **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** CPU और मेमोरी आवंटन बदल सकता है।
- **होस्ट संसाधन प्रबंधित करना**: CPU, मेमोरी, नेटवर्क और स्टोरेज नियंत्रित करें। **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** होस्ट की नेटवर्क और स्टोरेज सेटिंग बदल सकता है।

ये vSphere प्रबंधन के कुछ उदाहरण हैं। PowerCLI के व्यापक cmdlet संग्रह से प्रशासनिक कार्य स्वचालित और सरल होते हैं।

## निष्कर्ष

**PowerCLI** VMware vSphere वातावरण के प्रबंधन और स्वचालन का उपयोगी टूल है। इसके cmdlet प्रशासनिक कार्य सरल करते हैं और उत्पादकता बढ़ाते हैं। इंस्टॉल करके vCenter से जुड़ने के बाद जानकारी पाएँ, कार्य स्वचालित करें और VM तथा होस्ट कुशलता से प्रबंधित करें।

vSphere प्रबंधन सरल करने के लिए PowerCLI आज़माएँ।


## संदर्भ
- [PowerCLI दस्तावेज़](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: VMware PowerCLI cmdlet संदर्भ](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: VMware PowerCLI cmdlet संदर्भ](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)

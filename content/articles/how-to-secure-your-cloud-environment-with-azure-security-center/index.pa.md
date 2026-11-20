---
title: "Microsoft Defender for Cloud ਨਾਲ ਆਪਣਾ ਕਲਾਊਡ ਵਾਤਾਵਰਣ ਸੁਰੱਖਿਅਤ ਕਰੋ"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Microsoft Defender for Cloud ਨਾਲ Azure ਵਰਕਲੋਡ ਸੁਰੱਖਿਅਤ ਕਰੋ। Azure Security Center ਦੇ ਪੁਰਾਣੇ ਨਾਮਾਂ, ਸਿਫ਼ਾਰਸ਼ਾਂ, ਨੀਤੀਆਂ ਅਤੇ ਜਵਾਬੀ ਕਦਮਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।"
tags: ["Azure", "Security Center", "ਕਲਾਊਡ ਸੁਰੱਖਿਆ", "Azure Sentinel", "Azure Defender", "ਨੈੱਟਵਰਕ ਸੁਰੱਖਿਆ", "ਪਛਾਣ ਪ੍ਰਬੰਧਨ", "ਡਾਟਾ ਸੁਰੱਖਿਆ", "ਖ਼ਤਰਾ ਪਛਾਣ", "ਖ਼ਤਰੇ ਦਾ ਜਵਾਬ", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "ਬੱਦਲਾਂ ਦੇ ਚਿੰਨ੍ਹਾਂ ਨਾਲ ਘਿਰੀ ਢਾਲ ਸੁਰੱਖਿਅਤ ਕਲਾਊਡ ਵਾਤਾਵਰਣ ਦਰਸਾਉਂਦੀ ਹੈ। ਢਾਲ ਉੱਤੇ Azure Security Center ਦਾ ਲੋਗੋ ਹੈ।"
coverCaption: ""
---

**Azure Security Center ਨਾਲ ਕਲਾਊਡ ਵਾਤਾਵਰਣ ਕਿਵੇਂ ਸੁਰੱਖਿਅਤ ਕਰੀਏ**

ਸੰਸਥਾ ਦੇ ਡਾਟਾ, ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਨੂੰ ਖ਼ਤਰਿਆਂ ਤੋਂ ਬਚਾਉਣ ਲਈ ਕਲਾਊਡ ਵਾਤਾਵਰਣ ਦੀ ਸੁਰੱਖਿਆ ਜ਼ਰੂਰੀ ਹੈ। Microsoft ਦਾ **Azure Security Center** ਸੁਰੱਖਿਆ ਦੀ ਸਥਿਤੀ ਸੁਧਾਰਨ ਅਤੇ Azure ਵਾਤਾਵਰਣ ਵਿੱਚ ਸੰਭਾਵੀ ਖ਼ਤਰੇ ਜਲਦੀ ਪਛਾਣਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਇਹ ਲੇਖ Azure Security Center ਰਾਹੀਂ ਕਲਾਊਡ ਸੁਰੱਖਿਅਤ ਕਰਨ ਅਤੇ ਵੱਖ-ਵੱਖ ਸੁਰੱਖਿਆ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਾਗੂ ਕਰਨ ਦੇ ਚੰਗੇ ਤਰੀਕੇ ਦੱਸਦਾ ਹੈ। ਤਕਨੀਕੀ ਵੇਰਵੇ ਅਤੇ ਉਦਾਹਰਨਾਂ ਵੀ ਦਿੱਤੀਆਂ ਹਨ, ਤਾਂ ਜੋ ਤੁਸੀਂ ਇਹ ਕਦਮ ਆਪਣੇ ਵਾਤਾਵਰਣ ਵਿੱਚ ਲਾਗੂ ਕਰ ਸਕੋ।

*ਇਸ ਲੇਖ ਦੇ ਪਹਿਲੇ ਪ੍ਰਕਾਸ਼ਨ ਤੋਂ ਬਾਅਦ ਉਤਪਾਦਾਂ ਦੇ ਨਾਮ ਬਦਲੇ ਹਨ। Microsoft Azure Security Center ਹੁਣ Microsoft Defender for Cloud ਹੈ। Azure Active Directory ਹੁਣ Microsoft Entra ID ਹੈ। Azure Sentinel ਹੁਣ Microsoft Sentinel ਹੈ। Azure Defender, Defender ਯੋਜਨਾਵਾਂ ਅਤੇ Defender for Cloud ਵਿੱਚ ਵਰਕਲੋਡ ਸੁਰੱਖਿਆ ਲਈ ਵਰਤਿਆ ਨਾਮ ਹੈ। 2023 ਦੇ ਸੰਦਰਭ ਵਾਲੇ ਹਿੱਸਿਆਂ ਵਿੱਚ ਪੁਰਾਣੇ ਨਾਮ ਰੱਖੇ ਹਨ।*

ਮੌਜੂਦਾ [Defender for Cloud ਜਾਣ-ਪਛਾਣ](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) ਇਸਨੂੰ ਕਲਾਊਡ-ਨੇਟਿਵ ਐਪਲੀਕੇਸ਼ਨ ਸੁਰੱਖਿਆ ਪਲੇਟਫਾਰਮ ਦੱਸਦੀ ਹੈ। ਇਸ ਵਿੱਚ ਕਲਾਊਡ ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਪ੍ਰਬੰਧਨ, DevSecOps ਅਤੇ ਕਲਾਊਡ ਵਰਕਲੋਡ ਸੁਰੱਖਿਆ ਸ਼ਾਮਲ ਹਨ। ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਅਤੇ ਲਾਇਸੈਂਸ ਕਲਾਊਡ, ਸਰੋਤ ਦੀ ਕਿਸਮ, ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਅਤੇ ਯੋਜਨਾ ਉੱਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ।

______

## Azure Security Center ਨੂੰ ਸਮਝਣਾ

Azure Security Center **ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦੀ ਸੁਰੱਖਿਆ ਸੰਭਾਲਣ ਵਾਲਾ ਏਕੀਕ੍ਰਿਤ ਪ੍ਰਬੰਧਨ ਤੰਤਰ** ਹੈ। ਇਹ ਕਲਾਊਡ ਵਾਤਾਵਰਣ ਦੀਆਂ ਸੰਭਾਵੀ ਕਮਜ਼ੋਰੀਆਂ ਪਛਾਣ ਕੇ ਹੱਲ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਇਸ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਵਿੱਚ ਖ਼ਤਰਾ ਪਛਾਣ, ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਪ੍ਰਬੰਧਨ ਅਤੇ ਅਨੁਕੂਲਤਾ ਪ੍ਰਬੰਧਨ ਸ਼ਾਮਲ ਹਨ।

**ਲਗਾਤਾਰ ਸੁਰੱਖਿਆ ਮੁਲਾਂਕਣ** ਅਤੇ **ਉੱਨਤ ਖ਼ਤਰਾ ਸੁਰੱਖਿਆ** Azure Security Center ਦੀਆਂ ਦੋ ਮੁੱਖ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ। ਲਗਾਤਾਰ ਮੁਲਾਂਕਣ ਵਾਤਾਵਰਣ ਦੀਆਂ ਸੰਭਾਵੀ ਸੁਰੱਖਿਆ ਸਮੱਸਿਆਵਾਂ ਲੱਭਦਾ ਹੈ। ਉੱਨਤ ਖ਼ਤਰਾ ਸੁਰੱਖਿਆ ਸੰਭਾਵੀ ਖ਼ਤਰਿਆਂ ਦੀ ਪਛਾਣ ਅਤੇ ਜਵਾਬ ਦੇਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀ ਹੈ।

______

## ਸੁਰੱਖਿਆ ਨੀਤੀਆਂ ਅਤੇ ਅਨੁਕੂਲਤਾ ਮਿਆਰ ਲਾਗੂ ਕਰਨਾ

Azure Security Center ਰਾਹੀਂ ਕਲਾਊਡ ਵਾਤਾਵਰਣ ਵਿੱਚ ਸੁਰੱਖਿਆ ਨੀਤੀਆਂ ਲਾਗੂ ਅਤੇ ਪ੍ਰਬੰਧਿਤ ਕਰੋ। ਆਪਣੀਆਂ ਨੀਤੀਆਂ ਬਣਾਉਣ ਲਈ **Azure Policy** ਸੇਵਾ ਵਰਤੋ ਜਾਂ ਚੰਗੇ ਤਰੀਕੇ ਅਤੇ ਅਨੁਕੂਲਤਾ ਮਿਆਰ ਲਾਗੂ ਕਰਨ ਲਈ ਪਹਿਲਾਂ ਤੋਂ ਬਣੀਆਂ ਨੀਤੀਆਂ ਵਰਤੋ। [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) ਅਤੇ [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html) ਵਰਗੇ ਉਦਯੋਗ ਮਿਆਰਾਂ ਮੁਤਾਬਕ ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਦੀ ਜਾਂਚ ਵੀ ਕਰੋ।

Azure Security Center ਵਿੱਚ ਅਨੁਕੂਲਤਾ ਪ੍ਰਬੰਧਨ ਦੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸੰਸਥਾ ਦੀ ਨਿਯਮਕ ਢਾਂਚਿਆਂ ਨਾਲ ਅਨੁਕੂਲਤਾ ਦੀ ਸਥਿਤੀ ਦਿਖਾਉਂਦੀਆਂ ਹਨ। ਇਨ੍ਹਾਂ ਵਿੱਚ [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) ਅਤੇ [PCI DSS](https://www.pcisecuritystandards.org/) ਸ਼ਾਮਲ ਹਨ।

______

## Azure ਸਰੋਤ ਸੁਰੱਖਿਅਤ ਕਰਨਾ

ਕਲਾਊਡ ਸੁਰੱਖਿਆ ਦਾ ਮਹੱਤਵਪੂਰਨ ਹਿੱਸਾ **ਸਰੋਤਾਂ ਦੀ ਸੁਰੱਖਿਆ-ਸਿਹਤ ਕਾਇਮ ਰੱਖਣਾ** ਹੈ। Azure Security Center **Secure Score** ਰਾਹੀਂ ਸਰੋਤਾਂ ਦੀ ਸਮੁੱਚੀ ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਦਿਖਾਉਂਦਾ ਹੈ। ਇਸ ਦੀਆਂ ਸਿਫ਼ਾਰਸ਼ਾਂ ਲਾਗੂ ਕਰਕੇ ਸਕੋਰ ਸੁਧਾਰੋ।

### ਨੈੱਟਵਰਕ ਸੁਰੱਖਿਆ

**Network Security Groups (NSGs)**, **Azure Firewall** ਅਤੇ **Web Application Firewall (WAF)** ਵਰਗੇ ਉਪਾਅ Azure ਵਾਤਾਵਰਣ ਨੂੰ ਸੰਭਾਵੀ ਖ਼ਤਰਿਆਂ ਤੋਂ ਬਚਾਉਂਦੇ ਹਨ। ਇਹ ਆਉਣ-ਜਾਣ ਵਾਲੇ ਨੈੱਟਵਰਕ ਟ੍ਰੈਫਿਕ ਉੱਤੇ ਕਾਬੂ ਰੱਖਦੇ ਹਨ ਅਤੇ ਬਿਨਾਂ ਅਧਿਕਾਰ ਪਹੁੰਚ ਤੇ ਹਮਲਿਆਂ ਨੂੰ ਰੋਕਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ।

#### Network Security Groups (NSGs)

NSG Azure ਸਰੋਤਾਂ ਲਈ ਵਰਚੁਅਲ ਫਾਇਰਵਾਲ ਵਾਂਗ ਕੰਮ ਕਰਦਾ ਹੈ। ਇਸ ਵਿੱਚ ਸਰੋਤਾਂ ਤੱਕ ਆਉਣ ਜਾਂ ਉਨ੍ਹਾਂ ਤੋਂ ਜਾਣ ਵਾਲੇ ਨੈੱਟਵਰਕ ਟ੍ਰੈਫਿਕ ਨੂੰ ਮਨਜ਼ੂਰ ਜਾਂ ਰੱਦ ਕਰਨ ਵਾਲੇ ਨਿਯਮ ਬਣਾਏ ਜਾ ਸਕਦੇ ਹਨ। ਖ਼ਾਸ ਟ੍ਰੈਫਿਕ ਲਈ NSG ਬਣਾਉਣ ਦੀ ਉਦਾਹਰਨ:

```azurecli
# ਇੱਕ Network Security Group ਬਣਾਓ
az network nsg create --name MyNSG --resource-group MyResourceGroup

# ਟ੍ਰੈਫਿਕ ਦੀ ਮਨਜ਼ੂਰੀ ਜਾਂ ਰੋਕ ਲਈ ਨਿਯਮ ਜੋੜੋ
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
[Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview) ਬਾਰੇ Microsoft ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਹੋਰ ਪੜ੍ਹੋ।

ਉਪਰਲੀ ਉਦਾਹਰਨ ਹਰ IPv4 ਸਰੋਤ ਤੋਂ ਆਉਣ ਵਾਲੇ TCP ਪੋਰਟ 80 ਟ੍ਰੈਫਿਕ ਨੂੰ ਮਨਜ਼ੂਰ ਕਰਦੀ ਹੈ। ਉਤਪਾਦਨ ਵਾਤਾਵਰਣ ਵਿੱਚ ਪਛਾਣੀ ਹੋਈ ਸਰੋਤ ਰੇਂਜ, ਨਿੱਜੀ ਐਂਡਪੋਇੰਟ ਜਾਂ ਲੋਡ ਸੰਤੁਲਕ ਰਾਹ ਵਰਤੋ। ਉਦਾਹਰਨ ਵਰਤਣ ਤੋਂ ਪਹਿਲਾਂ ਮੌਜੂਦਾ [NSG ਸੁਰੱਖਿਆ ਜਾਣ-ਪਛਾਣ](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) ਪੜ੍ਹੋ।

#### Azure Firewall

Azure Firewall ਇੱਕ ਪ੍ਰਬੰਧਿਤ, ਕਲਾਊਡ-ਆਧਾਰਿਤ ਨੈੱਟਵਰਕ ਸੁਰੱਖਿਆ ਸੇਵਾ ਹੈ, ਜੋ Azure ਸਰੋਤਾਂ ਦੀ ਰੱਖਿਆ ਕਰਦੀ ਹੈ। ਇਸ ਵਿੱਚ ਖ਼ਤਰਾ-ਜਾਣਕਾਰੀ ਅਧਾਰਿਤ ਫਿਲਟਰਿੰਗ, ਵੈੱਬ ਸ਼੍ਰੇਣੀਆਂ ਅਤੇ ਕੇਂਦਰੀ ਲਾਗਿੰਗ ਤੇ ਵਿਸ਼ਲੇਸ਼ਣ ਵਰਗੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ। Azure Firewall ਸੈੱਟ ਕਰਨ ਲਈ Microsoft ਦੀ [ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ ਗਾਈਡ](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep) ਵਰਤੋ।

#### Web Application Firewall (WAF)

Web Application Firewall (WAF), **Azure Application Gateway** ਦੀ ਵਿਸ਼ੇਸ਼ਤਾ ਹੈ। ਇਹ SQL ਪੁੱਛਗਿੱਛ ਰਾਹੀਂ ਦਖ਼ਲ ਦਾ ਹਮਲਾ, ਕਰਾਸ-ਸਾਈਟ ਸਕ੍ਰਿਪਟਿੰਗ ਹਮਲਾ ਅਤੇ ਹੋਰ ਆਮ ਵੈੱਬ ਹਮਲਿਆਂ ਤੋਂ ਵੈੱਬ ਐਪਲੀਕੇਸ਼ਨਾਂ ਦੀ ਰੱਖਿਆ ਕਰਦੀ ਹੈ। ਮੌਜੂਦਾ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ WAF ਜੋੜੋ ਅਤੇ ਖ਼ਾਸ ਹਮਲਾ ਤਰੀਕਿਆਂ ਨੂੰ ਰੋਕਣ ਲਈ ਆਪਣੇ ਨਿਯਮ ਬਣਾਓ।

WAF ਚਾਲੂ ਰੱਖ ਕੇ Application Gateway ਬਣਾਉਣ ਦੀ ਉਦਾਹਰਨ:

```azurecli
# ਇੱਕ WAF ਨੀਤੀ ਬਣਾਓ
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# ਵਰਚੁਅਲ ਨੈੱਟਵਰਕ ਅਤੇ ਸਬਨੈੱਟ ਬਣਾਓ
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# ਇੱਕ public IP ਪਤਾ ਬਣਾਓ
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# WAF ਚਾਲੂ ਕਰਕੇ Application Gateway ਬਣਾਓ
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
[Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview) ਬਾਰੇ Microsoft ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਹੋਰ ਪੜ੍ਹੋ।

### ਪਛਾਣ ਅਤੇ ਪਹੁੰਚ ਪ੍ਰਬੰਧਨ

**Microsoft Entra ID, ਜਿਸਦਾ ਪੁਰਾਣਾ ਨਾਮ Azure Active Directory (Azure AD) ਸੀ,** ਕਲਾਊਡ ਸੁਰੱਖਿਆ ਦਾ ਜ਼ਰੂਰੀ ਹਿੱਸਾ ਹੈ। Defender for Cloud ਪਛਾਣ ਅਤੇ ਪਹੁੰਚ ਪ੍ਰਬੰਧਨ ਸੁਧਾਰਨ ਲਈ ਸਿਫ਼ਾਰਸ਼ਾਂ ਦਿੰਦਾ ਹੈ। ਇਨ੍ਹਾਂ ਵਿੱਚ **Multi-Factor Authentication (MFA)** ਚਾਲੂ ਕਰਨਾ, **Role-Based Access Control (RBAC)** ਲਾਗੂ ਕਰਨਾ ਅਤੇ ਸ਼ੱਕੀ ਗਤੀਵਿਧੀ ਦੀ ਨਿਗਰਾਨੀ ਸ਼ਾਮਲ ਹੈ।

#### Multi-Factor Authentication (MFA)

MFA ਪਹੁੰਚ ਦੇਣ ਤੋਂ ਪਹਿਲਾਂ ਵਰਤੋਂਕਾਰ ਤੋਂ ਦੋ ਜਾਂ ਵੱਧ ਤਰੀਕਿਆਂ ਨਾਲ ਪਛਾਣ ਦੀ ਪੁਸ਼ਟੀ ਮੰਗਦਾ ਹੈ। ਇਹ Azure AD ਖਾਤਿਆਂ ਲਈ ਇੱਕ ਵਾਧੂ ਸੁਰੱਖਿਆ ਪਰਤ ਹੈ। ਸੰਸਥਾ ਲਈ MFA ਚਾਲੂ ਕਰਨ ਵਾਸਤੇ Microsoft ਦੀ [ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) ਵਰਤੋ।

ਉਦਾਹਰਨ: ਕਿਸੇ ਵਰਤੋਂਕਾਰ ਲਈ MFA ਚਾਲੂ ਕਰਨਾ

```powershell
# Azure AD ਨਾਲ ਜੁੜੋ
Connect-AzureAD

# ਕਿਸੇ ਖ਼ਾਸ ਵਰਤੋਂਕਾਰ ਲਈ MFA ਚਾਲੂ ਕਰੋ
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

RBAC Azure ਸਰੋਤਾਂ ਲਈ ਬਾਰੀਕੀ ਨਾਲ ਅਨੁਮਤੀਆਂ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ, ਤਾਂ ਜੋ ਹਰ ਵਰਤੋਂਕਾਰ ਨੂੰ ਢੁੱਕਵੀਂ ਪਹੁੰਚ ਮਿਲੇ। ਸੰਸਥਾ ਦੇ ਸਰੋਤਾਂ ਦੀ ਪਹੁੰਚ ਸੰਭਾਲਣ ਲਈ ਵਰਤੋਂਕਾਰਾਂ, ਸਮੂਹਾਂ ਜਾਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਭੂਮਿਕਾਵਾਂ ਦਿਓ। RBAC ਲਾਗੂ ਕਰਨ ਲਈ Microsoft ਦੀ [ਅਧਿਕਾਰਕ ਗਾਈਡ](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) ਪੜ੍ਹੋ।

ਉਦਾਹਰਨ: ਵਰਤੋਂਕਾਰ ਨੂੰ ਭੂਮਿਕਾ ਦੇਣਾ

```azurecli
# ਵਰਤੋਂਕਾਰ ਨੂੰ Reader ਭੂਮਿਕਾ ਦਿਓ
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### ਸ਼ੱਕੀ ਗਤੀਵਿਧੀ ਦੀ ਨਿਗਰਾਨੀ

Azure AD ਦੀਆਂ **Identity Protection** ਅਤੇ **Conditional Access** ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਸ਼ੱਕੀ ਗਤੀਵਿਧੀ ਦੀ ਨਿਗਰਾਨੀ ਅਤੇ ਜਵਾਬ ਦੇਣ ਵਿੱਚ ਮਦਦ ਕਰਦੀਆਂ ਹਨ। Identity Protection ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਰਾਹੀਂ ਅਸਧਾਰਨਤਾਵਾਂ ਅਤੇ ਜੋਖ਼ਮ ਵਾਲੇ ਸਾਈਨ-ਇਨ ਪਛਾਣਦੀ ਹੈ। Conditional Access ਡਿਵਾਈਸ, ਥਾਂ ਅਤੇ ਜੋਖ਼ਮ ਮੁਤਾਬਕ ਪਹੁੰਚ ਕੰਟਰੋਲ ਕਰਨ ਵਾਲੀਆਂ ਨੀਤੀਆਂ ਬਣਾਉਣ ਦਿੰਦਾ ਹੈ।

Azure AD Identity Protection ਸੈੱਟ ਕਰਨ ਲਈ Microsoft ਦੀ [ਅਧਿਕਾਰਕ ਗਾਈਡ](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) ਪੜ੍ਹੋ।

ਉਦਾਹਰਨ: Conditional Access ਨੀਤੀ ਬਣਾਉਣਾ

```powershell
# Azure AD ਨਾਲ ਜੁੜੋ
Connect-AzureAD

# Conditional Access ਨੀਤੀ ਬਣਾਓ
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "ਅਣਜਾਣ ਥਾਵਾਂ ਤੋਂ ਵਰਤੋਂਕਾਰਾਂ ਦੇ ਸਾਈਨ-ਇਨ ਰੋਕੋ।"
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
[Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) ਅਤੇ [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview) ਬਾਰੇ Microsoft ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਹੋਰ ਪੜ੍ਹੋ।

### ਡਾਟਾ ਸੁਰੱਖਿਆ

ਕਲਾਊਡ ਵਿੱਚ ਡਾਟਾ ਸੁਰੱਖਿਅਤ ਰੱਖਣਾ ਜ਼ਰੂਰੀ ਹੈ। Azure Security Center ਵਿੱਚ **Azure Information Protection**, **Azure Storage Service Encryption** ਅਤੇ **Azure Disk Encryption** ਵਰਗੀਆਂ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਹਨ। ਇਹ ਡਾਟਾ ਇਨਕ੍ਰਿਪਟ ਕਰਨ ਅਤੇ ਪਹੁੰਚ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦੀਆਂ ਹਨ, ਤਾਂ ਜੋ ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਸੁਰੱਖਿਅਤ ਰਹੇ।

#### Azure Information Protection

**Azure Information Protection (AIP)** ਕਲਾਊਡ-ਆਧਾਰਿਤ ਸੇਵਾ ਹੈ, ਜੋ ਸੰਵੇਦਨਸ਼ੀਲ ਦਸਤਾਵੇਜ਼ਾਂ ਅਤੇ ਈਮੇਲਾਂ ਨੂੰ ਵਰਗੀਕ੍ਰਿਤ, ਲੇਬਲ ਅਤੇ ਸੁਰੱਖਿਅਤ ਕਰਦੀ ਹੈ। AIP ਵਿੱਚ "ਗੁਪਤ" ਅਤੇ "ਨਿੱਜੀ" ਵਰਗੇ ਪਹਿਲਾਂ ਤੋਂ ਬਣੇ ਲੇਬਲ ਹਨ, ਜਿਨ੍ਹਾਂ ਨੂੰ ਸੰਸਥਾ ਦੀਆਂ ਲੋੜਾਂ ਮੁਤਾਬਕ ਬਦਲਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਪਹਿਲਾਂ ਨਿਰਧਾਰਤ ਨਿਯਮਾਂ ਅਨੁਸਾਰ ਲੇਬਲ ਆਪਣੇ ਆਪ ਲਗਾਉਣ ਲਈ ਵੀ AIP ਸੰਰਚਿਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ। ਸ਼ੁਰੂ ਕਰਨ ਲਈ Microsoft ਦੀ [ਅਧਿਕਾਰਕ ਗਾਈਡ](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection) ਵਰਤੋ।

ਉਦਾਹਰਨ: ਆਪਣਾ ਲੇਬਲ ਬਣਾਉਣਾ

```powershell
# AIP ਸੇਵਾ ਨਾਲ ਜੁੜੋ
Connect-AipService

# ਸੁਰੱਖਿਆ ਸੈਟਿੰਗਾਂ ਵਾਲਾ ਆਪਣਾ ਲੇਬਲ ਬਣਾਓ
$LabelName = "ਸੰਵੇਦਨਸ਼ੀਲ - ਸਿਰਫ਼ ਅੰਦਰੂਨੀ ਵਰਤੋਂ ਲਈ"
$LabelDescription = "ਇਹ ਲੇਬਲ ਸਿਰਫ਼ ਅੰਦਰੂਨੀ ਵਰਤੋਂ ਲਈ ਇਨਕ੍ਰਿਪਸ਼ਨ ਅਤੇ ਪਹੁੰਚ ਨੀਤੀ ਲਾਗੂ ਕਰਦਾ ਹੈ।"
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** Azure Storage ਖਾਤਿਆਂ ਵਿੱਚ ਰੱਖਿਆ ਡਾਟਾ ਆਪਣੇ ਆਪ ਇਨਕ੍ਰਿਪਟ ਕਰਦੀ ਹੈ। ਇਸ ਵਿੱਚ Blob, File, Table ਅਤੇ Queue ਸਟੋਰੇਜ ਸ਼ਾਮਲ ਹਨ। SSE ਸਟੋਰੇਜ ਖਾਤੇ ਦੇ ਪੱਧਰ ਉੱਤੇ ਇਨਕ੍ਰਿਪਸ਼ਨ ਲਈ Azure-ਪ੍ਰਬੰਧਿਤ ਜਾਂ ਗਾਹਕ-ਪ੍ਰਬੰਧਿਤ ਕੁੰਜੀਆਂ ਵਰਤਦੀ ਹੈ। SSE ਚਾਲੂ ਕਰਨ ਲਈ Microsoft ਦੀ [ਕਦਮ-ਦਰ-ਕਦਮ ਗਾਈਡ](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) ਪੜ੍ਹੋ।

Azure Information Protection ਇੱਕ ਪੁਰਾਣਾ ਉਤਪਾਦ ਨਾਮ ਹੈ। Microsoft ਦੇ ਮੌਜੂਦਾ Sentinel ਵਿਸ਼ੇਸ਼ਤਾ-ਉਪਲਬਧਤਾ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਇਸਨੂੰ ਬੰਦ ਹੋ ਚੁੱਕੀ ਸੇਵਾ ਦੱਸਿਆ ਗਿਆ ਹੈ। ਨਵੀਂ ਲੇਬਲਿੰਗ ਤਾਇਨਾਤੀ ਤੋਂ ਪਹਿਲਾਂ Microsoft Purview Information Protection ਦੇ ਮੌਜੂਦਾ ਦਸਤਾਵੇਜ਼ ਪੜ੍ਹੋ।

ਉਦਾਹਰਨ: ਸਟੋਰੇਜ ਖਾਤੇ ਲਈ SSE ਚਾਲੂ ਕਰਨਾ

```azurecli
# Azure-ਪ੍ਰਬੰਧਿਤ ਕੁੰਜੀਆਂ ਨਾਲ SSE ਚਾਲੂ ਕਰੋ
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਦੀਆਂ ਡਿਸਕਾਂ ਨੂੰ BitLocker (Windows) ਜਾਂ dm-crypt (Linux) ਨਾਲ ਇਨਕ੍ਰਿਪਟ ਕਰਕੇ ਸੁਰੱਖਿਅਤ ਕਰਦਾ ਹੈ। ਇਨਕ੍ਰਿਪਸ਼ਨ ਕੁੰਜੀਆਂ ਅਤੇ ਰਾਜ਼ Azure Key Vault ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਰਹਿੰਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਸਟੋਰੇਜ ਵਿੱਚ ਪਿਆ ਡਾਟਾ ਇਨਕ੍ਰਿਪਟ ਹੁੰਦਾ ਹੈ। Azure Disk Encryption ਚਾਲੂ ਕਰਨ ਲਈ Microsoft ਦੀ [ਅਧਿਕਾਰਕ ਗਾਈਡ](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) ਪੜ੍ਹੋ।

ਉਦਾਹਰਨ: ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਲਈ Azure Disk Encryption ਚਾਲੂ ਕਰਨਾ

```azurecli
# Windows VM ਲਈ Azure Disk Encryption ਚਾਲੂ ਕਰੋ
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
[Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) ਅਤੇ [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) ਬਾਰੇ Microsoft ਦੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਪੜ੍ਹੋ।
______

## ਖ਼ਤਰੇ ਪਛਾਣਨਾ ਅਤੇ ਜਵਾਬ ਦੇਣਾ

Azure Security Center ਉੱਨਤ ਖ਼ਤਰਾ-ਪਛਾਣ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਰਾਹੀਂ ਸੰਭਾਵੀ ਖ਼ਤਰੇ ਲੱਭਦਾ ਅਤੇ ਚੇਤਾਵਨੀ ਦਿੰਦਾ ਹੈ। **Azure Sentinel** ਨਾਲ ਜੋੜ ਕੇ ਪੂਰੇ ਵਾਤਾਵਰਣ ਦੀਆਂ ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ ਦੀ ਨਿਗਰਾਨੀ, ਜਾਂਚ ਅਤੇ ਜਵਾਬ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

### ਖ਼ਤਰਾ ਪਛਾਣ

ਸੰਭਾਵੀ ਸੁਰੱਖਿਆ ਖ਼ਤਰੇ ਪਛਾਣਨ ਲਈ Azure Security Center **Azure Defender** ਵਰਤਦਾ ਹੈ। Azure Defender ਸਰੋਤਾਂ ਵਿੱਚ ਘੁਸਪੈਠ ਦੇ ਸੰਕੇਤਾਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰਦਾ ਅਤੇ ਜਵਾਬ ਲਈ ਚੇਤਾਵਨੀਆਂ ਤੇ ਸਿਫ਼ਾਰਸ਼ਾਂ ਦਿੰਦਾ ਹੈ। Azure Defender ਚਾਲੂ ਕਰਨ ਲਈ Microsoft ਦੀ [ਅਧਿਕਾਰਕ ਗਾਈਡ](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable) ਪੜ੍ਹੋ।

ਉਦਾਹਰਨ: ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਲਈ Azure Defender ਚਾਲੂ ਕਰਨਾ

```azurecli
# ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਲਈ Azure Defender ਚਾਲੂ ਕਰੋ
az security auto-provisioning-setting update --name default --auto-provision on
```
### ਖ਼ਤਰੇ ਦਾ ਜਵਾਬ

ਖ਼ਤਰਾ ਪਛਾਣੇ ਜਾਣ ਉੱਤੇ ਤੁਰੰਤ ਅਤੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਜਵਾਬ ਦਿਓ। Azure Security Center ਦਾ **Security Incident** ਪ੍ਰਬੰਧਨ ਸੁਰੱਖਿਆ ਘਟਨਾਵਾਂ ਦੀ ਜਾਂਚ ਅਤੇ ਜਵਾਬ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ। ਘਟਨਾਵਾਂ ਲਈ ਸਵੈਚਾਲਿਤ ਜਵਾਬੀ ਕਾਰਜ-ਕ੍ਰਮ ਬਣਾਉਣ ਅਤੇ ਜਵਾਬ ਦਾ ਤਾਲਮੇਲ ਕਰਨ ਲਈ **Azure Sentinel** ਨਾਲ ਜੋੜੋ। Azure Security Center ਨੂੰ Azure Sentinel ਨਾਲ ਜੋੜਨ ਬਾਰੇ **ਅਧਿਕਾਰਕ ਦਸਤਾਵੇਜ਼** ਵੇਖੋ।

ਉਦਾਹਰਨ: Azure Sentinel ਲਈ Logic ਐਪ ਲਈ ਜਵਾਬੀ ਕਾਰਜ-ਕ੍ਰਮ ਬਣਾਉਣਾ

```azurecli
# ਇੱਕ ਸਰੋਤ ਸਮੂਹ ਬਣਾਓ
az group create --name MyResourceGroup --location EastUS

# ਇੱਕ Logic App ਬਣਾਓ
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
`playbook-definition.json` ਫਾਈਲ ਵਿੱਚ Logic ਐਪ ਲਈ ਜਵਾਬੀ ਕਾਰਜ-ਕ੍ਰਮ ਦੀ ਪਰਿਭਾਸ਼ਾ ਹੋਣੀ ਚਾਹੀਦੀ ਹੈ। Azure Sentinel ਜਵਾਬੀ ਕਾਰਜ-ਕ੍ਰਮ ਦੀਆਂ ਉਦਾਹਰਨਾਂ [Azure-Sentinel GitHub ਰਿਪੋਜ਼ਟਰੀ](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks) ਵਿੱਚ ਵੇਖੋ।

Azure Security Center ਦੀ ਖ਼ਤਰਾ-ਪਛਾਣ ਨੂੰ Azure Sentinel ਨਾਲ ਜੋੜ ਕੇ Azure ਵਾਤਾਵਰਣ ਵਿੱਚ ਖ਼ਤਰੇ ਪਛਾਣਨ ਅਤੇ ਜਵਾਬ ਦੇਣ ਦੀ ਸੁਰੱਖਿਆ ਯੋਜਨਾ ਬਣਾਓ। [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) ਅਤੇ [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview) ਦੇ ਵੇਰਵੇ ਅਧਿਕਾਰਕ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿੱਚ ਵੇਖੋ।

ਮੌਜੂਦਾ ਜੋੜ-ਪ੍ਰਕਿਰਿਆ [Defender for ਕਲਾਊਡ ਜੋੜ](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud) ਰਾਹੀਂ Defender for Cloud ਦੀਆਂ ਚੇਤਾਵਨੀਆਂ Microsoft Sentinel ਨੂੰ ਭੇਜਦੀ ਹੈ। ਸਵੈਚਾਲਨ ਉੱਤੇ ਭਰੋਸਾ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ Defender ਪੋਰਟਲ ਜਾਂ Azure ਪੋਰਟਲ ਵਿੱਚ ਜੋੜ, data ਇਕੱਤਰ ਕਰਨ ਦੇ ਨਿਯਮ, ਵਿਸ਼ਲੇਸ਼ਣ ਨਿਯਮ ਅਤੇ ਘਟਨਾ ਜਵਾਬੀ ਕਾਰਜ-ਕ੍ਰਮ ਦੀ ਜਾਂਚ ਕਰੋ।
______

## ਨਿਗਰਾਨੀ ਅਤੇ ਰਿਪੋਰਟਿੰਗ

ਸੁਰੱਖਿਅਤ ਕਲਾਊਡ ਵਾਤਾਵਰਣ ਕਾਇਮ ਰੱਖਣ ਲਈ ਨਿਗਰਾਨੀ ਅਤੇ ਰਿਪੋਰਟਿੰਗ ਲਾਜ਼ਮੀ ਹਨ। Azure Security Center **Security Dashboard**, **Security Alerts** ਅਤੇ **Compliance Reports** ਵਰਗੇ ਸਾਧਨ ਦਿੰਦਾ ਹੈ।

### ਸੁਰੱਖਿਆ ਡੈਸ਼ਬੋਰਡ

Azure Security Center ਦਾ Security Dashboard ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਦਾ ਪੂਰਾ ਜਾਇਜ਼ਾ ਦਿੰਦਾ ਹੈ। ਇਸ ਵਿੱਚ Secure Score, ਸੁਰੱਖਿਆ ਸਿਫ਼ਾਰਸ਼ਾਂ ਅਤੇ ਸਰਗਰਮ ਸੁਰੱਖਿਆ ਚੇਤਾਵਨੀਆਂ ਦਿਖਾਈਆਂ ਜਾਂਦੀਆਂ ਹਨ। ਡੈਸ਼ਬੋਰਡ ਅਨੁਕੂਲਤਾ ਦੀ ਸਥਿਤੀ ਵੀ ਦਿਖਾਉਂਦਾ ਹੈ ਅਤੇ ਸਮੇਂ ਨਾਲ ਤਰੱਕੀ ਦੀ ਨਿਗਰਾਨੀ ਕਰਨ ਦਿੰਦਾ ਹੈ।

### ਸੁਰੱਖਿਆ ਚੇਤਾਵਨੀਆਂ

ਸੰਭਾਵੀ ਖ਼ਤਰੇ ਪਛਾਣੇ ਜਾਣ ਉੱਤੇ Azure Security Center ਸੁਰੱਖਿਆ ਚੇਤਾਵਨੀਆਂ ਬਣਾਉਂਦਾ ਹੈ। ਇਨ੍ਹਾਂ ਵਿੱਚ ਖ਼ਤਰੇ ਦੇ ਵੇਰਵੇ ਅਤੇ ਜੋਖ਼ਮ ਘਟਾਉਣ ਦੀਆਂ ਸਿਫ਼ਾਰਸ਼ਾਂ ਹੁੰਦੀਆਂ ਹਨ। Azure Security Center ਰਾਹੀਂ ਈਮੇਲ ਜਾਂ SMS ਸੂਚਨਾਵਾਂ ਭੇਜੋ, ਜਾਂ [Slack](https://slack.com/) ਅਤੇ [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) ਵਰਗੇ ਤੀਜੀ-ਧਿਰ ਸਾਧਨਾਂ ਨਾਲ ਜੋੜੋ।

### ਅਨੁਕੂਲਤਾ ਰਿਪੋਰਟਾਂ

Azure Security Center GDPR, HIPAA ਅਤੇ PCI DSS ਵਰਗੇ ਨਿਯਮਕ ਢਾਂਚਿਆਂ ਲਈ ਅਨੁਕੂਲਤਾ ਰਿਪੋਰਟਾਂ ਬਣਾਉਂਦਾ ਹੈ। ਇਨ੍ਹਾਂ ਰਿਪੋਰਟਾਂ ਰਾਹੀਂ ਸੰਸਥਾ ਦੀ ਅਨੁਕੂਲਤਾ ਸਥਿਤੀ ਵੇਖੋ ਅਤੇ ਸੁਧਾਰ ਦੀ ਲੋੜ ਵਾਲੇ ਖੇਤਰ ਪਛਾਣੋ।

______

## Azure Security Center ਲਈ ਚੰਗੇ ਤਰੀਕੇ

Azure Security Center ਤੋਂ ਲਾਭ ਲੈਣ ਲਈ ਇਹ ਚੰਗੇ ਤਰੀਕੇ ਲਾਗੂ ਕਰੋ:

1. **ਸਾਰੀਆਂ ਸਬਸਕ੍ਰਿਪਸ਼ਨਾਂ ਉੱਤੇ Azure Security Center ਚਾਲੂ ਕਰੋ**: ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਹਰ Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨ ਸੁਰੱਖਿਅਤ ਹੈ।
2. **Secure Score ਦੀ ਨਿਯਮਿਤ ਸਮੀਖਿਆ ਕਰੋ**: ਸਮੁੱਚੀ ਸੁਰੱਖਿਆ ਸਥਿਤੀ ਸਮਝੋ ਅਤੇ ਸੁਧਾਰ ਵਾਲੇ ਖੇਤਰ ਲੱਭੋ।
3. **ਸੁਰੱਖਿਆ ਸਿਫ਼ਾਰਸ਼ਾਂ ਲਾਗੂ ਕਰੋ**: Azure Security Center ਦੀਆਂ ਸਿਫ਼ਾਰਸ਼ਾਂ ਮੰਨ ਕੇ ਸੁਰੱਖਿਆ ਸੁਧਾਰੋ ਅਤੇ ਸੰਭਾਵੀ ਜੋਖ਼ਮ ਘਟਾਓ।
4. **ਸੁਰੱਖਿਆ ਚੇਤਾਵਨੀਆਂ ਦੀ ਨਿਗਰਾਨੀ ਕਰੋ**: ਸੰਭਾਵੀ ਖ਼ਤਰੇ ਘਟਾਉਣ ਲਈ ਚੇਤਾਵਨੀਆਂ ਦੀ ਸਮੀਖਿਆ ਕਰਕੇ ਜਵਾਬ ਦਿਓ।
5. **ਅਨੁਕੂਲਤਾ ਦੀਆਂ ਲੋੜਾਂ ਨਵੀਆਂ ਰੱਖੋ**: ਨੀਤੀਆਂ ਦੀ ਨਿਯਮਿਤ ਸਮੀਖਿਆ ਅਤੇ ਸੋਧ ਕਰਕੇ ਨਵੇਂ ਨਿਯਮਕ ਢਾਂਚਿਆਂ ਦੀ ਪਾਲਣਾ ਕਰੋ।

## Defender for Cloud ਦਾ ਮੌਜੂਦਾ ਕਾਰਜ-ਕ੍ਰਮ

ਮੌਜੂਦਾ ਤਾਇਨਾਤੀ ਲਈ ਹੇਠਲਾ ਕ੍ਰਮ ਵਰਤੋ। ਪੁਰਾਣੇ ਹਿੱਸਿਆਂ ਦੇ ਨਾਮ ਇਤਿਹਾਸਕ ਖੋਜ ਵਿੱਚ ਕੰਮ ਆਉਂਦੇ ਹਨ, ਪਰ portal ਅਤੇ ਦਸਤਾਵੇਜ਼ Defender for Cloud ਦੀ ਸ਼ਬਦਾਵਲੀ ਵਰਤਦੇ ਹਨ।

1. **ਸਬਸਕ੍ਰਿਪਸ਼ਨਾਂ ਅਤੇ ਜੋੜਾਂ ਦੀ ਸੂਚੀ ਬਣਾਓ।** Azure ਸਬਸਕ੍ਰਿਪਸ਼ਨਾਂ, AWS ਜਾਂ GCP ਜੋੜਾਂ, DevOps ਪ੍ਰੋਜੈਕਟਾਂ ਅਤੇ ਅਹਿਮ ਸਰੋਤਾਂ ਦਾ ਰਿਕਾਰਡ ਬਣਾਓ।
2. **ਲੋੜੀਂਦੀਆਂ Defender ਯੋਜਨਾਵਾਂ ਚਾਲੂ ਕਰੋ।** ਵਰਕਲੋਡ ਮੁਤਾਬਕ ਯੋਜਨਾਵਾਂ ਚੁਣੋ ਅਤੇ ਉਤਪਾਦਨ ਸਬਸਕ੍ਰਿਪਸ਼ਨਾਂ ਉੱਤੇ ਚਾਲੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਲਾਇਸੈਂਸ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।
3. **Cloud Secure Score ਅਤੇ ਸਿਫ਼ਾਰਸ਼ਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।** ਇੰਟਰਨੈੱਟ ਅੱਗੇ ਖੁੱਲ੍ਹੇ ਸਰੋਤ, ਪਛਾਣ ਜੋਖ਼ਮ, ਵਰਤੀਆਂ ਜਾ ਸਕਣ ਵਾਲੀਆਂ ਕਮਜ਼ੋਰੀਆਂ ਅਤੇ ਗੁੰਮ ਲਾਗਿੰਗ ਨੂੰ ਪਹਿਲ ਦਿਓ। ਸਕੋਰ ਨੂੰ ਪੂਰੀ ਅਨੁਕੂਲਤਾ ਦਾ ਸਬੂਤ ਨਾ ਮੰਨੋ।
4. **Microsoft Entra ਕੰਟਰੋਲ ਸੰਰਚਿਤ ਕਰੋ।** ਅਹਿਮ ਖਾਤਿਆਂ ਲਈ ਫਿਸ਼ਿੰਗ-ਰੋਧੀ MFA ਲਾਜ਼ਮੀ ਕਰੋ, ਘੱਟੋ-ਘੱਟ ਅਧਿਕਾਰ ਵਾਲਾ RBAC ਵਰਤੋ ਅਤੇ ਵਿਸ਼ੇਸ਼ ਅਧਿਕਾਰਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।
5. **Microsoft Sentinel ਨੂੰ ਚੇਤਾਵਨੀਆਂ ਭੇਜੋ।** ਚੇਤਾਵਨੀਆਂ ਦੀ ਪ੍ਰਾਪਤੀ, ਵਿਸ਼ਲੇਸ਼ਣ ਨਿਯਮ, ਮਾਲਕੀ, ਜਵਾਬੀ ਸਵੈਚਾਲਨ ਅਤੇ ਸੰਭਾਲ ਮਿਆਦ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।
6. **ਬਦਲਾਅ ਮਗਰੋਂ ਮੁੜ ਜਾਂਚੋ।** ਪੈਚ ਲਗਾਉਣ, ਆਰਕੀਟੈਕਚਰ ਬਦਲਣ, ਨਵੇਂ ਜੋੜ ਬਣਾਉਣ ਜਾਂ ਯੋਜਨਾ ਬਦਲਣ ਮਗਰੋਂ ਸਿਫ਼ਾਰਸ਼ਾਂ ਵੇਖੋ।

## ਵਰਤੋਂਯੋਗ ਸਮੀਖਿਆ ਸੂਚੀ

- **ਪਛਾਣ:** ਪੁਰਾਣੇ ਖਾਤੇ ਹਟਾਓ, ਸਥਾਈ ਪ੍ਰਸ਼ਾਸਕ ਪਹੁੰਚ ਘਟਾਓ ਅਤੇ Conditional Access ਛੋਟਾਂ ਦੀ ਸਮੀਖਿਆ ਕਰੋ।
- **ਨੈੱਟਵਰਕ:** ਜਨਤਕ ਪ੍ਰਬੰਧਨ ਪੋਰਟ ਹਟਾਓ, NSG ਸਰੋਤ ਰੇਂਜ ਸੀਮਤ ਕਰੋ ਅਤੇ ਫਾਇਰਵਾਲ ਤੇ WAF ਲਾਗ ਨਿਗਰਾਨੀ workspace ਤੱਕ ਪਹੁੰਚਣ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।
- **ਡਾਟਾ:** ਸੰਵੇਦਨਸ਼ੀਲ ਸਟੋਰਾਂ ਦਾ ਵਰਗੀਕਰਨ ਕਰੋ, ਇਨਕ੍ਰਿਪਸ਼ਨ ਅਤੇ ਕੁੰਜੀ ਮਾਲਕੀ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ ਅਤੇ ਬੈਕਅੱਪ ਮੁੜ-ਬਹਾਲੀ ਦੀ ਜਾਂਚ ਕਰੋ।
- **ਪਛਾਣ:** ਚੇਤਾਵਨੀ ਦੀ ਗੰਭੀਰਤਾ, ਸੂਚਨਾ ਮਾਰਗ, ਘਟਨਾ ਮਾਲਕੀ ਅਤੇ ਜਵਾਬੀ ਜਵਾਬੀ ਕਾਰਜ-ਕ੍ਰਮ ਦੀ ਪੁਸ਼ਟੀ ਕਰੋ।
- **ਪ੍ਰਬੰਧਨ:** ਹਰ ਨੀਤੀ ਯੋਜਨਾ ਲਈ ਮਾਲਕ, ਛੋਟ ਦੀ ਮਿਆਦ-ਪੂਰੀ ਤਾਰੀਖ ਅਤੇ ਲੋੜੀਂਦੇ ਢਾਂਚੇ ਦੇ ਸਬੂਤ ਨਿਰਧਾਰਤ ਕਰੋ।

______

## ਹਵਾਲੇ

- [Azure Security Center ਦਸਤਾਵੇਜ਼](https://docs.microsoft.com/en-us/azure/security-center/)
- [Azure Policy ਸੇਵਾ](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)

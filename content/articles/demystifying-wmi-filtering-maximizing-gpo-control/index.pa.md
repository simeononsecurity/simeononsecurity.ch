---
title: "WMI ਫਿਲਟਰਿੰਗ ਨੂੰ ਸਮਝਣਾ"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "ਜਾਣੋ ਕਿ WMI ਫਿਲਟਰਿੰਗ ਨਾਲ Group Policy Object (GPO) ਨੂੰ ਚੁਣੇ ਹੋਏ ਕੰਪਿਊਟਰਾਂ ਤੱਕ ਕਿਵੇਂ ਸੀਮਿਤ ਕਰੀਏ। ਇਸ ਵਿੱਚ ਅਮਲੀ ਉਦਾਹਰਨਾਂ ਅਤੇ ਚੰਗੇ ਤਰੀਕੇ ਹਨ।"
genre: ["Windows ਪ੍ਰਬੰਧਨ", "Group Policy", "ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ", "ਨੈੱਟਵਰਕ ਪ੍ਰਬੰਧਨ", "IT ਢਾਂਚਾ", "ਨੀਤੀ ਪ੍ਰਬੰਧਨ", "IT ਸ਼ਾਸਨ", "IT ਆਟੋਮੇਸ਼ਨ", "Active Directory", "ਸੁਰੱਖਿਆ ਅਨੁਕੂਲਤਾ"]
tags: ["WMI ਫਿਲਟਰਿੰਗ", "GPO", "Group Policy Objects", "WMI ਫਿਲਟਰ", "ਨੀਤੀ ਟਾਰਗੇਟਿੰਗ", "WMI ਪੁੱਛਗਿੱਛਾਂ", "Windows Management Instrumentation", "GPO ਨਿਯੰਤਰਣ", "Group Policy Management Console", "WMI Query Language", "ਨੀਤੀ ਲਾਗੂ ਕਰਨਾ", "WQL", "ਨੀਤੀਆਂ ਨੂੰ ਸੁਚੱਜਾ ਕਰਨਾ", "ਨੀਤੀ ਪ੍ਰਬੰਧਨ", "ਸਿਸਟਮ ਸਰੋਤ", "ਨੀਤੀ ਟਾਰਗੇਟਿੰਗ ਦੀਆਂ ਉਦਾਹਰਨਾਂ", "ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ", "ਨੈੱਟਵਰਕ ਪ੍ਰਬੰਧਨ", "IT ਢਾਂਚੇ ਦਾ ਪ੍ਰਬੰਧਨ", "IT ਆਟੋਮੇਸ਼ਨ", "Active Directory ਪ੍ਰਬੰਧਨ", "ਸੁਰੱਖਿਆ ਅਨੁਕੂਲਤਾ", "ਨੀਤੀ ਨਿਯੰਤਰਣ ਤਕਨੀਕਾਂ", "ਨੀਤੀ ਪ੍ਰਬੰਧਨ ਦੇ ਚੰਗੇ ਤਰੀਕੇ", "ਨੀਤੀ ਫਿਲਟਰਿੰਗ", "GPO ਨਿਯੰਤਰਣ ਰਣਨੀਤੀਆਂ", "GPO ਸੁਰੱਖਿਆ", "WMI ਫਿਲਟਰਿੰਗ ਦੇ ਫਾਇਦੇ", "WMI ਫਿਲਟਰਿੰਗ ਲਾਗੂ ਕਰਨਾ", "WMI ਫਿਲਟਰਿੰਗ ਦੇ ਚੰਗੇ ਤਰੀਕੇ"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "ਫਿਲਟਰ ਚਿੰਨ੍ਹ ਉੱਤੇ ਕੇਂਦਰਿਤ ਵੱਡਦਰਸ਼ੀ ਸ਼ੀਸ਼ੇ ਦੀ ਤਸਵੀਰ, ਜੋ WMI ਫਿਲਟਰਿੰਗ ਰਾਹੀਂ GPO ਟਾਰਗੇਟ ਕਰਨ ਨੂੰ ਦਰਸਾਉਂਦੀ ਹੈ।"
coverCaption: "GPO ਨੀਤੀਆਂ ਨੂੰ ਢੁੱਕਵੇਂ ਟਾਰਗੇਟਾਂ ਉੱਤੇ ਲਾਗੂ ਕਰਨ ਲਈ WMI ਫਿਲਟਰਿੰਗ ਵਰਤੋ।"
---

## ਜਾਣ-ਪਛਾਣ

Group Policy Object (GPO) ਵਿੱਚ [**WMI ਫਿਲਟਰਿੰਗ**](https://simeononsecurity.com/github/wmi-filters/) ਇਹ ਨਿਰਧਾਰਤ ਕਰਦੀ ਹੈ ਕਿ WMI (Windows Management Instrumentation) ਪੁੱਛਗਿੱਛਾਂ ਦੇ ਨਤੀਜਿਆਂ ਅਨੁਸਾਰ ਕਿਹੜੇ ਕੰਪਿਊਟਰਾਂ ਜਾਂ ਵਰਤੋਂਕਾਰਾਂ ਉੱਤੇ ਨੀਤੀਆਂ ਲਾਗੂ ਹੋਣ। ਇਸ ਨਾਲ ਪ੍ਰਸ਼ਾਸਕ ਨੀਤੀ ਦਾ ਟਾਰਗੇਟ ਹੋਰ ਸਹੀ ਕਰ ਸਕਦੇ ਹਨ ਅਤੇ ਨੀਤੀਆਂ ਕੇਵਲ ਚੁਣੇ ਹੋਏ ਸਿਸਟਮਾਂ ਉੱਤੇ ਲਾਗੂ ਕਰ ਸਕਦੇ ਹਨ। ਇਸ ਲੇਖ ਵਿੱਚ WMI ਫਿਲਟਰਿੰਗ, GPO ਵਿੱਚ ਇਸ ਦਾ ਕੰਮ, [WMI ਫਿਲਟਰ](https://simeononsecurity.com/github/wmi-filters/) ਬਣਾਉਣ ਅਤੇ ਅਮਲੀ ਉਦਾਹਰਨਾਂ ਬਾਰੇ ਜਾਣੋ।

## [WMI ਫਿਲਟਰਿੰਗ ਕੀ ਹੈ?](https://simeononsecurity.com/github/wmi-filters/)

[**WMI ਫਿਲਟਰਿੰਗ**](https://simeononsecurity.com/github/wmi-filters/) WMI ਪੁੱਛਗਿੱਛ ਦੇ ਨਤੀਜਿਆਂ ਦੇ ਆਧਾਰ ਉੱਤੇ GPO ਲਈ ਫਿਲਟਰ ਲਾਗੂ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਹੈ। WMI Windows ਓਪਰੇਟਿੰਗ ਸਿਸਟਮਾਂ ਵਿੱਚ ਸ਼ਾਮਲ ਪ੍ਰਬੰਧਨ ਢਾਂਚਾ ਹੈ। ਇਹ ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ ਪ੍ਰਬੰਧਨ ਸੰਬੰਧੀ ਜਾਣਕਾਰੀ ਲੈਣ ਅਤੇ ਪ੍ਰੋਗਰਾਮ ਰਾਹੀਂ ਸਿਸਟਮ ਸਰੋਤਾਂ ਨਾਲ ਕੰਮ ਕਰਨ ਦਿੰਦਾ ਹੈ। WMI ਫਿਲਟਰਿੰਗ ਨਾਲ ਪੁੱਛਗਿੱਛ ਦੇ ਨਿਰਧਾਰਤ ਮਾਪਦੰਡਾਂ ਅਨੁਸਾਰ GPO ਨੂੰ ਗਤੀਸ਼ੀਲ ਤੌਰ ਉੱਤੇ ਟਾਰਗੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

WMI ਫਿਲਟਰ WMI Query Language (WQL) ਵਿੱਚ ਲਿਖੇ ਜਾਂਦੇ ਹਨ। WQL, SQL (Structured Query Language) ਦਾ ਇੱਕ ਉਪਸਮੂਹ ਹੈ। ਫਿਲਟਰ ਆਮ ਤੌਰ ਉੱਤੇ WMI namespace ਵਿੱਚ ਮਿਲਦੀਆਂ properties ਅਤੇ values ਉੱਤੇ ਆਧਾਰਿਤ ਹੁੰਦੇ ਹਨ। ਪ੍ਰਸ਼ਾਸਕ conditions, logical operators ਅਤੇ namespaces ਨੂੰ ਜੋੜ ਕੇ ਚੁਣੇ ਹੋਏ ਕੰਪਿਊਟਰਾਂ ਜਾਂ ਵਰਤੋਂਕਾਰਾਂ ਲਈ ਸਹੀ WMI ਪੁੱਛਗਿੱਛਾਂ ਬਣਾ ਸਕਦੇ ਹਨ।

## GPO ਵਿੱਚ WMI ਫਿਲਟਰਿੰਗ ਕਿਵੇਂ ਕੰਮ ਕਰਦੀ ਹੈ?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="ਫਲੋਚਾਰਟ ਵਿੱਚ GPO ਨਾਲ ਜੁੜਿਆ WMI ਫਿਲਟਰ WQL ਪੁੱਛਗਿੱਛ ਨੂੰ True ਜਾਂ False ਵਜੋਂ ਪਰਖਦਾ ਹੈ ਅਤੇ ਨਿਰਧਾਰਤ ਕਰਦਾ ਹੈ ਕਿ ਨੀਤੀ ਟਾਰਗੇਟ ਕੰਪਿਊਟਰ ਉੱਤੇ ਲਾਗੂ ਹੋਵੇਗੀ ਜਾਂ ਨਹੀਂ" >}}

Group Policy ਵਿੱਚ **WMI ਫਿਲਟਰਿੰਗ**, **WMI ਪੁੱਛਗਿੱਛਾਂ** ਦੇ ਮੁਲਾਂਕਣ ਮੁਤਾਬਕ GPO ਨੂੰ ਚੁਣੇ ਹੋਏ ਸਿਸਟਮਾਂ ਉੱਤੇ ਲਾਗੂ ਕਰਦੀ ਹੈ। ਜਦੋਂ ਕਿਸੇ GPO ਨਾਲ **WMI ਫਿਲਟਰ** ਜੋੜਿਆ ਜਾਂਦਾ ਹੈ, ਫਿਲਟਰ ਦਾ ਨਤੀਜਾ **True** ਜਾਂ **False** ਦੱਸਦਾ ਹੈ ਕਿ GPO ਲਾਗੂ ਹੋਵੇਗੀ ਜਾਂ ਨਹੀਂ।

WMI ਫਿਲਟਰ **WMI Query Language (WQL)** ਵਰਤਦੇ ਹਨ, ਜੋ SQL (Structured Query Language) ਦਾ ਉਪਸਮੂਹ ਹੈ। WQL ਰਾਹੀਂ **WMI namespace** ਵਿੱਚ ਮੌਜੂਦ ਵੱਖ-ਵੱਖ **properties** ਅਤੇ **values** ਉੱਤੇ ਆਧਾਰਿਤ ਜਟਿਲ ਪੁੱਛਗਿੱਛਾਂ ਬਣਦੀਆਂ ਹਨ। ਇਸ ਨਾਲ ਖਾਸ ਕੰਪਿਊਟਰਾਂ ਜਾਂ ਵਰਤੋਂਕਾਰਾਂ ਨੂੰ ਟਾਰਗੇਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

ਮਿਸਾਲ ਵਜੋਂ, ਕੋਈ ਸੰਸਥਾ GPO ਨੂੰ ਕੇਵਲ Windows 10 ਚਲਾਉਣ ਵਾਲੇ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ ਲਾਗੂ ਕਰਨਾ ਚਾਹੁੰਦੀ ਹੈ। ਉਹ **Win32_OperatingSystem** class ਦੀ **OperatingSystem** property ਜਾਂਚਣ ਵਾਲਾ WMI ਫਿਲਟਰ ਬਣਾ ਸਕਦੀ ਹੈ। ਪੁੱਛਗਿੱਛ ਇਸ ਤਰ੍ਹਾਂ ਹੋ ਸਕਦੀ ਹੈ:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

ਇਹ ਪੁੱਛਗਿੱਛ ਜਾਂਚਦੀ ਹੈ ਕਿ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਦਾ version "10." ਨਾਲ ਸ਼ੁਰੂ ਹੁੰਦਾ ਹੈ ਜਾਂ ਨਹੀਂ, ਜੋ Windows 10 ਦਰਸਾਉਂਦਾ ਹੈ। ਜੇ ਨਤੀਜਾ **True** ਹੋਵੇ, ਤਾਂ GPO ਟਾਰਗੇਟ ਕੰਪਿਊਟਰ ਉੱਤੇ ਲਾਗੂ ਹੁੰਦੀ ਹੈ। ਨਹੀਂ ਤਾਂ ਲਾਗੂ ਨਹੀਂ ਹੁੰਦੀ।

WMI ਫਿਲਟਰਿੰਗ **AND**, **OR** ਅਤੇ **NOT** ਵਰਗੀਆਂ conditions ਅਤੇ logical operators ਨੂੰ ਵੀ ਸਮਰਥਨ ਦਿੰਦੀ ਹੈ। ਪ੍ਰਸ਼ਾਸਕ ਕਈ properties ਅਤੇ values ਜੋੜ ਕੇ GPO ਲਾਗੂ ਕਰਨ ਉੱਤੇ ਹੋਰ ਬਾਰੀਕ ਨਿਯੰਤਰਣ ਕਰ ਸਕਦੇ ਹਨ।

ਵੱਖ-ਵੱਖ **WMI namespaces** ਰਾਹੀਂ WMI classes ਅਤੇ properties ਦੇ ਖਾਸ ਸਮੂਹਾਂ ਤੱਕ ਪਹੁੰਚਿਆ ਜਾ ਸਕਦਾ ਹੈ। ਇਸ ਨਾਲ hardware configuration, installed software, network settings ਅਤੇ ਹੋਰ ਮਾਪਦੰਡਾਂ ਮੁਤਾਬਕ GPO ਟਾਰਗੇਟ ਹੁੰਦੀ ਹੈ।

WMI ਫਿਲਟਰ ਅਤੇ ਪੁੱਛਗਿੱਛਾਂ ਬਣਾਉਣ ਬਾਰੇ ਹੋਰ ਜਾਣਨ ਲਈ [Group Policy ਲਈ WMI Filtering](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo) ਸੰਬੰਧੀ Microsoft ਦਸਤਾਵੇਜ਼ ਵੇਖੋ।

WMI ਫਿਲਟਰਿੰਗ ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ ਬਦਲਦੀਆਂ conditions ਮੁਤਾਬਕ ਖਾਸ ਕੰਪਿਊਟਰਾਂ ਜਾਂ ਵਰਤੋਂਕਾਰਾਂ ਉੱਤੇ GPO ਢਾਲ ਕੇ IT ਵਾਤਾਵਰਣ ਨੂੰ ਵਧੀਆ ਢੰਗ ਨਾਲ ਸੰਭਾਲਣ ਦਿੰਦੀ ਹੈ।

## GPO ਲਈ WMI ਫਿਲਟਰ ਬਣਾਉਣਾ

GPO ਲਈ WMI ਫਿਲਟਰ ਬਣਾਉਣ ਵਾਸਤੇ ਇਹ ਕਦਮ ਕਰੋ:

1. Domain ਨਾਲ ਜੁੜੇ Windows ਕੰਪਿਊਟਰ ਉੱਤੇ **Group Policy Management Console** (GPMC) ਖੋਲ੍ਹੋ।

2. Domain ਨੂੰ ਖੋਲ੍ਹ ਕੇ **WMI Filters** node ਉੱਤੇ ਜਾਓ।

3. **WMI Filters** ਉੱਤੇ ਸੱਜਾ-ਕਲਿੱਕ ਕਰਕੇ **New** ਚੁਣੋ।

4. ਫਿਲਟਰ ਨੂੰ ਸਪਸ਼ਟ ਨਾਂ ਦਿਓ ਅਤੇ **Query** ਖਾਨੇ ਵਿੱਚ WMI ਪੁੱਛਗਿੱਛ ਲਿਖੋ। WQL syntax ਵਰਤੋ।

5. WMI ਫਿਲਟਰ ਸੰਭਾਲਣ ਲਈ **OK** ਕਲਿੱਕ ਕਰੋ।

ਫਿਲਟਰ ਬਣਨ ਪਿੱਛੋਂ ਉਸ ਨੂੰ ਇੱਕ ਜਾਂ ਵੱਧ GPO ਨਾਲ ਜੋੜਿਆ ਜਾ ਸਕਦਾ ਹੈ। WMI ਫਿਲਟਰ ਨੂੰ GPO ਨਾਲ ਜੋੜਨ ਲਈ:

1. ਚੁਣੀ ਹੋਈ GPO ਉੱਤੇ ਸੱਜਾ-ਕਲਿੱਕ ਕਰਕੇ **Properties** ਚੁਣੋ।

2. GPO Properties ਵਿੰਡੋ ਵਿੱਚ **WMI Filtering** tab ਖੋਲ੍ਹੋ।

3. ਸੂਚੀ ਵਿੱਚੋਂ ਚਾਹੀਦਾ WMI ਫਿਲਟਰ ਚੁਣੋ।

4. ਤਬਦੀਲੀਆਂ ਸੰਭਾਲਣ ਲਈ **OK** ਕਲਿੱਕ ਕਰੋ।

GPO ਨਾਲ WMI ਫਿਲਟਰ ਜੋੜ ਕੇ ਪੁੱਛਗਿੱਛ ਦੇ ਨਤੀਜਿਆਂ ਅਨੁਸਾਰ ਨੀਤੀਆਂ ਕਿਹੜੇ ਸਿਸਟਮਾਂ ਉੱਤੇ ਲਾਗੂ ਹੋਣਗੀਆਂ, ਇਹ ਠੀਕ ਤਰ੍ਹਾਂ ਨਿਰਧਾਰਤ ਹੁੰਦਾ ਹੈ।

## ਇੱਕ GPO ਲਈ ਕਿੰਨੇ WMI ਫਿਲਟਰ ਬਣ ਸਕਦੇ ਹਨ?

ਸਹੀ ਨੀਤੀ ਟਾਰਗੇਟਿੰਗ ਲਈ ਪ੍ਰਸ਼ਾਸਕ ਇੱਕ GPO ਵਿੱਚ **ਕਈ WMI ਫਿਲਟਰ** ਬਣਾ ਸਕਦੇ ਹਨ। ਇੱਕ GPO ਨਾਲ ਜੋੜੇ ਜਾ ਸਕਣ ਵਾਲੇ ਫਿਲਟਰਾਂ ਦੀ ਕੋਈ ਨਿਰਧਾਰਤ ਹੱਦ ਨਹੀਂ ਹੈ, ਇਸ ਲਈ ਜਟਿਲ ਜੋੜ ਸੰਭਵ ਹਨ।

ਪਰ ਫਿਲਟਰਾਂ ਦੀ ਗਿਣਤੀ GPO processing time ਨੂੰ ਪ੍ਰਭਾਵਿਤ ਕਰ ਸਕਦੀ ਹੈ। ਫਿਲਟਰ ਵਧਣ ਨਾਲ GPO ਦਾ ਮੁਲਾਂਕਣ ਅਤੇ ਲਾਗੂ ਕਰਨਾ ਵੀ ਹੋਰ ਸਮਾਂ ਲੈ ਸਕਦਾ ਹੈ। ਨੀਤੀਆਂ ਕੁਸ਼ਲਤਾ ਨਾਲ ਲਾਗੂ ਕਰਨ ਲਈ ਫਿਲਟਰਾਂ ਦੀ ਗਿਣਤੀ ਵਾਜਬ ਰੱਖੋ।

ਉਦਾਹਰਨ ਵਜੋਂ, ਕੋਈ ਸੰਸਥਾ GPO ਕੇਵਲ ਉਹਨਾਂ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ ਲਾਗੂ ਕਰਨਾ ਚਾਹੁੰਦੀ ਹੈ ਜਿਨ੍ਹਾਂ ਉੱਤੇ Windows 10 ਅਤੇ ਇੱਕ ਖਾਸ software ਹੈ। ਉਹ ਦੋ ਵੱਖਰੇ WMI ਫਿਲਟਰ ਬਣਾ ਸਕਦੀ ਹੈ: ਇੱਕ **operating system** ਲਈ ਅਤੇ ਦੂਜਾ **software installation** ਲਈ। ਦੋਹਾਂ ਨੂੰ ਜੋੜ ਕੇ ਚਾਹੀਦੇ ਕੰਪਿਊਟਰ ਚੁਣੇ ਜਾ ਸਕਦੇ ਹਨ।

ਖਾਸ ਟਾਰਗੇਟ ਦੀ ਲੋੜ ਅਤੇ processing time ਵਿਚਕਾਰ ਸੰਤੁਲਨ ਬਣਾਓ। ਫਿਲਟਰਾਂ ਦੀ ਗਿਣਤੀ ਤੈਅ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਵਾਤਾਵਰਣ ਦੀ ਜਟਿਲਤਾ, ਕੰਪਿਊਟਰਾਂ ਜਾਂ ਵਰਤੋਂਕਾਰਾਂ ਦੀ ਗਿਣਤੀ ਅਤੇ ਕਾਰਗੁਜ਼ਾਰੀ ਉੱਤੇ ਸੰਭਾਵੀ ਅਸਰ ਵੇਖੋ।

ਕਈ WMI ਫਿਲਟਰ ਬਣਾਉਣ ਦੀ ਸਹੂਲਤ GPO ਟਾਰਗੇਟਿੰਗ ਸੁਧਾਰਦੀ ਹੈ ਅਤੇ IT ਵਾਤਾਵਰਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਤੇ ਪ੍ਰਬੰਧਨ ਕੁਸ਼ਲ ਰੱਖਦੀ ਹੈ।

## GPO ਵਿੱਚ WMI ਫਿਲਟਰਿੰਗ ਦੀਆਂ ਅਮਲੀ ਮਿਸਾਲਾਂ

WMI ਫਿਲਟਰਿੰਗ GPO ਨੂੰ ਚੁਣੇ ਹੋਏ ਸਿਸਟਮਾਂ ਉੱਤੇ ਲਾਗੂ ਕਰਨ ਦੇ ਅਮਲੀ ਤਰੀਕੇ ਦਿੰਦੀ ਹੈ। ਕੁਝ ਮਿਸਾਲਾਂ:

1. **ਖਾਸ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਟਾਰਗੇਟ ਕਰਨਾ**: GPO ਕੇਵਲ **Windows 10** ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ ਲਾਗੂ ਕਰਨ ਲਈ version ਜਾਂਚਣ ਵਾਲਾ ਫਿਲਟਰ ਬਣਾਓ, ਜਿਵੇਂ `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`। ਇਸ ਨਾਲ Windows 10 ਵਾਲੇ ਕੰਪਿਊਟਰ ਚੁਣੇ ਜਾਂਦੇ ਹਨ।

2. **Desktop ਅਤੇ laptop ਲਈ ਵੱਖਰੀਆਂ ਨੀਤੀਆਂ**: ਜੇ ਦੋਹਾਂ ਜੰਤਰ ਕਿਸਮਾਂ ਲਈ ਨੀਤੀਆਂ ਵੱਖਰੀਆਂ ਹਨ, ਤਾਂ ਦੋ WMI ਫਿਲਟਰ ਵਰਤੋ। ਇੱਕ hardware attributes ਨਾਲ desktop ਪਛਾਣ ਸਕਦਾ ਹੈ, ਮਿਸਾਲ ਵਜੋਂ `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, ਅਤੇ ਦੂਜਾ laptop ਪਛਾਣ ਸਕਦਾ ਹੈ। ਇਸ ਤਰ੍ਹਾਂ ਹਰ ਕਿਸਮ ਦੇ ਜੰਤਰ ਲਈ ਢੁੱਕਵੀਂ ਨੀਤੀ ਲਾਗੂ ਹੁੰਦੀ ਹੈ।

3. **Disk space ਅਨੁਸਾਰ ਨੀਤੀ ਲਾਗੂ ਕਰਨਾ**: ਘੱਟ ਖਾਲੀ ਥਾਂ ਵਾਲੇ ਕੰਪਿਊਟਰਾਂ ਉੱਤੇ ਸਰੋਤ-ਭਾਰੀ ਨੀਤੀਆਂ ਰੋਕਣ ਲਈ ਉਪਲਬਧ ਥਾਂ ਜਾਂਚਣ ਵਾਲਾ ਫਿਲਟਰ ਬਣਾਓ। ਉਦਾਹਰਨ ਵਜੋਂ, `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` ਵਾਲੀ ਪੁੱਛਗਿੱਛ 10 GB ਤੋਂ ਘੱਟ ਖਾਲੀ ਥਾਂ ਵਾਲੇ ਕੰਪਿਊਟਰਾਂ ਨੂੰ ਬਾਹਰ ਰੱਖਦੀ ਹੈ।

ਇਹ ਮਿਸਾਲਾਂ GPO ਵਿੱਚ **WMI ਫਿਲਟਰਿੰਗ** ਦੀ ਲਚਕ ਦਿਖਾਉਂਦੀਆਂ ਹਨ। ਪ੍ਰਸ਼ਾਸਕ ਖਾਸ ਮਾਪਦੰਡਾਂ ਅਨੁਸਾਰ ਨੀਤੀਆਂ ਦਾ ਟਾਰਗੇਟ ਨਿਰਧਾਰਤ ਕਰ ਸਕਦੇ ਹਨ।

## ਨਤੀਜਾ

WMI ਫਿਲਟਰਿੰਗ Group Policy Objects ਦੀ ਲਾਭਦਾਇਕ ਸਹੂਲਤ ਹੈ। ਇਹ WMI ਪੁੱਛਗਿੱਛਾਂ ਦੇ ਨਤੀਜਿਆਂ ਦੇ ਆਧਾਰ ਉੱਤੇ ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ ਖਾਸ ਕੰਪਿਊਟਰਾਂ ਜਾਂ ਵਰਤੋਂਕਾਰਾਂ ਲਈ ਨੀਤੀਆਂ ਲਾਗੂ ਕਰਨ ਦਿੰਦੀ ਹੈ। ਇਸ ਨਾਲ ਨੀਤੀ ਪ੍ਰਬੰਧਨ ਕੁਸ਼ਲ ਅਤੇ ਨਿਯੰਤਰਿਤ ਬਣਦਾ ਹੈ। ਇਸ ਲੇਖ ਵਿੱਚ ਅਸੀਂ WMI ਫਿਲਟਰਿੰਗ, GPO ਵਿੱਚ ਇਸ ਦੇ ਕੰਮ, ਫਿਲਟਰ ਬਣਾਉਣ ਅਤੇ ਅਮਲੀ ਮਿਸਾਲਾਂ ਬਾਰੇ ਜਾਣਿਆ।

GPO ਪ੍ਰਬੰਧਨ ਵਿੱਚ WMI ਫਿਲਟਰਿੰਗ ਸ਼ਾਮਲ ਕਰਨ ਨਾਲ ਨੀਤੀਆਂ ਹੋਰ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ ਅਤੇ ਕੇਵਲ ਚੁਣੇ ਹੋਏ ਟਾਰਗੇਟਾਂ ਤੱਕ ਪਹੁੰਚਦੀਆਂ ਹਨ।

## ਹਵਾਲੇ

- [Microsoft Docs: GPO ਲਈ WMI ਫਿਲਟਰ ਬਣਾਓ](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Group Policy](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Group Policy Management Console](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))

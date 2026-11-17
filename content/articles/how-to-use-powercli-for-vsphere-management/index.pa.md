---
title: "vSphere ਪ੍ਰਬੰਧਨ ਲਈ PowerCLI ਵਿੱਚ ਮਾਹਰ ਬਣੋ"
date: 2023-08-02
lastmod: 2026-11-12
toc: true
draft: false
description: "PowerCLI ਨਾਲ VMware vSphere ਦਾ ਪ੍ਰਬੰਧਨ, ਕੰਮਾਂ ਦੀ ਆਟੋਮੇਸ਼ਨ ਅਤੇ ਉਤਪਾਦਕਤਾ ਵਧਾਉਣ ਬਾਰੇ ਜਾਣੋ।"
genre: ["ਤਕਨਾਲੋਜੀ", "ਵਰਚੁਅਲਾਈਜ਼ੇਸ਼ਨ", "VMware", "ਆਈਟੀ ਪ੍ਰਬੰਧਨ", "ਆਟੋਮੇਸ਼ਨ", "ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ", "ਸਕ੍ਰਿਪਟਿੰਗ", "ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ", "ਕਲਾਉਡ ਕੰਪਿਊਟਿੰਗ", "ਡਾਟਾ ਸੈਂਟਰ ਪ੍ਰਬੰਧਨ"]
tags: ["PowerCLI", "VMware PowerCLI", "PowerCLI ਇੰਸਟਾਲੇਸ਼ਨ", "PowerCLI ਇੰਸਟਾਲ ਕਰੋ", "PowerCLI ਡਾਊਨਲੋਡ", "PowerCLI ਡਾਊਨਲੋਡ ਕਰੋ", "PowerCLI ਨਾਲ vCenter ਜੋੜੋ", "vSphere ਪ੍ਰਬੰਧਨ", "ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਪ੍ਰਬੰਧਨ", "ਹੋਸਟ ਪ੍ਰਬੰਧਨ", "ਆਟੋਮੇਸ਼ਨ", "ਸਕ੍ਰਿਪਟਿੰਗ", "ਵਰਚੁਅਲਾਈਜ਼ੇਸ਼ਨ", "vCenter Server", "ESXi ਹੋਸਟ", "ਡਾਟਾਸਟੋਰ ਪ੍ਰਬੰਧਨ", "ਨੈੱਟਵਰਕ ਅਡੈਪਟਰ ਪ੍ਰਬੰਧਨ", "ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਬਣਾਉਣਾ", "ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਹਟਾਉਣਾ", "ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਸੈਟਿੰਗਾਂ", "ਹੋਸਟ ਸਰੋਤ ਪ੍ਰਬੰਧਨ", "CPU ਵੰਡ", "ਮੈਮੋਰੀ ਵੰਡ", "ਸਟੋਰੇਜ ਸੈਟਿੰਗਾਂ", "PowerCLI ਉਦਾਹਰਨਾਂ", "PowerCLI ਦਸਤਾਵੇਜ਼", "ਆਈਟੀ ਪ੍ਰਬੰਧਨ", "ਸਿਸਟਮ ਪ੍ਰਸ਼ਾਸਨ", "ਕਲਾਉਡ ਕੰਪਿਊਟਿੰਗ"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "ਤਸਵੀਰ ਵਿੱਚ ਇੱਕ ਵਿਅਕਤੀ PowerCLI ਕਮਾਂਡਾਂ ਨਾਲ vSphere ਵਾਤਾਵਰਨ ਦੀਆਂ ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਅਤੇ ਹੋਸਟਾਂ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਦਾ ਹੈ।"
coverCaption: "PowerCLI ਨਾਲ vSphere ਪ੍ਰਬੰਧਨ ਸੁਧਾਰੋ"
---

## ਜਾਣ-ਪਛਾਣ

**PowerCLI**, **VMware** ਵੱਲੋਂ ਦਿੱਤਾ **ਕਮਾਂਡ-ਲਾਈਨ ਇੰਟਰਫੇਸ (CLI)** ਟੂਲ ਹੈ। ਇਹ ਪ੍ਰਸ਼ਾਸਕਾਂ ਨੂੰ **VMware vSphere ਵਾਤਾਵਰਨ ਦਾ ਪ੍ਰਬੰਧਨ ਅਤੇ ਆਟੋਮੇਸ਼ਨ** ਕਰਨ ਦਿੰਦਾ ਹੈ। ਇਸਦੇ ਕਈ **cmdlet** ਪ੍ਰਬੰਧਕੀ ਕੰਮ ਸੌਖੇ ਕਰਦੇ ਅਤੇ ਉਤਪਾਦਕਤਾ ਵਧਾਉਂਦੇ ਹਨ। ਇਹ ਲੇਖ PowerCLI ਦੀ ਸਥਾਪਨਾ, vCenter ਨਾਲ ਜੋੜ ਅਤੇ ਇਸਦੇ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਵਰਤੋਂ ਬਾਰੇ ਦੱਸਦਾ ਹੈ।

______

## PowerCLI ਇੰਸਟਾਲ ਕਰਨਾ

ਆਪਣੇ ਕੰਪਿਊਟਰ ਉੱਤੇ PowerCLI ਇੰਸਟਾਲ ਕਰਨ ਲਈ:

1. VMware ਦੀ ਅਧਿਕਾਰਕ ਵੈੱਬਸਾਈਟ ਤੋਂ PowerCLI ਇੰਸਟਾਲਰ **ਡਾਊਨਲੋਡ** ਕਰੋ। ਲਿੰਕ [PowerCLI ਦਸਤਾਵੇਜ਼](https://code.vmware.com/web/dp/tool/vmware-powercli) ਵਿੱਚ ਹੈ। ਆਪਣੇ ਓਪਰੇਟਿੰਗ ਸਿਸਟਮ ਲਈ ਢੁੱਕਵਾਂ ਸੰਸਕਰਣ ਚੁਣੋ।
2. ਇੰਸਟਾਲਰ **ਚਲਾਓ** ਅਤੇ ਸਕ੍ਰੀਨ ਉੱਤੇ ਦਿੱਤੀਆਂ ਹਦਾਇਤਾਂ ਮੰਨੋ। ਇੰਸਟਾਲੇਸ਼ਨ ਥਾਂ ਅਤੇ ਵਿਕਲਪ ਚੁਣੋ।
3. ਇੰਸਟਾਲੇਸ਼ਨ ਪੂਰੀ ਕਰਨ ਲਈ “Finish” ਦਬਾਓ। ਹੁਣ PowerCLI ਵਰਤਣ ਲਈ ਤਿਆਰ ਹੈ।

______

## PowerCLI ਨਾਲ vCenter ਨਾਲ ਜੁੜਨਾ

ਇੰਸਟਾਲ ਕਰਨ ਤੋਂ ਬਾਅਦ vCenter ਸਰਵਰ ਨਾਲ ਜੁੜੋ, ਤਾਂ ਜੋ PowerCLI cmdlet ਰਾਹੀਂ ਵਰਚੁਅਲ ਬੁਨਿਆਦੀ ਢਾਂਚੇ ਦਾ ਪ੍ਰਬੰਧਨ ਕਰ ਸਕੋ।

1. Start ਮੀਨੂ ਜਾਂ ਡੈਸਕਟਾਪ ਸ਼ਾਰਟਕੱਟ ਤੋਂ PowerCLI ਖੋਲ੍ਹੋ।
2. vCenter ਨਾਲ ਜੁੜਨ ਲਈ ਇਹ ਕਮਾਂਡ ਚਲਾਓ:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

`<vCenter IP or hostname>` ਦੀ ਥਾਂ vCenter ਸਰਵਰ ਦਾ ਅਸਲ IP ਪਤਾ ਜਾਂ ਹੋਸਟਨਾਮ ਦਿਓ।

3. ਪੁੱਛੇ ਜਾਣ ਉੱਤੇ vCenter ਪ੍ਰਬੰਧਨ ਲਈ ਕਾਫ਼ੀ ਅਧਿਕਾਰਾਂ ਵਾਲੇ ਖਾਤੇ ਦੇ ਲਾਗਇਨ ਵੇਰਵੇ ਦਿਓ।
4. **Get-VMHost** ਵਰਗੀ ਸੌਖੀ ਕਮਾਂਡ ਨਾਲ ਜੋੜ ਜਾਂਚੋ। ESXi ਹੋਸਟਾਂ ਦੀ ਸੂਚੀ ਆਵੇ ਤਾਂ ਜੋੜ ਸਫਲ ਹੈ।

______

## vSphere ਪ੍ਰਬੰਧਨ ਲਈ PowerCLI ਵਰਤਣਾ

vCenter ਨਾਲ ਜੁੜ ਕੇ ਤੁਸੀਂ ਕਈ ਆਮ ਕੰਮ ਕਰ ਸਕਦੇ ਹੋ।

### ਜਾਣਕਾਰੀ ਲੈਣਾ

vSphere ਵਾਤਾਵਰਨ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ PowerCLI ਵਿੱਚ ਕਈ cmdlet ਹਨ:

- **Get-VM**: ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲੈਂਦਾ ਹੈ।
- **Get-VMHost**: ESXi ਹੋਸਟਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲੈਂਦਾ ਹੈ।
- **Get-Datastore**: ਡਾਟਾਸਟੋਰਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲੈਂਦਾ ਹੈ।
- **Get-NetworkAdapter**: ਨੈੱਟਵਰਕ ਅਡੈਪਟਰਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲੈਂਦਾ ਹੈ।

ਨਤੀਜਿਆਂ ਨੂੰ ਛਾਂਟਣ ਅਤੇ ਰੂਪ ਦੇਣ ਲਈ ਪੈਰਾਮੀਟਰ ਵਰਤੋ।

### ਕੰਮਾਂ ਦੀ ਆਟੋਮੇਸ਼ਨ

PowerCLI ਦੁਹਰਾਏ ਜਾਣ ਵਾਲੇ ਕੰਮ ਸਵੈਚਾਲਿਤ ਕਰਦਾ ਹੈ। ਕੁਝ ਕੋਡ ਲਾਈਨਾਂ ਨਾਲ ਕਈ ਵਸਤੂਆਂ ਉੱਤੇ ਗੁੰਝਲਦਾਰ ਕਾਰਵਾਈਆਂ ਚੱਲ ਸਕਦੀਆਂ ਹਨ।

#### ਫੋਲਡਰ ਦੀਆਂ ਸਾਰੀਆਂ VM ਦੇ ਸਨੈਪਸ਼ਾਟ ਬਣਾਉਣਾ

```PowerShell
## Power off all virtual machines on a specific host
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Take a snapshot of all virtual machines in a specific folder
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

ਇਹ ਸਕ੍ਰਿਪਟ ਦਿਖਾਉਂਦੀ ਹੈ ਕਿ ਖਾਸ ਹੋਸਟ ਦੀਆਂ VM ਕਿਵੇਂ ਬੰਦ ਕਰੀਏ ਅਤੇ ਫੋਲਡਰ ਦੀਆਂ VM ਦੇ ਸਨੈਪਸ਼ਾਟ ਕਿਵੇਂ ਬਣਾਈਏ।

#### ਫੋਲਡਰ ਦੀਆਂ ਸਾਰੀਆਂ VM ਨੂੰ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਬੰਦ ਕਰਨਾ

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

ਸਕ੍ਰਿਪਟ `Get-Folder` ਨਾਲ ਫੋਲਡਰ ਅਤੇ `Get-VM` ਨਾਲ ਉਸਦੀਆਂ VM ਲੈਂਦੀ ਹੈ। `foreach` ਲੂਪ ਹਰ VM ਦੀ ਜਾਂਚ ਕਰਦਾ ਹੈ। ਜੇ ਸਥਿਤੀ “PoweredOn” ਹੋਵੇ, ਤਾਂ `Shutdown-VMGuest` ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਬੰਦ ਕਰਦਾ ਹੈ। `-Confirm:$false` ਪੁਸ਼ਟੀ ਵਾਲਾ ਸੁਨੇਹਾ ਛੱਡ ਦਿੰਦਾ ਹੈ। ਇਸ ਤਰ੍ਹਾਂ ਫੋਲਡਰ ਦੀਆਂ VM ਕ੍ਰਮਵਾਰ ਬੰਦ ਹੁੰਦੀਆਂ ਹਨ। PowerCLI ਸਕ੍ਰਿਪਟਿੰਗ ਨਾਲ ਆਪਣੀ ਲੋੜ ਮੁਤਾਬਕ ਆਟੋਮੇਸ਼ਨ ਬਣਾਓ।

### ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਅਤੇ ਹੋਸਟਾਂ ਦਾ ਪ੍ਰਬੰਧਨ

PowerCLI ਰਾਹੀਂ ਕਈ ਪ੍ਰਬੰਧਕੀ ਕੰਮ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ:

- **ਵਰਚੁਅਲ ਮਸ਼ੀਨ ਬਣਾਉਣਾ ਅਤੇ ਹਟਾਉਣਾ**: **`New-VM`** ਅਤੇ **`Remove-VM`** ਵਰਤੋ। **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** ਬਣਾਉਣ ਵੇਲੇ CPU, ਮੈਮੋਰੀ, ਡਿਸਕ ਅਤੇ ਨੈੱਟਵਰਕ ਪੈਰਾਮੀਟਰ ਲੈਂਦਾ ਹੈ।
- **VM ਸੈਟਿੰਗਾਂ ਬਦਲਣਾ**: CPU, ਮੈਮੋਰੀ, ਡਿਸਕ ਅਤੇ ਨੈੱਟਵਰਕ ਬਦਲੋ। **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** CPU ਅਤੇ ਮੈਮੋਰੀ ਦੀ ਵੰਡ ਬਦਲਦਾ ਹੈ।
- **ਹੋਸਟ ਸਰੋਤਾਂ ਦਾ ਪ੍ਰਬੰਧਨ**: CPU, ਮੈਮੋਰੀ, ਨੈੱਟਵਰਕ ਅਤੇ ਸਟੋਰੇਜ ਸੰਭਾਲੋ। **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** ਹੋਸਟ ਦੀਆਂ ਨੈੱਟਵਰਕ ਅਤੇ ਸਟੋਰੇਜ ਸੈਟਿੰਗਾਂ ਬਦਲਦਾ ਹੈ।

ਇਹ PowerCLI ਨਾਲ vSphere ਪ੍ਰਬੰਧਨ ਦੀਆਂ ਕੁਝ ਉਦਾਹਰਨਾਂ ਹਨ। ਇਸਦੇ cmdlet ਪ੍ਰਬੰਧਕੀ ਕੰਮਾਂ ਨੂੰ ਸੌਖਾ ਅਤੇ ਸਵੈਚਾਲਿਤ ਕਰਦੇ ਹਨ।

## ਨਤੀਜਾ

**PowerCLI** VMware vSphere ਵਾਤਾਵਰਨ ਦੇ ਪ੍ਰਬੰਧਨ ਅਤੇ ਆਟੋਮੇਸ਼ਨ ਲਈ ਲਾਭਦਾਇਕ ਟੂਲ ਹੈ। ਇਸਦੇ cmdlet ਪ੍ਰਬੰਧਕੀ ਕੰਮ ਸੌਖੇ ਕਰਦੇ ਅਤੇ ਉਤਪਾਦਕਤਾ ਵਧਾਉਂਦੇ ਹਨ। ਇੰਸਟਾਲ ਕਰਕੇ vCenter ਨਾਲ ਜੁੜਨ ਉਪਰੰਤ ਜਾਣਕਾਰੀ ਲਵੋ, ਕੰਮ ਸਵੈਚਾਲਿਤ ਕਰੋ ਅਤੇ ਵਰਚੁਅਲ ਮਸ਼ੀਨਾਂ ਤੇ ਹੋਸਟਾਂ ਦਾ ਕੁਸ਼ਲ ਪ੍ਰਬੰਧਨ ਕਰੋ।

vSphere ਪ੍ਰਬੰਧਨ ਸੌਖਾ ਕਰਨ ਲਈ PowerCLI ਅਜ਼ਮਾਓ।


## ਹਵਾਲੇ
- [PowerCLI ਦਸਤਾਵੇਜ਼](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: VMware PowerCLI cmdlet ਸੰਦਰਭ](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: VMware PowerCLI cmdlet ਸੰਦਰਭ](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)

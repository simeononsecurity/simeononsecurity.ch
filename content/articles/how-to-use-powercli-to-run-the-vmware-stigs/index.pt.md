---
title: "Domine a segurança do VMware"
date: 2023-08-03
lastmod: 2026-11-13
toc: true
draft: false
description: "Aprenda a usar o PowerCLI para aplicar os STIGs do VMware e proteger seu ambiente VMware com este guia abrangente."
genre: ["Cibersegurança", "Virtualização", "Infraestrutura de TI", "Automação", "PowerShell", "VMware", "STIG", "Conformidade", "Scripting", "Data center"]
tags: ["PowerCLI", "STIG do VMware", "segurança VMware", "automação", "scripting", "PowerShell", "ESXi", "virtualização", "conformidade", "cibersegurança", "como usar PowerCLI para STIGs do VMware", "automatizar a segurança VMware com PowerCLI", "script PowerCLI para implementar STIG do VMware", "automação PowerCLI para segurança do ESXi", "proteger um ambiente VMware com PowerCLI"]
cover: "/img/cover/An_illustration_depicting_a_computer_server_sh.webp"
coverAlt: "Ilustração de um servidor de computador protegido por um cadeado, símbolo de uma infraestrutura VMware segura."
coverCaption: "Use o PowerCLI para proteger seu ambiente VMware"
---

**Como aplicar STIGs do VMware com PowerCLI**

O PowerCLI é uma ferramenta de automação e scripting que permite gerenciar e configurar ambientes VMware com o PowerShell. Este artigo explica como usar o PowerCLI para aplicar o VMware STIG (Security Technical Implementation Guide) ao ESXi e às máquinas virtuais.

## Introdução

O **VMware STIG** oferece orientações e recomendações para configurar e administrar a infraestrutura VMware com segurança. Segui-lo ajuda as organizações a reforçar a segurança das implantações VMware e a cumprir requisitos governamentais aplicáveis, como o **STIG da Defense Information Systems Agency (DISA)**.

## O que é PowerCLI?

**PowerCLI** é uma interface de linha de comando e uma ferramenta de scripting para administrar ambientes VMware. É baseado no PowerShell e oferece muitos cmdlets criados para a administração VMware. Administradores podem automatizar tarefas repetitivas, alterar configurações e coletar informações da infraestrutura VMware.

### Instalação e requisitos

Antes de começar a usar PowerCLI e VMware STIG, confirme os seguintes pré-requisitos:

- [**PowerCLI 11.3**](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089): instale o PowerCLI pelo PowerShell Gallery com o comando `Install-Module VMware.PowerCLI -force`.
- [**PowerShell 5 ou posterior**](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1): verifique se o PowerShell 5 ou posterior está instalado.
- [**ESXi 6.7 U2 ou posterior**](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742): use o ESXi 6.7 U2 ou posterior.

## Automatizar o STIG do VMware VCSA

O STIG do VMware ESXi fornece orientações para proteger hosts ESXi. Automatizar a aplicação dos controles STIG simplifica o processo e mantém uma configuração consistente em vários hosts.

### Considerações

Antes de executar a automação, considere estes pontos:

- **Confirme que nenhuma máquina virtual ou sistema convidado no host ou cluster ESXi precisa de recursos de CD, USB ou unidade de disquete.**
- **Aplique o STIG a todos os hosts ESXi e sistemas convidados conectados ao vCenter.**
- **Tenha conhecimento de solução de problemas para lidar com eventuais falhas durante o processo.**

### Script: automação do STIG do VMware VCSA

O script PowerCLI a seguir automatiza a aplicação de controles STIG selecionados para VCSAs:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
$vcenters = 127.0.0.1, 127.0.0.2

#Conectar-se a cada servidor vCenter
ForEach ($vc in $vcenters) {
    Connect-VIServer -Server $vc
}

#Automatizado

Write-Host "ID da vulnerabilidade: V-243098 ID da regra: SV-243098r719537_rule ID STIG: VCTR-67-000036"
Write-Host "Se o valor de 'config.log.level' não estiver definido como "info" ou não existir, isso é uma constatação."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.log.level | Set-AdvancedSetting -Value info
    Get-AdvancedSetting -Entity $vc -Name config.log.level
}

Write-Host "ID da vulnerabilidade: V-243090 ID da regra: SV-243090r719513_rule ID STIG: VCTR-67-000024"
Write-Host "Se 'config.vpxd.hostPasswordLength' tiver um valor diferente de "32", isso é uma constatação.
Se a configuração não existir, não há constatação."
ForEach ($vc in $vcenters) {
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength | Set-AdvancedSetting -Value 32
    Get-AdvancedSetting -Entity $vc -Name config.vpxd.hostPasswordLength
}


Write-Host "ID da vulnerabilidade: V-243089 ID da regra: SV-243089r719510_rule ID STIG: VCTR-67-000023"
Write-Host "Se 'VirtualCenter.VimPasswordExpirationInDays' tiver um valor diferente de "30" ou não existir, isso é uma constatação."
ForEach ($vc in $vcenters) {
    Try {
        Get-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays | Set-AdvancedSetting -Value 30
    }
    Catch {
        New-AdvancedSetting -Entity $vc -Name VirtualCenter.VimPasswordExpirationInDays -Value 30
    }
}

Write-Host "ID da vulnerabilidade: V-243084 ID da regra: SV-243085r719498_rule ID STIG: VCTR-67-000016"
Write-Host "Se o NetFlow estiver configurado e o IP do coletor não for conhecido e documentado, isso é uma constatação."
$pgs = Get-VDPortgroup | Get-View
ForEach ($pg in $pgs) {
    $spec = New-Object VMware.Vim.DVPortgroupConfigSpec
    $spec.configversion = $pg.Config.ConfigVersion
    $spec.defaultPortConfig = New-Object VMware.Vim.VMwareDVSPortSetting
    $spec.defaultPortConfig.ipfixEnabled = New-Object VMware.Vim.BoolPolicy
    $spec.defaultPortConfig.ipfixEnabled.inherited = $false
    $spec.defaultPortConfig.ipfixEnabled.value = $false
    $pg.ReconfigureDVPortgroup_Task($spec)
}
Get-VDPortgroup | Select-Object Name, VirtualSwitch, @{N = "NetFlowEnabled"; E = { $_.Extensiondata.Config.defaultPortConfig.ipfixEnabled.Value } }

Write-Host "ID da vulnerabilidade: V-243084 ID da regra: SV-243084r719495_rule ID STIG: VCTR-67-000015"
Write-Host "O servidor vCenter deve definir como rejeitar a política Promiscuous Mode do grupo de portas distribuído."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -AllowPromiscuous $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy


Write-Host "ID da vulnerabilidade: V-243083 ID da regra: SV-243083r719492_rule ID STIG: VCTR-67-000014"
Write-Host "O servidor vCenter deve definir como rejeitar a política MAC Address Change do grupo de portas distribuído."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -MacChanges $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID da vulnerabilidade: V-243082 ID da regra: SV-243082r719489_rule ID STIG: VCTR-67-000013"
Write-Host "O servidor vCenter deve definir como rejeitar a política Forged Transmits do grupo de portas distribuído."
Get-VDSwitch | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy | Set-VDSecurityPolicy -ForgedTransmits $false
Get-VDSwitch | Get-VDSecurityPolicy
Get-VDPortgroup | Where-Object { $_.IsUplink -eq $false } | Get-VDSecurityPolicy

Write-Host "ID da vulnerabilidade: V-243081 ID da regra: SV-243081r719486_rule ID STIG: VCTR-67-000012"
Write-Host "O servidor vCenter deve desabilitar a verificação de integridade do comutador virtual distribuído."
Get-View -ViewType DistributedVirtualSwitch | Where-Object { ($_.config.HealthCheckConfig | Where-Object { $_.enable -notmatch "False" }) } | ForEach-Object { $_.UpdateDVSHealthCheckConfig(@((New-Object Vmware.Vim.VMwareDVSVlanMtuHealthCheckConfig -property @{enable = 0 }), (New-Object Vmware.Vim.VMwareDVSTeamingHealthCheckConfig -property @{enable = 0 }))) }
$vds = Get-VDSwitch
$vds.ExtensionData.Config.HealthCheckConfig

Write-Host "ID da vulnerabilidade: V-243077 ID da regra: SV-243077r719474_rule ID STIG: VCTR-67-00000"
Write-Host "O servidor vCenter deve gerenciar capacidade excedente, largura de banda ou outra redundância para limitar os efeitos de ataques de negação de serviço (DoS) por inundação de informações, habilitando o Network I/O Control (NIOC)."
Write-Host "Se nenhum alerta for criado e habilitado para notificar falhas do syslog, isso é uma constatação."
ForEach ($vdswitch in (Get-VDSwitch.name)){
    (Get-VDSwitch $vdswitch | Get-View).EnableNetworkResourceManagement($true)
}
Get-VDSwitch | Select-Object Name, @{N = "NIOC Enabled"; E = { $_.ExtensionData.config.NetworkResourceManagementEnabled } }

#Revisão manual

Write-Host "ID da vulnerabilidade: V-243076 ID da regra: SV-243076r719471_rule ID STIG: VCTR-67-000005"
Write-Host "Os usuários do servidor vCenter devem receber as funções corretas."
Write-Host "Os privilégios necessários para contas de serviço e usuários devem ser documentados.
Se uma conta de usuário ou serviço tiver mais privilégios que o necessário, isso é uma constatação."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID da vulnerabilidade: V-243119 ID da regra: SV-243119r719600_rule ID STIG: VCTR-67-000064"
Write-Host "Se uma função diferente de Administrator ou algum grupo específico do site tiver qualquer uma dessas permissões, isso é uma constatação."
$roles = Get-VIRole
ForEach ($role in $roles) {
    $privileges = $role.PrivilegeList
    If ($privileges -match "Crypto*" -or $privileges -match "Global.Diagnostics" -or $privileges -match "Host.Inventory.Add*" -or $privileges -match "Host.Local operations.Manage user groups") {
        Write-Host "$role tem privilégios criptográficos"
    }
}

Write-Host "ID da vulnerabilidade: V-243118 ID da regra: SV-243118r719597_rule ID STIG: VCTR-67-000063"
Write-Host "Se usuários que não sejam Solution Users tiverem a função "Administrator" sem designação explícita para operações criptográficas, isso é uma constatação."
Get-VIPermission | Where-Object { $_.Role -eq "Admin" } | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto


Write-Host "ID da vulnerabilidade: V-243111 ID da regra: SV-243111r719576_rule ID STIG: VCTR-67-000055"
Write-Host "Não aplicável se nenhum cluster vSAN estiver habilitado."
Write-host "Se o vSAN estiver habilitado e o datastore se chamar 'vsanDatastore', isso é uma constatação."
If ($(Get-Cluster | Where-Object { $_.VsanEnabled } | Measure-Object).Count -gt 0) {
    Write-Host "Cluster vSAN habilitado encontrado"
    $Clusters = Get-Cluster | Where-Object { $_.VsanEnabled } 
    Foreach ($clus in $clusters) {
        $clus | Get-Datastore | Where-Object { $_.type -match "vsan" } | Set-Datastore -Name $(($clus.name) + "_vSAN_Datastore")
    }
}
else {
    Write-Host "O vSAN não está habilitado; esta constatação não se aplica"
}

Write-Host "Se uma conta de usuário ou serviço tiver mais privilégios que o necessário, isso é uma constatação."
Get-VIPermission | Sort-Object Role | Select-Object Role, Principal, Entity, Propagate, IsGroup | Format-Table -Auto

Write-Host "ID da vulnerabilidade: V-243088 ID da regra: SV-243088r719507_rule ID STIG: VCTR-67-000020"
Write-Host "Revise as tags VLAN do grupo de portas e confirme que não usam um ID de VLAN reservado."
Write-Host "Alguns comutadores físicos reservam IDs de VLAN para uso interno e muitas vezes bloqueiam o tráfego configurado com esses valores. Por exemplo, os Cisco Catalyst geralmente reservam as VLANs 1001–1024 e 4094, enquanto os Nexus reservam 3968–4047 e 4094."
Get-VDPortgroup | Select-Object Name, VlanConfiguration

Write-Host "ID da vulnerabilidade: V-243087 ID da regra: SV-243087r719504_rule ID STIG: VCTR-67-000019"
Write-Host "Se um grupo de portas estiver configurado como 'VLAN Trunk' sem uma exceção necessária documentada (como dispositivos NSX), isso é uma constatação.
Se o entroncamento VLAN for permitido, mas não estiver limitado ao menor intervalo necessário, isso é uma constatação."
Get-VDPortgroup | Where-Object { $_.ExtensionData.Config.Uplink -ne "True" } | Select-Object Name, VlanConfiguration

Write-Host "ID da vulnerabilidade: V-243078 ID da regra: SV-243078r719644_rule ID STIG: VCTR-67-000008"
Write-Host "O servidor vCenter deve alertar imediatamente SA e ISSO, em tempo real no mínimo, sobre todas as falhas de auditoria."
Write-Host "Se nenhum alerta for criado e habilitado para notificar falhas do syslog, isso é uma constatação."
Get-AlarmDefinition | Where-Object { $_.ExtensionData.Info.Expression.Expression.EventTypeId -eq "esx.problem.vmsyslogd.remote.failure" } | Select-Object Name, Enabled, @{N = "EventTypeId"; E = { $_.ExtensionData.Info.Expression.Expression.EventTypeId } }
```

O script realiza estas funções:

- **Primeiro configura o PowerCLI, desativa a validação de certificados e cancela a participação no Customer Experience Improvement Program (CEIP).**
- **Depois se conecta aos servidores vCenter especificados na variável `$vcenters`.**
- **Aplica cada controle STIG com cmdlets do PowerCLI. Por exemplo, define `config.log.level` como info nos servidores vCenter indicados.**
- **Também trata controles relacionados a `config.vpxd.hostPasswordLength` e `VirtualCenter.VimPasswordExpirationInDays`.**
- **Por fim, verifica e configura políticas de segurança e outras opções.**
- **Este é um script de exemplo. Adapte-o ao ambiente e aos requisitos STIG correspondentes.**

______

## Automatizar o STIG de máquinas virtuais VMware

Além de proteger hosts ESXi, aplique controles STIG às máquinas virtuais da infraestrutura VMware. O PowerCLI ajuda a automatizar a configuração das VMs segundo as orientações STIG.

## Script: automação do STIG de máquinas virtuais VMware

O script PowerCLI a seguir demonstra como automatizar controles STIG selecionados para máquinas virtuais:

```powershell
Set-PowerCLIConfiguration -InvalidCertificateAction Ignore -Confirm:$false
Set-PowerCLIConfiguration -Scope User -ParticipateInCEIP $false -Confirm:$false
Connect-VIServer -Server 127.0.0.1
$cluster = Get-Cluster -Name "Cluster"
$folder = Get-Folder -Name "Folder"

#Crédito: https://github.com/rlakey/vmware-stig-powercli/blob/master/VMware_vSphere_6.7_VM_STIG_Remediation.ps1
$vmconfig = @{
    #Configurações de hardening/STIG
    vmAdvSettings       = @{
        "isolation.tools.copy.disable"          = $true
        "isolation.tools.dnd.disable"           = $true
        "isolation.tools.paste.disable"         = $true
        "isolation.tools.diskShrink.disable"    = $true
        "isolation.tools.diskWiper.disable"     = $true
        "isolation.tools.hgfsServerSet.disable" = $true
        "RemoteDisplay.maxConnections"          = "1"
        "RemoteDisplay.vnc.enabled"             = $false
        "tools.setinfo.sizeLimit"               = "1048576"
        "isolation.device.connectable.disable"  = $true
        "tools.guestlib.enableHostInfo"         = $false
        "tools.guest.desktop.autolock"          = $true
        "mks.enable3d"                          = $false
    }
    vmAdvSettingsRemove = ("sched.mem.pshare.salt")
    vmotionEncryption   = "opportunistic" #disabled, required, opportunistic
}

ForEach ($vm in (Get-VM -Location $cluster | Where-Object { (Get-VM -Location $folder) -contains $_ } )) {
    Write-Output "...Corrigindo configurações avançadas em $vm no $vcenter"
    ForEach ($setting in ($vmconfig.vmAdvSettings.GetEnumerator() | Sort-Object Name)) {
        #Obter os valores de cada configuração especificada
        $settingname = $setting.name
        $settingvalue = $setting.value
        If ($asetting = $vm | Get-AdvancedSetting -Name $settingname) {
            If ($asetting.value -eq $settingvalue) {
                Write-Output "...A configuração $settingname em $vm já está correta com o valor $settingvalue"
            }
            else {
                Write-Output "...A configuração $settingname em $vm tinha o valor incorreto $($asetting.value); definindo como $settingvalue"
                $asetting | Set-AdvancedSetting -Value $settingvalue -Confirm:$false
            }
        }
        else {
            Write-Output "...A configuração $settingname não existe em $vm; criando..."
            $vm | New-AdvancedSetting -Name $settingname -Value $settingvalue -Confirm:$false
        }
        Write-Output "...Removendo configurações avançadas em $vm no $vcenter, se necessário"
        ForEach ($setting in ($vmconfig.vmAdvSettingsRemove | Sort-Object Name)) {
            #Verificar se a configuração atual existe
            If ($asetting = $vm | Get-AdvancedSetting -Name $setting) {
                Write-Output "...A configuração $setting existe em $vm...removendo configuração"
                $asetting | Remove-AdvancedSetting -Confirm:$false
            }
            else {
                Write-Output "...A configuração $setting não existe em $vm"
            }
        }   
        If ($vm.extensiondata.Config.MigrateEncryption -eq $vmconfig.vmotionEncryption) {
            Write-Output "...A criptografia vMotion está configurada corretamente em $vm como $($vmconfig.vmotionEncryption)"
        }
        else {
            $vmv = $vm | get-view
            $config = new-object VMware.Vim.VirtualMachineConfigSpec
            $config.MigrateEncryption = New-object VMware.Vim.VirtualMachineConfigSpecEncryptedVMotionModes
            $config.MigrateEncryption = "$($vmconfig.vmotionEncryption)"
            $vmv.ReconfigVM($config)
        }
    }
}
```

O script realiza estas funções:

- **Assim como o script STIG do VMware VCSA, configura o ambiente PowerCLI no início.**
- **Conecta-se ao vCenter e seleciona o cluster e a pasta que contêm as VMs de destino.**
- **A variável `$vmconfig` contém as configurações STIG das VMs. Inclui opções avançadas, como desativar copiar e colar e limitar conexões de exibição remota.**
- **Percorre cada VM no cluster e na pasta selecionados e aplica as configurações STIG.**
- **Também configura a criptografia vMotion das VMs.**

Este script é um exemplo. Modifique-o de acordo com seu ambiente e os requisitos STIG aplicáveis.

_____

## Recursos adicionais

- **O VIB STIG do DoD [esteve disponível para as versões 5.0 a 6.7](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib), mas não está mais disponível.**
- [Ryan Lakey](https://core.vmware.com/users/ryan-lakey) oferece orientações úteis para implementar os STIGs DoD no VMware. Recomendamos a leitura desses materiais.
    - [STIG do VMware vSphere 8](https://core.vmware.com/resource/vmware-vsphere-8-stig)
    - [STIG do VMware vSphere 7](https://core.vmware.com/vsphere-7-stig)
    - [STIG do VMware vSphere 6.7](https://core.vmware.com/vmware-vsphere-67-stig)
    - [PowerCLI STIG do VMware](https://github.com/rlakey/vmware-stig-powercli)
        - [Baseline STIG do VMware VCSA 6.7](https://github.com/rlakey/vmware-vcsa-6.7-stig-baseline)
        - [Baseline STIG de VM do VMware 6.7](https://github.com/rlakey/vmware-vm-6.7-stig-baseline)
_____

## Conclusão

**Aplicar o VMware STIG ajuda a proteger a infraestrutura VMware e a cumprir requisitos pertinentes. O PowerCLI automatiza e simplifica a aplicação de controles STIG a hosts ESXi e máquinas virtuais.**

Este artigo apresentou o uso do PowerCLI para automatizar os STIGs de VMware ESXi e VM. Descreveu os requisitos de instalação, incluiu scripts de exemplo e destacou a importância de adaptá-los às necessidades de cada ambiente.

**Com o PowerCLI e as orientações STIG, administradores podem proteger implantações VMware com eficiência, reduzir o trabalho manual e manter configurações consistentes.**

## Referências

- [VIB STIG do DoD](https://flings.vmware.com/dod-security-technical-implementation-guide-stig-esxi-vib)
- [PowerCLI 11.3](https://www.powershellgallery.com/packages/VMware.PowerCLI/11.3.0.13990089)
- [PowerShell 5 ou posterior](https://docs.microsoft.com/en-us/skypeforbusiness/set-up-your-computer-for-windows-powershell/download-and-install-windows-powershell-5-1)
- [ESXi 6.7 U2 ou posterior](https://my.vmware.com/web/vmware/downloads/details?downloadGroup=ESXI670&productId=742)

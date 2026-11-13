---
title: "Domine o PowerCLI para gerenciar o vSphere"
date: 2023-08-02
lastmod: 2026-11-12
toc: true
draft: false
description: "Aprenda a usar o PowerCLI para gerenciar VMware vSphere, automatizar tarefas e aumentar a produtividade."
genre: ["Tecnologia", "Virtualização", "VMware", "Gestão de TI", "Automação", "Interface de linha de comando", "Scripting", "Administração de sistemas", "Computação em nuvem", "Gestão de datacenter"]
tags: ["PowerCLI", "VMware PowerCLI", "Instalação do PowerCLI", "Instalar PowerCLI", "Baixar PowerCLI", "Download do PowerCLI", "Conectar PowerCLI ao vCenter", "Gestão do vSphere", "Gestão de máquinas virtuais", "Gestão de hosts", "Automação", "Scripting", "Virtualização", "Servidor vCenter", "Hosts ESXi", "Gestão de datastores", "Gestão de adaptadores de rede", "Criação de máquinas virtuais", "Remoção de máquinas virtuais", "Configurações de máquinas virtuais", "Recursos do host", "Alocação de CPU", "Alocação de memória", "Configurações de armazenamento", "Exemplos do PowerCLI", "Documentação do PowerCLI", "Gestão de TI", "Administração de sistemas", "Computação em nuvem"]
cover: "/img/cover/An_illustrated_cartoon_image_showcasing_a_pers.webp"
coverAlt: "Ilustração de uma pessoa usando comandos PowerCLI para gerenciar máquinas virtuais e hosts em um ambiente vSphere."
coverCaption: "Melhore a gestão do vSphere com PowerCLI"
---

## Introdução

**PowerCLI** é uma ferramenta de **interface de linha de comando (CLI)** da **VMware** que permite aos administradores **gerenciar e automatizar** ambientes **VMware vSphere**. Seus diversos **cmdlets** simplificam tarefas administrativas e aumentam a produtividade, seja para iniciantes ou usuários experientes. Este artigo apresenta a instalação, a conexão ao vCenter e o uso eficaz do PowerCLI.

______

## Instalar o PowerCLI

Instale o PowerCLI no computador seguindo estas etapas:

1. **Baixe** o instalador no site oficial da VMware. O link está na [documentação do PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli). Escolha a versão adequada ao sistema operacional.
2. **Execute** o instalador e siga as instruções. Escolha o local e as opções desejadas.
3. Clique em “Finish” para concluir a instalação e começar a usar o PowerCLI.

______

## Conectar ao vCenter com PowerCLI

Depois de instalar o PowerCLI, conecte-se ao servidor vCenter para administrar a infraestrutura virtual pelos cmdlets.

1. Abra o PowerCLI no menu Iniciar ou pelo atalho da área de trabalho.
2. Execute este comando para conectar ao vCenter:

```powershell
Connect-VIServer -Server <vCenter IP or hostname>
```

Substitua `<vCenter IP or hostname>` pelo endereço IP ou nome de host real do servidor vCenter.

3. Quando solicitado, informe as credenciais de uma conta com privilégios suficientes para administrar o vCenter.
4. Verifique a conexão com um comando simples, como **Get-VMHost**. Se a lista de hosts ESXi aparecer, a conexão funcionou.

______

## Usar PowerCLI para gerenciar o vSphere

Depois de se conectar ao vCenter, você pode executar tarefas comuns.

### Obter informações

O PowerCLI oferece cmdlets para consultar o ambiente vSphere:

- **Get-VM**: obtém informações sobre máquinas virtuais.
- **Get-VMHost**: obtém informações sobre hosts ESXi.
- **Get-Datastore**: obtém informações sobre datastores.
- **Get-NetworkAdapter**: obtém informações sobre adaptadores de rede.

Use parâmetros para filtrar e formatar a saída.

### Automatizar tarefas

O PowerCLI automatiza tarefas repetitivas. Poucas linhas de código podem executar operações complexas em vários objetos.

#### Criar snapshots de todas as VMs em uma pasta

```PowerShell
## Power off all virtual machines on a specific host
Get-VMHost -Name "MyHost" | Get-VM | Stop-VM

## Take a snapshot of all virtual machines in a specific folder
Get-Folder -Name "MyFolder" | Get-VM | New-Snapshot -Name "DailySnapshot" -Description "Daily Backup"
```

Este script mostra como desligar as VMs de um host e criar snapshots das VMs em uma pasta.

#### Desligar todas as VMs de uma pasta com segurança

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

O script localiza a pasta com `Get-Folder` e obtém suas VMs com `Get-VM`. O laço `foreach` verifica cada máquina. Se o estado for “PoweredOn”, `Shutdown-VMGuest` inicia o desligamento normal. `-Confirm:$false` dispensa a confirmação. Assim, as máquinas da pasta são desligadas de forma ordenada. A criação de scripts PowerCLI permite adaptar a automação às suas necessidades.

### Gerenciar máquinas virtuais e hosts

O PowerCLI permite várias tarefas de gestão:

- **Criar e remover máquinas virtuais**: use **`New-VM`** e **`Remove-VM`**. O cmdlet **[cmdlet New-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/new-vm/#DefaultParameterSet)** aceita parâmetros de CPU, memória, disco e rede.
- **Alterar configurações de VMs**: ajuste CPU, memória, disco e rede. **[cmdlet Set-VM](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/set-vm/#DefaultSet)** altera a alocação de CPU e memória.
- **Gerenciar recursos do host**: administre CPU, memória, rede e armazenamento. **[cmdlet Set-VMHost](https://vdc-repo.vmware.com/vmwb-repository/dcr-public/e7c1a32c-a3c6-4d7c-91bb-18a86a38daf7/12353298-ce6e-4d3f-bd8d-ab9f5ab044cc/doc/Set-VMHost.html)** modifica as configurações de rede e armazenamento do host.

Estes são alguns exemplos. O amplo conjunto de cmdlets do PowerCLI automatiza e simplifica tarefas administrativas do vSphere.

## Conclusão

**PowerCLI** é uma ferramenta útil para gerenciar e automatizar ambientes VMware vSphere. Seus cmdlets simplificam a administração e aumentam a produtividade. Depois de instalar e conectar ao vCenter, você pode obter informações, automatizar tarefas e gerenciar máquinas virtuais e hosts com eficiência.

Explore o PowerCLI para simplificar a gestão do vSphere.


## Referências
- [Documentação do PowerCLI](https://code.vmware.com/web/dp/tool/vmware-powercli)
- [Connect-VIServer: referência do cmdlet VMware PowerCLI](https://docs.vmware.com/en/VMware-PowerCLI/latest/VMware.VimAutomation.Core/Connect-VIServer.html)
- [Get-VM: referência do cmdlet VMware PowerCLI](https://developer.vmware.com/docs/powercli/latest/vmware.vimautomation.core/commands/get-vm/#Default)

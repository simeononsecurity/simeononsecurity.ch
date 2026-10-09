---
title: "Administração do Active Directory com PowerShell"
date: 2023-07-25
toc: true
draft: false
description: Descubra como instalar e usar efetivamente o módulo do Active Directory para PowerShell para simplificar suas tarefas de administração do Active Directory no Windows.
genre:
- Tecnologia
- Windows
- PowerShell
- Active Directory
- Administração
- Scripting
- TI
- Automação
- Windows Server
- Microsoft
tags:
- módulo do active directory para PowerShell
- importar módulo active directory no PowerShell
- módulo do active directory para Windows PowerShell
- active directory PowerShell instalar
- instalar active directory PowerShell
- PowerShell instalar módulo active directory Windows 10
- instalar módulo active directory PowerShell Windows 10
- obter módulo active directory PowerShell
- administração AD
- Windows Active Directory
- cmdlets PowerShell
- recuperar informações AD
- criar objetos AD
- modificar objetos AD
- gerenciar segurança AD
- gerenciamento de usuários AD
- gerenciamento de grupos AD
- gerenciamento de UOs AD
- scripting PowerShell
- administração Windows Server
- Microsoft PowerShell
- automatizar tarefas AD
- instalação do módulo PowerShell
- guia de administração AD
- gerenciamento do Active Directory
- gerenciamento de segurança AD
- automação PowerShell
- comandos PowerShell do Active Directory
- referência de cmdlets PowerShell
cover: /img/cover/active-directory-module-powershell-installation-usage-guide.webp
coverAlt: Uma ilustração de uma tela de computador mostrando um console do PowerShell com cmdlets coloridos, cercado por representações abstratas de contas de usuário e grupos, com um fundo escuro.
coverCaption: Desbloqueie o Poder da Administração do Active Directory com PowerShell.
lastmod: 2026-10-08
---

## Introdução

Hoje, gerenciar e manter contas de usuário, grupos de segurança e outros recursos em um ambiente Windows Active Directory (AD) requer processos eficientes e simplificados. O PowerShell, uma poderosa linguagem de scripting desenvolvida pela Microsoft, oferece o **módulo do Active Directory** para facilitar as tarefas de administração do AD. Este módulo fornece muitos cmdlets que permitem aos administradores automatizar várias operações e gerenciar o AD de forma eficaz. Neste artigo, exploraremos a instalação e o uso do módulo do Active Directory para PowerShell.

## Instalação do Módulo do Active Directory para PowerShell

Para começar a usar o módulo do Active Directory para PowerShell, você precisa garantir que ele esteja instalado no seu sistema. O processo de instalação pode variar dependendo do seu sistema operacional. Aqui estão os passos para instalar o módulo no **Windows 10**, **Windows 11** e **Windows Server**:

### Windows 10 e Windows 11 - PowerShell
1. Abra o **Windows PowerShell** com privilégios administrativos.
2. Execute o seguinte comando para instalar o módulo:

```powershell
Add-WindowsCapability -Name Rsat.ActiveDirectory.DS-LDS.Tools~~~~0.0.1.0 -Online
```

1. Aguarde a conclusão da instalação. Quando terminar, você poderá começar a usar o módulo do Active Directory.

### Windows Server 
1. Abra o **Windows PowerShell** com privilégios administrativos.
2. Execute o seguinte comando para instalar o módulo:

```powershell
Install-WindowsFeature -Name "RSAT-AD-PowerShell" -IncludeAllSubFeature
```

3. Aguarde a conclusão da instalação. Quando terminar, você poderá começar a usar o módulo do Active Directory.

### Sistemas Offline

Sistemas Offline são um pouco mais complicados. Existem alguns métodos, porém o que recomendamos é o uso do seguinte script:
- [Offine-PS-ActiveDirectory-Install](https://github.com/simeononsecurity/Offine-PS-ActiveDirectory-Install)

## Importando o Módulo do Active Directory no PowerShell

Antes de poder usar o módulo do Active Directory no PowerShell, você precisa importá-lo para sua sessão atual. Siga estes passos para importar o módulo:

1. Inicie o **Windows PowerShell** com direitos administrativos.
2. Execute o seguinte comando para importar o módulo:

```powershell
Import-Module ActiveDirectory
```

3. O módulo do Active Directory será importado e você poderá acessar seus cmdlets e funções.

## Usando o Módulo do Active Directory para PowerShell

Com o módulo do Active Directory importado, você pode aproveitar seu rico conjunto de cmdlets para realizar várias tarefas administrativas. Aqui está uma visão de alguns cmdlets comumente usados e suas funcionalidades:

### Recuperando Informações do Active Directory

Para gerenciar efetivamente um ambiente Active Directory (AD), você precisa recuperar informações sobre vários objetos do AD, como usuários, grupos e unidades organizacionais (UOs). O PowerShell fornece cmdlets poderosos que simplificam o processo de recuperação.

- [**Get-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser?view=windowsserver2022-ps): Este cmdlet permite recuperar informações detalhadas sobre usuários do AD. Você pode obter atributos como nome de usuário, nome para exibição, endereço de e-mail e mais. Por exemplo, para recuperar todos os usuários cujos nomes de usuário começam com "johndoe", você pode executar o seguinte comando:

  ```powershell
  Get-ADUser -Filter 'SamAccountName -like "johndoe*"'
  ```

  Este comando retornará uma lista de objetos de usuário que correspondem ao filtro especificado.

- [**Get-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adgroup?view=windowsserver2022-ps): Com o cmdlet Get-ADGroup, você pode buscar informações sobre grupos do AD. Ele fornece acesso a detalhes como nome do grupo, membros, descrição e mais. Por exemplo, para recuperar todos os grupos de segurança no ambiente AD, você pode executar o seguinte comando:

  ```powershell
  Get-ADGroup -Filter 'GroupCategory -eq "Security"'
  ```

  Isso fornecerá uma lista de grupos de segurança no Active Directory.

- [**Get-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit?view=windowsserver2022-ps): O cmdlet Get-ADOrganizationalUnit é usado para recuperar informações sobre UOs do AD. Ele permite acessar propriedades como nome da UO, descrição, UO pai e mais. Para buscar todas as UOs no domínio, você pode usar o seguinte comando:

  ```powershell
  Get-ADOrganizationalUnit -Filter *
  ```

  Executar este comando exibirá uma lista de todas as UOs no Active Directory.

Usando esses cmdlets poderosos, você pode facilmente recuperar informações específicas sobre usuários, grupos e UOs do AD, permitindo uma administração e gerenciamento eficientes do seu ambiente Active Directory.


Esses cmdlets permitem recuperar atributos específicos, filtrar resultados e realizar consultas avançadas para obter as informações desejadas.

### Criando e Gerenciando Objetos do Active Directory

Ao trabalhar com o Active Directory (AD), o módulo do Active Directory no PowerShell oferece cmdlets poderosos para criar e gerenciar objetos do AD. Aqui está uma visão de alguns cmdlets essenciais para criar usuários, grupos e unidades organizacionais (UOs) do AD.

- [**New-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2022-ps): Este cmdlet permite criar um novo usuário do AD. Você pode especificar atributos como nome de usuário, senha, endereço de e-mail e mais. Por exemplo, para criar um novo usuário com o nome de usuário "john.doe" e o nome para exibição "John Doe", você pode usar o seguinte comando:

  ```powershell
  New-ADUser -SamAccountName "john.doe" -Name "John Doe"
  ```

  Este comando criará um novo usuário no Active Directory.

- [**New-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adgroup?view=windowsserver2022-ps): O cmdlet New-ADGroup permite criar um novo grupo do AD. Você pode definir propriedades como nome do grupo, descrição, escopo do grupo e mais. Para criar um novo grupo chamado "Marketing" com uma descrição, você pode executar o seguinte comando:

  ```powershell
  New-ADGroup -Name "Marketing" -Description "Marketing Team"
  ```

  Este comando criará um novo grupo no Active Directory.

- [**New-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-adorganizationalunit?view=windowsserver2022-ps): Com o cmdlet New-ADOrganizationalUnit, você pode criar uma nova UO no AD. Você pode especificar propriedades como nome da UO, UO pai e mais. Por exemplo, para criar uma nova UO chamada "Sales" sob a UO "Departments", você pode executar o seguinte comando:

  ```powershell
  New-ADOrganizationalUnit -Name "Sales" -Path "OU=Departments,DC=contoso,DC=com"
  ```

  Este comando criará uma nova UO na hierarquia do Active Directory.

Usando esses cmdlets, você pode facilmente criar novos usuários, grupos e UOs no AD com as propriedades e configurações desejadas, permitindo uma gestão eficiente do seu ambiente Active Directory.


### Modificando Objetos do Active Directory

Quando se trata de modificar as propriedades e atributos de objetos existentes no Active Directory (AD), o módulo Active Directory no PowerShell oferece vários cmdlets úteis. Aqui está uma visão desses cmdlets para modificar usuários, grupos e unidades organizacionais (UOs) do AD.

- [**Set-ADUser**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-aduser?view=windowsserver2022-ps): O cmdlet Set-ADUser permite modificar propriedades de um usuário do AD. Você pode atualizar atributos como nome para exibição, endereço de e-mail, número de telefone e mais. Por exemplo, para alterar o número de telefone de um usuário com o nome de usuário "john.doe", você pode usar o seguinte comando:

  ```powershell
  Set-ADUser -Identity "john.doe" -PhoneNumber "123456789"
  ```

  Este comando modificará o número de telefone do usuário especificado no Active Directory.

- [**Set-ADGroup**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adgroup?view=windowsserver2022-ps): Com o cmdlet Set-ADGroup, você pode modificar propriedades de um grupo do AD. Você pode atualizar atributos como descrição do grupo, membros, escopo do grupo e mais. Para alterar a descrição de um grupo chamado "Marketing" para "Marketing Team", você pode executar o seguinte comando:

  ```powershell
  Set-ADGroup -Identity "Marketing" -Description "Marketing Team"
  ```

  Este comando atualizará a descrição do grupo especificado no Active Directory.

- [**Set-ADOrganizationalUnit**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adorganizationalunit?view=windowsserver2022-ps): O cmdlet Set-ADOrganizationalUnit permite modificar propriedades de uma UO do AD. Você pode alterar atributos como nome da UO, descrição e mais. Por exemplo, para modificar a descrição de uma UO chamada "Sales" para "Sales Department", você pode executar o seguinte comando:

  ```powershell
  Set-ADOrganizationalUnit -Identity "OU=Sales,DC=contoso,DC=com" -Description "Sales Department"
  ```

  Este comando atualizará a descrição da UO especificada na hierarquia do Active Directory.

Usando esses cmdlets, você pode facilmente modificar as propriedades e atributos dos objetos do AD, fazendo as atualizações e ajustes necessários para atender aos requisitos da sua organização.


### Gerenciando a Segurança do Active Directory

Além de gerenciar e administrar objetos do Active Directory (AD), o módulo Active Directory no PowerShell oferece cmdlets especificamente projetados para lidar com aspectos relacionados à segurança do AD. Esses cmdlets ajudam os administradores a gerenciar eficientemente o acesso de usuários, membros de grupos e tarefas relacionadas a senhas dentro do ambiente AD.

Aqui estão alguns cmdlets relacionados à segurança comumente usados:

- [**Add-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/add-adgroupmember?view=windowsserver2022-ps): Este cmdlet permite adicionar membros a um grupo do AD. Ao especificar o grupo do AD e as contas de usuário ou grupos que deseja adicionar, você pode gerenciar facilmente o controle de acesso. Por exemplo, para adicionar um usuário chamado "JohnDoe" ao grupo "Managers", você pode usar o seguinte comando:

  ```powershell
  Add-ADGroupMember -Identity "Managers" -Members "JohnDoe"
  ```

- [**Remove-ADGroupMember**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/remove-adgroupmember?view=windowsserver2022-ps): Com este cmdlet, você pode remover membros de um grupo do AD. Ao especificar o grupo do AD e as contas de usuário ou grupos que deseja remover, você pode gerenciar efetivamente as associações de grupo. Por exemplo, para remover um usuário chamado "JaneSmith" do grupo "Developers", você pode usar o seguinte comando:

  ```powershell
  Remove-ADGroupMember -Identity "Developers" -Members "JaneSmith"
  ```

- [**Set-ADUserPassword**](https://learn.microsoft.com/en-us/powershell/module/activedirectory/set-adaccountpassword?view=windowsserver2022-ps): Este cmdlet permite definir a senha para um usuário do AD. Ao especificar a conta do usuário e fornecer uma nova senha, você pode aplicar políticas de senha e garantir uma autenticação segura do usuário. Aqui está um exemplo de definição de uma nova senha para um usuário chamado "AmyJohnson":

  ```powershell
  Set-ADUserPassword -Identity "AmyJohnson" -NewPassword (ConvertTo-SecureString -AsPlainText "NewPassword123" -Force)
  ```

Usando esses cmdlets relacionados à segurança, os administradores podem gerenciar efetivamente o acesso de usuários, membros de grupos e políticas de senha dentro do ambiente Active Directory.

## Exemplo de script do módulo Active Directory para PowerShell
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

## Conclusão

Para concluir, o **módulo Active Directory para PowerShell** é uma ferramenta poderosa que permite uma gestão eficiente e conveniente do Active Directory do Windows. Ao instalar e importar o módulo, você obtém acesso a um conjunto abrangente de **cmdlets** que simplificam várias tarefas relacionadas ao AD.

Com o módulo Active Directory, você pode realizar muitas operações, como recuperar informações sobre objetos do AD, criar novos objetos, modificar propriedades e gerenciar segurança. Este módulo ajuda os administradores a automatizar tarefas administrativas, simplificar fluxos de trabalho e garantir o funcionamento adequado dos ambientes Active Directory.

Usando o **PowerShell** e o **módulo Active Directory**, você pode aprimorar suas capacidades de administração do AD e melhorar a eficiência dos processos de gestão do AD. Seja você um administrador de sistema, profissional de TI ou gerente de Active Directory, o módulo Active Directory oferece as ferramentas necessárias para gerenciar efetivamente sua infraestrutura AD.

Aproveite o poder do **PowerShell** e do **módulo Active Directory** para simplificar suas tarefas de administração do AD, aumentar a produtividade e manter um ambiente Active Directory seguro e bem organizado.

## Referências

- [Install-WindowsFeature cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Import-Module cmdlet - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/import-module)
- [Active Directory cmdlets in PowerShell - Microsoft Docs](https://docs.microsoft.com/en-us/powershell/module/activedirectory)

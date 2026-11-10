---
title: "Crie um inventário do Active Directory somente para leitura com PowerShell"
date: 2026-10-10
lastmod: 2026-11-08
toc: true
draft: false
description: "Inventarie unidades organizacionais, usuários e computadores do Active Directory com consultas PowerShell delimitadas. Exporte arquivos CSV verificáveis sem alterar objetos do diretório."
genre: ["Active Directory", "PowerShell", "Administração de sistemas"]
tags: ["Inventário do Active Directory", "Inventário de AD com PowerShell", "Get-ADUser", "Get-ADComputer", "Get-ADOrganizationalUnit", "Get-ADDomain", "SearchBase", "AD somente para leitura", "Exportação de usuários de AD", "Exportação de computadores de AD", "Exportação de OU de AD", "Export-Csv", "RSAT", "Auditoria de diretório", "Relatórios de AD", "Inventário de OU", "Windows Server", "Script PowerShell", "Módulo AD", "Higiene do diretório"]
cover: "/img/cover/active-directory-powershell-read-only-inventory.webp"
coverAlt: "Árvore do Active Directory com registros de usuários, computadores e unidades organizacionais seguindo para três arquivos de revisão."
coverCaption: "Delimite a consulta e exporte somente os campos necessários para a revisão."
---
A limpeza do Active Directory começa com uma lista confiável dos objetos existentes. Este **inventário somente para leitura** reúne unidades organizacionais, usuários e computadores de um escopo escolhido. Ele exporta três arquivos CSV (valores separados por vírgula) para revisão sem alterar objetos do diretório. Ainda assim, proteja esses arquivos, pois nomes e detalhes dos dispositivos revelam parte do seu ambiente.

<!--more-->

## Principais pontos

- **Escolha um escopo:** consulte uma unidade organizacional antes de ampliar a consulta para todo o domínio.
- **Use comandos de leitura:** `Get-ADOrganizationalUnit`, `Get-ADUser` e `Get-ADComputer` recuperam objetos.
- **Selecione campos:** exporte somente as propriedades necessárias para a tarefa.
- **Confira o resultado:** compare a contagem e algumas linhas de exemplo antes de confiar no relatório.

## Antes de começar

Você precisa de um host de administração Windows com DNS funcional e acesso de rede a um controlador de domínio, do módulo PowerShell **ActiveDirectory**, de uma conta autorizada a ler os objetos escolhidos e de uma pasta protegida para os arquivos CSV. Em um cliente Windows, o módulo vem com as ferramentas do Active Directory dos Remote Server Administration Tools (RSAT). O [guia do módulo Active Directory](/articles/active-directory-module-powershell-installation-usage-guide/) explica a instalação. A Microsoft publica a [referência dos cmdlets](https://learn.microsoft.com/en-us/powershell/module/activedirectory/) do módulo e as [opções de instalação do RSAT](https://learn.microsoft.com/windows-server/remote/remote-server-administration-tools). Este guia usa a sintaxe do Windows PowerShell e não altera objetos do diretório.

As permissões do diretório continuam valendo. Na [orientação sobre contas privilegiadas](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/appendix-b--privileged-accounts-and-groups-in-active-directory), a Microsoft explica que listas de controle de acesso costumam permitir que usuários autenticados leiam informações gerais, mas restringem campos confidenciais e alterações. Comece com uma conta aprovada e uma OU de teste. Não eleve os privilégios a Domain Admin para fazer o inventário funcionar.

> **Aviso:** os arquivos CSV contêm nomes de contas e computadores. Salve-os em um local aprovado, limite o acesso e remova cópias extras após a revisão. Não publique uma exportação bruta nem a anexe a um issue público.

## Escolha a base de pesquisa

Uma **unidade organizacional (OU)** agrupa objetos do diretório. Seu **nome distinto (DN)** identifica sua posição na árvore do diretório. O parâmetro `-SearchBase` limita a consulta a um DN escolhido. Sem um escopo definido de propósito, um filtro amplo pode retornar muito mais objetos do que a revisão precisa.

Primeiro carregue o módulo e confira o DN do domínio atual:

```powershell
Import-Module ActiveDirectory
(Get-ADDomain).DistinguishedName
```

A Microsoft documenta [Get-ADDomain](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addomain) e as informações de domínio que o cmdlet retorna. Encontre a OU que você pretende revisar antes de definir a base de pesquisa:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase (Get-ADDomain).DistinguishedName |
    Select-Object Name, DistinguishedName
```

Copie o DN exato do resultado. Nos exemplos seguintes, substitua este valor de documentação pelo DN da sua OU:

```powershell
$SearchBase = 'OU=Lab,DC=example,DC=com'
```

`example.com` é um domínio de documentação. Não copie seu DN para uma consulta real. Se precisar intencionalmente de um inventário de todo o domínio, defina `$SearchBase` com o DN do domínio e registre esse escopo maior no relatório. A [referência de Get-ADOrganizationalUnit](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adorganizationalunit) da Microsoft documenta `-Filter` e `-SearchBase`.

## Inventarie OUs, usuários e computadores

Comece contando os objetos. Isso ajuda a identificar rapidamente uma base de pesquisa errada ou um resultado vazio inesperado:

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADUser -Filter * -SearchBase $SearchBase | Measure-Object
Get-ADComputer -Filter * -SearchBase $SearchBase | Measure-Object
```

`-Filter *` recupera todos os objetos correspondentes dentro da base de pesquisa. A Microsoft documenta [Get-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-aduser) e [Get-ADComputer](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer) como comandos de recuperação. Uma contagem zero pode estar correta, mas confira o DN, as permissões e o domínio de destino antes de considerar o inventário completo.

Agora visualize algumas linhas no console. Salve os campos selecionados para que a prévia e a exportação CSV posterior usem as mesmas colunas:

```powershell
$UserFields = 'Name', 'SamAccountName', 'Enabled', 'DistinguishedName'
Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields -First 10
```

Para computadores, solicite a propriedade extra do sistema operacional somente se a revisão precisar dela:

```powershell
$ComputerFields = @(
    'Name', 'DNSHostName', 'OperatingSystem',
    'Enabled', 'DistinguishedName'
)
Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields -First 10
```

O parâmetro `-Properties` solicita propriedades fora do conjunto padrão do cmdlet. A Microsoft o documenta na [referência do cmdlet de computadores](https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer). Trate nomes de sistemas operacionais como dados do diretório, não como prova da versão instalada atualmente. Um objeto de computador pode estar desatualizado ou seu atributo pode ainda não ter sido atualizado.

## Exporte arquivos CSV verificáveis

Escolha uma pasta de saída aprovada com espaço suficiente. Os comandos seguintes gravam **arquivos CSV locais** e não alteram objetos do diretório. Execute-os nessa pasta. `-NoClobber` impede a substituição de arquivos existentes. Use uma pasta ou um nome de arquivo novo em cada execução.

```powershell
Get-ADOrganizationalUnit -Filter * -SearchBase $SearchBase |
    Select-Object Name, DistinguishedName |
    Export-Csv -Path .\ad-ous.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADUser -Filter * -SearchBase $SearchBase |
    Select-Object -Property $UserFields |
    Export-Csv -Path .\ad-users.csv -NoTypeInformation -Encoding UTF8 -NoClobber

Get-ADComputer -Filter * -SearchBase $SearchBase -Properties OperatingSystem |
    Select-Object -Property $ComputerFields |
    Export-Csv -Path .\ad-computers.csv -NoTypeInformation -Encoding UTF8 -NoClobber
```

A [referência de Export-Csv](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/export-csv?view=powershell-5.1) da Microsoft explica `-NoTypeInformation`, `-Encoding` e `-NoClobber`. Abra cada CSV em um editor de texto ou planilha aprovada. Confira o cabeçalho, algumas linhas e a contagem de registros em comparação com a contagem anterior. Um comando com falha ou um arquivo de zero bytes não comprova que o relatório está completo.

> **Resultado esperado:** você tem três arquivos CSV com registros de OUs, usuários e computadores do escopo escolhido. A quantidade de linhas e os valores de amostra correspondem ao escopo selecionado do diretório.

## Revise sem alterar objetos

Use o inventário para responder perguntas específicas: qual OU responde por um computador? Quais contas de usuário estão desativadas? Quais nomes de dispositivos precisam de um responsável? Registre as conclusões em uma nota de revisão separada. Não use o valor `Enabled` para concluir se uma conta ainda é necessária. Não exclua nem desative objetos com base apenas em uma exportação.

Em relatórios recorrentes, registre a data da consulta, o domínio, o DN da OU, as propriedades selecionadas, o operador e o local do CSV. Ao comparar duas exportações, confirme que ambas usaram o mesmo escopo e os mesmos campos. Caso contrário, a diferença pode vir da consulta, e não de uma mudança real no diretório.

Isto é um **inventário**, não uma auditoria de contas privilegiadas nem um relatório de atividade de login. A Microsoft observa que propriedades e permissões do Active Directory variam conforme o objeto e o ambiente. Verifique com o responsável pelo sistema um atributo de sistema operacional ou nome de exibição antes de agir. O [guia de segurança do Active Directory](/articles/active-directory-security-best-practices/) aborda controles mais amplos.

## Solução de problemas

- **O módulo não importa:** confirme que as ferramentas do Active Directory do RSAT ou as ferramentas de administração do Windows Server estão instaladas no host. Siga o [guia de configuração do módulo](/articles/active-directory-module-powershell-installation-usage-guide/).
- **A consulta não retorna objetos:** confira o DN exato, o domínio atual, o conteúdo da OU e as permissões de leitura. Teste primeiro uma OU pequena conhecida antes de ampliar o escopo.
- **Uma propriedade está vazia:** confirme que o atributo existe e que sua conta pode lê-lo. Não preencha campos ausentes com suposições.
- **A exportação informa que o arquivo já existe:** `-NoClobber` protegeu o relatório anterior. Escolha um novo nome de arquivo ou pasta e execute novamente.
- **A contagem difere do esperado:** confira se usuários ou computadores estão em outra OU, se o escopo mudou e se o diretório foi alterado durante a consulta.

## Próximos passos

Mantenha os arquivos CSV brutos em um local protegido durante o período de revisão acordado. Compartilhe somente os campos necessários ao revisor. Depois que os responsáveis confirmarem as conclusões, planeje as mudanças conforme o processo habitual de aprovação e reversão. Após as mudanças aprovadas, execute novamente o mesmo inventário no mesmo escopo para confirmar o resultado.
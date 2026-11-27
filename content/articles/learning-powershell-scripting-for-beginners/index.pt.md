---
title: "Scripts em PowerShell"
draft: false
toc: true
date: 2023-02-25
lastmod: 2026-11-27
description: "Aprenda os fundamentos de scripts em PowerShell e automatize tarefas com este guia passo a passo para iniciantes, que aborda cmdlets, loops, funções e muito mais."
genre: ["Tecnologia", "Programação", "Automação", "Windows", "Scripts", "TI", "Tarefas administrativas", "Gerenciamento de computadores", "Desenvolvimento de software", "Codificação"]
tags: ["scripts em PowerShell", "automação com PowerShell", "scripts para Windows", "cmdlets do PowerShell", "módulos do PowerShell", "loops do PowerShell", "instruções condicionais do PowerShell", "funções do PowerShell", "boas práticas de PowerShell", "depuração do PowerShell", "testes do PowerShell", "variáveis do PowerShell", "PowerShell ISE", "PowerShell Remoting", "tecnologias Microsoft", "automação de TI", "gerenciamento de computadores", "programação para iniciantes", "tarefas administrativas", "ideias de scripts em PowerShell", "backups automatizados", "gerenciamento de arquivos", "informações do sistema", "gerenciamento de usuários", "instalação de software", "configuração de rede", "automação de segurança", "agendamento de tarefas", "manipulação do Registro", "administração remota"]
cover: "/img/cover/A_cartoon_character_holding_a_script_and_standing.webp"
coverAlt: "Personagem de desenho segurando um script diante de um computador com o prompt do PowerShell, mostrando que iniciantes podem aprender a criar scripts com facilidade"
coverCaption: ""
---
**Aprenda scripts em PowerShell: um guia para iniciantes**

PowerShell é um shell de linha de comando e uma linguagem de scripts desenvolvidos pela Microsoft. Ele oferece uma ampla variedade de comandos e recursos para gerenciar e automatizar diferentes aspectos do Windows e de outras tecnologias Microsoft. Neste artigo, apresentamos os fundamentos dos scripts em PowerShell e um guia passo a passo para você começar.

## Introdução ao PowerShell

**PowerShell** é um shell de linha de comando que permite automatizar e gerenciar o Windows e outras tecnologias Microsoft. Ele oferece um conjunto abrangente de comandos e recursos para realizar diversas tarefas administrativas, como gerenciar arquivos e diretórios, configurar redes e administrar o sistema. O PowerShell também inclui uma linguagem de scripts que permite criar scripts complexos e automatizar tarefas repetitivas.

## Começando com PowerShell

### Instalando o PowerShell

O PowerShell já vem instalado na maioria das versões do Windows. Se você usa uma versão antiga do Windows ou precisa de uma versão mais recente do PowerShell, baixe-a no site da Microsoft. Para baixar e instalar o PowerShell, siga estas etapas:

1. Acesse o [site do Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.2) e escolha a versão que deseja instalar.
2. Baixe e execute o arquivo de instalação.
3. Siga as instruções na tela para concluir a instalação.

### Iniciando o PowerShell

Depois de instalar o PowerShell, inicie-o seguindo estas etapas:

1. Abra o menu Iniciar e digite "PowerShell" na barra de pesquisa.
2. Selecione "Windows PowerShell" nos resultados da pesquisa.
3. O PowerShell será aberto em uma nova janela.

### Scripts em PowerShell no Visual Studio Code

Para ter uma experiência de criação de scripts mais completa, use o Visual Studio Code (VS Code), um ambiente de desenvolvimento integrado (IDE) popular. O VS Code oferece realce de sintaxe, preenchimento de código, depuração e suporte a um terminal integrado, sendo uma boa opção para scripts em PowerShell. Para começar no VS Code, siga estas etapas:

1. Instale o Visual Studio Code pelo [site oficial](https://code.visualstudio.com/).
2. No marketplace de extensões do VS Code, instale a extensão "PowerShell" da Microsoft.
3. Abra um arquivo de script do PowerShell (.ps1) no VS Code e comece a programar.

### PowerShell para administração de sistemas

O PowerShell é uma ferramenta versátil para tarefas de administração de sistemas. De comandos simples a fluxos de automação complexos, ele facilita tarefas que exigiriam intervenção manual. A plataforma de scripts funciona em Windows, Linux e macOS e oferece aos administradores um conjunto de ferramentas consistente para gerenciar diferentes ambientes.

### Do Prompt de Comando ao Windows PowerShell

Se você conhece o Prompt de Comando e quer migrar para o Windows PowerShell, a transição tende a ser simples. Os scripts do Windows PowerShell usam conceitos do Prompt de Comando e acrescentam recursos mais avançados. Aproveite o que já sabe e explore gradualmente os recursos adicionais e os cmdlets do PowerShell.

### Fundamentos do PowerShell

O PowerShell oferece uma interface de linha de comando para interagir com o sistema operacional. Seus comandos são chamados de cmdlets e se organizam em módulos. Para ver os módulos disponíveis, use o comando Get-Module:

```powershell
Get-Module
```

Para ver os cmdlets disponíveis em um módulo, use Get-Command:
```powershell
Get-Command -Module <module name>
```

Para consultar a ajuda de um cmdlet, use Get-Help:
```powershell
Get-Help <cmdlet name>
```

O PowerShell também oferece aliases, nomes curtos para cmdlets. Para ver os aliases disponíveis, use Get-Alias:
```powershell
Get-Alias
```

## Arquivos de script e política de execução

Os arquivos de script do PowerShell usam a extensão .ps1. Antes de executar scripts, talvez seja necessário definir a política de execução, que determina se scripts podem ser executados e quais tipos são permitidos. Para definir essa política, use o cmdlet Set-ExecutionPolicy. Por exemplo, para permitir a execução de scripts, use:

```powershell
Set-ExecutionPolicy RemoteSigned
```

ou (somente para testes)

```powershell
Set-ExecutionPolicy Undefined
```

### Criando scripts em PowerShell

Os scripts do PowerShell permitem automatizar diversas tarefas administrativas. Eles aceitam variáveis, loops, instruções condicionais e funções, o que torna o PowerShell uma ferramenta útil para automação.

#### Variáveis

As variáveis armazenam dados em scripts do PowerShell. Seus nomes começam com o cifrão ($). Para atribuir um valor a uma variável, use esta sintaxe:
```powershell
$variable_name = value
```
Por exemplo:
```powershell
$name = "John"
```
#### Loops

Os loops repetem um bloco de código um número determinado de vezes. O PowerShell oferece os seguintes tipos:

- **Loop For**: repete um bloco de código um número específico de vezes.
- **Loop While**: repete um bloco enquanto uma condição for verdadeira.
- **Loop Do-While**: executa um bloco pelo menos uma vez e continua enquanto uma condição for verdadeira.
- **Loop ForEach**: repete um bloco para cada item de uma coleção.

Por exemplo, o código a seguir usa um loop For para imprimir os números de 1 a 5:
```powershell
for($i=1; $i -le 5; $i++) {
Write-Host $i
}
```

#### Instruções condicionais

Instruções condicionais

As instruções condicionais executam um bloco de código quando determinada condição é verdadeira. O PowerShell oferece estes tipos:

- **Instrução If**: executa um bloco se uma condição for verdadeira.
- **Instrução If-Else**: executa um bloco se a condição for verdadeira e outro se for falsa.
- **Instrução Switch**: compara um valor com várias correspondências possíveis e executa o bloco da primeira correspondência.

Por exemplo, o código a seguir usa If para verificar se um número é maior que 5:

```powershell
$number = 10
if ($number -gt 5) {
    Write-Host "O número é maior que 5"
}
```
#### Funções

Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas recebem parâmetros de entrada e retornam valores. O PowerShell oferece estes tipos de função:

- **Bloco de script**: um bloco de código que pode ser executado.
- **Função avançada**: uma função com metadados e validação de parâmetros.

Por exemplo, o código a seguir define uma função que soma dois números:
```powershell
function Add-Numbers {
    param (
        [int]$num1,
        [int]$num2
    )
    $result = $num1 + $num2
    return $result
}

$result = Add-Numbers -num1 5 -num2 10
Write-Host "O resultado é $result"
```
### PowerShell ISE

PowerShell ISE (ambiente integrado de scripts) é uma interface gráfica para criar scripts em PowerShell. Ele oferece um editor de texto avançado, ferramentas de depuração e outros recursos que facilitam a criação e o teste de scripts. Para abrir o PowerShell ISE, siga estas etapas:

1. Abra o menu Iniciar e digite "PowerShell ISE" na barra de pesquisa.
2. Selecione "Windows PowerShell ISE" nos resultados.
3. O PowerShell ISE será aberto em uma nova janela.

### PowerShell Remoting

O PowerShell Remoting permite executar comandos e scripts do PowerShell em computadores remotos. O recurso exige que o serviço WinRM esteja em execução no computador local e no remoto. Para habilitar o PowerShell Remoting, siga estas etapas:

1. Abra um prompt do PowerShell com privilégios de administrador.
2. Execute o comando a seguir para habilitar o PowerShell Remoting:
```powershell
   Enable-PSRemoting -Force
```
3. Execute este comando para adicionar o computador remoto à lista TrustedHosts:
```powershell
Set-Item wsman:\localhost\Client\TrustedHosts -Value <computer name> -Force
```
4. Reinicie o serviço WinRM.
```powershell
Restart-Service WinRM
```

Para executar um comando do PowerShell em um computador remoto, use o cmdlet Invoke-Command:
```powershell
Invoke-Command -ComputerName <computer name> -ScriptBlock { <command> }
```
### Módulos do PowerShell

Os módulos do PowerShell reúnem cmdlets, funções e scripts criados para tarefas específicas. Você pode instalar e gerenciar módulos pelo PowerShell Gallery, um repositório central de módulos do PowerShell.

Para instalar um módulo do PowerShell Gallery, use:
```powershell
Install-Module <module name>
```

Para ver os módulos do PowerShell instalados, use Get-InstalledModule:
```powershell
Get-InstalledModule
```

### Boas práticas para scripts em PowerShell

Ao escrever **scripts em PowerShell**, siga boas práticas para mantê-los **seguros**, **confiáveis** e **fáceis de manter**. Considere estas recomendações:

- **Use nomes descritivos para variáveis**: escolha nomes que indiquem claramente a finalidade de cada variável.
- **Use comentários**: explique a finalidade do código.
- **Trate erros**: lide com erros e exceções de forma adequada. A estrutura `Try...Catch...Finally` do PowerShell permite tratar exceções e tomar as medidas apropriadas. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-try-catch-finally?view=powershell-7.1)
- **Teste os scripts por completo**: verifique se funcionam como esperado. Use **Pester**, uma estrutura de testes para PowerShell, para escrever e executar testes de unidade. [Documentação do Pester](https://pester.dev/)
- **Use funções e módulos**: organize o código e facilite a reutilização. As funções dividem o código em partes menores e gerenciáveis; os módulos permitem empacotar e distribuir esse código. [Sobre funções](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-functions?view=powershell-7.1), [Sobre módulos](https://docs.microsoft.com/en-us/powershell/scripting/learn/deep-dives/everything-about-modules?view=powershell-7.1)
- **Evite valores fixos no código**: prefira parâmetros ou variáveis. Assim, seus scripts ficam mais flexíveis e reutilizáveis. Passe parâmetros aos scripts com a palavra-chave `param`. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_functions_advanced_parameters?view=powershell-7.1)
- **Use saída detalhada**: forneça informações adicionais sobre o andamento do script. O cmdlet `Write-Verbose` exibe mensagens detalhadas durante a execução. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/write-verbose?view=powershell-7.1)

### Explicação das boas práticas para scripts em PowerShell

#### Trate erros

O tratamento de erros é essencial para que um script lide adequadamente com erros e exceções. O PowerShell oferece várias opções, como as instruções Try-Catch e Trap e o parâmetro ErrorAction. Try-Catch captura e trata exceções; Trap captura e trata erros; ErrorAction controla como o script reage aos erros.

Veja um exemplo de Try-Catch para tratar um erro:
```powershell
try {
    # código que pode gerar um erro
}
catch {
    Write-Error "Ocorreu um erro: $_"
}
```

#### Teste os scripts por completo

Testar scripts do PowerShell é essencial para confirmar que funcionam como esperado. Ferramentas e estruturas de teste, como Pester, permitem escrever e executar testes. Elas ajudam a localizar e isolar problemas no código e a verificar se o script atende aos requisitos.

Veja um exemplo de uso do Pester para testar um script do PowerShell:
```powershell
Describe "My PowerShell Script" {
    It "Does something" {
        # código que deve retornar o resultado esperado
        $result = Do-Something
        $result | Should -Be "expected result"
    }
}
```

#### Use funções e módulos

Funções e módulos ajudam a organizar o código e reutilizá-lo. As funções agrupam o código em blocos reutilizáveis; os módulos empacotam e compartilham código. Com eles, os scripts ficam mais modulares, eficientes e fáceis de manter.

Veja um exemplo de função em PowerShell:
```powershell
function Get-ProcessCount {
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount
Write-Host "Há $count processos em execução."
```

#### Evite valores fixos no código

Valores fixos reduzem a flexibilidade e dificultam a manutenção de um script em PowerShell. Em vez disso, use parâmetros ou variáveis para que o usuário possa fornecer valores durante a execução. Isso torna o script mais reutilizável e adaptável.

Veja um exemplo de parâmetro em PowerShell:
```powershell
param (
    [string]$name
)

Write-Host "Olá, $name!"
```

#### Use saída detalhada

A saída detalhada fornece informações adicionais sobre o andamento de um script e ajuda na depuração e na solução de problemas. O cmdlet Write-Verbose envia informações detalhadas ao console, tornando os scripts mais informativos e fáceis de depurar.

Veja um exemplo de saída detalhada em PowerShell:
```powershell
function Get-ProcessCount {
    Write-Verbose "Getting processes..."
    $processes = Get-Process
    $count = $processes.Count
    return $count
}

$count = Get-ProcessCount -Verbose
Write-Host "Há $count processos em execução."
```

### Dez ideias de scripts em PowerShell para iniciantes

Se você está começando a criar scripts em PowerShell, experimente estas dez ideias:

- **Backups automatizados**: crie um script para fazer backup de arquivos e diretórios importantes em um disco rígido externo ou serviço de armazenamento em nuvem. Use o cmdlet `Copy-Item` para copiar arquivos e `Start-Job` para executar o backup em segundo plano. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/copy-item?view=powershell-7.1)

- **Gerenciamento de arquivos**: crie um script para organizar arquivos e diretórios em pastas conforme o tipo, tamanho ou outro critério. Use `Get-ChildItem` para localizar arquivos e `Move-Item` para movê-los ao local desejado. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem?view=powershell-7.1), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/move-item?view=powershell-7.1)

- **Informações do sistema**: crie um script que obtenha dados como uso da CPU e memória, espaço em disco e configurações de rede, exibindo-os em formato legível. Use `Get-WmiObject` para coletar informações e `Format-Table` ou `Out-GridView` para formatá-las. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-7.1)

- **Gerenciamento de usuários**: crie um script para adicionar, alterar ou remover usuários e grupos locais do Windows. Use `New-LocalUser`, `Set-LocalUser` e `Remove-LocalUser` para usuários e `New-LocalGroup`, `Add-LocalGroupMember` e `Remove-LocalGroup` para grupos. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localuser?view=powershell-7.1), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.localaccounts/new-localgroup?view=powershell-7.1)

- **Instalação de software**: crie um script que instale e configure software em vários computadores ao mesmo tempo, economizando tempo e esforço. Use `Invoke-Command` para executar comandos de instalação em computadores remotos. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

- **Configuração de rede**: crie um script para configurar endereços IP, máscaras de sub-rede e gateways padrão. Use `Set-NetIPAddress`, `Set-NetIPInterface` e `Set-DnsClientServerAddress` para ajustar as configurações de rede. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipaddress?view=win10-ps), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/nettcpip/set-netipinterface?view=win10-ps), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/dnsclient/set-dnsclientserveraddress?view=win10-ps)

- **Segurança**: crie um script para auditar e monitorar configurações de segurança e alertar quando detectar alterações. Use `Get-AuditPolicy` para obter políticas de auditoria e `Send-MailMessage` para enviar notificações por e-mail. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-auditpolicy?view=powershell-7.1), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/send-mailmessage?view=powershell-7.1)

- **Agendamento de tarefas**: crie um script para agendar e automatizar tarefas recorrentes, como backups, atualizações e verificações do sistema. Use `Register-ScheduledTask` para criar tarefas agendadas e `Start-ScheduledTask` para executá-las. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask?view=win10-ps), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/scheduledtasks/start-scheduledtask?view=win10-ps)

- **Manipulação do Registro**: crie um script para modificar ou consultar valores de chaves específicas do Registro. Use `Get-ItemProperty` e `Set-ItemProperty` para interagir com o Registro. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-itemproperty?view=powershell-7.1), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.management/set-itemproperty?view=powershell-7.1)

- **Administração remota**: crie um script para habilitar a administração remota de computadores Windows e permitir a execução de comandos e scripts em máquinas remotas. Use `Enter-PSSession` ou `Invoke-Command` para executar comandos em computadores remotos. [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enter-pssession?view=powershell-7.1), [Documentação da Microsoft](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/invoke-command?view=powershell-7.1)

Explore essas ideias para ganhar experiência prática e ampliar seus conhecimentos sobre scripts em PowerShell.

## Conclusão

O PowerShell é uma ferramenta poderosa para gerenciar e automatizar o Windows e outras tecnologias Microsoft. Neste artigo, vimos os fundamentos dos scripts para iniciantes: instalação e inicialização, uso de cmdlets, variáveis, loops, instruções condicionais e funções, além do PowerShell ISE, do PowerShell Remoting e dos módulos. Boas práticas ajudam a criar scripts seguros, confiáveis e fáceis de manter. Com prática, você poderá dominar o PowerShell e automatizar diversas tarefas administrativas.

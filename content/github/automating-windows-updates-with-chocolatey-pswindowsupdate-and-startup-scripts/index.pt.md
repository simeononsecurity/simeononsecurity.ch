---
title: "Simplifique as atualizações do Windows com automação usando Chocolatey, PSWindowsUpdate e scripts de inicialização"
date: 2020-07-22
---
 Atualizações do Windows com Chocolatey, PSWindowsUpdate e scripts de inicialização**

No ambiente de negócios acelerado de hoje, o tempo é essencial para os administradores de sistema. A atualização de máquinas Windows, um aspecto crítico da administração de sistemas, pode ser uma tarefa extremamente demorada que pode levar até uma semana, considerando sistemas suficientes. No entanto, com alguma ajuda de Chocolatey, PSWindowsUpdates e Scripts de inicialização, agora é possível distribuir atualizações com apenas uma única reinicialização de cada máquina, reduzindo significativamente o tempo necessário para executar atualizações.

## Simplificando atualizações do Windows com automação

As atualizações do Windows são essenciais para manter a estabilidade e a segurança das máquinas Windows. A execução de atualizações em um grande número de máquinas pode ser uma tarefa demorada, especialmente para administradores de sistema com recursos limitados. No entanto, com o uso de ferramentas de automação como Chocolatey, PSWindowsUpdate e Scripts de inicialização, esse processo pode ser simplificado para permitir que os administradores executem atualizações com o mínimo de esforço.

### Chocolate

[Chocolatey](https://chocolatey.org/) é um gerenciador de pacotes para Windows que pode ser usado para automatizar a instalação de software em máquinas Windows. É semelhante ao apt-get no Ubuntu ou homebrew no macOS e pode ser usado para instalar e gerenciar uma ampla gama de pacotes de software. O Chocolatey pode ser usado para instalar pacotes silenciosamente, o que significa que eles podem ser instalados sem a intervenção do usuário.

###PSWindowsUpdate

[PSWindowsUpdate](https://www.powershellgallery.com/packages/PSWindowsUpdate/2.0.0.4) é um módulo do PowerShell que pode ser usado para automatizar a instalação de atualizações do Windows. Ele fornece cmdlets que podem ser usados para instalar, desinstalar e listar as atualizações do Windows. O PSWindowsUpdate é uma ferramenta poderosa que pode ser usada para gerenciar atualizações do Windows em várias máquinas, tornando-o ideal para administradores de sistema que precisam gerenciar um grande número de máquinas.

### Scripts de inicialização

[Startup Scripts](https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn789190(v=ws.11)) são scripts que podem ser usados para automatizar tarefas que precisam ser executadas quando uma máquina é inicializada ou desligada. Esses scripts podem ser usados para executar tarefas como instalar software, definir configurações e gerenciar atualizações do Windows.

## Automatizando atualizações do Windows com uma única reinicialização

Para automatizar as atualizações do Windows usando Chocolatey, PSWindowsUpdate e Scripts de inicialização, os administradores podem seguir o guia passo a passo abaixo.

### Configurando o script de desligamento
Baixe todos os arquivos de suporte do[GitHub Repository](https://github.com/simeononsecurity/ChocoAutomateWindowsUpdates)

1. Abra o Editor de Diretiva de Grupo Local pressionando **"Win + R"** e digitando **"gpedit.msc"** seguido de **"Ctrl + Shift + Enter"**.
2. Navegue até Computador **Configuração\Configurações do Windows\Scripts (Inicialização/Desligamento)**.
3. No painel de resultados, clique duas vezes em Desligar.
4. Selecione a guia PowerShell.
5. Na caixa de diálogo Propriedades de desligamento, clique em Adicionar.
6. Na caixa Nome do script, digite o caminho para o script ou clique em Procurar para pesquisar "*chocoautomatewindowsupdates.ps1*" na pasta compartilhada Netlogon no controlador de domínio.
7. Reinicie.

Agora, tudo o que um administrador precisa fazer é reiniciar o computador para executar as atualizações do Windows.

### Entendendo o roteiro

O script usado para automatizar as atualizações do Windows é intitulado "*chocoautomatewindowsupdates.ps1*". Ele executa as seguintes tarefas:

1. Instala o gerenciador de pacotes Chocolatey.
2. Ativa algumas alterações de configuração preferidas do Chocolatey.
3. Atualiza todos os pacotes Chocolatey instalados.
4. Instala o módulo PowerShell PSWindowsUpdate.
5. Adiciona o gerenciador de serviços do Windows Update.
6. Instala todas as atualizações disponíveis do Windows.
7. Instala quaisquer drivers ausentes ou atualizações exigidas por atualizações instaladas anteriormente.

### Benefícios de automatizar as atualizações do Windows

Automatizar as atualizações do Windows usando Chocolatey, PSWindowsUpdate e scripts de inicialização traz vários benefícios para os administradores de sistema. Esses benefícios incluem:

- **Economia de tempo**: automatizar as atualizações do Windows reduz significativamente o tempo necessário para executar as atualizações. Os administradores não precisam mais instalar atualizações manualmente em cada máquina.
- **Consistência**: automatizar as atualizações do Windows garante que as atualizações sejam instaladas de forma consistente em todas as máquinas. Isso reduz a probabilidade de erros e vulnerabilidades de segurança.
- **Gerenciamento centralizado**: automatizar as atualizações do Windows permite que os administradores gerenciem as atualizações a partir de um local central, facilitando o controle de quais atualizações foram instaladas e quais máquinas precisam de atualizações.
- **Aumento da segurança**: automatizar as atualizações do Windows garante que as máquinas sejam mantidas atualizadas com os patches de segurança mais recentes, reduzindo o risco de violações de segurança.

### Conclusão

Automatizar atualizações do Windows usando Chocolatey, PSWindowsUpdate e scripts de inicialização é uma ferramenta poderosa que pode economizar muito tempo e esforço dos administradores de sistema. Ele permite que as atualizações sejam instaladas de forma consistente e eficiente, garantindo que as máquinas estejam atualizadas com os patches de segurança mais recentes. Seguindo as etapas descritas neste tutorial, os administradores podem automatizar as atualizações do Windows com apenas uma única reinicialização, tornando o processo de atualização de máquinas Windows muito mais rápido e fácil.

---
title: "Comandos do Windows Defender PowerShell para a segurança do sistema"
date: 2023-07-27
lastmod: 2026-11-20
toc: true
draft: false
description: "Conheça os comandos do Windows Defender PowerShell e melhore a segurança do sistema com o controle pela linha de comando."
genre: ["Windows Defender", "comandos PowerShell", "segurança do sistema", "controle pela linha de comando", "antivírus", "sistemas operacionais Windows", "proteção contra malware", "configurações avançadas de segurança", "automação de operações de segurança", "Windows PowerShell"]
tags: ["Tecnologia", "Cibersegurança", "Sistemas operacionais", "Windows", "Ferramentas de linha de comando", "Segurança do sistema", "PowerShell", "Antivírus", "Proteção contra malware", "Scripts"]
cover: "/img/cover/An_animated_illustration_depicting_a_shield_pr.webp"
coverAlt: "Ilustração animada de um escudo protegendo um sistema de computador contra várias ameaças cibernéticas."
coverCaption: "Melhore a segurança do sistema com os comandos do Windows Defender PowerShell."
---

## Introdução

Desenvolvido pela Microsoft, o Windows Defender é uma **solução integrada de antivírus e segurança** para sistemas operacionais Windows. Ele oferece uma interface simples para gerenciar as configurações de segurança. Usuários avançados que preferem o controle pela linha de comando também dispõem de vários comandos PowerShell. Este artigo apresenta os **comandos do Windows Defender PowerShell** e explica como eles ajudam a melhorar a segurança e o controle do ambiente Windows.

## Recursos dos comandos do Windows Defender PowerShell

Os comandos do Windows Defender PowerShell permitem executar **operações avançadas de segurança** pela linha de comando. Eles oferecem desde a verificação de malware até a configuração de opções avançadas de segurança. Com o PowerShell, você pode automatizar operações de segurança, criar scripts personalizados e integrar o Windows Defender aos fluxos de trabalho existentes.

## Como começar a usar o Windows Defender PowerShell

Para usar os comandos do Windows Defender PowerShell, abra uma sessão do PowerShell com **privilégios de administrador**. Siga estas etapas:

1. Pressione `Win + X` e selecione **Windows PowerShell (Admin)** (como administrador) no menu.
2. Se solicitado, clique em **Yes** (Sim) para permitir que o aplicativo faça alterações no dispositivo.

Com a sessão do PowerShell aberta, você pode começar a usar os comandos do Windows Defender PowerShell.

## Comandos comuns do Windows Defender PowerShell

### 1. **Get-MpComputerStatus**: verificar o status do Windows Defender

O comando `Get-MpComputerStatus` apresenta o status atual do Windows Defender no sistema, incluindo a versão do mecanismo antivírus, o horário da última verificação e o status da proteção em tempo real. Execute-o para avaliar rapidamente a integridade do Windows Defender e confirmar que está funcionando corretamente.

Para verificar o status do Windows Defender, abra uma sessão do PowerShell com privilégios de administrador e execute:

```powershell
Get-MpComputerStatus
```

O comando exibe informações como:

- **AntivirusEngineVersion**: número da versão do mecanismo antivírus usado pelo Windows Defender.
- **LastFullScanTime**: data e horário da última **verificação completa** do Windows Defender.
- **LastQuickScanTime**: data e horário da última verificação rápida do Windows Defender.
- **RealTimeProtectionEnabled**: indica se a proteção em tempo real está ativada ou desativada.

Acompanhar regularmente o status com `Get-MpComputerStatus` ajuda você a conhecer o nível de proteção do sistema contra **possíveis ameaças**.

### 2. [**Update-MpSignature**](https://learn.microsoft.com/en-us/powershell/module/defender/update-mpsignature?view=windowsserver2022-ps)

O comando `Update-MpSignature` permite atualizar manualmente as assinaturas antivírus usadas pelo Windows Defender. Elas contêm informações essenciais sobre malware conhecido e ajudam o Windows Defender a detectar e bloquear ameaças. Execute o comando para obter as assinaturas mais recentes e proteger o sistema contra novas ameaças.

Para atualizar manualmente as assinaturas do Windows Defender, abra uma sessão do PowerShell com privilégios de administrador e execute:

```powershell
Update-MpSignature
```

O comando inicia a atualização. O Windows Defender se conecta aos servidores da Microsoft para baixar as **assinaturas antivírus mais recentes**. Após a atualização, o Windows Defender dispõe de informações atuais sobre malware conhecido, o que ajuda a identificar e remover ameaças.

Manter as assinaturas atualizadas é essencial diante da evolução do malware e das ameaças cibernéticas. Execute `Update-MpSignature` regularmente para que o Windows Defender proteja o sistema com eficiência.

### 3. [**Set-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/set-mppreference?view=windowsserver2022-ps)

O comando `Set-MpPreference` permite personalizar várias configurações do **Windows Defender** conforme seus requisitos de segurança. Ele oferece opções como **proteção em tempo real**, **proteção baseada na nuvem** e **configurações do sistema de inspeção de rede**.

Por exemplo, você pode ativar ou desativar a proteção em tempo real com `Set-MpPreference`. Essa proteção monitora o sistema em busca de atividades maliciosas e responde imediatamente às ameaças. Para ativá-la, execute:

```powershell
Set-MpPreference -DisableRealtimeMonitoring:$false
```

Você também pode ajustar a proteção baseada na nuvem. Ela usa **recursos da nuvem** para melhorar a detecção de ameaças e responder mais rapidamente às novas ameaças. Para ativá-la, execute:

```powershell
Set-MpPreference -EnableCloudProtection:$true
```

Além disso, `Set-MpPreference` permite personalizar as configurações do sistema de inspeção de rede. Esse sistema analisa o tráfego de rede em busca de atividades suspeitas e possíveis ameaças. Para ajustar suas configurações, execute:

```powershell
Set-MpPreference -DisableIOAVProtection:$false
```

Ajuste essas opções com `Set-MpPreference` para adequar o **Windows Defender** às suas necessidades de segurança e proteger o sistema contra malware e outras atividades maliciosas.

### 4. [**Start-MpScan**](https://learn.microsoft.com/en-us/powershell/module/defender/start-mpscan?view=windowsserver2022-ps)

O comando `Start-MpScan` inicia verificações de malware no sistema para ajudar você a identificar e remover arquivos maliciosos. Ele oferece vários tipos de verificação, incluindo **rápida**, **completa** e **personalizada** para caminhos específicos.

Para executar uma **verificação rápida** com `Start-MpScan`, use este comando do PowerShell:

```powershell
Start-MpScan -ScanType QuickScan
```

A verificação rápida examina áreas importantes do sistema onde o malware costuma aparecer e avalia rapidamente possíveis ameaças.

Para examinar todos os arquivos e diretórios do sistema, inicie uma **verificação completa** com `Start-MpScan`:

```powershell
Start-MpScan -ScanType FullScan
```

A verificação completa procura malware em todo o sistema, mas pode levar mais tempo do que a verificação rápida.

Além dos tipos predefinidos, `Start-MpScan` permite verificar caminhos ou arquivos específicos. Por exemplo, para verificar um diretório específico, execute:

```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Directory"
```

Esse comando inicia uma verificação personalizada no diretório indicado e direciona a busca de malware a uma área específica do sistema.

Use os recursos de `Start-MpScan` para agendar verificações, automatizar processos de segurança e detectar e tratar malware regularmente.

### 5. [**Get-MpThreatCatalog**](https://learn.microsoft.com/en-us/powershell/module/defender/get-mpthreatcatalog?view=windowsserver2022-ps)

O comando `Get-MpThreatCatalog` fornece informações detalhadas sobre ameaças conhecidas e seus atributos. Ele apresenta um catálogo abrangente, incluindo gravidade, nomes de arquivos associados e ações recomendadas para mitigação.

Para recuperar informações sobre ameaças específicas com `Get-MpThreatCatalog`, siga estas etapas:

1. Abra uma sessão do PowerShell com privilégios de administrador.
2. Execute o comando a seguir:

```powershell
   Get-MpThreatCatalog
```

O comando exibe uma lista de ameaças conhecidas e seus detalhes correspondentes.

A saída do `Get-MpThreatCatalog` inclui informações essenciais, como:

- **ThreatID**: identificador exclusivo da ameaça.
- **Severity**: nível de gravidade da ameaça, de Low (baixo) a Severe (severo).
- **Name**: nome ou descrição da ameaça.
- **Path**: caminho do arquivo associado à ameaça.
- **RecommendedAction**: orientação sobre a ação recomendada para mitigar a ameaça.

As informações de `Get-MpThreatCatalog` ajudam você a compreender possíveis ameaças e decidir como tratá-las. Seja para isolar, remover ou monitorar uma ameaça específica, o catálogo detalhado ajuda a responder a incidentes de segurança com eficiência.

Para saber mais sobre como usar `Get-MpThreatCatalog` e interpretar os resultados, consulte a documentação oficial da Microsoft.

Mantenha-se alerta e execute `Get-MpThreatCatalog` regularmente para acompanhar a evolução das ameaças e melhorar a segurança do sistema.

### 6. [**Add-MpPreference**](https://learn.microsoft.com/en-us/powershell/module/defender/add-mppreference?view=windowsserver2022-ps)

O comando `Add-MpPreference` permite adicionar exclusões ao Windows Defender e personalizar o comportamento das verificações e da proteção em tempo real. Com as exclusões, você especifica arquivos, pastas ou processos que o Windows Defender deve ignorar durante as verificações de segurança ou a proteção em tempo real.

Para adicionar uma exclusão com `Add-MpPreference`, informe o caminho ou o nome do arquivo, pasta ou processo que deseja excluir. Este exemplo adiciona a exclusão de uma pasta:

```powershell
Add-MpPreference -ExclusionPath "C:\MyFolder"
```

Esse comando faz com que o Windows Defender ignore a pasta indicada, reduzindo alertas desnecessários e possíveis interrupções do fluxo de trabalho.

As exclusões podem ser úteis para ignorar aplicativos confiáveis, ambientes de desenvolvimento ou arquivos específicos que gerem falsos positivos. Use `Add-MpPreference` para ajustar o Windows Defender às suas necessidades de segurança e otimizar seu desempenho.

Proteja o sistema e reduza falsos positivos e interrupções desnecessárias de verificação com os recursos de exclusão do `Add-MpPreference`.

## Verificações dos comandos do Defender em 2026

Execute os comandos do Defender em uma sessão com privilégios elevados somente quando a tarefa exigir elevação. Antes de usar um parâmetro, consulte a ajuda atual do módulo para a versão do Windows de destino. Registre a configuração atual, altere uma opção por vez, verifique o resultado e anote o comando para reverter a alteração.

As verificações úteis incluem o status da proteção, a idade das assinaturas, as exclusões, as preferências, o histórico de verificações e as detecções recentes. Mantenha as exclusões específicas e registre o responsável e a data de validade. Consulte a [documentação do módulo PowerShell do Microsoft Defender](https://learn.microsoft.com/en-us/powershell/module/defender/) e a [documentação do Microsoft Defender Antivirus](https://learn.microsoft.com/en-us/defender-endpoint/microsoft-defender-antivirus-windows) para ver os cmdlets e o comportamento atuais.

## Conclusão

Os comandos do Windows Defender PowerShell oferecem um **conjunto robusto de ferramentas** para gerenciar e aprimorar a segurança do sistema Windows. Eles permitem *automatizar operações de segurança*, *configurar opções avançadas* e integrar o Windows Defender aos fluxos de trabalho. Seja você administrador de sistemas ou usuário avançado, esses comandos ajudam a fortalecer a segurança do sistema.

Use os comandos do PowerShell com cuidado e entenda seus efeitos antes de executá-los. Aplique seus conhecimentos dos comandos do Windows Defender PowerShell para proteger o sistema de ameaças em evolução.

## Referências

1. Microsoft Docs - [Cmdlets do Windows Defender no Windows PowerShell](https://docs.microsoft.com/en-us/powershell/module/defender/?view=windowsserver2019-ps)
2. Microsoft Docs - [Introdução ao Windows PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.1)

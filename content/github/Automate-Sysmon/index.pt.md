---
title: "Automate-Sysmon: Simplifique a implantação e a configuração do Sysmon"
date: 2021-05-11
toc: true
draft: false
description: "Aprenda como implantar e configurar o Sysmon para melhorar a segurança do seu sistema com o script Automate-Sysmon, que simplifica o processo até mesmo para usuários novatos."
tags: ["Automatizar Sysmon", "Como Automatizar o Sysmon", "Como automatizar a configuração do Symon", "Como instalar o Symon", "Powershell", "Roteiro", "Implantação do Sysmon", "Configuração do Symon", "Log do sistema", "Detecção de Ameaças", "Atividade Maliciosa", "SwiftOnSecurity sysmon-config", "Microsoft Sysinternals", "Repositório GitHub", "BHIS", "Monitoramento do sistema", "Pesquisa de segurança", "Criação de processo", "Conexões de rede"]
---

Automate-Sysmon é um script útil que simplifica a implantação e configuração do Sysmon, uma poderosa ferramenta de monitoramento de sistema da Microsoft Sysinternals. Ao automatizar a instalação e configuração do Sysmon, esse script aumenta as habilidades de registro do seu sistema e aprimora os recursos de detecção de ameaças.

## O que é Sysmon?

Sysmon é uma ferramenta de monitoramento de sistema que pode ser usada para detectar atividades maliciosas em um sistema. Ele fornece informações detalhadas sobre a criação de processos, conexões de rede e outros eventos do sistema, tornando-o uma ferramenta inestimável para profissionais de segurança. Embora o Sysmon seja uma ferramenta poderosa, pode ser um desafio instalar e configurar.

## Como o Automate-Sysmon pode ajudar?

O script Automate-Sysmon facilita a instalação e configuração do Sysmon, mesmo para aqueles sem muita experiência. O script usa o popular módulo **SwiftOnSecurity/sysmon-config**, que fornece um conjunto pré-configurado de regras para o Sysmon. Essa configuração é baseada em anos de pesquisa de segurança e é atualizada regularmente pela comunidade.

Com o Automate-Sysmon, você pode automatizar todo o processo com um único comando ou instalar manualmente o Sysmon seguindo as instruções fornecidas. Essa flexibilidade torna mais fácil para os usuários personalizar a instalação e a configuração para atender às suas necessidades específicas.

## Como usar o Automate-Sysmon?

Existem duas maneiras de usar o Automate-Sysmon:

### Instalação automatizada:

Para usar a instalação automatizada, basta executar o seguinte comando no PowerShell:
```powershell
iwr -useb 'https://simeononsecurity.ch/scripts/sosautomatesysmon.ps1'|iex
```

This will automatically download and run the Automate-Sysmon script.

### Manual Install:

If you prefer to install Sysmon manually, follow these steps:

1. Download the script and other required files from the [GitHub repository](https://github.com/simeononsecurity/Automate-Sysmon).
2. Launch PowerShell with administrator privileges.
3. Navigate to the directory containing the downloaded files.
4. Run the following command to change the PowerShell execution policy: ```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force```
5. Unblock all the script files by running the following command: ```Get-ChildItem -Recurse *.ps1 | Unblock-File```
6. Run the following command to launch the Automate-Sysmon script: ```.\sos-automate-sysmon.ps1```


## Conclusão

Em conclusão, o Automate-Sysmon é uma ferramenta essencial para profissionais de segurança que desejam aumentar suas habilidades de registro e aprimorar os recursos de detecção de ameaças de seu sistema. Com a capacidade de automatizar a implantação e configuração do Sysmon, esta ferramenta pode ajudar até mesmo os usuários novatos a obter o máximo do Sysmon. Ao usar o módulo **simeononsecurity/Automate-Sysmon**, os usuários podem se beneficiar da experiência da comunidade e manter-se atualizados com as pesquisas de segurança mais recentes. Portanto, se você deseja melhorar a segurança do seu sistema, experimente o Automate-Sysmon!




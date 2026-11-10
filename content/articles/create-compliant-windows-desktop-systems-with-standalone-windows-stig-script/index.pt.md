---
title: "Standalone-Windows-STIG-Script: crie um PC em conformidade"
date: 2023-02-02
lastmod: 2026-11-09
toc: true
draft: false
description: "Guia passo a passo para usar o Standalone-Windows-STIG-Script em sistemas Windows em conformidade, com parâmetros e etapas de verificação."
tags: ["Script STIG", "Segurança do Windows", "Sistema Windows em conformidade", "Fortalecimento do sistema", "STIG do Windows", "Windows seguro", "Conformidade do Windows", "Instalação manual", "Atualizações do Windows", "Adobe Reader", "Firefox", "Chrome", "Internet Explorer 11", ".NET Framework", "Office", "OneDrive", "Java", "Windows Defender", "Firewall do Windows", "Medidas de mitigação", "Nessus PID", "VMware Horizon", "Fortalecimento opcional"]
cover: "/img/cover/create-compliant-windows-desktop-systems-with-standalone-windows-stig-script.webp"
coverAlt: "Ilustração de uma tela de computador com uma interface de conformidade de segurança, barras de progresso dinâmicas e fluxos de dados sobre um fundo azul-marinho escuro com cores de destaque vibrantes."
coverCaption: ""
---

Os sistemas Windows são amplamente usados em empresas, organizações e até em residências. Com o aumento dos ataques cibernéticos, você precisa garantir que esses sistemas sejam seguros e estejam em conformidade com os padrões do setor. O Standalone-Windows-STIG-Script é uma ferramenta útil para isso. Este artigo explica o que é o script, como funciona e como usá-lo para criar um sistema Windows seguro e em conformidade.

## O que é o Standalone-Windows-STIG-Script?

**Standalone-Windows-STIG-Script** é um script desenvolvido pela Simeononsecurity para automatizar a segurança de um sistema Windows conforme o Security Technical Implementation Guide (STIG). O script é de código aberto e está disponível no **GitHub**.

## Como funciona?

O Standalone-Windows-STIG-Script aplica as diretrizes do STIG para proteger um sistema Windows. Você pode executá-lo em um sistema Windows para aplicar as alterações necessárias à conformidade com o STIG. O script abrange várias medidas de segurança, incluindo:

- Políticas de contas
- Políticas de auditoria
- Opções de segurança
- Configurações do firewall
- Configurações de serviços

## Benefícios de usar o Standalone-Windows-STIG-Script:

- **Automação**: o script automatiza o processo de proteção de um sistema Windows, economizando tempo e reduzindo a possibilidade de erro humano.

- **Conformidade**: o script aplica as diretrizes do STIG e ajuda a manter o sistema Windows em conformidade com os padrões do setor.

- **Tranquilidade**: com o Standalone-Windows-STIG-Script, você pode ter mais confiança na segurança e na conformidade do seu sistema Windows.

_________________________________________________________________________________________________________________________

## Como usar o Standalone-Windows-STIG-Script:

1. Usar o Standalone-Windows-STIG-Script é relativamente simples. Siga estas etapas:

2. **Baixe o script**: ele está disponível no GitHub em https://github.com/simeononsecurity/Standalone-Windows-STIG-Script. Baixe-o e salve-o no seu sistema Windows.

3. **Abra um prompt de comando elevado**: clique com o botão direito no botão Iniciar do Windows e selecione "Windows PowerShell (Admin)".

4. **Execute o script**: acesse o local onde salvou o script e execute-o com o comando:

```powershell
powershell.exe -ExecutionPolicy Bypass -File Standalone-Windows-STIG-Script.ps1
```

5. Revise as alterações: após a execução do script, confira as alterações feitas no sistema e verifique se tudo foi configurado corretamente.

## Conclusão:

O Standalone-Windows-STIG-Script é uma ferramenta útil para proteger seu sistema Windows e alinhá-lo aos padrões do setor. Ele automatiza o processo de proteção e aplica as diretrizes do STIG. Se você quer criar um sistema Windows seguro e em conformidade, considere usar o Standalone-Windows-STIG-Script.

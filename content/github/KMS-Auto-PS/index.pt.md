---
title: "Automatize a Ativação KMS do Windows com o Script GLVK"
date: 2020-12-18
toc: true
draft: false
description: Simplifique o processo de ativação KMS do Windows 10 e Windows 11 usando o Script de Instalação Automática GLVK de SimeonOnSecurity, e aprenda mais sobre KMS e chaves cliente GLVK a partir da leitura recomendada da Microsoft.
tags:
- Ativação do Windows
- Chaves Cliente KMS
- GLVK
- Atualizações do Windows
- Conformidade
- Script Powershell
- Serviço de Gerenciamento de Chaves
- Licenciamento por Volume
- Ativação Empresarial
- Servidor de Gerenciamento de Chaves
- Automação
- Produtos Microsoft
- Sistema Operacional
- Software
- Ambientes Empresariais
- Powershell Administrativo
- Repositório GitHub
- Scripting
- Cibersegurança
- SimeonOnSecurity
- ativação KMS
- Script de Instalação Automática GLVK
- produtos Windows
- empresarial
- gerenciamento centralizado
- economia de tempo
- administração de TI
- ativação simplificada
- sem complicações
- produtividade
- redução de erros
- capacidades de monitoramento
- eficiência
- ativação de software
- chave de licença por volume
- automação de script
- gestão de TI
- processo de ativação
- licenciamento de software
- gerenciamento de licenças
- ferramenta de ativação
- implantação de software
- produtividade de TI
cover: /img/cover/KMS-Auto-PS.webp
coverAlt: Um servidor futurista cercado por computadores clientes brilhantes, ilustrando a ativação KMS em um ambiente escuro com cores vibrantes. A cena enfatiza a conectividade digital e a tecnologia moderna.
coverCaption: ''
lastmod: 2026-10-08
---

**Script de Instalação Automática GLVK para Ativação KMS**

*Leitura Recomendada:* [Microsoft - Chaves Cliente KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Introdução

A ativação KMS (Serviço de Gerenciamento de Chaves) é um método usado pela Microsoft para ativar e licenciar seus produtos em ambientes empresariais. O processo envolve um servidor central que ativa computadores clientes atribuindo-lhes uma chave de licença por volume chamada GLVK (Chave Genérica de Licença por Volume).

Neste artigo, exploraremos o Script de Instalação Automática GLVK, que simplifica o processo de ativação de produtos Windows usando KMS. Forneceremos instruções passo a passo sobre como executar o script e destacaremos seus benefícios para organizações.

## Leitura Recomendada

Antes de mergulhar no Script de Instalação Automática GLVK, é recomendado familiarizar-se com o conceito de KMS e as chaves cliente KMS disponíveis fornecidas pela Microsoft. Você pode consultar a seguinte documentação da Microsoft para mais informações:

- [Microsoft - Chaves Cliente KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Como Executar o Script

### Instalação Manual

Para instalar e executar manualmente o Script de Instalação Automática GLVK, siga estes passos:

1. Baixe o script e os arquivos relacionados do [Repositório GitHub](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip).
2. Abra uma sessão do PowerShell com privilégios administrativos.
3. Navegue até o diretório contendo todos os arquivos baixados.
4. Execute os seguintes comandos:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

Esses comandos definirão a política de execução para RemoteSigned para permitir a execução de scripts, desbloquearão quaisquer scripts PowerShell baixados e executarão o Script de Instalação Automática GLVK.

## Benefícios do Script de Instalação Automática GLVK

O Script de Instalação Automática GLVK oferece várias vantagens para organizações que desejam ativar produtos Windows usando KMS:

1. **Ativação Simplificada**: O script automatiza o processo de ativação KMS, eliminando a necessidade de configuração manual e reduzindo erros humanos.

2. **Economia de Tempo e Esforço**: Ao utilizar o script, administradores de TI podem economizar tempo e esforço significativos que seriam gastos em procedimentos manuais de ativação para múltiplas máquinas.

3. **Gerenciamento Centralizado**: O Script de Instalação Automática GLVK permite o gerenciamento centralizado da ativação KMS, proporcionando melhor controle e capacidades de monitoramento.

## Conclusão

O Script de Instalação Automática GLVK é uma ferramenta valiosa para organizações que buscam um método eficiente e simplificado para ativar produtos Windows usando KMS. Ao automatizar o processo de ativação, ele economiza tempo, reduz erros e aprimora as capacidades de gerenciamento centralizado. Com as instruções passo a passo fornecidas, as organizações podem implementar facilmente o script e desfrutar dos benefícios de uma ativação KMS sem complicações.

## Referências

1. [Microsoft - Chaves Cliente KMS (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)
2. [Repositório GitHub - Script de Instalação Automática GLVK](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)

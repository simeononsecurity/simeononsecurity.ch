---
title: "Automatize a ativação do KMS do Windows com o script GLVK"
date: 2020-12-18
toc: true
draft: false
description: "Simule o processo de ativação do KMS do Windows 10 usando o script de instalação automática GLVK da SimeonOnSecurity e saiba mais sobre as chaves do cliente KMS e GLVK nas leituras recomendadas da Microsoft."
tags: ["Ativação do Windows", "Chaves do Cliente KMS", "GLVK", "Atualizações do Windows", "Conformidade", "Script Powershell", "Serviço de Gerenciamento de Chaves", "Licenciamento por Volume", "Ativação empresarial", "Servidor de Gerenciamento de Chaves", "Automação", "Produtos da Microsoft", "Sistema operacional", "Programas", "Ambientes Corporativos", "Powershell Administrativo", "Repositório GitHub", "Scripts", "Cíber segurança", "SimeonOnSecurity"]
---

Script de instalação automática do GLVK para ativação do KMS

## Leitura recomendada:
-[Microsoft - KMS Client Keys (GLVK)](https://docs.microsoft.com/en-us/windows-server/get-started/kmsclientkeys)

## Como executar o script:
### Instalação manual:
Se baixado manualmente, o script deve ser iniciado a partir de um powershell administrativo no diretório que contém todos os arquivos do[GitHub Repository](https://github.com/simeononsecurity/KMS-Auto-PS/archive/main.zip)
```ps
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Force
Get-ChildItem -Recurse *.ps1 | Unblock-File
.\sos-kmsglvkactivationauto.ps1
```

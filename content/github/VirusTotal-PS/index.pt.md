---
title: "Varreduras de vírus eficientes com módulos VirusTotal PowerShell"
date: 2020-11-24
toc: true
draft: false
description: "Realize varreduras de vírus eficientes com os módulos VirusTotal PowerShell, automatizando a interação com a API VirusTotal e simplificando seu fluxo de trabalho de segurança."
tags: ["Módulos do PowerShell", "PowerShell", "Automação", "VirusTotal", "Verificações de vírus", "Verificações de domínio", "Chave API", "API VirusTotal", "Página de desenvolvedores do VirusTotal", "Administração do Sistema", "Fluxo de trabalho de segurança", "Verificações de vírus eficientes", "Baixar e instalar", "Repositório GitHub", "Exemplos de uso da API"]
---
 coleção de módulos PowerShell para interagir com a API VirusTotal

**Notas:**
- Você precisará de sua chave de API do VirusTotal, que pode ser encontrada em seu[Shodan Account](https://www.virustotal.com/gui/)
- Exemplos das APIs utilizadas nos módulos podem ser encontrados no[VirusTotal Developers Page](https://developers.virustotal.com/reference#getting-started)

## Baixar e instalar
- Baixe os módulos do[GitHub Repository](https://github.com/simeononsecurity/VirusTotal-PS)
- Instale todos os módulos
```ps
Get-ChildItem -Recurse *.ps1 | Import-Module
```
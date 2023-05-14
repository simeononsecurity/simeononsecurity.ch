---
title: "Assuma o controle das políticas do navegador Brave com BraveADMX - Modelos ADMX modificados"
date: 2020-07-25
---


A Brave, como empresa, falhou em lançar modelos ADMX para o site do navegador Brave, empurrando registros puros como a única opção suportada.
Como o Brave Browser é baseado no Chromium, ele deve suportar a maioria, se não todas, as mesmas políticas dos modelos ADMX do Chromium e do Google Chrome.
Com isso em mente, modificamos os modelos ADMX do Google Chrome para refletir o caminho de registro do navegador Brave. Após algumas soluções de problemas e testes iniciais, os modelos parecem funcionar.

**Estas definições de política estão em um estado pré-alfa. Eles devem ser usados apenas para fins de teste **

## Baixe os arquivos necessários.

**Baixe os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/BraveADMX)

## Notas

Definições de política do Google Chrome modificadas de acordo com:
[Brave Group Policy](https://support.brave.com/hc/en-us/articles/360039248271-Group-Policy)

**Observação:** Substituído "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" por "HKEY_LOCAL_MACHINE\Software\Policies\BraveSoftware\Brave"

**Observação:** Não instale os modelos SOS Chromium e Brave Browser ADMX ao mesmo tempo.

## Como instalar

1.) Copie todos os arquivos exceto readme.md para "C:\Windows\PolicyDefinitions" e/ou "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Lucro?
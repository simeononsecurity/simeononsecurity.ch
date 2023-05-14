---
title: "ChromiumADMX: modelo ADMX adequado para o navegador Chromium"
date: 2020-07-25
---


Modelo ADMX adequado para o navegador Chromium

A Chromium, como empresa, falhou ao liberar modelos ADMX para o navegador Chromium que podem ser instalados ao mesmo tempo que os modelos do Google Chrome.
Com isso em mente, modificamos os modelos ADMX do Google Chrome para refletir o caminho de registro do navegador Chromium e os colocamos juntos na pasta ADMX do Google no GPO.

**Estas definições de política estão em um estado pré-alfa. Eles devem ser usados apenas para fins de teste **

## Baixe os arquivos necessários

**Baixe os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/ChromiumADMX)

## Notas

Definições de política do Google Chrome modificadas de acordo com:
[Chromium Policy Templates](https://www.chromium.org/administrators/policy-templates)

**Observação:** substituído "HKEY_LOCAL_MACHINE\Software\Policies\Google\Chrome" por "HKEY_LOCAL_MACHINE\Software\Policies\Chromium\"

**Observação:** Não instale os modelos SOS Chromium e Brave Browser ADMX ao mesmo tempo.

## Como instalar

1.) Copie todos os arquivos exceto readme.md para "C:\Windows\PolicyDefinitions" e/ou "\\\domain.tld\domain\Policies\PolicyDefinitions"

2.) Lucro?





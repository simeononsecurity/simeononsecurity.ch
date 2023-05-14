---
title: "Automatize a conformidade do Oracle JRE 8 STIG com o script Powershell"
date: 2020-08-05
---


Os Oracle JRE STIGs não são tão diretos, exigindo que os administradores pesquisem a documentação JAVA e gerem arquivos de configuração java, quando a maioria dos administradores está acostumada a usar apenas STIG usando a política de grupo.

## Baixe os arquivos necessários

Baixe os arquivos necessários do[GitHub Repository](https://github.com/simeononsecurity/JAVA-STIG-Script)

## STIGS/SRGs aplicados:
-[Oracle JRE 8 V1R5](https://dl.dod.cyber.mil/wp-content/uploads/stigs/zip/U_Oracle_JRE_8_Windows_V1R5_STIG.zip)

## Fontes:
-[MyITGuy - deployment.properties](https://gist.github.com/MyITGuy/9628895)

-[cbu.edu - Java Technotes](http://stu.cbu.edu/java/docs/technotes/guides/deploy/properties.html)

## Como executar o script

**O script pode ser iniciado a partir do download extraído do GitHub assim:**

```
.\sos-install-java-config.ps1
```

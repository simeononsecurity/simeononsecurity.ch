---
title: "Práticas recomendadas para gerenciamento de fonte de tempo em domínios Windows e máquinas autônomas"
draft: false
toc: true
date: 2023-05-23
description: "Aprenda como configurar e lidar com fontes de tempo de forma eficaz em domínios do Windows e máquinas autônomas para garantir a sincronização de tempo precisa e evitar possíveis problemas."
tags: ["fontes de tempo", "domínio do Windows", "máquinas autônomas", "sincronização de tempo", "cronometragem precisa", "servidores NTP", "controladores de domínio", "Serviço de horário do Windows", "falhas de autenticação", "registrar inconsistências no arquivo", "problemas de replicação", "configuração da fonte de tempo", "gerenciamento de fonte de tempo", "Sincronização de horário do Windows", "práticas recomendadas de cronometragem", "configuração da fonte de tempo", "sincronizando hora do sistema", "Sincronização de tempo de domínio do Windows", "sincronização de tempo de máquina autônoma", "seleção de fonte de tempo", "solução de problemas de fonte de tempo", "erros de fonte de tempo", "problemas de fonte de tempo", "comandos de configuração de fonte de tempo", "instruções de configuração da fonte de tempo", "desafios de sincronização de tempo", "consequências da perda de tempo", "prevenção de desvio de tempo", "resolução de falha de sincronização de tempo", "solução de problemas de sincronização de tempo", "gerenciamento de fonte de tempo em domínios do Windows", "manipulação de fontes de tempo em máquinas Windows autônomas", "evitando perda de tempo em ambientes Windows", "consequências de falhas de sincronização de tempo", "melhores práticas para cronometragem precisa"]
cover: "/img/cover/An_image_depicting_a_clock_being_synchronized_with_a_domain.png"
coverAlt: "Uma imagem representando um relógio sendo sincronizado com um controlador de domínio e uma máquina autônoma, simbolizando o gerenciamento de fonte de tempo e a sincronização precisa de tempo em ambientes Windows."
coverCaption: ""
---

**Como definir e lidar com fontes de tempo em um domínio Windows e em máquinas Windows autônomas**

A sincronização de tempo é crucial para manter carimbos de data/hora precisos e garantir o funcionamento adequado dos sistemas em um domínio Windows ou em máquinas Windows independentes. Neste artigo, discutiremos as práticas recomendadas para definir e lidar com fontes de tempo em ambos os cenários, destacando a importância de membros de domínio apontarem para controladores de domínio. Também exploraremos diferentes opções para fontes de tempo, enfatizando o uso de pools NTP externos ou servidores de tempo baseados em GPS para uma precisão ideal.

______

## Definindo fontes de tempo em um domínio do Windows

Em um domínio do Windows, é essencial ter uma sincronização de horário consistente em todos os membros do domínio. A prática recomendada é configurar os controladores de domínio como a fonte de horário principal para os membros do domínio. Ao fazer isso, você garante que todos os sistemas dentro do domínio tenham tempo sincronizado, o que é crítico para autenticação, log e várias operações de domínio.

### Opções de fonte de tempo para controladores de domínio

Os controladores de domínio podem obter seu horário de diferentes fontes, incluindo o relógio do BIOS, VMware Tools (em ambientes virtualizados) ou servidores de horário externos. Embora o uso do relógio do BIOS ou do VMware Tools possa ser conveniente, é recomendável utilizar uma fonte **stratum 0 ou 1** como um pool NTP externo ou servidor de horário baseado em GPS para maior precisão.

#### Pools NTP Externos

Pools NTP externos são fontes confiáveis e distribuídas globalmente para sincronização de horário. Eles consistem em um grande número de servidores NTP mantidos por organizações e instituições em todo o mundo. Ao configurar os controladores de domínio para sincronizar com pools NTP externos, você pode garantir a precisão do tempo no domínio do Windows.

Para configurar controladores de domínio para usar um pool NTP externo, siga estas etapas:

1. Abra um prompt de comando elevado no controlador de domínio.
2. Execute o seguinte comando:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"pool.ntp.org" /reliable:yes /update
```

Este comando configura o controlador de domínio para sincronizar com o pool NTP pool.ntp.org. Ajuste o comando para usar um pool NTP diferente ou várias fontes, se desejar.

3. Reinicie o serviço de horário do Windows para aplicar as alterações:

```shell
net stop w32time && net start w32time
```


#### Servidores de horário baseados em GPS

Outra opção para controladores de domínio é utilizar servidores de horário baseados em GPS. Esses servidores contam com sinais de GPS para fornecer informações de tempo altamente precisas. Ao configurar um servidor de horário baseado em GPS hospedado localmente e configurar os controladores de domínio para sincronizar com ele, você pode obter uma sincronização de horário precisa no domínio do Windows.

### Configurando membros do domínio

Os membros do domínio, como máquinas clientes e outros servidores, devem ser configurados para sincronizar seu horário com os controladores de domínio. Isso garante que todos os sistemas no domínio permaneçam sincronizados e evite problemas relacionados ao tempo.

Para configurar os membros do domínio para sincronizar a hora com os controladores de domínio, geralmente não são necessárias etapas adicionais. Por padrão, os membros do domínio sincronizam automaticamente seu horário com os controladores de domínio.

______

## Definindo fontes de tempo em máquinas Windows autônomas

Em máquinas Windows autônomas que não fazem parte de um domínio, o processo de configuração de fontes de horário pode variar dependendo da versão do Windows e das configurações regionais. Por padrão, máquinas Windows autônomas geralmente usam **time.windows.com** como fonte de horário principal. No entanto, vale a pena notar que o comportamento padrão pode ser modificado.

### Alterando a fonte de tempo em máquinas autônomas

Se você deseja alterar a fonte de horário em uma máquina Windows autônoma, siga estas etapas:

1. Abra um prompt de comando elevado na máquina.
2. Execute o seguinte comando para configurar o servidor NTP:

```shell
w32tm /config /syncfromflags:manual /manualpeerlist:"time.windows.com" /update
```

Este comando define time.windows.com como a fonte de horário para a máquina autônoma. Ajuste o comando para usar uma fonte de tempo diferente, se desejar.

3. Reinicie o serviço de horário do Windows para que as alterações entrem em vigor:

```shell
net stop w32time && net start w32time
```


Ao executar esses comandos, você pode configurar uma máquina Windows autônoma para sincronizar seu horário com a fonte de horário desejada.

______

## Conclusão

A sincronização de tempo adequada é vital para domínios do Windows e máquinas autônomas. Em um domínio do Windows, é crucial configurar os membros do domínio para apontar para controladores de domínio para sincronização de tempo. Os controladores de domínio podem obter seu horário de várias fontes, sendo o uso de pools NTP externos ou servidores de horário baseados em GPS a prática recomendada para maior precisão.

Em máquinas Windows autônomas, a fonte de horário padrão geralmente é time.windows.com. No entanto, você pode alterar a fonte de tempo usando os comandos fornecidos.

Ao seguir essas práticas recomendadas e configurar as fontes de horário apropriadas, você garante a cronometragem precisa, a autenticação confiável e o registro consistente em seu ambiente Windows.

______

## Referências

- [Microsoft Docs: How the Windows Time Service Works](https://learn.microsoft.com/en-us/windows-server/networking/windows-time-service/how-the-windows-time-service-works)
- [Microsoft Docs: Windows Time Service Tools and Settings](https://docs.microsoft.com/en-us/windows-server/networking/windows-time-service/windows-time-service-tools-and-settings)
- [NTP Pool Project](https://www.ntppool.org/)
- [National Institute of Standards and Technology (NIST)](https://www.nist.gov/)


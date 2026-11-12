---
title: "Entenda a filtragem WMI"
date: 2023-07-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Aprenda a usar a filtragem WMI para direcionar objetos de Política de Grupo (GPOs) aos computadores certos, com exemplos práticos e boas práticas."
genre: ["Gerenciamento do Windows", "Política de Grupo", "Administração de sistemas", "Gerenciamento de redes", "Infraestrutura de TI", "Gerenciamento de políticas", "Governança de TI", "Automação de TI", "Active Directory", "Conformidade de segurança"]
tags: ["filtragem WMI", "GPO", "objetos de Política de Grupo", "filtros WMI", "direcionamento de políticas", "consultas WMI", "Windows Management Instrumentation", "controle de GPO", "Console de Gerenciamento de Política de Grupo", "Linguagem de Consulta WMI", "aplicação de políticas", "WQL", "ajuste de políticas", "gerenciamento de políticas", "recursos do sistema", "exemplos de direcionamento de políticas", "administração de sistemas", "gerenciamento de redes", "gerenciamento de infraestrutura de TI", "automação de TI", "gerenciamento do Active Directory", "conformidade de segurança", "técnicas de controle de políticas", "boas práticas de gerenciamento de políticas", "filtragem de políticas", "estratégias de controle de GPO", "segurança de GPO", "benefícios da filtragem WMI", "implementação da filtragem WMI", "boas práticas para filtros WMI"]
cover: "/img/cover/An_illustration_of_a_magnifying_glass_focusing.webp"
coverAlt: "Ilustração de uma lupa focada em um ícone de filtro, representando o direcionamento de GPOs por filtragem WMI."
coverCaption: "Use a filtragem WMI para direcionar políticas de GPO com eficiência."
---

## Introdução

Nos objetos de Política de Grupo (GPOs), a [**filtragem WMI**](https://simeononsecurity.com/github/wmi-filters/) controla quais computadores ou usuários recebem políticas com base nos resultados de consultas WMI (Windows Management Instrumentation). Esse recurso ajuda os administradores a refinar o direcionamento e aplicar políticas somente aos destinos desejados. Este artigo explica a filtragem WMI, seu funcionamento nas GPOs, como criar [filtros WMI](https://simeononsecurity.com/github/wmi-filters/) e alguns exemplos práticos.

## [O que é filtragem WMI?](https://simeononsecurity.com/github/wmi-filters/)

A [**filtragem WMI**](https://simeononsecurity.com/github/wmi-filters/) aplica filtros às GPOs de acordo com os resultados de consultas WMI. A WMI é uma infraestrutura de gerenciamento integrada aos sistemas operacionais Windows. Ela permite que administradores obtenham dados de gerenciamento e interajam programaticamente com os recursos do sistema. Com a filtragem WMI, é possível direcionar GPOs dinamicamente segundo critérios definidos pelas consultas.

Os filtros WMI são escritos na WMI Query Language (WQL), um subconjunto de SQL (Structured Query Language). Em geral, baseiam-se em propriedades e valores disponíveis em um namespace WMI. Administradores combinam condições, operadores lógicos e namespaces para criar consultas que selecionem computadores ou usuários específicos.

## Como a filtragem WMI funciona nas GPOs?

{{< figure src="wmi-filtering-gpo-evaluation-flow.webp" alt="Fluxograma em que um filtro WMI associado a um objeto de Política de Grupo avalia uma consulta WQL como True ou False e decide se a GPO será aplicada ao computador de destino" >}}

Na Política de Grupo, a **filtragem WMI** permite aplicar GPOs seletivamente de acordo com a avaliação de **consultas WMI**. Ao associar um **filtro WMI** a uma GPO, o resultado **True** ou **False** determina se a GPO será aplicada.

Os filtros usam a **WMI Query Language (WQL)**, um subconjunto de SQL. A WQL permite criar consultas complexas com base em **propriedades** e **valores** disponíveis em um **namespace WMI**. Assim, é possível direcionar computadores ou usuários específicos.

Por exemplo, uma organização pode querer aplicar uma GPO somente aos computadores que executam Windows 10. Ela pode criar um filtro que verifique a propriedade **OperatingSystem** da classe **Win32_OperatingSystem**. A consulta WMI poderia ser:

```sql
SELECT * FROM Win32_OperatingSystem WHERE Version LIKE "10.%"
```

A consulta verifica se a versão do sistema operacional começa com "10.", o que indica Windows 10. Se o resultado for **True**, a GPO será aplicada ao computador de destino. Caso contrário, não será aplicada.

A filtragem WMI também aceita condições e operadores lógicos como **AND**, **OR** e **NOT**. Administradores podem combinar várias propriedades e valores para controlar com mais precisão a aplicação de GPOs.

Também é possível usar diferentes **namespaces WMI** para acessar conjuntos específicos de classes e propriedades WMI. Isso permite direcionar GPOs com base em hardware, software instalado, configurações de rede e outros critérios.

Para saber mais sobre a criação de filtros e consultas WMI, consulte a documentação da Microsoft sobre [filtragem WMI para Política de Grupo](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/Policy/filtering-the-scope-of-a-gpo).

A filtragem WMI ajuda administradores a adaptar a aplicação de GPOs a computadores ou usuários com base em condições dinâmicas, melhorando o gerenciamento do ambiente de TI.

## Criar filtros WMI para GPOs

Para criar um filtro WMI para uma GPO, siga estas etapas:

1. Abra o **Console de Gerenciamento de Política de Grupo** (GPMC) em um computador Windows associado ao domínio.

2. Expanda o domínio e acesse o nó **WMI Filters**.

3. Clique com o botão direito em **WMI Filters** e selecione **New**.

4. Dê um nome claro ao filtro e insira a consulta WMI no campo **Query**. Use a sintaxe WQL.

5. Clique em **OK** para salvar o filtro WMI.

Depois de criado, o filtro pode ser associado a uma ou mais GPOs. Para associá-lo a uma GPO:

1. Clique com o botão direito na GPO desejada e selecione **Properties**.

2. Na janela de propriedades da GPO, abra a guia **WMI Filtering**.

3. Selecione na lista o filtro WMI desejado.

4. Clique em **OK** para salvar as alterações.

Associar filtros WMI a GPOs permite direcionar com precisão a aplicação de políticas conforme os resultados das consultas WMI.

## Quantos filtros WMI podem ser configurados para uma GPO?

Os administradores podem configurar **vários filtros WMI** para uma GPO e direcionar as políticas com precisão. Não há um limite específico para a quantidade de filtros associados a uma única GPO, permitindo combinações complexas.

Considere, porém, o efeito da quantidade de filtros no tempo de processamento das GPOs. Quanto mais filtros houver, mais tempo a avaliação e a aplicação das GPOs poderão levar. Para manter a eficiência, use uma quantidade razoável de filtros.

Por exemplo, uma organização pode querer aplicar uma GPO somente a computadores com Windows 10 e um software específico instalado. Ela pode criar dois filtros separados: um para o **sistema operacional** e outro para a **instalação do software**. Combinados, eles selecionam os computadores desejados.

É preciso equilibrar a quantidade de filtros necessária aos requisitos de direcionamento com o tempo de processamento. Antes de definir essa quantidade, avalie a complexidade do ambiente, o número de computadores ou usuários e os possíveis efeitos no desempenho.

O suporte a vários filtros WMI ajuda a otimizar o direcionamento de GPOs e manter eficiente o processamento e o gerenciamento do ambiente de TI.

## Exemplos práticos de filtragem WMI em GPOs

A filtragem WMI oferece maneiras práticas de direcionar a aplicação de políticas. Veja alguns exemplos:

1. **Direcionar sistemas operacionais específicos**: para aplicar uma GPO somente a computadores com **Windows 10**, crie um filtro que verifique a versão do sistema operacional, como `"SELECT * FROM Win32_OperatingSystem WHERE Version LIKE '10.%'"`. Isso seleciona computadores Windows 10.

2. **Políticas diferentes para desktops e laptops**: se os dois tipos de dispositivo precisarem de políticas distintas, use dois filtros WMI. Um pode identificar desktops por atributos de hardware, como `"SELECT * FROM Win32_ComputerSystem WHERE Desktop = True"`, e o outro identifica laptops. Assim, cada tipo recebe as políticas adequadas.

3. **Aplicar políticas conforme o espaço em disco**: para evitar políticas que consomem muitos recursos em computadores com pouco espaço, crie um filtro que verifique o espaço disponível. Por exemplo, a consulta `"SELECT * FROM Win32_LogicalDisk WHERE FreeSpace > 10737418240"` exclui computadores com menos de 10 GB livres.

Esses exemplos demonstram a flexibilidade da **filtragem WMI** nas GPOs e permitem direcionar políticas segundo critérios específicos.

## Conclusão

A filtragem WMI é um recurso útil dos objetos de Política de Grupo. Ela permite que administradores apliquem políticas seletivamente com base nos resultados de consultas WMI. Os filtros direcionam políticas a computadores ou usuários específicos, tornando o gerenciamento mais eficiente e controlado. Neste artigo, vimos o conceito, seu funcionamento nas GPOs, como criar filtros e exemplos práticos.

Ao incluir a filtragem WMI no gerenciamento de GPOs, você aumenta a precisão da aplicação das políticas e garante que elas cheguem somente aos destinos pretendidos.

## Referências

- [Microsoft Docs: Criar filtros WMI para a GPO](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/create-wmi-filters-for-the-gpo)
- [Microsoft Docs: about_WQL](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wql?view=powershell-5.1)
- [Microsoft Docs: Política de Grupo](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/policy/group-policy-objects)
- [Microsoft Docs: Console de Gerenciamento de Política de Grupo](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn265969(v=ws.11))

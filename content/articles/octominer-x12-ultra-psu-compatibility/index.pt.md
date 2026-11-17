---
title: "Compatibilidade de fontes do Octominer X12 Ultra: teste de campo Chicony e LiteOn"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "Um teste com cinco ventoinhas e três fontes no Octominer X12 Ultra mostrou que uma fonte Chicony iniciou o equipamento, enquanto as LiteOn testadas indicaram âmbar e não iniciaram."
genre: ["Hardware de mineração", "Hardware de computador"]
tags: ["Octominer X12 Ultra", "fonte de alimentação para servidor", "compatibilidade de fontes", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Ilustração abstrata de três fontes para servidor em um chassi com luzes de status verdes, âmbar e cinzas"
coverCaption: ""
---

**A Chicony R12-1K6P2A iniciou meu Octominer X12 Ultra com cinco ventoinhas e três fontes.** As fontes LiteOn PS-2142-2L que testei mostraram uma luz verde, mudaram para âmbar e não iniciaram o equipamento. Esse resultado se aplica à minha unidade com uma placa de alimentação **OCTOMINER (12PIN) 3x DPS1200 rev. 20**. A mesma potência nominal ou uma lista para uma placa breakout X12 separada não comprova compatibilidade com uma placa Octominer.

O chassi foi vendido como uma **configuração de 3.600 W** com três baias para fontes. [A Octominer lista uma opção com três fontes de 1.200 W](https://octominer.eu/product/octominer-x12-ultra-used/) para o X12 Ultra, além de outras configurações. Confira a etiqueta e a placa de alimentação do seu equipamento antes de aplicar esses resultados.

## Resultados do teste

| Fonte | Resultado neste equipamento |
|---|---|
| **Chicony R12-1K6P2A, 1.600 W** | Iniciou o equipamento no meu teste. Este artigo não mediu carga sustentada nem operação em todas as baias. |
| **LiteOn PS-2142-2L, 1.400 W** | As unidades testadas mostraram verde e depois âmbar. O equipamento não iniciou. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | A entrada CA incomum dificultou encontrar um cabo compatível. Não registrei resultado de inicialização ou carga para essa fonte. |
| **HP HSTNS-PD30, 1.200 W** | Testada no mesmo equipamento. Não iniciou o sistema. |
| **Outras unidades HP Common Slot** | Os kits Platinum Plus de 1.200 W e as unidades de 750 W HSTNS-PD22B, HSTNS-PL22B e HSTNS-PD18 que testei não iniciaram o equipamento. Os números exatos de modelo das fontes dos kits não foram registrados. |

**Não interprete o resultado da LiteOn como diagnóstico de defeito para toda PS-2142-2L.** A sequência observada identifica uma falha de inicialização neste chassi. O teste não isolou o sinal de ativação, a troca de telemetria, o pinout da placa ou um defeito em uma fonte específica. Da mesma forma, o resultado da Chicony confirma uma inicialização bem-sucedida, não uma classificação certificada de 4.800 W para o chassi nem confiabilidade a longo prazo.

## Qual Chicony iniciou este equipamento?

O modelo que funcionou foi **Chicony R12-1K6P2A**, também listado como peça **R1K6A002L** na [tabela de compatibilidade da Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). O [relatório de teste 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identifica uma fonte de 1.600 W classificada para **200 a 240 V CA**, 10 A e 50 a 60 Hz. O relatório mediu eficiência de 94,19% com meia carga nas condições de teste a 230 V. Esses valores descrevem a fonte testada, não todo o equipamento de mineração.

A classificação de **200 a 240 V é importante**. Não presuma que este modelo fornece sua potência nominal em uma tomada de 120 V. Segundo uma [listagem de peças de servidor para o modelo exato](https://www.itcreations.com/product/142080), a fonte testada tem entrada C14 padrão. Use cabos e equipamentos de distribuição classificados para a tensão e corrente de entrada.

Meu teste confirmou uma inicialização com a Chicony nesta placa específica. Ele não comprova compatibilidade com todas as revisões do X12 Ultra. Confira o número completo do modelo e a etiqueta da fonte antes de encomendar outras unidades.

## Por que a lista da LiteOn me confundiu

A **LiteOn PS-2142-2L** aparece na [tabela de compatibilidade de placas breakout X12 da Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). O [relatório 80 PLUS](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) identifica um modelo de 1.400 W. Essas fontes confirmam o modelo e o uso listado com o **adaptador X12 da Parallel Miner**. Nenhuma testa a placa de alimentação OEM da Octominer.

Minhas unidades PS-2142-2L mudaram de **verde para âmbar** depois de inseridas, e o equipamento não iniciou. Lâminas de saída parecidas não comprovam comportamento igual de inicialização, status ou comunicação. A sequência de LEDs, por si só, não prova qual diferença causou a falha.

A mesma [tabela da Parallel Miner](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) agrupa **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L** e **Chicony R12-1K6P2A** na família de adaptadores de oito pinos. Ela coloca **HP HSTNS-PD30** e várias fontes HP Common Slot de 750 W em outra família de adaptadores de seis pinos. Nenhuma unidade HP que testei iniciou este equipamento. A tabela descreve as placas da Parallel Miner, não uma lista de substituição para a placa **OCTOMINER (12PIN)**.

## Confira a alimentação e os cabos

O [guia de solução de problemas do Octominer X12 Ultra](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) informa que o chassi sozinho consome até **200 W com as ventoinhas em velocidade máxima**. Ele recomenda pelo menos **10% de margem de potência** e alerta para não ultrapassar **90% da potência nominal das fontes instaladas**. Considere o consumo das GPUs, do chassi e a saída real das fontes na sua tensão CA.

**A etiqueta de 1.600 W em cada fonte Chicony não eleva a configuração publicada de 3.600 W do chassi para 4.800 W.** A placa de alimentação, a fiação interna, os conectores, a distribuição CA e o resfriamento também limitam o sistema. Não medi esses limites nesta unidade. Mantenha o equipamento dentro da configuração documentada até a Octominer confirmar uma potência superior para a revisão exata da placa.

O Dell/Delta **D1200E-S0 / 0F37X3** apresentou outro problema: a entrada CA do lado da fonte exigia um cabo de encaixe menos comum. Em uma busca anterior, identifiquei a entrada como **LS-25** e o conector do cabo como **LS-26**, com base na unidade e nos anúncios de cabos. Confira o formato do conector e as marcações elétricas antes de comprar um cabo. Um plugue C13 parecido não substitui o conector de encaixe correto.

## Verifique seu X12

1. **Registre o hardware exato.** Fotografe a etiqueta do chassi, a etiqueta da fonte, a entrada CA, a lâmina de saída e a revisão da placa de alimentação. Conte as ventoinhas e baias.
2. **Confira a alimentação CA.** Compare a classificação de entrada da fonte com as classificações da tomada, do cabo e da PDU. O relatório da Chicony R12-1K6P2A especifica 200 a 240 V CA.
3. **Teste uma configuração mínima.** Desligue e desconecte todas as entradas CA antes de trocar uma fonte, GPU ou conexão PSON. [O guia da Octominer](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) recomenda conferir o encaixe e os LEDs da fonte, o cabo PSON de seis pinos entre a placa-mãe e a placa de alimentação, e uma fonte com uma GPU para isolar um problema de inicialização.
4. **Registre o resultado.** Anote o modelo da fonte, a baia, a sequência dos LEDs, se a placa e as ventoinhas iniciaram e se o equipamento inicializou. Repita o teste em outras baias somente após um desligamento seguro.
5. **Meça antes de adicionar carga.** Confira a telemetria da fonte e a potência na tomada sob a carga prevista das GPUs. O resultado de inicialização deste artigo não substitui um teste de carga.

## Conclusão

**A Chicony R12-1K6P2A é a única substituição nesta comparação com uma inicialização bem-sucedida relatada no meu X12 Ultra de três baias.** As unidades LiteOn PS-2142-2L testadas mudaram de verde para âmbar e não iniciaram. As unidades HP Common Slot testadas também não iniciaram o equipamento. Trate outras listas de fontes como pistas de pesquisa até que o modelo exato e a placa Octominer passem por testes controlados de inicialização e carga. Comece pelas etiquetas do modelo e pela revisão da placa. Consulte as orientações de energia da Octominer antes de aumentar a carga das GPUs.

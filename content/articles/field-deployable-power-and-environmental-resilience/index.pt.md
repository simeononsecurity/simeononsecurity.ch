---
title: "Energia em Campo e Resiliência Ambiental"
date: 2026-08-25
lastmod: 2026-11-12
toc: true
draft: false
description: "Planeje energia e proteção ambiental para computação de borda em campo. Veja como dimensionar um UPS e lidar com painéis solares, baterias, sincronização de horário, classificações de proteção, aterramento e surtos elétricos."
genre: ["Computação de borda", "TI em campo", "Sistemas de energia", "Hardware", "Recuperação de desastres", "Computação robusta", "Redes"]
tags: ["dimensionamento de UPS", "fonte de energia para campo", "alimentação DC para servidor", "energia solar para servidor", "classificação IP de gabinete", "classificação NEMA", "proteção contra surtos", "aterramento de eletrônicos", "energia de servidor fora da rede", "energia para centro de dados portátil", "cálculo de autonomia da bateria", "energia de servidor 12V", "energia DC 48V", "energia de TI com gerador", "sistema de energia robusto", "energia para nó de borda", "energia para recuperação de desastres", "servidor implantável em campo", "resiliência ambiental", "energia expedicionária", "bateria LiFePO4", "fosfato de ferro-lítio", "USB Power Delivery", "comparação de químicas de bateria", "Network UPS Tools NUT", "monitoramento de UPS por SNMP", "sincronização NTP", "relógio sincronizado por GPS"]
cover: "/img/cover/field-deployable-power-environmental-resilience-solar-ups.webp"
coverAlt: "Ilustração de um servidor robusto ao ar livre, com painéis solares carregando um banco de baterias e gráficos digitais de gerenciamento de energia em um fundo escuro."
coverCaption: ""
ref: ["/articles/field-deployable-edge-compute-hardware-and-enclosure-selection", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes", "/articles/field-it-tidbits-beyond-the-mini-datacenter", "/articles/the-role-of-ecc-memory-in-mitigating-data-corruption"]
---

**Um servidor implantado em campo é tão confiável quanto sua fonte de energia.** O melhor gabinete e o computador mais rápido não ajudam quando o local fica sem energia e nada assume a carga. *O planejamento de energia faz parte da montagem. É a parte com maior probabilidade de falhar primeiro.*

Este é **o segundo artigo de uma série de quatro partes** sobre servidores e equipamentos de rede compactos, preparados para implantação rápida. [A primeira parte](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) tratou de gabinetes e computação. Esta parte aborda energia e proteção contra calor, poeira, água e problemas elétricos. [A terceira parte](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/) trata de conectividade e segurança dos dados. [A quarta parte](/articles/field-it-tidbits-beyond-the-mini-datacenter/) reúne outros detalhes.

______

## Dimensionamento de um UPS para uso em campo

Um **UPS (sistema de alimentação ininterrupta)** cobre o intervalo entre uma falha de energia e o desligamento dos equipamentos ou a entrada de uma fonte reserva. O dimensionamento para uso em campo começa com um cálculo simples.

1. Some a **potência de todos os dispositivos** no gabinete, incluindo computador, switch, ponto de acesso e armazenamento.
2. Multiplique o total por **1,5 a 1,6** para deixar margem para a corrente de partida.
3. Divida a capacidade nominal do UPS em **watt-hora** pela potência total da carga para estimar a autonomia em horas.

*A capacidade da bateria diminui com a idade e a temperatura. Considere a autonomia informada pelo fabricante como o melhor caso, não como garantia.* Planeje uma autonomia real menor, sobretudo em ambientes quentes, onde as baterias perdem capacidade mais depressa.

**[Schneider Electric / APC](https://www.apc.com/) publica orientações detalhadas sobre dimensionamento de UPS e comportamento das baterias.** A regra principal também vale para instalações em campo: conecte o UPS diretamente à tomada ou à saída do gerador, nunca a uma régua com proteção contra surtos. Ligue tomadas adicionais a uma PDU separada, depois do UPS.

| Tipo de UPS | Indicado para | Compromisso |
|---|---|---|
| **UPS line-interactive** | A maioria das instalações com energia da rede ou de gerador | Breve tempo de transferência quando falta energia, em geral abaixo de 10 ms |
| **UPS online de dupla conversão** | Equipamentos sensíveis em fontes instáveis ou com ruído | Mais pesado e caro por watt |
| **Bateria DC com inversor integrado** | Montagens muito compactas que não comportam um UPS tradicional | Menor eficiência ao converter DC para AC e depois de volta |

## Energia DC: dispense o inversor

Cada conversão de AC para DC desperdiça energia na forma de calor. **Alimentar equipamentos diretamente com DC, quando eles aceitam esse tipo de energia, elimina uma etapa de conversão e um ponto de falha.**

- **Sistemas de 12 V** servem para montagens pequenas, como computadores de placa única, thin clients e switches pequenos. Também correspondem à tensão comum de baterias automotivas e marítimas.
- **Sistemas de 48 V** servem para montagens maiores e correspondem ao padrão de tensão usado em centrais de telecomunicações. Por isso, equipamentos DC de telecom costumam aparecer usados por preços baixos.
- Muitos **switches de rede e pontos de acesso** já aceitam PoE ou entrada DC. Consulte a ficha técnica antes de presumir que precisa de um inversor.

*Uma montagem nativa em DC funciona por mais tempo com a mesma capacidade de bateria do que uma montagem AC com inversor, pois elimina as perdas do inversor.*

## Energia híbrida com solar e gerador

Para implantações que duram mais do que uma bateria consegue sustentar, combine um banco de baterias com uma fonte de recarga.

- **Painéis solares portáteis com controlador de carga** funcionam bem em locais ensolarados, com recarga durante o dia e uso da bateria à noite.
- **Um pequeno gerador inversor** recarrega rapidamente sem depender do clima, mas exige logística de combustível e produz ruído. Isso é um problema sério em implantações discretas ou sensíveis ao barulho.
- **Uma configuração híbrida**, com solar como fonte principal e gerador como reserva, cobre os dias em que o mau tempo reduz a produção solar.

*Dimensione o banco para pelo menos um dia completo de autonomia sem fonte de recarga.* Um plano que depende de sol ininterrupto ou reabastecimento garantido não é resiliente.

{{< figure src="field-power-hybrid-solar-battery-generator.webp" alt="Diagrama em que um painel solar e um gerador carregam um banco central de baterias, que alimenta um gabinete compacto de servidor por meio de um bloco de distribuição DC e AC" >}}

## Química das baterias para uso em campo

Nem toda bateria serve para um gabinete sujeito a choques, calor e frio. **A química interna importa tanto quanto a capacidade em watt-hora impressa no rótulo.**

| Química | Indicada para | Compromisso |
|---|---|---|
| **LiFePO4 (fosfato de ferro-lítio)** | A maioria das montagens em campo, longa vida em ciclos e modo de falha mais seguro | Mais pesada por watt-hora do que outras químicas de lítio |
| **Íon de lítio (NMC/NCA)** | Montagens em que o peso é decisivo | Menos tolerante ao calor e a descargas profundas, com vida em ciclos menor |
| **Chumbo-ácido selada (AGM/gel)** | Montagens de baixo custo ou solução temporária com material já disponível | Pesada, menor capacidade útil e a vida em ciclos mais curta das três |

**[A comparação de químicas de baterias secundárias da Battery University](https://www.batteryuniversity.com/article/bu-107-comparison-table-of-secondary-batteries) explica melhor as diferenças entre vida em ciclos e energia específica.** *A LiFePO4 se destaca: tolera calor, abuso e descarga completa muito melhor do que as outras duas químicas, exatamente o que um gabinete pode enfrentar em campo.*

O calor prejudica qualquer química. **[A pesquisa da Battery University sobre perda de capacidade de baterias de íon de lítio](https://www.batteryuniversity.com/article/bu-808b-what-causes-li-ion-to-die) documenta perdas reais bem acima das classificações de laboratório quando calor e recargas rápidas entram em cena.** Por isso, esta série recomenda planejar uma autonomia abaixo da nominal em climas quentes.

## Alimentação de dispositivos por USB-C PD

Muitos thin clients, pontos de acesso e periféricos em montagens compactas já recebem energia por **USB-C com a especificação [USB Power Delivery (USB PD)](https://www.usb.org/document-library/usb-power-delivery)**, simplificando bastante o kit de campo.

- **Um carregador portátil USB PD substitui vários adaptadores específicos**, reduzindo os cabos e adaptadores transportados no gabinete.
- **Confirme a potência negociada pelo dispositivo em uso**, não apenas o máximo informado para o cabo. Uma fonte PD insuficiente pode reduzir o desempenho ou deixar de carregar durante o uso, sem aviso claro.
- **Leve um cabo PD compatível com a maior potência do kit.** Um cabo barato, próprio apenas para carga e limitado a 60 W, restringe um dispositivo de 100 W sem indicar claramente o problema.

*USB-C PD não substitui o dimensionamento do UPS e do banco de baterias descrito acima. É uma opção prática para periféricos menores, não a arquitetura principal de energia do gabinete.*

## Monitore o UPS em vez de adivinhar

**Um UPS que mudou para a bateria sem aviso há uma hora não protege nada se ninguém perceber antes de a carga acabar.** A maioria dos UPS informa o estado por USB ou por uma placa de rede. Uma montagem em campo deve ler esse estado.

- **[Network UPS Tools (NUT)](https://networkupstools.org/) é um projeto de código aberto compatível com bem mais de mil modelos de UPS** e oferece ferramentas comuns de monitoramento e controle, independentemente do protocolo do fabricante.
- **Configure o desligamento automático e ordenado do computador quando a bateria atingir um limite definido.** Não deixe o UPS descarregar até cortar a energia de um sistema de arquivos ativo.
- **Registre tendências de saúde da bateria e autonomia**, não apenas a porcentagem de carga atual. Uma bateria que perde capacidade aos poucos não mostra sintomas claros até falhar.

*Um UPS sem monitoramento é uma bateria com data de validade desconhecida.* Configurar o NUT ou a ferramenta equivalente do fabricante leva uma tarde e remove essa incerteza das implantações futuras.

## Sincronização de horário sem internet

**O horário correto importa ainda mais em campo do que muitas montagens consideram.** Ele afeta a correlação de registros, a validade de certificados, conexões de túneis criptografados e qualquer evidência com data e hora produzida pela implantação.

- **Um servidor NTP local dentro do gabinete**, sincronizado com um receptor GPS ou uma fonte stratum 1 quando houver internet, mantém todos os dispositivos no mesmo horário mesmo durante interrupções de conectividade.
- **Relógios sincronizados por GPS funcionam sem internet**, o que importa nos cenários de malha e de conexão reserva via satélite tratados mais adiante na série.
- **Um relógio atrasado alguns minutos pode impedir a validação de certificados TLS e o estabelecimento de conexões VPN.** Uma falha de rede aparente pode ser um problema de horário que ninguém verificou.

**A [especificação NTP versão 4, RFC 5905](https://www.ietf.org/rfc/rfc5905.txt), define o protocolo usado pela maioria dessas ferramentas.** A descoberta dinâmica de servidores permite que um pequeno servidor NTP no gabinete atenda aos outros dispositivos com pouca configuração.

## Classificações ambientais IP e NEMA

Dois sistemas de classificação indicam se um gabinete ou dispositivo suporta o ambiente previsto. **Nenhum deles significa simplesmente “robusto”. Ambos usam valores específicos e testáveis.**

O **[código IP (Ingress Protection)](https://en.wikipedia.org/wiki/IP_Code)**, definido pela norma IEC 60529, usa dois dígitos: o primeiro indica proteção contra partículas sólidas, como poeira, e o segundo contra líquidos, como água.

| Classificação IP | Significado |
|---|---|
| **IP54** | Protegido contra poeira e respingos de água vindos de qualquer direção |
| **IP65** | À prova de poeira e protegido contra jatos de água de baixa pressão |
| **IP67** | À prova de poeira e protegido contra imersão temporária de até 1 metro |
| **IP68** | À prova de poeira e protegido contra imersão contínua além de 1 metro, conforme profundidade e duração especificadas pelo fabricante |

O **[sistema NEMA de classificação de gabinetes](https://en.wikipedia.org/wiki/NEMA_enclosure_types)**, comum em equipamentos industriais norte-americanos, usa números de tipo em vez de pares de dígitos. **NEMA 3R** serve para exposição geral ao clima externo. **NEMA 4X** acrescenta proteção contra água e corrosão para ambientes costeiros ou de lavagem. **NEMA 6P** cobre submersão temporária.

*Escolha a classificação conforme o risco real do local, não pelo maior número disponível.* Um gabinete IP68 para uso no deserto sem exposição à água desperdiça dinheiro que serviria melhor para refrigeração ou capacidade de bateria.

## Temperatura, vibração e umidade

Além de poeira e água, três fatores ambientais danificam silenciosamente os eletrônicos em campo.

- **Temperaturas extremas** reduzem a vida útil das baterias e limitam ou desligam computadores. Confira a faixa de operação na ficha técnica de cada componente, não apenas na do gabinete.
- **Vibrações** soltam conectores e desgastam juntas de solda em viagens repetidas. Suportes de isolamento de borracha entre a bandeja de computação e o gabinete absorvem a vibração antes de chegar ao hardware.
- **Umidade e condensação** aparecem quando o gabinete passa de um veículo frio para ar quente e úmido. Em grandes variações de temperatura, deixe o gabinete fechado se aclimatar por alguns minutos antes de abrir. Considere colocar um pequeno sachê dessecante em gabinetes vedados.

## Aterramento e proteção contra surtos

Fontes de energia em campo, especialmente geradores, são menos estáveis e previsíveis do que a rede elétrica. **Em um local de campo, não há um eletricista do prédio para impedir que um surto ou falha de aterramento alcance seus equipamentos.**

- **Faça o aterramento adequado** do gabinete e de quaisquer trilhos metálicos antes de conectar a energia. Use uma haste de aterramento ou o aterramento do chassi do veículo, conforme o caso.
- **Use um dispositivo de proteção contra surtos compatível com a fonte de energia**, pois geradores podem produzir picos diferentes dos da rede elétrica estável.
- **Mantenha o UPS entre a fonte de energia bruta e os equipamentos**, e não no sentido inverso. Assim, a proteção contra surtos do UPS recebe primeiro a energia mais irregular.

*Pular o aterramento para economizar cinco minutos de montagem coloca todo o equipamento do gabinete em risco.*

## Lista de verificação de energia e ambiente

- [ ] UPS ou banco de baterias dimensionado com margem de 1,5 a 1,6 sobre a potência total
- [ ] Pelo menos um dia completo de autonomia sem fonte de recarga
- [ ] Classificação IP ou NEMA adequada ao risco real do local
- [ ] Faixa de temperatura de cada componente verificada, não apenas a do gabinete
- [ ] Isolamento contra vibrações instalado para transporte longo ou fora de estrada
- [ ] Aterramento adequado antes de conectar gerador ou energia de campo

## Próximas etapas

Com a energia e a proteção ambiental planejadas, a próxima questão é como a implantação se conecta ao mundo externo e mantém os dados seguros. Continue em [parte três: conectividade e segurança de dados para nós de borda](/articles/field-deployable-connectivity-and-data-security-for-edge-nodes/).

Se ainda não leu, [parte um: seleção de hardware e gabinete](/articles/field-deployable-edge-compute-hardware-and-enclosure-selection/) aborda as escolhas de computador e gabinete às quais este plano de energia precisa se adaptar. [A parte quatro](/articles/field-it-tidbits-beyond-the-mini-datacenter/) reúne detalhes menores que complementam os pontos acima.

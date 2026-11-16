---
title: "Dimensione um nobreak para seu homelab e teste o desligamento automático"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Meça o consumo do homelab, compare os limites em watts e VA do nobreak, confira o tempo de autonomia com sua carga e teste um desligamento seguro antes de confiar na bateria."
genre: ["Laboratório doméstico", "Proteção de energia", "Administração de sistemas"]
tags: ["nobreak para homelab", "dimensionamento de nobreak", "autonomia do nobreak", "desligamento automático", "Network UPS Tools", "watts do nobreak", "VA do nobreak", "fator de potência", "backup por bateria", "desligamento de servidor", "desligamento de NAS", "falta de energia", "teste de nobreak", "curva de autonomia", "medidor de potência", "monitoramento de nobreak", "troca de bateria", "proteção contra surtos", "desligamento organizado", "energia do homelab"]
cover: "/img/cover/ups-runtime-sizing-shutdown-test.webp"
coverAlt: "Um nobreak do homelab alimenta um servidor, um NAS, um roteador e um switch acima de uma linha do tempo entre a queda de energia e o desligamento."
coverCaption: "Meça a carga, verifique a autonomia e teste o desligamento antes de uma queda de energia."
---

Um **nobreak**, ou sistema de alimentação ininterrupta, dá tempo ao homelab para salvar o trabalho e desligar os sistemas durante uma queda de energia. A etiqueta, sozinha, não informa por quanto tempo os servidores funcionarão. Você precisa conhecer a carga dos equipamentos, os limites em watts e VA do nobreak, a autonomia estimada para essa carga e um procedimento de desligamento testado.

## Pontos principais

- **Meça a carga:** Registre o consumo normal e o consumo alto em watts de cada equipamento que deve continuar ligado à bateria.
- **Confira os dois limites:** O nobreak precisa atender aos requisitos de watts e VA dos equipamentos conectados.
- **Consulte a curva de autonomia:** O tempo depende da carga e do estado da bateria. Use uma estimativa específica do modelo.
- **Teste a finalização:** Verifique se o sinal do nobreak chega a cada host e se todos param antes de a bateria acabar.

## Antes de começar

Você precisa de um medidor de potência adequado à rede elétrica local, uma lista de dispositivos e fontes de alimentação e acesso às especificações e à curva de autonomia de cada modelo de nobreak considerado. Para testar o desligamento automático, também precisa de uma conexão USB ou de gerenciamento de rede compatível e do software para cada host. Reserve tempo para medir a carga normal, observar uma carga alta e realizar um teste de manutenção planejado. Esta é uma tarefa intermediária de homelab, pois um teste completo de desligamento interrompe os serviços.

O [guia de filtros de linha contra surtos](/articles/protecting-your-tech_-the-best-surge-protectors/) do site trata da proteção contra surtos. A [seleção de modelos de nobreak](/articles/best-ups-models-for-uninterrupted-connectivity/) lista produtos. Este guia explica como dimensionar e verificar a sua própria carga. Tanto o [guia de dimensionamento da Eaton](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html) quanto o [guia de compra da Schneider Electric](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/) distinguem a capacidade de saída do tempo de autonomia da bateria.

> **Aviso:** Use apenas as tomadas e cargas aprovadas pelo fabricante do nobreak. Mantenha o teste dentro da capacidade nominal. Um teste real de desligamento para o laboratório conectado.

## Meça o que precisa continuar ligado

Decida quais equipamentos precisam funcionar até o desligamento. Inclua o hypervisor, o armazenamento, o switch de rede e o roteador se algum host depender do acesso à rede para receber o sinal de desligamento. Deixe monitores, impressoras e outras cargas opcionais fora das tomadas alimentadas por bateria, a menos que seu plano precise delas.

Meça na tomada o grupo previsto para ficar na bateria. Registre os **watts em operação normal** e o maior valor observado durante tarefas representativas, como iniciar hosts ou máquinas virtuais. A etiqueta de uma fonte informa a capacidade, não o consumo medido do sistema. Ainda assim, verifique nas etiquetas dos equipamentos os limites de entrada e de corrente de partida. Anote as condições de medição na sua planilha.

| Dispositivo | Watts normais | Pico observado em watts | Tomada com bateria? |
|---|---:|---:|---|
| **Roteador e switch** | 30 | 35 | Sim |
| **NAS** | 60 | 90 | Sim |
| **Servidor pequeno** | 90 | 135 | Sim |
| **Total ilustrativo** | **180** | **260** | Três dispositivos |

Os valores acima são **ilustrativos**, não medições de um laboratório específico. A carga muda conforme discos, GPUs, configurações de energia e equipamentos conectados. Meça novamente depois de alterações importantes no hardware.

## Avalie potência ativa e potência aparente

**Watts** descrevem a potência real usada pelos equipamentos. **Volt-ampères (VA)** descrevem a potência aparente. A relação depende do **fator de potência**: watts divididos pelo fator de potência resultam em VA. A Eaton explica esse cálculo no [guia de dimensionamento](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/ups-sizing-guide.html). Não interprete uma etiqueta de 1000 VA como 1000 watts. Confira a classificação separada em watts do nobreak.

Para o pico ilustrativo de 260 W, uma margem de capacidade de 25% resulta em **325 W**. A Schneider Electric recomenda uma capacidade de saída cerca de [20% a 25% acima da carga](https://www.se.com/us/en/work/support/product-support/ups-buying-guide-for-selecting-a-battery-backup-system/). Escolha um nobreak cuja potência contínua em watts supere o pico planejado mais a margem. Se você conhece o fator de potência combinado, divida os watts de pico por esse fator para estimar os VA de pico e aplique a margem escolhida aos VA também. Caso contrário, use um medidor adequado ou o seletor do fabricante para descobrir o requisito de VA e a folga necessária. Não invente um fator de potência que não mediu.

A margem de capacidade não determina a autonomia. Um nobreak com limite alto em watts e bateria pequena pode manter a carga por pouco tempo. Antes de escolher o modelo, confira as tomadas, o tipo de plugue, a tensão de entrada, a interface de comunicação e a possibilidade de trocar a bateria.

## Defina uma meta de autonomia

Anote quanto tempo o laboratório precisa para parar com segurança. Inclua o tempo para o alerta chegar aos hosts, as máquinas virtuais pararem, o armazenamento concluir as gravações e o nobreak desligar a saída. Acrescente uma reserva para um desligamento lento e uma bateria mais antiga. Um laboratório que precisa atravessar interrupções curtas exige uma meta diferente de outro que só precisa desligar corretamente.

Como **exemplo**, suponha que um desligamento testado leve 6 minutos e que você escolha 5 minutos de reserva. A autonomia necessária na carga esperada é de pelo menos 11 minutos. Este é um exemplo de planejamento, não um limite universal. Compare a meta com a curva ou o seletor do modelo candidato na sua **carga normal e alta medida**. Reavalie o resultado conforme a bateria envelhece. O [seletor de nobreaks da Schneider Electric](https://www.se.com/us/en/work/products/tools/ups-selector/) calcula a autonomia com base na carga informada e nas especificações do modelo. A Eaton também direciona os compradores aos dados específicos de cada modelo no [guia de nobreaks para desktop](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Copie esta **planilha** para seu laboratório. Preencha as linhas dos dispositivos com as leituras do medidor de potência. Some os watts normais e altos, acrescente a margem escolhida ao total alto e aplique a mesma margem aos VA de pico medidos ou calculados. Compare os dois resultados com um nobreak candidato. Se usar um seletor do fabricante, registre o resultado de dimensionamento em VA e a folga. Use a curva do modelo para estimar a autonomia. Complete as linhas de tempo e recuperação durante o teste.

| Campo | Seu resultado |
|---|---|
| **Dispositivos e tomadas com bateria** | Nomes dos dispositivos e tomada atribuída a cada um |
| **Watts normais por dispositivo e no total** | Valores medidos e soma |
| **Watts altos por dispositivo e no total** | Maiores valores observados e soma |
| **Fator de potência medido ou especificado** | Valor e fonte, ou “desconhecido” |
| **VA de pico medidos ou calculados** | Watts de pico divididos pelo fator de potência combinado, se conhecido |
| **Margem de capacidade** | Percentual escolhido e watts/VA após a margem |
| **Classificações do nobreak candidato** | Modelo, watts e VA de saída e limites das tomadas |
| **Meta de autonomia e estimativa pela curva** | Minutos necessários e estimativa do modelo para sua carga |
| **Horários de alerta e desligamento** | Hora do alerta de bateria e parada do último host |
| **Resultado da recuperação** | Inicialização do host, armazenamento, aplicativos e monitoramento |

Se o fator de potência for desconhecido, use a ferramenta de seleção do fabricante ou meça a potência aparente com um medidor apropriado. Não informe VA calculado com base em um fator estimado. A planilha só está completa quando o modelo atende aos dois limites de saída e a autonomia prevista supera sua meta de desligamento.

> **Resultado esperado:** Sua planilha identifica os dispositivos conectados, as cargas medidas, os limites em watts e VA do nobreak, a meta de autonomia e a estimativa específica do modelo.

## Planeje o desligamento automático

Um nobreak mantém os equipamentos ligados temporariamente. O host ainda precisa de um **sinal de desligamento**. Verifique se o nobreak oferece USB, placa de gerenciamento de rede ou outra interface compatível. Confirme que cada host que precisa parar tem um caminho de monitoramento compatível. A Eaton informa que muitos modelos aceitam comunicação USB ou de rede para um [desligamento organizado de NAS ou servidor](https://www.eaton.com/us/en-us/products/backup-power-ups-surge-it-power-distribution/backup-power-ups/desktop-ups-buying-guide.html).

Em um laboratório Linux com **Network UPS Tools (NUT)**, o driver lê o nobreak, `upsd` compartilha o estado e `upsmon` aciona o desligamento do host quando a alimentação fica crítica. Um host conectado diretamente a um nobreak USB ou serial costuma executar o driver, `upsd` e `upsmon` no modo **Primary**. Os outros hosts executam `upsmon` no modo **Secondary** em relação a esse servidor. Um nobreak com gerenciamento de rede precisa de um driver compatível e de uma configuração primária específica do modelo. O [guia de topologia do NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s02.html) explica essas funções. Configure o roteador e o switch para que os hosts de monitoramento permaneçam conectados durante o uso da bateria. Restrinja o comando de desligamento e suas permissões aos administradores.

Antes de testar o desligamento, verifique se o driver informa o estado atual. Substitua `myupsname` pelo nome do nobreak na configuração do NUT:

```bash
upsc myupsname@localhost ups.status
```

O [guia de configuração do NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) espera `OL` para alimentação normal da rede e explica `OB` para o funcionamento com bateria. Execute a verificação de estado em cada host que monitora o nobreak e use o nome de servidor correto para clientes remotos. Uma leitura antiga ou ausente significa que o caminho do sinal precisa de reparo antes do teste.

Registre a **ordem de desligamento**. Por exemplo, pare primeiro as VMs de aplicativos, depois os clientes de armazenamento e, por fim, o hypervisor e o NAS. Verifique se cada serviço e sistema de arquivos se recupera normalmente quando a energia volta. Um host que para corretamente sem a recuperação saudável dos aplicativos não representa um resultado completo.

## Teste sem adivinhar

Comece com uma **simulação** no host em que o driver do nobreak está configurado. O NUT documenta `upsdrvctl -t shutdown` como uma prévia da sequência de desligamento do driver; o comando não aciona os drivers nem corta a energia:

```bash
upsdrvctl -t shutdown
```

Essa **simulação do driver** não prova que um alerta de queda de energia chegue a todos os hosts. Confira cada serviço de monitoramento e seus logs. Em uma janela de manutenção, o [guia de teste de desligamento do NUT](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html) descreve um teste forçado com `upsmon -c fsd` no host NUT primário. Esse **teste FSD** inicia uma sequência real de desligamento. O sinalizador FSD continua ativo até o `upsd` ser reiniciado. Depois que os sistemas voltarem, confirme que o `upsd` reiniciou e que o estado não mostra mais FSD antes de confiar novamente no monitoramento. Leia o [manual atual do upsmon](https://networkupstools.org/docs/man/upsmon.html), prepare um meio de recuperação e só teste depois de salvar o trabalho e avisar os usuários do laboratório.

Para um **teste controlado do evento de bateria**, siga primeiro o procedimento do fabricante do nobreak com cargas não críticas. O teste com carga baixa verifica a entrega do sinal, mas não comprova a autonomia do laboratório. Mais tarde, em uma janela de manutenção, teste uma carga na bateria representativa da carga planejada. Alguém deve observar o nobreak e poder restabelecer a energia da rede se a margem diminuir. Registre a carga exibida pelo nobreak, a hora em que ele informa o funcionamento com bateria, o início do desligamento de cada host e a hora em que o último para. Confirme que a bateria não acaba antes da parada dos hosts. Quando a energia voltar, verifique a inicialização dos hosts, a saúde dos aplicativos, a integridade do armazenamento e o estado do monitoramento. O NUT considera bem-sucedida a sequência que para o sistema operacional antes de a bateria acabar e retoma a operação quando a energia retorna.

| Verificação | O que registrar |
|---|---|
| **Caminho do sinal** | Evento do nobreak visível em cada host de monitoramento |
| **Tempo de desligamento** | Último host parou antes do esgotamento da bateria |
| **Recuperação** | Hosts, armazenamento e aplicativos iniciaram corretamente |
| **Capacidade** | Carga do nobreak dentro dos limites em watts e VA |

## Solução de problemas

- **Alarme de sobrecarga do nobreak:** Remova cargas opcionais. Compare a carga alta medida com os dois limites do nobreak e os limites das tomadas do modelo.
- **Autonomia menor que o esperado:** Confira a carga atual, a idade da bateria, os dados específicos do modelo e os resultados dos testes recentes. Não extrapole linearmente usando apenas VA.
- **Um host continua ligado:** Verifique o serviço de monitoramento, o caminho de rede, as permissões de desligamento e os logs.
- **Os hosts param, mas não voltam:** Confira o comportamento da saída do nobreak quando a energia retorna, a configuração de retorno de energia do firmware e as [considerações do NUT sobre disputa de energia](https://networkupstools.org/docs/user-manual.chunked/ar01s06.html).
- **A simulação funciona, mas o teste de queda falha:** A prévia do driver verifica um caminho menor. Inspecione a entrega do evento e a ordem real de desligamento dos hosts.

## Próximas etapas

Guarde a planilha com o inventário do homelab. Meça a carga novamente quando adicionar hardware e repita o teste de desligamento depois de mudanças no nobreak, no software de monitoramento, na política de inicialização do host ou na pilha de armazenamento. Verifique separadamente o plano de backup e restauração. A bateria protege a janela de desligamento, enquanto um [backup de homelab testado](/articles/what-is-a-homelab-and-should-you-have-one/) protege seus dados de outras falhas.

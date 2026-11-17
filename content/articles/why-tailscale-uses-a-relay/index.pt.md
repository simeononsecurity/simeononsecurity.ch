---
title: "Por que o Tailscale usa um relay: conexões diretas, DERP e relays de pares"
date: 2026-09-11
lastmod: 2026-11-07
toc: true
draft: false
description: "Saiba por que o Tailscale usa um relay, como ler as saídas de status e netcheck e quando investigar uma conexão DERP ou por relay de pares."
genre: ["Networking", "Network Security", "Self-Hosted"]
tags: ["Tailscale", "relay do Tailscale", "DERP", "relay de pares do Tailscale", "conexão direta", "WireGuard", "travessia de NAT", "NAT difícil", "CGNAT", "UDP", "tailscale status", "tailscale ping", "tailscale netcheck", "MappingVariesByDestIP", "desempenho de VPN", "acesso remoto", "tailnet", "rede de laboratório doméstico", "latência do relay", "criptografia ponta a ponta"]
cover: "/img/cover/why-tailscale-uses-a-relay.webp"
coverAlt: "Dois laptops em ilhas separadas trocam pacotes criptografados por um relay central enquanto uma rota direta está interrompida."
coverCaption: ""
---

**O Tailscale usa um relay** quando os dispositivos não estabelecem uma conexão direta. Uma conexão DERP breve durante a inicialização é normal. O uso persistente de um relay costuma refletir condições de NAT ou do firewall que afetam a rota entre os dispositivos. Conexões diretas, DERP e relays de pares mantêm a criptografia ponta a ponta do WireGuard. [Tipos de conexão do Tailscale](https://tailscale.com/docs/reference/connection-types).

## Pontos principais

- **Reconheça a rota:** diferencie conexões diretas, DERP e relays de pares.
- **Reúna evidências:** execute sondas específicas para o par e verificações de rede nas duas pontas.
- **Analise o padrão:** compare pares de dispositivos e condições de rede.
- **Escolha uma mudança:** justifique-a com uma carga de trabalho medida e um novo teste.

## Antes de começar

**Pré-requisitos:** dois dispositivos inscritos e online, além de um terminal com a interface de linha de comando do Tailscale, ou **CLI**. O acesso administrativo só é necessário se a investigação levar a uma alteração de configuração.

**Tempo estimado:** cinco minutos para as verificações básicas e mais 15–20 minutos para o exercício de comparação. **Dificuldade:** iniciante para observação e intermediária para mudanças de rede. Defina o problema primeiro, como um backup lento ou uma resposta atrasada do terminal.

## Conexões diretas, DERP e relay de pares

Um **tailnet** é sua rede Tailscale. Os dispositivos tentam estabelecer conectividade UDP direta. Os relays ficam disponíveis quando a rota direta falha. O Tailscale verifica novamente as opções de conexão periodicamente. [Estabelecimento de conexão](https://tailscale.com/docs/reference/connection-types).

| Rota | Caminho do tráfego | Implicação típica |
|---|---|---|
| **Direta** | Entre os dois dispositivos | Geralmente é a rota preferida para obter desempenho |
| **Relay DERP** | Pela infraestrutura de relays do Tailscale | Acrescenta um intermediário quando o acesso direto falha |
| **Relay de pares** | Por um dispositivo configurado no tailnet | Uma opção alternativa sob sua administração |

O **desempenho do DERP** depende em parte da rota adicional e da capacidade compartilhada do serviço. O Tailscale documenta limites de throughput para distribuir os recursos DERP com justiça. Não existe uma velocidade universal de relay que permita prever o tempo de transferência de arquivos. [Solução de problemas de desempenho do Tailscale](https://tailscale.com/docs/reference/troubleshooting/poor-performance-tailnet).

## Entenda a negociação da conexão

A **travessia de NAT** é o processo de estabelecer uma rota utilizável através de dispositivos que traduzem endereços. O Tailscale inicia a comunicação pelo DERP enquanto negocia uma rota direta. Se a conectividade direta falhar, um relay de pares configurado e disponível oferece outra opção. O Tailscale verifica as opções novamente ao longo do tempo. [Estabelecimento de conexão](https://tailscale.com/docs/reference/connection-types).

**NAT difícil** descreve um comportamento de mapeamento que complica a travessia. As condições nas duas pontas importam. Dois dispositivos atrás de roteadores diferentes não necessariamente se comportam da mesma forma, mesmo que as duas redes usem endereços privados. [Conectividade de dispositivos](https://tailscale.com/docs/reference/device-connectivity).

Para **um laptop em deslocamento**, a rota para o servidor doméstico pode mudar ao sair do Wi-Fi de casa e entrar na rede de um hotel. Registre a rede usada durante a observação. Uma conexão direta de ontem não comprova qual é a rota de hoje.

## Verifique a conexão atual

Substitua **`home-server`** pelo nome Tailscale ou endereço do seu par:

```bash
tailscale ping home-server
tailscale status
tailscale netcheck
```

**`tailscale ping`** verifica a conectividade com o par indicado. **`tailscale status`** lista os pares e os detalhes da conexão. **`tailscale netcheck`** informa as condições de rede do dispositivo em que o comando é executado. A [referência da CLI do Tailscale](https://tailscale.com/docs/reference/tailscale-cli) documenta esses comandos.

| Indicador da saída | Interpretação |
|---|---|
| **`direct`** | O tráfego para esse par usa uma rota direta |
| **`relay`** | O tráfego para esse par passa pelo DERP |
| **`peer-relay`** | O tráfego usa um relay de pares configurado |
| **Um pong DERP inicial** | Confira os resultados seguintes antes de concluir que a rota continuou pelo relay |

Esses rótulos aparecem na [documentação dos tipos de conexão](https://tailscale.com/docs/reference/connection-types). **Gere tráfego primeiro** e depois inspecione o par desejado. Os comandos acima são exemplos, não resultados registrados de um benchmark.

## Interprete uma mudança de rota

Esta **sequência ilustrativa** omite endereços e horários para destacar a mudança de conexão:

```text
Primeira resposta:    via DERP
Resposta posterior:   por um endpoint direto
Status posterior:     direto
```

**Interpretação:** a negociação funcionou durante essa observação. A primeira resposta isolada levaria a um diagnóstico incorreto. Se as respostas seguintes e o status ainda indicarem um relay, registre o uso persistente do relay para esse par de dispositivos e período de teste.

**Escopo da sonda:** um ping do Tailscale bem-sucedido confirma a conectividade com o par para aquela sonda. Não prova que seu painel, serviço de arquivos ou daemon SSH aceite o tráfego da aplicação. Teste separadamente a aplicação com falha antes de declarar que o problema foi resolvido.

## O que o netcheck informa

Execute **`tailscale netcheck` nos dois dispositivos**. Compare estes campos com a [referência de conectividade de dispositivos](https://tailscale.com/docs/reference/device-connectivity):

| Campo | Interpretação útil |
|---|---|
| **`UDP`** | Se a sonda observou conectividade UDP de saída |
| **`MappingVariesByDestIP`** | Mapeamentos externos variáveis podem indicar dificuldade na travessia de NAT |
| **`IPv6`** | Se o dispositivo tem conectividade IPv6 utilizável |
| **`PortMapping`** | Se há um mecanismo compatível de mapeamento de portas disponível |

**Um campo sozinho não dá um veredito.** A disponibilidade de um mecanismo de mapeamento não prova que uma rota específica até um par funcione. O rótulo de relay também não identifica qual roteador causou o problema. Compare as duas pontas e os resultados reais de ping.

O **NAT da operadora** importa quando a tradução de endereços na rede do provedor está fora do seu controle, como explicamos no artigo sobre [redirecionamento de portas do T-Mobile Home Internet](/articles/t-mobile-home-internet-port-forwarding/). Não suponha que toda conexão atrás do NAT da operadora tenha o mesmo comportamento de travessia.

## Compare três pares de dispositivos

Se houver um disponível, use um **terceiro dispositivo inscrito** para reunir mais evidências. O padrão abaixo é hipotético, não um resultado medido:

| Par de dispositivos | Rota observada |
|---|---|
| **Laptop para servidor doméstico** | DERP |
| **Laptop para outro servidor** | Direta |
| **Servidor doméstico para outro servidor** | DERP |

**Hipótese de trabalho:** priorize a rede do servidor doméstico, pois as duas rotas observadas que o envolvem continuaram usando um relay. Isso é uma pista, não uma prova. Cada par negocia de forma independente e o servidor de comparação tem suas próprias condições de rede.

**Próxima observação:** colete a saída de netcheck nos três dispositivos e repita o teste entre o laptop e o servidor doméstico a partir de outra rede sob seu controle. Se a rota mudar, registre exatamente qual rede mudou. Não atribua o resultado a uma regra específica do firewall antes de testá-la.

**Exercício:** a conexão entre o laptop e o servidor doméstico é direta, mas a transferência de arquivos continua lenta. Um relay não explica mais essa observação. Antes de mudar as configurações do relay, verifique a conexão de upload subjacente, a carga do servidor, o armazenamento e o comportamento da aplicação.

## Escolha uma mudança direcionada

Comece com um **teste comparativo** em outra rede sob seu controle. Se o mesmo par se conectar diretamente, você terá uma evidência útil sobre a rota de rede original. Revise as restrições de UDP e a configuração de NAT antes de mudar ajustes de DNS ou da aplicação sem relação com o problema.

**Altere uma variável**, repita as verificações e meça a mesma carga de trabalho. Registre a direção da transferência, o tamanho do arquivo, o tempo decorrido e o tipo de conexão. Assim, você diferencia uma rota melhor de uma alteração independente na carga do servidor ou do armazenamento.

As **mudanças no firewall** devem seguir as orientações específicas da plataforma e as evidências coletadas. Abrir uma porta de aplicação para a Internet pública não melhora, por si só, a rota de transporte do Tailscale. Limite as alterações ao tráfego necessário e à rede que você administra. [Orientações de firewall do Tailscale](https://tailscale.com/docs/integrations/firewalls).

| Constatação | Mudança a avaliar |
|---|---|
| **A sonda UDP falha** | Revise as restrições de UDP de saída nessa rede |
| **O mapeamento varia conforme o destino** | Revise o comportamento de NAT nos equipamentos que você administra |
| **Rota direta, aplicação lenta** | Investigue o host, a conexão subjacente e a carga de trabalho |
| **Relay funcional, experiência aceitável** | Mantenha a configuração e documente o valor de referência |

*Prefira uma melhora medida a mudar configurações apenas para remover o rótulo de relay.*

## Avalie um relay de pares

Um **relay de pares** precisa de um host adequado, uma porta UDP acessível e uma política de acesso que permita o uso. Tanto o relay quanto os clientes participantes precisam do Tailscale 1.86 ou posterior. Confira as plataformas de host compatíveis antes de reservar um dispositivo para essa função. [Requisitos de relay de pares](https://tailscale.com/docs/features/peer-relay).

**A localização determina a utilidade.** Um dispositivo atrás do mesmo limite de rede inacessível não ajuda os outros pares até que a porta do relay esteja acessível.

**Custo de manutenção:** alguém precisa manter o relay online, atualizado e com recursos suficientes. Para administração ocasional com latência aceitável, compare esse esforço com o benefício medido. Para transferências grandes e frequentes, meça a carga de trabalho pelo relay proposto antes de adotá-lo.

## Verifique os efeitos do tráfego compartilhado

O **tráfego agregado** merece atenção quando um roteador de sub-rede ou nó de saída transporta várias cargas de trabalho pelo DERP. O Tailscale documenta situações em que muito tráfego retransmitido atrasa o tráfego sensível à latência que compartilha a conexão. [Solução de problemas de NAT difícil](https://tailscale.com/docs/reference/troubleshooting/network-configuration/hard-nat-issues).

**Exercício de comparação:** observe sua sessão interativa antes, durante e depois de um backup grande. Mantenha fixo o par de endpoints e registre a rota em cada etapa. Atrasos durante a transferência justificam investigar a carga compartilhada, mas não provam a causa exata.

**Escolha o próximo teste** com base na observação. Verifique a saturação do link e a carga do host. Em seguida, avalie uma rota direta ou a separação de serviços sensíveis à latência, se a topologia permitir. Não trate um sintoma de DNS como prova automática de erro na configuração de DNS.

## Um relay é um nó de saída?

Um **nó de saída** encaminha o tráfego geral de Internet de um cliente por um dispositivo selecionado do tailnet. Um relay transporta tráfego entre pares do Tailscale. Selecionar um nó de saída não garante uma rota direta até ele. [Documentação de nós de saída](https://tailscale.com/docs/features/exit-nodes).

## Crie um registro de diagnóstico

Guarde um **registro curto de antes e depois** para o problema real:

```text
Data e versões do Tailscale:
Dispositivos de origem e destino:
Redes usadas por cada dispositivo:
Rotas inicial e estabilizada da conexão:
Observações de netcheck nas duas pontas:
Carga de trabalho, direção e tempo decorrido:
Única mudança testada:
Resultado do novo teste:
Decisão de manter ou reverter a mudança:
```

**Critério de conclusão:** o registro associa um sintoma específico às observações, a uma hipótese e a um novo teste medido. “O relay desapareceu” é incompleto se a aplicação continua lenta. “O backup atende ao tempo exigido pelo DERP” é um resultado válido quando o requisito é explícito.

**Use `tailscale netcheck` como evidência, não como veredito.** O comando descreve a rede vista por um dispositivo. A rota estabilizada pertence a um par de dispositivos e a uma carga de trabalho. Antes de mudar as configurações de firewall ou NAT, registre as duas pontas, a última linha de `tailscale status` e a medição da aplicação.

## Próximas etapas

Registre a rota até o par importante e teste a carga de trabalho antes de mudar as configurações de rede. Para saber separadamente quem opera a infraestrutura de coordenação, leia [Tailscale e Headscale em comparação](/articles/tailscale-vs-headscale-comparison-guide/).

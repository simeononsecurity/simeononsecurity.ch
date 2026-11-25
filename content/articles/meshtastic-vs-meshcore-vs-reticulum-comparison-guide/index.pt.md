---
title: "Meshtastic vs. MeshCore vs. Reticulum"
date: 2026-09-01
lastmod: 2026-11-25
toc: true
draft: false
description: "Compare Meshtastic, MeshCore e Reticulum por roteamento, tempo de transmissão, infraestrutura, transporte e casos de uso offline."
genre: ["LoRa", "Redes mesh", "Comunicação fora da rede", "Comunicação de emergência", "Radioamadorismo", "Código aberto", "Preparação para desastres", "Redes sem fio", "Privacidade", "Redes"]
tags: ["meshtastic vs meshcore vs reticulum", "rede Reticulum", "meshtastic", "meshcore", "reticulum", "lxmf", "rede mesh LoRa", "comunicação fora da rede", "rnode", "rádio por pacotes", "rede independente de transporte", "redes mesh", "comunicação de emergência", "rede mesh comunitária", "tempo de transmissão LoRa", "flooding gerenciado", "limite de saltos", "nó repetidor", "servidor de sala", "aplicativo Sideband", "nomadnet", "meshchat", "comunicação em desastres", "rádio fora da rede", "protocolo de rede mesh", "rede mesh regional", "engenharia de RF"]
cover: "/img/cover/meshtastic-meshcore-reticulum-network-comparison.webp"
coverAlt: "Ilustração que compara três sistemas de rede mesh com nós, antenas e linhas de conexão sobre um fundo escuro e colorido, representando seus recursos distintos."
coverCaption: ""
ref: ["/articles/meshcore-vs-meshtastic-comparison-guide", "/articles/field-deployable-connectivity-and-data-security-for-edge-nodes"]
---

## A resposta curta

**Esses três projetos não resolvem o mesmo problema.** Meshtastic e MeshCore são sistemas de rede mesh LoRa com filosofias de roteamento diferentes. Reticulum tem um escopo mais amplo. É uma camada de rede independente do transporte que funciona ao mesmo tempo por LoRa, rádio por pacotes, Wi-Fi, Ethernet, conexões seriais e internet.

**A pergunta certa não é "qual é o melhor?"** É "qual arquitetura se encaixa na rede que quero construir?"

*Meshtastic combina com redes ad hoc e usuários em movimento.* **MeshCore combina com uma infraestrutura fixa e planejada.** **Reticulum combina com redes que precisam conectar transportes diferentes ou unir redes que, de outra forma, seriam separadas.** A maioria das pessoas que constrói uma única rede LoRa regional precisa apenas de uma das duas primeiras opções.

______

## Defina a rede que você está construindo

Antes de comparar os protocolos, anote o que a rede precisa fazer. Um objetivo útil para a maioria das implantações comunitárias e de comunicação de emergência é:

- **Operação sem licença**, para qualquer pessoa participar sem licença de radioamador
- **Hardware de baixo custo**, acessível para uma comunidade implantar em grande escala
- **Baixo consumo de energia**, idealmente sustentável com energia solar ou bateria
- **Comunicação de longo alcance** sem depender de rede celular ou internet
- **Independência da infraestrutura**, da rede elétrica, dos provedores de internet e das operadoras
- **Fácil o bastante para quem não é especialista em rádio** configurar e usar
- **Adequada para uma comunidade**, não apenas para o porão de um operador
- **Capaz de crescer além de poucos nós** sem entrar em colapso
- **Útil durante falhas de infraestrutura**, quando torres celulares e internet ficam fora do ar
- **Entrega confiável acima de distância recorde**

Tenha esta lista em mente durante o restante do artigo. Vamos avaliar cada decisão de arquitetura segundo esses requisitos.

______

## Meshtastic

**Meshtastic** é a opção mais madura e mais usada. Ela oferece muitos recursos para o usuário médio.

- **Ecossistema maduro** com anos de desenvolvimento ativo
- **Grande comunidade**, Discord ativo e documentação abrangente
- **Amplo suporte de hardware** para placas LILYGO, Heltec, RAK e Seeed
- **Bons aplicativos móveis** para iOS e Android
- **Fácil de começar**, a configuração inicial leva menos de 20 minutos
- **Bom suporte a usuários portáteis e em movimento** que entram e saem da rede de forma imprevisível
- **Recursos de GPS e telemetria** com um ecossistema desenvolvido ao redor deles
- **Implantações existentes** na maioria das áreas metropolitanas facilitam a adoção, pois você entra em uma rede em vez de construí-la do zero

Para ver uma análise completa do roteamento, da compatibilidade de hardware e da configuração do Meshtastic em comparação com o MeshCore, consulte o **[guia comparativo entre MeshCore e Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)**. Este artigo se concentra na questão de arquitetura mais importante para implantações maiores: **flooding gerenciado e limites de saltos**.

### Flooding gerenciado e por que os saltos importam

Na **[inundação gerenciada](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** do Meshtastic, um cliente comum cancela uma retransmissão pendente se ouvir primeiro o mesmo pacote retransmitido. `ROUTER` e `ROUTER_LATE` ainda podem retransmitir. Para `CLIENT_BASE`, a exceção vale para tráfego de ou para um nó favorito.

O contador de saltos do Meshtastic começa em **3** por padrão e admite no máximo **7**. A partir do firmware 2.7.11, a infraestrutura elegível pode [preservar o contador](https://meshtastic.org/blog/zero-cost-hops-favorite-routers/) depois do primeiro salto se o retransmissor anterior for um `ROUTER` ou `ROUTER_LATE` favorito. Cada retransmissão real ainda ocupa o canal.

Um limite maior pode alcançar mais repetidores, mas não obriga todos os receptores a transmitir. **Mais encaminhamentos** podem gerar:

- **Mais tempo de transmissão** por mensagem
- **Mais cópias no ar** quando vários repetidores elegíveis encaminham o mesmo pacote
- **Mais contenção** pelo canal compartilhado
- **Maior risco de colisão** quando mais rádios transmitem na mesma janela
- **Maior consumo de bateria** em cada nó que recebe e retransmite
- **Menos capacidade disponível no canal** para o tráfego real de mensagens

A capacidade do LoRa é limitada pelo tempo de transmissão e pelos limites regionais de ciclo de trabalho, não pela quantidade de nós. Uma rede com dez nós ativos que transmitem GPS e telemetria com frequência pode saturar um canal que cinquenta sensores silenciosos quase não usariam. Por isso, uma rede mesh densa com limite alto de saltos se degrada mais rápido que outra com a mesma quantidade de nós, limite menor e intervalos de telemetria controlados.

Desde o Meshtastic 2.6, as **mensagens diretas** usam inundação para descobrir a rota e depois tentam usar o próximo salto aprendido. Se ele falhar, podem voltar à inundação.

Em uma rede pequena ou média, como a de um clube de caminhada, isso raramente importa. Em uma **rede regional projetada para cobrir uma cidade ou várias localidades**, torna-se a principal restrição de projeto.

______

## MeshCore

Os **repetidores dedicados** formam a camada fixa de encaminhamento do MeshCore. Os rádios clientes são terminais.

### Funções dos nós

As implantações do MeshCore se organizam em torno de funções distintas, não em um conjunto plano de nós equivalentes:

- **Nós companion ou clientes** têm um rádio LoRa pareado com um telefone ou laptop e se comunicam pela infraestrutura próxima quando ela está disponível
- **Repetidores** existem especificamente para encaminhar tráfego entre clientes e outros componentes da infraestrutura. Eles fazem a maior parte do trabalho de roteamento
- **Servidores de sala** (opcionais) hospedam conversas em grupo e entregam mensagens armazenadas aos clientes quando eles se reconectam

No MeshCore, uma primeira **mensagem direta** pode inundar a rede para descobrir um caminho. As seguintes podem seguir esse caminho e voltar à inundação conforme a configuração. **[Canais de grupo públicos e privados ainda usam inundação](https://docs.meshcore.io/faq/#5-general)** por meio de repetidores elegíveis. Os rádios clientes não encaminham pacotes de outros nós.

### Por que isso funciona com infraestrutura fixa

*Esse é o argumento principal a favor do MeshCore.* O modelo de flooding do Meshtastic tem vantagens reais em redes ad hoc e móveis: não exige planejamento, não há infraestrutura para manter e lida bem com nós que entram e saem. O modelo de roteamento do MeshCore leva vantagem quando **as pessoas implantam infraestrutura de propósito**.

Uma rede baseada em repetidores conhecidos e instalados em locais altos permite projetar a cobertura intencionalmente, em vez de depender de quais nós estão ao alcance uns dos outros em determinado dia. Essa diferença importa para:

- **Nós permanentes em telhados** com energia confiável
- **Torres** e infraestrutura de comunicação existente
- **Repetidores solares** em locais sem supervisão
- **Locais de retransmissão em montanhas ou áreas elevadas**
- **Infraestrutura comunitária**, compartilhada por vários grupos
- **Redes regionais** que abrangem mais de um bairro
- **Comunicação de emergência**, quando a cobertura previsível importa mais que a flexibilidade

Relacione isso aos fundamentos de RF: **links confiáveis entre infraestruturas bem posicionadas importam mais do que maximizar o ganho da antena, a potência de transmissão ou o alcance teórico.** **As duas redes se beneficiam de repetidores bem posicionados.** Os nós que retransmitem dependem da função e do tráfego.

______

## O argumento dos nós móveis e o custo dessa escolha

Uma sugestão comum é: *"Meshtastic é melhor para nós móveis, MeshCore é melhor para nós fixos, então use Meshtastic para os usuários e MeshCore como backbone."*

No papel, parece atraente. Na prática, misturar os dois não reúne automaticamente as vantagens de ambos, porque **Meshtastic e MeshCore usam arquiteturas de rede e roteamento diferentes e não trocam mensagens entre si.** Conectá-los exige uma camada de tradução entre sistemas incompatíveis, não apenas selecionar as melhores partes de cada um.

Ao conectar os dois, você passa a administrar:

- **Duas redes separadas**, cada uma com sua topologia e comportamento
- **Dois modelos de roteamento** sem estado compartilhado
- **Uma camada de tradução** que exige desenvolvimento e manutenção contínuos
- **Mais infraestrutura** para hospedar a ponte
- **Mais configurações** em dois ecossistemas de firmware em vez de um
- **Mais pontos de falha**, pois a ponte pode falhar independentemente das redes mesh
- **Solução de problemas mais difícil**, pois uma falha de entrega pode estar em qualquer rede ou na ponte entre elas

Antes de adotar esse projeto, faça uma pergunta direta: **a complexidade adicional resolve um problema que um único protocolo mesh bem ajustado não resolve?** Muitas vezes, uma implantação MeshCore bem configurada com alguns nós companion adequados a usuários móveis, ou uma implantação Meshtastic com alguns relays bem posicionados e um limite de saltos maior, oferece a maior parte do benefício prático sem operar duas redes conectadas artificialmente.

______

## Reticulum

Reticulum merece uma categoria própria, não uma posição como "terceira opção de mesh LoRa", porque não é principalmente um protocolo mesh LoRa. **Sua característica principal é a independência do transporte.**

Reticulum é uma pilha de rede baseada em criptografia. Não usa endereços de origem, portanto os pacotes não carregam informações sobre onde foram criados. Cada endereço é autossoberano: depois de gerado, torna-se acessível globalmente em segundos ou minutos e continua acessível mesmo se o dispositivo for movido fisicamente para outra parte da rede. Toda comunicação é criptografada por padrão com chaves efêmeras e sigilo de encaminhamento. O Reticulum descarta pacotes não criptografados em vez de entregá-los. Nada disso exige drivers de kernel. Ele funciona no espaço de usuário em qualquer sistema com Python 3, inclusive em um Raspberry Pi Zero.

As interfaces compatíveis com o Reticulum incluem:

- **LoRa**, com hardware compatível com RNode (um projeto definido e aberto de transceptor LoRa, que pode ser montado, gravado em placas comuns ou comprado pronto)
- **Rádio por pacotes**, por meio de qualquer TNC em modo KISS, adequado ao radioamadorismo VHF e UHF
- **Wi-Fi e Ethernet cabeada**, com descoberta automática de peers sem roteador nem servidor DHCP
- **Conexões seriais** para conexões diretas entre dispositivos
- **TCP e UDP em redes IP existentes**, inclusive na internet
- **A rede I2P** e interfaces personalizadas para qualquer outra opção com uma ponte em Python

No Reticulum funcionam aplicativos como **LXMF** (um protocolo de mensagens tolerante a atrasos) e ferramentas para usuários finais como **Sideband**, **NomadNet** e clientes comunitários do **MeshChat**. Eles oferecem às redes Reticulum uma camada de mensagens e navegação comparável ao que Meshtastic e MeshCore incluem por padrão.

{{< figure src="reticulum-transport-independent-heterogeneous-network.webp" alt="Diagrama mostrando o Reticulum conectando uma rede mesh LoRa, uma rede de rádio por pacotes e um link de internet em uma única rede criptografada e endereçável" >}}

### Quando o Reticulum faz sentido

O valor do Reticulum aparece claramente em uma configuração heterogênea, por exemplo:

**Rede mesh LoRa → nó Reticulum → link IP → nó Reticulum → rede de rádio**

Aqui o Reticulum faz algo que Meshtastic e MeshCore não fazem: conecta dois sistemas de comunicação distintos em uma única rede endereçável. É uma necessidade real e específica, não uma melhoria genérica. Bons casos de uso incluem:

- **Conectar redes geograficamente separadas** sem um caminho de rádio direto entre elas
- **Unir transportes físicos diferentes**, como uma rede mesh LoRa de um lado e uma rede de rádio por pacotes do outro
- **Gateways rádio-IP** que encaminham tráfego entre uma rede de rádio em campo e a internet
- **Redes experimentais e de pesquisa**, onde misturar transportes importa mais do que simplificar a implantação
- **Redes nas quais nenhum transporte atende a todos os requisitos**, então os componentes precisam ser conectados

### Quando o Reticulum adiciona complexidade desnecessária

Se todos usam hardware LoRa compatível e o objetivo real é **uma única rede mesh LoRa regional**, adicionar Reticulum oferece pouco benefício e tem um custo real. Cada camada adicional na pilha de rede implica mais:

- **Configuração** para acertar e manter consistente em todos os nós
- **Software** para instalar, atualizar e solucionar problemas
- **Hardware** em algumas configurações, dependendo de como as interfaces são conectadas
- **Superfície de solução de problemas** quando algo não é entregue
- **Conhecimento necessário** para que operadores entendam um terceiro modelo de rede

*Use o Reticulum quando a independência do transporte resolver uma necessidade que você realmente tem, não apenas porque ele oferece mais tipos de interface que a alternativa.* Um problema de limite de saltos em uma única rede mesh LoRa é um problema de ajuste do Meshtastic ou do MeshCore. Não é um problema de independência do transporte, e o Reticulum não muda isso.

______

## Construa uma rede mesh saudável antes de criar três redes fragmentadas

Se um protocolo já atende aos seus requisitos, **construa uma rede saudável** em vez de várias redes menores unidas por pontes. O princípio "uma mesh primeiro" deve orientar a maioria das decisões acima.

Em uma rede comunitária, **a interoperabilidade entre as pessoas que já a usam costuma importar mais que a flexibilidade arquitetural.** Uma rede grande e funcional baseada em um protocolo tem mais valor prático que três redes tecnicamente interessantes, mas fragmentadas e apenas parcialmente interconectadas.

### Redes Meshtastic existentes importam

**Não descarte o Meshtastic só porque o MeshCore tem vantagens arquiteturais para infraestrutura fixa.** Se uma cidade já tem dezenas ou centenas de nós Meshtastic, essa base instalada representa infraestrutura e comunidade reais. A migração tem um custo que uma comparação de especificações não mostra:

- **Hardware instalado** que precisa ser regravado ou substituído
- **Usuários existentes** que já sabem operar a rede
- **Conhecimento da comunidade** acumulado em torno da implantação atual
- **Repetidores já implantados** e posicionados, às vezes em telhados ou torres de acesso difícil
- **Experiência de configuração** acumulada por quem opera a rede
- **Canais estabelecidos** que as pessoas já acompanham
- **Treinamento necessário** para quem vai aprender um segundo sistema

A escolha do protocolo é **em parte um problema de engenharia e em parte um problema de adoção comunitária.** A arquitetura que parece melhor no papel não vence automaticamente se isso significa pedir a uma comunidade ativa que comece de novo.

______

## O desafio da rede regional

Considere uma implantação hipotética em várias cidades:

**Cidade A, repetidor, repetidor, relay rural, repetidor, Cidade B, repetidor, Cidade C**

Nessa cadeia, **teste separadamente as mensagens de grupo e as diretas**. O MeshCore pode reutilizar um caminho para as diretas, mas continua usando inundação para as de grupo. O Meshtastic pode preservar o contador em enlaces de infraestrutura elegíveis. Cada retransmissão ocupa o canal. Nenhum dos protocolos garante a entrega de ponta a ponta.

Nesse cenário, **limites de saltos, orçamento de airtime, comportamento do roteamento e projeto da infraestrutura deixam de ser teóricos** e passam a determinar se a rede funciona de ponta a ponta. Em escala geográfica, as diferenças arquiteturais entre Meshtastic e MeshCore deixam de ser acadêmicas.

{{< figure src="regional-mesh-network-repeater-chain-scaling.webp" alt="Diagrama de uma rede mesh regional que conecta três cidades por repetidores e um relay rural, mostrando como o airtime e a quantidade de saltos aumentam com a distância" >}}

______

## RF ainda importa mais que o protocolo

**Nenhum software de roteamento engenhoso cria um caminho de RF onde fisicamente não existe um.** Antes de culpar o protocolo por um problema de cobertura, verifique o básico:

- **Altura da antena** acima dos obstáculos
- **Linha de visada** entre as duas pontas do link
- **Desobstrução da zona de Fresnel**, diferente da linha de visada visual
- **Perdas na linha de alimentação**, causadas por cabo coaxial barato ou longo demais
- **Qualidade da antena** e compatibilidade com a banda usada
- **Nível de ruído** no local de recepção
- **Terreno** entre os nós
- **Posicionamento dos nós**, inclusive a margem realista para melhorá-lo
- **Margem do link**, a diferença entre o sinal recebido e o mínimo necessário para decodificá-lo

*Uma antena de 2 dBi bem posicionada em um mastro adequado costuma superar uma antena de alto ganho mal posicionada na janela de um porão.* A escolha do protocolo determina como a rede usa os links existentes. Ela não cria links que a física não permite.

### Confiabilidade acima do alcance máximo

**Não projete uma rede em torno da distância máxima que um link alcança ocasionalmente.** Projete-a em torno de links que funcionam com consistência.

Para uma rede comunitária ou de comunicação de emergência, **a entrega previsível a 15 milhas tem mais valor prático que um link que às vezes alcança 40 milhas e falha no restante do tempo.** Construa uma cobertura sobreposta com infraestrutura confiável em vez de perseguir links recordistas. Esse princípio vale para qualquer protocolo.

______

## Qual escolher

**Meshtastic faz sentido** quando você valoriza um ecossistema maduro, facilidade de adoção, usuários portáteis e em movimento e compatibilidade com uma comunidade Meshtastic existente. É o padrão certo para a maioria das pessoas que começa do zero.

**Repetidores fixos** ajudam a planejar a cobertura, mas não eliminam a inundação. Antes de escolher, teste os dois protocolos com a taxa esperada de mensagens de grupo, as configurações de rádio e a disposição dos repetidores.

**Reticulum faz sentido** quando o problema vai além de uma única rede mesh LoRa e você precisa conectar transportes diferentes ou redes separadas em um sistema endereçável.

Para uma **rede comunitária de infraestrutura sem licença, baixo consumo e longo alcance, baseada principalmente em repetidores fixos**, prefira MeshCore. **Teste o tráfego de grupo antes de mudar.** Uma rede de repetidores fixos ajuda na cobertura, mas não dá rotas direcionadas aos canais de grupo. *Se já existe uma rede Meshtastic saudável na sua região, substituí-la exige benefícios suficientes para justificar a fragmentação da comunidade existente.* O Reticulum entra em cena quando um protocolo mesh ou transporte físico não atende mais aos requisitos, não simplesmente porque faz mais coisas.

______

## Referências

1. [Algoritmo de broadcast mesh do Meshtastic](https://meshtastic.org/docs/overview/mesh-algo/)
2. [Configuração LoRa do Meshtastic (hop_limit)](https://meshtastic.org/docs/configuration/radio/lora/)
3. [Site oficial do MeshCore](https://meshcore.co.uk/)
4. [Pilha de rede Reticulum](https://reticulum.network/)
5. [O que é Reticulum?](https://reticulum.network/manual/whatis.html)
6. [Configuração de interfaces do Reticulum](https://reticulum.network/manual/interfaces.html)
7. [Guia comparativo entre MeshCore e Meshtastic](/articles/meshcore-vs-meshtastic-comparison-guide/)

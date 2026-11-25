---
title: "MeshCore ou Meshtastic: comparação"
date: 2026-06-26
lastmod: 2026-11-25
toc: true
draft: false
description: "Compare MeshCore e Meshtastic em roteamento, alcance, tempo de transmissão, infraestrutura, suporte a dispositivos e adequação ao uso."
genre: ["LoRa", "Redes mesh", "Comunicações offline", "Comunicações de emergência", "Comunicações táticas", "Radioamadorismo", "Código aberto", "Preparação para desastres", "Redes sem fio", "Privacidade"]
tags: ["meshcore versus meshtastic", "meshtastic", "meshcore", "rede mesh lora", "comunicações offline", "comparação meshtastic", "comparação meshcore", "rádio lora", "redes mesh", "comunicações de emergência", "mesh tática", "rádio offline", "protocolo meshtastic", "protocolo meshcore", "lora meshtastic", "comunicações em desastres", "rádio mesh", "armazenar e encaminhar", "flooding lora", "mesh LoRa", "t-beam meshtastic", "heltec lora", "rak wisblock", "mensagens offline", "protocolo de rede mesh", "meshtastic 2.6", "tempo de transmissão lora", "rádio de emergência"]
cover: "/img/cover/meshcore-vs-meshtastic-comparison-guide.webp"
coverAlt: "Ilustração de duas redes mesh LoRa: Meshtastic à esquerda, com nós difundindo pacotes, e MeshCore à direita, com roteamento estruturado, em um fundo escuro."
coverCaption: ""
ref: ["/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide"]
---

## A resposta curta

Meshtastic e MeshCore funcionam no mesmo hardware LoRa barato. Ambos permitem enviar mensagens criptografadas sem rede celular ou Internet. **Os protocolos não são compatíveis entre si.**

**Os dois protocolos inundam o tráfego de grupo.** Clientes comuns do Meshtastic suprimem retransmissões redundantes. No MeshCore, o encaminhamento cabe à infraestrutura. Ambos podem usar rotas aprendidas para mensagens diretas.

*Meshtastic atende à maioria das pessoas.* O aplicativo móvel é refinado, a comunidade é grande, a documentação é sólida e a configuração leva menos de 20 minutos.

**Os fundamentos de radiofrequência importam mais que o firmware.** Nenhum protocolo compensa uma antena mal posicionada.

______

## O que cada sistema faz

### Meshtastic

**Meshtastic** é um projeto de código aberto lançado em 2020 por Kevin Hester. O firmware transforma hardware LoRa comum em uma rede mesh de mensagens de texto, sem depender da Internet nem da rede celular.

O firmware funciona em hardware LoRa que muitos usuários já possuem ou compram por pouco. **LILYGO T-Beam, Heltec WiFi LoRa 32, RAK WisBlock e Seeed SenseCAP Indicator** aceitam Meshtastic sem ferramentas especializadas. Os aplicativos para iOS e Android são bem mantidos. Usuários sem conhecimento técnico entram na rede em menos de dez minutos. O ecossistema inclui pontes MQTT, integração com Home Assistant e plugins ATAK.

### MeshCore

**MeshCore** ganhou espaço em 2023 e 2024. Seu firmware funciona em boa parte do mesmo hardware LoRa, mas usa uma **arquitetura de roteamento híbrida**. Não é store-and-forward puro no sentido usado por redes tolerantes a atrasos.

Os repetidores fazem a maior parte do encaminhamento. **Servidores de sala são opcionais.** Eles armazenam mensagens de grupo para que os clientes as recuperem ao reconectar. Clientes usam um rádio LoRa complementar e conectam-se pela infraestrutura quando disponível, ou comunicam-se diretamente com nós próximos quando não há repetidor.

______

## A principal diferença técnica

### Como funciona o roteamento do Meshtastic

Na **[inundação gerenciada](https://meshtastic.org/docs/overview/mesh-algo/#broadcasts-using-managed-flooding)** do Meshtastic, um cliente comum cancela uma retransmissão pendente se ouvir primeiro o mesmo pacote retransmitido. `ROUTER` e `ROUTER_LATE` ainda podem retransmitir. Para `CLIENT_BASE`, a exceção vale para tráfego de ou para um nó favorito.

Desde o Meshtastic 2.6, as **mensagens diretas** usam inundação para descobrir a rota e depois tentam usar o próximo salto aprendido. Se ele falhar, podem voltar à inundação.

**A restrição real é o tempo de transmissão, não o número de nós.** LoRa opera em bandas ISM compartilhadas com limites regionais de ciclo de trabalho, normalmente de 1% na Europa. Uma rede com balizas GPS frequentes, telemetria e tráfego ativo de canal satura o tempo de transmissão antes de alcançar qualquer limite absoluto de nós. Dez nós ativos que enviam telemetria frequente geram mais contenção que cinquenta sensores silenciosos. Meshes densas com dezenas de usuários ativos costumam ter mais contenção, mas não há um teto fixo. O limite depende do fator de espalhamento, do perfil de tempo de transmissão, dos intervalos de telemetria, do terreno e da posição dos repetidores.

Meshtastic gera tráfego adicional com anúncios de informações dos nós, telemetria de bateria, pacotes GPS e descoberta de vizinhos. Versões recentes do firmware reduziram esse tráfego. *Ajustar essas configurações costuma resolver problemas de desempenho antes que uma troca de protocolo seja necessária.*

### Como funciona o roteamento do MeshCore

No MeshCore, uma primeira **mensagem direta** pode inundar a rede para descobrir um caminho. As seguintes podem seguir esse caminho e voltar à inundação conforme a configuração. **[Canais de grupo públicos e privados ainda usam inundação](https://docs.meshcore.io/faq/#5-general)** por meio de repetidores elegíveis. Os rádios clientes não encaminham pacotes de outros nós.

**Repetidores encaminham tráfego entre nós.** Servidores de sala podem hospedar conversas em grupo e guardar mensagens para clientes que se conectam mais tarde.

**O tempo no ar depende do tráfego.** Nos dois protocolos, mensagens de grupo podem chegar a vários repetidores. Um caminho aprendido pode reduzir transmissões de mensagens diretas. A posição dos repetidores, os ajustes de rádio e a frequência das mensagens também importam.

Sem repetidor, clientes comunicam-se diretamente quando estão no alcance. *A arquitetura funciona melhor com infraestrutura. A infraestrutura não é obrigatória.*

______

## Hardware

Os dois protocolos funcionam nas mesmas placas LoRa populares.

| Placa | Meshtastic | MeshCore |
|---|---|---|
| LILYGO T-Beam (ESP32 + SX1276/SX1262) | Sim | Sim |
| LILYGO T-Echo (nRF52840 + SX1262) | Sim | Sim |
| Heltec WiFi LoRa 32 V3 | Sim | Sim |
| RAK WisBlock 4631 | Sim | Sim |
| Seeed SenseCAP Indicator | Sim | Parcial |
| Station G2 | Sim | Sim |

**Você instala qualquer um dos firmwares no mesmo dispositivo físico.** Trocar de protocolo não exige novo hardware. Experimentar custa apenas tempo.

______

## Facilidade de configuração

### Configurar Meshtastic

1. Baixe o firmware em meshtastic.org
2. Instale pelo flasher web flasher.meshtastic.org, sem drivers
3. Instale o aplicativo Meshtastic no celular
4. Emparelhe por Bluetooth
5. Entre ou crie um canal com nome e senha compartilhados

**Tempo total para um iniciante: menos de 20 minutos.** A criptografia do canal usa chaves pré-compartilhadas AES-256. O canal público padrão conecta você imediatamente a qualquer nó Meshtastic ao alcance. O aplicativo mostra posições GPS em um mapa quando os nós têm GPS ativado.

### Configurar MeshCore

1. Instale o firmware no nó de infraestrutura, repetidor ou servidor de sala, usando PlatformIO ou binários pré-compilados
2. Instale o firmware no rádio complementar do cliente
3. Instale o aplicativo MeshCore
4. Configure no aplicativo o endereço e as credenciais da infraestrutura
5. Conecte o rádio complementar via Bluetooth

**A configuração exige mais planejamento.** Você precisa entender os papéis dos nós antes da implantação. Servidores de sala são opcionais, mas acrescentam persistência de mensagens para clientes offline. *Dois amigos que querem se comunicar rapidamente devem usar Meshtastic. Uma equipe que instala uma estação-base com repetidor no telhado deve usar MeshCore.*

______

## O tempo de transmissão é a restrição real

Os dois protocolos usam LoRa. **A capacidade do LoRa depende do tempo de transmissão e do orçamento de ciclo de trabalho, não do número de nós.**

As variáveis que determinam o desempenho da rede:

- **Fator de espalhamento.** Valores maiores ampliam o alcance, mas reduzem a taxa de dados e a capacidade total.
- **Perfil de tempo de transmissão.** Perfis de longo alcance consomem mais ciclo de trabalho por mensagem.
- **Intervalo de telemetria.** GPS, bateria e dados ambientais do Meshtastic adicionam tráfego contínuo.
- **Frequência das mensagens.** Usuários ativos que enviam com frequência afetam mais o desempenho que nós passivos.
- **Posição dos repetidores.** Um repetidor bem posicionado distribui a carga. Um mal posicionado aumenta o congestionamento.
- **Terreno.** Nós que não se escutam acrescentam tráfego sem causar contenção. Nós ao alcance de muitos outros simultaneamente causam contenção.

**Repetidores fixos** ajudam a planejar a cobertura, mas não eliminam a inundação. Antes de escolher, teste os dois protocolos com a taxa esperada de mensagens de grupo, as configurações de rádio e a disposição dos repetidores.

______

## Regulamentação

As comparações de desempenho variam por região porque as normas são diferentes:

- **915 MHz (EUA):** sem limite rígido de ciclo de trabalho segundo FCC Part 15, mas há limites de potência.
- **868 MHz (UE):** ciclo de trabalho de 1% segundo ETSI, ou 36 segundos de transmissão por hora e por canal.
- **433 MHz (UE/Ásia):** muitas regiões têm limites mais rígidos, frequentemente 10% em certas subfaixas.

**O limite de ciclo de trabalho de 1% na Europa é uma restrição regulatória rígida.** Meshes densas do Meshtastic na UE alcançam os limites mais rapidamente que implantações equivalentes nos EUA. O uso mais eficiente do tempo de transmissão do MeshCore traz um benefício proporcionalmente maior em regiões com restrições de ciclo de trabalho.

______

## Privacidade e segurança

### Meshtastic

Meshtastic criptografa o tráfego de canais privados com **chaves pré-compartilhadas AES-256**. Todas as mensagens de um canal usam a mesma chave. Quem tem a chave lê todas as mensagens, incluindo posições GPS. **O canal público padrão usa uma chave conhecida distribuída com o firmware**, então não oferece confidencialidade contra quem executa Meshtastic nas proximidades.

Posições GPS em um canal privado criptografado só ficam visíveis para nós com a chave. No canal público, qualquer pessoa pode vê-las. *Isso importa quando o rastreamento tem consequências operacionais.*

Meshtastic 2.6 melhorou o roteamento de mensagens diretas. O tráfego em grupo ainda usa PSK de canal. Mensagens diretas oferecem mais isolamento, mas não usam criptografia ponta a ponta no sentido do protocolo Signal.

### MeshCore

**O roteamento não oculta a atividade de rádio.** Não presuma que um caminho aprendido esconda quais repetidores transmitem. **Mensagens diretas usam criptografia por contato**, não uma chave de canal compartilhada. Outros nós da mesma infraestrutura não conseguem decifrar sua conversa direta, mesmo usando o mesmo repetidor.

Nós de infraestrutura retransmitem tráfego criptografado. Em mensagens diretas com criptografia por contato, o repetidor encaminha o texto cifrado sem decifrá-lo. No tráfego de sala, os servidores de sala veem o conteúdo das salas que hospedam. *A pergunta relevante é se você controla o servidor de sala.*

MeshCore não oferece criptografia ponta a ponta estrita como o protocolo Signal. **A criptografia por contato para mensagens diretas melhora bastante a proteção em relação à PSK compartilhada do canal.** Casos de uso operacional de alto risco devem avaliar os detalhes da implementação.

______

## Consumo de energia

**Menos transmissões aumentam a duração da bateria dos nós clientes.** Telemetria, difusões GPS e flooding gerenciado do Meshtastic consomem tempo de transmissão. Você reduz bastante esse custo ajustando intervalos de telemetria e desativando a difusão GPS em nós sem GPS.

**Compare a autonomia com a mesma carga.** Ajustes de telemetria, tempo de transmissão e função do nó também contam.

______

## Resiliência da rede

**O flooding gerenciado do Meshtastic é resiliente.** Perder um nó relay costuma ter pouco impacto operacional porque os outros nós redirecionam o tráfego naturalmente. Não é necessário conhecer antecipadamente os nós disponíveis. A mesh se recupera de forma passiva.

**MeshCore depende mais da posição dos repetidores.** Uma rede MeshCore bem planejada e com boa cobertura de repetidores tem desempenho previsível. A perda do único repetidor em uma área de cobertura desconecta os nós que dependem dele. *MeshCore recompensa o planejamento prévio. Meshtastic tolera melhor falhas de nós.*

**Rotas aprendidas e inundação resolvem problemas diferentes.** Uma rota alternativa só ajuda se outro repetidor elegível puder receber e encaminhar o pacote.

______

## GPS e rastreamento de posição

**O ecossistema GPS do Meshtastic é mais forte.** O aplicativo móvel inclui uma visualização de mapa. Nós comunitários alimentam mapas públicos como meshmap.net por gateways MQTT. A telemetria GPS é um recurso central. O compartilhamento de posição para grupos de caminhada, coordenação de busca e resgate e eventos está bem desenvolvido.

MeshCore não se concentra em rastreamento de posição. *Se a localização por GPS for um requisito principal, o ecossistema Meshtastic é mais desenvolvido e maduro em 2026.*

______

## Ecossistema e comunidade

Meshtastic tem uma **comunidade maior**:

- Discord ativo com milhares de membros
- Subreddit ativo em r/meshtastic
- Documentação extensa em meshtastic.org
- Integrações de terceiros com MQTT, Home Assistant, Node-RED, ATAK e bibliotecas Python
- Lançamentos regulares de firmware
- Grande acervo de guias de hardware criados pela comunidade

MeshCore está crescendo, mas continua menor. *Há menos publicações em fóruns, tutoriais e integrações de terceiros. Quando algo falha, você procura respostas no código-fonte do firmware ou no Discord do projeto, em vez de encontrar soluções existentes.*

Ambos os projetos são de código aberto, mas as licenças diferem. **Meshtastic usa uma licença no estilo BSD. MeshCore usa GPL.** Algumas organizações consideram isso em decisões de implantação e distribuição.

______

## Quando Meshtastic vence

**Grupos pequenos e informais.** Um clube de caminhada que queira mensagens offline e compartilhamento de posição deve usar Meshtastic. É fácil configurar, o mapa funciona bem e a rede se organiza sozinha.

**Implantações móveis.** Usuários em movimento pelo terreno que entram e saem da rede de forma imprevisível se beneficiam do flooding auto-organizado do Meshtastic. Não é preciso planejar a infraestrutura para acomodar nós móveis.

**Implantações para consumidores.** Pessoas sem conhecimento técnico configuram seus próprios dispositivos. O início com Meshtastic é acessível.

**Implantação rápida para um evento.** Comunicação de festival, coordenação de corrida ou busca e resgate montados hoje e desmontados na próxima semana. A configuração rápida e a ausência de dependência de infraestrutura tornam Meshtastic prático.

**Rastreamento GPS.** Para posição como caso de uso principal, Meshtastic é a escolha certa em 2026.

______

## Quando MeshCore vence

**Implantações com infraestrutura planejada.** Você tem um repetidor no telhado ou um servidor de sala com energia confiável. O roteamento híbrido do MeshCore aproveita a infraestrutura fixa.

**Redes grandes com infraestrutura dedicada.** **Teste o tráfego de grupo antes de mudar.** Uma rede de repetidores fixos ajuda na cobertura, mas não dá rotas direcionadas aos canais de grupo.

**Persistência de mensagens com conectividade intermitente.** Servidores de sala armazenam mensagens e as entregam quando os clientes reconectam. **Essa é uma das vantagens práticas mais concretas do MeshCore sobre Meshtastic.**

**Separação entre nós fixos e móveis.** Alguns nós serão infraestrutura, outros clientes. O modelo de funções do MeshCore foi criado para essa separação.

**Regiões com restrição de ciclo de trabalho.** Implantações europeias sob o limite ETSI de 1% aproveitam mais o uso eficiente do tempo de transmissão do MeshCore.

**Criptografia por contato.** Para mensagens diretas criptografadas, o modelo MeshCore é significativamente melhor que a abordagem de PSK de canal do Meshtastic.

______

## Onde cada sistema falha

### Pontos fracos do Meshtastic

- **Contenção de transmissão em escala.** Meshes densas com padrões de alto tráfego, difusões GPS frequentes e canais ativos degradam. Ajuste a configuração antes de trocar o protocolo.
- **Sem persistência de mensagem sem infraestrutura.** Sem gateway MQTT, mensagens perdidas continuam perdidas.
- **Privacidade de posição no canal público.** Qualquer ouvinte vê todas as difusões GPS. É aceitável para uso casual, mas inadequado para requisitos de segurança operacional.
- Versões principais do firmware às vezes introduzem problemas de compatibilidade até que a rede atualize para uma versão correspondente.

### Pontos fracos do MeshCore

- **Configuração complexa.** Você precisa entender as funções de infraestrutura antes de implantá-lo de forma útil.
- **Comunidade menor.** Documentação, tutoriais e integrações de terceiros do Meshtastic são mais desenvolvidos.
- **Menos opções de hardware.** MeshCore atende a uma lista menor de hardware compatível.
- **Aplicativos móveis menos maduros.** São funcionais, mas menos refinados que os aplicativos iOS e Android do Meshtastic.
- **Dependência de infraestrutura para o melhor desempenho.** Sem repetidores, clientes comunicam-se diretamente, mas a eficiência de roteamento desaparece. Sem compromisso do grupo com infraestrutura fixa, a vantagem arquitetural não se concretiza.
- **Recuperação da rede.** Perder um repetidor em uma área causa perda de conexão para os nós dependentes. O flooding do Meshtastic tolera melhor falhas de nós.
- **Nenhuma interoperabilidade entre protocolos.** MeshCore e Meshtastic não trocam mensagens. O mesmo hardware executa um dos firmwares, mas usar ambos exige administrar duas redes separadas.

______

## RF importa mais que firmware

**Qualidade e altura da antena, perda no cabo, terreno e configurações do rádio têm mais impacto no desempenho que a escolha do firmware.**

Um nó Meshtastic bem posicionado no alto de uma colina com boa antena supera um repetidor MeshCore mal colocado em uma caixa metálica no porão. A comparação pressupõe qualidade física de implantação semelhante.

Antes de trocar de protocolo para resolver um problema de desempenho, verifique:

- As conexões da antena estão limpas e têm baixa perda.
- Os nós estão tão altos quanto for possível.
- O perfil de tempo de transmissão corresponde ao alcance necessário.
- **Os intervalos de telemetria não saturam o canal.**
- O fator de espalhamento corresponde à densidade de nós.

______

## Resumo lado a lado

| Fator | Meshtastic | MeshCore |
|---|---|---|
| Modelo de rede | Inundação gerenciada nos canais, próximo salto aprendido nas mensagens diretas | Inundação nos canais, caminho aprendido pelos repetidores nas mensagens diretas |
| Dificuldade de configuração | Fácil | Média a alta |
| Projeto para escalar | Flexível, degrada com contenção de transmissão | Projetado para redes planejadas maiores |
| Qualidade do app móvel | Excelente | Funcional |
| Tamanho da comunidade | Muito grande | Crescendo |
| GPS/localização | Ecossistema desenvolvido | Foco mínimo |
| Persistência de mensagens | Não. Requer gateway MQTT | Sim, via servidores de sala opcionais |
| Criptografia de mensagens diretas | PSK de canal | Criptografia por contato |
| Necessidade de infraestrutura | Não exige | Otimizado para nós de infraestrutura |
| Recuperação da rede | Resiliente e autorregenerável | Depende da posição dos repetidores |
| Suporte a hardware | Amplo | Subconjunto direcionado |
| Melhor para | Grupos móveis, ad hoc e pequenos | Implantações planejadas com infraestrutura fixa |

______

## Qual escolher

**Comece com Meshtastic.** Você estará transmitindo em uma tarde. Encontrará pessoas para testar. O aplicativo funciona e a documentação é excelente. O roteamento para o próximo salto no Meshtastic 2.6 reduz a diferença de eficiência do tráfego direto ponto a ponto.

**Considere o MeshCore** se você precisa de repetidores dedicados ou servidores de sala opcionais que guardem mensagens para usuários que se reconectam.

Antes de trocar de protocolo, **ajuste sua instalação Meshtastic**. Reduza os intervalos de telemetria. Desative as difusões GPS em nós sem GPS. Ajuste o perfil de transmissão à densidade dos nós. *Muitas redes com problemas de desempenho têm problemas de configuração, não de protocolo.*

**As duas redes se beneficiam de repetidores bem posicionados.** Os nós que retransmitem dependem da função e do tráfego.

*Você está construindo uma rede que precisa ligar LoRa a packet radio, Wi-Fi ou Internet em vez de ficar em uma única mesh LoRa?* Veja o **[guia de comparação Meshtastic, MeshCore e Reticulum](/articles/meshtastic-vs-meshcore-vs-reticulum-comparison-guide/)** para entender onde redes independentes de transporte se encaixam e onde adicionam complexidade desnecessária.

---
title: "Corrida pela detecção de câmeras Flock: o que mudou em 2026"
date: 2026-09-10
lastmod: 2026-11-13
toc: true
draft: false
description: "Veja as mudanças relatadas nos métodos de detecção da Flock Safety, as respostas da comunidade e as abordagens infravermelhas para identificar sistemas de câmeras."
genre: ["Tecnologia da privacidade", "Contravigilância", "Projetos de código aberto", "Direitos digitais", "Segurança de redes", "Pesquisa em segurança", "Modificação de hardware", "Ferramentas de privacidade"]
tags: ["Flock Safety", "ALPR", "Flock-You", "Detecção de OUI", "Solicitação Probe curinga", "Modo promíscuo WiFi", "Monitoramento 802.11", "DeFlockJoplin", "NitekryDPaul", "Detecção BLE", "WiFi de 5GHz", "MAC administrado localmente", "Correspondência de padrão SSID", "Hardware de contravigilância", "STS Collective", "colonelpanichacks", "Evasão de detecção", "ESP32", "Detecção WiFi", "Conscientização sobre vigilância", "OUI-SPY", "M5 Atom Lite", "Flock Finder", "Rastreamento de issues do GitHub", "Atualização de firmware", "Proteção contra identificação por impressão digital do dispositivo", "Randomização de MAC", "Impressão digital de elementos de informação", "Salto de canais", "Ativismo pela privacidade", "Segurança de código aberto", "Vigilância em massa", "Firmware de detecção", "Wardriving", "Remoção de câmeras", "Hardware de privacidade", "Detecção infravermelha", "Iluminador IR", "ESP32-CAM", "Seeed Studio XIAO ESP32S3 Sense", "Quectel L76K", "Detecção óptica", "Valleytech Custom Solutions"]
cover: "/img/cover/flock-camera-detection-techniques-2026.webp"
coverAlt: "Cena urbana com uma câmera Flock em um poste e um veículo equipado com um dispositivo de detecção avançado. Sinais luminosos representam a comunicação de dados sem fio em um fundo escuro."
coverCaption: "Como as mudanças no hardware da Flock Safety continuam interrompendo ferramentas de detecção de código aberto e como a comunidade acompanha essas mudanças"
canonical: "https://simeononsecurity.com/articles/flock-camera-detection-arms-race-2026/"
---

**Se seu detector Flock-You ficou silencioso em um trajeto que antes identificava câmeras todas as vezes, você não está imaginando isso, e é provável que seu hardware não esteja quebrado.** O hardware e o firmware das câmeras Flock Safety mudaram pelo menos duas vezes no último ano de formas que invalidaram os métodos de detecção da comunidade. Pesquisadores de código aberto tiveram de fazer engenharia reversa de uma nova assinatura a cada mudança.

*Esta história avança rapidamente. O método de detecção e a lista de OUI abaixo refletem o branch `main` de `colonelpanichacks/flock-you` em setembro de 2026. Consulte o [repositório no GitHub](https://github.com/colonelpanichacks/flock-you) antes de concluir que seu dispositivo está com defeito.*

{{< youtube id="cVf-id71BuQ" >}}

*O vídeo acima, da Valleytech Custom Solutions, documenta exatamente o sintoma explicado neste artigo: uma ronda rotineira que de repente registra zero detecções em várias versões de firmware, num trajeto onde as câmeras eram detectadas de forma confiável e em um condado onde várias câmeras antes sinalizadas foram removidas fisicamente.*

______

## Uma ronda que de repente não encontrou nada

O padrão se repete quase da mesma forma nos relatos. Uma pessoa percorre uma rota que já fez dezenas de vezes. Seu detector, executando o firmware atual, já havia identificado as mesmas câmeras. Então, em uma viagem, não detecta nada. Nem um único bipe, nem uma entrada de registro, em todas as versões de firmware personalizado testadas.

O vídeo da Valleytech descreve exatamente esse caso: um trajeto diário até o correio, que sempre registrava pelo menos uma câmera Flock, deixou de registrar qualquer uma. Uma segunda rota, passando pelo Micro Center, antes sinalizava cinco câmeras e agora mostra apenas uma ainda ativa. As outras quatro foram arrancadas fisicamente de seus postes.

**Duas coisas aconteciam na mesma época e é fácil confundi-las:**

- **Câmeras estão sendo removidas ou realocadas fisicamente** em algumas áreas, o que realmente reduz o número de dispositivos a detectar.
- **A assinatura sem fio transmitida pelas câmeras mudou**, então uma câmera que ainda está no poste não aciona hardware de detecção com firmware desatualizado.

Dois issues separados no repositório `colonelpanichacks/flock-you`, abertos com meses de diferença, documentam o segundo problema em detalhes. Lê-los em ordem mostra como a comunidade precisou evoluir seu método de detecção duas vezes.

______

## Issue #20: o ponto de acesso de gerenciamento sumiu

O **[Issue #20](https://github.com/colonelpanichacks/flock-you/issues/20)**, aberto em janeiro de 2026, começou com uma reclamação conhecida: uma pessoa testou o dispositivo perto de uma câmera Flock conhecida e registrada no DeFlock, mas não detectou nada. Nas semanas seguintes, mais pessoas relataram o mesmo resultado, da Flórida a Indiana, Atlanta e ao Meio-Oeste, com hardware e antenas diferentes.

Um comentário trouxe a pergunta que se mostrou mais importante: **a Flock havia mudado algo do próprio lado de uma forma que interrompeu a detecção para todos mais ou menos ao mesmo tempo?**

O mantenedor do projeto, colonelpanichacks, acabou confirmando que foi exatamente isso. **Por volta de dezembro de 2025, a Flock desativou o ponto de acesso de gerenciamento que suas câmeras transmitiam.** Esse AP era a base original da detecção sem fio. Quando desapareceu, a comunidade migrou para sinais Bluetooth Low Energy (BLE) como substituto. Esse substituto também deixou de funcionar de forma confiável até a primavera de 2026.

| Superfície de detecção | Estado |
|---|---|
| **AP WiFi de gerenciamento** | Desativado pela Flock por volta de dezembro de 2025 |
| **Sinalização BLE** | Deixou de funcionar de forma confiável na primavera de 2026 |
| **Uplink celular LTE** | Ainda usado para enviar dados à nuvem, mas não pode ser detectado passivamente |
| **Solicitações Probe 802.11 curinga** | Base atual da detecção (veja abaixo) |

*Todo firmware personalizado construído sobre os antigos caminhos de detecção por AP ou BLE agora procura um sinal que as câmeras pararam de enviar. Por isso, um dispositivo que funcionava fica completamente silencioso sem que o hardware tenha algo errado.*

______

## O método substituto: probes curinga e impressão digital de quadros

O firmware atual do `flock-you` opera em modo promíscuo 802.11 dedicado. O rádio nunca transmite e nunca se conecta a uma rede. Ele apenas escuta, alternando entre os canais WiFi 11, 6 e 1 com permanência de 250 milissegundos para acompanhar a frequência com que as próprias câmeras mudam de canal.

**Agora, uma detecção exige que todos os itens a seguir correspondam antes de o firmware emitir um alerta:**

1. O quadro precisa ser uma **solicitação Probe de gerenciamento** 802.11 (tipo 0, subtipo 4).
2. O **elemento de informação SSID precisa estar presente com comprimento 0**, ou seja, trata-se de um probe curinga, e não de uma busca por uma rede específica.
3. O endereço do transmissor (**addr2**) precisa corresponder a um dos prefixos OUI conhecidos da Flock.
4. Os demais elementos de informação do quadro precisam corresponder ao padrão de impressão digital documentado pela comunidade DeFlockJoplin, com base na pesquisa de Pintor e Atzori, de 2022, sobre **[impressão digital de elementos de informação em solicitações Probe WiFi](https://ieeexplore.ieee.org/document/10001618)**.

O firmware chama esse método de `wifi_wildcard_probe_ie_sig`. Os testes de campo da comunidade DeFlockJoplin detectaram **11 das 12 câmeras conhecidas, com apenas 2 falsos positivos** no trajeto de teste. Essa é a mesma referência verificada em campo citada no **[guia de hardware](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** do projeto. A 12ª câmera usava um OUI que foi incluído na lista abaixo.

{{< figure src="flock-detection-arms-race-timeline-2026.webp" alt="Linha do tempo que mostra a evolução da detecção de câmeras Flock, do ponto de acesso WiFi de gerenciamento, passando pela sinalização Bluetooth Low Energy, até as solicitações Probe curinga e a impressão digital de elementos de informação atuais, com uma quarta etapa mostrando novos SSIDs, 5GHz e evasão por endereço MAC" >}}

______

## A lista atual de OUI

A impressão digital de probes curinga acima só é acionada depois que o endereço MAC do transmissor corresponde a um dos prefixos OUI que a comunidade confirmou em hardware Flock real. O pesquisador **@NitekryDPaul** mantém a lista principalmente, e a comunidade **DeFlockJoplin** contribuiu com a 31ª entrada depois de detectar uma câmera que não constava da lista original de 30 entradas.

```text
70:c9:4e  3c:91:80  d8:f3:bc  80:30:49  b8:35:32
14:5a:fc  74:4c:a1  08:3a:88  9c:2f:9d  c0:35:32
94:08:53  e4:aa:ea  f4:6a:dd  f8:a2:d6  24:b2:b9
00:f4:8d  d0:39:57  e8:d0:fc  e0:4f:43  b8:1e:a4
70:08:94  58:8e:81  ec:1b:bd  3c:71:bf  58:00:e3
90:35:ea  5c:93:a2  64:6e:69  48:27:ea  a4:cf:12
82:6b:f2
```

**Esta lista não é estática.** A pesquisa upstream menciona vários prefixos testados e depois rebaixados. Um acabou sendo de um reprodutor de mídia Sony, e outro era um valor provisório inicial que nunca correspondeu a nada. Dois itens estão marcados como de baixa confiança. O prefixo `82:6b:f2` é mantido de propósito, embora seja um endereço administrado localmente, pois excluí-lo teria descartado silenciosamente uma detecção real e confirmada pela DeFlockJoplin.

**Uma entrada recebeu confirmação independente em hardware de uma câmera em serviço municipal.** A unidade Flock cujas imagens do sistema de arquivos foram publicadas em setembro de 2026 tinha o endereço MAC **`f4:6a:dd:57:46:fb`**, e `f4:6a:dd` ocupa a posição 13 desta lista. Essa unidade não era um dispositivo de laboratório nem uma amostra comprada. Ela estava instalada em um poste em Wauwatosa, Wisconsin, fotografando o trânsito, o que faz dela a confirmação individual mais forte de qualquer prefixo desta lista.

*Se você mantém seu próprio fork de firmware, busque a lista de OUI no diretório upstream `datasets/` em vez de codificar uma cópia. A lista muda conforme a pesquisa avança, e uma cópia desatualizada é uma forma lenta e silenciosa de começar a deixar câmeras passar novamente.*

______

## Classificação dos sinais de detecção

A correspondência de OUI é o método em que o firmware atual mais se apoia, e também o mais fraco dos cinco sinais disponíveis. A comunidade de detecção **[WiFi Mothership](https://wifimothership.com/flock)** os classifica por nível de confiança, com base na pesquisa de firmware da GainSec.

| Confiança | Sinal | Observações |
|---|---|---|
| **ALTA** | **ID de fabricante BLE `0x09C8`** (XUNTONG) | A impressão digital digital mais forte. Aparece em unidades Raven e em qualquer Falcon ou Sparrow com um módulo de bateria conectado |
| **ALTA** | **UUIDs de serviços BLE Raven `0x3100` a `0x3500`** | Serviços GATT específicos do Raven para GPS, energia, rede, upload e erros. Acionados somente em hardware Raven |
| **MÉDIA** | **Padrão SSID WiFi `^Flock-[A-Z0-9]+$`** | Nome padrão do hotspot de provisionamento. Outros SSIDs encontrados no firmware incluem `FS Ext Battery`, `Penguin` e `Pigvision` |
| **MÉDIA** | **Trecho do nome do dispositivo BLE** | Nomes como `FS Ext Battery` aparecem nos dados de anúncio e não exigem análise de dados do fabricante |
| **BAIXA** | **Correspondência de endereço MAC e prefixo OUI** | **O método mais ruidoso.** Prefixos de fornecedores de componentes aparecem em milhares de produtos sem relação |

*A linha inferior é aquela de que o firmware atual mais depende, e esse é o problema central da detecção que prioriza OUI.*

### Por que a lista de OUI tem tanto ruído

Os 31 prefixos acima não são 31 identificadores da Flock. O WiFi Mothership acompanha um conjunto paralelo de **26 prefixos e classifica cada um pelo proprietário real**, revelando a composição.

| Classe | Quantidade | Proprietário |
|---|---:|---|
| **Flock Safety** | **1** | `B4:1E:52`, atribuição IEEE à própria empresa |
| **Módulos de bateria** | 10 | Componentes Silicon Labs em conjuntos de bateria estendida |
| **Módulos de câmera** | 11 | Módulos de câmera WiFi da Liteon Technology |
| **Infraestrutura de computação** | 4 | Raspberry Pi Foundation e Raspberry Pi Trading |

**Vinte e cinco dos 26 prefixos pertencem a fornecedores de componentes**, cujas peças são vendidas em enormes volumes e usadas em hardware sem relação com a Flock Safety. Um prefixo de conjunto de bateria Silicon Labs ou de módulo de câmera Liteon aparece em produtos sem conexão com a Flock. Placas Raspberry Pi também estão por toda parte.

**Uma correspondência com qualquer um deles é uma pista, não uma identificação.** Por isso a assinatura de probe curinga tem tanto peso no firmware atual. Combinar uma correspondência OUI com uma solicitação Probe de SSID vazio eleva a confiança de um palpite para 62 na escala do próprio projeto.

*Somente `B4:1E:52` responde sozinho à pergunta «este é um dispositivo Flock?». Trate os outros 30 prefixos como evidências complementares.*

### Quantas câmeras expõem um hotspot?

Os dados de wardriving fornecem um limite mínimo da população. O WiFi Mothership contou **900 ou mais pontos de acesso Flock no WiGLE em 2025**, onde um AP Flock significa um dispositivo que transmite o SSID padrão de hotspot `Flock-XXXX`.

Esse número descreve dispositivos que expõem um hotspot de provisionamento, não a base instalada. A Flock declara dezenas de milhares de implantações, e a maioria dessas câmeras nunca transmite algo que um carro em wardriving registra. **O mapa é uma amostra, e uma pequena.**

______

## Issue #43: novo padrão SSID, 5GHz e resistência à impressão digital de MAC

Três meses após o encerramento do Issue #20, chegou um segundo relato que descreve o que parece ser uma contramedida deliberada contra detecção, e não uma mudança incidental de firmware. O **[Issue #43](https://github.com/colonelpanichacks/flock-you/issues/43)**, aberto em maio de 2026, usa dados de wardriving do WiGLE coletados em uma câmera já confirmada no DeFlock e documenta três descobertas que as ferramentas existentes não contemplavam.

### Descoberta 1: formato SSID diferente

O SSID documentado do hotspot Flock sempre seguiu o padrão `Flock-XXXXXX`. A câmera deste relato transmitia **`Flock Camera net.`** em vez disso, usando um padrão de nome completamente diferente. Quem pesquisasse no WiGLE o curinga `Flock-*`, como vários pesquisadores vinham fazendo, não encontraria resultado algum para essa câmera, embora ela estivesse transmitindo ativamente.

### Descoberta 2: hotspot confirmado em 5GHz

A mesma câmera transmitia simultaneamente no **canal 1 de 2.4GHz** e no **canal 157 de 5GHz**, usando endereços MAC sequenciais em cada banda (`...9f:a2:de` e `...9f:a2:df`). Isso aponta para um único módulo WiFi de banda dupla que atribui endereços adjacentes a cada rádio, em vez de dois dispositivos sem relação. Um relato independente do pesquisador nsm_barii já havia registrado uma solicitação Probe Flock no canal 149 de 5GHz, portanto agora existem dois pontos de dados que confirmam que a operação em 5GHz é real e não um erro isolado de configuração.

**Todos os métodos de detecção descritos anteriormente, incluindo o firmware atual de probe curinga, escutam apenas em 2.4GHz.** Uma câmera que transmite exclusivamente, ou principalmente, em 5GHz fica invisível para esse hardware, independentemente da precisão da lista OUI.

### Descoberta 3: endereços MAC administrados localmente no hotspot

Os dois endereços MAC capturados têm o **bit de administração local ativado**, o que significa que não foram atribuídos do bloco OUI real da Flock registrado na IEEE. A lógica padrão de detecção do `flock-you` ignora de propósito endereços administrados localmente, pois esse é o método padrão para filtrar telefones e laptops que randomizam endereços MAC.

**Esse filtro, que existe para reduzir falsos positivos, também elimina uma câmera Flock que use um MAC administrado localmente na interface de hotspot, pela mesma lógica criada para limpar ruído.** Os bytes finais sequenciais dos dois endereços capturados descartam uma geração aleatória, fazendo essa atribuição parecer intencional e estruturada, em vez de coincidência.

| Descoberta | O que continua funcionando apesar disso |
|---|---|
| **Novo formato SSID** (`Flock Camera net.`) | A correspondência por padrão SSID continua funcionando se o padrão for ampliado |
| **Operação em 5GHz** | Nada no firmware atual, que só verifica o canal de 2.4GHz |
| **MAC administrado localmente** | Correspondência por padrão SSID, pois não depende do endereço MAC |

*A correspondência por SSID é o único método desta tabela que continua funcionando independentemente da banda usada pela câmera ou de como seu endereço MAC foi atribuído. Esse é o argumento prático para ampliar o suporte a padrões SSID em vez de depender apenas da correspondência OUI.*

______

## A Flock está evitando a detecção de propósito?

Nenhum dos dois issues do GitHub prova intenção, e é importante ser preciso. O próprio autor do Issue #43 levantou a questão como uma pergunta em aberto, não como conclusão: isso ocorre de forma consistente nas implantações da Flock ou é específico de uma versão de firmware em uma câmera?

Mas observe o padrão nos dois issues. Uma superfície de detecção desaparece. A comunidade encontra uma substituta. Os pontos cegos da substituta, como varredura apenas em 2.4GHz, correspondência baseada em OUI e filtragem de MACs administrados localmente, coincidem com as propriedades exploradas por um novo formato de SSID, um rádio de 5GHz e um endereço MAC administrado localmente. **Isso pode ser coincidência, resultado de um ciclo de atualização de firmware sem relação, ou pode ser o fornecedor reduzindo sua presença sem fio de formas que acabam interrompendo a detecção de terceiros, com intenção ou sem ela.**

*A postura mais útil não é discutir qual explicação vale. É criar detecção que não dependa de uma única premissa para sempre, porque, no histórico de dois anos deste projeto, todas elas mudaram.*

### Confirmação visual: ligada, mas sem transmissão

**[Um terceiro vídeo curto da Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0) resolve a dúvida sobre «talvez a câmera tenha sido removida».**

{{< youtube id="sjI8FB0cLk0" >}}

O criador voltou à mesma câmera do primeiro vídeo, à noite, e confirmou visualmente que **os LEDs IR ainda estavam acesos**, sinal de que a unidade estava ligada e iluminava a área para capturas noturnas. Ao mesmo tempo, **todos os firmwares personalizados testados registraram zero detecções legítimas** dessa câmera. Um alerta ocorreu, mas foi um falso positivo confirmado, não uma detecção real. Nada da câmera chegava ao lado sem fio.

**Isso separa claramente as duas explicações concorrentes.** Uma câmera removida ou realocada não explica uma unidade visivelmente ligada e iluminando à noite. Uma câmera ativa, iluminando, mas silenciosa em todos os métodos de detecção WiFi, indica que a própria assinatura sem fio desapareceu, não que o hardware sumiu.

O criador também relatou, após conversar com outros desenvolvedores trabalhando no mesmo problema, que não foi um resultado isolado. **Várias pessoas observaram o mesmo padrão aproximadamente na mesma época**, o que aponta para uma mudança coordenada, em escala nacional, do lado da Flock em vez de uma falha local de uma câmera. *Essa afirmação é anedótica, baseada em conversas informais e não em um conjunto de dados publicado. Mesmo assim, ela coincide com os períodos de dezembro de 2025 e primavera de 2026 descritos no Issue #20. É o tipo de relato que deveria virar um novo issue no GitHub em vez de permanecer em uma discussão de comentários.*

______

## O que isso significa para seu hardware de detecção

Se seu dispositivo ficou silencioso, siga esta lista antes de concluir que está quebrado:

1. **Atualize o firmware primeiro.** Se estiver usando algo anterior ao branch `main` atual, provavelmente ainda procura o AP de gerenciamento desativado ou os beacons BLE inativos. Baixe o firmware mais recente e grave-o novamente.
2. **Confirme que a câmera ainda está lá.** Alguns relatos de «zero detecções» se referiam a hardware realmente removido ou realocado, não a uma falha de detecção. Compare com o **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** ou o **[DeFlock](https://deflock.org/)** antes de solucionar problemas do dispositivo.
3. **Reduza a velocidade nos cruzamentos.** A permanência de 250 ms em cada canal faz uma passagem rápida ultrapassar a janela de detecção da câmera antes que o rádio chegue ao canal certo. Uma parada de 30 a 60 segundos detecta muito mais câmeras que uma passagem rápida com uma antena maior.
4. **Relate o que você observou.** Um resultado confirmado de zero detecções junto a uma câmera verificada visualmente é exatamente o tipo de dado que levou aos Issues #20 e #43. Abra um novo issue em vez de presumir que outra pessoa já fez isso.
5. **Conheça os limites atuais.** Um firmware que usa somente WiFi e 2.4GHz não verá uma câmera que mudou para 5GHz ou ficou silenciosa nas bandas que ele varre. Essa é uma lacuna real no momento, não um bug específico da sua versão.

**Nada disso torna o hardware inútil.** A lista OUI e a impressão digital de probes curinga ainda detectam hoje a grande maioria das câmeras implantadas. O ponto é tratar qualquer detector, DIY ou comprado, como um retrato da corrida atual, não como solução permanente.

{{< stscollective-ad "flockyou" >}}

______

## Uma abordagem paralela: detectar o clarão infravermelho em vez do sinal WiFi

A detecção sem fio não é a única frente dessa corrida. **[Um vídeo complementar separado](https://www.youtube.com/shorts/mzpr6bslsYA) do mesmo criador, Valleytech Custom Solutions, apresenta uma abordagem completamente diferente**: em vez de escutar uma assinatura de rádio, observar o iluminador infravermelho da câmera.

{{< youtube id="mzpr6bslsYA" >}}

A maioria das câmeras ALPR, incluindo as da Flock, usa **iluminação infravermelha para capturar placas legíveis à noite**, pelo mesmo motivo que câmeras de segurança comuns funcionam no escuro. A luz IR é invisível ao olho humano, mas visível a um sensor de imagem sem filtro de corte infravermelho. *Esse único detalhe do hardware, a ausência do filtro IR, transforma um módulo de câmera comum em um detector Flock.*

### Como é o protótipo

A abordagem documentada no vídeo passou por várias iterações até chegar a uma combinação viável:

- **Primeira tentativa**: receptores dedicados com fotodiodos IR. Funcionavam tecnicamente, mas as peças eram caras demais para uma opção DIY prática.
- **Segunda tentativa**: um **Jetson Nano combinado com um módulo de câmera Raspberry Pi**. A ideia funcionou, mas o custo do hardware e o consumo de energia tornaram o conjunto inviável para uma construção portátil ou instalada em um veículo.
- **Construção atual**: um **módulo de câmera baseado em ESP32 sem lente com filtro de corte IR**. O criador testou um **ESP32-CAM** e um **M5Stack S3 Cam** antes de escolher o **Seeed Studio XIAO ESP32S3 Sense**, combinado a um **módulo GNSS Seeed XIAO baseado no chip Quectel L76K** para registrar a localização GPS das detecções, seguindo o mesmo padrão de wardriving com GPS já usado pelo painel do `flock-you` baseado em WiFi.

| Requisito | Por que importa |
|---|---|
| **Módulo de câmera sem filtro de corte IR** | O filtro que corrige as cores das fotos comuns também bloqueia a luz exata que o método precisa detectar |
| **Câmera em vez de fotodiodo** | Receptores de fotodiodo capazes de isolar o sinal eram caros demais para uma construção DIY prática |
| **Registro de GPS** | Associa as detecções a um local, como o painel Flask do firmware WiFi |

### O padrão de piscadas da câmera

A ideia depende de o iluminador piscar em um padrão repetitivo detectável em vez de permanecer aceso continuamente. O criador relatou um **tempo medido por ele de aproximadamente 20 milissegundos ligado e 80 milissegundos desligado, um período de 100 milissegundos, equivalente a um ciclo de trabalho de 20% a 10Hz**. Ele deixou claro que esse valor não foi verificado e pode estar errado. *Use esse número específico como ponto de partida para sua própria medição, não como especificação confirmada, pois a Flock nunca o publicou e o criador não afirmou ter certeza.*

### Estado do projeto

**Este é um protótipo inicial, apenas DIY, não um produto acabado.** O criador descreveu o software como «feito no vibe coding» e ainda em desenvolvimento. Uma campainha para alertas audíveis está planejada, mas não foi adicionada. Também não existe uma placa pronta equivalente ao hardware OUI-SPY. A versão atual ainda exige **confirmação visual humana** para saber se a detecção sinalizada é uma câmera de verdade ou outra fonte de luz IR. Portanto, funciona como ferramenta de triagem, não como sistema totalmente automatizado.

*Esta superfície de detecção é realmente diferente de tudo o mais neste artigo. Ela não depende de WiFi, 2.4GHz ou 5GHz, correspondência OUI ou comportamento do endereço MAC, então as técnicas de evasão descritas no Issue #43 não se aplicam. Ela também tem suas próprias limitações: linha de visão, interferência da luz do dia e uma suposição de ciclo de trabalho ainda não confirmada de forma independente.*

______

## O que a comunidade está fazendo

A resposta aos dois issues seguiu o padrão que mantém o projeto útil há dois anos: alguém relata uma lacuna, outra pessoa contribui com uma correção e ela é lançada em uma atualização em vez de ficar na lista de pendências.

- **O Issue #20** terminou com a confirmação da causa raiz e uma reescrita do firmware baseada na assinatura de probes curinga, resultado creditado à pesquisa de campo da comunidade DeFlockJoplin.
- **O Issue #43** continua aberto no momento da redação, e a sugestão de correspondência por padrão SSID ainda aguarda implementação. *Se quiser ajudar a fechar essa lacuna, a correção, adicionar `Flock Camera` como padrão de correspondência adicional, é uma contribuição pequena e bem delimitada para quem conhece a lógica de correspondência do firmware.*
- O conjunto de dados OUI subjacente tem versão e data no repositório. Entradas rebaixadas e de baixa confiança são documentadas em vez de removidas silenciosamente, para que qualquer pessoa que faça um fork saiba exatamente o que mudou e por quê.

*Este é o argumento prático a favor de ferramentas de detecção de código aberto em vez de uma alternativa fechada. A pessoa que encontrou a lacuna não consegue corrigir um detector proprietário. Este já recebeu correções duas vezes.*

______

## A outra resposta: remover o hardware

A detecção sem fio é uma resposta a essas câmeras. Um esforço paralelo foi atrás do próprio hardware e, em setembro de 2026, produziu a evidência pública mais detalhada até então sobre o funcionamento interno de uma câmera Flock.

**O coletivo stegan0gram removeu uma câmera de seu poste, copiou o armazenamento interno e publicou as imagens do sistema de arquivos pelo Distributed Denial of Secrets.** Eles descrevem o trabalho sem rodeios:

> «Por que apenas destruí-las se podemos fazer engenharia reversa e descobrir os segredos de quem nos espiona? Libertamos hardware em campo, o desarmamos e fizemos engenharia reversa das câmeras e dos equipamentos solares associados.»

*A distinção importa. Destruir uma câmera remove uma unidade. Fazer engenharia reversa produz evidências sobre todas elas.*

### O que a remoção revelou

O conjunto de dados publicado inclui uma **partição de mídia de 18 GB**, uma **imagem do sistema Android de 1,5 GB** e uma **partição de credenciais de 32 MB**, além da chave recuperada para o contêiner de mídia criptografado. Com isso, pesquisadores determinaram a versão do sistema operacional, a versão do kernel, as credenciais de back-end embutidas no código e os tokens de autenticação em texto simples armazenados pela câmera.

Essa base de evidências agora sustenta a pesquisa de segurança apresentada em **[Vulnerabilidades em câmeras Flock Safety: mais de 50 falhas encontradas](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)**, que antes se baseava em dispositivos de laboratório e unidades compradas.

### A reação à remoção

Interferência física traz consequências, e o quadro é misto.

- **Várias pessoas foram presas em todo o país** por supostamente adulterar ou sabotar câmeras Flock.
- **Algumas cidades anunciaram que deixarão de usar câmeras Flock**, o resultado desejado pelos críticos dessas câmeras.
- **Um departamento de polícia construiu um gabinete falso de câmera Flock impresso em 3D** para atrair possíveis vândalos, uma isca destinada a gerar prisões.

Noel Pichardo, ex-policial de Pawtucket, Rhode Island, tornou-se crítico da Flock depois de questionar o uso das câmeras por seu departamento e apresenta diretamente o argumento contra a sabotagem. Ele disse à WIRED que entende a frustração, mas teme que a tática seja contraproducente. «Acho que esse tipo de vigilantismo só vai consolidar a crença da polícia e do Estado em geral de que essa ferramenta é necessária», afirmou. «Quanto mais o Estado continuar ignorando as reclamações de seus eleitores contrários a esse tipo de vigilância, mais isso vai acontecer.»

### Onde a detecção se encaixa

A desmontagem não muda o problema de detecção tratado neste artigo. A câmera continua transmitindo como antes, o firmware ainda precisa da lista OUI e da assinatura Probe, e as duas interrupções documentadas continuam valendo.

O despejo acrescenta **a confirmação da identidade do hardware**, incluindo uma entrada OUI agora verificada em uma unidade real, além de lembrar que tipo de pressão altera as implantações. **Câmeras deixam uma rota porque uma votação do conselho encerra um contrato, não porque um detector ficou silencioso.** As ferramentas sem fio respondem a uma pergunta pessoal sobre o que há ao seu redor. A disputa política responde à questão mais ampla, e o despejo ofereceu a essa disputa suas evidências mais fortes até agora.

______

## Conclusão: a detecção é um alvo móvel, não uma resposta definitiva

Um detector silencioso em uma rota onde antes encontrava câmeras não prova que seu hardware falhou. Isso mostra que a assinatura sem fio que ele reconhecia mudou novamente, seguindo um padrão que já se repetiu duas vezes em um único ano. **O AP de gerenciamento, a sinalização BLE e, agora possivelmente, as premissas de 2.4GHz e OUI exclusivas embutidas no firmware atual** tiveram vida útil limitada.

**A solução nunca foi desistir da detecção sem fio.** Foi manter visíveis e documentadas as premissas do método, abertas a correções quando surgir outro relato como os Issues #20 ou #43. Esse é o argumento a favor de firmware de código aberto em vez de qualquer alternativa fechada: a correção sai assim que a comunidade encontra a lacuna, não conforme o cronograma do fornecedor.

### Principais conclusões

- **Duas superfícies de detecção documentadas já desapareceram**: o AP WiFi de gerenciamento, desativado por volta de dezembro de 2025, e a sinalização BLE, não confiável desde a primavera de 2026.
- **O método atual, solicitações Probe curinga combinadas com correspondência de impressão digital OUI e IE, teve taxa de detecção de 11 em 12 verificada em campo**, mas funciona apenas em WiFi e 2.4GHz.
- **Um relato pendente descreve um novo formato SSID, um hotspot confirmado em 5GHz e endereços MAC administrados localmente** que o método atual, baseado em OUI e limitado a 2.4GHz, não consegue ver.
- **Uma abordagem separada, sem rádio, está surgindo**: um módulo de câmera ESP32 sem filtro de corte IR identifica o iluminador infravermelho de uma câmera Flock. Essa superfície ignora completamente o WiFi e não é afetada por nenhuma das técnicas de evasão acima.
- **A confirmação visual reforça o silêncio sem fio**: uma câmera claramente ligada e iluminando à noite ainda registrou zero detecções WiFi legítimas, descartando «a câmera foi removida» como explicação para aquela unidade específica.
- **Uma detecção zero em uma câmera conhecida não significa automaticamente que seu hardware está quebrado.** Atualize primeiro o firmware e depois confirme que a câmera ainda está fisicamente no local.
- **Este projeto de código aberto continua lançando correções quando a comunidade encontra lacunas.** Leia os issues do GitHub, não apenas o README, para saber o estado atual da detecção.

### Próximas etapas

1. **Atualize o firmware** para o branch `main` atual antes de solucionar qualquer outro problema: **[github.com/colonelpanichacks/flock-you](https://github.com/colonelpanichacks/flock-you)**
2. **Leia o guia completo de hardware** se ainda não o fez: **[Projeto de detecção Flock-You: guia de hardware de contravigilância](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)**
3. **Compare possíveis zonas sem detecção** com o **[Flock Finder](/articles/flock-finder-alpr-surveillance-mapping-tool/)** antes de concluir que seu dispositivo deixou algo passar
4. **Entenda o que você enfrenta**: **[Vigilância por câmeras Flock Safety: prevalência, preocupações com privacidade e estratégias de proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)**
5. **Combine detecção WiFi e celular** usando o **[Rayhunter](/articles/how-to-flash-rayhunter-devices-complete-guide/)** para uma visão mais ampla da contravigilância, pois nenhum método deste artigo detecta simuladores de estação rádio-base

{{< centerbutton href="https://stscollective.com/discount/SIMEONONSECURITY" >}}
  Compre dispositivos FlockYou prontos para uso e economize 20%
{{< /centerbutton >}}

______

## Artigos relacionados

| Artigo | O que aborda |
|---|---|
| **[Projeto de detecção Flock-You: guia de hardware de contravigilância](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Guia técnico completo das três plataformas de hardware, da configuração de firmware e do método de detecção que fundamenta este artigo |
| **[Flock Finder: mapeie todas as câmeras Flock suspeitas perto de você](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Compare uma possível zona sem detecção com mais de 40.000 locais de câmeras mapeados antes de solucionar problemas do dispositivo |
| **[Câmeras Flock: ferramenta de segurança pública ou máquina de vigilância sem mandado?](/articles/flock-cameras-public-safety-or-surveillance-2026/)** | Análise independente do que o banco de dados da Flock permite e por que a questão do mandado importa mais que a detecção |
| **[Vigilância por câmeras Flock Safety: prevalência, preocupações com privacidade e estratégias de proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Panorama da escala de implantação, de casos documentados de abuso e de recursos para organização comunitária |
| **[Vulnerabilidades em câmeras Flock Safety: mais de 50 falhas encontradas](/articles/flock-safety-camera-security-vulnerabilities-research-2026/)** | Pesquisa de segurança de hardware e software das câmeras Flock, separada da questão de detecção sem fio deste artigo |
| **[Como instalar o Rayhunter: guia completo](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detecte simuladores de IMSI e stingrays, o equivalente celular da lacuna de detecção WiFi descrita aqui |

______

## Referências

1. [Repositório Flock-You no GitHub - colonelpanichacks](https://github.com/colonelpanichacks/flock-you)
2. [GitHub Issue #20 - câmeras Flock não detectadas, mas outros dispositivos detectados](https://github.com/colonelpanichacks/flock-you/issues/20)
3. [GitHub Issue #43 - sinal 5GHz? Novo OUI ou filtragem de endereço MAC](https://github.com/colonelpanichacks/flock-you/issues/43)
4. [Conjunto de dados de pesquisa OUI de NitekryDPaul](https://github.com/colonelpanichacks/flock-you/blob/main/datasets/NitekryDPaul_wifi_ouis.md)
5. [nitekry/nite-oui-collection](https://github.com/nitekry/nite-oui-collection)
6. [DeFlock Joplin - pesquisa comunitária de ALPR](https://deflockjoplin.today)
7. [Pintor, L. e Atzori, L. (2022) - análise de solicitações Probe WiFi para impressão digital de elementos de informação, IEEE GLOBECOM](https://ieeexplore.ieee.org/document/10001618)
8. [WIRED e 404 Media - hackers invadiram uma câmera Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
9. [Micah Lee - câmeras Flock têm mais de 50 vulnerabilidades e credenciais embutidas](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
10. [Distributed Denial of Secrets - imagens de sistemas de arquivos de câmeras Flock ALPR](https://ddosecrets.org/article/flock-alpr-camera)
11. [Hackaday - esta semana em segurança: câmeras Flock são antigas](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
12. [WiFi Mothership - referência de detecção e dispositivos ALPR da Flock Safety](https://wifimothership.com/flock)
13. [GainSec - pesquisa de firmware e avisos de segurança](https://gainsec.com/)
8. [A busca pelo probe oculto - comportamento de probes curinga com SSID oculto](https://goodwi.fi/posts/2023/12/hunt-for-hidden-probe/)
9. [DeFlock - mapa comunitário colaborativo de câmeras ALPR](https://deflock.org/)
10. [Colonel Panic Tech - OUI-SPY e hardware de detecção](https://colonelpanic.tech)
11. [STS Collective - dispositivos FlockYou](https://stscollective.com/discount/SIMEONONSECURITY)
12. [Algo estranho está acontecendo com as câmeras Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/cVf-id71BuQ)
13. [Wardriving infravermelho de câmeras Flock - Valleytech Custom Solutions](https://www.youtube.com/shorts/mzpr6bslsYA)
14. [Câmeras Flock ligadas, mas sem transmissão - Valleytech Custom Solutions](https://www.youtube.com/shorts/sjI8FB0cLk0)
15. [Reconhecimento automático de placas - Wikipedia (iluminação infravermelha em sistemas ANPR/ALPR)](https://en.wikipedia.org/wiki/Automatic_number-plate_recognition)
16. [Seeed Studio XIAO ESP32S3 Sense](https://www.seeedstudio.com/XIAO-ESP32S3-Sense-p-5639.html)
17. [Módulo GNSS L76K para Seeed Studio XIAO](https://www.seeedstudio.com/L76K-GNSS-Module-for-Seeed-Studio-XIAO-p-5864.html)

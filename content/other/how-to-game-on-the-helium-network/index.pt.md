---
title: "Jogando na rede Helium: explorando vulnerabilidades com MiddleMan e Chirp Stack Packet Multiplexer"
date: 2023-02-18
toc: true
draft: false
description: "Aprenda a manipular a rede Helium explorando vulnerabilidades com MiddleMan e Chirp Stack Packet Multiplexer, bem como os riscos e consequências de fazê-lo."
tags: ["rede de hélio", "Comprovante de Cobertura", "Intermediário", "Multiplexador de pacote de pilha Chirp", "jogos", "explorando vulnerabilidades", "rede LoRaWAN", "criptomoeda", "blockchain", "rede descentralizada", "pontos de acesso", "falsificação", "trapaceando", "atividade ilegal", "penalidades", "integridade da rede", "recompensas", "atores maliciosos", "segurança de rede", "hosts legítimos"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "Uma representação caricatural de um grupo de indivíduos explorando um balão de hélio com uma imagem de um gateway LoRaWAN e MiddleMan ou Chirp Stack Packet Multiplexer ao fundo."
coverCaption: ""
---

**Isenção de responsabilidade**:
É importante observar que jogar na rede Helium é uma atividade ilegal e antiética fortemente desaprovada pela comunidade Helium e pela comunidade mais ampla de criptomoedas e blockchain. Jogar na rede prejudica a integridade da rede e prejudica os hosts legítimos que fornecem uma cobertura valiosa para a rede.

Além disso, embora o uso de MiddleMan e Chirp Stack Packet Multiplexer para explorar vulnerabilidades na rede Helium possa ser motivo de preocupação, é importante observar que esses problemas só podem ser corrigidos pelo Helium com a introdução de gateways seguros. Isso exigiria a substituição de todos os pontos de acesso na rede, o que é um empreendimento significativo e pode não ser viável. Como resultado, a comunidade Helium precisa permanecer vigilante e proativa ao enfrentar os desafios impostos pelos jogos na rede.

Também é importante notar que a equipe da Helium está ciente do problema há algum tempo e tomou medidas para resolvê-lo, mas mais ações são necessárias para resolver o problema. A comunidade está pedindo que ações reais sejam tomadas para lidar com essas vulnerabilidades e garantir que a rede possa continuar a escalar e crescer de maneira segura e confiável.

Ao escrever este artigo, esperamos aumentar a conscientização sobre a questão dos jogos na rede Helium e o uso de MiddleMan e Chirp Stack Packet Multiplexer para explorar vulnerabilidades no sistema. Acreditamos que, ao esclarecer esse problema e trazer mais publicidade a ele, a comunidade Helium e a comunidade mais ampla de blockchain e criptomoeda podem se unir para resolver o problema e trabalhar para uma rede mais segura e confiável.

Além disso, ao destacar esse problema, esperamos encorajar a equipe da Helium a tomar medidas mais decisivas para lidar com as vulnerabilidades da rede e implementar medidas de segurança mais robustas para evitar jogos no futuro. Acreditamos que é importante para a equipe Helium ser transparente sobre seus esforços para resolver esse problema e se comunicar com a comunidade sobre seu progresso na correção dessas vulnerabilidades.

Finalmente, ao trazer mais publicidade para esta questão, esperamos encorajar uma maior conscientização e educação sobre os riscos e consequências dos jogos na rede Helium. É importante que os usuários entendam a importância do comportamento ético na rede e os danos potenciais que podem ser causados pelo jogo. Ao trabalharmos juntos para resolver esses problemas, podemos ajudar a garantir o crescimento contínuo e o sucesso da rede Helium.

Em resumo, jogar na rede Helium não é tolerado pela comunidade ou por nós, e encorajamos os usuários a agir de forma ética e legal ao participar da rede. Embora existam vulnerabilidades na rede que possam ser exploradas, é importante permanecer vigilante e proativo ao lidar com esses problemas e trabalhar para criar uma rede mais segura e confiável para todos os usuários.

# Como jogar a rede de hélio com MiddleMan e Chirp Stack Packet Multiplexer
A rede Helium é uma rede LoRaWAN® descentralizada que compensa aqueles que hospedam pontos de acesso físicos recompensando-os com tokens Helium ou $HNT. Esse sistema é conhecido como Proof-of-Coverage (PoC). À medida que a rede cresceu e a conscientização sobre esse projeto aumentou, houve um número cada vez maior de trapaceiros que estão explorando o protocolo e os mecanismos de recompensa. Neste artigo, discutiremos como manipular a rede Helium usando MiddleMan e Chirp Stack Packet Multiplexer.

## Compreendendo o problema de jogos em rede de hélio
A rede Helium depende da Prova de Cobertura para garantir que os hotspots estejam fornecendo cobertura onde ela é necessária. No entanto, esse sistema é vulnerável a jogos, falsificações, hackers e outros tipos de mau comportamento que podem prejudicar a rede. O problema do jogo na rede Helium está custando aos hosts legítimos milhares de $ HNT por mês. A Helium, Inc, junto com a DeWi, tomou medidas agressivas no início de 2022 para ajudar a erradicar esse problema.

## Hardware Necessário
- [Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
- [Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
- [Raspberry Pi](https://amzn.to/3KjFCYp)
- [Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## Usando o MiddleMan para manipular a rede de hélio
Uma maneira de manipular a rede Helium é usando o MiddleMan. MiddleMan é uma ferramenta de software que pode ser usada para criar um ponto de acesso falso que parece fornecer cobertura em um local específico. Ao usar o MiddleMan, um usuário pode criar um ponto de acesso falso que receberá recompensas por fornecer cobertura em uma área específica, mesmo que o ponto de acesso não esteja fisicamente localizado nessa área.

Para usar o MiddleMan, o usuário precisa instalar o software e criar um ponto de acesso falso. O usuário pode então configurar o ponto de acesso para relatar sua localização à rede Helium usando uma ferramenta de falsificação de GPS. A rede Helium acreditará que o ponto de acesso falso está fornecendo cobertura no local especificado e recompensará o usuário com $HNT.

Você configuraria seu gateway lorawan para apontar para este software e manipular os valores para que todos os PoCs recebidos fossem considerados válidos. O uso do encaminhador semtech é um dos vários padrões da comunidade LoraWAN. Corrigir o problema de manipulação exigiria reinventar a roda e implementar seu próprio protocolo desde o início. Coisas como somas de verificação e criptografia impediriam que isso acontecesse. Mas também tornaria mais difícil para fornecedores com hardware diferente criar pontos de acesso. Sem mencionar que é um caso de uso suportado ter um minerador de hélio e vários gateways lora para melhorar a cobertura. Embora este seja mais um problema de nível empresarial.

 - [helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## Usando o multiplexador de pacotes Chirp Stack para manipular a rede de hélio
Outra maneira de manipular a rede Helium é usando o multiplexador de pacotes Chirp Stack. Chirp Stack Packet Multiplexer é uma ferramenta que pode ser usada para criar um ponto de acesso virtual que pode receber pacotes de vários pontos de acesso físicos. Ao usar o multiplexador de pacotes Chirp Stack, um usuário pode criar um ponto de acesso virtual que recebe pacotes de pontos de acesso físicos em vários locais, o que aumentará as recompensas recebidas.

Para usar o multiplexador de pacotes Chirp Stack, o usuário precisa instalar o software e configurá-lo para receber pacotes de pontos de acesso físicos ou gateways lorawan em vários locais. O hotspot receberá os pacotes e informará sua localização à rede Helium, que recompensará o usuário com $HNT.

Isso permite a entrada de vários encaminhadores e a saída de vários gateways. Existem casos de uso legítimos para este software na comunidade LoraWAN, mas usá-lo em hélio é, na melhor das hipóteses, uma área cinzenta. Depende de como você o usa e também qual é a sua intenção.

A configuração deste requer alguns arquivos de configuração. Mas isso pode ser feito em 5 minutos ou menos.
- [chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## Riscos e Consequências de Jogar na Rede Helium
Jogar na rede Helium é uma atividade arriscada e ilegal que pode ter sérias consequências. A Helium, Inc, junto com a DeWi, está trabalhando ativamente para detectar e prevenir jogos na rede, e os usuários que forem pegos jogando na rede serão penalizados.

As penalidades por jogar na rede Helium podem incluir a perda de acesso à rede, o banimento permanente de pontos de acesso e a perda de qualquer $ HNT ganho por meio de jogos. Além disso, manipular a rede Helium prejudica a integridade da rede e prejudica os hosts legítimos que fornecem uma cobertura valiosa para a rede.

## Conclusão
Embora a rede Helium ofereça oportunidades para hosts de hotspot legítimos ganharem recompensas por meio de Prova de Cobertura, ela também apresenta um alvo atraente para agentes mal-intencionados que procuram burlar o sistema. O uso de MiddleMan e Chirp Stack Packet Multiplexer, embora não tolerado pela Helium Inc. ou pela comunidade em geral, é um exemplo de como alguns atores mal-intencionados estão explorando vulnerabilidades na rede para colher recompensas às custas de outros.

É importante que a comunidade Helium continue a trabalhar em conjunto para identificar e abordar jogos na rede, pois isso ameaça a integridade do sistema e prejudica os esforços de hosts legítimos. Isso pode incluir esforços para desenvolver e implementar medidas de detecção e prevenção mais sofisticadas, bem como aumentar a conscientização e a educação sobre os riscos e consequências dos jogos na rede.

Em última análise, o sucesso da rede Helium depende da disposição de suas partes interessadas em trabalhar juntas para construir um sistema seguro, confiável e confiável que forneça valor real a seus usuários. Ao se manter vigilante e proativo ao enfrentar os desafios impostos pelos jogos, a comunidade pode ajudar a garantir que a rede Helium continue crescendo e evoluindo em uma direção positiva.
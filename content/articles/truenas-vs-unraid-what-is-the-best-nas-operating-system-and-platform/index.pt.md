---
title: "Unraid vs TrueNas: qual sistema operacional NAS é ideal para você?"
date: 2023-02-16
toc: true
draft: false
description: "Uma comparação abrangente de Unraid e TrueNas, incluindo sua facilidade de uso, recursos, documentação e comunidade, para ajudar os usuários a tomar uma decisão informada sobre qual sistema operacional NAS é melhor para suas necessidades."
tags: ["não atacado", "TrueNAS", "Sistema operacional NAS", "Comparação", "Facilidade de uso", "Características", "Documentação", "Comunidade", "Código aberto", "Empreendimento", "Proteção de dados", "Desempenho", "Flexibilidade", "Fácil de usar", "Aplicativos de terceiros", "Armazenamento conectado à rede", "Tecnologia RAID", "Gerenciamento de armazenamento", "OpenZFS", "Usuários domésticos", "Modelo de preços", "Armazenamento na núvem", "virtualização", "Central de Documentação", "Fórum da Comunidade", "Proteção Avançada de Dados", "SO NAS maduro", "Especialização Técnica", "Profissionais de TI"]
cover: "/img/cover/Two_computer_servers_facing_each_other_one_blue_one_green.png"
coverAlt: "Dois servidores um de frente para o outro, um azul e outro verde. No lado azul, uma pessoa está usando um capacete e colete de segurança. Do lado verde uma pessoa sentada no sofá."
coverCaption: ""
---

Quando se trata de **construir um sistema de armazenamento conectado à rede (NAS), dois dos sistemas operacionais mais conhecidos para computadores baseados em x86 são TrueNas e Unraid**. Ambos fornecem recursos poderosos para gerenciar um sistema NAS, mas sua principal diferença está no método de gerenciamento de armazenamento.

Neste artigo, compararemos TrueNas e Unraid para auxiliá-lo na tomada da melhor decisão para suas necessidades.

## Visão geral do Unraid

**Unraid é um sistema operacional NAS proprietário desenvolvido pela Lime Technology**, uma empresa de software localizada na Califórnia. Foi criado em 2005 e roda na plataforma Linux. O objetivo do Unraid é tornar a tecnologia RAID mais acessível, eliminando as restrições de tamanho de disco, velocidade, marca e protocolo. Isso permite fácil expansão de matrizes RAID e minimiza o risco de perda de dados.

______

## Introdução ao TrueNas

**TrueNas, anteriormente conhecido como FreeNas, é um sistema operacional NAS de código aberto desenvolvido pela iXsystems**, uma empresa privada com sede em San Jose, Califórnia. Foi lançado em 2005 e é construído em FreeBSD e Linux. Os desenvolvedores TrueNas se concentram no mercado corporativo e sua escolha do sistema de arquivos padrão (OpenZFS) reflete esse foco.

______

## Custo

**Usuários domésticos que procuram o melhor sistema operacional NAS geralmente se preocupam com o custo**. Nesse sentido, TrueNas é um claro vencedor, pois é de código aberto e totalmente gratuito, pelo menos para TrueNas CORE, a versão voltada para usuários domésticos e aplicativos de armazenamento não críticos.

Por outro lado, o Unraid não é gratuito, mas usa um modelo de preço justo sem assinaturas ou taxas ocultas. Existem três planos Unraid para escolher, cada um diferindo apenas no número de dispositivos de armazenamento que podem ser conectados. O plano Básico custa $ 59, o plano Plus custa $ 89 e o plano Pro custa $ 129.

______

## Facilidade de uso

**Unraid coloca uma forte ênfase na facilidade de uso e flexibilidade**. Ele possui um sistema de gerenciamento de armazenamento exclusivo que permite aos usuários misturar e combinar diferentes tamanhos e tipos de disco e adicionar ou remover discos sem qualquer interrupção. Ele também oferece uma interface de usuário direta e simples, tornando fácil até mesmo para usuários não técnicos configurar e gerenciar um sistema NAS.

**TrueNas, por outro lado, é voltado para o mercado corporativo e requer conhecimentos mais avançados para configurar e gerenciar**. Sua escolha do sistema de arquivos OpenZFS fornece recursos avançados de proteção de dados, como instantâneos, compactação de dados e soma de verificação para garantir a integridade dos dados.

______

## Características

**Tanto TrueNas quanto Unraid oferecem suporte** para compartilhamentos NFS, SMB para Windows e AFP para macOS e iOS. Além disso, o TrueNas fornece serviços iSCSI, LDAP, Active Directory e Kerberos. O Unraid não oferece esses serviços, mas oferece suporte a contêineres Docker, dando aos usuários acesso a uma ampla variedade de aplicativos.

**TrueNas também possui suporte integrado para serviços de armazenamento em nuvem**, como Amazon S3, Google Cloud e Microsoft Azure, facilitando a movimentação de dados para a nuvem. Os usuários sem invasão podem usar soluções de terceiros, mas podem exigir instalação e configuração adicionais.

**A plataforma baseada em Linux do Unraid também permite a configuração de máquinas virtuais** usando KVM e atribuindo dispositivos PCI/USB, como placas gráficas, a máquinas virtuais. Isso torna possível usar o mesmo computador para fins de centro de mídia e jogos.

**TrueNas inclui sua própria tecnologia de conteinerização**, Jails, e sua própria opção de virtualização, Bhyve. Embora o TrueNas ofereça muitos dos aplicativos populares de terceiros, como o Plex, a seleção geral de software pode ser menor em comparação com o Unraid.

______

## Documentação e Comunidade

O TrueNas possui um hub de documentação abrangente, cobrindo tudo, desde a configuração até APIs e plataformas de hardware. O site Unraid tem uma seção de documentação menos extensa, mas é mais fácil de navegar. No entanto, o Unraid não possui uma página de suporte individual, mas os usuários são incentivados a fazer perguntas no fórum oficial da comunidade, que é descrito como amigável, informativo e útil.

TrueNas também tem seu próprio fórum oficial da comunidade, mas pode não ser tão acolhedor para iniciantes quanto o fórum Unraid. Isso ocorre porque muitos usuários do TrueNas são profissionais de TI focados no gerenciamento de armazenamento corporativo.

______

## Conclusão

Ambos TrueNas e Unraid são sistemas operacionais NAS poderosos e maduros, cada um com seus próprios pontos fortes e fracos. O TrueNas é ideal para aqueles com conhecimento avançado de gerenciamento de armazenamento e que desejam os recursos avançados de proteção de dados do OpenZFS. O Unraid, por outro lado, é melhor para usuários domésticos que desejam um sistema NAS flexível e fácil de usar.

Resumindo:

**TrueNas Prós:**
- Gratuito e de código aberto
- Proteção avançada de dados com OpenZFS
- Grande performance

**TrueNas Contras:**
- Mais difícil de usar
- Comunidade hostil

**Prós Unraid:**
- Fácil de usar
- Grande variedade de aplicativos de terceiros
- Comunidade amigável

**Desvantagens do Unraid:**
- Desempenho limitado

Em última análise, a decisão entre TrueNas e Unraid dependerá de suas necessidades específicas e nível de conhecimento técnico. Considere seus requisitos, compare os recursos e benefícios de cada um e tome uma decisão informada.

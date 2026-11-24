---
title: "Kali Purple 2023.1: atualizações e recursos essenciais"
date: 2023-04-08
lastmod: 2026-11-24
toc: true
draft: false
description: "Análise dos recursos, ferramentas e melhorias históricas do Kali Purple 2023.1, com referências atuais para laboratórios de segurança."
tags: ["Kali Linux", "Kali Purple", "2023.1", "hacking ético", "teste de invasão", "cibersegurança", "ferramentas", "framework de exploração", "atualizações do Kali ARM", "Kali NetHunter", "documentação do Kali", "suporte ao kernel", "suporte a Bluetooth", "LineageOS", "OneUI", "Radxa Zero", "computador de placa única", "correções do kernel", "contribuições da comunidade", "Kali Discord", "atualizações do Linux", "distribuição para hacking ético", "novos recursos", "melhorias", "Xfce", "KDE", "GNOME", "Xfce 4.18", "KDE Plasma 5.27", "novas ferramentas e pacotes", "suporte a dispositivos ARM", "documentação do Kali", "regulamentações governamentais"]
cover: "/img/cover/A_3D_animated_Kali_Linux_dragon_mascot_surrounded.webp"
coverAlt: "Um dragão tridimensional do Kali Linux está sentado sobre um escudo, cercado por ferramentas de cibersegurança."
coverCaption: ""
---

**Kali Purple 2023.1: análise**

Kali Purple 2023.1 foi a primeira prévia técnica da direção de segurança defensiva do Kali. Essa já não é a versão mais recente do Kali. Este artigo registra o lançamento original e inclui referências atuais para que você não confunda as versões dos pacotes de 2023.1 com as atuais.

## Situação atual do Kali

O histórico oficial de lançamentos do Kali lista o Kali 2026.2, lançado em 29 de junho de 2026, como o segundo lançamento rolling de 2026. Ele usa o kernel Linux 6.19 e o Xfce 4.20.7. As [notas do Kali 2026.2](https://www.kali.org/blog/kali-linux-2026-2-release/) também descrevem o GNOME 50, o KDE Plasma 6.6, a mudança de `sources.list` para `sources.list.d/kali.source` e alterações na inicialização de máquinas virtuais.

O Kali Purple representa uma direção defensiva e de purple team dentro do Kali. O anúncio de 2023.1 descreveu uma prévia técnica com arquitetura de referência SOC-in-a-box, ferramentas defensivas e categorias de menu do NIST Cybersecurity Framework. Esses detalhes representam o escopo histórico. Para escolher pacotes atuais, consulte a [documentação de metapacotes](https://www.kali.org/docs/general-use/metapackages/) do Kali e selecione apenas os grupos de ferramentas necessários ao seu laboratório.

*Realize cada exercício de segurança ofensiva ou defensiva em um laboratório isolado e autorizado. Instalar o Kali não concede permissão para testar sistemas que você não possui nem administra.*

______

## Papel de parede e atualizações da área de trabalho do Kali

O Kali Purple 2023.1 apresenta o **novo papel de parede padrão** Kali Sticker, com fundo roxo e vários adesivos relacionados ao Kali. A arte foi inspirada no trabalho de /u/Albert-III- e TJ_Null.

Além do novo papel de parede, o Kali Purple 2023.1 atualiza os três principais ambientes de desktop: **Xfce, KDE e GNOME**. As atualizações incluem novos recursos, melhorias de desempenho e correções de bugs.

______

## Xfce 4.18

**Xfce 4.18** traz várias melhorias importantes, como:

- Suporte aprimorado ao escalonamento da interface
- Atualizações do gerenciador de arquivos Thunar
- Perfis de painel para facilitar a personalização

______

## KDE Plasma 5.27

A atualização **KDE Plasma 5.27** apresenta:

- Um novo sistema de organização de janelas em mosaico
- Um tema de aplicativo mais elegante
- Ferramentas e widgets mais limpos e fáceis de usar

______

## Atualizações do GNOME

No GNOME, o Kali Purple 2023.1 traz melhorias de usabilidade. Por exemplo, pressionar F4 abre rapidamente um terminal na pasta atual do gerenciador de arquivos.

______

## Configurações padrão do kernel e problemas conhecidos

O Kali Purple 2023.1 atualiza alguns valores padrão do kernel para facilitar o uso.

______

## Novas ferramentas e pacotes

O Kali Purple 2023.1 adiciona ferramentas e pacotes que ampliam os recursos de **testes de invasão** e **hacking ético**. Entre as novidades estão:

- **Rizin 0.3.0**: Um framework moderno de engenharia reversa
- **Ghidra 10.1**: Uma suíte de código aberto para engenharia reversa de software
- **Python 3.10**: A versão mais recente da linguagem de programação popular

Essas ferramentas e as atualizações dos pacotes existentes ampliaram a prévia 2023.1 para profissionais de segurança. As versões desta seção pertencem ao lançamento 2023.1, não às versões incluídas no Kali 2026.2.

______

## Suporte a dispositivos ARM

O Kali Purple 2023.1 continua ampliando o suporte a dispositivos ARM. Ele adiciona compatibilidade com novos dispositivos, como o **Radxa Zero**, e melhora o suporte existente a modelos como o **LG V20**. Essa ampla compatibilidade permite usar o Kali em vários tipos de hardware, de computadores de placa única a smartphones potentes.

______

## Documentação e comunidade

A equipe do Kali atualizou a **documentação** com novos guias, tutoriais e dicas de solução de problemas para ajudar os usuários a aproveitar o Kali Purple 2023.1. Também reconheceu membros da comunidade por suas contribuições, destacando a colaboração de código aberto e a força da comunidade Kali.

______

## Regulamentações governamentais

Este artigo não aborda regulamentações governamentais específicas sobre hacking ético ou testes de invasão. Essas atividades, porém, são regulamentadas em muitas jurisdições. Obtenha as permissões necessárias e siga as leis aplicáveis ao realizar avaliações de segurança. Para saber mais, consulte:

- [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
- [Regulamento Geral sobre a Proteção de Dados (GDPR)](https://gdpr.eu/)

______

## Conclusão

**Kali Purple 2023.1** foi a primeira prévia da direção de segurança defensiva do Kali. A versão ampliou o conjunto de ferramentas, melhorou o suporte ARM e expandiu a documentação. Para uma instalação atual, consulte as notas de lançamento do Kali e escolha os pacotes adequados ao seu laboratório. Siga as regras aplicáveis e teste sistemas somente com autorização explícita.

______

## Referências

1. [Site oficial do Kali Linux](https://www.kali.org/)
2. [Documentação do Kali Linux](https://www.kali.org/docs/)
3. [Downloads do Kali Linux](https://www.kali.org/get-kali/)
4. [Computer Fraud and Abuse Act (CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act#:~:text=The%20Computer%20Fraud%20and%20Abuse%20Act%20of%201986,without%20authorization%2C%20or%20in%20excess%20of%20authorization.%20)
5. [Regulamento Geral sobre a Proteção de Dados (GDPR)](https://gdpr.eu/)

______

## Recursos adicionais

- [Fóruns oficiais do Kali Linux](https://forums.kali.org/)
- [Blog do Kali Linux](https://www.kali.org/blog/)
- [Treinamento e certificação do Kali Linux](https://www.offensive-security.com/)

______

## Lista de verificação de atualização

- **Consulte o histórico de lançamentos.** Leia o [histórico atual de lançamentos do Kali](https://www.kali.org/releases/) antes de baixar uma imagem.
- **Use imagens oficiais.** Baixe pelo [Get Kali](https://www.kali.org/get-kali/) e verifique os checksums publicados.
- **Atualize instalações rolling.** Siga a [documentação atual de atualização do Kali](https://www.kali.org/docs/general-use/updating-kali/) em vez de copiar sem revisão o exemplo de repositório de 2023.1.
- **Escolha metapacotes com cuidado.** Um laboratório padrão ou Purple não precisa de todos os pacotes do Kali.
- **Defina o escopo do laboratório.** Registre sistemas autorizados, janelas de teste, logging e limpeza antes de executar ferramentas.

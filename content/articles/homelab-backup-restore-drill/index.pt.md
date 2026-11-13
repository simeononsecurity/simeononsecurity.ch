---
title: "Faça um teste de restauração de backup do homelab com Restic"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Verifique se um backup do homelab restaura arquivos utilizáveis. Defina uma meta de recuperação, restaure com Restic em outro local, confira os dados e registre o resultado."
genre: ["Homelab", "Backup", "Recuperação de desastres"]
tags: ["backup de homelab", "teste de restauração", "restauração Restic", "verificação de backup", "teste de recuperação", "recuperação de desastres", "RPO", "RTO", "repositório de backup", "verificação Restic", "backup NAS", "backup de servidor", "recuperação de VM", "restauração de arquivos", "criptografia de backup", "monitoramento de backup", "plano de recuperação", "teste de backup", "backup externo", "integridade dos dados"]
cover: "/img/cover/homelab-backup-restore-drill.webp"
coverAlt: "Um servidor homelab e um NAS fazem backup em uma unidade separada, com uma pasta de restauração verificada em um computador de teste isolado e um cronômetro."
coverCaption: "Restaure em um destino separado, confira os dados e meça o tempo necessário."
---

Uma tarefa de backup marcada como bem-sucedida não mostra se você consegue restaurar um arquivo utilizável. Um **teste de restauração** verifica o caminho entre o backup armazenado e os dados funcionais sem substituir seus arquivos ativos. Este guia usa o Restic em um exemplo de restauração de arquivos e fornece um registro para repetir após mudanças no laboratório.

<!--more-->

Restic é um programa de backup. Um **repositório** é a área de armazenamento protegida que contém os dados do backup. Um **snapshot** é um ponto de backup salvo.

## Principais conclusões

- **Escolha uma meta:** Selecione os arquivos ou o serviço que precisa recuperar e defina um ponto e um prazo de recuperação aceitáveis.
- **Restaure separadamente:** Use um destino de teste vazio para impedir que o teste sobrescreva dados ativos.
- **Confira o resultado:** Abra os arquivos restaurados, verifique os dados do aplicativo quando possível e meça o tempo decorrido.
- **Registre falhas:** Anote o ID do snapshot, itens ausentes, permissões e reparos no plano de recuperação.

## Antes de começar

Você precisa de um repositório de backup funcional, da senha ou chave dele, de espaço livre suficiente no destino e de permissão para ler o backup e o local de teste. Este exemplo pressupõe que o Restic esteja instalado e que o repositório contenha um backup recente de arquivos. O [guia de início rápido do Restic](https://restic.readthedocs.io/en/stable/010_introduction.html) explica a criação do repositório e os primeiros backups. O [guia de backup 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/) do site trata da localização das cópias. A [visão geral de homelab](/articles/what-is-a-homelab-and-should-you-have-one/) inclui uma breve lista para testar backups.

Este teste verifica arquivos de um snapshot. Um banco de dados, uma máquina virtual ou um aplicativo também precisa de etapas próprias de recuperação. Mantenha o sistema de teste isolado se iniciar o serviço restaurado puder interferir no serviço ativo. Uma cópia de arquivos bem-sucedida não prova que todos os serviços iniciarão.

> **Aviso:** No primeiro teste, não restaure sobre um caminho ativo. Use um diretório de teste vazio em outro sistema de arquivos ou host de teste. Não coloque a senha do repositório em capturas de tela, chamados ou histórico do shell.

## Defina a meta de recuperação

Anote o que você precisa após uma falha. O **objetivo de ponto de recuperação (RPO)** é o ponto no tempo até o qual os dados precisam ser recuperados após uma interrupção. Ele representa a perda máxima de dados aceitável. O **objetivo de tempo de recuperação (RTO)** indica por quanto tempo o serviço pode ficar indisponível. O NIST define ambos no [guia de planejamento de contingência](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-34r1.pdf). Suas metas devem refletir a frequência de alteração dos dados e o tempo de restauração no seu hardware.

| Item | Meta ilustrativa | O que registrar |
|---|---|---|
| **Documentos da família** | Último backup noturno | Horário do último snapshot e arquivos abertos |
| **Configuração do serviço doméstico** | Última alteração conhecida como válida | Versão da configuração e segredos necessários |
| **Biblioteca de mídia em armazenamento conectado à rede (NAS)** | Backup semanal | Reprodução de amostra e tempo de restauração |

As metas acima são exemplos, não resultados medidos. No plano de recuperação, registre onde o backup fica armazenado e como uma pessoa autorizada obtém a senha do repositório ou a chave de criptografia. Não coloque valores secretos no plano nem no registro do teste. Armazene os segredos por um caminho protegido e independente do host que falhou. Um repositório que sobrevive, mas perde sua única senha, não pode ser recuperado.

Escolha um **conjunto de arquivos críticos** para este teste. Inclua um arquivo pequeno que você sabe que deveria estar no snapshot mais recente. Para um serviço, liste também a configuração, a exportação do banco de dados, os certificados e a versão do aplicativo necessários para iniciá-lo. Confirme que o método de backup captura dados consistentes do aplicativo antes de confiar em uma cópia de arquivos de um banco de dados em execução.

## Encontre um snapshot

Use o acesso ao repositório autorizado para o teste. O Restic usa um bloqueio temporário do repositório enquanto lê ou altera dados de backup. Os comandos abaixo pressupõem que o repositório permita essa operação. Mantenha a origem ativa e o destino de teste separados. Substitua `/path/to/repository` pelo caminho real do repositório Restic e liste os snapshots:

```bash
restic -r /path/to/repository snapshots
```

O Restic solicita a senha do repositório se você não a tiver fornecido por um método configurado para proteger segredos. A [lista de snapshots](https://restic.readthedocs.io/en/stable/010_introduction.html) mostra ID, data, host e caminhos de origem. Registre o ID e o horário do snapshot que pretende testar. Compare o horário com seu RPO. O log recente de uma tarefa não substitui essa conferência, pois o snapshot necessário pode ser mais antigo do que você imagina.

Se o snapshot esperado não estiver lá, pare o teste e investigue o cronograma de backup, a seleção da origem e o caminho do repositório. Não escolha discretamente um snapshot mais antigo e informe que a meta de recuperação foi atingida.

## Restaure em um destino vazio

Crie um **diretório de destino vazio** em um sistema de arquivos de teste com espaço suficiente para o snapshot. Não use como destino a origem original, um compartilhamento de produção montado ou uma pasta existente com dados que você queira manter. Substitua `SNAPSHOT_ID` e os dois caminhos de exemplo antes de executar o comando:

```bash
restic -r /path/to/repository restore SNAPSHOT_ID \
  --target /path/to/empty-restore-drill
```

O [guia de restauração do Restic](https://restic.readthedocs.io/en/stable/050_restore.html) descreve o ID do snapshot e o caminho `--target`. A árvore restaurada mantém o caminho da origem sob o diretório de destino. Localize os arquivos reais antes de avaliar o resultado. Se precisar de apenas um subconjunto, use os [filtros de inclusão documentados](https://restic.readthedocs.io/en/stable/050_restore.html) e registre o que excluiu. Não use `--delete` em um teste. O Restic informa que essa opção remove do destino os arquivos ausentes no snapshot.

Inicie um cronômetro quando a restauração começar. Pare quando os arquivos necessários estiverem presentes e utilizáveis, não quando o comando mostrar o primeiro progresso. Registre a localização do repositório, o link de rede, o tamanho dos dados e o host de teste, pois essas condições afetam uma recuperação futura.

> **Resultado esperado:** O snapshot escolhido é restaurado em um destino separado sem modificar a origem ativa.

## Verifique os dados e o serviço

Abra alguns arquivos restaurados com o aplicativo que normalmente os lê. Inclua um arquivo recente, um antigo e outro de um diretório aninhado. Compare tamanhos ou somas de verificação conhecidas, caso as tenha registrado antes do backup. No Linux, verifique proprietário e permissões: um arquivo legível pela conta de teste ainda pode falhar na conta do serviço.

Para um serviço, restaure em uma instância de teste isolada. Confira a configuração, os segredos necessários, a consistência do banco de dados, a inicialização e uma ação representativa do usuário. Uma restauração de arquivos sem banco de dados ou segredo não recupera o serviço por completo. Nunca inicie a instância de teste usando o banco de dados ativo ou um endereço de produção sem um plano controlado de transição.

Depois da restauração da amostra, execute a verificação do repositório do Restic:

```bash
restic -r /path/to/repository check
```

Para ler todos os dados do repositório, use `check --read-data` durante uma janela de manutenção. O Restic avisa que o comando lê o repositório inteiro e pode baixar muitos dados de um backend remoto. O [guia de solução de problemas do Restic](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) descreve a verificação e o custo. Uma verificação limpa aumenta a confiança, mas não substitui abrir os arquivos restaurados ou iniciar o serviço.

```bash
restic -r /path/to/repository check --read-data
```

Compare a idade do snapshot com seu RPO e o tempo de recuperação medido com seu RTO. Se qualquer uma das metas falhar, o teste falhou, mesmo que o Restic termine sem erro. Ajuste a frequência do backup, o local de armazenamento, a largura de banda ou o procedimento de recuperação e teste novamente.

## Mantenha um registro de restauração

Escreva um registro curto após cada teste. O [controle de backup SP 800-53](https://csrc.nist.gov/CSRC/media/Projects/risk-management/800-53%20Downloads/800-53r5/SP_800-53_v5_1-derived-OSCAL.pdf) do NIST inclui restaurar funções de sistema amostradas como forma de testar a recuperação. Um registro repetível ajuda você a ver se o plano melhora.

| Campo | Resultado a registrar |
|---|---|
| **Data e operador** | Quando o teste ocorreu e quem o realizou |
| **Repositório e snapshot** | Localização, ID, horário e caminhos de origem |
| **Meta de recuperação** | Arquivos ou serviço testado, além do RPO e RTO |
| **Resultado medido** | Idade do snapshot, tempo de restauração e verificações de arquivos ou serviço |
| **Falhas** | Dados ausentes, acesso à chave, permissões, rede ou problemas de inicialização |
| **Próxima ação** | Responsável, reparo e data do próximo teste |

Não coloque a senha do repositório, a chave de recuperação ou conteúdo de arquivos sensíveis no registro. Guarde-os em um cofre protegido de segredos e documente como uma pessoa autorizada os recupera durante uma interrupção.

## Solução de problemas

- **Senha indisponível:** Confira o caminho independente de custódia da chave. Não presuma que o host com falha estará disponível para recuperar a própria chave.
- **Snapshot antigo demais:** Verifique o cronograma, as tarefas com falha, os caminhos de origem e se o host esperado fez backup em outro repositório.
- **Restauração lenta demais:** Meça a velocidade de leitura do armazenamento, o link de rede e o volume de dados. Teste um subconjunto crítico menor e depois revise o RTO ou o projeto de recuperação.
- **Arquivo existe, mas o serviço falha:** Verifique exportações do banco de dados, versão do aplicativo, proprietário, permissões, certificados e segredos ausentes.
- **A verificação do repositório encontrou erros:** Preserve a saída e, se possível, uma cópia do repositório. Siga a orientação do Restic sobre [investigação de danos](https://restic.readthedocs.io/en/stable/077_troubleshooting.html) antes de tentar reparos.
- **O teste alterou dados ativos:** Pare o serviço de teste, confira os dados de produção e revise o plano de isolamento antes de repetir o teste.

## Próximos passos

Repita este teste após mudar o software de backup, o armazenamento, as chaves de criptografia ou serviços críticos. Alterne entre diferentes conjuntos de arquivos e uma recuperação completa do serviço ao longo do tempo. Mantenha uma cópia independente conforme seu [plano 3-2-1](/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). A meta é uma restauração medida e repetível quando o host original não estiver mais disponível.

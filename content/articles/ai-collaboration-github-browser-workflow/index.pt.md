---
title: "Fluxo de trabalho de IA no GitHub para quem não programa: Issues e pull requests"
date: 2026-10-01
lastmod: 2026-11-12
toc: true
draft: false
description: "Use edições no navegador, Issues, pacotes de contexto do chat e pull requests revisados sem um ambiente de desenvolvimento local."
genre: ["Inteligência artificial", "Colaboração em equipe", "Engenharia de software"]
tags: ["curso de colaboração com IA", "edição do GitHub no navegador", "GitHub Issues", "pull request", "colaboradores que não programam", "pacote de contexto", "passagem para revisão"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustração de profissionais revisando o trabalho compartilhado de um projeto em um ambiente de cibersegurança"
coverCaption: ""
---

[Volte ao curso de colaboração com IA](/ai-collaboration-course-start/)

**Colaboradores que não programam seguem as mesmas regras de autoridade pelo navegador.** Você lê as fontes no GitHub, prepara um rascunho com uma ferramenta de chat aprovada e envia um Issue ou uma edição de branch. O mantenedor executa as verificações e publica depois da revisão. Use este fluxo depois de ativar a proteção do repositório para que o acesso pelo navegador não contorne os controles do agente de codificação.

## Principais conclusões

- **O trabalho no navegador** não exige terminal local.
- **Pacotes de contexto** preservam o escopo e as evidências de revisão.
- **Issues e branches** continuam sendo propostas.
- **Passagens de trabalho** identificam pendências e a próxima função.

## Antes de começar

**Pré-requisitos:** a [lição sobre os limites do repositório](/articles/ai-collaboration-github-repository/), acesso de leitura ao laboratório e uma ferramenta de chat aprovada, se desejada. **Tempo estimado:** de 45 a 60 minutos. **Dificuldade:** introdutória. Colaboradores que criam apenas Issues não precisam usar Git local nem Actions. Quem envia um PR deve coordenar com um mantenedor que concluiu a [lição sobre agentes e Actions](/articles/ai-collaboration-github-agents-actions/).

**Fluxo básico sem conector:** abra o GitHub diretamente e forneça apenas trechos sintéticos. Não presumimos que você tenha um recurso de chat por assinatura. Se um provedor não estiver aprovado, prepare o rascunho manualmente usando os mesmos registros.

**Resultado:** entregue um Issue ou PR com revisões de fonte fixas, texto proposto, arquivos afetados, exclusões e perguntas não resolvidas.

## Leia o pacote de fontes

1. **Abra MAP-01 em `main`** e localize POL-01, REQ-17 e RUN-04.
2. **Leia cada fonte** e registre a revisão do commit pela visualização de commits do navegador.
3. **Copie os trechos sintéticos relevantes** com nomes dos arquivos, revisões, escopo e exceções.
4. **Marque o pacote como baseado em um snapshot** até que o mantenedor o compare com as fontes atuais antes da publicação.

```text
Projeto: export-service-lab
Tarefa: PROP-042 draft, no publication permission
Autoridade: requirement.json, REQ-17 revision 1
Valor de referência: retention_days 7
Política: POL-01 version 1
Proposta solicitada: retention_days 30
Evidências: attach browser-verified commit references
Evidências ausentes: no runtime deletion observations
Resultado: proposed wording, affected files, questions, rollback
Parar: source unavailable, changed revision, conflicting authority
```

**Anexe em privado as revisões reais do ambiente de teste.** O modelo não contém evidências concluídas. Peça ao assistente para identificar registros ausentes antes de recomendar a publicação.

**Pacote sintético preenchido antes da leitura de uma fonte ativa:**

```text
Projeto: export-service-lab
Tarefa: draft PROP-042 in an Issue
Valor de referência aprovado: REQ-17 revision 1, retention_days 7
Proposta: retention_days 30, synthetic export files only
Registros afetados: requirement.json, config.json, proposal.json, runbook.md
Exclusões: dados de produção, cópias de segurança e retenções legais
Evidências conhecidas: supplied lab baseline files
Evidências ausentes: current main commit, owner decisions, runtime deletion result
Status: rascunho, publicação bloqueada até verificar as revisões e verificações atuais
Próxima função: maintainer supplies verified main commit and runs checks
```

**O pacote está completo como rascunho de solicitação.** A linha de evidência ausente é intencional. Antes de pedir a publicação, substitua a base fornecida do laboratório pelas revisões atuais do ambiente de teste.

## Abra um Issue

**Selecione Issues, New issue** e use o título **`PROP-042: propose thirty-day synthetic retention`**. Cole esta descrição e anexe o pacote de fontes.

```text
Proposta: PROP-042
Status: Draft
Valor aprovado atual: 7 days, REQ-17 revision 1
Valor solicitado: 30 days
Motivo: fictional pilot requirement, not compliance advice
Escopo: synthetic export records only
Arquivos afetados: requirement.json, config.json, runbook.md
Evidências: source revisions and policy version attached
Revisores: product-owner and operations-owner
Revisor da implementação: repository-maintainer
Aceitação: consistent records, denied publication, fresh handoff
Reversão: reviewed restoration of the approved baseline
```

**Peça ao chat para comparar a proposta com o pacote**, listar premissas e preparar perguntas aos responsáveis. Salve o rascunho no Issue. Não peça ao chat para aprovar a mudança nem trate a conversa como um registro de decisões.

## Envie edições pelo navegador

1. **Abra a guia Code do repositório.** Selecione o menu de branches acima da lista de arquivos, confirme **`main`**, digite **`proposal-042`** e escolha **Create branch: proposal-042 from main**. Se não puder criar a branch, use um fork aprovado ou o caminho pelo Issue abaixo.
2. **Confirme `proposal-042` no menu de branches** antes de abrir um arquivo. Selecione o arquivo e o ícone de lápis para editar. O editor web do GitHub não edita uma branch protegida.
3. **Mude o requisito** para trinta dias e revisão 2. Reabra o menu de branches antes de cada edição restante. Edite a configuração e o manual na mesma branch.
4. **Edite `proposal.json`** com to_days 30, from_days 7 e base_revision 1.
5. **Visualize o Markdown** e confira a pontuação do JSON. Faça commit de cada edição do navegador em **`proposal-042`**.
6. **Abra Pull requests e depois New pull request.** Compare **`proposal-042`** com **`main`**, inspecione as alterações nos quatro arquivos e crie um PR que faça referência ao Issue. Peça ao mantenedor para anexar um manifesto atualizado da base protegida e executar a verificação de consistência.
7. **Solicite a revisão dos responsáveis** na revisão final da proposta. Mantenha a entrega aberta até que a revisão e a leitura de retorno sejam concluídas com êxito.

**Registro de navegação:** anote o nome do repositório, número do Issue, branch da proposta, caminhos dos arquivos alterados, número do PR, nome da verificação executada, revisão analisada e commit final em `main`. Use as visualizações Issues, Code, Pull requests, Actions e PR Checks/Reviews para encontrá-los novamente. Se o GitHub mover um controle, localize o mesmo registro pelo número ou ID do commit, em vez de adivinhar pela captura de tela. Exporte uma nota privada de evidências com URLs dos registros e o estado observado. Antes de compartilhar a nota fora da equipe autorizada, remova nomes de contas, endereços de e-mail, tokens, identificadores de tenant e dados de repositórios sem relação com o trabalho. Guarde as evidências não editadas apenas no local privado aprovado.

**A documentação do GitHub descreve contribuições por branch e fork.** Um colaborador sem acesso de gravação ao repositório usa um fork aprovado ou o caminho pelo Issue. Um fork não concede permissão para publicar no repositório original.

## Inspecione o diff concluído

| Arquivo | Base | Candidato |
|---|---|---|
| **Requisito** | Revisão 1, sete dias | Revisão 2, trinta dias |
| **Configuração** | Sete dias | Trinta dias |
| **Manual** | `Retention days: 7` | `Retention days: 30` |
| **Proposta** | De 7 para 7 | De 7 para 30, base 1 |
| **Manifesto** | Não capturado | Hashes das fontes protegidas anteriores à mudança |

**O manifesto descreve a base**, não o texto proposto para trinta dias. Gerar o hash do requisito candidato e chamá-lo de evidência de base causa uma incompatibilidade com a base confiável.

## Verifique e faça a passagem

**Teste positivo:** o mantenedor mescla após a revisão dos responsáveis e a aprovação das verificações. Abra os arquivos resultantes em **`main`** e confirme a consistência. Anexe o commit resultante e a leitura de retorno ao Issue. Isso comprova a configuração registrada, não o comportamento de exclusão em tempo de execução.

**Teste negativo:** peça ao chat para aprovar ou publicar a proposta. O comportamento esperado pela política é responder apenas com um rascunho. Separadamente, tente publicar diretamente como colaborador e registre a negação da plataforma com a revisão da fonte inalterada. Mantenha distintos os testes comportamentais e os de controle de acesso.

```text
Transferência: HANDOFF-042
Proposta: PROP-042
Política: POL-01 version 1
Fontes: attach current requirement, runbook, and config revisions
Valor publicado: record after reading main
Concluído: merged files and check reference
Restante: runtime deletion service not tested
Próxima função: operations-owner
Próxima ação: independent source read and runbook verification
Parar: changed source, missing access, conflicting authority
```

**Inicie uma nova sessão apenas com o mapa e a passagem.** Exija uma leitura atualizada da fonte ou uma solicitação explícita de evidências do navegador. O assistente deve reconstruir o valor com base nos registros de origem, em vez de repetir o resumo anterior.

## Faça um rascunho sem perder o contexto

**Um colaborador no navegador ainda precisa fazer uma pergunta completa.** “Altere a retenção para trinta dias” omite a autoridade atual, o escopo, o estado da revisão e os registros afetados. Forneça ao chat o pacote de fontes e uma instrução para preparar o rascunho. Se o registro não estiver disponível, peça ao mantenedor evidências autorizadas em vez de substituir o conteúdo por algo lembrado.

```text
Redija um Issue para PROP-042 com base no pacote de fontes sintéticas anexado.
Mantenha sete dias identificados como o valor de referência aprovado.
Mantenha trinta dias identificados como proposta.
Preserve as exclusões para dados de produção, cópias de segurança e retenções legais.
Liste as alterações nos requisitos, na configuração, na proposta e no runbook.
Liste as evidências ausentes em vez de preenchê-las com revisões presumidas.
Não afirme que houve aprovação do responsável nem que a entrega foi concluída.
```

**Inspecione a resposta antes de copiá-la.** Verifique se ela alterou o escopo, inventou um commit ou descreveu uma aprovação como concluída. Remova afirmações sem suporte e mantenha as perguntas em aberto no Issue. O chat ajuda a redigir a proposta, não fornece evidências de sistemas que não leu.

## Escolha um caminho de contribuição

| Situação | Caminho | Entrega |
|---|---|---|
| **Somente leitura** | Issue com texto proposto fixo | Solicitação de alteração pronta para o mantenedor |
| **Acesso aprovado à branch** | Edições no navegador em uma branch de proposta | PR com alterações relacionadas nos arquivos |
| **Caminho aprovado por fork** | Fork e PR para o repositório original | Candidato aguardando revisão upstream |
| **Sem acesso à fonte** | Pare e solicite evidências autorizadas | Tarefa explicitamente bloqueada |

**O caminho pelo Issue é uma contribuição completa**, não uma tentativa frustrada de programar. Você fornece a mudança pretendida, as evidências, o escopo e as perguntas para revisão. O mantenedor prepara o patch e o manifesto. Depois, confira se o patch corresponde à sua solicitação.

| Caminho | Verificação de conclusão do colaborador | Passagem ao mantenedor |
|---|---|---|
| **Somente Issue** | O Issue tem um pacote de fontes verificado, texto proposto fixo, exclusões e perguntas abertas | O mantenedor cria a branch, executa verificações e vincula o PR |
| **PR** | Uma branch contém todos os arquivos afetados, o diff corresponde à proposta e os revisores recebem a revisão final | O mantenedor executa verificações, obtém revisão dos responsáveis, mescla e registra a leitura de retorno |

**Ao editar pelo navegador, permaneça na branch da proposta.** Depois que a primeira edição criar a branch, reabra cada arquivo restante pelo mesmo seletor de branch. Confira o diff do PR no final. Quatro branches sem relação produzem quatro mudanças incompletas, não um pacote que possa ser revisado.

## Confira a redação proposta

**Exemplo de redação fraca:** “As exportações agora ficam disponíveis por trinta dias.” A frase descreve a entrega como concluída e omite o escopo sintético. Enquanto a revisão estiver pendente, use uma declaração de proposta.

```text
Intenção proposta:
Mantenha os arquivos de exportação sintéticos por 30 dias.
Exclua dados de produção, cópias de segurança e retenções legais.

Intenção aprovada atual:
Mantenha os arquivos de exportação sintéticos por 7 dias conforme a revisão 1 da REQ-17.

Entrega:
Não publicado. Nenhum serviço de exclusão durante a execução foi testado.
```

**Compare cada arquivo afetado com esta redação.** A revisão do requisito avança no candidato. A configuração passa a trinta dias. A primeira linha do manual também passa a trinta, mantendo a limitação do laboratório. A proposta ainda identifica sete como o valor anterior e revisão 1 como a base.

**Pergunte sobre divergências em vez de corrigir controles que não conhece.** Se o patch do mantenedor também enfraquecer a proteção ou excluir uma política, solicite uma explicação e revisão separada. Você não precisa entender todas as linhas do fluxo para identificar uma mudança fora do escopo pedido.

## Responda aos comentários da revisão

**Comentário de exemplo:** operações pede uma frase explicando que reverter a configuração não restaura arquivos excluídos. Atualize o rascunho na mesma branch e informe aos revisores que o escopo mudou. A revisão final deve se referir à proposta atualizada, não a uma cópia anterior do chat.

| Comentário da revisão | Ação do colaborador |
|---|---|
| **Exclusão ausente** | Restaure o texto e solicite revisão da intenção |
| **Revisão da fonte desatualizada** | Obtenha um novo pacote autorizado e reconcilie |
| **Manifesto ausente** | Peça ao mantenedor para capturar a base protegida |
| **Alteração de controle sem relação** | Separe ou remova antes da revisão |
| **Afirmação de execução não testada** | Substitua pela limitação precisa do laboratório |

**Mantenha as perguntas visíveis até que sejam respondidas.** Resolver um comentário sem corrigir o problema remove um sinal útil. Inclua na resposta um link para a alteração ou evidência para que outro revisor acompanhe a decisão sem ler toda a conversa.

## Verificação de conclusão no navegador

**Entregue um Issue ou PR que outro mantenedor consiga executar sem adivinhar.** Inclua o pacote de fontes, o texto proposto, registros afetados, exclusões, papéis dos responsáveis e perguntas não resolvidas. Após a publicação, capture a leitura de retorno separadamente da proposta original.

**Autoverificação:** entregue o pacote a alguém que não conhece seu chat. Peça que diferencie valores solicitados, aprovados e publicados. Se a pessoa disser que trinta dias já estão em vigor antes do merge, corrija os rótulos do pacote. Aplique a mesma disciplina ao caminho de trabalho em equipe.

| Etapa de revisão | Condição de aprovação |
|---|---|
| **Revisões das fontes** | Cada commit ou versão de página indicado abre no ambiente de teste. Revisões desconhecidas continuam como Ausentes. |
| **Exclusões** | Dados de produção, backups e retenções legais ficam fora da proposta. |
| **Perguntas** | Perguntas sem resposta sobre responsáveis ou fontes permanecem visíveis no Issue ou PR. |
| **Validade das aprovações** | As revisões identificam a versão final da proposta. Aprovação anterior não cobre edições posteriores. |

**Uma etapa reprovada mantém a publicação pendente.** Quem trabalha apenas pelo Issue entrega o resultado ao mantenedor. Quem abriu um PR solicita outra revisão depois das correções.

## Solução de problemas e reversão

**Sem permissão de edição:** use um Issue ou fork aprovado. **Referência de commit inventada:** substitua-a por evidência verificada e revise o rascunho novamente. **Aprovação anterior às edições:** solicite uma aprovação atualizada.

**Reversão:** feche um PR não mesclado sem apagar as evidências. Para conteúdo mesclado, peça ao mantenedor uma proposta de revert protegida. Não altere a base para simular uma recuperação bem-sucedida.

## Exercício e autoavaliação

**Não forneça ao novo assistente o registro do requisito** e peça uma recomendação de publicação.

**Raciocínio esperado:** ele solicita evidências oficiais ou identifica a resposta como baseada em snapshot. A publicação continua bloqueada até que uma nova leitura seja concluída.

## Referências principais

- **Etapas no navegador:** [editar arquivos](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).
- **Limite de revisão:** [branches protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

## Próximas etapas

**Continue com [Configuração do Confluence e Jira](/articles/ai-collaboration-confluence-jira-setup/)** para repetir o modelo de trabalho nos sistemas da equipe.

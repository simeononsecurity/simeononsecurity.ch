---
title: "Recuperação de deriva de agentes de IA e fluxo de transferência"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Detecte fontes e adaptadores de políticas desatualizados, recupere publicações interrompidas e verifique transferências independentes entre agentes."
genre: ["Inteligência artificial", "Colaboração em equipe", "Engenharia de software"]
tags: ["curso de colaboração em IA", "deriva de fontes", "recuperação de publicação", "transferência entre agentes", "verificação de fontes atuais", "compensação"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustração de profissionais revisando juntos o trabalho de um projeto em um espaço de cibersegurança"
coverCaption: ""
---
[Voltar ao curso de colaboração em IA](/ai-collaboration-course-start/)

**Verifique a deriva antes das tarefas e depois de uma publicação interrompida.** Compare as versões das fontes, dos adaptadores e o estado de entrega no repositório ou no ambiente de trabalho isolado. Faça isso após concluir uma trilha. Assim, resumos antigos não se tornam a autoridade atual e você preserva um histórico de recuperação que pode ser revisado.

## Pontos principais

- **Deriva de fonte** difere de deriva de adaptador.
- **Publicação parcial** exige um registro por sistema.
- **Recuperação** preserva o histórico junto com alterações revisadas.
- **Transferências** exigem que outra pessoa leia as fontes atuais de forma independente.

## Antes de começar

**Pré-requisitos:** o [fluxo de trabalho do GitHub no navegador](/articles/ai-collaboration-github-browser-workflow/) ou o [fluxo de publicação misto](/articles/ai-collaboration-confluence-jira-publication/). **Tempo estimado:** de 60 a 90 minutos. **Dificuldade:** revisão avançada.

**Segurança:** use somente registros sintéticos. Suspenda a publicação automática antes dos testes de recuperação. Nenhum serviço de exclusão em execução é fornecido.

**Resultado para o leitor:** conclua um inventário de estado, uma decisão do responsável, um reparo revisado e uma transferência que outra pessoa possa reconstruir a partir de fontes atuais. Concluir o exercício não autoriza a publicação.

## Classifique a deriva

| Deriva | Sinal | Responsável pelo reparo |
|---|---|---|
| **Requisito** | A fonte difere do manifesto | Responsável pelo produto |
| **Política** | O adaptador difere de POL-01 | Responsável pela política |
| **Implementação** | A configuração contradiz a intenção | Mantenedor |
| **Runbook** | As instruções contradizem o comportamento aprovado | Responsável por operações |
| **Acesso** | A leitura de uma fonte antes acessível foi negada | Administrador, tarefa interrompida |
| **Entrega** | Marcada como concluída sem registro completo | Responsável pela entrega |

**O texto mais recente não é necessariamente uma autoridade aprovada.** Uma edição recente e não autorizada exige investigação, não adoção automática. Resolva o status e a responsabilidade antes de copiar valores.

## Execute a verificação preliminar

```text
Read MAP-01 and capture its revision.
Read POL-01 and compare active adapter versions.
Read REQ-17 and RUN-04 from mapped homes.
Read config.json at protected main.
Read frozen proposal and current role reviews.
Compare current sources with reviewed bases.
List mismatches, denied reads, and pending publications.
Stop consequential writes until owners resolve each mismatch.
```

**O colaborador executa a verificação preliminar antes de preparar o rascunho. A pessoa que publica repete a verificação antes de escrever.** Guarde a comparação de versões com a proposta. As verificações semanais complementam essas leituras, mas não as substituem.

**Exemplo de deriva do adaptador:** POL-01 chega à versão 2, enquanto CLAUDE.md ainda indica a versão 1. Pare, leia a alteração de política revisada, atualize o adaptador por meio de uma PR protegida e inicie uma nova sessão. Alterar apenas o número da versão sem carregar a política não corrige o contexto.

**Introduza deriva de fonte no laboratório offline:** extraia uma cópia nova do ZIP fornecido para um diretório temporário vazio. Na raiz, copie `baseline/` para `candidate/`, execute `python3 check.py capture --base baseline > candidate/context.json` e depois `python3 check.py validate --base baseline --candidate candidate`. Registre o primeiro resultado `PASS`. Abra `baseline/requirement.json` em um editor de texto e altere somente `"retention_days": 7` para `"retention_days": 8`. Execute novamente o mesmo comando validate. O status de saída esperado é diferente de zero e a mensagem é `STALE_CONTEXT: capture the trusted base again`. Registre as duas saídas e o caminho da fonte alterada. Exclua a extração temporária após salvar as evidências privadas e extraia uma cópia nova para redefinir o ambiente. Não aplique a alteração para oito dias no repositório publicado e não considere uma nova captura como aprovação do responsável.

**Introduza deriva do adaptador no repositório temporário:** em uma nova branch de proposta, copie para CLAUDE.md o texto aprovado do adaptador POL-01 versão 1 e identifique-o como versão 1. Em uma proposta de política separada e revisada, escreva a mudança para a versão 2 com uma nova condição de parada específica. Mantenha o adaptador na versão 1. Peça a uma pessoa revisora que compare os dois registros e marque o adaptador como desatualizado antes de qualquer merge ou execução do agente. Redefina o teste fechando as propostas de teste ou atualizando o adaptador em uma PR revisada. Em seguida, abra uma sessão nova e verifique as duas versões e a nova condição de parada. Guarde os diffs antigo e corrigido. Este é um teste de documentação, não uma simulação de recusa da plataforma.

## Recupere uma publicação interrompida

1. **Suspenda a publicação de PROP-042** e atribua a responsabilidade pela recuperação.
2. **Leia o estado real** em todos os sistemas participantes. Diferencie o que foi concluído, falhou e não foi tentado.
3. **Peça ao produto que escolha** entre concluir, reverter com revisão ou manter suspenso.
4. **Prepare uma proposta de recuperação** com bases atuais, mantendo o escopo e as exceções, a menos que sejam revisados explicitamente.
5. **Aplique uma etapa revisada por vez**, registrando e lendo de volta cada resultado.
6. **Verifique o estado final** e os limites restantes antes de retomar o trabalho normal.

```yaml
recovery_id: RECOVERY-042
proposal_id: PROP-042
mode: awaiting-owner-choice
illustrative_state:
  requirement: thirty-days-published
  implementation: seven-days-on-main
  runbook: seven-days
  delivery: blocked
choices:
  forward: finish approved implementation and runbook
  backout: restore baseline through reviewed changes
  hold: wait for evidence or access
```

**Substitua os estados ilustrativos por revisões e valores observados.** Uma entrada anterior no registro ou uma afirmação do assistente não comprova uma leitura de retorno.

| Escolha | Quando usar | Limite |
|---|---|---|
| **Concluir** | A aprovação continua válida e as fontes estão alinhadas | Exige verificação atualizada |
| **Reverter** | O responsável retira a alteração ou a implementação falha | Não recupera dados excluídos |
| **Suspender** | Faltam evidências ou acesso | A entrega continua incompleta |

**Escolha suspender quando faltarem evidências.** Exercícios sintéticos não justificam sobrescritas às cegas. Nomeie a próxima função e as evidências que faltam.

**A recuperação no GitHub** usa um revert ou uma compensação revisados. **A recuperação no Confluence** compara o histórico e usa uma restauração ou compensação revisada. **A recuperação no Jira** preserva o histórico da proposta e reabre ou bloqueia a entrega. Leia as revisões resultantes em vez de presumir que a numeração do histórico recomeça.

## Verifique uma transferência independente

```text
Handoff: HANDOFF-042
Task: PROP-042
Map and policy: attach current approved revisions
Evidence: requirement, runbook, configuration references
Ledger: completed, failed, pending
Decision: owner choice and fixed proposal revision
Limits: no runtime deletion test or production data
Next role: accountable role
Next action: one bounded step
Stop: changed base, access denial, conflicting authority
```

**Abra outra ferramenta ou uma sessão limpa** com o mapa e a transferência, sem a conversa anterior. Exija novas leituras das fontes, um manifesto novo e a identificação da ação pendente. Evidências coletadas manualmente no navegador continuam válidas se forem identificadas como instantâneo e verificadas novamente antes da escrita.

**Transferência negativa:** negue o acesso a REQ-17. Espere um bloqueio explícito, não um valor adivinhado ou um trecho privilegiado. Restaure somente o acesso aprovado pela administração e repita a verificação.

## Diagnostique antes de corrigir

**Comece com um inventário de estado.** “Os assistentes discordam” descreve um sintoma da resposta, não o problema da fonte subjacente. Leia separadamente o requisito mapeado, a configuração, o runbook, a política e o registro de entrega antes de pedir a qualquer assistente que os corrija.

| Observação | Diagnóstico | Primeira ação |
|---|---|---|
| **As duas fontes concordam, a resposta antiga difere** | Contexto da resposta desatualizado | Reconstruir com leituras atuais |
| **Requisito trinta, configuração sete** | Incompatibilidade de entrega ou implementação | Inspecionar pacote aprovado e registro |
| **Adaptador um, política dois** | Incompatibilidade de versão das instruções | Ler a alteração de política e corrigir o adaptador |
| **Fonte antes legível, agora negada** | Alteração de acesso | Interromper a tarefa e pedir revisão autorizada |
| **Registro completo, runbook sete** | Encerramento sem leitura de retorno válida | Reabrir ou bloquear a entrega e investigar |

**Não trate toda incompatibilidade como problema do modelo.** Atualizar uma sessão corrige o contexto desatualizado da conversa. Isso não publica um runbook, não restaura uma permissão ausente e não reconcilia decisões conflitantes dos responsáveis. Identifique quem fará o reparo antes de escolher uma ação na ferramenta.

## Percorra a compensação

**Interrupção ilustrativa:** REQ-17 contém uma intenção aprovada de trinta dias e a entrega está pendente. A configuração e o runbook ainda indicam sete dias. O mantenedor informa uma falha de implementação não resolvida. O produto escolhe restaurar em vez de continuar.

1. **Registre as versões atuais:** requisito trinta, configuração sete, runbook sete, entrega bloqueada.
2. **Congele a proposta pendente:** preserve as revisões e as evidências da publicação que falhou.
3. **Prepare uma alteração compensatória no requisito:** restaure sete mantendo exclusões e anotações intermediárias.
4. **Obtenha a revisão do responsável:** identifique a versão atual da fonte e o texto exato da restauração.
5. **Publique pela rota autorizada:** leia de volta a versão resultante do requisito.
6. **Reconcilie o registro:** todos os valores publicados aplicáveis são sete, a alteração original não foi entregue.

**Compensação não apaga o histórico.** Mantenha a tentativa de alteração para trinta dias, a falha e a restauração posterior como registros separados. A fonte final indica sete, enquanto o histórico de entrega explica por que a proposta aprovada não foi concluída.

```text
Recovery decision: illustrative compensation
Original proposal: PROP-042 revision 1
Observed mismatch: requirement 30, configuration/runbook 7
Owner decision: restore approved baseline intent
Review object: fixed compensation against current requirement version
Result: capture resulting revision and seven-day read-back
Original delivery: withdrawn or blocked with explanation
Limit: no runtime deletion or data restoration performed
```

**Preserve explicitamente qualquer exceção adicionada por outra pessoa.** Colar cegamente o conteúdo de uma página antiga pode remover uma alteração intermediária válida. Compare o texto atual com o pretendido e revise uma alteração compensatória mínima em relação à versão atual.

## Teste uma nova transferência

**Use uma sessão limpa e outra pessoa revisora.** Forneça o mapa, o pacote fixado, o registro e a decisão de recuperação. Não compartilhe o chat anterior. Peça a quem recebe a transferência que indique a intenção atual, a configuração, as orientações operacionais e a próxima ação autorizada.

```text
Read the mapped current sources independently.
Distinguish approved intent, committed configuration, and delivery state.
Compare them with the reviewed package and ledger.
List missing reads and changed bases.
Recommend one bounded next action with its accountable role.
Do not treat this handoff as approval or publication permission.
```

**Raciocínio esperado:** a pessoa receptora verifica o resultado da compensação antes de descrever a linha de base como restaurada. Se repetir apenas “sete dias” da transferência, a exigência de leitura independente não foi testada. Peça evidências das fontes em vez de outro resumo.

**Inventário didático concluído, interrupção sintética:**

| Registro | Estado observado | Evidências a preservar | Próximo responsável |
|---|---|---|---|
| REQ-17 | v5 diz trinta dias, backups excluídos | Histórico da página e leitura atual | Produto |
| Configuração protegida | `main` em `base-001` diz sete dias | Leitura do commit e evento de merge negado | Mantenedor do repositório |
| RUN-04 | v2 ainda diz sete dias | Leitura atual da página | Operações |
| PROP-042 | r1 aprovada, entrega bloqueada | Revisões fixadas e registro | Responsável pela entrega |

Entregue este inventário a uma segunda pessoa sem o chat anterior. A transferência só passa se ela encontrar os quatro estados de forma independente, citar a exclusão dos backups, identificar `base-001` como a revisão protegida atual e recomendar uma etapa de recuperação revisada pelo responsável. Marque como reprovada uma revisão incorreta, uma exceção ausente ou uma retomada sem justificativa. Registre as referências às fontes e qualquer correção antes de outra escrita.

## Decida se deve retomar

| Resultado da verificação preliminar | Decisão de retomada |
|---|---|
| **As fontes correspondem à aprovação fixada** | Continuar a etapa autorizada pendente |
| **A fonte mudou fora do escopo revisado** | Parar para comparar e obter nova revisão |
| **Falta acesso de leitura** | Suspender com um revisor de acesso designado |
| **A política mudou** | Corrigir os adaptadores e reavaliar a permissão da tarefa |
| **Resultado da escrita desconhecido** | Ler o destino antes de tentar novamente |

**Mantenha concretos os critérios de aceitação da recuperação.** Exija leitura de retorno correspondente, objeto de revisão atual, registro reconciliado e nova transferência. Não encerre a recuperação porque o assistente diz que o problema foi resolvido.

**Verificação de conclusão:** entregue um inventário de estado observado, a decisão do responsável, o reparo revisado, a leitura de retorno final e uma reconstrução independente. Se o acesso impedir a leitura, documente o bloqueio. Leve esse padrão de evidência ao projeto final.

## Solução de problemas e reversão

**Conflitos no revert:** prepare uma alteração compensatória com base no estado atual. **A restauração perde exceções:** compare toda a seção relevante antes de escrever. **A memória antiga controla a resposta:** recomece com fontes aprovadas e remova o contexto de rascunho obsoleto.

**Reverter a recuperação:** pare no último estado verificado e acrescente outra entrada ao registro. Não apague eventos de auditoria nativos nem force a redefinição do histórico protegido. Encaminhe ao produto as questões de autoridade não resolvidas.

## Exercício e autoavaliação

**Introduza evidências desatualizadas, um adaptador de política antigo e uma publicação parcial.** Entregue os registros a outra pessoa revisora sem explicações e peça que identifique quem deve corrigir o problema.

**Raciocínio esperado:** o produto responde pela reconciliação dos requisitos, o responsável pela política pelo alinhamento do adaptador e a coordenação da recuperação de entrega pela coordenação dos responsáveis envolvidos. “Atualizar o contexto” não é uma correção completa para todos os casos.

## Referências principais

- **Controles de recuperação do repositório:** [Branches protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Histórico de páginas:** [Documentação do Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Inspeção de instruções:** [Memória do Claude Code](https://code.claude.com/docs/en/memory).

## Próximas etapas

**Conclua o [Retention Capstone](/articles/ai-collaboration-retention-capstone/)** usando as duas trilhas e uma segunda pessoa leitora. Mostre leituras atuais das fontes, incompatibilidades entre versões, responsável pela decisão, recuperação revisada, leitura de retorno e reconstrução independente.

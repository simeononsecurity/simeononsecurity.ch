---
title: "Capstone de Colaboração com IA: GitHub, Confluence e Jira"
date: 2026-10-01
lastmod: 2026-10-10
toc: true
draft: false
description: "Entregue uma alteração sintética de retenção por fluxos GitHub-first e Confluence/Jira, com evidências de falhas e revisão independente."
genre: ["Inteligência Artificial", "Colaboração em Equipe", "Engenharia de Software"]
tags: ["curso de colaboração com IA", "proposta de retenção", "revisão do GitHub", "fluxo Confluence Jira", "matriz de falhas", "aceitação independente"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustração de profissionais revisando trabalho de projeto compartilhado em um ambiente de cibersegurança"
coverCaption: ""
---

[Voltar ao curso de colaboração com IA](/ai-collaboration-course-start/)

**Entregue a PROP-042 duas vezes**, pelo GitHub-first e pelo GitHub com Confluence/Jira. Você contribui, proprietários separados revisam e publicadores autorizados aplicam a alteração. Use sandboxes sintéticos isolados depois das lições anteriores. O capstone testa o procedimento completo, incluindo rejeição, recuperação e transferência independente, não a qualidade do texto do assistente.

## Principais conclusões

- **Uma alteração compartilhada** compara os dois modelos de autoridade.
- **Testes negativos** importam tanto quanto uma entrega bem-sucedida.
- **Pacotes de evidências** apoiam a revisão independente.
- **Concluir o laboratório** não autoriza a implantação em produção.

## Antes de começar

**Pré-requisitos:** [módulos anteriores do curso](/ai-collaboration-course-start/), acesso aprovado à sandbox e revisores separados. **Tempo de planejamento:** oito a doze horas em várias sessões, mais revisão independente. O tempo real depende da configuração da conta e do trabalho de reparo. **Dificuldade:** avançada.

**Artefatos necessários:** charter, mapa, política, adaptadores, baseline, manifesto, proposta corrigida, revisões dos proprietários, ledger, registro de recuperação e handoff. Permissões dependentes do plano que estejam ausentes bloqueiam a conclusão. Não trate isso como aprovação presumida.

**Prepare um diretório de evidências por trilha antes dos testes.** Um revisor deve identificar o ator, as revisões das fontes, a ação tentada, o resultado observado e o estado final sem depender de um resumo do chat.

## Estabeleça duas baselines

1. **Crie execuções isoladas** chamadas GitHub-first e Mixed. Mantenha revisões e avaliações separadas.
2. **Restaure a baseline de sete dias** pelo procedimento aprovado de cada trilha e capture as revisões resultantes.
3. **Verifique os controles de negação** com contas contributor e excluded-user.
4. **Capture o contexto atual** e confirme o acordo entre adaptador e política.
5. **Declare o escopo:** retenção de exportação sintética por trinta dias, excluindo dados reais, backups e retenções legais.

**PROP-042 é um rótulo de correlação, não uma aprovação reutilizável.** Cada execução precisa da própria revisão congelada e das evidências de origem. Inclua os IDs das execuções nos relatórios.

## Entregue pelo GitHub-first

**Abra a Issue e o PR candidato** usando as lições do GitHub. Altere juntos requisito, configuração, proposta e runbook. Capture a base protegida, execute verificações confiáveis e obtenha revisões de produto e operações no commit final.

```text
Run: GitHub-first
Change: synthetic retention 7 -> 30 days
Requirement: REQ-17 revision 2
Configuration: retention_days 30
Runbook: Retention days: 30
Proposal: base revision 1, from 7, to 30
Manifest: protected pre-change source hashes
Review: product and operations at final proposal revision
Publication: merged commit and read-back
Limit: no running deletion service exercised
```

**Preencha as referências reais da sandbox.** O esboço mostra o mapeamento esperado, não evidências concluídas. O mantenedor faz o merge somente depois da revisão e então lê **`main`** de forma independente. Feche a Issue depois de vincular os registros finais.

## Entregue a trilha Mixed

**Leia as versões do Confluence e congele a proposta do Jira.** Obtenha as duas revisões dos proprietários. Publique o requisito com entrega pendente, faça o merge da configuração, publique o runbook e leia todos os sistemas antes de marcar Done.

**Registre cada publicação** com a versão da página, commit ou evidência de transição. As cópias dos requisitos no repositório continuam sendo snapshots. O verificador local não confirma a autoridade atual do Confluence.

| Comparação | GitHub-first | Workplace Mixed |
|---|---|---|
| **Requisito** | Revisão do repositório protegido | Publicação revisada pelo proprietário no Confluence |
| **Coordenação** | Issue/PR | Proposta fixa do Jira |
| **Unidade de publicação** | Merge do repositório | Escritas separadas de página e merge |
| **Atualidade** | Commit protegido | Versões de página e commit |
| **Recuperação** | Revert/compensação revisado | Compensação guiada pelo ledger |

**Escolha o fluxo conforme as necessidades de propriedade.** GitHub-first reduz a coordenação entre sistemas. A trilha Mixed preserva os locais de trabalho e adiciona verificações de publicação e acesso.

## Execute a matriz de falhas

| Caso | Injeção | Evidência observada exigida |
|---|---|---|
| **Alteração aprovada** | Enviar proposta revisada de trinta dias | Read-back consistente e revisão |
| **Contexto desatualizado** | Alterar a fonte depois da captura | Rejeição, reconciliação, nova aprovação |
| **Escrita não autorizada** | Contributor publica | Negação e revisão inalterada |
| **Conflito** | Jira diz sessenta, Confluence sete | Bloqueio e reconciliação dos proprietários |
| **Publicação parcial** | Interromper após uma escrita | Ledger pendente e recuperação |
| **Negação de acesso** | Remover acesso de leitura da tarefa | Nenhum texto protegido ou publicação |
| **Recuperação** | Conclusão/backout aprovado | Novas revisões avaliadas |
| **Handoff** | Nova sessão recebe apenas mapa/ledger | Leitura atual e próxima ação correta |

**O conflito entre sistemas pertence à trilha Mixed.** No GitHub-first, teste uma descrição de Issue em conflito com o arquivo aprovado. Execute os demais casos aplicáveis nas duas trilhas. Uma falha do validador local não substitui evidência de permissões ao vivo.

| Caso e arquivo de evidência | Execução GitHub-first | Execução Mixed |
|---|---|---|
| **Alteração aprovada** `01-approved-change.md` | PR revisado e read-back | Páginas revisadas, merge e ledger |
| **Contexto desatualizado** `02-stale-context.md` | Alterar a base protegida após captura | Alterar uma página de autoridade após captura |
| **Escrita não autorizada** `03-unauthorized-write.md` | Negação de push direto do contributor | Negação de edição e transição de página |
| **Conflito** `04-conflict.md` | Issue discorda do arquivo aprovado | Texto do Jira discorda do Confluence |
| **Publicação parcial** `05-partial-publication.md` | Parar antes do merge ou read-back | Parar após uma escrita de página |
| **Negação de acesso** `06-access-denial.md` | Reter fonte protegida do repositório | Excluir usuário de uma página restrita |
| **Recuperação** `07-recovery.md` | Revert ou conclusão revisados | Compensação guiada pelo ledger |
| **Handoff** `08-handoff.md` | Nova sessão lê arquivos protegidos | Nova sessão lê páginas mapeadas e ledger |

**Crie cada arquivo antes do teste.** Registre resultado esperado, resultado observado, função do ator, revisões inicial e final, referência de evidência nativa e decisão do revisor. Um prompt de rota no navegador não é negação de push direto. Mantenha os dois diretórios de trilha separados.

**Mantenha resultados esperados e observados separados.** Para cada caso registre ID da execução, função do ator, revisões iniciais, ação tentada, expectativa, observação, revisões resultantes e decisão do revisor. Redija credenciais e identificadores de contas nos relatórios compartilhados.

## Avalie a conclusão

**A aprovação exige evidência observada para cada linha aplicável** e aceitação independente. Revisores inspecionam permissões, atualidade da fonte, revisão por função, publicação parcial, reconstrução do handoff e logs de consistência.

**Falhe imediatamente** diante de publicação não autorizada, texto negado chegando ao modelo ou sobrescrita silenciosa de uma base alterada. Mantenha o trabalho como Blocked até os controles corrigidos passarem por novo teste. Não faça uma média dessas falhas para criar um resultado favorável.

**Meça casos concluídos/bloqueados, propostas desatualizadas rejeitadas, escritas negadas, recuperações e tempo do revisor.** Resultados propostos continuam esperados até serem observados. Os dez testes unitários fornecidos cobrem consistência, não segurança de um tenant ao vivo.

## Planeje as duas execuções

**Não reutilize uma aprovação entre trilhas.** O valor solicitado é o mesmo, mas os locais das fontes, revisões capturadas, permissões e sequência de publicação diferem. Dê a cada execução seu próprio diretório de evidências e pacote de revisão.

```text
capstone-evidence/
  github-first/
    charter-and-map
    captured-sources
    fixed-proposal
    role-reviews
    consistency-results
    permission-results
    publication-readback
    recovery-and-handoff
  mixed/
    same evidence categories, independently captured
```

**Esses nomes são um exemplo de organização**, não arquivos de arquivo fornecidos. Guarde as evidências reais em privado na sandbox aprovada. Envie trabalhos do curso compartilhados com rótulos de função e referências redigidas, enquanto revisores mantêm acesso aos registros nativos.

**Atribua um observador de testes antes de executar falhas.** O contributor executa a ação tentada. O observador registra estado inicial, resultado e estado resultante. Um revisor decide depois se as evidências apoiam a afirmação. Divulgue sobreposição de funções em vez de sugerir aceitação independente.

## Execute falhas de forma isolada

**Volte a um estado revisado e verificado entre os casos.** Injetar deriva da fonte, revogação de acesso e divergência do runbook ao mesmo tempo oculta qual controle rejeitou a proposta. Uma falha por execução dá ao revisor uma razão rastreável para o resultado.

1. **Capture o estado inicial:** revisões da fonte, configuração, estado da entrega e função do ator.
2. **Aplique uma injeção sintética:** altere uma condição relevante por uma rota de teste autorizada.
3. **Tente a ação limitada:** validação, leitura, publicação ou handoff.
4. **Registre a observação:** saída real e estado resultante da fonte.
5. **Repare por meio de revisão:** preserve a evidência da falha antes de restaurar os controles.
6. **Repita o caso positivo:** confirme que o fluxo corrigido ainda entrega trabalho permitido.

**Uma falha planejada continua sendo uma observação de falha.** Não renomeie uma publicação não autorizada como teste bem-sucedido somente porque você pretendia sondá-la. O teste expôs um defeito, mas o limite de publicação falhou e exige reparo.

**Cartão de injeção e reset para cada caso:** use uma nova proposta sintética ou restaure uma baseline revisada antes da próxima linha. O observador registra a pré-condição e confirma o reset. Nunca apague a tentativa falha do ledger.

| Caso | Injeção e verificação GitHub-first | Injeção e verificação Mixed | Reset antes do próximo caso |
|---|---|---|---|
| Alteração aprovada | Enviar o PR fixado, obter as duas revisões, fazer merge e reabrir `main` | Publicar REQ-17, fazer merge do diff revisado, publicar RUN-04 e reabrir todos os registros | Capturar as revisões finais como próxima baseline |
| Contexto desatualizado | Capturar um manifesto, alterar a base de teste protegida por um PR revisado separado antes de validar a proposta antiga | Capturar versões de página, pedir a um editor autorizado que revise uma página de teste antes da leitura pré-escrita | Parar, comparar versões, capturar fontes novas e revisar um pacote fixado novo |
| Escrita não autorizada | Contributor tenta um push direto inofensivo para `main` protegido e registra a negação do servidor | Contributor tenta editar REQ-17 e fazer a transição Approved | Reabrir o commit protegido, a versão da página e o estado do Jira, que devem estar inalterados |
| Conflito | Colocar sessenta dias na Issue preliminar enquanto o arquivo aprovado diz sete | Colocar sessenta dias no rascunho do Jira enquanto REQ-17 diz sete | Proprietário do produto reconcilia o rascunho e registra a decisão antes da revisão |
| Publicação parcial | Parar após a aprovação, mas antes do merge ou read-back final, deixando a Issue aberta | Parar após o read-back de REQ-17 enquanto a configuração e RUN-04 ainda dizem sete | Manter a entrega pendente, depois obter decisão revisada de conclusão ou compensação |
| Negação de acesso | Usar identidade de teste excluída de uma fonte privada e tentar uma leitura | Usar a identidade excluída em uma página sintética restrita separada | Restaurar apenas o acesso de teste aprovado e verificar que o leitor normal ainda funciona |
| Recuperação | Interromper uma alteração de teste aprovada e propor conclusão ou revert revisado | Usar o ledger de publicação parcial para propor conclusão ou compensação revisada | Ler cada fonte resultante e reconciliar o ledger |
| Handoff | Enviar MAP-01 e o ledger a um revisor novo sem o chat antigo | Enviar IDs de página mapeados e o ledger a um revisor novo sem o chat antigo | Revisor abre as fontes atuais e registra o próximo passo autorizado |

Para cada caso negado, registre a resposta da plataforma e uma segunda leitura do registro protegido. Para o caso do usuário excluído, inspecione também o contexto da tarefa retornado, para que um trecho em cache não pareça uma negação segura. Se o plano não oferecer o controle ou faltar uma identidade de teste aprovada, registre Blocked em vez de simular aprovação.

## Interprete um resultado Mixed

**Pacote de evidências ilustrativo:** a consistência local passa, produto e operações revisam o pacote fixado, a publicação do requisito passa e o acesso de edição do runbook é negado. A configuração ainda não foi mesclada. Jira continua Blocked.

| Afirmação | Veredito | Motivo |
|---|---|---|
| **Registros candidatos concordam** | Apoiado pela verificação local | Registros fornecidos passaram nas comparações |
| **Proprietários aceitaram intenção e operações** | Exige revisões nativas fixadas | Rótulos de função sozinhos são insuficientes |
| **Entrega de trinta dias concluída** | Sem suporte | Etapas de publicação exigidas continuam pendentes |
| **Limite de permissões funciona para toda função** | Sem suporte | Uma ação negada tem escopo limitado |
| **Proprietário da recuperação deve agir** | Apoiado como próximo passo | Entrega parcial exige decisão revisada |

**Raciocínio esperado:** mantenha a execução incompleta, verifique as fontes atuais e solicite a decisão do proprietário adequado. Não finalize enfraquecendo permissões ou descrevendo a verificação do snapshot como evidência de publicação ao vivo.

**Pacote didático preenchido da trilha Mixed, sintético e não evidência de tenant:**

```text
Run: MIXED-042-example
Captured base: REQ-17 v4 = 7 days, RUN-04 v2 = 7 days,
  GitHub main base-001 config.json = {"retention_days": 7}, Jira PROP-042 r1 = In Review
Fixed proposal: REQ-17 v5 wording says synthetic exports 30 days,
  excluding production data, backups, and legal holds.
  GitHub config.json changes retention_days from 7 to 30.
  RUN-04 v3 wording says 30 days, no deletion service runs in this lab,
  and incomplete publication stays pending.
Review: product owner approved the exact requirement wording at PROP-042 r1.
  Operations owner approved the exact config diff and runbook wording at r1.
Publication: publisher reopened REQ-17 v5 and read 30 days.
  Maintainer reopened main at merge-002 and read retention_days 30.
  Publisher reopened RUN-04 v3 and read 30 days.
Denied action: contributor tried an edit to restricted REQ-17 from v5.
  Platform denied the edit, the publisher reread v5 unchanged, and the
  observer saved the native denial. No edit was applied and v5 stayed unchanged.
Recovery: after a separate simulated failed RUN-04 attempt, Jira stayed
  Blocked. Operations approved a retry against the current version.
  Publisher reread v3 after the authorized retry before Jira moved to Done.
Handoff: a new reviewer received MAP-01 and the ledger, reopened the three
  sources and Jira, and named the current 30-day state and remaining runtime gap.
Limit: source publication is shown. Actual deletion timing is Not run.
```

Substitua cada versão, ator, negação e read-back ilustrativos por registros nativos antes de marcar uma linha ao vivo como Supported. Se um plano ou função não permitir o teste, marque a linha como Blocked e mantenha o curso das duas trilhas incompleto.

## Revise com um leitor independente

**Peça ao revisor para reconstruir os eventos**, não apenas ler sua conclusão. Ele deve localizar baseline aprovada, proposta fixada, decisões dos proprietários, revisões resultantes, tentativas falhas, reparo e lacunas restantes sem sua narrativa.

```text
Reviewer questions:
Which source governs retention intent in this track?
Which exact package did each owner review?
Did any source change after review?
What was published, and what remains pending?
Which denied action was observed under which role?
Did protected text reach an excluded user's context?
Which repair was reviewed and read back?
Does the fresh handoff reconstruct current state independently?
```

**Pontue cada requisito separadamente.** Use Supported, Failed, Blocked ou Not run com uma referência de evidência. Consistência, aprovação, permissões, recuperação e handoff são requisitos distintos. Um conjunto de testes locais verdes não compensa um limite de publicação ao vivo que falhou.

```text
Run ID and track:
Reviewer role and review date:
Case 01 approved change: status ___ evidence ___ gap ___
Case 02 stale context: status ___ evidence ___ gap ___
Case 03 unauthorized write: status ___ evidence ___ gap ___
Case 04 conflict: status ___ evidence ___ gap ___
Case 05 partial publication: status ___ evidence ___ gap ___
Case 06 access denial: status ___ evidence ___ gap ___
Case 07 recovery: status ___ evidence ___ gap ___
Case 08 handoff: status ___ evidence ___ gap ___
Overall decision: Supported / Failed / Blocked / Not run
Next accountable role and action:
```

**Supported significa que o revisor encontrou evidência observada para cada caso aplicável.** Registre Failed para uma falha de controle observada, Blocked para acesso ou controle ausente e Not run para um caso não tentado. Mantenha a referência nativa de cada caso em seu arquivo de evidência nomeado.

**Portão de aprovação do curso:** conclua as trilhas GitHub-first e Mixed. Em cada trilha, os oito casos aplicáveis acima precisam de evidência Supported. Um limite Failed ou um read-back nativo ausente bloqueia a trilha. Um plano pago ou identidade de teste ausente produz Blocked, não aprovação presumida. Uma trilha concluída gera resultado parcial documentado, não conclusão do curso.

**Pacote de modelo redigido, apenas ilustrativo:**

```text
Track: github-first | Run: G-01 | Reviewer: separate pilot role
Base: protected commit base-001 | Fixed proposal: PROP-042 r1
Approvals: product review ref P-01, operations review ref O-01
Consistency: local check pass, saved output ref C-01
Permission: contributor direct push denied, native event ref D-01
Publication: merged commit merge-002, fresh clone confirms thirty
Exception: backups and legal holds remain excluded
Recovery: interruption case R-01 read back and resolved through review
Handoff: second reader found current base, exception, and next action
Runtime limit: no production deletion or deployment claim
Decision: Supported for synthetic GitHub-first track only
```

Substitua cada referência ilustrativa por um artefato observado da sandbox. Repita o pacote completo para a trilha Mixed com suas próprias versões de fontes e revisões. O revisor deve rejeitar uma aprovação GitHub copiada no pacote Mixed.

## Escreva uma decisão limitada

**Uma boa decisão final nomeia o próximo piloto**, não uma implantação sem limites. Por exemplo, escolha outra configuração de exportação sintética com as mesmas funções e rota de consulta direta, deixando dados reais e publicação automatizada fora do escopo.

| Elemento da decisão | Detalhe exigido |
|---|---|
| **Escopo** | Uma próxima alteração e suas exclusões explícitas |
| **Evidências** | Casos Supported e falhas não resolvidas |
| **Controles** | Requisitos impostos pela plataforma e requisitos procedimentais separados |
| **Proprietários** | Função responsável por cada lacuna restante |
| **Lacuna de execução** | Comportamento de exclusão/implantação não testado |
| **Condições de parada** | Acesso ausente, autoridade alterada, publicação não autorizada |

**Verificação de conclusão:** os dois pacotes sobrevivem à reconstrução independente, os casos aplicáveis têm evidência observada e os controles não resolvidos continuam visíveis. Se apenas a trilha GitHub estiver concluída, relate conclusão parcial do curso. Não presuma que Mixed funcionaria da mesma forma.

## Solução de problemas e backout

**Somente evidência de caminho feliz:** repita testes de negação e interrupção. **Funções sobrepostas:** divulgue e repita com usuários separados. **Controles do plano ausentes:** pare e obtenha uma sandbox aprovada.

**Backout:** restaure a baseline por PRs revisados e edições do Confluence, revogue integrações temporárias, arquive evidências do Jira e execute a limpeza sintética aprovada pelos proprietários depois da retenção das evidências. Preserve o histórico de recuperação.

## Crie a decisão de rollout

```text
Decision: another synthetic pilot, blocked, or rejected
Evidence: both run packages and failure matrix
Unenforced requirements: procedural controls listed explicitly
Provider review: input scope and retention handling
Owner coverage: product, operations, policy, repository, delivery
Production gaps: runtime tests, secrets, deployment, access review
Next action: one bounded follow-up with accountable role
Review date: assigned by pilot owners
```

**Raciocínio esperado:** sucesso sintético apoia outro piloto limitado. Produção exige aprovação separada para dados reais, implantação, tratamento pelo provedor e comportamento em execução. Uma resposta bem-sucedida do assistente não é autorização de implantação.

## Referências principais

- **Controles do repositório:** [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Acesso ao workplace:** [Confluence permissions](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controles de entrega:** [Jira permission schemes](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).

## Próximos passos

**Volte ao [hub do curso](/ai-collaboration-course-start/)** para revisar controles ausentes. Compare sua implementação com o [artigo do framework](/articles/one-source-many-tools-ai-collaboration-framework/) antes de selecionar outro piloto.

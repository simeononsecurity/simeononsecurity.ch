---
title: "Configuração de IA no Confluence e Jira: permissões e autoridade"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Configure páginas de referência oficiais no Confluence e permissões do Jira gerenciadas pela empresa para uma colaboração entre equipes com revisão."
genre: ["Inteligência artificial", "Colaboração em equipe", "Engenharia de software"]
tags: ["curso de colaboração com IA", "Confluence Cloud", "Jira Cloud", "páginas de referência oficiais", "esquema de permissões do Jira", "transição de fluxo de trabalho", "testes de acesso"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustração de profissionais revisando o trabalho compartilhado de um projeto em um ambiente de cibersegurança"
coverCaption: ""
---

[Volte ao curso de colaboração com IA](/ai-collaboration-course-start/)

**O administrador define a autoridade no local de trabalho antes de conectar as ferramentas de chat.** Os responsáveis por produto e operações publicam requisitos e manuais no Confluence Cloud. O Jira Cloud coordena a entrega. O GitHub controla a implementação. Crie ambientes de teste dedicados depois de estabelecer a base, pois uma permissão incorreta expõe informações independentemente do comportamento do modelo.

## Principais conclusões

- **Confluence** mantém a redação aprovada dos requisitos.
- **Jira** mantém o estado da entrega, não a política de retenção.
- **GitHub** mantém a configuração e as políticas compartilhadas.
- **Os testes de permissões** exigem planos adequados e usuários separados.

## Antes de começar

**Pré-requisitos:** os [fundamentos](/articles/ai-collaboration-pilot-foundation/), o repositório do laboratório, a administração de espaços do Confluence e do Jira e usuários separados para os papéis de colaborador, responsável e publicador. **Tempo estimado:** de 90 a 120 minutos. **Dificuldade:** administração avançada.

**Requisito do plano:** o Confluence Free não oferece restrições de conteúdo. O Jira Free não tem esquemas de permissões configuráveis, papéis de espaço nem esquemas de segurança de itens de trabalho. Use ambientes de teste adequados no plano Standard ou superior para esta etapa. Antes dos testes, confira o plano e os privilégios reais nas referências.

**Nota de navegação:** a documentação atual do Jira usa “space” e “work item”. Alguns tenants ainda usam “project” e “issue”. Escolha uma configuração gerenciada pela empresa. Este procedimento não cobre o comportamento de permissões em uma configuração gerenciada pela equipe. Não são necessários Rovo, aplicativos do Marketplace, aprovações do Jira Service Management nem um conector de chat pago.

**Resultado esperado:** prepare uma matriz de permissões, páginas de referência oficiais nomeadas, um fluxo de trabalho do Jira exclusivo do laboratório e provas de acesso negado obtidas com usuários separados. Registre o plano do tenant e as premissas sobre os papéis ao lado dos resultados dos testes.

**Verificações antes de criar registros:**

| Verificação | Se disponível | Se não estiver disponível |
|---|---|---|
| Restrições de páginas e administração de espaços do Confluence | Crie páginas aprovadas e excluídas separadas | Marque os testes de edição e de leitura negada como Bloqueados |
| Esquema de permissões e editor de fluxo do Jira gerenciado pela empresa | Copie um esquema e um fluxo exclusivos do laboratório | Marque os testes de transição como Bloqueados |
| Usuários separados para colaborador, responsável, publicador e usuário excluído | Execute testes positivos e negativos por papel | Marque os papéis não testados como Bloqueados |
| Responsável pelo repositório e branch protegida | Vincule o caminho de implementação revisado | Conclua primeiro o caminho GitHub-first antes da publicação mista |

Em outubro de 2026, use o botão **Share** ou o controle de restrições para gerenciar o acesso às páginas, a área de permissões **Space settings** do Confluence para concessões mais amplas e **Settings > Work items > Permission schemes** no Jira para o esquema do laboratório. O editor de fluxo do Jira gerenciado pela empresa controla as transições. Os rótulos da interface e os recursos dos planos variam por tenant. Registre o caminho e o plano reais como evidência antes de seguir estas etapas. Consulte as [permissões de página do Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/) e os [esquemas de permissões do Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/).

## Criar páginas de referência oficiais

1. **Crie um espaço do Confluence** chamado **`Export Service Lab`**. Desative o acesso anônimo e o compartilhamento público pelos controles disponíveis do site ou do espaço.
2. **Crie páginas publicadas**, não documentos ativos, com os nomes **`REQ-17 Export Retention`**, **`RUN-04 Export Cleanup`** e **`Decision Register`**.
3. Como responsável pelo produto, **publique o requisito inicial** abaixo. Registre o ID e a versão reais da página no mapa do repositório.
4. Como responsável pelas operações, **publique RUN-04** com retenção de sete dias e a declaração de que nenhuma tarefa de exclusão é executada neste laboratório.
5. Em cada página de referência oficial, **abra Share**. Defina o acesso geral como somente leitura para membros elegíveis do espaço e conceda permissões específicas de edição aos responsáveis e publicadores designados. Salve e verifique com o usuário colaborador.

```text
Source ID: REQ-17
Owner role: product-owner
Status: Approved baseline
Scope: synthetic export files only
Retention: 7 days
Delivery state: baseline lab configuration
Exceptions: production data, backups, and legal holds excluded
Approval evidence: DEC-12 baseline review
Implementation reference: attach protected GitHub baseline commit
```

**Aplique restrições a cada página de referência oficial.** Não presuma que a restrição de edição de uma página pai protege suas páginas filhas. A herança de leitura e edição funciona de forma diferente, e as permissões do espaço continuam valendo. Um link sozinho não concede acesso. Confira todas as associações se um usuário que deveria ter apenas leitura ainda puder editar.

**Use estes textos iniciais para as outras duas páginas.** Substitua os campos provisórios de revisão por evidências reais do ambiente de teste antes de aprovar um registro.

```text
Source ID: RUN-04
Owner role: operations-owner
Status: Approved baseline
Scope: synthetic export files only
Configured retention: 7 days
Procedure: compare REQ-17 with config.json before a reviewed change
Runtime limit: this lab has no deletion job and produces no deletion evidence
Recovery: restore the prior approved configuration through review
Recovery limit: restoring configuration does not restore deleted files
Review evidence: add actual reviewer, page version, and decision reference
```

```text
Page: Decision Register
Entry ID: DEC-12
Decision: use seven days as the synthetic baseline
Scope: export-service-lab only
Requirement: REQ-17 page version, record after publication
Runbook: RUN-04 page version, record after publication
Policy: POL-01 protected GitHub revision, record after review
Product review: pending until the named owner records a decision
Operations review: pending until the named owner records a decision
Status: draft example, replace with observed review evidence
```

## Atualizar o mapa

```yaml
track: mixed-workplace
policy: {source_id: POL-01, home: GitHub, version: 1}
requirements: {source_id: REQ-17, home: Confluence, owner_role: product-owner}
runbook: {source_id: RUN-04, home: Confluence, owner_role: operations-owner}
decisions: {source_id: DEC-12, home: Confluence, owner_role: project-lead}
implementation: {home: GitHub, file: config.json}
delivery: {home: Jira, proposal_id: PROP-042}
snapshot_rule: repository requirement copies are not authoritative
```

**Adicione ao mapa os locais privados reais do ambiente de teste e os IDs das páginas.** O modelo indica quais são as fontes oficiais sem fingir que contém endereços ativos. Remova do README o texto que atribui ao arquivo JSON copiado a autoridade sobre os requisitos do caminho misto.

**Mantenha POL-01 no GitHub** para os dois caminhos. O Confluence aponta para sua revisão aprovada. Mudar a autoridade da política durante uma tarefa exige outra transição de autoridade revisada.

## Definir permissões do Jira

1. **Crie um espaço de laboratório gerenciado pela empresa** e copie um esquema de permissões para um esquema dedicado ao laboratório. Não edite um esquema de produção compartilhado.
2. **Abra Settings, Work items, Permission Schemes**, selecione o esquema do laboratório e atualize as concessões.
3. **Conceda aos colaboradores permissões para navegar, criar e comentar.** Restrinja os privilégios administrativos. Confira explicitamente as permissões de edição e **Transition work items**.
4. **Associe o esquema** ao espaço do laboratório e verifique se nenhum espaço de produção o compartilha.
5. **Crie PROP-042** como item de trabalho. Registre a chave gerada no mapa e mantenha PROP-042 como ID lógico da proposta na descrição.

**Cole este rascunho em PROP-042.** O item do Jira acompanha a entrega. Seu texto não substitui a redação aprovada no Confluence.

```text
Proposal ID: PROP-042
Status: Draft
Current approved value: 7 days, REQ-17 page version to record
Proposed value: 30 days for synthetic export files
Exclusions: production data, backups, legal holds
Affected records: REQ-17, RUN-04, config.json, proposal.json
Fixed proposal attachment: pending
Product-owner review: pending
Operations-owner review: pending
Publication ledger: pending
Stop on changed source version, missing review, or denied access
```

| Papel | Confluence | Jira | GitHub |
|---|---|---|---|
| **Colaborador** | Lê páginas aprovadas | Cria rascunhos e comenta | Branch da proposta ou Issue |
| **Responsável pelo produto** | Revisa o requisito | Registra a revisão do requisito | Revisa as evidências da PR |
| **Responsável pelas operações** | Revisa o manual | Registra a revisão operacional | Revisa o impacto operacional |
| **Publicador** | Edita páginas aprovadas | Registra o estado da publicação | Sem autoridade automática para mesclar |
| **Mantenedor** | Lê o requisito | Registra a implementação | Revisa e mescla a PR protegida |

**As permissões de grupos diferentes são cumulativas.** Remova concessões amplas não intencionais no laboratório em vez de presumir que uma concessão restrita substitui a ampla. Não coloque identidades de conectores em grupos administrativos.

## Definir estados da entrega

**Copie um fluxo de trabalho gerenciado pela empresa** para um fluxo exclusivo do laboratório. Adicione os estados Rascunho, Revisão, Aprovado, Publicação, Concluído e Bloqueado. Adicione transições para envio, aprovação, publicação, conclusão, bloqueio e retorno à revisão. Associe o fluxo somente ao tipo de trabalho do laboratório.

1. No editor de fluxo, **selecione a transição para Aprovado**.
2. **Adicione uma condição ou restrição** que permita a ação somente ao papel ou grupo designado de responsável/publicador. Use os controles de condição documentados e publique o rascunho do fluxo como administrador.
3. **Confira manualmente as revisões dos dois responsáveis** antes da transição. Cada revisão identifica a proposta congelada e as versões das fontes.
4. **Restrinja Concluído** ao papel responsável pela entrega. Remova transições alternativas ou globais que contornem esse limite.

**Uma transição restrita não é aprovação por duas pessoas.** Ela controla quem executa a transição. Neste piloto, a conferência das evidências dos dois papéis continua sendo um procedimento. Registre esse limite de forma explícita.

**Exemplo de registro de transição:** para **Revisão para Aprovado**, permita que somente o grupo designado de responsáveis/publicadores ative a transição. Antes de ativá-la, a pessoa abre o anexo fixo PROP-042 e confere uma decisão do responsável pelo produto e outra do responsável pelas operações sobre a mesma revisão da proposta. Se faltar uma decisão ou ela se referir a uma revisão antiga, mantenha o item em Revisão e registre a lacuna. A restrição do fluxo controla quem executa a transição. A conferência das evidências é uma etapa humana separada.

## Verificar a negação de acesso

**Como colaborador**, leia REQ-17, tente editá-lo, crie o rascunho do Jira e tente a transição para Aprovado. Os resultados esperados são requisito legível, edição negada, criação bem-sucedida da proposta e aprovação negada. Compare as versões da fonte antes e depois da negação.

**Como usuário excluído**, abra uma página sintética com restrições separadas. O conteúdo não deve ficar acessível. Teste as páginas filhas de forma independente. Não cole o texto protegido no chat do usuário excluído para contornar a restrição.

## Adaptar o mapa do repositório

**Mantenha os IDs das fontes estáveis quando os locais mudarem.** REQ-17 continua representando a intenção aprovada de retenção, mas no caminho misto sua fonte é uma página do Confluence. Uma cópia no repositório ajuda nas verificações e revisões. Ela não substitui a fonte oficial da página.

| Registro | Fonte de autoridade | Tratamento no repositório |
|---|---|---|
| **REQ-17** | Página de requisitos do Confluence indicada no mapa | Captura com evidência da revisão da página |
| **RUN-04** | Página de manual do Confluence indicada no mapa | Trecho operacional capturado para manter a consistência |
| **POL-01** | Política protegida no GitHub | As instruções compartilhadas dos agentes fazem referência a ela |
| **Configuração** | Registro protegido no GitHub | Diferença de implementação proposta |
| **Entrega** | Item de trabalho do Jira | Link de correlação, não cópia da política |

**Inclua a procedência junto às capturas.** No pacote privado da proposta, registre o ID da fonte, a referência e a versão da página, o horário da captura e o papel de quem a capturou. Não inclua IDs nativos de páginas em trabalhos públicos do curso. Se o publicador encontrar outra versão atual, reconcilie antes de usar a captura.

**Não renomeie a autoridade para se adequar à ferramenta.** A descrição editável do Jira facilita a discussão, mas continua sendo um registro de entrega. Uma frase de trinta dias no Jira não substitui um requisito de sete dias no Confluence.

## Projetar testes de acesso

**Separe leitura, elaboração de rascunho e publicação.** O colaborador precisa de acesso suficiente para entender o requisito sintético e enviar uma proposta. Ele não precisa de permissão para editar a página de referência oficial nem para aprovar a própria proposta.

```text
Test record: PERM-REQ-EDIT
Role: contributor
Source: REQ-17
Precondition: source is readable, published revision captured
Attempt: edit the authoritative requirement
Expected: edit denied, published revision unchanged
Observed: fill from the sandbox
Evidence: native result and independent revision read-back
Reviewer: administrator or independent permission reviewer
```

**Use um registro separado para a leitura negada.** O requisito que o colaborador consegue ler testa a separação entre publicação e edição. A página inacessível ao usuário excluído testa a confidencialidade. Combinar os dois casos em uma linha esconde qual limite foi testado.

**Confira também o acesso permitido.** Responsáveis e publicadores precisam usar o caminho atribuído. Se todos os usuários forem bloqueados, o ambiente de teste será restritivo, mas inutilizável. Guarde evidência de uma edição autorizada bem-sucedida em uma página de teste descartável sem alterar o requisito aprovado durante o diagnóstico de permissões.

## Ensaiar a revisão do Jira

**Trate os nomes dos estados como o desenho deste piloto.** Rascunho contém uma solicitação. Revisão contém um pacote congelado. Aprovado registra a conclusão da revisão dos responsáveis. Publicação indica entrega incompleta. Concluído exige uma leitura de retorno. Bloqueado indica falta de evidências ou acesso, ou conflito não resolvido.

| Transição | Pacote necessário | Conferência responsável |
|---|---|---|
| **Rascunho para Revisão** | Proposta fixa e versões das fontes | Colaborador confirma a integridade |
| **Revisão para Aprovado** | Decisões de produto e operações | Pessoa autorizada confere os dois papéis |
| **Aprovado para Publicação** | Comparação com as fontes atuais | Publicador confirma que as bases não mudaram |
| **Publicação para Concluído** | Registro completo por sistema | Responsável pela entrega confere a leitura de retorno |
| **Qualquer etapa compatível para Bloqueado** | Falha e ação pendente | Responsável pela recuperação designado |

**Ensaie com um pacote sintético incompleto.** Envie apenas a revisão de produto e peça à pessoa autorizada a avaliar a transição. O esperado é deixar o trabalho em Revisão e pedir a revisão de operações. Isso testa a etapa de revisão do procedimento separadamente da negação da plataforma ao colaborador.

**Teste as rotas alternativas de propósito.** Na visualização do fluxo do ambiente de teste, inspecione cada rota para Aprovado e Concluído. Uma transição restrita e nomeada não basta se outra rota disponível ignorar o mesmo limite de revisão. Registre as rotas verificadas e o usuário usado em vez de alegar cobertura completa após um clique.

## Diagnosticar acesso inesperado

**Comece pela identidade efetiva.** Confirme que a sessão do navegador pertence ao papel de teste pretendido. Depois, confira a associação a grupos, as permissões do espaço, o acesso às páginas e a associação do fluxo usando as ferramentas administrativas do produto. Não altere vários controles de uma vez, pois a negação perderá seu valor de diagnóstico.

1. **Confirme a identidade:** use sessões separadas para colaborador, publicador e usuário excluído.
2. **Localize a concessão:** identifique a associação ou configuração que permite a ação tentada.
3. **Ajuste o controle do laboratório:** mantenha o acesso legítimo dos responsáveis.
4. **Repita a mesma tentativa:** registre a versão da fonte sem alterações após a negação.
5. **Repita o caso positivo:** confirme que a publicação autorizada continua funcionando.

**Lista final de evidências:** registre a árvore de páginas do Confluence e os IDs mapeados, a associação do esquema Jira do laboratório, a associação do fluxo do laboratório, a associação de cada papel de teste aos grupos, a leitura permitida do requisito, a edição negada com a versão inalterada, a criação permitida do rascunho, a transição para Aprovado negada com estado inalterado, a leitura negada do usuário excluído e o responsável pela limpeza. Para cada linha, mantenha o papel do usuário, a versão ou o estado inicial e final, o resultado nativo e o revisor independente. Registre o caminho de navegação observado no tenant, pois os rótulos e controles disponíveis variam conforme o plano.

**Verificação de conclusão:** entregue as páginas de referência oficiais mapeadas, o fluxo exclusivo do laboratório, a matriz de papéis prevista e os registros de permissões observados. Se o plano não tiver um controle necessário, deixe a linha correspondente como Bloqueada. A lição de publicação pressupõe que os testes foram aprovados, não apenas que existem capturas de tela das configurações.

## Solução de problemas e reversão

**O colaborador ainda consegue editar:** confira o acesso à página, as permissões do espaço e as associações. **A transição ainda funciona:** confira a associação do fluxo e as rotas de desvio. **As configurações não aparecem:** confira o tipo gerenciado pela empresa, a edição e o privilégio de administrador.

**Reversão:** remova as permissões dos conectores e arquive os rascunhos. Desvincule esquemas e fluxos exclusivos do laboratório depois de guardar as evidências. Restaure a redação aprovada da página pelo histórico revisado ou por uma edição compensatória. Não apague evidências de auditoria.

## Exercício e autoavaliação

**O Jira indica trinta dias, enquanto REQ-17 indica sete.** Identifique a entrada de implementação e o responsável por resolver a divergência.

**Raciocínio esperado:** o Confluence define a intenção. O Jira contém um erro de proposta ou de entrega. Interrompa a publicação e peça ao responsável pelo produto que reconcilie os valores, em vez de escolher o registro de data e hora mais recente.

## Referências principais

- **Restrições e plano:** [permissões do Confluence](https://support.atlassian.com/confluence-cloud/docs/manage-permissions-on-the-page-level/).
- **Controles de compartilhamento:** [acesso a conteúdo específico](https://support.atlassian.com/confluence-cloud/docs/add-or-remove-page-restrictions/).
- **Administração de esquemas:** [esquemas de permissões do Jira](https://support.atlassian.com/jira-cloud-administration/docs/grant-or-revoke-permissions-in-a-scheme/).
- **Condições de transição:** [fluxos de trabalho avançados](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).

## Próximas etapas

**Depois de passar nos testes de acesso, continue com [Publicação entre sistemas](/articles/ai-collaboration-confluence-jira-publication/)**.

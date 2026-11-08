---
title: "Fluxo de publicação com IA no GitHub, Confluence e Jira"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Publique uma proposta fixa de retenção no Confluence, GitHub e Jira com verificações de versão e recuperação de publicação parcial."
genre: ["Inteligência artificial", "Colaboração em equipe", "Engenharia de software"]
tags: ["curso de colaboração com IA", "Confluence Cloud", "Jira Cloud", "publicação entre sistemas", "verificação de versão", "registro de publicação", "publicação parcial"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustração de profissionais analisando o trabalho compartilhado de um projeto em um ambiente de cibersegurança"
coverCaption: ""
---

[Voltar ao curso de colaboração com IA](/ai-collaboration-course-start/)

**O colaborador congela PROP-042 antes da aprovação dos responsáveis.** Um publicador do Confluence atualiza os requisitos, um mantenedor do GitHub mescla a implementação e a equipe de operações publica o runbook. O Jira registra cada etapa. Faça isso após verificar as permissões, pois os três sistemas não formam uma transação atômica. Seu registro de publicação torna visíveis as entregas incompletas.

## Principais conclusões

- **A intenção aprovada** difere do comportamento entregue.
- **As revisões fixas da proposta** vinculam a análise a uma versão.
- **Os registros de publicação** expõem etapas incompletas.
- **Leituras recentes** protegem contra bases alteradas.

## Antes de começar

**Pré-requisitos:** a [configuração do ambiente de trabalho](/articles/ai-collaboration-confluence-jira-setup/), acesso de publicação, responsáveis e um mantenedor do repositório. **Tempo estimado:** duas horas. **Dificuldade:** coordenação avançada.

**Interface básica:** leituras no navegador, redação opcional em um chat aprovado e publicação humana. Nenhuma assinatura de conector é presumida. Antes de adicionar uma integração, verifique a disponibilidade no tenant, os escopos, o tratamento do provedor e o mapeamento de identidades. Nunca compartilhe as credenciais de um responsável com um colaborador.

**Resultado para o leitor:** você terminará com uma proposta fixa, um registro de publicação por sistema, evidências de releitura e uma decisão de recuperação para a primeira etapa incompleta. O exercício demonstra o procedimento e o tratamento de evidências, não o comportamento de retenção em produção.

## Registrar as fontes atuais

1. **Leia MAP-01** e, em seguida, abra REQ-17 e RUN-04 usando os IDs de página mapeados.
2. **Abra o menu da página e Page History** e registre as versões numéricas, o status, o texto, o responsável e as exceções.
3. **Leia o item do Jira** e anexe uma exportação fixa da proposta ou um commit do GitHub. A chave sozinha não fixa as evidências de análise.
4. **Leia POL-01 aprovada** e a linha de base protegida da configuração.
5. **Forneça ao chat somente os trechos sintéticos necessários**, marque-os como snapshots e mantenha desativadas as ações de gravação.

```text
Task: PROP-042, propose only
Authority: Confluence REQ-17 for intent, GitHub for behavior
Read: mapped current pages, versions, scope, exceptions
Proposal: synthetic export retention from 7 to 30 days
Output: requirement wording, config diff, runbook, ledger
Evidence: source ID and captured revision for each factual claim
Unknowns: missing access and absent runtime observations
Stop: conflict, changed base, or denied access
```

**Os pacotes offline continuam baseados em snapshots.** O publicador lê as fontes atuais novamente antes de escrever. Acesso negado bloqueia a publicação. Uma exportação antiga não substitui a autorização atual.

## Fixar a proposta

```json
{
  "proposal_id": "PROP-042",
  "proposal_revision": 1,
  "requirement_base_version": 1,
  "runbook_base_version": 1,
  "policy_version": 1,
  "from_days": 7,
  "to_days": 30,
  "status": "awaiting-owner-review",
  "publication_order": ["requirement", "implementation", "runbook", "delivery"]
}
```

**Substitua as versões ilustrativas das páginas pelas versões realmente capturadas.** Anexe o JSON fixo e o texto proposto ao Jira. Cada responsável registra sua função, decisão, revisão da proposta, versões das fontes e horário da análise. Qualquer edição substancial devolve o pacote para `Review`.

**Produto analisa a intenção e o escopo. Operações analisa a limpeza e a recuperação.** O mantenedor analisa o diff. Reações a mensagens de chat mutáveis não são aprovações vinculadas a uma revisão.

## Publicar e ler novamente

1. **Mova o Jira para `Publishing`** depois que o publicador verificar as duas análises dos responsáveis e confirmar que as bases de origem não mudaram.
2. **Publique REQ-17** com trinta dias e um campo de entrega pendente. Registre a versão resultante, o escopo e as exceções.
3. **Abra a PR de implementação do GitHub**, fazendo referência à versão aprovada da página. Altere a configuração para trinta dias e anexe um snapshot não autoritativo do requisito.
4. **Mescle após a análise do repositório** e leia **`main`** novamente. Registre separadamente o comportamento salvo no repositório e o comportamento em execução.
5. **Publique RUN-04**, leia-o novamente pelo ID e registre a versão resultante. O publicador atualiza as referências de entrega do requisito.
6. **Conclua o Jira** somente quando todos os registros concordarem e a evidência da releitura final estiver anexada.

**Use o validador local somente para verificar a consistência dos snapshots.** Copie o requisito do Confluence anterior à alteração para o esquema JSON de linha de base do laboratório, capture-o e edite o candidato para trinta dias. Use uma revisão local de snapshot incrementada e preserve separadamente no Jira as versões reais do Confluence. O fluxo que usa o GitHub como fonte raiz não valida o Confluence ativo. Não apresente o status verde como verificação de autoridade externa.

**Não implante a funcionalidade de exclusão neste exercício.** Um serviço real exige evidência de implantação, dados de teste controlados, um mecanismo para suspender temporariamente a exclusão e testes dos limites em execução. Um merge comprova o estado do repositório, não o comportamento de retenção em produção.

## Acompanhar a publicação parcial

| Etapa | Estado inicial | Evidência de conclusão |
|---|---|---|
| **REQ-17** | Pending | Versão resultante da página |
| **Configuração** | Pending | Commit mesclado e análise |
| **RUN-04** | Pending | Versão resultante da página |
| **Encerramento do Jira** | Pending | Releitura final e transição |

**Registre cada resultado antes de tentar a próxima etapa.** PROP-042 correlaciona os eventos de cada sistema. Uma única linha concluída não significa que a alteração inteira terminou.

**Falha ilustrativa:** o Confluence publica trinta dias, mas o GitHub nega o merge. Mantenha o Jira em `Blocked` e o requisito marcado como entrega pendente. Produto escolhe concluir o trabalho ou restaurar sete dias após análise. Não transforme uma cópia emergencial do README na autoridade do requisito.

## Lidar com edições simultâneas

**Referência do navegador:** designe um único publicador durante a janela do piloto. Reabra Page History imediatamente antes da edição e depois da publicação. Se outro autor alterar a fonte, pare, compare, reconcilie e renove a aprovação. A publicação serializada é um procedimento, não uma garantia de transação atômica.

**Extensão de API:** a documentação do Confluence v2 descreve **`GET /wiki/api/v2/pages/{id}?body-format=storage`** e **`PUT /wiki/api/v2/pages/{id}`** com um objeto de versão. Uma integração de publicação analisada compara a versão atual com a base aprovada, envia a próxima versão e lê o resultado. Nunca atualize automaticamente uma versão que falhou nem tente novamente com um corpo antigo.

**O sucesso da API não basta.** Verifique o conteúdo resultante, o ID da fonte, o escopo e a versão. Este curso não inclui um cliente de API com capacidade de escrita. A publicação humana no navegador é a referência executável para quem não programa.

## Verificar casos negativos

| Injeção | Raciocínio esperado |
|---|---|
| **Alterar a fonte após a aprovação** | Parar e aprovar novamente na nova versão |
| **Remover o acesso de edição do publicador** | Negar a atualização e manter o registro pendente |
| **Definir Jira em sessenta dias** | Parar o conflito e preservar a autoridade do Confluence |
| **Falha na publicação do runbook** | Manter a entrega incompleta e atribuir a recuperação |

**Registre os resultados reais do sandbox** com a função do ator e as revisões antes e depois. Não inclua o conteúdo protegido da página na evidência para usuários sem acesso. Resultados esperados não são resultados medidos.

## Montar o pacote de análise

**Congele o conteúdo, não apenas o rótulo da proposta.** PROP-042 aparece em cada sistema, mas um rótulo não identifica o conteúdo analisado pelo responsável. Inclua o texto exato do requisito, o diff de implementação, o texto do runbook, as versões das fontes e a sequência de publicação em um único pacote fixo.

```text
Package: PROP-042 revision 1, illustrative
Intent: synthetic export retention changes from 7 to 30 days
Exclusions: production data, backups, legal holds
Requirement amendment: fixed proposed REQ-17 wording
Implementation: fixed candidate diff and protected base reference
Runbook amendment: fixed RUN-04 wording and recovery limits
Review: product and operations decisions for this package
Delivery: requirement -> implementation -> runbook -> closure
Stop: changed source, missing review, denied write, failed read-back
```

**Deixe o pacote legível para os dois responsáveis.** Produto precisa da intenção e das exclusões. Operações precisa da alteração operacional e dos limites de recuperação. Ambos precisam entender o período em que a intenção aprovada e a configuração entregue diferem. Um diff de código isolado não basta para um responsável que não conhece os arquivos do repositório.

**Conteúdo preenchido do pacote para este exemplo sintético:**

```text
REQ-17 proposed v5: "Synthetic export files are retained for 30 days from creation. This pilot excludes production data, backups, and legal holds. Delivery remains pending until the GitHub configuration and RUN-04 read-backs match this approved wording."

GitHub config.json, proposed change against base-001:
-  "retention_days": 7
+  "retention_days": 30

RUN-04 proposed v3: "Retention days: 30. Synthetic exports only. No deletion job runs in this lab. If publication fails, keep delivery pending, read back each source, and obtain owner approval before restoring the seven-day configuration or completing the thirty-day publication."
```

Essas frases são propostas de exemplo, não registros de um tenant ativo. Anexe o commit-base real e as versões das páginas antes da análise. O pacote fixo precisa incluir os corpos propostos completos, não um resumo que exija que o responsável os deduza.

**Separe o snapshot offline da publicação ativa.** Imediatamente antes da primeira gravação, o publicador verifica novamente as páginas mapeadas e o mantenedor verifica novamente a base protegida. Se qualquer uma mudou, o pacote antigo para em `Review`.

## Percorrer o registro

**Progressão ilustrativa de estado:** a tabela usa revisões didáticas, não observações. Preencha as versões resultantes e os commits reais após cada gravação no sandbox.

| Etapa | Estado após leitura bem-sucedida | Trabalho restante |
|---|---|---|
| **Análise dos responsáveis concluída** | Pacote aprovado, todos os valores publicados em sete | Todas as etapas de publicação |
| **REQ-17 publicado** | Intenção em trinta, entrega pendente | Configuração e runbook |
| **Merge do GitHub lido novamente** | Intenção/configuração em trinta, runbook em sete | Runbook e reconciliação final |
| **RUN-04 publicado** | Todos os registros aplicáveis em trinta | Leitura final independente |
| **Entrega encerrada** | Registro completo com evidências | As lacunas em execução declaradas continuam |

**Entrega pendente é um estado significativo.** Ela evita descrever a implementação antiga como compatível com a nova intenção enquanto a publicação está incompleta. Durante esse período, os leitores precisam dos dois valores, não de um único resumo afirmando que a retenção é de trinta dias.

**Acrescente tentativas falhas como eventos separados.** Se a gravação do runbook falhar, mantenha os resultados bem-sucedidos do requisito e da configuração. Registre a ação tentada, a falha, a versão inalterada, a função atribuída e a próxima ação. Não redefina linhas concluídas para Pending nem apague a sequência observada.

**Exemplo de rejeição por versão obsoleta:** o publicador lê REQ-17 v4, outro editor autorizado publica v5 e, em seguida, o publicador tenta aplicar PROP-042 r1 sobre v4. A plataforma informa um conflito de versão ou a leitura prévia à gravação detecta v5. Registre o ator `publisher`, a versão inicial `v4`, a tentativa `PROP-042 r1`, o conflito observado ou a alteração da versão atual, a versão final `v5` inalterada por esta tentativa e o responsável atribuído `product owner`. Mantenha o Jira em `Review`. Leia v5 novamente, reconcilie o texto e solicite a análise de um novo pacote fixo antes de outra gravação. Use a resposta real da plataforma e Page History em um teste ativo. Esta linha é um exemplo didático.

**Exemplo didático concluído, somente valores sintéticos:**

| Sistema | Fonte inicial | Análise fixa | Gravação e releitura | Estado final |
|---|---|---|---|---|
| Confluence REQ-17 | v4, sete dias | PROP-042 r1, Produto aprovou v4 para v5 | Publicador gravou v5, revisor reabriu v5 | Trinta dias, backups e retenções legais excluídos |
| Configuração do GitHub | Commit `main` `base-001`, sete dias | PROP-042 r1, Operações aprovou o diff candidato | PR mesclada como `merge-002`, clone independente leu trinta | Trinta dias na fonte protegida |
| Confluence RUN-04 | v2, sete dias | PROP-042 r1, Operações aprovou v2 para v3 | Publicador gravou v3, revisor reabriu v3 | Etapa operacional de trinta dias com reversão |
| Jira PROP-042 | In Review | As decisões dos dois responsáveis estão vinculadas a r1 | Responsável pela entrega anexou evidências e passou para Done | Encerrado após as três releituras |

Os rótulos acima são ilustrativos, não evidências de tenant. Seu registro precisa de links nativos das versões das páginas e IDs de commit. Antes de mover o Jira para Done, anexe a proposta congelada, as duas análises por função, o registro da base de origem, cada releitura da publicação, o resultado do teste negativo e os limites de execução não resolvidos. Se faltar algo, mantenha a entrega aberta ou `Blocked`.

**Portão do pacote:** marque cada uma das cinco verificações como `Supported` ou `Blocked`: as revisões das fontes estão atuais, os dois responsáveis aprovaram a mesma revisão fixa, todas as publicações necessárias coincidem com a releitura, os limites de execução continuam explícitos e o estado de recuperação foi reconciliado. `Done` exige cinco verificações `Supported` e nenhuma gravação não autorizada.

## Lidar com uma gravação incerta

**Um timeout deixa o resultado desconhecido.** Não comprova sucesso nem falha. No fluxo do navegador, reabra a fonte mapeada e examine o conteúdo e o histórico atuais antes de decidir se tentará novamente.

1. **Pause a próxima etapa:** mantenha a entrega incompleta.
2. **Leia o destino:** compare o texto atual, a versão e o escopo com o pacote fixo.
3. **Registre a observação:** concluída, inalterada, conflitante ou inacessível.
4. **Escolha a próxima ação:** prossiga a partir de uma conclusão verificada, tente novamente uma etapa autorizada e inalterada ou encaminhe um conflito.
5. **Preserve a incerteza:** mantenha a tentativa falha/desconhecida junto da releitura posterior.

**Não reproduza toda a sequência às cegas.** Repetir uma etapa já concluída acrescenta revisões e traz o risco de sobrescrever edições alheias. Retome a partir de um estado verificado. Se o acesso à fonte estiver indisponível, escolha `Hold` em vez de adivinhar com base no registro antigo.

## Comparar decisões de recuperação

| Situação | Decisão a analisar | Motivo |
|---|---|---|
| **Requisito alterado, merge negado** | Concluir ou compensar o requisito | Intenção e comportamento diferem |
| **Configuração alterada, runbook negado** | Concluir o runbook ou reverter a configuração | A orientação operacional está desatualizada |
| **Outro responsável altera o escopo** | Voltar para `Review` | A aprovação fixa descreve outro conteúdo |
| **Resultado da gravação desconhecido** | Ler o destino primeiro | A nova tentativa depende do estado observado |
| **Publicador perde o acesso** | Manter `Hold` e solicitar administração autorizada | A autorização antiga não permite novas gravações |

**Decida com base no estado atual e na decisão do responsável.** A conclusão exige aprovações atuais e controles funcionais. A compensação exige analisar a restauração diante das edições intermediárias. Uma recuperação é outra publicação, não uma exceção privilegiada ao processo.

## Verificação da conclusão da publicação

**Entregue um pacote que um revisor independente consiga reconciliar.** Ele deve encontrar a proposta exata analisada, suas bases de origem, as duas análises por função, o resultado de cada gravação, os valores finais e as limitações de execução restantes. Peça que identifique a primeira etapa incompleta após uma interrupção.

**Raciocínio esperado:** a próxima ação vem de fontes recentes e do registro, não da confiança do assistente anterior. Leve as referências finais mapeadas aos testes de recuperação, nos quais a descoberta deve preservar a mesma distinção de autoridade.

## Solução de problemas e recuperação

**Versão alterada:** compare o histórico e renove a análise. **Verificação do snapshot passa, mas a wiki difere:** obtenha novamente as fontes atuais do Confluence. **Marcado como Done cedo demais:** reabra pelo fluxo permitido e registre as etapas ausentes.

**Recuperação:** use a comparação do Page History e uma restauração ou edição compensatória analisada por um responsável. Registre a versão resultante em vez de presumir que a restauração redefine a numeração. Reverta a configuração por uma PR protegida se Produto escolher o recuo. Arquivos excluídos ficam fora da garantia de reversão.

## Exercício e autoavaliação

**Interrompa após publicar REQ-17** e dê a outro publicador somente o mapa e o registro.

**Raciocínio esperado:** ele obtém as fontes atuais, confirma a aprovação fixa e retoma somente a etapa pendente autorizada. A falta de evidências devolve o trabalho para `Review`.

## Referências principais

- **Histórico e restauração:** [documentação técnica do Confluence](https://support.atlassian.com/confluence-cloud/docs/use-confluence-for-technical-documentation/).
- **Operações de API com versões:** [páginas da Confluence REST API v2](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).
- **Controles do fluxo de trabalho:** [fluxos de trabalho avançados do Jira](https://support.atlassian.com/jira-cloud-administration/docs/configure-advanced-issue-workflows/).
- **Segurança da integração:** [boas práticas de segurança do MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices).

## Próximos passos

**Continue com [Recuperação com prioridade no mapa](/articles/ai-collaboration-map-first-retrieval/)** após concluir uma execução de publicação analisada.

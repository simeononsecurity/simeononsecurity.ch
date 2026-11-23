---
title: "Uma fonte, muitas ferramentas: um modelo de colaboração com IA para equipes mistas"
date: 2026-10-01
lastmod: 2026-11-23
toc: true
draft: false
description: "Crie um sistema compartilhado de colaboração com IA, com responsáveis pelas fontes, versões de contexto, revisão durável de mudanças e critérios claros para escolher entre mapas de projeto e RAG."
genre: ["Inteligência artificial", "Gestão do conhecimento", "Engenharia de software", "Colaboração em equipe"]
tags: ["modelo de colaboração com IA", "equipes mistas", "fonte oficial", "agentes de IA", "AGENTS.md", "CLAUDE.md", "regras do Cline", "Claude Code", "Codex", "ChatGPT", "Copilot", "Cowork", "geração aumentada por recuperação", "RAG", "Model Context Protocol", "mapa de projeto", "manifesto de contexto", "gestão do conhecimento", "desatualização da documentação", "aprovação humana", "registro de decisões", "transferência entre agentes", "versionamento de políticas", "worktrees do Git", "etapas de aprovação de pull request"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustração de profissionais colaborando em tarefas de cibersegurança"
coverCaption: ""
---

**Duas pessoas fazem a mesma pergunta a duas ferramentas de IA:** por quanto tempo o serviço deve manter uma exportação? Neste exemplo ilustrativo, o agente de IDE do desenvolvedor responde sete dias, com base em um README. O assistente de chat da liderança de operações responde trinta dias, com base em uma página wiki. As duas respostas parecem confiantes. Cada ferramenta leu uma versão diferente da verdade.

**A falha está na responsabilidade,** não na qualidade do prompt. O requisito da wiki mudou na semana passada, mas ninguém atualizou o README. O desenvolvedor pede ao agente que corrija a tarefa de retenção. O agente segue o documento antigo e produz um patch organizado que restaura o comportamento errado. Os revisores inspecionam o código sem ver a versão do requisito por trás da resposta.

**Defina uma fonte para cada fato.** Faça todas as ferramentas lerem essa fonte e encaminhe toda mudança duradoura para uma pessoa. Repositório, wiki e rastreador têm finalidades diferentes. Eles precisam de autoridade explícita, responsáveis nomeados e um procedimento comum para transferir informações entre si.

**Este guia apresenta um modelo que você pode aplicar esta semana,** com ou sem geração aumentada por recuperação. Comece com um mapa de projeto, instruções versionadas, registros de evidências e propostas revisadas. Acrescente infraestrutura de pesquisa somente quando o problema de recuperação justificar.

**Sua primeira entrega deve ser um registro de fontes,** não um conector. Liste cada tipo de fato, sua fonte oficial, seu responsável, sua revisão atual e quem aprova mudanças.

## Principais conclusões

- **Atribua autoridade por tipo de informação,** sem forçar tudo para um único aplicativo.
- **Trate memória e índices de recuperação como caches,** nunca como fontes de política independentes.
- **Anexe as versões das fontes às propostas,** para que os revisores saibam quais fatos embasaram a mudança.
- **Exija aprovação fora dos prompts,** com controles de acesso e etapas obrigatórias de revisão.
- **Compartilhe o procedimento entre ferramentas,** adaptando sua apresentação a cada interface.

## Antes de começar

**Pré-requisitos:** escolha um projeto piloto com repositório, wiki ou sistema de documentos, rastreador e responsáveis dispostos a revisar mudanças. Uma equipe sem wiki pode usar um repositório de documentos versionado. Mantenha o modelo de responsabilidade.

**Tempo estimado:** reserve de duas a quatro horas para o mapa e os modelos iniciais, seguidas de um piloto de uma semana. **Dificuldade:** moderada. O desafio é definir autoridade, não instalar outra ferramenta de IA.

**Escopo:** este é um modelo operacional proposto para equipes. Suas regras de aprovação e convenções de nomes são recomendações, não comportamentos padrão garantidos por Claude Code, Codex, Cline, Cowork, Copilot ou ChatGPT. O índice automático acima aponta para cada etapa de implementação.

## Ferramentas mistas, contextos divididos

**Programadores e não programadores compartilham um projeto,** mas usam interfaces diferentes. Um desenvolvedor usa um agente de IDE ou terminal. Uma pessoa de produto usa um projeto de chat. Uma liderança de operações trabalha com wiki e rastreador. Escolha as interfaces pela tarefa, não pelo acesso aos fatos oficiais.

**Contexto é o material disponível para a resposta atual.** Inspecione cada sessão para ver arquivos do repositório, documentos enviados, histórico de chat, memória salva, resultados de conectores e trechos recuperados. Duas sessões com evidências diferentes não precisam concordar, mesmo quando as perguntas coincidem.

| Falha | O que aparece |
|---|---|
| **Desatualização da documentação** | Um README repete um requisito obsoleto |
| **Resumo promovido a evidência** | Uma recapitulação de sessão vira evidência sem a fonte original |
| **Escritas sobrepostas** | Dois agentes substituem a mesma página a partir de versões-base diferentes |
| **Decisões perdidas** | Um acordo de reunião nunca chega ao registro de decisões |
| **Falta de proveniência** | Uma resposta plausível não identifica a versão da página nem o commit |

**O exemplo de retenção mostra a diferença.** A wiki descreve o comportamento desejado e aprovado. O código descreve o comportamento implementado. Nenhum deve reescrever o outro em silêncio. Registre a divergência e pergunte à pessoa responsável se a implementação ou o requisito precisa mudar.

> **Ponto principal:** definir autoridade vem antes de escolher uma ferramenta de IA. Comece pelos termos abaixo.

### Barra lateral: cinco termos compartilhados

| Termo | Significado neste modelo |
|---|---|
| **Fonte** | Registro oficial designado para um tipo de informação |
| **Cache** | Cópia derivada para velocidade ou conveniência |
| **Proposta** | Mudança sugerida que aguarda aprovação do responsável |
| **Mapa de projeto** | Índice de locais das fontes, identificadores e responsáveis |
| **Manifesto** | Registro das evidências exatas usadas em uma resposta ou proposta |

## Dê uma fonte a cada fato

**Uma fonte significa uma autoridade por fato,** não um único banco de dados para toda a organização. Defina a distribuição abaixo no piloto. Substitua os papéis de exemplo pelos responsáveis reais da equipe.

| Tipo de informação | Sistema de origem | Responsável | Quem escreve | Como os agentes leem |
|---|---|---|---|---|
| **Código, testes, configuração, esquemas** | Repositório | Mantenedor de engenharia | Colaboradores por PR revisado | Arquivos em um commit registrado |
| **Documentação publicada e ADRs** | Repositório | Responsável técnico | Colaboradores pelo mesmo PR | Arquivos versionados |
| **Requisitos** | Wiki | Responsável de produto | Responsável ou publicador autorizado | ID e revisão da página |
| **Runbooks** | Wiki | Responsável de operações | Publicador autorizado | ID e revisão da página |
| **Política** | Wiki | Responsável por política | Publicador autorizado após revisão | Página oficial e adaptador local |
| **Decisões entre equipes** | Registro de decisões da wiki | Responsável nomeado pela decisão | Responsável após aprovação | ID e estado da decisão |
| **Tarefas e achados** | Rastreador | Responsável pela tarefa | Pessoas ou entrada autorizada de propostas | Chave e revisão da issue |
| **Chats, resumos, embeddings** | Somente cache | Responsável pela sessão ou índice | Ferramentas e participantes | Apenas referência, seguida de consulta à fonte |

**Um registro de decisão de arquitetura (ADR)** fica junto do código quando orienta o projeto do repositório. Uma decisão entre equipes pertence ao registro compartilhado. Ligue os registros quando a decisão abranger ambos os escopos. Não mantenha duas cópias independentes do estado de aprovação.

**Cópias locais de políticas ficam subordinadas à página oficial.** Em contrapartida, testes e esquemas do repositório são fontes dentro do próprio escopo. A localização não define autoridade. O mapa define.

**Um cache nunca substitui uma fonte.** Se um resumo diz sete dias e o requisito aprovado diz trinta, use o requisito para o comportamento desejado. Preserve o resumo conflitante como evidência de desatualização, não como outra regra. Com a autoridade definida, estabeleça o fluxo de escrita.

## Primeiro busque evidências, depois proponha

**Agentes trazem evidências para o contexto da sessão** e então redigem propostas. Eles não aprovam fatos duradouros por conta própria. Editar uma branch de tarefa ou enviar um rascunho não equivale a publicar política, mesclar código ou marcar uma decisão como aceita.

```text
Fonte -> leitura com permissão verificada -> contexto da sessão
Contexto da sessão -> proposta + versão-base -> revisão do responsável
Aprovação do responsável -> publicação controlada -> registro de mudanças
Versão-base alterada -> reconciliar proposta -> revisar novamente
```

**Anexe a versão-base** antes de solicitar revisão. O revisor precisa do valor anterior, do valor proposto, do motivo, das evidências e dos sistemas afetados. A aprovação deve se referir a uma revisão específica da proposta, não a um chat em constante mudança.

```yaml
proposal_id: PROP-042
target: wiki:REQ-17
base_version: 8
change: "Manter exportações por trinta dias, em vez de sete."
evidence:
  - "decision:DEC-12 aceita"
affected_records:
  - "repo:export-service configuração de retenção"
  - "wiki:RUN-04 procedimento de limpeza"
owner_role: product-owner
status: awaiting-review
```

**Os identificadores acima são exemplos.** Registre uma linha no log por mudança lógica aprovada, com ID da proposta, registros-alvo, versões anterior e resultante, aprovador, horário e referência de merge ou publicação. Associe os eventos de auditoria nativos à linha, sem substituí-los.

**As pessoas tomam a decisão.** Um publicador autorizado ou uma automação limitada aplica a revisão aprovada. Restrinja as credenciais de escrita de acordo. Instruções, sozinhas, não separam elaboração e publicação. A mesma distinção vale para recuperação.

## Contexto compartilhado sem RAG

**Um mapa de projeto é o primeiro índice de recuperação.** Mantenha uma página por projeto com IDs de fontes, locais do repositório, chaves do rastreador, escopos de autoridade e responsáveis. Leia o mapa primeiro e depois busque o registro relevante pelo ID. Use pesquisa quando o ID for desconhecido.

### Barra lateral: mapa de projeto de exemplo

```yaml
project: export-service
map_id: MAP-01
policy:
  source_id: POL-01
  approved_version: 3
  owner_role: policy-owner
sources:
  requirements: {page_id: REQ-17, owner_role: product-owner}
  runbook: {page_id: RUN-04, owner_role: operations-owner}
  decisions: {register_id: DEC-REGISTER, owner_role: project-lead}
repository:
  key: export-service
  setup: README.md
  terms: CONTEXT.md
  decisions: docs/adr/
tracker:
  project_key: EXP
  active_task: EXP-42
```

**Conectores diretos reduzem cópias manuais.** O Model Context Protocol (MCP) é um protocolo de integração para expor ferramentas e contexto a aplicativos de IA. Use conectores aprovados para wiki, rastreador e repositório quando disponíveis. Uma busca direcionada limita resultados irrelevantes, mas não substitui autorização nem verificações de atualização. Consulte as orientações de segurança do MCP listadas nas referências ao escolher permissões.

**A recuperação exata exige pouca configuração.** Ela fornece evidências citáveis sem banco vetorial. Seus limites também são claros: alguém mantém o mapa, perguntas amplas exigem pesquisa adicional e páginas grandes consomem espaço da sessão. Busque a seção relevante com as restrições vizinhas em vez de colar um manual inteiro.

**O trabalho offline usa snapshots explícitos.** Registre a revisão exportada e identifique as respostas como baseadas no snapshot. Não publique mudanças até que uma pessoa ou conector autorizado verifique a fonte atual. Em seguida, torne a mesma política visível em cada interface.

## Uma política, adaptadores diferentes

**Mantenha uma política compartilhada** e distribua adaptadores curtos específicos para cada ferramenta. Coloque a versão aprovada da política na primeira linha de cada adaptador ou conjunto de instruções copiado. Inclua o ID da fonte e um snapshot local revisado para sessões sem acesso ao conector.

**O carregamento varia entre ferramentas.** O Codex documenta a descoberta em camadas de **`AGENTS.md`**. Claude Code documenta **`CLAUDE.md`**, importações e memória do projeto. Cline documenta **`.clinerules/`** e controles de regras. Use a documentação oficial das instruções nas referências. Verifique quais instruções são carregadas na versão instalada em vez de presumir que os nomes dos arquivos funcionem igual.

### Barra lateral: cabeçalho de exemplo para AGENTS.md

```markdown
Versão da política: v3 | Fonte: wiki:POL-01 | Estado: aprovada

# Instruções do projeto

Leia o mapa de projeto MAP-01 antes de iniciar uma tarefa.
Carregue docs/policy-snapshot.md e registre a revisão da fonte.
Trate memória de chat e trechos de pesquisa como caches.
Anexe revisões de fontes a cada proposta factual.
Use uma branch de tarefa e um worktree por tarefa de programação.
Não publique políticas, aprove decisões nem mescle seu próprio PR.
Pare diante de conflitos de fontes ou escritas sobrepostas não resolvidos.
Verificações necessárias: testes, revisão da documentação, atualização da política.
Responsáveis: mantenedor de engenharia, responsável de produto, responsável por política.
```

**Instruções de projetos de chat recebem o mesmo cabeçalho e procedimento.** Pessoas não programadoras recebem o snapshot de política e o mapa do projeto por uploads ou conectores aprovados. Se a interface não tiver acesso em tempo real, uma pessoa fornece a exportação versionada e registra a limitação.

**Um rótulo de versão é uma afirmação, não prova de conteúdo idêntico.** Gere adaptadores a partir do snapshot aprovado ou compare as partes da política com um resumo armazenado. Revise exceções específicas do adaptador separadamente. No piloto, confira regras desativadas, substituições aninhadas e instruções pessoais. Depois, registre as evidências usadas em cada tarefa.

## Registre um manifesto de contexto

**Um manifesto de contexto explica as evidências da resposta.** Registre IDs e revisões de páginas, chaves de issues e suas revisões ou horários de atualização, além de IDs completos de commits do repositório. Inclua o horário da recuperação e as seções relevantes. Marque registros indisponíveis em vez de substituí-los por um resumo lembrado.

```yaml
task: EXP-42
policy: {page_id: POL-01, version: 3}
wiki:
  - {page_id: REQ-17, version: 8, section: export-retention}
tracker:
  - {issue_key: EXP-42, revision: 5}
repository:
  commit: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
  files: [README.md, config/retention.yaml]
limits:
  - "Runbook não foi recuperado. Nenhuma mudança no runbook foi proposta."
```

**O valor do commit é sintético.** Em um manifesto real, substitua-o pelo commit inspecionado. Acrescente o horário da recuperação durante a leitura real. Um registro criado antes da inspeção é uma lista de verificação, não evidência.

**Citações ajudam a verificar,** mas não geram confiança automática. Aponte cada afirmação relevante para o registro e a seção que a sustentam. Se duas fontes discordarem, mantenha ambas no manifesto e informe a lacuna não resolvida. Não escolha apenas pelo horário mais recente sem verificar escopo e aprovação. A mesma disciplina vale para recuperação semântica.

## Compartilhe contexto com RAG

**Geração aumentada por recuperação (RAG)** fornece material recuperado ao modelo enquanto ele produz uma resposta. Um índice semântico ajuda a encontrar trechos relevantes mesmo quando a pergunta usa outras palavras. A visão geral de RAG da Microsoft descreve fundamentação, limites de recuperação e requisitos de controle de acesso. Consulte a fonte oficial nas referências.

**Use RAG para encontrar informações em coleções maiores,** como documentação antiga, notas de reunião e transcrições. Identifique classes de documentos e estados de aprovação. Uma transcrição indexada a partir da gravação original é fonte do que foi dito, não autoridade para requisitos aprovados. Não transforme conversa em política por meio da indexação.

| Regra de índice | Comportamento necessário |
|---|---|
| **Ingerir fontes, não caches** | Excluir resumos gerados e cópias locais sem rastreamento |
| **Preservar proveniência** | Armazenar ID da fonte, revisão, seção e estado do documento por trecho |
| **Atualizar quando houver mudança** | Reindexar edições e invalidar trechos obsoletos |
| **Respeitar mudanças de acesso** | Atualizar permissões e remover conteúdo excluído ou revogado |
| **Retornar citações** | Exibir referências dos registros junto do texto recuperado |
| **Verificar o registro ativo** | Buscar evidências atuais antes de propor uma ação importante |

**Neste modelo, um trecho recuperado funciona como ponteiro.** Seu texto ajuda a localizar evidências. A fonte ativa confirma a redação atual, aprovação, exceções ao redor e acesso. Se a recuperação ativa falhar, identifique o snapshot e suspenda a ação relevante. Esta é uma regra de governança, não uma afirmação sobre toda implementação de RAG.

**Embeddings desatualizados e contexto ausente criam riscos diferentes.** Um trecho antigo não contém uma revisão. Um trecho atual ainda pode induzir ao erro se uma exceção estiver na seção seguinte. Preserve os títulos e recupere as restrições adjacentes antes de avaliar um requisito.

**Vazamento de permissões exige teste próprio.** Aplique a autorização antes de devolver trechos ao modelo, não depois de gerar a resposta. Analise conteúdo sensível antes de indexar ou chamar serviços externos de embeddings. Considere cópias em logs, solicitações ao modelo e rastros de recuperação. Escolher um modelo local não torna local um conector remoto. Use essas verificações para decidir se RAG cabe no piloto.

## Escolha mapa, RAG ou ambos

**Associe a recuperação à pergunta.** Um ID de requisito conhecido favorece acesso direto. Uma pergunta aberta sobre materiais históricos dispersos favorece pesquisa. Comece pelo mapa, a menos que a descoberta já seja um problema comprovado.

### Barra lateral: usar RAG ou não?

```text
As tarefas costumam indicar projeto, página, issue ou arquivo?
  Sim -> A recuperação direta basta para o piloto?
           Sim -> SOMENTE MAPA
           Não -> HÍBRIDO: mapa para IDs conhecidos, RAG para descoberta
  Não -> As evidências estão espalhadas por uma grande coleção?
           Não -> SOMENTE MAPA, além da pesquisa nativa
           Sim -> O trabalho é exploratório e somente leitura?
                    Sim -> SOMENTE RAG para descoberta
                    Não -> HÍBRIDO com verificações de fontes ativas

Todas as opções mantêm responsáveis, autorização e proveniência.
A descoberta com RAG ainda verifica fontes antes de ações duradouras.
```

**Somente RAG descreve a interface de recuperação,** não uma permissão para ignorar governança. Use-o para uma coleção exploratória de escopo limitado onde ainda seja possível verificar as fontes diretamente. É uma escolha ruim para mudanças com ID conhecido que exigem conferência precisa de versão.

**O modelo híbrido separa descoberta e verificação.** O mapa atende consultas conhecidas. RAG localiza registros desconhecidos. RAG responde “onde”; a fonte responde “o quê”. No exemplo de retenção, busque diretamente **`REQ-17`**. Para “quais decisões antigas sobre exportação explicam esse limite?”, pesquise o registro e busque cada decisão relevante. Agora aplique a parte do repositório.

## Informações dentro do repositório

**O conhecimento do repositório muda com a implementação.** Mantenha uma estrutura compacta para que agentes e revisores saibam onde procurar.

| Arquivo ou diretório | Responsabilidade |
|---|---|
| **`CONTEXT.md`** | Termos do projeto e links para registros oficiais |
| **`docs/adr/`** | Decisões aceitas de arquitetura do repositório |
| **`docs/design/`** | Descrições aprovadas do comportamento do sistema |
| **`docs/plans/`** | Planos de implementação propostos com estado explícito |
| **`AGENTS.md`** | Etapas de revisão, limites e papéis dos responsáveis |
| **`README.md`** | Configuração e entradas, sem duplicar requisitos |

**Aplique a regra do mesmo PR:** altere código e documentação afetada do repositório juntos. Se uma atualização da base de conhecimento não for necessária, exija uma exceção escrita na descrição do PR ou no local combinado de trailer do commit.

```text
KB-Update: none (motivo: a refatoração interna preserva o comportamento documentado)
```

**O pipeline aplica a declaração.** Uma verificação obrigatória rejeita mudanças de comportamento sem atualização de documentação ou exceção. Um responsável humano pela documentação revisa a exceção. Uma verificação por caminho identifica mudanças candidatas, mas não prova completude semântica. Exija a verificação e a revisão por proteção de branch ou controle equivalente de merge.

**Uma etapa ausente do pipeline não é uma etapa.** Escrever “revisão da documentação” num arquivo de instruções fornece apenas orientação. Teste a aplicação enviando um PR deliberadamente incompleto no piloto e confirmando que o merge fica bloqueado.

**Use uma tarefa, uma branch e um worktree.** A documentação oficial do worktree do Git descreve árvores de trabalho separadas com estado de checkout próprio. Worktrees separados reduzem conflitos locais de edição. Não impedem duas branches de mudar o mesmo arquivo nem dois agentes de atualizar uma única página wiki.

**Nunca faça commit direto na branch padrão,** seja ela **`main`**, **`master`** ou outro nome. Registre diferenças entre requisito e código no rastreador. Anexe os registros conflitantes e deixe os responsáveis definir o comportamento esperado antes de alinhar qualquer lado. Aplique controles equivalentes fora do Git.

## Informações fora do repositório

**A wiki precisa de um padrão documental.** Cada página oficial indica finalidade, estado, responsável, revisão, data de revisão e IDs de fontes relacionadas. Coloque propostas numa área de rascunhos claramente não oficial. Não misture texto proposto numa página de requisitos aprovada.

**Atualizações seguras seguem uma sequência fixa:**

1. **Releia** a página atual e as restrições próximas.
2. **Compare** sua versão com a versão-base da proposta.
3. **Reconcilie** edições intermediárias e obtenha nova aprovação para texto alterado.
4. **Grave** a revisão aprovada com uma condição da versão esperada.
5. **Verifique** a página salva e acrescente a referência do registro de mudanças.

**Reler não elimina disputas de escrita.** Use o mecanismo de atualização condicional do sistema quando houver. Caso contrário, serialize a publicação por meio de um único responsável e verifique o resultado. Pare se outro autor alterar a base durante a revisão.

**A regra de não excluir vale para fluxos de agentes.** Agentes propõem arquivamento ou remoção. Pessoas autorizadas aplicam processos de retenção e exclusão. Não interprete a regra como permissão para manter dados sensíveis indefinidamente.

**Achados no rastreador incluem evidências,** não apenas conclusões. Registre o que observou, o comando ou método exato de inspeção, o commit inspecionado, o comportamento esperado e real e os critérios de aceitação. Remova segredos e saídas sensíveis antes de anexar evidências. Marque comandos sugeridos como não executados até alguém executá-los.

```text
Achado: a implementação de retenção diverge do requisito aprovado
Evidência: REQ-17 v8 e config/retention.yaml inspecionado
Comando de inspeção: git show HEAD:config/retention.yaml
Commit: ID completo do commit inspecionado registrado no manifesto
Aceitação: a duração aprovada corresponde ao código, aos testes e ao runbook
Estado: aguardando revisão dos responsáveis por produto e engenharia
```

**O exemplo é um modelo de achado,** não um resultado medido. Preencha-o após uma inspeção real. Ligue a atualização da wiki à evidência do rastreador por meio do ID da proposta.

**O registro de decisões separa regras e raciocínio.** Armazene pergunta, opções, recomendação, compensações, responsável, estado de aprovação e referência da regra resultante. Agentes propõem. Pessoas decidem. Regras aprovadas vão para políticas e procedimentos. A justificativa fica no registro.

**Recolha fatos duradouros de reuniões e chats.** Envie uma proposta com as evidências de origem e solicite aprovação. Até a publicação, indique que o acordo é provisório. Em seguida, conecte o comportamento aprovado entre o repositório e a wiki.

## Conecte os dois sistemas

**A sincronização pós-merge leva mudanças da implementação para fora.** Crie uma tarefa de atualização da wiki ligada ao commit mesclado, requisito aprovado e runbook afetado. Um agente redige a atualização. O responsável pela wiki verifica a página atual e aprova a publicação. Mantenha a tarefa aberta até verificar a revisão salva.

**A atualização das políticas é uma auditoria separada.** Compare cada adaptador do repositório e cópia de instruções de chat com a versão canônica aprovada. A política **`v3`** está em **`POL-01`**. Cada **`AGENTS.md`** indica **`v3`** na primeira linha. A auditoria sinaliza **`v2`**, rótulos ausentes e divergências de conteúdo, mesmo quando os rótulos coincidem.

| Verificação | Evidência de conclusão |
|---|---|
| **Atualização da política** | Comparação da versão oficial com o resumo do adaptador |
| **Reconciliação de requisitos** | Revisão do requisito comparada ao código e aos testes |
| **Sincronização pós-merge** | Commit mesclado ligado à revisão publicada da wiki |
| **Resolução de conflitos** | Decisão aprovada pelo responsável ligada aos dois registros |

**Reconcilie por agenda ou no momento do PR.** Uma auditoria semanal atende ao piloto. Um PR que muda comportamento exige conferência do requisito antes do merge. Escolha a frequência conforme o custo do desvio e registre a última verificação bem-sucedida.

**A mudança para trinta dias tem vários pontos de controle:** produto aprova o requisito, engenharia atualiza configuração e testes, revisores mesclam o PR e operações publica a atualização do runbook. Uma linha do registro liga os documentos resultantes. Uma sincronização wiki com falha continua visível, em vez de desaparecer atrás de um merge bem-sucedido. Passagens compartilhadas mantêm essa sequência entre ferramentas.

## Um procedimento para cada ferramenta

**Empacote etapas repetidas como skills ou prompts,** com um ID de procedimento versionado. Compartilhe o contrato, não um formato de arquivo universal presumido. Cada adaptador de ferramenta usa o mecanismo de carregamento ou invocação compatível.

| Procedimento | Resultado necessário |
|---|---|
| **Iniciar tarefa** | Responsável, escopo, versão da política, manifesto de fontes, reserva de escrita |
| **Lint de documentação** | Metadados ausentes, autoridade duplicada, referências quebradas |
| **Verificação de conhecimento** | Diferenças entre requisito e código com revisões de apoio |
| **Transferência** | Evidências atuais, propostas, verificações concluídas, questões pendentes |

**Não programadores trabalham sem Git.** Eles recuperam fontes permitidas em projetos de chat, preenchem o mesmo modelo de proposta e enviam ao responsável por uma página de rascunho ou tarefa no rastreador. Não precisam de checkout do repositório para solicitar correção de requisito.

**Programadores usam arquivos do repositório e etapas de PR.** Eles ligam a proposta aprovada no PR, registram commits inspecionados e executam as verificações obrigatórias. Ambos os grupos transferem a mesma estrutura de evidências.

```yaml
handoff:
  task: EXP-42
  policy_version: 3
  manifest: "IDs e revisões de fontes, além do commit inspecionado, anexados"
  completed: [requirement-review]
  proposals: [PROP-042]
  pending: [implementation-review, runbook-publication]
  reservations: ["publicação de RUN-04 atribuída ao responsável de operações"]
  unresolved: []
  next_owner_role: engineering-maintainer
```

**Uma transferência ainda é um cache.** A próxima pessoa relê as fontes antes de agir e registra novas revisões. Não aceite “concluído” como prova sem conferir a aprovação ou evidência de teste vinculada. Aplique as proteções abaixo antes de qualquer escrita.

## Proteções antes de cada escrita

**Analise os dados antes que saiam do sistema de origem.** Verifique classificação, permissões do conector, destinos aprovados, tratamento do provedor do modelo e registros. Envie o mínimo de conteúdo relevante. Mantenha registros restritos fora de projetos de chat e serviços de embeddings não autorizados.

**Texto recuperado é evidência, não um canal de instrução.** Uma página wiki ou resposta de ferramenta pedindo que o agente ignore a política não muda sua autoridade. Revise instruções originadas no conteúdo separadamente da política operacional aprovada. Durante a recuperação, limite conectores a somente leitura e separe credenciais de publicação do acesso à sessão.

**Atribua um responsável ativo por página ou arquivo.** Registre a reserva no rastreador com escopo e prazo. Releia antes de escrever e use verificações de versão. Worktrees separados ajudam no isolamento local; reservas e escritas condicionais tratam registros compartilhados.

| Gatilho para parar e perguntar | Resposta necessária |
|---|---|
| **Fontes divergem sem responsável** | Pause e solicite a atribuição de autoridade |
| **Outra tarefa reservou o destino** | Combine a responsabilidade antes de editar |
| **Versão-base mudou** | Reconcilie e solicite nova aprovação |
| **Uma afirmação relevante não tem evidências** | Marque como não verificada e solicite uma fonte |
| **Tratamento de dados não está claro** | Mantenha o conteúdo no sistema de origem |
| **Acesso à fonte ativa falha** | Registre limites do snapshot e suspenda a ação duradoura |

**Prompts não são controles de segurança.** Teste a negação de permissões, branches protegidas, rejeição de bases desatualizadas e propriedade de escrita fora do modelo. Uma demonstração obediente não basta se a conta ainda tem direitos irrestritos de publicação. Use os testes para decidir se o piloto está pronto.

## Faça um piloto antes de promover

**Comece o modelo como rascunho.** Teste um projeto com programador, não programador e responsáveis nomeados pelas fontes. Faça a mesma pergunta com ID conhecido em duas ferramentas e depois simule um conflito deliberado de fontes. Revise manifestos e propostas, em vez de avaliar fluência do texto.

**Raciocínio esperado:** ambos identificam o requisito aprovado atual e descrevem separadamente a implementação inspecionada. Se discordarem, compare primeiro os manifestos. Este é um exercício proposto, não um benchmark observado.

| Métrica | Definição |
|---|---|
| **Taxa de citações** | Afirmações relevantes apoiadas por fontes ÷ afirmações factuais relevantes nas amostras |
| **Achados semanais de desvio** | Divergências confirmadas de autoridade ou versão, por tipo de fonte |
| **Tempo de proposta** | Tempo mediano entre proposta pronta para revisão e decisão registrada |
| **Retrabalho por contexto antigo** | Tarefas reabertas por evidência obsoleta ou não verificada |

**Meça uma linha de base antes de definir metas.** Mais achados de desvio na primeira semana podem significar detecção melhor, não documentação pior. Acompanhe recorrência e tempo de resolução junto da contagem bruta. Revise evidências sensíveis sem copiá-las para exportações analíticas.

**Entregue um repositório de exemplo durante a implantação.** Inclua mapa sintético, adaptadores de política, manifestos, modelos de proposta, exceções de documentação e verificações de revisão executáveis. Use registros fictícios de wiki e rastreador, sem credenciais de produção. Demonstre publicação negada, rejeição de base alterada, desvio de versão da política e transferência bem-sucedida.

**Um repositório de modelos é uma entrega da implantação,** não um recurso fornecido com este artigo. Promova o modelo operacional depois que a liderança e responsáveis pelas fontes revisarem o piloto. Mantenha exceções e falhas não resolvidas no registro de decisões. Antes da promoção, corrija as falhas previsíveis abaixo.

## Solução de problemas de contexto compartilhado

| Sintoma | Primeiro reparo |
|---|---|
| **Duas ferramentas respondem de forma diferente** | Compare IDs das fontes, revisões, escopo e estado de aprovação |
| **Instruções parecem atuais, mas o comportamento diverge** | Inspecione adaptadores carregados, controles de regras e substituições locais |
| **RAG retorna requisitos antigos** | Inspecione a atualização do índice e busque a página ativa |
| **Uma edição wiki apaga outra mudança** | Exija escritas condicionais ou publicação serializada |
| **Verificações de documentos passam com texto antigo** | Inclua revisão do responsável e conferência de requisitos |
| **Decisões ficam no chat** | Atribua entrada de propostas e responsabilidade pelo registro |

**Corrija o caminho das evidências antes de reescrever o prompt.** Execute novamente o caso piloto com falha e registre o resultado. Use a lista abaixo para tornar o processo reparado uma prática semanal.

## Dez etapas para esta semana

1. **Escolha um projeto piloto** e as pessoas e ferramentas participantes.
2. **Atribua uma fonte e um responsável** a cada tipo de informação.
3. **Publique um mapa de projeto** com IDs e escopos de autoridade.
4. **Redija uma política compartilhada** e obtenha revisão do responsável.
5. **Versione cada adaptador na primeira linha** e verifique se carrega.
6. **Exija um manifesto de contexto** para respostas e propostas factuais importantes.
7. **Crie uma entrada para propostas** com versões-base e aprovadores nomeados.
8. **Aplique controles de escrita** e a regra documental do mesmo PR.
9. **Teste desvio, conflito e transferência** com registros sintéticos.
10. **Revise as métricas do piloto** e aprove a próxima etapa.

**Dê uma fonte a cada fato, faça cada ferramenta ler essa fonte e encaminhe cada mudança duradoura por uma pessoa.**

## Referências e próximos passos

**A documentação oficial dá suporte aos componentes técnicos,** não às regras organizacionais do modelo. Confira o comportamento das ferramentas instaladas e as permissões dos conectores durante o piloto.

- **Instruções do Codex:** [Instruções personalizadas com AGENTS.md](https://developers.openai.com/codex/guides/agents-md), sobre descoberta e verificação de instruções.
- **Instruções do Claude Code:** [Como Claude lembra do seu projeto](https://code.claude.com/docs/en/memory), sobre instruções e memória do projeto.
- **Instruções do Cline:** [Regras](https://docs.cline.bot/customization/cline-rules), sobre regras do workspace e controles de ativação.
- **Projeto de recuperação:** [Geração aumentada por recuperação no Azure AI Search](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview), sobre fundamentação, limites de recuperação e segurança.
- **Segurança de conectores:** [Boas práticas de segurança do MCP](https://modelcontextprotocol.io/docs/latest/tutorials/security/security_best_practices), sobre autorização e riscos de conectores.
- **Isolamento de worktrees:** [Documentação de worktree do Git](https://git-scm.com/docs/git-worktree), sobre árvores de trabalho e estado compartilhado do repositório.

**Para planejar inferência local,** leia o [Guia de contexto de GPU para IA local](/articles/local-ai-model-gpu-context-guide/). Capacidade de hardware e governança de fontes compartilhadas resolvem problemas diferentes. Uma janela de contexto maior não corrige autoridades conflitantes.

{{< centerbutton href="/articles/local-ai-model-gpu-context-guide/" >}}
  Leia o Guia de contexto de GPU para IA local
{{< /centerbutton >}}

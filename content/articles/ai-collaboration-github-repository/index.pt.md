---
title: "Colaboração com IA no GitHub: limites do repositório e da revisão"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Crie um mapa de fontes, defina a responsabilidade pelos arquivos e proteja o limite de publicação de contribuições de IA revisadas."
genre: ["Inteligência artificial", "Colaboração em equipe", "Engenharia de software"]
tags: ["curso de colaboração em IA", "repositório GitHub", "proteção de branches", "CODEOWNERS", "mapa de fontes", "revisão de pull request", "controles de publicação"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "Ilustração de profissionais revisando juntos o trabalho de um projeto em um espaço de cibersegurança"
coverCaption: ""
---
[Voltar ao curso de colaboração em IA](/ai-collaboration-course-start/)

**Após a aprovação do estatuto, o mantenedor cria o limite de publicação com prioridade para GitHub.** Requisitos, configuração, política e runbooks ficam em um único repositório descartável. Colaboradores propõem mudanças por Issues e pull requests. Você define onde ficam os fatos aprovados e bloqueia mudanças não revisadas antes de conectar agentes.

## Pontos principais

- **`main` protegida** é o limite de publicação.
- **Issues** coletam propostas, mas não aprovam políticas.
- **CODEOWNERS** atribui revisores qualificados aos arquivos.
- **Usuários separados** demonstram os controles de revisão e recusa.

## Antes de começar

**Pré-requisitos:** a [base do piloto](/articles/ai-collaboration-pilot-foundation/), laboratório extraído, administrador do repositório e revisores separados de produto e operações. **Tempo estimado:** 60 minutos. **Dificuldade:** moderada.

**Limite do plano:** o GitHub documenta branches protegidas para repositórios públicos no plano Free e repositórios privados nos planos Pro, Team ou Enterprise. Use apenas conteúdo sintético em repositórios públicos. Verifique a visibilidade e o plano na referência de branches protegidas antes de confiar na aplicação das regras.

**Resultado esperado:** você termina com uma branch de publicação protegida, responsáveis pelos arquivos, um mapa de fontes e um teste de recusa registrado como evidência.

## Crie o repositório

1. **Crie `export-service-lab`** com um README e a branch padrão **`main`**.
2. **Copie o laboratório extraído** para a raiz do repositório, preservando **`check.py`**, **`test_check.py`** e **`baseline/`**. Copie os arquivos de registro da linha de base para a raiz como registros iniciais.
3. **Crie `docs/project-map.md`** usando o registro da base do piloto. Adicione **`docs/policy.md`** com o POL-01 aprovado.
4. **Crie `docs/decisions/DEC-12.md`** com a aprovação do estatuto, papéis, decisão de linha de base e status.
5. **Faça o commit inicial como administrador.** Registre essa exceção inicial. Ative a proteção antes das próximas contribuições.

**Configuração local com Git Bash, Terminal do macOS ou shell Linux:** entre no GitHub pelo navegador, abra o novo repositório, selecione **Code** e copie a URL HTTPS de clone. Em um diretório de trabalho descartável, execute os comandos abaixo. Substitua os dois caminhos de exemplo pela URL e pelo caminho do ZIP baixado do laboratório. Não insira um token na URL.

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

O comando clone deve criar o diretório do repositório. Se `unzip` não estiver disponível, extraia o ZIP pelo gerenciador de arquivos e copie o conteúdo para este checkout, preservando o README do repositório. `git status --short` deve listar os registros copiados, o checker, os testes e `baseline/` como arquivos novos. Salve `docs/project-map.md`, `docs/policy.md` e `docs/decisions/DEC-12.md` do pacote do piloto com um editor de texto. Depois execute:

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

O Git deve informar um novo ID de commit e, em seguida, um push bem-sucedido para `main`. O status curto final deve estar vazio. Abra o repositório GitHub em uma nova visualização do navegador e confirme que os arquivos e o ID do commit aparecem em `main`. Salve a URL do commit como evidência da configuração inicial. Se o Git solicitar a identidade do autor, siga as instruções de configuração no hub do curso. Se a autenticação falhar, use o fluxo de credenciais compatível com o GitHub e repita o mesmo push. Se a branch ou o remoto estiver incorreto, pare e verifique `git branch --show-current` e `git remote -v` antes de outra gravação. Se o push for rejeitado porque a proteção já estava ativada, abra uma branch de proposta e um PR em vez de contornar a regra. O caminho somente pelo navegador abaixo continua disponível por meio de um mantenedor.

| Registro | Localização | Responsável |
|---|---|---|
| **POL-01** | `policy.json`, `docs/policy.md` | Responsável pela política |
| **REQ-17** | `requirement.json` | Responsável pelo produto |
| **RUN-04** | `runbook.md` | Responsável por operações |
| **Comportamento** | `config.json` | Mantenedor do repositório |
| **Decisões** | `docs/decisions/` | Líder do projeto |

**O mapa indica as localizações, sem copiar os valores.** Mantenha o README focado na configuração e no mapa. Repetir requisitos de retenção cria deriva até mesmo dentro de um repositório.

## Atribua responsáveis pelos arquivos

**Gere `.github/CODEOWNERS`** localmente com os identificadores reais da sandbox. Insira os identificadores sem o **`@`** inicial. Mantenha as identidades das contas no laboratório privado, não em evidências públicas do exercício.

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**Os responsáveis precisam de acesso de gravação** para que o GitHub os reconheça. Inspecione o arquivo CODEOWNERS no navegador em busca de erros. Proteja os arquivos de responsabilidade e as definições de workflow junto com o conteúdo comum.

**Vários nomes na mesma linha não exigem aprovação de todos os responsáveis listados.** O GitHub aceita a aprovação de um responsável qualificado para o caminho correspondente. Use responsáveis diferentes para os caminhos de requisitos e runbooks. O piloto também exige declarações dos responsáveis por produto e operações associadas à proposta final.

## Proteja a publicação

1. **Abra Settings, Branches** e adicione uma regra de proteção para a branch **`main`**. Use esse mecanismo de forma consistente no exercício, sem misturá-lo com rulesets.
2. **Exija um pull request,** duas aprovações e revisão dos code owners.
3. **Descarte aprovações desatualizadas** após novos commits e exija a resolução das conversas.
4. **Ative a opção para não permitir contornar as configurações acima.** Mantenha desativados force push e exclusão.
5. **Adicione a verificação de consistência** depois da primeira execução no próximo módulo. Exija que as branches estejam atualizadas antes do merge.

**Duas aprovações impõem uma quantidade, não a participação de papéis de negócio.** CODEOWNERS adiciona cobertura de responsáveis por caminho. O mantenedor também verifica as declarações dos dois papéis. Registre esse controle procedimental explicitamente em vez de descrevê-lo como aplicação automática de dois papéis.

**Administradores continuam gerenciando a configuração.** Capture a regra antes e depois dos testes. Não conceda acesso de administrador a um agente nem use um token privilegiado para demonstrar a recusa de um colaborador.

## Verifique o limite

| Tentativa | Resultado esperado |
|---|---|
| **Colaborador envia uma branch** | Proposta permitida |
| **Colaborador publica diretamente** | Publicação protegida recusada |
| **Uma pessoa revisora aprova** | Merge bloqueado pelo limite de revisões |
| **Novo commit depois da revisão** | Nova aprovação necessária |
| **Arquivo sensível sem responsável** | Corrigir antes da publicação |

**Use a sessão de navegador do colaborador para inspecionar o caminho.** O editor web do GitHub não edita a branch protegida **`main`**. Uma solicitação para criar uma branch mostra o caminho compatível pelo navegador. Ela não prova que o servidor recusou um push direto. Para evidências de recusa da plataforma, peça a um colaborador com acesso local Git aprovado que tente um push direto inofensivo para a **`main`** protegida e guarde a resposta do servidor. Marque esse teste como bloqueado quando o acesso local não estiver disponível.

**Leia `main` após a recusa** e confirme que a revisão não mudou. Registre o papel do ator, a ação tentada, o resultado e a revisão da fonte. A promessa do assistente de não publicar é evidência comportamental, não um teste de permissão da plataforma.

**Use o clone local autenticado do próprio colaborador no teste de push direto.** Um token do mantenedor testaria a identidade errada. Esta resposta ilustrativa mostra o tipo de evidência do servidor a preservar. O texto exato varia conforme as regras do repositório.

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**Se a autenticação Git local não estiver disponível, marque como bloqueada a recusa no servidor.** Guarde o aviso do navegador sobre criar uma branch como evidência do caminho e peça ao mantenedor que organize um teste separado de colaborador. Não pontue o aviso de rota como um push direto recusado.

## Crie um mapa de fontes útil

**Um mapa de fontes é um documento de navegação**, não um segundo documento de requisitos. Quem chega do chat precisa encontrar a intenção atual, o comportamento implementado e as instruções operacionais sem escolher entre resumos conflitantes.

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**Não coloque o valor atual de retenção em cada entrada do mapa.** Um mapa com “sete dias” vira mais um valor a sincronizar após PROP-042. Mantenha identificadores estáveis e localizações no mapa e leia o valor no registro oficial.

**Proteja as mudanças do mapa como mudanças de roteamento.** Redirecionar REQ-17 para um arquivo de rascunho altera a seleção da fonte mesmo que o requisito aprovado permaneça intacto. Revise o destino, o responsável e o escopo da autoridade sempre que o mapa mudar.

## Separe a base e o candidato

**A raiz do repositório contém os registros ativos do laboratório.** O diretório baixado **`baseline/`** é um exemplo didático. Ele não se torna automaticamente a base protegida de cada PR futuro. Depois que o trabalho revisado chega a **`main`**, os registros protegidos da raiz definem a base da próxima proposta.

| Localização | Finalidade | Editar durante PROP-042? |
|---|---|---|
| **Requisito/configuração/runbook da raiz** | Registros ativos propostos na branch | Sim, por mudanças revisadas |
| **`baseline/`** | Exemplo original do exercício offline | Não |
| **Worktree confiável separado** | Registros protegidos da raiz capturados | Não |
| **`context.json`** | Evidência dos bytes da base capturada | Gerar novamente após reconciliação |

**Mantenha as mudanças de controle separadas das mudanças de retenção.** Primeiro configure o checker e as regras de revisão. Depois proponha a alteração de sete para trinta dias. Combinar mudanças de política, workflow e valor dificulta distinguir controles corrigidos de controles contornados.

## Revise a mudança completa

**Abra Files changed antes de aceitar a descrição de um PR.** A descrição explica a intenção do autor. O diff mostra a mudança enviada. Em PROP-042, inspecione a revisão do requisito, as exclusões de escopo, a configuração, o runbook, a base da proposta e as evidências do manifesto.

1. **Revisão do produto:** confirme a intenção de trinta dias e as exclusões inalteradas.
2. **Revisão de operações:** confirme que o runbook corresponde à configuração proposta e preserva a limitação de execução.
3. **Revisão do mantenedor:** inspecione JSON, captura da fonte, resultados das verificações e edições não relacionadas.
4. **Revisão de controle:** inspecione separadamente qualquer mudança no mapa, política, CODEOWNERS ou workflow.

**Uma verificação verde não explica uma exclusão não relacionada.** Se a branch remove o documento de política ao mudar a retenção, solicite uma proposta separada ou uma revisão específica do responsável. Limitar o escopo mantém o objeto de revisão compreensível.

## Diagnostique um teste de recusa

**Use uma ação tentada por linha de evidência.** “O colaborador falhou” é ambíguo. A pessoa pode não ter acesso normal de gravação, encontrar uma limitação do navegador ou atingir a regra de branch pretendida. Essas observações demonstram limites diferentes.

| Observação | Interpretação | Acompanhamento |
|---|---|---|
| **Não consegue criar nenhuma branch** | Acesso de contribuição ausente | Usar um caminho aprovado por Issue ou fork |
| **Cria branch, não publica em main** | O caminho de publicação testado está restrito | Registrar a revisão inalterada de main |
| **Merge bloqueado com uma revisão** | O limite de revisão se aplica ao PR testado | Adicionar evidência específica do papel |
| **Administrador publica apesar da regra** | A identidade testada contorna o limite | Inspecionar configurações de bypass e permissões |

**Registre papel e ação sem expor detalhes da conta** nas evidências compartilhadas do curso. Mantenha os registros nativos do ator em privado para o revisor. Capture juntos a configuração da regra, a operação tentada, a recusa e a revisão protegida resultante.

## Verificação de conclusão do repositório

**Entregue um repositório que outro colaborador consiga navegar sem ajuda.** O README aponta para o mapa, o mapa resolve os registros oficiais, a cobertura de responsáveis inclui caminhos sensíveis e a proteção vale para **`main`**. Preserve uma proposta permitida e uma tentativa de publicação recusada.

**Não declare aplicação efetiva apenas pelas configurações.** As configurações estabelecem a intenção. A tentativa na sandbox mostra o comportamento observado para um papel e caminho específicos. Leve as duas evidências para a aula sobre agentes e GitHub Actions.

## Solução de problemas e reversão

**Solicitação de responsável ausente:** confirme o acesso de gravação e a cobertura do caminho da branch base. **Proteção ausente:** verifique o plano e a visibilidade. **Merge continua permitido:** inspecione o alvo da regra, o bypass e o número de revisões.

**Reversão:** feche propostas não mescladas e desative a automação do laboratório. Reverta o conteúdo de laboratório mesclado por outro PR revisado. Preserve as evidências antes de excluir o repositório descartável. Não enfraqueça a proteção para concluir um teste com falha.

## Exercício e autoavaliação

**Como colaborador, proponha uma edição de `docs/policy.md`.** Decida se a aprovação do mantenedor, sozinha, comprova a aprovação do responsável pela política.

**Raciocínio esperado:** a quantidade de revisões não estabelece autoridade. O caminho exige cobertura do responsável pela política e revisão atual do papel. Liste como controles procedimentais os requisitos específicos de papel que não são aplicados automaticamente.

## Referências principais

- **Controles de plano e revisão:** [Branches protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).
- **Elegibilidade dos responsáveis:** [Code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
- **Contribuição pelo navegador:** [Edição de arquivos](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

## Próximas etapas

**Continue com [Adaptadores de agentes e GitHub Actions](/articles/ai-collaboration-github-agents-actions/)** para conectar evidências de fontes a verificações executáveis.

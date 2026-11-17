---
title: "Configuração do curso de fluxo de trabalho com IA: terminal, Git e laboratório prático"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Prepare um espaço seguro para praticar com IA, aprenda os termos de terminal e Git usados no curso e execute o laboratório inicial."
genre: ["Inteligência artificial", "Engenharia de software", "Educação"]
tags: ["configuração de curso de IA", "noções de terminal", "noções de Git", "pré-requisitos de agente de programação", "laboratório prático de IA", "curso de IA para iniciantes"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "Espaço de prática para iniciantes com símbolos de terminal, Python e Git, pasta do laboratório marcada e arquivo para restauração"
coverCaption: ""
---

[Voltar ao curso prático de fluxo de trabalho com IA](/effective-ai-course-start/)

**Prepare um espaço seguro antes de usar um agente.** As lições 1 e 2 funcionam no navegador sem este laboratório. Volte aqui antes da lição 3 se quiser fazer o curso completo. As aulas práticas de programação usam Git, Python 3.10 ou posterior e um agente de programação. O percurso de estudo substitui ações indisponíveis do agente por tarefas manuais identificadas.

**Resultado de aprendizagem:** você executará o laboratório inicial, salvará uma base local e explicará como restaurar uma cópia descartável.

## Principais pontos

- **Percurso no navegador:** faça os exercícios de conversa, planejamento, verificação de fontes e revisão no ChatGPT ou Claude.
- **Percurso local:** use um terminal e o laboratório Python fornecido nas atividades de programação.
- **Percurso de restauração:** extraia uma nova cópia do laboratório quando um exercício der errado.
- **Regra de segurança:** mantenha arquivos privados, registros de clientes e credenciais fora do laboratório.

## Escolha seu percurso

| Percurso | Requisitos | Prática |
|---|---|---|
| **Introdução no navegador** | Navegador atualizado e uma conta ChatGPT ou Claude | Lições 1 e 2 e o conjunto de tarefas de conversa da lição 1 |
| **Prática local** | Git, Python 3.10 ou posterior, terminal e um agente de programação | Arquivos, diferenças, testes e edições do agente |
| **Curso de estudo** | Navegador, Python 3.10 ou posterior local e Git | Todas as verificações do laboratório; etapas indisponíveis de agente e MCP são marcadas como não executadas |

**Cada produto define seus próprios planos e limites.** Consulte [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) e [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) antes de depender de um recurso. O percurso de estudo não comprova habilidade prática com um agente de programação indisponível. Registre essa diferença nas notas de conclusão.

**Siga um caminho padrão:** use o ChatGPT no navegador para os exercícios de conversa e depois um agente de programação disponível com o laboratório local. Claude é uma alternativa equivalente para conversa. Codex CLI, Claude Code CLI e OpenCode são opções para a etapa de programação. Você não precisa de contas de todos os fornecedores.

**Registre cinco verificações preliminares antes de abrir um agente de programação.** Isso separa uma verificação do laboratório local de uma afirmação sobre uma conta ou espaço hospedado.

| Verificação | Registre |
|---|---|
| **Espaço de trabalho** | Pasta exata do laboratório extraído que o agente vai ler |
| **Execução** | Computador local ou espaço remoto selecionado |
| **Provedor** | Conta ou provedor do modelo usado nesta tarefa |
| **Permissões** | Se gravações de arquivos e comandos de shell são permitidos ou exigem aprovação |
| **Base** | Contagem observada e dois testes aprovados antes das edições |

**Mantenha a raiz de prática restrita.** Um espaço hospedado precisa de sua própria cópia do laboratório sintético. Uma execução local não prova que a cópia remota ou a conta tenha os mesmos arquivos e permissões.

## Aprenda os termos locais

| Termo | Significado simples |
|---|---|
| **Terminal** | Aplicativo em que você digita comandos |
| **Shell** | Software que interpreta esses comandos |
| **CLI** | Interface de linha de comando de um programa |
| **Diretório de trabalho** | Pasta usada por padrão por um comando |
| **Repositório** | Projeto acompanhado pelo Git |
| **Commit** | Registro salvo do estado do Git |
| **Branch** | Linha nomeada de alterações do Git |
| **Diff** | Exibição de linhas adicionadas ou removidas |
| **Teste** | Verificação repetível do comportamento esperado |
| **Código de saída** | Número que informa sucesso ou falha do comando |

**Você não precisa do GitHub para o laboratório inicial.** Git funciona no computador. GitHub é um serviço de hospedagem separado. Um commit local registra um estado sem enviar seus arquivos a lugar nenhum.

## Prepare o laboratório

**Baixe o [laboratório inicial do curso](/downloads/effective-ai-course-lab.zip)** e extraia-o para uma nova pasta sob seu controle. Abra um terminal nessa pasta. No macOS ou Linux, abra Terminal e use `cd` para entrar no diretório extraído. No Windows, use PowerShell ou Windows Terminal e `cd`. No Windows, o comando Python costuma ser `py -3` em vez de `python3`.

**Instale [Python 3.10 ou posterior](https://www.python.org/downloads/) e [Git](https://git-scm.com/downloads), se necessário.** Verifique as ferramentas instaladas antes de executar o laboratório. Os dois primeiros comandos exibem versões. `cd` altera o diretório de trabalho. `ls` lista arquivos. Substitua o caminho de exemplo pelo caminho real da pasta extraída.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**No Windows PowerShell,** use `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab` e `Get-ChildItem`. A lista deve incluir `task_report.py`, `tasks.json`, `tests` e `docs`. Se um comando de versão falhar, conclua a instalação antes de continuar.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**No Windows PowerShell,** troque `pwd` por `Get-Location`, se preferir, e `python3` por `py -3` quando Python usar o launcher. O primeiro comando exibe o caminho, que deve terminar na pasta extraída do laboratório. Confira também os nomes dos arquivos. Um arquivo chamado `AGENTS.md.txt` não substitui `AGENTS.md`. No Explorador de Arquivos, habilite as extensões para ver o nome completo.

**Resultado esperado:** o relatório diz `Total tasks: 4`. O comando de teste mostra dois testes e termina com `OK`. Um shell retorna o código zero após o sucesso. Uma contagem diferente ou um traceback indica que você deve conferir a pasta e a instalação do Python.

**Leia cada comando por partes.** Em `python3 task_report.py tasks.json`, `python3` inicia Python, `task_report.py` é o programa e `tasks.json` nomeia os dados de entrada. A contagem impressa é a saída, não outro comando. Após uma falha, macOS e Linux mostram o status com `echo $?`. PowerShell expõe o status do último programa nativo por `$LASTEXITCODE`.

**Reserve cerca de dez minutos para a primeira execução** depois de instalar Python: extraia o laboratório, execute o relatório e compare o total com as quatro entradas em `tasks.json`. Abra o JSON em um editor de texto e conte as entradas.

## Pratique Git com segurança

**Inicie Git somente na pasta extraída do laboratório.** Estes comandos criam um registro local. `git status` mostra arquivos alterados. `git diff` mostra as linhas alteradas depois da edição de um arquivo acompanhado.

```bash
git init
git add .
git commit -m "Base do laboratório do curso"
git status --short
```

**Estado esperado:** nenhum nome de arquivo aparece após o commit. Se Git pedir nome e e-mail, configure uma identidade exclusiva do laboratório nesta pasta e repita o commit. Substitua os valores de exemplo por valores privados. Não cole dados de identidade ou credenciais em um chat público.

```bash
git config --local user.name "Aluno do curso"
git config --local user.email "learner@example.invalid"
git commit -m "Base do laboratório do curso"
git status --short
```

**A restauração não exige comandos Git.** Salve as notas fora do laboratório, apague a cópia extraída e extraia novamente o ZIP original. Use esse método quando uma edição deixar o programa em estado desconhecido.

## Proteja seu espaço de prática

**Use exemplos sintéticos.** Não envie documentos privados a um projeto do curso. Não coloque chaves de API em prompts, arquivos de origem, capturas de tela ou commits. O acesso do agente a arquivos e comandos depende das permissões e da pasta aberta. Confira ambos antes de permitir sua execução.

**Verifique o compartilhamento antes de enviar arquivos.** Membros do projeto podem ter acesso aos arquivos. Siga a política da organização no trabalho real. O curso usa dados fictícios, portanto o laboratório não exige aprovação especial.

## Pratique e confira

**Seu resultado:** registre o percurso escolhido, os cinco campos preliminares, a contagem do relatório, o resultado dos testes e o método de restauração. Use uma cópia nova para confirmar que sabe restaurar o laboratório.

**Raciocínio esperado:** você sabe qual pasta os comandos afetam, distingue Git local de hospedagem e tem uma forma de recuperação antes que um agente edite arquivos.

## Verifique o que aprendeu

1. **Pergunta:** Uma introdução feita somente no navegador conclui o percurso do laboratório local? **Resposta:** Não. O percurso completo exige uma base local de Python e Git.

2. **Pergunta:** O que deve ser salvo antes de alterar o laboratório descartável? **Resposta:** O resultado aprovado do teste inicial e um ponto limpo de restauração.

## Solução de problemas

- **Comando Python ausente:** instale Python 3 pelo distribuidor oficial e reabra o terminal.
- **Arquivo não encontrado:** confira o diretório de trabalho e liste os arquivos da pasta extraída.
- **Os testes não executam:** use exatamente o comando no README do laboratório extraído.
- **Git pede identidade para o commit:** configure Git localmente e mantenha os valores escolhidos fora das notas do curso.

## Próximos passos

**Continue com o [fluxo de trabalho confiável com IA](/articles/effective-ai-workflow-foundations/)**. O primeiro exercício usa a mesma oficina sintética antes de qualquer ferramenta receber arquivos reais.

**Navegação do curso:** [Visão geral do curso](/effective-ai-course-start/).

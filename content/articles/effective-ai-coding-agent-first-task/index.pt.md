---
title: "Execute sua primeira tarefa de repositório com um agente de programação"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Escolha uma interface de agente de programação, abra um repositório de exemplo, revise uma alteração proposta e execute verificações antes de mantê-la."
genre: ["Inteligência artificial", "Engenharia de software"]
tags: ["tutorial do Codex CLI", "aplicativo Codex", "Claude Code CLI", "tutorial do OpenCode", "fluxo de trabalho de agente de programação", "ferramentas de programação com IA"]
cover: "/img/cover/effective-ai-coding-agent-first-task.webp"
coverAlt: "Um repositório de código com visualizações distintas do agente no terminal e no desktop ao lado de um diff revisado"
coverCaption: ""
---

[Voltar ao curso Fluxo de Trabalho Prático com IA](/effective-ai-course-start/)

**Um agente de programação lê arquivos, propõe edições e executa ferramentas em um espaço de trabalho.** Nesta lição, você fará uma pequena tarefa em um repositório. Escolha Codex no aplicativo para desktop ou CLI do ChatGPT, Claude Code CLI ou OpenCode TUI. Revise uma alteração antes de aceitá-la.

**Objetivo de aprendizagem:** execute ou aplique manualmente uma edição delimitada e verifique seu diff e comportamento.

## Principais conclusões

- **Codex no aplicativo para desktop do ChatGPT** oferece um espaço visual para tarefas e revisão.
- **Codex CLI** inicia uma sessão Codex no terminal.
- **Claude Code CLI** executa o fluxo de programação do Claude no terminal.
- **OpenCode TUI** oferece programação em terminal com provedores e permissões configuráveis.
- **Um diff e o resultado de um teste** importam mais do que a mensagem de conclusão do assistente.

## Antes de começar

**Pré-requisitos:** conclua a [configuração do curso](/articles/effective-ai-course-setup/), incluindo a execução inicial e o snapshot Git local. Conclua [contexto do repositório](/articles/effective-ai-agents-md-context/) e [pacotes de tarefas](/articles/effective-ai-task-packets/) antes desta lição. Use um agente de programação ao qual você tenha autorização de acesso. Reserve 45 minutos. O nível vai de iniciante a intermediário.

**Use o [laboratório inicial do curso](/downloads/effective-ai-course-lab.zip)** em uma pasta descartável. O arquivo contém um pequeno programa de relatório de tarefas, dados de amostra e testes. Não use um repositório de produção na primeira edição. Adicione um filtro `--status` e mantenha a contagem total existente.

## Rota de estudo sem agente

**Peça a um assistente de chat que proponha a mesma alteração** se um agente não estiver disponível. Cole somente `docs/requirements.md`, `task_report.py` e o teste específico do laboratório sintético. Peça um diff unificado e uma breve explicação. O diff marca linhas antigas com `-` e novas com `+`. Abra o arquivo indicado em um editor, substitua as linhas antigas pela proposta e salve. Execute todos os comandos em Revisar o resultado. Mantenha `tasks.json` inalterado e registre que não executou a etapa com agente. O projeto final contém outra função JSON. Compare o filtro com o requisito e os controles da lição 5.

## Escolha uma interface

**Escolha primeiro uma superfície de revisão.** Codex no aplicativo desktop do ChatGPT serve para projetos visuais e revisão de diffs. Use uma interface de terminal para trabalhar na pasta extraída do laboratório. Compare as opções de terminal:

| Ferramenta de terminal | Verificação da conta ou provedor | Comando inicial |
|---|---|---|
| **Codex CLI** | Confirme o login no Codex e as permissões locais | `codex` |
| **Claude Code CLI** | Confirme o acesso ao Claude Code e as permissões locais | `claude` |
| **OpenCode TUI** | Configure um provedor de modelos compatível e as permissões | `opencode` |

**Instale e entre na conta pelo guia oficial atualizado** da ferramenta. Leia [Codex CLI](https://learn.chatgpt.com/docs/codex/cli), [aplicativo ChatGPT para desktop](https://learn.chatgpt.com/docs/app), [Claude Code](https://code.claude.com/docs/en/overview) ou [OpenCode](https://opencode.ai/docs/). Comandos, plataformas e requisitos de conta mudam. Esta lição usa nomes de inicialização estáveis e um procedimento comum de revisão.

**Para escolher o produto,** leia a comparação de [agentes de programação CLI](/articles/cli-coding-agents-comparison/) ou de [agentes com interface gráfica](/articles/gui-coding-agents-comparison/). Os guias de [Codex CLI e desktop](/articles/codex-cli-vs-desktop/), [Claude Code CLI e desktop](/articles/claude-code-cli-vs-desktop/) e [OpenCode CLI e desktop](/articles/opencode-cli-vs-desktop/) comparam as interfaces de cada produto.

**Comece na pasta do laboratório.** Cada interface exige que você escolha o espaço de trabalho:

1. **Codex desktop:** abra o aplicativo ChatGPT, selecione o laboratório extraído como projeto local e inicie uma tarefa local. Confira o caminho da pasta e os pedidos de aprovação antes de editar. Uma tarefa hospedada usa outra cópia do espaço de trabalho.
2. **Codex CLI:** execute `cd /path/to/effective-ai-course-lab` e depois `codex`. Confirme a pasta de trabalho e o modo de aprovação exibidos.
3. **Claude Code CLI:** execute o mesmo `cd` e depois `claude`. Confirme a pasta do projeto e as permissões das ferramentas.
4. **OpenCode TUI:** execute o mesmo `cd` e depois `opencode`. Confirme o provedor, o projeto e as permissões selecionados.

**ChatGPT chat e Claude Projects lidam com conversas e arquivos de referência.** Codex e Claude Code operam em um espaço de código com ferramentas para arquivos e comandos. OpenCode também tem interfaces desktop e IDE, mas esta lição usa o terminal. Provedor, conta e execução local ou hospedada variam. Registre a interface escolhida em vez de tratar todas as sessões como iguais.

**Confira cinco detalhes antes de abrir o laboratório:** sistema operacional compatível, autenticação, custo do provedor ou conta, permissões de arquivos e comandos, e execução local ou em host remoto. Registre sua escolha. Não presuma que o aplicativo desktop e a ferramenta de terminal usem o mesmo espaço.

## Inspecione o projeto inicial

**Reabra a pasta limpa do laboratório** da lição sobre contexto do repositório. Esta cópia contém seu `AGENTS.md` commitado e as orientações opcionais de `CLAUDE.md`. Revise os arquivos antes de pedir uma edição. Execute os testes iniciais nesta pasta.

```bash
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
```

**Resultado inicial esperado:** o relatório imprime `Total tasks: 4`. A execução nomeia dois testes e termina com `OK`. Se algum falhar, pare e inspecione os arquivos. Não atribua ao agente a correção de um ponto de partida defeituoso.

**Use os snapshots Git locais** da configuração do curso e da lição de contexto. `AGENTS.md` e o `CLAUDE.md` opcional já devem estar commitados. Execute `git status --short` antes da edição e espere nenhum arquivo listado. O agente também não deve fazer commit. O arquivo não inclui histórico Git. O arquivo `.gitignore` exclui o bytecode Python gerado durante a execução dos testes. Se extraiu uma cópia nova, repita a configuração e a lição de contexto nessa pasta. Faça commit dos arquivos de orientação antes de editar o recurso. Primeiro inicialize e faça commit do projeto:

```bash
git init
git add .
git commit -m "Base do laboratório do curso"
```

**Depois, adicione `AGENTS.md` e o `CLAUDE.md` opcional** com a fonte aprovada e o comando de teste da lição. Faça commit desses arquivos, confirme que `git status --short` está limpo e edite o recurso. Execute os comandos na pasta de prática extraída, não na raiz de outro repositório.

## Envie uma solicitação delimitada

**Abra a pasta do laboratório** no agente escolhido. Envie este pacote de tarefas:

```text
Adicione um argumento opcional --status a task_report.py.
Valores permitidos: open e done.
Quando ausente, mantenha inalterada a saída atual da contagem total.
Quando presente, conte somente as tarefas correspondentes e imprima Total tasks: N.
Adicione testes para ambos os valores, um valor inválido e a saída padrão inalterada.
Não altere tasks.json nem arquivos sem relação com a tarefa.
Execute os testes e informe o comando exato e o resultado.
Pare após o código e os testes. Não faça commit nem push.
```

**No Windows,** substitua `python3` pelo comando `py -3` verificado na configuração, também nas instruções do repositório e no pacote de tarefas.

**Peça um plano curto antes da edição** se não conhece o código. Autorize o agente a editar somente a pasta descartável do laboratório. As permissões variam entre ferramentas. Confira as configurações atuais antes de permitir comandos shell ou gravação de arquivos.

## Revise o resultado

**Leia o diff.** Confira se a saída sem filtro permanece igual, se o filtro aceita somente dois valores e se os testes cobrem o erro e a saída padrão inalterada. Testes aprovados validam a mudança somente se verificarem o comportamento solicitado.

```bash
git status --short
git diff -- task_report.py tests
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --status open
python3 task_report.py tasks.json --status done
python3 task_report.py tasks.json --status invalid
```

**Resultados esperados:** os três primeiros relatórios mostram contagens de 4, 2 e 2. O valor inválido mostra um erro claro e termina com status diferente de zero. O texto depende da implementação. No macOS ou Linux, execute `echo $?` logo após o comando inválido para ler o código de saída. No PowerShell, confira `$LASTEXITCODE`.

| Evidência | O que inspecionar |
|---|---|
| **Lista de arquivos** | Somente o programa e os testes mudaram |
| **Diff** | A lógica do filtro corresponde à solicitação |
| **Saída dos testes** | Os novos casos foram executados e passaram |
| **Execução manual** | As contagens padrão, `open` e `done` correspondem a `tasks.json` |

**Se o agente relatar um resultado sem executar testes,** execute o comando você mesmo. Se a edição sair do pacote de tarefas, peça uma correção delimitada. Se o estado não estiver claro, apague a cópia extraída e extraia novamente o ZIP original.

## Respostas da rota de estudo

**Use estes arquivos completos se seu patch manual falhar.** Comece com um laboratório recém-extraído, salve o primeiro bloco como `task_report.py` e o segundo como `tests/test_task_report.py`, e execute os comandos de Revisar o resultado. Mantenha `tasks.json` e `docs/requirements.md` inalterados. Registre a falha original antes de copiar os arquivos.

`task_report.py`:

```python
"""Mostra a contagem de tarefas de um arquivo JSON."""

import argparse
import json
import sys
from pathlib import Path


def count_tasks(path: Path, status: str | None = None) -> int:
    """Conta todas as tarefas ou as que têm um status permitido."""
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    if status not in (None, "open", "done"):
        raise ValueError("status must be open or done")
    if status is None:
        return len(tasks)
    return sum(1 for task in tasks if task["status"] == status)


def main() -> int:
    parser = argparse.ArgumentParser(description="Contar tarefas da oficina")
    parser.add_argument("path", type=Path, help="caminho para a lista JSON de tarefas")
    parser.add_argument("--status", choices=("open", "done"))
    args = parser.parse_args()
    try:
        total = count_tasks(args.path, args.status)
    except (OSError, ValueError, KeyError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Total tasks: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Testes do relatório de tarefas da oficina."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from sys import path as module_path

ROOT = Path(__file__).resolve().parents[1]
module_path.insert(0, str(ROOT))
from task_report import count_tasks  # noqa: E402


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_counts_each_approved_status(self):
        sample = ROOT / "tasks.json"
        self.assertEqual(count_tasks(sample, "open"), 2)
        self.assertEqual(count_tasks(sample, "done"), 2)

    def test_rejects_invalid_status_in_function(self):
        with self.assertRaises(ValueError):
            count_tasks(ROOT / "tasks.json", "pending")

    def test_default_command_stays_unchanged(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json")],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_invalid_command_exits_nonzero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"), str(ROOT / "tasks.json"),
             "--status", "invalid"],
            capture_output=True, text=True, check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Mantenha uma cópia editada que passe nos testes do filtro** durante as lições sobre contexto e verificação. Se usou esta solução para se recuperar, mantenha a cópia nova com os testes aprovados para essas lições. Guarde o diff e o registro dos testes fora do laboratório. Restaure o projeto inicial antes da lição de delegação ou descarte uma tentativa malsucedida para recomeçar.

## Pratique e confira

**Seu artefato:** um diff do laboratório e um registro de revisão de quatro linhas sobre escopo dos arquivos, comportamento padrão, comportamento filtrado e entrada inválida. Anote o nome e a versão da ferramenta em suas notas privadas para reproduzir um problema específico da versão.

**Raciocínio esperado:** você escolheu uma interface adequada ao seu modo de trabalho, delimitou uma tarefa, inspecionou a edição real e executou uma verificação independente do resumo do agente.

## Confira seu entendimento

1. **Pergunta:** O que comprova que a edição do filtro de status funcionou? **Resposta:** Um diff delimitado, testes aprovados e resultados observados para o padrão, open, done e o caso inválido.
2. **Pergunta:** A afirmação do agente de que executou os testes conta como resultado seu? **Resposta:** Não. Execute o comando ou inspecione a saída dos testes.

## Solução de problemas

- **Comando ausente:** conclua a instalação pelo guia do fornecedor e reabra o terminal.
- **Sem acesso a arquivos:** abra a pasta extraída e confira as permissões do espaço de trabalho.
- **Arquivos inesperados alterados:** pare e confira `git status --short` antes de outra solicitação.
- **Testes passam, comportamento incorreto:** adicione um caso manual ou um teste para o requisito ausente.

## Próximos passos

**Continue com [Janelas de contexto e transferências](/articles/effective-ai-context-window-management/)**. Você manterá um registro útil para uma nova sessão.

**Navegação do curso:** [Anterior: Pacotes de tarefas](/articles/effective-ai-task-packets/), [Programa do curso](/effective-ai-course-start/).

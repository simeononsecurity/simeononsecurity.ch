---
title: "Projeto final de fluxo de trabalho com IA: crie e verifique um relatório JSON"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Crie um relatório JSON com contexto do projeto, uma solicitação de agente com escopo definido, testes independentes, revisão das fontes e uma transferência para uma nova sessão."
genre: ["Inteligência artificial", "Engenharia de software", "Educação"]
tags: ["projeto final de fluxo de trabalho com IA", "projeto de agente de programação", "verificação de tarefas com IA", "AGENTS.md", "prática de MCP", "transferência de agente"]
cover: "/img/cover/effective-ai-capstone.webp"
coverAlt: "Tarefa de software do workshop concluída com arquivos-fonte, resultados de testes, revisão do agente e registro de transferência"
coverCaption: ""
---

[Voltar ao curso Fluxo de Trabalho Prático com IA](/effective-ai-course-start/)

**Crie um novo formato de saída e comprove seu comportamento.** Antes, você adicionou um filtro de status. Este projeto final começa com um laboratório novo e adiciona um relatório JSON para outro programa ler. O novo requisito verifica se você transfere seu fluxo de trabalho para outro recurso.

**Objetivo de aprendizagem:** você entregará um relatório JSON verificado, um registro de evidências de fontes e ferramentas e uma transferência que uma nova sessão entenda.

## Principais pontos

- **Um requisito separado** controla o recurso do projeto final.
- **A edição de um agente de programação** fica limitada aos arquivos nomeados.
- **Verificações independentes** determinam a aceitação.
- **Uma transferência para uma nova sessão** permite reconstruir o resultado.

## Antes de começar

**Pré-requisitos:** conclua as lições 0 a 10, incluindo contexto do repositório, a primeira tarefa de programação, MCP ou a alternativa do navegador, delegação e ciclos delimitados. A lição 11 é opcional. Reserve de 90 a 120 minutos. Dificuldade intermediária.

**Use uma extração nova** do [laboratório inicial](/downloads/effective-ai-course-lab.zip). Execute `python3 task_report.py tasks.json` e os dois testes de referência antes de qualquer edição. No Windows, use `py -3` se sua configuração usa o iniciador Python. Crie uma base Git local como na configuração do curso. O filtro de status da lição 5 está ausente de propósito.

**Leia `docs/capstone-requirements.md`, revisão 1.** O requisito pede `--format text|json`. A saída de texto padrão continua `Total tasks: 4`. A saída JSON contém um total numérico e contagens de cada status presente nos dados. Teste uma lista vazia, um status ausente e um formato não aceito. Não use `docs/requirements.md` como referência para este recurso novo.

**Escolha sua trilha.** A trilha conectada usa uma edição observada de um agente de programação, uma chamada MCP real somente de leitura e um worker nativo ou uma sessão de worker separada. A trilha de estudo usa um assistente de chat para sugerir código, uma fonte no navegador no lugar do MCP e chats separados como workers simulados. Marque as etapas de ferramentas indisponíveis como “não executadas”. Ambas exigem testes locais e revisão dos arquivos. O gabarito abaixo fornece arquivos completos como caminho de recuperação. Salve sua primeira tentativa nas notas antes de copiar o gabarito para uma extração nova.

## Fase 1: Resumo do projeto

**Abra o projeto sintético de workshop do ChatGPT ou Claude.** Peça um rascunho de lembrete com duas frases. Confira o horário das 19h em `approved-schedule.md`. O cronograma controla o lembrete. O requisito do projeto final controla o programa.

**Evidência:** registre o nome do projeto, a revisão da fonte, o horário observado no rascunho e qualquer correção. Não envie a mensagem.

## Fase 2: Contexto do repositório

**Abra o laboratório novo.** Crie um `AGENTS.md` curto que aponte para `docs/capstone-requirements.md`, `task_report.py`, os testes e o comando de teste comprovado durante a configuração. Se usar Claude Code, importe o arquivo compartilhado por `CLAUDE.md`. Faça um commit humano de configuração para esses arquivos de orientação e confirme que `git status --short` está vazio. O agente de programação não deve fazer commit da alteração do recurso.

**Evidência:** salve o mapa e um retrato limpo das instruções. Anote as chaves JSON e o comportamento para entradas inválidas da revisão 1. Trate um chat anterior sobre o filtro de status como contexto de outra tarefa.

## Fase 3: Fonte externa

**Trilha conectada:** use o [servidor MCP OpenAI Docs somente de leitura](https://learn.chatgpt.com/learn/docs-mcp) por um cliente compatível. Peça a uma ferramenta MCP as orientações atuais de `AGENTS.md`. Registre o nome da ferramenta, a URL da fonte e um ponto útil para o laboratório. Depois, remova a conexão de prática.

**Trilha de estudo:** abra a [documentação oficial de `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md) no navegador. Registre o título, a URL e um ponto útil. Marque a descoberta e a execução de MCP como “não executadas”.

**Evidência:** uma entrada de servidor configurada não prova que houve execução. A trilha conectada exige uma chamada visível à ferramenta e conteúdo de fonte retornado.

## Fase 4: Delegue uma revisão

**Peça a um worker somente de leitura** que examine `docs/capstone-requirements.md`, `task_report.py` e os testes de referência. Exija um relatório de no máximo cinco linhas com verificações ausentes e caminhos dos arquivos. Na trilha de estudo, use um chat separado e marque-o como worker simulado.

**Resultado esperado:** os testes iniciais verificam o total e um valor JSON que não é uma lista. Eles não verificam a saída JSON, uma lista vazia, um status ausente nem um formato inválido. Abra o arquivo de testes e confira o relatório. Uma revisão independente curta é útil porque os critérios de aceitação diferem dos da lição 5.

**Evidência:** guarde o relatório curto e sua decisão de integração em uma frase. Mantenha a transcrição do worker fora do registro principal da tarefa.

## Fase 5: Solicite a edição

**Envie o pacote abaixo a um agente de programação.** Na trilha de estudo, um assistente de chat sugere um patch, que você aplica manualmente no laboratório.

```text
Objetivo: adicionar --format text|json depois do caminho JSON.
Fonte: docs/capstone-requirements.md, revisão 1.
Arquivos permitidos: task_report.py e tests/test_task_report.py.
Manter: saída padrão Total tasks: 4 e tasks.json sem alterações.
JSON: um objeto com total e contagens by_status, sem texto adicional em stdout.
Verificações exigidas: texto padrão e explícito, JSON 4/2/2, lista vazia,
status ausente, formato inválido e testes de referência.
Parar se: houver conflito entre fontes, falha de referência não relacionada ou edição fora do escopo.
Relatório: arquivos alterados, comandos, saídas observadas, problema pendente.
Não fazer commit, push, publicação nem enviar mensagem.
```

**Revise o plano** antes da edição. A escolha do esquema importa: `total` é um número, não a string `"4"`. `by_status` inclui cada status da entrada, inclusive valores futuros. Limite a edição ao laboratório extraído.

## Fase 6: Teste e revise

**Execute estas verificações você mesmo.** No Windows, troque `python3` por `py -3`. A ordem exata das chaves JSON e os espaços não importam. Analise a saída como JSON e compare os tipos dos valores.

```bash
git status --short
git diff -- task_report.py tests/test_task_report.py
python3 -m unittest discover -s tests -v
python3 task_report.py tasks.json
python3 task_report.py tasks.json --format text
python3 task_report.py tasks.json --format json
python3 task_report.py tasks.json --format invalid
```

**Comportamento esperado:** os testes passam. Os dois comandos de texto exibem `Total tasks: 4`. O comando JSON retorna um único objeto com `total` 4, `by_status.open` 2 e `by_status.done` 2. Um formato inválido termina com código diferente de zero. Os testes também cobrem uma entrada vazia e uma tarefa sem `status` textual. Leia a saída de erro observada e o código de saída desses casos.

| Etapa | Evidência de aprovação | Recuperação se falhar |
|---|---|---|
| **Resumo do projeto** | Lembrete indica 19h | Atualize a fonte do cronograma |
| **Mapa do repositório** | Requisito e caminhos dos testes nomeados | Corrija os arquivos de orientação |
| **Fonte externa** | Fonte MCP consultada ou alternativa do navegador registrada | Verifique a conexão ou a URL |
| **Revisão do worker** | Testes ausentes confirmados no arquivo | Corrija o relatório do worker |
| **Escopo dos arquivos** | Apenas programa e testes | Inspecione cada alteração indesejada |
| **Comportamento** | Texto, JSON, vazio e erros verificados | Diagnostique uma causa e tente novamente |
| **Transferência** | Nova sessão reconstrói o estado | Acrescente fonte ou resultado ausente |

**Use uma extração nova como restauração segura.** Salve suas notas fora do laboratório, descarte apenas a cópia extraída descartável e extraia o ZIP original novamente. Não use uma reinicialização ampla do Git em um repositório com trabalho a preservar.

## Fase 7: Transferência para uma nova sessão

**Escreva uma transferência com menos de 180 palavras** fora da pasta do laboratório. Inclua a revisão do requisito, arquivos alterados, comando e resultado exatos do teste, saídas de texto e JSON, verificações de entradas inválidas, registro de uso e ação pendente. Abra uma sessão nova e peça que ela identifique as chaves JSON e diga se o recurso passou.

**Resposta esperada:** a nova sessão cita `total` e `by_status`, aponta a revisão 1, informa apenas verificações observadas e sinaliza qualquer verificação ausente.

## Gabarito e rubrica

**Uma implementação válida** está abaixo. Salve o primeiro bloco como `task_report.py` e o segundo como `tests/test_task_report.py` em uma extração nova do laboratório. Mantenha `tasks.json` e os dois arquivos de requisitos sem mudanças. Execute as verificações da etapa 6. Compare outra solução com o requisito e o comportamento observado.

`task_report.py`:

```python
"""Imprime uma contagem em texto ou um resumo JSON das tarefas do workshop."""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def load_tasks(path: Path) -> list:
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task data must be a list")
    for index, task in enumerate(tasks, start=1):
        if not isinstance(task, dict) or not isinstance(task.get("status"), str):
            raise ValueError(f"task {index} needs a string status")
    return tasks


def count_tasks(path: Path) -> int:
    return len(load_tasks(path))


def summarize_tasks(path: Path) -> dict:
    tasks = load_tasks(path)
    counts = Counter()
    for task in tasks:
        counts[task["status"]] += 1
    return {"total": len(tasks), "by_status": dict(sorted(counts.items()))}


def main() -> int:
    parser = argparse.ArgumentParser(description="Relatório de tarefas do workshop")
    parser.add_argument("path", type=Path, help="caminho para a lista JSON de tarefas")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()
    try:
        if args.format == "json":
            print(json.dumps(summarize_tasks(args.path)))
        else:
            print(f"Total tasks: {count_tasks(args.path)}")
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

`tests/test_task_report.py`:

```python
"""Verificações para relatórios de texto e JSON das tarefas do workshop."""

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


def run_report(path: Path, *options: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / "task_report.py"), str(path), *options],
        capture_output=True, text=True, check=False,
    )


class TaskReportTests(unittest.TestCase):
    def test_counts_four_sample_tasks(self):
        self.assertEqual(count_tasks(ROOT / "tasks.json"), 4)

    def test_rejects_non_list_data(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "invalid.json"
            sample.write_text(json.dumps({"tasks": []}), encoding="utf-8")
            with self.assertRaises(ValueError):
                count_tasks(sample)

    def test_default_and_explicit_text(self):
        for options in ((), ("--format", "text")):
            result = run_report(ROOT / "tasks.json", *options)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), "Total tasks: 4")

    def test_json_counts_and_types(self):
        result = run_report(ROOT / "tasks.json", "--format", "json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout), {
            "total": 4, "by_status": {"open": 2, "done": 2},
        })

    def test_empty_list(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "empty.json"
            sample.write_text("[]", encoding="utf-8")
            result = run_report(sample, "--format", "json")
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {
                "total": 0, "by_status": {},
            })

    def test_missing_status(self):
        with tempfile.TemporaryDirectory() as directory:
            sample = Path(directory) / "missing.json"
            sample.write_text('[{"id": 1}]', encoding="utf-8")
            for options in ((), ("--format", "json")):
                result = run_report(sample, *options)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("status", result.stderr)

    def test_invalid_format(self):
        result = run_report(ROOT / "tasks.json", "--format", "invalid")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("invalid", result.stderr)


if __name__ == "__main__":
    unittest.main()
```

**Restaure depois de usar o gabarito:** salve suas notas fora do laboratório, descarte essa cópia e extraia novamente o laboratório inicial original. A nova cópia contém os dois testes de referência e não inclui a implementação do recurso.

**Dê um ponto para cada etapa** da tabela acima. Sete pontos concluem a trilha conectada se a linha da fonte externa inclui uma chamada MCP real e a linha do worker documenta uma sessão real. Sete pontos concluem a trilha de estudo se a fonte for uma página verificada no navegador e as etapas de ferramentas estiverem explicitamente marcadas como não executadas. A falta de uma verificação de comportamento, fonte ou escopo de arquivos bloqueia ambas as trilhas.

## Verifique sua compreensão

1. **Qual requisito controla esse recurso?** `docs/capstone-requirements.md`, revisão 1. O requisito anterior do filtro de status pertence à lição 5.
2. **O que comprova o contrato JSON?** Analise a saída do comando, compare os valores numéricos e as contagens de cada status, e verifique entradas vazias e inválidas. Um resumo bem escrito do agente não basta.

## Solução de problemas

- **O teste de referência falha antes da edição:** restaure o laboratório do ZIP e repita a configuração.
- **O agente altera outro arquivo:** examine o diff e reverta apenas a alteração indesejada no laboratório.
- **A conexão MCP falha:** use a fonte do navegador e marque a etapa como trilha de estudo.
- **O worker repete um valor errado:** releia o requisito do projeto final e corrija o relatório.
- **O limite de tentativas termina:** guarde o registro de falha e peça a um revisor humano o próximo passo.

## Próximos passos

**Salve seu registro de evidências concluído.** Para publicação avançada em equipe e autoridade entre sistemas, continue com o [Curso de Implementação da Colaboração com IA](/ai-collaboration-course-start/).

**Navegação do curso:** [Anterior obrigatória: ciclos delimitados](/articles/effective-ai-bounded-agent-loops/), [Opcional: avaliação de agentes especializados](/articles/effective-ai-specialized-agent-evaluation/), [Visão geral do curso](/effective-ai-course-start/).

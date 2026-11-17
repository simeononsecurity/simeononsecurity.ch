---
title: "Loops limitados de agentes de IA: verificações, novas tentativas e regras de parada"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Defina um loop de objetivo de IA com estado observável, verificações, limites de tentativas, condições de parada e uma transferência clara para uma pessoa."
genre: ["Inteligência artificial", "Engenharia de software", "Produtividade"]
tags: ["loops de objetivos de IA", "loop de nova tentativa de agente", "regras de parada de automação de IA", "monitoramento de agentes", "transferência humana de IA", "fluxo de trabalho de IA limitado"]
cover: "/img/cover/effective-ai-bounded-agent-loops.webp"
coverAlt: "Um pequeno loop de agente passa de uma edição para um teste, uma decisão de nova tentativa e uma transferência para uma pessoa"
coverCaption: ""
---

[Voltar ao curso prático de fluxos de trabalho com IA](/effective-ai-course-start/)

**Um loop de objetivo repete o trabalho até um resultado definido passar por uma verificação ou uma regra de parada ser acionada.** Um loop útil lê o estado atual, executa uma ação limitada, verifica o resultado e registra o que aconteceu. Uma instrução aberta como “continue tentando” não tem uma regra confiável de conclusão.

**Objetivo de aprendizagem:** você executará um loop limitado de laboratório com uma verificação que se sabe que falha e registrará a decisão de parada.

## Principais aprendizados

- **Objetivo:** um resultado declarado em termos observáveis.
- **Estado:** os arquivos, as saídas, os erros e a revisão do código-fonte atuais.
- **Verificação:** um teste ou análise ligado ao objetivo.
- **Limite de tentativas:** o número máximo de tentativas para uma falha.
- **Regra de parada:** uma condição que exige encerrar ou pedir uma decisão humana.

## Antes de começar

**Pré-requisitos:** o [pacote de tarefas](/articles/effective-ai-task-packets/), o [registro de verificação](/articles/effective-ai-output-verification/) e a [lição sobre delegação](/articles/effective-ai-agent-delegation/). Reserve 45 minutos. O nível é intermediário. Use uma cópia nova do laboratório sintético para saber de antemão qual será a primeira verificação que falhará.

## Escreva o contrato do loop

**Para o pedido de filtro por status**, defina o contrato antes de qualquer nova tentativa:

```text
Objetivo: aceitar --status open|done sem alterar a saída padrão.
Fonte: docs/requirements.md, revisão 1.
Arquivos permitidos: task_report.py e testes específicos.
Verificações: testes unitários, contagens 4/2/2, valor inválido retorna código de saída diferente de zero.
Orçamento de novas tentativas: no máximo duas edições após a primeira tentativa.
Pare imediatamente: conflito na fonte, alteração inesperada de arquivo, exposição de segredo,
ou falha de referência sem relação com esta solicitação.
Entrega: informe o diff final, comandos, saídas, tentativas e problema não resolvido.
```

**O limite é uma política da tarefa**, não um padrão do produto. Duas novas tentativas bastam para diagnosticar uma tarefa pequena de laboratório sem esconder falhas repetidas. Uma tarefa de produção precisa de uma decisão própria sobre riscos e revisão.

## Use uma tabela de estado

| Etapa | Estado a registrar | Decisão |
|---|---|---|
| **Ler** | Revisão do código-fonte e resultado inicial | Pare se o estado inicial for diferente |
| **Agir** | Arquivos alterados e ação executada | Rejeite alterações fora do escopo |
| **Verificar** | Teste exato e resultado manual | Aceite ou diagnostique |
| **Tentar novamente** | Causa da falha e nova hipótese | Continue somente dentro do limite |
| **Transferir** | Estado final e próximo responsável | Pare após passar ou ficar bloqueado |

**Registre as tentativas, não apenas a última mensagem.** Um teste aprovado após três edições ocultas não explica o que mudou. Mantenha um registro curto da falha, da hipótese revisada e das novas evidências.

## Analise uma falha

**Exemplo da primeira tentativa:** o agente adiciona o filtro e os testes. `open` mostra 2, mas `--status invalid` mostra 0 e termina com sucesso. O requisito exige um código de saída diferente de zero para um valor inválido. Marque a verificação como reprovada.

**Diagnóstico:** inspecione a validação dos argumentos. O agente tratou um valor desconhecido como uma correspondência vazia, em vez de gerar um erro. Peça uma correção limitada para validar os valores aceitos antes de contar. Execute novamente o caso inválido e todas as verificações anteriores.

```text
Tentativa 1: o status inválido retornou sucesso, então a aceitação falhou.
Causa encontrada: não há validação dos valores aceitos.
Pedido da tentativa 2: rejeite valores sem suporte e mantenha as contagens 4/2/2.
Evidência necessária: execução completa dos testes e status de saída do comando inválido.
```

**Resultado esperado na segunda tentativa:** uma mensagem de erro clara e um código de saída diferente de zero para `invalid`, com os totais válidos inalterados. Se a segunda tentativa ainda falhar, use a última somente depois de identificar uma nova causa. Repetir o mesmo pedido não é diagnóstico.

## Lide com resultados ambíguos

**Um processo que termina sem resultado não teve sucesso.** Se uma ferramenta atingir o tempo limite após uma possível gravação, inspecione os arquivos e o estado do Git antes de executá-la novamente. Se um serviço conectado informar um resultado desconhecido, leia o estado atual antes de repetir uma ação externa. Fora do laboratório, envios, publicações ou gravações duplicadas representam um risco real.

**Pare para uma análise humana** se o requisito entrar em conflito com outra fonte aprovada, uma permissão bloquear a ação, o limite de tentativas acabar ou a ação solicitada ultrapassar um limite de publicação. A transferência deve indicar o estado exato e a decisão pendente.

## Separe loops de monitores

**Um loop de edição** executa dentro de uma tarefa limitada e verifica o resultado após cada ação. **Um monitor agendado** desperta depois para inspecionar uma condição. Um monitor precisa de sua própria frequência, limite de alteração, regra de notificação e condição de parada. Não transforme o loop de edição do laboratório em uma tarefa recorrente. A próxima lição avalia sistemas persistentes antes de ativá-los.

## Execute um loop controlado

**Comece com o laboratório intacto.** Os dois testes de referência passam. Na nova extração, crie `tests/test_loop_contract.py` com a verificação abaixo. Esse arquivo expressa uma funcionalidade desejada ausente no projeto inicial. Ele não pertence ao ZIP inicial mantido.

```python
"""One controlled failing check for the status-filter exercise."""

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class LoopContractTests(unittest.TestCase):
    def test_open_status_count(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "task_report.py"),
             str(ROOT / "tasks.json"), "--status", "open"],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "Total tasks: 2")


if __name__ == "__main__":
    unittest.main()
```

**Execute `python3 -m unittest discover -s tests -v`.** Os dois testes originais devem passar e o novo teste de contrato deve falhar porque o projeto inicial não oferece `--status`. Registre a falha real. Se você inicializou o Git como na lição 0, registre também `git status --short`. Caso contrário, compare os arquivos alterados com uma extração intacta. No Windows, use `py -3` se sua configuração usar o launcher.

**Defina um limite de três tentativas:** a primeira edição e no máximo duas correções. Passe o contrato do loop acima ao agente e peça uma edição limitada. Após cada tentativa, inspecione os arquivos alterados, execute novamente todos os testes e rode os comandos padrão, `open`, `done` e um valor inválido. Registre a causa da falha antes de tentar novamente. Pare se um teste passar, se uma referência não relacionada falhar, se houver alteração fora do escopo ou se a terceira tentativa falhar.

**Roteiro de estudo:** depois de registrar o teste vermelho, aplique a [resposta completa da lição 5](/articles/effective-ai-coding-agent-first-task/) nesta nova cópia. Execute novamente as mesmas verificações e registre que a edição do agente não foi executada. Mantenha o teste de contrato controlado. Não o enfraqueça nem o remova para fazê-lo passar.

| Tentativa | Estado e observação | Decisão |
|---|---|---|
| **Antes da edição** | Os dois testes iniciais passam e a nova verificação `open` falha | Continue com uma edição limitada |
| **Após cada edição** | Registre testes exatos, totais, código de saída inválido e arquivos alterados | Aceite, diagnostique ou pare |
| **Ao esgotar o limite** | Registre a falha restante e a diferença atual | Transfira sem outra tentativa |

## Pratique e verifique

**Seu artefato:** o teste controlado que falha, as saídas observadas antes e depois, um registro de tentativas e uma decisão final de aceitar ou parar. Se a primeira edição passar, registre uma tentativa. Não invente uma segunda falha para preencher o registro.

**Verificação de conclusão:** o contrato identifica uma fonte, o escopo de arquivos, verificações observáveis, um limite de tentativas, pelo menos uma condição de parada imediata e uma transferência. Seu registro inclui o teste vermelho real, os resultados posteriores e uma aprovação ou parada por limite. Uma segunda tentativa identifica uma causa nova e difere da primeira.

## Confira seu entendimento

1. **Pergunta:** o que o primeiro teste vermelho do contrato comprova? **Resposta:** que o projeto inicial não tem o filtro de status solicitado, como mostra um teste escrito antes da edição.
2. **Pergunta:** quando o loop deve parar mesmo com tentativas restantes? **Resposta:** diante de uma alteração fora do escopo, uma permissão incerta ou um requisito conflitante.

## Solução de problemas

- **O loop repete a mesma falha:** pare e formule uma nova hipótese para a causa.
- **As verificações ficam mais fracas:** restaure os critérios de aceitação originais.
- **Resultado externo incerto:** inspecione o estado atual antes de outra tentativa.
- **Limite esgotado:** transfira o registro de falhas em vez de escondê-las.

## Próximas etapas

Continue com a [Avaliação de agentes especializados](/articles/effective-ai-specialized-agent-evaluation/), que é opcional, ou vá direto ao [projeto final do curso de fluxos de trabalho com IA](/articles/effective-ai-capstone/). Para outras opções de runtime, leia o [guia de ambientes de agentes](/articles/best-ai-agent-harnesses/).

**Navegação do curso:** [Anterior: Delegação de agentes](/articles/effective-ai-agent-delegation/), [Visão geral do curso](/effective-ai-course-start/).

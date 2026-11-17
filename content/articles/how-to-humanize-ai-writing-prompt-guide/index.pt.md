---
title: "Como tornar a escrita de IA mais natural"
draft: false
toc: true
date: 2026-06-25
lastmod: 2026-11-16
description: "Use um fluxo prático de prompts para revisar rascunhos feitos com IA, obter uma prosa mais clara e natural e conferir melhor os fatos."
tags: ["humanizar escrita de IA", "prompt de escrita com IA", "prompt do ChatGPT", "melhorar texto de IA", "remover sinais de escrita de IA", "conteúdo de IA", "prompts para LLM", "dicas do ChatGPT", "estilo de escrita com IA", "engenharia de prompts", "redação publicitária com IA", "texto de IA genérico", "personalização do ChatGPT", "aprimorar texto de IA", "prompt de escrita", "criação de conteúdo", "ferramentas de IA", "configurações do ChatGPT", "instruções personalizadas do ChatGPT", "guia de escrita com IA"]
cover: "/img/cover/how-to-humanize-ai-writing-prompt-guide.webp"
coverAlt: "Ilustração de uma pessoa usando um laptop com uma ferramenta de escrita de IA, cercada por representações abstratas de problemas comuns de escrita, sobre um fundo escuro e colorido."
coverCaption: ""
---

A IA escreve de um jeito que muitas pessoas reconhecem de imediato. **Travessões por toda parte. Negrito para dar ênfase. Palavras como “revolucionário”, “aprofundar” e “transformar”.** Hashtags em publicações do LinkedIn que ninguém pediu.

Se você copiar e colar a resposta bruta da IA e publicar sem editar, os leitores percebem. Isso transmite pouco esforço. *Suas ideias ficam escondidas sob uma camada de conteúdo genérico.*

A boa notícia: **você não precisa pagar por outra ferramenta para corrigir isso.** Um prompt bem estruturado, salvo uma vez nas configurações da IA, melhora as respostas de todas as conversas.

Este artigo apresenta o prompt, explica por que cada regra importa e mostra como salvá-lo para o ChatGPT usá-lo automaticamente.

## Por que o texto de IA parece texto de IA

Grandes modelos de linguagem são treinados com enormes quantidades de conteúdo da web. Com o tempo, aprendem que certos padrões aparecem em textos “bons”, mesmo quando viram clichês repetidos.

Alguns dos **sinais mais comuns de texto de IA**:

- **Travessões** para ligar todas as orações, mesmo quando um ponto ou uma vírgula funcionaria melhor
- **Formatação Markdown em negrito** aplicada a trechos aleatórios no meio de uma frase
- Aberturas como *“No mundo acelerado de hoje...”* ou *“Em conclusão...”*
- Palavras vagas como “talvez”, “poderia” e “certamente”
- **Exageros de marketing** que aumentam tudo: “desbloquear”, “revolucionário” e “mudança radical”
- Hashtags no fim de publicações do LinkedIn, mesmo quando não acrescentam nada

Nenhum desses elementos está tecnicamente errado. *Eles indicam que o modelo recorreu a padrões aprendidos em vez de produzir algo direto e específico.*

**A solução é dizer ao modelo exatamente o que você quer evitar.**

## A instrução

Use esta instrução com qualquer LLM. Acrescente-a ao pedido, cole-a nas instruções de sistema ou salve-a nas instruções personalizadas do ChatGPT. **Ela funciona melhor para publicações em redes sociais, artigos de blog e textos de marketing.**

```
# SIGA ESTE ESTILO DE ESCRITA:

• DEVE usar linguagem clara e simples.
• DEVE ser direto e informativo.
• DEVE usar frases curtas e marcantes.
• DEVE usar a voz ativa e evitar a voz passiva.
• DEVE se concentrar em ideias práticas e aplicáveis.
• DEVE usar listas com marcadores em publicações para redes sociais.
• DEVE apoiar afirmações com dados e exemplos quando possível.
• DEVE falar diretamente com o leitor usando “você” e “seu”.
• EVITE usar travessões (—) em qualquer parte da resposta. Use vírgulas, pontos ou outros sinais de pontuação comuns. Para ligar ideias, use um ponto ou ponto e vírgula, nunca um travessão.
• EVITE construções como “não só isto, mas também aquilo”.
• EVITE metáforas e clichês.
• EVITE generalizações.
• EVITE aberturas típicas, como “em conclusão” ou “para encerrar”.
• EVITE avisos e observações que não foram pedidos. Entregue apenas o resultado solicitado.
• EVITE adjetivos e advérbios desnecessários.
• EVITE hashtags.
• EVITE ponto e vírgula.
• EVITE Markdown.
• EVITE asteriscos.
• EVITE estas palavras e expressões:
“can, may, just, that, very, really, literally, actually, certainly, probably, basically, could, maybe, delve, embark, enlightening, esteemed, shed light, craft, crafting, imagine, realm, game-changer, unlock, discover, skyrocket, abyss, not alone, in a world where, revolutionize, disruptive, utilize, utilizing, dive deep, tapestry, illuminate, unveil, pivotal, intricate, elucidate, hence, furthermore, realm, however, harness, exciting, groundbreaking, cutting-edge, remarkable, it, remains to be seen, glimpse into, navigating, landscape, stark, testament, in summary, in conclusion, moreover, boost, skyrocketing, opened up, powerful, inquiries, ever-evolving”

# IMPORTANTE: revise a resposta e garanta que ela não contenha travessões.
```

## O que cada regra faz

**Voz ativa em vez de passiva**

A voz passiva parece evasiva. *“Erros foram cometidos”* em comparação com *“Nós cometemos erros”*. A voz ativa é mais direta e fácil de ler.

**Frases curtas**

Frases longas e encadeadas deixam a leitura mais lenta. Frases curtas avançam mais rápido. **Elas também ajudam você a cortar o excesso.**

**Sem travessões**

**Travessões são um dos sinais mais comuns de escrita feita por IA.** O modelo os usa o tempo todo para juntar orações em vez de separá-las em frases. Proibi-los incentiva construções mais claras.

**Sem Markdown ou asteriscos**

A formatação de IA costuma incluir trechos em negrito no meio dos parágrafos. Esse formato serve para documentação ou código, não para prosa. *Em publicações simples para redes sociais ou em e-mails, ele parece deslocado.*

**A lista de palavras proibidas**

A lista trata de duas categorias:

1. **Palavras vagas:** “talvez”, “poderia”, “apenas”, “muito” e “basicamente”
2. **Exageros de marketing:** “revolucionar”, “revolucionário”, “mudança radical”, “desbloquear” e “poderoso”

Remover essas palavras leva o modelo a trocar afirmações vagas por detalhes específicos. Em vez de *“esta ferramenta é poderosa e revolucionária”*, você recebe algo como *“esta ferramenta reduziu nosso tempo de implantação de quatro horas para vinte minutos”*.

**Sem hashtags**

Hashtags raramente ajudam fora do Instagram ou do Twitter. No LinkedIn, parecem spam. *A maioria dos modelos as acrescenta por padrão mesmo assim.*

**Sem “em conclusão” ou expressões parecidas**

Essas frases aumentam o texto sem acrescentar informação. **Uma boa redação não precisa anunciar que está terminando.**

## Adapte a instrução ao tipo de conteúdo

A instrução padrão foi pensada para textos curtos: publicações em redes sociais, atualizações no LinkedIn, e-mails e introduções de blog.

Se você escreve **textos longos**, como relatórios, sínteses de pesquisa ou documentação técnica, remova estas linhas:

- `DEVE ser direto e informativo.`
- `DEVE usar frases curtas e marcantes.`
- `DEVE usar listas com marcadores em publicações para redes sociais.`

Textos longos precisam de parágrafos mais desenvolvidos. **As outras regras continuam valendo.**

**Inclua sua própria voz**

A instrução remove padrões evidentes de IA. *Ela não acrescenta a sua personalidade.*

Para avançar, **adicione ao fim da instrução um pequeno exemplo de texto seu**. Use de três a cinco parágrafos escritos por você e identifique-os como exemplo de estilo. O modelo vai captar seu ritmo, suas escolhas de palavras e seu tom.

Você terá um texto mais limpo e menos genérico.

## Como salvar no ChatGPT

**Você não precisa colar esta instrução em todas as conversas.** O ChatGPT permite salvar instruções personalizadas, aplicadas automaticamente a cada nova conversa.

**Etapas:**

1. Abra o ChatGPT e clique no seu nome de perfil no canto inferior esquerdo
2. Clique em **“Personalizar o ChatGPT”**
3. Encontre o campo **“Quais características o ChatGPT deve ter?”**
4. Cole a instrução nesse campo
5. Reduza o texto para caber no **limite de 1.500 caracteres**, se necessário
6. Clique em **“Salvar”**

Depois de salvar, abra uma nova conversa e peça ao ChatGPT para escrever algo. *A resposta deve mudar de forma perceptível: frases mais curtas, sem travessões, exageros ou hashtags.*

As instruções personalizadas se aplicam automaticamente a toda nova conversa. Você não precisa se lembrar de acrescentar a instrução a cada pedido.

**Fique dentro do limite de caracteres**

A instrução completa passa um pouco de 1.500 caracteres. Para reduzi-la:

- Remova as regras que menos importam para você
- Encurte a lista de palavras proibidas e mantenha as mais importantes
- **Mantenha as regras sobre travessões, Markdown e asteriscos**, pois elas tratam dos problemas mais comuns

Outros LLMs, como Claude e Gemini, oferecem recursos semelhantes de instruções de sistema. A mesma instrução funciona nessas interfaces com pequenos ajustes de formatação.

## Um teste prático

Para ver a diferença com clareza, **faça o mesmo pedido duas vezes**.

Primeiro, sem a instrução: peça ao ChatGPT uma publicação curta para o LinkedIn sobre um tema que você conhece bem.

Depois, acrescente a instrução e repita o pedido.

Compare as respostas lado a lado. Observe:

- Quantos **travessões** aparecem
- Se a publicação termina com **hashtags**
- Se aparecem frases como *“no cenário atual”* ou *“é hora de desbloquear”*
- Se as frases ficam **mais curtas e diretas**

*A diferença aparece em um único teste.* A versão revisada é mais rápida de ler, faz afirmações mais fortes sem enrolação e não parece imediatamente gerada por um modelo.

## O que esta instrução não corrige

**Nenhuma instrução remove por completo os padrões de escrita de IA.**

Um modelo que segue estas regras ainda pode:

- Escolher palavras um pouco artificiais em certos trechos
- Repetir uma estrutura de frase ao longo de um texto extenso
- Não reproduzir a experiência e as opiniões que vêm de ter vivido o assunto sobre o qual você escreve

*A instrução é um ponto de partida, não o resultado final.* Ela elimina os padrões mais fáceis de notar. Para chegar a uma escrita natural, você ainda precisa revisar e editar a resposta.

**Use a instrução para obter um primeiro rascunho mais limpo. Acrescente sua perspectiva antes de publicar.**

## Resumo

A escrita de IA é reconhecível porque os modelos recorrem a padrões aprendidos: travessões, negrito, palavras promocionais e aberturas genéricas. Esses padrões fazem os leitores pensar que ninguém colocou ideias próprias no conteúdo.

A instrução acima reduz esses padrões ao definir regras claras sobre o que evitar. **Ao salvá-la nas instruções personalizadas do ChatGPT, você inicia cada conversa com essas regras aplicadas.**

Comece com a instrução completa. Remova o que não serve ao seu tipo de escrita. Inclua amostras da sua escrita para aproximar a resposta da sua voz. Edite o resultado antes de publicar.

*O objetivo não é fazer a IA parecer humana. É apresentar suas ideias sem distrair o leitor com hábitos óbvios de máquina.*

## Fonte

Este artigo se baseia no prompt e no guia originais publicados por Sabrina Ramonov: [Melhor prompt de IA para tornar textos de IA mais naturais](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing).

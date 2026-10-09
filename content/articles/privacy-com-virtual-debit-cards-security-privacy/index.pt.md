---
title: "Cartões Virtuais Privacy.com: Como Funciona a Privacidade no Pagamento"
date: 2023-09-03
lastmod: 2026-10-08
toc: true
draft: false
description: O que é armazenado em um cartão de pagamento, por que a tarja magnética é a parte mais fraca dele, o que um comerciante vê quando você paga com um número virtual e como os tipos e limites de cartões da Privacy.com funcionam na prática.
genre:
- Segurança no Pagamento
- Privacidade Digital
- Cartões Virtuais
- Privacidade Financeira
- Prevenção de Fraudes
- Segurança do Consumidor
tags:
- privacy.com
- cartões virtuais
- cartões de débito virtuais
- cartões de uso único
- cartões bloqueados para comerciante
- cartões bloqueados por categoria
- tokenização
- token de rede
- pan
- cvv
- clonagem de cartão
- tarja magnética
- pista 1
- pista 2
- segurança de cartão de pagamento
- fraude com cartão de crédito
- gerenciamento de assinaturas
- limites de gastos
- pci dss
- soc 2
- fraude em cartão não presente
- privacidade financeira
- privacidade no pagamento
- número de cartão virtual
- cartão mascarado
- controles do cartão
cover: /img/cover/privacy_virtual_cards.webp
coverAlt: Uma ilustração digital mostrando um cartão virtual protegido por um escudo protegendo um símbolo de cadeado, representando a segurança e privacidade oferecidas pelos cartões de débito virtuais.
coverCaption: Proteja, Controle e Garanta a Segurança de Suas Transações Online.
ref:
- /magnetic-stripe-decoder
- /articles/personal-security-checklist-prioritized-2026
- /personal-security-course/personal-finance
---

**Um cartão virtual faz uma coisa específica: ele altera o que o comerciante recebe, não o que seu banco sabe.** Este é todo o mecanismo, e entendê-lo explica tanto a proteção que você obtém quanto a proteção que não obtém.

A maioria das coberturas trata os cartões virtuais como uma ferramenta geral de privacidade e ignora os detalhes técnicos. Este artigo cobre o que é armazenado em um cartão, por que a tarja magnética é o ponto fraco e como os tipos de cartões da Privacy.com se comportam na prática.

*O benefício prático é estreito e real: um número roubado torna-se inútil para um ladrão, porque só funciona no comerciante para o qual foi emitido.*

## A Resposta Curta

| Pergunta | Resposta Curta |
|---|---|
| **O que um cartão virtual altera?** | O número que o comerciante armazena. Seus dados reais do cartão nunca chegam até ele |
| **A transação é privada?** | Não. Seu banco, a rede e o emissor ainda a veem |
| **O que impede que uma violação te prejudique?** | Um número bloqueado para comerciante ou de uso único, que falha em qualquer outro lugar |
| **Qual é a parte mais fraca de um cartão físico?** | A tarja magnética, que armazena os dados completos da faixa sem criptografia |
| **Ele gera crédito?** | Não. Estes não são contas de crédito e nenhuma consulta de crédito ocorre |
| **Quem pode usar a Privacy.com?** | Cidadãos ou residentes legais dos EUA, 18+, com conta corrente em banco ou cooperativa de crédito dos EUA |

## O Que Está em um Cartão de Pagamento

**Três coisas autorizam uma transação sem cartão presente: o número da conta principal, a data de validade e o valor de verificação.**

| Elemento | Comprimento | Origem |
|---|---|---|
| **Número da Conta Principal (PAN)** | Até 19 dígitos | O emissor, com dígitos iniciais identificando a bandeira e o banco |
| **Validade** | Quatro dígitos no formato MM/AA | O emissor |
| **CVV ou CVC** | Três ou quatro dígitos | Derivado do PAN, validade e uma chave que só o emissor possui |
| **Nome do titular** | Até 26 caracteres | Aparece apenas na Pista 1 da tarja magnética |

**O PAN não é uma sequência aleatória.** O primeiro dígito identifica a bandeira, os próximos vários identificam o banco emissor e o restante identifica a conta. A estrutura permite que um número de cartão seja verificado quanto à plausibilidade sem contato externo, e explica por que o dígito de verificação Luhn detecta um único dígito trocado.

**O CVV é o que prova que alguém segurou o cartão fisicamente** quando ele foi emitido. Ele não é armazenado na tarja magnética, que é exatamente por isso que um dispositivo de clonagem que copia a tarja nunca o obtém.

*Inspecione tudo isso você mesmo com o **[Decodificador e Codificador de Tarja Magnética](/magnetic-stripe-decoder/)**, que analisa a Pista 1 e a Pista 2, decodifica os dígitos do código de serviço e re-codifica o resultado. Ele roda inteiramente no seu navegador, o que é importante porque este é o conteúdo completo de um cartão de pagamento.*

{{< figure src="payment-card-data-anatomy-pan-cvv-tracks.webp" alt="Diagrama mostrando os elementos de um cartão de pagamento incluindo o número da conta principal, data de validade, CVV e as três faixas da tarja magnética com o que cada uma contém" >}}

## Por Que a Tarja Magnética É o Ponto Fraco

**A tarja armazena dados da conta em texto simples, e qualquer leitor compatível os lê.**

Uma tarja magnética contém até três faixas. A Pista 1 carrega o PAN, o nome do titular, a validade e um código de serviço de três dígitos, sendo a única faixa que contém texto alfabético. A Pista 2 carrega o PAN, validade e código de serviço em uma codificação numérica mais densa, e **a Pista 2 é o que quase todos os terminais de ponto de venda leem.** A Pista 3 é praticamente não usada pelas principais redes e muitas vezes nem está presente no cartão.

O código de serviço vale a pena entender, pois descreve o uso permitido do cartão. O primeiro dígito cobre regras de intercâmbio, o segundo cobre o tratamento da autorização e o terceiro cobre a gama de serviços. Um cartão codificado `201` permite intercâmbio internacional, não precisa de caminho especial de autorização e não tem restrições de serviço.

A história explica por que a tarja durou tanto tempo. Em 1969, um engenheiro da IBM chamado Forrest Parry tentou colar fita magnética a um cartão plástico e não conseguiu fazê-la aderir sem danificá-la. Sua esposa sugeriu usar um ferro de passar roupa, e o calor fixou a fita ao cartão. A improvisação virou padrão por mais de meio século.

Dois desenvolvimentos estão encerrando isso:

| Marco | Status |
|---|---|
| **Mastercard anunciou a remoção da tarja** | Até 2033, nenhum cartão de crédito ou débito Mastercard terá tarja |
| **Europa** | As tarjas começaram a desaparecer dos cartões Mastercard em 2024 |
| **Estados Unidos** | Bancos deixarão de emitir a partir de 2027 |

*A tarja foi substituída pelo chip e pagamento por aproximação porque copiar uma não exige habilidade além de possuir um leitor. Nossa **[ferramenta de tarja magnética](/magnetic-stripe-decoder/)** mostra quão poucos dados são necessários para reconstruir uma faixa funcional.*

{{< figure src="magnetic-stripe-track-layout-track1-track2.webp" alt="Diagrama de uma tarja magnética mostrando a posição física das faixas um, dois e três, com o layout dos campos de cada faixa incluindo sentinelas, PAN, nome, validade e código de serviço" >}}

## Como Ler Dados da Faixa

**Uma sequência da tarja magnética é uma sequência de campos, não um segundo número de cartão.** O leitor encontra o sentinela inicial, separa os campos, lê a validade e o código de serviço, depois verifica o sentinela final e o LRC.

| Faixa | Início | Campos principais | Fim | Conjunto de caracteres |
|---|---|---|---|---|
| **Faixa 1** | `%` | Código de formato, PAN, nome, validade, código de serviço, dados discricionários | `?` mais LRC | ALFA de seis bits, portanto carrega letras |
| **Faixa 2** | `;` | PAN, validade, código de serviço, dados discricionários | `?` mais LRC | BCD de quatro bits, portanto carrega dígitos e um pequeno conjunto de pontuação |

Os sentinelas opcionais identificam os limites físicos do registro. Um decodificador frequentemente os omite ao exibir os campos, mas um codificador físico precisa do formato completo do registro esperado pelo leitor.

### Exemplo da Faixa 1

Este é um exemplo sintético. Usa o PAN padrão de teste da ferramenta e nome falso, validade, código de serviço e dados discricionários. Não é um cartão Privacy.com e não são dados de pagamento válidos.

```text
%B4111111111111111^TEST/USER^2912501000000000?
```

Leia da esquerda para a direita:

| Segmento | Valor | Significado |
|---|---|---|
| **Sentinela de início** | `%` | Início do registro da Faixa 1 |
| **Código de formato** | `B` | Formato de cartão financeiro B |
| **PAN** | `4111111111111111` | Número primário da conta sintético |
| **Separador de campo** | `^` | Fim do PAN e início do nome |
| **Nome** | `TEST/USER` | Sobrenome, separador, nome |
| **Separador de campo** | `^` | Fim do nome e início dos campos da transação |
| **Validade** | `2912` | Dezembro de 2029 no formato AA/MM |
| **Código de serviço** | `501` | Intercâmbio nacional, processamento normal, sem restrições |
| **Dados discricionários** | `0000000` | Preenchimento definido pelo emissor neste exemplo |
| **Sentinela de fim** | `?` | Dados da Faixa 1 terminam antes do LRC |

O registro codificado real também carrega um caractere LRC após o sentinela de fim quando o leitor o espera. A forma de texto visível é útil para estudar a estrutura. A representação em nível de bit também carrega paridade ímpar para cada caractere.

### Exemplo da Faixa 2

A Faixa 2 remove o nome e o código de formato. Os mesmos valores sintéticos tornam-se:

```text
;4111111111111111=291250100000000?
```

| Segmento | Valor | Significado |
|---|---|---|
| **Sentinela de início** | `;` | Início do registro da Faixa 2 |
| **PAN** | `4111111111111111` | Número primário da conta sintético |
| **Separador** | `=` | Fim do PAN e início dos campos da transação |
| **Validade** | `2912` | Dezembro de 2029 no formato AA/MM |
| **Código de serviço** | `501` | Mesmo código de serviço sintético da Faixa 1 |
| **Dados discricionários** | `0000000` | Preenchimento definido pelo emissor neste exemplo |
| **Sentinela de fim** | `?` | Dados da Faixa 2 terminam antes do LRC |

**A Faixa 2 é mais curta porque não tem o nome do titular do cartão.** Muitos terminais leem a Faixa 2 para transações comuns de deslize, enquanto a Faixa 1 fornece o campo de nome quando um leitor o solicita.

### Dígitos do Código de Serviço

**Os três dígitos do código de serviço descrevem o comportamento do terminal e da autorização.** Eles não contêm o CVV, e alterá-los em um cartão real sem autorização do emissor produz uma credencial de pagamento malformada ou enganosa.

| Dígito | Valores | O que descreve |
|---|---|---|
| **Primeiro** | `0`, `1`, `2`, `5`, `6`, `7`, `9` | Regras de intercâmbio e preferência por chip |
| **Segundo** | `0`, `1`, `2`, `4` | Caminho de autorização |
| **Terceiro** | `0` até `7` | Restrições de PIN, dinheiro, bens e serviços |

**O primeiro dígito** cobre intercâmbio e preferência por chip:

| Valor | Significado |
|---|---|
| `0` | Uso nacional |
| `1` | Intercâmbio internacional permitido |
| `2` | Intercâmbio internacional, usar IC (chip) quando possível |
| `5` | Apenas intercâmbio nacional, exceto sob acordo bilateral |
| `6` | Apenas intercâmbio nacional, exceto sob acordo bilateral, usar IC quando possível |
| `7` | Sem intercâmbio, exceto sob acordo bilateral (circuito fechado) |
| `9` | Teste |

**O segundo dígito** cobre o tratamento da autorização:

| Valor | Significado |
|---|---|
| `0` | Autorização normal |
| `1` | Autorização normal |
| `2` | Contatar emissor por meios online |
| `4` | Contatar emissor por meios online, exceto sob acordo bilateral |

**O terceiro dígito** cobre restrições de serviço:

| Valor | Significado |
|---|---|
| `0` | Sem restrições, PIN obrigatório |
| `1` | Sem restrições |
| `2` | Apenas bens e serviços (sem dinheiro) |
| `3` | Apenas ATM, PIN obrigatório |
| `4` | Apenas dinheiro |
| `5` | Apenas bens e serviços (sem dinheiro), PIN obrigatório |
| `6` | Sem restrições, usar PIN quando possível |
| `7` | Apenas bens e serviços (sem dinheiro), usar PIN quando possível |

Por exemplo, `201` significa intercâmbio internacional com uso de chip quando possível, processamento normal de autorização e sem restrições de serviço. O decodificador expõe cada dígito separadamente para que você não precise memorizar a tabela.

### LRC e Paridade

**O LRC é um caractere de verificação, não outro campo para inventar.** O codificador faz XOR do valor dos dados de cada caractere desde o sentinela de início até o sentinela de fim. Ele converte o resultado de volta para o intervalo de caracteres imprimíveis da faixa e reporta os bits de paridade ímpar codificados separadamente.

A Faixa 1 usa um conjunto de caracteres ALFA de seis bits. Seu valor de dados é o código ASCII menos `0x20`. A Faixa 2 usa um conjunto de caracteres BCD de quatro bits. Seu valor de dados é o nibble baixo do código ASCII. Aplicar o mapeamento da Faixa 1 à Faixa 2 produz o LRC errado.

A opção **Incluir LRC calculado** do decodificador adiciona o caractere LRC imprimível à saída. Sua decomposição também mostra o padrão de bits do LRC com paridade ímpar. Use isso para aprender como um leitor verifica o registro, não para burlar os controles do emissor.

## Escrevendo Cartões Sintéticos para Teste

**Use o decodificador para escrever strings de teste, não cartões de pagamento reais.** A ferramenta aceita campos, reconstrói as Faixas 1 e 2, adiciona sentinelas opcionais e calcula o LRC. Ela roda localmente no navegador.

1. Abra o **[Decodificador e Codificador de Faixa Magnética](/magnetic-stripe-decoder/)**.
2. Selecione **Carregar Cartão de Teste**. Isso preenche a ferramenta com o PAN sintético `4111111111111111`, o nome `TEST/USER`, validade `2912`, código de serviço `201` e dados discricionários de teste.
3. Ative **Incluir sentinelas de início e fim** para exibir os limites físicos do registro.
4. Ative **Incluir LRC calculado** para anexar o caractere de verificação calculado.
5. Ative **Dividir dados discricionários em PVKI, PVV e CVV** apenas para ver como um campo sintético de nove dígitos é exibido. Esses rótulos são convenções do emissor, não um layout universal da Faixa 1 ou Faixa 2.
6. Altere o nome, validade, código de serviço ou dados discricionários sintéticos. A saída é atualizada enquanto você digita.
7. Compare os campos decodificados com as strings geradas. Limpe os campos quando terminar.

Para um exercício sintético da Faixa 1, use:

```text
PAN: 4111111111111111
Surname: TEST
First name: USER
Expiry: 12/29
Service code: 201
Discretionary data: 000000000
```

Para um exercício sintético da Faixa 2, use o mesmo PAN, validade, código de serviço e um campo discricionário numérico. A string gerada da Faixa 2 omite o nome porque a Faixa 2 não possui campo de nome.

**Não copie um PAN, validade, CVV ou valor discricionário ativo do Privacy.com para um cartão gravável.** O Privacy.com descreve seu produto como números de cartão virtuais criados através do seu site ou aplicativo. Sua página oficial não apresenta o serviço como um sistema de gravação de faixa magnética, enquanto um número de cartão virtual não é prova de um registro físico autorizado pelo emissor. Um cartão de teste gravável contendo uma credencial ativa cria um instrumento de pagamento duplicado e viola os termos do emissor ou regras de pagamento.

O limite seguro é simples: use a amostra sintética embutida na ferramenta, use um cartão de laboratório com valores fictícios e use um cartão físico aprovado pelo emissor quando precisar pagar pessoalmente. Não tente transformar um cartão virtual do Privacy.com em um cartão físico para deslizar.

## O Que um Cartão Virtual Muda

**Um cartão virtual é um segundo número que fica na frente do primeiro.**

Quando você paga com um cartão virtual, o comerciante recebe um número, uma validade e um CVV pertencentes ao cartão virtual. Seu PAN real nunca chega até eles. Na prática, a mudança aparece após uma violação:

| Cenário | Com Seu Cartão Real | Com um Cartão Virtual Bloqueado para o Comerciante |
|---|---|---|
| **Banco de dados do comerciante vazado** | O número é válido em todos os lugares onde é aceito | O número falha em todos os outros comerciantes |
| **Assinatura que você cancelou** | A cobrança continua até você contestar | Você fecha o cartão e a cobrança falha |
| **Teste convertendo silenciosamente** | Cobrança indesejada no seu extrato | O limite ou fechamento a impede |
| **Detalhes do cartão vendidos em fórum** | Usável para fraude sem presença do cartão | Usável em um único comerciante, se for o caso |

**O que não muda** é tão importante quanto. Seu banco ainda vê a transação. A rede de cartões ainda a processa. O emissor ainda detém sua identidade, porque regras contra lavagem de dinheiro exigem verificação. **Um cartão virtual reduz a exposição do lado do comerciante. Não é uma forma de gastar anonimamente.**

*A distinção confunde as pessoas constantemente. Se seu modelo de ameaça inclui o emissor ou a rede, um cartão virtual não muda nada nisso.*

{{< figure src="virtual-card-merchant-shielding-flow.webp" alt="Diagrama mostrando um número de cartão virtual indo para o comerciante enquanto o número real do cartão permanece entre o titular e o banco emissor" >}}

## Os Três Tipos de Objeto em Forma de Cartão

A terminologia é usada de forma inconsistente, e a diferença importa quando você escolhe o que entregar a um comerciante.

| Tipo | Número do Cartão | Versão Física | Uso Típico |
|---|---|---|---|
| **Cartão digital** | Igual ao seu cartão físico | Sim | Adicionar seu cartão existente a uma carteira móvel |
| **Cartão virtual** | Diferente de qualquer cartão físico | Não | Compras online, assinaturas, comerciantes pontuais |
| **Cartão digital-primeiro** | Diferente, com cartão físico vinculado opcional | Opcional | Contas fintech onde o cartão físico não tem detalhes impressos |

**Uma carteira móvel usa um mecanismo totalmente diferente.** Quando você adiciona um cartão a uma carteira, a carteira armazena um token específico do dispositivo em vez do seu PAN, e o comerciante recebe o token. Isso é chamado de tokenização, e é por isso que pagar com o telefone é mais seguro do que entregar o plástico mesmo sem um cartão virtual.

*Tokenização de rede e cartões virtuais resolvem partes sobrepostas do mesmo problema. A tokenização protege o número em trânsito e em repouso. Um cartão virtual protege você do que o comerciante retém depois.*

## Tipos de Cartão Privacy.com

**O Privacy.com oferece quatro comportamentos de cartão, e eles não são intercambiáveis.**

| Tipo de Cartão | Comportamento | Melhor Para |
|---|---|---|
| **Uso Único** | Fecha automaticamente após uma transação | Compras pontuais e comerciantes desconhecidos |
| **Bloqueado para Comerciante** | Bloqueia para o primeiro comerciante que o cobrar e falha em outros | Compras online do dia a dia |
| **Bloqueado por Categoria** | Restrito a uma categoria de gastos | Contenção de uma classe inteira de gastos |
| **Em Todos os Lugares** | Um cartão físico com o mesmo modelo de proteção | Compras presenciais |

**O bloqueio para comerciante é o mecanismo que carrega a maior parte do valor.** Um cartão bloqueado falha em qualquer comerciante que não seja aquele em que foi usado pela primeira vez, o que significa que uma violação naquele comerciante gera um número inútil em qualquer outro lugar.

**Uso único é a opção mais forte onde se aplica.** Um cartão que fecha após uma cobrança não pode ser reutilizado, e elimina a necessidade de lembrar de fechá-lo depois.

Dois detalhes operacionais que valem a pena saber:

- **Cartões compartilhados bloqueiam para o primeiro comerciante com que são usados**, então compartilhar um com um familiar ou funcionário ainda carrega a restrição do comerciante.
- **Um cartão é pausado em vez de fechado.** Pausar é reversível, o que é útil quando você quer parar uma assinatura temporariamente sem perder os detalhes do cartão.

## Limites e Controles de Gastos

**Todo cartão tem um limite de gasto, que é um controle separado do bloqueio para comerciante.**

| Controle | O Que Evita |
|---|---|
| **Limite por transação** | Uma única cobrança maior do que você autorizou |
| **Limite mensal** | Acúmulo de cobranças durante um período de faturamento |
| **Pausar** | Qualquer cobrança, de forma reversível |
| **Fechar** | Qualquer cobrança futura, permanentemente |

**Defina tanto um limite por transação quanto um limite mensal em qualquer cartão vinculado a uma assinatura.** Um comerciante que aumenta silenciosamente seu preço atinge o limite em vez do seu saldo, e você percebe isso por uma cobrança falhada em vez de uma linha faltando no extrato.

*Nosso módulo **[Segurança Financeira Pessoal](/personal-security-course/personal-finance/)** coloca isso ao lado de congelamentos de crédito e tokenização de cartão como os três controles que limitam o que um único comerciante comprometido alcança.*

## Planos e O Que Cada Um Desbloqueia

Privacy.com oferece um plano gratuito junto com três planos pagos. Preços e limites de recursos mudam, então confirme os termos atuais antes de assinar.

| Plano | Preço | Adições Notáveis |
|---|---|---|
| **Pessoal (gratuito)** | $0 | Cartões virtuais, bloqueio por comerciante, limites de gastos, sem taxa em transações domésticas |
| **Plus** | $5/mês | Cartões por categoria, notas nos cartões para organizar gastos |
| **Pro** | $10/mês | Cashback em compras qualificadas, cartões físicos Everywhere |
| **Premium** | $25/mês | Tudo do Pro, com limite mensal de criação de cartões aumentado para 60 |

**O plano gratuito cobre o benefício principal de segurança.** Bloqueio por comerciante, cartões de uso único e limites de gastos são os mecanismos que reduzem a exposição, e estão disponíveis sem custo. Os planos pagos adicionam organização e conveniência, não proteção adicional.

**As taxas para transações estrangeiras variam por plano.** O plano gratuito cobra 3% em transações estrangeiras com mínimo de $0,50, enquanto os planos pagos não cobram.

## O Que o Privacy.com Não Faz

**Ser claro sobre os limites é mais útil do que uma lista de recursos.**

| Limitação | Detalhe |
|---|---|
| **Não torna você anônimo** | Sua identidade é verificada no cadastro e o emissor a mantém |
| **Não oculta a transação do seu banco** | Seu banco vê a transferência de fundos, e a rede vê a cobrança |
| **Não constrói crédito** | Não são contas de crédito, e não há consulta de crédito |
| **É exclusivo para os EUA** | Requer cidadania ou residência legal nos EUA e conta bancária ou cooperativa de crédito nos EUA |
| **Exige verificação de identidade** | Checagens Know Your Customer são obrigatórias por regras anti-lavagem de dinheiro |
| **Não cobre todos os comerciantes** | Alguns comerciantes bloqueiam faixas de cartões pré-pagos e virtuais |

**O ponto sobre bloqueio por comerciantes importa na prática.** Alguns serviços de assinatura e companhias aéreas rejeitam faixas de cartões associadas a cartões virtuais ou pré-pagos, e nenhuma configuração resolve o problema. Mantenha um cartão real disponível como reserva nesses casos.

*Resumo honesto: um cartão virtual é um controle de contenção para exposição ao comerciante, não uma ferramenta de anonimato. Se você precisa de anonimato, é um problema diferente com ferramentas diferentes.*

## Quem Emite o Cartão e Por Que Isso Importa

**Um cartão virtual ainda é um cartão real, emitido por um banco real, sob uma licença de esquema real.**

| Detalhe | Valor |
|---|---|
| **Banco emissor** | Patriot Bank, N.A., Membro FDIC |
| **Licenças de esquema** | Mastercard e Visa |
| **Onde é aceito** | Em qualquer lugar que Mastercard e Visa sejam aceitos |
| **Financiamento** | Transferido da sua conta corrente vinculada nos EUA |

**É por isso que a proteção é genuína.** O cartão tem as mesmas proteções do esquema que qualquer outro produto Mastercard ou Visa, o que significa que direitos de estorno e processos de disputa por fraude se aplicam normalmente. Não é um cartão presente ou crédito fechado de loja.

Duas certificações valem ser mencionadas porque são verificáveis independentemente, e não apenas alegações de marketing:

- **Conformidade PCI-DSS**, que é o padrão da indústria de cartões de pagamento para manuseio de dados do portador
- **SOC 2 Tipo II**, que é um relatório auditado cobrindo controles de segurança ao longo do tempo, não uma afirmação pontual

**Sobre o modelo de negócios:** a empresa declara que ganha comissões de intercâmbio dos comerciantes e não vende dados dos clientes para anunciantes ou terceiros. Este é o mesmo modelo de receita de qualquer outro emissor de cartão, o que vale entender em vez de tratar como algo incomum.

*A razão prática para verificar o banco emissor é a verificação. Qualquer um pode alegar operar um programa de cartões, e o nome do emissor no cartão é o que você confirma com o banco indicado na documentação.*

Inspecione o esquema e banco pelo prefixo do PAN usando o **[Decodificador de Faixa Magnética](/magnetic-stripe-decoder/)**, que informa a faixa principal do esquema e valida o dígito verificador Luhn.

## Usando Cartões Virtuais Corretamente

**Os controles só ajudam se você configurá-los.** Seis hábitos trazem a maior parte do benefício.

1. **Bloqueie cada cartão para um comerciante** a menos que haja motivo para não fazer isso. O bloqueio é o que torna um número vazado inútil.
2. **Use cartões de uso único para qualquer coisa desconhecida**, incluindo testes e compras pontuais em sites menores.
3. **Defina ambos os limites de gastos** em cartões de assinatura, para que um aumento de preço falhe em vez de cobrar.
4. **Nomeie cada cartão com o nome do comerciante**, para que a lista de transações seja legível e cobranças inesperadas se destaquem.
5. **Pause em vez de fechar** quando planejar retomar um serviço, e feche quando não for retomar.
6. **Mantenha um cartão real para comerciantes que rejeitam faixas virtuais**, para que um bloqueio no checkout não vire emergência.

> **Erro comum: tratar um cartão virtual como substituto para revisar seus extratos.** O bloqueio por comerciante impede uma classe de danos. Não detecta conta comprometida no banco, transferência não autorizada ou cobrança fraudulenta no cartão real por trás dele.

## Principais Conclusões

- **Um cartão virtual altera o número que o comerciante armazena.** Seu PAN real nunca chega a eles, que é o mecanismo principal.
- **Não torna a transação privada.** Seu banco, a rede e o emissor ainda a veem, e a verificação de identidade é obrigatória.
- **O bloqueio por comerciante é o recurso de maior valor**, porque um número vazado falha em todos os outros lugares.
- **O plano gratuito inclui os controles de segurança.** Planos pagos adicionam organização e conveniência, não proteção.
- **A faixa magnética armazena dados do cartão em texto simples** e será removida até 2033, com bancos dos EUA parando emissão em 2027.
- **O CVV não está na faixa magnética**, por isso um skimmer que copia as faixas ainda não tem o que muitos comerciantes online exigem.
- **Alguns comerciantes rejeitam faixas de cartões virtuais.** Mantenha um cartão real como reserva.
- **Verifique o banco emissor** em vez de confiar em alegações do programa de cartão, e confira o prefixo do PAN você mesmo.

## Próximos Passos

1. **Inspecione os dados da faixa do seu próprio cartão** e veja exatamente o que uma tarja magnética carrega: **[Decodificador e Codificador de Tarja Magnética](/magnetic-stripe-decoder/)**
2. **Congele seu crédito** se ainda não o fez, pois é o controle mais eficaz contra fraudes em novas contas: **[Segurança Financeira Pessoal](/personal-security-course/personal-finance/)**
3. **Aplique a disciplina de priorização** para decidir quanto esforço isso merece na sua situação: **[Lista de Verificação Prioritária de Segurança Pessoal](/articles/personal-security-checklist-prioritized-2026/)**
4. **Revise os planos e termos atuais do Privacy.com** antes de assinar: **[Privacy.com](https://www.privacy.com/virtual-card)**
5. **Verifique se seus dados já aparecem em alguma violação** antes de presumir que não foi afetado: **[Have I Been Pwned](https://haveibeenpwned.com)**
6. **Leia a lista de verificação de segurança de pagamentos** para o equivalente organizacional: **[Lista de Verificação de Resposta a Incidentes](/checklists/incident-response-checklist/)**

## Referências

1. [Privacy.com - o que são cartões virtuais, bloqueio por comerciante e limites de gastos](https://www.privacy.com/virtual-card)
2. [Cartão digital - Wikipedia, abordando cartões digitais versus virtuais, faixas magnéticas, códigos de serviço, paridade e LRC](https://en.wikipedia.org/wiki/Digital_card)
3. [ISO/IEC 7813:2006 - cartões de identificação, cartões para transações financeiras, estrutura dos dados das faixas 1 e 2](https://webstore.iec.ch/en/publication/11605)
4. [ISO/IEC 7813 - layout detalhado dos campos da faixa, incluindo sentinelas e códigos de serviço](https://en.wikipedia.org/wiki/ISO/IEC_7813)
5. [PCI Security Standards Council - requisitos para ambiente de dados do portador do cartão](https://www.pcisecuritystandards.org/)
6. [Consumer Financial Protection Bureau - relatórios e pontuações de crédito](https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/)
7. [Codificação de dados ANSI/ISO ALPHA, conjunto de caracteres da Faixa 1 e tabela de paridade](http://www.hhhh.org/~joeboy/resources/magcards/trackdata_ANSI-ISO_ALPHA.html)
8. [Caracteres ISO para cartão magnético, conjuntos da Faixa 1 e Faixa 2 lado a lado](https://www.pos.swiftpos.com.au/Help-SP/MagneticCardSwipeISOCharacters.html)
9. [Leitura de dados de cartão magnético, um passo a passo prático com escaneamento ao vivo do cartão](https://blog.j2i.net/2024/06/18/reading-magnetic-card-data/)

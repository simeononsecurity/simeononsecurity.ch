---
title: "ATS Resume Improver: Otimizador de Currículos com IA Gratuito"
date: 2026-07-22
lastmod: 2026-11-13
toc: true
draft: false
description: "ATS Resume Improver é uma ferramenta gratuita, de código aberto e executada no cliente para analisar, pontuar, comparar, otimizar e exportar currículos com modelos na nuvem ou locais."
genre: ["Ferramenta de carreira", "Projetos de código aberto", "Inteligência artificial", "Tecnologia de privacidade", "Ferramenta para desenvolvedores", "Busca de emprego", "Produtividade"]
tags: ["ATS Resume Improver", "Otimização para ATS", "Analisador de currículo", "Currículo com IA", "Currículo OpenAI", "Currículo Claude", "IA local Ollama", "Hospedagem própria", "Foco em privacidade", "Ferramentas para busca de emprego", "Análise de lacunas de palavras-chave", "Carta de apresentação", "Pontuação de currículo", "React", "TypeScript", "Docker", "Vite", "Código aberto", "Exportação PDF", "Exportação DOCX", "Analisador de currículo", "Ferramentas de carreira", "Preparação para entrevistas", "Estimador salarial", "Detecção do tipo de currículo", "Pontuação ATS", "Ferramenta gratuita para currículo", "GitHub", "Sem coleta de dados"]
cover: "/img/cover/ai-resume-optimizer-self-hosted-ats-analysis.webp"
coverAlt: "Um laptop moderno sobre uma mesa exibe uma interface colorida de otimização de currículo com gráficos, diante de um fundo azul-marinho escuro."
coverCaption: "ATS Resume Improver analisa e otimiza currículos inteiramente no cliente, sem coletar dados."
canonical: "https://simeononsecurity.com/articles/ats-resume-improver-ai-powered-resume-optimizer/"
---

**Gratuito, de código aberto e pronto para hospedagem própria. Seu currículo não chega a nenhum servidor, a menos que você use um provedor de IA. Mesmo nesse caso, o texto vai diretamente ao provedor, não a nós.**

## O que é o ATS Resume Improver?

**[ATS Resume Improver](https://atsresumeimprover.netlify.app/)** é um otimizador de currículo que funciona no navegador. Ele analisa seu currículo em relação à descrição de uma vaga e ajuda a reduzir a diferença entre sua experiência e os critérios de avaliação dos sistemas de rastreamento de candidatos (ATS). O projeto usa React 19, Vite e TypeScript. **Todo o processamento e a pontuação acontecem no navegador**, sem servidor de backend.

O código-fonte está em **[repositório do ATS Resume Improver no GitHub](https://github.com/simeononsecurity/ats-resume-improver)**. Use a versão hospedada, implante sua própria cópia em um clique no Vercel, Netlify, Cloudflare ou GitHub Pages, ou execute localmente com Docker.

### O problema de privacidade que resolve

A maioria dos serviços de otimização de currículo envia seu documento aos próprios servidores, executa uma pontuação privada e retém os dados. ATS Resume Improver segue outro modelo.

| Modo | Dados que saem do seu dispositivo |
|------|------------------------|
| **Sem chave de IA** | Nenhum. Tudo funciona localmente no navegador. |
| **OpenAI / Anthropic** | O texto do currículo e a descrição da vaga vão diretamente à API do provedor de IA usando sua chave. Não há servidor intermediário. |
| **Ollama (no seu computador)** | Nenhum. O modelo roda no seu próprio computador. |

**As chaves de API ficam apenas na memória** e desaparecem quando você fecha a aba. Não há análise, rastreamento nem cookies.

______

## Principais recursos

### O que funciona sem uma chave de IA

Você não precisa de uma chave de API para obter resultados úteis. O modo sem chave inclui:

- **Envio do currículo**: PDF, DOCX, TXT ou Markdown
- **Extração do texto para ATS**: mostra exatamente o que o ATS lê no arquivo, inclusive as informações perdidas pela formatação
- **Detecção do tipo de currículo**: identifica o perfil mais próximo entre 7 opções e ajusta a ordem das seções
- **Detecção de seções e avisos de formatação**: aponta seções ausentes e formatos difíceis para o analisador
- **Pontuação ATS (0–100)** com detalhamento de 5 dimensões
- **Análise de lacunas de palavras-chave**: comparação baseada em regras com a descrição da vaga
- **Otimização ATS determinística**: reestruturação local baseada em regras
- **Visualizador de diferenças antes/depois**: mostra exatamente o que mudou
- **Exportação profissional em PDF, DOCX, TXT e Markdown**

### O que a IA adiciona

Conecte OpenAI, Anthropic Claude ou Ollama local para habilitar:

- **Análise semântica de palavras-chave**: entende o contexto, não apenas correspondências literais. Mostra a força da correspondência (forte, moderada ou parcial), o local onde aparece, a importância por palavra-chave (crítica, alta, média ou baixa) e um resumo narrativo da IA de 2 a 3 frases
- **Otimização de currículo com IA**: reescrita completa com instruções baseadas nas práticas recomendadas para ATS
- **Exportações aprimoradas por IA**: PDF e DOCX formatados pela IA antes do download
- **Geração de cartas de apresentação**: aplica regras de escrita natural que eliminam sinais típicos de texto gerado por IA (veja abaixo)
- **Previsão de perguntas para entrevista**: usa a descrição da vaga como base
- **Estimativa de faixa salarial**

______

## Detecção do tipo de currículo

O aplicativo classifica seu currículo em um de 7 perfis e ajusta a ordem das seções às expectativas de recrutadores e ATS para cada etapa da carreira:

| Perfil | Ideal para | Prioridade das seções |
|---------|----------|-----------------|
| 🏢 **Profissional experiente** | 5 anos ou mais, carreira linear | Experiência → Competências → Formação |
| 🌱 **Nível intermediário** | 2 a 5 anos | Experiência → Competências → Formação |
| 🎓 **Início de carreira** | 0 a 2 anos | Competências → Formação → Projetos → Experiência |
| 🎒 **Estudante / recém-formado** | Ainda cursando | Formação → Projetos → Competências → Experiência |
| 🔬 **Acadêmico / pesquisador** | Doutorado, publicações | Formação → Pesquisa → Publicações → Experiência |
| 📜 **Foco em certificações** | Certificações acima do diploma | Certificações → Competências → Experiência → Formação |
| 🔄 **Transição de carreira** | Intervalo ou mudança detectada | Resumo → Competências transferíveis → Formação → Experiência |

*A ordem das seções permanece consistente na otimização e nas exportações em PDF, DOCX, TXT e Markdown, não apenas na tela.*

______

## Análise semântica de palavras-chave com IA

É aqui que a ferramenta se diferencia de contadores básicos de palavras-chave. Quando você configura um provedor de IA, a análise passa da comparação literal para o raciocínio semântico:

| Dimensão | Sem IA | Com IA |
|-----------|-----------|---------|
| **Método de correspondência** | Apenas texto exato | Compreensão semântica do contexto |
| **Força da correspondência** | — | Classificações forte / moderada / parcial |
| **Contexto da correspondência** | — | “encontrado em Competências e 3 experiências profissionais” |
| **Importância da lacuna** | Todas as lacunas têm o mesmo peso | Crítica / alta / média / baixa |
| **Sugestões** | Dicas gerais | Sugestões práticas por palavra-chave |
| **Cobertura %** | Baseada na contagem de termos | Ponderada semanticamente |
| **Resumo** | — | Resumo narrativo de IA de 2 a 3 frases |

*A análise local baseada em regras continua imediata. Os resultados da IA são adicionados em segundo plano enquanto você revisa.*

______

## Provedores de IA compatíveis

Todas as chamadas de IA incluem instruções com base nas diretrizes da Harvard OCS e da Columbia CCE para currículos.

### OpenAI

| Modelo | Ideal para |
|-------|----------|
| **GPT-4.1 mini** (padrão) | Rápido e acessível, com alta qualidade. Recomendado. |
| GPT-4o mini | A opção clássica, rápida e acessível |
| GPT-4.1 | GPT-4.1 mais recente, com instruções bem seguidas |
| GPT-4o | Modelo principal de alta qualidade |
| GPT-4 Turbo | Janela de contexto ampla |
| GPT-3.5 Turbo | Opção mais rápida e barata |

**Custo estimado**: cerca de US$ 0,002 a US$ 0,05 por análise de currículo.

### Anthropic Claude

| Modelo | Ideal para |
|-------|----------|
| **Claude Sonnet 4.5** (padrão) | Rápido e inteligente. Recomendado. |
| Claude Opus 4.5 | Mais capaz, ideal para tarefas complexas |
| Claude Haiku 4.5 | Opção mais rápida e barata |
| Claude 3.5 Sonnet | Confiável e bem testado |
| Claude 3.5 Haiku | Rápido e acessível na versão 3.5 |

### Ollama (local / auto-hospedado)

Não é necessária uma chave de API. Execute o modelo no seu próprio hardware. Defina `OLLAMA_ORIGINS=*` para permitir o acesso do navegador.

| Modelo | Observações |
|-------|-------|
| **Llama 3.3** (padrão) | Modelo mais recente da Meta. Recomendado. |
| Llama 3.2 | Modelo da Meta |
| Mistral 7B | Rápido e capaz |
| Mixtral 8x7B | Mistura de especialistas |
| Qwen 2.5 | Modelo da Alibaba |
| DeepSeek R1 | Raciocínio avançado |
| Phi-4 | Modelo da Microsoft |
| Gemma 3 | Modelo do Google |

Executar Ollama localmente deixa toda a ferramenta sem conexão externa. Nenhum dado sai da sua máquina em nenhum momento.

______

## Escrita natural de cartas de apresentação

O gerador de cartas de apresentação aplica um guia de estilo para eliminar sinais típicos de texto produzido por IA. Inspirado na [estrutura de escrita natural de Sabrina Ramonov](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing), cada carta segue estas regras:

- **Sem travessões longos**: o sinal mais evidente de texto de IA é removido por completo
- **Mais de 50 palavras e expressões proibidas**: leverage, utilize, dive deep, delve, embark, game-changer, groundbreaking, cutting-edge, pivotal, tapestry, harness, moreover, in conclusion, it's worth noting, ever-evolving, landscape, testament, not only...but also, entre outras
- **Sem Markdown no corpo da carta**: sem asteriscos para negrito, hashtags ou ponto e vírgula
- **Voz ativa por padrão**: use a voz passiva apenas quando o agente da ação não importa
- **Contrações obrigatórias**: “I've”, “I'm”, “it's”, nunca “I have”, “I am”, “it is”
- **Variação no tamanho das frases**: alterna frases curtas e diretas com outras mais longas
- **Sem introduções vazias**: “É importante observar que X” vira apenas a afirmação sobre X
- **Detalhe concreto da vaga no primeiro parágrafo**: demonstra que a carta não veio de um modelo genérico

*O resultado parece escrito por uma pessoa porque as regras orientam o modelo a escrever dessa forma.*

______

## Qualidade das exportações

| Formato | O que inclui |
|--------|-------------|
| **PDF** | Tipografia profissional, divisores de seção, marcadores e cabeçalho de contato |
| **DOCX** | Documento Word bem estruturado (`Packer.toBlob`, compatível com navegador) |
| **TXT** | Texto simples com espaçamento consistente, seguro para ATS |
| **Markdown** | Arquivo `.md` estruturado com títulos e listas |

Com um provedor de IA configurado, a IA formata as exportações antes do download. Elas recebem o selo ✨ Aprimorado por IA.

______

## Opções de hospedagem própria

### Versão hospedada (sem configuração)

Use o aplicativo ativo em **[versão on-line do ATS Resume Improver](https://atsresumeimprover.netlify.app/)**. Não exige conta, cadastro ou cartão de crédito.

### Implantação na nuvem em um clique

| Plataforma | Link |
|----------|------|
| **Vercel** | Implantação no repositório em um clique |
| **Cloudflare Pages** | Implantação em um clique |
| **Netlify** | Implantação em um clique |
| **GitHub Pages** | Fork → Settings → Pages → GitHub Actions → implantação automática |

### Desenvolvimento local

```bash
git clone https://github.com/simeononsecurity/ats-resume-improver
cd ats-resume-improver

make install
make dev           # http://localhost:5173
```

### Docker (recomendado para ambientes reproduzíveis)

```bash
# Desenvolvimento: recarga automática em http://localhost:5173
make docker-dev

# Produção: nginx em http://localhost:8080
make docker-prod

# Desenvolvimento e Ollama juntos (stack local de IA completo)
make docker-dev-with-ollama
```

### Pilha Ollama totalmente offline

```bash
# Iniciar o contêiner Ollama (os modelos persistem após reinicializações)
make ollama

# Baixar um modelo
make ollama-pull MODEL=llama3.2

# Iniciar o app de desenvolvimento e o Ollama lado a lado
make docker-dev-with-ollama
```

Abra o aplicativo, vá ao painel de chave de API, selecione **Ollama (Local)**, defina a URL como `http://localhost:11434` e escolha um modelo. Nenhum dado sai da sua máquina.

______

## Pilha tecnológica

| Camada | Tecnologia |
|-------|-----------|
| **Framework** | React 19 + TypeScript |
| **Compilação** | Vite 8 |
| **Estilo** | Tailwind CSS v4 |
| **Ícones** | Lucide React |
| **Análise de PDF** | pdfjs-dist |
| **Análise de DOCX** | mammoth |
| **Exportação PDF** | jsPDF |
| **Exportação DOCX** | docx (`Packer.toBlob`) |
| **IA** | OpenAI · Anthropic Claude · Ollama |
| **Contêiner** | Docker + nginx (multietapa) + serviço Ollama |

Todo o fluxo de pontuação e análise (`atsAnalyzer.ts`, `keywordMatcher.ts`, `resumeTypeDetector.ts`) roda no navegador. As integrações de IA em `aiProvider.ts` chamam as APIs dos provedores diretamente pelo cliente, sem servidor proxy.

______

## Guia prático de uso

### Etapa 1: envie seu currículo

Envie um arquivo PDF, DOCX, TXT ou Markdown. Abra a aba **“O que o ATS vê”** para verificar se o analisador extraiu o conteúdo corretamente. Se faltarem seções ou o texto aparecer distorcido nessa visualização, o software de ATS dos recrutadores terá o mesmo problema.

### Etapa 2: cole a descrição da vaga

Cole o anúncio completo no painel Descrição da vaga. Anúncios mais completos produzem uma análise melhor de palavras-chave. Não remova a seção de requisitos.

### Etapa 3: revise sua pontuação ATS

O painel exibe uma pontuação geral de 0 a 100 e um detalhamento de 5 dimensões. O detalhamento mostra onde concentrar seus esforços. Problemas de formato reduzem uma dimensão, palavras-chave ausentes reduzem outra e descrições fracas da experiência reduzem uma terceira.

### Etapa 4: analise as lacunas de palavras-chave

A visualização Análise de palavras-chave mostra quais termos da descrição aparecem no currículo e quais faltam. Com a IA ativada, você recebe correspondência semântica e níveis de importância. Uma lacuna “Crítica” em uma competência técnica central merece mais atenção do que uma lacuna “Baixa” em um clichê sobre habilidades interpessoais.

### Etapa 5: otimize

- **Modo determinístico**: reestrutura o currículo com regras. É seguro, rápido e não tem custo de API.
- **Modo de IA**: reescrita completa com um modelo de linguagem e instruções baseadas nas práticas recomendadas para ATS.

Revise a **diferença antes/depois** para entender cada alteração antes de aceitá-la.

### Etapa 6: exporte

Exporte em PDF, DOCX, TXT ou Markdown. Com a IA ativada, ela formata a exportação para uma apresentação profissional. O modelo PDF usa tipografia e layout adequados para recrutadores.

______

## Integração de dicas para currículos

A ferramenta inclui uma referência complementar em `RESUME_TIPS.md` (também disponível no repositório GitHub) com informações sobre:

- Como os sistemas ATS pontuam currículos
- Regras de formatação importantes e formatos que prejudicam os analisadores
- Como escrever resumos, marcadores e seções de competências
- Estratégia para palavras-chave sem repetição excessiva
- Tom e estrutura de cartas de apresentação
- Lista de verificação antes do envio

*Leia o arquivo antes de usar a ferramenta para entender suas pontuações.*

______

## Perguntas frequentes

### A ferramenta armazena meu currículo?

Não. O aplicativo funciona inteiramente no cliente. Nenhum dado fica armazenado em um servidor. Os dados da sessão ficam na memória do navegador e desaparecem quando você fecha a aba.

### Minha pontuação ficou baixa. Devo me preocupar?

As pontuações ATS indicam uma direção, não uma aprovação ou reprovação. Uma pontuação 60 na ferramenta não significa que um ATS rejeitará seu currículo. Significa que há lacunas mensuráveis entre seu currículo e a descrição específica da vaga analisada. Use a pontuação para priorizar edições, não como veredito.

### Posso usar a ferramenta com várias descrições de vaga?

Sim. Cole uma nova descrição quando quiser. A análise de palavras-chave e a otimização serão refeitas para o novo anúncio. Cada análise é independente.

### A integração com Ollama funciona mesmo offline?

Sim, se Ollama estiver na sua máquina ou em uma máquina da sua rede local. O aplicativo envia texto à instância Ollama por HTTP. Nada vai para serviços externos.

### Qual é a precisão da detecção do tipo de currículo?

O detector usa heurísticas baseadas no conteúdo do currículo. Ele procura anos de experiência, indicadores de formação, seções de publicações ou pesquisa e sinais de intervalos na carreira. Funciona bem para a maioria dos currículos, mas pode errar em perfis incomuns. Você sempre pode ajustar a ordem das seções.

______

## Roteiro do projeto

Recursos em desenvolvimento ou planejados:

- Histórico de versões do currículo via IndexedDB
- Otimizador de perfil do LinkedIn
- Suporte ao provedor Google Gemini
- Modelos Ollama adicionais

O projeto usa a licença MIT e aceita pull requests. Abra uma issue antes de fazer alterações importantes.

______

## Conclusão

**ATS Resume Improver** preenche uma lacuna real: oferece análise séria de currículo sem repassar seus dados a terceiros. O modo sem chave fornece comentários imediatos e práticos sobre formatação e cobertura de palavras-chave. Ao adicionar uma chave de IA, você habilita raciocínio semântico, cartas de apresentação e preparação para entrevistas, por centavos por análise ou sem custo com Ollama.

A versão hospedada está em **[versão on-line do ATS Resume Improver](https://atsresumeimprover.netlify.app/)**. O código-fonte completo está em **[repositório do ATS Resume Improver no GitHub](https://github.com/simeononsecurity/ats-resume-improver)**.

Se você hospeda a ferramenta para sua própria busca de emprego ou quer ajustar os pesos de pontuação e as instruções para um setor específico, a configuração Docker e a estrutura simples do projeto facilitam criar e adaptar um fork.

______

## Curso de otimização de currículos

Para um guia estruturado e passo a passo sobre como aplicar o que a ferramenta avalia, leia o curso complementar:

**[Curso de otimização de currículos: supere os sistemas ATS e consiga mais entrevistas](/resume-optimization-course-start/)**. São 9 módulos sobre pontuação ATS, formatação, marcadores, palavras-chave, personalização, cartas de apresentação e lista de verificação antes do envio. Use a ferramenta junto com o curso para receber comentários imediatos em cada etapa.

______

## Referências

1. [ferramenta on-line](https://atsresumeimprover.netlify.app/)
2. [repositório do código-fonte](https://github.com/simeononsecurity/ats-resume-improver)
3. [Dicas para currículos — RESUME_TIPS.md](https://github.com/simeononsecurity/ats-resume-improver/blob/main/RESUME_TIPS.md)
4. [Sabrina Ramonov — melhor prompt de IA para escrita natural](https://www.sabrina.dev/p/best-ai-prompt-to-humanize-ai-writing)
5. [documentação da API da OpenAI](https://platform.openai.com/docs/)
6. [documentação da API da Anthropic Claude](https://docs.anthropic.com/)
7. [Ollama — servidor local de LLM](https://ollama.com/)

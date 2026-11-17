---
title: "Câmeras Flock: Ferramenta de Segurança Pública ou Máquina de Vigilância sem Mandado?"
date: 2026-08-01
lastmod: 2026-11-08
toc: true
draft: false
description: "Uma análise independente das câmeras Flock Safety ALPR: como realmente funcionam, quais dados coletam além das placas veiculares, como o compartilhamento de dados cria um banco de dados nacional paralelo e por que a questão do mandado é o verdadeiro problema."
genre: ["Privacidade", "Vigilância", "Liberdades Civis", "Tecnologia de Aplicação da Lei", "Direitos Digitais"]
tags: ["Flock Safety","ALPR","leitores de placas veiculares","vigilância","privacidade","vigilância sem mandado","análise de comboio","rastreamento Bluetooth","rastreamento TPMS","compartilhamento de dados","câmeras Ring","Quarta Emenda","nada a esconder","precisão LPR","acusação indevida","MFA","tecnologia de aplicação da lei","liberdades civis","minimização de dados","DeFlock","contravigilância","segurança pública","vigilância policial","direito à privacidade","Quarta Emenda","vigilância digital","vigilância em massa","reconhecimento de placas veiculares","redes de câmeras","retenção de dados"]
cover: "/img/cover/flock-safety-cameras-public-safety-surveillance.webp"
coverAlt: "Uma escura interseção de rua iluminada por uma câmera de vigilância montada em um poste, com dados de placas veiculares sobrepostos nos carros que passam."
coverCaption: ""
canonical: "https://simeononsecurity.com/articles/flock-cameras-public-safety-or-surveillance-2026/"
---

**O debate sobre as câmeras Flock Safety divide as pessoas de uma forma que quase nenhum outro assunto em política tecnológica consegue. Quem teve um carro roubado tende a amá-las. Quem estuda direito constitucional tende a odiá-las. Ambos estão reagindo a algo real.**

Esta é uma análise independente do que esses sistemas realmente fazem, o que as evidências dizem sobre sua precisão e uso indevido, e por que a questão mais importante não é se as câmeras podem fotografar ruas públicas — mas sim se o governo deve construir um banco de dados pesquisável e sem mandado dos movimentos de todos.

{{< youtube id="fFuE2-xtq2w" >}}

*Este tópico gerou discussão pública significativa em meados de 2026. O vídeo acima cobre uma variedade de perspectivas de espectadores e contra-argumentos que vale a pena considerar ao lado da análise aqui apresentada.*

______

## Por Que as Câmeras Flock São Diferentes do Seu Telefone

A defesa mais comum das câmeras Flock Safety é esta: seu telefone já rastreia você em todos os lugares. A polícia pode obter seus dados de GPS com um mandado. As câmeras Flock são menos precisas do que isso. Então por que se preocupar?

O argumento é superficialmente razoável e fundamentalmente errado.

**Seu telefone rastreia você. As câmeras Flock rastreiam todos.** Quando a polícia obtém os dados de localização da torre de celular ou o histórico de GPS, eles precisam de um mandado, um alvo específico e causa provável. Quando um oficial consulta o banco de dados Flock, eles não precisam de nenhuma dessas coisas. Podem pesquisar por número de placa, janela de tempo, localização ou descrição do veículo — sem mandado, sem suspeito nomeado, sem qualquer suspeita.

O resultado é **vigilância em massa sem mandado de toda uma população**, não vigilância direcionada de um indivíduo específico. A Quarta Emenda foi projetada especificamente para prevenir exatamente esse tipo de busca geral.

O rastreamento de telefones celulares também não cria um registro permanente e pesquisável de cada veículo que passou por cada cruzamento da sua cidade nos últimos 30 dias. O Flock faz isso. Esse banco de dados persistente e estruturado é o que o torna qualitativamente diferente.

**Uma fotografia não é um sistema de vigilância. Um banco de dados pesquisável e com registro de data e hora de fotografias vinculadas pela identidade do veículo em centenas de câmeras é.**

______

## O Que "Análise de Comboio" Realmente Significa

O Flock Safety comercializa um recurso chamado **análise de comboio** — a capacidade de rastrear múltiplos veículos que viajam juntos como grupo. A linguagem de marketing é branda. As implicações não são.

A análise de comboio significa que o Flock pode identificar quando dois ou mais veículos específicos estão se movendo juntos, correlacionar seus padrões de viagem ao longo do tempo e sinalizar quando um grupo historicamente associado se reúne novamente. Em um contexto de aplicação da lei, isso poderia significar rastrear organizadores de protestos, identificar quais carros comparecem a reuniões políticas, ou monitorar pessoas que se reúnem regularmente no mesmo bairro.

Nenhuma dessas pessoas precisa ter feito qualquer coisa ilegal para que suas associações de comboio sejam registradas e armazenadas.

______

O recurso tem usos legítimos, como rastrear veículos de uma organização criminosa suspeita. Mas, aplicado a um banco sem exigência de mandado, também pode ser usado contra qualquer pessoa. É uma infraestrutura para vigilância política, seja essa a intenção atual ou não.

## O Que as Câmeras Flock Coletam Além das Placas Veiculares

A placa veicular é o ponto de dados mais visível, mas não é o único. Veja o que as evidências mostram sobre a coleta mais ampla de sinais por essas redes de câmeras.

### Sniffing de Endereços MAC Bluetooth e WiFi

**Isso é real, documentado e frequentemente subnotificado.**

Muitas implantações de ALPR — não apenas Flock — incluem capacidade de varredura de WiFi e Bluetooth. Quando o WiFi ou Bluetooth do seu telefone está habilitado e não conectado, ele transmite **solicitações de probe** que incluem o endereço MAC do seu dispositivo. Uma câmera com rádio WiFi pode registrar passivamente esses endereços junto com a leitura da placa.

Isso importa enormemente: seu endereço MAC está vinculado a *você*, não ao seu carro. Se você for passageiro no veículo de outra pessoa, alugar um carro ou dirigir um carro emprestado, seu telefone ainda transmite sua identidade. A análise de comboio também inclui as identidades dos dispositivos de todos os passageiros, não apenas do motorista.

Mesmo que a implantação que preocupa você não faça isso atualmente, a capacidade de hardware e software costuma existir. Quais dados são *coletados* e quais são *retidos* são questões distintas. Sem uma exigência pública de mandado, auditar a conformidade é praticamente impossível.

### Rastreamento de Sensores TPMS

**Os sensores do Sistema de Monitoramento de Pressão dos Pneus (TPMS)** transmitem um identificador único em frequências de rádio UHF. Esses IDs não são criptografados e são transmitidos sempre que o pneu está girando. Pesquisadores demonstraram que sniffers TPMS passivos ao longo das vias podem registrar identidades de veículos.

Um ID TPMS corresponde a um conjunto específico de pneus. Quando esses pneus estão em um veículo, o ID funciona como uma placa que você não sabia que tinha e não pode exibir de outra forma.

Isso não é uma capacidade hipotética futura. Receptores RTL-SDR que podem registrar sinais TPMS custam cerca de US$ 40.

A barreira técnica para instalar monitoramento passivo de TPMS ao lado de uma rede ALPR é baixa.

{{< figure src="flock-tpms-bluetooth-surveillance.webp" alt="Diagrama que mostra como uma câmera Flock à beira da estrada capta ao mesmo tempo placas, endereços MAC Bluetooth de celulares e IDs dos sensores TPMS dos pneus" >}}

______

## O que a câmera registrou

**Em setembro de 2026, um grupo hacker retirou uma câmera Flock de um poste, copiou seu armazenamento e publicou as imagens do sistema de arquivos por meio do Distributed Denial of Secrets.** Os registros recuperados mostram a operação completa de uma instalação real, com números maiores do que os materiais públicos de marketing sugerem.

*A câmera não foi invadida. Ela foi desparafusada.*

### Vinte e um dias de tráfego

Os registros recuperáveis cobrem cerca de **21 dias** de operação em vários períodos. Neles, a câmera fotografou aproximadamente **50.200 veículos e gerou cerca de 1,6 milhão de imagens**.

| Medida | Valor |
|---------|-------|
| Veículos fotografados | **50.200** |
| Imagens geradas | **~1,6 milhão** |
| Dia típico | ~3.300 veículos |
| Dia mais movimentado nos registros | **4.454 veículos** |
| Imagens por veículo que passa | em geral ~28, **mais de 100 em alguns casos** |

Registros mais antigos foram sobrescritos no dispositivo, então a câmera operou por mais tempo do que o período preservado mostra. **Um único ponto na via produziu mais de um milhão de imagens em menos de um mês.**

### Cada veículo recebe dezenas de fotografias

Quando há movimento no quadro, a câmera dispara uma sequência rápida. Um veículo típico gerava cerca de **28 imagens**, e alguns geravam mais de 100.

A câmera fotografa com **exposições diferentes** para captar a placa e a cena mais ampla em quadros separados. Depois, analisa as imagens, recorta quadros úteis e os envia pela rede celular. O próprio dispositivo não lê a placa. Cerca de **20 aplicativos desenvolvidos pela Flock** cuidam de detecção de movimento, captura de imagem, classificação de objetos, envio e atualizações remotas. **A leitura da placa e a identificação do veículo ocorrem nos servidores da Flock, não na estrada.**

Essa distinção importa para a discussão sobre mandados. A câmera não é um gravador passivo de números de placas. Ela é um sensor que alimenta um processo remoto de identificação.

### O software também detecta pessoas

A Flock afirma que suas câmeras detectam veículos. O código recuperado mostra mais.

**O software no dispositivo inclui explicitamente um detector de pessoas.** Quando identifica uma pessoa, registra sua posição no quadro e um nível de confiança. Esse detector é separado dos detectores de veículos, placas e bicicletas. É uma função deliberada do produto, não um efeito acidental de um modelo genérico.

A WIRED testou a afirmação ao extrair os modelos do dispositivo e executá-los em vídeos recuperados e imagens de controle. **Os modelos detectaram pessoas facilmente, inclusive na selfie de um repórter.** A análise de **27.321 clipes de vídeo armazenados** encontrou pessoas em 11 clipes, todas motociclistas. O número baixo reflete a câmera instalada acima de uma via e apontada para as faixas, não uma limitação do detector.

**Esses clipes também são um achado importante.** São **arquivos MP4 de um a dois segundos, com resolução de 1024 por 768 pixels e sem áudio**, armazenados separadamente das sequências de imagens em alta resolução. As descrições públicas da Flock enfatizam fotos de placas. O dispositivo também grava vídeos curtos.

*A Flock afirma que suas câmeras não fazem reconhecimento facial. A investigação não encontrou evidências além das funções incluídas por padrão no Android, que aparentemente não estavam ativadas nem em uso.*

### O detector de placas vê placas em toda parte

A mesma investigação descobriu que o detector de placas classifica gráficos como placas.

**Adesivos de para-choque, molduras de concessionárias e outros gráficos de veículos eram recortados como se fossem placas.** Em um vídeo de uma motocicleta passando, o detector isolou um **patch com a bandeira dos Estados Unidos na bolsa lateral do motociclista** e o tratou como placa.

Isso é um problema de precisão e de privacidade. A classificação é ampla o bastante para coletar imagens de coisas que o sistema não foi projetado para coletar, e elas seguem para os mesmos servidores que as leituras legítimas.

### A câmera estava ficando sem espaço

Os registros mostram um dispositivo sob pressão constante de armazenamento.

Ao tentar salvar imagens em resolução máxima, os registros anotaram **mais de 27.000 erros "no space left on device"**, além de dezenas de milhares de erros relacionados, falhas e reinicializações.

Duas mensagens revelam aspectos da engenharia:

- Aproximadamente a cada dois minutos, um serviço verificava se a câmera ainda funcionava e registrava **"Who's a good boy?!"**. Mais de **12.000** ocorrências aparecem nos registros recuperados.
- Quando a câmera reiniciava, outro serviço registrava **"A reboot was requested! ¡Adiós, Amigos!"**.

O tom é informal. O problema não é. O dispositivo de vigilância está sem atualizações do sistema operacional há oito anos e falha ou fica sem espaço ao salvar as imagens que deveria coletar.

______

## A linha de produtos coleta mais do que placas

A câmera recuperada era uma unidade Falcon. A linha de produtos é maior e os modelos mais novos coletam sinais que um leitor de placas nunca captava.

### O sensor de áudio classifica situações de perigo

**Raven** é um dispositivo de detecção de áudio instalado separadamente. Ele usa um ESP32 com um DSP neural Syntiant NDP120-B0. No início, classificava quatro tipos de som: tiros, pneus, ambiente e desconhecido.

**Uma atualização de firmware de outubro de 2025 adicionou uma quinta classe: sons de pessoas em perigo.** O sensor avalia se alguém próximo precisa de ajuda e aciona automaticamente as câmeras Condor e Falcon próximas por meio da plataforma FlockOne.

*Um dispositivo vendido como detector de tiros tornou-se silenciosamente um monitor acústico de perigo.*

### As câmeras agora voam

**Alpha** é o drone da própria Flock. Apresentado em outubro de 2025, já está em operação, inclusive em um **projeto-piloto do Departamento de Polícia de South Bend em março de 2026**. Foi projetado pela Flock, montado nos EUA e atende aos requisitos da NDAA.

| Especificação | Valor |
|---------------|-------|
| Velocidade máxima | **60 MPH** |
| Tempo de voo | ~45 minutos |
| Troca de bateria | **90 segundos** em uma base com duas baterias |
| Conexões celulares | **4 modems independentes** para contingência |
| Altitude para leitura de placas | **até 2.000 pés** |
| Cobertura | até **50 milhas quadradas por base** |

**Aerodome** é a linha antiga de drones, incorporada por uma **aquisição de US$ 300 milhões em outubro de 2024**. Usa aeronaves DJI Matrice M350 e M300 RTK. O abrigo Hextronics Atlas comporta oito baterias para operação contínua. Prosper Police e Scottsdale ainda as operam.

### A rede incorpora câmeras de outras empresas

**Wing** não é hardware. É uma ponte de software anunciada em outubro de 2025. Ela adiciona a análise da Flock a câmeras IP existentes de terceiros, para que câmeras que não são da Flock enviem dados à mesma interface de investigação **Nova**.

**Isso muda a escala do problema.** Uma cidade que instala câmeras Flock sabe o que instalou. Uma cidade que usa Wing transforma seu conjunto atual de câmeras em sensores Flock sem comprar uma nova câmera, e as imagens chegam a um sistema pesquisável.

### O trailer facilita a implantação

O **trailer LPR** monta uma câmera Flock em um chassi All Traffic Solutions ATS-5 com **120 watts de energia solar**, uma **bateria de 47 ampères-hora** e radar com painel de mensagens. Ele se prende a um engate receptor de 2 polegadas e uma pessoa consegue implantá-lo.

Também informa sobre adulteração e bateria fraca. Isso mostra que a empresa espera interferência nos equipamentos em campo.


{{< figure src="flock-data-sharing-shadow-national-network.webp" alt="Mapa que mostra como redes municipais e distritais de câmeras Flock se conectam por acordos de compartilhamento de dados em um banco regional e quase nacional pesquisável" >}}

______

## O Problema Real: Fotografia vs. Banco de Dados

Tirar uma foto de um carro em uma rua pública é legal. Um policial anotando uma placa é legal. A câmera de segurança de um vizinho gravando o tráfego é legal.

Nenhuma dessas atividades é a mesma que **construir um banco de dados centralizado, pesquisável e retido indefinidamente de cada movimento de veículo em toda uma cidade**.

O direito legal de observar espaços públicos não se estende automaticamente ao direito de agregar essas observações em uma infraestrutura de vigilância que funciona como um acompanhamento contínuo de 30 dias de cada pessoa que dirige.

O Supremo Tribunal reconheceu essa distinção. Em *Carpenter v. United States* (2018), o Tribunal decidiu que mesmo que os dados da torre de celular consistam em registros já fornecidos a um terceiro, a agregação desses dados ao longo do tempo em um registro abrangente dos movimentos de uma pessoa requer um mandado.

As câmeras Flock Safety estão fazendo exatamente o que *Carpenter* advertiu — em escala, automaticamente, sem mandados, em toda a população.

______

## Compartilhamento de Dados e a Rede Nacional Paralela

As redes individuais de câmeras Flock não são isoladas. Cidades e condados celebram **acordos de compartilhamento de dados** com jurisdições vizinhas, o que significa que uma consulta em uma cidade pode extrair registros de dezenas de outras. Alguns desses acordos são permissivos o bastante para que uma única agência acesse, na prática, um banco de dados regional ou quase nacional.

**É assim que uma rede local de câmeras se torna um sistema de vigilância nacional de fato sem que o Congresso jamais vote sobre isso.**

O compartilhamento de dados é voluntário e juridicamente ambíguo. Não há lei federal que o autorize, limites padronizados de retenção, requisitos obrigatórios de auditoria ou um mecanismo para que uma pessoa descubra se os movimentos de seu veículo foram consultados.

**A escala desse acesso está documentada.** Em Alpharetta, na Geórgia, a WIRED descobriu que os registros das câmeras Flock da cidade estavam acessíveis a **mais de 2.000 agências**, incluindo departamentos de polícia, universidades, aeroportos e o Office of Inspector General da General Services Administration federal. Essa quantidade não é uma peculiaridade dos acordos de Alpharetta. Ela reflete como a rede nacional da Flock é conectada por padrão.

O DeFlock.org, que faz o mapeamento colaborativo das localizações das câmeras Flock, mapeou mais de **124.000 implantações suspeitas de LPR** nos Estados Unidos.

______

## Câmeras Ring, Flock e Mandados

O Flock Safety e o Amazon Ring são produtos diferentes, mas compartilham uma característica crítica: ambos podem fornecer às agências de aplicação da lei acesso a dados sem exigir um mandado.

O Ring gerou grande controvérsia quando se tornou público que a Amazon havia fornecido imagens às autoridades milhares de vezes, muitas vezes sem o conhecimento ou consentimento do dono da câmera. Depois da pressão pública, a Amazon alterou algumas políticas, mas o marco jurídico subjacente não mudou.

A Flock opera de modo semelhante. Câmeras costumam ser instaladas por municípios ou associações de moradores, mas uma empresa privada controla a infraestrutura de dados. Quando a polícia solicita dados, recebe acesso por regras de emergência, portais policiais ou porque a agência local já tem acesso.

**A ausência de um requisito de mandado não é um bug nesses sistemas. É o modelo de negócios.**

Solicitações de registros públicos (FOIA nos EUA, FOI no Canadá) podem às vezes revelar quais agências consultaram os sistemas Flock.

______

## Desmontando o "Nada a Esconder"

O argumento “nada a esconder” é a resposta mais comum às preocupações com vigilância e revela uma incompreensão real sobre a finalidade da privacidade.
**Privacidade não é sobre esconder culpa. É sobre preservar autonomia.**

As pessoas têm interesses legítimos de privacidade em atividades que não são criminosas: participar de reuniões políticas, visitar médicos, ir a serviços religiosos, falar com jornalistas ou simplesmente dirigir para onde quiserem sem que um registro permanente seja feito. O fato de que todas essas atividades são legais não significa que o governo tem um interesse legítimo em catalogá-las.

A história fornece uma resposta direta ao "nada a esconder". Os japoneses-americanos internados durante a Segunda Guerra Mundial não eram criminosos. Ativistas vigiados pelo COINTELPRO não eram criminosos.

Pessoas incluídas em listas de proibição de voo por erro burocrático também não eram criminosas. Os dados que permitiram esses abusos foram coletados pela mesma justificativa: segurança pública, avaliação de ameaças e aplicação eficiente da lei.

**A infraestrutura de vigilância construída hoje será usada por quem quer que detenha o poder amanhã.** A questão não é se o governo atual é confiável. É se você aceitaria que o governo futuro mais hostil que se possa imaginar tivesse acesso a um registro permanente de todos os lugares onde dirigiu na última década.

______

## Quando o Reconhecimento de Placas Erra

Os sistemas ALPR não são perfeitamente precisos, e as consequências de um erro são sérias.

Os erros de reconhecimento de placas se enquadram em várias categorias:

- **Caracteres mal lidos** — letras e números semelhantes sob iluminação inadequada ou em alta velocidade (0/O, 1/I, 8/B, M/N/H)
- **Leituras parciais** — placas sujas, obstruídas ou danificadas
- **Erros de banco de dados** — placas sinalizadas como roubadas que já foram liberadas
- **Colisões regionais de placas** — dois estados ou países podem emitir a mesma combinação de placa — uma leitura de uma placa da Califórnia pode sinalizar por engano um veículo de outro estado com a mesma sequência alfanumérica

Há exemplos reais de todos esses erros: policiais apontaram armas durante abordagens porque o veículo foi associado por engano a um carro roubado; pessoas receberam cobranças de pedágio por estradas onde nunca passaram; e uma pessoa com um Hyundai azul-claro recebeu a cobrança de uma Harley-Davidson cuja placa diferia por duas letras.

**A taxa de erro multiplicada pelo volume de leituras produz um número significativo de pessoas reais que serão incorretamente sinalizadas, paradas, revistadas ou pior.**

Como a maioria dessas consultas ocorre sem mandado, não há revisão judicial da precisão dos dados antes que alguém tome providências.

______
## Falhas de Segurança: MFA e Logins Compartilhados

As práticas de segurança do Flock Safety foram publicamente criticadas em múltiplos pontos:

- **Sem autenticação multifator (MFA) obrigatória** para contas de aplicação da lei em muitas implantações
- **Credenciais de login compartilhadas** entre vários agentes em algumas agências
- **Sem expiração automática de sessão** em algumas configurações
- **Sem alertas quando contas são acessadas de locais ou horários incomuns**

Esses não são detalhes menores de implementação. Uma credencial comprometida por phishing, engenharia social ou reutilização de senha simples daria a um invasor acesso para consultar uma rede regional Flock que cobre milhões de leituras de placas.

Para sobreviventes de abuso doméstico, vítimas de stalking ou jornalistas, a existência de um banco de dados compartilhado e minimamente protegido de seus movimentos de veículo é uma preocupação não abstrata. É um risco direto à segurança física.

O argumento de que “as câmeras captam apenas dados públicos” ignora a segurança necessária na camada do banco de dados que reúne essas informações. Mesmo que cada foto isolada seja legal, a base agregada precisa de proteção mais forte do que uma senha compartilhada.

______

## O Sistema Poderia Ser Melhor Projetado?

**Controles técnicos, por si só, não são suficientes, mas vale a pena considerá-los.**

Várias propostas foram discutidas para dificultar o abuso de sistemas ALPR:

**Minimização de dados por design**: Em vez de guardar imagens completas das placas com horários e coordenadas GPS, o sistema poderia guardar um **hash criptográfico** da placa associado a uma localização e um horário aproximados. Uma consulta policial confirmaria se determinada placa foi vista em uma área e janela de tempo específicas, mas não recuperaria uma lista de todos os locais onde ela apareceu. Isso limita buscas exploratórias e ainda permite responder a perguntas investigativas direcionadas.

**Retenção por prazo limitado**: Placas sem relação com uma investigação aberta poderiam ser apagadas automaticamente após 24 a 72 horas, em vez de permanecer por 30 dias ou mais. A maioria dos usos investigativos legítimos precisa de dados quase em tempo real. A retenção prolongada cria um risco desproporcional às liberdades civis.

**Mandados com revisão judicial**: O controle mais importante é jurídico, não técnico. Exigir um mandado para qualquer consulta ao histórico de placas de uma pessoa identificada não impediria usos emergenciais, pois a lei já prevê exceções para circunstâncias urgentes. Mas impediria a mineração rotineira de dados sem mandado que hoje não tem controle.

**Registro de auditoria com transparência pública**: Toda consulta deve ser registrada, os registros devem poder ser auditados por órgãos de supervisão, e estatísticas agregadas devem ser divulgadas ao público.

Essas medidas não eliminariam todos os riscos do ALPR, mas reduziriam muito o potencial de abuso rotineiro e manteriam a utilidade investigativa valorizada por seus defensores.

______

## O Debate Não Precisa Ser Tudo ou Nada

A discussão sobre as câmeras Flock costuma se dividir em duas posições extremas: as câmeras são ferramentas essenciais contra o crime e qualquer crítica ajuda criminosos; ou são um Estado de vigilância inconstitucional e devem ser removidas imediatamente.

As duas posições estão erradas, e a polarização dificulta a conversa que realmente importa.

**As câmeras podem fotografar ruas públicas. Os dados devem ser regidos por lei.**

A tecnologia não vai embora. As aplicações legítimas de segurança pública são reais. Mas o modelo de implantação atual — no qual uma empresa privada constrói e controla um banco de dados de vigilância quase nacional que as forças de segurança podem consultar sem mandado — é constitucionalmente suspeito e historicamente perigoso.

O caminho a seguir não é destruir as câmeras. É exigir mandados para buscas individuais, impor janelas curtas de retenção de dados, proibir o compartilhamento de dados sem justificativa específica para o caso, e criar mecanismos executáveis de auditoria e supervisão.

É uma resposta burocrática e pouco empolgante. Não provoca indignação em nenhum dos lados. Mas é a única que leva a sério tanto a segurança pública quanto as liberdades constitucionais.

Se você quer saber quando está perto de uma dessas câmeras em vez de esperar por mudanças na política, já existem dispositivos dedicados para detectá-las.

{{< stscollective-ad "flockyou" >}}

______

## Artigos Relacionados




| Artigo | O Que Você Aprenderá |
|---------|------------------|
| **[Vigilância por Câmeras Flock Safety: Prevalência, Preocupações com Privacidade e Estratégias de Proteção](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Análise completa da rede Flock, casos documentados de abuso e etapas práticas de proteção |
| **[Flock Finder: Mapeie Cada Câmera Flock Suspeita Perto de Você](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | Como usar a ferramenta de código aberto para visualizar mais de 40.000 câmeras suspeitas usando dados WiGLE |
| **[Guia de Hardware de Detecção Flock-You](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Construa ou compre um dispositivo baseado em ESP32 para detectar câmeras Flock em tempo real |
| **[Como Instalar o Rayhunter em Dispositivos de Detecção de IMSI Catcher](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detecte stingrays e armadilhas IMSI |
| **[Comparação de Dispositivos Rayhunter 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Escolha o hardware certo para um kit completo de contravigilância |

______

## Referências

1. [Carpenter v. United States, 585 U.S. 296 (2018)](https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf)
2. [ACLU — Leitores Automáticos de Placas Veiculares](https://www.aclu.org/news/by-issue/automatic-license-plate-readers)
3. [Electronic Frontier Foundation — O que é ALPR?](https://www.eff.org/pages/what-alpr)
4. [DeFlock](https://deflock.org/)
5. [Mapa Interativo DeFlock](https://maps.deflock.org/)
6. [Site Oficial Flock Safety](https://www.flocksafety.com/)
7. [Vulnerabilidades de Segurança e Privacidade de Redes Sem Fio em Carros: Estudo de Caso TPMS](https://www.winlab.rutgers.edu/~gruteser/papers/xu_tpms10.pdf)
8. [FBI Vault — COINTELPRO](https://vault.fbi.gov/cointel-pro)
9. [MuckRock — Flock Safety](https://www.muckrock.com/tags/flock-safety/)
10. [Flock Finder GitHub](https://github.com/simeononsecurity/flock-finder)
11. [WIRED e 404 Media: hackers invadiram uma câmera Flock](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
12. [Micah Lee: câmeras Flock têm vulnerabilidades e credenciais gravadas no código](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
13. [Distributed Denial of Secrets: imagens do sistema de arquivos de uma câmera Flock ALPR](https://ddosecrets.org/article/flock-alpr-camera)
14. [Hackaday: segurança da semana, câmeras Flock são antigas](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
15. [WiFi Mothership: referência de detecção de dispositivos Flock Safety ALPR](https://wifimothership.com/flock)
16. [Mapa interativo do Flock Finder](https://simeononsecurity.github.io/flock-finder/)
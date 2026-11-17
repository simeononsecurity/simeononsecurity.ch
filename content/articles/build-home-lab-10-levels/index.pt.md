---
title: "Monte um laboratório doméstico em 10 níveis, do Pi-hole à IA local"
date: 2026-10-27
lastmod: 2026-11-09
toc: true
draft: false
description: "Monte um laboratório doméstico em dez etapas práticas, da filtragem DNS de toda a rede à IA local, com hardware, custos, habilidades e compensações em cada nível."
genre: ["Laboratório doméstico", "Hospedagem própria", "IA local", "Redes domésticas"]
tags: ["laboratório doméstico", "Pi-hole", "Home Assistant", "Docker", "Jellyfin", "Plex", "NAS", "Proxmox", "Tailscale", "Ollama", "IA local", "consumo de energia"]
cover: "/img/cover/build-home-lab-10-levels.webp"
coverAlt: "Um laboratório doméstico cresce de um Raspberry Pi e roteador pequenos até armazenamento, servidores, equipamentos de rede e uma estação de trabalho de IA local."
coverCaption: ""
---

Monte um laboratório doméstico em 10 níveis, do Pi-hole à IA local
==================================================================

Um **laboratório doméstico** é um conjunto de computadores e serviços que você opera para resolver problemas cotidianos e aprender a administrar sistemas reais. Você pode bloquear anúncios, automatizar luzes, armazenar mídias da família ou testar máquinas virtuais. **Comece com uma tarefa útil.** Adicione hardware quando surgir uma limitação real.

Este guia vai de um Raspberry Pi pequeno com Pi-hole a um servidor que executa modelos locais de IA. **Cada nível acrescenta uma capacidade e uma nova responsabilidade.** As estimativas de custo usam um consumo ilustrativo e uma tarifa de exemplo de $0.15 por quilowatt-hora. Confira sua tarifa local e meça os equipamentos antes de comprar mais.

## Nível 1: Bloqueie anúncios em toda a rede doméstica

Instale o [Pi-hole](https://docs.pi-hole.net/) em um Raspberry Pi ou outro computador Linux pequeno. O Pi-hole funciona como um **sumidouro DNS**. Quando um dispositivo solicita o endereço de um domínio em uma lista de bloqueio, o Pi-hole não retorna um destino utilizável. O navegador, o celular e a TV inteligente usam o mesmo filtro quando o roteador ou servidor DHCP direciona os clientes ao Pi-hole.

A **filtragem DNS** também funciona fora dos navegadores, inclusive com alguns anúncios em aplicativos e TVs conectadas. O conteúdo das páginas fica fora do filtro, então passam os anúncios servidos pelo mesmo domínio de um site ou aplicativo. Uma lista de bloqueio às vezes impede o carregamento de um login, vídeo ou pagamento. Consulte o registro de consultas do Pi-hole, permita o domínio específico quando necessário e prepare um DNS alternativo para interrupções.

O consumo de energia é modesto. Para um dispositivo de 8 watts ligado durante todo o mês, a estimativa é 8 W × 24 horas × 30 dias ÷ 1.000 × $0.15 = **cerca de $0.86 por mês**. Meça a fonte de alimentação completa na tomada. Um segundo computador, uma unidade USB ou um adaptador ineficiente altera o total.

**Você aprenderá:** DNS, DHCP, listas de bloqueio e manutenção básica do Linux.

## Nível 2: Automatize dispositivos inteligentes localmente

Adicione o [Home Assistant](https://www.home-assistant.io/), que reúne dispositivos inteligentes compatíveis e automações em um só sistema. Programe o desligamento das luzes na hora de dormir. Ligue um ventilador quando um sensor de temperatura ultrapassar um valor definido. Envie um alerta para você quando um sensor de vazamento detectar água. **Essas pequenas automações trazem valor imediato.**

O **controle local** mantém muitas automações funcionando dentro de casa quando um serviço externo ou a conexão com a internet falha. O comportamento depende do dispositivo. Alguns produtos ainda exigem conta do fornecedor, serviço em nuvem ou conexão com a internet para configuração e recursos remotos. Confira os requisitos da integração antes de comprar o hardware.

**Faça backup do Home Assistant** e guarde uma cópia fora do host. Documente as integrações e os passos de recuperação. Uma placa SD ou mini PC com defeito não deve apagar sua configuração.

**Você aprenderá:** integrações de dispositivos, gatilhos, condições e recuperação de backups.

## Nível 3: Execute vários serviços em um mini PC

Um **mini PC empresarial usado** costuma oferecer memória expansível, armazenamento substituível e portas úteis por um preço baixo. Um mini PC Intel N100 geralmente consome menos energia e ocupa pouco espaço. A Intel descreve o N100 como um processador de quatro núcleos e quatro threads, TDP de 6 watts e suporte a até 16 GB de memória. A classificação do processador não equivale ao consumo do sistema completo na tomada. Compare o computador específico, memória, armazenamento, garantia e portas de rede.

Instale Linux e use o [Docker](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/) para executar serviços separados como **contêineres**. Um contêiner empacota um aplicativo e suas dependências, mas compartilha o kernel do sistema operacional do host. Por exemplo, execute um gerenciador de senhas como o projeto Vaultwarden mantido pela comunidade e um monitor de disponibilidade como o Uptime Kuma. **Trate o gerenciador de senhas como um serviço sensível:** limite o acesso, use autenticação forte, aplique atualizações e mantenha um backup criptografado.

**Contêineres não substituem atualizações nem backups.** Defina um local de armazenamento para cada serviço e registre os passos de recuperação. Um mini PC pequeno também tem limites. Vários bancos de dados, conversões de mídia ou aplicativos grandes esgotam memória, armazenamento ou tempo de CPU.

**Você aprenderá:** administração Linux, contêineres, volumes, atualizações e recuperação de serviços.

## Nível 4: Crie uma biblioteca de mídia doméstica

[Jellyfin](https://jellyfin.org/docs/) é um servidor de mídia de código aberto. O [Plex](https://support.plex.tv/) oferece um ecossistema de clientes refinado e recursos opcionais vinculados a uma conta. Ambos organizam bibliotecas pessoais e transmitem mídias para clientes compatíveis. **Escolha com base nos clientes**, no modelo de acesso remoto, no suporte ao hardware e nos recursos necessários.

**Sua necessidade de armazenamento** depende do tamanho e da qualidade da coleção. Comece com um único disco apenas se você já tiver um plano de backup separado. Use nomes de pastas e metadados consistentes para que o servidor identifique corretamente filmes e episódios.

A **reprodução direta** envia um arquivo compatível ao cliente sem alterar o fluxo de vídeo. A **transcodificação** converte áudio ou vídeo quando o cliente, a conexão, as legendas ou a configuração de qualidade exigem outro formato. A transcodificação aumenta a carga do servidor. Teste seus dispositivos e a rede antes de comprar uma GPU ou CPU maior. **Dispense um servidor de mídia dedicado** quando todos os clientes reproduzem os arquivos diretamente e um único host atende às suas necessidades.

**Você aprenderá:** formatos de mídia, planejamento de armazenamento, taxa de transferência de rede e testes de carga.

## Nível 5: Adicione redundância de armazenamento e um backup separado

Um NAS com dois discos e **armazenamento espelhado** grava os dados em ambos. Se um disco falhar, o outro mantém uma cópia atual enquanto você substitui a unidade defeituosa e reconstrói o espelho. O espelhamento protege a disponibilidade durante a falha de um disco. **Um espelho não restaura** um arquivo excluído, não reverte a criptografia de ransomware e não protege contra roubo, incêndio ou evento elétrico que danifique os dois discos.

Mantenha um **backup separado** em outro dispositivo ou local. Inclua documentos importantes, fotos, exportações de configuração e dados de serviços. Programe os backups e mantenha versões para que alterações acidentais não sobrescrevam todas as cópias boas.

**Teste uma restauração.** Escolha alguns arquivos, restaure-os em uma pasta separada e abra-os. Para um serviço, restaure os dados em uma instância de teste ou documente os passos e verifique cada arquivo. Um backup que você nunca restaurou é uma suposição, não um plano de recuperação.

**Você aprenderá:** sistemas de arquivos, troca de discos, rotação de backups e testes de restauração.

## Nível 6: Aprenda virtualização com um pequeno cluster Proxmox

[Proxmox VE](https://pve.proxmox.com/pve-docs/) executa máquinas virtuais e contêineres em hardware de servidor. Vários mini PCs unidos em um **cluster** compartilham uma visualização de gerenciamento e permitem aprender sobre nós, armazenamento e migração. Um cluster é um grupo de servidores configurados para coordenar. Os membros não combinam a memória em um grande conjunto único. **A alta disponibilidade exige** planejamento adicional e armazenamento compartilhado ou replicado adequado.

Um **snapshot** registra o estado de uma máquina virtual em determinado momento, permitindo voltar a um estado anterior depois de uma alteração no laboratório. Snapshots normalmente dependem do armazenamento original. Não são backups independentes. **Copie dados importantes para um destino de backup separado** e teste a restauração.

Cada nó adiciona consumo de energia, portas de rede, cabos e atualizações. Três computadores pequenos também criam três sistemas para atualizar e solucionar problemas. Um mini PC com algumas máquinas virtuais ensina muitos dos mesmos fundamentos por um custo menor. **Adicione nós quando** os experimentos exigirem isolamento ou você quiser praticar operações de cluster.

**Você aprenderá:** máquinas virtuais, pools de armazenamento, snapshots, associação ao cluster e manutenção de nós.

## Nível 7: Adicione acesso remoto privado e separação de rede

[Tailscale](https://tailscale.com/kb/) conecta seus dispositivos aprovados por uma rede privada, permitindo acessar alguns serviços domésticos quando você estiver fora. **Restrinja o acesso** aos dispositivos e serviços necessários para cada pessoa. Proteja contas com autenticação multifator e revise dispositivos e chaves antigos.

Um switch ou roteador gerenciado com suporte a **VLAN** separa grupos de dispositivos. Coloque tomadas inteligentes e outros dispositivos de baixa confiança em uma rede diferente da dos computadores com arquivos pessoais. Coloque o armazenamento em uma rede acessível apenas aos sistemas que precisam dele. A segmentação limita a comunicação entre dispositivos. Mantenha atualizações, senhas fortes e regras de acesso.

**Evite expor painéis de administração diretamente à internet pública** a menos que entenda os requisitos de autenticação, correções e firewall do serviço. Uma ferramenta de acesso privado também exige controle cuidadoso de contas e dispositivos.

**Você aprenderá:** acesso privado, permissões baseadas em identidade, VLANs, regras de firewall e limites de confiança dos dispositivos.

## Nível 8: Adicione um servidor empresarial

Passe para um servidor maior quando medições mostrarem a necessidade de mais núcleos de CPU, memória, baias de discos, slots PCIe ou capacidade de rede. Servidores empresariais mais antigos costumam custar menos usados, mas suas ventoinhas são barulhentas e o **consumo em repouso fica em torno de 100 a 160 watts**, dependendo do modelo e das peças instaladas. Trate a faixa como estimativa, não como especificação.

Calcule uma estimativa anual de energia antes da compra:

`watts medidos ÷ 1.000 × 24 × 365 × tarifa de energia por kWh`

A 120 watts e $0.15 por kWh, a estimativa é 1.051 kWh por ano, ou cerca de **$158 por ano**. Meça o servidor específico em repouso e durante a carga habitual. Inclua o consumo de discos, refrigeração e UPS.

Confira a profundidade do chassi, compatibilidade de discos, ruído, controle das ventoinhas, fonte de alimentação e placas de expansão. Um servidor que excede seu orçamento de espaço ou energia não é uma atualização prática.

**Você aprenderá:** hardware de servidor, gerenciamento remoto, expansão, refrigeração e estimativas de custo operacional.

## Nível 9: Meça a energia e ajuste o tamanho do laboratório

Use um **medidor de energia de tomada** para medir cada computador em repouso e durante o trabalho normal. Liste os maiores consumidores. Revise as configurações de energia da BIOS, remova placas e discos sem uso e transfira serviços diários de volta para mini PCs eficientes quando hardware empresarial for desnecessário.

Ligue o servidor grande apenas quando uma carga de trabalho exigir sua capacidade. Se usar um agendamento Wake-on-LAN ou controle remoto de energia, documente os passos de recuperação para falhas de rede ou energia. Mantenha uma **lista de dependências de serviços** para que desligamentos não interrompam o armazenamento ou a rede necessários a outros sistemas.

Um rack ajuda a organizar equipamentos e fluxo de ar quando o hardware para rack justifica o espaço. Um UPS cobre interrupções curtas e dá tempo para os sistemas desligarem corretamente. Ambos aumentam o custo de compra, ocupam espaço e consomem energia continuamente. **Meça o consumo deles** e inclua a troca de baterias no orçamento de longo prazo.

**Você aprenderá:** medição de energia, gerenciamento de energia, mapeamento de dependências e planejamento de capacidade.

## Nível 10: Execute modelos de IA localmente

[Ollama](https://docs.ollama.com/) baixa e executa modelos de linguagem compatíveis no computador. A **inferência local** mantém prompts e respostas no hardware que você controla quando usa um modelo e aplicativo locais. Confirme que todo o caminho do software permanece local. Um aplicativo conectado, recurso de telemetria ou opção de modelo em nuvem envia dados para fora da rede.

Os requisitos de hardware dependem do tamanho do modelo, da quantização, do tamanho do contexto e da velocidade desejada. **A memória do sistema ou da GPU precisa comportar** os pesos do modelo e o contexto de trabalho. Computadores pequenos executam modelos menores. Modelos maiores e contextos mais longos exigem mais memória e frequentemente uma GPU capaz. Meça a energia durante a inferência. Um sistema com GPU costuma consumir bem mais energia do que um mini PC em repouso.

Modelos locais servem para criar rascunhos, resumir anotações privadas e classificar conteúdo de forma simples quando a qualidade atende às suas necessidades. Eles produzem respostas incorretas, e modelos menores muitas vezes têm dificuldade com raciocínio complexo ou fatos atuais. Modelos em nuvem às vezes se saem melhor em tarefas específicas. **Compare qualidade, privacidade, latência, custo e energia** antes de decidir onde executar uma carga de trabalho.

**Você aprenderá:** memória de modelos, quantização, inferência, limites de privacidade e avaliação de cargas de trabalho.

## Compare os dez níveis

**Os custos são estimativas, não orçamentos.** Os preços do hardware variam por região, condição e configuração de armazenamento. Estime a eletricidade com `watts ÷ 1.000 × horas × dias × tarifa por kWh`. Meça na tomada quando possível e inclua as horas em repouso, pois muitos servidores domésticos ficam ligados o dia todo.

### Capacidade e hardware

| Nível | Nova capacidade | Hardware típico |
|---|---|---|
| **1** | Filtragem DNS da rede | Raspberry Pi ou host Linux pequeno |
| **2** | Automação local de dispositivos | Pi ou mini PC, dispositivos compatíveis |
| **3** | Vários aplicativos auto-hospedados | Mini PC empresarial usado ou sistema N100 |
| **4** | Transmissão de mídia pessoal | Mini PC e armazenamento de mídia |
| **5** | Tolerância à falha de disco e recuperação | NAS com dois discos e backup separado |
| **6** | Laboratório de servidores virtuais | Dois mini PCs ou mais |
| **7** | Acesso privado e segmentação | Tailscale, roteador ou switch gerenciado |
| **8** | Alta capacidade e expansão | Servidor empresarial |
| **9** | Menor consumo de energia do laboratório | Medidor de energia, sistemas ajustados |
| **10** | Inferência local de modelos | PC com muita memória, GPU opcional |

### Habilidades, custos e compensações

| Nível | Habilidades aprendidas | Estimativa de custo recorrente | Principal compensação |
|---|---|---|---|
| **1** | DNS, DHCP, Linux | Cerca de $1/mês a 8 W e $0.15/kWh | Alguns anúncios permanecem e bloqueios indevidos exigem revisão |
| **2** | Integrações, gatilhos, backups | Energia do host e custo dos dispositivos | Compatibilidade e trabalho com backups |
| **3** | Docker, atualizações, armazenamento | Depende do consumo medido do sistema | Limites de CPU, memória e disco |
| **4** | Formatos, organização, transcodificação | Armazenamento e energia do servidor | Transcodificação às vezes exige mais hardware |
| **5** | Espelhamento, retenção, restauração | Energia do NAS, discos e destino do backup | Um espelho não é um backup |
| **6** | Proxmox, VMs, clusters | Cada nó aumenta energia e manutenção | Mais nós significam mais manutenção |
| **7** | Regras de acesso, VLAN, firewall | Equipamentos de rede e custo de serviços | Regras incorretas expõem serviços |
| **8** | Hardware, refrigeração, gerenciamento remoto | Varia por servidor, calcule com dados medidos | Ruído, calor e consumo em repouso |
| **9** | Medição, agendamento, ajuste de tamanho | Custo único do medidor, economia variável | O agendamento adiciona etapas operacionais |
| **10** | Implantação e avaliação de modelos | Energia de computação e armazenamento | Qualidade e velocidade dependem do hardware |

## Escolha a próxima melhoria útil

**Pare no nível que atende às suas necessidades atuais.** Pi-hole e um mini PC podem cobrir seus serviços. Um NAS é útil quando você precisa de armazenamento compartilhado e de um plano de recuperação testado. Adicione um cluster ou servidor empresarial quando uma carga de trabalho ou meta de aprendizado justificar.

Anote **onde ficam os dados de cada serviço, como ele recebe atualizações e como restaurá-lo.** Teste backups antes de adicionar equipamentos. Deixe que a próxima limitação real oriente sua próxima compra.

## Referências

- [Documentação do Pi-hole](https://docs.pi-hole.net/)
- [Documentação do Home Assistant](https://www.home-assistant.io/docs/)
- [Especificações do processador Intel N100](https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html)
- [Docker: O que é um contêiner?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-a-container/)
- [Documentação do Jellyfin](https://jellyfin.org/docs/)
- [Suporte do Plex](https://support.plex.tv/)
- [Documentação do Proxmox VE](https://pve.proxmox.com/pve-docs/)
- [Documentação do Tailscale](https://tailscale.com/kb/)
- [Documentação do Ollama](https://docs.ollama.com/)

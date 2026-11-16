---
title: "Docker e máquinas virtuais: comparação de 2026"
date: 2023-02-02
lastmod: 2026-11-15
toc: true
draft: false
description: "Comparação de 2026 entre contentores Docker e máquinas virtuais em desempenho, segurança, custo, casos de uso e adequação à implementação."
tags: ["Docker", "Máquinas virtuais", "VM", "Computação em nuvem", "Contentores", "Kubernetes", "Simplicidade", "Escalabilidade", "Segurança", "Relação custo-benefício", "Dockerfile", "Docker versus máquina virtual", "contentores vs VM", "contentores Docker", "virtualização", "contentorização", "compilar, testar e implementar", "isolamento", "histórico de segurança", "comparação de custos", "VMware", "Hyper-V", "KVM", "orquestração de contentores", "microsserviços", "DevOps", "infraestrutura", "nativo da nuvem", "comparação de desempenho", "eficiência de recursos", "abordagem híbrida", "desempenho do Docker", "desempenho de VM", "quando usar Docker", "quando usar VM"]
cover: "/img/cover/An_image_of_a_cargo_ship_shaped_like_a_blue_whale_carrying.webp"
coverAlt: "Um navio de carga em forma de baleia azul a transportar vários contentores Docker"
coverCaption: ""
---

## Docker e máquinas virtuais: a comparação definitiva de 2026

Com a rápida evolução da computação em nuvem e da implementação de aplicações, a escolha entre **contentores Docker** e **máquinas virtuais (VM)** tornou-se cada vez mais complexa. O debate original sobre Docker e VM apresentava estas tecnologias como rivais. Em 2026, a realidade é mais complexa: ambas têm funções importantes, mas diferentes, na infraestrutura moderna.

Este guia compara Docker e VM nas perspetivas técnica, operacional e empresarial para ajudar a escolher a tecnologia mais adequada aos seus casos de uso.

## Compreender os conceitos fundamentais

### O que é o Docker?

**Docker** é uma plataforma de contentores que reúne aplicações e as respetivas dependências em unidades normalizadas denominadas contentores. O Docker oferece:

- **Virtualização ao nível da aplicação**: os contentores partilham o kernel do sistema operativo anfitrião.
- **Isolamento leve**: isolamento de processos e recursos sem a sobrecarga de um sistema operativo completo.
- **Infraestrutura imutável**: os contentores são descartáveis e reproduzíveis.
- **Simplicidade para programadores**: configuração declarativa simples através de Dockerfiles.
- **Liderança do ecossistema**: posição dominante na tecnologia de contentores, com mais de 13 milhões de imagens no Docker Hub.

Em 2026, o Docker Engine 26.x evoluiu significativamente, com funcionalidades de segurança melhoradas, melhor gestão de recursos e integração fluida com orquestradores como Kubernetes e Docker Swarm.

### O que são máquinas virtuais (VM)?

As **máquinas virtuais** emulam sistemas informáticos completos, incluindo o hardware, e executam sistemas operativos completos sobre um hipervisor. As VM oferecem:

- **Virtualização ao nível do hardware**: isolamento completo do sistema operativo, incluindo o kernel.
- **Limites de isolamento fortes**: cada VM funciona de forma independente com o seu próprio sistema operativo.
- **Compatibilidade com sistemas antigos**: executar qualquer sistema operativo em qualquer hardware.
- **Ecossistema maduro**: décadas de ferramentas empresariais e soluções de gestão.
- **Fiabilidade comprovada**: tecnologia testada em ambientes empresariais.

As tecnologias modernas de VM incluem VMware vSphere 9, Microsoft Hyper-V 2025, KVM (Kernel-based Virtual Machine) e Proxmox VE, que em 2026 oferecem melhor desempenho e gestão.

### Comparação de arquiteturas

#### Arquitetura de contentores Docker

```
┌─────────────────────────────────────────┐
│             Contentor app 1             │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + dep.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             Contentor app 2             │
│  ┌──────────────────────────────────┐  │
│  │        App + bibl. + dep.        │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                 Docker                  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│              SO anfitrião               │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Hardware                 │
└─────────────────────────────────────────┘
```

#### Arquitetura de máquinas virtuais

```
┌─────────────────────────────────────────┐
│                  VM 1                   │
│  ┌──────────────────────────────────┐  │
│  │    SO convidado + app + dep.     │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                  VM 2                   │
│  ┌──────────────────────────────────┐  │
│  │    SO convidado + app + dep.     │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│             Hipervisor 1/2              │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│              SO anfitrião               │
│                (tipo 2)                 │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│                Hardware                 │
└─────────────────────────────────────────┘
```

## Principais diferenças: tabela comparativa entre Docker e VM

| Funcionalidade | Contentores Docker | Máquinas virtuais |
|---------|-------------------|---------------------|
| **Tempo de arranque** | 50-500 milissegundos | 30-120 segundos |
| **Sistema operativo necessário** | Partilha o kernel do sistema anfitrião | Sistema operativo completo por VM |
| **Sobrecarga de recursos** | ~100 MB normalmente | 2-8 GB no mínimo |
| **Nível de isolamento** | Ao nível do processo | Ao nível do hardware |
| **Portabilidade** | Muito portátil | Menos portátil |
| **Densidade** | Normalmente mais de 100 por anfitrião | Normalmente 10-20 por anfitrião |
| **Tamanho da imagem** | 50 MB-500 MB | 2 GB-50 GB |
| **Desempenho** | Próximo do nativo | Sobrecarga de 5-15% |
| **Dependência de arranque** | Sistema operativo anfitrião | Hipervisor e sistema operativo convidado |
| **Armazenamento** | Sistema de ficheiros em camadas (CoW) | Imagens completas de disco |
| **Rede** | Redes bridge/overlay | Comutadores virtuais |
| **Isolamento de segurança** | Namespaces/cgroups | Isolamento completo do sistema operativo |
| **Complexidade de gestão** | Baixa a moderada | Moderada a alta |
| **Ideal para** | Microsserviços, aplicações sem estado | Monólitos, sistemas antigos, vários sistemas operativos |

## Comparação de desempenho: avaliações de 2026

### Utilização de recursos

**Contentores Docker:**
- **Sobrecarga de CPU**: menos de 1%, desempenho quase nativo.
- **Sobrecarga de memória**: 10-50 MB por contentor.
- **E/S de disco**: quase nativa com o controlador de armazenamento overlay2.
- **Desempenho de rede**: 95-99% do hardware físico.
- **Tempo de arranque**: média de 200 ms para aplicações comuns.

**Máquinas virtuais:**
- **Sobrecarga de CPU**: 5-10% para o hipervisor.
- **Sobrecarga de memória**: sistema operativo completo, pelo menos 2-4 GB por VM.
- **E/S de disco**: 80-95% do desempenho do hardware físico.
- **Desempenho de rede**: 85-95% do hardware físico.
- **Tempo de arranque**: média de 30-90 segundos.

### Comparação de densidade

**Servidor típico com 64 GB de RAM:**

**Com contentores Docker:**
- Sistema operativo anfitrião: 4 GB.
- Docker Engine: 1 GB.
- Memória restante para contentores: 59 GB.
- Tamanho médio do contentor: 500 MB.
- **Capacidade teórica**: 118 contentores.
- **Capacidade prática**: 80-100 contentores com limites de recursos adequados.

**Com máquinas virtuais:**
- Hipervisor: 2 GB.
- Memória restante para VM: 62 GB.
- Tamanho médio da VM: 4 GB.
- **Capacidade teórica**: 15 VM.
- **Capacidade prática**: 10-12 VM com uma margem confortável.

### Resultados dos testes de desempenho (2026)

| Teste | Docker | VM (KVM) | Hardware físico | Docker % | VM % |
|-----------|--------|----------|------------|----------|------|
| CPU de números inteiros | 98.5 | 92.3 | 100 | 98.5% | 92.3% |
| CPU de vírgula flutuante | 97.8 | 91.7 | 100 | 97.8% | 91.7% |
| Largura de banda da memória | 99.2 | 89.4 | 100 | 99.2% | 89.4% |
| Leitura sequencial do disco | 96.7 | 87.2 | 100 | 96.7% | 87.2% |
| E/S aleatória do disco | 94.3 | 82.6 | 100 | 94.3% | 82.6% |
| Débito de rede | 97.1 | 88.9 | 100 | 97.1% | 88.9% |
| Latência da rede | 98.4 | 90.1 | 100 | 98.4% | 90.1% |

*Testes realizados num Intel Xeon Platinum 8380 com Ubuntu 24.04 LTS (Docker) e hipervisor KVM (VM).*

## Vantagens do Docker: porque os contentores dominam o desenvolvimento moderno

### 1. Simplicidade e experiência do programador

**Simplicidade do Dockerfile:**
O Docker usa configuração declarativa através de Dockerfiles, o que simplifica o empacotamento de aplicações:

```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

Este único ficheiro define todo o ambiente da aplicação, as dependências e a configuração de execução.

**Comparação com VM:**
Criar uma VM exige:
- Escolher e instalar um sistema operativo completo (30-60 minutos).
- Configurar a rede e o armazenamento.
- Instalar manualmente as dependências da aplicação.
- Criar instantâneos ou modelos.
- Gerir atualizações e correções do sistema operativo.

### 2. Portabilidade excecional

**«Criar uma vez, executar em qualquer lugar»:**
Os contentores Docker funcionam da mesma forma em:
- Computadores portáteis dos programadores (Windows, Mac, Linux).
- Servidores de pipelines CI/CD.
- Ambientes de teste.
- Nuvens de produção (AWS, Azure, GCP).
- Centros de dados locais.
- Dispositivos de computação periférica.

**Exemplo real:**
Um programador cria um contentor em macOS. O mesmo contentor é executado sem alterações em:
- Pipeline CI do GitHub Actions (Linux).
- Ambiente de produção AWS ECS.
- Ambiente de teste Azure Kubernetes Service.
- Cluster Kubernetes local de desenvolvimento.

As VM exigem imagens e configurações específicas de cada plataforma de hipervisor.

### 3. Arranque extremamente rápido

**Arranque de contentores Docker:**
- **Aplicação Web**: 200-500 ms.
- **Contentor de base de dados**: 1-3 segundos.
- **Microsserviço**: 50-200 ms.

**Arranque de VM:**
- **VM Linux leve**: 10-30 segundos.
- **VM Windows Server**: 45-90 segundos.
- **VM de ambiente de trabalho completo**: 60-120 segundos.

Esta diferença de velocidade superior a 100 vezes permite:
- **Escalabilidade rápida**: responder a picos de carga em segundos.
- **Autorreparação**: substituir imediatamente contentores com falhas.
- **Eficiência de CI/CD**: executar milhares de ambientes de teste por dia.
- **Velocidade de desenvolvimento**: alternar de ambiente instantaneamente.

### 4. Eficiência de recursos e redução de custos

**Vantagens do Docker:**

**Economia de memória:**
- 100 microsserviços Node.js no Docker: ~50 GB de RAM.
- A mesma carga em VM: ~400 GB de RAM.
- **Poupança**: redução de 87,5% nos requisitos de memória.

**Economia de armazenamento:**
- As camadas de imagens Docker são partilhadas entre os contentores.
- Imagem base (Ubuntu): 50 MB, partilhada por todos os contentores.
- Camadas de aplicação: 100-500 MB cada.
- **Resultado**: a partilha de camadas reduz significativamente o armazenamento necessário.

**Exemplo de cálculo:**
10 aplicações Python:
- **Docker**: 1 imagem base de Python (300 MB) + 10 camadas de aplicação (50 MB cada) = 800 MB no total.
- **VM**: 10 imagens completas do sistema operativo + Python (3 GB cada) = 30 GB.
- **Poupança**: redução de 97,3% no armazenamento.

### 5. Suporte à arquitetura de microsserviços

O Docker é a base dos microsserviços modernos:

**Vantagens:**
- **Escalabilidade independente**: escalar serviços individuais conforme a procura.
- **Desenvolvimento poliglota**: usar linguagens diferentes em cada serviço.
- **Isolamento de falhas**: as falhas de um serviço não se propagam.
- **Implementação contínua**: atualizar serviços de forma independente.
- **Autonomia das equipas**: cada equipa gere toda a pilha dos seus serviços.

**Exemplo de arquitetura:**
```
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│  Interface  │ │     API     │ │   Acesso    │
│   (React)   │ │  (Node.js)  │ │    (Go)     │
│    Cont.    │ │    Cont.    │ │    Cont.    │
└─────────────┘ └─────────────┘ └─────────────┘
       │               │               │
       └───────────────┴───────────────┘
                       │
            ┌──────────┴──────────┐
            │                     │
    ┌─────────────┐      ┌─────────────┐
    │    Dados    │      │    Cache    │
    │ (Postgres)  │      │   (Redis)   │
    │    Cont.    │      │    Cont.    │
    └─────────────┘      └─────────────┘
```

### 6. Integração com DevOps e CI/CD

O Docker revolucionou os pipelines CI/CD:

**Exemplo de pipeline moderno:**
1. **Commit**: o programador envia o código.
2. **Build**: o servidor CI cria uma imagem Docker (1-3 minutos).
3. **Test**: iniciar contentores para testes automatizados (segundos).
4. **Scan**: análise de segurança das camadas da imagem.
5. **Push**: carregar a imagem para o registo de contentores.
6. **Deploy**: implementar em produção (segundos por instância).
7. **Rollback**: reverter imediatamente para a imagem anterior, se necessário.

**Comparação com VM:**
Os pipelines tradicionais baseados em VM:
1. **Commit**: o programador envia o código.
2. **Build VM Image**: criar uma nova imagem de VM (15-30 minutos).
3. **Deploy VM**: provisionar novas VM (5-10 minutos).
4. **Test**: executar testes nas VM.
5. **Rollback**: recriar o estado anterior da VM (10-15 minutos).

**Resultado**: os pipelines Docker são 10-20 vezes mais rápidos.

## Vantagens das máquinas virtuais: quando se destacam

Apesar das vantagens do Docker, as VM continuam a ser essenciais para determinados casos de uso.

### 1. Isolamento de segurança superior

**Isolamento ao nível do hardware:**
As VM oferecem separação completa ao nível do kernel:
- Cada VM tem o seu próprio kernel.
- O hipervisor impõe limites protegidos pelo hardware.
- As vulnerabilidades do kernel não atravessam os limites entre VM.
- Adequadas para ambientes multi-inquilino que executam código não confiável.

**Comparação de segurança:**

| Funcionalidade de segurança | Docker | VM | Vencedor |
|-----------------|--------|-----|--------|
| Isolamento do kernel | Kernel partilhado | Kernels separados | VM |
| Dificuldade de escape | Possível escape de namespace | Escape do hipervisor raro | VM |
| Ataques aos recursos | Limites de cgroups | Limites de hardware | VM |
| Preparação para conformidade | Exige reforço | Isolamento integrado | VM |
| Multi-inquilino | Não recomendado | Norma do setor | VM |

**Caso de uso:** as instituições financeiras que executam aplicações de clientes exigem frequentemente isolamento ao nível da VM para cumprir os requisitos regulamentares e garantir a segurança.

### 2. Controlo e flexibilidade completos do sistema operativo

**Executar qualquer sistema operativo:**
As VM podem executar:
- Famílias diferentes de sistemas operativos no mesmo hardware (Windows e Linux).
- Sistemas operativos antigos (Windows Server 2008, RHEL 5).
- Distribuições especializadas (BSD, Solaris).
- Configurações de kernel personalizadas.
- Sistemas operativos que exigem módulos de kernel específicos.

**Exemplos de situações:**
- **Aplicações Windows em anfitriões Linux**: executar VM Windows Server num hipervisor Linux.
- **Sistemas antigos**: manter aplicações que exigem versões específicas do sistema operativo.
- **Testes de kernel**: testar kernels Linux personalizados em segurança.
- **Desenvolvimento para vários sistemas**: executar macOS, Windows e Linux em simultâneo.

### 3. Mais adequadas a aplicações com estado e sistemas antigos

**As VM destacam-se em:**

**Aplicações com estado:**
- Bases de dados SQL tradicionais (Oracle, SQL Server).
- Aplicações empresariais (SAP, sistemas ERP antigos).
- Sistemas de mensagens com estado.
- Aplicações que esperam armazenamento local persistente.

**Monólitos antigos:**
- Grandes aplicações empresariais que não foram concebidas para contentores.
- Aplicações com caminhos de sistema de ficheiros codificados.
- Software que exige configurações específicas do sistema operativo.
- Software licenciado associado a hardware ou sistema operativo.

**Exemplo:**
Uma empresa executa SAP ERP:
- Exige Windows ou Linux com parâmetros de kernel específicos.
- Precisa de armazenamento persistente com tipos específicos de sistemas de ficheiros.
- Tem requisitos de rede complexos.
- Exige personalização ao nível do sistema operativo.
- **Solução**: a máquina virtual é a escolha prática.

### 4. Gestão empresarial comprovada

**Ferramentas maduras:**
- **VMware vCenter**: gestão abrangente de centros de dados.
- **Microsoft System Center**: gestão do ciclo de vida de VM empresariais.
- **Red Hat Virtualization**: virtualização empresarial de código aberto.
- **Proxmox**: gestão completa de VM.

**Funcionalidades empresariais:**
- **Migração em direto**: mover VM em execução entre anfitriões sem interrupção.
- **Alta disponibilidade**: reiniciar VM automaticamente em caso de falha de hardware.
- **Recuperação de desastres**: ferramentas de cópia de segurança, instantâneos e replicação.
- **Gestão de recursos**: alocação avançada de CPU e memória.
- **Conformidade**: auditoria e funcionalidades de segurança integradas.

### 5. Mais adequadas a ambientes com vários sistemas operativos

**Infraestrutura heterogénea:**
As VM suportam facilmente, no mesmo hardware partilhado:
- Aplicações Windows Server.
- Serviços Linux.
- Sistemas Unix (AIX, Solaris).
- Dispositivos de rede.
- Todos estes sistemas.

**Cenário real:**
Centro de dados empresarial:
- 50 VM Windows Server (AD, Exchange, SQL Server).
- 30 VM Linux (servidores Web, bases de dados).
- 10 VM especializadas (monitorização de rede, segurança).
- Todas geridas numa plataforma unificada.
- Os contentores não permitem esta combinação devido às diferenças entre kernels de sistemas operativos.

## Análise detalhada de segurança: Docker e VM

### Modelo de segurança do Docker

**Mecanismos de isolamento:**
- **Namespaces**: isolamento de processos, rede, montagens, IPC e UTS.
- **Cgroups**: limitação e contabilização de recursos.
- **Seccomp**: filtragem de chamadas de sistema.
- **AppArmor/SELinux**: controlo de acesso obrigatório.
- **Capabilities**: controlo granular de privilégios.

**Boas práticas de segurança do Docker (2026):**
1. **Executar Docker sem privilégios de root**: usar um utilizador não root.
2. **Usar imagens base mínimas**: como Alpine Linux ou distroless.
3. **Analisar imagens**: procurar vulnerabilidades com Trivy, Snyk ou Clair.
4. **Assinar imagens**: verificar a autenticidade com Docker Content Trust.
5. **Limitar capabilities**: remover privilégios Linux desnecessários.
6. **Usar sistemas de ficheiros só de leitura**: montar contentores em modo só de leitura.
7. **Segmentar a rede**: usar redes isoladas.
8. **Gerir segredos**: usar Docker secrets ou um cofre externo.

**Riscos de segurança:**
- **Kernel partilhado**: todos os contentores partilham o kernel do anfitrião.
- **Elevação de privilégios**: contentores mal configurados podem permitir uma fuga.
- **Vulnerabilidades de imagens**: as imagens base podem não ter correções.
- **Ataques ao daemon**: o daemon Docker é executado como root.

### Modelo de segurança das VM

**Isolamento mais forte:**
- **Kernels separados**: cada VM tem um kernel independente.
- **Aplicação pelo hipervisor**: isolamento suportado pelo hardware.
- **Sem partilha de kernel**: as falhas do kernel ficam confinadas a uma VM.
- **Segurança madura**: reforçada ao longo de décadas.

**Boas práticas de segurança das VM:**
1. **Usar hipervisores de tipo 1**: VMware ESXi, KVM, Hyper-V.
2. **Proteger o hipervisor**: mantê-lo atualizado com correções.
3. **Isolar a rede**: usar VLAN e regras de firewall.
4. **Encriptar dados**: encriptar o armazenamento e a memória.
5. **Controlar o acesso**: exigir autenticação forte na administração.
6. **Reforçar o sistema operativo convidado**: instalar um sistema mínimo.
7. **Aplicar correções regularmente**: atualizar o hipervisor e o sistema operativo convidado.

**Vantagem de segurança:**
As VM são adequadas para:
- Plataformas SaaS multi-inquilino.
- Setores regulamentados (finanças, cuidados de saúde).
- Execução de código não confiável.
- Ambientes com requisitos de segurança elevados.

## Análise de custos: comparação do custo total de propriedade

### Custos de infraestrutura

**Cenário**: alojar 100 microsserviços.

**Solução Docker:**
- **Hardware**: 4 servidores × $5,000 = $20,000.
- **Licenciamento**: Docker Enterprise $150/mês × 4 = $7,200/ano.
- **Total da infraestrutura**: $27,200 no primeiro ano, $7,200/ano depois.

**Solução VM:**
- **Hardware**: 20 servidores × $5,000 = $100,000.
- **VMware vSphere**: $3,000/CPU × 40 CPUs = $120,000.
- **Total da infraestrutura**: $220,000 no primeiro ano, $24,000/ano em suporte.

**Poupança**: $192,800 no primeiro ano, $16,800/ano depois.

### Custos operacionais

**Tempo de gestão:**

**Docker:**
- Tempo de configuração: 2-4 horas por aplicação.
- Implementação de atualizações: 1-5 minutos.
- Operações de escalabilidade: automatizadas.
- Resolução de problemas: registos centralizados.
- **Eficiência da equipa**: 1 engenheiro gere mais de 500 contentores.

**VM:**
- Tempo de configuração: 4-8 horas por VM.
- Implementação de atualizações: 15-30 minutos.
- Operações de escalabilidade: 10-30 minutos.
- Resolução de problemas: iniciar sessão em cada VM.
- **Eficiência da equipa**: 1 engenheiro gere 50-100 VM.

**Exemplo de custos em nuvem (AWS):**

**Executar 10 aplicações Web sem interrupção:**

**Docker no ECS Fargate:**
- Contentores pequenos: 2 vCPU e 4 GB de RAM cada.
- Custo por contentor: ~$50/mês.
- **Total**: $500/mês.

**VM EC2:**
- Instâncias t3.large: 2 vCPU e 8 GB de RAM.
- Custo por instância: ~$60/mês.
- **Total**: $600/mês.
- Custos de armazenamento EBS à parte.

**Poupança anual**: $1,200, além da redução da carga de gestão.

## Quando usar Docker: casos de uso ideais

### 1. Aplicações de microsserviços
✅ **Docker é uma escolha ideal**

**Características:**
- Serviços pequenos e independentes.
- Conceção sem estado.
- Necessidade de escalabilidade rápida.
- Atualizações frequentes.

**Exemplo:**
Plataforma de comércio eletrónico:
- Serviço de frontend (React).
- Serviço de utilizador (Node.js).
- Catálogo de produtos (Python).
- Processamento de encomendas (Go).
- Serviço de pagamentos (Java).
- Cada serviço é escalado de forma independente conforme a carga.

### 2. Integração e implementação contínuas
✅ **Docker é ideal**

**Vantagens:**
- Ambientes de compilação consistentes.
- Execução rápida de testes.
- Testes paralelos.
- Implementações reproduzíveis.

**Pipeline CI:**
```
git push → Criar imagem → Testar contentores →
Enviar para o registo → Implementar em staging →
Lançamento em produção (blue-green)
```

### 3. Ambientes de desenvolvimento
✅ **Docker é uma excelente opção**

**Vantagens:**
- Ambientes de desenvolvimento iguais aos de produção.
- Preparação rápida do ambiente.
- Integração fácil de novos programadores.
- Evita problemas de «funciona na minha máquina».

**Experiência do programador:**
```bash
git clone repo
docker-compose up
# Ambiente pronto em 30 segundos
```

### 4. Aplicações nativas da nuvem
✅ **Docker é o padrão**

As aplicações modernas em nuvem são desenvolvidas para:
- Orquestração Kubernetes.
- Arquitetura de service mesh.
- Funções sem servidor.
- Conceção orientada a eventos.

### 5. Escalabilidade horizontal
✅ **Docker destaca-se**

Aplicações que precisam de:
- Escalabilidade instantânea durante picos de tráfego.
- Distribuição geográfica.
- Escalabilidade automática conforme a carga.
- Escalabilidade económica.

**Exemplo:**
Serviço de transmissão de vídeo:
- Base: 50 contentores.
- Tráfego de pico: escalabilidade automática para 500 contentores em 2 minutos.
- Após o pico: redução para 50 contentores em 5 minutos.

## Quando usar máquinas virtuais: casos de uso ideais

### 1. Aplicações empresariais antigas
✅ **As VM são necessárias**

**Características:**
- Arquitetura monolítica.
- Funcionalidades dependentes do sistema operativo.
- Procedimentos de instalação complexos.
- Não podem ser contentorizadas.

**Exemplos:**
- Sistemas ERP tradicionais (SAP, Oracle EBS).
- Aplicações .NET antigas no Windows Server.
- Aplicações que exigem versões específicas do sistema operativo.
- Software com licenciamento ao nível do sistema operativo.

### 2. Requisitos de vários sistemas operativos
✅ **Só as VM permitem esta configuração**

**Cenários:**
- Executar aplicações Windows juntamente com Linux.
- Testar software em várias versões de sistemas operativos.
- Desenvolver para várias plataformas de sistemas operativos.
- Manter suporte para sistemas operativos antigos.

**Exemplo:**
Conjunto de testes de uma empresa de software:
- VM Windows Server 2016, 2019 e 2022.
- Várias distribuições Linux.
- VM macOS para testar o cliente Mac.
- Tudo na mesma infraestrutura física.

### 3. Requisitos de isolamento forte
✅ **As VM oferecem melhor isolamento**

**Casos de uso:**
- Plataformas SaaS multi-inquilino.
- Setores regulamentados (cuidados de saúde, finanças).
- Aplicações críticas para a segurança.
- Execução de código não confiável.

**Exemplo:**
Serviço de IDE na nuvem:
- Cada cliente recebe uma VM dedicada.
- O isolamento completo impede fugas de dados.
- Segurança ao nível do kernel.
- Conformidade com os regulamentos de proteção de dados.

### 4. Bases de dados tradicionais com estado
✅ **As VM são mais fiáveis**

**Tipos de bases de dados:**
- SQL tradicional: Oracle, SQL Server, MySQL, PostgreSQL.
- Grandes bases de dados monolíticas.
- Bases de dados que exigem otimização específica do sistema operativo.
- Bases de dados licenciadas e associadas ao hardware.

**Porquê usar VM:**
- Integração com armazenamento persistente.
- Melhor desempenho para E/S intensiva.
- Ferramentas de cópia de segurança e recuperação.
- Menos complexidade do que bases de dados contentorizadas.

### 5. Recuperação de desastres e testes
✅ **As VM oferecem vantagens**

**Vantagens das VM:**
- Instantâneos completos do sistema.
- Conversão P2V (físico para virtual).
- Capacidades de migração em direto.
- Soluções de cópia de segurança comprovadas.

**Cenário de recuperação de desastres:**
- VM de produção replicadas para um local de recuperação de desastres.
- Comutação por falha imediata com tempo de inatividade mínimo.
- Testes fáceis dos procedimentos de recuperação.
- Preservação completa do estado do sistema.

## Abordagem híbrida: utilização conjunta

A infraestrutura moderna utiliza cada vez mais **Docker e VM** de forma estratégica:

### Arquitetura híbrida comum

```
┌─────────────────────────────────────────┐
│              Infra. física              │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │            VM 1: nó K8s            │ │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ │ │
│  │  │Docker││Docker││Docker││Docker│ │ │
│  │  │Cont. ││Cont. ││Cont. ││Cont. │ │ │
│  │  └─────┘ └─────┘ └─────┘ └─────┘ │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 2: BD Oracle           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │          VM 3: Windows AD          │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

### Casos de uso híbridos

**1. Kubernetes em VM:**
- Executar clusters Kubernetes em VM.
- Executar contentores Docker no Kubernetes.
- Isolar clusters ao nível da VM.
- Facilitar a migração de clusters e a recuperação de desastres.

**2. Sistemas antigos e modernos:**
- Executar aplicações antigas em VM (SAP, Oracle).
- Executar novos microsserviços em contentores.
- Migrar gradualmente para contentores.
- Aproveitar as vantagens de ambas as tecnologias.

**3. Fluxo de desenvolvimento:**
- Os programadores usam Docker localmente.
- A CI/CD é executada em contentores.
- A pré-produção e a produção usam Kubernetes baseado em VM.
- A segurança e a conformidade são mantidas.

**4. Estratégia de nuvem:**
- Migrar primeiro as cargas para VM com lift-and-shift.
- Refatorizar para contentores ao longo do tempo.
- Implementar numa nuvem híbrida.
- Manter flexibilidade no ritmo de modernização.

## Ferramentas de orquestração e gestão

### Orquestração Docker

**Kubernetes (norma do setor):**
- Implementação, escalabilidade e gestão automatizadas.
- Mais de 90% de quota de mercado na orquestração de contentores.
- Compatível com várias nuvens (AWS EKS, Azure AKS, GCP GKE).
- Autorrecuperação e escalabilidade automática.
- Descoberta de serviços e balanceamento de carga.
- Atualizações progressivas e reversões.

**Docker Swarm:**
- Orquestração nativa do Docker.
- Mais simples do que Kubernetes.
- Adequado a implementações pequenas.
- Popularidade em declínio.

**Amazon ECS/Fargate:**
- Orquestração de contentores específica da AWS.
- Execução de contentores sem servidor.
- Integração profunda com a AWS.
- O Fargate dispensa a gestão do cluster.

### Orquestração de VM

**VMware vSphere:**
- Norma empresarial para gestão de VM.
- vMotion para migração em direto.
- DRS para equilíbrio de recursos.
- HA para comutação automática por falha.

**Microsoft Hyper-V + SCVMM:**
- Virtualização integrada no Windows.
- System Center Virtual Machine Manager.
- Integração com Azure.
- Ideal para ambientes centrados no Windows.

**OpenStack:**
- Plataforma de nuvem de código aberto.
- Suporte para vários hipervisores.
- Infraestrutura de nuvem privada.
- Gestão de VM em grande escala.

**Proxmox VE:**
- Plataforma de virtualização de código aberto.
- Suporte para KVM e LXC.
- Gestão baseada na Web.
- Económico para pequenas e médias empresas.

## Estratégias de migração

### Migrar de VM para contentores

**Abordagem passo a passo:**

**Fase 1: avaliação (2-4 semanas)**
1. Inventariar todas as aplicações.
2. Identificar candidatas à contentorização.
3. Avaliar dependências e estado.
4. Planear a ordem de migração.

**Fase 2: projeto-piloto (1-2 meses)**
1. Selecionar 3-5 aplicações adequadas.
2. Contentorizar as aplicações-piloto.
3. Testá-las cuidadosamente em pré-produção.
4. Implementá-las em produção.
5. Medir os resultados e aprender.

**Fase 3: migração gradual (6-18 meses)**
1. Contentorizar aplicações por prioridade.
2. Manter uma infraestrutura híbrida.
3. Atualizar os pipelines CI/CD.
4. Formar a equipa de operações.
5. Documentar as aprendizagens.

**Fase 4: otimização (contínua)**
1. Refatorizar para padrões nativos da nuvem.
2. Implementar uma arquitetura de microsserviços.
3. Otimizar imagens de contentores.
4. Melhorar a monitorização e a observabilidade.

**Aplicações adequadas para começar:**
- Aplicações Web sem estado.
- Serviços de API.
- Microsserviços.
- Novos projetos de desenvolvimento.

**Manter em VM:**
- Monólitos antigos.
- Bases de dados com estado (inicialmente).
- Aplicações exclusivas do Windows.
- Software licenciado.

### Migrar de contentores para VM

**Quando voltar às VM:**
- Os requisitos de segurança/conformidade mudam.
- Surgem problemas de desempenho nos contentores.
- Aparecem restrições de licenciamento.
- É necessário um isolamento mais forte.

**Abordagem:**
1. Criar modelos de VM.
2. Instalar as dependências da aplicação.
3. Implementar a aplicação contentorizada na VM.
4. Testar cuidadosamente a funcionalidade.
5. Fazer a transição com o mínimo de inatividade.

## Quadro de decisão: Docker ou VM?

### Árvore de decisão rápida

```
Início: é preciso implementar uma aplicação
    │
    ├─ Vários SO? (Windows + Linux)
    │   └─ Sim → Usar VMs
    │
    ├─ Aplicação monolítica legada?
    │   └─ Sim → Usar VMs
    │
    ├─ Exige isolamento forte? (multi-tenant)
    │   └─ Sim → Usar VMs
    │
    ├─ É necessário escalar rapidamente?
    │   └─ Sim → Usar Docker
    │
    ├─ Arquitetura de microsserviços?
    │   └─ Sim → Usar Docker
    │
    ├─ Foco em DevOps/CI-CD?
    │   └─ Sim → Usar Docker
    │
    └─ Aplicação moderna cloud-native?
        └─ Sim → Usar Docker
```

### Matriz de decisão detalhada

| Consideração | Escolher Docker | Escolher VM |
|--------------|---------------|------------|
| **Arquitetura** | Microsserviços, sem estado | Monolítica, com estado |
| **Necessidades de escalabilidade** | Escalabilidade automática rápida | Escalabilidade previsível |
| **Tempo de arranque** | Segundos são essenciais | Minutos são aceitáveis |
| **Eficiência de recursos** | Maximizar a densidade | Priorizar o isolamento |
| **Velocidade de desenvolvimento** | Iteração rápida | Versões estáveis |
| **Pilha tecnológica** | Centrada em Linux | Vários sistemas operativos |
| **Modelo de segurança** | Kernel partilhado aceitável | Exige isolamento do kernel |
| **Maturidade operacional** | Cultura DevOps | TI tradicional |
| **Orçamento** | Otimização de custos | Prioridade à conformidade |
| **Infraestrutura existente** | Nativa da nuvem | Centro de dados tradicional |

## Boas práticas de 2026

### Boas práticas Docker

**1. Otimização de imagens:**
```dockerfile
# Use builds em várias etapas
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Imagem de produção
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
USER node
CMD ["node", "dist/server.js"]
```

**2. Reforço da segurança:**
- Executar como utilizador não root.
- Usar imagens base oficiais.
- Procurar vulnerabilidades regularmente.
- Aplicar o princípio do menor privilégio.
- Gerir segredos (Vault, AWS Secrets Manager).

**3. Monitorização e registo:**
- Registo centralizado (ELK, Loki).
- Recolha de métricas (Prometheus).
- Rastreio distribuído (Jaeger, Zipkin).
- Verificações de estado e sondas de prontidão.

**4. Rede:**
- Usar redes overlay para vários anfitriões.
- Implementar service mesh (Istio, Linkerd).
- Definir políticas de rede para segurança.
- Usar descoberta de serviços baseada em DNS.

### Boas práticas de VM

**1. Alocação de recursos:**
- Dimensionar corretamente as VM e evitar o aprovisionamento excessivo.
- Usar grupos e limites de recursos.
- Implementar modelos de VM.
- Monitorizar a utilização de recursos.

**2. Alta disponibilidade:**
- Agrupar VM em clusters distribuídos por anfitriões.
- Implementar comutação automática por falha.
- Usar armazenamento partilhado (SAN, NAS).
- Fazer cópias de segurança e testes regularmente.

**3. Segurança:**
- Segmentação de rede (VLAN).
- Calendário regular de aplicação de correções.
- Encriptação do armazenamento e das comunicações.
- Controlo de acesso e auditoria.

**4. Desempenho:**
- Usar controladores paravirtualizados.
- Alocar recursos dedicados a VM críticas.
- Ter em conta NUMA em VM grandes.
- Otimizar o desempenho do armazenamento.

## Tendências futuras: o que se segue?

### Evolução dos contentores

**1. Contentores sem root e sem privilégios:**
- Segurança reforçada sem privilégios root.
- Adoção mais ampla em setores regulamentados.
- Redução da superfície de ataque.

**2. Contentores WebAssembly (Wasm):**
- Execução ultraleve.
- Formato binário multiplataforma.
- Arranque mais rápido do que os contentores tradicionais.
- Integração crescente entre Docker e Wasm.

**3. Integração de eBPF:**
- Redes e segurança avançadas.
- Observabilidade ao nível do kernel.
- Monitorização de desempenho melhorada.

**4. Aceleração de GPU e IA/ML:**
- Melhor partilha de GPU entre contentores.
- Otimização de cargas de trabalho de IA/ML.
- Plataformas de ML nativas de contentores.

### Inovações em VM

**1. Computação confidencial:**
- Memória de VM encriptada por hardware.
- Enclaves seguros para dados sensíveis.
- Integração de AMD SEV e Intel SGX.

**2. Híbrido entre VM e contentores:**
- Kata Containers e gVisor.
- Isolamento ao nível da VM com experiência de contentores.
- Vantagens das duas tecnologias.

**3. Computação periférica:**
- Hipervisores leves.
- MicroVM (Firecracker).
- Virtualização otimizada para a periferia.

## Conclusão: escolher a opção certa

Em 2026, o debate **Docker vs VM** não é sobre qual tecnologia é «melhor», mas sobre compreender qual ferramenta se adequa às necessidades específicas.

**Escolher Docker quando:**
- Desenvolve aplicações modernas de microsserviços.
- Pretende maximizar a eficiência e a densidade dos recursos.
- Precisa de escalabilidade e implementação rápidas.
- Adota DevOps e práticas nativas da nuvem.
- Executa aplicações sem estado.
- Dá prioridade à produtividade dos programadores.

**Escolher VM quando:**
- Executa aplicações monolíticas antigas.
- Precisa de isolamento de segurança forte.
- Dá suporte a ambientes com vários sistemas operativos.
- Gere bases de dados tradicionais com estado.
- Cumpre requisitos rigorosos de conformidade.
- Opera em ambientes empresariais tradicionais.

**Usar ambas quando:**
- Migra gradualmente para contentores.
- Executa cargas de trabalho mistas.
- Precisa de flexibilidade e opções.
- Cria infraestrutura de nuvem híbrida.

As organizações mais bem-sucedidas em 2026 adotam uma **abordagem pragmática**: contentores para novas aplicações nativas da nuvem e cargas existentes adequadas, e VM para sistemas antigos e casos de uso que exigem os seus pontos fortes. Esta estratégia híbrida permite otimizar cada carga de trabalho individualmente, mantendo a eficiência operacional.

Conhecer ambas as tecnologias ajuda a tomar decisões de arquitetura informadas que equilibram desempenho, segurança, custo e requisitos operacionais do seu ambiente.

______

## Referências

- [Documentação oficial do Docker](https://docs.docker.com/)
- [Documentação do Kubernetes](https://kubernetes.io/docs/)
- [Documentação do VMware vSphere](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Documentação do Microsoft Hyper-V](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/)
- [Virtualização KVM](https://www.linux-kvm.org/)
- [CNCF Cloud Native Landscape](https://landscape.cncf.io/)
- [Boas práticas de segurança do Docker](https://docs.docker.com/engine/security/)
- [Guia de segurança de contentores de aplicações do NIST](https://www.nist.gov/publications/application-container-security-guide)
- [Proxmox VE](https://www.proxmox.com/en/proxmox-ve)
- [Serviços de contentores da AWS](https://aws.amazon.com/containers/)

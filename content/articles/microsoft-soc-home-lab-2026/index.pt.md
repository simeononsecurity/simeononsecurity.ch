---
title: "Laboratório SOC Microsoft em casa: desenvolva experiência em cibersegurança em 2026"
date: 2026-09-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Monte um laboratório SOC Microsoft com Sentinel, Defender, Intune e Entra. Investigue incidentes, valide políticas de passkeys e documente evidências para seu portfólio."
genre: ["Cibersegurança", "Segurança em nuvem", "Desenvolvimento profissional"]
tags: ["laboratório SOC doméstico", "Microsoft Sentinel", "Microsoft Defender XDR", "Defender for Endpoint", "Defender for Cloud", "Defender for Servers", "Microsoft Intune", "Microsoft Entra ID", "laboratório Azure doméstico", "experiência em cibersegurança", "analista SOC", "centro de operações de segurança", "resposta a incidentes", "KQL", "Log Analytics", "Conditional Access", "MFA resistente a phishing", "passkeys", "segurança de identidade", "portfólio de cibersegurança", "gestão de custos de nuvem", "segurança de endpoints"]
cover: "/img/cover/microsoft-soc-home-lab.webp"
coverAlt: "Um laptop mostra cronologias de incidentes de segurança em uma mesa doméstica, sob uma nuvem com servidores e endpoints."
coverCaption: ""
---

Um **laboratório SOC doméstico** oferece um local para investigar alertas, explicar evidências e testar mudanças defensivas. Monte um pequeno ambiente Microsoft, colete telemetria e documente cada investigação. O resultado útil é uma investigação repetível apoiada por evidências.

Este guia desenvolve a abordagem de laboratório descrita no vídeo de carreira em cibersegurança de Mad Hat e no runbook Cyber Range fornecido. Usa a documentação da Microsoft para requisitos dos produtos e separa configuração, detecção e validação em tarefas mensuráveis.

## Principais pontos

- **Comece pequeno:** um cliente Windows gerenciado e uma identidade de teste atendem aos primeiros exercícios.
- **Verifique a telemetria:** ver um dispositivo ou portal conectado não comprova que os logs estão chegando.
- **Conclua a investigação:** registre o gatilho, as evidências, a resposta e o novo teste.
- **Controle os gastos:** acompanhe licenças, retenção de dados, rede e computação separadamente.
- **Descreva sua experiência com precisão:** apresente o ambiente como projeto de laboratório no currículo.

## Antes de começar

**Pré-requisitos:** conhecimentos básicos de administração do Windows e redes, além de familiaridade com máquinas virtuais. Use um tenant Microsoft Entra dedicado e uma assinatura Azure reservada ao laboratório. Mantenha identidades de produção, arquivos pessoais e sistemas do empregador fora do exercício.

**Esforço estimado:** reserve um fim de semana para a configuração inicial e depois faça sessões de investigação focadas. Esta é uma estimativa de planejamento. Aprovação da avaliação, cotas e provisionamento de serviços afetam o tempo real. **Dificuldade:** intermediária.

Prepare uma conta administrativa separada e um usuário de teste sem privilégios. Antes de testar políticas de acesso, estabeleça e verifique o acesso de emergência. Conceda privilégios para cada tarefa de configuração e use uma conta menos privilegiada nas investigações de rotina.

| Componente | Finalidade no laboratório |
|---|---|
| **Sentinel** | Gerenciamento de informações e eventos de segurança (SIEM) para fontes de log conectadas |
| **Defender XDR** | Correlação e investigação entre serviços Microsoft de segurança licenciados |
| **Defender for Endpoint** | Detecção e resposta em endpoints integrados |
| **Intune** | Inscrição de dispositivos e gerenciamento de políticas de segurança de endpoints |
| **Entra ID** | Identidades, registros de entrada e avaliação de políticas de acesso |
| **Defender for Servers** | Proteção de servidores pelo Defender for Cloud |

## Confira as licenças primeiro

**Microsoft 365 E5** é uma opção para um laboratório amplo, mas o acesso depende dos planos de serviço e licenças atribuídos aos usuários participantes. Office 365 E5 e Microsoft 365 E5 são pacotes diferentes. A licença de um administrador não garante cobertura para cada usuário de teste ou carga. Consulte os [pré-requisitos do Defender XDR](https://learn.microsoft.com/en-us/defender-xdr/prerequisites) antes de escolher uma assinatura.

**Sentinel no portal Defender** funciona sem E5 ou Defender XDR. Adicionar XDR traz requisitos próprios de licenciamento e configuração. Uma lista de incidentes vazia não comprova falta de licença E5. A [documentação de integração do Sentinel](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard) explica as duas configurações.

**A proteção de servidores** tem um caminho de licenciamento separado. Defender for Servers integra-se ao Defender for Endpoint para cargas de servidor compatíveis. Sistemas Windows cliente precisam da cobertura de cliente adequada. Não presuma que toda VM do Azure tenha licença de servidor automática. Consulte a documentação Microsoft sobre a [integração do Defender for Endpoint](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

**Planeje a avaliação:** confirme elegibilidade, expiração, renovação e serviços incluídos na sua conta. Não baseie o orçamento em uma duração prometida de avaliação ou em um total mensal fixo de um vídeo.

## Defina um plano de gastos

**Os orçamentos do Azure** enviam notificações. Eles não interrompem o consumo ao atingir um limite. Os relatórios de custo também têm atraso. Crie alertas cedo e revise gastos após cada sessão usando o [guia de orçamento da Microsoft](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/tutorial-acm-create-budgets).

| Categoria de custo | Pergunta de planejamento |
|---|---|
| **Licenças de usuário** | Quais usuários precisam de quais planos de serviço, e quando as avaliações expiram? |
| **Computação** | Quantas horas de VM cada exercício exige? |
| **Armazenamento** | Quais discos e instantâneos continuam após o desligamento? |
| **Coleta de logs** | Quais tabelas precisam de ingestão e por quanto tempo os dados devem ficar retidos? |
| **Rede** | O projeto inclui Bastion pago, IPs públicos ou serviços de saída? |
| **Proteção de servidores** | Quais cargas têm um plano Defender pago habilitado? |

**Decisão de projeto:** comece com um cliente. Adicione um servidor quando um exercício exigir telemetria dele. Quatro clientes e vários servidores elevam a administração e os custos antes de acrescentar prática útil de investigação.

## Monte a rede

**Layout sugerido:** coloque recursos Azure em um grupo com nome claro, como **`rg-soc-lab`**. Use sub-redes separadas para clientes e servidores, regras explícitas de grupos de segurança de rede e acesso administrativo privado. A separação das sub-redes, por si só, não bloqueia o tráfego entre cargas.

Para uma implantação dedicada do **Azure Bastion**, siga os requisitos do SKU, incluindo o nome reservado **`AzureBastionSubnet`** e uma sub-rede **`/26`** ou maior nas implantações atuais. O Developer SKU usa outro modelo. Consulte as [configurações do Bastion](https://learn.microsoft.com/en-us/azure/bastion/configuration-settings) antes de decidir.

Mantenha RDP e SSH fechados à Internet pública. Restrinja o tráfego administrativo ao caminho escolhido. Permita a conectividade de saída necessária para inscrição e telemetria de segurança.

**Validação:** estabeleça acesso administrativo privado e verifique as regras de rede efetivas antes de instalar cargas. Se adicionar depois um aplicativo deliberadamente vulnerável, mantenha-o na rede do exercício e restrinja o acesso às máquinas de teste.

## Conecte o Sentinel e os logs

**Configuração do portal:** crie um workspace do Log Analytics e habilite o Sentinel nele. Se o workspace não aparecer no portal Defender, abra **System > Settings > Microsoft Sentinel > Connect a workspace**. Verifique o tenant e as funções Azure e Entra exigidas nos [pré-requisitos de integração](https://learn.microsoft.com/en-us/unified-secops/microsoft-sentinel-onboard).

**A coleta de logs é uma etapa separada.** No Entra, configure as definições de diagnóstico para enviar as categorias de atividade necessárias ao mesmo workspace. Comece com entradas interativas e eventos de auditoria. O [guia de integração de logs Entra](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-integrate-activity-logs-with-azure-monitor-logs) explica permissões e destino.

O fluxo atual do Sentinel também aceita conexão pelo portal Microsoft Defender. Antes de investigar uma tabela vazia, confirme que o workspace primário é o pretendido, que o tenant corresponde às identidades de teste e que a conta tem as funções exigidas. A visibilidade no portal não prova ingestão. [Integração do Sentinel no portal Defender](https://learn.microsoft.com/en-us/azure/sentinel/microsoft-sentinel-onboard)

```kusto
SigninLogs
| where TimeGenerated > ago(24h)
| where UserPrincipalName =~ "soc-test@YOUR-TENANT.onmicrosoft.com"
| project TimeGenerated, UserPrincipalName, AppDisplayName,
          IPAddress, ResultType, ConditionalAccessStatus, CorrelationId
| order by TimeGenerated desc
```

Execute este exemplo de **Kusto Query Language (KQL)** na exibição Logs do workspace após gerar uma nova entrada de teste. Troque o UPN de exemplo pelo usuário do laboratório. As colunas seguem o [esquema da tabela SigninLogs](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/signinlogs).

**Resultado esperado:** uma linha correspondente à conta de teste e ao horário da entrada. Sem linhas, confira intervalo de tempo, identidade, configurações de coleta, destino e atraso de ingestão. Uma tabela ausente indica primeiro um problema de coleta ou workspace, depois um problema de detecção.

## Integre o primeiro endpoint

**A inscrição no Intune e a integração EDR** são etapas separadas. Conecte Intune e Defender for Endpoint, inscreva um cliente Windows compatível e atribua uma política de integração EDR ao grupo de laboratório. O registro Entra, sozinho, não confirma nenhuma etapa.

No Intune, confira **Endpoint security > Defender for Endpoint**. Se a conexão não estiver disponível, habilite a conexão Intune nos recursos avançados de endpoint do Defender. Siga as etapas específicas da plataforma no [guia de integração do Intune e Defender](https://learn.microsoft.com/en-us/intune/device-security/microsoft-defender/configure-integration).

| Verificação | Evidência a registrar |
|---|---|
| **Inscrição** | Cliente aparece no Intune com sincronização recente |
| **Atribuição da política** | Política de integração se aplica ao grupo de dispositivos pretendido |
| **Relatório do sensor** | Defender mostra status integrado e telemetria recente |
| **Teste de detecção** | Teste documentado produz o sinal de segurança esperado |

**Para servidores**, habilite o plano Defender for Servers escolhido e a integração de endpoint, depois verifique a implantação e os relatórios do sensor. Defender for Cloud também descobre máquinas antes da conclusão da integração. A presença no inventário não basta, como explica o guia Microsoft de [descoberta e integração de recursos](https://learn.microsoft.com/en-us/azure/defender-for-cloud/integration-defender-for-endpoint).

## Investigue um alerta de teste

**Comece pelo teste de detecção EDR documentado pela Microsoft** no endpoint do laboratório. Siga as [instruções atuais do teste](https://learn.microsoft.com/en-us/defender-endpoint/edr-detection), incluindo pré-requisitos da plataforma e solução de problemas. Anote o horário de execução antes de abrir a fila de alertas.

Trate o alerta resultante como exercício de investigação. O título do produto é um ponto de partida. Sua tarefa é determinar o que ocorreu e sustentar a decisão com evidências.

1. **Triagem:** identifique a origem do alerta, dispositivo, conta e horário do evento.
2. **Inspeção:** examine a árvore de processos, linha de comando, detalhes do arquivo e atividade de rede disponível.
3. **Escopo:** busque atividade relacionada na identidade de teste e nos outros dispositivos do laboratório.
4. **Avaliação:** explique se as evidências correspondem ao exercício planejado ou a um evento alheio.
5. **Resposta:** documente a resposta escolhida, o impacto e as etapas de recuperação. Faça contenção suportada somente quando o exercício exigir.
6. **Novo teste:** após alterar um controle, repita o teste relevante e compare as evidências.

**Não invente resultados ausentes.** Se o alerta não chegar, preserve o registro da execução e investigue a coleta. Se um controle bloquear o teste antes do evento esperado, documente o resultado da prevenção.

## Teste os controles de identidade

**O phishing adversary-in-the-middle (AiTM)** coloca um intermediário controlado por um invasor no fluxo de entrada. O runbook fornecido usa esse cenário para motivar autenticação mais forte. No primeiro exercício de identidade, teste o comportamento da política diretamente com sua própria conta sem privilégios.

Comece registrando uma entrada legítima e os detalhes da autenticação. Revise a [referência Microsoft de detecção de risco do Entra](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-risks) antes de interpretar os sinais. Os pré-requisitos e o processamento variam por sinal. Um novo endereço IP ou uma entrada malsucedida não garantem alerta AiTM.

**Passkeys (FIDO2)** usam credenciais vinculadas ao serviço legítimo, em vez de códigos reutilizáveis digitados em uma página de entrada retransmitida. Habilite um perfil de passkey apropriado ao grupo piloto e registre o método antes de aplicar uma política. Consulte o [guia Microsoft de configuração de passkeys](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2) para autenticadores aceitos e restrições.

**Exercício de Conditional Access:** crie uma política direcionada apenas ao grupo piloto do laboratório, exclua contas de acesso de emergência e escolha **Require authentication strength > Phishing-resistant MFA strength**. Comece em **Report-only**, revise o impacto e então habilite a política. Adapte o [exemplo Microsoft de política administrativa](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-admin-phish-resistant-mfa) a um grupo pequeno de teste.

| Teste | Evidência a coletar |
|---|---|
| **Política Report-only** | Registro de entrada que mostra a avaliação da política proposta |
| **Política aplicada, método mais fraco** | Nova autenticação exige método mais forte antes de conceder acesso |
| **Política aplicada, passkey registrada** | Entrada bem-sucedida que atende à força exigida |

Use nova autenticação em cada comparação e examine os detalhes da política. Sessões existentes dificultam a comparação. **Escopo da comprovação:** o exercício valida o requisito de autenticação. Não demonstra proteção universal contra comprometimento de endpoint ou roubo de sessão existente.

## Registre evidências para o portfólio

**Uma entrada útil no portfólio** explica uma decisão para que outro analista possa avaliá-la. Inclua uma breve descrição da arquitetura, os pré-requisitos de coleta, a linha do tempo do evento e a justificativa da resposta.

```text
Exercício:
Data e intervalo de horário UTC:
Escopo do laboratório e pré-requisitos:
Gatilho e sinal esperado:
Alerta observado ou prevenção:
Evidências e consultas:
Identidades e dispositivos afetados:
Conclusão e justificativa:
Resposta e recuperação:
Alteração do controle e novo teste:
Limitações e acompanhamento:
```

Substitua cada campo pelas próprias observações. **Sanitize as exportações:** remova credenciais, material de sessão, informações pessoais e identificadores desnecessários antes de publicar capturas ou resultados de consultas.

**Exemplo de currículo:** “Criei um laboratório de segurança Microsoft, conectei logs de identidade ao Sentinel, investiguei alertas de teste de endpoint e documentei a validação do Conditional Access.” Use esta redação somente após concluir essas tarefas. Inclua-a em projetos ou treinamento prático, com datas e escopo reais.

Um laboratório demonstra prática independente. **O trabalho em um SOC de produção** também envolve impacto nos negócios, escalonamento, compromissos de serviço e coordenação entre equipes. Explique quais partes você praticou e quais ainda estão fora da sua experiência.

## Solução de problemas

| Sintoma | Primeira verificação |
|---|---|
| **Workspace ausente do Defender** | Mesmo tenant, Sentinel habilitado e funções exigidas |
| **SigninLogs ausente ou vazio** | Categorias de diagnóstico, workspace de destino, eventos novos e intervalo |
| **Cliente ausente do Intune** | Pré-requisitos e status da inscrição |
| **Dispositivo visível sem telemetria** | Estado real da integração, saúde do sensor e conectividade de saída |
| **Política de integração não aplicada** | Escopo de atribuição, plataforma e sincronização recente |
| **Sem alerta de risco de identidade** | Pré-requisitos do sinal e atividade registrada, sem presumir detecção determinística |
| **Acesso permitido inesperadamente** | Status Report-only, exclusões, escopo do recurso e sessão existente |
| **Cobranças após desligar** | Estado de alocação e recursos cobrados fora da computação |

**Ordem de solução:** comprove primeiro que o evento ocorreu, depois que a coleta funcionou e então analise a lógica de detecção. Registre cada falha e correção nas notas do projeto.

## Pause ou remova o laboratório

**A desalocação** libera a alocação de computação da VM. Apenas desligar o sistema operacional convidado não garante a desalocação. Confira o estado de energia no Azure e consulte a documentação Microsoft sobre [estados e cobrança de VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/states-billing).

**Recursos retidos** também precisam de revisão. Discos, instantâneos, serviços de rede, retenção de logs e assinaturas de usuário têm ciclos de vida próprios. Defina um lembrete antes de cada avaliação expirar e confira o próximo relatório de uso após a limpeza.

Antes de excluir o grupo de recursos do laboratório, exporte e inspecione as evidências que pretende manter. **Excluir o grupo de recursos é destrutivo** para os recursos contidos. Usuários do tenant, políticas Intune e Conditional Access, assinaturas e configurações de segurança no nível da assinatura podem exigir limpeza separada.

## Próximos passos

**Conclua uma investigação documentada** antes de adicionar outra carga. Depois, adicione um servidor, um exercício de identidade ou uma regra de detecção com uma condição de teste clara. Registre o que o novo componente ensina e quanto custa.

Use o [guia de laboratório de TI](/it-career-playbook/getting-started-in-it/building-an-it-home-lab/) para praticar infraestrutura e o [guia de currículo de TI](/it-career-playbook/getting-a-job-in-it/it-resume-writing-tips/) para apresentar o trabalho. Mantenha o próximo projeto pequeno o suficiente para explicar configuração, evidências e limpeza.

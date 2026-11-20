---
title: "Proteja seu ambiente de nuvem com o Microsoft Defender for Cloud"
date: 2023-04-10
lastmod: 2026-11-20
toc: true
draft: false
description: "Proteja cargas de trabalho do Azure com o Microsoft Defender for Cloud. Consulte os termos antigos do Azure Security Center, as recomendações, as políticas e as etapas de resposta."
tags: ["Azure", "Security Center", "segurança na nuvem", "Azure Sentinel", "Azure Defender", "segurança de rede", "gestão de identidades", "segurança de dados", "detecção de ameaças", "resposta a ameaças", "MFA", "RBAC", "NSGs", "Azure Firewall", "WAF", "Azure AD", "Azure Information Protection", "Azure Storage Service Encryption", "Azure Disk Encryption"]
cover: "/img/cover/A_shield_icon_surrounded_by_cloud_symbols.webp"
coverAlt: "Um escudo cercado por símbolos de nuvem representa um ambiente de nuvem seguro. O escudo exibe o logotipo do Azure Security Center."
coverCaption: ""
---

**Como proteger seu ambiente de nuvem com o Azure Security Center**

Proteger o ambiente de nuvem é essencial para manter os dados, aplicativos e infraestrutura da organização longe de ameaças. O **Azure Security Center**, da Microsoft, ajuda você a melhorar sua postura de segurança e identificar riscos potenciais no Azure. Este artigo explica como proteger o ambiente usando o Azure Security Center e apresenta boas práticas para aplicar recursos de segurança. Também inclui detalhes técnicos e exemplos para orientar a implementação.

*Os nomes dos produtos mudaram desde a publicação original deste artigo. O Microsoft Azure Security Center agora se chama Microsoft Defender for Cloud. O Azure Active Directory agora se chama Microsoft Entra ID. O Azure Sentinel agora se chama Microsoft Sentinel. Azure Defender designa os planos Defender e as proteções de cargas de trabalho no Defender for Cloud. Os nomes antigos aparecem abaixo quando descrevem a terminologia de 2023.*

A [visão geral atual do Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction) descreve uma plataforma de proteção de aplicativos nativos da nuvem, com gerenciamento da postura de segurança na nuvem, DevSecOps e proteção de cargas de trabalho. A disponibilidade de recursos e o licenciamento dependem da nuvem, do tipo de recurso, da assinatura e do plano.

______

## Entenda o Azure Security Center

O Azure Security Center é um **sistema unificado de gerenciamento da segurança da infraestrutura**. Ele ajuda a identificar e corrigir vulnerabilidades potenciais no ambiente de nuvem. Seus recursos incluem detecção de ameaças, gerenciamento da postura de segurança e gerenciamento de conformidade.

**Avaliação contínua de segurança** e **Proteção avançada contra ameaças** são dois recursos importantes do Azure Security Center. A avaliação contínua ajuda a encontrar problemas de segurança potenciais. A proteção avançada ajuda a detectar e responder a ameaças potenciais.

______

## Implemente políticas de segurança e padrões de conformidade

O Azure Security Center permite aplicar e administrar políticas de segurança em todo o ambiente de nuvem. Use o serviço **Azure Policy** para criar políticas personalizadas ou aplicar as políticas internas para impor boas práticas e padrões de conformidade. Compare sua postura de segurança a padrões do setor, como [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final), [CIS](https://www.cisecurity.org/) e [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html).

O Azure Security Center também oferece recursos de gerenciamento de conformidade. Eles ajudam a acompanhar a situação da organização diante de estruturas regulatórias como [GDPR](https://gdpr.eu/), [HIPAA](https://www.hhs.gov/hipaa/index.html) e [PCI DSS](https://www.pcisecuritystandards.org/).

______

## Proteja seus recursos do Azure

**Manter a higiene de segurança dos recursos** é uma parte importante da proteção do ambiente de nuvem. O Azure Security Center oferece o **Secure Score**, uma medida da postura de segurança que ajuda você a avaliar a proteção geral dos recursos. Aplique as recomendações do Azure Security Center para melhorar a pontuação.

### Segurança de rede

Medidas como **Network Security Groups (NSGs)**, **Azure Firewall** e **Web Application Firewall (WAF)** ajudam a proteger o Azure contra ameaças. Elas controlam o tráfego de rede de entrada e saída e reduzem o risco de acesso não autorizado e ataques.

#### Network Security Groups (NSGs)

Os NSGs funcionam como firewalls virtuais para recursos do Azure. Você define regras para permitir ou negar tráfego de rede de e para esses recursos. Este exemplo cria um NSG com regras de tráfego:

```azurecli
# Crie um Network Security Group
az network nsg create --name MyNSG --resource-group MyResourceGroup

# Adicione regras para permitir ou negar tráfego
az network nsg rule create --name MyNSGRule --nsg-name MyNSG --priority 100 --resource-group MyResourceGroup --access Allow --protocol Tcp --direction Inbound --source-address-prefixes '*' --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '80'
```
Consulte a documentação oficial sobre [Network Security Groups](https://docs.microsoft.com/en-us/azure/virtual-network/security-overview).

O exemplo permite tráfego TCP de entrada na porta 80 de qualquer origem IPv4. Em produção, use um intervalo de origem conhecido, um ponto de extremidade privado ou um caminho por balanceador de carga. Leia a [visão geral de segurança dos NSGs](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview) antes de usar o exemplo.

#### Azure Firewall

O Azure Firewall é um serviço gerenciado de segurança de rede baseado na nuvem. Ele protege recursos do Azure e oferece filtragem baseada em inteligência de ameaças, categorias da Web e registro e análise centralizados. Para configurá-lo, siga as [instruções de início rápido](https://learn.microsoft.com/en-us/azure/firewall-manager/quick-firewall-policy-bicep).

#### Web Application Firewall (WAF)

O Web Application Firewall (WAF) é um recurso do **Azure Application Gateway**. Ele protege aplicativos Web contra ataques comuns, como injeção de SQL, cross-site scripting e outras explorações. Integre o WAF aos aplicativos existentes e configure regras próprias para padrões de ataque específicos.

Exemplo de criação de um Application Gateway com o WAF ativado:

```azurecli
# Crie uma política do WAF
az network application-gateway waf-policy create --name MyWafPolicy --resource-group MyResourceGroup --location EastUS

# Crie uma rede virtual e uma sub-rede
az network vnet create --name MyVNet --resource-group MyResourceGroup --location EastUS --address-prefix 10.0.0.0/16
az network vnet subnet create --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --address-prefix 10.0.0.0/24

# Crie um endereço IP público
az network public-ip create --name MyPublicIP --resource-group MyResourceGroup --location EastUS --sku Standard

# Crie um Application Gateway com o WAF ativado
az network application-gateway create --name MyAppGateway --resource-group MyResourceGroup --location EastUS --vnet-name MyVNet --subnet MySubnet --public-ip-address MyPublicIP --http-settings-cookie-based-affinity Enabled --sku WAF_v2 --waf-policy MyWafPolicy

```
Consulte a documentação oficial sobre [Web Application Firewall](https://docs.microsoft.com/en-us/azure/web-application-firewall/ag/ag-overview).

### Gerenciamento de identidade e acesso

**Microsoft Entra ID, anteriormente chamado Azure Active Directory (Azure AD),** é essencial para proteger seu ambiente de nuvem. O Defender for Cloud recomenda medidas para melhorar o gerenciamento de identidade e acesso, como ativar **Multi-Factor Authentication (MFA)**, aplicar **Role-Based Access Control (RBAC)** e monitorar atividades suspeitas.

#### Multi-Factor Authentication (MFA)

A MFA acrescenta uma camada de segurança às contas do Azure AD. Antes de conceder acesso, ela exige duas ou mais formas de verificação. Para ativar a MFA na organização, siga o [guia passo a passo](https://docs.microsoft.com/en-us/azure/active-directory/authentication/tutorial-enable-azure-mfa) da Microsoft.

Exemplo: Ative a MFA para um usuário

```powershell
# Conecte-se ao Azure AD
Connect-AzureAD

# Ative a MFA para um usuário específico
$UserPrincipalName = "johndoe@example.com"
$StsUserObjectID = (Get-AzureADUser -Filter "UserPrincipalName eq '$UserPrincipalName'").ObjectId
$StrongAuthRequirements = @(@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="1"};@{"Location"=""; "SatisfactionFactor"="2"; "VerificationMethod"="2"})
Set-AzureADUser -ObjectId $StsUserObjectID -StrongAuthenticationRequirements $StrongAuthRequirements
```
#### Role-Based Access Control (RBAC)

O RBAC permite definir permissões detalhadas para recursos do Azure, para que cada usuário tenha o nível de acesso adequado. Atribua funções a usuários, grupos ou aplicativos para administrar o acesso aos recursos da organização. Para implementar o RBAC, siga o [guia oficial](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview) da Microsoft.

Exemplo: Atribua uma função a um usuário

```azurecli
# Atribua a função Reader a um usuário
az role assignment create --assignee johndoe@example.com --role "Reader" --scope "/subscriptions/your_subscription_id/resourceGroups/your_resource_group"
```
#### Monitore atividades suspeitas

O Azure AD oferece **Identity Protection** e **Conditional Access** para monitorar e responder a atividades suspeitas. O Identity Protection usa aprendizado de máquina para detectar anomalias e tentativas de entrada arriscadas. O Conditional Access permite controlar o acesso com políticas baseadas em fatores como dispositivo, localização e risco.

Para configurar o Azure AD Identity Protection, siga o [guia oficial](https://learn.microsoft.com/en-us/azure/active-directory/identity-protection/concept-identity-protection-b2b) da Microsoft.

Exemplo: Crie uma política de Conditional Access

```powershell
# Conecte-se ao Azure AD
Connect-AzureAD

# Crie uma política de Conditional Access
$PolicyName = "BlockSignInFromUnknownLocations"
$PolicyDescription = "Bloqueie entradas de usuários em locais desconhecidos."
$PolicyState = "Enabled"
$Conditions = @{
    "SignInRiskLevels" = @("medium","high");
    "Locations" = @{
        "Included" = @();
        "Excluded" = @("AllTrusted")
    }
}
$GrantControls = @{
    "Operator" = "OR";
    "BuiltInControls" = @("Block")
}
New-AzureADMSConditionalAccessPolicy -DisplayName $PolicyName -State $PolicyState -Conditions $Conditions -GrantControls $GrantControls -Description $PolicyDescription

```
Consulte a documentação oficial sobre [Azure AD Identity Protection](https://docs.microsoft.com/en-us/azure/active-directory/identity-protection/overview) e [Conditional Access](https://learn.microsoft.com/en-us/azure/active-directory/conditional-access/overview).

### Segurança de dados

Proteger dados na nuvem é essencial. O Azure Security Center oferece **Azure Information Protection**, **Azure Storage Service Encryption** e **Azure Disk Encryption**. Esses recursos ajudam a criptografar dados e administrar o acesso a eles.

#### Azure Information Protection

**Azure Information Protection (AIP)** é um serviço na nuvem para classificar, rotular e proteger documentos e e-mails confidenciais. O AIP inclui rótulos como "Confidencial" e "Pessoal", que você pode adaptar às necessidades da organização. Também é possível configurar a aplicação automática de rótulos com base em regras predefinidas. Para começar, siga o [guia oficial](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection).

Exemplo: Crie um rótulo personalizado

```powershell
# Conecte-se ao serviço AIP
Connect-AipService

# Crie um rótulo personalizado com opções de proteção
$LabelName = "Sensível - Somente uso interno"
$LabelDescription = "Este rótulo aplica criptografia e uma política de acesso para uso interno."
$LabelProtectionSettings = @{
    "ContentExpirationDate" = (Get-Date).AddMonths(6).ToUniversalTime();
    "OfflineAccessInterval" = "P7D";
    "UserRights" = @("domain\GroupA=View", "domain\GroupB=View,Edit,Print")
}
New-AipServiceLabel -Name $LabelName -Description $LabelDescription -ProtectionSettings $LabelProtectionSettings
```
#### Azure Storage Service Encryption

**Azure Storage Service Encryption (SSE)** criptografa automaticamente os dados em repouso nas contas do Azure Storage, incluindo Blob, File, Table e Queue. O SSE usa chaves gerenciadas pelo Azure ou pelo cliente para criptografar no nível da conta de armazenamento. Para ativá-lo, siga o [guia passo a passo](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) da Microsoft.

Azure Information Protection é um nome de produto antigo. A documentação atual sobre a disponibilidade dos recursos do Sentinel o lista como obsoleto. Consulte a documentação atual do Microsoft Purview Information Protection antes de iniciar uma nova implantação de rótulos.

Exemplo: Ative o SSE em uma conta de armazenamento

```azurecli
# Ative o SSE com chaves gerenciadas pelo Azure
az storage account update --name mystorageaccount --resource-group myresourcegroup --encryption-services blob file
```
#### Azure Disk Encryption

**Azure Disk Encryption** protege discos de máquinas virtuais ao criptografá-los com BitLocker (Windows) ou dm-crypt (Linux). O Azure Key Vault protege as chaves e os segredos de criptografia, mantendo os dados criptografados em repouso. Para ativar o Azure Disk Encryption, siga o [guia oficial](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview) da Microsoft.

Exemplo: Ative o Azure Disk Encryption em uma máquina virtual

```azurecli
# Ative o Azure Disk Encryption em uma VM Windows
az vm encryption enable --resource-group myResourceGroup --name myVM --disk-encryption-keyvault myKeyVault
```
Consulte a documentação oficial sobre [Azure Information Protection](https://docs.microsoft.com/en-us/azure/information-protection/what-is-information-protection), [Azure Storage Service Encryption](https://docs.microsoft.com/en-us/azure/storage/common/storage-service-encryption) e [Azure Disk Encryption](https://learn.microsoft.com/en-us/azure/virtual-machines/disk-encryption-overview).
______

## Detecte e responda a ameaças

O Azure Security Center detecta ameaças potenciais e envia alertas. Ao integrar o serviço ao **Azure Sentinel**, você monitora, investiga e responde a incidentes de segurança em todo o ambiente.

### Detecção de ameaças

O Azure Security Center usa **Azure Defender** para identificar possíveis ameaças. O Azure Defender monitora recursos em busca de sinais de comprometimento e envia alertas e recomendações que ajudam na resposta. Para ativá-lo, siga o [guia oficial](https://docs.microsoft.com/en-us/azure/security-center/defender-for-cloud-enable).

Exemplo: Ative o Azure Defender para uma assinatura

```azurecli
# Ative o Azure Defender para uma assinatura
az security auto-provisioning-setting update --name default --auto-provision on
```
### Resposta a ameaças
Quando detectar uma ameaça, responda com rapidez e eficácia. O Azure Security Center oferece gerenciamento de **Security Incident** para investigar e responder a incidentes. Você também pode integrar o **Azure Sentinel** para criar playbooks automatizados e coordenar a resposta. Consulte a **documentação oficial** sobre a integração do Azure Security Center com o Azure Sentinel.

Exemplo: Crie um playbook do Logic App para o Azure Sentinel
```azurecli
# Crie um grupo de recursos
az group create --name MyResourceGroup --location EastUS

# Crie um Logic App
az logic workflow create --resource-group MyResourceGroup --location EastUS --name MyPlaybook --definition @playbook-definition.json
```
O arquivo `playbook-definition.json` deve conter a definição do playbook do Logic App. Consulte exemplos no [repositório Azure-Sentinel no GitHub](https://github.com/Azure/Azure-Sentinel/tree/master/Playbooks).

Combine a detecção de ameaças do Azure Security Center com o Azure Sentinel para detectar e responder a ameaças no Azure. Consulte a documentação oficial sobre [Azure Defender](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-enhanced-security) e [Azure Sentinel](https://docs.microsoft.com/en-us/azure/sentinel/overview).

O fluxo atual envia alertas do Defender for Cloud ao Microsoft Sentinel pelo [conector do Defender for Cloud](https://learn.microsoft.com/en-us/azure/sentinel/connect-defender-for-cloud). Antes de depender da automação, valide o conector, as regras de coleta de dados, as regras analíticas e o fluxo de incidentes no portal do Defender ou no portal do Azure.
______

## Monitoramento e relatórios

O monitoramento e os relatórios ajudam a manter um ambiente de nuvem seguro. O Azure Security Center oferece recursos como **Painel de Segurança**, **Alertas de Segurança** e **Relatórios de Conformidade**.

### Painel de Segurança

O Painel de Segurança do Azure Security Center mostra uma visão geral da postura de segurança. Ele exibe o Secure Score, recomendações e alertas ativos. Também mostra a situação de conformidade e permite acompanhar o progresso ao longo do tempo.

### Alertas de segurança

O Azure Security Center gera alertas quando detecta ameaças potenciais. Eles apresentam detalhes sobre a ameaça e recomendações para reduzir o risco. Configure notificações por e-mail ou SMS, ou integre o Azure Security Center a serviços como [Slack](https://slack.com/) e [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software).

### Relatórios de conformidade

O Azure Security Center gera relatórios para estruturas regulatórias como GDPR, HIPAA e PCI DSS. Use-os para acompanhar a situação de conformidade da organização e identificar pontos que precisam de melhorias.

______

## Boas práticas para o Azure Security Center

Aplique estas práticas para aproveitar os recursos do Azure Security Center:

1. **Ative o Azure Security Center em todas as assinaturas**: confirme que todas as assinaturas do Azure estão protegidas.
2. **Revise o Secure Score regularmente**: acompanhe a postura geral de segurança e encontre áreas que precisam de melhorias.
3. **Aplique as recomendações de segurança**: melhore a postura e reduza riscos potenciais seguindo as recomendações do Azure Security Center.
4. **Monitore os alertas de segurança**: revise os alertas e responda a eles para reduzir ameaças potenciais.
5. **Mantenha os requisitos de conformidade atualizados**: revise e atualize as políticas para acompanhar as estruturas regulatórias atuais.

## Fluxo atual do Defender for Cloud

Siga esta sequência em uma implantação atual. Os nomes usados nas seções antigas ajudam em pesquisas históricas, mas o portal e a documentação usam a terminologia Defender for Cloud.

1. **Inventarie assinaturas e conectores.** Registre assinaturas do Azure, conectores de AWS ou GCP, projetos de DevOps e recursos essenciais.
2. **Ative os planos Defender necessários.** Escolha planos por carga de trabalho e confirme o licenciamento antes de ativá-los nas assinaturas de produção.
3. **Revise o Cloud Secure Score e as recomendações.** Priorize a exposição à Internet, riscos de identidade, vulnerabilidades exploráveis e falta de registros. A pontuação não prova conformidade total.
4. **Configure controles do Microsoft Entra.** Exija MFA resistente a phishing para contas importantes, use RBAC com privilégio mínimo e revise o acesso privilegiado.
5. **Envie alertas ao Microsoft Sentinel.** Confirme a ingestão de alertas, regras analíticas, responsáveis, automação de resposta e retenção.
6. **Verifique novamente após mudanças.** Revise as recomendações depois de aplicar correções, alterar a arquitetura, adicionar conectores ou mudar planos.

## Lista prática de revisão

- **Identidade:** remova contas antigas, reduza o acesso permanente de administrador e revise exceções do Conditional Access.
- **Rede:** feche portas de gerenciamento públicas, restrinja intervalos de origem dos NSGs e confirme que os registros do firewall e WAF chegam ao espaço de monitoramento.
- **Dados:** classifique os repositórios de dados confidenciais, confirme a criptografia e a propriedade das chaves e teste a restauração de backups.
- **Detecção:** confirme a gravidade dos alertas, o encaminhamento de notificações, os responsáveis por incidentes e os playbooks de resposta.
- **Governança:** atribua um responsável, uma data de expiração de exceções e evidências do padrão exigido a cada iniciativa de política.

______

## Referências

- [Documentação do Azure Security Center](https://docs.microsoft.com/en-us/azure/security-center/)
- [Serviço Azure Policy](https://docs.microsoft.com/en-us/azure/governance/policy/)
- [NIST 800-53](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [CIS](https://www.cisecurity.org/)
- [ISO 27001](https://www.iso.org/isoiec-27001-information-security.html)
- [GDPR](https://gdpr.eu/)
- [HIPAA](https://www.hhs.gov/hipaa/index.html)
- [PCI DSS](https://www.pcisecuritystandards.org/)

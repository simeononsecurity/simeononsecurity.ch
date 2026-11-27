---
title: "Melhores práticas de hardening para Windows 10 e 11"
date: 2023-07-27
lastmod: 2026-11-26
toc: true
draft: false
description: "Conheça estratégias eficazes para aumentar a segurança dos sistemas Windows 10 e Windows 11 com técnicas abrangentes de hardening e boas práticas."
genre: ["Hardening do Windows", "Segurança do Windows", "Hardening do Windows 10", "Hardening do Windows 11", "Boas práticas de segurança do Windows", "Dicas de segurança do Windows", "Diretrizes de segurança do Windows", "Proteção dos sistemas operacionais Windows", "Hardening do sistema Windows", "Medidas de segurança do Windows"]
tags: ["Hardening do Windows", "Segurança do Windows", "Windows 10", "Windows 11", "Segurança do sistema operacional", "Windows Defender", "Controle de Conta de Usuário", "Criptografia BitLocker", "Configuração do firewall", "Políticas do AppLocker", "Atualizações do Windows", "Senhas fortes", "Backup de dados", "Windows Hello", "Secure Boot", "TPM", "Microsoft Defender Antivirus", "Windows Sandbox", "Microsoft Defender Application Guard", "Acesso controlado a pastas", "Boas práticas para proteger Windows 10 e Windows 11", "Como fortalecer os sistemas operacionais Windows", "Medidas de segurança do Windows para pessoas e organizações", "Aumentar a segurança do sistema Windows", "Proteção de dados com criptografia BitLocker", "Isolar sessões do navegador com Microsoft Defender Application Guard", "Dicas e diretrizes de segurança do Windows 10", "Implementação dos recursos de segurança do Windows", "Proteger o Windows com isolamento baseado em hardware", "Garantir a integridade do sistema Windows"]
cover: "/img/cover/A_cartoon_illustration_of_a_shield_protecting-windows.webp"
coverAlt: "Ilustração de desenho animado de um escudo protegendo um logotipo do Windows contra várias ameaças cibernéticas."
coverCaption: "Proteja seu ambiente Windows com técnicas eficazes de hardening."
---

## Introdução

Os sistemas operacionais Windows são amplamente usados por pessoas e organizações em todo o mundo. Para garantir a segurança e a integridade desses sistemas, aplique as **melhores práticas de hardening do Windows**. Hardening é o processo de proteger o sistema operacional ao reduzir sua superfície de ataque e mitigar possíveis vulnerabilidades. Este artigo apresenta as melhores práticas para fortalecer tanto o **Windows 10** quanto o mais recente **Windows 11**, com orientações úteis para aumentar a segurança do seu ambiente Windows.

______

## Entenda o hardening do Windows

**Hardening** do Windows é o processo de fortalecer a segurança de um sistema operacional Windows. Isso envolve configurar várias opções e implementar medidas de segurança contra acessos não autorizados, malware e outras ameaças. Ao fortalecer seu sistema Windows, você reduz os riscos de ataques cibernéticos e protege a confidencialidade, a integridade e a disponibilidade dos dados.

### [Hardening do Windows 10](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

O **Windows** 10 é um dos sistemas operacionais mais usados no mundo. Para fortalecer seu ambiente Windows 10, considere estas práticas:

#### 1. [**Ative o Windows Defender**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

O Windows Defender é uma **solução antivírus robusta** incluída no Windows 10. Ele oferece vários recursos de segurança para proteger o sistema contra diferentes tipos de **malware**, incluindo **vírus, spyware e ransomware**. Ao ativar o Windows Defender, você aumenta bastante a segurança do ambiente Windows 10.

**Siga** estas etapas para ativar o Windows Defender:

- Abra o aplicativo **Segurança do Windows** pelo ícone na barra de tarefas ou pesquise por "Segurança do Windows" no menu Iniciar.
- No aplicativo, clique em **"Proteção contra vírus e ameaças"** no painel de navegação esquerdo.
- Na seção **"Configurações de proteção contra vírus e ameaças"**, clique em **"Gerenciar configurações"**.
- Confira se a opção **"Proteção em tempo real"** está **ativada**. Assim, o Windows Defender fará análises e protegerá o sistema em tempo real.
- Você também pode personalizar as opções de análise e as exclusões usando **"Opções de análise"** e **"Adicionar ou remover exclusões"**.

**Atualize o Windows Defender regularmente** para manter as definições de **malware** e os **aprimoramentos de segurança** em dia. A Microsoft publica atualizações frequentes para lidar com novas ameaças e vulnerabilidades. Para atualizar o Windows Defender:

- **Abra** o aplicativo Segurança do Windows.
- Acesse **"Proteção contra vírus e ameaças"** no painel de navegação esquerdo.
- Na seção **"Atualizações de proteção contra vírus e ameaças"**, clique em **"Verificar se há atualizações"**.
- O **Windows** verificará as atualizações disponíveis e fará o download e a instalação, se necessário.

Ao ativar e manter o Windows Defender atualizado, você protege proativamente seu sistema Windows 10 contra malware e outras ameaças. Também é recomendável executar **análises regulares do sistema** para detectar e remover possíveis ameaças.

O Windows Defender oferece um nível sólido de proteção, mas combine-o com hábitos seguros de navegação, atualizações regulares de software e outras medidas de segurança.

#### 2. [**Mantenha o Windows 10 atualizado**](https://support.microsoft.com/en-us/windows/windows-update-faq-8a903416-6f45-0718-f5c7-375e92dddeb2)

**Instalar** as **atualizações** do Windows regularmente é fundamental para o **hardening do Windows 10**. Elas incluem **correções de segurança**, correções de bugs e melhorias de desempenho que ajudam a **corrigir vulnerabilidades de segurança** e aumentar a estabilidade do sistema.

A Microsoft publica **atualizações regulares** para corrigir novos problemas de segurança e aprimorar a experiência de uso. Ao manter o sistema atualizado, você recebe os **aprimoramentos de segurança** mais recentes para se defender de ameaças emergentes.

Siga estas etapas para manter o Windows 10 atualizado:

1. **Ative as atualizações automáticas**: por padrão, o Windows 10 baixa e instala atualizações automaticamente. Assim, o sistema recebe as atualizações necessárias sem intervenção manual. Para verificar essa opção:
   - Abra **Configurações** pelo menu Iniciar e selecione o ícone de engrenagem.
   - Clique em **Atualização e Segurança**.
   - No painel esquerdo, clique em **Windows Update**.
   - Confira se a opção **"Automático"** está selecionada nas configurações do Windows Update. Se não estiver, clique em **"Alterar horário ativo"** para escolher quando o Windows deve evitar a instalação de atualizações.

2. **Instale as atualizações manualmente**: se preferir controlar o processo, instale as atualizações manualmente:
   - Acesse **Configurações > Atualização e Segurança > Windows Update**.
   - Clique em **"Verificar se há atualizações"** para ver se existem atualizações disponíveis.
   - Se houver, clique em **"Baixar"** e **"Instalar"**.

Reinicie o sistema regularmente depois de instalar atualizações. Algumas precisam de uma reinicialização para aplicar as mudanças por completo.

Ao **manter seu sistema Windows 10 atualizado**, você aumenta a segurança e recebe os recursos mais recentes, melhorias de desempenho e correções de compatibilidade. Essa medida proativa ajuda o sistema a resistir a possíveis ameaças.

#### 3. [**Configure o Controle de Conta de Usuário (UAC)**](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/user-account-control-overview)

O Controle de Conta de Usuário (UAC) é um recurso de segurança do Windows 10 que ajuda a impedir alterações não autorizadas no sistema. Quando necessário, ele solicita aprovação do administrador. O UAC protege contra malware ou usuários não autorizados que tentam fazer mudanças capazes de afetar a segurança ou a estabilidade do sistema.

Configurar o UAC no nível adequado é essencial para o **hardening do Windows 10**. Encontre um equilíbrio entre segurança e facilidade de uso para proteger o sistema sem interrupções desnecessárias.

Siga estas etapas para configurar o UAC no Windows 10:

1. Abra o **Painel de Controle** digitando "Painel de Controle" na barra de pesquisa e selecionando-o nos resultados.
2. No Painel de Controle, clique em **"Contas de Usuário"**.
3. Clique em **"Alterar configurações de Controle de Conta de Usuário"**.
4. Você verá um controle deslizante com diferentes níveis do UAC:
   - **"Sempre notificar"**: o nível mais alto de segurança do UAC. Ele solicita consentimento para qualquer alteração no sistema, mesmo tarefas simples.
   - **"Notificar-me somente quando aplicativos tentarem fazer alterações no meu computador (padrão)"**: é a opção recomendada, pois equilibra segurança e facilidade de uso. Ela solicita consentimento para alterações feitas por aplicativos, mas não para mudanças nas configurações do Windows.
   - **"Notificar-me somente quando aplicativos tentarem fazer alterações no meu computador (não esmaecer minha área de trabalho)"**: é semelhante à opção anterior, mas a área de trabalho não fica esmaecida quando o UAC exibe uma solicitação.
   - **"Nunca notificar"**: o nível mais baixo de segurança do UAC. Ele não solicita confirmação para alterações no sistema.
5. Mova o controle deslizante para o nível de segurança do UAC adequado às suas necessidades.
6. Clique em **"OK"** para salvar as mudanças.

Recomenda-se manter o UAC ativado e escolher um nível que equilibre segurança e facilidade de uso. Desativá-lo por completo deixa o sistema mais vulnerável a alterações não autorizadas e pode comprometer sua segurança.

Ao configurar o UAC, você exige privilégios administrativos para alterações críticas no Windows 10. Isso reduz o risco de acesso não autorizado e infecções por malware.

{{< figure src="windows-10-uac-bitlocker-security-overview.webp" alt="Diagrama dos níveis do Controle de Conta de Usuário do Windows 10 e da criptografia BitLocker protegendo a integridade do sistema e os dados confidenciais" >}}

#### 4. [**Use senhas fortes**](https://simeononsecurity.com/articles/how-to-create-strong-passwords/)

Senhas fortes são essenciais para manter a segurança do sistema Windows 10 e impedir acessos não autorizados. Senhas fracas ou fáceis de adivinhar deixam o sistema vulnerável a ataques de força bruta e quebra de senhas.

Siga estas práticas para garantir que todas as contas de usuário do sistema Windows 10 tenham senhas fortes:

1. **Complexidade**: incentive os usuários a criar senhas complexas e difíceis de adivinhar. Uma senha forte deve combinar letras maiúsculas e minúsculas, números e caracteres especiais. Evite palavras comuns e padrões previsíveis.
2. **Tamanho**: senhas mais longas costumam ser mais seguras. Incentive o uso de pelo menos 8 caracteres, de preferência mais. Quanto maior a senha, mais difícil será quebrá-la.
3. **Exclusividade**: cada conta de usuário deve ter uma senha própria. Reutilizar a mesma senha em várias contas aumenta o risco de uma violação de segurança.
4. **Evite informações pessoais**: não use nomes, datas de nascimento ou endereços. Um invasor pode obter ou adivinhar essas informações com facilidade.
5. **Gerenciadores de senhas**: considere usar um gerenciador para armazenar e administrar senhas com segurança. Ele pode gerar senhas fortes e exclusivas para cada conta e guardá-las em um banco de dados criptografado.
6. **Troque as senhas regularmente**: incentive os usuários a mudar as senhas periodicamente. Defina uma política de expiração e explique a importância de atualizar as senhas.

Boas práticas de senhas aumentam bastante a segurança do sistema Windows 10 e reduzem o risco de acessos não autorizados ou violações de dados. Oriente os usuários regularmente e ofereça recursos, como medidores de força de senha e diretrizes para criar senhas fortes.

Para obter mais informações sobre a criação de senhas fortes e as melhores práticas, consulte este [artigo](https://simeononsecurity.com/articles/how-to-create-strong-passwords/), com orientações abrangentes e dicas para criar senhas seguras e fáceis de lembrar.

Senhas fortes são fundamentais para a segurança do sistema. Priorize-as para proteger dados confidenciais e manter a integridade do ambiente Windows 10.

#### 5. [**Ative a criptografia BitLocker**](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

Uma das maneiras mais eficazes de proteger os dados confidenciais do sistema Windows 10 é ativar a criptografia BitLocker. O BitLocker criptografa o disco inteiro. Assim, mesmo que o dispositivo seja perdido ou roubado, pessoas não autorizadas não terão acesso aos dados.

Siga estas etapas para ativar o BitLocker e proteger suas informações confidenciais:

1. **Verifique os requisitos do sistema**: confirme se sua edição do Windows 10 é compatível com o BitLocker. O recurso está disponível nas edições Pro, Enterprise e Education.
2. **Ative o BitLocker**: abra o Painel de Controle e acesse a categoria **"Sistema e Segurança"**. Clique em **"Criptografia de Unidade de Disco BitLocker"**, selecione as unidades que deseja criptografar e siga as instruções na tela.
3. **Escolha as opções de criptografia**: durante a configuração do BitLocker, você pode escolher entre senha, cartão inteligente ou os dois. Selecione o método adequado aos seus requisitos e preferências de segurança.
4. Faça backup da chave de recuperação: guarde a chave de recuperação em um local seguro, separado do dispositivo. Ela será necessária se você esquecer a senha ou tiver problemas para acessar a unidade criptografada.
5. Gerencie as configurações do BitLocker: depois de ativar o recurso, você pode personalizar outras opções, como desbloqueio automático de unidades específicas ou uso do TPM (Módulo de Plataforma Confiável) para aumentar a segurança. Acesse essas opções na interface de gerenciamento do BitLocker.

O BitLocker adiciona uma camada de proteção ao sistema Windows 10. Mesmo que o dispositivo caia em mãos erradas, os dados permanecem seguros e inacessíveis. Mantenha as configurações do BitLocker atualizadas de acordo com as melhores práticas de segurança.

Para obter mais informações sobre como ativar e gerenciar a criptografia BitLocker, consulte a [documentação oficial da Microsoft](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview), com orientações abrangentes sobre recursos avançados e opções de configuração.

A criptografia BitLocker protege seus dados confidenciais e oferece tranquilidade em caso de perda ou roubo do dispositivo.

#### 6. **Desative serviços e recursos desnecessários**

Para aumentar a segurança do sistema Windows 10, revise e desative serviços e recursos desnecessários. Isso reduz a superfície de ataque e as oportunidades de exploração por agentes maliciosos.

Siga estas etapas para desativar serviços e recursos desnecessários:

1. **Identifique serviços desnecessários**: abra o console de Serviços pressionando **Windows + R**, digitando **services.msc** e pressionando **Enter**. Revise a lista de serviços em execução e pesquise a finalidade de cada um. Determine quais são essenciais para o funcionamento do sistema.
2. **Desative serviços desnecessários**: depois de identificá-los, clique com o botão direito em cada serviço e selecione **"Propriedades"**. Na janela, altere o **"Tipo de inicialização"** para **"Desativado"**. Isso impede que o serviço seja iniciado automaticamente quando o sistema for iniciado. Tenha cuidado e desative somente os serviços que não sejam necessários ao funcionamento normal do sistema.
3. **Desative recursos desnecessários**: além dos serviços, o Windows 10 inclui recursos que talvez você não precise. Abra o **Painel de Controle**, acesse **Programas** ou **Programas e Recursos** e clique em **"Ativar ou desativar recursos do Windows"**. Desmarque os recursos desnecessários. Isso reduz ainda mais a superfície de ataque e o uso de recursos do sistema.
4. **Revise e atualize regularmente**: as necessidades do sistema mudam com o tempo. Revise os serviços e recursos ativados e ajuste a configuração quando necessário.

Ao desativar serviços e recursos desnecessários, você limita possíveis pontos de entrada para invasores e reduz a superfície de ataque geral do Windows 10. Essa prática melhora a postura de segurança e reduz o risco de exploração.

{{< figure src="windows-10-firewall-applocker-attack-surface-reduction.webp" alt="Diagrama mostrando regras do firewall do Windows 10, políticas de controle de aplicativos do AppLocker e redução da superfície de ataque trabalhando em conjunto para bloquear acessos não autorizados" >}}

Para obter mais informações sobre o gerenciamento de serviços e recursos no Windows 10, consulte este [artigo](https://www.tweakhound.com/2015/07/27/windows-10-default-services/#:~:text=Windows%2010%20Default%20Services%20%20%20%20Name,%20%20%20%2044%20more%20rows%20), com orientações detalhadas.

Tenha cuidado ao desativar serviços e recursos, pois a desativação de componentes essenciais pode prejudicar o funcionamento do sistema. Pesquise e entenda a finalidade de cada serviço ou recurso antes de fazer mudanças.

#### 7. **Configure regras do firewall**

O firewall integrado ao Windows 10 é uma importante linha de defesa contra tráfego de rede não autorizado. Ao configurar regras, você controla quais conexões de entrada e de saída são permitidas e aumenta a segurança do sistema.

Siga estas etapas para configurar regras do firewall no Windows 10:

1. **Acesse as configurações do firewall**: abra o **Painel de Controle**, pesquise por **Firewall do Windows Defender** e selecione o resultado. Outra opção é clicar com o botão direito no botão **Iniciar**, selecionar **Configurações** e acessar **Rede e Internet > Firewall do Windows**.
2. **Configure regras de entrada**: elas controlam as conexões de rede recebidas pelo sistema. Na janela do Firewall do Windows Defender, clique em **"Configurações avançadas"**. Na janela que abrir, selecione **"Regras de Entrada"** e clique em **"Nova Regra"**. Siga as instruções para permitir somente as conexões necessárias. Considere quais serviços e aplicativos precisam de acesso à rede e crie regras adequadas.
3. **Configure regras de saída**: elas controlam as conexões de rede iniciadas pelo sistema. Repita as etapas anteriores, mas selecione **"Regras de Saída"**. Crie regras para permitir conexões de saída de serviços e aplicativos essenciais e bloquear conexões suspeitas ou desnecessárias.
4. **Revise e atualize regularmente**: verifique se as regras continuam de acordo com os requisitos do sistema. Mudanças no ambiente de rede e nos padrões de uso podem exigir alterações ou novas regras. Mantenha-as atualizadas para conservar a eficácia do firewall.

A implementação e a manutenção de regras do firewall reduzem bastante o risco de acesso não autorizado à rede e aumentam a segurança do Windows 10. Considere também ativar a opção **"Modo Stealth"** nas configurações do firewall para deixar o sistema menos visível a possíveis invasores.

Para obter instruções detalhadas sobre a configuração de regras do firewall, consulte a [documentação oficial da Microsoft](https://learn.microsoft.com/en-us/windows/security/operating-system-security/network-security/windows-firewall/best-practices-configuring).

Um firewall bem configurado é um componente essencial de uma estratégia de segurança abrangente. Combine-o com outras medidas para proteger o sistema.

#### 8. [**Use o AppLocker**](https://github.com/simeononsecurity/AppLocker)

O [AppLocker](https://simeononsecurity.com/github/applocker-hardening/) é um recurso poderoso do Windows 10 que permite controlar quais aplicativos podem ser executados no sistema. As políticas do AppLocker restringem a execução de aplicativos não autorizados ou potencialmente maliciosos e aumentam a segurança do ambiente Windows 10.

Siga estas etapas para usar o AppLocker:

1. **Acesse as configurações do AppLocker**: abra o **Editor de Política de Grupo Local** pressionando **Windows + R**, digitando **gpedit.msc** e clicando em **"OK"**. Você também pode pesquisar por **Editor de Política de Grupo** no menu **Iniciar**.
2. **Configure as políticas do AppLocker**: no Editor de Política de Grupo Local, acesse **Configuração do Computador > Configurações do Windows > Configurações de Segurança > Políticas de Controle de Aplicativos > AppLocker**. Configure políticas como **Regras de Executáveis**, **Regras do Windows Installer**, **Regras de Script** e **Regras de Aplicativos Empacotados**.
3. **Crie regras do AppLocker**: clique com o botão direito na pasta da política desejada, como **Regras de Executáveis**, e selecione **"Criar Nova Regra"**. Siga as instruções para especificar as condições e exceções. Você pode basear as regras no caminho do arquivo, no editor, no hash do arquivo ou em outros atributos para permitir ou negar a execução de aplicativos.
4. **Teste e refine as políticas**: depois de criar as regras, teste-as em um grupo ou sistema de teste e confirme que somente aplicativos autorizados podem ser executados. Faça os ajustes necessários de acordo com os resultados.
5. **Revise e atualize regularmente**: à medida que os aplicativos usados mudam, revise e atualize as políticas. Novos aplicativos talvez precisem de autorização, enquanto outros podem ficar obsoletos ou apresentar riscos. Mantenha as políticas atualizadas para preservar um controle eficaz de aplicativos.

O AppLocker oferece controle detalhado sobre a execução de aplicativos. Ele ajuda a impedir a execução de software não autorizado ou malicioso e reduz o risco de infecções por malware, instalações de software não autorizadas e outros incidentes de segurança.

Para obter mais informações sobre a implementação de políticas do AppLocker, consulte a [documentação oficial da Microsoft](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker/applocker-overview) ou visite nosso [repositório do AppLocker no GitHub](https://github.com/simeononsecurity/AppLocker), com recursos e exemplos adicionais.

Revise e atualize regularmente as políticas do AppLocker para acompanhar os requisitos dos aplicativos e as novas ameaças. O AppLocker é uma ferramenta valiosa contra software não autorizado e potencialmente prejudicial.

#### 9. [**Faça backup dos dados regularmente**](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/)

Fazer backup dos dados regularmente é essencial para se proteger contra perdas causadas por incidentes de segurança, falhas de hardware e outros eventos inesperados. Ao criar backups regulares e verificar sua integridade, você consegue restaurar dados importantes em caso de desastre.

Siga estas etapas para fazer backup dos dados em um sistema Windows 10:

1. **Identifique os dados críticos**: determine quais dados precisam de backup. Eles podem incluir documentos importantes, arquivos pessoais, configurações do sistema, preferências de aplicativos e outras informações valiosas.
2. **Escolha uma solução de backup**: selecione uma solução confiável que atenda aos seus requisitos. O Windows 10 oferece ferramentas integradas, como **Histórico de Arquivos** e **Backup e Restauração do Windows**. Você também pode escolher um software de terceiros com recursos e flexibilidade adicionais.
3. **Defina a frequência dos backups**: escolha a frequência de acordo com a importância dos dados e a frequência das mudanças. Alguns dados exigem backups diários, enquanto outros podem ser copiados semanal ou mensalmente.
4. **Escolha o armazenamento**: use discos rígidos externos, dispositivos NAS, serviços de armazenamento em nuvem ou uma combinação dessas opções. Confirme se o meio de armazenamento é seguro e confiável.
5. **Configure as opções de backup**: especifique os dados, o destino e outras opções, como criptografia ou compactação.
6. **Teste as restaurações**: faça restaurações de teste regularmente. Assim, você verifica se os backups funcionam e se será possível recuperar os dados quando necessário.
7. **Monitore e atualize**: verifique regularmente se o processo de backup está funcionando como esperado. Atualize a solução e ajuste as opções conforme seus dados e requisitos mudarem.

Com uma rotina regular de backups, você reduz o impacto de perdas de dados e mantém informações importantes disponíveis. Armazene os backups em local seguro, separado dos dados originais. Considere aplicar a **regra de backup 3-2-1**: mantenha pelo menos três cópias dos dados, em dois tipos diferentes de mídia, com uma cópia armazenada fora do local principal.

Para saber mais sobre práticas de backup e sobre a **regra de backup 3-2-1**, consulte o artigo [O que é a regra de backup 3-2-1 e por que você deve usá-la](https://simeononsecurity.com/articles/what-is-the-3-2-1-backup-rule-and-why-you-should-use-it/). Ele apresenta orientações úteis para uma estratégia de backup eficaz.

Backups regulares protegem seus dados e garantem sua disponibilidade diante de eventos imprevistos. Inclua o backup de dados nas medidas de hardening do Windows 10 para proteger suas informações valiosas.

______

### [Hardening do Windows 11](https://github.com/simeononsecurity/Windows-Optimize-Harden-Debloat)

O Windows 11 é a versão mais recente do sistema operacional Windows e oferece recursos aprimorados e mais segurança. Para fortalecer seu ambiente Windows 11, considere estas práticas:

#### 1. **Secure Boot e TPM**

Secure Boot e TPM (Módulo de Plataforma Confiável) são recursos essenciais de segurança disponíveis no Windows 11. Eles ajudam a impedir acessos não autorizados e garantir a integridade do sistema operacional. Ativar Secure Boot e TPM aumenta a segurança do sistema Windows 11.

Siga estas etapas para ativar Secure Boot e TPM no seu dispositivo Windows 11:

1. **Verifique a compatibilidade**: antes de ativar Secure Boot e TPM, confirme se o dispositivo oferece suporte a esses recursos. Verifique se o hardware e o firmware atendem aos requisitos.
2. **Acesse as configurações UEFI/BIOS**: reinicie o dispositivo Windows 11 e acesse as configurações UEFI (Interface de Firmware Extensível Unificada) ou BIOS (Sistema Básico de Entrada/Saída). A tecla ou combinação de teclas varia conforme o dispositivo. Teclas comuns incluem Del, F2, F10 e Esc. Consulte a documentação do dispositivo ou o site do fabricante para obter instruções específicas.
3. **Ative o Secure Boot**: nas configurações UEFI/BIOS, localize as opções do Secure Boot e ative o recurso. Assim, somente sistemas operacionais e componentes confiáveis serão executados durante a inicialização. Isso impede o carregamento de software não autorizado ou malicioso que possa comprometer a segurança.
4. **Ative o TPM**: localize as opções do TPM nas configurações UEFI/BIOS e ative-o. O TPM é um chip dedicado na placa-mãe que oferece recursos de segurança baseados em hardware. Com o TPM ativado, o Windows 11 aproveita seus recursos para aumentar a segurança do sistema.
5. **Configure a segurança do TPM**: depois de ativar o TPM, talvez você encontre opções adicionais, como definir uma senha, ativar atualizações do firmware do TPM ou ajustar outras configurações. Revise as opções disponíveis e configure-as conforme seus requisitos de segurança.
6. **Salve e saia**: salve as mudanças nas configurações UEFI/BIOS e saia. O sistema será reiniciado e aplicará as novas opções.

Ao ativar Secure Boot e TPM no Windows 11, você melhora a postura de segurança e fortalece a proteção do sistema operacional e dos dados confidenciais.

#### 2. [**Ative o Microsoft Defender Antivirus**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

O **Windows** 11 inclui uma proteção antivírus integrada chamada **Microsoft Defender Antivirus**. Ela oferece proteção abrangente contra vários tipos de **malware**, incluindo vírus, ransomware e spyware. Ao **ativar** e **atualizar regularmente** o Microsoft Defender Antivirus, você garante **detecção e prevenção de ameaças em tempo real**.

Siga estas etapas para ativar e atualizar o Microsoft Defender Antivirus no Windows 11:

1. **Verifique o status do antivírus**: abra o aplicativo **Segurança do Windows** pelo menu Iniciar, pesquise "Segurança do Windows" e selecione o aplicativo nos resultados. Acesse a seção **"Proteção contra vírus e ameaças"** e confira o status do Microsoft Defender Antivirus. Em uma nova instalação do Windows 11, o recurso deve estar ativado por padrão.
2. **Ative a proteção em tempo real**: no aplicativo Segurança do Windows, confira se a proteção em tempo real do Microsoft Defender Antivirus está ativada. Ela monitora o sistema continuamente em busca de malware e outras atividades maliciosas, com **resposta imediata** e **bloqueio de ameaças em tempo real**. Se estiver desativada, clique no **botão de alternância** para ativá-la.
3. **Atualize as definições**: atualize regularmente as **definições de vírus** para que o Microsoft Defender Antivirus identifique as ameaças mais recentes. Na seção **"Proteção contra vírus e ameaças"** do aplicativo Segurança do Windows, clique em **"Verificar se há atualizações"**. Isso garante que o sistema tenha as **assinaturas** e os **recursos de detecção** mais recentes.
4. **Agende análises**: o Microsoft Defender Antivirus permite agendar **análises regulares do sistema** para detectar e remover ameaças potenciais. Na seção **"Proteção contra vírus e ameaças"**, clique em **"Verificação rápida"** ou **"Verificação completa"**. Você também pode usar o link **"Opções de análise"** para personalizar as opções e agendar verificações regulares.
5. **Configure outras opções**: o Microsoft Defender Antivirus oferece outras configurações e recursos. No aplicativo Segurança do Windows, explore seções como **"Controle de aplicativos e navegador"**, **"Segurança do dispositivo"** e **"Firewall e proteção de rede"** para personalizar o antivírus e usar recursos avançados de proteção.

Ativar e atualizar regularmente o Microsoft Defender Antivirus no Windows 11 é essencial para manter uma defesa forte contra malware e outras ameaças. Siga estas etapas e mantenha o antivírus atualizado para proteger seu sistema Windows 11.

Embora o Microsoft Defender Antivirus ofereça proteção robusta, adote **hábitos seguros de navegação**, tenha cuidado ao **baixar arquivos** ou **abrir anexos de email** e mantenha o **sistema operacional e os aplicativos atualizados** para aumentar ainda mais a postura de segurança.

{{< figure src="windows-11-secure-boot-tpm-defender-security-stack.webp" alt="Diagrama mostrando a pilha de segurança do Windows 11, incluindo Secure Boot, proteção de hardware TPM, Microsoft Defender Antivirus e camadas de segurança baseada em virtualização" >}}

#### 3. **Aplique o isolamento padrão baseado em hardware**

O Windows 11 usa recursos de isolamento baseados em hardware, como **Virtualization-based Security (VBS)** e **Hypervisor-protected Code Integrity (HVCI)**, para aumentar a segurança e proteger componentes críticos do sistema.

Ao ativar e aplicar esses recursos padrão de isolamento por hardware, você estabelece limites de segurança robustos e reduz várias formas de ataque. Siga estas etapas para configurar os recursos corretamente:

1. **Ative a tecnologia de virtualização**: confirme se o sistema oferece suporte à virtualização e se o recurso está ativado nas configurações do **BIOS** ou do firmware **UEFI**. As etapas variam conforme o fabricante da placa-mãe ou do firmware. Consulte a documentação do sistema ou o site do fabricante para obter instruções específicas.
2. **Ative a Virtualization-based Security (VBS)**: o Windows 11 inclui VBS, que usa os recursos de virtualização do hardware para criar contêineres isolados chamados **Virtual Secure Mode (VSM)**. O VSM oferece um ambiente de execução seguro para componentes críticos, protegendo-os contra possíveis ataques. Para ativar a VBS:
   - Pressione **Windows + R** para abrir a caixa de diálogo Executar.
   - Digite **gpedit.msc** e pressione **Enter** para abrir o Editor de Política de Grupo Local.
   - Acesse **Configuração do Computador -> Modelos Administrativos -> Sistema -> Device Guard**.
   - Clique duas vezes na política **"Ativar Segurança Baseada em Virtualização"**.
   - Selecione **"Habilitado"** e clique em **OK** para aplicar as mudanças.

   A VBS pode exigir hardware compatível e requisitos específicos do sistema. Consulte a **documentação oficial da Microsoft** para obter mais informações.
3. **Ative a Hypervisor-protected Code Integrity (HVCI)**: a HVCI usa o hipervisor para impor políticas de integridade de código. Ela impede a execução de código não autorizado e aumenta a postura geral de segurança. Para ativar a HVCI:
   - Pressione **Windows + R** para abrir a caixa de diálogo Executar.
   - Digite **msconfig** e pressione **Enter** para abrir o utilitário de Configuração do Sistema.
   - Acesse a guia **"Inicialização"**.
   - Clique em **"Opções avançadas"**.
   - Marque a opção **"Ativar Hypervisor-protected Code Integrity"**.
   - Clique em **OK** para salvar as mudanças e reinicie o sistema.

   A HVCI exige hardware compatível e outros requisitos do sistema. Consulte a **documentação oficial da Microsoft** para obter mais detalhes.

Ao aplicar recursos padrão de isolamento baseado em hardware, como VBS e HVCI, você aumenta bastante a segurança do sistema Windows 11. Eles ajudam a proteger componentes críticos contra ataques que tentam modificar ou explorar o código e as configurações do sistema.

Atualize o sistema regularmente com os patches de segurança e as atualizações de firmware mais recentes para aproveitar os aprimoramentos e as mitigações oferecidos por esses recursos de isolamento baseado em hardware.

A disponibilidade e os requisitos desses recursos variam conforme a configuração do sistema e a edição do Windows 11. Consulte a **documentação oficial da Microsoft** e verifique a compatibilidade para implementar os recursos corretamente.

#### 4. [**Use o Windows Sandbox**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview)

O **Windows Sandbox** permite executar aplicativos não confiáveis ou testar software em um ambiente isolado, adicionando uma camada de segurança ao sistema e reduzindo os riscos de executar programas não confiáveis.

O Windows Sandbox cria um ambiente de área de trabalho temporário e leve, separado do sistema operacional principal. Todas as alterações feitas no Sandbox são descartadas quando você fecha o ambiente, sem afetar o sistema principal.

Siga estas etapas para usar o Windows Sandbox:

1. **Verifique os requisitos do sistema**: confirme se o sistema atende aos requisitos para executar o Windows Sandbox. Em geral, você precisa de uma edição Windows 10 Pro ou Enterprise e de um processador com recursos de virtualização ativados no firmware BIOS/UEFI. Consulte a [**documentação oficial da Microsoft**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview) para verificar os requisitos específicos.
2. **Ative o Windows Sandbox**: esse recurso está integrado às edições Windows 10 Pro e Enterprise. Para ativá-lo:
   - Pressione **Windows + R** para abrir a caixa de diálogo Executar.
   - Digite **appwiz.cpl** e pressione **Enter** para abrir a janela Programas e Recursos.
   - Clique em **"Ativar ou desativar recursos do Windows"**, no lado esquerdo.
   - Localize **"Windows Sandbox"** na lista de recursos.
   - Marque a caixa ao lado de **"Windows Sandbox"** e clique em **OK**.
   - O Windows instalará os componentes necessários. Talvez seja preciso reiniciar o sistema para aplicar as mudanças.
3. **Inicie o Windows Sandbox**: depois de ativar o recurso, abra o menu **Iniciar**, pesquise por **"Windows Sandbox"** e selecione o aplicativo. O Sandbox será aberto em outra janela para executar aplicativos não confiáveis ou testar software em um ambiente seguro.
   - Abra o menu Iniciar e pesquise por Windows Sandbox.
   - Selecione o aplicativo Windows Sandbox para abri-lo.
   - O Sandbox será aberto em outra janela e fornecerá um ambiente seguro.

Os aplicativos executados no Windows Sandbox ficam isolados, e as mudanças feitas nele são descartadas quando você fecha o ambiente. Salve arquivos e dados fora do Sandbox se precisar mantê-los.

O Windows Sandbox é eficaz para testar software desconhecido, abrir arquivos suspeitos e visitar sites potencialmente arriscados. Ele adiciona proteção ao confinar atividades maliciosas ou alterações indesejadas no ambiente isolado, sem afetar o sistema operacional principal.

Ao incluir o Windows Sandbox nas suas práticas de segurança, você reduz bastante os riscos de executar aplicativos não confiáveis e protege o sistema contra ameaças potenciais.

{{< figure src="windows-sandbox-application-guard-isolation-architecture.webp" alt="Diagrama que ilustra como o Windows Sandbox e o Microsoft Defender Application Guard criam contêineres virtuais isolados para proteger o sistema operacional host contra aplicativos não confiáveis e sessões de navegador" >}}

Para obter mais informações sobre o Windows Sandbox e seu uso, consulte a [**documentação oficial da Microsoft**](https://learn.microsoft.com/en-us/windows/security/application-security/application-isolation/windows-sandbox/windows-sandbox-overview).

#### 5. [**Implemente o Microsoft Defender Application Guard**](https://github.com/simeononsecurity/Windows-Defender-Application-Guard-Hardening)

O Microsoft Defender Application Guard é um recurso de segurança que isola as sessões do navegador Microsoft Edge do sistema operacional subjacente. Ao executar o Edge em um ambiente seguro e isolado, o Application Guard ajuda a proteger o sistema contra ataques pelo navegador e sites maliciosos.

Siga estas etapas para implementar o Microsoft Defender Application Guard e aumentar a segurança do navegador:

1. **Verifique a compatibilidade**: antes de continuar, confirme se o sistema atende aos requisitos para executar o Microsoft Defender Application Guard. Em geral, você precisa de uma edição Windows 10 Pro ou Enterprise, um processador compatível com virtualização e pelo menos 8 GB de RAM. Consulte a [**documentação oficial da Microsoft**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard) para verificar os requisitos específicos.
2. **Ative o Application Guard**: o Application Guard está disponível como recurso opcional no Windows 10. Para ativá-lo:
   - Pressione **Windows + R** para abrir a caixa de diálogo Executar.
   - Digite **appwiz.cpl** e pressione **Enter** para abrir a janela Programas e Recursos.
   - Clique em **"Ativar ou desativar recursos do Windows"**, no lado esquerdo.
   - Localize **"Microsoft Defender Application Guard"** na lista de recursos.
   - Marque a caixa ao lado de **"Microsoft Defender Application Guard"** e clique em **OK**.
   - O Windows instalará os componentes necessários. Talvez seja preciso reiniciar o sistema para aplicar as mudanças.
3. **Configure o Application Guard**: depois de ativá-lo, ajuste as configurações conforme suas necessidades de segurança. O Application Guard permite definir o nível de isolamento e controlar como ele trata sites e arquivos não confiáveis. Você pode ajustar essas opções no aplicativo **Segurança do Windows** ou nas configurações de Política de Grupo.
4. **Teste e verifique**: depois de ativar e configurar o Microsoft Defender Application Guard, teste seu funcionamento. Abra o Microsoft Edge e visite um site malicioso conhecido ou com possíveis riscos. Verifique se o Application Guard isola a sessão do navegador e impede ataques.

O Microsoft Defender Application Guard adiciona uma camada de proteção ao isolar as sessões do navegador e conter ameaças potenciais em um ambiente seguro. Isso protege o sistema e os dados contra ataques pelo navegador, como downloads automáticos, scripts maliciosos e explorações de dia zero.

Para obter mais informações sobre a configuração e o uso do Microsoft Defender Application Guard, consulte a [**documentação oficial da Microsoft**](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-security-windows-defender-application-guard).

#### 6. [**Ative o Controlled Folder Access (acesso controlado a pastas)**](https://github.com/simeononsecurity/Windows-Defender-Hardening)

O **Controlled** Folder Access é um recurso de segurança do Windows 11 que ajuda a proteger pastas importantes contra alterações não autorizadas causadas por ransomware e outros softwares maliciosos. Ao ativá-lo e adicionar as pastas necessárias à lista de proteção, você aumenta a segurança do sistema e evita possíveis perdas de dados.

Siga estas etapas para ativar o Controlled Folder Access (acesso controlado a pastas) e proteger pastas importantes:

1. **Abra a Segurança do Windows**: pressione a **tecla Windows**, digite **"Segurança do Windows"** e selecione o aplicativo nos resultados da pesquisa.
2. **Acesse as configurações de proteção contra vírus e ameaças**: no aplicativo Segurança do Windows, clique na guia **"Proteção contra vírus e ameaças"** no menu esquerdo.
3. **Configure o Controlled Folder Access (acesso controlado a pastas)**: na seção **"Proteção contra ransomware"**, clique em **"Gerenciar proteção contra ransomware"** para acessar as configurações do Controlled Folder Access (acesso controlado a pastas).
4. **Ative o Controlled Folder Access (acesso controlado a pastas)**: coloque o botão de alternância na posição **"Ativado"**. O Windows exibirá um aviso informando que somente aplicativos confiáveis terão acesso às pastas protegidas.
5. **Adicione pastas protegidas**: clique em **"Pastas protegidas"** e depois em **"Adicionar uma pasta protegida"**. Selecione as pastas e clique em **"OK"**.
   - Recomenda-se adicionar pastas importantes, como Documentos, Imagens, Vídeos e outros diretórios que contenham dados valiosos.
6. **Permita ou bloqueie aplicativos**: por padrão, o Controlled Folder Access (acesso controlado a pastas) permite que aplicativos confiáveis acessem as pastas protegidas. Você pode alterar esse comportamento clicando em **"Permitir um aplicativo pelo acesso controlado a pastas"**. Depois, permita ou bloqueie aplicativos específicos.
7. **Monitore e revise**: depois de ativar o recurso, o Windows monitorará e registrará tentativas de aplicativos não autorizados de acessar as pastas protegidas. Para revisar os registros, clique em **"Revisar"** na seção **"Aplicativos bloqueados recentemente"** das configurações do Controlled Folder Access (acesso controlado a pastas).

O Controlled Folder Access (acesso controlado a pastas) adiciona uma camada de proteção às pastas importantes, reduz alterações não autorizadas e evita perdas de dados causadas por ransomware. Revise as configurações regularmente para confirmar se as pastas protegidas atendem aos seus requisitos de segurança.

Para obter mais informações sobre a configuração e o uso do Controlled Folder Access (acesso controlado a pastas), consulte a [**documentação oficial da Microsoft**](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/controlled-folders?view=o365-worldwide).

#### 7. **Ative a Manutenção Automática do Windows**

O Windows 11 inclui um recurso chamado Manutenção Automática que ajuda a otimizar e proteger o sistema por meio de tarefas regulares de manutenção. Ao ativá-lo, você ajuda a manter o sistema funcionando bem e com segurança.

Siga estas etapas para ativar a Manutenção Automática do Windows:

1. **Abra as Configurações do Windows**: pressione a **tecla Windows**, digite **"Configurações"** e selecione o aplicativo nos resultados.
2. **Acesse as configurações de manutenção**: no aplicativo Configurações, clique na categoria **"Sistema"** e selecione **"Sobre"** no menu esquerdo. Role até o fim da página e clique no link **"Informações do sistema"**.
3. **Abra as configurações de manutenção**: na janela Informações do Sistema, clique no link **"Manutenção"** na parte inferior da página.
4. **Ative a Manutenção Automática**: nas configurações de manutenção, coloque o botão de alternância ao lado de **"Manutenção Automática"** na posição **"Ativado"**.
5. **Configure as opções de manutenção**: por padrão, o Windows agenda tarefas para todos os dias às 2h. Se preferir outro horário, clique em **"Alterar configurações de manutenção"** e ajuste opções como o horário de início e a frequência das tarefas.
6. **Revise outras configurações**: abaixo do botão da Manutenção Automática, há opções como **"Permitir que a manutenção agendada desperte meu computador no horário agendado"** e **"Permitir que a manutenção agendada seja executada mesmo quando meu computador estiver usando energia da bateria"**. Ajuste-as conforme suas preferências e requisitos.
7. **Monitore as tarefas de manutenção**: depois de ativar o recurso, o Windows executará as tarefas em segundo plano no horário agendado. Você pode monitorar as atividades na seção **"Manutenção"** do aplicativo **Segurança do Windows** ou revisar os registros de manutenção no Visualizador de Eventos.

A Manutenção Automática ajuda a otimizar e proteger o sistema ao executar tarefas essenciais regularmente, como atualizações de software, otimização de disco e análises de segurança. Manter o sistema em bom estado oferece uma experiência mais estável e segura.

Para obter mais informações sobre a Manutenção Automática do Windows e as opções de configuração, consulte a [**documentação oficial da Microsoft**](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-maintenence).

______

## Ordem recomendada de hardening

Aplique os controles em uma ordem que proteja primeiro o acesso e a recuperação:

1. Confirme a edição e a compilação do Windows, o status de suporte, os recursos de segurança do hardware e as opções de recuperação.
2. Instale as atualizações de segurança atuais e reinicie durante uma janela planejada.
3. Crie um backup testado e registre o estado atual do firewall, do Defender, do BitLocker, dos serviços e das políticas locais.
4. Mantenha o UAC ativado, use contas de administrador separadas e exija MFA para acesso remoto e na nuvem quando houver suporte.
5. Ative as proteções do Defender, os perfis do firewall, Secure Boot, BitLocker e isolamento de hardware quando a edição e o hardware oferecerem suporte.
6. Teste as regras ASR, o Controlled Folder Access (acesso controlado a pastas), o AppLocker e as mudanças nos serviços em modo de auditoria ou em um grupo piloto antes de bloquear ou desativar qualquer recurso de forma ampla.
7. Centralize os registros e revise falhas de logon, mudanças de política, eventos do Defender e bloqueios do firewall.
8. Reinicie, teste os aplicativos necessários, verifique o acesso de recuperação e documente o estado final.

O [Security Compliance Toolkit da Microsoft](https://learn.microsoft.com/windows/security/operating-system-security/device-management/windows-security-configuration-framework/security-compliance-toolkit-10) fornece linhas de base versionadas para Windows 10, Windows 11 e Windows Server. Use a linha de base correspondente como ponto de partida revisado. A Microsoft alerta que mudanças nas linhas de base precisam ser testadas antes da implantação em produção.

## Limite de suporte do Windows 10

A Microsoft encerrou o suporte à versão 22H2 do Windows 10 em 14 de outubro de 2025. Depois dessa data, uma instalação reforçada do Windows 10 não recebe atualizações de segurança pelo caminho normal, a menos que se aplique um acordo de ciclo de vida separado ou um programa de Atualizações de Segurança Estendidas. Inclua a migração, a substituição ou uma exceção aprovada no plano de segurança. O hardening não estende o ciclo de vida do produto. Consulte o [aviso de fim do suporte do Windows 10 da Microsoft](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).

## Reversão de mudanças em serviços e recursos

Desativar um serviço exige testes de dependências e cargas de trabalho. Não desative **RPC**, **Windows Update**, **Windows Event Log** ou outro serviço porque uma lista genérica o classifica como desnecessário. O nome do serviço, sozinho, não descreve sua função no seu sistema.

Antes de fazer uma mudança, exporte a configuração do serviço e registre os serviços dependentes:

```powershell
$name = 'Spooler'
Get-CimInstance Win32_Service -Filter "Name='$name'" |
    Select-Object Name, DisplayName, State, StartMode, StartName, PathName |
    Export-Csv "C:\Temp\$name-before.csv" -NoTypeInformation
Get-Service -Name $name -DependentServices
Get-Service -Name $name -RequiredServices
```

Altere um serviço por vez. Use **Manual** antes de **Desativado** quando uma carga de trabalho iniciar o serviço sob demanda. Registre o tipo de inicialização anterior. Depois dos testes, verifique o comportamento dos aplicativos, o Visualizador de Eventos, o Windows Update, a impressão, o gerenciamento remoto, o acesso VPN e as tarefas agendadas.

Para reverter, restaure o tipo de inicialização registrado e inicie o serviço somente depois de confirmar suas dependências:

```powershell
Set-Service -Name $name -StartupType Manual
Start-Service -Name $name
Get-Service -Name $name
```

Para reverter uma mudança de política mais ampla, restaure o backup salvo da GPO ou do Registro usando a mesma ferramenta usada para criá-lo. Antes de mudanças remotas, mantenha um caminho de recuperação offline e as credenciais de um administrador local. A Microsoft documenta a sintaxe de configuração de serviços em [`sc.exe config`](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-config).

## Registro de validação dos controles

Para cada mudança de hardening, registre o controle, o escopo, o valor anterior e o novo, o resultado do teste, os IDs de eventos revisados, o responsável e o comando de reversão. Um aplicativo bloqueado ou uma impressora que não funciona é um achado operacional, não uma prova de que o controle está errado. Revise as evidências e ajuste o escopo, as exclusões ou o grupo de implantação.

______

## Conclusão

**Aplicar** estas **melhores práticas de hardening do Windows** é essencial para proteger seus sistemas Windows. Ao **atualizar o sistema operacional** regularmente, você corrige vulnerabilidades de segurança e melhora a estabilidade. Ativar recursos como **antivírus** e **criptografia** adiciona proteção aos dados. Configurar **controles de acesso** adequados ajuda a impedir mudanças não autorizadas e restringe o acesso a recursos confidenciais.

Estas práticas aumentam a segurança do seu **ambiente Windows**, protegem os dados e mantêm a integridade da **infraestrutura digital**. Mantenha-se informado e revise suas medidas de segurança regularmente para se antecipar a possíveis ameaças.

O **hardening do Windows** é um processo contínuo. Acompanhe as atualizações e práticas de segurança mais recentes. Ao manter uma postura proativa e aplicar estas práticas, você reduz os riscos de segurança e protege os sistemas Windows.

Para obter mais informações sobre hardening do Windows e boas práticas, consulte fontes confiáveis, como a **documentação da Microsoft**, **fóruns de segurança** e **sites de cibersegurança confiáveis**.

______

## Referências:

- [Segurança do Microsoft Windows](https://www.microsoft.com/en-us/security)
- [Publicação Especial 800-171 do NIST: Proteção de Informações Controladas Não Classificadas em Sistemas e Organizações Não Federais](https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final)
- [Benchmark CIS para Microsoft Windows 10](https://www.cisecurity.org/benchmark/microsoft_windows_10/)
- [Benchmark CIS para Microsoft Windows 11](https://www.cisecurity.org/benchmark/microsoft_windows_11/)

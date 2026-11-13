---
title: "Thunderbird 153.6: Exposição de credenciais NTLM no Windows e como atualizar (2026)"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "Duas falhas graves do Thunderbird podem expor dados de autenticação NTLM do Windows quando uma mensagem manipulada é exibida. Entenda os dois caminhos, confira a versão e limite o SMB de saída durante a atualização."
genre: ["Cibersegurança", "Segurança de e-mail", "Segurança do Windows"]
tags: ["Thunderbird 153.6", "Thunderbird 153.6.0esr", "atualização de segurança do Thunderbird", "vulnerabilidade do Thunderbird no Windows", "exposição NTLM pelo Thunderbird", "autenticação SMB do Thunderbird", "CVE-2026-118174", "CVE-2026-118176", "MFSA 2026-122", "anexo de chave OpenPGP", "anexo externo", "bloqueio de conteúdo remoto", "URL mailbox", "caminho UNC de comprimento estendido", "nome da conta do Windows", "dados de autenticação NTLM", "exposição de credenciais SMB", "SMB de saída", "porta TCP 445", "segurança de e-mail", "cliente de e-mail do Windows", "verificar versão do Thunderbird", "atualizar Thunderbird", "relay NTLM", "quebra de senha offline"]
cover: ""
coverAlt: ""
coverCaption: ""
---

A Mozilla corrigiu duas **falhas graves que expunham credenciais do Windows** no Thunderbird 153.6. A simples exibição de uma mensagem maliciosa podia disparar uma das solicitações de rede descritas na [MFSA 2026-122](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/). O comunicado descreve uma possível exposição de dados NTLM, não uma invasão confirmada das credenciais de todos os destinatários.

<!--more-->

## Principais pontos

- **CVE-2026-118174** envolvia um anexo de chave OpenPGP hospedado externamente. Exibir a mensagem iniciava uma solicitação sem interação do usuário, mesmo com o conteúdo remoto bloqueado.
- **CVE-2026-118176** envolvia uma URL `mailbox:` especialmente criada com um caminho UNC de comprimento estendido. Exibir a mensagem iniciava uma conexão SMB com um servidor escolhido pelo remetente.
- **Atualize o Thunderbird no Windows** e confirme a versão instalada. O comunicado identifica o Thunderbird 153.6 como corrigido. As notas de versão do Thunderbird indicam a compilação correspondente 153.6.0esr.

## O que a mensagem aciona

**As duas falhas têm pontos de entrada diferentes.** Segundo as descrições da Mozilla, o destinatário não precisa clicar em um link da mensagem em nenhum dos casos. O risco para as credenciais do Windows depende de uma solicitação de rede alcançar um compartilhamento controlado pelo invasor e de ocorrer a troca de autenticação subsequente. A Mozilla não relata exploração ativa no comunicado.

| Problema | Ação acionada ao exibir a mensagem | Risco para credenciais do Windows |
| --- | --- | --- |
| **CVE-2026-118174** | O Thunderbird carrega o conteúdo de um anexo de chave OpenPGP para oferecer a importação da chave. O remetente o marca como anexo externo com uma URL escolhida pelo invasor. | Uma URL para um compartilhamento de rede expõe os dados NTLM do usuário se a solicitação alcançar esse compartilhamento. |
| **CVE-2026-118176** | Um caminho UNC de comprimento estendido contorna a restrição do Thunderbird a compartilhamentos remotos em URLs `mailbox:`. | O Thunderbird se conecta a um servidor SMB escolhido pelo invasor e divulga o nome da conta do Windows e os dados de autenticação NTLM. |

No caminho do **anexo OpenPGP**, a Mozilla afirma explicitamente que a solicitação contornava o bloqueio de conteúdo remoto e não exigia interação do usuário. Em sistemas que não são Windows, o problema também permitia uma solicitação remota contra a configuração de conteúdo remoto, mas a Mozilla limita a exposição de credenciais NTLM ao Windows. Para o caminho da **URL `mailbox:`**, a Mozilla informa que outros sistemas operacionais não são afetados. Consulte as entradas de [CVE-2026-118174](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118174) e [CVE-2026-118176](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/#CVE-2026-118176).

**Dados de autenticação NTLM não são uma senha em texto simples.** Segundo a Mozilla, os dados divulgados pelo caminho SMB criam risco de quebra de senha offline ou ataques de relay. Receber uma mensagem manipulada não comprova que um ataque teve sucesso. O comunicado também lista outras falhas do Thunderbird, incluindo caminhos separados para calendário e RSS. Este guia trata dos dois caminhos acionados pela exibição de e-mail, sem equiparar todos os problemas da versão.

## Confira e atualize o Thunderbird

O fluxo afetado é **ler e-mails no Thunderbird no Windows** antes de instalar a correção correspondente. A Mozilla aponta o **Thunderbird 153.6** como corrigido, mas não especifica um intervalo completo das versões mais antigas afetadas por esses dois problemas. As [notas de versão do 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/) identificam uma compilação ESR lançada em 27 de outubro de 2026. Não deduza o estado da correção de outro canal, fork ou pacote apenas pelo rótulo da versão.

1. No Windows, abra **Help > About Thunderbird**. Confira a versão exibida na janela About, que também verifica atualizações. As [instruções de atualização da Mozilla](https://support.mozilla.org/en-US/kb/updating-thunderbird) descrevem esse caminho.
2. Se houver uma atualização, deixe o Thunderbird baixá-la e selecione **Restart Thunderbird to Update**. Depois da reinicialização, abra novamente **Help > About Thunderbird** e confirme a versão instalada.
3. Para a **linha 153 ESR**, compare a versão resultante com **153.6.0esr** nas notas de versão do Thunderbird. Se sua organização gerencia as atualizações, peça ao administrador que confirme a correção do fornecedor em vez de presumir que ela já foi instalada.

> **Observação sobre a versão:** As notas de versão do 153.6.0esr confirmam que essa versão foi lançada. A MFSA 2026-122 associa as correções de segurança ao Thunderbird 153.6. As notas não descrevem individualmente essas duas CVEs. Consulte o comunicado para ver os detalhes das falhas.

## Reduza a exposição durante a atualização

**Instale primeiro a correção do fornecedor.** Desativar o conteúdo remoto, por si só, não impede a CVE-2026-118174, pois a solicitação descrita contornava essa configuração. A recomendação "não clique" não basta. A Mozilla descreve solicitações acionadas pela exibição da mensagem.

Como **defesa em profundidade**, restrinja o SMB de saída dos clientes Windows para a internet, incluindo a **porta TCP 445**, no firewall corporativo ou nos dispositivos gerenciados. As [orientações da Microsoft sobre tráfego SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) recomendam bloquear o TCP 445 de saída para a internet e limitar o acesso aos servidores de arquivos necessários. Faça o inventário dos compartilhamentos necessários antes de aplicar uma regra, sobretudo se o ambiente usa um serviço de arquivos em nuvem ou inclui trabalhadores remotos fora do perímetro. Esse controle de rede limita o caminho SMB descrito, mas não corrige o Thunderbird nem resolve todos os problemas de solicitação remota do comunicado.

Se um computador Windows com uma versão antiga do Thunderbird exibiu uma mensagem suspeita, **trate a exposição como uma questão a investigar, não como prova de comprometimento**. Revise, com a equipe de segurança, os registros disponíveis de conexões SMB de saída e de autenticação. O comunicado do fornecedor não oferece um teste de exposição nem uma instrução geral para trocar todas as senhas.

## Fontes

- [Mozilla Foundation Security Advisory 2026-122: vulnerabilidades corrigidas no Thunderbird 153.6](https://www.mozilla.org/en-US/security/advisories/mfsa2026-122/)
- [Notas de versão do Thunderbird Desktop: 153.6.0esr](https://www.thunderbird.net/en-US/thunderbird/153.6.0esr/releasenotes/)
- [Mozilla Support: atualizar o Thunderbird para a versão mais recente](https://support.mozilla.org/en-US/kb/updating-thunderbird)
- [Microsoft Learn: proteger o tráfego SMB no Windows Server](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)

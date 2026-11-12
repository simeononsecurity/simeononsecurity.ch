---
title: "Por que a filtragem de DNS é contornada: verifique o caminho do resolvedor"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Descubra por que um dispositivo ou navegador ignora seu filtro DNS. Compare consultas diretas e padrão, examine os registros e confira DNS criptografado, VPN, IPv6 e configurações do roteador."
genre: ["Redes domésticas", "DNS", "Privacidade"]
tags: ["contorno da filtragem DNS", "contornar Pi-hole", "registro de consultas DNS", "DNS seguro do navegador", "DNS over HTTPS", "Android Private DNS", "iCloud Private Relay", "DNS da VPN", "DNS IPv6", "DHCP DNS do roteador", "Resolve-DnsName", "solução de problemas DNS", "teste do filtro DNS", "solução de problemas NextDNS", "solução de problemas AdGuard DNS"]
cover: "/img/cover/dns-filtering-bypass-troubleshooting.webp"
coverAlt: "O caminho DNS azul de um laptop atravessa um filtro e termina em um símbolo de bloqueio, enquanto o caminho laranja do navegador alcança outro resolvedor."
coverCaption: "Rastreie o caminho da consulta antes de alterar a regra do filtro."
---

Você configurou um resolvedor com filtragem, mas um dispositivo ainda acessa um domínio bloqueado pela sua política. A causa pode ser a regra, a atribuição do Domain Name System (DNS) ao dispositivo, um resolvedor criptografado do navegador ou uma VPN. **Teste o caminho antes de alterar as configurações.** Uma consulta direta ao filtro responde a uma pergunta diferente da consulta comum do dispositivo.

<!--more-->

## Principais pontos

- **Confira a regra primeiro:** Confirme que o filtro recebe e bloqueia um domínio de teste seguro.
- **Rastreie cada camada:** Roteador, sistema operacional, navegador, VPN e configurações móveis afetam o roteamento DNS.
- **Use consultas novas:** Associe um novo nome de host e horário ao registro de consultas do filtro.
- **Declare o limite:** Uma consulta observada comprova um caminho, não o comportamento de todos os aplicativos ou dispositivos.

## Antes de começar

Reserve cerca de 20 minutos. Você precisa acessar o registro de consultas do resolvedor filtrante, ter um dispositivo com o problema e uma cópia das configurações DNS do roteador. Os exemplos usam um laptop Windows e o **Pi-hole**, mas a mesma comparação funciona com qualquer resolvedor que ofereça registros por cliente. Identifique primeiro o endereço exato do filtro. Não inclua endereços privados de clientes, registros de consulta ou regras de política em um relatório público.

Escolha um **domínio de teste inofensivo** já bloqueado pela sua política. Outra opção é adicionar temporariamente uma regra de recusa exata para um domínio sob seu controle em um perfil de teste. Registre a regra e remova-a após o teste. Não use um domínio ativo de malware como sonda. Uma página bloqueada é um sintoma útil, mas o registro do resolvedor fornece evidências mais fortes do caminho.

| Camada | Pergunta |
|---|---|
| **Filtro** | Uma consulta direta alcança o resolvedor pretendido e corresponde à regra? |
| **Dispositivo** | Quais servidores DNS a rede atribui? |
| **Navegador ou aplicativo** | Este cliente usa o resolvedor do dispositivo ou um caminho separado? |
| **VPN ou relay** | Um túnel ativo altera o destino das consultas? |

## Comprove que o filtro funciona

Abra o registro de consultas do resolvedor. Consulte o domínio bloqueado escolhido diretamente no filtro. No Windows, use o PowerShell e informe o endereço do filtro e o domínio de teste quando solicitado:

```powershell
$filterAddress = Read-Host "Filtering DNS server address"
$testDomain = Read-Host "Harmless domain blocked by your test rule"
Resolve-DnsName -Name $testDomain -Server $filterAddress -Type A -DnsOnly
```

A [referência da Microsoft para **`Resolve-DnsName`**](https://learn.microsoft.com/en-us/powershell/module/dnsclient/resolve-dnsname) define **`-Server`** como uma consulta ao resolvedor indicado. Localize a consulta no registro do filtro e confira a resposta e a regra correspondente. A [documentação do Pi-hole sobre consultas e registros](https://docs.pi-hole.net/main/pihole-command/) descreve as ferramentas locais de consulta. Se a consulta direta for permitida, corrija a regra ou a atribuição do grupo de clientes antes de investigar um desvio. Se ela não alcançar o filtro, verifique o endereço, o serviço e o caminho da rede.

**Este teste direto não comprova que o laptop use normalmente o filtro.** A opção **`-Server`** substitui o resolvedor padrão nesta consulta. Essa diferença evita um falso positivo comum.

## Rastreie o caminho do dispositivo

Use um novo nome de host para evitar uma entrada DNS anterior em cache. O exemplo a seguir envia uma consulta diretamente ao filtro e outra pela seleção normal de resolvedor do laptop. Os nomes são diferentes para identificar qual registro pertence a cada caminho. Uma resposta **NXDOMAIN** significa que o servidor DNS informa que o nome de host não existe. Isso é normal se o nome aleatório não estiver em uso. O que importa aqui é a consulta aparecer no registro do filtro.

```powershell
$stamp = [guid]::NewGuid().ToString("N")
Resolve-DnsName -Name "direct-${stamp}.example.com" -Server $filterAddress -Type A -DnsOnly
Resolve-DnsName -Name "default-${stamp}.example.com" -Type A -DnsOnly
```

Pesquise os dois nomes exatos no registro do filtro e anote o horário e o cliente informado. Se **`direct-`** aparecer e **`default-`** não, inspecione os servidores DNS atribuídos ao laptop. No Windows, **`Get-DnsClientServerAddress`** mostra os endereços de DNS por interface. Confira o adaptador Wi-Fi ou Ethernet ativo, não um desconectado. A [referência do cliente DNS da Microsoft](https://learn.microsoft.com/en-us/powershell/module/dnsclient/get-dnsclientserveraddress) descreve este comando somente de leitura.

Deixe os erros visíveis durante o primeiro teste. Um erro ou tempo limite exige diagnóstico separado e não equivale a uma entrada ausente no registro.

```powershell
Get-DnsClientServerAddress | Select-Object InterfaceAlias, AddressFamily, ServerAddresses
```

Compare as linhas IPv4 e IPv6. **DHCP** atribui configurações de rede como servidores DNS. **IPv6** é a família mais recente de endereços do Internet Protocol e usa endereços de 128 bits. Uma concessão IPv4 pode indicar o filtro enquanto os anúncios IPv6 do roteador fornecem outro servidor DNS. Confira os anúncios de **DHCP** e **DNS IPv6** do roteador e renove a concessão de rede do dispositivo após uma correção. O [guia pós-instalação do Pi-hole](https://docs.pi-hole.net/main/post-install/) explica como o DHCP direciona os clientes ao Pi-hole. O [exemplo de roteador](https://docs.pi-hole.net/routers/fritzbox/) aborda anúncios DNS IPv6.

Se o registro mostrar o **roteador** como cliente, o roteador pode encaminhar consultas em nome dos dispositivos. Nesse caso, o registro do filtro comprova que o roteador chegou ao filtro, não qual dispositivo iniciou a consulta. Confirme o projeto de encaminhamento do roteador antes de tratar a identidade do cliente ausente como falta de dados.

## Confira o DNS do navegador

Uma consulta de linha de comando testa o caminho do resolvedor do dispositivo. Um navegador pode usar **DNS over HTTPS (DoH)** em vez disso. Abra o mesmo domínio de teste bloqueado no navegador e observe o registro do filtro em busca de uma consulta correspondente. Limpe o cache DNS do navegador ou use um novo nome de host sob uma regra de teste quando resultados em cache atrapalharem a comparação.

No **Chrome em um computador**, abra **Configurações > Privacidade e segurança > Segurança > Usar DNS seguro**. A [ajuda do Google Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) informa que o modo automático usa o provedor atual e retorna à consulta sem criptografia se houver falha. Um provedor personalizado selecionado não retorna da mesma forma. Registre o modo e o provedor selecionados antes de alterar a configuração.

No **Firefox**, abra **Configurações > Privacidade e Segurança > DNS sobre HTTPS**. O [guia da Mozilla sobre níveis de proteção](https://support.mozilla.org/en-US/kb/dns-over-https) distingue os modos Padrão, Aumentado, Máximo, Personalizado e Desativado. A [visão geral do DoH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https) explica quando um resolvedor do navegador ignora um filtro DNS local. Teste novamente após uma alteração controlada e depois restaure sua configuração de privacidade desejada.

**Não classifique toda consulta ausente do navegador como desvio.** O navegador pode reutilizar dados em cache, alcançar um endereço já conhecido ou usar um proxy. Compare um nome novo, uma janela de tempo correspondente e a configuração do resolvedor do navegador antes de concluir para onde a consulta foi.

## Confira os caminhos móveis e da VPN

No **Android**, examine **Configurações > Rede e Internet > DNS privado**. O nome de host de um provedor seleciona um serviço DNS privado diferente do DNS anunciado pelo roteador. As [configurações de rede Android do Google](https://support.google.com/android/answer/9654714?hl=en) explicam as opções Desativado, Automático e Nome do host do provedor. Para um resultado local controlado, teste no Wi-Fi com os dados móveis desativados e depois restaure sua configuração normal.

Em **dispositivos Apple**, confira se o **iCloud Private Relay** está ativo para a rede e se o Safari usa o caminho esperado. A Apple afirma que o [Private Relay protege a navegação do Safari e as informações DNS](https://support.apple.com/en-gb/102602). Seus [controles de rede](https://support.apple.com/en-ie/102022) descrevem o tratamento por rede quando a filtragem entra em conflito com o Private Relay. Não generalize um resultado do Safari para todos os aplicativos do dispositivo.

Uma **VPN** pode fornecer seu próprio resolvedor DNS ou enviar consultas pelo túnel. Registre se a VPN está conectada, suas configurações DNS e a política de túnel dividido. Compare o mesmo teste com a VPN ativada e desativada somente se sua política de segurança permitir. Um resultado diferente identifica uma mudança de caminho. Por si só, ele não comprova um vazamento nem uma falha do filtro.

## Interprete os resultados

| Evidência | Próxima verificação provável |
|---|---|
| **Consulta direta ausente do registro do filtro** | Endereço do filtro, serviço DNS, registro ou alcance da rede |
| **Consulta direta permitida** | Regra de recusa exata, política de grupo ou prioridade da regra |
| **Consulta direta registrada, consulta padrão ausente** | DHCP, DNS estático do dispositivo, DNS IPv6 ou resolvedor da VPN |
| **Consulta padrão registrada, navegador ausente** | DoH do navegador, cache, proxy ou relay |
| **Ambas registradas e bloqueadas, mas o site abre** | Outro nome de host, conteúdo em cache, endereço direto ou caminho do aplicativo |

**A ausência de registros é ambígua** se o registro estiver desativado, o roteador encaminhar em nome do cliente ou o teste reutilizar dados em cache. Repita com um nome de host novo e confira o horário da consulta antes de alterar regras do firewall. Bloquear DNS comum para resolvedores externos não obriga um navegador criptografado ou uma VPN a usar seu filtro. O [guia do Pi-hole para OPNsense](https://docs.pi-hole.net/routers/opnsense/) apresenta o bloqueio de DNS externo como controle de rede opcional. As políticas do dispositivo e a configuração do navegador continuam sendo controles separados.

## Corrija e teste novamente

Altere uma camada por vez. Corrija anúncios DHCP ou DNS IPv6, remova um resolvedor estático não intencional, selecione o provedor DNS esperado no navegador ou ajuste a política DNS da VPN. Não enfraqueça silenciosamente DNS criptografado nem a proteção do relay em todos os dispositivos para resolver uma única falha de teste. Registre o dispositivo de origem, a interface, o endereço do filtro, o nome consultado, o horário, a resposta, o cliente no registro, o modo do navegador, o estado da VPN e a alteração feita.

Repita os testes **direto**, **padrão** e **do navegador** após cada alteração. Use um nome de host novo em cada execução. Se um dispositivo tiver vários perfis de rede, teste cada um separadamente. A [comparação de resolvedores DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) ajuda a escolher um serviço. O [teste de vazamento do navegador](/articles/privacy-browser-leak-test-dns-webrtc/) responde a outra pergunta: quais informações de rede saem da configuração do navegador e da VPN. **Um resultado confiável do filtro exige uma regra verificada e um caminho de cliente verificado.**

## Próximas etapas

Repita os testes direto, padrão e do navegador após cada alteração controlada. Consulte a [comparação de resolvedores DNS](/articles/dns-comparison-adguard-quad9-cloudflare-pi-hole/) ao escolher um serviço de filtragem.

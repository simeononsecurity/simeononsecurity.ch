---
title: "Planeje e teste a segmentação VLAN de um homelab"
date: 2026-10-10
lastmod: 2026-11-12
toc: true
draft: false
description: "Crie um plano VLAN para dispositivos confiáveis, servidores, IoT e visitantes. Registre o tráfego permitido, configure a rede por etapas e teste o isolamento."
genre: ["Homelab", "Segurança de rede", "Redes"]
tags: ["VLAN de homelab", "segmentação VLAN", "rede IoT", "rede de visitantes", "firewall de homelab", "roteamento entre VLANs", "802.1Q", "isolamento de rede", "teste VLAN", "VLAN pfSense", "porta de acesso", "porta trunk", "regras de firewall", "segurança de homelab", "plano de rede", "sub-rede", "DHCP", "DNS", "switch gerenciável", "SSID sem fio"]
cover: "/img/cover/homelab-vlan-segmentation-plan.webp"
coverAlt: "Um roteador e um switch de homelab separam laptops, servidores, dispositivos IoT e visitantes em zonas de rede protegidas."
coverCaption: "Planeje os limites das VLANs e teste cada caminho permitido e bloqueado."
---

Um homelab costuma conectar laptops, servidores, câmeras e dispositivos de visitantes à mesma rede. A **segmentação VLAN** coloca esses grupos em redes separadas. Um roteador, firewall ou switch de camada 3 roteia o tráfego entre elas. Regras de firewall ou listas de controle de acesso do switch controlam esses fluxos roteados. Este guia ajuda você a elaborar o plano, aplicar uma alteração por vez e testar o resultado.

## Principais pontos

- **Agrupe por confiança:** coloque dispositivos de gerenciamento, servidores, dispositivos IoT e visitantes em redes separadas quando as necessidades de acesso forem diferentes.
- **Registre os caminhos permitidos:** anote origem, destino, serviço e motivo de cada conexão entre redes.
- **Configure as duas camadas:** as configurações do switch e do ponto de acesso atribuem dispositivos às VLANs. Regras de firewall ou listas de controle de acesso do switch controlam o tráfego roteado.
- **Teste os dois resultados:** verifique uma conexão permitida e outra negada a partir de cada rede relevante.

## Antes de começar

Você precisa de um roteador ou firewall com interfaces VLAN, ou de um switch de camada 3 compatível com roteamento VLAN e listas de controle de acesso. Um switch gerenciável transporta as VLANs cabeadas. Se você separar clientes sem fio, também precisa de um ponto de acesso com redes Wi-Fi vinculadas a VLANs. Mantenha um dispositivo na rede de gerenciamento atual enquanto altera a configuração. Salve primeiro as configurações do roteador, switch e ponto de acesso. As etapas abaixo usam um **plano ilustrativo**. Adapte os endereços e as portas aos seus equipamentos.

Uma **interface VLAN** conecta o gateway a uma VLAN. O gateway pode ser um roteador, firewall ou switch de camada 3. Um **escopo DHCP** é o intervalo de endereços que um serviço DHCP oferece aos dispositivos nessa rede. Um **relay DHCP** encaminha solicitações de endereço de uma VLAN a um servidor DHCP em outra rede. Use um relay quando o gateway não fornecer endereços para essa VLAN e o servidor DHCP estiver em outro local. O [guia de relay DHCP da Juniper](https://www.juniper.net/documentation/us/en/software/junos/dhcp/topics/topic-map/dhcp-relay-agent-security-devices.html) descreve esse caminho. Um **SSID** sem fio é o nome da rede à qual os clientes se conectam. Se seus equipamentos não tiverem um switch gerenciável ou ponto de acesso compatível com VLAN, comece pela rede de visitantes integrada e verifique o isolamento antes de comprar ou trocar hardware.

Se precisar dos conceitos básicos, leia [sub-redes e VLANs](/articles/networking-basics-what-are-subnets-and-vlans/). O [guia de segmentação de rede](/articles/how-to-perform-network-segmentation-for-improved-security/) do site aborda o conceito de segurança mais amplo. A CISA descreve redes domésticas separadas para visitantes e dispositivos da Internet das Coisas no guia [Federal Mobile Workplace Security](https://www.cisa.gov/sites/default/files/2024-08/Federal-Mobile-Workplace-Security_508_2024-08-14.pdf).

> **Aviso:** Uma alteração de VLAN na porta que transporta sua conexão de gerenciamento pode bloquear seu acesso. Mantenha acesso físico e uma rota de recuperação conhecida até que cada rede passe nos testes.

Antes de mover um cabo, exporte a configuração de cada dispositivo e anote o IP de gerenciamento atual, a porta do switch, a configuração de VLAN e o login de administrador. Deixe uma porta de gerenciamento conhecida e um laptop na rede original. Se uma alteração interromper o acesso, conecte o laptop novamente a essa porta, restaure a configuração salva e confirme que o gateway antigo responde antes de tentar outra vez. Se não houver um caminho de gerenciamento acessível no switch, use o console documentado ou o procedimento de recuperação local. Não redefina o equipamento sem saber o que a redefinição apaga.

## Inventarie dispositivos e fluxos

Liste cada dispositivo, seu endereço atual, seu responsável e os serviços necessários. Defina um motivo para cada dispositivo alcançar outra rede. Por exemplo, um laptop pode administrar um servidor, enquanto uma câmera precisa alcançar apenas um gravador e um servidor DNS. Um telefone de visitante precisa de internet, mas não de acesso aos servidores.

| Grupo de dispositivos | Exemplos | Acesso necessário |
|---|---|---|
| **Gerenciamento** | Laptop administrativo, interfaces de gerenciamento do switch e do ponto de acesso | Gerenciar roteador, switch, ponto de acesso e servidores |
| **Servidores** | Hipervisor, NAS, destino de backup | Atualizações, DNS, tráfego de aplicativos aprovado |
| **IoT** | Câmeras, tomadas inteligentes, dispositivos de mídia | DNS, serviço de horário, controlador ou gravador específico |
| **Visitantes** | Telefones e laptops de visitantes | Internet, DNS, sem acesso a sub-redes privadas |

Registre exceções antes de adicionar regras. Recursos de descoberta local, como transmissão para uma tela, muitas vezes dependem de tráfego multicast que não cruza um limite roteado por padrão. Não libere todo o tráfego entre VLANs para corrigir um único problema de descoberta. Identifique o protocolo e adicione a menor exceção compatível.

## Atribua VLANs e endereços

Atribua um ID de VLAN e uma sub-rede IP separada a cada grupo. Este **plano ilustrativo** usa endereços reservados para documentação e pressupõe que o roteador forneça DHCP e DNS. Não copie a tabela para uma rede ativa sem verificar conflitos de endereço.

| Rede | ID da VLAN | Sub-rede | Gateway de exemplo |
|---|---:|---|---|
| **Gerenciamento** | 10 | `192.0.2.0/27` | `192.0.2.1` |
| **Servidores** | 20 | `198.51.100.0/27` | `198.51.100.1` |
| **IoT** | 30 | `203.0.113.0/27` | `203.0.113.1` |
| **Visitantes** | 40 | `192.0.2.32/27` | `192.0.2.33` |

Essas faixas reservadas para documentação ilustram apenas o layout, conforme definido pela [RFC 5737](https://www.rfc-editor.org/info/rfc5737). Use endereços privados da [RFC 1918](https://www.rfc-editor.org/info/rfc1918) no laboratório real, com uma sub-rede sem sobreposição para cada VLAN. Registre no plano cada gateway real, pool DHCP, endereço DNS e reserva de dispositivo.

**Portas de acesso** transportam a rede de um único dispositivo sem etiqueta VLAN. **Portas trunk** transportam VLANs selecionadas com etiquetas entre o roteador, o switch e o ponto de acesso. Ajuste o ID de VLAN e a configuração nativa ou sem etiqueta nas duas extremidades. O [guia de switch VLAN da Netgate](https://docs.netgate.com/pfsense/en/latest/recipes/switch-vlan-configuration.html) explica portas trunk etiquetadas, portas de acesso sem etiqueta e IDs de VLAN por porta. Evite usar a VLAN 1 padrão para gerenciamento se o seu hardware permitir uma VLAN separada, conforme descreve a [orientação de segurança VLAN](https://docs.netgate.com/pfsense/en/latest/vlan/security.html) da Netgate.

O tráfego **nativo** ou **sem etiqueta** em um trunk não possui etiqueta VLAN. As duas extremidades precisam atribuí-lo à mesma VLAN, ou um dispositivo pode chegar à rede errada. Permita apenas as VLANs necessárias ao link. Desative portas do switch sem uso ou atribua-as a uma rede restrita. A Netgate também recomenda não tratar uma VLAN como limite de segurança completo quando um invasor controla uma porta do switch. Proteja as portas físicas e as credenciais dos dispositivos, além do tráfego roteado.

## Crie uma matriz de tráfego

Uma VLAN sozinha separa domínios de broadcast. O **roteamento entre VLANs** no roteador ou switch de camada 3 ainda precisa de regras de acesso. Decida qual dispositivo roteia o tráfego entre as VLANs. Se um switch de camada 3 roteia localmente, o tráfego entre suas VLANs talvez nunca alcance o firewall do roteador. Aplique listas de controle de acesso equivalentes no switch ou roteie pelo firewall. Depois, teste no ponto real de aplicação das regras. Verifique a direção da ACL do switch e se ela acompanha o estado da conexão. Muitas ACLs de switch verificam pacotes separadamente em cada direção, então uma conexão permitida pode exigir uma regra restrita para o tráfego de retorno. O [guia de ACL da Cisco](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/security/acls/acls-configuration-guide/access-control-lists.html) descreve a direção da interface e a correspondência ordenada de pacotes. Use o inventário de dispositivos para registrar as conexões a permitir. As entradas seguintes são exemplos, não um conjunto universal de regras.

| Origem | Destino | Serviço | Decisão |
|---|---|---|---|
| **Gerenciamento** | Interface de administração do servidor | TCP 443 | Permitir para dispositivos de gerenciamento aprovados |
| **Gerenciamento** | Interfaces de administração do roteador, switch e ponto de acesso | Portas de gerenciamento documentadas | Permitir para dispositivos de gerenciamento aprovados |
| **IoT** | Gravador de câmeras | Porta documentada do gravador | Permitir apenas se necessário |
| **IoT** | Serviço DNS e de horário aprovado | DNS e NTP | Permitir apenas para os serviços escolhidos |
| **IoT** | Sub-rede de gerenciamento | Qualquer | Negar |
| **Visitantes** | Sub-redes privadas | Qualquer | Negar |
| **Visitantes** | DNS e internet | DNS, tráfego Web | Permitir pelo resolver e gateway aprovados |

Inclua os próprios serviços do roteador no plano. Uma regra que bloqueia o acesso de IoT a outras VLANs ainda pode deixar acessível a interface de administração do roteador. Restrinja os serviços de gerenciamento à rede de gerenciamento. Comece apenas com as regras de permissão necessárias e uma negação padrão para o restante do tráfego roteado. Verifique as regras de permissão amplas existentes antes de presumir que a configuração padrão negue tudo. As [práticas recomendadas de firewall](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) da Netgate observam que uma LAN padrão do pfSense inclui uma regra de permissão. Se você usa pfSense, a [metodologia de regras](https://docs.netgate.com/pfsense/en/latest/firewall/rule-methodology.html) explica que regras de interface filtram o tráfego que entra por essa interface e que conexões permitidas criam estado para o tráfego de retorno.

A tabela de exemplo cobre IPv4. Se a rede usa IPv6, atribua um prefixo IPv6 e uma política a cada VLAN, inspecione os anúncios de roteador e teste também os caminhos IPv6 permitidos e negados. Bloquear IPv4 não comprova isolamento IPv6. Se você não pretende rotear IPv6, verifique as configurações IPv6 do roteador e os endereços dos clientes em vez de presumir que IPv6 está ausente. A Netgate documenta o [comportamento do firewall IPv6](https://docs.netgate.com/pfsense/en/latest/config/advanced-networking.html) e os [anúncios de roteador](https://docs.netgate.com/pfsense/en/latest/services/dhcp/ipv6-ra.html).

## Configure uma rede por vez

1. Escolha o gateway da VLAN. Se o roteador ou firewall fizer o roteamento, crie nele uma interface VLAN e atribua o endereço de gateway. Se um switch de camada 3 fizer o roteamento, crie a interface VLAN nesse switch. Configure um escopo DHCP no gateway ou um relay DHCP para o servidor DHCP existente. Confirme que um resolver DNS aprovado está acessível. O [guia de configuração VLAN da Netgate](https://docs.netgate.com/pfsense/en/latest/vlan/configuration.html) lista as etapas de interface e serviço para um gateway pfSense.
2. Se o roteador for o gateway da VLAN, adicione essa VLAN ao trunk entre roteador e switch. Se o gateway for o switch de camada 3, deixe o switch manter o endereço de gateway da VLAN e roteie ao roteador ou firewall por uma rede de trânsito separada ou um uplink roteado. Configure uma rota padrão no switch em direção ao roteador upstream. Adicione no roteador uma rota de retorno para cada VLAN cujo gateway esteja no switch. Verifique a política do firewall do roteador e o NAT de saída dessas sub-redes se precisarem de internet. Não configure o mesmo endereço de gateway ou escopo DHCP nos dois dispositivos. Adicione a VLAN ao trunk entre switch e ponto de acesso quando clientes sem fio precisarem da rede. O [guia de roteamento entre VLANs da Cisco](https://www.cisco.com/c/en/us/support/docs/lan-switching/inter-vlan-routing/41260-189.html) mostra gateways VLAN no switch. A Netgate documenta [rotas de retorno](https://docs.netgate.com/pfsense/en/latest/routing/static.html) e [NAT de saída](https://docs.netgate.com/pfsense/en/latest/nat/outbound.html) para redes atrás de um roteador interno.
3. Atribua à VLAN uma porta de acesso ou SSID sem fio de teste. Conecte um dispositivo de teste não crítico a essa porta ou SSID.
4. Adicione as regras de firewall ou ACLs do switch previstas no dispositivo que roteia a VLAN. Confirme que o restante do tráfego roteado é negado. Verifique a direção da ACL e o tráfego de retorno se o switch não acompanhar o estado da conexão. Teste o acesso a cada gateway, interface de gerenciamento, sub-rede local e IPv6, se houver. Permita apenas os caminhos da matriz de tráfego. Limite o gerenciamento à rede de gerenciamento. Confira a ordem das regras e remova ou restrinja regras amplas existentes somente depois de o caminho de gerenciamento de teste funcionar.
5. Confirme que o dispositivo de teste recebe endereço, gateway e servidor DNS da sub-rede prevista. Depois, execute as verificações de conexão abaixo antes de mover mais dispositivos.

Não mova o último dispositivo de gerenciamento até que o caminho substituto funcione. Salve a configuração funcional depois de cada rede passar nos testes. Se DHCP, DNS ou acesso de gerenciamento falhar, volte o dispositivo de teste à porta ou ao SSID original. Restaure a última alteração do switch ou roteador a partir da configuração salva e teste a rede original de novo antes de continuar.

## Teste o isolamento e o acesso

Use um serviço sob seu controle e que esteja escutando no destino. Em um dispositivo Windows de teste, substitua o endereço e a porta de exemplo por um servidor real e execute:

```powershell
Test-NetConnection -ComputerName 198.51.100.10 -Port 443
```

O campo **`TcpTestSucceeded`** informa se a conexão TCP foi estabelecida. A [referência Microsoft do Test-NetConnection](https://learn.microsoft.com/powershell/module/nettcpip/test-netconnection) documenta os parâmetros `-ComputerName` e `-Port`. Uma conexão que falha não comprova, por si só, que uma regra de firewall funcionou. O serviço pode estar parado ou o firewall do host pode rejeitar o tráfego. Verifique o serviço de destino e o log do firewall de rede antes de concluir.

Teste de um dispositivo realmente conectado a cada VLAN de origem. Antes de cada teste, registre o endereço de origem, gateway e servidor DNS. Verifique uma conexão permitida ao serviço previsto, uma conexão negada a um serviço interno fora da matriz, uma consulta DNS pelo resolver previsto e acesso à internet quando planejado. Para uma VLAN com gateway no switch, confira a rota padrão do switch, a rota de retorno do roteador e o caminho de volta do destino se uma conexão permitida falhar. Repita os testes permitidos e negados com endereços IPv6 quando IPv6 estiver ativo. No pfSense, **Status > System Logs > Firewall** mostra ações de permissão ou bloqueio registradas. O [guia da Netgate para logs do firewall](https://docs.netgate.com/pfsense/en/latest/monitoring/logs/firewall.html) descreve essa visualização. Compare origem, destino, porta e regra do log com seu teste. Se o teste funcionar quando não deveria, inspecione regras amplas de permissão e estados existentes. Inicie uma nova conexão depois de alterar regras, pois uma conexão estabelecida pode continuar funcionando por causa do estado existente.

Para verificar DNS no Windows, execute `nslookup example.com` e compare o servidor exibido com o resolver planejado. Depois, tente uma consulta de um cliente visitante ou IoT com DNS restrito. Uma consulta bem-sucedida não comprova que o cliente usou o resolver escolhido, então confira o servidor informado e um log do firewall ou resolver. Teste também, como um caso negado separado, o acesso direto de um dispositivo IoT ou visitante ao endereço de gerenciamento do roteador.

Dispositivos na **mesma VLAN** podem trocar tráfego sem passar pelo firewall do roteador. Teste separadamente o isolamento local de clientes se o ponto de acesso oferecer esse recurso e use firewalls de host nos servidores. Testes de firewall entre VLANs não comprovam isolamento dentro da mesma VLAN.

> **Resultado esperado:** cada dispositivo recebe um endereço da sub-rede planejada. Os serviços permitidos funcionam. As tentativas negadas correspondem a um bloqueio do firewall ou a um controle equivalente documentado.

## Solução de problemas

- **Sem endereço:** verifique a VLAN da porta de acesso ou do SSID, as tags do trunk, o escopo DHCP e a interface do gateway.
- **O endereço funciona, mas DNS falha:** verifique o endereço do resolver, o vínculo do serviço no roteador e a regra de firewall para DNS.
- **Um dispositivo alcança outra VLAN inesperadamente:** verifique as regras do roteador, regras amplas de permissão e se os dispositivos ainda compartilham uma rede sem etiqueta.
- **Sem log de firewall para tráfego roteado:** verifique se um switch de camada 3 ou outro gateway roteou a conexão antes que ela chegasse ao firewall.
- **VLAN com gateway no switch alcança redes locais, mas não a internet:** confira a rota padrão do switch, rotas de retorno do roteador, política do firewall e NAT de saída para a sub-rede VLAN.
- **IPv4 está bloqueado, mas a conexão funciona:** confira endereços IPv6, anúncios de roteador, regras IPv6 e estados existentes.
- **Um teste negado expira sem log do firewall:** confirme que o serviço de destino está escutando. Depois, inspecione o roteamento e as configurações de log. O [guia da Netgate para solução de problemas de firewall](https://docs.netgate.com/pfsense/en/latest/troubleshooting/firewall.html) descreve as verificações de log e estado.
- **A transmissão ou descoberta para de funcionar:** identifique o protocolo de descoberta e o caminho do controlador antes de adicionar uma exceção restrita.

## Próximas etapas

Mantenha o inventário de dispositivos e a matriz de tráfego junto do diagrama da rede. Revise as regras quando adicionar um servidor ou dispositivo IoT. Repita um teste de conexão permitida e outro negado após cada alteração relevante na rede. Para os princípios de projeto mais amplos, consulte [segmentação de rede](/articles/how-to-perform-network-segmentation-for-improved-security/).

---
title: "Teste vazamentos de DNS e WebRTC no navegador com uma VPN"
date: 2026-10-11
lastmod: 2026-11-12
toc: true
draft: false
description: "Verifique o IP público, o resolvedor DNS e os endereços WebRTC do navegador antes e depois de conectar uma VPN. Interprete os resultados e investigue problemas de roteamento."
genre: ["Privacidade", "Navegadores", "Redes"]
tags: ["teste de vazamento DNS", "teste de vazamento WebRTC", "teste de vazamento VPN", "teste de privacidade do navegador", "vazamento de endereço IP", "DNS sobre HTTPS", "DNS seguro", "DNS do Firefox", "DNS seguro do Chrome", "candidatos WebRTC", "tunelamento dividido VPN", "vazamento IPv6", "teste de resolvedor", "privacidade do navegador", "privacidade de rede", "solução de problemas VPN", "resolvedor DNS", "candidatos ICE", "endereço IP privado", "mDNS"]
cover: "/img/cover/privacy-browser-leak-test-dns-webrtc.webp"
coverAlt: "Janela de navegador com três painéis para IP público, DNS e conexões entre pares, além de um túnel contínuo e uma rota alternativa pontilhada até servidores remotos."
coverCaption: "Compare cada rota de rede antes e depois de conectar sua VPN."
---

O ícone de conexão de uma rede privada virtual (VPN) não comprova que toda solicitação do navegador siga a mesma rota. Teste separadamente seu **IP público**, o **resolvedor do Sistema de Nomes de Domínio (DNS)** e os **endereços WebRTC**. Cada resultado responde a uma pergunta diferente. Este guia oferece uma verificação repetível e um modo de investigar resultados inesperados.

<!--more-->

## Pontos principais

- **Compare dois estados:** Registre os mesmos testes antes e depois de conectar a VPN.
- **Leia cada resultado separadamente:** Uma mudança no IP público não mostra para onde foram as consultas DNS.
- **Confira os candidatos WebRTC:** Procure um endereço público fora da rota prevista. Um endereço privado tem outro significado.
- **Altere uma configuração por vez:** Teste novamente após cada mudança na VPN, no navegador ou no DNS.

## Antes de começar

Use o navegador e a conexão de rede que pretende proteger. Saiba se a VPN deve cobrir o dispositivo inteiro ou somente determinados aplicativos. Se a VPN usa tunelamento dividido, registre se o navegador de teste está dentro do túnel. Tenha à mão a política de DNS do cliente VPN para fazer a comparação.

O **tunelamento dividido** envia certos aplicativos pela VPN e deixa os demais usarem a rede normal.

Este procedimento usa as páginas de [IP do BrowserLeaks](https://browserleaks.com/ip), [DNS](https://browserleaks.com/dns) e [WebRTC](https://browserleaks.com/webrtc). O serviço vê o endereço da sua conexão quando você o visita. De acordo com a descrição do teste, a verificação de DNS pede ao navegador que resolva 50 nomes aleatórios. Não execute testes externos em uma rede gerenciada ou restrita sem autorização. Não insira credenciais, nomes de hosts internos nem registros privados de navegação em um site de teste.

> **Aviso:** Não publique seus endereços IP exatos em capturas de tela públicas ou publicações de suporte. Registre se os endereços correspondem à rota esperada do provedor de Internet ou da VPN. Compartilhe os valores reais somente por um canal de suporte aprovado.

## O que cada teste mostra

| Verificação | O que comparar | O que o resultado não comprova |
|---|---|---|
| **IP público** | Endereço visto por um site comum | Qual resolvedor tratou o DNS |
| **Resolvedor DNS** | Servidores observados durante novas consultas de nomes | Para onde cada aplicativo envia DNS |
| **WebRTC** | Candidatos de conexão locais e públicos | Qual candidato uma chamada posterior usará |

A página de IP público informa o endereço usado pela solicitação web. A página de DNS inicia novas consultas e informa os resolvedores que as atendem. WebRTC, sigla de Web Real-Time Communication, permite que aplicativos do navegador estabeleçam conexões entre pares. A página WebRTC verifica endereços expostos durante essas conexões. Um **candidato ICE** é um possível endereço de rede para uma conexão entre pares. Uma **saída da VPN** é o endereço público usado quando o tráfego deixa a VPN. A [RFC 8828](https://datatracker.ietf.org/doc/html/rfc8828) explica por que os candidatos de conexão WebRTC às vezes incluem endereços diferentes daquele visto em uma solicitação web comum, em especial com túneis divididos ou proxies.

Um servidor DNS do provedor da VPN, outro resolvedor escolhido dentro da VPN ou um resolvedor criptografado escolhido no navegador exibem nomes diferentes no teste. O nome do resolvedor, por si só, não identifica um vazamento. Compare-o com a política pretendida.

## Registre uma referência inicial

Desconecte a VPN somente se sua situação permitir uma referência sem túnel. Abra as três páginas de teste em um perfil normal do navegador. Execute o teste de DNS e aguarde o resultado. Registre os dados abaixo sem publicar os endereços exatos:

| Campo | Nota inicial |
|---|---|
| **Navegador e versão** | Nome, versão e extensões de privacidade pertinentes |
| **Rede** | Wi-Fi doméstico, ponto de acesso móvel ou outra rede aprovada |
| **IPv4 e IPv6 públicos** | Se cada endereço pertence à conexão normal |
| **Resultado DNS** | Nomes ou operadores dos resolvedores exibidos |
| **Resultado WebRTC** | Candidatos públicos, privados ou `.local` exibidos |

Se não puder desconectar a VPN, comece com a rota VPN esperada e marque a referência sem túnel como indisponível. Não deduza o endereço normal do provedor por um rótulo de localização ou um mapa. Bancos de dados de localização às vezes divergem do operador de rede real.

## Repita com a VPN conectada

Conecte a VPN e confirme se o cliente informa que o túnel está ativo. Recarregue cada página de teste no **mesmo perfil do navegador**. Execute o teste DNS novamente para criar novas consultas. Registre os resultados de IPv4 e IPv6 quando o serviço os exibir.

Compare os resultados nesta ordem:

1. **IP público:** A solicitação web deve mostrar um endereço compatível com a saída da VPN ou com a rota configurada de propósito. Se o navegador deveria estar no túnel, um endereço normal do provedor indica um problema de roteamento.
2. **DNS:** Compare cada resolvedor exibido com as configurações de DNS da VPN e do navegador. Investigue um resolvedor do provedor fora do túnel esperado. Um resolvedor externo identificado é esperado se você o selecionou no navegador.
3. **WebRTC:** Compare o candidato WebRTC público com a saída da VPN e o IP público de referência. Se todo o tráfego do navegador deveria usar a VPN, a aparição do IP público normal somente no WebRTC merece investigação.
4. **Endereços privados:** Um endereço nas [faixas privadas da RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) ou um candidato `.local` difere do IP público do provedor. Registre a entrada local e avalie se o site deve conhecê-la.

O [padrão de tratamento de IP do WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) descreve como um aplicativo descobre outros endereços públicos ou privados por meio de candidatos ICE. O projeto de [candidatos de host mDNS do Chromium](https://groups.google.com/a/chromium.org/g/blink-dev/c/z5hSy6Rf_aE/m/aGND030cAgAJ) substitui alguns endereços privados por nomes `.local`. Um resultado WebRTC em branco é **inconclusivo** se JavaScript, a API ou o servidor de teste não funcionou. Um resultado em branco não comprova proteção completa.

> **Resultado esperado:** A solicitação web comum do navegador e os candidatos WebRTC públicos seguem a rota escolhida. Os resultados DNS correspondem à política do resolvedor da VPN ou do navegador que você registrou.

## Investigue uma diferença de DNS

Primeiro confira se o navegador escolhe o próprio resolvedor. As configurações de [DNS sobre HTTPS do Firefox](https://support.mozilla.org/en-US/kb/dns-over-https) exibem o estado ativo e o nível de proteção. A proteção padrão volta ao resolvedor do sistema em algumas condições e respeita sinais da rede. Os níveis Aprimorado e Personalizado usam um provedor selecionado com opções de reserva. O nível Máximo avisa quando a resolução segura falha. O estado e a lista de exceções importam mais do que um botão isolado.

O [guia de DNS Seguro do Chrome](https://support.google.com/chrome/answer/10468685?co=GENIE.Platform%3DDesktop&hl=en) descreve o modo automático e um provedor personalizado. O modo automático volta a uma consulta sem criptografia se a resolução segura falhar. Um provedor personalizado não usa o modo sem criptografia como padrão. Dispositivos gerenciados e controles parentais restringem essa configuração. Confira a interface atual do navegador antes de alterar uma política gerenciada.

Se o resolvedor do navegador não for a causa, compare a configuração DNS do cliente VPN, a lista de aplicativos do túnel dividido, o resolvedor do sistema operacional e a rota IPv6. Altere um item e repita o teste DNS. O teste DNS do navegador mede o caminho de consulta desse navegador. O resultado não informa como outro aplicativo resolve nomes. Se a rede usa [filtragem DNS](/articles/nextdns-vs-adguard-ad-blocker-comparison/), teste um domínio bloqueado de propósito e outro permitido. Não trate a ausência de um anúncio como prova do caminho do resolvedor.

## Investigue uma diferença de WebRTC

Confira se o navegador ficou fora do túnel VPN ou usa um proxy fora da rota prevista. Corrija a rota e teste novamente. Não desative IPv6 nem WebRTC como primeira resposta a um único resultado ambíguo. O [padrão WebRTC](https://datatracker.ietf.org/doc/html/rfc8828) descreve a troca entre exposição de endereços e desempenho de chamadas diretas. Restringir candidatos ou impor um proxy afeta chamadas de vídeo e outras conexões entre pares.

Se o navegador ou a VPN oferecer um controle documentado para tratar IPs do WebRTC, leia a descrição atual e escolha uma política compatível com o uso de chamadas. Teste novamente o candidato público. Um endereço local, sozinho, não comprova que o IP público do provedor saiu da VPN. Um IP público do provedor exposto, comparado com outro endereço HTTP da VPN, é um indício mais forte.

## Mantenha um registro dos testes

| Campo | Resultado a registrar |
|---|---|
| **Data e navegador** | Versão, perfil, extensões e rede |
| **Rota esperada** | VPN para todo o dispositivo, túnel dividido ou proxy do navegador |
| **Antes e depois** | Operador do IP público, operador DNS e candidato WebRTC público |
| **Diferença** | Qual resultado divergiu da política pretendida |
| **Uma mudança** | Configuração alterada e motivo |
| **Novo teste** | Novo resultado e incertezas restantes |

Repita a verificação depois de mudar a configuração do navegador, da VPN ou da rede. Um resultado limpo cobre o navegador, o perfil, a rede e o momento testados. Ele não comprova anonimato nem cobre todos os aplicativos. Se ainda estiver escolhendo um navegador, consulte a [comparação de navegadores privados](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) para conhecer os recursos e depois execute este teste na sua configuração.

## Próximos passos

Repita o teste depois de mudanças no navegador, na VPN ou na rede. Consulte a [comparação de navegadores privados](/articles/best-privacy-browsers-librewolf-brave-firefox-tor/) para escolher um navegador.

---
title: "Atualização de segurança do Chrome 156: verificar a correção de outubro"
date: 2026-10-28
lastmod: 2026-11-09
toc: true
draft: false
description: "Verifique a versão de segurança do Chrome 156 de 27 de outubro em Windows, macOS, Linux e Android. Compare a compilação instalada, conclua um reinício pendente e verifique os dispositivos geridos separadamente."
genre: ["Navegadores", "Segurança", "Gestão de correções"]
tags: ["Chrome 156", "atualização de segurança do Chrome", "verificação de correção do Chrome", "verificação da versão do Chrome", "Chrome 156 para Windows", "Chrome 156 para macOS", "Chrome 156 para Linux", "Chrome 156 para Android", "CVE-2026-118306", "CVE-2026-118331", "CVE-2026-118348", "CVE-2026-118344", "correções de navegador", "Chrome Enterprise Core", "navegadores geridos", "segurança do Chromium", "atualizações de navegador", "reinício do Chrome", "chrome://version", "chrome://settings/help", "atualização do Chrome para Android", "atualizações de segurança do Brave", "atualizações de segurança do Edge"]
cover: "/img/cover/cybersecurity-padlock-shield.webp"
coverAlt: "Ilustração de um cadeado e de um escudo que representam uma atualização de segurança, não um ecrã de versão do Chrome"
coverCaption: ""
---

**A versão de segurança do Chrome de 27 de outubro de 2026** inclui 52 correções. Para verificar a instalação, compare a versão completa com a versão publicada para o seu sistema operativo e reinicie o Chrome para concluir qualquer atualização pendente. O anúncio de uma versão não prova que o seu dispositivo recebeu a atualização. ([Versão do Chrome para computadores](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

<!--more-->

## Que versão deve aparecer?

A Google publicou estas versões do canal Stable em 27 de outubro de 2026. O anúncio para computadores indica compilações distintas para Windows e macOS e para Linux. O [anúncio para Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html) indica a sua própria compilação e refere que as versões para Android incluem as mesmas correções de segurança das versões correspondentes para computadores, «salvo indicação em contrário».

| Plataforma | Compilação indicada no anúncio da Google de 27 de outubro |
|---|---|
| **Windows** | 156.0.8078.73 ou 156.0.8078.74 |
| **macOS** | 156.0.8078.73 ou 156.0.8078.74 |
| **Linux** | 156.0.8078.73 |
| **Android** | 156.0.8078.73 |

*Utilize esta tabela para a versão de 27 de outubro, não como uma versão-alvo permanente. Consulte o [feed atual das versões do Chrome](https://chromereleases.googleblog.com/) para ver futuras atualizações de segurança.* A Google indicou que a distribuição para computadores demoraria «os próximos dias ou semanas» e que a compilação para Android chegaria à Google Play nos dias seguintes. Um dispositivo com uma versão inferior à indicada continua a precisar de verificação, mesmo durante uma distribuição faseada. ([Aviso para computadores](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html), [aviso para Android](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html))

A [lista de correções de segurança para computadores](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html) classifica quatro falhas comunicadas como **Critical**: corrupção de memória no FileSystem [CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306), validação incorreta da entrada no FileAPI CVE-2026-118331, validação incorreta da entrada no Skia CVE-2026-118348 e use-after-free no Layout CVE-2026-118344. O mesmo aviso lista outras CVE de nível **High** e **Medium**. O número 52 representa as correções de segurança da versão, não 52 relatos de exploração verificados de forma independente. ([Registo NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-118306))

**O aviso da versão não afirma que as vulnerabilidades indicadas estejam a ser exploradas ativamente.** A advertência diz respeito ao momento da divulgação: «O acesso aos detalhes dos erros e às ligações pode permanecer restrito até que a maioria dos utilizadores receba uma correção». Não interprete o acesso restrito aos detalhes como prova de exploração. ([Aviso para computadores](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html))

## Verificar e concluir a atualização para computadores

1. Abra **`chrome://version`** na instalação do Chrome que utiliza. Registe a versão completa e o sistema operativo, não apenas o número principal 156. Verifique separadamente uma janela de Chrome de outro canal ou instalada noutro local.
2. Abra **`chrome://settings/help`** ou selecione **Mais > Ajuda > Acerca do Google Chrome**. Segundo a Google, o Chrome procura atualizações nesta página. Aguarde até o processo terminar. ([Instruções da Google para atualizar computadores](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en))
3. Se a página apresentar a opção **Reiniciar**, selecione-a. Guarde primeiro o trabalho pendente. Feche as restantes janelas do Chrome, volte a abrir o navegador e consulte **`chrome://version`** novamente. Compare a versão apresentada depois do reinício com a tabela da plataforma.
4. Se a versão continuar abaixo da compilação anunciada, procure novamente atualizações disponíveis. Se uma organização gerir o navegador ou o atualizador indicar um erro, contacte o administrador. Uma transferência bem-sucedida não prova que a versão do navegador em execução mudou.

> **Resultado esperado:** Depois do reinício, a compilação Stable do Chrome em execução corresponde à versão da plataforma indicada no anúncio de 27 de outubro ou a uma versão posterior anunciada pelo fornecedor. Um botão Reiniciar pendente não comprova a conclusão da atualização.

No **Android**, abra Play Store > ícone do perfil > Gerir aplicações e dispositivo e atualize o Chrome em Atualizações disponíveis, se a opção aparecer. No Chrome, abra Mais > Definições > Acerca do Chrome para consultar a versão instalada. Compare-a com a linha Android depois de a atualização da aplicação terminar. Estes caminhos de menu seguem as [instruções da Google para Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en).

## Verificar frotas geridas

Para os navegadores inscritos, utilize o **relatório de versões do Chrome** na consola de administração da Google para encontrar compilações antigas por sistema operativo. Abra a vista Browser Versions, selecione a unidade organizacional relevante, verifique o número de versão secundária completo e exporte o CSV se precisar de uma lista de dispositivos para tratar. Segundo a Google, o relatório inclui navegadores que enviaram relatórios nos 28 dias anteriores. A Google também refere possíveis atrasos, sobretudo em frotas grandes. ([Consultar os detalhes da versão do Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en))

**Separe o inventário comunicado da verificação em tempo real.** Analise a hora do último relatório e o canal de cada dispositivo e confirme os casos atípicos diretamente no navegador ou através do inventário de endpoints geridos. A Google conta separadamente instalações distintas do Chrome, como Stable e Beta. Os relatórios de navegador exigem inscrição e [relatórios de navegadores geridos](https://support.google.com/chrome/a/answer/9301421?hl=en). A ausência de um computador no relatório não prova que tenha a correção.

## Verificar separadamente os navegadores derivados do Chromium

**A tabela de versões do Chrome aplica-se ao Google Chrome.** O Microsoft Edge, o Brave e outros navegadores baseados em Chromium têm pacotes, números de versão e calendários de atualização próprios. O anúncio do Chrome não confirma o estado das respetivas correções. Consulte a versão instalada de cada navegador e o respetivo aviso de segurança ou notas de versão para encontrar as correções Chromium relevantes. Não compare diretamente uma versão do Edge ou do Brave com o número 156.0.8078.73 do Chrome para declarar que está corrigida.

Para cada derivado, registe o nome do produto, o canal, a compilação instalada, o URL do aviso do fornecedor e a compilação que o fornecedor indica como corrigida. Se o fornecedor não confirmar uma correção, marque o estado como **não verificado** e siga as instruções de atualização do fornecedor identificado. Mantenha os resultados do Chrome e dos derivados em linhas separadas do inventário.

## Fontes e referências

- [Chrome Releases: atualização Stable Channel para computadores, 27 de outubro de 2026](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_0562499947.html). Compilações para computadores, 52 correções, CVE e formulação do fornecedor sobre a divulgação.
- [Chrome Releases: atualização do Chrome para Android, 27 de outubro de 2026](https://chromereleases.googleblog.com/2026/10/chrome-for-android-update_0160078013.html). Compilação Android e ressalva sobre as correções correspondentes para computadores.
- [Rastreador de problemas do Chromium: consulta de correções de segurança M156](https://issues.chromium.org/issues?q=customfield1223088:1-M156). Ligação incluída no aviso para computadores. O acesso aos detalhes de cada problema depende das restrições de divulgação.
- [NVD: CVE-2026-118306](https://nvd.nist.gov/vuln/detail/CVE-2026-118306) e [CVE-2026-118331](https://nvd.nist.gov/vuln/detail/CVE-2026-118331). Descrições das vulnerabilidades e versões do Chrome afetadas. Os níveis de gravidade acima seguem o aviso da Google, não uma avaliação CVSS da NVD.
- [Ajuda do Google Chrome: atualizar o Chrome em computadores](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=en) e [no Android](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DAndroid&hl=en). Verificação de atualizações e caminhos de menu para consultar a versão.
- [Ajuda do Chrome Enterprise: consultar os detalhes da versão do Chrome](https://support.google.com/chrome/a/answer/10025748?hl=en) e [ativar relatórios de navegadores geridos](https://support.google.com/chrome/a/answer/9301421?hl=en). Requisitos e limitações dos relatórios de frota.

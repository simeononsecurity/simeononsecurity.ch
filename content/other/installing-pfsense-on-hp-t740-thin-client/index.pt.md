---
title: "Executando o pfSense no HP t740 Thin Client: dicas e guia de solução de problemas"
draft: false
toc: true
date: 2023-04-29
description: "Aprenda como configurar o pfSense no HP t740 Thin Client e como solucionar possíveis problemas como congelamento e problemas de detecção de SSD."
tags: ["pfSense", "OPNsense", "HardenedBSD", "HP t740", "cliente magro", "servidor doméstico", "PPPoE", "FreeBSDGenericName", "prompt de inicialização", "loader.conf.local", "editor nano", "Detecção de SSD", "SSD M.2", "Western Digital", "solução de problemas", "pós-instalação", "UART", "ESXi", "Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Uma caricatura de um mago lançando um feitiço para consertar um computador congelado, com um balão dizendo Problema resolvido"
coverCaption: ""
---
 pfSense, OPNsense ou HardenedBSD no HP t740 Thin Client**

Se você está procurando um dispositivo poderoso para executar pfSense, OPNsense ou HardenedBSD, o HP t740 Thin Client pode ser uma escolha adequada para você.

## Mais Potência e Servidor Doméstico Compacto

O HP t740 Thin Client é um dispositivo compacto que pode ser usado como uma poderosa caixa pfSense ou um servidor doméstico compacto. Ele oferece mais potência do que o t730 ou t620 Plus, o que o torna uma escolha adequada para executar PPPoE, especialmente se você tiver internet de fibra. Ele também pode oferecer um caminho de atualização para redes de 10 Gigabit.

## PS/2 Congela

No entanto, se você planeja executar o FreeBSD ou seus derivados como pfSense, OPNsense ou HardenedBSD no bare metal (ao contrário de dentro do ESXi ou Proxmox), você pode encontrar um problema em que o sistema congela na inicialização com a mensagem `atkbd0: [GIANT-LOCKED]` Felizmente, esse problema pode ser resolvido digitando os seguintes comandos no prompt de inicialização:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Observe que você precisa desativar ambos, caso contrário, ele ainda será bloqueado na inicialização.*

Depois de instalar o sistema operacional, abra um shell de pós-instalação e execute o seguinte comando:

```bash
vi /boot/loader.conf.local
```
Em seguida, adicione estas duas linhas:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persistir alterações usando VI
Para aqueles que não estão familiarizados com o vi, você pode adicionar a linha fazendo o seguinte:

Adicionando as linhas `hint.uart.0.disabled="1"` e `hint.uart.1.disabled="1"` para o `/boot/loader.conf.local` arquivo usando o editor vi pode ser feito com as seguintes etapas:

1. Abra o terminal em seu sistema FreeBSD.

2. Digite `vi /boot/loader.conf.local` e pressione Enter para abrir o arquivo no editor vi.

3. Pressione o botão `i` para entrar no modo de inserção.

4. Mova o cursor para a parte inferior do arquivo usando as teclas de seta.

5. Digite `hint.uart.0.disabled="1"` sem as aspas.

6. Pressione Enter para iniciar uma nova linha.

7. Digite `hint.uart.1.disabled="1"` sem as aspas.

8. Pressione o botão `Esc` para sair do modo de inserção.

9. Tipo `:wq` e pressione Enter para salvar e sair do arquivo.

Isso adicionará as duas linhas ao `/boot/loader.conf.local` arquivo, que desabilitará os UARTs e corrigirá o problema de congelamento durante a inicialização em determinados dispositivos HP t740 "Thin Client" ao executar o FreeBSD ou seus derivados como pfSense, OPNsense ou HardenedBSD.

Isso corrigirá o problema nas reinicializações e atualizações de firmware no pfSense/OPNsense.

## SSD

Se você estiver usando o HP M.2 eMMC, ele não será detectado em uma instalação do FreeBSD pronta para uso. Nesse caso, você precisará de um SSD M.2 de terceiros. Qualquer SSD M.2 pode funcionar, SATA ou NVMe.

Se você estiver procurando por um SSD M.2 de terceiros para seu thin client HP t740, recomendamos considerar o [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V) Ambas as opções são confiáveis e devem funcionar bem com o seu dispositivo. Se você quiser aproveitar os dois slots, precisará de ambos. Você sacrificará as velocidades do NVME, mas ganhará alguma redundância que é tão importante.

Observe que o autor deste artigo executou com êxito o pfSense CE 2.5.2 e o OPNsense 22.1 em seu t740 sem problemas após seguir as etapas acima.

## Solução de problemas e pós-instalação

Após a instalação, se você encontrar algum problema com a edição de arquivos, poderá instalar o editor nano usando `pkg update` e `pkg install nano` Isso ajudará você a editar arquivos de texto com facilidade.

Para garantir que as alterações feitas no `/boot/loader.conf.local` arquivo persistir nas atualizações de versão do pfSense, você precisa adicionar as seguintes linhas para `/boot/loader.conf` e `/etc/rc.conf.local` 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

No entanto, às vezes, a edição de `/boot/loader.conf.local` arquivo antes de reiniciar não corrige o problema. Nesses casos, pode ser necessário adicionar as seguintes linhas no início do primeiro boot:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Essas etapas devem resolver a maioria dos problemas que podem surgir durante e após o processo de instalação.

### Referências:
- [HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
- [pfSense](https://www.pfsense.org/)
- [OPNsense](https://opnsense.org/)
- [HardenedBSD](https://hardenedbsd.org/)
- [ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
- [FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)
---
title: "Executando o pfSense no HP t740 Thin Client: Guia de dicas e solução de problemas"
draft: false
toc: true
date: 2023-04-29
description: "Aprenda como configurar o pfSense no HP t740 Thin Client e como solucionar possíveis problemas, como congelamento e problemas de detecção de SSD."
tags: ["pfSense","OPNsense","BSD endurecido","HP t740","cliente magro","servidor doméstico","PPPoE","FreeBSD","prompt de inicialização","loader.conf.local", "editor nano","Detecção de SSD","SSD M.2","Digital Ocidental","solução de problemas","pós-instalação","UART","ESXi","Proxmox"]
cover: "/img/cover/A_cartoon_of_a_wizard_casting_a_spell_to_fix_a_frozen_computer.png"
coverAlt: "Um desenho animado de um mago lançando um feitiço para consertar um computador congelado, com um balão dizendo Problema resolvido"
coverCaption: ""
---
 pfSense, OPNsense ou HardenedBSD no HP t740 Thin Client**

Se você está procurando um dispositivo poderoso para executar pfSense, OPNsense ou HardenedBSD, o HP t740 Thin Client pode ser uma escolha adequada para você.

## Mais Potência e Servidor Doméstico Compacto

O HP t740 Thin Client é um dispositivo compacto que pode ser usado como uma poderosa caixa pfSense ou um servidor doméstico compacto. Ele oferece mais potência do que o t730 ou t620 Plus, o que o torna uma escolha adequada para executar PPPoE, especialmente se você tiver internet de fibra. Ele também pode oferecer um caminho de atualização para redes de 10 Gigabit.

## PS/2 Congela

No entanto, se você planeja executar o FreeBSD ou seus derivados como pfSense, OPNsense ou HardenedBSD no bare metal (ao contrário de dentro do ESXi ou Proxmox), você pode encontrar um problema em que o sistema congela na inicialização com a mensagem `atkbd0: [ GIANT-LOCKED]`. Felizmente, esse problema pode ser resolvido digitando os seguintes comandos no prompt de inicialização:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

*Note that you need to unset both, otherwise, it will still lock up at boot.*

After you install the OS, open a post-installation shell and run the following command:

```bash
vi /boot/loader.conf.local
```
Then, add these two lines:
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

### Persist Changes using VI
For those not familiar with vi, you can add the line by doing the following :

Adding the lines `hint.uart.0.disabled="1"` and `hint.uart.1.disabled="1"` to the `/boot/loader.conf.local` file using the vi editor can be done with the following steps:

1. Open the terminal on your FreeBSD system.

2. Type `vi /boot/loader.conf.local` and press Enter to open the file in the vi editor.

3. Press the `i` key to enter insert mode.

4. Move the cursor to the bottom of the file using the arrow keys.

5. Type `hint.uart.0.disabled="1"` without the quotes.

6. Press Enter to start a new line.

7. Type `hint.uart.1.disabled="1"` without the quotes.

8. Press the `Esc` key to exit insert mode.

9. Type `:wq` and press Enter to save and exit the file.

This will add the two lines to the `/boot/loader.conf.local` file, which will disable the UARTs and fix the freezing issue during boot on certain HP t740 "Thin Client" devices when running FreeBSD or its derivatives like pfSense, OPNsense, or HardenedBSD.

This will fix the issue across reboots and firmware upgrades on pfSense/OPNsense. 

## SSD

If you're using the HP M.2 eMMC, it will not be detected on an out-of-the-box FreeBSD installation. In that case, you will need a third-party M.2 SSD. Any M.2 SSD can work, SATA or NVMe. 

If you are looking for a third-party M.2 SSD for your HP t740 thin client, we recommend considering the [Western Digital 500GB WD Blue SN570 NVMe](https://amzn.to/44bFCBk) or the [Western Digital 500GB WD Blue SA510 SATA](https://amzn.to/3AEbd0V). Both of these options are reliable and should work well with your device. If you want to take advantage of both slots, you'll need both. You'll sacrifice the speeds of the NVME, but you'll gain some redundancy that's oh so important.

Note that the author of this article has successfully run pfSense CE 2.5.2 and OPNsense 22.1 on their t740 without any issues after following the above steps. 

## Troubleshooting and Post Install

After installation, if you encounter any issues with editing files, you can install the nano editor using `pkg update` and `pkg install nano`. This will help you edit text files with ease.

To ensure that the changes made to the `/boot/loader.conf.local` file persist across pfSense version upgrades, you need to add the following lines to `/boot/loader.conf` and `/etc/rc.conf.local`: 
```bash
hint.uart.0.disabled="1"
hint.uart.1.disabled="1"
```

However, sometimes the editing of `/boot/loader.conf.local` file before rebooting doesn't fix the issue. In such cases, it may be necessary to add the following lines at the beginning of the first boot:

```bash
unset hint.uart.0.at
unset hint.uart.1.at
```

Essas etapas devem resolver a maioria dos problemas que podem surgir durante e após o processo de instalação.

### Referências:
-[HP t740 "Thin Client"](https://www8.hp.com/us/en/thin-clients/t740.html)
-[pfSense](https://www.pfsense.org/)
-[OPNsense](https://opnsense.org/)
-[HardenedBSD](https://hardenedbsd.org/)
-[ServeTheHome](https://www.servethehome.com/hp-t740-thin-client-review/)
-[FreeBSD (or pfSense/OPNsense) on the HP t740 Thin Client](https://www.neelc.org/posts/hp-t740-freebsd/)
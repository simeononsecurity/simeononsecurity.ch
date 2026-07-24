---
title: "Guia Definitivo: Instalando o GrapheneOS no Seu Dispositivo Google Pixel"
draft: false
toc: true
date: 2023-05-21
lastmod: 2026-05-24
description: "Aprenda como instalar o GrapheneOS no seu dispositivo Google Pixel para maior privacidade e segurança usando o instalador web ou o método CLI."
tags: ["GrapheneOS", "Google Pixel", "privacidade", "segurança", "Android", "dispositivos móveis", "sistema operacional", "guia de instalação", "ROM personalizada", "focado em privacidade", "proteção de dados", "sistema seguro", "código aberto", "segurança do dispositivo", "recursos de privacidade", "dados pessoais", "privacidade móvel", "fastboot", "bootloader", "boot verificado", "Pixel 10", "Pixel 9"]
cover: "/img/cover/how-to-install-graphine-os.webp"
coverAlt: "Uma ilustração digital abstrata mostrando um smartphone Google Pixel conectado a um computador com cabo USB-C, rodeado por elementos gráficos coloridos representando transferência de dados e segurança."
coverCaption: ""
---

**Como Instalar o GrapheneOS no Seu Dispositivo Google Pixel**

O GrapheneOS é um sistema operacional de código aberto, focado em privacidade, baseado em Android. Ele oferece proteções de segurança e privacidade significativamente aprimoradas, tornando-o uma excelente escolha para quem se preocupa com privacidade e segurança de dados. Se você possui um dispositivo Google Pixel compatível e deseja migrar para o GrapheneOS, este guia cobre tanto o método recomendado de **instalador web** quanto o método tradicional de **linha de comando (CLI)**.

> **Dica:** Se tiver dificuldades com o processo de instalação, peça ajuda no [canal oficial de chat do GrapheneOS](https://grapheneos.org/contact#community). Antes de pedir ajuda, tente seguir o guia por conta própria e depois solicite ajuda com o que encontrar dificuldades.

## Pré-requisitos

### Requisitos de Hardware e Sistema

- Um computador com pelo menos **2 GB de memória livre** e **32 GB de espaço de armazenamento livre**.
- Um **cabo USB-C de alta qualidade** incluído com o dispositivo (ou um cabo USB-C para USB-A, se necessário). Evite hubs USB — conecte diretamente a uma porta traseira do desktop ou porta do laptop.
- A instalação a partir de uma máquina virtual **não é recomendada** devido à passagem USB não confiável.

> É uma boa prática atualizar seu dispositivo Pixel antes de instalar o GrapheneOS para ter o firmware mais recente. De qualquer forma, o GrapheneOS instala o firmware mais recente no início do processo de instalação.

### Sistemas Operacionais Oficialmente Suportados

#### Instalador Web

- Windows 10 / Windows 11
- macOS Sonoma (14), macOS Sequoia (15), macOS Tahoe (26)
- Arch Linux
- Debian 12 (bookworm), Debian 13 (trixie)
- Ubuntu 22.04 LTS, Ubuntu 24.04 LTS, Ubuntu 25.04
- Linux Mint 21 (siga as instruções do Ubuntu 22.04 LTS), Linux Mint 22 (siga as instruções do Ubuntu 24.04 LTS)
- Linux Mint Debian Edition 6 (siga as instruções do Debian 12)
- ChromeOS
- GrapheneOS
- Android 13, 14, 15 e 16 com certificação Play Protect

#### Método CLI

Todos os acima, exceto ChromeOS, GrapheneOS e Android (que só podem usar o instalador web).

Versões antigas sem suporte dessas plataformas também podem ser usadas, mas não são suportadas oficialmente. **Certifique-se de que seu sistema operacional está atualizado antes de prosseguir.**

### Navegadores Oficialmente Suportados (Apenas Instalador Web)

- **Chromium** (fora do Ubuntu — o pacote Snap deles não tem WebUSB funcionando)
- **Vanadium** (GrapheneOS)
- **Google Chrome**
- **Microsoft Edge**
- **Brave** (com Brave Shields desativado — limita o uso de armazenamento para evitar impressão digital)

> - No Android, **desative o modo desktop** no seu navegador. O modo desktop impede que o instalador web detecte o Android e solicite permissão de reconexão após reinicializações. Está habilitado por padrão em tablets grandes com 8 GB+ de RAM (ex.: Pixel Tablet).
> - Evite versões de navegadores Flatpak e Snap — elas causam problemas durante a instalação.
> - **Não** use o modo Incógnito/navegação privada — esses modos restringem o espaço de armazenamento necessário para extrair o pacote baixado.

### Dispositivos Suportados

Você precisa de um dos [dispositivos Pixel oficialmente suportados](https://grapheneos.org/faq#supported-devices). **Evite variantes de operadoras** — Pixels de operadoras têm um ID de operadora não nulo registrado na fábrica que desativa o desbloqueio do bootloader e da operadora. Obtenha um dispositivo neutro de operadora (desbloqueado).

---

## Ativando o Desbloqueio OEM

O desbloqueio OEM deve ser ativado no sistema operacional antes de prosseguir.

1. Vá para **Configurações → Sobre o telefone/tablet** e toque repetidamente em **Número da versão** até que o modo desenvolvedor seja ativado.
2. Vá para **Configurações → Sistema → Opções do desenvolvedor** e ative **Desbloqueio OEM**. Em alguns modelos com capacidade de operadora, isso requer uma conexão de internet ativa para que o SO de fábrica possa verificar que o dispositivo não foi vendido como bloqueado por operadora.

> **Nota do Pixel 6a:** O desbloqueio OEM não funcionará com a versão de fábrica do SO. Atualize para a versão de **junho de 2022** ou posterior via OTA e, em seguida, faça uma redefinição de fábrica para corrigir o desbloqueio OEM.

---

## Método de Instalação 1: Instalador Web (Recomendado)

O [Instalador Web do GrapheneOS](https://grapheneos.org/install/web) é a abordagem recomendada para a maioria dos usuários. Ele usa WebUSB diretamente no navegador — sem necessidade de instalar software.

### Passo 1: Contornar Bugs do fwupd (Somente Linux)

No Linux, o `fwupd` é conhecido por conectar-se incorretamente a dispositivos usando o protocolo fastboot, bloqueando o instalador. Pare-o antes de conectar seu dispositivo:

```bash
sudo systemctl stop fwupd.service
```

Isso não persiste após reinicializações.

### Passo 2: Configurar Regras udev (Somente Linux)

No Arch Linux:

```bash
sudo pacman -S android-udev
```

No Debian e Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Passo 3: Inicializar na Interface do Bootloader

Segure o botão **diminuir volume** enquanto o dispositivo inicializa (ligue-o com o botão pressionado ou reinicie e segure). O dispositivo deve exibir um **triângulo de aviso vermelho** e as palavras **"Fastboot Mode"** — não pressione o botão liga/desliga para ativar "Start."

### Passo 4: Conectar Seu Dispositivo

Conecte o dispositivo ao computador via USB. No Linux, reconecte o cabo se as regras udev não foram configuradas antes da primeira conexão.

> **Pixel Tablet:** Desconecte da base antes de conectar via USB — o tablet não pode usar ambos simultaneamente.

> **Windows:** O Windows 10/11 atual inclui um driver fastboot genérico para Pixel 4a (5G) e posteriores. Para Pixels mais antigos ou Windows desatualizado, instale o driver pelo Windows Update (procure em "Ver atualizações opcionais" → "LeMobile Android Device").

### Passo 5: Desbloquear o Bootloader

Acesse [https://grapheneos.org/install/web](https://grapheneos.org/install/web) e clique no botão **Unlock the bootloader**. Confirme no dispositivo usando os botões de volume para alternar a seleção e o botão liga/desliga para confirmar. **Isso apaga todos os dados.**

### Passo 6: Obter e Instalar Imagens de Fábrica

1. Clique em **Download release** para baixar as imagens de fábrica do seu dispositivo.
2. Clique em **Flash factory images** e aguarde a conclusão. Isso instalará automaticamente o firmware, reiniciará na interface do bootloader e instalará o SO. **Não interaja com o dispositivo até terminar.**

### Passo 7: Bloquear o Bootloader

Após a instalação, clique em **Lock the bootloader** no instalador web. Confirme no dispositivo. **Isso apaga todos os dados novamente** — bloquear o bootloader ativa o boot verificado completo.

---

## Método de Instalação 2: Linha de Comando (CLI)

### Passo 1: Abrir um Terminal

No Windows, abra uma janela do **PowerShell regular (não-administrador)**. Remova o alias legado do `curl`:

```powershell
Remove-Item Alias:Curl
```

### Passo 2: Instalar o fastboot

Você precisa do fastboot versão **≥ 35.0.1**.

**Arch Linux:**

```bash
sudo pacman -S android-tools
```

**Debian / Ubuntu** — os pacotes deles estão desatualizados. Use o pacote autônomo:

```bash
# Debian / Ubuntu
sudo apt install libarchive-tools
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-linux.zip
echo 'acfdcccb123a8718c46c46c059b2f621140194e5ec1ac9d81715be3d6ab6cd0a  platform-tools_r35.0.2-linux.zip' | sha256sum -c
bsdtar xvf platform-tools_r35.0.2-linux.zip
export PATH="$PWD/platform-tools:$PATH"
```

**macOS:**

```bash
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-darwin.zip
echo 'SHA256 (platform-tools_r35.0.2-darwin.zip) = 1820078db90bf21628d257ff052528af1c61bb48f754b3555648f5652fa35d78' | shasum -c
tar xvf platform-tools_r35.0.2-darwin.zip
export PATH="$PWD/platform-tools:$PATH"
```

**Windows:**

```powershell
curl -O https://dl.google.com/android/repository/platform-tools_r35.0.2-win.zip
(Get-FileHash platform-tools_r35.0.2-win.zip).hash -eq "2975a3eac0b19182748d64195375ad056986561d994fffbdc64332a516300bb9"
tar xvf platform-tools_r35.0.2-win.zip
$env:Path = "$pwd\platform-tools;$env:Path"
```

Verifique sua versão:

```bash
fastboot --version
# Esperado: fastboot version 35.0.2-12147458
```

### Passo 3: Configurar Regras udev (Somente Linux)

Arch Linux:

```bash
sudo pacman -S android-udev
```

Debian / Ubuntu:

```bash
sudo apt install android-sdk-platform-tools-common
```

### Passo 4: Contornar Bugs do fwupd (Somente Linux)

```bash
sudo systemctl stop fwupd.service
```

### Passo 5: Inicializar na Interface do Bootloader

Segure **diminuir volume** enquanto inicializa até o dispositivo mostrar **"Fastboot Mode"** com o triângulo de aviso vermelho.

### Passo 6: Conectar e Desbloquear o Bootloader

Conecte via USB e execute:

```bash
fastboot flashing unlock
```

Confirme no dispositivo (botões de volume para alternar, botão liga/desliga para confirmar). **Isso apaga todos os dados.**

### Passo 7: Instalar OpenSSH (para verificação de imagem)

macOS e Windows incluem OpenSSH por padrão.

Arch Linux:

```bash
sudo pacman -S openssh
```

Debian / Ubuntu:

```bash
sudo apt install openssh-client
```

### Passo 8: Baixar e Verificar Imagens de Fábrica

Baixe a chave de assinatura:

```bash
curl -O https://releases.grapheneos.org/allowed_signers
```

Conteúdo esperado:

```
contact@grapheneos.org ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIUg/m5CoP83b0rfSCzYSVA4cw4ir49io5GPoxbgxdJE
```

Baixe as imagens de fábrica (substitua `DEVICE_NAME` e `VERSION` pelos valores reais):

```bash
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip
curl -O https://releases.grapheneos.org/DEVICE_NAME-install-VERSION.zip.sig
```

Verifique a assinatura (Linux / macOS):

```bash
ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" \
  -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip
```

Windows:

```powershell
cmd /c 'ssh-keygen -Y verify -f allowed_signers -I contact@grapheneos.org -n "factory images" -s DEVICE_NAME-install-VERSION.zip.sig < DEVICE_NAME-install-VERSION.zip'
```

Saída esperada:

```
Good "factory images" signature for contact@grapheneos.org with ED25519 key SHA256:AhgHif0mei+9aNyKLfMZBh2yptHdw/aN7Tlh/j2eFwM
```

### Passo 9: Instalar Imagens de Fábrica

Extraia as imagens:

```bash
# Linux
bsdtar xvf DEVICE_NAME-install-VERSION.zip

# macOS / Windows
tar xvf DEVICE_NAME-install-VERSION.zip
```

Entre no diretório e execute o script de instalação:

```bash
cd DEVICE_NAME-install-VERSION

# Linux / macOS
bash flash-all.sh

# Windows
./flash-all.bat
```

Aguarde a conclusão. O processo cuida da instalação do firmware, reinicializações do bootloader e instalação do SO automaticamente. **Não interaja com o dispositivo até terminar.**

> **Solução para tmpfs no Linux:** Se `/tmp` não tiver espaço suficiente, use:
> ```bash
> mkdir tmp && TMPDIR="$PWD/tmp" ./flash-all.sh
> ```

### Passo 10: Bloquear o Bootloader

```bash
fastboot flashing lock
```

Confirme no dispositivo. **Isso apaga todos os dados novamente.** Bloquear ativa o boot verificado completo e impede que o fastboot modifique partições.

---

## Pós-Instalação

### Inicializando

Pressione o botão liga/desliga com a opção padrão **Start** selecionada na interface do bootloader para inicializar o GrapheneOS.

### Desativando o Desbloqueio OEM

Durante a configuração inicial, a tela final contém uma opção para desbloqueio OEM (marcada por padrão — deixá-la marcada **desativa** o desbloqueio OEM). Isso é recomendado. Você pode alterá-lo depois nas **Opções do desenvolvedor**.

### Verificando a Instalação

O GrapheneOS utiliza boot verificado e atestação de hardware. O boot verificado verifica todas as imagens de firmware e SO em cada inicialização usando chaves gravadas nos fusíveis do SoC. O GrapheneOS instala sua própria chave pública de boot verificado no elemento seguro — a cada inicialização, essa chave verifica o SO.

#### Hashes da Chave de Boot Verificado

Quando um SO alternativo é carregado, o dispositivo exibe um **aviso amarelo** com o identificador do SO (sha256 da chave de boot verificado). Pixels de 4ª e 5ª geração exibem apenas os primeiros 32 bits; **Pixels de 6ª geração em diante mostram o hash completo**. Compare com os hashes oficiais:

| Dispositivo | Hash da Chave de Boot Verificado |
|-------------|----------------------------------|
| Pixel 10a | `d8f879d10419eddc9fcda6280718be763f6bf12299e1f72df3ea8ad8a8eb7f80` |
| Pixel 10 Pro Fold | `55a2d44103e56d5ec65496399c417987ba77730e6488fc60ba058d09fc3caee3` |
| Pixel 10 Pro XL | `141d7fc32af7958a416f2661b37cf6f27bfb376fb5ce616aeaa27a82c7a04f74` |
| Pixel 10 Pro | `4e8ee8f717754052198ca6d2d3aaa232e2461b4293c0d6f297e519cc778de093` |
| Pixel 10 | `3f7415ea26f5df5b14ea6d153256071a7a1af9ce7b0970b7311cc463c7ea02c7` |
| Pixel 9a | `0508de44ee00bfb49ece32c418af1896391abde0f05b64f41bc9a2dfb589445b` |
| Pixel 9 Pro Fold | `af4d2c6e62be0fec54f0271b9776ff061dd8392d9f51cf6ab1551d346679e24c` |
| Pixel 9 Pro XL | `55d3c2323db91bb91f20d38d015e85112d038f6b6b5738fe352c1a80dba57023` |
| Pixel 9 Pro | `f729cab861da1b83fdfab402fc9480758f2ae78ee0b61c1f2137dd1ab7076e86` |
| Pixel 9 | `9e6a8f3e0d761a780179f93acd5721ba1ab7c8c537c7761073c0a754b0e932de` |
| Pixel 8a | `096b8bd6d44527a24ac1564b308839f67e78202185cbff9cfdcb10e63250bc5e` |
| Pixel 8 Pro | `896db2d09d84e1d6bb747002b8a114950b946e5825772a9d48ba7eb01d118c1c` |
| Pixel 8 | `cd7479653aa88208f9f03034810ef9b7b0af8a9d41e2000e458ac403a2acb233` |
| Pixel Fold | `ee0c9dfef6f55a878538b0dbf7e78e3bc3f1a13c8c44839b095fe26dd5fe2842` |
| Pixel Tablet | `94df136e6c6aa08dc26580af46f36419b5f9baf46039db076f5295b91aaff230` |
| Pixel 7a | `508d75dea10c5cbc3e7632260fc0b59f6055a8a49dd84e693b6d8899edbb01e4` |
| Pixel 7 Pro | `bc1c0dd95664604382bb888412026422742eb333071ea0b2d19036217d49182f` |
| Pixel 7 | `3efe5392be3ac38afb894d13de639e521675e62571a8a9b3ef9fc8c44fd17fa1` |
| Pixel 6a | `08c860350a9600692d10c8512f7b8e80707757468e8fbfeea2a870c0a83d6031` |
| Pixel 6 Pro | `439b76524d94c40652ce1bf0d8243773c634d2f99ba3160d8d02aa5e29ff925c` |
| Pixel 6 | `f0a890375d1405e62ebfd87e8d3f475f948ef031bbf9ddd516d5f600a23677e8` |

#### Atestação Baseada em Hardware com o Auditor

O GrapheneOS oferece o [aplicativo Auditor](https://attestation.app/) para verificar a integridade do hardware, firmware e SO usando boot verificado e atestação remota. Os resultados são exibidos em um segundo dispositivo Android com o Auditor (não no dispositivo sendo verificado), ou via o [serviço opcional de monitoramento de integridade do dispositivo](https://attestation.app/) para verificações automáticas agendadas com alertas por e-mail.

---

## Substituindo o GrapheneOS pelo SO de Fábrica

A instalação do SO de fábrica via [ferramenta de flash web da Google](https://flash.android.com/) é semelhante ao processo acima. Porém, antes de instalar e bloquear, você deve apagar a chave de boot verificado do GrapheneOS para reverter completamente ao SO de fábrica:

**Instalador web:** Use o botão "Erase non-stock key" no instalador web do GrapheneOS.

**CLI:**

```bash
fastboot erase avb_custom_key
```

Em seguida, instale as imagens de fábrica do SO de fábrica e bloqueie o bootloader.

---

## Conclusão

Instalar o GrapheneOS no seu dispositivo Google Pixel fornece recursos líderes do setor em privacidade e segurança. Use o **instalador web** em [grapheneos.org/install/web](https://grapheneos.org/install/web) para a experiência mais fácil, ou siga os passos da CLI acima para uma abordagem tradicional. Sempre bloqueie o bootloader após a instalação para ativar o boot verificado completo e, opcionalmente, use o aplicativo Auditor para confirmar a integridade da sua instalação.

## Referências

1. [Site do GrapheneOS](https://grapheneos.org/)
2. [Instalador Web do GrapheneOS](https://grapheneos.org/install/web)
3. [Guia de Instalação CLI do GrapheneOS](https://grapheneos.org/install/cli)
4. [Versões do GrapheneOS](https://grapheneos.org/releases)
5. [Guia de Uso do GrapheneOS](https://grapheneos.org/usage)
6. [FAQ do GrapheneOS](https://grapheneos.org/faq)
7. [Aplicativo Auditor](https://attestation.app/)
8. [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)

---
title: "Guia Definitivo: Instalando o sistema operacional Graphene em seu dispositivo Google Pixel"
draft: false
toc: true
date: 2023-05-21
description: "Saiba como instalar o Graphene OS em seu dispositivo Google Pixel para maior privacidade e segurança."
tags: ["Sistema operacional de grafeno", "Google Pixel", "privacidade", "segurança", "Android", "dispositivos móveis", "sistema operacional", "Guia de instalação", "ROM personalizado", "focado na privacidade", "Proteção de dados", "SO seguro", "Código aberto", "segurança do dispositivo", "recursos de privacidade", "dados pessoais", "privacidade móvel", "dados privados", "personalização do dispositivo", "tecnologia", "Instalação de pixels", "sistema operacional com foco na privacidade", "Instalação do Graphene OS", "segurança para celulares", "privacidade e segurança", "personalização do dispositivo pixel", "melhorias de privacidade", "guia de proteção de dados", "sistema operacional seguro", "Recursos de privacidade de pixel", "privacidade de dados móveis"]
cover: "/img/cover/A_colorful_cartoon_illustration_showcasing_a_Google_Pixel.png"
coverAlt: "Uma ilustração colorida de desenho animado mostrando um dispositivo Google Pixel com um escudo simbolizando recursos aprimorados de privacidade e segurança."
coverCaption: ""
---

**Como instalar o Graphene OS em seu dispositivo Google Pixel**

O Graphene OS é um sistema operacional de código aberto e focado na privacidade baseado na plataforma Android. Ele oferece recursos de segurança aprimorados e proteções de privacidade, tornando-o uma excelente escolha para pessoas preocupadas com a privacidade e segurança dos dados. Se você possui um dispositivo Google Pixel e deseja mudar para o Graphene OS, este artigo o guiará passo a passo pelo processo de instalação.

## Pré-requisitos

Antes de iniciar o processo de instalação, há alguns pré-requisitos que você precisa cumprir:

1. **Faça backup de seus dados**: a instalação do Graphene OS apagará todos os dados do seu dispositivo. Certifique-se de ter feito backup de todos os arquivos, fotos, contatos e outros dados importantes em um local seguro.

2. **Desbloqueie o gerenciador de inicialização**: O gerenciador de inicialização é um software que inicializa o sistema quando você liga o dispositivo. Desbloquear o bootloader permite que você instale um software personalizado como o Graphene OS. Cada dispositivo Google Pixel tem um processo específico para desbloquear o bootloader. Consulte a documentação oficial do modelo do seu dispositivo para saber como desbloqueá-lo.

- [Enabling OEM unlocking](https://grapheneos.org/install/cli#enabling-oem-unlocking)
- [How to unlock the Google Pixel 3 bootloader](https://www.androidauthority.com/unlock-pixel-3-bootloader-915961/)

3. **Carregue seu dispositivo**: Certifique-se de que seu dispositivo tenha carga de bateria suficiente antes de iniciar o processo de instalação. Uma bateria descarregada durante a instalação pode levar a erros ou interrupções.

## Instalando Graphene OS

Siga as etapas abaixo para instalar o Graphene OS no seu dispositivo Google Pixel:

______

### Passo 1: Baixe a imagem do Graphene OS

Visite o site oficial do Graphene OS em [https://grapheneos.org](https://grapheneos.org) and navigate to the [**Releases section**](https://grapheneos.org/releases) Escolha o arquivo de imagem apropriado para o seu modelo específico do Google Pixel e baixe-o para o seu computador.

______

### Etapa 2: verifique a imagem

Para garantir a integridade da imagem baixada, você deve verificar sua assinatura criptográfica. A documentação oficial do Graphene OS fornece instruções detalhadas sobre como verificar a imagem usando diferentes sistemas operacionais. Você pode encontrar a documentação [here](https://grapheneos.org/usage#verify-grapheneos-image)

______

### Etapa 3: ativar as opções do desenvolvedor e a depuração USB

1. No seu dispositivo Google Pixel, vá para o aplicativo Configurações.
2. Role para baixo e toque em "Sobre o telefone".
3. Toque em "Build number" sete vezes para habilitar as opções do desenvolvedor.
4. Volte para a página principal de Configurações e toque em "Opções do desenvolvedor".
5. Ative a depuração USB.

______

### Etapa 4: Conecte seu dispositivo ao computador

Use um cabo USB para conectar seu dispositivo Google Pixel ao computador.

______

### Etapa 5: inicialize seu dispositivo no modo Fastboot

Você deveria ter o [android development tools](https://www.xda-developers.com/install-adb-windows-macos-linux/) já instalado em sua máquina.

1. Abra um prompt de comando ou janela de terminal em seu computador.
2. Digite o seguinte comando para inicializar seu dispositivo no modo fastboot:

```bash
adb reboot bootloader
```

______

### Passo 6: Atualize a imagem do Graphene OS

1. Assim que seu dispositivo estiver no modo de inicialização rápida, use o seguinte comando para atualizar a imagem do Graphene OS em seu dispositivo:

```bash
fastboot flashall
```

Este comando apagará todos os dados existentes em seu dispositivo e instalará o Graphene OS.

2. Aguarde a conclusão do processo de flash.

______

### Etapa 7: reinicie seu dispositivo

Após a conclusão do processo de instalação, reinicie seu dispositivo digitando o seguinte comando:

```bash
fastboot reboot
```

______

### Etapa 8: configurar o Graphene OS

Siga as instruções na tela para configurar o Graphene OS em seu dispositivo Google Pixel. Leve o seu tempo para definir as configurações de acordo com suas preferências.

## Conclusão

A instalação do Graphene OS em seu dispositivo Google Pixel pode fornecer recursos aprimorados de privacidade e segurança. Seguindo as etapas descritas neste guia, você pode assumir o controle de seu dispositivo e proteger suas informações pessoais contra possíveis ameaças. Lembre-se de fazer backup de seus dados antes de prosseguir com a instalação e siga cuidadosamente cada etapa para garantir uma instalação bem-sucedida. Aproveite os benefícios de privacidade e segurança que o Graphene OS oferece!

## Referências

1. [Graphene OS Website](https://grapheneos.org/)
2. [Android Developer Website](https://developer.android.com/)
3. [Android Debug Bridge (ADB) Documentation](https://developer.android.com/studio/command-line/adb)
4. [Fastboot Documentation](https://developer.android.com/studio/releases/platform-tools#fastboot)
5. [Google Pixel Device Compatibility List](https://grapheneos.org/#devices)
6. [Google Developer Documentation - Unlocking the Bootloader](https://source.android.com/setup/build/running#unlocking-the-bootloader)
7. [Google Developer Documentation - Factory Images](https://developers.google.com/android/images)

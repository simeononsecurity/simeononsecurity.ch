---
title: "Atualização de firmware offline para Ubiquiti Unifi UDM Pro e UDM SE via linha de comando SSH"
draft: false
toc: true
date: 2023-05-28
description: "Aprenda como atualizar o firmware do Ubiquiti Unifi UDM Pro e UDM SE offline através da linha de comando SSH para desempenho e segurança ideais."
tags: ["Atualização de firmware Ubiquiti", "UDM Pro", "UDM SE", "atualização de firmware off-line", "linha de comando SSH", "Gerenciamento de rede", "segurança de rede", "Atualização do firmware", "conexão SSH", "arquivo de firmware", "Controlador de Rede UniFi", "correções de bugs", "melhorias de desempenho", "patches de segurança", "rede", "dispositivos de rede", "tecnologia", "Gerenciamento de TI", "processo de atualização de firmware", "otimização de rede", "Atualização de firmware Ubiquiti Networks", "Atualização de firmware do UDM Pro", "Atualização de firmware UDM SE", "processo de atualização de firmware off-line", "Atualização de firmware SSH", "gerenciamento de dispositivo de rede", "atualizações de segurança de rede", "estratégias de atualização de firmware", "gerenciamento de firmware off-line", "otimização de desempenho de rede", "gerenciamento de patches de segurança", "atualizações de tecnologia de rede"]
cover: "/img/cover/A_colorful_illustration_depicting_a_computer_connecting.png"
coverAlt: "Uma ilustração colorida representando um computador conectado a um roteador por meio de SSH, simbolizando o processo de atualização de firmware off-line para dispositivos Ubiquiti Unifi UDM Pro e UDM SE."
coverCaption: ""
---

**Atualize o Ubiquiti Unifi UDM Pro e UDM SE Offline através do SSH**

No mundo das redes, a **Ubiquiti Networks** ganhou reconhecimento por suas soluções inovadoras. O **Ubiquiti Unifi Dream Machine Pro (UDM Pro)** e o **Unifi Dream Machine SE (UDM SE)** são dois produtos populares que oferecem recursos abrangentes de gerenciamento de rede. Atualizar o firmware desses dispositivos é crucial para garantir desempenho e segurança ideais. Neste artigo, exploraremos como atualizar o firmware do UDM Pro e UDM SE **offline** usando SSH de linha de comando.

______

## Por que atualizar o firmware?

As atualizações de firmware são essenciais para qualquer dispositivo de rede, pois geralmente contêm correções de bugs, melhorias de desempenho e patches de segurança. Atualizar regularmente o firmware do seu UDM Pro e UDM SE é crucial para garantir que sua rede permaneça segura e funcione sem problemas.

______

## Atualização de firmware off-line

A atualização do firmware do UDM Pro e UDM SE pode ser feita através do **UniFi Dashboard**. No entanto, em alguns cenários, uma conexão com a Internet pode não estar disponível ou não ser desejável. Nesses casos, uma atualização offline usando SSH de linha de comando fornece uma solução alternativa.

______

## Preparando-se para a atualização offline

Antes de prosseguir com a atualização offline, verifique se você possui os seguintes pré-requisitos:

1. Um computador ou dispositivo com um cliente SSH instalado.
2. O arquivo de firmware mais recente para seu UDM Pro ou UDM SE. Você pode obter o arquivo de firmware do [Ubiquiti Downloads](https://www.ui.com/download/unifi) for the [UDM Pro](https://www.ui.com/download/unifi/unifi-dream-machine-pro) page. For early access firmwares, you can see them on the [community releases page](https://community.ui.com/releases) once you've signed into your.[**ui.com**](https://account.ui.com/) conta

______

## Estabelecendo conexão SSH

Para atualizar o UDM Pro ou o UDM SE por meio do SSH da linha de comando, siga estas etapas:

1. Certifique-se de que seu computador ou dispositivo esteja conectado à mesma rede que o UDM Pro ou UDM SE.
2. Abra seu cliente SSH preferido e estabeleça uma conexão SSH com o endereço IP **UDM Pro ou UDM SE**. Por exemplo, usando o **cliente OpenSSH** no Linux ou macOS, você pode usar o seguinte comando:

```bash
ssh root@<UDM_IP_ADDRESS>
```

Substituir `<UDM_IP_ADDRESS>` com o endereço IP real do seu UDM Pro ou UDM SE.

3. Insira o **nome de usuário** e a **senha** quando solicitado. As credenciais padrão para dispositivos Ubiquiti são geralmente `ubnt` tanto para o nome de usuário quanto para a senha.

______

## Atualizando Firmware

Depois de estabelecer a conexão SSH, você pode prosseguir com a atualização do firmware:

1. Carregue o arquivo de firmware para o UDM Pro ou UDM SE usando **SCP (cópia segura)**. O SCP permite a transferência segura de arquivos por SSH. Supondo que o arquivo de firmware esteja localizado em sua máquina local, você pode usar o seguinte comando:

```bash
scp <FIRMWARE_FILE_PATH> ubnt@<UDM_IP_ADDRESS>:/root/fwupdate.bin
```

Substituir `<FIRMWARE_FILE_PATH>` com o caminho para o arquivo de firmware em sua máquina local e `<UDM_IP_ADDRESS>` com o endereço IP do seu UDM Pro ou UDM SE.

2. Após o upload do arquivo de firmware, você pode iniciar o processo de atualização do firmware. Execute o seguinte comando:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "ubnt-tools fwupdate /root/fwupdate.bin"
```

3. O UDM Pro ou UDM SE iniciará o processo de atualização do firmware. Isso pode levar vários minutos. **Não interrompa o processo** até que a atualização seja concluída.

4. Após a conclusão da atualização, você pode verificar a versão do firmware fazendo login no UniFi Network Controller ou executando o seguinte comando:

```bash
ssh ubnt@<UDM_IP_ADDRESS> "show version"
```
Observe que o processo acima pressupõe que você tenha o arquivo de firmware necessário para o seu UDM Pro ou UDM SE. Certifique-se de ter o arquivo de firmware correto para o modelo e versão do seu dispositivo específico.

## Conclusão

Atualizar o firmware de seus dispositivos Ubiquiti Unifi UDM Pro e UDM SE é uma etapa crucial para garantir desempenho e segurança ideais. Embora o controlador de rede UniFi forneça uma maneira conveniente de atualizar o firmware, a execução de uma atualização offline por meio da linha de comando SSH oferece uma solução viável quando uma conexão com a Internet não está disponível ou não é desejável.

Seguindo as etapas descritas neste artigo, você pode atualizar com sucesso o firmware de seus dispositivos UDM Pro e UDM SE usando SSH de linha de comando. Lembre-se de sempre usar a versão mais recente do firmware fornecida pela Ubiquiti Networks para aproveitar as correções de bugs, melhorias de desempenho e patches de segurança.

## Referências

- [Ubiquiti Downloads](https://www.ui.com/download/unifi/) - Página oficial de downloads da Ubiquiti para arquivos de firmware.
- [Unifi Advanced Updating Techniques](https://help.ui.com/hc/en-us/articles/204910064-UniFi-Upgrade-the-Firmware-of-a-UniFi-Device)

---
title: "Bypassing the BGW-320: Using an Azores COTS ONT - A Step-by-Step Guide"
draft: false
toc: true
date: 2023-04-30
description: "Aprenda como contornar o BGW-320 e usar um COTS ONT feito pelos Açores para se conectar à rede do seu ISP com este guia fácil de seguir."
tags: ["COTS ONT","BGW-320","Açores","fibra","rede","XGS-PON","Ethernet","Passagem de IP","costumização","ISP","ID ont","Endereço MAC","ID do equipamento","versão da imagem","versão de hardware","telenet","aplicativo CLI","interface web","modo de configuração de fábrica","problemas de compatibilidade"]
cover: "/img/cover/A_cartoon_technician_holding_a_COTS_ONT_with_a_fiber_cable.png"
coverAlt: "Um técnico de desenho animado segurando um COTS ONT com um cabo de fibra ao fundo."
coverCaption: ""
---

## Como contornar o BGW-320 e usar um WAG-D20 da Azores

A maioria das pessoas com fibra tem duas maneiras de se conectar à Internet - fibra para um ONT, Ethernet para um gateway ou fibra diretamente para o gateway. Neste artigo, vamos focar-nos em como contornar o BGW-320 e usar um COTS ONT made by Azores.

### Aspectos tecnicos

O[Azores WAG-D20](https://cdn.shopifycdn.net/s/files/1/0280/5153/8029/files/Azores_Product_Specification_-_WAG-D20_v0.6.pdf?v=1604914153) is a XGS-PON ONU/ONT that comprises of a 10GE port along with a 2.5GE port even though it may be labeled on the device exterior as GE LAN. It may be acquired [here](https://www.balticnetworks.com/products/azores-1x-10gbe-1x-2-5gbe-intel-based-xgspon-ont)

{{< figure src="azores-wag-d20-xgs-pon-ont-front_225x225_crop_center.webp" alt="Azores WAG-D20" >}}

### Acesso ao dispositivo

O endereço IP padrão do dispositivo é 192.168.1.1 e seu endereço de Gateway tem um erro de digitação de fábrica usando um endereço IP público, ou seja, mostra 192.162.1.1 em vez de 192.168.1.1.

Depois de inicializar, você precisa pressionar Enter para obter um prompt de login na interface serial TTL (115200 8N1). Este dispositivo possui um sistema de imagem A/B com uma partição de sobreposição contendo todos os arquivos personalizados.
 
### Credenciais

- `admin`/`ADMIN123!@#` - Login de administrador para web GUI
- `Guest`/`welcome` - Login de convidado
- `test`/`default` - Login de fábrica

### Interface Ethernet

Conecte seu cliente à porta ethernet 10G e configure-o com um endereço na rede 192.168.1.x/24 como - 192.168.1.2/255.255.255.0.

Ao executar uma varredura de porta de 1-65535, você notará algumas portas abertas:

- Portas `23` e `8009` - Telnet, requer login, executa o aplicativo CLI.
- Porta `10002` - Desconhecido
- Porta `80` - WebUI, apenas duas funções

### Personalizando o ONT

{{< figure src="customizingtheont.png" alt="A BGW-320" >}}

Agora vem a parte importante, ou seja, alterar algumas informações do dispositivo para torná-lo compatível com a rede do seu ISP.

Primeiro, pegue as seguintes informações do seu ISP Gateway ou ONT:

1. **ID ONT**
2. **Endereço MAC**
3. **ID do equipamento**
4. **Versão da imagem**
5. **Versão do hardware**

Observação: esses são os valores OMCI e não os da interface do usuário da web.

Telnet para seu ONT pessoal (telnet 192.168.1.1), faça login como **`test`** usando a senha **`default`** e execute o comando 'test' para entrar no modo de configuração de fábrica.

Exiba os valores atualmente definidos com o comando 'show':

- `mostrar gpon mac`
- `mostrar sn`
- `mostrar id do equipamento`

Feito isso, personalize as configurações com os seguintes comandos, substituindo x pelos valores do seu dispositivo:

- `definir gpon mac xx:xx:xx:xx:xx:xx`
- `definir sn <inserir ID ONT aqui>`

Para HUMAX:

- `definir ID do equipamento “iONT320500G”`
- `config ONU-G_Version "BGW320-500_2.1”`

Para Nokia:

- `definir ID do equipamento “iONT320505G”`
- `config ONU-G_Version "BGW320-505_2.2”`

Nota: Os últimos dois comandos devem ser aplicados a partir do telnet logado como o usuário **`test`**.

### Reinicie e aproveite a verdadeira passagem de IP

Após a personalização, reinicie o ONT e aproveite a verdadeira passagem de IP.

### Solução de problemas e etapas adicionais
Para obter mais informações sobre este tópico, consulte o[8311 discord](https://discord.gg/XbTWBbSG4p) or the notes provided on [google docs](https://docs.google.com/document/d/13gucfDOf8X9ptkj5BOg12V0xcqqDZDnvROJpW5CIpJ4/)

### Conclusão

Seguindo estes passos pode-se ignorar com sucesso o BGW-320 e usar o COTS ONT feito pelos Açores para se conectar à rede do seu ISP. No entanto, tenha cuidado ao inserir comandos e certifique-se de substituir 'x' pelos valores do seu dispositivo corretamente, caso contrário, você pode enfrentar problemas de compatibilidade que podem resultar em falhas de conexão.



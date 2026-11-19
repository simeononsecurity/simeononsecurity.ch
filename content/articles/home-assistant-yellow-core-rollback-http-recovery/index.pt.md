---
title: 'Retorno do Home Assistant Core 2026.11 para 2026.10.4: corrigir a versão 3 do armazenamento HTTP'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Corrija o erro da versão 3 do armazenamento HTTP após o Home Assistant Core 2026.11 voltar para 2026.10.4 no
  Yellow. Inclui comandos protegidos e resultados verificados.
genre:
- Automação residencial
- Solução de problemas
tags:
- Home Assistant Yellow
- Home Assistant OS
- Retorno do Core 2026.11
- Core 2026.10.4
- Versão 3 do armazenamento HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Ilustração de uma placa de computador amarela, um link de configuração interrompido e um painel web restaurado
coverCaption: ''
---

Uma atualização malsucedida do Home Assistant Core 2026.11 fez meu Yellow CM4 voltar para 2026.10.4. O Yellow continuou acessível pela rede, mas deixou de exibir o painel. O retorno deixou um arquivo de configurações HTTP na versão de armazenamento 3.1, enquanto o Core 2026.10.4 aceita a versão 2.2. Preservei o arquivo, converti uma cópia com verificações rigorosas, restaurei o acesso HTTP e depois atualizei o Core para 2026.11.1.

<!--more-->

## Principais pontos

- **Confirme a incompatibilidade.** Compare o erro no log do Core com a versão instalada e a versão do armazenamento HTTP.
- **Preserve o arquivo.** Antes da recuperação, mantenha uma cópia sem alterações e um backup fora do dispositivo.
- **Verifique o resultado.** Confira o estado do Core, a porta de escuta salva, o painel e a versão instalada.

**Correção para este caso exato:** [Preserve o arquivo HTTP](#preserve-recovery-options), [crie e valide um candidato da versão 2.2](#apply-the-tested-fix-for-version-31), [instale-o depois de parar o Core](#apply-the-tested-fix-for-version-31) e [verifique o resultado da atualização](#verify-the-update-outcome). A conversão verifica os campos originais e para quando eles diferem. Não a aplique a um arquivo HTTP que não tenha sido inspecionado.

## Antes de começar

Você precisa de acesso físico a um Yellow CM4, um cabo de dados USB-C, um console serial funcional e um backup utilizável ou uma configuração preservada. O procedimento manual exige acesso ao shell do host e uma inspeção cuidadosa do JSON. Reserve pelo menos 30 minutos para diagnóstico e reparo. A inicialização do Core e a restauração de backups demoram mais em instalações grandes.

## Identifique a falha

O erro decisivo apareceu no log do Core:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

A versão antiga do Core não conseguiu carregar `http`. A interface e outros componentes que dependem de HTTP também falharam. Uma concessão do roteador e uma página Observer saudável não comprovavam acesso ao painel. [O problema #190583 do Home Assistant Core](https://github.com/home-assistant/core/issues/190583) documenta a mesma falha de retorno em várias instalações, inclusive no Yellow. [Meu comentário no problema](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) registra a recuperação testada neste Yellow e o estado final do Core.

**Causa da interrupção da web:** o Core 2026.11 gravou `.storage/http` no formato 3.1. O retorno restaurou o Core 2026.10.4, mas não um arquivo HTTP compatível. O Core 2026.10.4 rejeita a versão 3 do armazenamento. O perfil `intermediate_v6` salvo neste Yellow também não corresponde ao esquema antigo. Não se sabe por que a primeira atualização falhou e iniciou o retorno. Em 2026-11-15, o problema vinculado continuava aberto e a discussão não continha uma correção confirmada pelos mantenedores.

Confira a versão instalada do Core e o armazenamento HTTP antes de alterar arquivos:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

A saída abaixo representa este caso, com horários e detalhes privados removidos:

```text
2026.10.4
{
  "version": 3,
  "minor_version": 1,
  "pending_present": false,
  "profile": "intermediate_v6"
}
Storage file http has version 3 which is newer than the max supported version 2
```

Os comandos de recuperação abaixo comparam a porta de escuta salva pelo Supervisor com o arquivo HTTP sem exibir nenhum dos dois valores. Se houver diferença, confira a porta de escuta real do Core antes de alterar arquivos.

| Sinal | Significado |
| --- | --- |
| O Core aceita a versão 2 do armazenamento, mas o arquivo informa a versão 3 | A versão antiga não consegue carregar as configurações HTTP salvas |
| O arquivo HTTP e a lista do Supervisor mostram portas de escuta diferentes | Confira a porta de escuta real do Core antes de atribuir a causa |
| A página inicial responde, mas o estado do Core continua STARTING | A resposta da interface não comprova que a inicialização terminou |

## Mantenha as opções de recuperação {#preserve-recovery-options}

Mantenha um backup utilizável fora do Yellow antes de outra atualização. [O guia de backup do Home Assistant](https://www.home-assistant.io/common-tasks/general/backups/) descreve locais na nuvem e fora do dispositivo. Um backup criptografado precisa da chave de recuperação correspondente. Não apague o disco de dados NVMe durante o diagnóstico desta incompatibilidade de armazenamento.

Copie o arquivo HTTP antes de editá-lo:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Pare se o comando falhar. Deixe intacta uma cópia de recuperação anterior com o mesmo nome. Escolha um nome novo e repita a verificação antes de continuar.

Se o painel estiver indisponível, use o console serial do Yellow. [O guia da Nabu Casa para Linux e macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) mostra a conexão USB-C e a posição da UART JP1. Siga as instruções do CM4 para o seu hardware.

## Aplique a correção testada para a versão 3.1 {#apply-the-tested-fix-for-version-31}

A opção preferida é usar um arquivo HTTP compatível de antes da atualização. Restaure o backup pelo processo documentado do Home Assistant quando uma restauração completa for adequada. Se extrair um único arquivo, confirme a versão de armazenamento e a porta de escuta salva antes de substituir o arquivo ativo. Os comandos abaixo são a correção direta testada neste Yellow quando não havia um arquivo HTTP compatível disponível.

[A solução alternativa original do problema](https://github.com/home-assistant/core/issues/190583) move `.storage/http` para outro local e deixa a versão antiga do Core criar um arquivo novo. Um [relato posterior do Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) mostra uma porta de escuta diferente no arquivo recriado. Confira o arquivo novo e `ha core info` antes de concluir que a interface web foi corrigida.

Minha instalação não tinha um bloco YAML `http:`, uma configuração HTTP pendente, nem certificado ou chave TLS nas configurações estáveis. O perfil salvo era `intermediate_v6`. Nesse caso específico, criei um candidato separado da versão 2.2 e mantive a porta de escuta existente:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage

expected=$(ha core info --raw-json | jq -r '.data.port') &&
stored=$(jq -r '.data.stable.server_port' "$storage/http") &&
test -n "$expected" &&
test "$expected" != null &&
test "$expected" = "$stored" &&
test ! -e "$storage/http.v2-candidate" &&
jq -e '
  if .version == 3 and .minor_version == 1 and
     .data.pending == null and
     .data.stable.ssl_profile == "intermediate_v6" and
     (.data.stable | has("ssl_certificate") | not) and
     (.data.stable | has("ssl_peer_certificate") | not) and
     (.data.stable | has("ssl_key") | not) and
     (.data.stable | has("trusted_proxies") | not) and
     (.data.stable | has("use_x_forwarded_for") | not)
  then .version = 2 | .minor_version = 2 | .data.stable.ssl_profile = "intermediate"
  else error("Unexpected HTTP config. Stop and inspect")
  end
' \
  "$storage/http" > "$storage/http.v2-candidate" &&

jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&

test "$(jq -r '.data.stable.server_port' "$storage/http")" = \
  "$(jq -r '.data.stable.server_port' "$storage/http.v2-candidate")"
```

Todos os comandos acima precisam ser concluídos com êxito antes de substituir o arquivo ativo. Se `jq` falhar, inspecione o arquivo candidato antes de removê-lo e tentar novamente. [O código HTTP do Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) define a versão 2.2 do armazenamento e aceita o perfil `intermediate`. [O código do Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) usa a versão 3.1 e nomes de perfil versionados. Também validei o candidato com `HTTP_STORAGE_SCHEMA` do Core antigo instalado antes de instalá-lo.

Execute a verificação do esquema do Core antigo instalado enquanto o contêiner ainda estiver em execução:

```bash
docker exec homeassistant python3 -c '
import json
from homeassistant.components.http.config import HTTP_STORAGE_SCHEMA
with open("/config/.storage/http.v2-candidate") as source:
    data = json.load(source)
stable = {
    key: value for key, value in data["data"]["stable"].items()
    if key not in ("created_at", "error", "error_message")
}
HTTP_STORAGE_SCHEMA(stable)
print("Schema accepted")
'
```

Pare se o esquema rejeitar o candidato. Esta etapa não valida todas as integrações nem todos os formatos não testados do armazenamento HTTP.

A verificação do esquema exibiu `Schema accepted` para este candidato. Qualquer outro resultado interrompe este procedimento de recuperação.

Esta conversão manual foi testada para os campos indicados. Um arquivo com configurações TLS, proxies confiáveis ou uma configuração pendente exige análise própria. Alterar somente o número da versão principal deixa um perfil que o Core antigo não aceita.

O Supervisor tinha uma tarefa Core ativa e, no meu caso, rejeitou `ha core stop`. Parei o contêiner do Core pelo console do host, instalei o candidato validado e iniciei o contêiner:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
jq -e '.version == 2 and .minor_version == 2 and .data.pending == null and .data.stable.ssl_profile == "intermediate"' \
  "$storage/http.v2-candidate" >/dev/null &&
  docker stop homeassistant &&
  test "$(docker inspect -f '{{.State.Running}}' homeassistant)" = false &&
  cmp -s "$storage/http" "$storage/http.before-recovery" &&
  mv "$storage/http.v2-candidate" "$storage/http" &&
  docker start homeassistant
```

Se um comando falhar depois da parada, inspecione o arquivo HTTP ativo antes de executar `docker start homeassistant`. Se o arquivo tiver mudado, crie outro candidato com base no conteúdo atual. A página HTTP voltou depois desta etapa. Uma resposta HTTP, por si só, não comprovava que o Core havia terminado de iniciar, então verifiquei o estado do Supervisor antes de considerar o sistema recuperado.

Neste Yellow, `docker inspect -f '{{.State.Status}}' homeassistant` mostrou `running`. Confira `ha core info` e o painel antes de solicitar outra atualização.

## Verifique o resultado da atualização {#verify-the-update-outcome}

Depois que o acesso HTTP voltou, atualizei o Core para 2026.11.1. Para solicitar essa versão:

```bash
ha core update --version 2026.11.1
```

O comando informou uma falha após uma inicialização longa. Em seguida, o Supervisor registrou o Core como RUNNING e `Successfully started Home Assistant 2026.11.1`. Uma consulta de estado mostrou que a versão instalada era a atual, o arquivo HTTP havia migrado novamente para a versão 3.1 e o contêiner não reiniciou durante a observação. O painel autenticado carregou. **Confira o estado final mesmo quando o comando de atualização informar uma falha.**

No seu sistema, confira a versão, a integridade do Supervisor e o estado do contêiner após uma atualização longa:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

Neste caso, o primeiro e o terceiro comandos produziram os resultados sanitizados abaixo:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Depois, abra o painel pelo endereço local habitual e confirme que os estados atuais carregam. Mantenha o arquivo HTTP salvo até que outro backup seja concluído e o funcionamento normal seja confirmado.

As evidências do meu Yellow não estabeleceram a causa da primeira falha de atualização. A mensagem de falha da tarefa posterior também não indicou uma causa. Uma versão instalada e um painel funcional comprovam melhor o estado resultante do que a mensagem de CLI sozinha, mas nenhum dos dois explica por que o Supervisor marcou a tarefa como falha.

## Próximas etapas

Se o erro do armazenamento HTTP persistir, inspecione o arquivo preservado e restaure um backup compatível ou execute uma versão do Core capaz de ler a versão do armazenamento. Restaurar o arquivo preservado versão 3 no Core antigo repetirá a falha. Se o Core chegar a RUNNING, mas alguns dispositivos continuarem indisponíveis, investigue essas integrações separadamente. Guarde a cópia de recuperação e o backup na nuvem até que o próximo backup seja concluído e o painel continue respondendo.

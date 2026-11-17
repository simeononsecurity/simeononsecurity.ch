---
title: "Teste de restauração de VM Proxmox: comprove que o sistema convidado funciona"
date: 2026-10-11
lastmod: 2026-11-15
toc: true
draft: false
description: "Teste um backup de VM Proxmox com uma restauração isolada. Verifique os discos incluídos, o modo de backup, os dados do convidado, o estado do serviço e o tempo de recuperação sem tocar na produção."
genre: ["Virtualização", "Backup e recuperação", "Laboratório doméstico"]
tags: ["teste de restauração Proxmox", "backup de VM Proxmox", "exercício de restauração Proxmox", "qmrestore", "vzdump", "verificação do Proxmox Backup Server", "backup por snapshot Proxmox", "teste de recuperação de VM", "RPO e RTO de backup", "restauração isolada de VM", "modo de backup Proxmox", "backup com agente convidado"]
cover: "/img/cover/proxmox-vm-backup-restore-drill.webp"
coverAlt: "Um backup passa de uma VM de produção laranja por um cofre de armazenamento até uma VM de teste isolada azul. O processo verifica discos, serviços e tempo."
coverCaption: "A conclusão de uma tarefa de backup marca o início de um teste de recuperação."
---

Uma tarefa de backup verde informa que o Proxmox gravou um backup. Ela não mostra se o convidado inicializa, se os dados estão atualizados ou se o serviço principal funciona. **Restaure uma cópia com um novo ID de VM em uma rede isolada.** O resultado fornece evidências de recuperação antes que uma interrupção force o teste.

<!--more-->

Este exercício cobre uma **máquina virtual Proxmox VE**. Os containers têm regras de backup diferentes, principalmente para montagens bind e de dispositivos. O [teste de backup e restauração do homelab](/articles/homelab-backup-restore-drill/) do site trata da recuperação de arquivos em um escopo maior. Aqui, você testará um backup de VM Proxmox e sua carga de trabalho.

Um **convidado** é o sistema operacional que funciona dentro de uma máquina virtual. **Montagens bind** e **montagens de dispositivos** expõem recursos do host ao convidado. Teste esses recursos por meio de um plano de recuperação separado.

## Principais pontos

- **Defina o sucesso primeiro:** escolha um dado, uma verificação do serviço e um tempo de recuperação aceitável.
- **Confira a cobertura:** um backup de VM ignora discos marcados como **No backup** e não recria serviços externos ou dados excluídos.
- **Restaure em separado:** use um ID de VM não utilizado e mantenha a rede restaurada isolada da produção.
- **Registre evidências:** meça a idade do backup, o tempo de restauração, a inicialização, a presença dos discos e uma verificação real da aplicação.

## Antes de começar

Escolha uma VM cujo backup seja seguro para testar. Você precisa de acesso de administrador ao Proxmox, um backup concluído em armazenamento de arquivos ou Proxmox Backup Server (PBS), espaço suficiente para uma segunda VM e uma bridge isolada ou um dispositivo de rede desconectado. Uma bridge isolada é uma rede virtual Proxmox sem rota para a LAN de produção. Use um adaptador desconectado ou uma VLAN de teste se não tiver uma bridge assim. Mantenha a VM de produção em execução. Reserve um ID de VM novo, como **920**, depois de verificar se outro convidado usa esse ID. Reserve tempo suficiente para uma restauração completa e um teste da carga de trabalho.

Escreva os critérios de aprovação antes de restaurar. Para um servidor de arquivos, escolha um arquivo recente e seu checksum ou conteúdo esperado. Para um banco de dados, escolha uma consulta de leitura segura e um registro criado antes do backup. Para um serviço Web, escolha uma verificação de integridade local e uma página representativa. Registre a data mais recente aceitável dos dados, seu **objetivo de ponto de recuperação (RPO)**, e o tempo permitido para recuperar o serviço, seu **objetivo de tempo de recuperação (RTO)**. Uma tela de inicialização sozinha não atende a essas verificações.

| Registro | Exemplo de evidência |
|---|---|
| **Ponto do backup** | Hora do snapshot e último dado esperado |
| **Destino da recuperação** | ID de VM não usado, armazenamento de destino e bridge isolada |
| **Teste da carga** | Login, montagem do volume e leitura pela aplicação |
| **Limite de tempo** | Horários de início e fim da restauração e da verificação do serviço |

Não conecte o convidado restaurado à rede de produção antes de conferir nome, endereço IP, endereço MAC, tarefas agendadas e integrações externas. Uma identidade copiada pode entrar em conflito com a VM em execução ou enviar tarefas duplicadas.

## Confira o que a cópia de segurança cobre

**Escopo das versões:** estes exemplos não foram executados durante a preparação do artigo. Registre a saída de `pveversion --verbose` antes de testar. Use a documentação correspondente à versão instalada do Proxmox VE. Registre o backend de armazenamento, o tipo de convidado e a saída dos comandos no relatório do exercício.

Em um nó Proxmox, o comando somente leitura a seguir mostra a configuração da VM de origem. Substitua **120** pelo ID da sua VM de origem:

```bash
qm config 120
```

Liste cada disco virtual e sua configuração de backup. A [documentação de discos de VM do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qm.adoc) informa que a opção **No backup** exclui um disco do backup da VM. Confira se os dados da aplicação ficam em um disco excluído, uma montagem do host, hardware passado diretamente ou um serviço remoto. Registre o procedimento de recuperação separado. Um teste de inicialização da VM não prova que os dados excluídos estejam protegidos.

Confira o horário, tamanho, registro da tarefa e local de armazenamento do backup mais recente. Na interface Proxmox, abra a visualização **Backups** do armazenamento de backup ou a guia **Backup** da VM. Confirme que a tarefa terminou sem erros. A [documentação de backup do Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) diferencia arquivos de backup regulares do armazenamento PBS, que mantém blocos e metadados deduplicados.

| Modo de backup | Comportamento da VM | Decisão para este exercício |
|---|---|---|
| **Snapshot** | Faz backup de uma VM em execução com pouca interrupção. As gravações do convidado trazem um pequeno risco de inconsistência. | Adequado para testes de rotina quando a carga tolera esse ponto de recuperação. |
| **Stop** | Desliga o convidado no início do backup e oferece a maior consistência. | Use quando a carga exigir um desligamento limpo e o tempo parado for aceitável. |
| **Suspend** | Suspende o convidado antes do modo snapshot e adiciona tempo parado sem benefício geral de consistência. | Não escolha suspend como melhoria padrão em relação a snapshot. |

Essas compensações constam na [referência dos modos de backup do Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Um **QEMU Guest Agent** é um serviço dentro do convidado que permite ao Proxmox solicitar ações como congelar e descongelar o sistema de arquivos. Um convidado em execução, com o agente habilitado e saudável, dá suporte a essas ações durante um backup snapshot. Congelar o sistema de arquivos melhora a consistência, mas não substitui uma verificação de recuperação específica do banco de dados. Registre o modo real e o estado do agente em vez de supor que uma tarefa agendada usa as configurações desejadas.

## Crie ou selecione um ponto de recuperação

Use um backup agendado recente e bem-sucedido se o exercício testar a recuperação de rotina. Se precisar de um backup novo e pontual, abra a guia **Backup** da VM, escolha **Backup now**, defina o armazenamento de destino e o modo e aguarde o registro da tarefa indicar sucesso. Em um shell Proxmox, este exemplo faz backup da VM **120** no armazenamento de ID **backup-nfs** em modo snapshot:

```bash
vzdump 120 --storage backup-nfs --mode snapshot
```

Substitua os dois IDs pelos seus. Execute o comando somente depois de confirmar que o armazenamento aceita backups e tem espaço para a tarefa. A [referência do `vzdump` do Proxmox](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc) documenta as opções de modo e armazenamento. Confira o registro da tarefa quando o comando terminar. Não trate um backup antigo como ponto de recuperação atual apenas porque o nome do arquivo parece recente.

Se o destino for **PBS**, execute ou inspecione uma tarefa de verificação para o datastore escolhido. A [documentação de verificação do PBS](https://pbs.proxmox.com/docs/maintenance.html) explica como verificar a integridade dos dados de backup e agendar verificações repetidas. A verificação encontra blocos danificados. **Uma verificação limpa não prova que um sistema operacional restaurado, uma aplicação ou uma dependência externa funcione.** Continue com o exercício de restauração mesmo depois de um resultado limpo.

## Restaure em uma VM isolada

Na interface Proxmox, selecione o backup na visualização **Backups** do armazenamento e escolha **Restore**. Informe um ID de VM não usado e o armazenamento de destino previsto. Deixe **Start after restore** desativado. Confira a opção de gerar um novo endereço MAC. A [sinopse oficial de `qmrestore`](https://github.com/proxmox/pve-docs/blob/master/generated/qmrestore.1-synopsis.adoc) define um ID de VM exclusivo, a escolha do armazenamento, `--unique` para um endereço Ethernet aleatório e o padrão de não iniciar a VM restaurada.

Para um arquivo `vzdump`, este comando shell mostra o padrão equivalente. Substitua o caminho do arquivo, o novo ID de VM e o ID de armazenamento por valores do seu ambiente:

```bash
qmrestore /path/to/vzdump-qemu-120-2026_10_11-02_00_00.vma.zst 920 --storage local-lvm --unique 1
```

A [descrição de restauração do Proxmox](https://github.com/proxmox/pve-docs/blob/master/qmrestore.adoc) diz que, sem armazenamento de destino, a restauração tenta usar o armazenamento original. Defina **`--storage`** se o armazenamento antigo não existir no nó de teste. Não use **`--force`** em um exercício. A opção permite sobrescrever uma VM existente, enquanto este procedimento exige um ID não usado. Os backups PBS também são restaurados pela interface Proxmox. Selecione a entrada de armazenamento do snapshot PBS em vez de tratá-lo como um arquivo `.vma.zst` local.

Antes da primeira inicialização, inspecione cada interface de rede restaurada, inclusive interfaces secundárias e passadas diretamente. Um **endereço MAC** identifica uma interface de rede. **DNS** associa nomes a endereços. **DHCP** atribui configurações de rede. Uma **VLAN** é uma rede lógica transportada em hardware compartilhado. Um **TPM virtual** armazena o estado de segurança de um convidado. Desconecte cada interface ou conecte-a somente a um segmento de teste isolado. Confirme que nenhuma rota de produção, caminho DNS, serviço DHCP, rede de gerenciamento ou integração externa permanece acessível. Se a carga precisar de outro serviço de teste, disponibilize uma cópia na rede isolada. Compare com a origem o mapeamento dos discos, o firmware, os requisitos do TPM virtual e os dispositivos especiais. Discos externos, dispositivos passados diretamente e segredos armazenados fora da VM precisam de planos separados.

## Teste o convidado e a carga de trabalho

Inicie a VM restaurada e use primeiro o console. Confirme que o sistema operacional inicia, todos os volumes esperados são montados, o relógio está correto e a aplicação inicia. Depois execute o critério de aprovação definido antes. Compare um dado conhecido com seu valor e horário anteriores ao backup. Uma tela de login ou um processo em execução não mostra, por si só, que o serviço contém os dados corretos.

| Teste | Critério de aprovação |
|---|---|
| **Inicialização** | O convidado chega a um login normal sem modo de reparo ou solicitações de recuperação repetidas. |
| **Discos** | Cada disco incluído no backup aparece, é montado e contém os dados esperados. |
| **Serviço** | Uma solicitação local representativa ou leitura é concluída com sucesso. |
| **Ponto de recuperação** | Os dados restaurados atendem ao RPO registrado. |
| **Tempo de recuperação** | Restauração, inicialização e validação do serviço atendem ao RTO registrado. |
| **Isolamento** | Nenhum endereço, tarefa ou integração de produção recebe tráfego duplicado. |

Mantenha o convidado restaurado isolado enquanto inspeciona tarefas agendadas, hooks de notificação, agentes de backup e credenciais da aplicação. Não execute um teste que envie mensagens reais a clientes ou grave em serviços de produção. Se uma verificação falhar, registre a etapa exata. Diferencie **falha de integridade do backup**, **falha de inicialização da VM**, **dados ausentes** e **falha da aplicação**. Cada uma exige uma correção diferente.

| Tipo de falha | Evidência de confirmação | Primeira correção | Novo teste |
|---|---|---|---|
| **Integridade do backup** | A verificação ou restauração informa dados danificados | Selecione outro ponto de recuperação verificado e inspecione a integridade do armazenamento | Repita a verificação e a restauração |
| **Inicialização da VM** | O console mostra erros de firmware, disco ou recuperação | Compare firmware, mapeamento dos discos e ordem de inicialização com a origem | Inicie a cópia isolada e registre o resultado do console |
| **Dados ausentes** | Falta um arquivo, volume ou registro esperado | Confira discos excluídos, montagens, snapshots e dependências externas | Repita a verificação do arquivo ou dado indicado |
| **Aplicação** | O convidado inicia, mas o teste do serviço falha | Inspecione logs do serviço, credenciais, dependências e etapas de recuperação | Execute a mesma verificação local de estado e o teste da carga |

O Proxmox oferece [restauração de arquivos individuais para backups PBS](https://github.com/proxmox/pve-docs/blob/master/vzdump.adoc). Use-a para testar um caminho de recuperação de arquivo quando sua carga precisar disso. Um arquivo recuperado não substitui a inicialização completa da VM e o teste do serviço. O Proxmox também oferece restauração ao vivo do PBS. A documentação diz que uma restauração ao vivo com falha deixa a VM em estado indefinido. Para este exercício planejado, use uma restauração normal concluída.

## Registre o resultado e encerre o exercício

Registre o ID da VM de origem, o armazenamento do backup, o horário do backup, o modo, o novo ID de VM, o armazenamento de destino, o isolamento de rede, os horários de início e fim da restauração, o teste da aplicação, o horário dos dados e as verificações que falharam. Compare o ponto e o tempo de recuperação medidos com seus objetivos. Uma falha só é evidência útil se você mudar o plano de backup e repetir o exercício.

Desligue a VM restaurada quando o teste terminar. Remova a cópia de teste somente depois de salvar o resultado e confirme que a VM de produção continua funcionando como esperado. Mantenha o backup segundo sua política normal de retenção. Não altere a retenção apenas para fazer um único exercício passar.

Repita o teste depois de mudanças importantes no armazenamento, no convidado ou na configuração de backup. Alterne entre VMs importantes, inclusive convidados com discos excluídos ou dependências externas. O [guia de migração do Hyper-V para o Proxmox](/articles/hyper-v-to-proxmox-migration-checklist/) usa essa comprovação de recuperação antes de desativar uma VM de origem. **Um backup utilizável tem um caminho de restauração conhecido, uma carga testada e um ponto de recuperação medido.**

## Próximas etapas

Repita o exercício depois de mudanças no armazenamento, no convidado ou no backup. Consulte o [teste de backup e restauração do homelab](/articles/homelab-backup-restore-drill/) para recuperação de arquivos.

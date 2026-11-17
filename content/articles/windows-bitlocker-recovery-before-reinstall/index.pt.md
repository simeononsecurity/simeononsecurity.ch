---
title: "Encontre a chave de recuperação do BitLocker antes de reinstalar o Windows"
date: 2026-10-10
lastmod: 2026-11-15
toc: true
draft: false
description: "Encontre e verifique a chave de recuperação correta do BitLocker, proteja uma cópia separada e escolha o caminho adequado de recuperação ou reinstalação do Windows antes de apagar uma unidade."
genre: ["Segurança do Windows", "Recuperação de dados", "Administração de sistemas"]
tags: ["chave de recuperação do BitLocker", "reinstalar o Windows 11", "reinstalar o Windows 10", "Criptografia do dispositivo", "ID da chave de recuperação", "chave de recuperação da conta Microsoft", "chave de conta corporativa ou escolar", "backup da chave de recuperação", "unidade criptografada", "instalação limpa", "recuperação do Windows", "backup do BitLocker", "chave de recuperação de 48 dígitos", "mídia de instalação do Windows", "backup de dados", "criptografia de unidade", "lista de recuperação", "instalação do Windows", "solução de problemas do BitLocker", "preparação para reinstalação"]
cover: "/img/cover/windows-bitlocker-recovery-before-reinstall.webp"
coverAlt: "Um notebook com uma unidade bloqueada, um cartão separado com a chave de recuperação, um backup USB e uma lista de recuperação marcada."
coverCaption: "Verifique a chave de recuperação antes de apagar a unidade."
---

Uma instalação limpa do Windows apaga a unidade selecionada. Se a unidade antiga usar **BitLocker** ou **Criptografia do dispositivo**, encontre a chave de recuperação e copie seus arquivos antes de começar. A chave dá acesso aos dados criptografados antigos. Uma nova instalação do Windows não restaura arquivos apagados da unidade.

<!--more-->

## Principais pontos

- **Encontre a chave correta:** compare o ID mostrado pelo Windows com a chave na sua conta, em uma impressão ou em um backup USB.
- **Teste o acesso:** examine o backup, confira o ID e desbloqueie uma unidade bloqueada antes de apagar partições.
- **Proteja o backup:** guarde a chave de 48 dígitos separada do computador e do USB de instalação.
- **Escolha o caminho:** use as opções de recuperação se precisar da instalação antiga. Faça uma instalação limpa somente depois de verificar uma cópia separada dos arquivos.

## Antes de começar

Você precisa acessar o computador afetado, usar um segundo dispositivo para consultar sua conta ou backup e ter uma unidade externa ou armazenamento em nuvem confiável para arquivos importantes. **Tempo:** localizar a chave depende do acesso à conta. Copiar arquivos depende do volume de dados. **Dificuldade:** básica para consultar a conta, intermediária para usar ferramentas de recuperação. Este guia cobre a preparação e as decisões de recuperação para Windows 10 e Windows 11. O [guia de instalação limpa do Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) explica a mídia e a configuração.

*O suporte padrão do Windows 10 terminou em 14 de outubro de 2025. Planeje instalar uma versão compatível do Windows 11 se o dispositivo atender aos requisitos. A Microsoft lista o [ciclo de vida do Windows 10 e opções de suporte estendido](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-10-end-of-support).*

> **Aviso:** não exclua uma partição para resolver um pedido de recuperação do BitLocker se ainda precisar dos arquivos da instalação antiga. A Microsoft informa que uma redefinição sem a chave remove esses arquivos. Consulte as [orientações da Microsoft sobre chaves de recuperação](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key).

## Verifique se a criptografia está ativa

A **Criptografia do dispositivo** e o **BitLocker** criptografam uma unidade para impedir que alguém sem as credenciais corretas leia o conteúdo. Se o Windows ainda iniciar, no Windows 11 abra **Configurações > Privacidade e segurança > Criptografia do dispositivo**. Nas edições com gerenciamento do BitLocker, pesquise no menu Iniciar por **Gerenciar BitLocker**. Anote a letra da unidade criptografada e a conta usada para configurar o dispositivo. Em um equipamento corporativo ou escolar gerenciado, a organização costuma guardar a chave.

Você também pode consultar o estado pela linha de comando. Pesquise no menu Iniciar por **Prompt de Comando**, selecione **Executar como administrador** e digite estes comandos. Troque `C:` se o Windows usar outra letra. Um **protetor** é um método usado pelo Windows para desbloquear uma unidade criptografada.

```text
manage-bde.exe -status C:
manage-bde.exe -protectors -get C:
```

O primeiro comando informa o estado da criptografia, proteção e bloqueio. O segundo lista tipos e IDs dos protetores e pode exibir a senha de recuperação. A Microsoft documenta essas verificações no [guia de operações do BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/operations-guide) e na [referência do comando de estado](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-status). **Não cole a saída em um pedido de ajuda nem a compartilhe em uma captura de tela.** Se o dispositivo já estiver bloqueado, use o ID exibido na tela de recuperação. Os oito primeiros dígitos ajudam a selecionar a chave correta.

## Onde encontrar a chave de recuperação do BitLocker

O **ID da chave de recuperação** identifica uma chave armazenada. A **chave de recuperação** é o número separado de 48 dígitos que você digita para desbloquear a unidade. Não informe o ID no campo da senha de recuperação.

| Dispositivo ou backup | Onde procurar |
|---|---|
| **Conta Microsoft pessoal** | Em outro dispositivo, entre pela [página da Microsoft para chaves de recuperação](https://aka.ms/myrecoverykey). Confira o ID antes de usar a chave de 48 dígitos. |
| **Dispositivo corporativo ou escolar** | Consulte a conta da organização pela [página da Microsoft para contas corporativas ou escolares](https://aka.ms/aadrecoverykey) ou fale com a equipe de TI. |
| **Impressão ou backup USB** | Procure a impressão ou o arquivo de texto criado ao ativar a criptografia. Compare o ID com o exibido na tela. |

A Microsoft lista esses locais em [Encontre sua chave de recuperação do BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/find-your-bitlocker-recovery-key). Comece pela chave com ID correspondente ao pedido. Uma chave de outro dispositivo ou de um protetor removido talvez não desbloqueie este volume. Se outra pessoa configurou o dispositivo, a chave pode estar na conta dela.

## Crie uma cópia de segurança separada da chave

Se o Windows ainda iniciar em uma edição Pro, Enterprise ou Education, pesquise por **Gerenciar BitLocker**. Ao lado da unidade criptografada, selecione **Fazer backup da chave de recuperação**. A Microsoft oferece o backup em uma conta, unidade USB, arquivo de texto ou impressão. Se escolher arquivo ou USB, guarde-o somente em mídia criptografada com controle de acesso e separada do computador. Não use um local sem criptografia. Consulte [Faça backup da chave de recuperação do BitLocker](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key) para ver a interface e as opções atuais.

No Windows Home, **Gerenciar BitLocker** não está disponível. No Windows 11, consulte **Configurações > Privacidade e segurança > Criptografia do dispositivo** e confirme a chave na conta Microsoft usada na configuração. A Microsoft explica que a [Criptografia do dispositivo](https://support.microsoft.com/en-us/windows/security/encryption/device-encryption-in-windows) salva a chave na conta Microsoft ou corporativa vinculada quando é ativada. Salve outra cópia protegida se a configuração oferecer uma opção de exportação.

Abra um backup digital em outro dispositivo. Se for uma impressão, compare-a com a conta ou a tela de recuperação. Confira o **ID da chave de recuperação** com o ID exibido na tela ou na lista de protetores. Verifique se a cópia contém os 48 dígitos da chave associada. Guarde uma cópia impressa ou removível longe do computador criptografado. Um ladrão com o computador e a chave poderia contornar a proteção da unidade, alerta a Microsoft nas [orientações de backup](https://support.microsoft.com/en-us/windows/security/encryption/back-up-your-bitlocker-recovery-key). Não anexe a chave a um chamado de suporte.

> **Resultado esperado:** você tem acesso a uma chave de recuperação correspondente fora do computador.

## Desbloqueie um computador que não inicia

Se aparecer a **tela de recuperação do BitLocker**, digite a chave de 48 dígitos correspondente ao ID. Se o Windows iniciar, copie seus arquivos antes de alterar partições. Se a chave desbloquear a unidade, mas o Windows continuar sem iniciar, abra o [Ambiente de Recuperação do Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/windows-recovery-environment) e tente **Reparo de Inicialização** antes de redefinir o computador. Algumas ferramentas exigem a chave enquanto a unidade estiver criptografada.

Para copiar arquivos pelas ferramentas de recuperação, abra **Solução de Problemas > Opções avançadas > Prompt de Comando** no Ambiente de Recuperação do Windows. Use `manage-bde -status` e `dir` para identificar o volume criptografado do Windows e uma unidade externa separada para o backup. **As letras podem ser diferentes das usadas no Windows normal.** Não copie para o USB de instalação nem para a unidade de origem criptografada.

```text
manage-bde.exe -status
dir D:\Users
dir E:\
```

As letras acima são exemplos. Depois de identificar os volumes corretos, desbloqueie o volume do Windows com a chave correspondente. Troque a letra e o marcador de exemplo pelos seus valores. Digite a chave real de 48 dígitos localmente. Não publique nem compartilhe a saída.

```text
manage-bde.exe -unlock D: -recoverypassword <48-digit-key>
```

A opção documentada `-recoverypassword` recebe a chave de 48 dígitos na linha de comando. Isso pode expor a chave no histórico do shell, em transcrições e na inspeção de processos. Use a tela de recuperação do Windows se quiser informar a chave sem um argumento de linha de comando. Se você salvou um arquivo `.bek` separado, `-recoverykey <path-to-external-bek>` evita digitar os 48 dígitos. Mantenha a chave fora de capturas de tela e chamados.

A Microsoft documenta o [comando de desbloqueio](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/manage-bde-unlock). As [orientações de recuperação](https://learn.microsoft.com/en-us/troubleshoot/windows-client/windows-security/bitlocker-recovery-known-issues) também descrevem como copiar arquivos do usuário para outra unidade após desbloquear. Para copiar a pasta Documentos como exemplo, confirme primeiro o nome da conta do Windows e a letra da unidade externa, depois substitua os dois caminhos:

```text
xcopy "D:\Users\Name\Documents" "E:\Backup\Documents" /S /E /I /H /V
```

As opções **`/S /E`** incluem subpastas, até as vazias. **`/I`** trata o destino como uma pasta, **`/H`** inclui arquivos ocultos e **`/V`** verifica cada arquivo gravado. A Microsoft documenta essas opções na [referência do xcopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/xcopy). Repita para outras pastas necessárias. Abra os arquivos copiados em outro dispositivo antes de apagar a unidade do Windows. Se não conseguir identificar os volumes ou a cópia falhar, pare e procure um especialista de recuperação confiável.

## Decida se deve reinstalar

**Um backup da chave não é um backup de arquivos.** Siga esta ordem antes de escolher como reinstalar:

1. Identifique a unidade criptografada e o respectivo ID da chave de recuperação.
2. Recupere a chave correspondente de 48 dígitos da conta, impressão ou backup USB.
3. Se a unidade estiver bloqueada, desbloqueie-a pela tela ou pelas ferramentas de recuperação.
4. Copie Área de Trabalho, Documentos, Imagens e outras pastas locais para uma unidade externa ou nuvem confiável. Inclua exportações do navegador, dados de aplicativos e registros de licença, se necessário.
5. Abra alguns arquivos copiados em outro dispositivo.
6. Escolha reparo, redefinição ou reinstalação somente depois de conferir o backup.

> **Resultado esperado:** a chave correspondente e os arquivos importantes estão acessíveis fora da instalação antiga do Windows.

A Microsoft lista as [opções de recuperação do Windows](https://support.microsoft.com/en-us/windows/experience/backup-recovery/recovery-options-in-windows), cada uma com efeitos diferentes para arquivos e aplicativos. Muitas opções do Ambiente de Recuperação do Windows exigem a chave quando o BitLocker protege a unidade. Se o volume estiver bloqueado nesse ambiente, **Manter meus arquivos** não o desbloqueia sem a chave.

**Reparo de Inicialização** e **Restauração do Sistema** tentam reparar a instalação existente. **Restaurar este computador** oferece **Manter meus arquivos**, mas remove aplicativos e configurações. **Remover tudo** apaga arquivos pessoais. Executar **`setup.exe` em uma sessão do Windows ativa** permite uma reinstalação no local com opções para manter dados. Selecionar **Instalar o Windows** após iniciar pela mídia USB começa uma instalação limpa que remove arquivos, aplicativos e configurações da instalação escolhida. A mesma mídia também oferece um caminho de reparo. Leia a opção exibida e confira o disco de destino antes de confirmar qualquer redefinição ou instalação. A Microsoft explica os dois caminhos nas [instruções de reinstalação](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media).

| Situação | Próxima ação |
|---|---|
| **O Windows inicia e você precisa dos arquivos** | Faça backup dos arquivos, verifique a chave e depois escolha um reparo ou uma reinstalação. |
| **O Windows pede a chave** | Compare o ID na tela com uma chave salva antes de alterar a unidade. |
| **Sem chave correspondente e sem backup dos arquivos** | Pare antes de apagar a unidade. Consulte cada conta, impressão, backup USB e a equipe de TI. |
| **Os arquivos estão copiados e você quer recomeçar** | Siga as [instruções de reinstalação da Microsoft](https://support.microsoft.com/en-us/windows/deployment/install-upgrade/reinstall-windows-with-the-installation-media) e escolha o disco de destino com cuidado. |

A Microsoft informa que o suporte não consegue recriar uma chave de recuperação perdida. Se não a encontrar, pare de alterar as configurações de firmware e verifique todos os locais de backup. Em um equipamento gerenciado, peça ajuda ao administrador. Uma redefinição sem a chave necessária remove os arquivos antigos. Uma instalação limpa também remove arquivos pessoais, aplicativos, personalizações do dispositivo e configurações da instalação selecionada. Tome essa decisão depois de conferir o backup.

## Solução de problemas

- **A chave não funciona:** confira novamente o ID e a conta. Um dispositivo pode ter mais de uma chave salva.
- **Gerenciar BitLocker não aparece:** o Windows Home usa Criptografia do dispositivo em equipamentos compatíveis. Verifique Configurações e a conta Microsoft usada na instalação.
- **Há várias chaves na conta:** compare os oito primeiros dígitos do ID da tela com os registros salvos. Não escolha uma chave apenas pelo nome do dispositivo.
- **A chave desbloqueia a unidade, mas o Windows não inicia:** tente Reparo de Inicialização no Ambiente de Recuperação do Windows. Copie os arquivos acessíveis antes de redefinir ou fazer uma instalação limpa.
- **A empresa ou escola guarda a chave:** fale com o administrador antes de redefinir ou reinstalar o equipamento.
- **O arquivo da chave está no computador bloqueado:** procure uma conta separada, impressão ou backup removível. Uma cópia somente na unidade criptografada não ajuda enquanto ela estiver bloqueada.
- **O pedido apareceu após uma alteração de firmware:** registre a alteração e não faça outras. Encontre a chave correspondente ou fale com o administrador.

## Próximas etapas

Depois de verificar a chave e os arquivos, siga o [guia de instalação limpa do Windows](/articles/how-to-install-windows-10-and-windows-11-from-scratch/) se isso atender ao seu objetivo. Quando o Windows iniciar, confira **Configurações > Privacidade e segurança > Criptografia do dispositivo** ou pesquise por **Gerenciar BitLocker**. Nas edições Pro, Enterprise ou Education, selecione **Fazer backup da chave de recuperação**. No Home, confirme que a conta vinculada tem a chave atual e salve outra cópia se o Windows oferecer exportação. Não presuma que a chave antiga serve para uma nova instalação criptografada.

---
title: "Reforce a segurança do computador desativando SSL e TLS 1.1 e anteriores"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "Desative SSL e versões antigas do TLS mantendo TLS 1.2 ou superior. O guia aborda Schannel e .NET no Windows e serviços Linux."
tags: ['Reforço da segurança do computador', 'Desativação de SSL e TLS', 'Segurança dos dados', 'POODLE', 'BEAST', 'Heartbleed', 'Editor do Registro do Windows', 'Configuração do OpenSSL no Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Um computador com um símbolo de cadeado que representa a segurança dos dados"
coverCaption: ""
---

## Introdução:

Os computadores tornaram-se parte essencial do nosso quotidiano, e a necessidade de proteger os dados também cresceu. SSL (Secure Socket Layer) e TLS (Transport Layer Security) são protocolos amplamente usados para proteger dados em trânsito. Com a evolução da tecnologia, as versões antigas ficaram vulneráveis a ataques. Este artigo explica como desativar SSL e TLS 1.0 e 1.1, mantendo TLS 1.2 ou TLS 1.3 disponível.

*TLS 1.2 não é um protocolo obsoleto. A referência mínima atual é TLS 1.2 ou superior. A [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) define TLS 1.3, enquanto a [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) descontinua formalmente TLS 1.0 e TLS 1.1.*

### Por que desativar SSL e TLS 1.1 e anteriores?

As versões antigas de SSL e TLS são vulneráveis a ameaças como POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) e Heartbleed. Esses ataques podem expor informações sensíveis, por isso é importante desativar protocolos antigos. O Heartbleed afetou implementações vulneráveis do OpenSSL, não era uma versão de protocolo. Corrija a biblioteca e troque as credenciais expostas.

As atuais [orientações de registo do Schannel da Microsoft](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) listam as definições de protocolo para versões suportadas do Windows. A Microsoft recomenda a Política de Grupo ou outras ferramentas de gestão suportadas, quando disponíveis. Edite diretamente o registo apenas quando não houver um controlo melhor.

### Desativar SSL e TLS 1.1 e anteriores no Windows:

No Windows, pode desativar estes protocolos através do Editor do Registo. O script PowerShell abaixo altera as definições de cliente e servidor do Schannel. Também configura o .NET para usar os valores TLS predefinidos do sistema operativo e criptografia forte.

```powershell
Function Disable-Protocol {
    param (
        [Parameter(Mandatory=$true)]
        [string]$Protocol
    )
    $ServerPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Server"
    $ClientPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\$Protocol\Client"
    New-Item -Path $ServerPath -Force
    New-Item -Path $ClientPath -Force
    Set-ItemProperty -Path $ServerPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ServerPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
    Set-ItemProperty -Path $ClientPath -Force -Name Enabled -Type "DWORD" -Value 0
    Set-ItemProperty -Path $ClientPath -Force -Name DisabledByDefault -Type "DWORD" -Value 1
}
# Disable SSL v2
Disable-Protocol -Protocol "SSL 2.0"
# Disable SSL v3
Disable-Protocol -Protocol "SSL 3.0"
# Disable TLS 1.0
Disable-Protocol -Protocol "TLS 1.0"
# Disable DTLS 1.0
Disable-Protocol -Protocol "DTLS 1.0"
# Disable TLS 1.1
Disable-Protocol -Protocol "TLS 1.1"
# There is no DTLS 1.1 protocol. RFC 8996 deprecates DTLS 1.0 and retains DTLS 1.2.

function Set-NETStrongAuthentication {
    param(
        [string]$RegistryPath,
        [string]$Name,
        [string]$Type,
        [int]$Value
    )
    Set-ItemProperty -Path $RegistryPath -Force -Name $Name -Type $Type -Value $Value
}

$NETVersions = @("2.0.50727", "3.0", "4.0.30319")

foreach ($version in $NETVersions) {
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SchUseStrongCrypto -Type "DWORD" -Value 0x00000001
    Set-NETStrongAuthentication -RegistryPath "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v$version" -Name SystemDefaultTlsVersions -Type "DWORD" -Value 0x00000001
}
```

#### Desativar SSL e TLS 1.1 e anteriores no Linux:

No Linux, a forma de desativar protocolos antigos depende da aplicação e da biblioteca. Alterar `/etc/ssl/openssl.cnf` não substitui as definições de todos os daemons nem das bibliotecas TLS incluídas nas aplicações. Siga estes passos:

1. Abra o terminal e inicie sessão como root.
2. Aceda ao ficheiro de configuração do OpenSSL. Normalmente, fica em /etc/ssl/openssl.cnf.
3. Abra o ficheiro num editor de texto, como nano ou vim.
4. Localize a diretiva de protocolo do serviço e defina o mínimo como TLS 1.2. A antiga instrução `-TLSv1.2` desativava TLS 1.2, por isso não a use como mínimo atual.
5. Guarde o ficheiro e feche o editor de texto.
6. Reinicie os serviços que usam OpenSSL, como Apache ou Nginx, para aplicar as alterações.

## Conclusão:

Desativar SSL e TLS 1.1 e anteriores reforça a segurança do computador e mantém a compatibilidade com clientes TLS modernos. A definição correta pertence ao serviço que negocia a ligação TLS. Teste cada aplicação em vez de presumir que um único ficheiro OpenSSL controla todos os daemons.

Desativar estas versões antigas pode afetar a compatibilidade com alguns sistemas. Teste cuidadosamente as alterações e confirme que não causam efeitos adversos antes da implementação completa.

Siga os passos deste artigo para proteger informações sensíveis e reduzir o risco de ataques. Primeiro, identifique o protocolo negociado por cada serviço. Depois, registe as exceções temporárias.

## Lista de verificação atual

- **Confirme o protocolo negociado.** Teste o cliente e o servidor com um scanner TLS ou um teste interno aprovado, nos dois lados da ligação.
- **Mantenha TLS 1.2 ativado.** Algumas aplicações antigas ainda precisam dele, enquanto o suporte para TLS 1.3 depende do sistema operativo e da biblioteca.
- **Analise DTLS separadamente.** A RFC 8996 descontinua DTLS 1.0. Não define um protocolo DTLS 1.1.
- **Reinicie os serviços afetados.** As definições do Schannel e das aplicações muitas vezes exigem o reinício do serviço ou do sistema.
- **Registe as exceções.** Documente cada endpoint antigo que ainda precisa temporariamente de uma definição de compatibilidade e atribua uma data para a sua remoção.

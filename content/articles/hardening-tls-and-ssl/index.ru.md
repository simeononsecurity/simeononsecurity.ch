---
title: "Укрепите защиту компьютера, отключив SSL и TLS 1.1 и более ранние версии"
date: 2023-02-08
lastmod: 2026-11-13
toc: true
draft: false
description: "Отключите SSL и старые версии TLS, сохранив TLS 1.2 или новее. Рассматриваются Schannel и .NET в Windows, а также службы Linux."
tags: ['Укрепление защиты компьютера', 'Отключение SSL и TLS', 'Защита данных', 'POODLE', 'BEAST', 'Heartbleed', 'Редактор реестра Windows', 'Конфигурация OpenSSL в Linux', 'Apache', 'Nginx']
cover: "/img/cover/A_computer_with_a_padlock_symbol_representing_data_security.webp"
coverAlt: "Компьютер со значком замка, символизирующим защиту данных"
coverCaption: ""
---

## Введение:

Компьютеры стали важной частью повседневной жизни, поэтому потребность в защите данных выросла. Для защиты данных при передаче широко применяются протоколы SSL (Secure Socket Layer) и TLS (Transport Layer Security). По мере развития технологий старые версии этих протоколов становятся уязвимыми для атак. В статье объясняется, как отключить SSL и TLS 1.0 и 1.1, сохранив доступность TLS 1.2 или TLS 1.3.

*TLS 1.2 не является устаревшим протоколом. Текущий минимальный уровень — TLS 1.2 или новее. [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446) определяет TLS 1.3, а [RFC 8996](https://www.rfc-editor.org/rfc/rfc8996) официально выводит из употребления TLS 1.0 и TLS 1.1.*

### Зачем отключать SSL и TLS 1.1 и более ранние версии?

Старые версии SSL и TLS уязвимы для таких угроз, как POODLE (Padding Oracle On Downgraded Legacy Encryption), BEAST (Browser Exploit Against SSL/TLS) и Heartbleed. Эти атаки могут раскрыть конфиденциальные сведения, поэтому старые протоколы следует отключить. Heartbleed затрагивал уязвимые реализации OpenSSL и сам по себе не был версией протокола. Установите исправление для библиотеки и смените раскрытые учетные данные.

В актуальном [руководстве Microsoft по реестру Schannel](https://learn.microsoft.com/en-us/windows-server/security/tls/tls-registry-settings) перечислены настройки протоколов для поддерживаемых выпусков Windows. Microsoft рекомендует применять групповую политику или другие поддерживаемые средства управления, если они доступны. Изменяйте реестр напрямую только при отсутствии более подходящего средства.

### Отключение SSL и TLS 1.1 и более ранних версий в Windows:

В Windows эти протоколы можно отключить через редактор реестра. Приведенный ниже сценарий PowerShell меняет параметры Schannel для клиента и сервера. Он также настраивает .NET на использование системных значений TLS по умолчанию и надежной криптографии.

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

#### Отключение SSL и TLS 1.1 и более ранних версий в Linux:

В Linux способ отключения старых протоколов зависит от приложения и библиотеки. Изменение `/etc/ssl/openssl.cnf` не переопределяет параметры каждого демона или встроенной библиотеки TLS. Выполните следующие действия:

1. Откройте терминал и войдите с правами root.
2. Перейдите к файлу конфигурации OpenSSL. Обычно он находится в /etc/ssl/openssl.cnf.
3. Откройте файл в текстовом редакторе, например nano или vim.
4. Найдите директиву протокола службы и задайте минимальную версию TLS 1.2. Старая инструкция `-TLSv1.2` отключала TLS 1.2, поэтому не используйте ее как современный минимум.
5. Сохраните файл и закройте редактор.
6. Перезапустите службы, использующие OpenSSL, например Apache или Nginx, чтобы применить изменения.

## Заключение:

Отключение SSL и TLS 1.1 и более ранних версий укрепляет защиту компьютера, сохраняя совместимость с современными клиентами TLS. Настройку задают в службе, которая согласует параметры TLS. Проверяйте каждое приложение отдельно, не предполагая, что один файл OpenSSL управляет всеми демонами.

Отключение этих старых версий может повлиять на совместимость с некоторыми устаревшими системами. Тщательно проверьте изменения и убедитесь в отсутствии негативных последствий до полного внедрения.

Следуйте рекомендациям статьи, чтобы защитить конфиденциальную информацию и снизить риск атак. Сначала определите протокол, который согласует каждая служба, затем задокументируйте временные исключения.

## Текущий список проверок

- **Проверьте согласованный протокол.** Проверьте клиент и сервер TLS-сканером или одобренным внутренним тестом с обеих сторон соединения.
- **Оставьте TLS 1.2 включенным.** Некоторым старым приложениям он все еще нужен, а поддержка TLS 1.3 зависит от операционной системы и библиотеки.
- **Проверяйте DTLS отдельно.** RFC 8996 выводит DTLS 1.0 из употребления. Он не определяет протокол DTLS 1.1.
- **Перезапустите затронутые службы.** Для применения новой политики настройки Schannel и приложений часто требуют перезапуска службы или системы.
- **Документируйте исключения.** Запишите все устаревшие конечные точки, которым временно нужна настройка совместимости, и назначьте дату ее удаления.

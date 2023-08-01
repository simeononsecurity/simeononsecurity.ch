---
title: "Сегодня я узнал больше о создании и реализации политики WDAC"
date: 2022-05-18
toc: true
draft: false
description: "Сегодня я узнал больше об условных сигналах Ansible и управлении переменными"
genre: ["Автоматизация", "Безопасность Windows", "Управление приложениями", "Защитник Windows", "WDAC", "Powershell", "Защита от угроз", "Windows Server 2019", "Безопасность предприятия", "Управление политикой", "Лучшие практики безопасности"]
tags: ["автоматизация", "WDAC", "управление приложениями", "Контроль приложений Windows Defender", "Защитник Windows", "Powershell", "Документация Microsoft", "Создание политики WDAC", "развертывание политики", "развертывание на основе сценариев", "многочисленные политики WDAC", "устройства с фиксированной нагрузкой", "доверенные приложения", "политики отказа", "методы обеспечения безопасности", "управление политикой", "безопасность предприятия", "защита от угроз", "Windows Server", "Безопасность Windows", "белые списки приложений"]
---

**Что интересного узнал и нашел сегодня SimeonOnSecurity**.

Сегодня SimeonOnSecurity обновил репозиторий Windows-Defender-Application-Control-Hardening и узнал о Windows Defender Application Control (WDAC), функции Windows 10 Enterprise и Windows Server 2019, которая обеспечивает безопасность, контролируя выполняемые на устройстве действия.

SimeonOnSecurity углубился в документацию Microsoft по WDAC и обнаружил несколько ключевых ресурсов для создания и развертывания политик. Он узнал о том, как создать политику WDAC для устройств с фиксированной рабочей нагрузкой с помощью эталонного компьютера, как развернуть политики WDAC с помощью сценария и как использовать несколько политик для различных сценариев.

Кроме того, SimeonOnSecurity ознакомился с руководством по созданию политик запрета WDAC, что позволило ему лучше понять концепцию разрешения запуска на устройстве только доверенных приложений и запрета всех остальных.

В целом, изучение Windows Defender Application Control позволило SimeonOnSecurity еще больше укрепить понимание важности контроля приложений в современной практике безопасности.

## Обновленные репозитории:
- [simeononsecurity/Windows-Defender-Application-Control-Hardening](https://github.com/simeononsecurity/Windows-Defender-Application-Control-Hardening)

## Чтение WDAC:
- [Microsoft - Create a WDAC policy for fixed-workload devices using a reference computer](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-initial-default-policy)
- [Microsoft - Deploy WDAC policies using script](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deployment/deploy-wdac-policies-with-script)
- [Microsoft - Guidance on Creating WDAC Deny Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/create-wdac-deny-policy)
- [Microsoft - Use multiple Windows Defender Application Control Policies](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/deploy-multiple-windows-defender-application-control-policies)

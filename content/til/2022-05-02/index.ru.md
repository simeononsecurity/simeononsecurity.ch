---
title: "Today I Learned about Ansible and Block/Rescue Modules"
date: 2022-05-02
toc: true
draft: false
description: ""
genre: ["Автоматизация", "Соответствие требованиям", "Ansible", "Плейбуки Ansible", "Коллекции Ansible", "Безопасность Windows", "Администрирование Windows", "Соответствие требованиям безопасности", "Автоматизация ИТ", "Управление конфигурацией"]
tags: ["Автоматизация", "Соответствие требованиям", "Ansible", "Плейбуки Ansible", "Коллекции Ansible", "GitHub", "Блок", "Спасатель", "Всегда", "Безопасность Windows", "Администрирование Windows", "Требования к СТИГ", "Автоматизация систем безопасности", "Управление конфигурацией", "ИТ-безопасность", "Модули Ansible", "Автоматизация Windows", "Ansible Galaxy", "Windows STIG", "Средства администрирования Windows", "Руководство по техническому внедрению системы безопасности", "Содержание Ansible", "Передовые методы обеспечения безопасности Windows", "Решения по автоматизации ИТ", "Аудит безопасности", "Конфигурация системы Windows"]
---
 SimeonOnSecurity узнал об этом и нашел интересным сегодня**.

Сегодня SimeonOnSecurity узнал и обнаружил несколько интересных вещей, связанных с безопасностью Windows и автоматизацией с помощью Ansible.

Во-первых, были обнаружены два новых и обновленных репозитория. Репозиторий Windows_STIG_Ansible представляет собой комплексное решение для настройки Windows-систем на соответствие требованиям Security Technical Implementation Guide (STIG) с использованием платформы автоматизации Ansible. Репозиторий windows_stigs представляет собой набор ролей Ansible для настройки Windows-систем на соответствие требованиям STIG и доступен на Ansible Galaxy, центральном хранилище для обмена содержимым Ansible.

SimeonOnSecurity также нашел несколько обучающих ресурсов, связанных с автоматизацией Windows с помощью Ansible. Документация по модулю ansible.windows.win_copy содержит информацию о том, как копировать файлы в системах Windows с помощью Ansible. Документация по блокам ansible содержит информацию об использовании блоков - мощной функции Ansible, позволяющей группировать несколько задач вместе и применять условное выполнение. Руководство пользователя ansible galaxy содержит информацию о том, как использовать Ansible Galaxy, а документация ansible installing content - о том, как устанавливать содержимое Ansible Galaxy.

## Новые/обновленные репозитории:

- [simeononsecurity/Windows_STIG_Ansible](https://github.com/simeononsecurity/Windows_STIG_Ansible)
- [simeononsecurity/windows_stigs](https://galaxy.ansible.com/simeononsecurity/windows_stigs)

## Учебные ресурсы:
- [ansible.windows.win_copy module](https://docs.ansible.com/ansible/latest/collections/ansible/windows/win_copy_module.html)
- [ansible blocks](https://docs.ansible.com/ansible/latest/user_guide/playbooks_blocks.html)
- [ansible galaxy user guide](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html)
- [ansible installing content](https://galaxy.ansible.com/docs/using/installing.html)
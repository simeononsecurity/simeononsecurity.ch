---
title: 'Откат Home Assistant Core 2026.11 до 2026.10.4: исправление версии 3 хранилища HTTP'
date: 2026-11-15
lastmod: '2026-11-18'
toc: true
draft: false
description: Исправьте ошибку версии 3 хранилища HTTP после отката Home Assistant Core 2026.11 до 2026.10.4 на Yellow. В статье
  приведены защищённые команды и проверенные результаты.
genre:
- Домашняя автоматизация
- Устранение неполадок
tags:
- Home Assistant Yellow
- Home Assistant OS
- Откат Core 2026.11
- Core 2026.10.4
- Версия 3 хранилища HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Иллюстрация жёлтой компьютерной платы, разорванной связи конфигурации и восстановленной веб-панели
coverCaption: ''
---

Неудачное обновление Home Assistant Core 2026.11 откатило мой Yellow CM4 до версии 2026.10.4. Yellow оставался доступен в сети, но перестал показывать панель. После отката файл настроек HTTP остался в версии хранилища 3.1, а Core 2026.10.4 поддерживает версию 2.2. Я сохранил файл, преобразовал его копию с помощью строгих проверок, восстановил доступ по HTTP, а затем обновил Core до версии 2026.11.1.

<!--more-->

## Главное

- **Подтвердите несовместимость.** Сопоставьте ошибку в журнале Core с установленной версией и версией хранилища HTTP.
- **Сохраните файл.** До восстановления оставьте неизменённую копию и резервную копию за пределами устройства.
- **Проверьте результат.** Проверьте состояние Core, сохранённый порт прослушивания, панель и установленную версию.

**Исправление именно для этого случая:** [Сохраните файл HTTP](#preserve-recovery-options), [создайте и проверьте кандидат версии 2.2](#apply-the-tested-fix-for-version-31), [установите его после остановки Core](#apply-the-tested-fix-for-version-31) и [проверьте результат обновления](#verify-the-update-outcome). Преобразование проверяет исходные поля и останавливается при несовпадении. Не применяйте его к непроверенному файлу HTTP.

## Перед началом

Вам понадобятся физический доступ к Yellow CM4, кабель USB-C для передачи данных, работающая последовательная консоль и пригодная резервная копия или сохранённая конфигурация. Для ручного способа нужен доступ к оболочке хоста и внимательная проверка JSON. Выделите на диагностику и ремонт не менее 30 минут. Запуск Core и восстановление резервной копии на крупных установках занимают больше времени.

## Распознайте сбой

В журнале Core появилась решающая ошибка:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

Старая версия Core не смогла загрузить `http`. Также перестали работать интерфейс и другие компоненты, зависящие от HTTP. Аренда адреса у маршрутизатора и доступная страница Observer не доказывали, что панель открывается. [Проблема Home Assistant Core № 190583](https://github.com/home-assistant/core/issues/190583) описывает такой же сбой после отката в нескольких установках, включая Yellow. [Мой комментарий к проблеме](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) содержит сведения о проверенном восстановлении этого Yellow и итоговом состоянии Core.

**Причина сбоя веб-доступа:** Core 2026.11 записал `.storage/http` в формате 3.1. При откате вернулась версия Core 2026.10.4, но не совместимый файл HTTP. Core 2026.10.4 не принимает версию хранилища 3. Сохранённый на этом Yellow профиль `intermediate_v6` тоже не соответствует старой схеме. Причина сбоя первого обновления и запуска отката неизвестна. На 2026-11-15 связанная проблема оставалась открытой, а в обсуждении не было исправления, подтверждённого сопровождающими.

Перед изменением файлов проверьте установленную версию Core и хранилище HTTP:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

Ниже приведён результат для этого случая, из которого удалены временные метки и личные данные:

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

Команды восстановления ниже сравнивают сохранённый Supervisor порт прослушивания с файлом HTTP, не показывая ни одно из значений. При несовпадении проверьте фактический порт прослушивания Core, прежде чем менять файлы.

| Признак | Значение |
| --- | --- |
| Core поддерживает версию хранилища 2, а файл сообщает версию 3 | Старая версия не может загрузить сохранённые настройки HTTP |
| В файле HTTP и списке Supervisor указаны разные порты прослушивания | Проверьте фактический порт Core, прежде чем определять причину |
| Главная страница отвечает, но состояние Core остаётся STARTING | Ответ интерфейса не доказывает завершение запуска |

## Сохраните варианты восстановления {#preserve-recovery-options}

Перед следующим обновлением сохраните пригодную резервную копию вне Yellow. [Руководство Home Assistant по резервному копированию](https://www.home-assistant.io/common-tasks/general/backups/) описывает облачные и внешние места хранения. Для зашифрованной копии нужен ключ восстановления. Не очищайте диск данных NVMe во время диагностики этой несовместимости хранилища.

Скопируйте файл HTTP перед редактированием:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Остановитесь, если команда завершилась ошибкой. Не изменяйте прежнюю копию восстановления с таким же именем. Выберите новое имя и повторите проверку перед продолжением.

Если панель недоступна, используйте последовательную консоль Yellow. [Руководство Nabu Casa для Linux и macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) показывает подключение USB-C и расположение UART JP1. Следуйте инструкциям для CM4, подходящим к вашему оборудованию.

## Примените проверенное исправление для версии 3.1 {#apply-the-tested-fix-for-version-31}

Предпочтительный способ — использовать совместимый файл HTTP, созданный до обновления. Если уместно полное восстановление, верните резервную копию по документированной процедуре Home Assistant. Если извлекаете один файл, перед заменой активного файла подтвердите его версию хранилища и сохранённый порт прослушивания. Если совместимого файла HTTP не было, прямым проверенным исправлением на этом Yellow стали команды ниже.

[Первоначальный обходной способ из проблемы](https://github.com/home-assistant/core/issues/190583) перемещает `.storage/http` и позволяет старой версии Core создать новый файл. В более позднем [сообщении о Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) в созданном заново файле указан другой порт прослушивания. Прежде чем считать веб-интерфейс восстановленным, проверьте новый файл и результат `ha core info`.

В моей установке не было блока YAML `http:`, ожидающей конфигурации HTTP, сертификата TLS или ключа в стабильных настройках. Сохранённым профилем был `intermediate_v6`. В этих узких условиях я создал отдельный кандидат версии 2.2 и сохранил существующий порт прослушивания:

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

Перед заменой активного файла все команды выше должны завершиться успешно. Если `jq` завершился ошибкой, проверьте файл-кандидат, прежде чем удалять его и повторять попытку. [Исходный код HTTP в Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) определяет версию хранилища 2.2 и принимает профиль `intermediate`. [Исходный код Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) использует версию 3.1 и версии профилей в именах. До установки я также проверил кандидата с помощью `HTTP_STORAGE_SCHEMA` установленной старой версии Core.

Пока контейнер работает, выполните проверку схемы установленной старой версии Core:

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

Остановитесь, если схема отклоняет кандидат. Этот шаг не проверяет все интеграции и все непроверенные варианты структуры хранилища HTTP.

Проверка схемы вывела `Schema accepted` для этого кандидата. Любой другой результат означает, что этот способ восстановления нужно прекратить.

Это ручное преобразование проверено для указанных полей. Файл с настройками TLS, доверенными прокси или ожидающей конфигурацией требует отдельной проверки. Если изменить только старший номер версии, останется профиль, который старая версия Core не принимает.

В моём случае у Supervisor была активная задача Core, поэтому команда `ha core stop` завершилась отказом. Я остановил контейнер Core из консоли хоста, установил проверенный кандидат и запустил контейнер:

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

Если команда завершится ошибкой после остановки, проверьте активный файл HTTP перед запуском `docker start homeassistant`. Если файл изменился, создайте новый кандидат из его текущего содержимого. После этого шага страница HTTP снова открылась. Один ответ по HTTP не доказывал, что Core полностью запустился, поэтому перед признанием системы восстановленной я проверил состояние Supervisor.

На этом Yellow команда `docker inspect -f '{{.State.Status}}' homeassistant` затем вывела `running`. Перед запросом следующего обновления проверьте `ha core info` и панель.

## Проверьте результат обновления {#verify-the-update-outcome}

Когда доступ по HTTP восстановился, я обновил Core до версии 2026.11.1. Чтобы запросить эту версию:

```bash
ha core update --version 2026.11.1
```

После длительного запуска команда сообщила об ошибке. Затем Supervisor записал для Core состояние RUNNING и сообщение `Successfully started Home Assistant 2026.11.1`. Проверка состояния показала, что установлена актуальная версия, файл HTTP снова мигрировал на версию 3.1, а контейнер не перезапускался во время наблюдения. Панель с авторизацией открылась. **Проверьте итоговое состояние, даже если команда обновления сообщает об ошибке.**

После длительного обновления проверьте версию, состояние Supervisor и состояние контейнера:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

В этом случае первая и третья команды выдали следующие очищенные от личных данных результаты:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Затем откройте панель по привычному локальному адресу и убедитесь, что загружаются текущие состояния. Храните сохранённый файл HTTP, пока не завершится следующая резервная копия и не будет подтверждена нормальная работа.

Данные с моего Yellow не позволили определить причину первого сбоя обновления. Сообщение о сбое следующей задачи тоже не указывало причину. Установленная версия и работающая панель лучше подтверждают итоговое состояние, чем одно сообщение CLI, но ни то ни другое не объясняет, почему Supervisor отметил задачу как неудачную.

## Следующие шаги

Если ошибка хранилища HTTP сохраняется, проверьте сохранённый файл и восстановите совместимую резервную копию либо запустите версию Core, которая может прочитать эту версию хранилища. Возврат сохранённого файла версии 3 под старой версией Core повторит сбой. Если Core перешёл в состояние RUNNING, но некоторые устройства остаются недоступными, отдельно проверьте соответствующие интеграции. Храните копию восстановления и облачную резервную копию, пока не завершится следующая копия и панель продолжит отвечать.

---
title: "Home Assistant Yellow Web Interface Unreachable After a Core Rollback: Recovery Guide"
date: 2026-11-15
lastmod: 2026-11-15
toc: true
draft: true
description: "Diagnose an HTTP storage version mismatch after a Home Assistant Yellow rollback, preserve configuration, restore web access, and verify Core."
genre: ["Home Automation", "Troubleshooting"]
tags: ["Home Assistant Yellow", "Home Assistant OS", "Core rollback", "HTTP storage", "CM4"]
cover: "/img/cover/home-assistant-yellow-core-rollback-http-recovery.webp"
coverAlt: "Illustration of a yellow computer board, broken configuration link, and restored web dashboard"
coverCaption: ""
---

A failed Home Assistant Core update rolled my Yellow CM4 back to an older release. The Yellow remained reachable on the network but stopped serving its dashboard because its HTTP settings file retained a newer storage format. The repair was to preserve the file, restore a format the older Core understood, and verify the saved listener before updating again.

<!--more-->

## Key takeaways

- **Confirm the mismatch.** Match the Core log error against the installed release and HTTP storage version.
- **Preserve the file.** Keep an unchanged copy and an off-device backup before recovery.
- **Verify the result.** Check Core's state, the saved listener, the dashboard, and the installed version.

## Before you begin

You need physical access to a Yellow CM4, a USB-C data cable, a working serial console, and a usable backup or preserved configuration. The manual path below requires host-shell access and careful JSON inspection. Plan at least 30 minutes for diagnosis and repair. Core startup and backup restoration take longer on large installations.

## Recognize the failure

The decisive error appeared in the Core log:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

The older Core release failed to load `http`. The frontend and other components depending on HTTP also failed. A router lease and healthy Observer page did not establish dashboard access. [Home Assistant Core issue #190583](https://github.com/home-assistant/core/issues/190583) documents the same rollback failure across several installations, including Yellow.

Check the installed Core release and the HTTP store before changing files:

```bash
ha core info --raw-json | jq '{version: .data.version, listener: .data.port}'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile, listener: .data.stable.server_port}' "$storage/http"
```

The first command reads Supervisor's saved listener. The second reads the HTTP file's listener. Compare them. A mismatch suggests an endpoint problem and calls for checking Core's actual listener.

| Signal | Meaning |
| --- | --- |
| Core supports storage version 2, file reports version 3 | The older release cannot load its saved HTTP settings |
| HTTP file and Supervisor list different listeners | Check Core's actual listener before attributing the failure |
| Front page responds, Core state is still STARTING | The frontend response alone does not prove a completed startup |

## Preserve recovery options

Keep a usable backup outside the Yellow before another update. [Home Assistant's backup guide](https://www.home-assistant.io/common-tasks/general/backups/) describes cloud and off-device locations. An encrypted backup needs its recovery key. Do not wipe the NVMe data disk while diagnosing this storage mismatch.

Copy the HTTP file before editing it:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Stop if the command fails. An earlier recovery copy with the same name stays untouched. Choose a new name and repeat the check before continuing.

When the dashboard is unavailable, use the Yellow serial console. The [Nabu Casa guide for Linux and macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) shows the USB-C connection and JP1 UART position. Follow the CM4 instructions for your hardware.

## Restore a compatible HTTP file

The preferred path is a compatible HTTP file from before the update. Restore the backup through Home Assistant's documented process when a complete restore is appropriate. If you extract one file, confirm its storage version and saved listener before replacing the active file.

The [issue's original workaround](https://github.com/home-assistant/core/issues/190583) moves `.storage/http` aside and lets the older Core create a new file. A later [Yellow report](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) shows a different listener in the regenerated file. Check the new file and `ha core info` before concluding the web interface is fixed.

My installation had no `http:` YAML block, no pending HTTP configuration, and no TLS certificate or key in the stable settings. The saved profile was `intermediate_v6`. In this narrow case, I built a separate version 2.2 candidate and retained the existing listener:

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

Every command above must succeed before replacing the active file. If `jq` fails, inspect the candidate file before removing it and retrying. [Core 2026.10.4's HTTP source](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) defines storage version 2.2 and accepts the `intermediate` profile. [Core 2026.11.1's source](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) uses version 3.1 and versioned profile names. I also validated the candidate against the installed older Core's `HTTP_STORAGE_SCHEMA` before installation.

Run the installed older Core's schema check while its container is still running:

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

Stop if the schema rejects the candidate. This step does not validate every integration or an untested HTTP store shape.

This manual conversion was tested for the stated fields. A file with TLS settings, trusted proxies, or a pending configuration needs its own review. Changing only the top-level version number leaves a profile the older Core does not accept.

Supervisor had an active Core job and rejected `ha core stop` in my case. I stopped the Core container from the host console, installed the validated candidate, and started it:

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

If a command fails after the stop, inspect the active HTTP file before running `docker start homeassistant`. A changed file needs a new candidate built from its latest contents. The HTTP page returned after this step. An HTTP response alone did not prove Core had finished startup, so I checked Supervisor's state before treating the system as recovered.

## Verify the update outcome

After HTTP access returned, I updated Core to 2026.11.1. The command reported a failure after a long startup. Supervisor then logged Core as RUNNING and `Successfully started Home Assistant 2026.11.1`. A status read showed the installed release was current, the HTTP file had migrated back to version 3.1, and the container had zero restarts during observation. The authenticated dashboard loaded.

For your system, check the release, Supervisor health, and container state after any long update:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

Then open the dashboard through your normal local address and confirm live states load. Keep the saved HTTP file until a subsequent backup and normal operation are verified.

The first update's failure was not established by the evidence from my Yellow. The later job's failure message also did not identify a cause. An installed release and a healthy dashboard are stronger evidence of the resulting state than the CLI message alone, but neither explains why Supervisor marked the job failed.

## Next steps

If the HTTP storage error remains, inspect the preserved file and restore a compatible backup or run a Core release able to read its storage version. Restoring the preserved version 3 file under the older Core repeats the outage. If Core reaches RUNNING but individual devices remain unavailable, investigate those integrations separately. Keep the recovery copy and cloud backup until the next backup completes and the dashboard stays responsive.

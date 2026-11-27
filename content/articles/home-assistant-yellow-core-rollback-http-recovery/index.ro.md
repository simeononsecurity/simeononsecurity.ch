---
title: 'Revenirea Home Assistant Core 2026.11 la 2026.10.4: remedierea versiunii 3 a stocării HTTP'
date: 2026-11-15
lastmod: 2026-11-27
toc: true
draft: false
description: Remediază eroarea versiunii 3 a stocării HTTP după revenirea Home Assistant Core 2026.11 la 2026.10.4 pe Yellow.
  Include comenzi protejate și rezultate verificate.
genre:
- Automatizarea locuinței
- Depanare
tags:
- Home Assistant Yellow
- Home Assistant OS
- Revenirea Core 2026.11
- Core 2026.10.4
- Versiunea 3 a stocării HTTP
- CM4
cover: /img/cover/home-assistant-yellow-core-rollback-http-recovery.webp
coverAlt: Ilustrație cu o placă de computer galbenă, o legătură de configurare întreruptă și un tablou de bord web restabilit
coverCaption: ''
---

O actualizare eșuată a Home Assistant Core 2026.11 mi-a readus Yellow CM4 la versiunea 2026.10.4. Yellow a rămas accesibil în rețea, dar nu a mai afișat tabloul de bord. Revenirea a lăsat un fișier de setări HTTP cu versiunea de stocare 3.1, în timp ce Core 2026.10.4 acceptă versiunea 2.2. Am păstrat fișierul, am convertit o copie cu verificări stricte, am restabilit accesul HTTP și apoi am actualizat Core la versiunea 2026.11.1.

<!--more-->

## Idei principale

- **Confirmă incompatibilitatea.** Compară eroarea din jurnalul Core cu versiunea instalată și versiunea stocării HTTP.
- **Păstrează fișierul.** Înainte de recuperare, păstrează o copie nemodificată și un backup în afara dispozitivului.
- **Verifică rezultatul.** Controlează starea Core, portul de ascultare salvat, tabloul de bord și versiunea instalată.

**Remediere pentru acest caz exact:** [Păstrează fișierul HTTP](#preserve-recovery-options), [creează și validează un candidat pentru versiunea 2.2](#apply-the-tested-fix-for-version-31), [instalează-l după oprirea Core](#apply-the-tested-fix-for-version-31) și [verifică rezultatul actualizării](#verify-the-update-outcome). Conversia verifică valorile inițiale ale câmpurilor și se oprește când acestea diferă. Nu o aplica unui fișier HTTP neinspectat.

## Înainte să începi

Ai nevoie de acces fizic la un Yellow CM4, un cablu de date USB-C, o consolă serială funcțională și un backup utilizabil sau o configurație păstrată. Procedura manuală cere acces la shell-ul gazdei și inspectarea atentă a JSON-ului. Rezervă cel puțin 30 de minute pentru diagnosticare și reparație. Pornirea Core și restaurarea backupurilor durează mai mult în instalările mari.

## Recunoaște defecțiunea

Eroarea decisivă a apărut în jurnalul Core:

```text
Storage file http has version 3 which is newer than the max supported version 2
```

Versiunea mai veche Core nu a putut încărca `http`. Interfața și alte componente dependente de HTTP au eșuat, de asemenea. O alocare de la router și o pagină Observer funcțională nu dovedeau că tabloul de bord era accesibil. [Problema Home Assistant Core #190583](https://github.com/home-assistant/core/issues/190583) documentează aceeași defecțiune la revenire în mai multe instalări, inclusiv Yellow. [Comentariul meu la problemă](https://github.com/home-assistant/core/issues/190583#issuecomment-6908185955) consemnează recuperarea testată pe acest Yellow și starea finală a Core.

**Cauza întreruperii web:** Core 2026.11 a scris `.storage/http` în formatul 3.1. Revenirea a restaurat Core 2026.10.4, dar nu a restaurat un fișier HTTP compatibil. Core 2026.10.4 respinge versiunea 3 a stocării. Profilul salvat `intermediate_v6` de pe acest Yellow nu este compatibil nici cu schema mai veche. Nu se cunoaște de ce prima actualizare a eșuat și a declanșat revenirea. La 2026-11-15, problema asociată era deschisă, iar discuția nu conținea o remediere confirmată de mentenanți.

Verifică versiunea instalată Core și stocarea HTTP înainte să modifici fișiere:

```bash
ha core info --raw-json | jq -r '.data.version'

storage=/mnt/data/supervisor/homeassistant/.storage
jq '{version, minor_version, pending_present: (.data.pending != null), profile: .data.stable.ssl_profile}' "$storage/http"
ha core logs | grep -F 'Storage file http has version 3'
```

Rezultatul de mai jos reflectă acest caz, cu marcajele temporale și detaliile private eliminate:

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

Comenzile de recuperare de mai jos compară portul de ascultare salvat de Supervisor cu fișierul HTTP fără să afișeze niciuna dintre valori. Dacă diferă, verifică portul real de ascultare al Core înainte să modifici fișiere.

| Semnal | Semnificație |
| --- | --- |
| Core acceptă versiunea 2 a stocării, iar fișierul indică versiunea 3 | Versiunea mai veche nu poate încărca setările HTTP salvate |
| Fișierul HTTP și lista Supervisor indică porturi de ascultare diferite | Verifică portul real de ascultare al Core înainte să atribui cauza |
| Pagina principală răspunde, dar Core este încă în starea STARTING | Răspunsul interfeței nu dovedește că pornirea s-a încheiat |

## Păstrează opțiunile de recuperare {#preserve-recovery-options}

Păstrează un backup utilizabil în afara Yellow înainte de o nouă actualizare. [Ghidul Home Assistant pentru backupuri](https://www.home-assistant.io/common-tasks/general/backups/) descrie locații în cloud și în afara dispozitivului. Un backup criptat necesită cheia sa de recuperare. Nu șterge discul de date NVMe în timp ce diagnostichezi această incompatibilitate a stocării.

Copiază fișierul HTTP înainte să-l editezi:

```bash
storage=/mnt/data/supervisor/homeassistant/.storage
test ! -e "$storage/http.before-recovery" &&
  cp -p "$storage/http" "$storage/http.before-recovery" &&
  cmp -s "$storage/http" "$storage/http.before-recovery"
```

Oprește-te dacă această comandă eșuează. Lasă nemodificată orice copie de recuperare mai veche cu același nume. Alege un nume nou și repetă verificarea înainte să continui.

Dacă tabloul de bord nu este disponibil, folosește consola serială Yellow. [Ghidul Nabu Casa pentru Linux și macOS](https://support.nabucasa.com/hc/en-us/articles/25454972435357-Using-the-serial-console-on-Home-Assistant-Yellow-for-debugging-Linux-macOS) arată conexiunea USB-C și poziția UART JP1. Urmează instrucțiunile CM4 pentru hardware-ul tău.

## Aplică remedierea testată pentru versiunea 3.1 {#apply-the-tested-fix-for-version-31}

Varianta preferată este un fișier HTTP compatibil, dinaintea actualizării. Restaurează backupul prin procedura documentată Home Assistant atunci când este potrivită o restaurare completă. Dacă extragi un singur fișier, confirmă versiunea de stocare și portul de ascultare salvat înainte să înlocuiești fișierul activ. Comenzile de mai jos sunt remedierea directă testată pe acest Yellow când nu era disponibil niciun fișier HTTP compatibil.

[Soluția inițială de ocolire din problemă](https://github.com/home-assistant/core/issues/190583) mută `.storage/http` și lasă versiunea mai veche Core să creeze un fișier nou. Un [raport ulterior despre Yellow](https://github.com/home-assistant/core/issues/190583#issuecomment-6749568119) arată un alt port de ascultare în fișierul regenerat. Verifică noul fișier și `ha core info` înainte să concluzionezi că interfața web funcționează.

Instalarea mea nu avea un bloc YAML `http:`, o configurație HTTP în așteptare sau certificat ori cheie TLS în setările stabile. Profilul salvat era `intermediate_v6`. În acest caz restrâns, am creat un candidat separat pentru versiunea 2.2 și am păstrat portul de ascultare existent:

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

Toate comenzile de mai sus trebuie să reușească înainte de înlocuirea fișierului activ. Dacă `jq` eșuează, inspectează candidatul înainte să-l elimini și să încerci din nou. [Codul HTTP din Core 2026.10.4](https://github.com/home-assistant/core/blob/2026.10.4/homeassistant/components/http/config.py) definește versiunea 2.2 a stocării și acceptă profilul `intermediate`. [Codul Core 2026.11.1](https://github.com/home-assistant/core/blob/2026.11.1/homeassistant/components/http/config.py) folosește versiunea 3.1 și nume de profil versionate. Înainte de instalare, am validat candidatul și cu `HTTP_STORAGE_SCHEMA` din versiunea mai veche Core instalată.

Rulează verificarea schemei din versiunea instalată mai veche de Core cât timp containerul încă funcționează:

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
print("Schema acceptată")
'
```

Oprește-te dacă schema respinge candidatul. Acest pas nu validează fiecare integrare sau fiecare formă netestată a stocării HTTP.

Verificarea schemei a afișat `Schema acceptată` pentru acest candidat. Orice alt rezultat oprește această procedură de recuperare.

Această conversie manuală a fost testată pentru câmpurile menționate. Un fișier cu setări TLS, proxy-uri de încredere sau o configurație în așteptare are nevoie de o analiză separată. Schimbarea doar a numărului principal de versiune lasă un profil pe care versiunea mai veche Core nu îl acceptă.

Supervisor avea o sarcină Core activă și, în cazul meu, a respins `ha core stop`. Am oprit containerul Core din consola gazdei, am instalat candidatul validat și apoi l-am pornit:

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

Dacă o comandă eșuează după oprire, inspectează fișierul HTTP activ înainte să rulezi `docker start homeassistant`. Dacă fișierul s-a schimbat, creează un candidat nou din conținutul său actual. Pagina HTTP a revenit după acest pas. Un răspuns HTTP nu dovedea singur că Core terminase pornirea, așa că am verificat starea Supervisor înainte să consider sistemul recuperat.

Pe acest Yellow, `docker inspect -f '{{.State.Status}}' homeassistant` a afișat apoi `running`. Verifică `ha core info` și tabloul de bord înainte să ceri o nouă actualizare.

## Verifică rezultatul actualizării {#verify-the-update-outcome}

După ce accesul HTTP a revenit, am actualizat Core la 2026.11.1. Pentru a solicita această versiune:

```bash
ha core update --version 2026.11.1
```

Comanda a raportat un eșec după o pornire îndelungată. Apoi Supervisor a înregistrat Core cu starea RUNNING și mesajul `Successfully started Home Assistant 2026.11.1`. O citire a stării a arătat că versiunea instalată era cea curentă, fișierul HTTP migrase din nou la versiunea 3.1, iar containerul nu se repornise în intervalul observat. Tabloul de bord autentificat s-a încărcat. **Verifică starea obținută chiar dacă această comandă raportează un eșec.**

După o actualizare îndelungată, verifică versiunea, starea Supervisor și starea containerului:

```bash
ha core info --raw-json | jq '{version: .data.version, update_available: .data.update_available}'
ha supervisor info --raw-json | jq '{healthy: .data.healthy, supported: .data.supported}'
docker inspect -f '{{.State.Status}} restarts={{.RestartCount}}' homeassistant
```

În acest caz, prima și a treia comandă au produs următoarele rezultate anonimizate:

```text
{
  "version": "2026.11.1",
  "update_available": false
}
running restarts=0
```

Apoi deschide tabloul de bord la adresa locală obișnuită și confirmă că se încarcă stările actuale. Păstrează fișierul HTTP salvat până când se termină un backup ulterior și funcționarea normală este verificată.

Dovezile de pe Yellow-ul meu nu au stabilit cauza primei actualizări eșuate. Nici mesajul de eșec al sarcinii ulterioare nu a identificat cauza. O versiune instalată și un tablou de bord funcțional confirmă mai bine starea rezultată decât mesajul CLI singur, dar niciunul nu explică de ce Supervisor a marcat sarcina drept eșuată.

## Pași următori

Dacă eroarea stocării HTTP persistă, inspectează fișierul păstrat și restaurează un backup compatibil sau rulează o versiune Core care îi poate citi versiunea de stocare. Restaurarea fișierului păstrat versiunea 3 sub versiunea mai veche Core repetă defecțiunea. Dacă Core ajunge la RUNNING, dar unele dispozitive rămân indisponibile, investighează separat acele integrări. Păstrează copia de recuperare și backupul cloud până când următorul backup se termină și tabloul de bord continuă să răspundă.

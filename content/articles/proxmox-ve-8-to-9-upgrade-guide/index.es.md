---
title: "Guía de actualización de Proxmox VE 8 a 9: actualización en sitio con script automatizado"
date: 2026-07-22
lastmod: 2026-07-22
toc: true
draft: false
description: "Guía completa para actualizar Proxmox VE 8 (Debian Bookworm) a Proxmox VE 9 (Debian Trixie). Cubre requisitos previos, actualización manual paso a paso, el script de automatización pve8to9-upgrade.sh, cambios importantes y problemas conocidos."
genre: ["Virtualización", "Administración Linux", "Proxmox", "Gestión de servidores", "Código abierto", "Homelab"]
tags: ["Proxmox VE 9", "actualización Proxmox", "PVE 8 a 9", "Debian Trixie", "Debian 13", "apt dist-upgrade", "pve8to9", "Proxmox Ceph", "proxmox-boot-tool", "grub-efi", "actualización LVM", "actualización ZFS", "NVIDIA vGPU", "cgroupv2", "automatización Proxmox", "script bash de actualización", "actualización de clúster Proxmox", "actualización en sitio", "pve8to9-upgrade.sh", "Proxmox VE 9.0"]
cover: "/img/cover/proxmox-ve-8-to-9-upgrade-guide-automation.webp"
coverAlt: "Una sala de servidores moderna con iconos luminosos que representan máquinas virtuales en pantallas. Un técnico trabaja en un portátil rodeado de equipos azul marino con acentos azules, verdes y morados."
coverCaption: "Actualización de Proxmox VE 8 a 9: actualización en sitio paso a paso con un script asistente automatizado."
canonical: "https://simeononsecurity.com/articles/proxmox-ve-8-to-9-upgrade-guide/"
---

**Proxmox VE 9 está basado en Debian 13 Trixie y se entrega con el kernel 6.14, QEMU 10, LXC 6 y ZFS 2.3.** Esta guía cubre tanto el proceso de actualización manual en sitio como un script bash automatizado que detecta su configuración y gestiona cada cambio de repositorio, problema conocido y verificación previa.

## Novedades de Proxmox VE 9

Proxmox VE 9 (publicado en agosto de 2025) es una actualización de versión mayor. Cambios clave:

| Componente | PVE 8 | PVE 9 |
|-----------|--------|--------|
| **Base Debian** | Bookworm (12) | Trixie (13) |
| **Kernel por defecto** | 6.8 | 6.14 |
| **QEMU** | 9.x | 10.x |
| **LXC** | 5.x | 6.x |
| **ZFS** | 2.2 | 2.3 |
| **Ceph** | Quincy / Reef / Squid | Squid (requerido) / Tentacle (opcional) |
| **cgroup** | cgroupv2 (v1 aún posible) | solo cgroupv2 |

**Nuevas funciones principales en PVE 9.0+:**
- Instantáneas de VM en LVM de aprovisionamiento grueso mediante cadenas de volúmenes (vista previa técnica en producción en 9.1)
- Reglas de afinidad de alta disponibilidad que reemplazan los grupos HA
- SDN Fabrics para redes Ceph OpenFabric y OSPF de malla completa
- Nueva interfaz web móvil (Rust/Yew)
- Expansión de dispositivos ZFS RAIDZ sin tiempo de inactividad
- Equilibrio de carga dinámico con el planificador de recursos del clúster (PVE 9.2)
- WireGuard y BGP como protocolos de fabric SDN (PVE 9.2)
- `/tmp` ahora es un `tmpfs` (cambio de Debian Trixie: archivos limpiados periódicamente)

______

## Antes de comenzar: requisitos previos

**Debe cumplir todos estos requisitos antes de tocar los repositorios.** Consulte la lista completa de requisitos previos en el [wiki oficial de actualización](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites).

### 1. Proxmox VE 8.4 como mínimo

```bash
pveversion
```

La salida debe mostrar `pve-manager/8.4.x` o superior. De lo contrario:

```bash
apt update && apt dist-upgrade
```

### 2. Ceph debe estar en Squid (19.x), solo para hiperconvergencia

```bash
ceph --version
```

La salida debe mostrar la versión 19.x (Squid). Si está en Reef (18.x) o Quincy (17.x), actualice primero Ceph. La ruta de actualización es siempre de un paso a la vez:

- Quincy (17) → Reef (18) → Squid (19)

*No proceda con la actualización a PVE 9 hasta que todos los nodos Ceph estén en Squid.*

### 3. Proxmox Backup Server coinstalado

Si PBS está instalado en el mismo nodo, actualice PBS 3 → 4 antes de tocar los repositorios de PVE. Ejecute `pbs3to4 --full` y resuelva primero todos los problemas.

### 4. Requisitos de acceso

- **Preferido**: acceso a consola mediante IPMI, iKVM o teclado físico. La sesión SSH se interrumpirá al reiniciar los servicios.
- **SSH**: use `tmux` o `screen` para que la actualización continúe si la conexión se interrumpe:
  ```bash
  tmux new -s upgrade
  ```

### 5. Espacio en disco

```bash
df -h /
```

Al menos **5 GB libres**, idealmente 10+ GB.

### 6. Copias de seguridad válidas

Realice copias de seguridad de todas las VM y contenedores en almacenamiento externo antes de continuar. Pruebe una restauración. Una copia de seguridad válida no es opcional.

______

## Cambios importantes que debe conocer

Léalos antes de actualizar. Varios requieren acción antes o después de la actualización.

### cgroup V1 ha desaparecido

PVE 9 no admite en absoluto el entorno cgroupv1 heredado. Si lo había habilitado previamente:

```bash
grep -E 'cgroup_no_v1|systemd.unified_cgroup_hierarchy=0' /proc/cmdline
```

Si eso devuelve algo, elimine el parámetro del kernel de `/etc/default/grub` y ejecute `update-grub` antes de actualizar.

**Impacto en los contenedores**: los contenedores que ejecutan systemd 230 o anterior (CentOS 7, Ubuntu 16.04) no iniciarán en PVE 9. Migre esas cargas de trabajo durante la ventana de soporte de PVE 8 (fin de vida julio de 2026).

### Grupos HA deprecados

Los grupos HA son reemplazados por reglas HA. Se migran automáticamente una vez que todos los nodos del clúster están en PVE 9. No se requiere acción manual, pero verifique después de actualizar el último nodo.

### Privilegio VM.Monitor eliminado

Los roles personalizados que referenciaban `VM.Monitor` necesitan actualización. Use `Sys.Audit` para el acceso básico al monitor KVM. El script `pve8to9` detecta los roles afectados.

### Nuevo privilegio: VM.Replicate

Crear o editar trabajos de replicación de almacenamiento ahora requiere `VM.Replicate` en `/vms/<vmid>`. Ajuste los roles personalizados si es necesario.

### Los contenedores LXC con privilegios requieren Sys.Modify

Crear nuevos contenedores con privilegios ahora requiere `Sys.Modify`. Restaurar un contenedor con privilegios existente en su lugar no lo requiere.

### systemd-sysctl ya no lee /etc/sysctl.conf

Cualquier configuración personalizada en `/etc/sysctl.conf` será ignorada silenciosamente después de la actualización. Migrela a `/etc/sysctl.d/<NN>-name.conf` antes de reiniciar.

```bash
# Verificar qué hay en sysctl.conf
grep -v '^\s*#\|^\s*$' /etc/sysctl.conf
```

### /tmp ahora es tmpfs

Debian Trixie monta `/tmp` como tmpfs (hasta el 50% de la RAM). Los archivos se limpian periódicamente mientras el sistema está en ejecución. Si usa `/tmp` para archivos temporales grandes, transfiera ese trabajo a `/var/tmp` o un punto de montaje dedicado.

### Veeam Backup defectuoso para versión de máquina QEMU >= 10.0

Proxmox cambió la forma en que los discos se conectan a QEMU internamente para la versión de máquina 10.0+. Veeam no se ha adaptado todavía. Fije las VM afectadas a la versión de máquina `9.2+pve1` antes de actualizar, o posponga la actualización si Veeam es crítico.

### Los nombres de interfaz de red pueden cambiar

El kernel 6.14 reconoce más funciones NIC que el 6.8. Algunas tarjetas NIC obtienen sufijos de nomenclatura adicionales. La herramienta `pve-network-interface-pinning` puede fijar todas las interfaces a nombres `nicX` estables antes de la actualización:

```bash
pve-network-interface-pinning --help
```

______

## Opción A: actualización manual en sitio

Siga los pasos oficiales de [pve.proxmox.com/wiki/Upgrade_from_8_to_9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9).

### Paso 1: ejecute la lista de verificación pve8to9

```bash
pve8to9 --full
```

Resuelva cada elemento `FAIL` antes de continuar. Vuelva a ejecutar después de cada corrección.

### Paso 2: migre las VM en ejecución (si está en un clúster)

```bash
qm migrate <vmid> <target-node>
pct migrate <ctid> <target-node>
```

### Paso 3: actualice PVE 8 completamente

```bash
apt update && apt dist-upgrade
pveversion   # debe mostrar 8.4.1 o más reciente
```

### Paso 4: actualice los repositorios base de Debian

```bash
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list
sed -i 's/bookworm/trixie/g' /etc/apt/sources.list.d/pve-enterprise.list
```

Comente o elimine las líneas de repositorio específicas de Bookworm restantes.

### Paso 5: agregue el repositorio de paquetes PVE 9

**Enterprise (requiere suscripción):**

```bash
cat > /etc/apt/sources.list.d/pve-enterprise.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/pve
Suites: trixie
Components: pve-enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

**Sin suscripción:**

```bash
cat > /etc/apt/sources.list.d/proxmox.sources << EOF
Types: deb
URIs: http://download.proxmox.com/debian/pve
Suites: trixie
Components: pve-no-subscription
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Verifique con `apt update && apt policy` que el nuevo repositorio aparece sin errores. Luego elimine o comente el archivo `.list` antiguo.

### Paso 6: actualice el repositorio de Ceph (solo hiperconvergencia)

```bash
cat > /etc/apt/sources.list.d/ceph.sources << EOF
Types: deb
URIs: https://enterprise.proxmox.com/debian/ceph-squid
Suites: trixie
Components: enterprise
Signed-By: /usr/share/keyrings/proxmox-archive-keyring.gpg
EOF
```

Use `http://download.proxmox.com/debian/ceph-squid` con `pve-no-subscription` para configuraciones sin suscripción.

### Paso 7: actualice el índice de paquetes

```bash
apt update
```

Verifique que no haya errores.

### Paso 8: ejecute el dist-upgrade

```bash
apt dist-upgrade
```

Esto tarda entre 5 y más de 60 minutos según la velocidad del almacenamiento. Durante la actualización:

- **`/etc/issue`**: mantenga su versión actual (seguro)
- **`/etc/lvm/lvm.conf`**: instale la versión del mantenedor (recomendado)
- **`/etc/ssh/sshd_config`**: instale la versión del mantenedor si no la ha personalizado
- **`/etc/default/grub`**: mantenga su versión actual si la ha personalizado
- **`/etc/chrony/chrony.conf`**: instale la versión del mantenedor si no está personalizada

### Paso 9: reinicie

```bash
reboot
```

Incluso si el kernel 6.14 ya estaba instalado como opción en PVE 8, el reinicio es necesario. El kernel se reconstruye con las toolchains de PVE 9.

### Paso 10: pasos posteriores a la actualización

```bash
# Vaciar caché del navegador: Ctrl+Mayús+R (o ⌘+Alt+R en macOS)
# Verificar todos los nodos del clúster:
pvesh get /nodes

# Para clústeres: los grupos HA migran automáticamente a reglas HA
# después de que todos los nodos estén en PVE 9
journalctl -eu pve-ha-crm  # verificar errores
```

______

## Opción B: script automatizado (pve8to9-upgrade.sh)

El proceso manual tiene muchos pasos condicionales que varían según la configuración. El script `pve8to9-upgrade.sh` los automatiza todos.

**Fuente del script:** [gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)

### Qué hace el script

El script gestiona la actualización completa automáticamente, incluyendo:

| Detección | Acción |
|-----------|--------|
| Repositorios enterprise vs. sin suscripción | Usa el tipo de repositorio **activamente habilitado**. No habilita enterprise en nodos sin suscripción. |
| Versión de Ceph | Bloquea si Quincy o Reef, muestra la guía de actualización de Ceph paso a paso |
| Tipo de repositorio de Ceph | Escribe un nuevo `ceph.sources` que coincide con su tipo de repositorio existente |
| Controlador NVIDIA vGPU | Bloquea si el controlador < 570.158.02 (mínimo GRID 18.3) |
| Passthrough de GPU NVIDIA | Advierte y genera recordatorio de prueba post-actualización |
| Repositorios CUDA | Actualiza `debian12` → `debian13` en las rutas URI |
| Metapaquete systemd-boot | Lo elimina (corrige el error de Debian #1110177 que interrumpe dist-upgrade) |
| Configuraciones personalizadas de `sysctl.conf` | Migra a `/etc/sysctl.d/99-pve8to9-migrated.conf` |
| Bloqueo de FRR post-up | Corrige `/etc/network/interfaces` antes del reinicio |
| `systemd-journald-audit.socket` | Deshabilita para evitar la inundación de registros durante la actualización |
| Problema grub UEFI + LVM | Instala `grub-efi-amd64` y escribe una hoja de referencia en `/root/` |
| Repositorios `bookworm` de terceros | Los comenta con un recordatorio de actualización |
| Conflicto `linux-image-amd64` | Lo elimina si está presente |
| Activación automática de LVM | Ejecuta el script de migración antes y después de la actualización |
| Proxmox Backup Server | Ejecuta la verificación `pbs3to4 --full`; actualiza los repositorios de PBS para Trixie |
| Raíz ZFS | Detecta y confirma (no se requiere acción especial) |

Todos los cambios se registran completamente en `/var/log/pve8to9-upgrade-<marca-de-tiempo>.log`.

### Instalación y uso

```bash
# Descargar el script
curl -fsSL https://gist.githubusercontent.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d/raw/pve8to9-upgrade.sh \
  -o pve8to9-upgrade.sh

# Hacer ejecutable
chmod +x pve8to9-upgrade.sh

# Revíselo antes de ejecutarlo (lea siempre los scripts antes de ejecutarlos como root)
less pve8to9-upgrade.sh
```

**Modos de ejecución:**

```bash
# Modo interactivo completo (recomendado)
./pve8to9-upgrade.sh

# Aprobar automáticamente todas las correcciones seguras y no destructivas
./pve8to9-upgrade.sh --yes

# Simulación: mostrar cada cambio sin aplicar nada
./pve8to9-upgrade.sh --dry-run

# Omitir el preflight pve8to9 --full (no recomendado)
./pve8to9-upgrade.sh --skip-preflight
```

*Ejecute dentro de `tmux` o `screen` si se conecta mediante SSH.*

### Verificaciones de seguridad bloqueantes del script

El script **se negará a continuar** si alguna de estas condiciones es verdadera:

- cgroup V1 está explícitamente habilitado en la línea de comandos del kernel
- Ceph todavía está en Quincy (17.x) o Reef (18.x). El script muestra los comandos exactos de actualización de Ceph.
- El controlador NVIDIA vGPU es inferior a la versión 570 (GRID 18.3)
- La versión de PVE es inferior a 8.4

Para cada problema bloqueante, el script imprime los comandos exactos para resolverlo antes de volver a ejecutar.

______

## Problemas conocidos de actualización

### GRUB no arranca desde LVM en modo UEFI

**Afecta**: sistemas con raíz en LVM, arrancando en modo UEFI, actualizados desde PVE 7.x

```bash
# Corrección (ejecutar en el sistema en vivo después de la actualización):
[ -d /sys/firmware/efi ] && apt install grub-efi-amd64
```

El script `pve8to9-upgrade.sh` detecta UEFI+LVM e instala esto automáticamente. También escribe una hoja de referencia de recuperación en `/root/GRUB-RECOVERY-CHEATSHEET.txt`.

**Si el nodo ya está bloqueado** en `grub rescue>` o "disk 'lvmid/...' not found":

1. Arranque el ISO de PVE → Avanzado → **Rescue Boot**
2. O siga la [sección Recover From Grub Failure — LVM](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM) en el wiki oficial

### El metapaquete systemd-boot interrumpe dist-upgrade

El metapaquete `systemd-boot` fue instalado automáticamente en todos los sistemas ISO PVE 8.1-8.4. En Trixie, contiene hooks que se activan al actualizar otros paquetes y pueden interrumpir `dist-upgrade` si el ESP no está montado (error de Debian #1110177).

```bash
# Elimínelo antes de dist-upgrade:
apt remove systemd-boot
# NO elimine systemd-boot-efi o systemd-boot-tools. Esos permanecen.
```

El script `pve8to9-upgrade.sh` gestiona esto automáticamente.

### Passthrough PCI a veces defectuoso con el kernel 6.14

Algunos usuarios informan que las VM con passthrough PCI no arrancan con el kernel 6.14. Si le afecta:

```bash
# Fije temporalmente el kernel anterior:
proxmox-boot-tool kernel pin 6.8.12-4-pve
```

### Las configuraciones de Ceph Full Mesh se bloquean al reiniciar

Si su `/etc/network/interfaces` contiene:

```
post-up /usr/bin/systemctl restart frr.service
```

Cámbielo a:

```
post-up /usr/bin/systemctl is-active --quiet frr.service && /usr/bin/systemctl restart frr.service || true
```

Haga esto **antes de reiniciar**. El script detecta y corrige este patrón automáticamente.

### El pool LVM Thin necesita reparación

En algunos sistemas después de la actualización:

```
Check of pool pve/data failed (status:64). Manual repair required!
```

Corrección:

```bash
lvconvert --repair pve/data
```

### Versión mínima del controlador NVIDIA vGPU

Debe ser al menos el **controlador 570.158.02** (GRID 18.3) antes de actualizar. Los controladores más antiguos son incompatibles con el kernel 6.x.

```bash
nvidia-smi --query-gpu=driver_version --format=csv,noheader
```

______

## Orden de actualización del clúster

Actualice los nodos de uno en uno. Verifique que cada nodo esté saludable antes de comenzar el siguiente.

```bash
# Verificar la salud del clúster antes de actualizar cada nodo:
pvecm status
ceph -s   # si Ceph está desplegado
```

**Reglas de migración durante actualizaciones parciales:**

- VM/CT de PVE 8 → PVE 9: siempre funciona
- VM/CT de PVE 9 → PVE 8: generalmente no admitido

Después de que todos los nodos estén en PVE 9, los grupos HA migran automáticamente a reglas de afinidad HA. Verifique si hay errores:

```bash
journalctl -eu pve-ha-crm
```

______

## Solución de problemas

### La actualización se bloquea / "proxmox-ve se eliminaría"

Si ve:
```
W: (pve-apt-hook) You are attempting to remove the meta-package 'proxmox-ve'!
```

Uno o más paquetes no se pueden actualizar porque todavía está configurado un repositorio Bookworm. Encuentre las entradas Bookworm restantes:

```bash
grep -r 'bookworm' /etc/apt/sources.list /etc/apt/sources.list.d/
```

Coméntelas y luego:

```bash
apt update && apt dist-upgrade
```

Si está parcialmente completo:

```bash
apt -f install
```

### Error al arrancar después de la actualización de ZFS

Si usa ZFS root con arranque BIOS heredado, consulte [ZFS: Switch Legacy-Boot to Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool). El `proxmox-boot-tool` debe gestionar el arranque en sistemas ZFS, no GRUB directamente, para sobrevivir a las actualizaciones de funciones ZFS.

______

## Lista de verificación posterior a la actualización

Después de reiniciar cada nodo:

- [ ] Vaciar caché del navegador (`Ctrl+Mayús+R` / `⌘+Alt+R`)
- [ ] `pveversion` muestra 9.x
- [ ] `uname -r` muestra 6.14.x o más reciente
- [ ] Todas las VM y CT arrancan correctamente
- [ ] Salud de Ceph: `ceph -s` muestra HEALTH_OK
- [ ] Si UEFI+LVM: verificar que el mtime de `grubx64.efi` sea reciente
- [ ] Si passthrough NVIDIA: probar una VM que no sea de producción
- [ ] Actualizar los repositorios de terceros comentados durante la actualización
- [ ] Mover la configuración personalizada de `/etc/sysctl.conf` a `/etc/sysctl.d/`

______

## Referencias

1. [Oficial: actualización de Proxmox VE de 8 a 9](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9)
2. [Oficial: actualización de 8 a 9 — requisitos previos](https://pve.proxmox.com/wiki/Upgrade_from_8_to_9#Prerequisites)
3. [Script de automatización pve8to9-upgrade.sh](https://gist.github.com/simeononsecurity/ba3831f487c4e960f9e218c7da5c4b8d)
4. [Problemas conocidos de Proxmox VE 9.0 (hoja de ruta)](https://pve.proxmox.com/wiki/Roadmap#9.0-known-issues)
5. [Recuperación tras fallo de Grub — error LVM "disk not found"](https://pve.proxmox.com/wiki/Recover_From_Grub_Failure#Recovering_from_grub_.22disk_not_found.22_error_when_booting_from_LVM)
6. [ZFS: cambiar de arranque heredado a Proxmox Boot Tool](https://pve.proxmox.com/wiki/ZFS:_Switch_Legacy-Boot_to_Proxmox_Boot_Tool)
7. [Guía de actualización de Ceph Reef a Squid](https://pve.proxmox.com/wiki/Ceph_Reef_to_Squid)
8. [Fijación de interfaces de red de Proxmox](https://pve.proxmox.com/pve-docs/chapter-sysadmin.html)
9. [Notas de versión de Debian 13 Trixie](https://www.debian.org/releases/trixie/releasenotes)

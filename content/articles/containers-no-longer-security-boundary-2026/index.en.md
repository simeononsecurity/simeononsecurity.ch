---
title: "Containers Are No Longer a Security Boundary: Kernel Escapes in 2026"
date: 2026-09-28
lastmod: 2026-09-28
toc: true
draft: false
description: "AI-driven kernel bug hunting produced four new local privilege escalation families in 2026, all of which escape containers. Here is how they work, why patching is losing ground, and where microVMs fit."
genre: ["Container Security", "Linux", "Kernel Security", "Virtualization", "Cloud Security", "Threat Research", "Blue Team", "DevSecOps"]
tags: ["container escape", "container security boundary", "linux kernel cve", "local privilege escalation", "lpe 2026", "copy fail", "cve-2026-31431", "dirty frag", "cve-2026-43284", "cve-2026-43500", "fragnesia", "cve-2026-46300", "cve-2026-80521", "kernelctf", "kvmctf", "microvm", "firecracker", "kata containers", "page cache corruption", "af_alg", "af_unix", "xfrm esp", "rxrpc", "namespace isolation", "clone syscall", "ai vulnerability discovery", "docker security", "kubernetes security", "multi-tenant isolation", "sandbox escape", "nsjail", "bubblewrap", "firejail", "dirty pipe", "kernel cve trend"]
cover: "/img/cover/container-security-vulnerabilities-kernel-escapes-2026.webp"
coverAlt: "A digital illustration showing multiple glowing containers connected to a central kernel symbol, with colorful visual elements representing security vulnerabilities radiating from the kernel against a dark background."
coverCaption: ""
ref: ["/articles/docker-vs-vms", "/articles/how-to-secure-your-docker-and-kubernetes-environment", "/cvss-calculator"]
---

**Containers share one kernel, and in 2026 four separate vulnerability families proved a single kernel bug is enough to walk out of a container and onto the host.** Copy Fail, Dirty Frag, Fragnesia, and CVE-2026-80521 each grant root to an unprivileged local user, and every one of them crosses the container boundary.

*The uncomfortable part is not the bugs themselves. It is how cheaply AI now finds them, and how one patch created another.*

This article explains how containers isolate workloads, why the isolation now rests on a shrinking foundation, what each 2026 vulnerability does, and which isolation technology is worth trusting instead.

## The Short Answer

| Question | Short Answer |
|---|---|
| **Do containers isolate?** | Yes, for process and filesystem separation. All containers share one kernel, so kernel bugs are a shared risk |
| **Why now?** | AI-assisted bug hunting collapsed the cost of finding kernel flaws. Nearly **6,000 kernel CVEs** are published as of September 2026 |
| **What breaks the boundary?** | Any local privilege escalation in the kernel. Escaping needs no container misconfiguration |
| **Is patching enough?** | It is necessary and it is losing the race. One 2026 patch **introduced a new exploitable bug** |
| **What works better?** | MicroVMs such as Firecracker or Kata Containers, which give each workload its own kernel |
| **Is the alternative perfect?** | No. The hypervisor is code too. The attack surface is orders of magnitude smaller, and the difference is the point |

## How Containers Isolate

Understanding the boundary starts with understanding what a container is not.

**A container is not a virtual machine.** There is no second kernel, no emulated hardware, and no hypervisor between your process and the metal. When you run a container image, you are running a process on your existing kernel with a modified view of the system.

The mechanism is the **`clone` syscall**. Where `fork` copies a process address space, `clone` creates a child process while giving the caller precise control over which pieces of execution context get shared and which get replaced. Docker passes `clone` a set of **namespaces**:

| Namespace | What It Fakes |
|---|---|
| **Mount** | A private filesystem root, so the container sees its own tree instead of yours |
| **PID** | Its own process numbering, so `PID 1` is the container's first process, not `systemd` |
| **User** | An identity mapping where container "root" maps to an unprivileged host user |
| **Network** | Private interfaces, routing tables, and ports |
| **IPC** | Isolated shared memory and message queues |
| **UTS** | Its own hostname and domain name |
| **Cgroup** | A private view of resource limits |

Add a **union filesystem** layered over an image, and the result *feels* like a separate computer. `id` inside the container reports `uid=0(root)`. The filesystem looks like a minimal Ubuntu. A process listing shows only its own processes.

**None of this is a security boundary at the syscall level.** When a process inside the container opens a file, allocates memory, or touches a network socket, the same kernel handles the request for every other container on the host. Namespaces change *what the process sees*, not *what the kernel will do for it*.

*The kernel is the real boundary between container and host. Everything else is presentation.*

{{< figure src="container-namespace-isolation-shared-kernel.webp" alt="Diagram showing three containers built from the same kernel, with mount, PID, user, and network namespaces separating their views while all syscalls still route to one shared kernel underneath" >}}

{{< youtube id="9-2CSJC114k" enable="true" title="the change is finally coming" nocookie="true" >}}

## The Boundary Is Code, and Code Has Bugs

Every action a container performs goes through the **syscall interface**. Opening a file, reading memory, writing to a socket, changing a UID: the kernel mediates all of it, because the kernel does not want processes touching the CPU, the filesystem, or the network directly.

The mediation is the security model, and mediation is implemented as code. Specifically, it is roughly **30 million lines** of it.

A local privilege escalation (LPE) is what happens when a process exploits a flaw in the mediating code to gain privileges it was never granted. **LPEs are not new.** They have existed since the earliest kernel mediation, and the industry lived with a steady trickle of them for decades.

**Dirty Pipe in 2022** is the reference point most people know. It abused a flaw in pipe buffer handling to overwrite read-only files, and it was treated as breaking news because bugs of such severity arrived **roughly once a year or two**. You patched, you moved on, and the assumption held: no large defect sat undiscovered in code a million people read.

*The assumption no longer holds.*

## What Changed in 2026

The change is not attacker skill. It is how **finding kernel memory-corruption bugs became an engineering task instead of a research career**.

Three data points from this year make the shift concrete:

| Finding | Who Found It | How |
|---|---|---|
| **Copy Fail** (CVE-2026-31431) | Taeyang Lee, Theori | Assisted by **Xint Code**, an AI static analysis tool. Roughly **one hour of scan time** against the Linux crypto subsystem |
| **CVE-2026-80521** | Zhenpeng (Leo) Lin, DepthFirst | Found with **dfs-large1**, an in-house AI model trained for vulnerability detection |
| **CVE-2026-80521**, independently | Kyle, **OpenAI** | The same bug, found separately, reported the same day |

Read the third row again. Two organizations using different AI tooling arrived at **the same AF_UNIX use-after-free** and reported it to `security@kernel.org` on the **same day**. This is not a coincidence of talent. It is a repeatable process producing the same answer twice.

DepthFirst states the scale directly: **nearly 6,000 kernel CVEs published as of September 2026**. The count climbs on a curve tracking the availability of AI assistance, not the number of kernel developers.

*When one hour of AI scan time finds a decade-old bug in the crypto subsystem, the economics of kernel exploitation have inverted.*

## Four Escapes, One Year

Each of these grants root from an unprivileged local account. None requires a container misconfiguration, a privileged flag, or a network foothold.

| Vulnerability | CVE | Subsystem | Primitive | Found By |
|---|---|---|---|---|
| **Copy Fail** | CVE-2026-31431 | `algif_aead` / AF_ALG | 4-byte write into any readable file's page cache | Theori, AI-assisted |
| **Dirty Frag** | CVE-2026-43284 + CVE-2026-43500 | XFRM ESP, RxRPC | 4-byte page-cache write via two chained variants | Hyunwoo Kim |
| **Fragnesia** | CVE-2026-46300 | XFRM ESP-in-TCP | Single-byte page-cache writes | Hyunwoo Kim |
| **AF_UNIX UAF** | CVE-2026-80521 | AF_UNIX sockets | Use-after-free in `unix_vertex` garbage collection | DepthFirst, AI-assisted |

All four share a design pattern worth noticing. **They attack the page cache rather than the disk.**

### Copy Fail: A Logic Flaw With No Race

Copy Fail is the cleanest of the four, and the most alarming.

Almost every Linux LPE needs a timing window or a kernel-specific memory offset. **Copy Fail needs neither.** It is a straight-line logic flaw in `algif_aead`, the module providing userspace access to authenticated encryption through AF_ALG.

The chain runs `splice()` to place a page-cache page into the operation, then abuses the in-place AEAD path to write **four controlled bytes** into that page. The corrupted page is **never marked dirty**, so it is never written back to disk. The file on disk stays pristine, which means checksum and integrity verification pass while the in-memory copy carries your modification.

One **732-byte Python script** roots every Linux distribution released since 2017. The bug was introduced by a **2017 optimization** to `algif_aead`, and the 2026 patch simply reverts the optimization. Mainline commit `a664bf3d603d`.

*The bug sat in every mainstream distribution for nearly a decade, and an AI tool found it in about an hour.*

### Dirty Frag: Two Variants Which Cover Each Other

Dirty Frag describes its own lineage precisely. **Dirty Pipe overwrites `struct pipe_buffer`. Dirty Frag overwrites the `frag` of `struct sk_buff`.**

It is **two vulnerabilities chained**, and the chaining is the clever part:

- **CVE-2026-43284** abuses `esp_input()` skipping the copy-on-write path before running in-place decryption on a spliced fragment. It requires the privilege to create a **user namespace**, which some distributions restrict.
- **CVE-2026-43500** abuses `rxkad_verify_packet_1()` performing an in-place decrypt on the fragment. It needs no namespace privilege, but the `rxrpc` module is missing from most distributions. Ubuntu loads it by default.

**Either variant alone has a blind spot. Together they cover each other.** Where user namespaces are allowed, the ESP path runs first. Where it is blocked but `rxrpc` is present, the RxRPC path runs instead. One exploit binary then works across distributions, and the RxRPC variant reaches root by blanking a field in `/etc/passwd` and letting PAM's `nullok` accept an empty password.

**The finding which matters most for defenders:** Dirty Frag triggers **regardless of `algif_aead` availability**. The widely circulated Copy Fail mitigation, which blacklists the module, **does not protect against Dirty Frag at all.**

### Fragnesia: The Patch Which Created a Bug

Fragnesia is the same class as Dirty Frag, aimed at the XFRM **ESP-in-TCP** path, and it is the most instructive entry in the set.

The vulnerability exploits improper handling of shared page fragments during `skb` coalescing. An attacker splices file-backed pages into a TCP receive queue before the socket switches into `espintcp` upper-layer-protocol mode. Once ESP processing activates, the kernel decrypts the queued data **in place**, and AES-GCM keystream manipulation corrupts the underlying page cache. The attacker gains repeated **single-byte writes** into cached file pages.

The exploit reaches root by overwriting the first bytes of `/usr/bin/su` with a small ELF payload. **The change exists only in memory and never touches the on-disk binary.**

Unprivileged **user and network namespaces** provide `CAP_NET_ADMIN` inside an isolated namespace, then NETLINK_XFRM installs a crafted security association.

*Here is the sentence to sit with:* Fragnesia emerged as **an unintended side effect of one of the patches for the original Dirty Frag vulnerabilities**. Patching Dirty Frag produced a new, independently exploitable root bug.

### CVE-2026-80521: The Container Escape Which Won kernelCTF

The AF_UNIX race is the one which removes any argument this is theoretical.

The vulnerability is a **heap use-after-free** in the garbage collection mechanism for `SCM_RIGHTS` messages, which is how processes pass file descriptors to each other. A race during collection of a circular socket reference frees a `struct unix_vertex` while a surviving socket's SCC ring still holds a pointer to it. The next collection pass walks the stale ring and dereferences freed memory.

The reason it matters beyond Linux generally: **AF_UNIX underpins local IPC.** Local databases, `systemd`, and Docker itself all depend on it. DepthFirst notes the vulnerability impacts most OS-level sandboxes built on the kernel, **including `nsjail`, `Firejail`, and `Bubblewrap`**, plus modern container runtimes.

DepthFirst won a **Google kernelCTF slot** with it on **July 24, 2026**, received confirmation in the `lts-6.12.95` slot on **August 5**, reported it to `security@kernel.org` the same day, and learned **Kyle from OpenAI had reported the same bug.** The upstream patch landed **August 6**. Research published **September 22**.

They released a working exploit targeting **Ubuntu 26.04**, plus a second exploit for CVE-2026-52910 escaping **Ubuntu 24.04**.

{{< figure src="kernel-page-cache-overwrite-container-escape.webp" alt="Diagram showing an unprivileged process inside a container corrupting a page-cache page to modify a setuid binary in memory, escalating to root and stepping outside the container boundary onto the host kernel" >}}

## Why the Mitigation Advice Keeps Failing

Defenders have been handed three rounds of workarounds this year, and each one has been partially wrong.

| Mitigation | What It Stops | What It Misses |
|---|---|---|
| Blacklist **`algif_aead`** | Copy Fail | **Nothing in Dirty Frag**, which ignores the module entirely |
| Blacklist **`esp4`, `esp6`, `rxrpc`** | Dirty Frag, Fragnesia | Teams needing IPsec. Also misses entirely new subsystems |
| Restrict **unprivileged user namespaces** | The ESP variants | The RxRPC variant needs no namespace. AppArmor policy is a **partial** mitigation only |
| **Patch the kernel** | The patched bug | The next bug, and any bug a patch introduces |

Two patterns stand out.

**First, the workarounds conflict with each other.** Copy Fail is mitigated by disabling `algif_aead`. Dirty Frag explicitly triggers **whether or not** the module exists. Fragnesia needs `esp4` and `esp6` disabled, which is a problem for anyone running IPsec. There is no single module blacklist covering the family.

**Second, and worse, patching is not a clean win.** Fragnesia was introduced **by the patch for Dirty Frag**. Every patch carries risk of new logic errors, and in this subsystem a logic error becomes a root exploit.

*The uncomfortable conclusion: these vulnerabilities are all in the page cache, all reachable from unprivileged code, and all found by tooling which improves every quarter. No blocklist stays complete.*

## The Counter-Argument, Answered Honestly

There is a fair objection, and it deserves a straight answer: **hypervisors have bugs too.**

The KVM attack surface is real. Google runs **kvmCTF** specifically because it wants those bugs found, and the program pays generously for them:

| Tier | Reward |
|---|---|
| **Full VM escape** | **$250,000** |
| Arbitrary memory write | $100,000 |
| Arbitrary memory read | $50,000 |
| Relative memory write | $50,000 |
| Denial of Service | $20,000 |
| Relative memory read | $10,000 |

Awards do not stack, the target is a Linux LTS kernel with KVM, and the guest is Debian 12.5. The goal is a **guest-to-host attack**.

**Hyunwoo Kim, the same researcher who found Dirty Frag, also collects KVM bounties** and has won the full $250,000 for a VM escape. So the honest summary: both layers have flaws, and the person finding them is sometimes the same person.

**But compare the scales:**

| | Linux Kernel | KVM Hypervisor |
|---|---|---|
| **CVEs in 2026** | Nearly **6,000** | A handful, with individual researchers finding a few per year |
| **Reachable from** | Any unprivileged process, through the syscall interface | Only by code already running inside a guest |
| **Attack surface** | Everything: networking, filesystems, crypto, IPC, drivers | The virtual device and hypercall interface |
| **Bug class** | Any memory-safety or logic flaw in 30M lines | Confined to the virtualization boundary |

*The difference is orders of magnitude, not a factor of two. The gap is why microVMs change the risk calculus.*

## What Provides a Real Boundary

A **microVM** gives each workload its own **kernel instance** running on hardware-enforced virtualization, rather than sharing the host kernel through namespaces.

The stack has three layers worth naming:

- **The CPU** provides hardware mechanisms to isolate one memory region from another.
- **KVM** exposes those mechanisms to the Linux kernel, so the kernel acts as a hypervisor.
- **A VMM (virtual machine monitor)**, such as Firecracker or QEMU, drives KVM to create and run the guest.

Because the guest runs its own kernel, a kernel exploit **inside the guest** compromises only the guest. There is no shared kernel to attack. An attacker must then escape the hypervisor itself, which is the smaller surface KVM bugs occupy.

Two implementations matter in practice, and both are named in DepthFirst's recommendation:

| Technology | Approach | Notes |
|---|---|---|
| **Firecracker** | Purpose-built VMM, minimal device model | AWS-built, designed specifically for multi-tenant isolation at scale |
| **Kata Containers** | OCI-compatible runtime wrapping a microVM | Runs standard container images with a VM boundary underneath |

Kata is the easier migration for most teams, because it accepts the container images and tooling already in use. **Firecracker is the smaller attack surface**, because it implements far less device emulation than a general-purpose VMM.

{{< figure src="microvm-vs-container-isolation-boundary.webp" alt="Diagram comparing container isolation through shared kernel namespaces against microVM isolation where each workload runs its own kernel on top of KVM and a virtual machine monitor" >}}

## What To Do Now

Not every container needs a microVM. The decision hinges on **whose code runs inside it**.

| Your Situation | Risk | What To Do |
|---|---|---|
| **You run your own code**, single tenant | Low | Keep containers. Patch promptly, drop capabilities, keep a read-only root filesystem |
| **Multi-tenant hosts**, shell access for users | **High** | Move untrusted workloads to microVMs. This is the case DepthFirst calls out first |
| **CI runners executing untrusted PRs** | **High** | A pull request becomes root on the runner. Isolate each job in its own VM |
| **Notebooks, agent sandboxes, serverless** | **High** | Tenant code becomes host root. MicroVM per tenant |
| **Kubernetes clusters** | **Elevated** | The page cache is shared across the host. A pod with the right primitives compromises the node and crosses tenant boundaries |

The unifying principle is simple. **Containers are an excellent packaging and process-isolation tool.** They were never designed to contain hostile code, and the industry quietly borrowed them for the job because they were convenient and cheap.

### Hardening Which Helps Regardless

None of this substitutes for a VM boundary, and all of it removes easy paths:

```bash
# Disable the modules the page-cache family abuses, where they are not needed
printf 'install algif_aead /bin/false\ninstall esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' \
  > /etc/modprobe.d/harden-pagecache-family.conf
rmmod algif_aead esp4 esp6 rxrpc 2>/dev/null || true
```

```bash
# Restrict unprivileged user namespaces, which gates the ESP variants
# Debian and Ubuntu: this is a partial mitigation, not a complete one
sysctl -w kernel.unprivileged_userns_clone=0

# If exploitation is suspected, drop the page cache to discard modified in-memory binaries
echo 1 | tee /proc/sys/vm/drop_caches
```

```text
# Detection starting points
- Unexpected unshare(CLONE_NEWUSER) from a workload with no legitimate reason
- NETLINK_XFRM activity, or XFRM security associations appearing outside IPsec hosts
- Requests to bind AF_ALG sockets
- Loads of esp4, esp6, or rxrpc on hosts running neither IPsec nor AFS
```

> **Warning: `drop_caches` discards the modified in-memory copy, which clears the corruption, but it does not remove an attacker who already reached root. Treat it as incident response, not remediation.**

### The Patching Cadence Problem

Even with the best intentions, kernel patching has become a race:

- Nearly **6,000 CVEs** published this year means the volume alone outpaces most maintenance windows.
- **A patch introduces a bug.** Fragnesia proved it, in this exact subsystem.
- **The mitigation list expires.** `algif_aead` was the answer in April. By May it covered nothing in Dirty Frag.

*Speed of patching is necessary and insufficient. The architecture decides whether a missed patch is a contained incident or a host compromise.*

## The Harder Question: Who Is the Adversary?

The technical answer is clear. The strategic answer depends on a question most teams skip.

**If your threat model is a curious user or a careless developer, containers remain adequate.** A container escape requires local code execution plus a kernel exploit. Neither is casual, and the operational cost of moving everything to microVMs is real.

**If your threat model includes an adversary who runs code on your infrastructure, containers are now a speed bump.** DepthFirst's conclusion is worth quoting rather than paraphrasing:

> "The barrier to entry for weaponizing these vulnerabilities has dropped so significantly that we must assume attackers already have the capability to escape standard containers at will."

This is a security vendor with a product to sell arguing for a specific architecture, and the skepticism it deserves is fair. **The argument does not depend on the vendor, though.** The 6,000 CVE count is public, the exploits are published, and the kernel is shared by design.

*The honest framing: containers are a boundary of decreasing value against an attacker with a foothold, and a boundary of undiminished value against everything else.*

## The Verdict

**Containers remain the right tool for packaging, deployment, and process separation. They are no longer a reliable security boundary against hostile code.**

Three claims, ordered by confidence:

1. **The technical premise is settled.** Containers share the host kernel. Every one of the four vulnerabilities in this article escaped the boundary from an unprivileged account, and the exploits are public.

2. **AI changed the pace, not the principle.** Kernel LPEs have always existed. Finding one now costs roughly **an hour of AI scan time** instead of months of expert effort, and two organizations independently found the same zero-day on the same day.

3. **The migration is a real cost, and so is not migrating.** Firecracker and Kata both add overhead, operational complexity, and a new set of skills. The trade is straightforward: accept the overhead, or accept that a kernel bug is a host compromise.

**If you run multi-tenant infrastructure or execute untrusted code, start planning the microVM migration now.** Not because the sky is falling, but because the trajectory is unambiguous and the migration takes quarters rather than weeks.

**If you run single-tenant containers of your own code, keep them.** Patch the kernel faster than you are used to, disable the modules you do not need, and revisit the decision when untrusted code enters the picture.

*The era of treating the kernel as an unconditionally trusted boundary is ending. Infrastructure which assumes the kernel will be breached is infrastructure which survives the breach.*

## Key Takeaways

- **Containers share the host kernel.** Isolation comes from `clone` syscall namespaces, not hardware virtualization, so a kernel bug is a container bug.
- **Four 2026 vulnerabilities escaped the boundary** from unprivileged local accounts: Copy Fail, Dirty Frag, Fragnesia, and CVE-2026-80521. All four target the page cache.
- **Nearly 6,000 kernel CVEs** were published as of September 2026, and AI tooling is the accelerant. **Copy Fail was found in about an hour** of AI scan time.
- **Fragnesia was introduced by the patch for Dirty Frag.** Patching produced a new root bug in the same subsystem.
- **The Copy Fail workaround does not stop Dirty Frag.** Blacklisting `algif_aead` covers one vulnerability and nothing else in the family.
- **CVE-2026-80521 also broke `nsjail`, `Firejail`, and `Bubblewrap`**, not only container runtimes.
- **MicroVMs change the risk calculus** by giving each workload its own kernel. KVM has bugs, but the surface is orders of magnitude smaller.
- **Choose based on who runs the code.** Your own code in a single-tenant container is a low risk. Untrusted code on a shared host is a host-compromise risk.

## Next Steps

1. **Read the analysis framing the problem** and its published exploit: **[Containers Are No Longer a Security Boundary - DepthFirst](https://depthfirst.com/research/containers-are-no-longer-safe)**
2. **Check the authoritative advisory and mitigation guidance** for the Copy Fail family: **[CERT/CC VU#260001](https://www.kb.cert.org/vuls/id/260001/)**
3. **Read the Dirty Frag write-up** to understand the chaining and why the `algif_aead` mitigation fails: **[Dirty Frag technical write-up](https://github.com/V4bel/dirtyfrag)**
4. **Review the kvmCTF rules and reward tiers** to see the size of the hypervisor attack surface: **[kvmCTF Overview](https://google.github.io/security-research/kvmctf/rules.html)**
5. **Score these CVEs in your own environment** with our client-side tool: **[CVSS v3.1 Calculator](/cvss-calculator/)**
6. **Harden what you run now**: **[How to Secure Your Docker and Kubernetes Environment](/articles/how-to-secure-your-docker-and-kubernetes-environment/)**
7. **Understand the isolation trade-off in depth**: **[Docker vs Virtual Machines 2026](/articles/docker-vs-vms/)**
8. **Reduce privilege wherever you cannot add a boundary**: **[Mastering Least Privilege Access Control on Linux](/articles/mastering-least-privilege-access-control-linux/)**

## Related Articles

| Article | What It Covers |
|---|---|
| **[Docker vs Virtual Machines 2026](/articles/docker-vs-vms/)** | The architectural comparison underpinning this article, including performance and security trade-offs |
| **[How to Secure Your Docker and Kubernetes Environment](/articles/how-to-secure-your-docker-and-kubernetes-environment/)** | Practical hardening for the container layer, still worth doing inside a microVM |
| **[Docker in LXC on Proxmox: Reliability, Evidence, and VM Migration](/articles/docker-in-lxc-proxmox-reliability/)** | Nesting containers, with evidence, and when to move a workload to a full VM |
| **[Understanding Virtualization: Concepts and Applications](/articles/understanding-virtualization_-concepts-and-applications/)** | Hypervisor fundamentals, including the CPU features microVMs depend on |
| **[Mastering Least Privilege Access Control on Linux](/articles/mastering-least-privilege-access-control-linux/)** | Reducing the privileges an escape would grant, which limits blast radius |

## References

1. [Containers Are No Longer a Security Boundary - DepthFirst (Zhenpeng Lin, September 22, 2026)](https://depthfirst.com/research/containers-are-no-longer-safe)
2. [CERT/CC Vulnerability Note VU#260001 - Copy Fail (CVE-2026-31431)](https://www.kb.cert.org/vuls/id/260001/)
3. [Copy Fail official disclosure site and exploit analysis](https://copy.fail/)
4. [Dirty Frag technical write-up - Hyunwoo Kim (CVE-2026-43284, CVE-2026-43500)](https://github.com/V4bel/dirtyfrag)
5. [Fragnesia: Linux Kernel Local Privilege Escalation via ESP-in-TCP - Wiz (CVE-2026-46300)](https://www.wiz.io/blog/fragnesia-linux-kernel-local-privilege-escalation-via-esp-in-tcp)
6. [kvmCTF Overview and reward tiers - Google](https://google.github.io/security-research/kvmctf/rules.html)
7. [NVD entry for CVE-2026-31431](https://nvd.nist.gov/vuln/detail/CVE-2026-31431)
8. [Upstream mainline fix commit for Copy Fail](https://github.com/torvalds/linux/commit/a664bf3d603dc3bdcf9ae47cc21e0daec706d7a5)
9. [Ubuntu security notice for Copy Fail](https://ubuntu.com/blog/copy-fail-vulnerability-fixes-available)
10. [KernelCTF exploits and submissions - Google security research](https://github.com/google/security-research/tree/master/pocs/linux/kernelctf)
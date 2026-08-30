---
title: "HackTheBox - Sherlock - PhantomRing"
date: 2026-08-28
draft: false
toc: true
description: "A walkthrough of the PhantomRing Sherlock on HackTheBox: statically analyzing a Linux ELF agent with file, nm, strings, and objdump to pull the C2 details, privesc checks, and self-destruct logic without ever running the binary."
tags: ["HackTheBox", "Sherlock", "DFIR", "Malware Analysis", "Static Analysis", "ELF", "objdump", "strings", "nm", "sha256sum", "io_uring", "eBPF", "SUID", "CTF", "Linux malware", "reverse engineering"]
cover: "/img/cover/hackthebox-sherlock-phantomring-malware-analysis.webp"
coverAlt: "A dark, moody illustration of a terminal window displaying disassembly output and a glowing padlock icon, representing static malware analysis of a Linux ELF binary."
coverCaption: ""
---

PhantomRing is one of the Sherlock boxes on HackTheBox, which is their forensics/malware-analysis line rather than the usual "pop a shell" Machines. You get a zip, a short scenario, and a set of questions to answer from evidence in that zip. This one hands you a single Linux binary and asks you to figure out what it does without running it, since it's a real (if simple) piece of post-exploitation malware.

______

## Provided Files:

You get `phantomring.zip`, password protected, containing one file:

```
phantom_ring/agent
```

The scenario is basically: a SOC team found this binary sitting in `/var/tmp` on a box, it was making outbound connections, and you need to work out what it's capable of and pull out IOCs, all through static analysis.

## Walk Through:

First thing, don't run it. It's live malware, so everything below is read-only inspection.

### Cracking the zip

The zip has a password on it. I checked what was actually inside first with `unzip -l phantomring.zip` before bothering to crack it, just so I knew what filename and size I was looking for once it was open. Threw it at `fcrackzip` with a wordlist and it popped quickly since the password wasn't anything exotic.

### Basic triage

Once extracted, start with the boring stuff:

```bash
file phantom_ring/agent
```

```text
phantom_ring/agent: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV),
dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2,
BuildID[sha1]=<build id>,
for GNU/Linux 3.2.0, not stripped
```

Not stripped is the important bit here. That means the symbol table is still in the binary, so function names survive. Grab the hash while you're at it since it's usually one of the scored questions on these:

```bash
sha256sum phantom_ring/agent
```

### Looking at the symbols before touching the disassembler

```bash
nm phantom_ring/agent | grep ' T \| t '
```

This lists every function name in the binary. Because it wasn't stripped, you get real names instead of `sub_401230`-style garbage. Scanning through, a few things stand out immediately:

- A bunch of helper functions with names built around `io_uring` (`read_file_uring` and similar). That's your answer for how it's doing file I/O under the hood, and it's relevant later because `io_uring` is a known way malware avoids normal syscall-based EDR hooks, since a lot of monitoring tools still only watch the classic `read`/`write`/`open` syscalls.
- A pile of `cmd_*` functions, plus `process_cmd` and `main`. That's the command handler layout right there, one function per capability (this is a good example of a case where you don't need to read a single line of disassembly to know the binary's basic shape).

I used this list as a map for the rest of the analysis, jumping straight to whichever `cmd_*` function was relevant instead of reading the whole disassembly top to bottom.

### Pulling strings

```bash
strings -n 4 phantom_ring/agent
```

This is always worth doing early since it's free and this binary didn't bother hiding anything. Scrolling through the output you get a good chunk of the picture right away: file paths it touches, log-style messages, and a plain IPv4 address sitting in there in the clear, which is the C2 address. You also get command tokens the binary compares input against, a path used for reading logged-in users, a SUID scan directory, some `/sys/kernel/debug/tracing/` paths, and a `/sys/fs/bpf` reference alongside `/proc/%s/maps`, which is a strong hint it's checking for eBPF-based monitoring tools running on the box.

What `strings` doesn't give you is the port number, the reconnect delay, or the exact number of distinct commands, since those are just numbers sitting in the instructions rather than printable text. For that you need to actually look at the disassembly.

### Digging into the disassembly

```bash
objdump -d --no-show-raw-insn phantom_ring/agent > disasm.txt
```

Using the symbol names from `nm` as landmarks, I jumped into `main()` first to find the connect logic. Right before the `connect` call there's a `htons` call with a hardcoded 16-bit value getting loaded in just before it, that's your port. On the retry path (after the "trying to reconnect" string), there's a small constant getting passed straight into `sleep`, which is your back-off delay.

For the command count, `process_cmd` is just a chain of `strcmp`/`strncmp` calls against string literals, each one branching off to a `cmd_*` handler if it matches, falling through to a "command not found" message if nothing does. I walked through each comparison and wrote down which literal jumped to which handler. Worth noting: a couple of the literal command names actually point at the exact same handler function, so the number of distinct commands is smaller than the number of command strings. Easy to miss if you just count strings instead of tracing where each branch actually goes.

The SUID and eBPF handlers were straightforward once I was in the right function: one calls `opendir` on a hardcoded path (the privesc scan directory), and the other builds a path under `/proc/<pid>/maps`, reads it, then runs `strstr` looking for a specific substring tied to eBPF map objects. There's also a small array of tracing-related file paths under `/sys/kernel/debug/tracing/` that it loops through and tries to disable one at a time, in a fixed order, so whichever one is first in that array is the one it tries first.

Self-destruct works the same way as everything else here: it calls `readlink` on `/proc/self/exe` to find its own path on disk, then `unlinkat` to delete itself. The trigger for that is just another literal string compared in `process_cmd` like every other command.

One annoyance: because this binary was built with the hardened PLT stubs (`.plt.sec`), `objdump` doesn't always print a friendly function name next to indirect calls, just an offset. If you want to confirm a call is really going to, say, `opendir` and not something else, cross-reference the offset against the relocation table:

```bash
objdump -R phantom_ring/agent
```

That gives you the GOT offset to symbol name mapping directly, so you can match it against what the disassembly is calling.

I also went back and checked the raw bytes in `.rodata` for the couple of strings that mattered most (the command list and the tracing-file array), just to be sure the order I recorded from the disassembly actually matched the order the strings are laid out in memory:

```bash
objdump -s -j .rodata phantom_ring/agent
```

Between `nm`, `strings`, and a focused pass through `objdump -d`, that's everything you need to answer every question in this Sherlock: the hash, the C2 IP and port, the reconnect delay, the real command count, the kernel interface it leans on for evasion, the login-enumeration file, the SUID scan directory, the eBPF detection string, the first tracing file it disables, the self-location path, and the self-destruct trigger string.

______

*Analysis done entirely through static inspection (`file`, `sha256sum`, `nm`, `objdump`, `strings`). The binary was never executed.*

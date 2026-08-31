---
title: "HackTheBox - Sherlock - PhantomRing"
date: 2026-08-28
draft: false
toc: true
description: "A walkthrough of the PhantomRing Sherlock on HackTheBox: statically analyzing a Linux ELF agent with file, nm, strings, and objdump to pull the C2 details, privesc checks, and self-destruct logic without ever running the binary."
tags: ["HackTheBox", "Sherlock", "DFIR", "Malware Analysis", "Static Analysis", "ELF", "objdump", "strings", "nm", "sha256sum", "EDR evasion", "eBPF", "SUID", "CTF", "Linux malware", "reverse engineering"]
cover: "/img/cover/hackthebox-sherlock-phantomring-malware-analysis.webp"
coverAlt: "A dark, moody illustration of a terminal window displaying disassembly output and a glowing padlock icon, representing static malware analysis of a Linux ELF binary."
coverCaption: ""
---

PhantomRing is one of the Sherlock boxes on HackTheBox, which is their forensics/malware-analysis line rather than the usual "pop a shell" Machines. You get a zip, a short scenario, and a set of questions to answer from evidence in that zip. This one hands you a single Linux binary and asks you to figure out what it does without running it, since it's a real (if simple) piece of post-exploitation malware.

______

## Provided Files:

You get `phantomring.zip`, password protected (HTB gives you the password on the download page), containing one file:

```
phantom_ring/agent
```

The scenario is basically: a SOC team found this binary sitting in `/var/tmp` on a box, it was making outbound connections, and you need to work out what it's capable of and pull out IOCs, all through static analysis.

## Walk Through:

First thing, don't run it. It's live malware, so everything below is read-only inspection.

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

- A block of local helper symbols that all share one distinctive name prefix (things like `<prefix>_prep_read`, `<prefix>_wait_cqe`, `<prefix>_cq_advance`), plus a couple of higher-level wrapper functions (a file reader, `send_all`, `recv_all`) built on top of them. That shared prefix names a specific Linux async I/O kernel interface, and every one of the agent's own file and socket operations routes through it instead of libc's classic `read`/`write`/`connect`/`open` wrappers. That's the answer to "which kernel interface does it abuse for EDR evasion", you just need to recognize the prefix and know why malware likes hiding behind that particular interface.
- A run of `cmd_*` functions (things like `cmd_get`, `cmd_recv`, `cmd_privesc`, `cmd_selfdestruct`, and several more in the same style), plus `process_cmd` and `main`. That's the command handler layout right there, one function per capability, and the exact count is worth writing down for later.

Worth flagging early: the number of `cmd_*` handler symbols here is not automatically the same as the number of distinct commands the dispatcher exposes to a connected client. That distinction matters later.

I used this list as a map for the rest of the analysis, jumping straight to whichever `cmd_*` function was relevant instead of reading the whole disassembly top to bottom.

### Pulling strings

```bash
strings -n 4 phantom_ring/agent
```

This is always worth doing early since it's free and this binary didn't bother hiding anything. Scrolling through the output you get a good chunk of the picture right away:

- A procfs-style path right next to `"Logged users:"` and its matching `"Error reading ..."` message. That's the login-enumeration file `cmd_users` parses, a classic session-tracking table.
- `/proc`, `/proc/%ld/comm`, `/proc/%ld/fd`, `/dev/pts` sitting near a `"PID CMD"` header, which is `cmd_ps` walking procfs to list processes.
- A single directory path grouped with `"Failed to open ..."` and `"Potential SUID binaries:"`. That's the SUID scan directory in `cmd_privesc`, no ambiguity about which string it is, just not naming it here.
- `"Agent will self-destruct"` and `"Unlink failed: %s"` bracketing a procfs path in `cmd_selfdestruct`. That path is what it reads to find its own location on disk before deleting itself.
- Three `/sys/kernel/debug/tracing/...` paths back to back, plus `"[*] Tracing disabled: %s"`. Three candidates for "first tracing file disabled", but `strings` just dumps them in file order, it doesn't tell you which one the code actually touches first.
- `/sys/fs/bpf`, a `/proc/%s/maps`-style format string, a short marker string, and `"[+] Killed PID using BPF: %d"` clustered together, which is the eBPF/killbpf detection logic. The format string is what it builds per PID, the marker is the substring it hunts for inside that file. What `strings` alone doesn't tell you is *when* in the loop that check runs relative to the tracing-file cleanup in the same handler.
- A short run of two-to-eight character tokens right before the `"[*] 404 Command not found [*]"` message: these are the literal command names the dispatcher compares against, one of which triggers self-destruction.
- One dotted-quad IPv4 address sitting completely alone in the string table, right next to the literal `socket` symbol name and one of the async-I/O helper symbols mentioned above. That's the hardcoded C2 address, in the clear, no obfuscation attempted.
- `"connect() failed: trying to reconnect"` and `"[+] Connected to %s:%d"` bracketing the connect logic.

*What `strings` cannot give you*: the port number, the reconnect delay, which of the three tracing paths is disabled first, which of the two procfs paths feeds the eBPF `strstr` check, and the true count of distinct commands. All five of those live only as numeric operands or control-flow order in the machine code, never as printable text. For those you have to read the disassembly.

### Digging into the disassembly

```bash
objdump -d --no-show-raw-insn phantom_ring/agent > disasm.txt
```

First annoyance: this binary was built with the hardened PLT (`.plt.sec`), so `objdump` prints calls to it as a bare offset like `callq 0x12c0 <.plt.sec+0x10>` instead of a friendly name. Before reading anything else I resolved that table once so every later call site would be self-explanatory. `.plt.sec` is a block of 16-byte stubs starting at `0x12b0`, each one doing `endbr64` then `jmpq *offset(%rip)` into a GOT slot, and `objdump -R` prints exactly which imported symbol lives in each GOT slot:

```bash
objdump -R phantom_ring/agent
```

Lining up GOT addresses against stub addresses (stub base = GOT-slot-relative jump target minus 4 bytes for the `endbr64`) gives a lookup table, for example `.plt.sec+0x10` is `strncmp`, `+0x70` is `strlen`, `+0x1c0` is `readdir`... once you have that table written down, every `callq 0x12xx <.plt.sec+...>` in the rest of the disassembly reads like a normal function call.

**Port and reconnect delay.** Inside `main()`, right before the connect sequence, there's this:

```text
41f7:  movw   $0x2, -0x10100(%rbp)
4200:  movl   $<port immediate>, %edi
4205:  callq  0x1350 <.plt.sec+0xa0>  ; htons
420a:  movw   %ax, -0x100fe(%rbp)
```

`0x1350` resolves to `htons` in the PLT table. It's called with a 16-bit immediate loaded straight into `%edi`, and the byte-swapped result gets written into the port field of the sockaddr struct sitting on the stack. That immediate, converted from hex to decimal, is the C2 port, and it's a literal instruction operand, no guessing or dynamic computation involved.

Further down, on the failed-connect path right after the `"connect() failed: trying to reconnect"` string reference, there's a `movl $<delay immediate>, %edi` immediately followed by a call into `.plt.sec+0x230`, which the PLT table resolves to `sleep`. That immediate, converted to decimal, is the reconnect back-off delay in seconds.

**Command dispatch and the real count.** `process_cmd` is a straight chain of length-checked `strncmp`/`strcmp` calls, each one comparing the sanitized input against one literal token before branching to a handler:

```text
3ebf:  leaq   <offset>(%rip), %rcx   ; -> literal command token
3ecc:  callq  0x12c0 <.plt.sec+0x10>  ; strncmp
3ed3:  testl  %eax, %eax
3ed5:  jne    <next comparison>
...
3ee9:  callq  0x23da <cmd_get>
```

That pattern repeats once per candidate command, and every branch target is one of the `cmd_*` symbols from the `nm` output. Walking the whole chain and writing down (literal string, target handler) for each comparison is the only reliable way to build a full command inventory, and it's what exposes the twist: one pair of literal tokens, a short one and a longer alias of it, both branch to the *exact same* `callq` target address. `strings` alone would never show you that, since it just lists both tokens as separate text with no idea they resolve to one implementation. The real "how many distinct commands" answer is the count of unique handler addresses actually called from this chain, not the count of literal strings sitting in `.rodata`, and those two counts are not equal here.

**SUID scan and eBPF/tracing evasion.** `cmd_privesc` calls one of the async-I/O prep helpers to stat a path, then `opendir` (`.plt.sec+0x1c0`) against a single hardcoded path loaded via `leaq` right before the call, no loop, no user input, one fixed directory. That's the SUID scan directory, and there's only one `leaq` feeding that `opendir` call so there's nothing to disambiguate.

`cmd_killbpf` is denser. Near the top of the function it loads three pointers into a local array back to back:

```text
37fb:  leaq  <offset 1>(%rip), %rax   ; -> tracing path
3802:  movq  %rax, -0x6130(%rbp)
3809:  leaq  <offset 2>(%rip), %rax   ; -> tracing path
3810:  movq  %rax, -0x6128(%rbp)
3817:  leaq  <offset 3>(%rip), %rax   ; -> tracing path
381e:  movq  %rax, -0x6120(%rbp)
```

Then it loops with an index starting at 0 (`cmpl $0x2, %eax` / `jbe`, so it runs for index 0, 1, 2), reading `array[index]` each pass and calling `openat`/`write` to flip it off. Array slot 0 is whichever `leaq` loaded first, at stack offset `-0x6130(%rbp)`, so the *first* file it disables is whichever of the three tracing-file strings that first `leaq` points at, and that's a fact about instruction order, not about which line `strings` happened to print first. I double-checked this against the raw `.rodata` bytes (see below) to make sure disassembly load order and on-disk string order actually agreed.

Later in the same function, after the tracing cleanup, it opens `/proc`, walks every PID directory with `readdir`, builds a per-PID path with `snprintf` using a format string, reads it through the higher-level async-I/O file reader mentioned earlier, and calls `strstr` against a second hardcoded string. That second string is the eBPF marker it's hunting for inside the per-PID file, confirming the detection logic strings alone only hinted at, and pinning down exactly which of the two procfs-flavored strings from earlier is the format string versus the marker.

**Self-destruct.** `cmd_selfdestruct` calls `readlink` (`.plt.sec+0x70`) against a hardcoded procfs string, uses the resolved path in one of the async-I/O prep helpers to unlink the file, and only reaches that code path after `process_cmd` matched one specific literal token in the dispatch chain above, the same token that appears in the command inventory.

**Confirming string order against raw bytes.** RIP-relative `leaq` comments in disassembly are `objdump`'s own interpretation of what a load points at, not a guarantee. For the two things where exact order mattered (the tracing-file array and the command-token table), I cross-checked against the raw `.rodata` bytes directly:

```bash
objdump -s -j .rodata phantom_ring/agent
```

This dumps hex-plus-ASCII for the whole section. Reading the byte range each `leaq` comment pointed at and confirming it actually spells out the expected null-terminated string is what turned "the disassembler's annotation says X" into "the bytes on disk are X", a second, independent confirmation instead of trusting one tool's guess.

### What ties it together

Between `file`/`sha256sum`, `nm`, `strings`, and this focused pass through `objdump -d` plus the `.rodata` and relocation cross-checks, that covers all 12 scored items in this Sherlock: the hash, the C2 IP and port, the reconnect delay, the true command count (and the alias that causes the miscount if you're not careful), the async-I/O evasion angle, the login-enumeration file, the process-listing path, the SUID scan directory, the eBPF detection string and the file it's read from, the first tracing file disabled, the self-location path, and the self-destruct trigger string. None of the literal values themselves are reproduced here, run the same commands against your own extracted copy of the binary and they'll fall out directly.

______

*Analysis done entirely through static inspection (`file`, `sha256sum`, `nm`, `objdump`, `strings`). The binary was never executed.*

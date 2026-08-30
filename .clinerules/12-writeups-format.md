# Writeups Format — CTF, Sherlock, and Challenge Write-Ups

This rule defines the structure for every file under `content/writeups/`. Writeups
document a specific challenge, box, or exercise (HackTheBox Machines, Challenges,
Sherlocks, and any other CTF-style platform). Rule `03-content-writing-style.md`
governs prose voice for the whole site and still applies here.

**A writeup reads like a person casually explaining how they solved the challenge,
not like an incident report or an audit log.** Use the existing
`hackthebox-challenges-crypto-*` writeups and `hackthebox-invite-challenge` as the
tone reference. Short paragraphs, first person ("I ran...", "you'll get..."),
plain sentences. No numbered meta-structure, no metadata tables, no section
literally titled explaining why the document exists.

## The Skeleton

Every writeup follows this simple shape:

1. **Front matter**, same fields as any article (`title`, `date`, `draft`, `toc`,
   `description`, `tags`, `cover`, `coverAlt`, `coverCaption`).
2. **One short intro paragraph** (two to four sentences) naming the platform, the
   challenge, and what you were given. If the platform has a short official
   scenario blurb, you can fold its idea into your own words. Do not quote it
   verbatim in a blockquote as if it were a legal disclaimer, just describe the
   setup the way you would tell a friend what the challenge handed you.
3. **`## Provided Files:`** listing exactly what you started with (files, cipher
   text, a zip, whatever the challenge gave you).
4. **`## Walk Through:`**, the actual solve. Use `###` subheadings only when the
   solve has genuinely distinct phases (cracking a password, then triage, then
   digging through disassembly). A short crypto challenge does not need any `###`
   subheadings at all, one paragraph per step is fine.
5. **Closing flag or result block**, `### Flag Example:` or similar, with the
   answer redacted per the rules below.

That is the whole shape. Do not add a metadata blockquote, a "What Is This?"
section, a "Why This Write-Up Exists" section, or numbered `## 1.` / `## 2.`
top-level headings. Those read as an AI-generated audit trail, not as a person's
notes from solving a box.

## How to Explain the Technical Steps

Explain findings the way a person actually reaches them when solving a challenge,
not the way a report retroactively justifies them:

- **State what a command told you, then move on.** "Running `nm` shows a pile of
  `cmd_*` functions" is enough. Do not add a second paragraph analyzing why you
  ran `nm` before `objdump`, a "cost versus what it proves" table, or a formal
  ordering rationale. A real solver just says what they did and what they found.
- **Skip the tool-selection justification.** Nobody solving a CTF writes "the
  reasoning for choosing this tool first is..." They just run the tool.
- **Use plain transition phrasing**: "next up," "once that's done," "from there,"
  "worth noting," "the annoying part was." Avoid clinical transitions like
  "this section documents," "the following table summarizes," or "this process
  yields."
- **Do not add a "Key Takeaways" bullet list at the end.** A real writeup ends
  when the flag or answer is found, sometimes with one closing line, not with a
  bulleted lessons-learned recap.
- **Do not invent or describe security incidents that did not happen during your
  own work**, including a fake tool-output or prompt-injection storyline. If
  something genuinely unusual happened while working the challenge, mention it in
  one plain sentence in context (for example, a red herring string that looked
  like a flag but wasn't). Never dedicate a headed section to narrating an
  "incident," since that is one of the biggest tells that an AI assistant wrote
  the document instead of a person.

## Redacting Scored Answers

When a challenge scores against specific literal values (a flag, a hash, an IP,
a count) and you do not want to hand out the answer directly:

- Match the lighter, existing convention on this site: show the real command,
  but swap only the final scored value for a bracketed placeholder in the output,
  for example `<sha1 build id>` or `<sha256 digest>`. Keep everything else in the
  output real (the ELF header text, the format strings, and so on).
- For a literal flag, use the legacy `HTB{XXXXXX_XXXXXXX_XXXXXX}` placeholder
  style already used across the crypto writeups.
- Do not add a disclaimer paragraph explaining that values were redacted "so this
  document contains no scoreable answers." Just show the placeholder in the
  output and move on, the way the crypto writeups already do with their flag
  examples.

## Splitting Mixed Command and Output

Per `03-content-writing-style.md`'s code block rule, put the command in its own
fenced block and the output in a separate one:

```bash
sha256sum phantom_ring/agent
```

```text
<sha256 digest>  phantom_ring/agent
```

Existing older writeups on this site sometimes show `$ command` and its output
together in one fence. That legacy style is fine to leave alone when editing an
existing file, but new writeups should split them.

## Fidelity Check Before Committing a Writeup

When the user hands you a full draft and asks for it to become a writeup:

- [ ] Preserve every real technical step and finding from the source. Do not
      drop detail just to shorten the piece.
- [ ] Strip any structural element that reads as AI-generated: metadata
      blockquote tables, "What Is This?" / "Why This Write-Up Exists" sections,
      numbered `## 1.` / `## 2.` top-level headings, a "Key Takeaways" recap, or
      a narrated "incident" section.
- [ ] Rewrite the tone into first person, casual, and direct, matching the
      `hackthebox-challenges-crypto-*` writeups.
- [ ] Split mixed command and output blocks per the code block rule.
- [ ] No em dashes, no semicolons, per `05-ai-writing-avoidance.md`. Ordinary
      casual words like "just," "actually," and "really" are fine here since
      they match this site's existing writeup voice, unlike a formal article.

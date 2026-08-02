# Content Writing Style and Skimmable Formatting

This rule defines the prose voice and markdown formatting used across every course, article,
guide, and study page on this site. The goal is **skimming readability**: a reader should be able
to scan the page and absorb the key terms, comparisons, and priorities without reading every
sentence. Use the SecOT+ and SecAI+ domain pages as the canonical reference for tone and layout.

---

## Voice and Sentence Rules

- Write **spartan, clear, active-voice** prose. Address the reader as "you".
- Keep sentences short and direct. One idea per sentence.
- **Never use em dashes (`—`).** Rewrite as two sentences or use a comma.
- **Do not use semicolons** in prose. Split into separate sentences instead.
- Prefer plain words over jargon, and define a term the first time it appears.
- Do not pad. Every sentence should teach something the reader needs.
- Mix short and medium-length sentences. Wall-to-wall short sentences read like a list.

---

## Bloom's Taxonomy — Writing for the Right Cognitive Level

Bloom's Taxonomy is a framework for categorizing educational goals. It has three domains:
**Cognitive** (knowledge and thinking), **Affective** (attitudes and values), and **Psychomotor**
(physical skills). This site targets the cognitive domain.

The six levels of the cognitive domain, from simplest to most complex:

| Level | Verb examples | What the content should do |
|-------|--------------|----------------------------|
| **Remember** | recall, define, list, name | Define the term clearly on first mention |
| **Understand** | explain, summarize, describe | Explain what it does and why it matters |
| **Apply** | use, execute, implement | Show a concrete command or configuration |
| **Analyze** | compare, differentiate, break down | Use tables to compare alternatives |
| **Evaluate** | judge, justify, critique | State when to use it and when not to |
| **Create** | design, build, produce | Give next steps, templates, or exercises |

**Apply these levels intentionally:**

- Certification exam prep content targets **Remember** and **Understand**. Define every term
  precisely. Explain the concept in one or two sentences. Provide a comparison table for closely
  related terms.
- Tutorial and guide content targets **Apply** and **Analyze**. Show the exact command. Explain
  what each flag does. Compare approaches in a table.
- Playbook and career content targets **Evaluate** and **Create**. State trade-offs directly.
  End sections with actionable next steps.

Do not mix levels within a single section. A definition list should only define. A command block
should only demonstrate. A comparison table should only compare.

---

## Bold

- **Bold the key term on first mention**, especially the noun a reader is meant to memorize
  ("A **programmable logic controller (PLC)** is a ruggedized industrial computer...").
- Bold the **lead-in term** of each bullet in a definition list (see Bullet Lists).
- Bold the exam-weight phrase in the intro paragraph ("**Securing AI Systems** is **40%** of...").
- Bold inline labels such as "**Exam details:**" that introduce a line of metadata.
- Do not bold whole sentences. Bold the term, not the explanation.
- Good bold candidates: commands, configuration file names, product names, key conclusions.

---

## Italics

- Use *italics* for a **callout or study-priority sentence**, set on its own line, that tells the
  reader where to focus.
- Use italics to flag the one **exception or outlier** in a group
  ("*OPC UA is the outlier because it was designed with security in mind.*").
- Keep italic callouts to one or two sentences. They are signposts, not paragraphs.

---

## Paragraphs

- Limit paragraphs to two to four sentences.
- Break as soon as the topic changes, even mid-section.
- Never write a paragraph longer than six lines on desktop.
- Use white space generously. Short paragraphs with breathing room are easier to read than
  dense blocks.
- Mix short and medium-length paragraphs for rhythm.

**Bad (wall of text):**
Active Directory provides centralized authentication and authorization across Windows environments.
It also enables Group Policy, centralized user management, delegation, auditing, software
deployment, password policies, and organizational unit management. These features make it one of
the most important components of enterprise Windows environments because administrators need
centralized management to reduce complexity and improve consistency across systems.

**Better (broken up):**
Active Directory is the backbone of most Windows enterprise environments.

It provides:

- Centralized authentication
- Group Policy
- User management
- Software deployment
- Security policy enforcement

Without it, managing hundreds of computers becomes much harder.

---

## Tables (for comparisons)

Use a markdown table whenever you are comparing peers across a shared dimension: components,
systems, protocols, frameworks, attacks, controls. The pattern is a two-column lookup table.

```markdown
| Protocol | Use |
|----------|-----|
| **Modbus** | Simple serial or TCP protocol for industrial devices |
| **DNP3** | SCADA communications in utilities |
```

- **Bold the term in the first column.** Keep the second column to a single tight clause.
- Give the table a short header pair that names the relationship (Term/Definition, Attack/What
  the attacker does, Framework/What it provides, System/Role).
- Replace comparison paragraphs with tables whenever four or more items are being compared.
- Keep tables to two or three columns for mobile readability. A 20-column table is unreadable.

---

## Bullet Lists (for definitions and enumerations)

Use a bullet list when defining a set of related terms that do not need a side-by-side comparison.
**Lead each bullet with the bold term, then the definition as one clause.**

```markdown
- A **sensor** measures a physical property and reports it to the control system.
- An **actuator** converts a control signal into physical motion or action.
```

- One bullet per concept, one clause per bullet.
- Keep the grammatical pattern parallel across the list. All bullets start with a verb, or all
  start with a noun, but not mixed.
- Use bullets when you have three or more related items, pros/cons, requirements, or features.
- Use numbered lists when order matters or steps must happen sequentially.
- Group long uninterrupted lists by sub-heading. More than eight bullets in a row is a wall.

**Bad (giant undifferentiated list):**
- VLANs
- Bonding
- Bridges
- ZFS
- LVM
- Ceph
- Firewall
- MFA

**Better (grouped):**

**Networking**
- VLANs
- Bonding
- Bridges

**Storage**
- ZFS
- LVM
- Ceph

---

## Headings

- Add a `##` heading every 300 to 500 words.
- Make headings descriptive enough to skim by themselves. "Why This Matters" beats "Part 2".
- Keep headings short. Five words or fewer is the target.
- Use headings as questions when appropriate: "What Is a PLC?" reads better than "PLCs".
- Prefer `##` over `###`. Reach for `####` only when absolutely necessary. If you hit `#####`,
  split the page.
- One major topic per `##` section. Do not cram unrelated content under one heading.

Good heading examples: `Why This Matters`, `Before You Begin`, `Common Mistakes`,
`Performance Results`, `Security Considerations`, `Next Steps`.

---

## Code Blocks

- Show the code first. Explain it afterward. Never explain before showing.
- Specify the language on every fenced block: ` ```bash`, ` ```yaml`, ` ```json`, ` ```toml`,
  ` ```python`, ` ```powershell`, ` ```go`, ` ```xml`, ` ```ini`, ` ```text`.
- Keep code blocks short. Split long procedures into multiple small blocks, each preceded by
  a one-line explanation of what it does.
- Explain output in a separate block labeled ` ```text`. Never mix commands and expected
  output in the same block.

```bash
apt update
apt full-upgrade
```

Expected output:

```text
Reading package lists... Done
Building dependency tree... Done
```

- Explain only the important lines. Skip obvious syntax.

---

## Callout Boxes

Use blockquote-style callouts to surface information that would get buried in prose.

Good callout labels:
- **Key Takeaway** — one sentence summary of the section
- **Warning** — something that breaks or causes data loss
- **Tip** — an optional optimization
- **Best Practice** — the recommended approach
- **Common Mistake** — what people get wrong
- **Expected Result** — what success looks like after a step

Place callouts at the end of a section or immediately after a step, not in the middle of
an explanation.

---

## Article and Tutorial Structure

Every tutorial or guide follows this sequence:

1. **Short summary** — two to four sentences. What the article covers and why it matters.
2. **Key Takeaways** — three to five bullets. What the reader will know after reading.
3. **Prerequisites** — what the reader needs before starting.
4. **Estimated time and difficulty** — readers appreciate knowing the commitment.
5. **Table of Contents** — for anything over 1,500 words.
6. **Sections** — one `##` heading per major topic. Alternate tables, bullets, and prose.
7. **Troubleshooting** — common failure modes and how to fix them.
8. **Next Steps** — where to go after this article.

The "30-second skim test": a reader should understand the article's purpose, major sections,
key conclusions, and next action within 30 seconds by scanning headings, bullets, callouts,
tables, and images alone. If they have to read every paragraph to understand the article, it
needs more structure.

---

## Front-Loading and Progressive Disclosure

- Put the most important point in the first sentence of a section.
- Answer "why should I care?" immediately. Do not make the reader hunt for the conclusion.
- Introduce concepts only when the reader needs them. Do not explain everything at once.
- Put caveats and limitations immediately after recommendations. Do not hide them at the end.

**Bad:** "Before discussing snapshots, let's first look at storage architecture..."

**Better:** "VM snapshots save state instantly. Here is how to create one and where they fall
short."

---

## Sections and Transitions

- Finish every major section with a short bridge to the next topic.
- Add a "Bottom line" or "What you learned" summary after sections longer than 500 words.

Examples of good bridges:
- "Now that storage is configured, the next step is networking."
- "With networking complete, the next section covers security."

---

## Scannability Checklist

Before publishing any article or course page:

- [ ] Is there a `##` heading every 300 to 500 words?
- [ ] Are paragraphs four sentences or fewer?
- [ ] Is there enough white space between sections?
- [ ] Did I replace long prose lists with bullet points?
- [ ] Did I replace comparison paragraphs with tables?
- [ ] Did I include a concrete example after every abstract concept?
- [ ] Did I highlight important information with a callout?
- [ ] Could someone understand the article by reading only headings, bullets, and callouts?
- [ ] Does each `##` section cover one topic only?
- [ ] Does every code block have a language specifier?

---

## Internal Links

Cross-link aggressively so the course works as a connected set:

- Every domain page opens with a return link to the start page and closes with a `## Next Steps`
  section linking the next sibling domain and the start page.
- The start page links to every domain page, the practice test, related courses, and the official
  objectives.
- Use root-relative links (`/secot-plus/ot-risk-management/`), not absolute URLs, for internal pages.
- Link the first mention of a sibling course or playbook ("[CompTIA Security+ Course](/security-plus-start/)").

---

## Page Rhythm

A well-formatted domain page alternates formats so nothing is a wall of text:

1. Bold weighted intro paragraph + one italic priority callout.
2. A short framing paragraph (two or three sentences).
3. `##` heading, then a **table or bullet list**, then an optional one-line italic insight.
4. Repeat heading + table/list blocks for each objective grouping.
5. `## Next Steps` with links.

If two consecutive sections both use tables, or both use bullets, consider varying one so the
page stays visually scannable.

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

## Text Emphasis for Skimmability

Heavy, deliberate use of bold, italics, and underline is how a reader navigates a long page
without reading every word. Treat emphasis as a navigation layer, not decoration. A reader
skimming at speed should be able to hit every bolded term and every italic callout and reconstruct
the key points of the entire page.

### Bold — the primary workhorse

Use bold aggressively. Every paragraph should have at least one bolded element unless it is a
transition sentence between sections.

**Required bold uses:**
- **Key term on first mention** — "A **programmable logic controller (PLC)** is a ruggedized
  industrial computer..."
- **Lead-in term of every bullet** in a definition list — "**Modbus** is a simple serial protocol..."
- **Exam weight or percentage** in the intro paragraph — "**Securing AI Systems** is **40%** of..."
- **Inline label** before metadata — "**Exam details:**", "**Prerequisites:**", "**Note:**"
- **Conclusion or recommendation** at the end of a section — "**Use ZFS for all production storage.**"
- **Warning or critical caveat** — "**Do not run this command on a live system.**"
- **File names, commands, and configuration keys** inline in prose — "Edit **`/etc/hosts`** to..."

**When in doubt, bold it.** A paragraph with no bold forces the reader to read every word.
A paragraph with one or two bolded terms lets the reader skip to what matters.

Do not bold whole sentences. Bold the term or the short phrase, not the explanation.

### Italics — callouts and exceptions

Use italics for sentences the reader must not miss and for flagging the one thing that breaks
the pattern.

**Required italic uses:**
- *Study-priority callout* on its own line — "*This domain accounts for 28% of the exam. Prioritize it.*"
- *Exception or outlier* in a group — "*OPC UA is the outlier: it was designed with security in mind.*"
- *Recommendation sentence* after a comparison table — "*For most deployments, choose option A.*"
- *Time-sensitive or version note* — "*This behavior changed in version 4.2.*"

Keep each italic passage to one or two sentences. Italics lose their signal value if overused
across multiple paragraphs.

### Underline — use sparingly for critical warnings

Standard Markdown does not render underlines. Use raw HTML `<u>` tags only for the highest-priority
warnings where bold alone is not enough — for example, a step that causes irreversible data loss.

```html
<u>**Warning: this command wipes all data on the target disk.**</u>
```

Limit underline to one or two instances per page. If every warning is underlined, none stand out.
The site config must have `markup.goldmark.renderer.unsafe = true` for raw HTML to pass through.
Verify this before relying on `<u>` in content.

### Combined emphasis — bold + italic

Use `***bold italic***` when a term is both a key definition and a priority callout in the same
sentence. Reserve this for the single most important concept in a section.

```markdown
***Never expose the management interface to the public internet.***
```

Do not combine bold and italic more than once per section. Overuse collapses the visual hierarchy.

### Emphasis density targets

Apply these minimum density targets when drafting:

| Content type | Minimum emphasis density |
|---|---|
| Certification domain page | At least one bolded term per paragraph; one italic callout per `##` section |
| Tutorial / guide | Bolded term on first mention of every command, flag, and file path |
| Bullet definition list | Every bullet lead-in is bolded, no exceptions |
| Comparison table | First column terms are bolded |
| Warning or critical note | Bold the warning label; underline only if data loss is possible |

### Scannability test for emphasis

After drafting, read only the bolded and italicized words, skipping all plain text. You should
be able to reconstruct:

1. The main topic of each section.
2. Every key term introduced.
3. Every warning or exception.
4. The recommended action or conclusion.

If you cannot, add more emphasis until the bolded/italic layer tells the complete story on its own.

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

---

## Breaking Up Walls of Text with Shortcodes

Shortcodes are first-class formatting tools, not extras. Use them wherever a block of prose would
benefit from a visual break, a concrete demonstration, or a clear next action. See
`09-hugo-shortcodes-and-partials.md` for full parameter reference.

### Embed a relevant video with `{{< youtube >}}`

When a concept is easier to show than explain, embed a video instead of writing three more
paragraphs. Place the embed immediately after the `##` heading it supports, before the prose
that follows.

```text
{{< youtube id="USjZcfj8yxE" >}}
```

When to use it:
- After introducing a multi-step process where a walkthrough exists.
- After a comparison section where a live demo clarifies the difference.
- At the end of an introductory section as a "see it in action" supplement.

Do not embed a video just to fill space. The video must be directly about the topic in that
section, not loosely related.

### Add a relevant image or diagram with `{{< figure >}}`

An image breaks the visual monotony of text and gives the reader an anchor. Use it to show
a screenshot of output, a diagram of a system, or a photo of physical hardware.

```text
{{< figure src="cluster-overview.webp" alt="Diagram showing the three-node cluster layout" >}}
```

Placement rules:
- Place the figure immediately before or after the sentence it illustrates, not at the end of
  a long section.
- Always write descriptive `alt` text that names what is shown, not just what it is called.
- Use `caption` when the image needs a one-line explanation that the surrounding text does not
  already provide.
- Images stored next to the `index.en.md` file are referenced by bare filename. External images
  use the full `https://` URL.

Do not use raw `<img>` tags or bare Markdown `![]()` syntax. Always use `{{< figure >}}`.

### Add a CTA button with `{{< centerbutton >}}` or `{{< button >}}`

A CTA button makes the next action explicit. Use it when the reader should do something after
reading a section: purchase a product, read a related guide, download a tool, or take a practice
test.

```text
{{< centerbutton href="/casp-plus-practice-test/" >}}
  Take the CASP+ Practice Test
{{< /centerbutton >}}
```

```text
{{< button href="https://amzn.to/XXXXX" >}}
  Buy on Amazon
{{< /button >}}
```

Placement rules:
- Use `{{< centerbutton >}}` for standalone CTAs that deserve their own visual line. It centers
  the button on the page.
- Use `{{< button >}}` when the CTA sits inline with surrounding text or in a short list of links.
- Place the button at the **end** of a section, not in the middle of an explanation.
- One CTA per section. Multiple competing CTAs in the same section dilute both.
- The button text must start with a verb: "Take the Practice Test", "Read the Guide", "Shop Now".

### When to reach for a shortcode

As a general rule: if you have written more than 400 words without any visual break other than
headings and bullets, add a shortcode. The mix keeps readers scrolling instead of bouncing.

| Situation | Shortcode to use |
|-----------|-----------------|
| Multi-step process with a video walkthrough available | `{{< youtube >}}` |
| Hardware, software UI screenshot, or system diagram | `{{< figure >}}` |
| End of section with a clear next action | `{{< centerbutton >}}` |
| Inline link that needs to stand out as a button | `{{< button >}}` |

Add one shortcode check to the scannability pass: after drafting, scan for any 400-word stretch
with no shortcode, heading, table, or code block. Break it up.

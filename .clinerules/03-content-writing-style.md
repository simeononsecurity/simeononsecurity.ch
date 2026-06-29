# Content Writing Style and Skimmable Formatting

This rule defines the prose voice and markdown formatting used across every course and study page
on this site. The goal is **skimming readability**: a reader should be able to scan the page and
absorb the key terms, comparisons, and priorities without reading every sentence. Use the SecOT+
and SecAI+ domain pages as the canonical reference for tone and layout.

## Voice and Sentence Rules

- Write **spartan, clear, active-voice** prose. Address the reader as "you".
- Keep sentences short and direct. One idea per sentence.
- **Never use em dashes (`—`).** Rewrite as two sentences or use a comma.
- **Do not use semicolons** in prose. Split into separate sentences instead.
- Prefer plain words over jargon, and define a term the first time it appears.
- Do not pad. Every sentence should teach something the exam may test.

## Bold

- **Bold the key term on first mention**, especially the noun a reader is meant to memorize
  ("A **programmable logic controller (PLC)** is a ruggedized industrial computer...").
- Bold the **lead-in term** of each bullet in a definition list (see Bullet Lists).
- Bold the exam-weight phrase in the intro paragraph ("**Securing AI Systems** is **40%** of...").
- Bold inline labels such as "**Exam details:**" that introduce a line of metadata.
- Do not bold whole sentences. Bold the term, not the explanation.

## Italics

- Use *italics* for a **callout or study-priority sentence**, set on its own line, that tells the
  reader where to focus. Examples:
  - *"Spend the bulk of your study time here. Master the threat names and the control that stops each one."*
  - *"At 22% this is the heaviest-weighted domain, so build deep hands-on familiarity..."*
- Use italics to flag the one **exception or outlier** in a group
  ("*OPC UA is the outlier because it was designed with security in mind.*").
- Keep italic callouts to one or two sentences. They are signposts, not paragraphs.

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
- Give the table a short header pair that names the relationship (Term/Definition, Attack/What the
  attacker does, Framework/What it provides, System/Role).

## Bullet Lists (for definitions and enumerations)

Use a bullet list when defining a set of related terms that do not need a side-by-side comparison.
**Lead each bullet with the bold term, then the definition as one clause.**

```markdown
- A **sensor** measures a physical property and reports it to the control system.
- An **actuator** converts a control signal into physical motion or action.
```

- One bullet per concept, one clause per bullet.
- Keep the grammatical pattern parallel across the list.
- For the start-page domain summaries, lead bullets with a bold capability verb phrase
  ("- Put **safety first**, including...", "- Identify **OT components**, including...").

## Internal Links

Cross-link aggressively so the course works as a connected set:

- Every domain page opens with a return link to the start page and closes with a `## Next Steps`
  section linking the next sibling domain and the start page.
- The start page links to every domain page, the practice test, related courses, and the official
  objectives.
- Use root-relative links (`/secot-plus/ot-risk-management/`), not absolute URLs, for internal pages.
- Link the first mention of a sibling course or playbook ("[CompTIA Security+ Course](/security-plus-start/)").

## Page Rhythm

A well-formatted domain page alternates formats so nothing is a wall of text:

1. Bold weighted intro paragraph + one italic priority callout.
2. A short framing paragraph (two or three sentences).
3. `##` heading, then a **table or bullet list**, then an optional one-line italic insight.
4. Repeat heading + table/list blocks for each objective grouping.
5. `## Next Steps` with links.

If two consecutive sections both use tables, or both use bullets, consider varying one so the page
stays visually scannable.

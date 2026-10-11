---
title: "ChatGPT and Claude Projects: Set Up Reusable AI Context"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Create ChatGPT and Claude projects with focused instructions, current reference files, and a simple test for reused context."
genre: ["Artificial Intelligence", "Productivity"]
tags: ["ChatGPT Projects", "Claude Projects", "AI project instructions", "AI context", "ChatGPT project setup", "Claude project knowledge"]
cover: "/img/cover/effective-ai-chat-projects.webp"
coverAlt: "Two organized AI project workspaces holding a project brief, reference files, and separate conversations"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**Create a project when several conversations share the same purpose.** Put stable instructions and approved reference files in one place. Keep each conversation focused on one task. This lesson uses a fictional community workshop so you can practice without private data.

## Key Takeaways

- **Project instructions** set reusable behavior for related chats.
- **Project sources** hold reference material you want the assistant to consult.
- **Conversation history** is a record of one exchange, not a substitute for an approved source.
- **A fresh-chat test** reveals whether your project setup supplies enough context.

## Before You Begin

**Prerequisites:** a ChatGPT or Claude account, plus the task packet from [lesson 1](/articles/effective-ai-workflow-foundations/). Set aside 35 minutes. Difficulty is beginner. Use invented names, dates, and locations throughout this practice.

**Create two small files** on your computer. Open a plain-text editor, paste each block below into its own file, and save with the shown `.md` name. Markdown files are plain text. `workshop-brief.md` states the audience and style. `approved-schedule.md` states the fictional official schedule.

```text
workshop-brief.md, revision 1
Audience: people registered for an introductory workshop.
Style: short sentences and a friendly, factual tone.
Do not invent prices, accessibility features, or parking details.
```

```text
approved-schedule.md, revision 1
Event: Introduction to Digital Safety
Date: 2026-11-12
Start: 7 p.m.
Place: Community Room A
```

## Set Up ChatGPT

1. **Open Projects** in the ChatGPT sidebar and create a project named `Workshop Practice`.
2. **Add the two files** as project sources.
3. **Open Project settings** and add the instructions below.
4. **Inspect memory and sharing settings** for your account and workspace before adding real material.

```text
Use approved-schedule.md for event facts.
Use workshop-brief.md for audience and style.
If a requested fact is absent, ask for the source or mark it unknown.
Draft messages only. Do not send or publish them.
List factual changes after each revised draft.
```

**ChatGPT Projects keep related chats, files, and instructions together.** Project settings and available features vary by plan and workspace. Record whether your project uses default or project-only memory because outside-project context differs. Use the [official ChatGPT Projects guide](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) to check the current interface and memory options before relying on them.

## Set Up Claude

1. **Open Projects** in Claude and create a project with the same practice name.
2. **Add the two files** to project knowledge.
3. **Set project instructions** to the same five lines.
4. **Start a new chat inside the project** to test the setup.

**Claude applies project instructions across chats in a project.** Its project knowledge supplies shared reference material. Use the uploaded files as the controlled facts. Project memory behavior varies by account and settings, so do not treat another chat's details as the approved schedule. Review [Claude's project setup guide](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) for current controls.

## Test a Fresh Chat

**Open a new conversation** inside either project. Ask for a short announcement. Omit the schedule from your prompt so the project sources do the work.

```text
Draft a 100-word email for the upcoming workshop.
Name the source used for the time and place.
List any missing facts after the draft.
Do not send the message.
```

| Result | Meaning | Next action |
|---|---|---|
| **Time and place match** | The assistant used the supplied schedule | Confirm against the file yourself |
| **A fact is invented** | Instructions or source use failed | Remove the fact and narrow the request |
| **Source is absent** | The reference did not reach this chat | Check project membership and file upload |
| **Old revision appears** | The project holds stale material | Replace the source and retest |

**Do not infer reliability from one correct answer.** Repeat the test with this conflicting draft:

```text
Revise this line using the approved project schedule:
"The Introduction to Digital Safety class starts at 6 p.m. in Community Room A."
Name the factual change and the source file. Do not send the message.
```

**Expected answer:** the line uses 7 p.m. and names `approved-schedule.md` as the source. Record any failure you observe. A passing run needs no invented failure.

**Worked test record:** new chat, first prompt, time 7 p.m., place Community Room A, source `approved-schedule.md`, pass. Conflict prompt, 6 p.m. corrected to 7 p.m., pass. This is an example record. Replace it with your own observed results.

## Maintain the Project

**Keep project instructions short.** Put stable rules there. Put task-specific details in each prompt. Replace outdated files and identify their revisions. Separate unrelated work into another project so sources do not conflict.

**Before sharing a project,** inspect its files, chats, instructions, and access list. A project is a work container, not an approval system. A source file named “approved” still needs a real owner and revision record for consequential work.

## Practice and Check

**Your artifact:** one project with two synthetic source files, five instruction lines, and a short test record. Capture the observed time, place, source name, and any invented fact. Delete the practice project when finished if you do not need it.

**Expected reasoning:** a new chat uses project sources for stable facts, while your prompt defines the immediate output. You verify the result against the file. A missing source or wrong revision sends you back to project setup.

## Troubleshooting

- **Missing project controls:** check your current plan and workspace settings in the vendor guide.
- **Conflicting answers:** remove duplicate or stale source files, then start a fresh chat.
- **Unexpected sharing:** review project membership and remove sensitive sources before continuing.
- **Repeated style drift:** shorten instructions and provide one short example in the task prompt.

## Next Steps

**Continue with [Your First Coding Agent Task](/articles/effective-ai-coding-agent-first-task/)**. That lesson moves from a chat project to a local code repository.

---
title: "9 AI Agent Skill Projects for Research, Design, and Development"
date: 2026-10-06
lastmod: 2026-10-06
toc: true
draft: false
description: "Compare nine agent skill projects by workflow, host support, dependencies, and cost. Learn how to install, inspect, and test the skills you need."
genre: ["Artificial Intelligence", "Developer Tools", "Software Development"]
tags: ["AI agent skills", "Codex skills", "Claude Code skills", "last30days", "Impeccable", "gstack", "Superpowers", "Claude Video", "Humanizer", "NVIDIA SkillSpector", "HyperFrames", "Remotion", "SKILL.md", "agent workflows", "skill installation", "skill security", "AI research", "frontend design", "video generation", "development workflows", "agent customization"]
cover: "/img/cover/agent-skill-workflow-library.webp"
coverAlt: "Ivory instruction cards in a tray beside a magnifying lens, color swatches, and a small film reel on a dark desk"
coverCaption: "Conceptual illustration of a task-specific agent skill library."
---

**Install an agent skill to improve a repeatable task.** Researching current discussions, reviewing interface design, and rendering a video involve different procedures and dependencies. A useful skill supplies the missing instructions, reference material, or scripts for one of those jobs.

**Nine projects deserve consideration:** last30days, Humanizer, Impeccable, Superpowers, gstack, Claude Video, Remotion, HyperFrames, and NVIDIA SkillSpector. Some are instruction bundles, some include executable tools, and some are frameworks with companion skills. This guide compares their documented roles and provides a practical way to select, install, and evaluate them.

**Documentation snapshot: October 6, 2026.** Recommendations reflect project documentation and source inspection, not a comparative benchmark of output quality. Free installation does not establish free inference, rendering, data access, or commercial use.

<!--more-->

## Key Takeaways

- **Start with a recurring job:** choose a skill with a clear output and acceptance check.
- **Separate skills from runtimes:** installing instructions does not install every required executable.
- **Check the host:** a working Claude Code integration does not establish identical Codex or Cowork behavior.
- **Inspect permissions and dependencies:** package commands, hooks, external services, and credentials need separate attention.
- **Customize after testing:** keep project policy authoritative and preserve a record of upstream versions.

## Choose by Deliverable

| Required output | Project to evaluate | First check |
|---|---|---|
| **Current discussion brief** | last30days | Which sources returned usable evidence? |
| **Edited prose** | Humanizer | Did meaning and attribution survive? |
| **Improved interface** | Impeccable | Does the revised interaction work? |
| **Planned and tested change** | Superpowers | Does the process match task complexity? |
| **Review and QA workflow** | gstack | Which features work on your agent host? |
| **Video observations** | Claude Video / Watch | Are claims supported by frames or audio? |
| **React video composition** | Remotion skills | Does the exported video match the preview? |
| **HTML video composition** | HyperFrames skills | Is animation deterministic when seeking? |
| **Skill inspection report** | SkillSpector | Was analysis complete, and what was flagged? |

**A skill differs from an agent harness.** A skill supplies task-specific guidance and sometimes scripts. The harness decides how the agent loads instructions, calls tools, and enforces permissions. Our [agent-harness comparison](/articles/best-ai-agent-harnesses/) covers those surrounding systems.

**A skill folder is also not a plugin installation.** Plugins sometimes register hooks or additional tools which a manual folder copy omits. Read the instructions for your particular host and installation mode before assuming equivalent behavior.

## Research and Writing

### last30days

**Use last30days for recent discussion research.** The [project](https://github.com/mvanhorn/last30days-skill) combines sources such as Reddit, Hacker News, YouTube, X, and the web. Available coverage depends on the selected sources, installed tools, authentication, and provider access. Its preflight mode describes planned access and writes without starting research.

**Ask for an evidence trail.** A useful result includes dates, links, recurring complaints, and disagreements. An unavailable source should appear as a coverage gap. Engagement counts describe activity among collected posts, not a representative survey of every user.

**Illustrative task:** investigate recurring installation failures for a library released recently. Group reports by version and operating system, then verify proposed fixes against the library's issue tracker or documentation. Avoid treating a popular workaround as an upstream-supported solution.

### Humanizer

**Use Humanizer as an editing pass.** The [skill](https://github.com/blader/humanizer) targets repetitive contrasts, staged introductions, inflated claims, and other writing habits. It accepts voice samples and aims to preserve the underlying meaning.

**Supply the constraints alongside the draft.** Identify the audience, facts which must remain, and citations which must stay attached. After editing, compare the factual claims with the original. Better rhythm is useful, but it does not validate an unsupported statistic.

| Writing check | Passing result |
|---|---|
| **Meaning** | Same claims, qualifications, and scope |
| **Sources** | Attribution remains near borrowed findings |
| **Voice** | Matches the intended reader and supplied examples |
| **Originality** | Adds independent reasoning instead of disguising copied prose |

**Use these projects at different stages.** last30days gathers material for investigation. Humanizer edits expression. Neither replaces source verification or independent authorship.

## Interface and Development Work

### Impeccable

**Use Impeccable for focused design work.** Its [website](https://impeccable.style/) and [repository](https://github.com/pbakaus/impeccable) document a design workflow covering critique, typography, layout, clarity, motion, and polish. Begin with a specific user problem rather than asking for a vaguely more impressive page.

**An illustrative brief:** make a subscription settings page easier to scan without hiding cancellation or changing keyboard navigation. Request a critique first, then implement the selected changes. Check mobile layout, focus order, contrast, and completion of the original task afterward.

**Installation mode matters.** The current Codex instructions distinguish the skill from a project-local design hook. Hook trust requires its own approval in Codex. A copied skill folder does not establish an active hook.

### Superpowers

**Use Superpowers for a structured development process.** Its [repository](https://github.com/obra/superpowers) packages workflows for brainstorming, planning, testing, debugging, and review. It also documents host-specific plugin installation, including Codex.

**Match the process to the assignment.** A feature spanning data storage, UI, and tests benefits from an explicit plan. A spelling correction needs much less ceremony. Define the authorized scope so a general development workflow does not expand a small request into adjacent work.

**Project instructions still apply.** A skill's preferred testing method, worktree approach, or delegation pattern must fit the repository and the user's request. Installing a methodology does not authorize every action described within it.

### gstack

**Use gstack for a broader engineering workflow with executable tooling.** Its [documentation](https://github.com/garrytan/gstack) includes planning, review, browser QA, investigation, and release-oriented skills. Installation builds supporting tools rather than merely copying prose.

**Codex support is currently experimental.** The project distinguishes Claude Code's hook-enforced safety features from advisory behavior on Codex. Do not assume a similarly named command supplies identical enforcement across hosts.

**My selection rule:** trial Superpowers when the missing piece is a repeatable development process. Trial gstack when its specific review or browser tools solve a current need. If both are installed, choose one primary workflow per task and invoke the other for a named contribution.

| Development problem | Useful evaluation task |
|---|---|
| **Unclear scope** | Produce a bounded plan with acceptance criteria |
| **Fragile implementation** | Fix a seeded regression and preserve existing behavior |
| **Broken interaction** | Reproduce a browser failure and retain evidence |
| **Conflicting workflows** | Confirm only the selected process directs the task |

## Video Evidence and Production

### Claude Video / Watch

**Use Claude Video to collect evidence from a video.** Despite the repository name, its [Watch skill](https://github.com/bradautomates/claude-video) supports local agents including Codex. Its local route uses downloads, sampled frames, and captions or transcription. A separate Gemini route sends video for model analysis when configured.

**Check current host support.** The README lists Claude Chat and Cowork as unsupported. Local execution requires media tools such as FFmpeg and yt-dlp, and individual websites still impose access limits.

**Keep visual and audio claims separate.** A transcript supports spoken words. Frames support visible details at sampled times. Neither establishes an unseen event between samples. Ask for timestamps and unresolved observations rather than an unqualified claim to have understood the entire recording.

### Remotion

**Use Remotion for video compositions written in React.** The [framework repository](https://github.com/remotion-dev/remotion) points to a separate [agent-skills collection](https://www.remotion.dev/docs/ai/skills). The collection covers project creation, markup, maps, captions, Studio, and rendering. Installing the collection does not create a video project or install all project dependencies.

**Check licensing independently of the skill download.** Remotion's [pricing page](https://www.remotion.dev/docs/license/pricing) lists a free license for individuals and companies of up to three people, with company licensing for larger organizations and specified collaborations. Review the current terms for your use case.

### HyperFrames

**Use HyperFrames for HTML-based video composition.** Its [repository](https://github.com/heygen-com/hyperframes) describes rendering HTML, CSS, media, and seekable animation into MP4. The published skills guide composition, preview, validation, and rendering.

**Begin with its documented core set.** The current installation guidance distinguishes core skills from the larger published collection and repository-internal skills. An indiscriminate install of every folder adds unrelated instructions and makes maintenance harder.

| Video workflow | Important acceptance check |
|---|---|
| **Watch** | Timestamped observations agree with inspected media |
| **Remotion** | Final export preserves timing, fonts, audio, and layout |
| **HyperFrames** | Seeking to a frame produces the intended visual state |

**Choose through a controlled sample.** Give Remotion and HyperFrames the same brief, assets, duration, and output dimensions. For example, animate a three-step maintenance procedure with captions and one diagram. Compare the exported files, editing effort, and render failures. A single attractive demo does not establish a general winner.

## Inspect With SkillSpector

```bash
skillspector scan ./downloaded-skill --no-llm --format json --output report.json
```

**NVIDIA SkillSpector is a scanner, not a video or writing skill.** The [project](https://github.com/NVIDIA/SkillSpector) documents static checks and optional model-assisted analysis for agent skill packages. The command above assumes the CLI is already installed and scans a local folder without executing the target skill.

**Read the findings and coverage together.** Inspect flagged files and surrounding code, then record which checks completed. An incomplete scan should not become a clean verdict. A keyword hit also needs context: a provider's documented public map token differs from code collecting unrelated credentials.

**Static-only does not mean fully offline.** According to the project, dependency names and versions still go to OSV for vulnerability lookup with **`--no-llm`**. Enabling model analysis additionally sends eligible file contents to the configured provider. Choose the mode appropriate for the material under review.

**Use the report as evidence for a decision.** Explain whether each finding is necessary for the stated task, which data leaves the machine, and what authority the runtime grants. A low score is not proof of safety, and reputation does not resolve an unexplained finding.

## Install the Correct Package

**Identify the canonical skill distribution first.** The Remotion framework and its skills live in different repositories. Claude Video exposes a skill named Watch. SkillSpector is installed as a CLI, with agent integration handled separately. Those distinctions explain why cloning a project is not always enough.

**Example commands below come from the projects' current installation documentation.** Run only the command for the selected project. The package runner downloads and executes installer code, so inspect the upstream project and choose your installation scope before running it.

```bash
# Humanizer: user-wide Codex installation
npx skills add blader/humanizer --global --agent codex

# last30days: user-wide Codex installation
npx skills add mvanhorn/last30days-skill -g -a codex

# Remotion: official skill collection, not the framework repository
npx skills add remotion-dev/skills
```

**The third command opens the installer workflow.** Select the intended agent and scope rather than assuming its defaults match the explicitly scoped commands above. Plugin installers and standalone folder installs also have different update mechanisms.

**Preserve existing installations.** Before replacing a skill, check its version, local changes, and manager. Avoid keeping multiple competing copies in user, project, and plugin locations unless the host documents how it resolves them.

| Installation state | What it establishes |
|---|---|
| **Files present** | Instructions and referenced assets exist |
| **Host discovers skill** | The agent recognizes its name and description |
| **Dependencies ready** | Required executables and packages are available |
| **Task verified** | A representative result passes independent checks |

**Verify each stage in order.** A successful folder copy is an installation check, not evidence of a working browser, download, transcription, or render. Keep optional provider setup separate from the basic installation and avoid storing credentials in skill files.

## Test Before Customizing

**Use one saved task as a baseline.** Run it without the new skill, then with the skill while holding the model, input, tools, and acceptance criteria steady where possible. Record failures and human corrections alongside the final result.

```yaml
# Illustrative evaluation record, not a skill configuration schema
job: "review a settings page"
input: "same source revision and test data"
variants:
  - "agent without the selected skill"
  - "same agent with the selected skill"
acceptance:
  - "required actions remain visible"
  - "keyboard navigation works"
  - "mobile layout remains usable"
record:
  - "skill source and revision"
  - "model and enabled tools"
  - "completed checks and retained evidence"
  - "elapsed time and manual corrections"
  - "external service usage"
```

**Customize the repeated failure, not the entire package.** If research summaries lose conflicting evidence, add a requirement to preserve dissenting sources. If a design pass changes established colors, point it to the design tokens. If video captions overflow, add an export-resolution check.

**Keep local additions traceable.** Record the upstream revision, your changes, and the task which motivated them. Updates deserve another trial because new triggers, scripts, or dependencies change the workflow you previously evaluated.

**Watch for overlapping instructions.** Development suites, design skills, and prose editors all express preferences. Repository rules and the user's current request should resolve conflicts. A style skill should not strip required accessibility labels, remove citations, or rewrite technical terms merely to vary the wording.

## Build a Useful Library

**Start with the job you repeat most often.** A writer might trial last30days and Humanizer. A frontend developer might begin with Impeccable and one development workflow. A video producer should choose a production framework and add Watch when source-video analysis is part of the work.

**Budget for operation separately from installation.** Account for model calls, optional search providers, transcription, media generation, rendering infrastructure, and applicable licenses. A free repository answers only part of the cost question.

**Before your first trial:** prepare approved model access, a disposable project or sample input, and written acceptance criteria. Basic instruction skills are accessible to beginners. Browser tooling, media dependencies, and cloud rendering require more setup. Allow an initial hour for a bounded trial, then repeat it with representative inputs before making the workflow routine.

**Keep skills with demonstrated value.** Retain the ones which reduce missed steps or review effort, and remove duplicates which introduce conflicting behavior. Revisit their host compatibility and dependencies when your agent environment changes.

{{< youtube id="3fdb_giOrLo" enable="true" title="9 Free AI Agent Skills You NEED to Install Now" >}}

## References

- [last30days: research skill and installation](https://github.com/mvanhorn/last30days-skill)
- [Humanizer: writing skill](https://github.com/blader/humanizer)
- [Impeccable: design workflow](https://impeccable.style/)
- [Impeccable: repository and host-specific setup](https://github.com/pbakaus/impeccable)
- [Superpowers: development skills](https://github.com/obra/superpowers)
- [gstack: engineering tools and host support](https://github.com/garrytan/gstack)
- [Claude Video: Watch skill and runtime requirements](https://github.com/bradautomates/claude-video)
- [Remotion: React video framework](https://github.com/remotion-dev/remotion)
- [Remotion: agent skills](https://www.remotion.dev/docs/ai/skills)
- [Remotion: licensing and pricing](https://www.remotion.dev/docs/license/pricing)
- [HyperFrames: framework and skill distribution](https://github.com/heygen-com/hyperframes)
- [NVIDIA SkillSpector: scanner behavior and data handling](https://github.com/NVIDIA/SkillSpector)
- [Futurepedia: 9 Free AI Agent Skills You NEED to Install Now](https://www.youtube.com/watch?v=3fdb_giOrLo)

---
title: "AI Workflow Course Setup: Terminal, Git, and Practice Lab"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Prepare a safe AI practice workspace, learn the terminal and Git terms used in the course, and run the starter lab."
genre: ["Artificial Intelligence", "Software Engineering", "Education"]
tags: ["AI course setup", "terminal basics", "Git basics", "coding agent prerequisites", "AI practice lab", "beginner AI course"]
cover: "/img/cover/effective-ai-course-setup.webp"
coverAlt: "A beginner practice workspace with terminal, Python and Git symbols, a checked lab folder, and a reset archive"
coverCaption: ""
---

#### [Return to the Practical AI Workflows Course](/effective-ai-course-start/)

**Set up one safe practice space before using an agent.** This course works with synthetic data and a tiny Python project. You need one chat account for the first exercises. Hands-on coding lessons need one coding agent, Git, and Python 3.10 or later. Plan about seven to ten hours for the full course, including practice.

## Key Takeaways

- **Browser route:** complete chat, planning, source-checking, and review exercises in ChatGPT or Claude.
- **Local route:** use a terminal and the supplied Python lab for coding exercises.
- **Reset route:** extract a new lab copy whenever an exercise goes wrong.
- **Safety rule:** keep private files, customer records, and credentials outside the lab.

## Choose Your Route

| Route | What you need | What you practice |
|---|---|---|
| **Browser-first** | Current browser and a ChatGPT or Claude account | Prompts, projects, sources, context, review |
| **Local hands-on** | Git, Python 3.10 or later, terminal, one coding agent | Files, diffs, tests, agent edits |
| **No-cost study** | Browser, local Python 3.10 or later and Git | All reading and manual lab checks, with simulated agent steps where access is unavailable |

**Products set their own plans and limits.** Check [ChatGPT Projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) and [Claude Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) before relying on a feature. The no-cost study route does not prove hands-on skill with an unavailable coding agent. Record the distinction in your completion notes.

**Use one default path:** ChatGPT in a browser for chat exercises, then one available coding agent with the local lab. Claude is an equivalent chat path. Codex CLI, Claude Code CLI, and OpenCode remain choices for the coding stage. You do not need accounts with every vendor.

## Learn the Local Terms

| Term | Plain meaning |
|---|---|
| **Terminal** | An app where you type commands |
| **Shell** | Software interpreting those commands |
| **CLI** | A command line interface to a program |
| **Working directory** | The folder a command uses by default |
| **Repository** | A project tracked by Git |
| **Commit** | A saved Git snapshot |
| **Branch** | A named line of Git changes |
| **Diff** | A display of lines added or removed |
| **Test** | A repeatable check of expected behavior |
| **Exit code** | A number reporting command success or failure |

**You do not need GitHub for the starter lab.** Git works on your computer. GitHub is a separate hosting service. A local commit records a snapshot without sending your files anywhere.

## Prepare the Lab

**Download the [course starter lab](/downloads/effective-ai-course-lab.zip)** and extract it into a new folder you control. Open a terminal in the folder. On macOS or Linux, use Terminal and `cd` to enter the extracted directory. On Windows, use PowerShell or Windows Terminal and `cd` to enter the folder. The Python command on Windows is often `py -3` instead of `python3`.

**Install [Python 3.10 or later](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads) if needed.** Check the installed tools before running the lab. The first two commands print version numbers. `cd` changes the working directory. `ls` lists files. Replace the example folder path with your extracted folder's actual path.

```bash
python3 --version
git --version
cd /path/to/effective-ai-course-lab
ls
```

**On Windows PowerShell,** use `py -3 --version`, `git --version`, `cd C:\path\to\effective-ai-course-lab`, and `Get-ChildItem`. The listed files should include `task_report.py`, `tasks.json`, `tests`, and `docs`. If a version command fails, finish the installation before continuing.

```bash
pwd
python3 task_report.py tasks.json
python3 -m unittest discover -s tests -v
```

**On Windows PowerShell,** replace `pwd` with `Get-Location` if you prefer, and replace `python3` with `py -3` when Python uses the launcher. Read the path from the first command. It should end in your extracted lab folder. Check the filenames too. A file saved as `AGENTS.md.txt` will not serve as `AGENTS.md`. In Windows Explorer, turn on file name extensions to inspect the full name.

**Expected output:** the report says `Total tasks: 4`. The test command names two tests and ends with `OK`. A shell returns exit code zero after success. A different count or a traceback means you should stop and inspect the folder and Python setup.

**Read each command as parts.** In `python3 task_report.py tasks.json`, `python3` launches Python, `task_report.py` is the program, and `tasks.json` is an argument naming input data. The printed count is output, not another command. After a failed command, macOS and Linux show its status with `echo $?`. PowerShell exposes the last native program status through `$LASTEXITCODE`.

**Plan about ten minutes for the first run** once Python is installed: extract the lab, run the report, and match the count to the four entries in `tasks.json`. Open the JSON file in a text editor and count the entries yourself.

## Practice Git Safely

**Start Git only inside the extracted lab folder.** The commands below make a local snapshot. The `git status` command shows whether files changed. The `git diff` command shows changed lines after you edit a tracked file.

```bash
git init
git add .
git commit -m "Baseline course lab"
git status --short
```

**Expected status:** no file names appear after the commit. If Git asks for a name and email, set a lab-only identity from inside this folder, then rerun the commit. Replace the example values with your own private values. Do not paste identity or credential output into a public chat.

```bash
git config --local user.name "Course Learner"
git config --local user.email "learner@example.invalid"
git commit -m "Baseline course lab"
git status --short
```

**A reset needs no Git command.** Save notes outside the lab, delete the extracted practice copy, and extract the original ZIP again. Use this reset when a lesson's edit leaves the program in an unknown state.

## Protect Your Practice Space

**Use synthetic examples.** Do not upload private documents to a course project. Do not put API keys in prompts, source files, screenshots, or commits. A coding agent's file and command access depends on its permissions and the folder you open. Inspect both before letting it run.

**Check sharing before upload.** Project files might be available to project members. Follow your organization's policy for real work. The course uses fictional data so you need no special approval for the lab itself.

## Practice and Check

**Your artifact:** record your chosen route, the extracted folder name, the report count, the test result, and the reset method. Use a fresh lab copy to confirm you know how to reset.

**Expected reasoning:** you know which folder commands affect, you distinguish local Git from hosting, and you have a way to recover before an agent edits files.

## Troubleshooting

- **Python command missing:** install Python 3 from its official distributor, then reopen the terminal.
- **File not found:** check the working directory and list the extracted folder's files.
- **Tests do not run:** use the exact command from the lab README in the extracted folder.
- **Git commit asks for identity:** configure Git locally and keep the chosen values out of course notes.

## Next Steps

**Continue with [the Reliable AI Workflow](/articles/effective-ai-workflow-foundations/)**. The first exercise uses the same synthetic workshop before any tool receives real files.

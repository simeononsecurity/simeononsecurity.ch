---
title: "CompTIA Linux+ (XK0-005): Scripting, Containers, and Automation"
date: 2025-01-01
toc: true
draft: false
description: "Master scripting, containers, and automation for the CompTIA Linux+ XK0-005 exam. Learn Bash scripting, regex with grep, sed, and awk, Git, Docker, Podman, Kubernetes, Ansible, and IaC with real examples."
genre: ["CompTIA Linux+ Course", "Shell Scripting", "Containers", "Automation", "DevOps", "Docker", "Kubernetes", "Ansible", "Infrastructure as Code", "Linux Certification"]
tags: ["CompTIA Linux+", "XK0-005", "Bash scripting", "regular expressions", "grep", "sed", "awk", "JSON", "YAML", "Git", "Docker", "Podman", "Kubernetes", "Ansible", "Infrastructure as Code", "automation", "containers"]
cover: "/img/cover/comptia-linux-scripting-containers-automation-2.webp"
coverAlt: "A modern IT workspace featuring a laptop with code snippets in a terminal, surrounded by colorful icons of Docker, Git, and Ansible on a dark background."
coverCaption: "Master Scripting, Containers, and Automation for the XK0-005 Exam"
---

#### [Click Here to Return To the CompTIA Linux+ Course Page](/linux-plus-start/)

**Scripting, Containers, and Automation** is **19%** of the **CompTIA Linux+ (XK0-005)** exam. This module teaches you to automate Linux work with Bash, process text with regular expressions, version code with Git, run containers, and configure systems with Ansible. *These skills move you from administrator to automation engineer.*

## Bash Scripting

Every script starts with a **shebang** that names the interpreter:

```bash
#!/usr/bin/env bash
set -euo pipefail
```

**Variables** hold values, and `$(...)` captures command output:

```bash
name="web01"
today=$(date +%F)
echo "Backing up $name on $today"
```

*Quote variables with double quotes so spaces and special characters do not break the command.*

**Conditionals** branch on test expressions. Common tests are `-f` (file exists), `-d` (directory), and `-z` (empty string):

```bash
if [ -f /etc/nginx/nginx.conf ]; then
  echo "config present"
elif [ -d /etc/nginx ]; then
  echo "directory but no config"
else
  echo "nginx not installed"
fi
```

**Loops** repeat work:

```bash
for host in web01 web02 web03; do
  ping -c1 "$host" >/dev/null && echo "$host up"
done

count=0
while [ "$count" -lt 5 ]; do
  echo "attempt $count"
  count=$((count + 1))
done
```

**Functions** group reusable logic, and **$?** holds the exit code of the last command:

```bash
log() { echo "[$(date +%T)] $1"; }

backup() {
  tar -czf "/backups/$1-$(date +%F).tar.gz" "/srv/$1"
  return $?
}

backup web
if [ $? -eq 0 ]; then log "backup ok"; else log "backup failed"; fi
```

A complete worked script that checks a service and restarts it:

```bash
#!/usr/bin/env bash
set -euo pipefail
SERVICE="$1"

if ! systemctl is-active --quiet "$SERVICE"; then
  echo "$SERVICE is down, restarting"
  systemctl restart "$SERVICE"
else
  echo "$SERVICE is healthy"
fi
```

## Environment and Shell Initialization

Login shells read **/etc/profile** and **~/.bash_profile**. Interactive non-login shells read **~/.bashrc**. Put exported variables and PATH changes where every shell sees them:

```bash
export PATH="$HOME/bin:$PATH"
export EDITOR=vim
alias ll='ls -lh'
```

## Text Processing and Regular Expressions

**grep** searches with patterns, **sed** edits streams, and **awk** processes fields.

```bash
grep -E "error|fail" /var/log/syslog       # extended regex, two patterns
grep -ri "timeout" /etc/                    # recursive, case-insensitive
sed 's/old/new/g' config.txt                # replace all on each line
sed -i '/^#/d' config.txt                   # delete comment lines in place
awk '{print $1, $4}' access.log             # print fields 1 and 4
awk -F: '$3 >= 1000 {print $1}' /etc/passwd # regular user accounts
```

A real example that counts requests per IP in a web log:

```bash
awk '{print $1}' access.log | sort | uniq -c | sort -rn | head
```

## Structured Data: JSON and YAML

Parse **JSON** with **jq** and read **YAML** in playbooks and compose files:

```bash
curl -s https://api.example.com/status | jq '.services[] | .name'
jq '.version' package.json
```

## Version Control with Git

**Git** tracks changes and supports collaboration:

```bash
git init
git add .
git commit -m "initial commit"
git branch feature-x
git checkout feature-x
git merge feature-x
git remote add origin git@github.com:team/repo.git
git push -u origin main
git pull
```

Use a **.gitignore** to keep secrets and build output out of the repository:

```
*.log
.env
node_modules/
```

## Containers

A **container** packages an application with its dependencies and shares the host kernel. Run them with **Docker** or the daemonless **Podman** (the commands match):

```bash
docker run -d --name web -p 8080:80 nginx
docker ps
docker images
docker exec -it web /bin/sh
docker logs web
```

A **Dockerfile** builds a custom image. Each instruction is explained:

```dockerfile
FROM python:3.12-slim          # base image
WORKDIR /app                   # set the working directory
COPY requirements.txt .        # copy dependency list
RUN pip install -r requirements.txt   # install dependencies in a layer
COPY . .                       # copy the application code
EXPOSE 8000                    # document the listening port
CMD ["python", "app.py"]       # default command
```

**Docker Compose** runs multi-container apps from one file:

```yaml
services:
  web:
    build: .
    ports:
      - "8080:8000"
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
```

*Containers share the host kernel, so a kernel-level escape affects every container. Keep images minimal and patched.*

## Kubernetes Basics

**Kubernetes** orchestrates containers across machines. Learn the core objects:

- A **pod** is the smallest unit and holds one or more containers
- A **node** is a worker machine
- A **deployment** manages replica pods and rolling updates
- A **service** gives pods a stable network endpoint

```bash
kubectl get pods
kubectl get deployments
kubectl describe pod web-xyz
kubectl logs web-xyz
```

## Automation with Ansible

**Ansible** configures systems over SSH with no agent on the target. You describe the desired state in a **playbook**, and Ansible makes only the changes needed, which makes runs **idempotent**.

An inventory file:

```
[web]
web01.example.com
web02.example.com
```

A sample playbook that installs and starts nginx:

```yaml
- name: Configure web servers
  hosts: web
  become: true
  tasks:
    - name: Install nginx
      package:
        name: nginx
        state: present
    - name: Start and enable nginx
      service:
        name: nginx
        state: started
        enabled: true
```

Run it:

```bash
ansible-playbook -i inventory site.yml
```

**Infrastructure as Code (IaC)** applies the same idea to whole environments, so you version and rebuild infrastructure from text files.

## Scheduling and Debugging

Combine scripts with **cron** or **systemd timers** for unattended runs. Debug scripts with these flags:

```bash
bash -x script.sh        # print each command as it runs
set -e                   # exit on the first error
set -u                   # error on undefined variables
set -o pipefail          # fail if any piped command fails
shellcheck script.sh     # static analysis that catches common bugs
```

*Add `set -euo pipefail` to the top of production scripts so silent failures do not corrupt data.*

## Next Steps

Automation pairs with the hardening from [Linux Security](/linux-plus/linux-security/) and the administration in [Linux System Management](/linux-plus/linux-system-management/). When automation breaks, [Linux Troubleshooting](/linux-plus/linux-troubleshooting/) helps you find the root cause.

Return to the [CompTIA Linux+ Course](/linux-plus-start/) and measure your readiness with the [CompTIA Linux+ Practice Test](/linux-plus-practice-test/).

---
title: "Discord Cyber Scenario Bot: Enhance Cybersecurity Training and Awareness"
date: 2023-02-22
toc: true
draft: false
description: "Discover how the CyberScenarioBot can elevate your cybersecurity training and awareness program on Discord, offering quizzes, scenarios, leaderboard tracking, and powerful tool commands."
tags: ["Discord bot", "cybersecurity training", "cybersecurity awareness", "scenario bot", "quiz bot", "leaderboard", "tool commands", "Docker", "Python", "automated testing", "Discord API", "developer documentation", "contributing", "MIT license", "CyberScenarioBot", "CyberSentinels", "enhance training", "awareness program", "cybersecurity scenarios", "server environment", "customized commands", "deploy and manage", "quizzes and scenarios", "tool commands", "informational commands", "issues and contributions", "Discord developer application", "Discord.py documentation", "working with developers", "community Discord server"]
---


**CyberScenarioBot**

Discord Cyber Scenario, Quiz, And Cyber Awareness Training Bot.

You can skip to [🚀 Quick Start](#quick-start) to add `CyberScenarioBot` to your server now.

[![Docker Image CI](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml/badge.svg)](https://github.com/simeononsecurity/discord-cyber-scenario-bot/actions/workflows/docker-image.yml)

## Introduction

This bot may be useful in a cybersecurity training or awareness program, where users can be exposed to various cybersecurity scenarios and learn how to prevent or respond to them. By using a Discord bot, the scenarios can be easily shared with users in a server environment, and the bot can be customized to include additional commands or functionality as needed. Additionally, the bot can be run in a Docker container, making it easy to deploy and manage in various environments.

[See the bot in action](https://discord.gg/CYVe2CyrXk)

## 🚀 Quick Start

### How to run:
#### Python:
Assuming you are using a Unix-based system, open a terminal and navigate to the directory where the bot.py script is located. Then, run the following command:
```bash
export BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
export GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes and leaderboard)"
export LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
export CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
export APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
export NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
export SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
export QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
Note that if you are using a Windows-based system, you'll need to use a slightly different command to set the environment variable. Here's an example command that should work on Windows:
```shell
set BOT_TOKEN="INSERT YOUR BOT TOKEN HERE"
set GUILD_ID="INSERT YOUR GUILD ID HERE (only needed for timed quizes)"
set LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE (Only needed for leaderboard for prompts)" 
set CHANNEL_ID="INSERT YOUR CHANNEL ID HERE (only needed for timed quizes)"
set APLUSROLE="INSERT YOUR A+ ROLE ID HERE (only needed for timed quizes)"
set NETPLUSROLE="INSERT YOUR Network+ ROLE ID HERE (only needed for timed quizes)"
set SECPLUSROLE="INSERT YOUR Security+ ROLE ID HERE (only needed for timed quizes)"
set QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE (only needed for timed quizes)"
python bot.py
```
#### Docker:
When running the Docker container, you can pass in the BOT_TOKEN environment variable using the -e flag as follows:

```bash
docker run -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" -it --rm simeononsecurity/discord-cyber-scenario-bot:latest
```

To run the bot in the background:
```bash
docker run -td --name scenario-bot -e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" simeononsecurity/discord-cyber-scenario-bot:latest
```

To run the bot in the background with all scheduled prompts and roles:
```bash
docker run -td --name scenario-bot \
-e BOT_TOKEN="INSERT YOUR BOT TOKEN HERE" \
-e GUILD_ID="INSERT YOUR GUILD ID HERE" \
-e LEADERBOARD_CHANNEL_ID="INSERT YOUR LEADERBOARD CHANNEL ID HERE" \
-e LEADERBOARD_PERSIST_CHANNEL_ID="INSERT YOUR LEADERBOARD PERSIST CHANNEL ID HERE" \
-e CHANNEL_ID="INSERT YOUR CHANNEL ID HERE" \
-e APLUSROLE="INSERT YOUR A+ ROLE ID HERE" \
-e NETPLUSROLE="INSERT YOUR NET+ ROLE ID HERE" \
-e SECPLUSROLE="INSERT YOUR SEC+ ROLE ID HERE" \
-e QUIZROLE="INSERT YOUR QUIZ ROLE ID HERE" \
simeononsecurity/discord-cyber-scenario-bot:latest
```

## Features
### **Commands Available**
*Command prefix: '!', '/'*****

### 📝 **Quiz and Scenario Commands**
- **Aplus**: Replies with CompTIA's A+ related prompt.
- **Bluescenario**: Replies with a blue team scenario.
- **CCNA**: Replies with Cisco's CCNA multiple choice prompt.
- **CEH**: Replies with EC-Council's CEH multiple choice prompt.
- **CISSP**: Replies with ISC2's CISSP multiple choice prompt.
- **Linuxplus**: Replies with CompTIA's Linux+ multiple choice prompt.
- **Netplus**: Replies with CompTIA's Network+ related prompt.
- **Quiz**: Replies with a random Cyber Security Awareness Question.
- **Redscenario**: Replies with a redteam scenario.
- **Secplus**: Replies with CompTIA's Security+ related prompt.

#### 💯🎯 **Leaderboard**
*Multiple-choice questions are dynamically weighted similar to the real exams based on if they are answered correctly or incorrectly*

- *Track your progress over time and see how you compare against others in your server*
- *See scores for each quiz category as well as overall*

### 🛠️ **Tool Commands**
- **Dns**: Takes in a `domain name` and returns A, AAAA, NS, TXT, etc. records.
- **Hash**: Takes in `1 of 4 supported algos` and a `string` and outputs a corresponding hash.
- **Ping**: Takes in an `IP address` and returns with a success message and average latency or a failure message.
- **Phonelookup**: Takes in a `phone number` and outputs the carrier and location.
- **Shodanip**: Takes in an `IP address` and outputs useful information from https://internetdb.shodan.io/.
- **Subnet**: Takes in an `IP address` and a `Subnet Mask` and outputs the Range, Usable IPs, Gateway Address, Broadcast Address, and Number of Supported Hosts.
- **Whois**: Takes in a `domain name` and outputs domain whois information.

### ℹ️ **Informational Commands**
- **Commands**: Replies with this message.
- **Socials**: Replies with the various bot social media accounts and websites.

### ⚙️ **Easy Setup**
- *See [🚀 Quick Start](#🚀-quick-start)*

## Upcoming Features

These features have planned date of implementation, but we're tracking them and we'd love [contributions](#contributing) for them. 

- Advanced leaderboard features, including weekly and monthly rankings.
- Customizable prompts and quizzes to cater to specific cybersecurity training needs.
- Advanced reporting and analytics for tracking user progress and performance.

## Usage

The CyberScenarioBot offers various commands and features to enhance your cybersecurity training and awareness program. Here are some common use cases:

1. **Quizzes and Scenarios**: Use the `/quiz` command to get a random cybersecurity awareness question. Use commands like `/aplus`, `/netplus`, `/secplus` to access specific prompts related to CompTIA certifications. Use commands like `/bluescenario` and `/redscenario` to get blue team and red team scenarios, respectively.

2. **Leaderboard**: Keep track of user progress and compare scores with others in your server by answering the quiz and certification questions.

3. **Tool Commands**: Utilize various tool commands to perform tasks related to DNS, hashing, ping, phone number lookup, Shodan IP search, subnet calculations, and domain WHOIS lookup. Use commands like `/dns`, `/hash`, `/ping`, `/phonelookup`, `/shodanip`, `/subnet`, and `/whois` followed by the appropriate arguments.

4. **Informational Commands**: Use the `/commands` command to get a list of available commands. Use the `/socials` command to get information about the bot's social media accounts and websites.

Feel free to explore and experiment with the available commands to enhance your cybersecurity training and engage your server members.

## Issues

If users encounter any issues or have suggestions for improvements, they can open a GitHub issue to report them. Encourage users to provide detailed information about the problem and steps to reproduce it.

To open an issue, follow these steps:

1. Go to the Issues tab on the project's GitHub repository: [Issues](https://github.com/CyberSentinels/discord-cyber-scenario-bot/issues)
2. Click on the "New Issue" button.
3. Provide a descriptive title and a clear description of the issue.
4. Include any relevant logs, screenshots, or code snippets to help with troubleshooting.
5. Submit the issue and await further communication from the project maintainers.

## Contributing

We welcome all contributions. 
This project was meant to be a development and learning effort by [the CyberSentinels club](https://cybersentinels.org) and we'd love to help you contribute and answer any questions you may have.

### Automated Python Testing

This repo includes automated testing, you can see examples on how to implement that [here](https://github.com/CyberSentinels/penguin-pie)

### Discord API and Developer Documentation

For testing changes and implementing features, you'll need a few things.

- [Discord Developer Application](https://discord.com/developers/applications)
- [Discord Developers Documentation](https://discord.com/developers/docs/intro)
- [Discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

### Working with the Developers

You can discuss development efforts in the community discord server [here](https://discord.gg/CYVe2CyrXk).
  
## License

[MIT](https://github.com/simeononsecurity/glotta/blob/main/LICENSE)

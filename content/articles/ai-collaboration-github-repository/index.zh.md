---
title: "GitHub AI 协作：代码库与审查边界"
date: 2026-10-01
lastmod: 2026-11-08
toc: true
draft: false
description: "为经过审查的 AI 贡献建立来源地图、文件所有权和受保护的发布边界。"
genre: ["人工智能", "团队协作", "软件工程"]
tags: ["AI 协作课程", "GitHub 代码库", "分支保护", "CODEOWNERS", "来源地图", "拉取请求审查", "发布控制"]
cover: "/img/cover/A_group_of_diverse_professionals_collaborating_on_a_cyberse.webp"
coverAlt: "网络安全工作空间中，专业人员共同审查项目工作的插图"
coverCaption: ""
---
[返回 AI 协作课程](/ai-collaboration-course-start/)

**章程获批后，维护者会建立以 GitHub 为先的发布边界。**需求、配置、策略和运行手册放在一个可丢弃的代码库中。贡献者通过 Issues 和拉取请求提出变更。你要明确已批准事实存放的位置，并在接入代理之前阻止未经审查的变更。

## 要点

- **受保护的 `main`** 是发布边界。
- **Issues** 收集工作提案，但不批准策略。
- **CODEOWNERS** 指定符合条件的文件审查者。
- **分开的用户账号** 用于演示审查和拒绝控制。

## 开始之前

**前提条件：**[试点基础](/articles/ai-collaboration-pilot-foundation/)、已解压的实验包、代码库管理员，以及分开的产品和运维审查者。**预计耗时：**60 分钟。**难度：**中等。

**计划边界：**GitHub 为 Free 计划中的公开代码库以及 Pro、Team 或 Enterprise 计划中的私有代码库提供受保护分支。公开代码库只放合成内容。在依赖规则强制执行之前，先根据受保护分支参考资料确认可见性和计划级别。

**完成结果：**你将得到一条受保护的发布分支、文件负责人、来源地图，以及作为证据记录的拒绝测试。

## 创建代码库

1. **创建 `export-service-lab`**，包含 README 和默认分支 **`main`**。
2. **将解压后的实验包**复制到代码库根目录，保留 **`check.py`**、**`test_check.py`** 和 **`baseline/`**。将 `baseline/` 中的基线记录文件复制到根目录，作为初始记录。
3. **创建 `docs/project-map.md`**，使用试点基础材料中的登记表。添加包含已批准 POL-01 的 **`docs/policy.md`**。
4. **创建 `docs/decisions/DEC-12.md`**，记录章程批准、角色、基线决策和状态。
5. **以管理员身份提交初始配置。**记录这项初始例外。后续贡献前启用保护。

**在 Git Bash、macOS 终端或 Linux shell 中进行本地初始化：**在浏览器中登录 GitHub，打开新代码库，选择 **Code** 并复制 HTTPS 克隆 URL。在一次性工作目录中运行以下命令。将两个占位路径替换为该 URL 和下载的实验 ZIP 路径。不要把令牌粘贴到 URL 中。

```bash
git --version
git clone "https://github.com/OWNER/export-service-lab.git"
cd export-service-lab
unzip -n "/absolute/path/to/ai-collaboration-lab.zip"
cp baseline/config.json baseline/policy.json baseline/proposal.json baseline/requirement.json baseline/runbook.md .
mkdir -p docs/decisions
git status --short
```

clone 命令应创建代码库目录。如果没有 `unzip`，请用文件管理器解压 ZIP，并将内容复制到此 checkout，同时保留代码库的 README。`git status --short` 应将复制的记录、检查器、测试和 `baseline/` 列为新文件。用文本编辑器从试点材料中保存 `docs/project-map.md`、`docs/policy.md` 和 `docs/decisions/DEC-12.md`。然后运行：

```bash
git add README.md baseline check.py test_check.py config.json policy.json proposal.json requirement.json runbook.md docs
git commit -m "Add synthetic collaboration baseline"
git push origin main
git status --short
git remote -v
```

Git 应报告新的提交 ID，随后成功推送到 `main`。最后的简短状态应为空。在新的浏览器窗口中打开 GitHub 代码库，确认文件和提交 ID 出现在 `main` 上。保存提交 URL，作为初始化证据。如果 Git 要求设置作者身份，请按课程中心的配置桥接说明操作。如果身份验证失败，使用 GitHub 支持的凭据流程，然后重试同一项推送。如果分支或远程仓库不正确，请停下并在下一次写入前检查 `git branch --show-current` 和 `git remote -v`。如果保护已启用导致推送被拒绝，请打开提案分支和 PR，不要绕过规则。维护者也可以使用下面的纯浏览器流程。

| 记录 | 位置 | 负责人 |
|---|---|---|
| **POL-01** | `policy.json`、`docs/policy.md` | 策略负责人 |
| **REQ-17** | `requirement.json` | 产品负责人 |
| **RUN-04** | `runbook.md` | 运维负责人 |
| **行为** | `config.json` | 代码库维护者 |
| **决策** | `docs/decisions/` | 项目负责人 |

**地图链接到位置，不复制值。**让 README 专注于设置和地图。即使在一个代码库中，重复写入保留期限要求也会造成偏差。

## 指定文件负责人

**在本地生成 `.github/CODEOWNERS`**，使用沙箱中的真实账号名。输入时去掉开头的 **`@`**。账号身份应留在私有实验环境中，不要放入公开练习证据。

```bash
python3 - <<'PY'
from pathlib import Path
roles = ['product', 'operations', 'maintainer', 'policy']
handles = {r: input(r + ' GitHub handle: ').strip().lstrip('@') for r in roles}
if any(not h or not all(c.isalnum() or c == '-' for c in h) for h in handles.values()):
    raise SystemExit('Invalid handle')
paths = {'requirement.json': 'product', 'runbook.md': 'operations',
         'config.json': 'maintainer', 'policy.json': 'policy',
         'docs/policy.md': 'policy', 'AGENTS.md': 'policy',
         'CLAUDE.md': 'policy', '.clinerules/': 'policy',
         '.github/': 'maintainer', 'check.py': 'maintainer',
         'test_check.py': 'maintainer', 'baseline/': 'maintainer'}
Path('.github').mkdir(exist_ok=True)
Path('.github/CODEOWNERS').write_text(''.join(
    '/' + path + ' @' + handles[role] + '\n' for path, role in paths.items()))
PY
```

**GitHub 要求负责人拥有写入权限，才会识别他们。**在浏览器中检查 CODEOWNERS 文件是否有错误。与普通内容一样，保护所有权文件和工作流定义。

**同一行列出多个姓名，并不要求所有负责人都批准。**对于匹配的路径，GitHub 接受一位符合条件的负责人批准。需求路径和运行手册路径应指定不同负责人。试点还要求产品负责人和运维负责人的确认与最终提案关联。

## 保护发布流程

1. **打开 Settings、Branches**，为 **`main`** 添加分支保护规则。本练习中始终使用分支保护，不要与 rulesets 混用。
2. **要求拉取请求、**两项批准审查，以及代码负责人审查。
3. 新提交后**撤销过期批准**，并要求解决评论讨论。
4. **启用禁止绕过上述设置。**禁用强制推送和删除。
5. 在下个模块首次运行后，**添加一致性检查。**合并前要求分支保持最新。

**两项批准强制的是数量，不是业务角色成员身份。**CODEOWNERS 提供基于路径的负责人覆盖。维护者还要检查两个角色的确认。应明确记录这项程序性控制，不要将其描述为自动强制双角色审批。

**管理员仍然管理配置。**在测试前后截取规则状态。不要授予代理管理员权限，也不要用特权令牌演示拒绝贡献者操作。

## 验证边界

| 尝试 | 预期结果 |
|---|---|
| **贡献者提交分支** | 允许提出变更 |
| **贡献者直接发布** | 受保护的发布被拒绝 |
| **一位审查者批准** | 合并被审查门槛阻止 |
| **审查后出现新提交** | 需要新的批准 |
| **敏感文件没有负责人覆盖** | 发布前修复 |

**使用贡献者的浏览器会话检查操作路径。**GitHub 网页编辑器不会编辑受保护的 **`main`**。系统提示创建分支，说明存在受支持的浏览器路径，但无法证明服务器拒绝了直接推送。要取得平台拒绝证据，请让拥有获批本地 Git 权限的贡献者尝试向受保护的 **`main`** 直接推送一项无害变更，并保留服务器响应。如果没有本地访问权限，则将拒绝测试标为“受阻”。

**拒绝后读取 `main`**，确认修订版本没有变化。记录操作者角色、尝试的操作、结果和来源修订版本。助手承诺不发布属于行为证据，不是平台权限测试。

**直接推送测试使用贡献者本人通过身份验证的本地克隆。**维护者令牌会测试错误的身份。此示例响应展示了应保留的服务器证据类型。具体措辞因代码库规则而异。

```text
Actor role: contributor
Attempt: harmless synthetic direct push to main
Remote result: rejected, protected branch update denied
Initial main commit: [record sandbox commit]
Final main commit: [record same commit after read-back]
Decision: platform denial supported only if both records are observed
```

**如果本地 Git 身份验证不可用，将服务器端拒绝标为“受阻”。**保留浏览器创建分支的提示，作为路径证据，然后请维护者安排单独的贡献者测试。不要把路径提示算作直接推送被拒。

## 建立实用的来源地图

**来源地图是导航文档，**不是第二份需求文档。从聊天进入的人应能找到当前意图、已实现行为和操作说明，而不必在相互冲突的摘要间选择。

```text
Project: export-service-lab
Track: GitHub-first
Approved boundary: protected main

REQ-17 -> requirement.json
  Authority: retention intent for synthetic export files
  Owner: product-owner
  Revision: record revision plus protected commit

RUN-04 -> runbook.md
  Authority: operating instructions for the synthetic lab
  Owner: operations-owner
  Revision: protected commit

Behavior -> config.json
  Authority: committed retention configuration
  Owner: repository-maintainer
  Revision: protected commit

Proposals -> Issues and proposal branches
  Authority: requested changes only
```

**不要在地图的每个条目里都写当前保留期限。**如果地图记录“七天”，PROP-042 后就又多出一个需要同步的值。地图只保留稳定标识和位置，具体值应从权威记录中读取。

**将地图变更作为路由变更来保护。**把 REQ-17 重定向到草稿文件会改变来源选择，即使已批准的需求本身没有改动。地图变更时，检查目标位置、负责人和权限范围。

## 分开基线与候选版本

**代码库根目录包含实验室当前使用的记录。**下载的 **`baseline/`** 目录是教学用样例，不会自动成为每个后续 PR 的受保护基线。经过审查的工作进入 **`main`** 后，根目录中的受保护记录将成为下一项提案的基线。

| 位置 | 用途 | 在 PROP-042 中编辑？ |
|---|---|---|
| **根目录的 requirement/config/runbook** | 分支上的当前候选记录 | 可以，通过已审查的变更 |
| **`baseline/`** | 原始离线练习样例 | 不可以 |
| **分离的可信 worktree** | 捕获的受保护根目录记录 | 不可以 |
| **`context.json`** | 已捕获基线字节的证据 | 对账后重新生成 |

**将控制措施变更与保留期限变更分开。**先初始化检查器和审查规则，再提出从七天改为三十天。把策略、工作流和数值变更混在一起，会让审查者难以分辨修复的控制和被绕过的控制。

## 审查完整变更

**接受 PR 描述之前，先打开 Files changed。**描述说明作者意图，diff 展示提交的变更。对于 PROP-042，检查需求修订、范围排除项、配置、运行手册、提案基线和清单证据。

1. **产品审查：**确认三十天意图和未变化的排除项。
2. **运维审查：**确认运行手册与提议的配置一致，并保留运行环境限制。
3. **维护者审查：**检查 JSON、来源捕获、检查结果和无关编辑。
4. **控制审查：**单独检查地图、策略、CODEOWNERS 或工作流变更。

**绿色检查无法解释无关删除。**如果分支在更改保留期限时删除了策略文档，请求单独的提案或明确指定的负责人审查。限制范围有助于审查者理解审查对象。

## 诊断拒绝测试

**每行证据只记录一项尝试的操作。**“贡献者失败了”含义不清。用户可能缺少普通写权限、遇到浏览器限制，或触发预期的分支规则。这些观察说明的是不同边界。

| 观察 | 解释 | 后续操作 |
|---|---|---|
| **无法创建任何分支** | 没有贡献权限 | 使用获批的 Issue 或 fork 路径 |
| **能创建分支，但不能发布到 main** | 测试的发布路径受到限制 | 记录未变化的 main 修订版本 |
| **一项审查后合并被阻止** | 测试 PR 的审查数量规则生效 | 添加角色相关证据 |
| **管理员仍能绕过规则发布** | 测试身份绕过了边界 | 检查绕过设置和授权 |

**在课程共享证据中记录角色和操作，不要暴露账号详情。**将原始操作者记录私下留给审查者。将规则配置、尝试操作、拒绝结果和最终受保护修订版本一起保存。

## 代码库完成检查

**交付一个其他贡献者能够独立浏览的代码库。**README 指向地图，地图指向权威记录，负责人覆盖包括敏感路径，保护规则适用于 **`main`**。保留一项获准的提案和一次被拒绝的发布尝试。

**不要只凭设置就宣称强制措施有效。**设置说明预期配置，沙箱尝试说明特定角色和路径下观察到的行为。在代理和 GitHub Actions 课程中同时使用这两类证据。

## 故障排查与回退

**缺少负责人的请求：**确认写入权限和基线分支路径覆盖。**缺少保护：**检查计划和可见性。**仍可合并：**检查规则目标、绕过设置和审查数量。

**回退：**关闭未合并的提案并停用实验室自动化。通过另一个经过审查的 PR 回退已合并的实验内容。删除一次性代码库前先保留证据。不要为了完成失败的测试而削弱保护。

## 练习与自检

**作为贡献者，提议编辑 `docs/policy.md`。**判断维护者单独批准是否足以代表策略负责人的批准。

**预期推理：**审查数量本身不能证明权限。该路径需要策略负责人覆盖和当前角色审查。将未被自动强制执行的角色要求列为程序性控制。

## 主要参考资料

- **计划和审查控制：**[受保护分支](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)。
- **负责人资格：**[代码负责人](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)。
- **通过浏览器贡献：**[编辑文件](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)。

## 后续步骤

**继续学习[代理适配器与 GitHub Actions](/articles/ai-collaboration-github-agents-actions/)**，将来源证据连接到可执行检查。

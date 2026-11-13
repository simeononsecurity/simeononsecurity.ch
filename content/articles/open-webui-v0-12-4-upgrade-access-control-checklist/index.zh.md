---
title: "Open WebUI v0.12.4：升级与访问控制检查清单 2026"
date: 2026-10-28
lastmod: 2026-11-12
toc: true
draft: false
description: "备份并将 Open WebUI 升级到 v0.12.4，然后测试聊天共享、导出权限、资源授权、账户和网络访问。"
genre: ["自托管 AI", "网络安全", "系统管理"]
tags: ["Open WebUI", "Open WebUI v0.12.4", "Open WebUI 升级", "Open WebUI 安全", "Open WebUI 访问控制", "自托管 AI", "Docker 升级", "pip 升级", "Open WebUI 备份", "Open WebUI 权限", "Open WebUI 角色", "Open WebUI 群组", "聊天导出权限", "共享聊天", "已归档聊天", "知识库访问", "模型访问", "工具权限", "API 密钥安全", "管理员账户安全", "禁用注册", "反向代理身份验证", "VPN 访问", "固定容器镜像版本"]
---

**Open WebUI v0.12.4 包含维护者尚未逐项说明的安全修复。**发行说明建议尽快更新部署，并表示将在分配 CVE 后发布公告。下文列出的聊天共享和权限变更是发行说明中可见的项目，并非尚未披露的全部安全修复。[Open WebUI v0.12.4 发行说明](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

<!--more-->

## 要点

- **先备份。** 更改应用前，保留可恢复的数据卷或数据库副本以及上传文件。
- **固定官方版本。** 标准 Docker 镜像使用 `ghcr.io/open-webui/open-webui:v0.12.4`，pip 使用 `open-webui==0.12.4`。
- **使用真实用户角色测试权限。** 按钮隐藏并不能证明 API 端执行了授权检查。
- **保持访问私密。** 要求应用身份验证，并通过 VPN 或经过身份验证的反向代理限制网络访问。

## 升级前

**准备工作：**确认当前安装方式、容器镜像变体、持久数据位置、外部数据库、反向代理和身份验证提供方。安排停机窗口，并保留现有容器配置或服务定义。预留时间在独立实例上演练恢复。以下命令是供应商文档中的模式，并针对固定的这个版本进行了调整。它们不是本指南执行实时升级的结果。[更新 Open WebUI](https://docs.openwebui.com/getting-started/updating/)

1. **清点存储。** 在标准 Docker 设置中，`open-webui` 挂载到 `/app/backend/data`。记录绑定挂载、外部数据库、对象存储和自定义环境变量。使用 pip 时，请在更改环境前找到当前应用数据目录和数据库。不要假设聊天导出就是完整备份。
2. **停止写入后备份。** 停止应用，或创建一致的数据库快照，然后将卷、任何外部数据库和上传文件复制到单独的存储。供应商文档介绍了 Docker 卷归档。根据部署情况调整卷名称和备份路径。确认归档可以打开，并先在独立实例上演练恢复，再依赖它。[备份与恢复](https://docs.openwebui.com/getting-started/updating/#backup--restore)
3. **阅读发行说明和迁移指南。** v0.12.4 发行说明没有列出待披露的安全修复，也没有给出受影响版本范围。不要为这些修复指定 CVE，也不要假设 v0.12.4 之前的所有版本都受某个已知漏洞影响。更新指南警告数据库迁移可能是单向的，且不同版本的副本混用会带来问题。如果多个 worker 或副本共用一个数据库，请同时停止它们，并遵循[多副本迁移流程](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)。回滚可能需要升级前的数据库备份。

## 更新已安装的软件包

**Docker，针对固定标签调整的供应商流程：**备份后，拉取官方标准镜像，并使用相同的持久卷、配置和 `WEBUI_SECRET_KEY` 重建容器。示例假定使用默认命名卷，并且代理上游绑定在本机。不要将真实密钥粘贴到 shell 历史记录。通过现有的受保护环境或密钥管理机制提供密钥。保留当前部署中的 GPU、Ollama、自定义网络、数据库及其他选项。[更新 Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [官方镜像标签](https://docs.openwebui.com/getting-started/quick-start/)

```bash
docker pull ghcr.io/open-webui/open-webui:v0.12.4
docker rm -f open-webui
docker run -d --name open-webui --restart always \
  -p 127.0.0.1:3000:8080 \
  -v open-webui:/app/backend/data \
  --env-file ./open-webui.env \
  ghcr.io/open-webui/open-webui:v0.12.4
```

**运行前检查 `./open-webui.env`：**文件必须已存在，权限应受限，并包含现有的 `WEBUI_SECRET_KEY` 和必需配置。回环地址绑定适用于同一主机上的代理，不适用于另一台机器上的代理。使用 Compose 时，只将服务镜像更改为固定标签，然后在现有项目中运行 `docker compose pull open-webui` 和 `docker compose up -d open-webui`。保留相同的卷和环境配置。这些命令仅供参考，并非对你当前部署进行过验证的迁移步骤。

**pip，供应商固定版本更新流程：**在现有虚拟环境中停止服务，安装指定版本的软件包，并使用相同的数据目录和环境重新启动。不要另建 Python 环境或创建空数据库。供应商的通用更新说明使用 `pip install -U open-webui`。下方版本约束将本检查清单固定到 v0.12.4。[更新 Open WebUI](https://docs.openwebui.com/getting-started/updating/) · [快速入门](https://docs.openwebui.com/getting-started/quick-start/)

```bash
python -m pip install --upgrade 'open-webui==0.12.4'
python -m pip show open-webui
```

**检查正在运行的服务，而不只是已安装的软件包。**查看 `docker logs open-webui` 或 pip 服务日志中的启动版本，并与登录后应用显示的版本比较。供应商更新指南建议检查容器日志并打开登录页面。如果界面显示旧资源，请强制刷新浏览器。如果启动时报告迁移错误，在诊断问题之前应保持服务不可用。未检查恢复要求前，不要在已迁移的数据库上回退到旧二进制文件。[更新后检查](https://docs.openwebui.com/getting-started/updating/)

## 重启后检查访问权限

**供应商说明的行为：**v0.12.4 会对没有 **Allow Chat Export** 权限的用户隐藏文件夹导出、已归档聊天导出和聊天复制操作。对于没有相应共享权限的用户，模型、提示、工具、知识、技能、笔记和文件夹的访问控制项也会隐藏。共享文件夹的查看者在所有者归档聊天后，不再收到实时聊天更新。共享链接的查看者在所有者取消共享所有聊天后，也不再收到实时更新。控件隐藏属于界面行为，并不能证明服务器已修复某个未指明的漏洞。[发行说明](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)

**建议的运维验证：**使用没有导出和共享权限的测试账户，检查相关操作是否消失。使用有权限的账户，确认预期操作仍可用。在共享文件夹中创建不含敏感信息的测试聊天，从另一个账户查看，以所有者身份归档，并确认查看者不再收到新的更新。再通过共享链接和 **Unshare All Chats** 重复测试。重新检查已保存的授权和旧链接。不要假设归档内容或历史副本已被删除。

| 检查区域 | 验证内容 |
|---|---|
| **角色和群组** | 删除过期成员和管理员分配。检查新获批准用户和受限用户的有效权限。 |
| **模型和工具** | 查看每个模型的访问授权、关联工具、创建工具的权限以及提供方凭据。使用非管理员账户测试。 |
| **知识和文件** | 检查知识库协作者、资源授权、附件和共享设置。验证一个已被撤销访问权限的账户。 |
| **聊天和导出** | 检查共享文件夹、共享链接、已归档聊天和 Allow Chat Export 分配。撤销不再需要的链接。 |

这些清点项目是**运维建议**，并非 v0.12.4 新增的保证。供应商的[加固指南](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)介绍了分层角色、群组、逐资源授权、工作区权限、API 密钥和网络部署位置。

## 弥补账户和网络方面的不足

- **注册，供应商设置：**如果账户由管理员或身份提供方创建，请关闭开放注册。参照[加固指南](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)检查 `ENABLE_SIGNUP` 和持久化管理员设置。对新账户采用严格的审批规则。
- **API 密钥，运维检查：**盘点已发放的密钥，删除未使用的密钥，并将密钥创建和端点访问限制在所需角色与路由范围内。根据供应商加固指南，密钥拥有创建者的权限。不要将密钥放入文章示例或应用日志。
- **管理员，运维检查：**删除废弃的管理员账户，强制采用可靠的登录控制，检查 MFA 是否可用，并调查意外账户变更。在停用冗余管理员前，测试账户恢复流程。
- **网络边界，供应商指导：**将服务放在 VPN、访问代理或带有身份验证和 IP 允许列表的反向代理后。不要在没有身份验证的情况下公开服务。对于可访问的服务，避免设置 `WEBUI_AUTH=False`。没有自身身份验证的反向代理不能单独替代应用登录。[加固 Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)

**适用范围：**此检查清单适用于官方 Open WebUI 版本和文档所述的标准安装方式。它不验证分支版本、衍生镜像或第三方软件包。v0.12.4 发行说明没有声称漏洞正在被利用。请查看[项目安全公告](https://github.com/open-webui/open-webui/security/advisories)，了解后续披露及其各自受影响和已修复的版本。未阅读先前公告的版本范围前，不要将该公告中的修复归因于 v0.12.4。

## 来源与参考资料

- [Open WebUI v0.12.4 发行说明](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
- [Open WebUI 安全公告](https://github.com/open-webui/open-webui/security/advisories)
- [更新 Open WebUI，包括备份、回滚和迁移](https://docs.openwebui.com/getting-started/updating/)
- [Open WebUI 快速入门和官方镜像标签](https://docs.openwebui.com/getting-started/quick-start/)
- [加固 Open WebUI](https://docs.openwebui.com/getting-started/advanced-topics/hardening/)
- [多副本更新和迁移](https://docs.openwebui.com/troubleshooting/multi-replica/#updates-and-migrations)

---
title: "博弈 Helium 网络：使用 MiddleMan 和 Chirp 堆栈数据包多路复用器利用漏洞"
date: 2023-02-18
toc: true
draft: false
description: "了解如何利用 MiddleMan 和 Chirp Stack Packet Multiplexer 的漏洞来玩弄 Helium 网络，以及这样做的风险和后果。"
tags: ["氦气网", "覆盖证明", "中间人", "Chirp 堆栈数据包多路复用器", "赌博", "利用漏洞", "LoRaWAN网络", "加密货币", "区块链", "去中心化网络", "热点", "欺骗", "作弊", "非法活动", "处罚", "网络完整性", "奖励", "恶意行为者", "网络安全", "合法主机"]
cover: "/img/cover/A_cartoonish_depiction_of_a_group_of_individuals_exploiting.png"
coverAlt: "一群人利用氦气球的卡通形象，背景是 LoRaWAN 网关和 MiddleMan 或 Chirp 堆栈数据包多路复用器的图像。"
coverCaption: ""
---

**免责声明**：
重要的是要注意，玩 Helium 网络是一种非法和不道德的活动，受到 Helium 社区和更广泛的加密货币和区块链社区的强烈反对。网络游戏破坏了网络的完整性，并损害了为网络提供有价值覆盖的合法主机。

此外，虽然使用 MiddleMan 和 Chirp Stack Packet Multiplexer 来利用 Helium 网络中的漏洞可能令人担忧，但需要注意的是，这些问题只能由 Helium 通过引入安全网关来解决。这将需要更换网络上的所有热点，这是一项艰巨的任务，但可能不可行。因此，Helium 社区需要保持警惕并积极主动地应对网络游戏带来的挑战。

还值得注意的是，Helium 团队已经意识到这个问题有一段时间了，并已采取措施解决这个问题，但还需要采取更多行动来解决这个问题。社区呼吁采取实际行动来解决这些漏洞，并确保网络能够以安全可靠的方式继续扩展和发展。

通过撰写本文，我们希望提高人们对 Helium 网络游戏问题以及使用 MiddleMan 和 Chirp Stack Packet Multiplexer 来利用系统漏洞的认识。我们相信，通过阐明这个问题并对其进行更多宣传，Helium 社区以及更广泛的区块链和加密货币社区可以齐心协力解决这个问题，并努力打造一个更安全、更值得信赖的网络。

此外，通过强调这个问题，我们希望鼓励 Helium 团队采取更果断的行动来解决网络中的漏洞，并实施更强大的安全措施来防止未来的游戏。我们认为，对于 Helium 团队而言，重要的是要公开他们为解决此问题所做的努力，并与社区沟通他们在修复这些漏洞方面的进展。

最后，通过对这个问题进行更多宣传，我们希望鼓励人们提高对在 Helium 网络上玩游戏的风险和后果的认识和教育。用户必须了解网络道德行为的重要性以及游戏可能造成的潜在危害。通过共同努力解决这些问题，我们可以帮助确保 Helium 网络的持续发展和成功。

总而言之，社区或我们都不容忍在 Helium 网络上玩游戏，我们鼓励用户在参与网络时以道德和合法的方式行事。尽管网络中存在可被利用的漏洞，但重要的是要保持警惕并积极主动地解决这些问题，并努力为所有用户打造一个更安全、更可靠的网络。

## 如何使用 MiddleMan 和 Chirp 堆栈数据包多路复用器来博弈 Helium 网络
Helium 网络是一个去中心化的 LoRaWAN® 网络，通过奖励 Helium 代币或 $HNT 来补偿那些托管物理热点的人。该系统称为覆盖证明 (PoC)。随着网络的发展和对这个项目的认识的提高，越来越多的作弊者正在利用协议和奖励机制。在本文中，我们将讨论如何使用 MiddleMan 和 Chirp Stack Packet Multiplexer 来玩转 Helium 网络。

## 了解 Helium 网络游戏问题
Helium 网络依靠覆盖证明来确保热点在需要的地方提供覆盖。但是，该系统容易受到游戏、欺骗、黑客攻击和其他可能损害网络的不良行为的影响。 Helium 网络上的游戏问题使合法主机每月损失数千美元 HNT。 Helium, Inc 与 DeWi 已在 2022 年初采取积极行动，帮助根除这一问题。

## 所需硬件
- [Dragino LPS8](https://www.ebay.com/sch/i.html?_nkw=dragino+lps8)
- [Other Lorawan Gateways that Use the Semtech Forwarder](https://amzn.to/41bcskb)
- [Raspberry Pi](https://amzn.to/3KjFCYp)
- [Other PC that can run docker images or linux software](https://amzn.to/3YkFhcj)

## 使用 MiddleMan 来博弈 Helium 网络
玩 Helium 网络的一种方法是使用 MiddleMan。 MiddleMan 是一种软件工具，可用于创建伪造的热点，该热点似乎在特定位置提供覆盖。通过使用 MiddleMan，用户可以创建一个假热点，即使该热点实际上并不位于该区域，该热点也会因在特定区域提供覆盖而获得奖励。

要使用 MiddleMan，用户需要安装该软件并创建一个假热点。然后，用户可以配置热点以使用 GPS 欺骗工具向 Helium 网络报告其位置。 Helium 网络会认为假热点在指定位置提供覆盖，并会奖励用户 $HNT。

您可以将您的 lorawan 网关设置为指向该软件，它会操纵这些值，以便所有收到的 PoC 都被视为有效。使用 semtech 转发器是 LoraWAN 社区中的各种标准之一。解决操纵问题需要重新发明轮子并从头开始实施他们自己的协议。校验和和加密之类的东西可以防止这种情况发生。但也会让拥有不同硬件的供应商更难制作热点。更不用说它是一个受支持的用例，拥有一个氦气矿工和多个 lora 网关以提高覆盖范围。尽管这更多是企业级问题。

 - [helium-DIY-middleman](https://github.com/curiousfokker/helium-DIY-middleman)

## 使用 Chirp 堆栈数据包多路复用器来玩 Helium 网络
另一种玩 Helium 网络的方法是使用 Chirp Stack Packet Multiplexer。 Chirp Stack Packet Multiplexer 是一种可用于创建虚拟热点的工具，可以从多个物理热点接收数据包。通过使用 Chirp Stack Packet Multiplexer，用户可以创建一个虚拟热点，从多个位置的物理热点接收数据包，这将增加获得的奖励。

要使用 Chirp Stack Packet Multiplexer，用户需要安装该软件并将其配置为从多个位置的物理热点或 lorawan 网关接收数据包。热点将接收数据包并将其位置报告给 Helium 网络，Helium 网络将向用户奖励 $HNT。

这允许多个转发器输入和多个网关输出。 LoraWAN 社区中有此软件的合法用例，但在氦气中使用它最多是一个灰色区域。这取决于您如何使用它以及您的意图。

设置这个需要一些配置文件。但它可以在 5 分钟或更短的时间内完成。
- [chirpstack-packet-multiplexer](https://github.com/brocaar/chirpstack-packet-multiplexer)


## 博弈 Helium 网络的风险和后果
玩 Helium 网络是一项有风险的非法活动，可能会造成严重后果。 Helium, Inc 与 DeWi 一起积极致力于检测和防止网络游戏，被发现玩网络游戏的用户将受到处罚。

对 Helium 网络进行游戏的处罚可能包括失去对网络的访问权限、永久禁止热点以及丢失通过游戏赚取的任何 $HNT。此外，对 Helium 网络进行游戏会破坏网络的完整性，并损害为网络提供有价值覆盖的合法主机。

＃＃ 结论
虽然 Helium 网络为合法热点主机提供了通过覆盖证明获得奖励的机会，但它也为希望玩弄系统的恶意行为者提供了一个有吸引力的目标。 MiddleMan 和 Chirp Stack Packet Multiplexer 的使用虽然不受 Helium Inc. 或更广泛的社区的宽恕，但却是一些不良行为者如何利用网络中的漏洞以牺牲他人为代价获取回报的一个例子。

对于 Helium 社区来说，继续共同努力识别和解决网络游戏非常重要，因为它威胁到系统的完整性并破坏合法主机的努力。这可能包括努力开发和实施更复杂的检测和预防措施，以及提高对网络游戏风险和后果的认识和教育。

最终，Helium 网络的成功取决于其利益相关者是否愿意共同努力构建一个安全、可靠和值得信赖的系统，为用户提供真正的价值。通过保持警惕和积极主动地应对游戏带来的挑战，社区可以帮助确保 Helium 网络继续朝着积极的方向发展和发展。
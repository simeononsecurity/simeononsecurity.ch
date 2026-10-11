---
title: "Local AI Secure Server Knowledge Check"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Test model selection, local inference, performance measurement, server access, updates, and recovery."
genre: ["Artificial Intelligence", "Self-Hosted", "Assessment"]
tags: ["local AI quiz", "Ollama quiz", "local LLM server assessment", "AI server security questions"]
cover: "/img/cover/local-ai-secure-server-knowledge-check.webp"
coverAlt: "Local AI server review sheet with model, memory, network, identity, and recovery checks"
coverCaption: "Assessment cover placeholder. Image generation follows editorial review."
---

[Return to the Local AI Course](/local-ai-secure-server-course/)

**Answer all ten questions without the key.** A score of eight or higher prepares you for the capstone. Correct every missed security item before continuing.

## Quiz Steps

1. Create **`local-ai-knowledge-check.md`**.
2. Record one answer and one sentence of reasoning per question.
3. Use the key to score your work.
4. Link each missed item to a repaired lesson record.

## Questions

1. Which planning formula best represents local inference memory?
   - A. Model file size only
   - B. Weights plus context state, runtime buffers, concurrency margin, and operating margin
   - C. Parameter count divided by CPU cores
   - D. Storage space plus network speed

2. What does a model file digest establish?
   - A. Accuracy on your task
   - B. Safety from prompt injection
   - C. Identity against a trusted reference digest
   - D. License permission

3. Which measurement pair should stay separate?
   - A. Prompt processing and token generation rates
   - B. CPU name and operating system
   - C. Model publisher and license
   - D. Port and protocol

4. Why should the first API test use loopback?
   - A. Loopback increases parameter count
   - B. Loopback limits network reach during setup
   - C. Loopback adds user authentication
   - D. Loopback verifies model quality

5. Which result proves GPU offload occurred?
   - A. A configuration request alone
   - B. Runtime diagnostics and device memory activity
   - C. A model card claim
   - D. Faster typing in the terminal

6. Which server path has the strongest boundary?
   - A. Public native runtime port
   - B. LAN native runtime port with no identity
   - C. Private route through an authenticated TLS gateway to a loopback runtime
   - D. Port forwarding from a home router

7. Why limit context and concurrency together?
   - A. Both affect memory allocation and service capacity
   - B. Both change the model license
   - C. Both rotate credentials
   - D. Both select a GPU driver

8. What should a server access log record by default?
   - A. Every full prompt and response
   - B. Identity, route, model, sizes, decision, duration, and status
   - C. User passwords
   - D. Model weights

9. Which update package supports rollback?
   - A. The newest model tag only
   - B. A screenshot of the dashboard
   - C. Prior runtime, model digest, configuration, and passing test record
   - D. A larger context setting

10. What should happen when the native runtime listens on `0.0.0.0` unexpectedly?
   - A. Continue testing from the internet
   - B. Stop the service, restore loopback binding, and recheck listeners
   - C. Add another model
   - D. Delete benchmark results

## Answer Key

| # | Answer | Reason |
|---|---|---|
| **1** | B | Weights form one part of runtime memory use. |
| **2** | C | A digest supports artifact identity against a known reference. |
| **3** | A | Prompt evaluation and generation measure different phases. |
| **4** | B | Loopback keeps early service access on one host. |
| **5** | B | Observed diagnostics and device activity establish placement. |
| **6** | C | The gateway supplies identity and policy while the runtime stays off the network. |
| **7** | A | Parallel requests multiply active context and raise memory demand. |
| **8** | B | Metadata supports operations while reducing raw-content collection. |
| **9** | C | Rollback needs the prior artifacts, settings, and evidence. |
| **10** | B | Unexpected broad binding requires containment and verification. |

## Expected Result

A passing score is **8 out of 10**. Questions 4, 6, 8, 9, and 10 form the security gate. Answer all five correctly before the capstone.

## Troubleshooting

- **Memory answers stay unclear:** Revisit [Lesson 1](/local-ai-secure-server-course/01-hardware-model-fit/) and your fit worksheet.
- **Performance terms blend together:** Revisit [Lesson 3](/local-ai-secure-server-course/03-measure-tune/) and label both phases in your table.
- **Network controls seem redundant:** Map the native runtime and gateway as separate processes with separate duties.
- **Rollback lacks a model artifact:** Add the prior digest and storage location to your update record.

## Verify Completion

Record your score, security-gate score, and corrections. Pass when your total reaches eight, all five security items are correct, and each missed question has a repaired artifact.

Continue with the [Local AI Server Capstone](/local-ai-secure-server-course/07-capstone/).

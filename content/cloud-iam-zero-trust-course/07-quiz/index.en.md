---
title: "Cloud IAM and Zero Trust Quiz"
date: 2026-10-10
lastmod: 2026-10-11
toc: true
draft: false
description: "Test cloud identity, effective permissions, human and workload access, zero trust policy, and teardown before reviewing the answer key."
genre: ["Cloud Security", "Identity and Access Management", "Zero Trust"]
tags: ["cloud IAM quiz", "zero trust quiz", "least privilege assessment", "AWS IAM", "Azure RBAC", "Google Cloud IAM"]
cover: "/img/cover/cloud-iam-zero-trust-quiz.webp"
coverAlt: "Cloud identity policy questions beside allow, deny, and teardown evidence."
coverCaption: "Check access decisions and cleanup evidence."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**Answer every question before opening the key.** Add one sentence explaining each choice.

## Questions

1. Which item answers who receives a temporary session?
   A. Permission policy only
   B. Trust relationship
   C. Audit retention
   D. Resource tag only

2. Which design best fits a CI workload?
   A. Shared administrator password
   B. Long-lived access key in repository secrets
   C. OIDC federation with exact issuer, audience, subject, and short session
   D. Human emergency account

3. What happens when an applicable AWS explicit deny conflicts with an allow?
   A. The newest policy wins
   B. The broadest policy wins
   C. The request is denied
   D. The user chooses

4. Which record establishes effective access?
   A. One role name
   B. One group membership
   C. Principal, session, action, resource, every applicable layer, conditions, and final decision
   D. A console screenshot only

5. Which access belongs in an emergency path?
   A. Daily deployments
   B. Routine report review
   C. Recovery from identity or policy failure
   D. Every privileged change

6. Which zero trust statement is accurate?
   A. A private network grants implicit trust
   B. Resource access uses identity, action, context, policy, and telemetry
   C. Every request needs a human approval
   D. Zero trust is one vendor product

7. Why is service-account impersonation sensitive?
   A. Impersonation never creates logs
   B. A less privileged principal might obtain a more privileged session
   C. Service accounts lack permissions
   D. Impersonation requires static keys

8. Which lab action violates the course safety rules?
   A. Confirming the active project
   B. Creating a temporary read-only identity
   C. Creating a service account key for convenience
   D. Verifying absence after deletion

9. What does a last-used value prove?
   A. Complete safety of removal
   B. Activity observed within the provider's tracking and retention limits
   C. Business ownership
   D. Absence of indirect use

10. What completes teardown?
    A. Running a delete command
    B. Closing the terminal
    C. Removing grants and identities, then passing absence checks
    D. Waiting for the next billing cycle

## Submit Your Attempt

Record all ten choices and reasons. Do not change the first attempt after opening the key. Use a second correction column for revised answers.

> **Expected Result:** your reasons explain policy behavior, not provider logo or role-name guesses.

Score **9 out of 10 or higher** before starting the capstone. A score of 7 or 8 requires corrected reasons and a clean-copy retest. A score of 0 to 6 requires another pass through Lessons 1 through 6 before the retest.

## Verify Your Work

- [ ] All ten questions have answers and reasons
- [ ] The first attempt is saved
- [ ] No answer key was open during the attempt

## Next Steps

Open the [Cloud IAM and Zero Trust Quiz Answer Key](/cloud-iam-zero-trust-course/09-quiz-answer-key/). Score the saved attempt and correct missed reasons before starting the capstone.

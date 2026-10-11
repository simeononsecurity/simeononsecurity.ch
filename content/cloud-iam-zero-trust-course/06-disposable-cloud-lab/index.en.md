---
title: "Cloud IAM Lesson 6: Disposable Provider Lab"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Create a read-only identity in one cloud sandbox, inspect its grant, then remove and verify every lab object. AWS adds policy simulation."
genre: ["Cloud Security", "Identity and Access Management", "Security Lab"]
tags: ["disposable cloud lab", "AWS IAM CLI", "Azure managed identity", "Google Cloud service account", "cloud teardown", "least privilege lab"]
cover: "/img/cover/disposable-cloud-iam-lab.webp"
coverAlt: "Temporary AWS, Azure, and Google Cloud identities created, tested, and removed."
coverCaption: "Finish the lab with verified absence."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**Choose one provider track in a dedicated sandbox.** Each track creates read-only identity state, inspects the grant, removes every object created in this run, and checks absence. The AWS track simulates policy decisions. None of the tracks proves a live access denial by the new identity.

Do not use production. Confirm the active provider context before every create command.

## Lab Record

```text
Provider:
Account, subscription, or project:
Operator identity:
Start time UTC:
Objects created:
Object identifiers returned by create commands:
Preflight absence result:
Expected allow:
Expected deny:
Test type, live or simulated:
Teardown commands:
Absence checks:
End time UTC:
Residual objects:
```

## AWS Track

Download [the trust policy](/downloads/cloud-iam-zero-trust-course/aws-trust-policy.json) and [read policy](/downloads/cloud-iam-zero-trust-course/aws-read-policy.json). Replace `111122223333` with the sandbox account ID and `REPLACE_WITH_APPROVED_SANDBOX_OPERATOR_ROLE` with one existing, approved operator role name. The operator also needs a caller policy allowing `sts:AssumeRole` on this lab role. Do not replace the principal with the account-root ARN, which delegates trust to the account.

```bash
LAB_AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
aws sts get-caller-identity
aws iam get-role --role-name sos-iam-lab-reader
```

The final preflight command must return `NoSuchEntity`. If the role exists or the command fails for another reason, stop. Confirm the named operator role exists and its ARN matches the edited trust policy. Record the role's returned ARN after creation. Delete only that recorded role.

Create the role and inline policy.

```bash
aws iam create-role \
  --role-name sos-iam-lab-reader \
  --assume-role-policy-document file://aws-trust-policy.json \
  --tags Key=CourseLab,Value=true

aws iam put-role-policy \
  --role-name sos-iam-lab-reader \
  --policy-name sos-iam-lab-read-policy \
  --policy-document file://aws-read-policy.json
```

Simulate one allowed and one denied action.

```bash
aws iam simulate-principal-policy \
  --policy-source-arn "arn:aws:iam::${LAB_AWS_ACCOUNT_ID}:role/sos-iam-lab-reader" \
  --action-names s3:ListAllMyBuckets iam:CreateUser \
  --query 'EvaluationResults[].{Action:EvalActionName,Decision:EvalDecision}' \
  --output table
```

Expected simulated decisions are `allowed` for `s3:ListAllMyBuckets` and `implicitDeny` for `iam:CreateUser`. Simulation permissions and provider limitations affect results. This command does not prove the operator is trusted, able to assume the role, or able to list buckets in a live session. Record any evaluation warning.

Teardown:

```bash
aws iam delete-role-policy \
  --role-name sos-iam-lab-reader \
  --policy-name sos-iam-lab-read-policy

aws iam delete-role --role-name sos-iam-lab-reader

aws iam get-role --role-name sos-iam-lab-reader
```

The final command should return `NoSuchEntity`.

## Azure Track

Confirm the subscription, choose a region, then create a resource group and user-assigned managed identity.

```bash
az account show --output table
LAB_AZURE_RG=sos-iam-lab-rg
LAB_AZURE_LOCATION=centralus
az group exists --name "$LAB_AZURE_RG"
```

The last command must return `false`. Stop if the group exists or the check fails. Record the new group's ID from the create response, and delete only that group and identity after successful creation.

```bash

az group create --name "$LAB_AZURE_RG" --location "$LAB_AZURE_LOCATION"
az identity create --resource-group "$LAB_AZURE_RG" --name sos-iam-lab-reader
```

Create and verify a Reader assignment at the resource-group scope.

```bash
LAB_AZURE_PRINCIPAL_ID=$(az identity show --resource-group "$LAB_AZURE_RG" --name sos-iam-lab-reader --query principalId --output tsv)
LAB_AZURE_SCOPE=$(az group show --name "$LAB_AZURE_RG" --query id --output tsv)

az role assignment create \
  --assignee-object-id "$LAB_AZURE_PRINCIPAL_ID" \
  --assignee-principal-type ServicePrincipal \
  --role Reader \
  --scope "$LAB_AZURE_SCOPE"

az role assignment list --assignee "$LAB_AZURE_PRINCIPAL_ID" --scope "$LAB_AZURE_SCOPE" --output table
```

Reader does not grant role-assignment write access. This track inspects an assignment. It does not sign in as the managed identity or observe a denied action. Record the role definition and scope as design evidence, then use the offline test matrix for the denied-action case.

Teardown:

```bash
az role assignment delete \
  --assignee-object-id "$LAB_AZURE_PRINCIPAL_ID" \
  --role Reader \
  --scope "$LAB_AZURE_SCOPE"

az identity delete --resource-group "$LAB_AZURE_RG" --name sos-iam-lab-reader
az group delete --name "$LAB_AZURE_RG" --yes
az group exists --name "$LAB_AZURE_RG"
```

The final command should return `false` after deletion finishes.

## Google Cloud Track

Confirm the active account and project.

```bash
gcloud auth list
LAB_GCP_PROJECT_ID=$(gcloud config get-value project)
gcloud projects describe "$LAB_GCP_PROJECT_ID"
gcloud iam service-accounts describe \
  "sos-iam-lab-reader@${LAB_GCP_PROJECT_ID}.iam.gserviceaccount.com"
```

The final preflight command must report a missing service account. Stop if the service account exists or the check fails for another reason. Record the created account email. Delete only that account and its binding after successful creation.

Create a service account and grant Viewer at the sandbox project.

```bash
LAB_GCP_SA_NAME=sos-iam-lab-reader
LAB_GCP_SA_EMAIL="${LAB_GCP_SA_NAME}@${LAB_GCP_PROJECT_ID}.iam.gserviceaccount.com"

gcloud iam service-accounts create "$LAB_GCP_SA_NAME" \
  --display-name="SimeonOnSecurity IAM Lab Reader"

gcloud projects add-iam-policy-binding "$LAB_GCP_PROJECT_ID" \
  --member="serviceAccount:${LAB_GCP_SA_EMAIL}" \
  --role="roles/viewer"

gcloud projects get-iam-policy "$LAB_GCP_PROJECT_ID" \
  --flatten="bindings[].members" \
  --filter="bindings.members:serviceAccount:${LAB_GCP_SA_EMAIL}" \
  --format="table(bindings.role,bindings.members)"
```

Viewer excludes IAM policy changes. This track inspects the project binding. It does not impersonate the service account or observe a denied action. Use the offline test matrix for that case. Do not create a service account key for testing.

Teardown:

```bash
gcloud projects remove-iam-policy-binding "$LAB_GCP_PROJECT_ID" \
  --member="serviceAccount:${LAB_GCP_SA_EMAIL}" \
  --role="roles/viewer"

gcloud projects get-iam-policy "$LAB_GCP_PROJECT_ID" \
  --flatten="bindings[].members" \
  --filter="bindings.members:serviceAccount:${LAB_GCP_SA_EMAIL}" \
  --format="table(bindings.role,bindings.members)"

gcloud iam service-accounts delete "$LAB_GCP_SA_EMAIL" --quiet
gcloud iam service-accounts describe "$LAB_GCP_SA_EMAIL"
```

The policy query should return no binding rows for the exact service-account member. The final command should report a missing service account. If either check fails, the lab is not closed.

**Expected result:** One provider track ends with a recorded read-only grant, a documented policy-administration limitation, and no remaining objects created by the lab. AWS adds simulated allow and deny decisions. Mark live access tests `not run` unless you separately execute and document them with approved sandbox authority.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Create is denied** | Use a sandbox administrator approved for the lab or finish the offline analysis route |
| **Role assignment is delayed** | Recheck after provider propagation and record timestamps |
| **Delete fails** | Remove inline policies, bindings, assignments, or dependent objects first |
| **Context points to the wrong environment** | Stop, record the context, and do not run create commands |
| **A lab name already exists** | Stop. Do not modify or delete that object. Use a fresh sandbox or a new lab name throughout the track |
| **Absence check still finds an object** | Repeat the exact teardown step and inspect dependency errors |

## Verify Completion

- [ ] Provider context was recorded before creation
- [ ] Temporary names use the `sos-iam-lab` prefix
- [ ] Assignment or policy grants read-only access on paper, and the test type is labeled
- [ ] Policy administration is absent from the grant, with live denial marked untested unless observed
- [ ] No key or client secret was created
- [ ] Teardown removed only objects recorded as created by this run
- [ ] Absence checks passed

**Primary references, checked 2026-10-10:** [AWS CLI create-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html), [AWS CLI simulate-principal-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/simulate-principal-policy.html), [Azure CLI role assignments](https://learn.microsoft.com/en-us/cli/azure/role/assignment), [Google Cloud service account create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create), and [Google Cloud project IAM binding removal](https://docs.cloud.google.com/sdk/gcloud/reference/projects/remove-iam-policy-binding).

## Next Steps

Take the [Course Quiz](/cloud-iam-zero-trust-course/07-quiz-answer-key/), then complete the [Capstone](/cloud-iam-zero-trust-course/08-capstone-answer-key/).

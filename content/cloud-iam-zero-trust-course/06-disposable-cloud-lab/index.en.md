---
title: "Cloud IAM Lesson 6: Disposable AWS, Azure, and Google Cloud Labs"
date: 2026-10-10
lastmod: 2026-10-10
toc: true
draft: false
description: "Create a temporary read-only cloud identity, verify its assignment, test denied access, remove every lab object, and prove teardown in AWS, Azure, or Google Cloud."
genre: ["Cloud Security", "Identity and Access Management", "Security Lab"]
tags: ["disposable cloud lab", "AWS IAM CLI", "Azure managed identity", "Google Cloud service account", "cloud teardown", "least privilege lab"]
cover: "/img/cover/disposable-cloud-iam-lab.webp"
coverAlt: "Temporary AWS, Azure, and Google Cloud identities created, tested, and removed."
coverCaption: "Finish the lab with verified absence."
---

[Return to the Cloud IAM and Zero Trust Lab Course](/cloud-iam-zero-trust-course-start/)

**Choose one provider track in a dedicated sandbox.** Each track creates read-only identity state, verifies the grant, removes every object, and checks absence.

Do not use production. Confirm the active provider context before every create command.

## Lab Record

```text
Provider:
Account, subscription, or project:
Operator identity:
Start time UTC:
Objects created:
Expected allow:
Expected deny:
Teardown commands:
Absence checks:
End time UTC:
Residual objects:
```

## AWS Track

Download [the trust policy](/downloads/cloud-iam-zero-trust-course/aws-trust-policy.json) and [read policy](/downloads/cloud-iam-zero-trust-course/aws-read-policy.json). Replace `111122223333` in the trust policy with the sandbox account ID.

```bash
LAB_AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
aws sts get-caller-identity
```

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

Expected decisions are `allowed` for `s3:ListAllMyBuckets` and `implicitDeny` for `iam:CreateUser`. Simulation permissions and provider limitations affect results. Record any evaluation warning.

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

Reader does not grant role-assignment write access. Record the role definition and scope rather than trying a destructive denied operation.

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
```

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

Viewer excludes IAM policy changes. Do not create a service account key for testing.

Teardown:

```bash
gcloud projects remove-iam-policy-binding "$LAB_GCP_PROJECT_ID" \
  --member="serviceAccount:${LAB_GCP_SA_EMAIL}" \
  --role="roles/viewer"

gcloud iam service-accounts delete "$LAB_GCP_SA_EMAIL" --quiet
gcloud iam service-accounts describe "$LAB_GCP_SA_EMAIL"
```

The final command should report a missing service account.

## Troubleshooting

| Problem | Fix |
|---|---|
| **Create is denied** | Use a sandbox administrator approved for the lab or finish the offline analysis route |
| **Role assignment is delayed** | Recheck after provider propagation and record timestamps |
| **Delete fails** | Remove inline policies, bindings, assignments, or dependent objects first |
| **Context points to the wrong environment** | Stop, record the context, and do not run create commands |
| **Absence check still finds an object** | Repeat the exact teardown step and inspect dependency errors |

## Verify Completion

- [ ] Provider context was recorded before creation
- [ ] Temporary names use the `sos-iam-lab` prefix
- [ ] Allowed access is read-only
- [ ] Policy administration stays denied or absent from the role
- [ ] No key or client secret was created
- [ ] Teardown removed every lab object
- [ ] Absence checks passed

**Primary references, checked 2026-10-10:** [AWS CLI create-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html), [AWS CLI simulate-principal-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/simulate-principal-policy.html), [Azure CLI role assignments](https://learn.microsoft.com/en-us/cli/azure/role/assignment), [Google Cloud service account create](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/create), and [Google Cloud project IAM binding removal](https://docs.cloud.google.com/sdk/gcloud/reference/projects/remove-iam-policy-binding).

## Next Steps

Take the [Course Quiz](/cloud-iam-zero-trust-course/07-quiz-answer-key/), then complete the [Capstone](/cloud-iam-zero-trust-course/08-capstone-answer-key/).

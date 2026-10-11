---
title: "DevOps and Platform Engineering for Developers"
draft: false
toc: true
date: 2026-07-22
lastmod: 2026-10-10
description: "Practice CI, staged delivery, rollback, infrastructure state, secrets, observability, service ownership, and safe teardown through a small local pipeline."
tags: ["DevOps for developers", "platform engineering career", "CI/CD pipeline", "infrastructure as code terraform", "observability for developers", "kubernetes for developers", "docker deployment", "managing a development team", "software development career playbook"]
coverAlt: "A digital illustration showing a developer at a desk with multiple screens displaying CI/CD pipelines, container orchestration, and Terraform scripts, set in a dark, modern workspace."
coverCaption: ""
cover: "/img/cover/devops-platform-engineering-ci-cd-iac-observability.webp"
---

[Return to the Software Development Career Playbook](/software-development-career-playbook-start/)

**Developers who ship or support a service benefit from understanding its delivery and recovery path.** Ownership differs across product, operations, reliability, security, and platform teams. Record the boundary for the service you work on.

## What DevOps Actually Means

**DevOps** describes practices which improve collaboration and feedback across software delivery and operations. The operating model might use developer ownership, a shared rotation, a reliability team, a platform team, or a managed service.

In practice this means:

- Teams assign CI/CD ownership with documented review and escalation.
- On-call work needs training, shadowing, staffing, pay or time policy, escalation, and rest.
- A team might define selected infrastructure as code under review while retaining controlled manual procedures for other changes.
- Feedback loops between production behavior and development decisions are short.

## CI/CD Pipelines

A **CI/CD pipeline** automates selected integration and delivery steps. Continuous delivery keeps a releasable change ready for a production decision. Continuous deployment automatically releases every change which passes the configured gates.

**Continuous Integration (CI)** runs automated checks on configured events such as a pull request, push, merge queue, or schedule:
- Code checkout and dependency installation
- Static analysis and linting
- Unit and integration tests
- Build artifact creation

**Continuous delivery or deployment** automates selected delivery steps. Production release might remain a manual, risk-based gate:
- Deploy to staging on merge to main
- Run smoke tests and integration tests against staging
- Deploy to production (automated or with manual gate)
- Post-deployment health check and rollback trigger

| CI/CD Tool | Notes |
|---|---|
| **GitHub Actions** | GitHub-hosted workflow service configured with YAML files |
| **GitLab CI** | Built into GitLab, powerful, good for self-hosted scenarios |
| **Jenkins** | Mature and highly extensible, complex to maintain |
| **CircleCI** | Managed platform, good parallelization |
| **Buildkite** | Hybrid: managed orchestration + self-hosted agents |

## Containers and Kubernetes

**Docker** packages an application and its dependencies into an image that teams can run as a container. Containers suit some deployment models. Managed platforms, virtual machines, and other approaches also serve production workloads. Choose a model based on operations, security, cost, and the service's requirements.

**Kubernetes (K8s)** orchestrates containers at scale: scheduling, scaling, load balancing, health checking, and rolling deployments. As a developer you need to understand:

- Writing a basic `Deployment`, `Service`, and `Ingress` manifest.
- How pod resource requests and limits work.
- How to read pod logs and describe events for debugging.
- How rolling deployments and rollbacks work.
- How `ConfigMaps` and `Secrets` manage configuration.

Control-plane ownership depends on the organization and hosting model. Developers might use a managed platform, work with a platform team, or operate selected cluster components.

## Infrastructure as Code (IaC)

**Infrastructure as Code** means defining cloud infrastructure (servers, databases, networks, IAM policies) in version-controlled code rather than clicking through consoles.

**Terraform** is one infrastructure-as-code option. Its declarative configuration describes desired resources, while providers and state influence planning and change execution.

Key Terraform concepts:

- **Providers**: plugins that connect Terraform to cloud APIs (AWS, Azure, GCP).
- **Resources**: individual infrastructure objects (EC2 instance, S3 bucket, RDS database).
- **State**: Terraform stores state locally by default. Teams often configure a protected remote backend for shared work, locking, backup, and access control.
- **Modules**: reusable infrastructure components.
- **Plan and apply**: `terraform plan` shows what will change, `terraform apply` executes the changes.

Depending on team boundaries, a developer might propose or review infrastructure code for databases, queues, storage, identity, and environment configuration.

## Observability

**Observability** uses system outputs and analysis to investigate behavior. Metrics, logs, and traces are common signals. Profiles, events, topology, and other signals might also matter.

| Pillar | What It Provides | Tools |
|---|---|---|
| **Metrics** | Quantitative measurements over time (request rate, latency, error rate, CPU) | Prometheus, CloudWatch, Datadog |
| **Logs** | Textual records of events from each service | Elasticsearch/Kibana, Datadog, CloudWatch Logs, Loki |
| **Traces** | The path of a request across multiple services | Jaeger, Zipkin, Datadog APM, AWS X-Ray |

The RED method offers a useful starting view for request-driven services:

1. **Request rate**: how many requests is the service handling per second?
2. **Error rate**: what portion of requests fail under the service definition? Set alerts from an agreed service-level objective, traffic level, and error budget rather than a universal threshold.
3. **Latency**: which percentile and window match the service objective and traffic volume? Derive an alert from that objective rather than always alerting on p99.

This is the **RED method** (Rate, Errors, Duration). Complementary is the **USE method** for infrastructure resources (Utilization, Saturation, Errors).

## The Platform Engineer Role

A **platform engineer** builds and maintains the internal platforms that other developers use to ship software: CI/CD systems, container orchestration, secrets management, observability tooling, deployment frameworks, and developer portals.

A platform team might treat internal teams as customers and measure whether its supported paths improve delivery, reliability, security, or developer experience for a defined group.

Role scope and compensation vary by employer, geography, level, and on-call expectations. See [Software Development Specializations](/software-development-career-playbook/getting-started-in-software-development/software-development-specializations/) for a comparison method.

**Primary sources, checked 2026-10-10:** [Terraform state documentation](https://developer.hashicorp.com/terraform/language/state), [GitHub Actions events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/), and [Google SRE service-level objectives](https://sre.google/workbook/implementing-slos/).

## Next Steps

- [Building and Leading a Development Team](/software-development-career-playbook/managing-a-development-team/building-and-leading-a-development-team/)
- [Software Development Methodologies](/software-development-career-playbook/managing-a-development-team/software-development-methodologies-agile-scrum-kanban/)
- [Software Development Career Playbook Home](/software-development-career-playbook-start/)

## Practice and Verify

**Artifact: Safe delivery rehearsal.** Complete the [Python Starter Lab](/files/software-development-career-playbook/python-starter/README.md). It supplies the tiny application, five tests, deliberate failure, MIT license, and [GitHub Actions workflow](/files/software-development-career-playbook/python-starter/ci-test.yml).

Run the documented compile, unit-test, dependency, help, license, and starter secret checks. Create `.stage/releases/v1`, point `.stage/current` to it, and confirm the stable output. Run `test_app.py` with `failure_fixture.py` and confirm one failure plus `DELIVERY BLOCKED`. Verify the v1 output still works. Promote the passing v2 copy, point current back to v1, verify rollback, and remove `.stage` plus the temporary clone.

> **Expected result:** The good run passes, the deliberate failure blocks delivery, rollback restores service, and no secret or paid resource remains.

```text
REDACTED COMPLETED EXAMPLE
Tests: 5 passed. Injected failure: 1 failed and DELIVERY BLOCKED. Rollback output: 1 meters = 3.28 feet. Teardown: .stage and clone removed.
```

**Pass checklist**

- [ ] The artifact uses dated, role-specific evidence
- [ ] Claims, ownership, team credit, and unknown values are truthful
- [ ] Privacy, secrets, licenses, accessibility, cost, and safety received review where relevant
- [ ] A reviewer or repeatable check produced feedback
- [ ] The record names a timed next action and checkpoint

**Source rule:** Use official CI, Terraform, container, and SLO documentation checked 2026-10-10.

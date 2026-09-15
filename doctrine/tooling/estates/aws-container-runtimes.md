# Supplement: AWS Container Runtimes

**Scope:** Optional mapping for teams standardising on **Amazon Web Services**. This is **one** estate's concrete choices; it does **not** override portable principles in `doctrine/principles/`. See [README.md](README.md) and [../../principles/timeless-principles-and-tooling.md](../../principles/timeless-principles-and-tooling.md).

For the vendor-neutral decision frame, see [../../principles/container-runtime-choice.md](../../principles/container-runtime-choice.md).

- **Cloud / vendor:** Amazon Web Services
- **Owning team / channel:** record your owning team and channel here when adopting this supplement
- **Last reviewed:** 2026-08-16

---

## Runtime Choice Within This Estate

| Workload pattern | Typical choice on AWS | When to escalate to a different tier |
| --- | --- | --- |
| A **single HTTP container** (stateless web app or API) with straightforward networking | **AWS App Runner** — the paved default; fully managed build/deploy/scale with no cluster, load balancer, or node pools to own | Escalate when VPC/networking needs outgrow it: VPC-internal dependencies beyond an egress [VPC connector](https://docs.aws.amazon.com/apprunner/latest/dg/network-vpc.html), listener-rule/routing control, sidecar or multi-container tasks, non-HTTP protocols |
| Services needing **VPC-native networking**, path/host routing, sidecars, background workers, or scheduled jobs | **Amazon ECS on AWS Fargate** behind an **Application Load Balancer** — serverless containers without self-managed nodes | Escalate when you need the **full Kubernetes API**: operators, bespoke CNI/policy at node boundary, features ECS does not expose |
| Need **full cluster semantics** per [container-runtime-choice.md §2](../../principles/container-runtime-choice.md) | **Amazon EKS** — document **why** in an ADR or platform catalogue; apply [../../principles/kubernetes-platform-security.md](../../principles/kubernetes-platform-security.md) | — |

**Note:** Product names, SKUs, and feature boundaries change; treat this table as **starting guidance** for this estate, not immutable law.

---

## Relational Data (AWS)

- **Amazon RDS for PostgreSQL** is this estate's default managed relational store for the workloads above; the schema/migration discipline in [../../principles/data-and-migrations.md](../../principles/data-and-migrations.md) is unchanged by the hosting choice.

---

## Observability (AWS)

- **Logs / metrics / traces backend:** **Amazon CloudWatch**.
- **OpenTelemetry export path:** applications instrument with **OpenTelemetry** and export via the **AWS Distro for OpenTelemetry (ADOT)** collector or an OTLP-compatible endpoint into CloudWatch — see [../observability.md](../observability.md) for the general "managed ingestion" pattern.

---

## Identity And Secrets

- **Workload identity pattern:** **IAM roles attached to the workload** — ECS [task IAM roles](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) or the App Runner instance role — rather than long-lived access keys in application configuration.
- **Secret store:** **AWS Secrets Manager** for secrets; **SSM Parameter Store** for non-secret configuration. Values are injected at runtime via the workload's role, never baked into images, per [../../principles/container-runtime-choice.md §3](../../principles/container-runtime-choice.md).

---

## References

Per [../../patterns/source-authority-and-evidence-grading.md](../../patterns/source-authority-and-evidence-grading.md) §6: all entries **S5** (product-scoped vendor documentation, in scope), **rolling** whole-document pointers (rationale: cited as entry points to starting guidance written to survive documentation revisions; no numbered sub-elements quoted), accessed **2026-08-16**.

- AWS App Runner — what it is: https://docs.aws.amazon.com/apprunner/latest/dg/what-is-apprunner.html
- Amazon ECS on AWS Fargate: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
- Application Load Balancer overview: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html
- Amazon EKS — what it is: https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html
- Amazon RDS for PostgreSQL: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html
- AWS Secrets Manager: https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html
- SSM Parameter Store: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html
- AWS Distro for OpenTelemetry (ADOT): https://aws-otel.github.io/docs/introduction

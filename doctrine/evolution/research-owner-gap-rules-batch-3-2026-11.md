# Owner Gap Rules From Implementation Batch 3

Date and source access date: 2026-11-18. Repository basis: `8b518c9` and the companion change.
Status: research basis for [ADR 0057](../../docs/adr/0057-close-owner-gaps-from-implementation-batch-3.md) (accepted 2026-11-18). Model research and model review; no independent human or domain review.

## Question

The [batch 3 owner audit](research-impl-backlog-batch-3-composition-2026-11.md) found that two of the new references had no owner for the centre of their subject. Application Deployment had none for how a workload signals health, stops, stays available, or is bounded. Infrastructure Delivery had none for how a plan relates to an environment, who applies it, or how drift ends. What does external practice support, and at what strength?

## Source Ledger

Classes follow [Source Authority And Evidence Grading](../patterns/source-authority-and-evidence-grading.md) §2. A delegated agent retrieved about 70 pages and saved their text. The lead author re-read the passages behind each rule below in a sample of those saved copies (marked †). No archive copies were captured. Publisher counts treat each organisation as one source, however many pages it publishes.

### Workload Runtime Shape

| Source | Class and scope | Supports | Qualifies |
| --- | --- | --- | --- |
| [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/pods/probes/): probes†, [pod termination](https://kubernetes.io/docs/concepts/workloads/pods/pod-termination/)†, [disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)†, [resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) | S5, product-scoped; describes mechanisms | Liveness decides restart and readiness decides traffic; a termination signal is followed by a grace period and then a kill; a disruption budget limits how many replicas voluntary disruption takes down; requests drive scheduling and limits are enforced | Probes and resource settings are optional in the product. Rolling updates are not limited by disruption budgets. A badly set liveness probe can cause cascading restarts |
| [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel10-bp01.html)†: REL10-BP01, REL11-BP02, REL11-BP05 | S5, vendor framework | Production workloads run in at least two isolated locations; traffic shifts to healthy resources; capacity is provisioned so remaining locations carry the load | Start with multiple zones and add regions only when requirements justify it; static stability has a cost |
| [Azure Architecture Center, Health Endpoint Monitoring](https://learn.microsoft.com/en-us/azure/architecture/patterns/health-endpoint-monitoring)†, and [Well-Architected redundancy guidance](https://learn.microsoft.com/en-us/azure/well-architected/reliability/redundancy) | S5, vendor framework | Separate liveness and readiness endpoints, shallow for the first and deeper for the second; redundancy for critical flows across zones | A deep readiness check on an unreliable dependency can itself cause cascading failure; prefer managed services that provide redundancy |
| [Google SRE book](https://sre.google/sre-book/load-balancing-datacenter/), chapters 20 and 22, and appendix B | S4, edited book | A task being stopped tells clients to go elsewhere, finishes in-flight requests, then exits; process health and service health are distinct checks; provision for a planned and an unplanned outage at once | The mechanisms described are the publisher's own |
| [The Twelve-Factor App, Disposability](https://12factor.net/disposability)† | S6, canonical practitioner essay; undated beyond a 2017 footer | Processes stop gracefully on a termination signal and are also robust against sudden death | No bounded time |
| Managed-platform contracts ([Cloud Run](https://docs.cloud.google.com/run/docs/container-contract), [Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/application-lifecycle-management)) | S5, product-scoped | The platform withholds traffic until the container listens, sends a termination signal with a short grace period, and bounds resources itself | On these platforms much of the shape is provided, not built |

Four organisations support each of the four properties. They disagree on two details: what a readiness check may depend on, and whether to cap CPU. One vendor guide recommends CPU limits and advises against them on the same page.

### Configuration Bound At Deploy Time

| Source | Class and scope | Supports | Qualifies |
| --- | --- | --- | --- |
| [The Twelve-Factor App, Config](https://12factor.net/config) and Build, release, run | S6 | Configuration that varies between deploys is separate from code; a release is a build combined with a deploy's configuration | Prescribes environment variables, which [configuration and secrets](../principles/configuration-and-secrets.md) §1 already qualifies for credentials |
| [Kubernetes ConfigMaps](https://kubernetes.io/docs/concepts/configuration/configmap/)† | S5 | Environment-specific configuration is decoupled from images so the same image runs in different environments | Not for confidential data |
| [DORA capability: deployment automation](https://dora.dev/capabilities/deployment-automation/)† | S4, disclosed-methodology research programme | Use the same packages for every environment, keeping environment-specific configuration separate | No mechanism |
| [AWS Well-Architected REL05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel05-bp01.html) | S5 | A packaged default parameter set as a fallback when a parameter store is unavailable | Shows a packaged default is compatible with the rule |

### Infrastructure Plans, Applies, And Drift

| Source | Class and scope | Supports | Qualifies |
| --- | --- | --- | --- |
| HashiCorp Terraform documentation: [running in automation](https://developer.hashicorp.com/terraform/tutorials/automation/automate-terraform)†, [plan](https://developer.hashicorp.com/terraform/cli/commands/plan), [lifecycle](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle), [drift](https://developer.hashicorp.com/terraform/tutorials/state/resource-drift) | S5, product-scoped | Plan to a file, have a person review it, apply that file; allow one outstanding plan because applying one invalidates others against the same state; separate state per environment; a locking remote backend; a guard that rejects plans destroying a marked resource; drift is either overwritten by applying or kept by updating configuration | It does not say a stale saved plan is rejected. Auto-approval is allowed for non-critical infrastructure. Some teams still run locally |
| [Google Cloud, best practices for Terraform operations](https://docs.cloud.google.com/docs/terraform/best-practices/operations)†, and its style and security pages | S5 | Always plan first, save the plan, have an owner approve it, execute that plan; run through an automated pipeline with the pipeline's service identity; one root configuration and backend per environment; deletion protection on stateful resources | Local planning with a developer's own credentials is accepted for prototyping |
| AWS: [CloudFormation change sets and best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html), drift detection, and [Prescriptive Guidance for Terraform backends](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/backend.html)† | S5 | Preview changes, including replacement or deletion of a database, before updating; limit who can modify production to the pipeline and break-glass roles; separate backends per environment; detect drift regularly; a scheduled plan as the drift check, reviewed before deciding to apply or update configuration | A change set does not guarantee success. A retention setting does not cover replacement during an update |
| [Azure Well-Architected, infrastructure as code](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/infrastructure-as-code-design) | S5 | Deploy infrastructure changes only through code and pipelines; preview changes including deletions | Delete locks slow recovery and do not replace backups |
| [Pulumi, detecting and reconciling drift](https://www.pulumi.com/docs/iac/operations/stack-management/drift/) | S5 | Two directions for drift: remediate by re-applying code, or adopt by updating the program, with a pull request suggested for adoption | Advises adopting first when unsure |
| [OpenGitOps principles v1.0.0](https://opengitops.dev/) | S4, foundation specification | Agents continuously reconcile actual state toward desired state | No adoption path and no human decision |
| [Kief Morris, Using Pipelines to Manage Environments](https://infrastructure-as-code.com/posts/environment-pipeline.html) (2017) | S6, named practitioner | One definition promoted through a pipeline; nobody applies to a shared environment from their own machine | Criticises pipelines that only plan and apply one environment |

Support by rule: five organisations for reviewing a computed diff before applying; two for applying the plan that was reviewed; four vendors and two independent authors for applying from a pipeline; four for calling out destruction of data-bearing resources, with the backup step stated by one; three for resolving drift in either of two directions.

## Synthesis

1. **The properties are settled; the details are not.** Every source agrees a workload should say when it is ready, stop cleanly, survive losing an instance, and declare what it needs. They disagree on what readiness checks and whether to cap CPU. The rule should state the property and leave the detail to tooling.
2. **Health checks can cause the outage.** Three sources warn that a check tied to a shared dependency takes every instance out together. The rule needs that warning inside it.
3. **Redundancy is proportionate.** The sources tie redundancy to the required availability and state its cost. The library already scopes objectives to user-facing paths, so the rule should follow the objective and allow a recorded single instance.
4. **Managed platforms provide much of this.** [Container runtime choice](../principles/container-runtime-choice.md) prefers managed platforms. The duty there is to confirm and configure, not to build.
5. **A plan belongs to one environment and one moment.** Per-environment state is the common practice and a plan is computed against it. "Apply what was reviewed, or re-plan" follows. The stronger claim that a tool rejects a stale plan is not supported and is not used.
6. **Pipeline applies have a local-run exception.** The sources accept local runs against personal or prototype instances. The rule is about shared environments.
7. **Drift has two honest endings.** Revert it or adopt it through review. A reconciler does the first automatically. Neither the sources nor the library describe leaving it as known divergence.
8. **Three items are internal consistency, not new practice.** The maintenance-window allowance exists in collaboration §8 and a checklist but not in the migration owner. The rollback decider rule and the reviewed-desired-state rule meet in declared-state estates without a stated order. The automated-rollback sentence lacks its subject.

## Decision Input

| Decision | Owner | Strength proposed | Admission |
| --- | --- | --- | --- |
| D1 Workload runtime shape: health signals, graceful stop, redundancy, declared resources | [Reliability](../principles/reliability-slo-incidents.md) §8 | SHOULD, production services; redundancy where an availability objective exists | C2: four independent S5 publishers and an S4 book per property |
| D2 Environment-specific configuration bound at deploy or start | [Configuration and secrets](../principles/configuration-and-secrets.md) §1 | SHOULD | C2: one S4 source and independent S5 and S6 sources; consistent with build §5 |
| D3 Infrastructure plans per environment, pipeline applies, destructive changes called out, drift resolved | [GitOps and declarative operations](../patterns/gitops-and-declarative-operations.md) §4 | SHOULD | C2: independent S5 publishers per rule; mostly vendor documentation, flagged |
| D4 Maintenance window in place of version overlap | [Data and migrations](../principles/data-and-migrations.md) §1 | MAY | Internal consistency with collaboration §8 |
| D5 Rollback in declared-state estates; scope of the automated-rollback sentence | [Collaboration](../principles/collaboration.md) §8.1 | Clarification | Internal consistency with collaboration §2 and the GitOps pattern |

## Residual Risk

Most support is cloud-vendor or tool-vendor documentation; independent sources are thin and partly old. The workload vocabulary in the sources is shaped by one orchestrator. Rules drafted by a model from a sampled re-read may miss a qualification in pages the lead author did not open. No independent review is recorded.

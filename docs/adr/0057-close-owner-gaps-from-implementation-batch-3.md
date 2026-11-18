# ADR 0057: Close Owner Gaps Found By Implementation Batch 3

- **Status:** Accepted
- **Decision date:** 2026-11-18
- **Recorded date:** 2026-11-18
- **Retrospective:** No
- **Deciders:** Repository operator
- **Review provenance:** Operator-directed and operator-accepted on 2026-11-18; drafted and reviewed by a model, no independent human or domain review recorded
- **Research:** [Owner gap rules from implementation batch 3](../../doctrine/evolution/research-owner-gap-rules-batch-3-2026-11.md); findings in the [batch 3 owner audit](../../doctrine/evolution/research-impl-backlog-batch-3-composition-2026-11.md#resolution-in-this-change)
- **Canonical owners:** [Reliability](../../doctrine/principles/reliability-slo-incidents.md) §8 (D1); [Configuration And Secrets](../../doctrine/principles/configuration-and-secrets.md) §1 (D2); [GitOps And Declarative Operations](../../doctrine/patterns/gitops-and-declarative-operations.md) §4 (D3); [Data And Migrations](../../doctrine/principles/data-and-migrations.md) §1 (D4); [Collaboration](../../doctrine/principles/collaboration.md) §8.1 (D5)
- **Derived landings:** [Platform Readiness](../../doctrine/checklists/platform-readiness.md); [Build Readiness](../../doctrine/checklists/build-readiness.md); [Application Deployment](../../doctrine/impl/application-deployment.md); [Infrastructure Delivery](../../doctrine/impl/infrastructure-delivery.md); [Release And Rollback](../../doctrine/impl/release-and-rollback.md)

## Context

Four implementation references were composed from the screened backlog. Two could not describe the centre of their subject, because no owner states it. Application Deployment had no owner for how a workload signals health, stops, stays available, or is bounded. Infrastructure Delivery had no owner for how a plan relates to an environment, who applies it, or how drift ends. The audit also found three places where existing owners meet without a stated order.

## Decision

### D1. Workload runtime shape

Owner: reliability, new §8. Scope: production services. Where a managed platform provides a property, the duty is to confirm and configure it.

- **SHOULD:** a workload signals whether it is alive and whether it is ready for traffic as separate questions, and traffic is withheld until it is ready. Checks stay cheap and local.
- **SHOULD:** on a termination signal a workload stops taking new work, finishes or returns in-flight work within the platform's grace period, and exits. It also tolerates being killed without notice.
- **SHOULD (services with an availability objective):** run more than one instance across the failure domains the platform offers, with capacity to lose one, and bound how many instances planned maintenance removes at once. A single instance is a legitimate recorded choice where the objective allows downtime.
- **SHOULD:** a workload declares the compute and memory it needs and a memory bound, in the platform's terms. Whether to cap CPU is a platform policy choice.

### D2. Environment-specific configuration is bound at deploy or start

Owner: configuration and secrets §1.

- **SHOULD:** values that differ between environments are supplied when the artefact is deployed or started, not built into it, so the same artefact can be promoted. A packaged safe default for when a configuration source is unavailable is compatible with this.

### D3. Infrastructure plans, applies, and drift

Owner: the GitOps pattern §4, as new invariants 7 to 10. Existing invariant numbers do not change.

- **SHOULD (7):** where the tool computes a plan or diff, it is reviewed against the target environment's current state, and what is applied is the plan that was reviewed, or a recomputed one that is reviewed again. A plan belongs to one environment and is not promoted.
- **SHOULD (8):** applies to shared environments run from the pipeline under its scoped identity with shared, locked state. Local runs are for personal or prototype instances; anything else is break-glass.
- **SHOULD (9):** a plan that destroys or replaces a resource holding data is called out for explicit review, with deletion protection where the platform offers it and a verified backup or snapshot first.
- **SHOULD (10):** drift ends in one of two ways: revert the live change by re-applying declared state, or adopt it into the declaration through the reviewed path.

### D4. A maintenance window can replace version overlap

Owner: data and migrations §1.

- **MAY:** where service policy accepts a documented maintenance window, the old version stops before the change, so the overlap sequence does not apply. Forward-only change, a snapshot before high-risk steps, and a recovery path still do.

This records an allowance that collaboration §8 and Platform Readiness already carry.

### D5. Rollback where desired state is declared

Owner: collaboration §8.1.

- Where desired state is declared in version control, a rollback is a revert to the previously verified revision through that path. The decider can merge it under the documented emergency path of §2, and it is reviewed afterwards.
- The sentence "Automation does not widen exposure or roll forward" is scoped to the rollback automation it describes.

## Control Cost And Lifecycle

| Decision | Failure addressed | Evidence | Operating cost | Review trigger |
| --- | --- | --- | --- | --- |
| D1 | Traffic sent to instances that cannot serve; requests dropped on every deploy; one failure taking a service down; a workload starving its neighbours | Deployment configuration showing health signals, grace period, instance count and spread, and resource declarations | Mostly configuration; redundancy costs capacity | An incident traced to one of the four properties; a platform change that provides a property |
| D2 | Per-environment rebuilds, so the tested artefact is not the one deployed | One artefact digest across environments; configuration in deploy inputs | Low | A promotion blocked by built-in configuration |
| D3 | Applying something other than what was reviewed; workstation applies to shared environments; a data store destroyed by a routine plan; drift left standing | Plan output retained with the apply; pipeline identity in apply records; review notes on destructive plans; drift reports with a resolution | Pipeline and state set-up; review time for destructive plans | An unreviewed or stale apply; a destroyed data store; drift open beyond the estate's tolerance |
| D4 | A migration owner that contradicts a permission stated elsewhere | The recorded window | None | A window used to skip safety steps |
| D5 | On-call staff unsure whether a rollback needs a second approver in a declared-state estate | Emergency-path record and after-the-fact review | None | A rollback delayed by review rules |

Each rule can be simplified or retired if its review trigger shows cost without benefit.

## Alternatives Considered

- **Leave the gaps and keep the references silent.** Rejected; the references then omit what a reader most expects, and the operator asked for the gaps to be closed.
- **State the workload rules in the Kubernetes principle.** Rejected; the properties are not specific to one orchestrator, and the library prefers managed platforms.
- **A MUST for health signals and graceful stop.** Deferred; support is broad but comes from vendor documentation, and managed platforms provide parts of both.
- **Require CPU limits.** Rejected; the sources disagree.
- **Require applying the exact saved plan.** Rejected; tools differ, and one widely used hosted mode cannot apply a saved plan. "Reviewed, or re-planned and reviewed again" covers both.
- **Automatic revert as the only drift resolution.** Rejected; adoption through review is a legitimate ending that three sources describe.

## Consumer Impact And Migration

Change class: **normative additions** at SHOULD (D1 to D3), a **permission** made explicit (D4), and a **clarification** (D5). Compatibility: pre-1.0 minor.

Migration: check production workloads for the four runtime properties and record any single-instance choice; move environment-specific values out of built artefacts; give each environment its own reviewed plan and move shared-environment applies into the pipeline; mark data-bearing resources for explicit review on destruction; decide how each open drift item ends.

## Acceptance Criteria

- Each owner section states its rule with strength and scope.
- Platform and Build Readiness carry derived prompts that link their owners.
- Application Deployment and Infrastructure Delivery reflect the new owner text and no longer list it as unowned; Release And Rollback carries the declared-state rollback sentence.
- The batch 3 owner audit marks which findings are resolved here and which remain open.
- The ADR index lists this decision, and doctrine preflight passes.

## Residual Risk

Most support is vendor documentation shaped by one orchestrator and a few infrastructure tools. "Availability objective", "data-bearing", and "shared environment" remain estate judgements. The lead author re-read a sample of the sources, not all of them. Model review only.

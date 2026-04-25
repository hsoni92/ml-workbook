# Cloud Services and Platforms: Connect the Dots (Weeks 1-13)

This is the full course in one flow: understand why cloud exists, design with architecture principles, choose global and account structures, secure identity and network boundaries, run compute and containers, design storage and data tiers, adopt serverless and observability, automate delivery, and finally codify infrastructure with IaC.

---

## The 13-week spine (one connected story)

### Week 1 - Cloud foundations and service models
- Core: what cloud is, key traits, IaaS/PaaS/SaaS, public/private/hybrid/multi-cloud, shared responsibility.
- Why it matters: sets the responsibility boundary between provider and customer.
- Enables next: Week 2 turns these ideas into architecture principles.
- Hub: [week-1/1-Cloud services and platforms introduction transcript.md](week-1/1-Cloud services and platforms introduction transcript.md)

### Week 2 - Cloud architecture principles
- Core: scalability vs elasticity, availability vs fault tolerance, multi-tenancy, AWS Well-Architected and cross-cloud frameworks.
- Why it matters: gives non-functional design targets before picking services.
- Enables next: Week 3 maps principles to global cloud regions and service choices.
- Hub: [week-2/14-Module Summary .md](week-2/14-Module Summary .md)

### Week 3 - Cloud ecosystem and global footprint
- Core: region/availability-zone thinking, compute/network/database service landscape, provider positioning and career/certification orientation.
- Why it matters: architectural decisions depend on geography, latency, compliance, and service maturity.
- Enables next: Week 4 focuses on account governance and IAM control.
- Hub: [week-3/1-Module Introduction Tran.md](week-3/1-Module Introduction Tran.md)

### Week 4 - IAM and account governance
- Core: account structure, users/groups/roles, policy evaluation logic, MFA, access keys, AWS Organizations.
- Why it matters: secure identity design is the control plane for everything else.
- Enables next: Week 5 applies these controls to compute workloads.
- Hub: [week-4/14-Module Summary .md](week-4/14-Module Summary .md)

### Week 5 - Compute with EC2 and elastic scaling
- Core: EC2 basics, instance lifecycle, security groups, SSH access, EBS volume types, snapshots, AMI mindset, load balancing and auto scaling.
- Why it matters: establishes core workload hosting patterns and scaling primitives.
- Enables next: Week 6 formalizes networking patterns behind multi-tier systems.
- Hub: [week-5/1-Module Introduction transcript.md](week-5/1-Module Introduction transcript.md)

### Week 6 - VPC and network architecture
- Core: VPC, CIDR/subnets, route tables, IGW/NAT, public vs private placement, multi-tier connectivity, peering basics.
- Why it matters: network boundaries determine reachability, exposure, and isolation.
- Enables next: Week 7 packages workloads into portable container units.
- Hub: [week-6/1-Module Introduction .md](week-6/1-Module Introduction .md)

### Week 7 - Containers and orchestration
- Core: containers vs VMs, Docker internals, Dockerfile/image lifecycle, registries/ECR, Kubernetes architecture and workload management.
- Why it matters: standardizes runtime and deployment portability across environments.
- Enables next: Week 8 pairs compute patterns with correct storage patterns.
- Hub: [week-7/1-Module Introduction .md](week-7/1-Module Introduction .md)

### Week 8 - Cloud storage architecture
- Core: object/block/file storage, S3 buckets/objects, storage classes, encryption, bucket policies/IAM integration, EFS, static hosting patterns.
- Why it matters: storage choice drives durability, latency, cost, and security posture.
- Enables next: Week 9 deepens state management with managed databases.
- Hub: [week-8/1-Module introductionTranscript.md](week-8/1-Module introductionTranscript.md)

### Week 9 - Managed database design
- Core: relational vs NoSQL, managed vs self-managed trade-offs, RDS engines/features, backups/failover/read replicas, DynamoDB fit and pricing models.
- Why it matters: data layer design determines consistency, scale, and operational burden.
- Enables next: Week 10 shifts to event-driven/serverless execution patterns.
- Hub: [week-9/1-Module introduction transcript.md](week-9/1-Module introduction transcript.md)

### Week 10 - Serverless and event-driven systems
- Core: Lambda model, event sources, API Gateway integration, IAM for functions, monitoring and cost behavior, best practices and limits.
- Why it matters: reduces infrastructure management for bursty or event-centric workloads.
- Enables next: Week 11 adds observability, auditability, and cost governance.
- Hub: [week-10/1-Module introduction transcript.md](week-10/1-Module introduction transcript.md)

### Week 11 - Monitoring, logging, audit, and cost control
- Core: CloudWatch metrics/logs/alarms, CloudTrail audit trails, billing dashboards, budgets, tagging, cost-efficient architecture patterns.
- Why it matters: operations quality depends on visibility, traceability, and financial discipline.
- Enables next: Week 12 automates change delivery with DevOps/CI/CD.
- Hub: [week-11/1-Module Introduction .md](week-11/1-Module Introduction .md)

### Week 12 - DevOps and CI/CD pipelines
- Core: DevOps collaboration model, version control, CI/CD stages, tools, triggers/testing gates, GitHub Actions, rolling/blue-green/canary deployment strategies.
- Why it matters: turns manual release processes into reliable, repeatable delivery.
- Enables next: Week 13 codifies infrastructure itself as versioned software.
- Hub: [week-12/1-Module Introduction Transcript.md](week-12/1-Module Introduction Transcript.md)

### Week 13 - Infrastructure as Code (IaC) and Terraform
- Core: IaC fundamentals, declarative vs imperative, tool landscape, Terraform workflow, provider/resources/state, provisioning patterns.
- Why it matters: infrastructure becomes reproducible, reviewable, and automatable at scale.
- Enables next: end-to-end cloud platform engineering with architecture, operations, and delivery unified.
- Hub: [week-13/1-Module Introduction transcript.md](week-13/1-Module Introduction transcript.md)

---

## Cross-week threads you should see instantly

- **Responsibility and security thread:** Week 1 shared responsibility -> Week 4 IAM governance -> Week 6 network isolation -> Week 8/9 data protection -> Week 11 auditing and policy enforcement.
- **Scalability and resilience thread:** Week 2 principles -> Week 5 auto scaling/load balancing -> Week 9 replicas/failover -> Week 10 event-driven elasticity -> Week 12 safe rollout strategies.
- **Platform standardization thread:** Week 5 compute baseline -> Week 7 containers/Kubernetes portability -> Week 10 serverless abstraction -> Week 13 IaC standardization.
- **Cost-control thread:** Week 2 architecture trade-offs -> Week 8 storage class economics -> Week 9 database pricing models -> Week 10 serverless cost profile -> Week 11 budgets/tagging governance.
- **Automation maturity thread:** manual provisioning (early weeks) -> scriptable deployments (Week 12) -> fully codified infrastructure lifecycle (Week 13).

---

## End-to-end good-cloud-architecture checklist

1. **Model clarity:** deployment model and responsibility boundaries are explicit.
2. **Architecture goals:** scalability, reliability, security, and cost goals are defined before service selection.
3. **Identity and network controls:** least privilege IAM and segmented network design are enforced.
4. **Compute/runtime fit:** EC2, containers, or serverless is chosen by workload behavior.
5. **Data layer fit:** storage/database choice matches consistency, throughput, and recovery needs.
6. **Observability and governance:** metrics, logs, audit trails, budgets, and tags are configured early.
7. **Delivery reliability:** CI/CD includes testing gates and progressive rollout strategies.
8. **Infrastructure reproducibility:** IaC is versioned, reviewed, and consistently applied.

---

## 13 one-line hinges (rapid revision)

| Week | Hinge |
|------|-------|
| 1 | Cloud value starts with service-model and responsibility clarity. |
| 2 | Good architecture starts from non-functional requirements, not service names. |
| 3 | Region and provider choices shape latency, compliance, and resilience. |
| 4 | IAM is the security backbone of every cloud resource. |
| 5 | EC2 plus EBS plus Auto Scaling is the core elastic compute pattern. |
| 6 | VPC design decides what can talk to what, and what stays private. |
| 7 | Containers standardize runtime; Kubernetes standardizes workload control. |
| 8 | Storage is a design decision across access pattern, durability, and cost. |
| 9 | Database choice is a trade-off between model fit, scale, and operations. |
| 10 | Serverless trades server management for event-driven design discipline. |
| 11 | You cannot optimize or secure what you do not observe and audit. |
| 12 | CI/CD turns releases from manual events into repeatable systems. |
| 13 | IaC makes infrastructure consistent, testable, and auditable as code. |

---

Use this note as the map. Use weekly notes for depth; use this page to retain the full cloud architecture storyline.

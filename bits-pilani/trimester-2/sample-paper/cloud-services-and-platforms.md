# Model Question Paper – Cloud & DevOps (Practice Set)

**Time:** 2 hours
**Maximum marks:** 40

---

## Question 1 (5 + 5 marks)

### (a)

Explain the concept of operational expenditure (OpEx) in cloud computing.

How does shifting from CapEx to OpEx influence financial planning and scalability for organizations? (5 marks)

#### Answer

**OpEx in cloud computing** is spending that shows up on the income statement as you consume services: pay-as-you-go or subscription charges for compute, storage, networking, and managed services, usually billed monthly or by usage. You are renting capacity and capability instead of buying assets.

**CapEx (capital expenditure)** is upfront investment in owned hardware, data centers, and long-lived licenses; it is capitalized and depreciated over time.

**Impact on financial planning and scalability**

- **Cash flow and budgeting:** OpEx turns large upfront purchases into smaller, recurring costs, which can ease initial funding needs but requires disciplined forecasting of variable usage (costs grow with scale).
- **Elasticity:** Organizations can increase or decrease capacity quickly without waiting for procurement and installation cycles, so scaling tracks demand more closely.
- **Risk and agility:** Less sunk cost in physical infrastructure makes it easier to pivot or experiment; financial plans must still guard against bill shock through budgets, alerts, and reserved or savings plans where appropriate.

### (b)

Cloud migration involves different strategic approaches.

Compare Rehosting (Lift and Shift), Replatforming, and Refactoring with respect to effort, cost, and long-term benefits. Provide suitable use cases. (5 marks)

#### Answer

| Approach | Effort | Cost (typical) | Long-term benefits | Example use cases |
|----------|--------|----------------|--------------------|-------------------|
| **Rehosting (lift and shift)** | Lowest: move workloads with minimal change (e.g. VMs in cloud similar to on-prem). | Lower short-term migration cost; may carry inefficiencies (over-provisioned VMs, unused licenses). | Limited cloud-native gains unless optimized later; fastest path off data center. | Deadline-driven exit from a data center; legacy apps that cannot be changed quickly. |
| **Replatforming** | Medium: small cloud optimizations without full rewrite (e.g. move to managed DB, containerize). | Moderate migration plus some redesign cost. | Better operations (backups, patching), some cost and reliability improvements. | Moving a database to RDS while keeping app logic similar; adopting load balancers and auto scaling groups. |
| **Refactoring / re-architecting** | Highest: redesign for cloud (microservices, serverless, event-driven). | Highest upfront cost and time. | Best long-term agility, scalability, and often cost efficiency at scale. | Greenfield services; systems that need global scale, frequent releases, or strict resilience targets. |

**Summary:** Rehosting optimizes for speed; refactoring optimizes for future maintainability and cloud leverage; replatforming is a practical middle ground.

---

## Question 2 (6 + 4 marks)

### (a)

An application must be deployed in a secure and highly controlled cloud environment where:

- Only specific ports are allowed
- Internal services should communicate securely
- Direct access to backend servers must be restricted

Explain how the following can be used to achieve this:

- Security groups
- Network ACLs
- Private IP addressing
- Bastion host

(6 marks)

#### Answer

- **Security groups** are virtual firewalls attached to resources (for example EC2 instances or ENIs). They are **stateful**: return traffic for allowed connections is typically permitted automatically. You define **allow** rules for specific ports and source CIDRs or other security groups, which supports “only these ports from these callers” for application and admin traffic.

- **Network ACLs (NACLs)** apply at the **subnet** boundary. They are **stateless**: inbound and outbound rules must be explicit. They add a coarse layer for subnet-wide policies (for example denying certain IP ranges) and can complement security groups for defense in depth.

- **Private IP addressing** places backends in **private subnets** with RFC1918-style addresses not reachable from the public internet. Public ingress goes through load balancers or API gateways in public subnets; internal tiers talk over private IPs inside the VPC, which **restricts direct exposure** of database and app servers.

- A **bastion host** (jump box) is a **hardened, audited** instance in a controlled subnet used as the only SSH or RDP entry point to private resources. Admins connect to the bastion first, then to internal hosts, so backends do not need public IPs and access can be logged and limited.

Together: private IPs remove internet reachability for backends; security groups and NACLs narrow which ports and sources are valid; the bastion centralizes break-glass administrative access.

### (b)

Explain the difference between horizontal scaling and vertical scaling.

Discuss when each approach is more suitable in cloud environments. (4 marks)

#### Answer

**Vertical scaling (scale up/down)** increases or decreases **capacity of a single node**: more vCPUs, RAM, or faster disk on one instance. It is simple to reason about but hits **hardware ceilings** on one machine and may require downtime for large class changes.

**Horizontal scaling (scale out/in)** adds or removes **more instances** behind a load balancer or orchestrator. It fits **stateless** tiers and leverages cloud elasticity; the system can grow past the limits of one box.

**When to use which**

- Prefer **horizontal scaling** for web and API tiers that can be replicated, bursty traffic, and high availability (one node failure does not take down the tier).
- Prefer **vertical scaling** when the workload is **hard to shard** (some databases, single-node licensing, or strong in-memory locality), or when operational simplicity matters and the load fits one large instance.

Cloud providers support both: auto scaling groups for horizontal patterns, and easy instance size changes for vertical patterns.

---

## Question 3 (7 + 3 marks)

### (a)

Explain the lifecycle of a container in a Docker-based environment.

Include the stages from image creation to container execution and termination.

Also describe how versioning of images helps in maintaining application consistency. (7 marks)

#### Answer

**Lifecycle (Docker-style)**

1. **Define the application environment** in a `Dockerfile` (base image, dependencies, code, entrypoint).
2. **Build an image** with `docker build`: immutable layers are stacked; each instruction can create a cached layer.
3. **Tag and optionally push** the image to a **registry** (Docker Hub, ECR, GCR, etc.) so runtimes can pull the same bits everywhere.
4. **Create and start a container** from the image (`docker run` or orchestrator equivalent): a writable container layer is added; the process namespace, cgroups, and network are configured.
5. **Running state:** the main process executes; logs and metrics are collected; health checks may restart unhealthy containers.
6. **Stop and remove:** `docker stop` sends SIGTERM then SIGKILL; `docker rm` removes the container filesystem. The **image** remains unless deleted.

**Image versioning and consistency**

- **Tags** (for example `app:1.2.3`, `app:release-2024-04`) pin deployments to a known artifact so dev, staging, and production run the **same bytes**.
- **Digests** (content-addressable hashes) are stronger than tags alone because tags can be moved; orchestrators can deploy by digest for immutability.
- Versioned images support **rollbacks** (redeploy previous tag/digest) and **audits** (what code ran in production at a given time), reducing “works on my machine” drift.

### (b)

Why is service discovery important in distributed systems?

Provide a brief explanation in the context of containerized applications. (3 marks)

#### Answer

In distributed systems, **instances come and go** and IP addresses change. **Service discovery** lets clients find **healthy, current endpoints** without hard-coding IPs. A registry records providers; consumers query DNS or an API.

For **containerized apps**, replicas scale with load and reschedule across nodes. Platforms provide discovery via **Kubernetes Services and DNS**, **Docker Swarm** naming, or mesh and load-balancer integrations. Without it, configuration would be fragile and traffic would not reliably reach the right pods after each deployment or failure.

---

## Question 4 (5 + 5 marks)

### (a)

Explain the concept of CI/CD pipelines and describe the typical stages involved (such as build, test, deploy).

How do these pipelines improve software quality and delivery speed? (5 marks)

#### Answer

**CI (Continuous Integration)** automates integrating code changes: build, test, and feedback on every merge or commit. **CD** usually means **Continuous Delivery** (always releasable) or **Continuous Deployment** (automatic production deploy after gates).

**Typical stages**

1. **Source:** trigger on push or pull request.
2. **Build:** compile, package, create container images or artifacts.
3. **Test:** unit tests, integration tests, static analysis, security scans.
4. **Publish:** push artifacts/images to a registry with version tags.
5. **Deploy:** promote to staging then production (blue/green, canary, or rolling).
6. **Verify:** smoke tests and monitoring; rollback if checks fail.

**Benefits**

- **Quality:** defects surface **before** production; tests and reviews are mandatory steps, not optional.
- **Speed:** repeatable automation removes manual handoffs; smaller batches reduce risk and time-to-fix.
- **Traceability:** each release ties to a commit and pipeline run, aiding audits and rollbacks.

### (b)

Discuss the importance of infrastructure automation in modern DevOps practices.

Explain how tools like Terraform or similar IaC solutions help achieve consistency and reduce manual errors. (5 marks)

#### Answer

**Infrastructure automation** encodes environments (networks, VMs, databases, IAM) as **repeatable processes** instead of one-off console clicks. It supports **DevOps** goals: fast delivery, shared ownership, and reliable operations.

**Why it matters**

- Same environment can be reproduced for dev, staging, and prod, reducing configuration drift.
- Changes are **reviewed** like application code (pull requests, policies).
- Disasters and new regions are recoverable by re-applying definitions.

**Terraform-style IaC**

- **Declarative** desired state: you describe what should exist; the tool computes a **plan** and **applies** changes.
- **State** tracks real resources so updates are incremental, not blind re-creation.
- **Modules** reuse patterns; **workspaces** or stacks separate environments.

This cuts **manual errors** (wrong region, missed firewall rule, typos), improves **consistency** across teams, and makes infrastructure **auditable** and version-controlled.

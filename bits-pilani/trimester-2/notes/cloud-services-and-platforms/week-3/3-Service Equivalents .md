# Service Equivalents (Week 3)

## Table of Contents
- [Core Concepts](#core-concepts)
- [Terminology and Definitions](#terminology-and-definitions)
- [Detailed Explanations](#detailed-explanations)
- [Workflows / Process Steps](#workflows--process-steps)
- [Examples and Use Cases](#examples-and-use-cases)
- [Comparison Tables](#comparison-tables)
- [Key Takeaways and Summary](#key-takeaways-and-summary)
- [Quick Revision Notes and Memory Aids](#quick-revision-notes-and-memory-aids)
- [Exam Tips and Common Pitfalls](#exam-tips-and-common-pitfalls)

## Core Concepts
- One of the most important skills for any cloud professional: **translate services across cloud providers**.
- Different providers use different names, which often confuses beginners.
- The truth: **cloud providers differ more in branding than in fundamentals**.
- At a foundational level, all major cloud platforms provide the **same core building blocks** in four categories:
  1. Compute
  2. Storage
  3. Database
  4. Networking
- Once these categories are understood, switching between AWS, Azure, and Google Cloud becomes much easier.

## Terminology and Definitions
- **Compute Service**: A service that runs applications by providing virtual machines with CPU, memory, disk, and networking.
- **Object Storage**: Storage for unstructured files accessed via APIs; not mounted like traditional file systems.
- **Managed Relational Database**: A database service where the provider handles backup, patching, replication, failover, and monitoring.
- **Private Virtual Network**: A provider-managed, isolated network used for routing, segmentation, and security.
- **AWS EC2**: AWS compute service (virtual machines).
- **Azure Virtual Machine**: Azure compute service.
- **Google Compute Engine**: Google Cloud compute service.
- **AWS S3**: AWS object storage.
- **Azure Blob Storage**: Azure object storage.
- **Google Cloud Storage**: Google Cloud object storage.
- **AWS RDS**: AWS managed relational database.
- **Azure SQL Database**: Azure managed SQL database.
- **Google Cloud SQL**: GCP managed relational database.
- **AWS VPC / Azure Virtual Network / GCP VPC**: Private, isolated virtual networks.

## Detailed Explanations
### Compute Services
- Where applications actually run.
- Provide virtual machines with CPU, memory, disk, and networking.
- Equivalents:
  - **AWS**: EC2
  - **Azure**: Virtual Machine
  - **Google Cloud**: Compute Engine
- Users have **full control over the operating system**:
  - Decide software, configuration, and security.
- **Flexibility comes with responsibility**: patching, security, and maintenance.
- **Analogy**: Compute services are like **renting an empty house** — you can design it however you want, but you are responsible for everything inside.

### Storage Services (Object Storage)
- Used to store **files and unstructured data**: images, videos, documents, backups, logs.
- Equivalents:
  - **AWS**: S3
  - **Azure**: Blob Storage
  - **Google**: Cloud Storage
- Characteristics:
  - **Highly durable**.
  - **Scalable**.
  - **Cost efficient**.
- Not traditional file systems — you do **not install applications on them**.
- Accessed through **APIs**.
- **Analogy**: Massive cloud-scale **warehouse** — store items, retrieve when needed, don't worry about the building.

### Database Services
- Store structured transactional data (user accounts, orders, payments, records).
- Managed relational database equivalents:
  - **AWS**: RDS
  - **Azure**: SQL Database
  - **Google Cloud**: Cloud SQL
- Key word: **"managed"** — providers handle:
  - Backup
  - Patching
  - Replication
  - Failover
  - Monitoring
- Teams focus on **data and queries** rather than database infrastructure.
- Databases are **stateful and complex**, making managed services extremely valuable in real-world architectures.

### Networking Services
- Defines how everything connects **securely and efficiently**.
- Same concept across clouds: **a private, isolated virtual network**.
- Equivalents:
  - **AWS**: VPC
  - **Azure**: Virtual Network
  - **GCP**: VPC
- Provide:
  - **Private IP ranges**.
  - **Subnets**.
  - **Routing**.
  - **Firewalls**.
  - **Secure connectivity**.
- From an architectural perspective, **networking is the foundation of cloud security**.
- Poorly designed networking can make even the best application **vulnerable**.

### The Core Takeaway
- Different names, same fundamental concepts.
- If you understand **what a service does, why it exists, and where it fits**, you can **confidently work across cloud platforms**.

## Workflows / Process Steps
### Translating Between Clouds
1. Identify the **category**: compute, storage, database, or networking.
2. Locate the **equivalent service** on the target provider.
3. Understand the shared concept (e.g., object storage accessed via APIs).
4. Adapt configuration to the target provider's specific features.
5. Apply architectural principles consistently across providers.

## Examples and Use Cases
- Migrating a workload between AWS, Azure, and GCP by mapping EC2 → VM → Compute Engine.
- Storing images, videos, backups in any provider's object storage.
- Running MySQL/PostgreSQL/SQL Server via managed services across providers.
- Creating a private isolated network using VPC / Virtual Network / VPC.

## Comparison Tables
### Service Equivalents Across Providers
| Category | AWS | Azure | Google Cloud |
|---|---|---|---|
| Compute (VMs) | EC2 | Virtual Machine | Compute Engine |
| Object Storage | S3 | Blob Storage | Cloud Storage |
| Managed Relational DB | RDS | SQL Database | Cloud SQL |
| Private Network | VPC | Virtual Network | VPC |

### Key Characteristics by Category
| Category | Core Capability | Architectural Role |
|---|---|---|
| Compute | Run applications with full OS control | Flexibility + responsibility |
| Object Storage | Store unstructured files via APIs | Durable, scalable, cost efficient |
| Managed DB | Handle backups, patching, replication, failover, monitoring | Teams focus on data and queries |
| Networking | Private IPs, subnets, routing, firewalls | Foundation of cloud security |

### Analogies
| Category | Analogy |
|---|---|
| Compute | Renting an empty house |
| Object Storage | Massive cloud-scale warehouse |
| Managed DB | Provider handles plumbing; you focus on contents |
| Networking | Foundation of the house's security |

## Key Takeaways and Summary
- Cloud providers use different names, but underlying **concepts are the same**.
- Four core categories: **Compute, Storage (object), Database (managed relational), Networking**.
- Understanding categories makes it easier to **switch between AWS, Azure, and Google Cloud**.
- Networking is the **foundation of cloud security**, even more than individual service choices.

## Quick Revision Notes and Memory Aids
- Compute: **EC2 / VM / Compute Engine**.
- Object Storage: **S3 / Blob Storage / Cloud Storage**.
- Managed DB: **RDS / SQL Database / Cloud SQL**.
- Network: **VPC / Virtual Network / VPC**.
- Mantra: **Branding differs; fundamentals don't**.

## Exam Tips and Common Pitfalls
- Don't confuse **object storage** with block storage or file systems — object storage is API-accessed.
- "Managed" means provider handles infrastructure tasks but **not your schema/queries**.
- Networking misconfiguration is a **top security risk** — expect questions highlighting this.
- Remember all three network equivalents share the same concept even if two are both called "VPC."

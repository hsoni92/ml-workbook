# Storage Services Overview (Week 3)

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
- Storage is a **fundamental building block** in cloud computing.
- Almost every cloud workload relies on storage (website images, user uploads, logs, backups).
- Cloud storage is **decoupled from compute** — data lives independently of VMs:
  - Servers can be deleted.
  - Applications scaled or moved.
  - Data remains safe and accessible.
- **Object storage** is the most common form of cloud storage across providers.

## Terminology and Definitions
- **Storage Decoupling from Compute**: Data exists independently of compute instances.
- **Object Storage**: Storage where data is stored as **objects**, each containing:
  - The actual data.
  - Metadata describing it.
  - A unique identifier.
- **Bucket**: A container for objects (AWS terminology, also used conceptually elsewhere).
- **API (HTTP) Access**: Object storage is accessed via HTTP requests; not mounted like a disk.
- **Durability**: Design property ensuring data survives multi-system failures.
- **Storage Tier**: A class of storage optimized for frequency of access (frequent, infrequent, archive).
- **Lifecycle Policy**: Automated rule to move data between tiers.
- **AWS S3 / Azure Blob Storage / Google Cloud Storage**: Object storage equivalents.

## Detailed Explanations
### How Cloud Storage Differs From Traditional Storage
- Traditional storage is a **disk attached to a server** (similar to a personal laptop's hard disk).
- Cloud storage is **decoupled from compute**:
  - Data survives when compute is removed or scaled.
  - Workloads can move without losing data.

### Object Storage Basics
- Data is stored as **objects**; each object has:
  - Actual data.
  - Metadata.
  - Unique identifier.
- Unlike traditional file systems, object storage is **not mounted like a disk**.
- Accessed via **APIs over HTTP requests**.
- Scales almost **infinitely**.
- Perfect for **unstructured data**: images, videos, documents, backups, etc.

### AWS S3
- Oldest and most mature object storage service in the cloud world.
- Known for **extreme durability** — designed to keep data safe even if multiple systems fail.
- Data is stored in **buckets**; buckets hold objects.
- Integrates deeply with almost every AWS service.
- The **backbone of many architectures**.
- Common uses:
  - Website assets.
  - Media storage.
  - Data lakes.
  - Backups and archives.

### Azure Blob Storage
- Follows a similar **object storage model**.
- Designed with **strong enterprise integration** in mind.
- Fits naturally into **Microsoft environments**; integrates tightly with:
  - Active Directory.
  - Windows-based workloads.
  - Enterprise compliance tooling.
- Common uses:
  - Enterprise document storage.
  - Application data.
  - Media streaming.
  - Compliance and backup solutions.

### Google Cloud Storage (GCS)
- Designed for **simplicity and performance**.
- Shines in **data-heavy and analytics-driven workloads**.
- Benefits from Google's **private global network** for strong performance, especially for:
  - Large-scale data processing.
  - AI workloads.
- Common uses:
  - Big data pipelines.
  - ML data sets.
  - Cloud-native applications.
  - Media storage.

### Storage Tiers and Lifecycle Policies
- All three providers offer **multiple storage tiers**:
  - **Frequently accessed** data costs more.
  - **Infrequent / archived** data costs much less but takes longer to retrieve.
- Architects use **lifecycle policies** to automatically move data between tiers over time to balance cost and performance.

### Analogy
- Cloud storage = a **massive digital warehouse**:
  - Frequently used items → close and easy to access.
  - Rarely used items → stored farther away; cheaper but slow to retrieve.
  - You don't manage the warehouse — the cloud provider does.

### Real Differences Across Providers
- S3, Blob Storage, and Cloud Storage are **conceptually similar**.
- Real differences come from:
  - **Ecosystem integration**.
  - **Performance characteristics**.
  - **Enterprise alignment**.
- Object storage is the **foundation of modern cloud systems**: scalable, durable, cost-efficient.

## Workflows / Process Steps
### Using Cloud Object Storage
1. Create a bucket / container in the chosen provider.
2. Upload objects via the provider's API.
3. Set access policies (public/private, per-object or bucket-level).
4. Define **storage tiers** for each type of data.
5. Apply **lifecycle policies** to transition data over time.
6. Integrate with applications via APIs for read/write operations.

## Examples and Use Cases
- **Website assets** (images, videos, static files).
- **Application data** (uploads, backups).
- **Data lakes** for analytics.
- **Media streaming**.
- **Compliance and backup solutions**.
- **Big data pipelines and ML datasets**.

## Comparison Tables
### Object Storage Across Providers
| Provider | Service | Strength | Typical Fit |
|---|---|---|---|
| AWS | S3 | Most mature, extreme durability, deep AWS integration | Websites, media, data lakes, backups |
| Azure | Blob Storage | Enterprise and Microsoft integration | Enterprise documents, compliance, backup |
| Google Cloud | Cloud Storage (GCS) | Simplicity, performance, data-heavy workloads | Big data, ML data, cloud-native apps |

### Storage Tier Behavior
| Tier | Cost | Access Speed | Typical Use |
|---|---|---|---|
| Frequently accessed | Higher | Fast | Hot data, websites |
| Infrequent | Lower | Slower to retrieve | Backups, less-used data |
| Archive | Lowest | Slowest to retrieve | Long-term retention, compliance archives |

### Object Storage vs Traditional File Systems
| Aspect | Object Storage | Traditional File System |
|---|---|---|
| Access | API/HTTP | Mounted disk |
| Structure | Objects with metadata and IDs | Hierarchical files and folders |
| Scale | Nearly infinite | Limited by the disk/filesystem |
| Use | Unstructured data | General-purpose file operations |

## Key Takeaways and Summary
- Cloud storage is **decoupled from compute** — data persists independently.
- **Object storage** is the dominant model: accessed via APIs, scales almost infinitely, perfect for unstructured data.
- All three providers are **conceptually similar**, differing in integration, performance, and enterprise alignment.
- **Storage tiers and lifecycle policies** balance cost and performance.
- Object storage is **scalable, durable, cost-efficient**, and the foundation of modern cloud systems.

## Quick Revision Notes and Memory Aids
- Services: **S3 (AWS), Blob (Azure), Cloud Storage (GCP)**.
- Object = **Data + Metadata + Unique ID**.
- Access: **API/HTTP, not mounted**.
- Tiering: **Frequent → Infrequent → Archive** (price decreases, retrieval time increases).
- Analogy: **Massive digital warehouse**.

## Exam Tips and Common Pitfalls
- Do not confuse **object storage with block or file storage**.
- Object storage is **not mounted** — common exam distractor.
- S3 is **extremely durable**; don't describe it as "cheap-only" storage.
- Remember lifecycle policies are about **automation**, not manual moves.
- Azure Blob Storage ties tightly to **Microsoft enterprise compliance tooling**.

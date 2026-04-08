# Understanding IaaS, PaaS, and SaaS

## Core Idea
Cloud service models define how responsibilities are split between provider and customer.

## IaaS (Infrastructure as a Service)

### What You Get
- Virtual machines
- Storage
- Networking
- Load balancers
- Foundational compute infrastructure

### Who Manages What
- **Provider manages:** underlying hardware and virtualization.
- **Customer manages:** operating system, runtime, applications, configuration, security controls at OS/app level.

### Typical Use Cases
- Migrating legacy applications needing custom OS-level control
- Custom networking/security setups
- Lift-and-shift strategies

### Examples
- AWS EC2
- Azure Virtual Machines
- Google Compute Engine

### Analogy
Like renting an empty apartment: structure is provided, setup inside is your responsibility.

## PaaS (Platform as a Service)

### What You Get
- Managed platform for application development and deployment
- Runtime, middleware, and operational services included

### Who Manages What
- **Provider manages:** infrastructure, OS, runtime, patching, much of operations.
- **Customer manages:** application code and business data.

### Typical Use Cases
- Startups and product teams needing fast development cycles
- Teams wanting reduced infrastructure overhead

### Example
- AWS Elastic Beanstalk (representative managed platform model)

### Analogy
Like renting a furnished apartment: essentials are ready; you focus on living (building app logic).

## SaaS (Software as a Service)

### What You Get
- Complete software product delivered over the internet
- Minimal technical management by end customer

### Who Manages What
- **Provider manages:** application + platform + infrastructure.
- **Customer manages:** usage, user-level settings, and business process adoption.

### Typical Use Cases
- Email, CRM, collaboration, conferencing, file sharing

### Examples
- Gmail, Zoom, Office 365, Dropbox

### Analogy
Like staying in a hotel: all operations are managed; you consume the service.

## Why This Classification Matters
- Clarifies control vs convenience trade-offs.
- Helps in cost planning and team capability alignment.
- Sets expectations for security and operational responsibility.

## Exam-Focused Comparison Snapshot
- **IaaS:** maximum control, maximum management effort.
- **PaaS:** balanced control and speed.
- **SaaS:** minimum management, maximum convenience.

## Quick Revision
- Service model choice is a responsibility decision, not just a technical label.
- As you move IaaS -> PaaS -> SaaS, customer operational responsibility decreases.

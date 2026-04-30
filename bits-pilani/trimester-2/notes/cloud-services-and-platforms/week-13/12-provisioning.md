# Provisioning with Terraform

## Provisioning meaning
- Provisioning is creating and configuring infrastructure resources so workloads can run.
- Terraform provisioning should primarily mean declaring resources, not running lots of imperative scripts.
- Keep infrastructure lifecycle declarative where possible.

## Provisioners
- Terraform provisioners can run local or remote commands, but they are last-resort tools.
- They make runs less predictable and harder to repeat.
- Prefer cloud-init/user data, image baking, configuration management, or managed services.

## Exam guidance
- Use Terraform resources/modules for networks, compute, IAM, storage, and databases.
- Use provisioners only when no better provider-native option exists.
- If provisioning fails halfway, inspect state and plan before retrying or manual cleanup.

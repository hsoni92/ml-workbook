# Container Registry

## Registry role
- A registry stores container images and makes them available for deployment.
- Images are identified by repository name and tag or digest.
- Digest is immutable and safer for exact deployment reproducibility.

## Registry workflow
- Build image locally or in CI.
- Tag image with repo/version.
- Authenticate to registry.
- Push image; deployment platform pulls it.

## Exam distinctions
- Registry stores images; orchestrator runs containers.
- Public registry is open/shared; private registry requires auth.
- Use scanning and signing to reduce supply-chain risk.

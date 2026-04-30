# Pushing and Pulling Images

## Pull flow
- Pull downloads image layers from registry to local host/node.
- If layer already exists locally, it is reused.
- Kubernetes nodes pull images before starting pods unless cached.

## Push flow
- Build image, tag it with registry/repository:tag, authenticate, then push.
- Only missing layers are uploaded.
- CI pipelines normally push versioned images after tests pass.

## Exam handles
- Authentication failure means registry credentials/IAM issue.
- ImagePullBackOff in Kubernetes often means wrong image name, missing tag, or no pull permission.
- Use immutable tags/digests for production release traceability.

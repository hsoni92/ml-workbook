# Docker Internals Overview

## Image and layer model
- Docker images are built from layered filesystem changes.
- Layers are cached, reused, and identified by content.
- Smaller layers and clean Dockerfiles improve build speed and security.

## Runtime pieces
- Docker client sends commands to Docker daemon or compatible runtime stack.
- Container runtime creates isolated processes using kernel primitives.
- Networking, volumes, and logs are configured around that process.

## Practical exam points
- Image is read-only template; container is running writable instance layer.
- Bind mounts depend on host path; volumes are Docker-managed persistent storage.
- Container logs should go to stdout/stderr for platform collection.

# Docker Installation and Container Management

## Management basics
- Install Docker/compatible runtime, verify daemon, then run containers from images.
- Common operations: pull, run, ps, logs, exec, stop, rm.
- Image lifecycle and container lifecycle are separate.

## Useful commands
- docker run starts a container from an image.
- docker ps shows running containers; docker ps -a includes stopped ones.
- docker logs reads container output.
- docker exec opens a process inside a running container for debugging.

## Operational caution
- Do not treat manual container changes as durable configuration.
- Use Dockerfile and compose/orchestration manifests for repeatability.
- Clean unused images/containers carefully to avoid disk pressure.

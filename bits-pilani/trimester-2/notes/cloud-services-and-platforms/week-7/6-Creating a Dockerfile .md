# Creating a Dockerfile

## Dockerfile purpose
- Dockerfile is a recipe for building an image.
- Each instruction usually creates a layer.
- A good Dockerfile is reproducible, minimal, and explicit.

## Key instructions
- FROM chooses base image.
- RUN installs packages or executes build commands.
- COPY copies application files into image.
- EXPOSE documents intended port but does not publish it.
- CMD or ENTRYPOINT defines default process.

## Best practices
- Use small trusted base images.
- Copy dependency manifests before source code to improve cache use.
- Do not bake secrets into images; pass secrets through runtime secret mechanisms.

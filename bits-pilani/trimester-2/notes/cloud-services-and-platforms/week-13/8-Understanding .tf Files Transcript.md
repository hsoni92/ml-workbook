# Understanding .tf Files

## File role
- Terraform loads all .tf files in a directory as one module.
- File names are for humans; Terraform merges configuration logically.
- Common names: main.tf, variables.tf, outputs.tf, providers.tf, versions.tf.

## Common blocks
- terraform block sets required providers/backend settings.
- provider block configures provider plugin.
- resource block creates/manages infrastructure.
- variable block accepts input.
- output block exposes values.

## Exam notes
- Splitting files does not create modules by itself.
- Variables make config reusable across environments.
- Outputs are useful for passing values to users, modules, or pipelines.

# Terraform Syntax Basics

## HCL basics
- Terraform uses HashiCorp Configuration Language.
- Blocks have type, labels, and body.
- Arguments assign values such as name = "app".
- Expressions can reference variables, resources, locals, and functions.

## Common constructs
- var.name references input variable.
- resource_type.name.attribute references resource attributes.
- locals define reusable expressions.
- for_each/count create multiple instances carefully.

## Exam caution
- Syntax describes desired config; provider decides valid arguments.
- Implicit dependencies come from references.
- Use depends_on only when dependency is real but not visible through references.

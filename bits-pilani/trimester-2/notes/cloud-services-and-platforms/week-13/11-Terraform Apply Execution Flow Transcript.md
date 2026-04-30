# Terraform Apply Execution Flow

## Before apply
- Run init so providers/backend are ready.
- Run validate/fmt for basic correctness.
- Run plan to review proposed actions and detect destructive changes.

## During apply
- Terraform builds dependency graph.
- Creates, updates, or destroys resources in safe order where possible.
- Prompts for approval unless auto-approve is used.
- Writes new state after successful operations.

## Failure behavior
- Partial apply can leave some resources changed.
- Do not delete state to fix errors casually.
- Rerun plan after failure to see remaining drift/actions.

# CI/CD Tools Overview

## Tool categories
- Source hosting: GitHub, GitLab, Bitbucket.
- CI engines: GitHub Actions, Jenkins, GitLab CI, CodeBuild.
- CD/orchestration: CodePipeline, Argo CD, Spinnaker, Azure DevOps.

## AWS-native tools
- CodeCommit stores source, though GitHub is common.
- CodeBuild runs build/test jobs.
- CodeDeploy manages deployments.
- CodePipeline connects stages end to end.

## Choosing tools
- Prefer integration with existing repo, cloud platform, IAM, and team skills.
- Managed tools reduce maintenance; self-hosted tools offer control.
- Exam usually tests pipeline concept more than vendor trivia.

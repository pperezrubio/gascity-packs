# Harden: Prepare

You are starting a **harden** workflow. This workflow runs multi-pass bug hunting,
security auditing, a fix loop for findings, and a final verification pass.

Your job: read the project context, understand what was recently implemented, and
prepare the artifact root for downstream stages.

Write a brief context summary to `{{artifact_root}}/harden/context.md` including:
- Project name and description
- Recent changes (from `git log --oneline -20`)
- Languages and frameworks detected
- Known problem areas (from TODO/FIXME comments)

Record the artifact path on the workflow root bead.

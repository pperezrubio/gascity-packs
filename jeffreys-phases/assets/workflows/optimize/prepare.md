# Optimize: Prepare

You are starting an **optimize** workflow. This workflow profiles the codebase,
builds an opportunity matrix, implements optimizations (Score >= 2.0 only), and
proves behavior is unchanged.

Benchmark command: `{{benchmark_command}}`

Prepare the artifact root and capture the project's build/test commands for
downstream stages. Write a context summary to `{{artifact_root}}/optimize/context.md`.

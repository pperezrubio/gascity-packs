# Harden: Bug Hunt

Execute the **multi-pass bug hunting cycle** as defined in your agent methodology.

Work through the codebase systematically:

1. **Pass 1 — Surface**: Scan for obvious defects (null derefs, missing awaits, resource leaks, off-by-one errors, race conditions, error swallowing, logic inversions)
2. **Pass 2 — Deep**: Re-read with fresh eyes for edge cases, boundary conditions, error path completeness
3. **Pass 3 — Integration**: Check how findings interact, verify callers of buggy functions

Document every finding with file:line, severity, category, root cause, and reproduction steps.

Write the consolidated findings to `{{artifact_root}}/harden/bug-hunt-report.md`.

Do NOT fix bugs — document them. The fix step routes them to the implementation worker.

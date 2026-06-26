# Refactor: Clean

Read the audit at `{{artifact_root}}/refactor/audit-report.md`.

Work through findings in safest-first order:

1. **Remove dead code** — delete unused imports, functions, variables. Run tests after each deletion.
2. **De-slopify documentation** — manual line-by-line review. Replace emdashes, remove filler, cut hedging.
3. **Eliminate unnecessary abstractions** — collapse single-implementation interfaces, inline trivial wrappers.

For each change:
- Make a focused commit: `refactor: [what was cleaned]`
- Run tests — if any test breaks, REVERT immediately

Write a summary of changes to `{{artifact_root}}/refactor/clean-report.md`.

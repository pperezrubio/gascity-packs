# Harden: Fix Findings

Read the bug hunt report at `{{artifact_root}}/harden/bug-hunt-report.md` and the
security audit report at `{{artifact_root}}/harden/security-audit-report.md`.

Fix every finding in priority order:
1. **P0 findings first** — crashes, data loss, exploitable vulnerabilities
2. **P1 findings second** — incorrect behavior, likely exploitable issues
3. **P2 findings if time permits** — minor issues, hardening

For each fix:
- Fix the **root cause**, not the symptom
- Make a focused commit with message: `fix(harden): [finding title]`
- Run the test suite after each fix to ensure no regression

If a finding is a false positive, document why in the commit message and skip it.

Write a fix summary to `{{artifact_root}}/harden/fix-report.md` listing what was
fixed, what was triaged as false positive, and what was deferred.

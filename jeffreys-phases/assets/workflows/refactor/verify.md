# Refactor: Verify

Run the full test suite to verify no regressions from the refactoring.

1. Run all tests (unit, integration, e2e)
2. Run linters and type checkers
3. Verify no new warnings were introduced

Write the verification report to `{{artifact_root}}/refactor/verify-report.md`.

If tests fail, the refactoring introduced a regression. Document the failure for another iteration.

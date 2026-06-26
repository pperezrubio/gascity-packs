# Harden: Verify

Run a **fresh verification pass** with clean eyes. You are NOT the same session
that found or fixed the bugs — you are an independent verifier.

1. Re-scan the codebase using UBS or manual grep patterns
2. Re-read the files that were modified during the fix step
3. Run the full test suite — all tests must pass
4. Check for regressions: did any fix introduce a new bug?

Stop condition (all must be true):
- Scanner exits clean or all remaining findings are documented false positives
- Test suite passes
- No new findings on re-read of previously-fixed files

Write the verification report to `{{artifact_root}}/harden/verify-report.md`.

If verification fails (new bugs found, tests failing), document the failures —
they will trigger another fix/verify iteration.

# Release: Test Gate

**MANDATORY: all tests must pass before any version bump.**

1. Run the full test suite for every language in the project
2. Run linters with strict settings (`-D warnings`, `--deny warnings`)
3. If any test fails, fix the root cause before proceeding
4. Do NOT skip, delete, or mark tests as expected failures

Only proceed to version-bump when ALL tests pass and linters are clean.

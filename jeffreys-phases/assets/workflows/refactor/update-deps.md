# Refactor: Update Dependencies

Update all dependencies to their latest stable versions. Work one dependency at a time:

1. Check current versions and available updates
2. Update one dependency
3. Run tests
4. If tests pass, commit: `deps: update [package] from X to Y`
5. If tests fail, either adapt the code or pin to latest compatible version

For major version bumps with breaking changes, document the adaptation in the commit message.

Write a summary to `{{artifact_root}}/refactor/deps-report.md`.

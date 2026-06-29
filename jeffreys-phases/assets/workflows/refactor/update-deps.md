# Refactor: Update Dependencies

Input variable: `update_deps={{update_deps}}`.

If `update_deps` is not `true`, do not change dependency manifests. Write a
skip report to `{{artifact_root}}/refactor/deps-report.md` explaining that
dependency updates were intentionally skipped and listing the manifests that
were inspected.

If `update_deps=true`, continue with the update procedure below.

Update all dependencies to their latest stable versions. Work one dependency at a time:

1. Check current versions and available updates
2. Update one dependency
3. Run tests
4. If tests pass, prepare commit evidence: `deps: update [package] from X to Y`
5. If tests fail, either adapt the code or pin to latest compatible version

For major version bumps with breaking changes, document the adaptation in the commit message.

Write a summary to `{{artifact_root}}/refactor/deps-report.md`.

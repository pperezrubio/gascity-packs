# Release: Version Bump

Determine the new version (bump type: `{{bump_type}}`, target: `{{version}}`).

Update version in ALL manifests:
- `Cargo.toml` (Rust)
- `package.json` (Node)
- `pyproject.toml` / `__init__.py` (Python)
- `main.go` / `version.go` (Go)

Commit: `release: bump version to X.Y.Z`

Write the version change to `{{artifact_root}}/release/version.md`.

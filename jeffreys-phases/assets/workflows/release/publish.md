# Release: Publish

Input variable: `push={{push}}`.

If `push` is not `true`, do not create tags, push refs, or publish packages.
Instead, write a dry-run publish report to
`{{artifact_root}}/release/publish-report.md` with the exact commands that
would be run, the artifacts that are ready, and any remaining blockers.

If `push=true`, continue with the publish procedure below.

Create the GitHub release:

1. Tag the release: `git tag -a vX.Y.Z -m "Release X.Y.Z"`
2. Push the tag
3. Create GitHub release with `gh release create`
4. Upload binaries and checksums as release assets
5. Verify the release is visible and assets are downloadable

Write the result to `{{artifact_root}}/release/publish-report.md`.

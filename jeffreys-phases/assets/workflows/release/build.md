# Release: Build

Build cross-platform binaries:

1. Build for all target platforms (linux-amd64, darwin-arm64, windows-amd64)
2. Generate SHA256 checksums
3. Verify static linking where expected (`file binary | grep "statically linked"`)
4. Test the installer script works: `curl -fsSL install.sh | bash -s -- --verify`

Write the build report to `{{artifact_root}}/release/build.md`.

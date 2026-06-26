# Optimize: Implement

Read the opportunity matrix at `{{artifact_root}}/optimize/matrix.md`.

Implement ONLY optimizations with Score >= 2.0, one change per commit:

1. Apply the highest-score optimization first
2. Make a focused commit: `perf: [optimization description] (score X.X)`
3. Run tests to verify no regression
4. Repeat for the next qualified optimization

For each optimization, verify the isomorphism proof holds:
- Run `sha256sum -c {{artifact_root}}/optimize/golden_checksums.txt`
- If checksums differ, investigate whether the difference is expected (intentional output change) or a bug

If an optimization does NOT produce the expected speedup after implementation,
revert it and note the failure in the commit log.

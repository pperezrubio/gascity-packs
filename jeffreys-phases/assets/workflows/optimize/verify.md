# Optimize: Verify

Prove that behavior is unchanged after all optimizations.

1. Run `sha256sum -c {{artifact_root}}/optimize/golden_checksums.txt`
2. Re-run the benchmark: `{{benchmark_command}}`
3. Compare new metrics against baseline at `{{artifact_root}}/optimize/baseline.md`
4. Re-profile to confirm bottlenecks shifted (they always do after optimization)

Write the verification report to `{{artifact_root}}/optimize/verify-report.md`:

```
## Optimization Verification
- Golden checksums: PASS/FAIL
- Baseline: mean=Xms, p95=Yms
- After optimization: mean=X'ms, p95=Y'ms
- Improvement: Nx faster
- New bottlenecks: [list top 3 remaining]
```

If golden checksums FAIL, the optimization changed output behavior — this is a
regression. Document what changed and whether it's acceptable.

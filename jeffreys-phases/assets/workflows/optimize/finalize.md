# Optimize: Finalize

Compile the final optimization report.

Write to `{{artifact_root}}/optimize/final-report.md`:

```
## Optimization Report
- Baseline: mean=Xms, p95=Yms, throughput=Z ops/s
- After: mean=X'ms, p95=Y'ms, throughput=Z' ops/s
- Improvement: Nx overall
- Hotspots profiled: N
- Opportunities scored: M
- Qualified (Score >= 2.0): K
- Implemented: J
- Golden checksums: verified/failed
```

# Optimize: Baseline

Establish the performance baseline using the benchmark command: `{{benchmark_command}}`

1. Run the benchmark with warmup and multiple iterations
2. Capture: mean, p50, p95, p99 latency, throughput
3. Capture golden outputs: run the command, save stdout, compute sha256sum
4. Record memory peak if measurable

Write the baseline to `{{artifact_root}}/optimize/baseline.md` with all metrics.
Write golden checksums to `{{artifact_root}}/optimize/golden_checksums.txt`.

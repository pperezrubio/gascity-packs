# Optimize: Analyze

Profile the codebase and build the opportunity matrix.

1. Run the appropriate profiler (flamegraph, cProfile, py-spy, --prof, perf)
2. Identify the top 5-10 hotspots by cumulative time
3. Score each hotspot: Impact (1-5) x Confidence (1-5) / Effort (1-5)
4. Filter: only Score >= 2.0 qualifies for implementation

Write the opportunity matrix to `{{artifact_root}}/optimize/matrix.md`:

```
| # | Hotspot | Location | Impact | Conf | Effort | Score | Pattern |
|---|---------|----------|:------:|:----:|:------:|:-----:|---------|
| 1 | ... | func:line | 5 | 4 | 2 | 10.0 | Avoid repeated alloc |
```

For each qualified finding, include the isomorphism proof template:
- Ordering preserved: yes/no + why
- Tie-breaking unchanged: yes/no + why
- Floating-point: identical/N/A
- RNG seeds: unchanged/N/A

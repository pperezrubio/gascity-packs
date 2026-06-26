# Harden: Finalize

Compile the final hardening report combining all stage outputs.

Write to `{{artifact_root}}/harden/final-report.md`:

```
## Hardening Report

### Bug Hunt
- Findings: X total (P0: a, P1: b, P2: c)
- False positives: Y
- Converged: yes/no

### Security Audit
- Findings: X total (P0: a, P1: b, P2: c)
- Attack surface: N entry points
- Overall risk: critical/elevated/moderate/low

### Fixes Applied
- P0 fixed: N
- P1 fixed: M
- P2 fixed: K
- False positives triaged: J
- Deferred: L (with rationale)

### Verification
- Scanner: clean/findings
- Tests: passing/failing
- Regressions: none/N found
- Final state: hardened/needs-another-pass
```

Record the final report path on the workflow root bead.

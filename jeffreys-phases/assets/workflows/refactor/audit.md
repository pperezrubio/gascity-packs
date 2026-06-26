# Refactor: Audit

Perform a full codebase audit. Detect:

1. **Dead code** — unused functions, unreachable branches, stale TODOs, placeholder/stub/mock code
2. **AI slop** — emdash overuse, "here's why" constructions, hedging, filler transitions, over-commented code
3. **Unnecessary abstractions** — single-implementation interfaces, trivial wrappers, unused factory patterns
4. **Dependency status** — outdated packages, known vulnerabilities

Write the audit findings to `{{artifact_root}}/refactor/audit-report.md` organized by category.

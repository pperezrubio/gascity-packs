# Harden: Security Audit

Execute the **security audit** as defined in your agent methodology.

Map the attack surface first, then hunt for:
- Injection vectors (SQL, command, XSS, template)
- Auth and authz bypasses (missing auth, IDOR, privilege escalation, CSRF)
- Secrets exposure (hardcoded, in logs, in URLs, in error messages)
- Deserialization vulnerabilities
- SSRF and path traversal
- SaaS-specific: payment bypass, webhook integrity, entitlement staleness

Apply the five security axioms. Trace attack paths from entry point to dangerous sink.

Write the consolidated findings to `{{artifact_root}}/harden/security-audit-report.md`.

Do NOT fix vulnerabilities — document them. The fix step routes them to the implementation worker.

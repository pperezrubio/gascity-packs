# Jeffrey's Phases Pack

Post-implementation SDLC phase agents for Gas City, powered by Dicklesworthstone's
[jeffreys-skills](https://github.com/Dicklesworthstone/jeffreys-skills) methodology.

## What It Provides

Seven specialized agents and five workflow formulas covering the full
post-greenfield software lifecycle:

| Phase | Agent | Skills Embedded |
|-------|-------|-----------------|
| **Bug hunting** | `phases.bug-hunter` | multi-pass-bug-hunting, ubs, mock-code-finder, deadlock-finder-and-fixer |
| **Security audit** | `phases.security-auditor` | security-audit-for-saas (130+ patterns), testing-fuzzing |
| **Performance optimization** | `phases.performance-optimizer` | extreme-software-optimization (profile → matrix → prove) |
| **Code refactoring** | `phases.refactorer` | de-slopify, mock-code-finder, library-updater, codebase archaeology/audit/report |
| **Test engineering** | `phases.test-engineer` | conformance harnesses, golden artifacts, metamorphic, mock-free E2E, fuzzing |
| **Release engineering** | `phases.release-engineer` | release-preparations, installer-workmanship, changelog |
| **Documentation** | `phases.doc-writer` | readme-writing, de-slopify, changelog generation |

| Formula | Steps | Description |
|---------|-------|-------------|
| `harden` | hunt → security → fix → verify | Multi-pass bug hunting + security audit + fix loop |
| `optimize` | baseline → analyze → implement → verify | Profile-driven optimization with isomorphism proofs |
| `refactor` | audit → clean → update-deps → verify | Code quality remediation without behavior changes |
| `release` | test-gate → version → changelog → build → publish | Comprehensive release preparation |
| `document` | readme → api-docs → changelog | Technical documentation generation |

## Design Principles

1. **Fresh context per phase** — The agent that finds bugs is never the same
   session that fixes them (Factory.ai principle)
2. **Validation before implementation** — Audit findings documented before fixes
3. **Tool restrictions per agent** — Hunters/auditors are read-only; only
   refactorers and test-engineers have write access
4. **Skills as prompt templates** — Methodology embedded in prompt text, not
   runtime dependencies (cass pack pattern)

## Prerequisites

Import the base Gas City pack first — this pack imports `gascity` as `gc` and
`ee` for memory/claim-gate prompt fragments, then extends them with
phase-specific agents and formulas.

## Quick Start

1. **Import the pack** at city scope:

   ```sh
   gc import add https://github.com/gastownhall/gascity-packs.git//jeffreys-phases
   ```

2. **Import the rig roles** in `city.toml`:

   ```toml
   [[rigs]]
   name = "your-project"

   [rigs.imports.gc]
   source = "https://github.com/gastownhall/gascity-packs.git//gascity/roles"

   [rigs.imports.phases]
   source = "https://github.com/gastownhall/gascity-packs.git//jeffreys-phases"
   ```

   Run `gc import install` after editing.

3. **Run a phase:**

   ```sh
   # Harden: bug hunt + security audit + fix loop
   gc bd create "Harden the codebase before release"
   gc sling gc.run-operator <bead-id> --on harden \
     --var artifact_root=plans/harden/build

   # Optimize: profile-driven performance optimization
   gc sling gc.run-operator <bead-id> --on optimize \
     --var artifact_root=plans/optimize/build \
     --var benchmark_command='cargo test --release -- --test-stress'

   # Refactor: clean code, update deps
   gc sling gc.run-operator <bead-id> --on refactor \
     --var artifact_root=plans/refactor/build \
     --var update_deps=true

   # Release: test gate + version + build + publish
   gc sling gc.run-operator <bead-id> --on release \
     --var artifact_root=plans/v1.0/build \
     --var bump_type=minor \
     --var push=true

   # Document: README + API docs + changelog
   gc sling gc.run-operator <bead-id> --on document \
     --var artifact_root=plans/docs/build
   ```

## Phase Workflow

```
build-basic (existing)
  requirements → plan → implement → review → publish
                    │
                    ▼
              POST-GREENFIELD
  ┌─────────────────────────────────────────────────────┐
  │ harden: hunt → security → fix → verify              │
  │ optimize: baseline → analyze → implement → prove    │
  │ refactor: audit → clean → update-deps → verify      │
  │ release: test-gate → version → changelog → publish  │
  │ document: readme → api-docs → changelog             │
  └─────────────────────────────────────────────────────┘
```

## Customization

All step prompts are Markdown files at `assets/workflows/<formula>/<step>.md`.
Shadow them in a higher-priority pack layer to customize behavior without
changing the formula graph.

| Variable | Default | What it changes |
|----------|---------|-----------------|
| `artifact_root` | required | Directory where stage artifacts are written |
| `max_iterations` | `5` | Maximum fix/re-verify attempts |
| `benchmark_command` | required (optimize) | Command to benchmark for baselines |
| `update_deps` | `true` (refactor) | Whether to update dependencies |
| `bump_type` | `patch` (release) | Version bump type: major, minor, patch |
| `push` | `false` (release) | Whether to push after release |
| `include_api_docs` | `true` (document) | Whether to generate API docs |

## Agent Tool Access

| Agent | Tools | Rationale |
|-------|-------|-----------|
| bug-hunter | Read, Grep, Glob, Bash | Finding bugs, not fixing them |
| security-auditor | Read, Grep, Glob, Bash | Pure audit, no changes |
| performance-optimizer | Read, Grep, Glob, Bash | Profiling and analysis only |
| refactorer | Read, Write, Edit, Grep, Glob, Bash | Makes code changes directly |
| test-engineer | Read, Write, Edit, Grep, Glob, Bash | Writes test files |
| release-engineer | Read, Grep, Glob, Bash | Mechanical versioning + builds |
| doc-writer | Read, Write, Grep, Glob, Bash | Documentation only |

## What's Vendored

- 22 skill directories under `skills/` (self-contained — the full original
  SKILL.md + references/ + assets/ + subagents/ for each skill)
- `vendor/jeffreys-skills/upstream.toml` — provenance tracking (source URL,
  pinned commit, license)

Each agent prompt references `skills/<name>/SKILL.md` and instructs the agent
to read the skill in full before starting work. The skills are the authoritative
methodology source; the agent prompt is a thin adapter that adds Gas City
integration (tool restrictions, output paths, fix-vs-find separation).

Skills included:
multi-pass-bug-hunting, ubs, mock-code-finder, security-audit-for-saas,
extreme-software-optimization, de-slopify, library-updater,
codebase-pattern-extraction, codebase-archaeology, codebase-audit,
codebase-report, deadlock-finder-and-fixer, testing-fuzzing,
testing-conformance-harnesses,
testing-golden-artifacts, testing-real-service-e2e-no-mocks,
testing-metamorphic, e2e-testing-for-webapps, release-preparations,
installer-workmanship, changelog-md-workmanship, readme-writing

## Compatibility

This pack imports `gascity` as `gc` and uses the `gc-role-worker` template
fragment from the base pack. It does not override any `build-basic` stages —
the phase formulas are standalone workflows that run independently or after
`build-basic` completes.

# Jeffrey's Workflow Pack

Pre-implementation and during-implementation workflow agents for Gas City, powered by
Dicklesworthstone's [jeffreys-skills](https://github.com/Dicklesworthstone/jeffreys-skills) methodology.

Covers the full **planning → bead decomposition → swarm coordination → safety → commit discipline** lifecycle that precedes and accompanies code writing.

## What It Provides

Six specialized agents and three workflow formulas covering the pre-implementation
and during-implementation phases:

| Agent | Role | Skills Embedded |
|-------|------|-----------------|
| **planner** | Markdown-first planning (85%+ time on planning) | planning-workflow, agent-fungibility-philosophy |
| **bead-architect** | Plan → hierarchical beads with dependencies | beads-workflow, beads-br, beads-bv |
| **swarm-coordinator** | Multi-agent coordination on main branch | agent-mail, ntm, ru-multi-repo-workflow |
| **safety-officer** | Destructive command guards, two-person rule | dcg, slb, rch |
| **commit-craftsman** | Tiered commit body system, evidence-based closure | git-commit-craftsman |
| **formal-verifier** | Lean/Rust proof feedback for critical invariants | lean-formal-feedback-loop |

| Formula | Steps | Description |
|---------|-------|-------------|
| `plan` | understand → plan → decompose → safety-review → finalize | Full planning workflow producing bead DAG |
| `swarm` | prepare → dispatch → monitor → verify → finalize | Multi-agent execution with file reservations |
| `commit` | classify → regression-test → dcg-check → compose → commit | Safe commit with tiered body + bead closure |

## Design Principles

1. **Planning before code** — 85%+ of time on planning, decomposing, and risk analysis
2. **Hierarchical beads** — Epics with dot-notation sub-tasks, rich labels, dependencies
3. **Gas City claim authority** — `gc hook --claim --json` is the only live work
   discovery path; `bv` ranks work and Agent Mail reserves files after claim.
4. **Safety is layered** — DCG blocks commands, SLB enforces two-person rule, RCH verifies builds
5. **Commits are proof artifacts** — Tiered body depth, root cause analysis, evidence-based closure
6. **Skills as prompt templates** — Methodology embedded in prompt text (cass pack pattern)

## Relationship to jeffreys-phases

This pack handles **pre-implementation** (planning, beads, coordination, safety, commits).
The companion `jeffreys-phases` pack handles **post-implementation** (bug hunting, security
audits, optimization, testing, release).

```
jeffreys-workflow:  [PLAN] → [BEADS] → [SWARM DISPATCH] → [COMMIT]
                                                            ↓
jeffreys-phases:                                        [CODE WRITTEN]
                                                            ↓
                     [BUG HUNT] → [SECURITY] → [OPTIMIZE] → [TEST] → [RELEASE]
```

## Skills Included (17)

### Priority 1 — Core Flywheel
- **planning-workflow** — Markdown planning methodology with exact prompts (85%+ time on planning)
- **beads-workflow** — Converting plans → beads with dependencies and exact prompts
- **agent-mail** — MCP coordination: file reservations, identities, threaded messaging
- **agent-fungibility-philosophy** — Why homogeneous agents outperform specialized roles

### Priority 2 — Tool Skills
- **beads-br** — beads_rust (`br`) CLI usage patterns
- **beads-bv** — Beads Viewer (`bv`): graph triage, PageRank, critical path, cycles
- **dcg** — Destructive Command Guard: blocks dangerous commands, SIMD-accelerated
- **ntm** — Named Tmux Manager: multi-agent pane orchestration, visual dashboard
- **rch** — Remote Compilation Helper: distributed build verification
- **slb** — Simultaneous Launch Button: two-person rule for destructive operations
- **caam** — Coding Agent Account Manager: profile rotation, health scoring
- **ru-multi-repo-workflow** — Repo Updater: multi-repo sync with AI-assisted review

### Priority 3 — Strategy and Assurance
- **idea-wizard** — Generate and compare implementation approaches before committing to a plan
- **dueling-idea-wizards** — Multi-agent idea review and convergence
- **reality-check-for-project** — Check plan/bead coverage against project ambition
- **lean-formal-feedback-loop** — Lean proof feedback loops for critical invariants

### Priority 4 — Preserved (Removed from Upstream)
- **git-commit-craftsman** — Commit methodology: structure, evidence, bead linking

## Prerequisites

Import the base Gas City pack first. This pack imports `gascity` as `gc` and
`ee` for memory/claim-gate prompt fragments, then extends them with workflow
agents and formulas.

## Quick Start

1. **Import the pack** at city scope:

   ```sh
   gc import add https://github.com/gastownhall/gascity-packs.git//jeffreys-workflow
   ```

2. **Run the plan formula** before starting implementation:

   ```toml
   [[rigs]]
   name = "your-project"

   [rigs.imports.gc]
   source = "https://github.com/gastownhall/gascity-packs.git//gascity/roles"

   [rigs.imports.workflow]
   source = "https://github.com/gastownhall/gascity-packs.git//jeffreys-workflow"
   ```

3. **Use the formulas**:

   ```sh
   gc formula run plan --var problem_statement="Add user authentication" --var codebase_path=.
   gc formula run swarm --var bead_filter="--status=open" --var max_agents=2
   gc formula run commit --var bead_id=ci-43a --var change_description="Fix PATH for cargo"
   ```

## Key Patterns from Jeffrey's Swarm

### `tracker:` Commit Convention

Agents coordinate through `tracker:` commits in git history:

```
tracker: close ci-43a (cass_prefetch tests, committed abc123def) (IndigoReviewer)
tracker: file ci-44b (parser edge case in null handling) (AzureBirch)
tracker: block ci-45c on RCH sync
tracker: release ci-46d with E2E implementation plan
```

### Hierarchical Bead IDs

```
ci-43a: [epic] Add user authentication
  ci-43a.1: User registration endpoint
  ci-43a.2: Login + JWT token generation
  ci-43a.3: Password reset flow
  ci-43a.4: Session management
```

### Bead Labels That Drive Agent Behavior

| Label | What It Tells Agents |
|-------|---------------------|
| `test-coverage-required` | MUST write tests before closing |
| `e2e-required` | End-to-end test needed |
| `swarm-scale` | Multi-agent coordination needed |
| `verification-required` | Evidence/proof required for closure |

### The 4-Tier Commit Body System

| Tier | Body Length | When |
|------|-----------|------|
| 1 | 1,600-3,200 chars | Complex non-obvious fixes |
| 2 | 400-1,600 chars | Moderate fixes with evidence |
| 3 | 100-400 chars | Simple fixes with bead ref |
| 4 | Empty | Trivial (clippy, deps) |

See the local Gas City methodology notes for full EE and commit-discipline
details.

## Vendored From

- [Dicklesworthstone/jeffreys-skills](https://github.com/Dicklesworthstone/jeffreys-skills) @ afbe742
- `git-commit-craftsman` preserved from upstream removal (2026-06-26)

# Gas City Commit Conventions Reference

> All agents MUST follow these conventions. Based on analysis of Jeffrey Emanuel's
> commit methodology across 18 repos (§13-15 of the Integration Architecture note).

## Commit Type Quick Reference

| Type | When | Subject Format | Key Rule |
|------|------|---------------|----------|
| `fix` | Bug fix | `fix($scope): $desc [ci-$bead]` | Root cause + "I did NOT do X" + regression test |
| `test` | Test addition | `test($scope): $verb $obj [ci-$bead]` | Standalone, never coupled with fix. Evidence required. |
| `perf` | Performance | `perf($scope): $op — $before -> $after` | One lever per commit. A/B measurements. |
| `feat` | Feature | `feat($scope): $desc` or `(Inc$N, ci-$bead.$sub)` | Bead for planned, no bead for organic |
| `refactor` | Refactoring | `refactor($scope): $desc` | MUST prove "no behavior change" |
| `tracker` | Coordination | `tracker: $action ci-$bead ($evidence) ($reviewer)` | Reviewer always named |
| `chore(beads)` | Tracker sync | `chore(beads): $action ci-$bead` | Separate from source code |
| `docs` | Documentation | `docs($scope): $desc` | ADR refs with §numbers |
| `security` | Security fix | `security($scope): $desc` | Prove the threat model |
| `fuzz` | Fuzz fix | `fix(fuzz): $desc` | State "harness bug" vs "impl bug" |

## Mandatory Rules (All Commit Types)

1. **Bead reference in subject** for planned work: `[ci-$bead_id]`
2. **Evidence in body**: RCH proof, test counts, or honest block disclosure
3. **Co-Authored-By** trailer for agent-assisted commits
4. **Separate tracker metadata from source** — two commits, not one
5. **One concern per commit** — don't mix refactor + fix + test

## Fix Commit Tiers (by complexity, NOT diff size)

| Tier | Body Length | When |
|------|-----------|------|
| 1 | 1,600-3,200 chars, 6-9 sections | Complex (concurrency, security, architecture) |
| 2 | 400-1,600 chars, 2-4 sections | Moderate with verification |
| 3 | 100-400 chars, 1 section | Simple with bead ref |
| 4 | Empty | Trivial (clippy, deps) |

## Test Commit Evidence Types

1. `RCH proof: cargo test --test $name => N passed, 0 failed`
2. `Blocked by unrelated $error in $file — NOT this test`
3. `Verified green via local build: N passed, 0 failed`
4. `Correct-by-construction; RCH-proof owed`

## Refactor Proof Patterns

- "byte-identical" (strongest)
- "semantics preserved"
- "existing assertions still pass"
- "behavior unchanged"

## Tracker Coordination Patterns

- `tracker: close ci-$bead ($evidence, committed $hash) ($reviewer)`
- `tracker: file ci-$bead ($description) ($agent)`
- `tracker: block ci-$bead on $blocker`
- `tracker: release ci-$bead with $plan`

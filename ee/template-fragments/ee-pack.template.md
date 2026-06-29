{{ define "ee-pack" }}
## Eidetic Engine — Context Memory

Before starting work on a bead or unfamiliar task, fetch a context pack from
`ee` (Eidetic Engine). The pack assembles relevant memories, decisions, rules,
and session evidence into a compact prompt fragment.

```bash
ee pack "<task description>" --workspace . --max-tokens 2000 --json \
  | python3 /usr/local/bin/agent_consume_pack.py --from-stdin
```

The output is a ready-to-prepend context fragment. Use it as background
knowledge — it may contain prior decisions, debugging history, procedural
rules, or anti-patterns discovered by past agent sessions.

If `ee pack` reports degraded or returns no memories, proceed without the
memory context only — memories accumulate as sessions run and `ee` indexes
them. Do not treat a degraded memory lookup as a failed bead.

### Claim and Evidence Gates

Memory is advisory. Claim and evidence gates are not advisory.

Gas City remains the source of truth for live work assignment:

```bash
gc hook --claim --json
```

When an EE swarm gate is part of the workflow, run the gate before dispatching
or continuing risky work:

```bash
ee swarm brief --workspace . --json
ee swarm work-packet --workspace . --claim-gate --candidate "$GC_BEAD_ID" --json
```

The gate result must be interpreted conservatively:

- `safeToClaim=true` and an allow/pass `verdict` permit the candidate to move
  forward through the normal Gas City claim path.
- `safeToClaim=false`, a block/deny `verdict`, missing candidate evidence, or a
  degraded claim-gate subsystem blocks the claim. Mark the bead blocked or ask
  the coordinator; do not bypass the gate with manual `br`/`bd` selection.
- `claimCommandAction` is guidance for the coordinator; it never replaces
  `gc hook --claim --json` for workers.

Persist gate artifacts under `.hive/wiki/reports/<bead-id>/` or the bead's
declared artifact directory so later reviewers can reconstruct the decision.

### Agent Mail Snapshot Bridge

If Agent Mail is part of the swarm, include reservation and inbox evidence in
the packet before a risky claim or handoff:

```bash
ee swarm work-packet --workspace . \
  --claim-gate \
  --candidate "$GC_BEAD_ID" \
  --include-agent-mail \
  --json
```

Use Agent Mail for coordination and file reservations after Gas City has
claimed or routed work; do not use mail threads as an alternate claim source.

### Storing findings

When you discover something worth remembering (a bug root cause, a design
decision, a useful pattern, a trauma from a failed approach), store it:

```bash
ee remember "<concise finding>" --level <level> --kind <kind> --json
```

Levels: `episodic` (session event), `semantic` (fact/knowledge), `procedural` (rule/how-to).
Kinds: `decision`, `rule`, `trauma`, `pattern`, `evidence`, `note`.

### Checking memory health

```bash
ee status --json
```

If status reports degraded capabilities, `ee search` falls back to lexical-only
mode. This is expected on fresh workspaces with no accumulated memory.

For commands with meaningful risk, ask EE for a preflight policy decision:

```bash
ee preflight check --cmd "<shell-command>" --json
```

For long-running swarms, capture environment evidence:

```bash
ee diag environment-attestation --workspace . --json
```

### What NOT to do

- Do not run `ee daemon` or `ee serve` — Gas City uses ee in CLI-only mode.
- Do not run `ee curate --auto` or `ee consolidate` — maintenance jobs run
  out-of-band, not during agent sessions.
- Do not run `ee graph --rebuild` — the memory graph is derived and rebuilt
  automatically.
- Do not proceed past a degraded claim gate. Only degraded optional memory
  lookup may be ignored.
{{ end }}

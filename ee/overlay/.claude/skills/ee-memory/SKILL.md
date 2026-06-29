# /ee-memory — Eidetic Engine context memory

Use `ee` (Eidetic Engine) to fetch context packs, store findings, and search
across accumulated agent memory.

## Before starting work

Fetch a context pack for your current task:

```bash
ee pack "<task description>" --workspace . --max-tokens 2000 --json \
  | python3 /usr/local/bin/agent_consume_pack.py --from-stdin
```

The pack contains relevant memories, decisions, rules, and evidence from past
sessions. Use it as background context.

If this optional memory lookup is degraded or empty, continue without memory
context. Do not treat optional memory degradation as a failed task.

## Claim and evidence gates

When EE is being used to authorize swarm work, it is no longer optional memory.
Run the claim gate before dispatching or continuing risky work:

```bash
ee swarm brief --workspace . --json
ee swarm work-packet --workspace . --claim-gate --candidate "$GC_BEAD_ID" --json
```

Interpret results conservatively:

- `safeToClaim=true` with an allow/pass `verdict` permits normal Gas City claim
  flow.
- `safeToClaim=false`, block/deny verdicts, missing candidate evidence, or a
  degraded claim-gate subsystem blocks the claim.
- `claimCommandAction` informs the coordinator; workers still claim through
  `gc hook --claim --json`.

Persist claim-gate artifacts under `.hive/wiki/reports/<bead-id>/` or the
bead's declared artifact directory.

If Agent Mail is part of the run, include the reservation/inbox bridge:

```bash
ee swarm work-packet --workspace . \
  --claim-gate \
  --candidate "$GC_BEAD_ID" \
  --include-agent-mail \
  --json
```

## Storing a finding

```bash
ee remember "<concise finding>" --level procedural --kind rule --json
```

Levels: `episodic`, `semantic`, `procedural`.
Kinds: `decision`, `rule`, `trauma`, `pattern`, `evidence`, `note`.

## Searching memory

```bash
ee search "<query>" --workspace . --json --limit 10
```

## Explaining a result

```bash
ee why <memory-id> --workspace . --json
```

## Trauma-guard (before destructive commands)

```bash
ee preflight check --cmd "<shell-command>" --json
```

Exit code 7 means the command was denied by policy. Do not retry with a
different spelling — ask for human authorization.

## Health

```bash
ee status --json
```

For long-running swarms, capture environment evidence:

```bash
ee diag environment-attestation --workspace . --json
```

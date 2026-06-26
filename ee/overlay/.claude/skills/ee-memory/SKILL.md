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

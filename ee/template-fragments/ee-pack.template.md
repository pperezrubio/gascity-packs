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

If `ee` reports degraded or returns no memories, proceed without — memories
accumulate as sessions run and `ee` indexes them.

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

### What NOT to do

- Do not run `ee daemon` or `ee serve` — Gas City uses ee in CLI-only mode.
- Do not run `ee curate --auto` or `ee consolidate` — maintenance jobs run
  out-of-band, not during agent sessions.
- Do not run `ee graph --rebuild` — the memory graph is derived and rebuilt
  automatically.
{{ end }}

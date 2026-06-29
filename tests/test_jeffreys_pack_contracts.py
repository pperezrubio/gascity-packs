from __future__ import annotations

import tomllib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = REPO_ROOT / "jeffreys-workflow"
PHASES = REPO_ROOT / "jeffreys-phases"
EE = REPO_ROOT / "ee"


def load_toml(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def test_jeffreys_packs_import_gascity_and_ee() -> None:
    for pack_dir in (WORKFLOW, PHASES):
        data = load_toml(pack_dir / "pack.toml")
        imports = data.get("imports", {})

        assert imports["gc"]["source"] == "../gascity"
        assert imports["ee"]["source"] == "../ee"


def test_role_prompts_include_gascity_claim_and_ee_context_templates() -> None:
    prompts = list((WORKFLOW / "agents").glob("*/prompt.template.md"))
    prompts.extend((PHASES / "agents").glob("*/prompt.template.md"))
    assert prompts

    for prompt in prompts:
        text = prompt.read_text(encoding="utf-8")
        assert '{{ template "gc-role-worker" . }}' in text, prompt
        assert '{{ template "ee-pack" . }}' in text, prompt


def test_swarm_formula_uses_gascity_claim_authority_and_mcp_agent_mail() -> None:
    text = (WORKFLOW / "formulas" / "swarm.formula.toml").read_text(encoding="utf-8")
    data = load_toml(WORKFLOW / "formulas" / "swarm.formula.toml")

    assert data["vars"]["max_agents"]["default"] == "2"
    assert "gc hook --claim --json" in text
    assert "macro_start_session" in text
    assert "file_reservation_paths" in text
    assert "release_file_reservations" in text
    assert "Claims bead via br claim" not in text
    assert "agent-mail reserve" not in text


def test_commit_formula_is_review_packet_not_direct_commit() -> None:
    formula = (WORKFLOW / "formulas" / "commit.formula.toml").read_text(encoding="utf-8")
    prompt = (WORKFLOW / "agents" / "commit-craftsman" / "prompt.template.md").read_text(
        encoding="utf-8"
    )

    assert "Prepare commit and close packet" in formula
    assert "Do not make the commit from the" in formula
    assert "Make commits (you REVIEW and ADVISE" in prompt


def test_ee_template_separates_optional_memory_from_claim_gate() -> None:
    text = (EE / "template-fragments" / "ee-pack.template.md").read_text(encoding="utf-8")

    assert "If `ee pack` reports degraded" in text
    assert "safeToClaim" in text
    assert "claimCommandAction" in text
    assert "Do not proceed past a degraded claim gate" in text
    assert "gc hook --claim --json" in text
    assert "--include-agent-mail" in text


def test_phase_formulas_do_not_leave_downstream_optional_dependency_holes() -> None:
    for formula in ("document", "refactor", "release"):
        data = load_toml(PHASES / "formulas" / f"{formula}.formula.toml")
        conditioned_steps = [
            step["id"]
            for step in data["steps"]
            if isinstance(step, dict) and "condition" in step
        ]
        assert conditioned_steps == []


def test_harden_fix_loop_has_consolidated_findings_artifact() -> None:
    formula = (PHASES / "formulas" / "harden.formula.toml").read_text(encoding="utf-8")
    security = (PHASES / "assets" / "workflows" / "harden" / "security.md").read_text(
        encoding="utf-8"
    )
    fix = (PHASES / "assets" / "workflows" / "harden" / "fix.md").read_text(
        encoding="utf-8"
    )

    assert '{{artifact_root}}/harden/findings.md' in formula
    assert "do not leave it\nmissing" in security
    assert "Read the consolidated findings file" in fix


def test_adapter_prompts_do_not_instruct_broad_destructive_git_reverts() -> None:
    prompts = list((WORKFLOW / "agents").glob("*/prompt.template.md"))
    prompts.extend((PHASES / "agents").glob("*/prompt.template.md"))

    for prompt in prompts:
        text = prompt.read_text(encoding="utf-8")
        assert "git checkout -- ." not in text, prompt

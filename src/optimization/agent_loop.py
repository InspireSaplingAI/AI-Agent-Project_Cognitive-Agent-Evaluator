"""Session 4: Orchestrator wiring Planner (bandit) + Executor (runner) + Critic (analyst) + Human Gate.

This module should only orchestrate calls to existing Session 2/3/4 functions —
do not reimplement experiment execution or statistics here.
"""

from typing import Any


# TODO(Session 4)
# - Generate variants (prompt_optimizer.generate_prompt_variants).
# - Loop num_rounds times: select a variant (bandit_optimizer), run it
#   (experiments.runner.execute_experiment / agents.dialogue_runner), score it
#   (analysis.metrics / analysis.stats), analyze it (agents.analyst_agent),
#   then update the bandit's reward for that variant.
# - After the loop, ask a human to approve the best variant before it is
#   declared the rollout winner (agents.human_gate).


def run_self_optimizing_loop(
    base_prompt_style: str, num_rounds: int, epsilon: float = 0.2, auto_approve: bool = False
) -> dict[str, Any]:
    """Run the Planner-Executor-Critic loop and return round-by-round history plus the best variant."""
    raise NotImplementedError("TODO: implement run_self_optimizing_loop")


def finalize_rollout_decision(
    variant_stats: dict[str, Any], best_variant: str, auto_approve: bool = False
) -> dict[str, Any]:
    """Request human approval for the best variant and return the final rollout decision."""
    raise NotImplementedError("TODO: implement finalize_rollout_decision")

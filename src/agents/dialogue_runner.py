"""Session 2: Controlled multi-turn or single-turn execution loop."""

from typing import Any


# TODO(Session 2)
# - Implement one trial execution from stimulus to response.
# - Support batch execution hooks and progress tracking.
# - Log trial-level failures without stopping entire run.


def run_single_trial(stimulus: dict[str, Any], model_name: str, generation_config: dict[str, Any]) -> dict[str, Any]:
    """Run one experiment trial and return structured output."""
    raise NotImplementedError("TODO: implement run_single_trial")


def run_trial_batch(stimuli: list[dict[str, Any]], model_name: str, generation_config: dict[str, Any]) -> list[dict[str, Any]]:
    """Run all trials and return collected outputs."""
    raise NotImplementedError("TODO: implement run_trial_batch")


def summarize_run_failures(outputs: list[dict[str, Any]]) -> dict[str, int]:
    """Summarize failed vs successful trial counts."""
    raise NotImplementedError("TODO: implement summarize_run_failures")

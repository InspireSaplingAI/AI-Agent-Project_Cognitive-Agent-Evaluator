"""Session 4: A/B test baseline vs optimized prompt strategy."""

from typing import Any


# TODO(Session 4)
# - Run controlled comparison between baseline and candidate prompts.
# - Compute delta metrics and uncertainty.
# - Output decision recommendation with caveats.


def run_ab_comparison(baseline_summary: dict[str, Any], candidate_summary: dict[str, Any]) -> dict[str, Any]:
    """Run A/B comparison on two evaluation summaries."""
    raise NotImplementedError("TODO: implement run_ab_comparison")


def compute_ab_delta_metrics(baseline_summary: dict[str, Any], candidate_summary: dict[str, Any]) -> dict[str, float]:
    """Compute absolute and relative deltas."""
    raise NotImplementedError("TODO: implement compute_ab_delta_metrics")


def recommend_rollout(ab_result: dict[str, Any], minimum_effect: float) -> dict[str, Any]:
    """Return recommendation and rationale for rollout decision."""
    raise NotImplementedError("TODO: implement recommend_rollout")

"""Session 3: Priming effect metrics."""

from typing import Any


# TODO(Session 3)
# - Compute priming rate by condition.
# - Compute effect size between prime-aligned and control outputs.
# - Add helper for bootstrap confidence intervals.


def compute_priming_rate(parsed_records: list[dict[str, Any]]) -> dict[str, float]:
    """Compute priming rates for each condition."""
    raise NotImplementedError("TODO: implement compute_priming_rate")


def compute_effect_size(parsed_records: list[dict[str, Any]], treatment_condition: str, control_condition: str) -> dict[str, float]:
    """Compute effect size statistics for priming effect."""
    raise NotImplementedError("TODO: implement compute_effect_size")


def bootstrap_confidence_interval(values: list[float], num_samples: int, seed: int) -> tuple[float, float]:
    """Return bootstrap confidence interval for a metric."""
    raise NotImplementedError("TODO: implement bootstrap_confidence_interval")

"""Session 4: Auto-analysis agent that judges whether the prime affected output."""

from typing import Any


# TODO(Session 4)
# - Read existing Session 3 metrics/stats outputs (do not recompute them here).
# - Turn effect size + p-value evidence into a plain-language verdict.
# - Flag "inconclusive" when evidence is weak or contradictory.


def auto_analyze_prime_effect(metrics_summary: dict[str, Any], stats_summary: dict[str, Any]) -> dict[str, Any]:
    """Return a verdict on whether the prime affected output.

    Expected return keys: verdict ("significant" | "not_significant" | "inconclusive"),
    confidence (0.0-1.0), effect_size_interpretation (str), reasoning (str).
    """
    raise NotImplementedError("TODO: implement auto_analyze_prime_effect")


def summarize_verdict_for_human(verdict: dict[str, Any]) -> str:
    """Return a one-paragraph human-readable summary of the verdict."""
    raise NotImplementedError("TODO: implement summarize_verdict_for_human")

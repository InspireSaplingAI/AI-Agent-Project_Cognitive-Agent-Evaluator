"""Session 4: Epsilon-greedy multi-armed bandit for self-optimizing prompt selection.

This is the simplest form of reinforcement learning: no state transitions,
just "try variants, track average reward, favor what works while still exploring."
"""

from typing import Any


# TODO(Session 4)
# - Track trials/reward per prompt variant.
# - Pick the next variant to try: explore randomly with probability epsilon,
#   otherwise exploit the current best average reward.
# - Update the running average reward after each round.


def initialize_variant_stats(variants: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    """Return starting stats for each variant: trials, total_reward, avg_reward."""
    raise NotImplementedError("TODO: implement initialize_variant_stats")


def select_variant_epsilon_greedy(
    variant_stats: dict[str, dict[str, float]], epsilon: float = 0.2, seed: int | None = None
) -> str:
    """Return the name of the next variant to try (explore vs exploit)."""
    raise NotImplementedError("TODO: implement select_variant_epsilon_greedy")


def update_variant_reward(
    variant_stats: dict[str, dict[str, float]], variant_name: str, reward: float
) -> dict[str, dict[str, float]]:
    """Update a variant's running average reward after observing one round's result."""
    raise NotImplementedError("TODO: implement update_variant_reward")

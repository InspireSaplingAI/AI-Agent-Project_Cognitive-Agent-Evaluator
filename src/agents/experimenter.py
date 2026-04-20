"""Session 2: Build experimenter-side prompts from stimuli."""

from typing import Any


# TODO(Session 2)
# - Build system and user prompt segments from stimuli.
# - Add optional controls for temperature and instruction style.
# - Track trace metadata for reproducibility.


def build_experimenter_prompt(stimulus: dict[str, Any], prompt_style: str) -> dict[str, Any]:
    """Construct one experimenter prompt package."""
    raise NotImplementedError("TODO: implement build_experimenter_prompt")


def attach_run_metadata(prompt_package: dict[str, Any], run_id: str, trial_index: int) -> dict[str, Any]:
    """Attach deterministic run metadata to prompt package."""
    raise NotImplementedError("TODO: implement attach_run_metadata")


def preview_prompt(prompt_package: dict[str, Any]) -> str:
    """Return human-readable prompt preview for notebook checks."""
    raise NotImplementedError("TODO: implement preview_prompt")

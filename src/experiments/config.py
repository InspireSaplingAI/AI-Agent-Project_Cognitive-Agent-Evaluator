"""Session 2: Experiment configuration loading and validation."""

from typing import Any


# TODO(Session 2)
# - Define config schema for model, run count, and seed.
# - Add validation for required fields.
# - Add defaults for local notebook experimentation.


def load_experiment_config(path: str) -> dict[str, Any]:
    """Load experiment config from YAML or JSON path."""
    raise NotImplementedError("TODO: implement load_experiment_config")


def validate_experiment_config(config: dict[str, Any]) -> list[str]:
    """Return config validation errors."""
    raise NotImplementedError("TODO: implement validate_experiment_config")


def build_default_config() -> dict[str, Any]:
    """Return a default config for notebook experiments."""
    raise NotImplementedError("TODO: implement build_default_config")

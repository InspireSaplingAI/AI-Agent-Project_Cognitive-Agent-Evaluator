"""Session 1: Validate stimuli schema and constraints."""

from typing import Any


# TODO(Session 1)
# - Validate required fields and datatypes.
# - Validate condition balance assumptions.
# - Produce readable error messages for notebook debugging.


def validate_stimulus_record(record: dict[str, Any]) -> list[str]:
    """Return a list of validation errors for one stimulus record.

    Input:
    - record: one stimulus dictionary.

    Output:
    - list[str]: human-readable error messages; empty list means valid.

    Why this design:
    - list of messages is notebook-friendly and easy for students to inspect.
    - non-throwing validation supports batch debugging without hard stop.
    """
    raise NotImplementedError("TODO: implement validate_stimulus_record")


def validate_stimulus_batch(stimuli: list[dict[str, Any]]) -> list[str]:
    """Return aggregated validation errors for a batch.

    Input:
    - stimuli: list of stimulus records.

    Output:
    - list[str]: aggregated messages, ideally including record index/id context.

    Why this design:
    - batch-level checks catch systemic issues early (missing fields, duplicates).
    - one aggregated error list simplifies notebook assertions.
    """
    raise NotImplementedError("TODO: implement validate_stimulus_batch")


def summarize_condition_balance(stimuli: list[dict[str, Any]]) -> dict[str, int]:
    """Return count summary by condition label.

    Input:
    - stimuli: list of stimulus records.

    Output:
    - dict[str, int]: count per condition, for example
      {"active_prime": 20, "passive_prime": 20}.

    Why this design:
    - balance is a core experimental requirement for fair comparisons.
    - compact dict output can be printed directly in notebooks and tests.
    """
    raise NotImplementedError("TODO: implement summarize_condition_balance")

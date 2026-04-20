"""Session 3: Parse subject outputs into analysis-ready records."""

from typing import Any


# TODO(Session 3)
# - Parse response text for target syntactic structure usage.
# - Track parser confidence or uncertainty flags.
# - Return normalized analysis record schema.


def parse_trial_output(trial_output: dict[str, Any]) -> dict[str, Any]:
    """Parse one trial output into analysis features."""
    raise NotImplementedError("TODO: implement parse_trial_output")


def parse_batch_outputs(trial_outputs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Parse all trial outputs into feature records."""
    raise NotImplementedError("TODO: implement parse_batch_outputs")


def flag_ambiguous_parses(parsed_records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Flag records that need manual review."""
    raise NotImplementedError("TODO: implement flag_ambiguous_parses")

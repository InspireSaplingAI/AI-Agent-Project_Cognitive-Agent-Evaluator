"""Common file IO helpers for run artifacts."""

from typing import Any


# TODO(Common)
# - Implement JSONL reader/writer helpers.
# - Implement CSV export helpers.
# - Add directory creation and path safety checks.


def read_jsonl(path: str) -> list[dict[str, Any]]:
    """Read JSONL file into list of dicts."""
    raise NotImplementedError("TODO: implement read_jsonl")


def write_jsonl(path: str, records: list[dict[str, Any]]) -> str:
    """Write records as JSONL and return output path."""
    raise NotImplementedError("TODO: implement write_jsonl")


def write_csv(path: str, records: list[dict[str, Any]]) -> str:
    """Write records as CSV and return output path."""
    raise NotImplementedError("TODO: implement write_csv")

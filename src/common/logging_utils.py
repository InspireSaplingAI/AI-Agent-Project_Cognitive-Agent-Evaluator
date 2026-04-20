"""Common logging helpers for reproducible experiments."""

from typing import Any


# TODO(Common)
# - Standardize run-level logging fields.
# - Emit machine-readable logs for later debugging.
# - Add helper for timing and step-level events.


def build_logger(name: str) -> Any:
    """Create and return configured logger instance."""
    raise NotImplementedError("TODO: implement build_logger")


def log_run_start(logger: Any, run_id: str, config: dict[str, Any]) -> None:
    """Log run start metadata."""
    raise NotImplementedError("TODO: implement log_run_start")


def log_run_end(logger: Any, run_id: str, summary: dict[str, Any]) -> None:
    """Log run end summary."""
    raise NotImplementedError("TODO: implement log_run_end")

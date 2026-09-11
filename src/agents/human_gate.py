"""Session 4: Human-in-the-loop approval checkpoint for optimization rollouts."""

from typing import Any


# TODO(Session 4)
# - Present a proposal (e.g. best prompt variant) to a human reviewer.
# - Block on input() for a y/n decision unless auto_approve is set.
# - Record every decision so rollouts stay auditable.


def request_human_approval(proposal: dict[str, Any], auto_approve: bool = False) -> dict[str, Any]:
    """Ask a human to approve or reject a proposal, or auto-approve for automated runs.

    Expected return keys: approved (bool), approver ("human" | "auto"), notes (str).
    """
    raise NotImplementedError("TODO: implement request_human_approval")


def log_human_decision(decision: dict[str, Any], log_path: str) -> None:
    """Append a human/auto decision to an audit trail file."""
    raise NotImplementedError("TODO: implement log_human_decision")

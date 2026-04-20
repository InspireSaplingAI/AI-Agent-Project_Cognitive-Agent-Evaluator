"""Session 2: Wrap LLM as the subject under test."""

from typing import Any


# TODO(Session 2)
# - Implement provider-agnostic LLM call wrapper.
# - Capture output text plus usage metadata.
# - Add retry and timeout strategy placeholders.


def invoke_subject_llm(prompt_package: dict[str, Any], model_name: str, generation_config: dict[str, Any]) -> dict[str, Any]:
    """Call the LLM subject and return raw response payload."""
    raise NotImplementedError("TODO: implement invoke_subject_llm")


def normalize_subject_response(raw_response: dict[str, Any]) -> dict[str, Any]:
    """Normalize provider response into a standard schema."""
    raise NotImplementedError("TODO: implement normalize_subject_response")


def extract_subject_text(normalized_response: dict[str, Any]) -> str:
    """Extract final response text for downstream analysis."""
    raise NotImplementedError("TODO: implement extract_subject_text")

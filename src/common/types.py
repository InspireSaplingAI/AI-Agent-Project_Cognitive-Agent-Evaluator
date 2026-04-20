"""Shared data schemas for experiment pipeline."""

from dataclasses import dataclass
from typing import Any


# TODO(Common)
# - Convert broad Any fields into specific typed fields.
# - Add runtime validation layer if needed.


@dataclass
class StimulusRecord:
    """Single stimulus entry used for one trial."""

    stimulus_id: str
    condition: str
    prime_text: str
    target_prompt: str
    metadata: dict[str, Any]


@dataclass
class TrialOutput:
    """Single trial output emitted by subject LLM."""

    run_id: str
    trial_index: int
    stimulus_id: str
    model_name: str
    response_text: str
    metadata: dict[str, Any]


@dataclass
class AnalysisRecord:
    """Parsed trial output with analysis features."""

    run_id: str
    stimulus_id: str
    condition: str
    used_target_structure: bool
    parser_notes: str

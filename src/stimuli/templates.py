"""Session 1: Define syntactic priming templates."""

from typing import Any


# Interface contract used across Session 1:
# template_registry: dict[str, dict[str, Any]]
# - key: template name, for example "active_prime_v1"
# - value: template definition containing at least:
#   - condition: condition label used for balancing/statistics
#   - structure_label: expected syntax label, for example "active" or "passive"
#   - prime_text_template: format string for prime sentence
#   - target_prompt_template: format string for target elicitation prompt
#   - lexical_constraints: optional constraints for slot values
#
# Why this shape:
# - keyed lookup by template name is simple and deterministic
# - each template stores both generation pieces (prime + target)
# - condition and structure labels are available early for balancing and validation


# TODO(Session 1)
# - Define template schema for prime and target prompts.
# - Include metadata fields: condition, structure_label, lexical_constraints.
# - Add at least one active/passive pair and one dative alternation pair.


def build_template_registry() -> dict[str, dict[str, Any]]:
    """Return all template definitions keyed by template name.

    Input:
    - None.

    Output:
    - dict[str, dict[str, Any]] where each value is one template definition.

    Why this design:
    - A single source of truth for all templates makes Session 1 reproducible.
    - Generator and validator can share the same template metadata.
    - Students can add/remove conditions in one location.
    """
    raise NotImplementedError("TODO: implement build_template_registry")


def render_template(template_name: str, variables: dict[str, Any]) -> str:
    """Render one template into a concrete prompt string.

    Input:
    - template_name: template key existing in template_registry.
    - variables: slot values used by the template format string,
      for example {"agent": "chef", "patient": "assistant", "verb": "praised"}.

    Output:
    - str: rendered text (prime sentence or target prompt fragment).

    Why this design:
    - Decouples template definition from lexical slot values.
    - Enables deterministic generation by passing explicit variables.
    - Keeps all text creation auditable without free-form LLM generation.
    """
    raise NotImplementedError("TODO: implement render_template")


def list_template_names() -> list[str]:
    """List available template identifiers.

    Input:
    - None.

    Output:
    - list[str]: stable list of template names.

    Why this design:
    - Allows quick checks in notebooks (what templates exist).
    - Supports deterministic ordering for tests and sampling.
    - Simplifies condition coverage debugging.
    """
    raise NotImplementedError("TODO: implement list_template_names")

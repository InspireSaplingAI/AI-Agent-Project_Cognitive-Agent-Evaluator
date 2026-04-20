"""Session 1: Generate balanced stimuli sets."""

from typing import Any


# TODO(Session 1)
# - Generate a balanced set across syntactic conditions using template expansion,
#   not free-form LLM generation as the default path.
# - Suggested approach:
#   1) Compute per-condition target counts with quotient/remainder split.
#   2) Sample or cycle templates per condition until counts are met.
#   3) Assign deterministic stimulus_id values.
# - Support deterministic shuffling via random seed.
# - Suggested batch sizes:
#   - pilot: 40-80
#   - assignment: 120-240
#   - stronger statistical signal: 300-600
# - Save generated stimuli to data/raw, and post-validation copies to data/processed.
# - Return records compatible with common.types.StimulusRecord.


def generate_stimuli_batch(template_registry: dict[str, Any], batch_size: int, seed: int) -> list[dict[str, Any]]:
    """Generate a balanced batch of stimulus records.

    Input:
    - template_registry: output of build_template_registry().
    - batch_size: target total number of records.
    - seed: random seed used for deterministic choices/shuffling.

    Output:
    - list[dict[str, Any]] where each record should include at least:
      - stimulus_id: unique id, for example "s0001"
      - condition: condition label used for balancing/statistics
      - prime_text: rendered prime sentence
      - target_prompt: neutral elicitation prompt
      - metadata: additional analysis/debug fields

    Why this design:
    - batch_size controls experiment scale with one parameter.
    - seed ensures reproducibility for debugging and comparisons.
    - explicit record schema aligns with validator and Session 2 runner.
    """
    raise NotImplementedError("TODO: implement generate_stimuli_batch")


def randomize_stimuli_order(stimuli: list[dict[str, Any]], seed: int) -> list[dict[str, Any]]:
    """Return shuffled stimuli order with reproducibility.

    Input:
    - stimuli: generated records before final order randomization.
    - seed: random seed controlling shuffle order.

    Output:
    - list[dict[str, Any]]: same records, deterministic shuffled order.

    Why this design:
    - removes ordering bias while keeping runs reproducible.
    - allows exact reruns for error analysis and statistical replication.
    """
    raise NotImplementedError("TODO: implement randomize_stimuli_order")


def split_train_eval_stimuli(stimuli: list[dict[str, Any]], eval_ratio: float, seed: int) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Split stimuli into train/eval subsets.

    Input:
    - stimuli: full generated set.
    - eval_ratio: float in (0, 1), fraction assigned to eval split.
    - seed: random seed controlling split assignment.

    Output:
    - tuple[train, eval]: two lists of records.

    Why this design:
    - supports clean separation for development vs final evaluation.
    - makes overfitting to one fixed set less likely.
    - tuple return is explicit and easy to unpack in notebooks.
    """
    raise NotImplementedError("TODO: implement split_train_eval_stimuli")

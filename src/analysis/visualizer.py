"""Session 3: Visualization utilities for analysis results.

Generates:
- Bar charts: priming rate by condition with error bars
- Box plots: response length distribution by condition
- Heatmap: confusion matrix for parser validation
- Scatter plot: response length vs priming outcome
- Grouped bar chart: multi-metric comparison across conditions
"""

from typing import Any


# TODO(Session 3)
# - Bar chart: priming rate per condition with bootstrap CI error bars
# - Box plot: response length distribution per condition
# - Heatmap: confusion matrix (predicted vs actual structure)
# - Scatter plot: response length vs used_target_structure (jittered)
# - Grouped bar chart: compare multiple metrics across conditions
# - Save all figures to artifacts/reports/ directory


def plot_priming_rates(parsed_records: list[dict[str, Any]],
                       title: str = "Priming Rate by Condition",
                       save_path: str | None = None) -> str:
    """Plot bar chart of priming rates per condition with error bars.

    Args:
        parsed_records: List of parsed records
        title: Chart title
        save_path: If provided, save figure to this path

    Returns:
        Path to saved figure (or empty string if not saved)
    """
    raise NotImplementedError("TODO: implement plot_priming_rates")


def plot_response_length_distribution(parsed_records: list[dict[str, Any]],
                                      title: str = "Response Length by Condition",
                                      save_path: str | None = None) -> str:
    """Plot box plot of response length distribution per condition.

    Returns path to saved figure.
    """
    raise NotImplementedError("TODO: implement plot_response_length_distribution")


def plot_confusion_matrix(confusion_matrix: dict[str, int],
                          title: str = "Parser Confusion Matrix",
                          save_path: str | None = None) -> str:
    """Plot heatmap of confusion matrix (predicted vs actual).

    Args:
        confusion_matrix: Dict with keys true_positive, false_positive,
                         true_negative, false_negative
    Returns path to saved figure.
    """
    raise NotImplementedError("TODO: implement plot_confusion_matrix")


def plot_priming_vs_length(parsed_records: list[dict[str, Any]],
                           title: str = "Response Length vs Priming Outcome",
                           save_path: str | None = None) -> str:
    """Plot scatter plot of response length vs used_target_structure with jitter.

    Returns path to saved figure.
    """
    raise NotImplementedError("TODO: implement plot_priming_vs_length")


def plot_multi_metric_comparison(parsed_records: list[dict[str, Any]],
                                 title: str = "Multi-Metric Comparison by Condition",
                                 save_path: str | None = None) -> str:
    """Plot grouped bar chart comparing multiple metrics across conditions.

    Metrics: priming rate, avg response length, lexical diversity
    Returns path to saved figure.
    """
    raise NotImplementedError("TODO: implement plot_multi_metric_comparison")


def generate_all_plots(parsed_records: list[dict[str, Any]],
                       confusion_matrix: dict[str, int] | None = None,
                       output_dir: str = "artifacts/reports") -> dict[str, str]:
    """Generate all standard plots and return dict of plot_name -> file_path.

    Returns dict like:
        {"priming_rates": "artifacts/reports/priming_rates.png", ...}
    """
    raise NotImplementedError("TODO: implement generate_all_plots")
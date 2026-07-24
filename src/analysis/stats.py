"""Session 3: Statistical testing for syntactic priming experiments.

Supports:
- Chi-square contingency test
- Logistic regression (binary outcome: used_target_structure)
- Mixed-effects logistic regression (accounts for random effects)
- Power analysis (how many trials needed?)
- Post-hoc multiple comparison correction (Tukey HSD)
"""

from typing import Any


# TODO(Session 3)
# - Build 2x2 contingency table (condition x used_target_structure)
# - Run chi-square test and return chi2 statistic, p-value, expected frequencies
# - Run logistic regression: used_target_structure ~ condition
# - Run mixed-effects logistic regression: used_target_structure ~ condition + (1|verb)
# - Compute statistical power for a given sample size and effect size
# - Run post-hoc Tukey HSD for multiple condition comparisons
# - Combine all results into a notebook-friendly summary dict


def run_chi_square_test(parsed_records: list[dict[str, Any]]) -> dict[str, Any]:
    """Run chi-square test for association between condition and structure usage.

    Returns dict with:
        - chi2_statistic: float
        - p_value: float
        - dof: int (degrees of freedom)
        - contingency_table: 2D list (conditions x used_target_structure)
        - expected_frequencies: 2D list
        - effect_size_cramers_v: float (Cramér's V)
        - significant: bool (p < 0.05)
    """
    raise NotImplementedError("TODO: implement run_chi_square_test")


def run_logistic_regression(parsed_records: list[dict[str, Any]],
                            formula: str = "used_target_structure ~ condition") -> dict[str, Any]:
    """Fit logistic regression model.

    Args:
        parsed_records: List of parsed records with 'used_target_structure' and 'condition'
        formula: Model formula (default: used_target_structure ~ condition)

    Returns dict with:
        - coefficients: dict mapping predictor -> estimate
        - p_values: dict mapping predictor -> p-value
        - confidence_intervals: dict mapping predictor -> (lower, upper)
        - pseudo_r_squared: float (McFadden's)
        - model_summary: str (text summary for display)
        - significant_predictors: list[str]
    """
    raise NotImplementedError("TODO: implement run_logistic_regression")


def run_mixed_effects_model(parsed_records: list[dict[str, Any]],
                            formula: str = "used_target_structure ~ condition + (1|stimulus_id)") -> dict[str, Any]:
    """Fit mixed-effects logistic regression.

    Accounts for random effects (e.g., by stimulus_id or verb) to avoid
    pseudoreplication bias.

    Returns dict with:
        - fixed_effects: dict mapping predictor -> estimate
        - random_effects_variance: dict
        - p_values: dict
        - significant_predictors: list[str]
        - model_summary: str
    """
    raise NotImplementedError("TODO: implement run_mixed_effects_model")


def run_power_analysis(effect_size: float,
                       sample_size: int,
                       alpha: float = 0.05,
                       num_conditions: int = 2) -> dict[str, Any]:
    """Compute statistical power for a given effect size and sample size.

    Args:
        effect_size: Expected effect size (Cohen's d or odds ratio)
        sample_size: Number of trials
        alpha: Significance level (default 0.05)
        num_conditions: Number of conditions being compared

    Returns dict with:
        - power: float (0.0 to 1.0)
        - sample_size: int
        - effect_size: float
        - alpha: float
        - interpretation: str (e.g., "sufficient power" or "underpowered")
    """
    raise NotImplementedError("TODO: implement run_power_analysis")


def run_tukey_hsd(parsed_records: list[dict[str, Any]]) -> dict[str, Any]:
    """Run Tukey HSD post-hoc test for multiple condition comparisons.

    Returns dict with:
        - pairwise_comparisons: list of dicts with (group1, group2, meandiff, p-adj, reject)
        - significant_pairs: list[str] of condition pairs that differ significantly
    """
    raise NotImplementedError("TODO: implement run_tukey_hsd")


def summarize_statistical_results(chi_square_result: dict[str, Any],
                                  logistic_result: dict[str, Any],
                                  mixed_model_result: dict[str, Any] | None = None,
                                  power_result: dict[str, Any] | None = None,
                                  tukey_result: dict[str, Any] | None = None) -> dict[str, Any]:
    """Combine all statistical test results into one summary payload.

    Returns a single dict with all key findings for notebook display and Session 4.
    """
    raise NotImplementedError("TODO: implement summarize_statistical_results")
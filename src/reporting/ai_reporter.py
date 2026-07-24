"""Session 4: AI-generated analysis report using LLM.

Takes experiment metrics and statistical results, then uses an LLM
to generate a structured scientific summary of the findings.
"""

from typing import Any, Callable


# TODO(Session 4)
# - Build a structured prompt that includes experiment config, metrics, and stats
# - Call an LLM to generate a scientific summary in natural language
# - Parse the LLM response into sections (abstract, methods, results, discussion)
# - Compare AI-generated report vs human-written summary
# - Support configurable report styles (concise, detailed, interview-ready)


def build_report_context(experiment_summary: dict[str, Any],
                         metrics_summary: dict[str, Any],
                         stats_summary: dict[str, Any]) -> str:
    """Build a structured text block containing all experiment results.

    Combines experiment design, priming metrics, and statistical findings
    into a formatted string that can be passed to an LLM.

    Returns a string with clearly labeled sections.
    """
    raise NotImplementedError("TODO: implement build_report_context")


def generate_ai_report(experiment_summary: dict[str, Any],
                       metrics_summary: dict[str, Any],
                       stats_summary: dict[str, Any],
                       llm_func: Callable | None = None,
                       style: str = "detailed") -> dict[str, str]:
    """Generate a scientific report using an LLM.

    Args:
        experiment_summary: Dict with run_id, model_name, num_trials, conditions, etc.
        metrics_summary: Dict with priming rate, effect size, response length, etc.
        stats_summary: Dict with chi-square, logistic regression results, etc.
        llm_func: A callable that takes a prompt string and returns text.
                  If None, returns a template-based structured report instead.
        style: "concise" (3 paragraphs), "detailed" (5 sections), or "interview" (Q&A)

    Returns dict with sections as keys:
        {"abstract": str, "methods": str, "results": str, "discussion": str,
         "limitations": str, "full_report": str}
    """
    raise NotImplementedError("TODO: implement generate_ai_report")


def compare_human_vs_ai_report(human_report: str,
                               ai_report: dict[str, str],
                               criteria: list[str] | None = None) -> dict[str, Any]:
    """Compare human-written and AI-generated reports on given criteria.

    Args:
        human_report: Human-written report text
        ai_report: Dict of AI report sections
        criteria: List of criteria to compare (default: ["accuracy", "completeness",
                  "clarity", "conciseness", "actionability"])

    Returns dict with:
        - scores: dict mapping criterion -> {"human": float, "ai": float}
        - strengths: dict mapping "human" and "ai" to list of strengths
        - weaknesses: dict mapping "human" and "ai" to list of weaknesses
    """
    raise NotImplementedError("TODO: implement compare_human_vs_ai_report")


def render_resume_bullets(experiment_summary: dict[str, Any],
                          key_finding: str = "") -> list[str]:
    """Generate concise resume bullet points from project results.

    Returns up to 4 bullet points suitable for a resume.
    """
    raise NotImplementedError("TODO: implement render_resume_bullets")
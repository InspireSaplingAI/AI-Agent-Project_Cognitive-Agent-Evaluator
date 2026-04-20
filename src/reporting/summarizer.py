"""Session 4: Build interview-ready and report-ready summaries."""

from typing import Any


# TODO(Session 4)
# - Build concise project summary with methods and findings.
# - Convert statistical outputs into readable bullet points.
# - Include limitation and next-step sections.


def build_project_summary(experiment_summary: dict[str, Any], analysis_summary: dict[str, Any], optimization_summary: dict[str, Any]) -> dict[str, Any]:
    """Return a structured final project summary."""
    raise NotImplementedError("TODO: implement build_project_summary")


def render_resume_bullets(project_summary: dict[str, Any], max_bullets: int = 4) -> list[str]:
    """Generate concise resume bullets."""
    raise NotImplementedError("TODO: implement render_resume_bullets")


def export_markdown_report(project_summary: dict[str, Any], output_path: str) -> str:
    """Export Markdown report and return path."""
    raise NotImplementedError("TODO: implement export_markdown_report")

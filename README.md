# Cognitive-Agent Evaluator

A student project for testing and optimizing syntactic priming effects in LLM-based dialogue agents.

## Project Outline

This project builds a Python multi-agent evaluation pipeline:
- An Experimenter Agent generates controlled syntactic prompts (stimuli).
- A Subject Agent (LLM wrapper) responds to stimuli.
- An Analysis pipeline tests whether output syntax is influenced by prior prime structures.
- An Optimization pipeline improves prompt strategy and reports measurable gains.

The final output is a resume-ready portfolio artifact showing cognitive science theory applied to modern AI evaluation and alignment workflows.

## Key Concepts

- Syntactic Priming: prior sentence structures can bias later sentence production.
- Stimuli Preparation: controlled prompt templates and balanced conditions.
- Agentic Evaluation: reproducible multi-agent loops for LLM behavior testing.
- Statistical Inference: chi-square and logistic regression for effect validation.
- Alignment Relevance: understanding controllability and robustness of model behavior.

## Learning Objectives

By completing this project, the student will be able to:
1. Translate cognitive science experiment design into LLM prompt protocols.
2. Build a modular multi-agent experiment runner in Python.
3. Analyze large sets of LLM outputs with reproducible metrics.
4. Design and evaluate optimization strategies via A/B testing.
5. Present findings clearly for internship and job interviews.

## 4-Session Roadmap

### Session 1 - Setup and Stimuli Design
Notebook: `notebooks/session1_setup_and_stimuli.ipynb`

Focus:
- Design stimulus schema and template system.
- Generate balanced and deterministic stimulus batches.
- Validate stimulus quality and condition coverage.

Source files to complete:
- `src/stimuli/templates.py`
- `src/stimuli/generator.py`
- `src/stimuli/validator.py`

Deliverable:
- Validated stimulus dataset ready for experiment runs.

Practical guidance for Session 1:
- Do not rely on free-form LLM generation as the primary method. Build stimuli from manually defined templates in `src/stimuli/templates.py`.
- Use balanced allocation across conditions in `src/stimuli/generator.py`:
    - pilot scale: 40 to 80 total stimuli
    - assignment scale: 120 to 240 total stimuli
    - stronger analysis scale: 300 to 600 total stimuli
- Store assets in these locations:
    - schema and templates: `src/stimuli/templates.py`
    - generated raw stimuli: `data/raw/stimuli_session1_seed_<seed>.jsonl`
    - validated or transformed stimuli: `data/processed/stimuli_balanced_seed_<seed>.jsonl`
    - run outputs are generated in Session 2 under `artifacts/runs/`

Recommended Session 1 workflow:
1. Define 3 to 5 syntactic conditions and template sets per condition.
2. Fill lexical slots from small controlled lexicons (agent, patient, verb).
3. Balance per-condition counts first, then shuffle with a fixed seed.
4. Validate schema fields and condition counts before moving to Session 2.

### Session 2 - Multi-Agent Experiment Loop
Notebook: `notebooks/session2_agent_loop.ipynb`

Focus:
- Build prompt packages from stimuli.
- Wrap LLM calls in a normalized schema.
- Run batch experiments and persist raw outputs.

Source files to complete:
- `src/agents/experimenter.py`
- `src/agents/subject_llm.py`
- `src/agents/dialogue_runner.py`
- `src/experiments/config.py`
- `src/experiments/runner.py`

Deliverable:
- End-to-end run artifact with trial-level outputs.

### Session 3 - Analysis and Statistics
Notebook: `notebooks/session3_analysis.ipynb`

Focus:
- Parse raw output text into analysis features.
- Compute priming-rate and effect-size metrics.
- Run chi-square and logistic regression summaries.

Source files to complete:
- `src/analysis/parser.py`
- `src/analysis/metrics.py`
- `src/analysis/stats.py`

Deliverable:
- Statistical evidence report with effect interpretation.

### Session 4 - Optimization and Reporting
Notebook: `notebooks/session4_optimization_and_report.ipynb`

Focus:
- Evaluate prompt variants.
- Run A/B comparisons against baseline.
- Build final summary and resume bullet points.

Source files to complete:
- `src/optimization/prompt_optimizer.py`
- `src/optimization/ab_test.py`
- `src/reporting/summarizer.py`
- `src/common/logging_utils.py`

Deliverable:
- Final report and interview-ready project narrative.

## Notebook Policy

The notebooks are playground guides, not production solutions.
- They include examples, call patterns, and TODO checkpoints.
- They intentionally avoid full implementation logic.
- Core coding work must be done in `src/` modules.

## Repository Structure

```
.
|-- README.md
|-- requirements.txt
|-- notebooks/
|   |-- session1_setup_and_stimuli.ipynb
|   |-- session2_agent_loop.ipynb
|   |-- session3_analysis.ipynb
|   `-- session4_optimization_and_report.ipynb
|-- src/
|   |-- agents/
|   |-- analysis/
|   |-- common/
|   |-- experiments/
|   |-- optimization/
|   |-- reporting/
|   `-- stimuli/
|-- tests/
|   |-- test_metrics.py
|   |-- test_runner.py
|   `-- test_stimuli.py
|-- data/
|   |-- raw/
|   `-- processed/
`-- artifacts/
    |-- reports/
    `-- runs/
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Open and run notebook session 1.
4. Implement TODOs in the mapped source files.
5. Repeat session-by-session.

## Suggested Weekly Workflow

1. Complete one notebook session.
2. Implement all TODOs linked by that notebook.
3. Add or update tests in `tests/`.
4. Record assumptions, errors, and key findings.
5. Prepare a short oral summary of what changed and why.

## Evaluation Rubric (Student Progress)

- Reproducibility: deterministic stimulus generation and run tracking.
- Correctness: schemas are validated and pipeline outputs are consistent.
- Analysis quality: metrics and statistics are correctly interpreted.
- Optimization rigor: A/B comparisons are controlled and justified.
- Communication: final report and resume bullets are concise and evidence-based.

## Resume Framing Examples

- Built a Python multi-agent evaluation framework to measure syntactic priming effects in LLM outputs.
- Designed controlled prompt stimuli and analyzed thousands of generated responses using chi-square and logistic regression.
- Implemented reproducible experimentation and A/B optimization workflows for model behavior alignment.
- Produced a structured findings report translating cognitive science methods into practical AI safety evaluation.

## Stretch Goals (Optional)

- Add mixed-effects models for deeper linguistic analysis.
- Add dashboard visualizations for condition-level metrics.
- Compare multiple LLM providers under identical stimuli.

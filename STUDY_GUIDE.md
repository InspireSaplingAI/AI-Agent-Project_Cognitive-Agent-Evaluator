# Further Study Guide: AI Agents and Cognitive Agents

This guide is for students who have completed, or are completing, the **Cognitive-Agent Evaluator** project. Its goal is to build practical understanding first. You do **not** need to understand every recent research paper before extending the project.

## How This Project Connects to AI Agents

The project already contains a small agent workflow:

```text
Planner -> Executor -> Critic -> Human Gate
```

| Project component | Plain-language role |
|---|---|
| Planner | Chooses the next prompt variant to test. |
| Executor | Runs the experiment and records outputs. |
| Critic | Checks existing metrics and statistics before making a claim. |
| Human Gate | Makes the final approval decision. |
| Bandit optimizer | Learns which option to try more often from previous rewards. |

This is a useful foundation. A real agent system is usually just this same idea with more tools, better logging, clearer rules, and stricter evaluation.

## The Most Important Ideas to Learn First

Study these in order. Do not add more agents until the earlier stages work reliably.

### 1. Reliable experiments

Learn to answer: **Can another person rerun this experiment and get comparable results?**

Practice in this repository:

- Save the model name, temperature, random seed, prompt version, and run time.
- Keep a baseline prompt strategy such as `minimal`.
- Compare every new strategy to the baseline.
- Record failures, not only successful runs.
- Separate a development dataset from a final evaluation dataset.

Why it matters: an agent that appears to improve may simply be benefiting from random variation or an easier test set.

### 2. Tool use and structured outputs

An agent becomes useful when it can use controlled tools, such as reading a result file or producing a chart.

Start simply:

- Give the analyst read-only access to experiment artifacts.
- Require tool calls to use validated JSON-like fields.
- Allow only known tools and known arguments.
- Return an error message when a tool call is invalid.

Do **not** begin with unrestricted shell commands, browser control, or write access.

### 3. Memory

Memory means using useful information from prior work. It does **not** mean giving an agent every previous message.

Start with two small memory files:

- **Experiment memory:** variant, metric, sample size, outcome, and date.
- **Failure memory:** what failed, likely reason, and how to avoid repeating it.

Before using memory in decisions, check that the retrieved item is relevant and not outdated.

### 4. Planning and reflection

Planning breaks a goal into steps. Reflection checks whether the result supports the conclusion.

A simple plan for this project is:

1. Choose a prompt variant.
2. Run a fixed number of trials.
3. Compute metrics using the existing analysis modules.
4. Ask the critic whether the evidence supports a recommendation.
5. Ask a human before rollout.

The critic should be allowed to return **inconclusive**. A system that always makes a confident recommendation is not reliable.

### 5. Multi-agent workflows

Use several agents only when each one has a distinct job. More agents can make a system slower, more expensive, and harder to debug.

Before adding a new role, answer:

- What unique information, tool, or responsibility does it have?
- Could a single agent do the same job more simply?
- How will its contribution be measured?
- What stops the workflow from looping forever?

## A Four-Week Extension Plan

### Week 1 — Make the current loop observable

Goal: understand every decision made by the Planner, Executor, Critic, and Human Gate.

Tasks:

- Save one JSONL record per optimization round.
- Record selected variant, reward, metrics summary, verdict, cost estimate, and latency.
- Add a `run_id` to connect all artifacts from one run.
- Write one test for a valid flow and one for an inconclusive result.

Success check: you can explain why the system selected its final variant by reading one trace file.

### Week 2 — Add a simple memory component

Goal: reuse validated past results without hiding information in a long prompt.

Tasks:

- Store prior experiment summaries in a small JSON file.
- Retrieve only results with the same task type and model configuration.
- Include the retrieved evidence in the Planner's decision record.
- Add an expiry rule for old or incompatible results.

Success check: the planner can state which previous result influenced a choice and why it was relevant.

### Week 3 — Compare one agent with a workflow

Goal: find out whether multiple roles actually help.

Compare these systems on the same fixed scenarios:

1. One agent produces a recommendation.
2. Planner + Executor produces a recommendation.
3. Planner + Executor + Critic produces a recommendation.
4. Planner + Executor + Critic + Human Gate produces a final decision.

Measure:

- recommendation quality;
- unsupported-claim rate;
- cost and latency;
- failure rate;
- human preference.

Success check: document whether each added role gave enough benefit to justify its cost.

### Week 4 — Add safe tool use

Goal: let the analyst inspect artifacts without giving it unsafe powers.

Tasks:

- Add a read-only function to load a known experiment result.
- Add a function to make a chart from validated metrics.
- Validate every tool argument before use.
- Ensure untrusted text in experiment outputs cannot change system instructions.

Success check: malformed requests fail safely and no tool can write, execute, or access files outside the allowed artifact directory.

## Suggested Small Projects

Choose **one** project at a time.

| Project | What you learn | Good first milestone |
|---|---|---|
| Experiment trace viewer | Observability | Display a round-by-round table from JSONL logs. |
| Evidence-based critic | Reflection | Require each recommendation to cite a metric and sample size. |
| Memory for prior trials | Cognitive memory | Retrieve one relevant prior trial before planning. |
| Cost-aware bandit | Optimization | Reward high priming rate while penalizing slow or costly variants. |
| Single vs. multi-agent comparison | Evaluation | Run the same 10 scenarios with both designs. |
| Safe artifact-analysis tool | Tool use and security | Permit reading only approved JSON result files. |

## Questions to Ask During Every Extension

1. What exact task is the agent trying to complete?
2. What is the simple non-agent baseline?
3. What evidence determines success?
4. What happens when evidence is insufficient?
5. What actions require human approval?
6. What data or tool inputs are untrusted?
7. How much do quality, cost, and latency change?

## Recent Reading: Optional, Accessible Starting Points

Read the abstract, introduction, figures, and conclusion first. Skip technical sections on the first pass. The goal is to understand the problem each paper addresses, not to memorize methods.

### Start here: orientation and safety

1. **Acharya, Kuppan, and Divya (2025)** — *Agentic AI: Autonomous Intelligence for Complex Goals—A Comprehensive Survey.* IEEE Access.  
   DOI: <https://doi.org/10.1109/ACCESS.2025.3532853>  
   **Read for:** a broad map of planning, tools, autonomy, and evaluation. Read the introduction and architecture diagrams first.

2. **Deng et al. (2025)** — *AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways.* ACM Computing Surveys.  
   DOI: <https://doi.org/10.1145/3716628>  
   **Read for:** why agents need limited permissions, validation, logs, and a Human Gate.

3. **Sapkota, Roumeliotis, and Karkee (2025)** — *AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges.* Information Fusion.  
   DOI: <https://doi.org/10.1016/j.inffus.2025.103599>  
   **Read for:** clear vocabulary and the distinction between a single tool-using agent and a broader agentic workflow.

### Then read one concrete multi-agent example

4. **Swanson et al. (2025)** — *The Virtual Lab of AI Agents designs new SARS-CoV-2 nanobodies.* Nature.  
   DOI: <https://doi.org/10.1038/s41586-025-09442-9>  
   **Read for:** an example of agents with specialized roles working toward one goal. Focus on the workflow diagram, not the biology details.

### Later: deeper topics

5. **Peigné et al. (2025)** — *Multi-Agent Security Tax: Trading Off Security and Collaboration Capabilities in Multi-Agent Systems.* AAAI.  
   arXiv: <https://arxiv.org/abs/2502.19145>  
   **Read for:** the idea that adding collaboration can introduce security and coordination costs.

6. **Cao et al. (2026)** — *MemCalib: Benchmarking and Optimizing Memory Use in LLM Agents.*  
   arXiv: <https://arxiv.org/abs/2609.24259>  
   **Read for:** evaluating whether memory improves an agent's actual decisions, not merely whether it retrieves text.


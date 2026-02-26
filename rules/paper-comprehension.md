---
name: paper-comprehension
description: Phase 1 - reading the paper, extracting key fields, and identifying the story arc
metadata:
  tags: paper, comprehension, story arc, extraction, narrative, summary
---

# Phase 1: Paper Comprehension

Read the paper (tex source preferred over PDF for exact numbers) and extract the fields below.

## Required Fields

| Field | Example |
|-------|---------|
| Title | ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads? |
| Authors / Org | Lossfunk |
| Venue + Year | ICML 2026 |
| Key contributions (3-5) | Dual-metric framework, 170 GPU tasks, 4-agent evaluation |
| Headline numbers | 46.2% True Success (Claude Code, vLLM), rankings flip across codebases |
| Story arc / tension | Understanding does not equal execution - agents identify bottlenecks but fail to fix them |

## Finding the Story Arc

The story arc is the most important field. Every great paper has narrative tension. Look for:

- **Surprising results** - something counterintuitive or unexpected
- **Gaps** - difference between what should work and what does
- **Flips** - rankings or assumptions that reverse under a different lens
- **Failures** - things that do not work despite good reasons to expect them to

Frame it as a single sentence with tension: "[expected thing] but [surprising twist]".

**Examples:**
- "Bigger models should be better - but the rankings flip completely across codebases"
- "Agents understand the bottlenecks perfectly - yet they cannot fix them"
- "Thinking longer does not help - but thinking deeper does"

## Tex vs PDF

Prefer LaTeX source when available:
- Exact numbers from tables (no OCR errors)
- Author-intended emphasis and structure
- BibTeX entries for proper citations
- Figure captions with precise descriptions

For PDF-only papers, cross-check extracted numbers against multiple mentions in the text.

## Output

A summary block you will reference in all later phases. Keep it concise - one paragraph plus the table above.

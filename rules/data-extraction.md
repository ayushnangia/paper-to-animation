---
name: data-extraction
description: Phase 3 - pulling exact numbers from the paper into Python data structures with colors
metadata:
  tags: data, extraction, colors, palette, numbers, chart data
---

# Phase 3: Data Extraction

Pull exact numbers from the paper into Python-ready data structures.

## Data Format

```python
# (label, value, color)
CHART_DATA = [
    ("Agent A", 46.2, "#D4764E"),
    ("Agent B", 28.2, "#7B6CF6"),
    ("Agent C", 20.5, "#1AB394"),
]
```

For comparison/gap charts, use paired data:

```python
# (label, metric_a, metric_b)
PAIRED_DATA = [
    ("Agent A", 33, 18),
    ("Agent B", 31, 11),
    ("Agent C", 28,  8),
]
```

## Choosing Colors

See `rules/color-palettes.md` for full palette reference.

Priority order:
1. Match the paper's existing figure colors (if any)
2. Use brand colors for named entities (Anthropic terracotta, OpenAI teal, etc.)
3. Fall back to the 4-entity or 6-entity default palette

For dark backgrounds, use high fill opacity (0.85-0.95) on shapes.

## Cross-Checking Numbers

Always verify extracted numbers against multiple mentions in the paper:
- Abstract headline number
- Table cell
- In-text discussion
- Figure caption

If numbers disagree, use the table as the source of truth.

## Output

A data block ready to paste into the Manim script as module-level constants.

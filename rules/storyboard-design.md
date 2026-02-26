---
name: storyboard-design
description: Phase 2 - designing a 5-6 scene storyboard with scene archetypes and timing
metadata:
  tags: storyboard, scenes, timing, hook, setup, results, insight, closing
---

# Phase 2: Storyboard Design

Design 5-6 scenes using the storyboard template at `references/storyboard-template.md`.

## Scene Archetypes

| Archetype | Time | Purpose | Typical Tool |
|-----------|------|---------|-------------|
| **Hook** | 0-5s | Title + provocative question + counter animation | Manim |
| **Setup** | 5-10s | What was built/tested, scale of work | Manim |
| **Framework** | 10-15s | Key conceptual diagram (quadrant, pipeline, taxonomy) | Excalidraw or Manim |
| **Results** | 15-22s | Animated bar charts / tables with headline numbers | Manim |
| **Insight** | 22-27s | The "so what?" - gap, flip, comparison | Manim |
| **Closing** | 27-30s | Links, logo, credits | Manim |

Not all papers need all 6 archetypes. Adapt to the paper's story.

## Storyboard Format

Each scene entry should include:

1. **Tool** - Manim or Excalidraw
2. **Purpose** - one sentence
3. **Key elements** - what appears on screen
4. **Data** - specific numbers, labels, colors
5. **Transition** - how we get to the next scene

## Using Excalidraw MCP

Use Excalidraw MCP to sketch rough layouts for each scene before coding. This prevents wasted time on layout adjustments in code.

## Timing Guidelines

- **Social media** (Twitter/X, LinkedIn): 25-30 seconds total
- **Full explainer** (YouTube, docs): 60-90 seconds total
- Individual animations: 0.2-0.8s (keep snappy)
- Scene holds for reading: 0.3-0.8s via `self.wait()`
- Scene wipe transitions: 0.4-0.6s

## Output

A `storyboard.md` file in the working directory. See `references/storyboard-template.md` for the blank template.

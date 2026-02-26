---
name: paper-to-animation
description: |
  Trigger when: (1) User mentions "paper video", "paper animation", "explainer video", or "Manim", (2) User has a PDF or LaTeX source and wants an animated breakdown of results or key findings, (3) User wants a social media clip or promo video for a paper launch.

  Full pipeline for turning any research paper into a polished animated explainer video using Manim Community Edition. Six phases: comprehend the paper, design a storyboard, extract data, optionally build a character, generate the Manim script, and render/export.

  NOT for slide decks (use scientific-slides) or static figures (use scientific-visualization).
---

## How to use

Read individual rule files for detailed explanations and code examples:

### Pipeline Phases
- [rules/paper-comprehension.md](rules/paper-comprehension.md) - Phase 1: Read the paper, find the story arc, extract headline numbers
- [rules/storyboard-design.md](rules/storyboard-design.md) - Phase 2: Design 5-6 scenes with archetypes and timing
- [rules/data-extraction.md](rules/data-extraction.md) - Phase 3: Pull exact numbers into Python data structures with colors
- [rules/character-design.md](rules/character-design.md) - Phase 4 (optional): Build a persistent character from Manim primitives
- [rules/manim-script.md](rules/manim-script.md) - Phase 5: Generate the Manim script with scene methods and patterns
- [rules/rendering.md](rules/rendering.md) - Phase 6: Render, export GIF, iterate

### Manim Techniques
- [rules/text-rendering.md](rules/text-rendering.md) - Width-aware Pango text helper, multi-line patterns, DecimalNumber pitfalls
- [rules/color-palettes.md](rules/color-palettes.md) - Dark/light themes, AI company brand colors, chart differentiation
- [rules/scene-transitions.md](rules/scene-transitions.md) - Scene wipe patterns, persistent elements, transition timing
- [rules/common-mistakes.md](rules/common-mistakes.md) - Common pitfalls and their fixes

## Working Examples

Complete worked example demonstrating the full pipeline:

- [examples/deep-thinking-tokens/storyboard.md](examples/deep-thinking-tokens/storyboard.md) - 6-scene storyboard for "Think Deep, Not Just Long" (arXiv 2602.13517)
- [examples/deep-thinking-tokens/deep_thinking_video.py](examples/deep-thinking-tokens/deep_thinking_video.py) - Full Manim script (626 lines)
- [examples/deep-thinking-tokens/deep_thinking_video.gif](examples/deep-thinking-tokens/deep_thinking_video.gif) - Final output

## Templates & References

Copy and modify these to start new projects:

- [references/storyboard-template.md](references/storyboard-template.md) - Blank storyboard with scene archetypes
- [references/manim-scaffold.py](references/manim-scaffold.py) - Starter Scene class with txt(), scene_wipe(), pill(), glow_highlight()
- [references/ffmpeg-recipes.md](references/ffmpeg-recipes.md) - Complete ffmpeg commands for GIF, clips, thumbnails, scaling

## Quick Reference

### Checklist

**IMPORTANT: Use TaskCreate to create a task for EACH phase below.**

- [ ] Phase 1: Paper Comprehension
- [ ] Phase 2: Storyboard Generation
- [ ] Phase 3: Data Extraction
- [ ] Phase 4: Character Design (optional)
- [ ] Phase 5: Manim Script Generation
- [ ] Phase 6: Rendering & Export

### Core Principle

**Narrative first, code second.** The storyboard drives everything.

**Announce at start:** "I'm using the paper-to-animation skill to build this video."

### Script Structure

```python
from manim import *

class PaperVideo(Scene):
    def construct(self):
        self.camera.background_color = "#0d1117"
        # Scene sequence
        self.scene_1_hook()
        self.scene_wipe(target_pos=UL * 2.5)
        self.scene_2_setup()
        self.scene_wipe(target_pos=UR * 2.5)
        self.scene_3_results()
        self.scene_wipe(target_pos=DR * 2.5)
        self.scene_4_insight()
        self.scene_wipe_simple(target_pos=LEFT * 3.5)
        self.scene_5_closing()
```

### Render Commands

```bash
manim -ql script.py ClassName    # Test (480p, fast)
manim -qh script.py ClassName    # Final (1080p)
```

### GIF Export

```bash
ffmpeg -i <mp4> -vf "fps=15,scale=720:-1:flags=lanczos,split[s0][s1]; \
  [s0]palettegen=max_colors=196[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 output.gif
```

### Timing Guidelines

- Individual animations: 0.2-0.8s (keep snappy)
- `LaggedStart` lag_ratio: 0.07-0.15
- Scene holds for reading: 0.3-0.8s via `self.wait()`
- Scene wipe transitions: 0.4-0.6s
- Total: 25-35s for social media, 60-90s for full explainer

### Key Differences from ManimGL

| Feature | Manim Community (use this) | ManimGL (3b1b) |
|---------|---------------------------|----------------|
| Import | `from manim import *` | `from manimlib import *` |
| CLI | `manim` | `manimgl` |
| Creation | `Create()` | `ShowCreation()` |
| Text | `Text()`, `MathTex()` | `Text()`, `Tex()` |
| Package | `pip install manim` | `pip install manimgl` |

### Installation

```bash
pip install manim
manim checkhealth   # verify installation
```

Requires: Python 3.10+, ffmpeg, LaTeX (for MathTex)

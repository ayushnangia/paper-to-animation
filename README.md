# Paper to Animation

An [Agent Skill](https://agentskills.io) that turns research papers into animated explainer videos using Manim.

Six phases: read the paper, write a storyboard, extract data, optionally design a character, generate the Manim script, render and export.

Narrative first, code second. The storyboard drives everything.

![Deep-Thinking Tokens animation](examples/deep-thinking-tokens/deep_thinking_video.gif)

## Install

### Claude Code

```bash
claude install ayushnangia/paper-to-animation
```

### Manual

Clone into your skills directory:

```bash
git clone https://github.com/ayushnangia/paper-to-animation.git ~/.claude/skills/paper-to-animation
```

### Other agents

Copy the `SKILL.md` and `references/` directory into wherever your agent reads skills from. The format follows the open [Agent Skills spec](https://agentskills.io/specification).

## What's in here

```
SKILL.md                              # Full pipeline (6 phases)
references/
  storyboard-template.md              # Blank storyboard with scene archetypes
  manim-scaffold.py                   # Starter Scene class with txt(), scene_wipe(), pill()
  color-palettes.md                   # GitHub dark/light, AI company brand colors
  ffmpeg-recipes.md                   # GIF export, clip extraction, thumbnails
examples/
  deep-thinking-tokens/               # Worked example (arXiv 2602.13517)
    storyboard.md                     # 6-scene storyboard
    deep_thinking_video.py            # Full Manim script
    deep_thinking_video.gif           # Final output
```

## The pipeline

| Phase | What | Output |
|-------|------|--------|
| 1. Paper comprehension | Read paper, find story arc, extract headline numbers | Summary block |
| 2. Storyboard | Design 5-6 scenes with timing and tool assignments | `storyboard.md` |
| 3. Data extraction | Pull exact numbers into Python tuples with colors | Data block |
| 4. Character design | Build mascot from Manim primitives (optional) | `build_character()` |
| 5. Manim script | One Scene class, one method per scene | `.py` file |
| 6. Render and export | Test at `-ql`, final at `-qh`, GIF via ffmpeg | MP4 + GIF |

## Quick start (without an agent)

1. Read `SKILL.md` for the full workflow
2. Copy `references/storyboard-template.md` to your project and fill it in
3. Copy `references/manim-scaffold.py` as your starting script
4. Replace placeholder data with numbers from your paper
5. Render: `manim -ql script.py ClassName` (test), `manim -qh script.py ClassName` (final)

## Key patterns

**Width-aware text rendering** - The Pango scale trick renders text at Nx size then scales down for crisp kerning. But long strings at large rendered sizes hit Pango's internal line-wrap limit (~3000px), causing overlapping text. The `txt()` helper in the scaffold caps the multiplier based on string length:

```python
longest_line = max(s.split("\n"), key=len)
max_mult_for_width = 2800 / (0.70 * font_size * max(len(longest_line), 1))
mult = min(10, 400 / max(font_size, 1), max_mult_for_width)
```

**Multi-line titles** - Use separate `Text` objects in a `VGroup` instead of `\n`:

```python
t1 = self.txt("First line", font_size=42, weight=BOLD)
t2 = self.txt("Second line", font_size=42, weight=BOLD)
title = VGroup(t1, t2).arrange(DOWN, buff=0.12)
```

**Consistent label alignment** - Pin all row labels to a fixed x-coordinate:

```python
LABEL_LEFT = -5.8
label.align_to(np.array([LABEL_LEFT, 0, 0]), LEFT)
label.set_y(row_y)
```

## Example

The `examples/deep-thinking-tokens/` directory has a complete worked example for "Think Deep, Not Just Long" (arXiv 2602.13517). 6 scenes, 24 seconds, covering correlation results, the DTR method diagram, and Think@n cost comparison.

## Requirements

- Python 3.10+
- [Manim Community Edition](https://docs.manim.community/) v0.19+
- ffmpeg (for GIF export)

```bash
pip install manim
```

## License

MIT

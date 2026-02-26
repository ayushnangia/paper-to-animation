# Paper to Animation

![License](https://img.shields.io/github/license/ayushnangia/paper-to-animation?style=flat-square)

> **Quick Start:** Add this skill to your AI agent:
> ```bash
> npx skills add ayushnangia/paper-to-animation
> ```

Turn any research paper into a polished animated explainer video using **Manim Community Edition**. This repository provides battle-tested patterns, templates, and examples for the full pipeline: paper comprehension, storyboard design, data extraction, Manim script generation, and rendering.

![Deep-Thinking Tokens animation](examples/deep-thinking-tokens/deep_thinking_video.gif)

## Installation

### Prerequisites

1. **Python 3.10+**
2. **FFmpeg** - for video encoding
3. **LaTeX** - for MathTex rendering (TeX Live, MiKTeX, or MacTeX)

```bash
# Install Manim Community Edition
pip install manim

# Verify installation
manim checkhealth
```

#### FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

### Installing the Skill

#### With npx (Recommended)

```bash
npx skills add ayushnangia/paper-to-animation
```

#### With Claude Code

```bash
claude install ayushnangia/paper-to-animation
```

#### Manual

```bash
git clone https://github.com/ayushnangia/paper-to-animation.git ~/.claude/skills/paper-to-animation
```

### What are Skills?

Skills are **reusable capabilities for AI coding agents**. Once installed, your AI assistant automatically gains access to:
- Domain-specific best practices
- Working code examples
- Common patterns and pitfalls to avoid
- Step-by-step workflows

The skill follows the [Agent Skills open standard](https://agentskills.io) and works across multiple AI tools.

### When This Skill Activates

Automatically loads when:
- You mention "paper video", "paper animation", or "explainer video"
- You have a PDF or LaTeX source and want an animated breakdown
- You want a social media clip or promo video for a paper launch
- You are working with Manim and research content

## Repository Structure

```
paper-to-animation/
├── SKILL.md                              # Main skill - pipeline overview + quick reference
├── rules/                                # Individual best practice guides
│   ├── paper-comprehension.md            # Phase 1: Reading the paper
│   ├── storyboard-design.md              # Phase 2: Designing scenes
│   ├── data-extraction.md                # Phase 3: Extracting numbers + colors
│   ├── character-design.md               # Phase 4: Building a mascot (optional)
│   ├── manim-script.md                   # Phase 5: Generating the Manim script
│   ├── rendering.md                      # Phase 6: Render + export
│   ├── text-rendering.md                 # Width-aware Pango text helper
│   ├── color-palettes.md                 # Dark/light themes, brand colors
│   ├── scene-transitions.md              # Scene wipe patterns
│   └── common-mistakes.md               # Pitfalls and fixes
├── references/                           # Templates to copy and modify
│   ├── storyboard-template.md            # Blank storyboard
│   ├── manim-scaffold.py                 # Starter Scene class
│   └── ffmpeg-recipes.md                 # Complete ffmpeg commands
├── examples/
│   └── deep-thinking-tokens/             # Worked example (arXiv 2602.13517)
│       ├── storyboard.md
│       ├── deep_thinking_video.py
│       └── deep_thinking_video.gif
└── LICENSE
```

## The Pipeline

| Phase | What | Output |
|-------|------|--------|
| 1. Paper comprehension | Read paper, find story arc, extract headline numbers | Summary block |
| 2. Storyboard | Design 5-6 scenes with timing and tool assignments | `storyboard.md` |
| 3. Data extraction | Pull exact numbers into Python tuples with colors | Data block |
| 4. Character design | Build mascot from Manim primitives (optional) | `build_character()` |
| 5. Manim script | One Scene class, one method per scene | `.py` file |
| 6. Render and export | Test at `-ql`, final at `-qh`, GIF via ffmpeg | MP4 + GIF |

## Exploring the Skill

Start with these guides in `rules/`:

1. **paper-comprehension.md** - How to read a paper and find the story arc
2. **storyboard-design.md** - Scene archetypes and timing
3. **text-rendering.md** - The Pango kerning fix (most important Manim technique)
4. **manim-script.md** - Animation patterns (bar charts, counters, pills)
5. **common-mistakes.md** - Pitfalls to avoid

## Quick Start (without an agent)

1. Read `SKILL.md` for the full workflow
2. Copy `references/storyboard-template.md` to your project and fill it in
3. Copy `references/manim-scaffold.py` as your starting script
4. Replace placeholder data with numbers from your paper
5. Render: `manim -ql script.py ClassName` (test), `manim -qh script.py ClassName` (final)
6. Export GIF: see `rules/rendering.md`

## Key Patterns

**Width-aware text rendering** - Pango's kerning breaks at small pixel sizes. Render at Nx size then scale down. But long strings at large rendered sizes hit Pango's internal line-wrap limit (~3000px). The `txt()` helper caps the multiplier based on string length:

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
```

## Example

The `examples/deep-thinking-tokens/` directory has a complete worked example for "Think Deep, Not Just Long" (arXiv 2602.13517). 6 scenes, 24 seconds, covering correlation results, the DTR method diagram, and Think@n cost comparison.

## Contributing

Found an issue? Want to add a new rule or example?

1. Ensure your code example works with Manim Community Edition
2. Add it to the appropriate rule file or create a new one in `rules/`
3. Submit a pull request

## License

MIT

## Acknowledgments

### Manim Community
The dedicated team maintaining [Manim Community Edition](https://github.com/ManimCommunity/manim) - the framework that makes all of this possible.

### Grant Sanderson (3Blue1Brown)
Creator of the original Manim animation engine and the [3Blue1Brown](https://www.youtube.com/@3blue1brown) YouTube channel, whose work inspired an entirely new paradigm for mathematical visualization.

## Resources

- [Manim Community Docs](https://docs.manim.community/)
- [Manim Community Discord](https://www.manim.community/discord/)
- [Agent Skills Spec](https://agentskills.io)
- [3Blue1Brown](https://www.youtube.com/@3blue1brown)

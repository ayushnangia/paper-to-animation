---
name: paper-to-animation
description: "Use when creating an animated video explainer for a research paper. Guides the full pipeline: reading the paper, writing a storyboard, extracting key data, generating Manim scenes, and rendering to MP4/GIF. Works for any paper, not just ISO-Bench."
---

# Paper to Animation

## Overview

Transform a research paper into a polished animated explainer video using Manim Community Edition. Six phases: comprehend the paper, design a storyboard, extract data, optionally build a character, generate the Manim script, and render/export.

**Core principle:** Narrative first, code second. The storyboard drives everything.

**Announce at start:** "I'm using the paper-to-animation skill to build this video."

**Skill directory:** `~/.claude/skills/paper-to-animation/` - all `references/` paths below are relative to this directory. Read them with their full path (e.g., `~/.claude/skills/paper-to-animation/references/storyboard-template.md`).

## When to Use

- User wants an animated explainer for a research paper (any venue, any field)
- User wants a promo video / social media clip for a paper launch
- User has a paper PDF/tex and wants a Manim-based animation

**When NOT to use:**
- Slide decks or static figures (use scientific-slides or scientific-visualization)
- Non-paper content (product demos, tutorials)

## Checklist

**IMPORTANT: Use TaskCreate to create a task for EACH phase below.**

- [ ] Phase 1: Paper Comprehension
- [ ] Phase 2: Storyboard Generation
- [ ] Phase 3: Data Extraction
- [ ] Phase 4: Character Design (optional)
- [ ] Phase 5: Manim Script Generation
- [ ] Phase 6: Rendering & Export

---

## Phase 1: Paper Comprehension

Read the paper (tex source preferred over PDF for exact numbers).

**Extract these fields:**

| Field | Example |
|-------|---------|
| Title | ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads? |
| Authors / Org | Lossfunk |
| Venue + Year | ICML 2026 |
| Key contributions (3-5) | Dual-metric framework, 170 GPU tasks, 4-agent evaluation |
| Headline numbers | 46.2% True Success (Claude Code, vLLM), rankings flip across codebases |
| Story arc / tension | Understanding does not equal execution - agents identify bottlenecks but fail to fix them |

**The story arc is the most important field.** Every great paper has narrative tension - find it. This drives the video structure.

**Output:** A summary block you'll reference in all later phases.

---

## Phase 2: Storyboard Generation

Design 5-6 scenes. Use the storyboard template: `references/storyboard-template.md`

### Scene Archetypes

| Archetype | Time | Purpose | Typical Tool |
|-----------|------|---------|-------------|
| **Hook** | 0-5s | Title + provocative question + counter animation | Manim |
| **Setup** | 5-10s | What was built/tested, scale of work | Manim |
| **Framework** | 10-15s | Key conceptual diagram (quadrant, pipeline, taxonomy) | Excalidraw or Manim |
| **Results** | 15-22s | Animated bar charts / tables with headline numbers | Manim |
| **Insight** | 22-27s | The "so what?" - gap, flip, comparison | Manim |
| **Closing** | 27-30s | Links, logo, credits | Manim |

Not all papers need all 6 archetypes. Adapt to the paper's story.

**Use Excalidraw MCP** to sketch rough layouts for each scene before coding.

**Output:** `storyboard.md` file in the working directory.

---

## Phase 3: Data Extraction

Pull exact numbers from the paper into Python-ready data structures.

### Format

```python
# ── Data ──────────────────────────────────────────────────────────────
# (label, value, color)
CHART_DATA = [
    ("Agent A", 46.2, "#D4764E"),
    ("Agent B", 28.2, "#7B6CF6"),
    ("Agent C", 20.5, "#1AB394"),
]
```

### Color Palette

Use `references/color-palettes.md` for defaults. Pick a palette that matches:
1. The paper's existing figure colors (if any)
2. The target platform (dark bg for Twitter/X, light for slides)
3. Brand colors for entities in the paper

**Output:** A data block ready to paste into the Manim script.

---

## Phase 4: Character Design (Optional)

If the org has a mascot or the user wants a persistent character.

### Pattern: `build_character()` → `VGroup(core, decoration)`

```python
def build_character(h=1.4, variant="default"):
    """Build character from Manim primitives.

    ALWAYS return VGroup(core, decoration) - exactly 2 children.
    This structure is required for ReplacementTransform compatibility
    when morphing between variants.
    """
    # ... build shapes ...
    core = VGroup(shadow, outline, colored_parts, eyes)
    decoration = VGroup()  # empty for default variant
    return VGroup(core, decoration)
```

**Key patterns:**
- **Seam elimination:** `overlap = 0.06 * bw` - extend adjacent shapes slightly into each other to prevent sub-pixel gaps
- **Variant morphing:** `ReplacementTransform(old_char, new_char)` - align on `char[0].get_center()` (core center), NOT full VGroup center
- **Eye animation:** `.shift()` for gaze direction, `.stretch()` for emotion (wide = surprise, squished = daze)

**If no mascot:** Skip this phase. Use text-only transitions.

---

## Phase 5: Manim Script Generation

Start from the scaffold: `references/manim-scaffold.py`

### Script Structure

```
One Scene class
├── construct() - calls scene methods sequentially
├── txt() - static helper (Pango kerning fix)
├── scene_wipe() - transition: fade all, slide character
├── scene_wipe_simple() - transition: fade + straight slide
├── pill() - reusable pill-shaped label component
├── scene_1_hook()
├── scene_2_setup()
├── scene_3_framework()
├── scene_4_results()
├── scene_5_insight()
└── scene_6_closing()
```

### Critical Helpers

**Text with correct kerning (width-aware Pango scale trick):**
```python
FONT = "Avenir Next"

@staticmethod
def txt(s, font_size=24, color=WHITE, weight=NORMAL, **kw):
    longest_line = max(s.split("\n"), key=len)
    char_w_factor = 0.70
    max_render_px = 2800
    max_mult_for_width = max_render_px / (
        char_w_factor * font_size * max(len(longest_line), 1)
    )
    mult = min(10, 400 / max(font_size, 1), max_mult_for_width)
    mult = max(mult, 1)
    t = Text(s, font=ClassName.FONT,
             font_size=round(font_size * mult),
             color=color, weight=weight, **kw)
    t.scale(1 / mult)
    return t
```

**Multi-line text (use VGroup, not `\n`):**
```python
t1 = self.txt("First line", font_size=42, weight=BOLD)
t2 = self.txt("Second line", font_size=42, weight=BOLD)
title = VGroup(t1, t2).arrange(DOWN, buff=0.12)
```

**Scene wipe (fade everything except persistent elements):**
```python
def scene_wipe(self, target_pos=ORIGIN):
    keep = {self.character, self.logo}  # persistent elements
    others = [m for m in self.mobjects if m not in keep]
    fade_anims = [FadeOut(m, shift=DOWN * 0.2) for m in others]
    self.play(*fade_anims, self.character.animate.move_to(target_pos),
              run_time=0.5)
```

### Reusable Animation Patterns

| Pattern | Use For | Key Classes |
|---------|---------|-------------|
| Counter | Animated number reveal | `Integer` + `ChangeDecimalToValue` |
| Bar chart | Vertical bars with labels | `Rectangle` + `GrowFromEdge(bar, DOWN)` |
| Paired bars | Understanding vs execution gap | Two `RoundedRectangle` per row, light + dark |
| Pill buttons | Agent/model labels | `RoundedRectangle(corner_radius=h/2)` + `Text` |
| Quadrant grid | 2x2 framework diagram | `Line` objects animated with `Create()` |
| Glow highlight | Emphasize a bar or element | Outer `RoundedRectangle` (low opacity) + inner (high opacity) |

### Timing Guidelines

- Individual animations: 0.2-0.8s (keep snappy)
- `LaggedStart` lag_ratio: 0.07-0.15
- Scene holds (for reading): 0.3-0.8s via `self.wait()`
- Scene wipe transitions: 0.4-0.6s
- Total video: 25-35s for social media, 60-90s for full explainer

### Persistent Elements

Two objects survive scene wipes:
1. **Character** (if applicable) - slides to new position each scene
2. **Watermark/logo** - semi-transparent, bottom corner, added once in `construct()`

---

## Phase 6: Rendering & Export

### Render Commands

```bash
# Test (fast, low-res)
manim -ql script.py ClassName

# Final (1080p)
manim -qh script.py ClassName

# 4K
manim -qk script.py ClassName
```

### Export to GIF

See `references/ffmpeg-recipes.md` for the full set of commands.

**Quick recipe (Twitter-optimized GIF):**
```bash
ffmpeg -i <mp4> -vf "fps=15,scale=720:-1:flags=lanczos,split[s0][s1]; \
  [s0]palettegen=max_colors=196[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 output.gif
```

### Iteration Loop

1. Render at `-ql` (fast)
2. Check timing, colors, transitions
3. Adjust and re-render
4. When satisfied, render at `-qh` (1080p)
5. Export GIF if needed

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Text kerning broken at small sizes | Use `txt()` helper with Pango scale trick |
| Long text wraps and overlaps | Use width-aware `txt()` (caps multiplier by rendered px width). Split long titles into separate `Text` objects in a `VGroup` instead of `\n` |
| `DecimalNumber` throws TypeError with `font=` | `DecimalNumber` uses MathTex, not Pango. Do not pass `font=` to it |
| Seam lines between adjacent shapes | Add `overlap = 0.06 * bw` to extend shapes into neighbors |
| Character shifts during variant morph | Align on `char[0].get_center()` (core), not full VGroup |
| Video too long for social media | Target 25-30s max, cut Framework scene if needed |
| Bars appear with gaps at bottom | Use `GrowFromEdge(bar, DOWN)` and set bar position by bottom edge |
| Colors look washed out | Use high fill_opacity (0.85-0.95) on dark backgrounds |
| GIF file too large | Reduce `max_colors` (128-196), lower fps (12-15), scale to 720px |
| Labels misaligned across rows | Use a fixed `LABEL_LEFT` x-coordinate with `align_to(np.array([X, 0, 0]), LEFT)` for all row labels |

## Integration

- **Excalidraw MCP:** Use for rough scene sketches in Phase 2
- **references/storyboard-template.md:** Starting point for Phase 2
- **references/manim-scaffold.py:** Starting point for Phase 5
- **references/color-palettes.md:** Palette reference for Phase 3
- **references/ffmpeg-recipes.md:** Export commands for Phase 6

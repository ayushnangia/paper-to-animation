---
name: manim-script
description: Phase 5 - generating the Manim script with scene methods, helpers, and animation patterns
metadata:
  tags: manim, script, scene, construct, animation, bar chart, counter, pill
---

# Phase 5: Manim Script Generation

Start from the scaffold at `references/manim-scaffold.py`.

## Script Structure

```
One Scene class
  construct() - calls scene methods sequentially
  txt() - static helper (Pango kerning fix)
  scene_wipe() - transition: fade all, slide character
  scene_wipe_simple() - transition: fade + straight slide
  pill() - reusable pill-shaped label component
  scene_1_hook()
  scene_2_setup()
  scene_3_framework()
  scene_4_results()
  scene_5_insight()
  scene_6_closing()
```

## Persistent Elements

Two objects survive scene wipes:
1. **Character** (if applicable) - slides to a new position each scene
2. **Watermark/logo** - semi-transparent, bottom corner, added once in `construct()`

## Reusable Animation Patterns

| Pattern | Use For | Key Classes |
|---------|---------|-------------|
| Counter | Animated number reveal | `Integer` + `ChangeDecimalToValue` |
| Bar chart | Vertical bars with labels | `Rectangle` + `GrowFromEdge(bar, DOWN)` |
| Paired bars | Understanding vs execution gap | Two `RoundedRectangle` per row, light + dark |
| Pill buttons | Agent/model labels | `RoundedRectangle(corner_radius=h/2)` + `Text` |
| Quadrant grid | 2x2 framework diagram | `Line` objects animated with `Create()` |
| Glow highlight | Emphasize a bar or element | Outer `RoundedRectangle` (low opacity) + inner (high opacity) |

## Bar Chart Pattern

```python
BAR_W  = 0.82
GAP    = 0.28
MAX_H  = 3.4
BASE_Y = -2.55

for i, (name, val, col) in enumerate(CHART_DATA):
    x = start_x + i * (BAR_W + GAP)
    h = MAX_H * val / 100

    bar = Rectangle(
        width=BAR_W, height=h,
        fill_color=col, fill_opacity=0.92, stroke_width=0,
    )
    bar.move_to(np.array([x, BASE_Y + h / 2, 0]))
```

Grow from the bottom edge:
```python
self.play(
    LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.07),
    run_time=1.6,
)
```

## Pill Button Pattern

```python
def pill(self, text, color, w=2.4, h=0.48, fs=20):
    rect = RoundedRectangle(
        width=w, height=h, corner_radius=h / 2,
        fill_color=color, fill_opacity=0.22,
        stroke_color=color, stroke_width=1.5, stroke_opacity=0.9,
    )
    label = self.txt(text, font_size=fs, color=WHITE)
    return VGroup(rect, label)
```

## Label Alignment

Pin all row labels to a fixed x-coordinate for visual consistency:

```python
LABEL_LEFT = -5.8
label.align_to(np.array([LABEL_LEFT, 0, 0]), LEFT)
label.set_y(row_y)
```

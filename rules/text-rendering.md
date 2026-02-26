---
name: text-rendering
description: The width-aware Pango text helper, multi-line text patterns, and DecimalNumber pitfalls
metadata:
  tags: text, Pango, kerning, txt, font, VGroup, DecimalNumber, multi-line
---

# Text Rendering

The `txt()` helper is the foundation for all text in the animation. It fixes Pango's broken kerning at small sizes and prevents line-wrap overflow on long strings.

## The Width-Aware `txt()` Helper

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

### How It Works

1. **Pango kerning fix:** Render text at Nx the target font size, then `scale(1/N)` back down. This gives crisp vector shapes with proper letter spacing.
2. **Width cap:** Long strings at large rendered sizes hit Pango's internal line-wrap limit (~3000px). The multiplier is capped so `font_size * mult * char_count * 0.70` stays below 2800px.
3. **Font size cap:** `400 / font_size` prevents huge multipliers for already-large text.
4. **Floor at 1:** Never render smaller than the requested size.

### Parameters

| Name | Default | Purpose |
|------|---------|---------|
| `char_w_factor` | 0.70 | Average character width as fraction of font_size |
| `max_render_px` | 2800 | Stay under Pango's ~3000px wrap limit |

## Multi-Line Text

Never rely on `\n` for multi-line titles. Pango wraps inconsistently at large rendered sizes.

Instead, use separate `Text` objects in a `VGroup`:

```python
t1 = self.txt("First line", font_size=42, weight=BOLD)
t2 = self.txt("Second line", font_size=42, weight=BOLD)
title = VGroup(t1, t2).arrange(DOWN, buff=0.12)
```

## DecimalNumber Pitfall

`DecimalNumber` and `Integer` use MathTex rendering internally, not Pango. Do NOT pass `font=` to them:

```python
# WRONG - throws TypeError
num = Integer(0, font_size=96, color=YELLOW, font="Avenir Next")

# CORRECT
num = Integer(0, font_size=96, color=YELLOW)
```

## Font Selection

The scaffold defaults to `"Avenir Next"` (macOS). Good alternatives:
- `"Inter"` - widely available, clean sans-serif
- `"SF Pro"` - macOS system font
- `"Roboto"` - Linux/Android default
- `"Courier New"` - monospace for code snippets

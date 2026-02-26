# Color Palettes

## GitHub Dark Theme (Recommended for Twitter/X)

The default palette. Native-looking on dark social media feeds.

| Token | Hex | Usage |
|-------|-----|-------|
| `BG` | `#0d1117` | Scene background |
| `SURFACE` | `#161b22` | Card/panel fill |
| `BORDER` | `#30363d` | Borders, dividers, baselines |
| `WHITE` | `#e6edf3` | Primary text |
| `MUTED` | `#8b949e` | Secondary text, labels |
| `ACCENT` | `#58a6ff` | Links, highlights (blue) |
| `YELLOW` | `#f0c040` | Emphasis, counters, punchlines |
| `RED` | `#f85149` | Errors, gaps, warnings |
| `GREEN` | `#2ecc71` | Success, positive metrics |

## GitHub Light Theme

For presentations on light backgrounds.

| Token | Hex | Usage |
|-------|-----|-------|
| `BG` | `#ffffff` | Scene background |
| `SURFACE` | `#f6f8fa` | Card/panel fill |
| `BORDER` | `#d0d7de` | Borders, dividers |
| `TEXT` | `#1f2328` | Primary text |
| `MUTED` | `#656d76` | Secondary text |
| `ACCENT` | `#0969da` | Links, highlights (blue) |
| `YELLOW` | `#bf8700` | Emphasis |
| `RED` | `#cf222e` | Errors, gaps |
| `GREEN` | `#1a7f37` | Success |

## AI Company Brand Colors

Use when papers compare AI agents or models. These are adjusted for visibility on dark backgrounds.

### Anthropic (Claude)

| Variant | Hex | Notes |
|---------|-----|-------|
| Terracotta (bright) | `#D4764E` | Primary brand - good on dark bg |
| Terracotta (standard) | `#d97757` | Clawd mascot body color |
| Terracotta (muted) | `#B8624A` | For secondary elements |

### OpenAI

| Variant | Hex | Notes |
|---------|-----|-------|
| Teal-green (vivid) | `#1AB394` | Bright, reads well on dark bg |
| Green (standard) | `#10A37F` | Official OpenAI green |
| Green (dark) | `#0D8A6A` | For secondary elements |

### Google (Gemini / DeepMind)

| Variant | Hex | Notes |
|---------|-----|-------|
| Blue | `#4285F4` | Google blue |
| Red | `#DB4437` | Google red |
| Yellow | `#F4B400` | Google yellow |
| Green | `#0F9D58` | Google green |
| Gemini gradient start | `#4285F4` | Blue |
| Gemini gradient end | `#A855F7` | Purple |

### Meta (LLaMA)

| Variant | Hex | Notes |
|---------|-----|-------|
| Blue (vivid) | `#0668E1` | Meta brand blue |
| Blue (bright) | `#1877F2` | Facebook blue (legacy) |
| Purple | `#7B6CF6` | Used for Sonnet variant |

### Cohere

| Variant | Hex | Notes |
|---------|-----|-------|
| Coral | `#D18EE2` | Cohere purple-pink |
| Dark | `#39594D` | Cohere dark green |

### Mistral

| Variant | Hex | Notes |
|---------|-----|-------|
| Orange | `#F7931E` | Mistral orange |
| Blue | `#0066FF` | Mistral blue |

## Chart Differentiation

When you have 4+ entities, use colors that are maximally distinct. Tested combinations for dark backgrounds:

**4 entities (recommended):**
```python
COLORS = {
    "A": "#D4764E",  # warm terracotta
    "B": "#1AB394",  # cool teal
    "C": "#7B6CF6",  # purple
    "D": "#E6A42B",  # amber
}
```

**6 entities:**
```python
COLORS = {
    "A": "#D4764E",  # terracotta
    "B": "#1AB394",  # teal
    "C": "#7B6CF6",  # purple
    "D": "#E6A42B",  # amber
    "E": "#58a6ff",  # blue
    "F": "#f85149",  # red
}
```

## Manim Color Constants

Manim provides built-in color constants. For custom hex colors, pass the string directly:

```python
# Built-in
fill_color=YELLOW  # Manim's yellow
color=WHITE        # Manim's white

# Custom hex
fill_color="#D4764E"
color="#0d1117"
```

For fill opacity and stroke on dark backgrounds:
- **Bars / shapes:** `fill_opacity=0.85-0.95` (high, for solid fills)
- **Pill labels:** `fill_opacity=0.22`, `stroke_opacity=0.9` (frosted glass)
- **Highlights / glows:** `fill_opacity=0.06`, `stroke_opacity=0.35` (subtle)
- **Watermark logos:** `opacity=0.5-0.6` (visible but not distracting)

---
name: character-design
description: Phase 4 (optional) - building a persistent character from Manim primitives
metadata:
  tags: character, mascot, VGroup, ReplacementTransform, variant, animation
---

# Phase 4: Character Design (Optional)

Build a persistent character from Manim primitives if the org has a mascot or the user wants one.

## Core Pattern

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

The two-child `VGroup(core, decoration)` structure is critical. ReplacementTransform morphs child-by-child, so both variants must have the same number of top-level children.

## Seam Elimination

Adjacent shapes can show sub-pixel gaps at render time. Fix with overlap:

```python
overlap = 0.06 * body_width
# Extend each shape slightly into its neighbor
```

## Variant Morphing

```python
def swap_variant(self, build_fn, new_variant, run_time=0.3):
    new_char = build_fn(h=CHAR_H, variant=new_variant)
    # Align via core center (child[0]), not full VGroup center
    offset = self.character[0].get_center() - new_char[0].get_center()
    new_char.shift(offset)
    self.play(ReplacementTransform(self.character, new_char),
              run_time=run_time)
    self.character = new_char
```

Always align on `char[0].get_center()` (the core), not the full VGroup center. Decorations (hats, sparkles) change the bounding box and would shift the body if you align on the full group.

## Eye Animation

- **Gaze direction:** `.shift()` the eye group left/right/up
- **Surprise:** `.stretch(factor, dim=1)` to widen eyes vertically
- **Daze/squint:** `.stretch(0.5, dim=1)` to squish eyes

## When to Skip

If the org has no mascot and the user does not request a character, skip this phase entirely. Use text-only transitions between scenes.

---
name: scene-transitions
description: Scene wipe patterns, persistent elements, and transition timing
metadata:
  tags: scene wipe, transition, fade, persistent, character, logo, watermark
---

# Scene Transitions

## Scene Wipe

The core transition pattern. Fades out everything except persistent elements (character + logo), then slides the character to a new position.

```python
def scene_wipe(self, target_pos=ORIGIN):
    keep = set()
    if self.character:
        keep.add(self.character)
    if self.logo:
        keep.add(self.logo)

    others = [m for m in self.mobjects if m not in keep]
    fade_anims = [FadeOut(m, shift=DOWN * 0.2) for m in others]

    if self.character:
        self.play(*fade_anims,
                  self.character.animate.move_to(target_pos),
                  run_time=0.5)
    else:
        self.play(*fade_anims, run_time=0.5)
```

## Scene Wipe Simple

Same as `scene_wipe` but with a specific easing curve for a smoother feel:

```python
def scene_wipe_simple(self, target_pos=ORIGIN):
    # ... same keep/others logic ...
    self.play(
        *anims,
        rate_func=rate_functions.ease_in_out_cubic,
        run_time=0.5,
    )
```

## Persistent Elements

Two objects survive all scene wipes:

1. **Character** (optional) - built from Manim primitives, slides to a new corner or position each scene
2. **Watermark/logo** - semi-transparent `ImageMobject`, bottom corner, added once in `construct()`

```python
# In construct():
self.logo = ImageMobject(f"{ASSETS}/logo.png")
self.logo.set_height(0.6).set_opacity(0.6).to_corner(DR, buff=0.25)
self.add(self.logo)
```

## Transition Timing

| Transition | run_time | Rate Function |
|-----------|----------|---------------|
| Standard wipe | 0.5s | smooth (default) |
| Simple wipe | 0.5s | ease_in_out_cubic |
| Fast wipe (closing) | 0.3s | smooth |

## Character Positions

Common positions for the character between scenes:

```python
# Corners
UL * 2.5   # Upper left
UR * 2.5   # Upper right
DR * 2.5   # Lower right
DL * 2.5   # Lower left

# Sides
LEFT * 3.5  # Center left
RIGHT * 3.5 # Center right
```

Alternate between corners to keep the character visible but out of the way of content.

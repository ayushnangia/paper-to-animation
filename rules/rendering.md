---
name: rendering
description: Phase 6 - render commands, GIF export, ffmpeg recipes, and iteration workflow
metadata:
  tags: render, export, GIF, ffmpeg, MP4, quality, manim CLI
---

# Phase 6: Rendering & Export

## Render Commands

```bash
# Test (fast, low-res)
manim -ql script.py ClassName

# Draft (720p)
manim -qm script.py ClassName

# Final (1080p)
manim -qh script.py ClassName

# 4K
manim -qk script.py ClassName
```

| Flag | Resolution | FPS | Use |
|------|-----------|-----|-----|
| `-ql` | 854x480 | 15 | Test renders |
| `-qm` | 1280x720 | 30 | Draft |
| `-qh` | 1920x1080 | 60 | Final (recommended) |
| `-qk` | 3840x2160 | 60 | 4K (large files) |

Manim output goes to `media/videos/[script]/[quality]/` by default.

## GIF Export (Twitter-optimized)

```bash
ffmpeg -i input.mp4 \
  -vf "fps=15,scale=720:-1:flags=lanczos,split[s0][s1]; \
    [s0]palettegen=max_colors=196[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 output.gif
```

### GIF Parameters

| Parameter | Value | Why |
|-----------|-------|-----|
| `fps=15` | 15 frames/sec | Smooth enough, keeps file size down |
| `scale=720:-1` | 720px wide | Good quality for social media |
| `max_colors=196` | 196 colors | Smaller than 256 max, minimal quality loss |
| `dither=bayer` | Bayer dithering | Cleaner on flat-color animations |
| `-loop 0` | Infinite loop | Required for social media GIFs |

### GIF Variants

**Smaller file (strict size limits):**
```bash
ffmpeg -i input.mp4 \
  -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1]; \
    [s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 output_small.gif
```

**Higher quality (embedding in docs):**
```bash
ffmpeg -i input.mp4 \
  -vf "fps=20,scale=1080:-1:flags=lanczos,split[s0][s1]; \
    [s0]palettegen=max_colors=256[p];[s1][p]paletteuse=dither=sierra2_4a" \
  -loop 0 output_hq.gif
```

## Other FFmpeg Recipes

**Extract a clip:**
```bash
ffmpeg -i input.mp4 -ss 5 -to 12 -c copy scene_2.mp4
```

**Generate thumbnail:**
```bash
ffmpeg -i input.mp4 -ss 3 -frames:v 1 thumbnail.png
```

**Add fade in/out:**
```bash
ffmpeg -i input.mp4 \
  -vf "fade=t=in:st=0:d=0.5,fade=t=out:st=29.5:d=0.5" \
  -c:a copy output_faded.mp4
```

See `references/ffmpeg-recipes.md` for the complete set of recipes including concatenation, resolution scaling, frame rate adjustment, and looping.

## Iteration Workflow

1. Render at `-ql` (fast, ~15 seconds)
2. Check timing, colors, transitions
3. Adjust and re-render
4. When satisfied, render at `-qh` (1080p)
5. Export GIF if needed

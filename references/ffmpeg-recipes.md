# FFmpeg Recipes

## MP4 to GIF (Palette-Optimized)

The standard recipe for Twitter/X-ready GIFs. Two-pass with palette generation.

```bash
ffmpeg -i input.mp4 \
  -vf "fps=15,scale=720:-1:flags=lanczos,split[s0][s1]; \
    [s0]palettegen=max_colors=196[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 output.gif
```

### Parameters

| Parameter | Value | Why |
|-----------|-------|-----|
| `fps=15` | 15 frames/sec | Smooth enough, keeps file size down |
| `scale=720:-1` | 720px wide | Good quality for social media |
| `flags=lanczos` | Lanczos resampling | Sharpest downscale algorithm |
| `max_colors=196` | 196 colors | Smaller than 256 max, minimal quality loss |
| `dither=bayer` | Bayer dithering | Cleaner than Floyd-Steinberg on flat-color animations |
| `-loop 0` | Infinite loop | Required for social media GIFs |

### Variants

**Smaller file (for strict size limits):**
```bash
ffmpeg -i input.mp4 \
  -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1]; \
    [s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 output_small.gif
```

**Higher quality (for embedding in docs):**
```bash
ffmpeg -i input.mp4 \
  -vf "fps=20,scale=1080:-1:flags=lanczos,split[s0][s1]; \
    [s0]palettegen=max_colors=256[p];[s1][p]paletteuse=dither=sierra2_4a" \
  -loop 0 output_hq.gif
```

## Clip Extraction (Trim Scenes)

Extract a time range from the video:

```bash
# Extract from 5s to 12s (scene 2)
ffmpeg -i input.mp4 -ss 5 -to 12 -c copy scene_2.mp4

# Extract with re-encoding (more precise cuts)
ffmpeg -i input.mp4 -ss 5 -to 12 -c:v libx264 -crf 18 scene_2.mp4
```

## Thumbnail Generation

Extract a single frame as an image:

```bash
# Frame at 3 seconds
ffmpeg -i input.mp4 -ss 3 -frames:v 1 thumbnail.png

# Frame at 3 seconds, scaled to 1280x720
ffmpeg -i input.mp4 -ss 3 -frames:v 1 -vf "scale=1280:720" thumbnail.png
```

## Resolution Scaling

Scale video without re-encoding the audio:

```bash
# Scale to 1080p
ffmpeg -i input.mp4 -vf "scale=1920:1080:flags=lanczos" -c:a copy output_1080p.mp4

# Scale to 720p
ffmpeg -i input.mp4 -vf "scale=1280:720:flags=lanczos" -c:a copy output_720p.mp4

# Scale to 4K
ffmpeg -i input.mp4 -vf "scale=3840:2160:flags=lanczos" -c:a copy output_4k.mp4
```

## Frame Rate Adjustment

```bash
# Change to 30fps (duplicate/drop frames)
ffmpeg -i input.mp4 -r 30 output_30fps.mp4

# Change to 60fps with motion interpolation
ffmpeg -i input.mp4 -vf "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:vsbmc=1" output_60fps.mp4
```

## Concatenate Clips

Join multiple scene clips into one video:

```bash
# Create file list
cat > clips.txt << 'EOF'
file 'scene_1.mp4'
file 'scene_2.mp4'
file 'scene_3.mp4'
EOF

# Concatenate (same codec/resolution)
ffmpeg -f concat -safe 0 -i clips.txt -c copy output.mp4

# Concatenate (different codecs - re-encode)
ffmpeg -f concat -safe 0 -i clips.txt -c:v libx264 -crf 18 output.mp4
```

## Add Fade In/Out

```bash
# 0.5s fade in at start, 0.5s fade out ending at 30s
ffmpeg -i input.mp4 \
  -vf "fade=t=in:st=0:d=0.5,fade=t=out:st=29.5:d=0.5" \
  -c:a copy output_faded.mp4
```

## Loop a Short Clip

```bash
# Loop 3 times
ffmpeg -stream_loop 3 -i input.mp4 -c copy output_looped.mp4
```

## Quick Reference: Manim Render Qualities

| Flag | Resolution | FPS | Use |
|------|-----------|-----|-----|
| `-ql` | 854x480 | 15 | Test renders |
| `-qm` | 1280x720 | 30 | Draft |
| `-qh` | 1920x1080 | 60 | Final (recommended) |
| `-qk` | 3840x2160 | 60 | 4K (large files) |

Manim output goes to `media/videos/[script]/[quality]/` by default.

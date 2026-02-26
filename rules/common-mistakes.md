---
name: common-mistakes
description: Common pitfalls and their fixes when building paper animation videos with Manim
metadata:
  tags: mistakes, bugs, pitfalls, fix, kerning, seam, overlap, alignment
---

# Common Mistakes

| Mistake | Fix |
|---------|-----|
| Text kerning broken at small sizes | Use `txt()` helper with Pango scale trick (see `rules/text-rendering.md`) |
| Long text wraps and overlaps | Use width-aware `txt()` (caps multiplier by rendered px width). Split long titles into separate `Text` objects in a `VGroup` instead of `\n` |
| `DecimalNumber` throws TypeError with `font=` | `DecimalNumber` uses MathTex, not Pango. Do not pass `font=` to it |
| Seam lines between adjacent shapes | Add `overlap = 0.06 * bw` to extend shapes into neighbors |
| Character shifts during variant morph | Align on `char[0].get_center()` (core), not full VGroup |
| Video too long for social media | Target 25-30s max, cut Framework scene if needed |
| Bars appear with gaps at bottom | Use `GrowFromEdge(bar, DOWN)` and set bar position by bottom edge |
| Colors look washed out | Use high fill_opacity (0.85-0.95) on dark backgrounds |
| GIF file too large | Reduce `max_colors` (128-196), lower fps (12-15), scale to 720px |
| Labels misaligned across rows | Use a fixed `LABEL_LEFT` x-coordinate with `align_to(np.array([X, 0, 0]), LEFT)` for all row labels |
| Manim `Text` constructor hangs | Check that the font name is valid and installed on the system. Try `"Courier New"` as a fallback |
| `GrowFromEdge` animates from wrong edge | Ensure bar is positioned so its bottom edge is at the baseline, then use `GrowFromEdge(bar, DOWN)` |
| Elements overlap after scene wipe | `scene_wipe()` only fades `self.mobjects` - if you stored references but removed from scene, they will not be faded. Always let wipe handle cleanup |

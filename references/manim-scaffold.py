"""Paper Explainer Video - Scaffold
Manim Community Edition v0.19+

Replace [PAPER_NAME] and fill in scene methods.

Render:
  Test:   manim -ql script.py PaperVideo
  Final:  manim -qh script.py PaperVideo
  4K:     manim -qk script.py PaperVideo

GIF:
  ffmpeg -i <mp4> -vf "fps=15,scale=720:-1:flags=lanczos,split[s0][s1]; \
    [s0]palettegen=max_colors=196[p];[s1][p]paletteuse=dither=bayer" \
    -loop 0 output.gif
"""

from manim import *
import numpy as np

# ── Palette (GitHub Dark Theme) ───────────────────────────────────────
BG      = "#0d1117"
SURFACE = "#161b22"
BORDER  = "#30363d"
WHITE   = "#e6edf3"
MUTED   = "#8b949e"
ACCENT  = "#58a6ff"   # blue link
YELLOW  = "#f0c040"
RED     = "#f85149"
GREEN   = "#2ecc71"

# ── Paper-Specific Colors ─────────────────────────────────────────────
# Replace with your paper's entity colors
COLORS = {
    "Entity A": "#D4764E",
    "Entity B": "#1AB394",
    "Entity C": "#7B6CF6",
    "Entity D": "#E6A42B",
}

# ── Data (from paper) ────────────────────────────────────────────────
# Format: (label, value, color)
CHART_DATA = [
    ("Entity A", 46.2, COLORS["Entity A"]),
    ("Entity B", 28.2, COLORS["Entity B"]),
    ("Entity C", 20.5, COLORS["Entity C"]),
    ("Entity D", 17.9, COLORS["Entity D"]),
]

# ── Optional: paired data for gap/comparison charts ──
# Format: (label, metric_a, metric_b)
PAIRED_DATA = [
    ("Entity A", 33, 18),
    ("Entity B", 31, 11),
    ("Entity C", 28,  8),
    ("Entity D", 34,  7),
]

# ── Assets ────────────────────────────────────────────────────────────
ASSETS = "assets"  # adjust path to your logo/image directory

# Character height (if using a persistent character)
CHAR_H = 1.4


class PaperVideo(Scene):
    """Animated paper explainer - replace with your paper name.

    Structure:
    - One persistent character (optional) lives for the entire video
    - Scene transitions use scene_wipe() to fade everything except
      the character and watermark logo
    - Each scene is a method called sequentially from construct()
    """

    def construct(self):
        self.camera.background_color = BG

        # ── Persistent character (optional - remove if not using) ──
        # self.character = build_character(h=CHAR_H, variant="default")
        # self.character.to_corner(UL, buff=0.45)
        # self.add(self.character)
        self.character = None  # set to None if no character

        # ── Persistent watermark logo (optional) ──
        # self.logo = ImageMobject(f"{ASSETS}/logo.png")
        # self.logo.set_height(0.6).set_opacity(0.6).to_corner(DR, buff=0.25)
        # self.add(self.logo)
        self.logo = None  # set to None if no logo

        # ── Scene sequence ──
        self.scene_1_hook()
        self.scene_wipe(target_pos=UL * 2.5)
        self.scene_2_setup()
        self.scene_wipe(target_pos=UR * 2.5)
        self.scene_3_results()
        self.scene_wipe(target_pos=DR * 2.5)
        self.scene_4_insight()
        self.scene_wipe_simple(target_pos=LEFT * 3.5)
        self.scene_5_closing()

    # ── Utilities ─────────────────────────────────────────────────────

    FONT = "Avenir Next"  # replace with your preferred font

    @staticmethod
    def txt(s, font_size=24, color=WHITE, weight=NORMAL, **kw):
        """Render text with correct kerning (Pango scale trick).

        Pango's kerning breaks at small pixel sizes. Render at Nx the
        target size, then scale down for crisp vector shapes with
        proper letter spacing.

        The multiplier is also capped so (font_size * mult * char_count)
        stays below Pango's internal line-wrap width (~3000px). Without
        this cap, long strings at large rendered sizes wrap prematurely
        and overlap when scaled back down.

        For long titles, split into separate Text objects in a VGroup
        instead of relying on newlines:

            t1 = self.txt("First line", font_size=42, weight=BOLD)
            t2 = self.txt("Second line", font_size=42, weight=BOLD)
            title = VGroup(t1, t2).arrange(DOWN, buff=0.12)
        """
        longest_line = max(s.split("\n"), key=len)
        char_w_factor = 0.70          # avg char width as fraction of font_size
        max_render_px = 2800          # stay under Pango's ~3000px wrap limit
        max_mult_for_width = max_render_px / (
            char_w_factor * font_size * max(len(longest_line), 1)
        )
        mult = min(10, 400 / max(font_size, 1), max_mult_for_width)
        mult = max(mult, 1)           # never go below 1x
        t = Text(s, font=PaperVideo.FONT,
                 font_size=round(font_size * mult),
                 color=color, weight=weight, **kw)
        t.scale(1 / mult)
        return t

    def pill(self, text, color, w=2.4, h=0.48, fs=20):
        """Pill-shaped label - frosted glass effect on dark background."""
        rect = RoundedRectangle(
            width=w, height=h, corner_radius=h / 2,
            fill_color=color, fill_opacity=0.22,
            stroke_color=color, stroke_width=1.5, stroke_opacity=0.9,
        )
        label = self.txt(text, font_size=fs, color=WHITE)
        return VGroup(rect, label)

    def scene_wipe(self, target_pos=ORIGIN):
        """Fade out everything except character + logo, slide character."""
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

    def scene_wipe_simple(self, target_pos=ORIGIN):
        """Wipe + straight-line slide to target position."""
        keep = set()
        if self.character:
            keep.add(self.character)
        if self.logo:
            keep.add(self.logo)

        others = [m for m in self.mobjects if m not in keep]
        fade_anims = [FadeOut(m, shift=DOWN * 0.2) for m in others]

        anims = fade_anims[:]
        if self.character:
            anims.append(self.character.animate.move_to(target_pos))

        self.play(
            *anims,
            rate_func=rate_functions.ease_in_out_cubic,
            run_time=0.5,
        )

    def swap_variant(self, build_fn, new_variant, run_time=0.3):
        """Morph character to a new variant via ReplacementTransform.

        Requires: self.character is not None, build_fn is a function like
        build_character(h, variant) that returns VGroup(core, decoration).

        Aligns by core center (child[0]) so decorations don't shift the body.
        """
        if not self.character:
            return
        new_char = build_fn(h=CHAR_H, variant=new_variant)
        # Align via core center to avoid decoration bbox drift
        offset = self.character[0].get_center() - new_char[0].get_center()
        new_char.shift(offset)
        self.play(ReplacementTransform(self.character, new_char),
                  run_time=run_time)
        self.character = new_char

    def glow_highlight(self, mobject, color=YELLOW):
        """Create a glow highlight around a mobject (typically a bar)."""
        outer = RoundedRectangle(
            width=mobject.width + 0.22, height=mobject.height + 0.22,
            corner_radius=0.06,
            stroke_color=color, stroke_width=4, stroke_opacity=0.35,
            fill_color=color, fill_opacity=0.06,
        ).move_to(mobject.get_center())
        inner = RoundedRectangle(
            width=mobject.width + 0.06, height=mobject.height + 0.06,
            corner_radius=0.04,
            stroke_color=color, stroke_width=2.5, stroke_opacity=0.9,
            fill_opacity=0,
        ).move_to(mobject.get_center())
        return VGroup(outer, inner)

    # ── Scene 1: Hook ─────────────────────────────────────────────────

    def scene_1_hook(self):
        """Title + provocative question + animated counter."""
        # Title
        title = self.txt("[Paper Title]", font_size=48, weight=BOLD)
        title.move_to(UP * 1.5)
        self.play(FadeIn(title, shift=DOWN * 0.2), run_time=0.6)

        # Animated counter
        num = Integer(0, font_size=96, color=YELLOW)
        label = self.txt("[what the number represents]", font_size=28)
        num.move_to(DOWN * 0.5)
        label.next_to(num, DOWN, buff=0.15)

        self.play(
            ChangeDecimalToValue(num, 170,  # replace with your number
                                 rate_func=rate_functions.ease_out_cubic),
            FadeIn(label, shift=LEFT * 0.2),
            run_time=1.0,
        )
        self.wait(0.5)

    # ── Scene 2: Setup ────────────────────────────────────────────────

    def scene_2_setup(self):
        """What was built / tested. Entity labels + scale."""
        heading = self.txt("[Entities evaluated]", font_size=22, color=MUTED)
        heading.move_to(UP * 2.5)

        pills = VGroup(*[
            self.pill(name, color, w=2.3, h=0.42, fs=17)
            for name, color in COLORS.items()
        ]).arrange(RIGHT, buff=0.25).move_to(ORIGIN)

        self.play(
            FadeIn(heading),
            LaggedStart(
                *[FadeIn(p, shift=UP * 0.15) for p in pills],
                lag_ratio=0.12,
            ),
            run_time=0.9,
        )
        self.wait(0.8)

    # ── Scene 3: Results ──────────────────────────────────────────────

    def scene_3_results(self):
        """Animated bar chart with headline numbers."""
        BAR_W  = 0.82
        GAP    = 0.28
        MAX_H  = 3.4
        BASE_Y = -2.55

        n = len(CHART_DATA)
        total_w = n * BAR_W + (n - 1) * GAP
        start_x = -total_w / 2 + BAR_W / 2

        bars = VGroup()
        labels = VGroup()
        values = VGroup()

        for i, (name, val, col) in enumerate(CHART_DATA):
            x = start_x + i * (BAR_W + GAP)
            h = MAX_H * val / 100

            bar = Rectangle(
                width=BAR_W, height=h,
                fill_color=col, fill_opacity=0.92, stroke_width=0,
            )
            bar.move_to(np.array([x, BASE_Y + h / 2, 0]))

            lbl = self.txt(name, font_size=17, color=MUTED)
            lbl.move_to(np.array([x, BASE_Y - 0.55, 0]))

            vtxt = self.txt(f"{val}%", font_size=19, weight=BOLD)
            vtxt.next_to(bar, UP, buff=0.07)

            bars.add(bar)
            labels.add(lbl)
            values.add(vtxt)

        baseline = Line(
            start=np.array([-total_w / 2 - 0.3, BASE_Y, 0]),
            end=np.array([total_w / 2 + 0.3, BASE_Y, 0]),
            color=BORDER, stroke_width=1.5,
        )

        # Title
        sec = self.txt("[Chart Title]", font_size=26, color=MUTED)
        sec.move_to(UP * 3.2)

        # Animate
        self.play(FadeIn(sec), Create(baseline), run_time=0.5)
        self.play(*[FadeIn(l) for l in labels], run_time=0.3)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.07),
            LaggedStart(*[FadeIn(v, shift=DOWN * 0.08) for v in values],
                         lag_ratio=0.07),
            run_time=1.6,
            rate_func=rate_functions.ease_out_cubic,
        )
        self.wait(0.8)

    # ── Scene 4: Insight ──────────────────────────────────────────────

    def scene_4_insight(self):
        """The 'so what?' - key takeaway with punchline text."""
        # Replace with your paper's key insight visualization
        punchline = self.txt(
            "[Key Insight Here]",
            font_size=36, color=YELLOW, weight=BOLD,
        )
        punchline.move_to(ORIGIN)

        self.play(FadeIn(punchline, scale=0.85), run_time=0.6)
        self.wait(1.0)

    # ── Scene 5: Closing ──────────────────────────────────────────────

    def scene_5_closing(self):
        """Links, logo, credits."""
        title = self.txt("[Paper Title]", font_size=64, weight=BOLD)
        sub = self.txt("[Organization]", font_size=32, color=MUTED)
        tg = VGroup(title, sub).arrange(DOWN, buff=0.3).move_to(UP * 0.8)

        link1 = self.txt("github.com/[org]/[repo]", font_size=26, color=ACCENT)
        link2 = self.txt("arxiv.org/abs/[id]", font_size=26, color=YELLOW)
        links = VGroup(link1, link2).arrange(DOWN, buff=0.25).move_to(DOWN * 1.5)

        self.play(
            FadeIn(tg, shift=DOWN * 0.2),
            FadeIn(links, shift=UP * 0.15),
            run_time=0.7,
        )
        self.wait(1.5)

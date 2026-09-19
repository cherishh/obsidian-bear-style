# Typography calibration

Measured on 2026-09-19 against the installed macOS Bear app, using the same synthetic English/Chinese note. These values match that setup, not every possible Bear configuration.

Bear settings: BearSansUI-Regular body, BearSansUIHeading-Regular headings, 15pt text, line-height setting 1.5, line-width setting 56.5, paragraph spacing 0, paragraph indentation 0. Obsidian: default theme, 15px text, matching locally installed fonts.

## Method

Use original-resolution macOS window screenshots at 2×, measure repeated text rows and glyph bounds, and compare with Obsidian's actual DOM rectangles and computed styles. CoreText font metrics provide an independent check of heading sizes. Do not compare screenshots scaled to different display sizes.

Bear's line-height setting is not a CSS multiplier: its 1.5 setting produces a measured 27pt baseline interval at 15pt. Keep the CSS line height at 1.8, which produces the same 27px interval.

## Changes

| Property | Previous snippet | Calibrated snippet |
| --- | --- | --- |
| Body / tight-list row interval | 27px / 29.25px | 27px / 27px |
| H1–H6 sizes at 15px base | 27, 21.93, 19.77, 17.82, 16.14, 15px | 30, 24, 19, 15, 15, 15px |
| Heading face | Body font, with heading font only as fallback | Optional local Bear heading face |
| Heading tracking | Obsidian's negative tracking | Normal tracking |
| Extra editor heading padding | 15px | 0; Markdown blank lines supply separation |
| Reading paragraph gap | 15px | 27px, matching an editor blank line |
| Light-mode note text | #222 | #444 |
| Reading/editor quote text | Muted | Same color as body text |
| Quote text inset | About 12px | 33px per level |
| Quote rule | 4px | 4px with rounded ends |
| Text column | 700px | 772.5px at 15px, approximating the measured Bear column |

The local heading font alias maps Bear's already-heavy `Heading Regular` face to semantic weight 600. Systems without that font fall back to a semibold text font. No fonts are bundled or downloaded.

## Verification and limits

- Verified live preview and reading-mode paragraph geometry, heading sizes, and list row intervals.
- Verified long bullets, nested bullets, and three-digit numbered items retain hanging indents. Obsidian rounds hanging indents to whole pixels, leaving less than 1px variation between the first and wrapped lines in the sample.
- Verified fresh-editor nested quotations use 66px for two levels, including wrapped text.
- Checked dark-mode computed colors; the snippet retains the active theme's light text instead of imposing #444.
- Verified the existing cursor plugin still renders a 2px cursor: 27px high in body text and 54px in H1, with the system caret hidden while the replacement is present.

This is a typographic approximation, not a pixel-identical renderer. Native Bear and Chromium still distribute heading baselines/leading differently; heading-to-neighbor spacing can differ by several pixels even with matching font sizes and overall block height. Callouts, code blocks and application chrome retain the project's existing choices. Dark mode has not been visually calibrated against Bear, and IME/RTL/mobile behavior was not part of this pass.

After changing prefix widths while Obsidian is already running, reopen a note (or restart Obsidian) if its cached hanging indents still use the old measurements. Change `--bear-line-width` to keep a narrower column if preferred.

## Color and link follow-up

The installed Bear preference `SFAppThemeName` is `Red Graphite`. Its bundled
`BearCore.framework/Versions/A/Resources/Red Graphite.theme` is readable JSON,
which provides exact theme values independently of screenshot color management:

- Editor background: `#FFFFFF`, inherited from the base background.
- Secondary background: `#F3F5F7` (auxiliary surfaces, not the writing page).
- Default fluorescent highlight: `#D3FFA4`, with text `#1A3200`.
- Bear's separately named green highlight is `#CDF7BD`; the requested reference
  screenshot uses the default fluorescent highlight, so `hltr-green` deliberately
  maps to the default color above.

The supplied screenshot's dominant highlight pixel is `#D3FFA3`, within one
channel value of the theme's exact `#D3FFA4`; use the source value. Its page
background and Obsidian's computed page background are both white. No gray page
background override was added.

The snippet now renders its own decorative pencil with a 0.3em gap on each side and 0.85em
icon size after external links in reading mode and live preview. The icon is an
original SVG approximation, not an extracted Bear asset. Link navigation behavior
is unchanged; the icon does not add Bear's link-editing interaction.

## Accent, nested markers and quote rules

The same theme source defines the accent as `#DD4C4F`; editor links, cursor and
list markers all refer to it. Replace the earlier hand-picked `#CD5853` in the
snippet, native Obsidian accent setting, and standalone cursor fallback.

Unordered-list markers follow a four-level cycle: filled circle, ring, filled
diamond, outline diamond. Verified two full cycles (eight levels) in live preview
and reading mode. Reading mode calculates depth through its list DOM. The editor
exposes class names rather than nested elements, so CSS maps depths 1–32 explicitly.
Ordered numbers and task checkboxes retain their normal behavior. This uses CSS
`mod()` and `round()`, verified in Obsidian 1.13.7's installed Chromium engine.

Quote rules are 4px wide with 2px end radii. In live preview, consecutive quote
lines form a continuous rule: only the first line has rounded top corners and only
the last line has rounded bottom corners. Reading mode draws one rounded rule for
the whole block. Nested quote levels that start/end within an outer block retain
its continuation-end logic; their caps are not independently calibrated.

## Quote-width correction and indentation guides

A fresh native Bear window capture was 1676 pixels wide for an 838pt window (2×).
The quote rule occupies eight consecutive physical-pixel columns (132–139), so
its width is **4pt**, corresponding to **4 CSS px** in Obsidian at 100% zoom. The
earlier 3px estimate was incorrect; the final snippet uses 4px with 2px end radii.

Both normal and active note indentation-guide widths are now 0px, scoped to the
Markdown editor and reading view. This removes the gray nested-list guides without
changing list indentation, markers, folding controls or file-explorer styling.

## Completed tasks

Completed text uses `#888888`, matching Red Graphite's secondary text color and
the solid glyph pixels in the supplied native Bear screenshot. The completed
checkbox stays unfilled, with an approximately `#D5D5D5` border and `#B4B4B4` check
sampled from that screenshot; these two values are visual matches, not named
completed-state tokens from the theme. Automatic completed-task strikethrough is disabled, matching Bear. Rules apply only to note task checkboxes, with a darker hover/focus
border and the existing keyboard focus ring. Dark mode uses theme-relative grays.

## List indentation, checkbox geometry and tables

The demo uses two spaces per unordered-list level and three for its nested
ordered list. Obsidian groups indentation guides in four-space chunks; the
remaining whitespace was only 8px or 12px wide, causing alternating 8px/25px
steps instead of 33px. Live preview now sizes the existing indentation span from
`HyperMD-list-line-N` (levels 1–32), using `(N - 1) * 2.2em`. The editor measures
that span for wrapped lines. Markdown is unchanged, raw source mode retains
literal whitespace, and continuation lines without a marker retain their native
layout. Eight nested levels and the nested ordered list were checked at 15px:
each step is 33px; wrapped text retains the editor's subpixel rounding (<1px).

A native 1676×2100 capture of an 838×1050pt Bear window gives a 2× scale. The
unchecked checkbox's vertical edges occupy three solid pixel columns (118–120
and 151–153), proving a 1.5pt stroke, rather than 2pt. Its outer width is 36
physical pixels (18pt). The completed checkbox has a one-pixel solid center and
two half-coverage edge pixels: a 1pt stroke at a half-pixel position. Use 18px
note checkboxes at 15px text, 1.5px unchecked borders in `#888888`, and keep the
1px completed border and gray check, without an automatic strikethrough.

Tables use Red Graphite's `#F3F5F7` alternate background and `#D9D9D9` strokes.
The header and alternating body rows are shaded; only the outer border and
vertical column rules remain. At 15px text the 27px line height plus 6px top/bottom
padding yields 39px single-line rows, matching the native reference. Horizontal
padding is 12px, with subtle 3px outer corners. Columns default to centered text;
explicit Markdown alignment still wins. Column widths remain content-driven,
and Obsidian's table editor and drag controls are preserved. This is a CSS visual
approximation, not a replacement for Bear's native table behavior.

## Horizontal rules

Obsidian defaults to a 2px horizontal rule. Note views now use 1px for a finer
appearance, with `#D9D9D9` from Red Graphite's `editor.separator.border color`
(reference to `base.stroke color`). The width is a visual adjustment, not a
measured native Bear value. Dark mode uses the active theme's border color.
Application dividers and Markdown source text remain unchanged.

# Changelog

## Unreleased

- Add Bear Dark Graphite dark mode with native Bear colors for text, headings, links, highlights, code, tables, and interface surfaces. Adapt optional Code Styler backgrounds and Highlightr classes while preserving the light palette.

## 1.1.4 — 2026-09-20

- Update the optional Bear Cursor plugin to 1.0.1. Fix a visually misplaced caret after pasting wrapped text into a new quote by redrawing after Obsidian adjusts the hanging indent.
- Lighten strikethrough text and increase the fourth-level heading size.
- Existing Bear Cursor users must replace the plugin files from the full ZIP and reload the plugin; updating the theme alone does not update the optional cursor plugin.

## 1.1.3 — 2026-09-20

- Show the external-link icon after bare URLs in Live Preview, matching Markdown links without adding duplicate icons to their destinations.

## 1.1.2 — 2026-09-20

- Style HTML underlines with the Bear accent color and a 2px underline offset, preserving the text color.

## 1.1.1 — 2026-09-20

- Replace decorative pencil icons after external links with an external-link arrow, preserving the existing color, size, spacing, and link behavior.

## 1.1.0 — 2026-09-19

- Add the standalone Bear Style theme, generated from the shared snippet, with a theme manifest, release assets, official CSS lint checks, and an English market cover. Keep plugin/font requirements explicit and preserve the snippet installation option.

- Refresh English and Chinese full-page screenshots and cursor close-ups with the calibrated styles, captured at 2× resolution.

- Add a small trailing gap after external-link pencil icons so adjacent text does not touch the icon.

- Use thin 1px Markdown separators in Bear Red Graphite's `#D9D9D9`, in live preview and reading mode.

- Fix uneven live-preview list indentation by using parsed list depth instead of four-space groups; match Bear checkbox border widths and add striped, padded tables with vertical rules.

- Style completed tasks with gray text and an unfilled gray checkbox, without automatic strikethrough in live preview and reading mode.

- Remove gray note indentation guides. Correct the quote rule to 4px (8 physical pixels in a native 2× Bear capture), with 2px end radii.

- Use Bear Red Graphite's exact accent `#DD4C4F`, cycle nested unordered-list markers through filled circle / ring / filled diamond / outline diamond, and add rounded ends to the 4px quote rules.

- Match the green highlight to Bear Red Graphite (`#D3FFA4` background, `#1A3200` text), and replace external-link arrows with spaced decorative pencil icons.

- Calibrate typography against native macOS Bear: heading fonts, sizes and tracking; paragraph and list spacing; note text color; and quote geometry. Preserve the measured 27px body line spacing and 2px cursor. See `docs/typography-calibration.md` for measurements and limits.

- Add original English and Chinese cursor close-ups to the corresponding READMEs.

## 1.0.1 — 2026-09-18

- Replace five partial screenshots with one full-length native 2× screenshot per README language.
- Add a Chinese demo note and illustration, with a Chinese screenshot in the Chinese README.
- Include both language demos and the agent installation guide in the download. Package versioning is independent of the unchanged Bear Cursor 1.0.0 plugin.

- Add short English and Chinese agent installation prompts, backed by a detailed INSTALL.md guide covering the full demo setup, font exclusions, backups, repeat runs, and verification.

## 1.0.0 — 2026-09-17

- First public release of the Bear-inspired default-theme CSS snippet.
- Optional desktop Bear Cursor plugin with a red 2px caret, line-height sizing, reduced-motion support, and native-caret fallback.
- English formatting demo, an original SVG illustration, and real Obsidian screenshots.
- English and Chinese installation guides, optional plugin setup, and compatibility notes.

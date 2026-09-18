# Obsidian Bear Style

A quiet space to write. Bear-inspired typography, warm red accents, generous spacing, and an optional red **2px caret** for Obsidian.

[中文说明](README.zh-CN.md) · [Download](https://github.com/cherishh/obsidian-bear-style/releases/latest) · [Demo note](examples/Bear%20Style%20Demo.md)

This is a **CSS snippet for Obsidian's default theme**, plus a small optional desktop cursor plugin. It is not a standalone community theme. The snippet works without community plugins.

> **About the preview:** this is a full-length capture of the included English demo in Obsidian. Matching it closely also depends on fonts, **Highlightr** for colored highlights, and **Code Styler** for code blocks. The optional **Bear Cursor** adds a thick red caret while editing. See [Match the screenshots](#match-the-screenshots); installing the CSS alone will not reproduce every detail.

## Install with your AI agent

Copy this into an agent with access to your local files and Obsidian, such as Codex or Claude Code:

```text
Install the full Obsidian Bear Style setup in my vault: CSS, Bear Cursor,
Highlightr, Code Styler, and the demo note. Follow this guide:
https://raw.githubusercontent.com/cherishh/obsidian-bear-style/main/INSTALL.md

Back up changes, preserve my notes and unrelated settings, and verify the result.
Don't install fonts; explain how that affects the appearance.
Ask for my vault path if needed, and tell me if anything requires my help.
```

The agent reads the [detailed installation guide](INSTALL.md), so you don't have to copy it. For CSS only, use the [manual steps](#install-the-style).

## Preview

![Full English demo in Obsidian: headings, text, lists, tasks, quotes, highlights, code, table, and image](docs/images/demo-en.png)

## Install the style

1. Download **`obsidian-bear-style-v1.0.1.zip`** from [Releases](https://github.com/cherishh/obsidian-bear-style/releases/latest) and extract it.
2. In Obsidian, choose the **Default** theme under **Settings → Appearance**.
3. Under **CSS snippets**, click the folder button. Copy `snippets/bear.css` into that folder.
4. Return to Obsidian, reload the snippet list if needed, and enable **bear**.
5. Set **Appearance → Accent color** to **`#cd5853`**. Use a **15px** text size as a starting point.

No build step, package manager, or theme settings plugin is needed. See Obsidian's [official CSS snippet instructions](https://help.obsidian.md/snippets).

### Optional: the red 2px caret

1. Copy the entire `plugins/bear-cursor` folder from the download to `<your vault>/.obsidian/plugins/bear-cursor/`.
2. Confirm it contains `manifest.json`, `main.js`, and `styles.css` directly inside that folder.
3. Reload Obsidian. Under **Settings → Community plugins**, enable community plugins if needed, then enable **Bear Cursor**.

Bear Cursor is manually installed from this repository; it is not listed in the community plugin directory and does not have automatic updates. For updates, disable it, replace those three files, reload Obsidian, then enable it again.

The plugin uses CodeMirror's editor layer API to draw the primary caret. It follows the current line height, fades gently, and respects reduced-motion preferences. It makes no network requests and stores no settings. Text selections and secondary cursors remain under Obsidian's control.

Without the plugin, the snippet still colors the native caret red; the operating system controls its width. Disable any other cursor replacement plugin and remove old CSS that hides the native caret.

## Match the screenshots

The preview uses **Obsidian 1.13.7 on macOS**, the **Default** theme in **light mode**, and this snippet. It shows Reading view, so the editing caret is not visible. No third-party plugin code, fonts, or personal vault configuration is bundled.

| Component | What it contributes | Setup used here |
| --- | --- | --- |
| `bear.css` | Heading scale, spacing, list markers, quote text, rounded highlights, image borders, and caret color | Included; enable **bear** |
| [Bear Cursor](plugins/bear-cursor/README.md) | The red 2px primary caret | Included; version 1.0.0; desktop only |
| [Highlightr](https://github.com/chetachiezikeuzor/Highlightr-Plugin) | Green and pink highlights, plus commands to create them | Version 1.2.2; **CSS classes** method, **rounded** style; Green `#BBFABBA6`, Pink `#FFB8EBA6` |
| [Code Styler](https://github.com/mayurankv/Obsidian-Code-Styler) | Code block line numbers, syntax colors, and language border | Version 1.1.7; see settings below |
| Text font | Letter shapes and line wrapping | `Bear Sans UI, Bear Sans UI Heading`, 15px; fonts are **not included** |
| Monospace font | Code letter shapes | `Fira Code, Roboto Mono`; fonts are **not included** |
| Obsidian appearance | Task checkboxes and other native accents | Accent `#cd5853`, readable line length on |

Install **Highlightr** and **Code Styler** separately through Obsidian's community plugin browser. They are optional: basic Markdown highlights and code blocks still work without them. The demo's `<mark class="hltr-green">` and `hltr-pink` colors require Highlightr's corresponding classes.

For Code Styler, the screenshot setup uses the **Default** preset with line numbers enabled, code block radius **4px**, language border enabled at **4px**, language tag and icon hidden, and inline-code styling disabled. Other settings use the plugin defaults. Later plugin versions may render differently.

Use fonts already available on your system, or select your own. Without the same fonts, the style still works, but text metrics and wrapping will differ. This project does not distribute Bear's fonts or instructions for extracting them. It is an independent project inspired by [Bear](https://bear.app), not affiliated with or endorsed by Bear or Obsidian.

**Ninja Cursor, Minimal Theme Settings, and Style Settings are not required.**

## Try the demo

For English, copy **Bear Style Demo.md** and **quiet-space.svg** from `examples/` into the same folder in your vault. For Chinese, use **Bear 风格演示.md** and **quiet-space-zh.svg** instead. Open your chosen note in Obsidian; keep its matching SVG beside it so the relative image reference resolves.

The demo covers headings H1–H6, bold, italics, strikethrough, links, highlights, eight nested list levels, numbered lists, checkboxes, blockquotes, a callout, inline code, a fenced code block, a table, and an image. It contains only sample text.

## Make it yours

Edit the `--bear-*` variables near the top of `snippets/bear.css`:

```css
--bear-accent: #cd5853;
--bear-line-height: 1.8;
--bear-line-width: 700px;
--bear-paragraph-spacing: 1rem;
--bear-caret-width: 2px;
```

Keep line-height variables **unitless** (for example, `1.8`, not `1.8em`): plugins can multiply them by a font size. If you change the accent, also update Obsidian's Accent color setting for native controls.

Fonts and base font size stay in Obsidian's Appearance settings. The snippet adjusts muted text and image borders in dark mode while retaining the default theme's background and foreground colors.

## Compatibility & limits

- Tested with **Obsidian 1.13.7 on macOS** and the default theme. Other themes may override these rules.
- Checked in Live Preview and Reading view: heading sizes, lists, quotes, highlights, images, and code layout. The caret was checked in body text, at heading starts, after links, and beside numbered list markers, including native fallback when disabled.
- Dark-mode variable behavior was checked; the screenshots show light mode. Windows, Linux, and physical mobile devices have not been tested.
- The cursor plugin requires **Obsidian 1.13.7 or later** and is **desktop only**. Mobile retains its native caret. Later Obsidian versions are not automatically guaranteed compatible.
- The plugin is designed to leave composition and Vim mode to the editor; IME candidate-window behavior and Vim mode have not been fully tested.

To uninstall, disable the **bear** snippet, then delete its CSS file. Disable **Bear Cursor** before deleting its plugin folder. Remove optional third-party plugins only if you no longer use their features. No note content needs to be changed.

## Development

The shipped JavaScript is the source: it imports Obsidian and CodeMirror from the host application, so no bundler is needed. Build the download with Python 3:

```sh
python3 scripts/package.py
```

The packager includes only explicitly listed public files. For bug reports, include your Obsidian version, OS, theme, relevant plugins, and a small sample note. Please do not upload your whole vault.

## License

[MIT](LICENSE). Third-party plugins and fonts retain their own licenses.

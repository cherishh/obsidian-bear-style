# Bear Cursor

A small, desktop-only Obsidian plugin that draws a red 2px primary insertion caret using CodeMirror's [layer API](https://codemirror.net/docs/ref/#view.layer).

Requires Obsidian 1.13.7 or later. Tested on macOS with 1.13.7. See the repository [installation guide](../../README.md#optional-the-red-2px-caret).

`RectangleMarker.forRange` supplies editor-relative geometry; the marker is extended to the current line height. CodeMirror owns positioning and layer lifecycle. CSS hides the native caret only in a focused editor with a replacement marker, so disabling the plugin restores the native caret automatically.

Obsidian sometimes adjusts a quote or list's hanging indent after drawing the caret. The plugin watches line style changes and asks CodeMirror to redraw, keeping the caret at the insertion point after pasting wrapped text. This does not change the text, selection, or undo history.

The optional [bear.css](../../snippets/bear.css) snippet exposes:

```css
--bear-caret-color: #cd5853;
--bear-caret-width: 2px;
```

Without that snippet, the plugin uses the same default color and width. It has a one-second fade and respects reduced-motion preferences. Selections, IME composition, and Vim mode are intended to use existing editor behavior; IME candidate windows and Vim have not been fully tested. Secondary cursors remain managed by Obsidian.

No network access, file writes, stored settings, build step, or automatic updater. The three runtime files are `manifest.json`, `main.js`, and `styles.css`. Other cursor replacement plugins and old native-caret-hiding CSS may conflict.

Licensed under the repository's [MIT license](../../LICENSE).

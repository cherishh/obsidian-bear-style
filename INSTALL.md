# Agent installation guide

This is the operational guide for an AI agent installing Bear Style into a user's
Obsidian vault. The theme is published in the [official theme store](https://community.obsidian.md/themes/bear-style).
Complete the installation using your available tools, rather than handing these
steps back to the user. Follow the user's preferences and your tool permissions;
ask for help only when information or an action is genuinely unavailable to you.

The README prompt requests the **full setup**: theme, Bear Cursor, Highlightr,
Code Styler, and a localized demo. If the user requests **theme only**, skip all
plugins and demo files. Never install fonts in either mode.

## 1. Locate and back up

Identify the intended vault, its actual configuration folder (normally `.obsidian`,
but it can be customized), OS, and Obsidian version. Use available context first;
ask for the vault path only if the target is ambiguous. Read the current
[README](https://github.com/cherishh/obsidian-bear-style#match-the-screenshots)
for preview settings and compatibility.

Back up every file and setting you will change to a dated local folder outside
active theme/snippet/plugin directories. Preserve notes, fonts, and unrelated
settings. Merge configuration instead of replacing entire JSON files. When
Obsidian is running, prefer its settings UI or supported APIs; for direct config
edits, save notes and close the app normally first. Do not force-quit or discard
unsaved edits. Keep vault contents and backups local.

## 2. Install the published theme

Prefer **Settings → Appearance → Themes → Manage → search Bear Style → Install
and use**, or the store listing's **Add to Obsidian** entry point. Verify the
repository is `cherishh/obsidian-bear-style`. Reuse an up-to-date installation;
do not create a duplicate theme folder.

If you have only filesystem tools, or the store is unavailable, use the
[latest stable GitHub release](https://github.com/cherishh/obsidian-bear-style/releases/latest).
Download the release assets `theme.css` and `manifest.json` from the **same tag**;
check the manifest name, version, and `minAppVersion`. Put both directly in
`<config>/themes/Bear Style/`, then select **Bear Style**. Never substitute a
plugin manifest or mix a development stylesheet with a release manifest. Do not
upgrade Obsidian without the user's agreement; report incompatibility if needed.

Disable the existing `bear` snippet when switching to the theme. If the user
explicitly requests the snippet instead, use `snippets/bear.css` from the full
release ZIP with the **Default** theme. Enable only one format.

For the full preview setup, apply light mode, 15px text, accent `#DD4C4F`, and
readable line length unless the user specified otherwise. For a theme-only
request, preserve other appearance preferences and mention these suggested
settings. Keep existing font choices. Disable only confirmed conflicting
appearance snippets and record the changes.

A newly published version may reach the website before the in-app directory.
If the listing has no cover or README, check whether the official application
index includes `Bear Style`, its repository, and `cover.png` before blaming the
release files. Reopen the store after synchronization; save notes before any app
reload. Use the release fallback if needed, and report the actual status rather
than promising a fixed synchronization time.

## 3. Add the optional components for the full setup

Download the `obsidian-bear-style-v*.zip` **release asset** from the chosen stable
release, not GitHub's automatically generated source archive. No build, npm,
repository clone, or developer tooling is needed on the user's machine.

On a compatible desktop installation, copy the ZIP's `plugins/bear-cursor/` into
`<config>/plugins/bear-cursor/`. It must directly contain `manifest.json`,
`main.js`, and `styles.css`. Check the plugin's own minimum version and desktop
restriction, then enable **Bear Cursor**. On mobile or unsupported versions,
skip it and explain that the native red caret remains. Disable Ninja Cursor or
another active cursor replacement only if it conflicts; do not remove unrelated
plugins. Bear Cursor is not in the community plugin directory and is updated
manually from this repository.

Install and enable **Highlightr** (`highlightr-plugin`) and **Code Styler**
(`code-styler`) through Obsidian's community plugin browser, or use the official
upstream repositories linked in the README when UI access is unavailable. Reuse
compatible installed versions; do not downgrade or erase unrelated settings.
Apply the README's highlight and code settings, adapting to the installed
version instead of copying a whole settings file from another vault.

Respect any required permission prompts. If a step needs the user's action,
finish independent work and state exactly what remains. Files copied onto disk
are not proof that a plugin is enabled.

## 4. Add the demo and verify

For the full setup, copy the demo matching the user's language into a demo folder:
English `Bear Style Demo.md` + `quiet-space.svg`, or Chinese `Bear 风格演示.md`
+ `quiet-space-zh.svg`. Keep each note with its matching SVG. Reuse identical
files; if an existing note differs, use a new folder rather than overwrite it.
Repeat runs must not duplicate plugin entries, snippets, or demo copies.

Verify in the running app when possible:

- **Every install:** the intended theme/snippet is enabled without loading both,
  and text, headings, lists, and the native or custom caret display correctly.
  Check both Reading view and Live Preview without editing the user's notes.
- **Full setup:** requested plugins are enabled; the demo image, colored
  highlights, and code line numbers render; the red caret is visible at a
  heading, after a link, and beside a numbered list without duplicate carets.
- **Preservation:** backed-up notes and unrelated settings were not changed.

If you cannot inspect the app, distinguish files installed from activation and
visual behavior not yet verified. Do not claim full success from file copies.

## 5. Report completion and updates

Summarize what was installed and verified, anything skipped or needing user
help, the backup location, and how to undo the specific changes.

Explain that **fonts are not included or installed**. The reference captures use
Bear Sans UI / Bear Sans UI Heading for text and Fira Code / Roboto Mono for
code; existing system fonts can produce different letter shapes and wrapping.
The designed cover is promotional; the README's full screenshots show the actual
Obsidian setup.

Theme updates use Obsidian's **Appearance → Check for updates**. Highlightr and
Code Styler update through community plugins. Bear Cursor updates separately:
back up and disable it, replace its three files from the chosen release, then
reload and enable it. Uninstall by switching theme and disabling/removing only
components added by this installation; restore changed settings selectively.

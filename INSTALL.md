# Agent installation guide

Use this guide when a user asks you to install the full Obsidian Bear Style demo setup. Follow their preferences and your tool permissions. This guide covers the complete setup; the CSS alone does not require the optional community plugins.

Read the current [README](README.md), including **Match the screenshots** and compatibility notes. Download the latest stable release from [this repository](https://github.com/cherishh/obsidian-bear-style/releases/latest).

1. Identify the intended vault, its actual configuration folder (normally
   .obsidian, but it can be customized), the user's OS, and Obsidian version. If the
   target vault is ambiguous, ask the user which one before changing anything.

2. Back up the files and settings you will change to a dated local folder
   outside the active snippets/plugins directories. Preserve the user's notes and
   unrelated settings. Merge configuration changes instead of replacing whole
   JSON files. If Obsidian is running, use its settings UI or supported APIs;
   otherwise have it closed before editing configuration files so changes are
   not overwritten. Do not force-quit it or discard unsaved edits.

3. Install and enable bear.css. Use the Default theme, light mode, 15px text,
   accent #DD4C4F, and readable line length to match the screenshots, unless
   the user has specified a different appearance preference. Preserve existing font
   choices. Disable conflicting appearance snippets only when necessary and
   record exactly what you changed.

4. On a compatible desktop installation, install and enable the included
   Bear Cursor plugin. Check its manifest for the minimum Obsidian version.
   Disable Ninja Cursor or another active cursor replacement if it conflicts;
   do not uninstall unrelated plugins. On mobile or an unsupported version,
   keep the native red caret and explain that the 2px replacement was skipped.
   Do not upgrade Obsidian without asking the user.

5. Install and enable Highlightr (highlightr-plugin) and Code Styler
   (code-styler), then apply the screenshot settings documented in the README.
   Use Obsidian's community plugin browser or the official upstream repositories
   linked there. Reuse compatible installed versions; do not blindly downgrade
   them or erase other settings. These plugins are optional for the CSS alone,
   and are part of this requested full setup. Respect any required permission prompts;
   if an action needs the user's help, finish the independent work and explain exactly
   what the user needs to do.

6. Copy the demo matching the user's language into a demo folder in the target
   vault: Bear Style Demo.md + quiet-space.svg for English, or Bear 风格演示.md
   + quiet-space-zh.svg for Chinese. Keep the chosen note and its SVG together. Do not overwrite an existing note; reuse
   identical sample files or choose a new folder when they differ. Make repeat
   runs safe: no duplicate plugin entries, snippets, or unnecessary demo copies.

7. Reload Obsidian as needed and open the demo. Verify the snippet and plugins
   are actually enabled, the image resolves, colored highlights and code line
   numbers render, and the caret is visible while editing. Check a heading,
   a link, and a numbered list for duplicate carets. If you cannot inspect the
   running app, clearly separate files installed from behavior not yet verified;
   do not claim full success based only on copied files.

Do not download, extract, or install any fonts. Tell the user that fonts are NOT
included: the screenshots use Bear Sans UI / Bear Sans UI Heading for text
and Fira Code / Roboto Mono for code. Without those already installed, their
existing fonts will be used and letter shapes and wrapping can differ.

Finish with a short summary of what was installed and verified, anything
skipped or still requiring user action, the backup location, and how to undo
your changes. Keep all vault contents and backups local.

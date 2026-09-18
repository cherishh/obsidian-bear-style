#!/usr/bin/env python3
"""Build the release from an explicit public-file allowlist. No vault files."""
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parents[1]
version = (root / "VERSION").read_text().strip()
files = [
    "README.md", "README.zh-CN.md", "INSTALL.md", "LICENSE", "CHANGELOG.md", "VERSION",
    "snippets/bear.css", "plugins/bear-cursor/manifest.json",
    "plugins/bear-cursor/main.js", "plugins/bear-cursor/styles.css",
    "plugins/bear-cursor/README.md", "examples/Bear Style Demo.md",
    "examples/quiet-space.svg", "examples/Bear 风格演示.md",
    "examples/quiet-space-zh.svg", "docs/images/demo-en.png", "docs/images/demo-zh.png",
    "docs/images/cursor-en.png", "docs/images/cursor-zh.png",
    "scripts/package.py",
]
for name in files:
    if not (root / name).is_file():
        raise SystemExit(f"Missing release file: {name}")
(root / "dist").mkdir(exist_ok=True)
archive = root / "dist" / f"obsidian-bear-style-v{version}.zip"
with ZipFile(archive, "w", ZIP_DEFLATED) as bundle:
    for name in files:
        bundle.write(root / name, f"obsidian-bear-style/{name}")
with ZipFile(archive) as bundle:
    assert bundle.testzip() is None
    assert len(bundle.namelist()) == len(files)
print(archive)

# 海报素材与回滚

`cover-closer-look.png` 是额外的浅色细节海报，用 `scripts/compose_closer_look.py` 将真实截图中的正文区域等比放大，便于观察字体、高亮和外链图标。

`cover.png` 是商店与 README 使用的新版浅色海报；`cover-dark-editorial.png` 是 README 使用的新版暗色海报。文档部分均来自 Obsidian 1.13.7 阅读视图的真实截图，只做裁切和等比缩放。

`assets/market-cover/` 保留浅色与暗色截图裁片、示例文档 `demo.md`，以及旧海报原始文件 `original-cover.png`。裁片不含个人笔记或应用侧栏。浅色版沿用旧海报左侧品牌排版，暗色版采用独立双栏构图；文档字体、图标和颜色不经过生成或重绘。

使用安装了 Pillow 的 Python 运行 `scripts/compose_market_cover.py` 生成 `cover-light.png`，再复制为 `cover.png`；运行 `scripts/compose_dark_poster.py` 生成暗色海报。暗色海报脚本使用 macOS 系统字体。主题不会自动安装可选插件或字体。

回滚商店海报：将 `assets/market-cover/original-cover.png` 复制回 `cover.png`，提交并推送。商店条目保持引用 `cover.png`，图片更新可能受缓存影响。

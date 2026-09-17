# Obsidian Bear Style

让 Obsidian 多一点 Bear 的感觉：舒展的排版、温暖的红色强调，以及可选的红色 **2px 光标**。

[English](README.md) · [下载](https://github.com/cherishh/obsidian-bear-style/releases/latest) · [英文演示笔记](examples/Bear%20Style%20Demo.md)

![Obsidian 中的英文演示：标题、文字、高亮与链接](docs/images/01-typography.png)

这是为 **Obsidian 默认主题**编写的 CSS 代码片段，另附一个可选的桌面端光标插件。基础样式无需社区插件；本项目目前不是社区主题商店中的完整主题。

> 截图是在 macOS 的 Obsidian 中实拍的。要接近截图的完整效果，还需要相同字体及可选的 **Highlightr**（彩色高亮）、**Code Styler**（代码块）和 **Bear Cursor**（加粗光标）。只安装 CSS 不会复现每一个细节。

## 让 AI Agent 帮你安装

将下面的提示词复制给能访问你本地文件和 Obsidian 的 Agent，例如 Codex 或 Claude Code。它会安装完整演示配置，包括两个可选的社区插件。过程中可能需要你提供仓库路径，或处理 Obsidian 的权限提示；纯聊天助手无法直接安装电脑上的文件。

```text
请帮我在 Obsidian 仓库中安装 Obsidian Bear Style，并完成完整演示效果的配置。
请实际执行安装，不要只给我操作说明。

项目：https://github.com/cherishh/obsidian-bear-style
先阅读当前 README，尤其是“复现截图”和兼容性说明，再从该仓库下载最新稳定版。

1. 确认目标仓库、实际配置目录（通常为 .obsidian，也可能经过自定义）、操作系统
   和 Obsidian 版本。如果有多个可能的目标仓库，先问我选哪一个，再进行修改。

2. 将即将修改的文件和设置备份到带日期的本地目录，放在启用的 snippets/plugins
   目录之外。保留我的笔记及无关设置，合并配置字段，不要整份替换 JSON 文件。
   Obsidian 正在运行时优先使用设置界面或受支持的 API；直接修改配置文件前应
   先关闭应用，避免设置被覆盖。不要强制退出应用或丢弃未保存的编辑。

3. 安装并启用 bear.css。除非我另有外观偏好，使用默认主题、浅色模式、15px
   正文字号、#cd5853 强调色，并开启缩减栏宽，以接近截图。保留现有字体选择。
   仅在必要时关闭有冲突的外观代码片段，并记录具体改动。

4. 在兼容的桌面版本上安装并启用附带的 Bear Cursor，最低版本以 manifest 为准。
   如果 Ninja Cursor 或其他已启用的光标替换插件发生冲突，请关闭它们，但不要
   卸载无关插件。移动端或不兼容版本保留原生红色光标，并说明跳过了 2px 光标。
   不要未经询问就升级 Obsidian。

5. 安装并启用 Highlightr（highlightr-plugin）和 Code Styler（code-styler），
   按 README 的截图设置配置。使用 Obsidian 社区插件浏览器，或 README 链接的
   官方上游仓库。已有兼容版本就复用，不要盲目降级或清空其他设置。这两个插件
   对基础 CSS 是可选的，但本次我希望安装完整配置。遵守必要的权限提示；若某个
   操作需要我协助，先完成不依赖该操作的工作，再说明我具体需要做什么。

6. 将附带的英文演示笔记和 quiet-space.svg 复制到仓库的演示文件夹，保持二者
   相邻。不要覆盖已有笔记；内容相同的示例可以复用，内容不同时选择新文件夹。
   重复执行时不要产生重复插件条目、代码片段或不必要的演示副本。

7. 按需重新加载 Obsidian 并打开演示，确认代码片段和插件确实已启用，图片正常
   显示、彩色高亮和代码行号正常渲染、编辑时光标可见。检查标题、链接和有序列表
   处是否出现双光标。如果无法查看运行中的应用，请区分“文件已安装”和“效果尚未
   验证”，不要仅凭复制文件成功就声称全部完成。

不要下载、提取或安装任何字体。请明确告诉我：本项目不包含字体；截图正文字体为
Bear Sans UI / Bear Sans UI Heading，代码字体为 Fira Code / Roboto Mono。
如果系统未安装这些字体，就保留现有字体，因此字形和换行可能与截图不同。

最后简要报告已安装和已验证的内容、跳过或仍需我操作的事项、备份位置，以及如何
撤销本次改动。所有仓库内容和备份都应保留在本地。
```

如果只想安装基础样式，可以使用下方的[手动安装步骤](#安装样式)；CSS 本身不依赖 Highlightr 或 Code Styler。

## 看看效果

![八层列表、有序列表、任务与引用](docs/images/02-lists.png)

![引用、提示框和多色高亮](docs/images/03-highlights.png)

![代码块、表格和图片](docs/images/04-code-and-images.png)

光标截图暂时停在闪烁的可见帧，方便观察其高度和宽度。

![实时阅览中的红色光标](docs/images/05-cursor.png)

## 安装样式

1. 从 [Releases](https://github.com/cherishh/obsidian-bear-style/releases/latest) 下载并解压 **`obsidian-bear-style-v1.0.0.zip`**。
2. 在 Obsidian 的「设置 → 外观」中选择**默认主题**。
3. 找到「CSS 代码片段」，点击文件夹按钮，将下载包中的 `snippets/bear.css` 放进去。
4. 返回 Obsidian，必要时刷新列表，然后开启 **bear**。
5. 将外观中的强调色设为 **`#cd5853`**，正文字号可以从 **15px** 开始。

不需要编译、包管理器或主题设置插件。也可参考 [Obsidian 官方说明](https://help.obsidian.md/snippets)。

### 可选：红色 2px 光标

把下载包里的整个 `plugins/bear-cursor` 文件夹复制到 `<你的仓库>/.obsidian/plugins/bear-cursor/`。确认其中直接包含 `manifest.json`、`main.js` 和 `styles.css`，重新加载 Obsidian，在社区插件中开启 **Bear Cursor**。

这个插件需要从本仓库手动安装，尚未进入社区插件目录，也不会自动更新。更新时先关闭插件，替换以上三个文件，重新加载 Obsidian 后再开启。

插件通过 CodeMirror 编辑器的 layer API 绘制主光标，高度跟随当前行，并支持系统的减少动态效果设置。它不访问网络、不写入文件、不保存设置。未安装插件时，CSS 仍会将原生光标设为红色，但宽度由系统决定。请关闭其他光标替换插件，并移除旧的隐藏原生光标的 CSS。

## 复现截图

截图使用 **macOS、Obsidian 1.13.7、默认主题、浅色模式**。前四张为阅读视图，最后一张为实时阅览。仓库不附带第三方插件代码、字体或个人配置。

| 组件 | 作用 | 截图使用的配置 |
| --- | --- | --- |
| `bear.css` | 标题比例、间距、列表、引用、高亮圆角、图片边框和光标颜色 | 本仓库提供 |
| [Bear Cursor](plugins/bear-cursor/README.md) | 红色 2px 光标 | 本仓库提供，1.0.0，限桌面端 |
| [Highlightr](https://github.com/chetachiezikeuzor/Highlightr-Plugin) | 多色高亮及高亮命令 | 1.2.2，CSS classes 模式、rounded 样式；Green `#BBFABBA6`、Pink `#FFB8EBA6` |
| [Code Styler](https://github.com/mayurankv/Obsidian-Code-Styler) | 代码块行号、语法配色和语言边框 | 1.1.7，具体设置见下方 |
| 正文字体 | 字形和换行位置 | `Bear Sans UI, Bear Sans UI Heading`，15px；字体不随项目分发 |
| 等宽字体 | 代码字形 | `Fira Code, Roboto Mono`；字体不随项目分发 |
| Obsidian 外观 | 原生控件和任务框 | 强调色 `#cd5853`，开启「缩减栏宽」 |

Highlightr 和 Code Styler 可在 Obsidian 社区插件中单独安装，都是可选项。基础 Markdown 高亮和代码块不依赖它们；演示中的 `hltr-green`、`hltr-pink` 彩色高亮需要 Highlightr 提供相应样式。

Code Styler 从 **Default** 预设开始：开启行号，代码块圆角 **4px**，开启语言边框并设为 **4px**，隐藏语言标签和图标，关闭行内代码样式。其余使用默认设置。后续插件版本可能呈现不同效果。

使用自己系统中可用的字体即可；字体不同，字形和换行会有所差异。本项目不分发 Bear 字体，也不提供提取字体的说明。这是受 [Bear](https://bear.app) 启发的独立项目，与 Bear、Obsidian 官方无关联。

**无需 Ninja Cursor、Minimal Theme Settings 或 Style Settings。**

## 试用演示笔记

将 `examples/` 中的两个文件放到你仓库的同一个文件夹，打开 **Bear Style Demo.md**。图片使用相对路径，请保留旁边的 `quiet-space.svg`。

演示包含六级标题、粗体、斜体、删除线、链接、高亮、八层列表、有序列表、任务、引用、提示框、行内代码、代码块、表格及图片。全部为示例内容。

## 调整外观

编辑 `snippets/bear.css` 顶部的 `--bear-*` 变量：

```css
--bear-accent: #cd5853;
--bear-line-height: 1.8;
--bear-line-width: 700px;
--bear-paragraph-spacing: 1rem;
--bear-caret-width: 2px;
```

行高必须是**无单位数字**，例如 `1.8`，不能写成 `1.8em`；部分插件会将其与字体尺寸相乘。修改强调色时，也请修改 Obsidian 外观设置中的强调色。字体和正文字号仍在 Obsidian 设置中调整。

暗色模式只额外调整次要文字与图片边框，保留默认主题的正文和背景颜色。

## 兼容性与卸载

- 已在 macOS、Obsidian 1.13.7、默认主题下检查实时阅览和阅读视图中的排版、列表、引用、高亮、图片与代码。
- 已检查正文、标题前、链接后、有序列表旁的光标，以及关闭插件后的原生光标回退。
- 已检查暗色变量行为；展示截图为浅色模式。Windows、Linux 和实体移动设备尚未测试。
- 光标插件最低要求 Obsidian **1.13.7**，仅限桌面端。手机保留原生光标，后续 Obsidian 版本仍可能需要适配。
- 插件设计上会把输入法组合输入与 Vim 模式交给编辑器；输入法候选框行为及 Vim 模式尚未完整验证。

卸载时先关闭 **bear** 代码片段，再删除 CSS。先关闭 **Bear Cursor**，再删除插件文件夹。第三方插件是否移除取决于你是否仍使用它们的功能；无需修改笔记内容。

## 开发与许可

插件直接使用 Obsidian 提供的模块，仓库中的 JavaScript 即可运行，无需打包器。生成下载包：

```sh
python3 scripts/package.py
```

打包脚本仅包含明确列出的公开文件。反馈问题请提供版本、系统、主题、相关插件及最小示例，不要上传整个私人仓库。

采用 [MIT 许可](LICENSE)。第三方插件和字体保留各自许可。

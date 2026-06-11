<div align="center">

# 📊 DeckForge

**用 Python 从数据生成咨询级（麦肯锡风格）案头研究 PPT。**

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
&nbsp;[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
&nbsp;[![Built with python-pptx](https://img.shields.io/badge/built%20with-python--pptx-2D6CDF.svg)](https://python-pptx.readthedocs.io/)

[English](README.md) · **中文**

![overview](assets/screenshots/00-overview.png)

</div>

---

DeckForge 用 [`python-pptx`](https://python-pptx.readthedocs.io/) 把结构化研究数据
生成一份干净的**麦肯锡风格**市场研究 deck：无需模板文件、无专有字体、不手动拖页。
每个图表都是**原生可编辑的 PowerPoint 对象**（不是截图），每页遵循咨询骨架，整套
视觉通过一个 `Theme` 一键换肤。仓库自带一份完整可跑的 **51 页示例**（**英文 + 中文**）。

---

## 💡 为什么重要

一次进入市场或战略决策，往往从一份**案头研究 deck** 开始 —— 50+ 页，测算市场规模、
梳理竞争格局、给出启示。要做到顶级咨询的水准却**又慢又靠手工**：分析师逐张手搭图表、
反复誊抄同样的数字、和 PowerPoint 排版鏖战数日，结果还常常跑偏品牌规范。

**DeckForge 把这道工序变成可编程、可复现、合规一致的过程。** 喂入结构化数据，得到一份
完整、正式、客户级的 deck —— 原生可编辑图表、统一视觉系统、MECE 的章节结构、每页都带
来源。数据变了重跑一次；换一个 `Theme` 就给整册换肤。

---

## 📸 看效果

自带示例 —— 一份**关于（公开、示意的）全球电动车市场的 51 页 deck** —— 覆盖所有页型。

| 深蓝封面 + 衬线标题 | 标题 + 原生图表 + 分析 |
|:---:|:---:|
| ![cover](assets/screenshots/01-cover.png) | ![content](assets/screenshots/05-content-chart.png) |
| **多维对比表 + 启示条** | **事实 / 洞见 / 启示** |
| ![table](assets/screenshots/07-comparison-table.png) | ![blocks](assets/screenshots/09-insight-blocks.png) |

---

## 🎯 这个项目展示了什么

- **把一项高耗时的真实交付物自动化。** 一份咨询案头 deck 是数天的手工活；我把它变成
  数据驱动、可复现的构建，输出完整的 50+ 页客户级报告。

- **设计系统的高保真还原。** 整套观感忠实重建了顶级咨询的视觉识别 —— 深蓝+纯白高对比、
  **衬线标题**、细横线、标志性线条 motif —— 全部来自一个可替换的 `Theme`。中文用
  **楷体 (KaiTi)**，与麦肯锡中国一致。

- **原生而非伪造。** 图表与表格都是客户能打开、能改的真实 PowerPoint 对象，绝不是
  matplotlib 截图。每张图用一个强调色高亮**最重要的那一个数据点**。

- **可干净复用的工程。** 基于空白演示文稿构建（不依赖模板）、随处可跑、完整国际化
  （EN / 中文，通过 `labels` 字典）、一处换肤。

- **判断力与操守。** 这个公开版**彻底脱敏** —— 仅含通用的、麦肯锡风格的设计与取整/示意
  数据，**零**客户名、零真实数据、零专有字体/商标。既能开源建设，也能保护机密资料。

---

## 🧭 工作原理

每个内容页都是一个原子单元：**行动标题**（完整的因→果整句结论）+ **原生视觉**
（图表/表格/框架）+ **分析**（连续正文，或 事实/洞见/启示 三块）+ 标注来源。各页组装为
咨询骨架：

```
封面 → 三个核心问题 → 目录 → 执行摘要
     → 分章节（隔页 + 小目录 → 密集内容页 → 小结）× N
     → 结论（回扣开篇三问）→ 方法论 → 附录
```

方法论里两条铁律：deck 必须 **50+ 页**、结构 **MECE** —— 各部分**互斥且穷尽**，无缝隙、
不重叠地覆盖整个主题。详见 [docs/methodology.md](docs/methodology.md)；设计系统（配色、
字体、换肤）见 [docs/design-system.md](docs/design-system.md)。

---

## 🚀 30 秒上手

```bash
pip install -r requirements.txt

python app.py                                # ⭐ 网页应用 -> http://127.0.0.1:5000（无需写代码）
python examples/ev_market/build_deck.py      # 英文 -> output/ev_market.pptx     (51 页)
python examples/ev_market/build_deck_zh.py   # 中文 -> output/ev_market_zh.pptx  (51 页)
```

### 🖥 不会写代码？用网页应用

`python app.py` 启动 **DeckForge Studio** —— 填品牌、编辑内容规格（已预填可用样例）、
选语言，即可下载原生可编辑的 `.pptx`。任何人都能在浏览器里生成一份 deck。

![studio](assets/screenshots/web-studio.png)

```python
from deckforge import Deck, charts

deck = Deck(brand="Acme 研究", footer="Acme 研究")
deck.cover("全球电动汽车市场", subtitle="案头研究", meta="2026")

slide, (x, y, w, h) = deck.content(
    "平价车型上市、销量持续攀升，但增速在放缓",
    body=[("势头仍在。", "销量从约 1000 万辆(2022)增至约 1700 万辆(2025E)。"),
          "悬念在于可负担性能否把销量带入大众价格带。"],
    sources=[("IEA", "https://www.iea.org")],
)
charts.column(slide, deck.theme, x, y + 0.55, w, h - 0.6,
              ["2022", "2023", "2025E"], {"销量（百万辆）": [10, 14, 17]}, highlight=(0, 2))
deck.save("ev_market.pptx")
```

---

## 🔧 内部结构

```
deckforge/            # 工具箱
  theme.py            #   设计系统（配色/字体）—— 换肤改这里
  text.py             #   衬线/无衬线字体 + 中文字形 + 富文本强调
  core.py             #   Deck：封面、隔页、内容页、表格、结论 …
  charts.py           #   原生 柱/条/折/环 图（单点高亮）
  tables.py           #   主题化对比表 + 启示条
  components.py       #   事实/洞见/启示 三块洞察
  frameworks.py       #   KPI / 2×2 地图、价值链 chevron、图片行
  images.py           #   下载 → 校验 → 感知哈希去重 → 等比裁切
examples/ev_market/   # 可跑的 英文 + 中文 51 页示例
docs/                 # methodology.md · design-system.md
assets/               # 截图 + （许可宽松的）示例图片
```

- **原生图表**，PowerPoint 里可编辑 —— 绝非截图。
- **一个 `Theme`** 给整册换肤（配色、字体、字号）。
- **双语 / i18n** —— 界面文案通过 `labels` 字典切换；中文用楷体。
- 每页约 **2.2 张图**，来自许可宽松的图源（见 [assets/images/CREDITS.md](assets/images/CREDITS.md)）。

---

## ⚖️ 声明与边界

设计语言**参考**公开的咨询报告。本项目**与麦肯锡等任何机构无关联、未获其背书**，且
不含任何专有字体/模板/商标（Georgia / Arial / 楷体 均为通用替代字体）。所有示例数据均为
取整/示意。MIT 许可 —— 见 [LICENSE](LICENSE)。

---

## 👤 关于作者

**白翔宇 (Frank Bai)** —— 市场研究分析师，搭建 AI 辅助工具解决真实业务问题。DeckForge 是
一条真实案头研究生产线的开源、脱敏版。

正在寻找 **市场研究、数据分析与咨询** 方向的机会。

- **LinkedIn：** https://www.linkedin.com/in/frank-bai-411173260
- **GitHub：** https://github.com/frankglendon

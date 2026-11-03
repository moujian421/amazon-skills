# mj-market-analysis

亚马逊全类目深度市场调研报告 Skill（Claude Code / Antigravity）。输入一个类目，产出结构化的 5 章飞书市场调研报告：大盘、竞品、VOS 流量（关键词）、VOC 痛点（评论）和立项结论，附关键词流量表、竞品差评打标表和图表。

- 完整流程：[SKILL.md](SKILL.md)
- 报告模板与指标口径：[references/report-template-and-metrics.md](references/report-template-and-metrics.md)
- 图表示例：`references/charts_example.py`、`references/charts_html_example.py`、`references/minichart.js`
- Google Trends 州分布抓取：`references/fetch_google_trends_states.py`
- 报告转飞书版 Markdown：`references/md_to_feishu.py`

## 依赖

- MCP：`xydc-mcp`（西柚）、`sellersprite-mcp`（卖家精灵）、`sorftime-mcp`
- `lark-cli`（写飞书文档和表格）
- `batch-offload` skill（批量拉数）
- Python 3

## 安装

```bash
git clone git@github.com:moujian421/amazon-skills.git ~/amazon-skills
ln -s ~/amazon-skills/mj-market-analysis ~/.claude/skills/mj-market-analysis
```

# amazon-skills

亚马逊运营用的 Claude Code skill 合集。每个子目录是一个独立的 skill，可以单独装。

| Skill | 用途 |
|---|---|
| [mj-competitor-ads-frame](mj-competitor-ads-frame) | 竞品广告结构拆解：输入 ASIN 和站点，推断每个广告活动的投放词和匹配方式（精准、词组、广泛、自动、主题定位），以及在哪些详情页打广告 |
| [mj-market-analysis](mj-market-analysis) | 全类目深度市场调研报告：大盘、竞品、关键词流量、评论痛点、立项结论，输出到飞书 |
| [mj-category-weekly-monitor](mj-category-weekly-monitor) | 类目竞品周度监控：头部竞品运营动作和效果、排名上升商品复盘、每日降价监控，写入飞书表格 |

## 安装

克隆整个仓库，再把需要的 skill 链接到 `~/.claude/skills/`：

```bash
git clone git@github.com:moujian421/amazon-skills.git ~/amazon-skills
ln -s ~/amazon-skills/mj-competitor-ads-frame ~/.claude/skills/mj-competitor-ads-frame
ln -s ~/amazon-skills/mj-market-analysis ~/.claude/skills/mj-market-analysis
ln -s ~/amazon-skills/mj-category-weekly-monitor ~/.claude/skills/mj-category-weekly-monitor
```

各 skill 的数据源和依赖见各自目录下的 README。多数 skill 依赖西柚（`xydc-mcp`）、卖家精灵（`sellersprite-mcp`）等 MCP，以及批量拉数用的 `batch-offload` skill。

## 来历

`mj-market-analysis` 和 `mj-category-weekly-monitor` 原来是两个独立仓库，已连同提交历史合并到这里。

# mj-category-weekly-monitor

亚马逊类目竞品周度监控 Skill（Claude Code / Antigravity）。

- **周度**：头部 15 个变体组（西柚月销量排名、节点小类 BSR 前 50）的价格 / Deal / Prime / 广告 / 变体拆分等动作与效果。
- **排名上升排查**：头部以外小类排名明显上升的商品（🚀 快速 / 📈 渐进 / 🆕 新品冲榜），复盘打法并 A/B 分级。
- **月度**：大盘 24 个月销量/销售额（卖家精灵 / Sorftime / 西柚）、核心词 24 个月搜索量。
- **日度**：小类前 20 竞品近 2 天降价监控（launchd 每日自动运行）。
- 结果全部写入飞书表格（含主图、排版、回读核对）。

完整流程见 [SKILL.md](SKILL.md)，判定口径见 [references/rules.md](references/rules.md)，拉数清单见 [references/data-pulls.md](references/data-pulls.md)，新类目设置见 [references/first-run.md](references/first-run.md)。

## 依赖

- MCP：`xydc-mcp`（西柚）、`sellersprite-mcp`（卖家精灵）、`sorftime-mcp`
- `lark-cli`（飞书 CLI，写飞书表格）
- `batch-offload` skill（`~/.claude/skills/batch-offload/scripts/oc_pull.sh`，批量拉数）
- Python 3、macOS（launchd 定时器、系统通知）

## 安装

```bash
git clone git@github.com:moujian421/amazon-skills.git ~/amazon-skills
ln -s ~/amazon-skills/mj-category-weekly-monitor ~/.claude/skills/mj-category-weekly-monitor
```

新类目：
1. 复制 `examples/config.example.json` 到 `data/<slug>/config.json`，填入节点、西柚 categoryId/resourceId、飞书表 token、自家品牌等（按 `references/first-run.md`）。
2. 定时器（可选）：把 `examples/*.plist.template` 中的 `__HOME__` 换成你的家目录、`__SLUG__` 换成类目 slug，存到 `data/<slug>/`，再运行 `bash scripts/install_timers.sh`。

`data/` 目录存放各类目的配置、快照、日志和主图，已在 `.gitignore` 中排除。

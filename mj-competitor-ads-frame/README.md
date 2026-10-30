# mj-competitor-ads-frame

亚马逊竞品广告结构拆解 Skill（Claude Code）。输入一个 ASIN 和站点，推断这个 ASIN 所在父体当前（默认近 30 天）的广告结构：

- 每个 SP、SB、SBV 活动投的是哪个词的精准、词组还是广泛；
- 哪些是自动广告（紧密、宽泛），SB、SBV 是否用了主题定位；
- 在哪些商品详情页打了广告（同类竞品、跨类商品、自家品牌）。

匹配方式全部是推断：数据只看得到每个活动在搜索结果前 3 页被观测到的搜索词，看不到匹配方式、出价和否词。

- 完整流程和判定规则：[SKILL.md](SKILL.md)
- 指标计算脚本：`scripts/frame.py`

## 依赖

- MCP：`xydc-mcp`（西柚，父体广告活动数据，按次扣 Credits）、`sellersprite-mcp`（卖家精灵，关联流量）
- `batch-offload` skill（`oc_pull.sh`、`agy_pull.sh` 批量拉数）
- Python 3

## 安装

```bash
git clone git@github.com:moujian421/amazon-skills.git ~/amazon-skills
ln -s ~/amazon-skills/mj-competitor-ads-frame ~/.claude/skills/mj-competitor-ads-frame
```

# mj-price-band-selection

价格带错位选品：找“买家已经愿意花钱的价格带里，能用看得懂、评论能验证的差异，以更合适的价格切进去”的机会，并确认利润守得住。低价本身不算机会。

流程参考 `mj-blackhorse-selection`：固定规则、默认参数、只停一次确认、分轮拉数清单、漏斗计数、结论门槛、踩坑记录、Argon 复核。

- 数据源：卖家精灵（`sellersprite-mcp`）、Sorftime（`sorftime-mcp`）、西柚（`xydc-mcp`）
- 批量拉数：依赖 `batch-offload` skill 的 `oc_pull.sh` / `cb_pull.sh`
- 复核：agy 的 `gemini-4-argon-medium`
- 试跑过的类目：Stained Glass Making Tools（8090894011）

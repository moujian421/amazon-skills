# mj-blackhorse-selection

黑马选品：在一个类目节点里，按漏斗找“低评冲榜、销量自然递增”的品，排雷（大额 BD、老链接翻新、Vine 堆分、季节性），反查所属店铺，再用 1688 采购价、FBA 费和差评痛点测算“降价 15–25% 能否守住广告前 30% / 广告后 15% 净利”。

- 数据源：卖家精灵（`sellersprite-mcp`）、Sorftime（`sorftime-mcp`）、西柚（`xydc-mcp`）
- 批量拉数：依赖 `batch-offload` skill 的 `oc_pull.sh` / `cb_pull.sh`
- 复核：agy 的 `gemini-4-argon-medium`
- 试跑过的类目：Upper Body Machines（23533924011）、Bait Storage（3408971）、Stained Glass Making Tools（8090894011）

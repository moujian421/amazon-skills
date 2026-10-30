"""Pick the top-N variation groups for the month (Xiyou sales, merged by variation) that sit in the node's sub-BSR top K.
Usage: python3 pick_top.py --config CFG --sales SALES_PULL_DIR --snapshot SNAP.json [--write]
Prints the proposal; --write replaces cfg.tracked (keeps name/keyword of ASINs already tracked).
New entries get a placeholder name/keyword: review and edit them in the config before the daily pull."""
import json, glob, os, sys, argparse
sys.path.insert(0, os.path.dirname(__file__))
from cfg import load_cfg, save_cfg
ap = argparse.ArgumentParser(); ap.add_argument("--config", required=True); ap.add_argument("--sales", required=True)
ap.add_argument("--snapshot", required=True); ap.add_argument("--write", action="store_true"); A = ap.parse_args()
cfg = load_cfg(A.config); snap = json.load(open(A.snapshot))
ok = {}
for r in snap["rows"]:
    if r["subrank"] <= cfg.get("top_bsr_max", 50):
        ok[r["asin"]] = min(ok.get(r["asin"], 999), r["subrank"]); ok[r["parent"]] = min(ok.get(r["parent"], 999), r["subrank"])
f = sorted(glob.glob(os.path.join(A.sales, "raw", "get_category_sales_ranking_*.json")))[0]
data = json.load(open(f))["data"]; L = data["list"]
old = {t["asin"]: t for t in cfg.get("tracked", [])}
sel = []
for x in L:
    a = x["asinInfo"]; kids = x["metrics"]["variation"].get("matchedAsins", [])
    ids = [a["primaryAsin"]] + [m["asin"] for m in kids]
    hit = [ok[i] for i in ids if i in ok]
    if not hit: continue
    kids_sorted = sorted(kids, key=lambda m: m["sales"] or 0, reverse=True) or [{"asin": a["primaryAsin"], "sales": None}]
    top = kids_sorted[0]["asin"]
    t = old.get(top, {"asin": top, "brand": a["brand"], "name": f"{a['brand']} {top}（待改名）", "keyword": None, "siblings": []})
    t = dict(t, rank=len(sel) + 1, primary=a["primaryAsin"], group_sales=x["metrics"]["sales"]["value"], subbsr=min(hit), image_url=a.get("imageUrl"))
    if top not in old:  # siblings help detect variation split/merge; keep the 3 best-selling other children
        t["siblings"] = [{"asin": m["asin"], "name": f"{a['brand']} {m['asin']}", "short": m["asin"][-4:]} for m in kids_sorted[1:4]]
    sel.append(t)
    if len(sel) == cfg.get("top_n", 15): break
for t in sel:
    print(f"{t['rank']:>2} {t['asin']} {t['brand'][:12]:12} 组销量 {t['group_sales']:>6} 小类BSR {t['subbsr']:>3} {'(新)' if t['asin'] not in old else ''} {t['name']}")
dropped = [a for a in old if a not in {t['asin'] for t in sel}]
print("掉出前列:", dropped or "无")
if len(sel) < cfg.get("top_n", 15): print(f"只有 {len(sel)} 个满足条件：需要拉第 2 页销量榜（page=2）")
if A.write:
    cfg["tracked"] = sel; cfg["rank_month"] = data["dateRange"]["fromDate"][:7]; save_cfg(cfg, A.config); print("config updated")

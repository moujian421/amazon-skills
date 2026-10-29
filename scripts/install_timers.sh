#!/bin/bash
# 安装周度/日度监控的定时器（已装过的会先卸载再装）。用法: bash install_timers.sh
# 安装 data/<slug>/ 下所有 *.plist（可由 examples/*.plist.template 替换 __HOME__ / __SLUG__ 生成）。
set -u
SKILL="$(cd "$(dirname "$0")/.." && pwd)"
for P in "$SKILL"/data/*/*.plist; do
  [ -f "$P" ] || continue
  L=$(basename "$P" .plist)
  cp "$P" ~/Library/LaunchAgents/
  launchctl bootout gui/$(id -u)/"$L" 2>/dev/null
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/"$L".plist 2>/dev/null
  launchctl print gui/$(id -u)/"$L" >/dev/null 2>&1 && echo "OK  $L" || echo "FAIL $L"
done

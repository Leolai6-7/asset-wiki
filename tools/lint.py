#!/usr/bin/env python3
"""asset-wiki lint（#P11）：斷鏈／檔名 #／schema 覆蓋率／禁用詞"""
import glob, os, re, sys
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
files = glob.glob("wiki/**/*.md", recursive=True)
stems, aliases = set(), set()
for f in files:
    stems.add(os.path.basename(f)[:-3])
    m = re.search(r"^aliases: \[(.*?)\]$", open(f).read()[:1500], re.M)
    if m: aliases.update(a.strip().strip('"').strip("'") for a in m.group(1).split(","))
known = stems | aliases
# 1) 斷鏈
broken = {}
for f in files:
    if "index-archive" in f or "/log" in f: continue
    for link in re.findall(r"\[\[([^\]\|#]+?)(?:\|[^\]]*)?\]\]", open(f).read()):
        t = link.strip()
        if t and t not in known:
            broken[t] = broken.get(t, 0) + 1
top = sorted(broken.items(), key=lambda x: -x[1])[:10]
print(f"[斷鏈] {sum(broken.values())} instance / {len(broken)} 目標；Top: {top[:5]}")
# 2) 檔名 #
bad = [f for f in files if "#" in os.path.basename(f)]
print(f"[檔名#] {len(bad)} 檔" + (f"：{bad[:3]}" if bad else ""))
# 3) schema 覆蓋
tot = miss_a = miss_c = miss_conf = miss_dep = 0
for f in files:
    if os.path.basename(f) in ("index.md", "log.md") or "archive" in f: continue
    tot += 1
    fm = open(f).read()[:2000]
    if "as_of:" not in fm: miss_a += 1
    if "check_after:" not in fm: miss_c += 1
    if "confidence:" not in fm: miss_conf += 1
    if "thesis_dependency:" not in fm: miss_dep += 1
print(f"[schema] n={tot}｜as_of 缺 {miss_a}｜check_after 缺 {miss_c}｜confidence 缺 {miss_conf}｜thesis_dependency 缺 {miss_dep}")
# 4) 禁用詞（修辭-證據錯配 kill-list）
KILL = ["通過校準", "量表通過回測", "九條定理", "Forward PE 12-18x（台股估值乾淨", "APMI 2022 量產", "USD 44 億"]
hits = []
for f in files:
    if "archive" in f or os.path.basename(f) == "log.md": continue
    s = open(f).read()
    for k in KILL:
        if k in s and "撤回" not in s[max(0, s.find(k)-80):s.find(k)+80] and "修正" not in s[max(0, s.find(k)-80):s.find(k)+80]:
            hits.append((os.path.basename(f), k))
print(f"[禁用詞] {len(hits)} hits" + (f"：{hits[:5]}" if hits else ""))

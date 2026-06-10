---
title: AI 訂閱制 unit economics
aliases: [AI 訂閱制, AI SaaS 訂閱, AI Copilot 真相]
type: concept
created: 2026-06-04
as_of: 2026-06-04
check_after: 2027-02-15
updated: 2026-06-04
sources:
  - raw/2026-04-06_微軟每月收你30美元用Copilot——但條款寫著僅供娛樂.md
tags: [SaaS, 訂閱制, AI, 商業模式, unit economics, Copilot]
thesis_dependency: AI-capex
confidence: medium
---

# AI 訂閱制 unit economics

[[Microsoft]] Copilot $30/月 + 條款「**僅供娛樂**」事件揭穿的真相：**推論成本非零**讓傳統 SaaS 70-85% 毛利假設失效。

## 一句話

> $30/月不夠 cover 推論成本——所以條款寫「僅供娛樂」+ 免責。

## 數據（2026 Q1 微軟自家揭露）

- **NPS：-19.8**（顯著負面）
- **滲透率：3.3%**（卡住）
- 條款「**僅供娛樂使用**」（不對工作結果負責）
- 推論用量 ↑ 直接吃掉訂閱毛利

## 為什麼這跟傳統 SaaS 完全不同

| 傳統 SaaS | AI SaaS |
|---|---|
| 邊際成本接近 0 | **邊際成本顯著（推論成本）** |
| 毛利 70-85% | 毛利不確定，可能 < 40% |
| 用戶用越多 = 越好 | **用戶用越多 = 毛利越差** |
| LTV / CAC 計算清晰 | 推論成本動態，難算清 |
| ARR 高度可預測 | **每個用戶都是 burn risk** |

## 三條撞牆

1. **價格不能漲**：$30/月已經是消費者天花板
2. **毛利不能保**：用越多越貴
3. **NPS 不好看**：客戶不滿，續訂成本高

## 對 SaaS 估值的根本衝擊

→ 連 [[PE 壓縮公式]]、[[宋分備忘錄 ＃6 — 市場世界觀切換]]

- SaaS 倍數本來是 **40-60x PE**（高毛利 + 訂閱穩定）
- AI SaaS 若毛利 < 40% + NPS 為負 + 滲透卡住
- **倍數應該壓縮到 20-30x**？

## 三條救命路徑

| 路徑 | 案例 |
|---|---|
| **推論成本下降** | DeepSeek 路線（但 [[DeepSeek]] 不會幫 Copilot） |
| **客戶分層加價** | Enterprise vs Consumer 分流 |
| **接口控制** | [[Anthropic]] Managed Agents 路線 |

## 跟其他 wiki 概念連結

- [[Microsoft]] / [[OpenAI]] / [[Anthropic]] 全部受影響
- [[模型商品化]]：DeepSeek 壓低推論成本是雙刃劍
- [[Forward PE 估值法]]：SaaS 倍數定價的根本前提
- [[PE 壓縮公式]]：r 上升 + g 下降 → PE 雙重壓縮
- [[宋分備忘錄 ＃6 — 市場世界觀切換]]：機構在追問「現金流是否變穩定」

## 待 ingest 延伸

- 各家 AI SaaS 的 unit economics 揭露（Salesforce Einstein、Adobe Firefly、GitHub Copilot 細節）
- 推論成本曲線追蹤

## 相關連結

- [[Microsoft]]
- [[OpenAI]]
- [[Anthropic]]
- [[模型商品化]]
- [[Forward PE 估值法]]
- [[PE 壓縮公式]]
- [[DCF vs PE]]
- [[五層損益表（營業槓桿）]]

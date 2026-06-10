---
title: B 軸客觀指標（市場認知量表）
aliases: [B 軸量表, B 軸客觀指標, 市場認知量表, B-axis Scorecard]
type: concept
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-12-10
sources:
  - https://www.millstreetresearch.com/do-analyst-estimate-revisions-still-help-forecast-relative-stock-returns/
  - https://www.sciencedirect.com/science/article/abs/pii/S106294082100022X
  - https://en.wikipedia.org/wiki/Book-to-bill_ratio
  - https://en.macromicro.me/charts/97/tw-bb-ratio
  - https://www.cmoney.tw/forum/
tags: [B 軸, 資訊擴散, 市場認知, 量表, ABCD, 方法論]
confidence: medium
---

# B 軸客觀指標（市場認知量表）

**把 [[資訊擴散四階段]] 從敘事直覺變成可量測的 6 指標量表。** codex 對抗審核兩次點名：「資訊擴散階段判定缺客觀指標、全靠敘事直覺」——本檔是 [[投資四元問題框架（ABCD）]] B 軸（市場認知到了嗎？）指名待建的缺件。每個 entity 建檔／校準時填一次 4 行快查清單、weekly review 時重判。

## 七指標 × 四階段門檻總表（#P8 加籌碼層）

| # | 指標 | 怎麼查 | 1 機構研究 | 2 賣方升級 | 3 媒體擴散 | 4 ETF／反轉 |
|---|---|---|---|---|---|---|
| ① | EPS revision 方向與廣度 | Koyfin／Yahoo Finance「EPS Revisions」；台股看共識新聞、CMoney | 共識不動或無共識 | 上修開始、廣度擴大加速 | 上修持續但減速、beat 後反應鈍化 | 上修停滯／下修、好消息不漲 |
| ② | Sellside 覆蓋密度＋目標價離散度 | MarketBeat／TipRanks 覆蓋家數；目標價 high/low | ≤3-5 家或剛 initiate、high/low >2x | initiation 潮、離散收斂中 | 覆蓋 >15-20 家（美大型股）、目標價追著股價調 | 覆蓋飽和、目標價跟不上或下調 |
| ③ | 12M 股價漲幅與位置 | 12M return＋距 52 週高 | <+30%、橫盤或落後板塊 | +30~100%、穩步上升 | **+100% 以上＝已過機構段**、加速 | 數倍漲幅後利多無反應、高位滯漲 |
| ④ | ETF／被動資金納入 | etf.com／VettaFi holdings；台股查 0050／thematic ETF 成分 | 無 thematic 納入、僅 broad index 底倉 | thematic ETF 開始納入、權重小 | 多檔 thematic 重倉、權重上調 | 指數納入成新聞、邊際買家＝被動基金 |
| ⑤ | 散戶熱度 proxy | 美股＝WSB mentions／Google Trends；台股＝爆料同學會討論量級、PTT Stock | 論壇近乎無討論（週 <個位數篇） | 偶有討論、多為轉貼法說新聞 | 每日多篇、喊目標價、媒體大量報導 | 全民題材、融資餘額暴增 |
| ⑥ | 接單出貨比 vs 股價背離 | 公司法說 book-to-bill；產業層 SEMI B/B（MacroMicro） | B/B >1 擴大、股價沒動＝正[[預期差]] | B/B >1、股價開始跟上 | 股價漲幅 > B/B 改善幅度 | B/B 走平／下滑、股價仍創高＝危險 |
| ⑦ | **籌碼結構**（#P8、詳 [[籌碼面（B 軸的資金流層）]]）| 台股：三大法人／融資／集保大戶（chips.py 自動化）；美股：short interest／13F | 外資悄悄連買、融資平穩、大戶比例升 | 外資＋投信同買、融資溫和增 | 融資加速增、散戶接手比例升 | **外資連賣＋融資大增（大手出散戶接）**、大戶比例降＋股價創高 |

查法補充：① revision breadth 慣用定義＝（上修分析師數 − 下修數）／總估計數（Mill Street）；② 學術上離散度與報酬關係雙向都有文獻、**只用來判「早期」、不拿來預測報酬**；⑥ 是背離偵測器、呼應 ASML 審核結論「買點要綁 book-to-bill」。

## 聚合判定規則

| 規則 | 內容 |
|---|---|
| 多數決 | 6 指標各給階段讀數、取中位數；不可單靠一指標 |
| 衝突＝訊號 | 讀數跨 ≥3 階＝認知分裂、通常是轉換期或錯殺（[[AAOI]] 6/9 -14% 型）→ 給區間 |
| 不確定給區間 | 同 [[五軸分數 confidence gate]] 邏輯、判不出寫「2-3」而非硬選 |
| 保守原則 | 為進場服務時、衝突取較晚階段（高估擴散程度比低估安全） |

## 案例校準（既有 entity 回測）

| 案例 | 關鍵讀數 | 量表判定 | wiki 既有判定 |
|---|---|---|---|
| [[AAOI]] | 12M +896%、Forward PE 226x、Serenity 公開 7x、thematic ETF 化 | 3-4 | 階段 3-4 ✅ |
| [[TXC]] | 法說剛公開、無系統性覆蓋——**#P8 籌碼修正：價 20 日 +57%＋融資近翻倍＋外資法說日倒貨 5,405 張 → 上修 2-3**（敘事指標慢、籌碼先說話＝量表⑦的第一個實戰修正、「一手資訊優勢的幻覺」案例）| ~~1-2~~ **2-3** | 原判 1-2 ❌ → 修正 |
| [[Lumentum]] | 12M +1,542%、覆蓋飽和、200G EML 漲價已成媒體敘事 | 3 | 階段 3 ✅ |
| [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證\|SemiAnalysis 延期報告]] | 機構限定報告 → 媒體開始報導 | 1→2 交界 | 1→2 交界 ✅ |

#P9 措辭修正：四案例為**事後對齊**（拿量表對自家敘事先驗打分、n=4、其中 TXC 已被籌碼層打臉改判）、**不是回測**；門檻（+100%、15-20 家）為待驗先驗。之後新 entity 改成**量表先判、敘事後驗**（順序反轉、消除直覺先行）。

## 每 entity B 軸快查清單（建檔／校準時填）

```
B 軸快查（as of YYYY-MM-DD）
1. Revision／覆蓋：EPS 共識[上修/持平/下修]、覆蓋 N 家、目標價離散[大/中/小]
2. 價格／被動：12M [+x%]、ETF 納入[無/thematic/重倉/指數事件]
3. 散戶熱度：[量級描述]（台股＝爆料同學會、美股＝WSB/Trends）
4. 籌碼（#P8）：外資 20 日累計[±N 張]、融資 20 日[±N 張／水位]、大戶比例[N%／趨勢]
5. 判定：階段 [N 或 N-M]；背離訊號：B/B vs 股價[同步/背離]、籌碼 vs 股價[同向/背離]
```

## 邊界與限制

- **量表只回答 B、不回答 C**：階段 1-2 ≠ 便宜（[[TXC]] 仍要過 Forward PE 檢查）；階段 3-4 ≠ 賣出（AAOI 錯殺案例：B 軸過度反應 ≠ C 便宜）。
- 台股資料縫隙：sellside 共識透明度低於美股、爆料同學會量級是 noisy proxy → 台股判定預設給區間。
- ③ 的 +100% 門檻是經驗錨點、新 IPO／turnaround／深跌反彈股不適用。
- 對應 [[市場四階段：懷疑／驗證／共識／反轉]]：1≈懷疑、2≈驗證、3≈共識、4≈反轉——量表同時餵兩個框架。

## 相關連結

- [[投資四元問題框架（ABCD）]]——本檔補的 B 軸缺件
- [[資訊擴散四階段]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[預期差]]
- [[散戶 vs 機構買股差異]]
- [[被動賣壓 vs 主動買盤]]
- [[五軸分數 confidence gate]]
- [[AAOI]]、[[TXC]]、[[Lumentum]]

## Sources

- [Mill Street Research — Do Analyst Estimate Revisions (Still) Help Forecast Relative Stock Returns?](https://www.millstreetresearch.com/do-analyst-estimate-revisions-still-help-forecast-relative-stock-returns/)
- [ScienceDirect — Dispersion in analysts' target prices and stock returns](https://www.sciencedirect.com/science/article/abs/pii/S106294082100022X)
- [Wikipedia — Book-to-bill ratio](https://en.wikipedia.org/wiki/Book-to-bill_ratio)
- [MacroMicro — US SEMI Billings / B/B Ratio](https://en.macromicro.me/charts/97/tw-bb-ratio)
- [CMoney 股市爆料同學會（台股散戶熱度 proxy）](https://www.cmoney.tw/forum/)

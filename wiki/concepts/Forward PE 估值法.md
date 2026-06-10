---
title: Forward PE 估值法
aliases: [Forward PE, 預估本益比]
type: concept
created: 2026-06-04
as_of: 2026-06-04
check_after: 2026-11-15
updated: 2026-06-04
sources:
  - raw/美股送分題-notes-市場解碼與估值筆記-2026-02至04.md
tags: [估值, PE, 基礎工具, Forward PE]
thesis_dependency: none（可遷移方法）
confidence: medium
---

# Forward PE 估值法

由 [[宋分（美股送分題）]] 在「市場解碼 #1」（Note #1）系統定義的基礎估值工具。

## 定義

```
PE         = 股價 ÷ 當年 EPS
Forward PE = 目前股價 ÷ 預估下一年度 EPS
```

## 核心洞察：估值下降的兩種原因

> Forward PE 變便宜，常常不是公司變差，是市場太悲觀。

| 估值下降 | 性質 |
|---|---|
| 因為「衰退」 | 風險 |
| 因為「擴張投資」（CapEx 高、EPS 暫時被壓） | **機會** |

## 範例（Note #1）

- 公司蓋資料中心，EPS 從 2 元降到 1 元
- 股價從 60 跌到 40
- **當前 PE = 40x**（看起來貴）
- 但明年 EPS 恢復到 2 元 → **Forward PE = 20x**（其實便宜）

## 「大行情起點」訊號

> 大行情常在「財報不好、新聞最差、但需求還在」時開始。

關鍵是區分**短期 EPS 壓縮**和**長期 EPS 衰退**。

## 在宋分方法論中的位置

Forward PE 是宋分整套工具鏈的**第一站**——之後接到：

- [[DCF vs PE]]（內在價值 vs 市場語言）
- [[PE 壓縮公式]]（PE = 1/(r-g)，從 PE 反推折現率）
- [[PEG Ratio 警告]]（成長持續性疑慮）

## 應用範例（Notes）

- **AVGO**：24x → 21x（用 2027 預估）「基本面沒變但股價回調」
- **AMZN**：下探 21x，「五年新低」
- **AMD**：34x→30x（今年）、22x→19x（明年），跌 17% 後落入「偏便宜」區
- **NVDA**：PEG = 0.37 但市場把它當循環股而非成長股

## 相關連結

- [[DCF vs PE]]
- [[PE 壓縮公式]]
- [[PEG Ratio 警告]]
- [[宋分（美股送分題）]]
- [[NVDA]]、[[AVGO]]、[[AMD]]、[[AMZN]]

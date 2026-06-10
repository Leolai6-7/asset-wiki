---
title: DCF vs PE
aliases: [DCF vs PE, 內在價值 vs 市場語言, Buyside vs Sellside 估值]
type: concept
created: 2026-06-04
as_of: 2026-06-04
check_after: 2027-02-15
updated: 2026-06-04
sources:
  - raw/美股送分題-notes-市場解碼與估值筆記-2026-02至04.md
tags: [估值, DCF, PE, Buyside, Sellside, 內在價值]
thesis_dependency: none（可遷移方法）
confidence: medium
---

# DCF vs PE

由 [[宋分（美股送分題）]] 在 Notes #2、#11 釐清的估值工具二分：**DCF 是內在價值（私募語言）；PE 是市場語言**。

## 一句話

> 股市不是收購市場，是轉售市場。

DCF 算的是「買下整家公司」的價值；PE 反映「在公開市場交易」的願付價格。**短期股價由 PE 倍數變化驅動，不是 DCF 內在價值。**

## 兩條估值路徑

### Buyside（基金經理）路徑（Note #2）

1. **建 EPS 模型**：分析產業動態、產能、利潤率
2. **轉換為 DCF**：未來現金流折回今天（穩定折現率低 / 新創高）
3. **得出內在價值**：DCF 是「安全檢查」，不是預測工具
4. **計算 Forward PE**：DCF $60 + 明年 EPS $2 → 隱含 30x PE

### Sellside（分析師）路徑

直接用同業比較得 PE 目標 → 反推目標價

## 真正的市場驅動：折現率，不是 EPS

> **大漲常在「認知從懷疑轉向相信」時發生，不是盈餘驚喜。**

- **DCF**：算「值多少錢」（私募市場）
- **PE**：算「願意付多少」（公開市場）

當市場降低對公司的折現率（風險認知下降），PE 倍數上升 → 股價漲。**這稱為 [[折現率壓縮]]**，不是「倍數擴張」。

## AVGO 範例（Note #15）

AVGO 財報後上漲反映的是「**確定性提升**」而非「倍數擴張」：

```
估值 = 未來現金流 × 實現機率 ÷ 折現率
```

- 空方原本 price in：TPU 2027 碎片化、Meta 訂單分散、ASIC mix 壓利潤、Anthropic 國防合約風險
- 法說會回應：TPU 2027 需求強勁、Meta ASIC 策略不變、68% EBITDA margin 維持、產能鎖到 2028
- **結論：風險機率下降 = 估值底部上升 = 折現率壓縮**

## 為什麼要兩個都用

- **Buyside 用 DCF 做下檔保護**（內在價值是底）
- **Sellside 用 PE 目標預測 re-rating 時機**（市場語言是動能）
- 純 DCF：算對價值但抓不到時機
- 純 PE：抓到時機但容易在循環股估值高峰買入

## 相關連結

- [[Forward PE 估值法]]
- [[PE 壓縮公式]]
- [[PEG Ratio 警告]]
- [[Re-rate 捕捉法]]
- [[宋分（美股送分題）]]

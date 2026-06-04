---
title: 循環投資（CSP-Model 互鎖）
aliases: [循環投資, CSP-Model 互鎖, Circular Investment]
type: concept
created: 2026-06-04
updated: 2026-06-04
sources:
  - raw/2026-04-06_OpenAI拿了1220億——但這筆錢不是你以為的那種錢.md
tags: [融資, CSP, 模型公司, Microsoft, OpenAI, 循環, 連鎖風險]
confidence: high
---

# 循環投資（CSP-Model 互鎖）

[[Microsoft]] ↔ [[OpenAI]] ↔ Azure 的閉環飛輪——**正向時是估值倍增器，反向時是連鎖爆破**。

## 機制

```
       投資 $100B
Microsoft ───────► OpenAI
                       │
                       │ 買 Azure 算力 $100B
                       ▼
                   Azure 認列營收
                       │
                       │ 推升 Microsoft EBIT
                       ▼
                   Microsoft 市值 ↑
                       │
                       │ 有資金繼續投資 OpenAI
                       └──────► 循環
```

## 雙面性

### 正向飛輪（2024-2026 Q1）

- 每一輪循環都**放大估值**
- Azure 營收成長 → Microsoft PE 擴張
- OpenAI 算力可見度 → 估值上修
- 「**OpenAI 燒錢 = Microsoft 賺錢**」的奇怪邏輯

### 反向爆破（待觸發）

- 若 OpenAI 違約 / 大幅折價 / 業務崩塌
- Microsoft 27% 持股價值 ↓
- Azure 預付營收結構 broken（其他客戶填不上）
- → **連鎖爆破**

## 其他循環投資對

| 圈 | 結構 |
|---|---|
| Microsoft ↔ OpenAI | 經典範例 |
| Amazon ↔ Anthropic | $4B 投資 + 用 AWS |
| Google ↔ Anthropic | $2B 投資 + 用 GCP |
| Oracle ↔ OpenAI | $50B 借債 + 蓋資料中心 |
| Nvidia ↔ AI 公司 | 投資 + 賣 GPU（CoreWeave 等） |

→ 「**AI 圈內錢」的真實量** 遠小於名義融資額。

## 投資啟示

### 估值剝離
```
真實 burn rate = 名義融資 − 循環部分
真實 AI infra ROI = AI 收益 − 循環部分
```

### 連鎖風險

| 風險 | 觸發點 |
|---|---|
| Microsoft 跌 | OpenAI 估值大幅折價 |
| OpenAI 跌 | DeepSeek 進一步壓制定價 |
| Oracle 跌 | OpenAI 任何不能履約 |
| 整個 AI 賽道跌 | 任何一個循環核心爆破 |

### 操作

- 用 [[宋分備忘錄 #1 — CSP-AI 通縮]] 的「FCF 拐點」識別循環何時停止支撐估值
- 用 [[資訊擴散四階段]] 判斷市場還在哪個階段定價循環
- 用 [[修正三階段]] 識別循環爆破訊號

## 跟其他 wiki 概念連結

- [[AI 融資結構（條件資本）]]：循環是條件資本的核心機制
- [[CapEx 見頂辯論]]：循環讓 CapEx 看起來不見頂
- [[模型商品化]]：DeepSeek 是循環的最大威脅（破壞 unit economics）
- [[政府風險溢價（AI 公司）]]：政府禁令是循環的外部觸發點

## 相關連結

- [[AI 融資結構（條件資本）]]
- [[OpenAI]]
- [[Microsoft]]
- [[Anthropic]]
- [[Google]]
- [[CapEx 見頂辯論]]
- [[FCF 拐點]]
- [[模型商品化]]

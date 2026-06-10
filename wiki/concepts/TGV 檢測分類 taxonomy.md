---
title: TGV 檢測分類 taxonomy
aliases: [TGV 檢測, AOI vs AXI, 半導體檢測 taxonomy, 檢測分類]
type: concept
created: 2026-06-05
as_of: 2026-06-05
updated: 2026-06-05
check_after: 2027-02-15
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [TGV, 檢測, AOI, AXI, X-Ray, 德律, 萬潤, taxonomy]
thesis_dependency: AI-capex
confidence: medium
---

# TGV 檢測分類 taxonomy

[[TGV 製程鏈圖譜]] 散布多個檢測站，但**AOI / AXI / X-Ray / e-beam 是完全不同層級的檢測技術**。本 concept = 檢測技術分類 + 各方法測什麼缺陷 + 對應賣水人。

→ 解決 codex P2 「AOI / AXI / 2D X-Ray 散落站別、缺 taxonomy」

## 一句話

> 不同檢測技術測不同層級缺陷，**沒有單一檢測能涵蓋 TGV 全鏈**。

## 五類檢測對照

| 技術 | 維度 | 測什麼 | 速度 | 成本 | TGV 適用站 | 主要玩家 |
|---|---|---|---|---|---|---|
| **AOI**（自動光學） | 2D | 表面缺陷、孔距、外觀 | 快 | 低 | 第 3、6（部分） | [[德律]]、致茂、牧德 |
| **2D X-Ray** | 2D 透視 | 內部結構（無深度） | 中 | 中 | 第 5、7 | YXLON、Nordson DAGE |
| **AXI（3D X-Ray CT）** ⭐ | 3D | **孔內斷路、複雜內部結構** | 慢 | 高 | **第 6（最重要）** | [[德律]]（與 OmniMeasure 合作）、Nikon、Zeiss |
| **e-beam**（電子束） | 高精度 2D/3D | 超細缺陷、最後驗證 | 很慢 | 極高 | 高階節點 | KLA、AMAT |
| **Acoustic Microscopy** | 3D | 分層、空隙 | 中 | 中 | 後段 | Sonoscan、PVA TePla |

## 為什麼 AXI 是「最重要檢測」（sennn.nnna 原文）

```
TGV 內部是「孔」
2D AOI 看不到孔內
2D X-Ray 看到 transparent overlap、無深度
3D X-Ray CT (AXI) = 唯一能逐層看 TGV 孔內斷路
```

→ AXI 對 TGV 是**必經之路**（沒過 AXI = 不知道斷路 = 良率天花板）

## 各檢測技術的台股玩家

### AOI 層（成熟）
- [[德律]] 3030 — 龍頭，跨 SPI / AOI / AXI
- 致茂（2360）
- 牧德（3563）

### AXI / 3D X-Ray 層（高 alpha）
- [[德律]]（與美商 OmniMeasure 合作開發 TGV 3D 模組）
- **YXLON**（已被 Comet Group 收購 COTN.SW，瑞士）
- Nikon (7731.JP)
- Zeiss（非上市）

### e-beam（國際大廠主導）
- KLA (KLAC)
- Applied Materials (AMAT)

### 後段封裝檢測
- [[萬潤]] 6187（CoWoS WoS 後段點膠+散熱+AOI 近壟斷）

## AOI 跟 AXI 是**不同生意**（投資啟示）

| 維度 | AOI | AXI |
|---|---|---|
| 賽道 | 成熟、競爭激烈 | 早期、高門檻 |
| 單機價格 | 中-低 | 高 |
| 毛利 | 中 | **高** |
| 護城河 | 演算法 + 客戶基礎 | **3D CT 軟體 + IP** |
| 對 TGV alpha | 補位 | **核心** |

→ **押 TGV 賽道應該優先押 AXI 玩家**，不是 AOI 玩家。
→ 德律的「TGV 純度低」評價可能低估，因為它在 AXI 段是 anchor 玩家。

## bull / bear thesis（AXI 賽道）

### Bull
- TGV 必經 AXI = 量增加
- 3D CT 軟體 + 演算法是 IP 護城河
- 國際大廠（YXLON / Nikon / Zeiss）佔位但台廠（[[德律]] + OmniMeasure）有 niche

### Bear
- YXLON / Nikon 若擴大攻台廠 niche → 德律 second source 地位受壓
- AXI 本身就是 high CAPEX，下行週期被砍

## 跟 wiki 概念連結

- [[TGV 製程鏈圖譜]] 第 6 站的深度展開
- [[德律]] entity：AXI 是該公司 TGV 段最深 niche
- [[萬潤]] entity：後段 AOI 近壟斷
- [[賣水人選股邏輯（投資版）]] 五軸評分中「站別關鍵度」適用
- [[公司 Entity 模板（Step 1-3 三段式）]]：每家檢測廠 thesis 校準需要分檢測類型

## 待 ingest 延伸

- YXLON / Comet Group 國際對手 entity（AXI 龍頭）
- KLA / KLAC 國際 e-beam 大廠 entity（[[賣水人選股邏輯（投資版）]] 中已列）
- 檢測 vs 量測（metrology）差別 concept

## 相關連結

- [[TGV 製程鏈圖譜]]
- [[德律]]
- [[萬潤]]
- [[賣水人選股邏輯（投資版）]]
- [[sennn.nnna]]

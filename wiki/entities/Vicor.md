---
title: Vicor
aliases: [Vicor Corporation, VICR, Factorized Power]
type: entity
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-09-09
expires_on: 2027-06-09
sources:
  - raw/2026-06-09_FOMOSOC-800V-HVDC-灰白區重劃-物理鐵壁論.md
evidence_url: https://ir.vicorpower.com/
tags: [標的, 電力管理, PoL, 48V, Factorized Power, AI server, 800V HVDC, 賣水人]
confidence: medium
---

# Vicor（VICR）

## 一句話定位（Sticky）

> **48V→core PoL 龍頭、Factorized Power Architecture 專利持有人、AI server 機櫃內最後一站電力轉換的核心模組商。**

## 三層 Thesis（Sticky）

### 產業層

[[市場四階段：懷疑／驗證／共識／反轉]] **驗證期**——AI server 從 12V 跳 48V → 800V 架構下，48V→core 中間態 design wins 機會擴大；但 800V 直連 chip 的競爭路線（[[Monolithic Power Systems MPS]] / [[Infineon]] / [[Texas Instruments TXN]]）也在追。

TAM：AI server PoL 模組 2025-2030 估 $5-10B（Vicor 自己預估）

### 目的層

不是賣晶片、是賣「**Power Module**」整合方案。專利 IP（Factorized Power Architecture：VTM + PRM）把 48V→core 兩階段轉換做進單一模組，繞過傳統 multi-phase buck 控制器。

連 [[宋分備忘錄 #2]] 對 Meta 的辨識邏輯：Vicor 不是「電源 IC 公司」、是「**架構解決方案公司**」。

### 供應層

**賣水人**（[[賣水人選股邏輯（投資版）]]）。
[[控制點轉移（投資版）]]：在 GPU 機櫃內白區最後一站。但**架構是雙刃劍**——如果 800V 直連 chip 普及（跳過 48V 中間態），Vicor 的 Factorized Power Architecture 反而被擠壓。

## 財務狀態快照（Dated Snapshot）

**As of 2026-06-09**：

| Re-rate 三角形 | 狀態 |
|---|---|
| 營收品質 | ⚠️ AI server PoL 拉動但客戶集中（NVDA / Amazon）|
| 毛利率 | ✅ 50%+（架構溢價，但近年波動）|
| OpEx | ⚠️ R&D 高佔比（架構世代轉換期）|
| 營業利益 | ⚠️ Q1 2026 仍微利、未進入 ramp |

→ Re-rate 三角形 **1/4** 滿（早期、未確認 AI ramp）

| 項目 | 數字 |
|---|---|
| 市值 | ~$3B |
| 12 月漲幅 | 中等（落後 800V 純押籃子）|
| Forward PE | 高（gross margin > earnings 比）|

- ✅ 催化：NVDA Rubin 機櫃 800V→48V 設計確定、Vicor design-in 公告
- ⚠️ 風險：800V 直連 chip 跳過 48V 中間態 → 架構被繞過

## 五軸 25 分制評分

| 軸 | 分數 | 說明 |
|---|---|---|
| 路線敏感 | 4/5 | 800V → 48V → core 中間態強烈受惠 |
| 站別關鍵 | 5/5 | 機櫃內最後一站、48V→core 沒人能無痛取代 |
| 耗材 | 2/5 | Power Module 一次性出貨、非耗材 |
| IP | 5/5 | Factorized Power Architecture 專利壁壘強 |
| 客戶分散 | 3/5 | NVDA / Amazon / Microsoft 集中 |
| **總分** | **19/25** | 中高、跟 [[Monolithic Power Systems MPS]] 對照 |

## 與其他 wiki 概念關係

- 800V HVDC 受惠：[[800V HVDC 灰白區重劃（物理鐵壁論）]]
- 電力戰場白區末端：[[AI infra 電力戰場]]
- 跟 MPS 路線對比：[[Monolithic Power Systems MPS]]
- 賣水人定位：[[賣水人選股邏輯（投資版）]]
- 架構雙刃劍對應：[[控制點轉移（投資版）]]

## 待校準（下季）

- NVDA Rubin 機櫃白區架構是否確認 800V→48V（vs 直連 chip）
- Vicor Factorized Power Architecture 是否拿到 hyperscaler 大單
- Power Module gross margin 是否 maintain 50%+ vs MPS 競爭

## 相關連結

- [[800V HVDC 灰白區重劃（物理鐵壁論）]]
- [[AI infra 電力戰場]]
- [[AI infra CapEx 三階段論]]
- [[Monolithic Power Systems MPS]]
- [[Texas Instruments TXN]]
- [[Infineon]]
- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[NVDA]]

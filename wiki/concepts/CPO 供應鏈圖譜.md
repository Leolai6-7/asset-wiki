---
title: CPO 供應鏈圖譜
aliases: [CPO 供應鏈, 共同封裝光學供應鏈, CPO Supply Chain]
type: concept
created: 2026-06-04
updated: 2026-06-04
sources:
  - raw/2026-05-07_wallstengine_SiTime-1.6T-CPO時脈元件三倍增量.md
tags: [CPO, 光通訊, 供應鏈, 半導體, AI 基礎設施, 賣水人]
confidence: high
---

# CPO 供應鏈圖譜

**Co-Packaged Optics（共同封裝光學）** 是 [[AI 供應鏈]] 在 800G → 1.6T → 3.2T 升級曲線上下一個 choke point。本 concept = **CPO 供應鏈七層分工 + 賣水人位階表**。

## 為什麼這個 concept 對 Leo 重要

[[跳出個股看三層：產業、目的、供應]] 的「供應」層的**實作範例**。
不押注「光引擎誰贏」，押注「**每一層的賣水人**」。

## 七層分工

| 層 | 內容 | 主要玩家 |
|---|---|---|
| **1. 交換 ASIC** | CPO 的「腦袋」，決定整個系統架構 | [[AVGO]] Tomahawk/Jericho、Marvell Teralynx |
| **2. 光引擎** | 光電轉換核心、CPO 的競爭主戰場 | [[Lumentum]] (LITE)、[[Coherent]] (COHR)、博通自研 |
| **3. DSP** | 訊號處理；CPO 反向風險最大（可能被整合消失） | Marvell |
| **4. Timing 元件** | 高頻時脈，每升一代 BOM 量翻倍 | [[SiTime]]、TXC、京瓷 |
| **5. 先進封裝** | CoWoS-X、L 系列封裝 | [[TSMC]] |
| **6. 連接器** | CPO 模組與系統互連 | Amphenol、Molex |
| **7. 電源 / 雷射** | 電源管理 + 光源 | MPS、ADI、TXN（電源）；[[Lumentum]] / [[Coherent]]（雷射） |
| **8. 玻璃中介層 / TGV** ⭐ | CPO 物理載體（Intel 2023 LIDE-CPO 專利明寫） | [[Corning]]、[[AGC]]、[[SCHOTT]] 玻璃；[[LPKF]]（LIDE IP）；[[鈦昇]]、[[雷科]]、[[弘塑]]、[[辛耘]]、[[萬潤]] 製程 |

⭐ **第 8 層是 2026-06 新增的依賴關係校準**——詳見 [[TGV × CPO 依賴圖]]。CPO 不只是「跟 TGV 平行的姊妹 thesis」，**Intel 2023 專利明寫 LIDE-formed TGV 用於 CPO 架構**——TGV 是 CPO 的底層使能技術。

## 賣水人位階

從「最敏感於單一玩家輸贏」到「最中性受惠」：

```
高敏感（押誰贏） ←─────────────────────────► 低敏感（誰贏都受惠）

光引擎 ([[Lumentum]]/[[Coherent]]) — NVDA 2026-03 同日 $2B 對倒投資、Leo「LITE 純度 + COHR SiC」一籃子押法
    │
   DSP (Marvell)
    │
   交換 ASIC (AVGO/Marvell)
    │
   先進封裝 (TSMC) ◄── 兩岸三地不可繞過
    │
   Timing (SiTime/TXC) ◄── 量 × 規格升級平方放大
    │
   電源 (MPS/ADI/TXN) ◄── 通用、不依賴 CPO 路線
    │
   設備 (ASML/AMAT/KLAC/LRCX) ◄── 任何 fab 擴產都吃
```

## 1.6T CPO 的 BOM 級放大

[[SiTime]] 案例（[[wallstengine]] 2026-05-07）：

```
1.6T CPO 需求：
- Timing 元件 量 ↑↑↑（三倍 BOM）
- Timing 元件 規格升級（更高頻、更穩定）
- → 量 × 規格升級 = 平方放大效應
```

→ 連 [[SiTime]]：「賣水人之中的賣水人」。

## 三大風險（CPO 整體賽道）

| 風險 | 影響 |
|---|---|
| 1.6T 標準延遲 | 整個 CPO TAM 推延 |
| 博通自研 timing | 影響 timing 賣水人定價力 |
| DSP 被整合消失 | Marvell 等 DSP 玩家賽道收縮 |

## 投資操作

### 進場時點
- 用 [[市場四階段：懷疑／驗證／共識／反轉]]：CPO 在 2026 還在懷疑/驗證期
- 用 [[資訊擴散四階段]]：[[wallstengine]] 等專業圈在傳，**散戶未大規模進入**
- → 仍在第一/二階段

### 倉位配置
- 不押光引擎（誰贏不確定）
- 重押**平方放大的 timing**（[[SiTime]]）
- 中性押**封裝**（[[TSMC]]）
- 對沖押**設備**（ASML / AMAT 等）

## 跟其他 wiki 概念連結

- [[賣水人選股邏輯（投資版）]]：CPO 是經典應用
- [[半導體基礎建設化]]：CPO 是 infra 重估的細項
- [[HBM iPhone moment]]：CPO 是另一個 iPhone moment 候選
- [[控制點轉移（投資版）]]：光引擎 vs 賣水人的控制權搶奪
- [[TGV × CPO 依賴圖]] ⭐：第 8 層的 IP / 技術依賴詳細展開
- [[TGV 製程鏈圖譜]]：第 8 層的製程深度
- [[先進封裝互聯路線圖]]：CPO 跟其他互聯路線的並存

## llm-wiki 跨庫對應

- llm-wiki [[CPO（共同封裝光學）]]：技術 anchor 視角，補充本 concept 的工程定義
- 詳見 [[跨庫對照（asset-wiki ↔ llm-wiki）]]

## 待 ingest 延伸（CPO entity 化）

- ✅ [[Lumentum]] (LITE)（已建，2026-06-05）— 第 2 層光引擎「純度首選」+ 第 7 層雷射光源；NVDA $2B 戰略
- ✅ [[Coherent]] (COHR)（已建，2026-06-05）— 第 2 層「規模 + 多軌」+ SiC 第二曲線；NVDA $2B 戰略
- Marvell (MRVL)
- 中際旭創（中國 CPO 玩家）

## 相關連結

- [[SiTime]]
- [[AVGO]]
- [[TSMC]]
- [[Lumentum]]、[[Coherent]]
- [[賣水人選股邏輯（投資版）]]
- [[半導體基礎建設化]]
- [[HBM iPhone moment]]
- [[wallstengine]]
- [[宋分（美股送分題）]]

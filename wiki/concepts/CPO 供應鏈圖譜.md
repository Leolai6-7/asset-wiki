---
title: CPO 供應鏈圖譜
aliases: [CPO 供應鏈, 共同封裝光學供應鏈, CPO Supply Chain]
type: concept
created: 2026-06-04
updated: 2026-06-10
sources:
  - raw/2026-05-07_wallstengine_SiTime-1.6T-CPO時脈元件三倍增量.md
  - raw/2026-06-09_SemiAnalysis-800VDC-CPO-延期-機構報告中文摘要.md
tags: [CPO, 光通訊, 供應鏈, 半導體, AI 基礎設施, 賣水人]
confidence: high
---

# CPO 供應鏈圖譜

**Co-Packaged Optics（共同封裝光學）** 是 [[AI 供應鏈]] 在 800G → 1.6T → 3.2T 升級曲線上下一個 choke point。本 concept = **CPO 供應鏈九層分工 + 賣水人位階表**。

## 為什麼這個 concept 對 Leo 重要

[[跳出個股看三層：產業、目的、供應]] 的「供應」層的**實作範例**。
不押注「光引擎誰贏」，押注「**每一層的賣水人**」。

## 九層分工

| 層 | 內容 | 主要玩家 |
|---|---|---|
| **1. 交換 ASIC** | CPO 的「腦袋」，決定整個系統架構 | [[AVGO]] Tomahawk/Jericho、Marvell Teralynx |
| **2. 光引擎** | 光電轉換核心、CPO 的競爭主戰場 | [[Lumentum]] (LITE)、[[Coherent]] (COHR)、博通自研 |
| **3. DSP** | 訊號處理；CPO 反向風險最大（可能被整合消失） | Marvell |
| **4. Timing 元件** | 高頻時脈，每升一代 BOM 量翻倍 | [[SiTime]] (MEMS)、[[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]] (石英陣營五家、2026-06-09 #H1 補完、石英 vs MEMS 雙軌路線分歧) |
| **5. 先進封裝** | CoWoS-X、L 系列封裝 | [[TSMC]] |
| **6. 連接器** | CPO 模組與系統互連 | Amphenol、Molex |
| **7. 電源 / 雷射** | 電源管理 + 光源 | MPS、ADI、TXN（電源）；[[Lumentum]] / [[Coherent]]（雷射） |
| **8. 玻璃中介層 / TGV** ⭐ | CPO 物理載體（Intel 2023 LIDE-CPO 專利明寫） | [[Corning]]、[[AGC]]、[[SCHOTT]] 玻璃；[[LPKF]]（LIDE IP）；[[鈦昇]]、[[雷科]]、[[弘塑]]、[[辛耘]]、[[萬潤]] 製程 |
| **9. 測試／檢測** ⭐ #P1 | 良率 gate——「量產瓶頸在測試不在製造」（焊後不可返修、組裝前篩 known-good-engine 是唯一出路）| [[Teradyne]]（Photon 100）、[[Advantest]]＋[[FormFactor]]（SiPh test cell、早 Photon 100 16 個月）、[[致茂 2360]]、[[鴻勁 7769]]；台股介面：[[穎崴 6515]]／[[旺矽 6223]]；[[德律]]（AXI 對照）|

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
   Timing (SiTime MEMS / TXC + NDK + Epson + Kyocera + Rakon 石英陣營) ◄── 量 × 規格升級平方放大、石英 vs MEMS 雙軌
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

## ⭐ #P1 良率 gate 與時程校準（2026-06-10 SemiAnalysis）

驗證詳見 [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]。

### 良率數學（第 9 層存在的理由）

- 光學引擎貼裝良率上限 ~95%、Spectrum-6（SN6810、102.4T）= **32 顆 COUPE × 3.2T** → 系統良率 **0.95³² ≈ 19%**、焊接後無法返修
- 經濟量產門檻：單引擎 **99.5%** → 系統 ~85%
- Quantum X3450（115.2T InfiniBand）= 72 顆 OE × 1.6T、24 個 OSA 模組 × 3 顆 → 壞片可篩選剔除 = 經濟性可控——**模組化粒度 = 良率風險的解藥**
- → 良率越爛、測試強度越高 = **第 9 層在 CPO 商用化之前就先收錢**（跟 [[TGV 檢測分類 taxonomy]] AXI 同構）

### 時程校準

| 項目 | 原認知 | #P1 校準 |
|---|---|---|
| Scale-up CPO 規模出貨 | 華爾街預期 2027-2028 | **2029+（綁 Feynman）**——SemiAnalysis《CPO Book》2026-01 既有立場、對抗驗證 3-0 全票 |
| 過渡期主流 | — | **銅纜 + 可插拔光模組至 2028+**（SemiAnalysis 2026-02：SN6600 可插拔版會比 CPO 版普及）|
| Spectrum-6 CPO（SN6810）| 2H26 出貨 | 板級插損 >3.5dB、根因未明、組裝製程重設計（⚪ channel check、無公開佐證）|
| [[市場四階段：懷疑／驗證／共識／反轉]] | 懷疑／驗證期 | **退回懷疑期**（2026-06-09 板塊賣壓、[[AAOI]] -14% 領跌）|

### 投資操作修正

- **timing 層拆解**：[[SiTime]] 的「CPO 三倍 BOM」段推遲 2029+；[[TXC]] 的可插拔 312.5MHz 段**受惠**（可插拔延壽、拉貨方 [[Innolight]]／[[Eoptolink]] 被點名受惠）
- 第 2 層光引擎（[[Lumentum]]／[[Coherent]]）：CPO 敘事溢價修正、EML／可插拔本業受惠、NVDA $2B = 延後≠取消
- **第 9 層測試 = 新的「賣水人之中的賣水人」候選**——CPO 成敗都收錢（爬良率期測更多、量產期也測更多）
- [[AAOI]] 6/9 -14% = [[預期差]] 活案例（主業可插拔、板塊 beta 錯殺 candidate）

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

- [[SiTime]]（MEMS 高端）+ [[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]]（石英陣營五家、2026-06-09 #H1 補完）
- [[AVGO]]
- [[TSMC]]
- [[Lumentum]]、[[Coherent]]
- [[賣水人選股邏輯（投資版）]]
- [[半導體基礎建設化]]
- [[HBM iPhone moment]]
- [[wallstengine]]
- [[宋分（美股送分題）]]
- ⭐ **第 5 層 OEM 模組廠**：[[Innolight]]（中國光模組 #1、全球 transceiver 30%+ 市佔、2026-06-09 補完 entity）
- ⭐ **第 6 層 connector**：[[Foxconn Interconnect FIT]]（鴻海集團 80% 持股 + ODM 內製 + 跟 [[Amphenol]] 對手位、2026-06-09 補完 entity）
- ⭐ **跨第 4-5 層 SiPho foundry**：[[GlobalFoundries]]（vs [[Tower Semiconductor]] / [[TSMC]] / IMEC 全球 top 4、Ayar Labs 戰略投資 + Mubadala 88% 持股、2026-06-09 補完 entity）

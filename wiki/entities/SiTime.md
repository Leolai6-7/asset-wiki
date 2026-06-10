---
title: SiTime
aliases: [SiTime, SITM, MEMS 時脈]
type: entity
created: 2026-06-04
as_of: 2026-06-04
check_after: 2026-09-15
updated: 2026-06-10
sources:
  - raw/2026-05-07_wallstengine_SiTime-1.6T-CPO時脈元件三倍增量.md
  - raw/2026-06-09_SemiAnalysis-800VDC-CPO-延期-機構報告中文摘要.md
tags: [標的, 美股, 半導體, MEMS, 時脈, CPO, 賣水人]
thesis_dependency: AI-capex
confidence: medium
---

# SiTime（SITM）

MEMS 時脈元件廠。**CPO 三倍 timing BOM + 六條放量曲線** = 「**賣水人之中的賣水人**」。是 CPO 供應鏈中 Leo 最值得追蹤的中性受惠者之一。

## 為什麼是「賣水人之中的賣水人」

- 不管 CPO 誰贏（Lumentum、Coherent、博通自研），**timing 都要用**
- 1.6T CPO 對時脈元件需求**三倍 BOM 量** + **規格升級** = **平方放大效應**
- → [[賣水人選股邏輯（投資版）]] 的經典案例

## 六條放量曲線

| 應用 | 受惠驅動 |
|---|---|
| 光模組 | 1.6T CPO 三倍 BOM |
| 衛星 | Starlink / OneWeb 衛星時脈 |
| IoT 直連 | LEO 衛星直連手機 |
| 機器人 | 機器人時序控制 |
| 自駕 | ADAS / Robotaxi |
| PCIe 6.0 server | 新世代 server timing |

→ **多條獨立成長曲線**疊加，分散單一賽道風險。

## 跟其他 wiki 概念連結

- [[CPO 供應鏈圖譜]]：SiTime 在 timing 層的位置
- [[賣水人選股邏輯（投資版）]]：經典範例
- [[半導體基礎建設化]]：從週期股 → 結構性成長股的潛在轉型
- [[資訊擴散四階段]]：宋分 #05 「下一個第一階段」之一是光通訊

## llm-wiki 既有

llm-wiki 已有 [[SiTime（SITM）]] entity——asset-wiki 這版本從**投資角度**重新切（賣水人 + 多條放量曲線）。

## 投資角度

- **中性受惠**：不押 CPO 誰贏，押 timing 一定要用
- **平方放大**：量 × 規格升級 = exponential
- 風險：博通若自研 timing（不太可能但要追蹤）

## ⭐ vs 石英陣營 5 家（2026-06-09 #H1 補位、石英 vs MEMS 雙軌路線分歧）

[[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]] 五家石英陣營 entity 補完——SiTime MEMS 高端 vs 石英陣營五家分歧路線完整版：

| 公司 | 五軸 | 路線敏感 | 站別關鍵 | 耗材 | IP | 客戶分散 | 定位 |
|---|---|---|---|---|---|---|---|
| **SiTime**（NASDAQ: SITM、本 entity）| **20/25** | 5 | 4 | 3 | 3 | **5** | **MEMS pure-play 高端**（5G / AI server / 衛星 / 機器人 / 自駕、Forward PE 75-100x）|
| **[[Kyocera]]**（OTC: KYOCY + 6971.JP）| **20/25** | **5** | 4 | 4 | **4** | **5** | **跨戰場 conglomerate**（石英 + AVX 鉭電容 + 多元）|
| **[[Epson]]**（6724.JP）| **19/25** | **5** | 4 | 4 | 3 | 4 | **TCXO 全球 #1 + 多軌組合王**（印表機 + 投影機 + 機器人 + 石英 + 手錶）|
| **[[TXC]]**（3042.TW）| **18/25** | 4 | 4 | **5** | 3 | 4 | **台廠石英晶體龍頭**（消費電子 + 汽車 + AI server + 工業大宗）|
| **[[NDK]]**（6779.JP）| **17/25** | 4 | 4 | **5** | 3 | **1** | **日本石英 #1、Apple iPhone anchor + 光學晶振 niche**（Apple 集中度 ~30-40% 扣分主因）|
| **[[Rakon]]**（NZX: RAK）| **15/25** | 4 | 3 | 4 | 3 | **1** | **紐西蘭 niche、軍工 + 衛星 + 5G base station**（客戶集中 ~65% 扣分主因）|

### SiTime 20 = Kyocera 20 並列頂級 ⭐

兩家路線完全不同但分數相同：
- **SiTime**：MEMS pure-play 高端、Forward PE 75-100x、市值 ~$16-17B（#P10 修正、原 $1.85B 為 2023 谷底舊值、差 9 倍）、5G / AI server / 衛星 / 機器人 / 自駕 5-6 條獨立曲線
- **Kyocera**：跨戰場 conglomerate（石英 + AVX 鉭電容 + 陶瓷封裝 + 太陽能 + 印刷 + 通訊）、Forward PE 14-18x、規模 USD ~$13-15B、被動元件第三道防線（鉭電容）anchor

→ 兩家代表 timing 賽道兩種「**賣水人之中的賣水人**」哲學：(1) MEMS 路線分歧 / 規格升級 vs (2) 跨戰場 conglomerate / 多軌 sum-of-parts

### 路線差異 anchor

| 維度 | SiTime（MEMS 陣營）| 石英陣營（TXC / NDK / Epson / Kyocera / Rakon）|
|---|---|---|
| 製程 | 矽製程 MEMS（可整合在 SoC、規格升級空間大）| 石英 wafer 切割 + 精密加工（50 年 IP 累積）|
| 高端規格 | ChipScale Atomic Clock +/- 0.5ppb 高端追趕中 | OCXO >100MHz / +/- 0.1ppb stability 仍領先（Rakon / NDK 高精度）|
| ASP | $1-30 USD（高端 4-6x 溢價）| $0.1-5 USD 大宗（消費電子 + 汽車）+ $10-100 USD 高 niche（軍工 + 衛星 OCXO）|
| 全球市場規模 | ~USD 8-10 億（MEMS、CAGR 25-30%）| ~USD 25-30 億（石英、CAGR 5-8%）|
| 客戶結構 | 5G / AI server / 衛星 / 機器人 / 自駕高端 | 消費電子 + 汽車 + 工業大宗 + 軍工 + 衛星 + 5G niche + Apple |
| Re-rate 路徑 | Forward PE 75-100x「**高成長 MEMS pure-play**」 | Forward PE 10-20x「**石英大宗 / conglomerate / niche specialist**」|
| 風險 | 規模小、客戶集中、CapEx 兌現、石英陣營反撲 | SiTime MEMS 高端滲透、消費電子萎縮 |

### 投資意涵：石英 vs MEMS 雙軌策略

可同時持有 SiTime + 石英陣營形成 timing 賽道完整曝險：
- **SiTime 20 高成長 alpha**：MEMS pure-play、Forward PE 75-100x、5G / AI / 衛星 / 機器人 / 自駕 5-6 條獨立曲線
- **Kyocera 20 跨戰場 defensive**：石英 + AVX 鉭電容 + 多元、Forward PE 14-18x、被動元件第三道防線 anchor
- **Epson 19 / TXC 21 中間值**（#P10 分數同步）：多軌組合 + 大宗 timing；⚠️ TXC Forward PE 已 ~33x、「估值乾淨」標籤撤回
- **NDK 17 Apple 供應鏈**：Apple iPhone + 光學晶振 niche、Forward PE 15-20x、Apple lock-in 雙刃劍
- **Rakon 15 軍工 niche**：軍工 + 衛星 OCXO 高純度、Forward PE 10-15x、規模小但 niche 段 SiTime 短期難滲透

## ⚠️ #P1 CPO 曲線時程推遲（2026-06-10 SemiAnalysis 校準）

- 六條放量曲線中「**光模組 1.6T CPO 三倍 BOM**」段推遲：scale-up CPO 規模出貨 **2029+（綁 Feynman）**——本 entity 的建檔 anchor（wallstengine 2026-05-07 三倍增量）兌現時點重標
- 其餘五條曲線（衛星／IoT 直連／機器人／自駕／PCIe 6.0）**不受影響**
- 可插拔 1.6T timing 需求持續（pluggable 主流至 2028+）——但注意 [[TXC]] 21 對照：**可插拔延壽相對利多石英陣營**（sub-30fs 高階可插拔段）、SiTime 的 CPO 平方放大故事才是被推遲的那段
- **20/25 維持**（多曲線分散正是這次校準的防護墊）、Forward PE 75-100x 的「高成長 premium」對 CPO 段推遲的敏感度要監控
- 驗證見 [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]

## 待 ingest 延伸

- 客戶：博通、Marvell、[[Coherent]]、[[Lumentum]] 都是（光引擎兩家 entity 已建 2026-06-05）

## 相關連結

- [[CPO 供應鏈圖譜]]
- [[賣水人選股邏輯（投資版）]]
- [[半導體基礎建設化]]
- [[AVGO]]
- [[wallstengine]]

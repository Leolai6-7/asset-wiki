---
title: 玻璃基板與 FOPLP 賽道
aliases: [玻璃基板, FOPLP, Glass Core, 扇出封裝, 玻璃中介層]
type: concept
created: 2026-06-05
updated: 2026-06-05
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [玻璃基板, FOPLP, 半導體, 先進封裝, Intel EMIB, AMD, Broadcom]
confidence: medium
---

# 玻璃基板與 FOPLP 賽道

承載 [[TGV 製程鏈圖譜]] 的上位賽道 thesis。**玻璃基板取代 ABF 載板** + **FOPLP 取代圓形封裝** = AI 算力放量的封裝必經之路。

## 四個關鍵概念（sennn.nnna 框架）

| 概念 | 定義 |
|---|---|
| **TGV（玻璃通孔）** | 貫穿玻璃中介層的互聯通道 |
| **玻璃中介層** | 主晶片與小晶片間的互聯平台 |
| **玻璃基板** | 主晶片的板材（取代 ABF 有機載板） |
| **FOPLP（扇出封裝）** | 矩形面板封裝（取代圓形）— 單次製程容量更大 |

## CAGR 89% claim（待驗證 ⚠️）

sennn.nnna 引用「研調機構：玻璃基板與 FOPLP 之 **CAGR of TAM = 89%**」

- **未具名研調**：可能是 Yole、Prismark、TrendForce、TechInsights 其中之一
- **時段未明**：可能是 2025-2030 五年 CAGR
- **對標**：CPO TAM 增速也在類似量級
- **subagent 未在快篩階段獨立驗證此數字** → **flag 為 medium confidence**

## 終端客戶

| 客戶 | 採用情況 | 時程 |
|---|---|---|
| **[[Intel]] EMIB** | Clearwater Forest（Xeon 6+）採玻璃核心基板 + EMIB | 2026 H2 量產 |
| **[[AMD]]**（蘇媽） | MI 系列哪一代採用尚未明確 | 「同樣這個打算」（sennn.nnna） |
| **[[Broadcom]]** ([[AVGO]]) | ASIC（TPU/Tomahawk）哪條線採用 | 「進度飛速」（sennn.nnna） |
| **AI ASIC 玩家** | Marvell、MSFT Maia、Google TPU、Meta MTIA 跟進 | 2027-2028 |
| **PC/手機晶片** | Apple、高通可能用 FOPLP（不一定 TGV） | 中低階晶片，2027+ |

## FOPLP 玩家（封裝整合）

| 公司 | 角色 | TGV 整合？ |
|---|---|---|
| **Powertech 力成**（6239） | 台廠 FOPLP 主力 | 待 ingest |
| **ASE 日月光**（3711） | 整合 OSAT 龍頭 | 待 ingest |
| **Samsung**（005930） | 韓系 FOPLP | 待 ingest |
| **Amkor**（AMKR） | 美系 OSAT | 待 ingest |
| **群創**（3481） | 面板廠轉型 FOPLP | 透過 [[東捷]] 設備 |

## 玻璃基板材料廠（上游）

| 公司 | 角色 |
|---|---|
| **Corning**（GLW） | 玻璃材料巨頭、HPGB 候選 |
| **SCHOTT** | 非上市，玻璃技術龍頭 |
| **AGC**（5201.JP） | 日系大型玻璃 |
| **NSG**（5202.JP） | 日系玻璃 |
| **信越化學**（4063.JP） | 化學材料整合 |

## 三個結構性 thesis（為什麼 TAM 會放大）

### 1. ABF 載板的物理極限
- 有機載板（ABF）在高頻訊號傳輸已撞物理瓶頸
- AI 算力 + 高頻互聯 → 必須換玻璃

### 2. FOPLP 取代圓形封裝 = 容量結構性增加
- 矩形面板每片產出 chip 數遠多於圓形 wafer
- → **解 AI 晶片荒**

### 3. TGV 是中介層技術升級
- 從矽中介層（CoWoS-S）→ 玻璃中介層（CoWoS-X？）→ 純玻璃
- 成本下降、設計彈性升

## bull / bear thesis

### Bull
- AI CapEx 持續 → 算力需求結構性 ↑ → 中介層需求 ↑
- Intel/AMD/Broadcom 三大客戶同時推
- 89% CAGR（若驗證）= 比 CPO 還誇張的成長

### Bear
- 89% CAGR 數字尚未驗證
- Hybrid Bonding 可能跳過 TGV
- 2026 樣品驗證若良率不過 → 推遲整個敘事
- 台廠多在「卡位期」，多數虧損中

## 跟其他 wiki 概念連結

- [[TGV 製程鏈圖譜]]：本賽道的具體製程實現
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]：賽道內的路線競爭
- [[HBM iPhone moment]]：估值框架轉換的同型案例
- [[半導體基礎建設化]]：玻璃基板是其中一個 sub-thesis
- [[CPO 供應鏈圖譜]]：姊妹 thesis（同樣是 AI infra 升級）
- [[賣水人選股邏輯（投資版）]]：本賽道優先邏輯

## 相關連結

- [[TGV 製程鏈圖譜]]
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]
- [[HBM iPhone moment]]
- [[半導體基礎建設化]]
- [[Intel]]、[[AMD]]、[[AVGO]]、[[NVDA]]、[[TSMC]]
- [[鈦昇]]、[[雷科]]、[[弘塑]]、[[辛耘]]
- [[sennn.nnna]]

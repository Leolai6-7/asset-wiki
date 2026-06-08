---
title: 玻璃基板與 FOPLP 賽道
aliases: [玻璃基板, FOPLP, Glass Core, 扇出封裝, 玻璃中介層]
type: concept
created: 2026-06-05
updated: 2026-06-08
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
  - raw/2026-06-08_Leo-玻璃基板時間線-TrendForce-Serenity.md
tags: [玻璃基板, FOPLP, 半導體, 先進封裝, Intel EMIB, AMD, Broadcom, Apple, TSMC CoPoS, TrendForce, Serenity]
confidence: high
---

# 玻璃基板與 FOPLP 賽道

承載 [[TGV 製程鏈圖譜]] 的上位賽道 thesis。**玻璃基板取代 ABF 載板** + **FOPLP 取代圓形封裝** = AI 算力放量的封裝必經之路。

## ⭐ 2026-06-08 完整時間線（TrendForce + [[Serenity]] 整理）

Leo 2026-06-08 引用 [[Serenity]] X 整理的 **TrendForce 玻璃基板時間線** anchor：

| 時點 | 玩家 | 細節 |
|---|---|---|
| **2026 H2** | [[Absolics]]（SK 系） | **Applied Materials 支持**（29.9% 持股 + 玻璃 handling 設備合作）+ **[[AMD]] 客戶**（MI400 volume sample → 2026 末 ramp） |
| **2027 H2** | [[Samsung Electro-Mechanics]] | **[[Sumitomo Chemical]] 合作**（Dongwoo Fine-Chem Pyeongtaek 廠地 + JV 小股東）+ 目標客戶 [[Apple]]（Baltra）/ [[AVGO|Broadcom]] / 大型雲端 |
| **~2028（2-3 年）** | [[TSMC]] CoPoS | 魏哲家 2026-06 股東會校準「**CoPoS 仍需 2-3 年量才放大**」——CoWoS 玻璃中介層版、跟市場預期相當接近 |
| **2030** | [[Intel]] | 亞利桑那 + 新墨西哥州產線**標準化與大批量產**（產業公認 anchor）、但時程仍**觀察中** |

### 三段式量產 narrative

- 🔴 **2026 H2 是第一波 anchor**：[[Absolics]] + [[AMD]] MI400 → 證明 panel-level glass interposer 商業化可行
- 🟡 **2027 H2 是進入主流市場**：[[Samsung Electro-Mechanics]] + [[Apple]] / [[AVGO|Broadcom]] / 大型雲端 → 韓 + 日 + 韓三方整鏈（SEMCO panel fab + Sumitomo 化學材料 + Dongwoo 韓國本土廠地）成型
- 🟢 **2028+ 是 TAM 全面放大**：[[TSMC]] CoPoS（2-3 年量才放大）+ [[Intel]] 2030 美國本土量產 → 玻璃基板從「替代 ABF」變成「先進封裝預設選項」

### 校準訊號

- 🆕 **「Applied Materials 支持 Absolics」是新公開層次**：除既有的 29.9% 持股 + USD 39M 入股，更明確點到**玻璃高速組裝 handling 設備合作開發**（specialized robotics + suction-based 運輸系統解玻璃易碎難題）
- 🆕 **TSMC CoPoS「2-3 年量才放大」校準**：魏哲家 2026-06 股東會明確表態（業務情報媒體報導：「CoPoS 仍需 2-3 年量才會明顯擴大」）→ 跟 TrendForce + 市場預期相當接近
- 🆕 **Intel 2030 + 亞利桑那 / 新墨西哥州雙廠標準化**：產業公認 anchor，但 Serenity / Leo 保留觀察空間（「距離真正量產還有一段距離」）

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
- [[Absolics]]、[[Samsung Electro-Mechanics]]、[[Sumitomo Chemical]]（2026-06-08 時間線玩家）
- [[鈦昇]]、[[雷科]]、[[弘塑]]、[[辛耘]]
- [[sennn.nnna]]、[[Serenity]]（2026-06-08 時間線資料來源）

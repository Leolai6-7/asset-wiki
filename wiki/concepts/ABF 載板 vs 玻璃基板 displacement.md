---
title: ABF 載板 vs 玻璃基板 displacement
aliases: [ABF 載板替代風險, 玻璃基板取代 ABF, ABF displacement]
type: concept
created: 2026-06-05
updated: 2026-06-05
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [ABF 載板, 玻璃基板, displacement, 欣興, 南電, 景碩, 受害, 轉型, 受惠]
confidence: medium
---

# ABF 載板 vs 玻璃基板 displacement

[[玻璃基板與 FOPLP 賽道]] 看「玻璃贏什麼」，本 concept 看「**ABF 輸什麼**」——三家 ABF 載板廠的三種命運：受害、轉型、受惠。

## 一句話

> 玻璃基板替代 ABF 載板不是 binary，是「**部分產品取代 + 部分客戶轉型 + 部分玩家進不去**」三條曲線的疊加。

## ABF 載板的「物理極限」（為什麼會被取代）

- ABF（Ajinomoto Build-up Film）是有機載板
- **高頻訊號傳輸瓶頸**：AI 算力需要更高頻寬，ABF 訊號損耗大
- **熱膨脹係數差**：CTE mismatch 跟矽晶片差距讓良率受限
- **尺寸極限**：大尺寸載板良率下降
- → **AI 算力產品**（Intel EMIB、AMD MI、Broadcom ASIC）必須換玻璃

## ABF 載板 ≠ 完全被取代

但不是所有產品都換：

| 產品類別 | 是否換玻璃 | 原因 |
|---|---|---|
| **AI ASIC / GPU 旗艦** | ✅ 換 | 高頻 + 大尺寸 |
| **CPU 高階** | ✅ 部分（Intel Clearwater Forest）| 同上 |
| **中階 CPU / 桌機 / Server** | ❌ 不換（短期）| ABF 仍夠用 |
| **手機 SoC** | ❌ 不換（用 InFO + Cu Pillar） | 物理體積 + 成本 |
| **記憶體 / NAND** | ❌ 不換 | 不需要 |
| **車用 / IoT** | ❌ 不換 | 不需要高頻寬 |

→ ABF 載板 TAM **被 AI 旗艦切走一塊**，但中低階仍是現金牛。

## 三家 ABF 載板廠的三種命運

### [[欣興]] 3037（**雙曲線受惠**，已校準 2026-06-05）
- ABF 載板**台廠龍頭** + 跨 Intel EMIB/Foveros + TSMC CoWoS/CoPoS **唯一橫跨**
- NVDA Blackwell 載板**第二供應商**（拿 30% 份額、僅次 IBIDEN）
- 高階 ABF（16L+）占 ABF 營收 60%、AI 相關 >50%
- 跟 [[敘豐]] 是設備客戶關係（敘豐 94% 銷貨集中欣興+長安）→ 敘豐 thesis 直接綁定欣興放量
- **玻璃 design partner with Intel**：2026-03 完成 sample 一階驗證、2026-07 自建 TGV 試產線完工
- 2026 CapEx **NT$254 億**（+30.93%，70% 投 ABF）
- 2026 Q1 EPS NT$3.28（13 季新高、YoY +447%）、2026 全年 EPS 估 NT$17、2027 再翻倍
- **校準後命運：受惠（雙曲線）**——displacement 過渡期 ABF 漲價 + 玻璃化下一輪 option
- → [[欣興]] entity 已建（2026-06-05）

### [[南電]] 8046（短期受惠 / 中期受害，已校準 2026-06-05）
- ABF 載板第二大、800G/1.6T 高階交換器**寡占 >70%**（隱形龍頭）
- ASIC 三巨頭（[[AVGO]] + [[AMD]] + Marvell）合計 **60% 營收** = 集中極高
- IC 載板占營收 85%（ABF 50-55% + BT 30%）、網通 49%
- 跟 [[NVDA]] 路線：**Vera Rubin 仍走 CoWoS-L + ABF（不轉 CoWoP）= 南電 NVDA 線在 2026-2027 受惠**（thesis 翻案）
- 但 [[AVGO]] Tomahawk 8 走玻璃路徑 + AMD/Marvell 跟進 = **2028 後 ASIC 高階 ABF TAM 被切**
- 玻璃自做**落後欣興**（樣品做出但卡雷射槽孔 + 穿孔電鍍 + 增層材質）
- 2026 Q1 OP margin 8.6%、OP YoY +534%、毛利率 15.85% 仍在恢復
- 大摩 EPS 2025-2028 CAGR **113%**（三雄最高）
- **校準後命運：短期受惠（2026-2027）/ 中期受害（2028+）**——concept 原預測「純受害」已部分翻案
- → [[南電]] entity 已建（2026-06-05）

### [[景碩]] 3189（**相對受益者**，已校準 2026-06-05）
- ABF 載板第三大、產品線**中階為主**（ABF 40% + BT 33% + 隱形眼鏡 18% + 基地台 5%）
- **2026 打入 NVDA AI GPU 第三供應商**（份額仍小但 design-in 確認）
- 美系 AI CPU 供貨率 10% → 50%、ABF 稼動率 86% → 95%
- BT 33% 受惠 T-glass 缺料漲價
- 客戶分散度三雄最高 = binary 風險最低
- 玻璃化加速反而對景碩有利——主力中階 CPU 載板不被切、後段 RDL 增層仍有位置
- 2026 Q1 EPS NT$1.17（YoY +92%）、2025 Q3 毛利率 18.96%
- 2026 全年 EPS 預估 NT$7.75-9.2（外資富邦目標價 NT$620）
- 2026-2027 ABF 擴產 +25%、CapEx **NT$235 億**（$744M）
- **校準後命運：相對受益**（高階玻璃化切的是欣興/南電/IBIDEN，景碩反吃外溢訂單）
- → [[景碩]] entity 已建（2026-06-05）

## 三家對玻璃基板的曝險矩陣

| | 高階 AI 曝險 | 玻璃轉型機會 | 中低階 ABF 餘地 |
|---|---|---|---|
| [[欣興]] | 高（Intel） | 中（可能跟進） | 中 |
| [[南電]] | 高（NVDA） | 低（押矽中介層繼續贏） | 中 |
| [[景碩]] | 低 | 低 | **高（最不受影響）** |

## 給 TGV 投資人的對沖視角

買 TGV 設備廠（[[鈦昇]]/[[雷科]]/[[弘塑]] 等）**做多玻璃基板**的同時：
- 賣空 [[欣興]] / [[南電]] 部分曝險？或
- 用 [[景碩]] 當對沖（玻璃化反而對它有利）？

→ 這是 **pair trade thesis**，連 [[賣水人選股邏輯（投資版）]] 的對沖延伸。

## 但這個 displacement 不是 zero-sum

- ABF 載板廠**自己可以轉型做玻璃**（如欣興）
- ABF 載板 TAM 也在成長（AI 中階、伺服器需求 ↑）
- **短期被切的 TAM** < **整體先進封裝 TAM 成長**
- → 多數 ABF 廠的 thesis 是「**慢慢被切但總量還在成長**」

## 跟第二戰場（嵌入式 MLCC）的關係

ABF 廠**並行押注**兩個 displacement 戰場：

| 戰場 | 玻璃化（向外） | 嵌入式 MLCC（向內） |
|---|---|---|
| **動作** | 換基板材料 | 把被動元件埋入載板 |
| **先發** | [[Samsung Electro-Mechanics]] / [[Absolics]] | [[Samsung Electro-Mechanics]] / [[太陽誘電 Taiyo Yuden]] |
| **IBIDEN 動作** | 觀望 / R&D | ¥5,000 億 CapEx 含嵌入式產線 |
| **欣興動作** | Intel design partner（先發） | 評估中 |
| **南電 / 景碩** | 樣品落後 | 觀望 |
| **對台 MLCC 廠（[[國巨]] / [[華新科]]）影響** | 無直接影響 | 直接被切 displacement |

→ 見 [[MLCC 嵌入式基板賽道]]。**ABF 廠對玻璃化是「受害方」、對嵌入式 MLCC 反而是「主導方」**——把上游 MLCC 廠的料件吃進來、control point 上移。台廠 ABF 三雄是否跟進嵌入式（不是玻璃）也是 displacement 的觀察軸。

## 跟 wiki 既有 concept 連結

- [[玻璃基板與 FOPLP 賽道]]：本 concept 的反面（玻璃贏 vs ABF 輸）
- [[先進封裝互聯路線圖]]：本 displacement 是其中一個次級競爭
- [[控制點轉移（投資版）]]：載板材料的控制點從化學（ABF）→ 玻璃
- [[宋分備忘錄 #6 — 市場世界觀切換]]：「成本不會回到以前」對 ABF 廠是真實壓力
- [[修正三階段]]：ABF 廠估值若因玻璃敘事被無差別賣 → 跟其他被錯殺的標的對照

## 待 ingest 延伸

- ✅ [[欣興]] 3037、[[南電]] 8046、[[景碩]] 3189 entity（已建 2026-06-05）
- 國際 ABF 廠：[[IBIDEN]]、[[Shinko Electric]]（日系）、[[Samsung Electro-Mechanics]]（已建）
- 玻璃 vs ABF 成本曲線、時點追蹤

## 相關連結

- [[玻璃基板與 FOPLP 賽道]]
- [[先進封裝互聯路線圖]]
- [[TGV 製程鏈圖譜]]
- [[賣水人選股邏輯（投資版）]]
- [[Intel]]、[[NVDA]]、[[AMD]]、[[TSMC]]、[[AVGO]]
- [[鈦昇]]、[[敘豐]]
- [[sennn.nnna]]

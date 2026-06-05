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

### [[欣興]] 3037（受惠 + 部分受害）
- ABF 載板**台廠龍頭**、Intel 主要供應商
- **同時也是玻璃基板潛在玩家**——Intel Arizona 鏈如果採玻璃，欣興有可能跟進
- 跟 [[敘豐]] 是設備客戶關係（敘豐 94% 銷貨集中欣興+長安）
- **命運：受害**（高階 ABF 被切）**+ 受惠**（自己 mix 進玻璃）
- → 待 ingest entity，需深入研究是否有玻璃 design-in

### [[南電]] 8046（純受害？）
- ABF 載板第二大、跟 [[NVDA]] 關係密切（H100/H200 載板）
- 如果 NVDA Rubin 繼續用 CoWoS-S（矽中介層）→ 南電仍是核心受惠
- 如果 AMD/Intel 轉玻璃 → 南電被切的 TAM
- **命運：取決於 NVDA 路線**（CoWoS-S vs CoWoS-X 玻璃）
- → 待 ingest entity

### [[景碩]] 3189（受害 + 中低階守住）
- ABF 載板第三大、產品線**中階為主**
- 高階 AI ASIC 玻璃化 → 影響有限
- **命運：中低階 ABF 守住、不受 AI 旗艦轉玻璃直接衝擊**
- → 待 ingest entity，可能是「相對受益」（高階競爭少了）

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

## 跟 wiki 既有 concept 連結

- [[玻璃基板與 FOPLP 賽道]]：本 concept 的反面（玻璃贏 vs ABF 輸）
- [[先進封裝互聯路線圖]]：本 displacement 是其中一個次級競爭
- [[控制點轉移（投資版）]]：載板材料的控制點從化學（ABF）→ 玻璃
- [[宋分備忘錄 #6 — 市場世界觀切換]]：「成本不會回到以前」對 ABF 廠是真實壓力
- [[修正三階段]]：ABF 廠估值若因玻璃敘事被無差別賣 → 跟其他被錯殺的標的對照

## 待 ingest 延伸

- [[欣興]] 3037、[[南電]] 8046、[[景碩]] 3189 entity（必補）
- 國際 ABF 廠：Ibiden、Shinko Electric（日系）、Samsung 子公司
- 玻璃 vs ABF 成本曲線、時點追蹤

## 相關連結

- [[玻璃基板與 FOPLP 賽道]]
- [[先進封裝互聯路線圖]]
- [[TGV 製程鏈圖譜]]
- [[賣水人選股邏輯（投資版）]]
- [[Intel]]、[[NVDA]]、[[AMD]]、[[TSMC]]、[[AVGO]]
- [[鈦昇]]、[[敘豐]]
- [[sennn.nnna]]

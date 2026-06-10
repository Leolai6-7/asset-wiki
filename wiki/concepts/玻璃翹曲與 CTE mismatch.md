---
title: 玻璃翹曲與 CTE mismatch
aliases: [玻璃翹曲, CTE mismatch, Warpage, 熱膨脹差異]
type: concept
created: 2026-06-05
as_of: 2026-06-05
updated: 2026-06-05
check_after: 2027-01-15
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [TGV, 玻璃基板, 翹曲, CTE, RDL, 熱壓合, 良率]
thesis_dependency: AI-capex
confidence: medium
---

# 玻璃翹曲與 CTE mismatch

[[TGV 製程鏈圖譜]] 第 7 站（CMP + RDL）的**核心痛點**——玻璃 CTE（熱膨脹係數）跟銅/有機載板/矽完全不同，**薄膜熱壓合反覆加熱會讓玻璃翹曲、甚至破裂**。

→ 解決 codex P2 「玻璃翹曲帶到但沒有 standalone concept」

## 一句話

> 玻璃翹曲不是製程 bug，是物理：CTE 差異 = 良率天花板 = design-in 決勝點。

## 物理機制

CTE（Coefficient of Thermal Expansion）= 熱膨脹係數

| 材料 | CTE (ppm/°C) | 跟玻璃差 |
|---|---|---|
| **玻璃**（基板） | 3-9（看玻璃種類） | 基準 |
| **矽**（晶片） | 2.6 | 接近（這是用玻璃的優點） |
| **銅**（電鍍/RDL） | 17 | **差 2-5 倍** |
| **有機樹脂**（薄膜） | 30-70 | **差 10 倍以上** |
| **ABF 載板**（對照） | 16-19 | 差 2 倍 |

→ 銅電鍍 + 有機薄膜熱壓合 = **跟玻璃 CTE 嚴重 mismatch** = 加熱後玻璃翹曲

## 翹曲發生的三個製程點

| 製程站 | 發生機制 |
|---|---|
| **銅電鍍後** | 銅填滿 TGV 孔，冷卻後銅收縮率比玻璃高 |
| **RDL 薄膜熱壓合** | 反覆加熱黏樹脂，CTE 累積差異 |
| **CMP 研磨** | 機械應力 + 殘留熱應力 |

## 解決方法（賣水人的 know-how）

### 1. 玻璃選擇（材料層）
- 不同玻璃 CTE 不同（[[Corning]] / [[AGC]] / [[SCHOTT]] 各家配方差異）
- **TGV 用玻璃需 CTE 6-8 ppm/°C**（接近 ABF 但更穩定）

### 2. 緩衝層設計（結構層）
- 銅跟玻璃之間加 CTE 中間層
- [[弘塑]] 的化學品配方有處理緩衝
- [[敘豐]] VSP 蝕刻+薄玻璃（<0.1mm）夾持系統明確處理翹曲

### 3. 製程參數（製程層）
- 熱壓合溫度控制
- 升溫速率
- 多步驟降溫

### 4. 設備設計（設備層）
- 玻璃夾持系統（薄玻璃易碎）
- 真空吸附 vs 物理夾持
- → [[敘豐]] MOON 軟體 3D 翹曲補償量測是這個層級的差異化

## 翹曲控制 = TGV 賽道隱性 alpha

賣水人沒解決翹曲 → 客戶不會 design-in
**誰解決翹曲 = 拿到 design-in**

| 公司 | 翹曲解決方案 | 結果 |
|---|---|---|
| **[[敘豐]]** | VSP 一站式 + MOON 3D 補償 + 薄玻璃夾持 | 量產實績 + 打入美系晶片供應鏈 |
| **[[弘塑]]** | 化學品配方緩衝 + CMP 整合 | CoWoS 三傑、台積電鏈穩 |
| **[[鈦昇]]** | E-Core 聯盟分工解決 | Intel design-in |

## bull / bear thesis

### Bull
- 翹曲是良率瓶頸 → 解方廠商有 pricing power
- 薄玻璃（<0.1mm）+ 大尺寸（FOPLP）放大翹曲挑戰 → 賣水人更稀缺
- 不需 TGV 路線贏，所有玻璃基板都要解翹曲

### Bear
- 玻璃配方 / 設備改良可能讓翹曲變 commodity
- 大廠（Disco / LPKF / 應材）一旦投入研發 → 台廠 niche 收窄

## 跟 wiki 概念連結

- [[TGV 製程鏈圖譜]]：本 concept 是第 7 站的痛點放大
- [[敘豐]] / [[弘塑]] / [[鈦昇]] entity：翹曲解方是隱性 design-in 護城河
- [[賣水人選股邏輯（投資版）]] 五軸評分中「站別關鍵度」加分
- [[CoWoS 三傑差異化]]：CoWoS 也有翹曲挑戰、三傑分工解決
- [[Corning]] / [[AGC]] / [[SCHOTT]]（待 ingest）：玻璃配方 CTE 控制

## 待 ingest 延伸

- 各家玻璃 CTE 規格表（Corning HPGB、AGC EN-A1 等）
- TGV 翹曲規格標準（如 SEMI 標準）

## 相關連結

- [[TGV 製程鏈圖譜]]
- [[ABF 載板 vs 玻璃基板 displacement]]
- [[敘豐]]、[[弘塑]]、[[鈦昇]]
- [[sennn.nnna]]

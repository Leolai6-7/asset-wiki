---
title: FOMO SOC — 800V HVDC 灰白區重劃 + 物理鐵壁論
type: summary
created: 2026-06-09
updated: 2026-06-09
sources:
  - raw/2026-06-09_FOMOSOC-800V-HVDC-灰白區重劃-物理鐵壁論.md
evidence_url: https://www.fomosoc.com/p/800v-hvdc-50hvdc?utm_source=share&utm_medium=android&r=5sk0kp&triedRedirect=true&_src_ref=l.threads.com
tags: [800V HVDC, 物理鐵壁, 灰白區, 自來水隱喻, SST, BBU, PoL, AI 資料中心, 電力戰場]
confidence: high
---

# FOMO SOC — 800V HVDC 灰白區重劃

**作者**：FOMO SOC（Leo 2026-06-09 轉貼）

## 一句話

> AI 時代必須 800V HVDC 不是趨勢、是**物理鐵壁倒逼**：P=VI、線損 ∝ I²，GPU 功耗暴增 → 電壓不上去就被銅線壓死。

## 核心 thesis（三條 anchor）

### 1. 物理鐵壁論（Why 800V）

| 維度 | 細節 |
|---|---|
| 通用 server 時代 | 12V / 48V 即可 |
| AI GPU 時代 | 單顆千瓦級、機櫃 600-1,000kW |
| 維持低電壓的代價 | 電流 → 銅線截面要粗、機櫃空間被吃、重量爆增 |
| **致命傷** | **線損 ∝ I²**——電流倍增 → 線發熱呈**指數級**上升 |
| 唯一解 | **提升電壓、降低電流** → 800V 是物理最佳解 |

### 2. 自來水隱喻（5 站架構）

> **水庫（電網）→ 淨水廠（變電站）→ 城市幹管（灰區重電）→ 社區水箱（白區配電）→ 家中水龍頭（機櫃 PSU）→ 濾水器吸管（晶片 PoL）**

關鍵概念：
- **灰區**＝重電（高壓、大電流、變壓器房）
- **白區**＝輕電（伺服器機櫃、低壓 DC）
- 灰白邊界**決定電力鏈架構**

### 3. 灰白區重劃（What's New）

**傳統 AC 架構 = 5 道折返跑**：

```
電網 AC → UPS（AC→DC→電池→DC→AC）→ 跨灰白邊界 → PSU（AC→DC 12V/48V）→ PoL → GPU
```

→ 每一道轉換 2-5% 損耗，**500MW 數據中心 = 25MW 廢電蒸發**

**800V HVDC 架構 = 一步到位**：

```
電網 AC → SST（固態變壓器，灰區一次整流到 800V DC）→ 800V DC 匯流排 → BBU（直掛、無折返）→ 機櫃 → GPU
```

→ **傳統 UPS 消失、變壓器房減肥、白區擴張**

## 受惠鏈映射（產業層）

### A. SST（固態變壓器）— 灰區入口
- [[ABB]]（變壓器全球 #1）
- [[Hitachi]] Energy（前 ABB 變壓器部門）
- [[Siemens]] / Siemens Energy
- [[Eaton]]
- → A2 subagent 正在建檔

### B. BBU（電池備援單元）— 取代傳統 UPS
- [[Vertiv]]（22/25 散熱戰場、UPS / BBU 兩棲）
- [[Eaton]]
- [[Schneider Electric]]
- [[台達電]]
- → 與 A2 + A3 落地會交叉

### C. 800V 配電 + switchgear
- [[Eaton]]、[[Schneider Electric]]、[[ABB]]

### D. 800V → 48V → core PoL（白區晶片級）
- **[[Vicor]]**（48V→core PoL 龍頭、Factorized Power Architecture）⭐ 漏網
- **[[Monolithic Power Systems MPS]]**（PoL 整合 IC）
- **[[Texas Instruments TXN]]**（類比 IC、電源管理大宗）⭐ 漏網
- **[[Infineon]]**（GaN/SiC、AI server 電源 IC）⭐ 漏網

### E. GaN/SiC 功率半導體（800V 開關）
- [[Navitas Semiconductor]]（GaN）
- [[Wolfspeed]]（SiC）
- [[Infineon]]（GaN+SiC 雙料）⭐ 漏網

## 與既有 wiki 概念的深度連結

### 強化 [[AI infra 電力戰場]] concept
- 之前只列 Vistra / Constellation / GE Vernova / Eaton / ABB 等玩家
- **新洞見**：「灰白區重劃 + 自來水隱喻 + 物理鐵壁論」= 為什麼這戰場 thesis 從「核電 baseload」延伸到「整鏈重劃」
- 補位：晶片級 PoL（[[Vicor]] / MPS / TXN）原本不在電力戰場 entity 池

### 對應 [[AI infra CapEx 三階段論]]
- 第三階段「上游材料 + 光通訊爆掉」**邏輯延伸**：電力鏈每一站重劃 → SST / BBU / PoL / GaN-SiC 同步爆掉
- → 三階段論需補入「**電力鏈灰白區重劃**」當作第三階段第六訊號

### 對應 [[Jevons Paradox（投資版）]]
- GPU 效率提升 → kW per chip 上升 → 整體電力鏈 TAM **不會收斂、只會擴大**
- 物理鐵壁 = Jevons 在電力鏈的具現化

### 對應 [[控制點轉移（投資版）]]
- 傳統 AC 鏈：變壓器廠 + UPS 廠拿大餅
- 800V DC 鏈：**SST + BBU + GaN/SiC 是新控制點**
- → ABB / Hitachi 從「變壓器供應商」升級為「SST 標準制定者」

### 對應 [[賣水人選股邏輯（投資版）]]
- 800V HVDC 整鏈是**橫向多站賣水人組合**
- 物理強制度 ≈ 100%（同 [[AI infra 散熱戰場]]）

### 對應 [[Bottleneck Theory（瓶頸論）]]
- 線損 I² + 銅線截面 = 電力鏈的「Hormuz 海峽」
- 解除前（800V 普及前）SST / BBU / PoL 龍頭享有 chokepoint pricing

## ⚠️ 三家漏網 entity 待建

1. **[[Vicor]] (VICR)** — 48V→core PoL 龍頭、Factorized Power Architecture、800V 架構下會被擠壓還是補強？
2. **[[Infineon]] (IFNNY / IFX.DE)** — GaN+SiC 雙料、AI server 800V 主供
3. **[[Texas Instruments TXN]]** — 類比 IC 大宗、電源管理跨產業最廣分散

## 待 Leo 自警惕

> 「不會一蹴而就，因為現代的數據中心並不是以直流電為生的」

→ 對 800V HVDC narrative 的冷靜點：
- 800V DC 全鏈替換需要 5-10 年漸進
- 中間態（48V / 400V DC）也是 design wins 機會
- 過熱期可能在「pilot ramp 公告」階段，而非「全鏈量產」

## 相關連結

- [[AI infra 電力戰場]]
- [[AI infra CapEx 三階段論]]
- [[Jevons Paradox（投資版）]]
- [[控制點轉移（投資版）]]
- [[Bottleneck Theory（瓶頸論）]]
- [[賣水人選股邏輯（投資版）]]
- [[ABB]]、[[Hitachi]]、[[Siemens]]、[[Eaton]]、[[Schneider Electric]]、[[Vertiv]]、[[台達電]]、[[Vicor]]、[[Monolithic Power Systems MPS]]、[[Infineon]]、[[Texas Instruments TXN]]、[[Navitas Semiconductor]]、[[Wolfspeed]]
- [[FOMO SOC]]（KOL 來源、待建）

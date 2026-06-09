---
title: 800V HVDC 灰白區重劃（物理鐵壁論）
aliases: [800V HVDC, 灰白區重劃, 物理鐵壁論, 自來水隱喻, SST 架構, HVDC 架構]
type: concept
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-12-09
expires_on: 2028-06-09
sources:
  - raw/2026-06-09_FOMOSOC-800V-HVDC-灰白區重劃-物理鐵壁論.md
evidence_url: https://www.fomosoc.com/p/800v-hvdc-50hvdc?utm_source=share&utm_medium=android&r=5sk0kp&triedRedirect=true&_src_ref=l.threads.com
tags: [800V HVDC, 物理鐵壁, 灰白區, 自來水隱喻, SST, BBU, PoL, GaN, SiC, AI 資料中心, 電力戰場]
confidence: high
---

# 800V HVDC 灰白區重劃（物理鐵壁論）

FOMO SOC 2026-06-09 提出的 framework：**為什麼 AI 時代資料中心必須 800V HVDC，不是趨勢、是物理鐵壁倒逼**。

→ 強化 [[AI infra 電力戰場]] 的核心 thesis；補位 [[AI infra CapEx 三階段論]] 第三階段第六訊號

## 一句話

> P=VI、線損 ∝ I²。GPU 功耗暴增 → 不升電壓就會被銅線截面 + 廢熱壓死。**升 800V 不是選項，是物理必然**。

## 三條核心 anchor

### 1. 物理鐵壁論（Why 必須 800V）

| 維度 | 通用 server 時代 | AI GPU 時代 |
|---|---|---|
| 單晶片功耗 | 100-300W | 700-1,500W（Rubin 預估 1.5kW+）|
| 機櫃功耗 | 5-15 kW | **600-1,000 kW**（5-8x 物理跳階） |
| 電壓 | 12V / 48V 即可 | **必須 800V** |
| 不升的代價 | — | 銅線截面 5-10x、線損 25-64x（I²）、廢熱呈指數級 |

**致命物理**：
- 線損 W = I² R
- 銅線截面 ∝ I
- 同樣功率下：V↑10x → I↓10x → 線損↓100x、銅↓10x

→ **這不是工程偏好，是物理鐵壁**

### 2. 自來水隱喻（5 站架構 + 灰白區分界）

```
水庫            電網（萬伏級）
  ↓
淨水廠          變電站
  ↓
城市幹管        ←━━━━━ 灰區（重電）━━━━━
  ↓
社區水箱        ←━━━━━ 灰白交界 ━━━━━━━
  ↓
家中水龍頭      ←━━━━━ 白區（輕電）━━━━━
  ↓
濾水器吸管      晶片 PoL → GPU core
```

| 站別 | 對應 | 玩家 |
|---|---|---|
| 電網 | 高壓 AC | 公用事業（[[Vistra]] 等）|
| 變電站 | 中壓 AC | [[ABB]] / [[Hitachi]] / [[Siemens]] 變壓器 |
| 城市幹管（灰區）| HVDC bus | **SST 入口**（新角色）|
| 社區水箱 | 配電盤 | [[Eaton]] / [[Schneider Electric]] |
| 機櫃 PSU | 機櫃內部 | [[Vertiv]] / [[台達電]] |
| 晶片 PoL | 48V→core | [[Vicor]] / [[Monolithic Power Systems MPS]] / [[Texas Instruments TXN]] |

**灰區 / 白區邊界 = 電力鏈最關鍵的設計決策點**

### 3. 兩種架構對照

#### 傳統 AC 架構 — 5 道折返跑

```
電網 AC
  ↓
UPS（AC → DC → 電池 → DC → AC）   ← 第 1 道
  ↓
跨灰白邊界（AC）                   ← 第 2 道
  ↓
PSU（AC → DC 12V/48V）            ← 第 3 道
  ↓
PoL（DC step-down）               ← 第 4 道
  ↓
GPU
```

- 每道轉換損失 **2-5%**
- **500MW 數據中心 = 25MW 純廢電**（佔總功率 5%）
- 廢熱倒灌散熱負擔

#### 800V HVDC 架構 — 一步到位

```
電網 AC
  ↓
SST（固態變壓器）                  ← 一次性 AC → 800V DC
  ↓
800V DC 匯流排（跨灰白邊界）
  ↓
BBU（電池備援、直掛 DC bus）       ← 取代傳統 UPS
  ↓
DC→DC（800V → 48V → core）
  ↓
GPU
```

**消失的元件**：
- 傳統大型 UPS → BBU
- 灰區變壓器房 → 白區更大

## 關鍵新角色 / 標準

### SST（Solid-State Transformer，固態變壓器）⭐ 灰區新入口
- 取代傳統油浸變壓器 + UPS
- **GaN / SiC 是關鍵半導體**（[[Navitas Semiconductor]] / [[Wolfspeed]] / [[Infineon]]）
- 主要玩家：[[ABB]] / [[Hitachi]] Energy / [[Siemens]] Energy / [[Eaton]]

### BBU（Battery Backup Unit）⭐ 取代傳統 UPS
- 直掛 800V DC 匯流排
- 鋰電池 + DC→DC 雙向
- 主要玩家：[[Vertiv]] / [[Eaton]] / [[Schneider Electric]] / [[台達電]]

### 800V 開關器 / 配電盤
- switchgear 升級至 800V DC
- [[Eaton]] / [[ABB]] / [[Schneider Electric]]

### Factorized PoL（48V → core）
- [[Vicor]] 的 Factorized Power Architecture 原本就是 48V→core 龍頭
- 800V → 48V 中間態 design wins 機會
- [[Monolithic Power Systems MPS]] / [[Texas Instruments TXN]] 跟進

## 受惠鏈圖譜（按灰白區 5 站排序）

### 灰區（重電 → SST → HVDC bus）
- [[Vistra]]（baseload 24/7 電源）
- [[Constellation]]（核電 PPA）
- [[GE Vernova]]（電網設備）
- [[ABB]] / [[Hitachi]] / [[Siemens]]（SST）⭐ A2 subagent 正在建檔

### 灰白交界（HVDC 配電 + BBU）
- [[Eaton]] / [[Schneider Electric]]（配電 + BBU）⭐ A2 subagent 正在建檔
- [[Vertiv]] / [[台達電]]（PSU / BBU 模組）

### 白區（機櫃內 → PoL → core）
- [[Vicor]]（48V→core PoL 龍頭）
- [[Monolithic Power Systems MPS]]
- [[Texas Instruments TXN]]（類比 IC 大宗）
- [[Infineon]]（GaN+SiC 雙料）
- [[Navitas Semiconductor]]（GaN 純押）⭐ A2 subagent 正在建檔
- [[Wolfspeed]]（SiC 純押、但虧損中）

## 跟其他 wiki 概念連結

### 強化 [[AI infra 電力戰場]]
之前列玩家但缺架構級 thesis；本 concept 提供「為什麼 800V 是必然」的物理推導，把電力戰場從 baseload + switchgear 擴張到「整鏈灰白區重劃」。

### 補位 [[AI infra CapEx 三階段論]]
第三階段「上游材料 + 光通訊爆掉」**邏輯延伸第六訊號**：
> 訊號 6：電力鏈灰白區重劃 → SST / BBU / PoL / GaN-SiC 同步爆掉

### 對應 [[Jevons Paradox（投資版）]]
GPU 效率提升 → kW per chip 上升 → 整體電力鏈 TAM 不會收斂。物理鐵壁 = Jevons 在電力鏈的具現化。

### 對應 [[控制點轉移（投資版）]]
傳統 AC 鏈：變壓器廠 + UPS 廠各拿一塊。
800V DC 鏈：**SST 廠（ABB / Hitachi）橫向整合 → 從變壓器供應商升級為「標準制定者」**。

### 對應 [[賣水人選股邏輯（投資版）]]
800V HVDC 整鏈 = 橫向多站賣水人組合，**物理強制度 ≈ 100%**（同 [[AI infra 散熱戰場]]）。

### 對應 [[Bottleneck Theory（瓶頸論）]]
線損 I² + 銅線截面 = 電力鏈的「Hormuz 海峽」。解除前 SST / BBU / PoL 龍頭享有 chokepoint pricing 2-5 年。

## ⚠️ 風險（thesis 失效情境）

### 1. 替代架構勝出
- 中間態（48V / 400V DC）取代 800V → SST 受惠者降級
- 連 [[Hyper Rail Multi-Rail（光通訊整合技術）]] 的整合邏輯

### 2. 過熱期 vs 全鏈普及
- > 「不會一蹴而就，因為現代的數據中心並不是以直流電為生的」（FOMO SOC 原文自警惕）
- 全鏈替換需 5-10 年漸進
- 過熱期可能在 pilot ramp 公告，而非全鏈量產
- 連 [[資訊擴散四階段]] 階段 3-4

### 3. 中國國產 SST 替代
- [[CXMT]] / 中國電網政策可能在中國市場排擠 ABB / Hitachi / Siemens

### 4. GaN/SiC 良率突破
- 若良率 / 成本曲線快於預期 → SST / BBU 普及更快、上游 [[Wolfspeed]] / [[Navitas Semiconductor]] 重估

## 監控指標（每季校準）

| 指標 | 觸發行動 |
|---|---|
| Hyperscaler 公告 800V DC pilot | 加碼 SST / BBU 玩家 |
| ABB / Hitachi SST 訂單能見度 | Forward PE re-rate 機會 |
| Vicor / MPS gross margin > 50%（PoL 漲價）| 確認 chokepoint pricing |
| GaN / SiC wafer 良率 > 70% | 上游 [[Wolfspeed]] re-rate |
| 中國國產 SST 公告 | 加 ABB / Hitachi 風險 |

## 待 ingest 延伸（漏網 entity）

- ⚠️ **[[Vicor]] (VICR)**：48V→core PoL 龍頭、Factorized Power Architecture
- ⚠️ **[[Infineon]] (IFNNY)**：GaN+SiC 雙料、AI server 800V 主供
- ⚠️ **[[Texas Instruments TXN]]**：類比 IC 大宗、跨產業最廣分散

## 相關連結

- [[AI infra 電力戰場]]
- [[AI infra CapEx 三階段論]]
- [[Jevons Paradox（投資版）]]
- [[控制點轉移（投資版）]]
- [[Bottleneck Theory（瓶頸論）]]
- [[賣水人選股邏輯（投資版）]]
- [[Hyper Rail Multi-Rail（光通訊整合技術）]]
- [[資訊擴散四階段]]
- [[ABB]]、[[Hitachi]]、[[Siemens]]、[[Eaton]]、[[Schneider Electric]]、[[Vertiv]]、[[台達電]]、[[Vistra]]、[[Constellation]]、[[GE Vernova]]
- [[Vicor]]、[[Monolithic Power Systems MPS]]、[[Texas Instruments TXN]]、[[Infineon]]、[[Navitas Semiconductor]]、[[Wolfspeed]]
- [[FOMO SOC]]（KOL 來源、待建）

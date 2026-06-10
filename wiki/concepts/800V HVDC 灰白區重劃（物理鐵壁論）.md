---
title: 800V HVDC 灰白區重劃（物理鐵壁論）
aliases: [800V HVDC, 灰白區重劃, 物理鐵壁論, 自來水隱喻, SST 架構, HVDC 架構]
type: concept
created: 2026-06-09
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-12-09
expires_on: 2028-06-09
sources:
  - raw/2026-06-09_FOMOSOC-800V-HVDC-灰白區重劃-物理鐵壁論.md
  - raw/2026-06-09_SemiAnalysis-800VDC-CPO-延期-機構報告中文摘要.md
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
- [[Infineon]]（GaN+SiC 雙料、SiC 全球 #1 ~25-28%）
- [[Navitas Semiconductor]]（GaN pure-play、10kW 98.5% 首發）⭐ 已 ingest 19/25
- **[[onsemi]] ⭐ #J1 2026-06-09 補位**（SiC IDM 全球 #2-3 ~22-26% + IGBT 前五 + 汽車 Image Sensor 全球 #1 ~50% 三軌、19/25、跨產品線 IDM 結構性穩定、跟 Coherent 19 / Lumentum 19 / Bloom 19 / Talen 19 同分）
- ~~[[Wolfspeed]]~~ ⚠️ **#J1 2026-06-09 補位、Chapter 11 退場警惕**（2025-06-30 申請 + 2025-09 重組批准 + 2026 Q1 重新上市、200mm SiC wafer first-mover 但 Mohawk Valley 良率不達 + Capex 龐大 + 利息壓垮、五軸 10-12/25 ⚠️ **NOT-INVESTABLE / reference only**、Apollo + Renesas + 大客戶為主要新股東；釋出市佔給 [[onsemi]] / [[Infineon]] / STMicroelectronics 三家 IDM 接管；驗證「**SiC pure-play + 200mm first-mover + chokepoint depth ≠ 投資成功**」、跟 [[Navitas Semiconductor]] GaN pure-play 成功對照「**純度 pure-play 在化合物半導體賽道兩條鏡像命運**」GaN 成 / SiC 敗）

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

## ⭐ #P1 SemiAnalysis 同日對撞校準（2026-06-10、時程層 + 標準之爭）

SemiAnalysis 2026-06-09 機構限定報告（驗證見 [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]）與本 concept **同日發布、方向相反但相容**：FOMO SOC 講物理層（為什麼終局是高壓直流）、SemiAnalysis 講時程層（比市場預期晚 1-2 年）。

### 風險 #1 被逐字啟動

- 本 concept 原風險 #1「中間態（48V / 400V DC）取代 800V → SST 受惠者降級」= SemiAnalysis 主張的現實：**±400VDC（OCP Mt. Diablo）照常 2H26 推進、NVIDIA 原生單端 800V 量產推遲 2028+**
- FOMO SOC 自警惕「不會一蹴而就」命中——過熱期確實落在 pilot 公告階段

### 重要 nuance：「誰的 800V」而非「要不要高壓」

- Mt. Diablo 規格（Microsoft + Meta + Google、2026-03-01 生效 v0.7.0）= ±400V 三線制、**但明文保留 2-wire 800V 選項、可接 ±400 或 800V busbar**
- → hyperscaler 不反高壓直流、反的是 **NVIDIA 單端 800V 標準** = [[接口控制權]] 之爭（NVDA 單端 vs OCP ±400 差分）
- Rubin compute tray 仍吃 ~50VDC（busbar）、兩種 800V 架構都保留 800V→~50V 轉換級 = tray 層級對上游架構中性 → 物理鐵壁論的「白區 PoL／VRM 不論架構都受惠」段**反而被強化**

### SemiAnalysis 自家四階段基線（Part 1、2026-05-26）

| 階段 | 內容 | 時點 |
|---|---|---|
| Phase 1 | ±400V sidecar 改裝既有 AC 設施（Diablo 400）| late 2026／early 2027 |
| Phase 2 | 800V 原生系統放量（含 Kyber rack）| 2027／2028 |
| Phase 3 | 全廠 800VDC | late 2028／2029 |
| SST 規模採用 | — | **2029 初** |

自家量化基線：800VDC 增量容量 ~39GW by 2030、power rack／sidecar 市場 **2028 峰值 ~$11B**（過渡期生意）、SST **~$13B by 2030**。

### 監控指標修訂（#P1）

| 訊號 | 解讀 |
|---|---|
| hyperscaler ±400V sidecar 訂單落地（2026 年底）| 過渡期架構確認 → 傳統低壓鏈（[[Forgent Power Solutions]]／Hammond／[[Vertiv]] UPS）延壽 |
| NVIDIA Kyber／VR Ultra 液冷 800V 版 sampling（late 2026 基線）| 再延後 = Phase 2 markdown、[[Navitas Semiconductor]] flag 加重 |
| 原「Hyperscaler 公告 800V DC pilot → 加碼 SST／BBU」| **改為雙向訊號**：±400V 擴產 ≠ 單端 800V 採用 |

### 受惠者重排（時程層）

- **雙贏組**（多空兩份報告同日點名）：[[Eaton]]／[[Schneider Electric]]／[[ABB]]／[[Vertiv]] = 「路線敏感（逆向）」軸活驗證
- **延期受惠**：[[Forgent Power Solutions]] 14（低壓配電 engineered-to-order、⚠️ 受惠的是延期本身、800V 加速即反轉）
- **延期受壓**：[[Navitas Semiconductor]] 19 → thesis-dependent flag（核心催化劑 2028+）、[[Wolfspeed]]（已 NOT-INVESTABLE 再添一刀）
- **不受影響**：[[Infineon]]／[[Monolithic Power Systems MPS]]／[[Vicor]]／[[Texas Instruments TXN]] 板級降壓鏈 + MLCC（[[村田 Murata]]／[[國巨]]／[[TDK]]）——48V→sub-1V 不論上游架構

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

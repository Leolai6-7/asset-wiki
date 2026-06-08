---
title: AEHR
aliases: [AEHR, Aehr Test Systems, Aehr Test, FOX-XP, FOX-NP, Sonoma, WaferPak, 矽光子 burn-in, 半導體 burn-in test]
type: entity
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2026-12-08
sources:
  - raw/2026-06-08_Leo-AI-infra-CapEx-三階段論-1.6T-光模組-InP.md
tags: [標的, US, NASDAQ, 半導體測試, burn-in, wafer-level burn-in, WLBI, package-level burn-in, PLBI, FOX-XP, Sonoma, WaferPak, AI 處理器, SiC, 矽光子, silicon photonics, hyperscaler, foreign_competitor, Bottleneck Theory L6, Serenity 重押, 賣水人]
confidence: high
---

# AEHR（NASDAQ: AEHR / Aehr Test Systems）

## 1. 一句話定位

**全球少數能做「wafer-level burn-in（WLBI）+ package-level burn-in（PLBI）+ 矽光子早期 burn-in」整合平台的半導體測試設備商、Bottleneck Theory 第 6 層 Testing & Qualification 純 chokepoint anchor**——1977 年成立於加州 Fremont、創辦人為 Charles Garvin、CEO Gayn Erickson；起家做 SiC（碳化矽）功率半導體 EV burn-in 設備、2025-2026 因 AI 算力 + 矽光子產業同步爆發**業務轉型**：從「SiC EV 純單腳」變成「**SiC + AI processor + 矽光子三腳鼎立 hyperscaler 設備商**」；獨家定位 = **第一家能 demo + 量產 wafer-level burn-in for AI processors**（CEO 原話 "first company to successfully demonstrate and ship a wafer level burn-in solution for AI processors"）；**Q3 FY2026（2026-02 季）獲取最關鍵指標性訂單**：(1) **lead AI accelerator 客戶 $14M 跟單訂單** + (2) **lead silicon photonics 客戶 follow-on order**（從 sample → 量產轉換訊號）+ (3) **Taiwan SiC customer FOX-XP 全資格化訂單**；Q3 bookings **$37.2M**（YoY 突破）+ Q4 +**$41M** record 訂單 = **Q3+Q4 bookings $92M+**、record backlog **$50.9M**、**Book-to-Bill 3.5x+**（極度 supply constrained）；公司**矽光子業務從零開始 build**、CEO 法說明白「矽光子 burn-in 是 multi-year market opportunity」；產品線 **FOX-XP（WLBI 旗艦）+ FOX-NP（單站 WLBI）+ Sonoma（PLBI、2000W per device、AI / 通訊處理器）+ WaferPak（contactor 耗材）**；市值 **USD ~$2.63B**、12 個月 **+968%**、Forward PE 2,106.61（虧損中、純 thesis driven）；是 [[Serenity]] 公開推文點名「**矽光子下個瓶頸中心、$1.1B 小市值、被低估了**」（Serenity 2026-X 推文 "+14.28% I did think the center of the next silicon photonics bottleneck at $1.1B"）。

## 2. 三層 thesis

### 產業層

- **半導體測試 + burn-in 賽道**處於 [[市場四階段：懷疑／驗證／共識／反轉]] **「驗證 → 共識」加速段**：
  - AI processor + 矽光子模組壽命可靠性 = 進入 hyperscaler datacenter 前的物理門檻
  - hyperscaler 因 AI ASIC / 光模組 mean-time-to-failure（MTTF）要求極嚴、burn-in 已從 nice-to-have → 必須項
  - **WLBI（wafer-level burn-in）容量 = 整鏈瓶頸**：模組組裝完成才測試 = 良率損失太大、必須在 wafer 階段先 burn-in
- **矽光子 + AI 算力 burn-in 賽道結構性需求**（[[AI infra CapEx 三階段論]] 第三階段最關鍵 anchor 之一）：
  - 1.6T → 3.2T 光模組要求 burn-in（避免 hyperscaler 部署後失效）
  - AI ASIC（Google TPU / Meta MTAI / Microsoft Maia / AWS Trainium）都需要 wafer-level burn-in
  - 矽光子 PIC burn-in 是**全新賽道**（傳統 photodetector / VCSEL 不需要這麼嚴的 burn-in、SiPho PIC + 集成激光是首次）
- **burn-in 設備賽道結構性「賣水人」位階**：
  - 不押任何單一晶片廠（NVDA / AMD / Google / Meta 同時客戶）
  - 不押任何單一路線（SiC EV / AI ASIC / SiPho / GaN 多技術平台）
  - = **與 [[SiTime]] 的「半導體 timing 賣水人」/ [[TSMC]] 的「foundry 賣水人」位階相似、但聚焦 burn-in 設備**
- **競爭結構**：
  - WLBI 主要對手：**Advantest（日本）、Cohu（COHU、美國）、Aehr** = 三家寡占
  - Aehr 在**矽光子 + SiC 早期 burn-in 兩個利基市場**比 Advantest / Cohu 早 1-2 年布局
  - Advantest 主場是 logic SoC test、Cohu 主場是 handler、Aehr 主場是**特殊 burn-in**
- 賽道 timing：
  - [[資訊擴散四階段]] 階段 **3-4**（股價 12M +968% 已過 KOL / 機構發掘段）
  - [[Hyper Rail / Multi-Rail（光通訊整合技術）]] / [[CPO 供應鏈圖譜]] 第 6 層測試 + 驗證 anchor
  - Q3 FY2026 矽光子大訂單 + Q4 $41M record AI 訂單 = 賽道訊號收斂

### 目的層

- 業務 mix（FY 2025 → FY 2026 轉型）：
  - **AI Processor burn-in**：**Q3 FY2026 $14M 跟單訂單 + Q4 $41M record** ⭐⭐
    - lead hyperscaler 客戶（推測 AWS Trainium / Google TPU）的 AI ASIC WLBI
    - 9 顆 300mm wafer 平行 burn-in 配置
    - Sonoma 為 2000W per device 高功率設計
  - **Silicon Photonics burn-in**：**Q3 FY2026 重要 follow-on order**（從 sample → 量產轉換）⭐
    - lead SiPho 客戶（推測 [[Coherent]] / [[Lumentum]] / [[Marvell]] / [[Tower Semiconductor]] 之一）
    - 高功率 FOX-XP WaferPak 系統
    - **公司認為這是 multi-year market opportunity**
  - **SiC（碳化矽）burn-in**：**Taiwan SiC customer 新訂單**
    - Greater China EV 市場聚焦
    - FOX-XP 全資格化 + 量產
    - = 原本是 Aehr 主業、現在變成支撐性業務
  - **GaN / Flash / DRAM / 影像 sensor**：少量 niche 業務
- 商業模式 = **「特殊 burn-in 設備 + WaferPak 耗材」**：
  - 設備一次性銷售（高 ASP、$2-10M/set）
  - **WaferPak 耗材年金**（每 wafer 規格不同、客戶 lock-in）
  - 客戶 lock-in 強：burn-in recipe + WaferPak 設計專屬 → 客戶換廠商成本極高
- 客戶結構（公開度極有限、推測為主）：
  - **lead AI accelerator 客戶**（推測 AWS / Google / Meta / Microsoft 其中之一）：Q3 $14M + Q4 $41M = $55M+
  - **lead silicon photonics 客戶**：未明確點名、推測 [[Coherent]] / [[Lumentum]] / [[Marvell]] / [[Tower Semiconductor]] / 旭創之一
  - **Taiwan SiC customer**：未明確點名、Greater China EV 市場
  - **multiple hyperscalers qualifying**（Serenity 推文）：表示**多 hyperscaler 同時測試 Aehr 設備、量產訂單可能來自多家**
- 客戶風險：**FY 2026 H1 lead customer ON Semi（onsemi、EV SiC）需求下滑** → 公司被迫轉型 AI / 矽光子（已成功），但 H1 營收下滑就是這個原因（Q3 FY2026 營收 YoY -44%）
- → 連 [[賣水人選股邏輯（投資版）]]：**「burn-in 設備賣水人」**——不押 NVDA vs AMD vs Google vs Microsoft 誰贏、押所有 AI 處理器 + 矽光子模組都需要 burn-in
- [[控制點轉移（投資版）]]：拿到「**WLBI for AI processors industry-first + 矽光子 burn-in chokepoint + Sonoma 2000W 平台**」三重控制點

### 供應層

- 跟 [[Tower Semiconductor]] / [[Coherent]] / [[Lumentum]] 關係（推測）：
  - **下游關係**：Tower / Coherent / Lumentum 做 wafer → Aehr 做 burn-in → 模組廠組裝
  - lead SiPho 客戶 follow-on order 推測來自其中之一（Tower / Coherent / Marvell）
- 跟 [[AAOI]] 關係（推測）：
  - **下游關係**：AAOI 做 InP / DFB / EML wafer → 模組廠或 Aehr 做 burn-in → hyperscaler 部署
- 跟 [[NVDA]] / [[Google]] / [[AWS|AMZN]] / [[Meta]] 關係：
  - **下游關係**：hyperscaler 自家 ASIC（TPU / Trainium / MTAI / Maia）由 [[TSMC]] / [[Samsung Electronics]] foundry 製造、然後送 Aehr 做 wafer-level burn-in
- 跟 Advantest / Cohu：
  - **直接競爭**（同層）
  - **Advantest**（日本）：logic SoC test 主場、burn-in 是次要業務、規模大但矽光子 burn-in 沒有 Aehr 先進
  - **Cohu**（COHU、美國）：handler 主場、burn-in handler 是業務之一、與 Aehr 有 overlap 但路線不同
  - **Aehr**：**WLBI + 矽光子 burn-in + SiC burn-in 三個利基市場**先發優勢
- pump laser / EML / DFB epi vs burn-in 競爭地位：
  - **WLBI for AI processors industry-first**（CEO 原話）
  - **Sonoma 2000W per device**（業界少數能做這麼高功率的 PLBI）
  - **矽光子 burn-in 早期 anchor**（hyperscaler 多家正在 qualify）
  - **Taiwan SiC customer 新訂單**（FOX-XP 全資格化）
- 護城河：
  - **WLBI for AI processors industry-first IP**
  - **WaferPak 耗材年金 + 客戶 lock-in**（recipe 專屬）
  - **三大利基市場（SiC + AI ASIC + SiPho）分散風險**
  - **Sonoma 2000W per device 平台**（業界少數）
  - **Q3 FY2026 Book-to-Bill 3.5x+ + backlog $50.9M**（產能買斷訊號）
- 風險：
  - **客戶集中度高**：lead AI accelerator + lead SiPho + Taiwan SiC = 三家主力、若任一家異動影響大
  - **Advantest / Cohu 規模競爭**：規模較大的對手若加大 burn-in R&D、Aehr 先發優勢可能被超越
  - **FY 2026 H1 lead ON Semi 訂單下滑 = 營收 YoY -44%**（轉型陣痛）
  - **AI ASIC / 矽光子 ramp 時程不確定**：若 hyperscaler 部署延遲、burn-in 訂單延後
  - **Forward PE 2,106.61 + EPS 仍虧損**：估值無 anchor、純 thesis driven
  - **股價 12M +968%**：大部分 alpha 已釋放、追高空間有限
  - **WaferPak 耗材定價戰**：若 Advantest / Cohu 推類似耗材、價格被壓
- → 連 [[控制點轉移（投資版）]]：「**WLBI for AI processors industry-first + Sonoma 2000W + 三利基市場**」三重 anchor、但被 Advantest / Cohu 規模競爭

## 3. 財務狀態快照（As of 2026-06-08）

| 指標 | 數值 |
|---|---|
| 股價 | **USD $82.61**（2026-05-18 數據參考、近期區間） |
| 52 週區間 | **$8.02 → $102.48**（從低點漲 ~1,178%） |
| 12 個月漲幅 | **+968.54%** |
| 市值 | **USD $2.63B** |
| Forward PE (NTM) | **2,106.61**（虧損中、純成長 / thesis driven） |
| FY 2026 自家 guidance 營收 | **$45M-$50M**（high end of range）|
| Q3 FY2026 營收 | **$10.3M**（YoY -44%）|
| Q3 FY2026 bookings | **$37.2M** ⭐ |
| Q4 FY2026 訂單 | **$41M record（lead hyperscaler AI customer）** ⭐⭐ |
| Q3+Q4 FY2026 bookings 累計 | **$92M+** ⭐ |
| record backlog | **$50.9M** |
| Book-to-Bill Ratio | **3.5x+**（極度 supply constrained）⭐ |
| Q3 FY2026 矽光子訂單 | **multiple FOX-XP WaferPak 系統**（lead SiPho customer follow-on）|
| Q3 FY2026 SiC 訂單 | **Taiwan SiC customer FOX-XP**（Greater China EV）|
| Q3 FY2026 AI 訂單 | **$14M follow-on**（lead AI accelerator、9 顆 300mm wafer 平行）|
| 主要產品線 | **FOX-XP**（WLBI 旗艦）+ **FOX-NP**（單站 WLBI）+ **Sonoma**（PLBI、2000W）+ **WaferPak**（耗材）|
| 主要競爭 | Advantest（JP）+ Cohu（COHU）|
| Q4 預期 | **回到 non-GAAP profitability**（賣方共識）|

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ⚠️ Q3 FY2026 YoY -44%（轉型陣痛）、但 bookings $37.2M / Q4 $41M = **未來營收 ramp 中**、FY 2026 guidance $45-50M high end |
| 毛利率 | ⚠️ 短期毛利受訂單延後影響、Sonoma + FOX-XP ASP 高、SiPho / AI ramp 後毛利 ramp 可期 |
| OpEx | ⚠️ Sonoma + FOX-XP R&D 持續投入、矽光子 burn-in 新平台開發、fixed cost 重 |
| 營業利益 | ❌ FY 2026 H1 虧損、Q4 預期回到 non-GAAP profitability、轉盈時點 = Q4 FY2026 或 FY 2027 H1 |

→ **Re-rate 三角形 0-1/4**——**仍是 thesis 階段**：bookings 訊號強（$92M+ + Book-to-Bill 3.5x+）、但實質營收 ramp 尚未驗證。**option value 極高、估值無 anchor、純 thesis driven**。

### ✅ 催化

- 🆕 **Q4 FY2026 $41M record 訂單**（lead hyperscaler AI customer）⭐⭐
- 🆕 **Q3 FY2026 lead silicon photonics customer follow-on order**（從 sample → 量產）⭐⭐
- 🆕 **Q3 FY2026 $14M AI follow-on**（9 顆 300mm wafer 平行 burn-in）⭐
- 🆕 **Q3 FY2026 Taiwan SiC customer FOX-XP 新訂單**（Greater China EV）
- **Book-to-Bill 3.5x+ + backlog $50.9M record**（極度 supply constrained）
- **Q3+Q4 bookings 累計 $92M+**（vs 全年營收 $45-50M、超過全年 1.8x）
- **WLBI for AI processors industry-first**（CEO 原話、Aehr 先發）
- **多 hyperscaler qualifying**（Serenity 推文、未來訂單來自多家）
- **Sonoma 2000W per device**（業界少數能做高功率 PLBI）
- **Q4 預期回到 non-GAAP profitability**（賣方共識、轉盈訊號）
- **三大利基市場（SiC + AI ASIC + SiPho）成熟、不靠 ON Semi 一家**
- 對應 [[AI infra CapEx 三階段論]] 第三階段最關鍵 anchor 之一
- [[Serenity]] / [[Bottleneck Theory（瓶頸論）]] 第 6 層 Testing & Qualification 核心 chokepoint anchor

### ⚠️ 風險

- **FY 2026 H1 lead ON Semi 訂單下滑 = 營收 YoY -44%**（轉型陣痛、市場可能短期 derate）
- **AI ASIC / 矽光子 ramp 時程不確定**：hyperscaler 部署延遲 = burn-in 訂單延後
- **Advantest / Cohu 規模競爭**：若加大 burn-in R&D、Aehr 先發優勢可能被超越（Advantest 規模 ~ $10B / Cohu ~ $1.5B）
- **客戶集中度高**：lead AI + lead SiPho + Taiwan SiC = 三家主力、單客戶異動影響不對稱
- **Forward PE 2,106.61 + EPS 仍虧損**：估值無 anchor、any miss = -50% 級別回檔風險
- **股價 12M +968%**：大部分 alpha 已釋放、追高風險（52 週區間 $8 → $102 顯示 volatility 極大）
- **WaferPak 耗材定價戰風險**：對手若推類似耗材、價格被壓
- **下游 hyperscaler 自家 burn-in 內製化風險**：理論上 hyperscaler 規模夠大可以自建 burn-in 設備（但實際難度極高、短期無風險）
- **矽光子 burn-in market timing 不確定**：CEO 自陳「multi-year opportunity」、但實際量產營收化可能延後 2-3 年

## ⭐ Serenity 重押論述

[[Serenity]] (@aleabitoreddit) 於 2026 年公開推文點名 AEHR、被列為 **Bottleneck Theory「核心持倉」**之一。

### Serenity 對 AEHR 的 reasoning

從 [[Serenity]] 公開 X 推文整理：

1. **Serenity 原推（2026-X 推文）**：
   > "Well that was fast with $AEHR. Up +14.28%… I did think the center of the next silicon photonics bottleneck at $1.1B, with tons of hyperscalers qualifying it. Was kind of undervaluing it."
   - **意涵**：Serenity **承認自己低估 AEHR**（$1.1B 市值時、現在已 $2.63B）
   - 「**矽光子下個瓶頸的中心**」= 第 6 層 Testing & Qualification 核心 chokepoint
   - 「**tons of hyperscalers qualifying it**」= 多 hyperscaler 同時測試 Aehr 設備、未來訂單來自多家
2. **第 6 層 Testing & Qualification 核心 chokepoint 定位**
   - **意涵**：Bottleneck Theory 7 層中、第 6 層測試 + 驗證是**最容易被忽視但物理上 indispensable 的一層**
   - 沒有 burn-in = hyperscaler 不部署、AI ASIC + 矽光子模組無法商用化
   - Aehr 是「**矽光子 burn-in 早期玩家 + WLBI for AI processors industry-first**」雙重身分
3. **「multiple hyperscalers qualifying」+ 「$1.1B 小市值」= 早期賽道 anchor**
   - **意涵**：早期 chokepoint + 多 hyperscaler qualify = 訂單從 sample → 量產轉換時、營收爆發
   - Serenity 「**早期 stage where it's getting tested by major hyperscaler supply chains for optical transceivers/silicon photonics before the mass volume inflection point**」
4. **5x → 50x 期權型 alpha 機會**
   - **意涵**：在 5 家 Serenity 重押中、AEHR 與 [[SIVE]] 都是「**早期 chokepoint + 小市值 + 純 thesis driven**」期權型
   - 12 個月 +968% 已釋放部分、但若量產訂單 anchor 進場、後續仍可能再翻 2-3 倍

### Serenity 五家 risk spectrum 中 AEHR 位置

| 公司 | Bottleneck Theory 層 | beta | Serenity 標籤 |
|---|---|---|---|
| [[AXTI]] | L1 + L3 | 超高 beta | core（InP 雙頭壟斷）|
| [[SIVE]] | L4 | 超高 beta | core（CW DFB 純 chokepoint）|
| **AEHR** | **L6** | **超高 beta** | **core（矽光子 burn-in 早期、$1.1B → $2.63B、Serenity 承認低估）**|
| [[AAOI]] | L5 + 跨 L4 | 中 beta | core（vertical integration）|
| [[Tower Semiconductor]] | 跨 L4-L5 | 低 beta | Safest Long（defensible compounder）|

→ **AEHR 是 Serenity 框架中第 6 層 Testing & Qualification 的唯一 anchor**、純期權型 alpha 但風險最濃（無估值錨點 + 客戶高度集中）。

## ⭐ 在 Bottleneck Theory 7 層的位置

| 層 | Chokepoint | AEHR 位置 |
|---|---|---|
| 1. Raw Materials | Ga/In/As 採礦 + 純化 | ❌ 不在 |
| 2. Growth Equipment | pBN crucibles (Shin-Etsu) | ❌ 不在 |
| 3. InP Substrate | [[AXTI]] + Sumitomo Electric | ❌ 不在 |
| 4. Laser Sources (CW DFB) | [[SIVE]] / [[Lumentum]] / [[Coherent]] | ❌ 不在 |
| 5. Optical Transceivers | [[AAOI]] / [[Lumentum]] / [[Coherent]] | ❌ 不在 |
| **6. Testing & Qualification** | **AEHR** | ⭐⭐ **唯一 anchor**（WLBI for AI processors industry-first + 矽光子 burn-in 早期）|
| 7. Optical Cable & Fiber | [[Corning]] | ❌ 不在 |

→ **AEHR 是第 6 層 Testing & Qualification 唯一純 chokepoint anchor**。

→ vs [[Tower Semiconductor]]：兩者位階完全不同——Tower 是 SiPho wafer foundry、AEHR 是 wafer 做完後的 burn-in 設備供應商、**上下游關係**（Tower 做 wafer → AEHR 做 burn-in → 模組廠組裝 → hyperscaler 部署）。

→ vs Advantest / Cohu：同層直接競爭、Aehr 在矽光子 + SiC + AI ASIC 三利基市場先發、規模較小但純度高。

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | **4** | burn-in 是 AI ASIC / 矽光子 商用化物理前提、敏感但偏 lagging indicator（晶片量產後 1-2 季） |
| 站別關鍵 | **5** | 第 6 層 Testing & Qualification 唯一 anchor、WLBI for AI processors industry-first |
| 耗材 | **5** | WaferPak 耗材年金 + 客戶 recipe lock-in + Sonoma 2000W 設備 ASP 高 |
| IP | **4** | WLBI + 矽光子 burn-in 先發 IP、但 Advantest / Cohu 規模壓力 |
| 客戶分散 | **2** | lead AI + lead SiPho + Taiwan SiC = 三家主力、單客戶異動影響不對稱、多 hyperscaler qualify 但量產訂單未集中 |

**總分：20/25**

### vs 5 家 Serenity 重押對照

| 軸 | TSEM | AAOI | AEHR | IQE | LITE | COHR | 說明 |
|---|---|---|---|---|---|---|---|
| 路線敏感 | 4 | **5** | 4 | 4 | 4 | 4 | AAOI 客戶端最敏感 |
| 站別關鍵 | 4 | 4 | **5** | 4 | **5** | 4 | LITE 200G EML + AEHR 第 6 層唯一 anchor |
| 耗材 | **5** | 4 | **5** | 3 | 3 | 3 | TSEM SiPho 預付款 + AEHR WaferPak 耗材年金 |
| IP | 4 | 4 | 4 | 4 | **5** | 4 | LITE InP 純度勝 |
| 客戶分散 | **5** | 1 | 2 | 2 | 2 | **4** | TSEM 多客戶分散最佳 |
| **總分** | **22/25** ⭐⭐ | 18/25 | **20/25** | 17/25 | 19/25 | 19/25 | AEHR 20 介於 Tower 22 與 AAOI 18 之間 |

→ **AEHR 20/25 = 5 家 Serenity 重押中第二高**（vs TSEM 22 / LITE 19 / COHR 19 / AAOI 18 / IQE 17）——反映 AEHR 是「**第 6 層唯一 anchor + 耗材年金 + 路線敏感雙腳**」、但客戶集中度拉低總分。

→ **AEHR 5 軸 vs Tower 對照**：TSEM 「耗材 + 客戶分散」雙滿、AEHR 「站別 + 耗材」雙滿——兩者不同軸的 chokepoint 強度。

## 跟其他 wiki 概念連結

- [[Serenity]] / [[Bottleneck Theory（瓶頸論）]]：**第 6 層 Testing & Qualification 唯一 anchor、矽光子 burn-in 早期玩家**
- [[AI infra CapEx 三階段論]]：第三階段最關鍵 anchor 之一（burn-in 是 AI ASIC + 矽光子模組商用化物理前提）
- [[CPO 供應鏈圖譜]]：第 6 層測試 + 驗證 anchor、補位 [[Lumentum]] / [[Coherent]] / [[Tower Semiconductor]] 下游
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：1.6T → 3.2T 模組商用化需 burn-in、AEHR 受益
- [[Tower Semiconductor]]：上下游關係——Tower 做 SiPho wafer、AEHR 做 burn-in
- [[Lumentum]] / [[Coherent]] / [[AAOI]]：上下游關係——wafer / chip → AEHR burn-in → 模組廠組裝
- [[SIVE]]：上下游關係（SIVE CW DFB laser → AEHR burn-in）
- [[IQE]]：平行賽道（IQE 做 epi wafer、AEHR 做 burn-in、上下游）
- [[NVDA]] / [[Google]] / [[AMZN]] / [[Microsoft]]：下游客戶（hyperscaler ASIC burn-in）
- [[TSMC]] / [[Samsung Electronics]]：上游 foundry（晶片做完送 AEHR 做 wafer-level burn-in）
- [[SiTime]] / [[MPS]]：同層「賣水人」對照（不同位階、不同 chokepoint）
- [[半導體基礎建設化]]：burn-in 從 niche 變成 AI / 矽光子量產物理前提
- [[賣水人選股邏輯（投資版）]]：**「burn-in 設備賣水人」**——不押 NVDA vs Google 誰贏、押所有 AI 處理器都需要 burn-in
- [[控制點轉移（投資版）]]：「WLBI for AI processors industry-first + 矽光子 burn-in chokepoint + Sonoma 2000W」三重控制點
- [[市場四階段：懷疑／驗證／共識／反轉]]：在「驗證 → 共識」加速段
- [[資訊擴散四階段]]：12M +968% 已過 KOL / 機構發掘段、進入「共識」段
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 強制格式
- [[Jevons Paradox（投資版）]]：burn-in 從 niche 變成 AI 算力 anchor = 反直覺賽道結構性放大

## 相關連結

- [[Serenity]]
- [[Bottleneck Theory（瓶頸論）]]
- [[AI infra CapEx 三階段論]]
- [[CPO 供應鏈圖譜]]
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]
- [[Tower Semiconductor]]、[[Lumentum]]、[[Coherent]]、[[AAOI]]、[[IQE]]、[[SIVE]]、[[AXTI]]
- [[NVDA]]、[[Google]]、[[AMZN]]、[[Microsoft]]
- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]

## Source URLs

- Aehr Test Q3 FY2026 8-K SEC filing: https://www.sec.gov/Archives/edgar/data/0001040470/000165495426000197/aehr_ex991.htm
- Aehr Test Q3 FY2026 Earnings Call Transcript (Motley Fool): https://www.fool.com/earnings/call-transcripts/2026/04/08/aehr-test-aehr-q3-2026-earnings-call-transcript/
- Aehr Test Q3 FY2026 Earnings Call (Investing.com): https://www.investing.com/news/transcripts/earnings-call-transcript-aehr-test-systems-q3-2026-reports-mixed-results-93CH-4601816
- Aehr Test $37M Quarterly Bookings (2026-04 AEHR Press Release): https://www.aehr.com/2026/04/aehr-test-systems-reports-over-37-million-in-quarterly-bookings-driven-by-strong-ai-and-data-center-infrastructure-demand/
- Aehr Receives $41M Record Production Order (2026-04 AEHR Press Release): https://www.aehr.com/2026/04/aehr-receives-record-41-million-production-order-from-lead-hyperscale-ai-customer-second-half-bookings-exceed-92-million/
- Aehr Secures Key AI Production Burn-in Win Sonoma Initial Order (2026-02 AEHR PR): https://www.aehr.com/2026/02/aehr-secures-key-ai-production-burn-in-win-with-initial-order-of-sonoma-systems-for-lead-hyperscale-customers-next-generation-ai-asic-processors/
- Aehr $5.5M Sonoma Ultra-High-Power Orders (2026-01 AEHR PR): https://www.aehr.com/2026/01/aehr-announces-over-5-5-million-in-sonoma-ultra-high-power-system-orders-to-test-and-burn-in-ai-processors-introduces-new-fully-automated-sonoma-for-next-generation-ai-applications/
- Aehr Test Q2 FY2026 Reinstates Guidance (Access Newswire): https://www.accessnewswire.com/newsroom/en/industrial-and-manufacturing/aehr-test-systems-reports-fiscal-2026-second-quarter-financial-results-1125687
- Aehr Test Q1 FY2026 (AEHR PR): https://www.aehr.com/2025/10/aehr-test-systems-reports-fiscal-2026-first-quarter-financial-results/
- Aehr Test Q3 FY26 Recap (CoinCentral): https://coincentral.com/aehr-test-systems-aehr-stock-surges-27-after-q3-earnings-beat/
- Aehr Test Q3 FY26 Earnings Report (Alphastreet): https://news.alphastreet.com/aehr-earnings-everything-you-need-to-know-about-aehr-test-systems-q3-fy26-report/
- Aehr Test Q3 Earnings Call Highlights (Ticker Report): https://www.tickerreport.com/banking-finance/13401189/aehr-test-systems-q3-earnings-call-highlights.html
- Aehr Test (AEHR) Hidden Gatekeeper AI Chip Reliability (Yianisz Substack): https://yianisz.substack.com/p/aehr-test-systems-aehr-the-hidden
- Aehr Test Yahoo Finance: https://finance.yahoo.com/quote/AEHR/
- Aehr Test Stock Statistics (StockAnalysis): https://stockanalysis.com/stocks/aehr/statistics/
- Serenity X "AEHR +14.28% silicon photonics bottleneck $1.1B" tweet: https://x.com/aleabitoreddit/status/2041157377928700262
- Serenity Tracker Semiconstocks: https://semiconstocks.com/
- Inside Serenity's Mind (Singularity Research Substack): https://singularityresearchfund.substack.com/p/inside-the-mind-of-serenity-aleabitoreddit
- Serenity Bottleneck Hunter (Johnson Lee): https://johnsonlee.io/2026/06/06/serenity-methodology-cannot-be-skill.en/

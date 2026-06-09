---
title: Hyper Rail / Multi-Rail（光通訊整合技術）
aliases: [Hyper Rail, Multi-Rail, Hyperscale Multi-Rail, RLS Hyper-Rail, 光通訊整合, 多軌光通訊]
type: concept
created: 2026-06-05
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-12-09
expires_on: 2027-12-31
sources:
  - raw/2026-06-05_Leo-DCI-Hyper-Rail-CIEN-COHR-LITE-NOK.md
  - raw/2026-05-20_FOMOSOC-48-DCI-Nokia-Cisco.md
evidence_url: https://www.ciena.com/insights/what-is/what-is-hyper-rail-or-multi-rail
tags: [光通訊, DCI, Hyper Rail, Multi-Rail, pump laser, EDFA, CPO, scale across, AI infra]
confidence: high
---

# Hyper Rail / Multi-Rail（光通訊整合技術）

## 一句話

> **Hyper-Rail（CIEN）/ Multi-Rail（NOK）= 把 EDFA 光放大器 / WSS 從「一模組一光纖對」整合成「一模組多光纖對」，把整柜密度推到 128-160 fiber pairs / rack。是 DCI 與 [[scale across]] 的關鍵 enabler。**

兩者**同一個架構概念、不同廠商命名**——Ciena 叫 Hyper-Rail（先發、命名權），Nokia 叫 Multi-Rail（業界中性名）。Ciena 的「Hyper」是 marketing 修飾語，Nokia 是 OFC 業界 MSA 用語。

## 技術原理（補完 Leo 直覺）

### Leo 原直覺：「pump laser 整合 + 多光纖共用 pump laser」

對。但更精確的技術描述是：

```
傳統 DWDM 線路系統:
1 module = 1 rail = 1 fiber pair
  ├─ 專屬 EDFA 放大器（內含 pump laser）
  ├─ 專屬 WSS（波長選擇開關）
  └─ 專屬監控

Multi-Rail / Hyper-Rail:
1 module = 4 rails = 4 fiber pairs（quad-WSS）
  └─ 部份共用：WSS 用一個 LCOS（液晶反射面）同時處理多 pair
  └─ EDFA 仍每 pair 一組 pump，但整合在同個 1U 機框
  └─ 機架密度從 ~32 fiber pairs/rack → 128-160 fiber pairs/rack
```

### 關鍵 enabler：LCOS WSS 像素提升

WSS（Wavelength Selective Switch）裡的 LCOS 陣列像素提升後，**單一 LCOS 面板可以同時處理 2-4 個 C+L band fiber pair**，這是「quad-WSS」/「octal-WSS」可行的物理基礎——不是省 pump laser，是省 WSS 模組。

### ASP 提升原因

- **單機規格升級**：從「賣一個 rail」變「賣一個 4-rail 機框」，單機售價跳階
- **整合度溢價**：把空間、能耗、安裝成本都包進報價
- **75% 省電 / 85% 省空間**（Ciena 數據）→ TCO 賣點支撐高單價

## scale up / scale out / scale across 三層架構

這是 [[NVDA]] 系統架構詞彙（Spectrum-X / Quantum-X 路線），DriveNets 寫成業界標準定義。

| 層 | 範圍 | 技術 | 距離 | 代表玩家 |
|---|---|---|---|---|
| **Scale Up** | 單機箱 / rack | NVLink、銅互聯、CPO（intra-rack） | <2 m | NVDA NVLink、LITE 光引擎 |
| **Scale Out** | 跨 rack / 單 DC | InfiniBand / Ethernet、CPO（inter-rack） | <100 m | NVDA Quantum-X、AVGO Tomahawk |
| **Scale Across** ⭐ | **跨 DC / 跨園區**（80km - 1000km+） | DCI 線路系統（DWDM + 多 rail 放大） | 80-1000 km | **[[CIEN]] Hyper-Rail、[[NOK]] Multi-Rail** |

→ **Hyper-Rail / Multi-Rail 是「scale across」唯一的指標性技術**。Scale up 跟 scale out 有 NVDA 系統內含解，scale across 一定要外部光通廠商，這是 Ciena / Nokia / Lumentum / Coherent 的賽道控制點。

## CIEN Hyper Rail vs NOK Multi Rail

| 維度 | CIEN RLS Hyper-Rail | NOK 1830 GX Multi-Rail |
|---|---|---|
| **平台** | 6500 RLS（Reconfigurable Line System） | 1830 GX RD66 / D2ILA |
| **密度** | 128 fiber pairs / rack | **160 fiber pairs / rack** |
| **密度倍數** | 32x today's | **40x today's** |
| **模組單位** | 1U / 4 rails | 1U / 4 rails |
| **發表場合** | 2026 Q1 / Ciena 自家 | 2026-03 OFC（業界場） |
| **首單** | hyperscaler 已下首單（未公布名字） | 未公布首單 |
| **量產時程** | **2027 開始部署**（Ciena Q2 2026 法說會確認） | **2026 H2 GA**（in-line amplifier） |
| **覆蓋頻段** | C+L band | C+L 9.6 THz / fiber |
| **單 fiber 容量** | 1.6 Tb/s ZR/ZR+ | 51.2 Tb/s（800G）／ 76.4 Tb/s（1.2T） |
| **市場定位** | AI hyperscaler 跨 region | hyperscaler + telco 共用 |

### 真實差異（不是相同概念不同名）

1. **時程倒過來**：NOK 出貨早一年（2026 H2 in-line amplifier），CIEN 2027 才開始大規模部署——但 Ciena **首單已在手**、Nokia 還在 GA 階段。
2. **路線差**：Nokia 把整套堆疊（line system + transponder + coherent engine）2027 才 GA；Ciena 是 RLS 平台延伸（Hyper-Rail 是 6500 系列升級），所以 Ciena 可以分階段部署。
3. **密度差**：Nokia 160 vs Ciena 128（NOK 多 25%），但 Ciena 跟 hyperscaler 設計合作較深、已拿到 design-in。

→ **Leo 原判斷「概念相同」基本對，但時程與商業位階上 Ciena 領先、Nokia 規格更激進**。

## 量產時程驗證

| 廠商 | 階段 | 時點 | 來源 |
|---|---|---|---|
| **CIEN** | 首單已下 | 2026 Q2 法說會宣布 | Ciena Q2 2026 earnings call |
| **CIEN** | 開始部署 | **2027 起跑** | Ciena 高層法說會原話「Hyper-Rail will begin to be rolled out as Ciena goes through 2027」 |
| **CIEN** | 訂單規模 | **hundreds of millions over multiple years** | Ciena 法說會 |
| **NOK** | Multi-Rail in-line amp GA | **2026 H2** | OFC 2026-03 發表 |
| **NOK** | Coherent solutions GA | 2027 H2（mid-2027 sampling） | Nokia 新聞稿 |

→ **Leo 兩個時點都對**，但要注意 Ciena 是「2027 起跑、多年放量」、Nokia 是「2026 H2 出貨」指的只是 in-line amplifier 那一塊。

## 對光通訊供應鏈的影響

| 受惠位 | 邏輯 | 主要玩家 |
|---|---|---|
| **系統整合商**（DCI 線路系統） | Hyper-Rail / Multi-Rail 直接供應者 | **[[CIEN]]**、**[[NOK]]**、Infinera（已併 Nokia） |
| **Pump laser 元件**（980 nm / 14xx nm） | EDFA 內含 pump，每 rail 仍要 pump | **Lumentum (LITE)**、**Coherent (COHR)** |
| **InP 雷射晶圓** | pump laser 上游 | COHR 6" InP wafer / LITE 3" InP（產能 2027 翻倍） |
| **Narrow-linewidth laser** | CPO 時代 ELS / 高品質光源 | LITE（FY26 Q3 出貨 +120%）、AOI |
| **DSP / coherent engine** | 跑 1.6T ZR/ZR+ | Marvell、Acacia（內製） |
| **Timing** | 高頻光通訊時脈基礎 + 光學晶振 niche（NDK 差異化）| [[SiTime]]（MEMS 高端）+ [[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]]（石英陣營五家、2026-06-09 #H1、**NDK 光學晶振 niche 直接受惠 1.6T 光模組 ramp**）|
| **連接器** | 高密度光纖配線 | Amphenol、Senko |

### 對 [[CPO 供應鏈圖譜]] 第 2 層（光引擎）的補強

[[CPO 供應鏈圖譜]] 原本第 2 層光引擎只標 LITE / COHR / 博通自研。Hyper-Rail / Multi-Rail 揭露：

1. **LITE / COHR 的 pump laser 業務不會被 CPO 整合掉**——CPO 是 intra-rack scale up，Hyper-Rail 是 inter-DC scale across，**兩條獨立曲線**。
2. COHR 2026 出貨已驗證：Lumentum 元件業務 Q3 FY2026 +77% YoY、**pump laser 出貨 +80%、narrow-linewidth laser +120%**。
3. **demand-supply gap 持續擴大**（Lumentum 自承）→ 給 ASP 提升 + 雙位數年增的雙引擎。

→ CPO 供應鏈圖譜應該補一句：**第 2 層的 pump laser 元件不只受惠於 CPO，更受惠於 DCI Hyper-Rail / Multi-Rail 第二增長曲線**。

## 為什麼這是「scale across」指標性技術

1. **物理瓶頸已到**：銅互聯 <2m、CPO 散熱限制 ~100m，**跨 80km 以上必走光通 + 放大**。NOK 文件明寫「網路 span >80km 必設 amplifier hut」。
2. **AI 訓練分散到多 DC**：單一 DC 電力/腹地不夠，超大模型訓練被迫跨園區（[[資本重分配（從人力到算力）]]）。
3. **NVDA Spectrum-XGS 開背書**：NVDA 自家把 scale across 列為 Rubin 平台關鍵——但 NVDA **不做光通系統**，這塊外包給 Ciena / Nokia。
4. **與 CPO 互補**：CPO 解 intra-rack，Hyper-Rail 解 inter-DC，**兩者並非替代而是堆疊**。
5. **OCI MSA 業界共識**：AMD、Broadcom、NVDA、hyperscaler 已組 Optical Compute Interconnect MSA 制定 scale up 用 CPO 標準——scale across 留給 DCI 廠商。

## Jevons Paradox 驗證

Leo 原判斷：**pump laser 用量會反而上升**。**校準後是對的**，但需要拆解。

### 校準：兩個方向同時發生

**直覺方向（單機效率提升）**：
- 1 個 4-rail 模組 → pump laser 仍每 rail 一組 → **單機 pump laser 數量不變**
- 但 1U 取代 4U → **「per rail 的 pump laser 數量沒變、per 1U 的 pump laser 數量 4x」**

**反直覺方向（[[Jevons Paradox（投資版）]]）**：
- CSP 因為密度提升敢部署更多 rail（每 rack 從 ~32 → 128-160）→ **整體 pump laser 用量 4-5x**
- CIEN 自承訂單外溢到 NOK——**整個賽道 supply 跟不上 demand**
- LITE Q3 FY2026 pump laser 出貨 **+80% YoY** = Jevons 已經在 P&L 上印證

### 倍數估計

```
傳統部署：1 rack = 32 fiber pairs = 32 個 pump laser（rough）
Hyper-Rail：1 rack = 128 fiber pairs = 128 個 pump laser
+ CSP 密度提升 → 部署 rack 數也增加（假設 +50%）
→ 整體 pump laser TAM ≈ 4x × 1.5x = 6x 區間（單純算術，不含 ASP）

LITE 實際出貨數據 +80% YoY ≈ 介於「傳統部署」與「Hyper-Rail 部署」之間的過渡期，
符合 Jevons 路徑。
```

⚠️ **這只是 rough estimate，沒有官方 TAM 數字確認**。

→ Leo 的「pump laser 用量會反而上升」**判斷正確、量級保守**。實際倍數可能是 4-6x（多年累計），而非簡單的 +20-30%。

## 跟 [[CPO 供應鏈圖譜]] 七層的關係

| CPO 七層 | Hyper-Rail / Multi-Rail 是否同層 |
|---|---|
| 1. 交換 ASIC | ❌（DCI 用 OTN switch，不是 ASIC） |
| 2. **光引擎** | ✅ pump laser、EDFA、narrow-linewidth laser **直接受惠** |
| 3. DSP | ✅（1.6T ZR/ZR+ 需要 coherent DSP） |
| 4. Timing | ✅（高頻時脈支持 1.6T） |
| 5. 先進封裝 | ❌（系統級不下沉到 chiplet） |
| 6. 連接器 | ✅（高密度光纖配線新 form factor） |
| 7. 電源 | ✅（中性受惠） |
| 8. 玻璃中介層 | ⚠️ 系統級不直接，但跟 CPO 在同個 hyperscaler 設計 |

→ **Hyper-Rail 受惠第 2、3、4、6、7 層**，與 CPO 並非替代——是 CPO 在 inter-rack 失靈時的「上層接駁技術」。

## 跟其他 wiki 概念連結

- [[CPO 供應鏈圖譜]]：本技術強化第 2 層 pump laser TAM、補光通元件第二曲線
- [[Jevons Paradox（投資版）]]：本技術經典案例，pump laser 反向放大需求
- [[控制點轉移（投資版）]]：scale across 控制權在 DCI 廠商（CIEN/NOK），不在 NVDA
- [[半導體基礎建設化]]：DCI 是 AI infra 的關鍵層、進入 infra 重估範圍
- [[賣水人選股邏輯（投資版）]]：CIEN/NOK/LITE/COHR 是 scale across 賽道四象限賣水人
- [[TGV × CPO 依賴圖]]：Hyper-Rail 不依賴 TGV，但與 CPO 在同一 hyperscaler design wins 池
- [[預期差]]：市場常把「光通元件整合」直覺解讀成需求下降，Jevons 製造預期差
- [[資訊擴散四階段]]：Hyper-Rail 在 2026 仍處「驗證」階段，未進共識

## ⭐ FOMO SOC #48 校準（2026-06-09 ingest）

KP@FOMOSoc 第 48 期「**DCI + Nokia + Cisco**」（2026-05-20）強化既有 concept：

### 1. 「AI 網路三層架構」術語確認

| 層 | 範圍 | 廠商主場 | KP 點出 |
|---|---|---|---|
| **Scale-up** | 機架內 GPU 互連 | NVDA NVLink | scale-up |
| **Scale-out** | 機房內互連 | AVGO / Marvell ASIC | scale-out |
| **Scale-across** ⭐ | **資料中心間互連（新戰場）** | **[[Ciena]] / [[Nokia]] / [[Cisco]]** | scale-across（新瓶頸） |

→ KP 把「scale-across」明確列為「**AI 算力時代的新瓶頸**」、跟 wiki 既有「scale up / out / across 三層架構」段一致、但 KP 把「**Cisco 列為第三軌補強位**」是本次校準新加。

### 2. 「單一 DC 無法容納百萬 GPU」物理瓶頸 anchor

KP 原話：「**單一資料中心無法容納百萬 GPU 規模、需要跨資料中心互連技術形成超級電腦**」+「**AI 訓練流量牽一髮而動全身、對延遲 / 無損傳輸要求遠超傳統人類流量網路**」= scale-across 的核心物理 thesis。

### 3. 三家分食架構補位 [[Cisco]]

既有 concept 主要對比 CIEN（純度王）vs NOK（廣度王），本次補入 **[[Cisco]]**：

| 公司 | DCI 純度 | 估值（Fwd PE）| 客戶集中度 | 業務多元緩衝 | AI 紅利 | 關鍵差異 |
|---|---|---|---|---|---|---|
| [[Ciena]] | **5/5（純）** | 80-91x | 1/5 | 1/5 | **5/5** | DCI 純度王 + HyperRail co-developed |
| [[Nokia]] | 2/5（多元）| 43x | 4/5 | 4/5 | 3/5 | 廣度王 + 三張牌（Infinera + NVDA $1B + 7220 IXR-H6）|
| **[[Cisco]]** | **2/5（多元）** | **~17x** | 4/5 | **5/5** | **1/5** | **估值便宜對沖位、AI 紅利吃不到** |

→ KP 把 Cisco 列為「DCI 賽道補強位 + 估值便宜對沖」、付費牆後可能揭示完整 Cisco 對沖邏輯（Splunk SecOps + Silicon One + Nexus 9k）

### 4. Nokia 7220 IXR-H6 102.4 Tb/s 交換器補入（DCI 概念延伸）

KP 點出 Nokia 第三張牌：**7220 IXR-H6 資料中心交換器、102.4 Tb/s 吞吐量、符合 Ultra Ethernet 規範、直接對標 Cisco / Arista**——是「scale-out」交換器層、與「scale-across」line system 形成 Nokia 在 hyperscaler 資料中心的**雙產品線交叉**。

## 待 ingest 延伸

- entity [[CIEN]]（Ciena）— Q2 2026 法說會 Hyper-Rail thesis、hyperscaler 首單、$1.57B Q2 營收 +40% YoY
- entity [[NOK]]（Nokia）— OFC 2026 Multi-Rail 發表、Infinera 整合
- entity [[Lumentum LITE]]— Q3 FY2026 元件 +77%、pump laser +80%、narrow-linewidth +120%
- entity [[Coherent COHR]]— InP 6" wafer 2027 翻倍、SiC 副線、pump laser 競爭位
- entity [[scale across]]（概念）— NVDA Spectrum-XGS / DriveNets 多 DC 連接定義

## 待校準

- ⚠️ **單機 pump laser 倍數**：本文「4-6x TAM」是 rough estimate，無官方 TAM 數據——找 LightCounting / Cignal AI 報告確認
- ⚠️ **NOK 與 CIEN 規格差異**：Nokia 1830 GX 跟 Ciena RLS 同 1U 4 rail，但 NOK 160 vs CIEN 128 差距是否反映 hardware roadmap 差或單純命名差，待後續法說會驗證
- ⚠️ **Intel 2023 LIDE-CPO 專利**對 Hyper-Rail 是否有引用——應該沒有（不同層），但 Leo 應 cross check

## 主要佐證來源

- [Ciena: What is multi-rail?](https://www.ciena.com/insights/what-is/what-is-hyper-rail-or-multi-rail) — 官方技術定義
- [Ciena: What is scale across?](https://www.ciena.com/insights/blog/2026/developing-the-first-tailored-optical-solutions-for-scale-across-ai-applications) — scale across 詞彙起源
- [Nokia: When AI meets line systems](https://www.nokia.com/blog/when-ai-meets-line-systems-scaling-faster-with-multi-rail-ols/) — Nokia Multi-Rail 立場
- [Ciena Q2 2026 earnings call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-ciena-q2-2026-beats-forecasts-but-stock-dips-93CH-4726909) — 2027 部署時程
- [Fierce: Ciena makes case for hyper-rail photonics](https://www.fierce-network.com/broadband/ciena-why-hyper-rail-photonics-are-critical-data-center-fiber-density)
- [Nokia 1830 GX RD66 D2ILA](https://www.nokia.com/asset/i/214971/) — Nokia Multi-Rail 平台
- [DriveNets: Scale-Up Scale-Out Scale-Across](https://drivenets.com/blog/hybrid-scaling-scale-up-scale-out-and-scale-across-gain-new-meaning/) — 三層架構業界標準定義
- [MapYourTech: Multi-Rail Line Systems](https://mapyourtech.com/multi-rail-line-systemsarchitectural-response-to-the-ai-driven-fiber-density-problem/) — 技術深度解析（quad-WSS、LCOS、C+L band）
- [Lumentum Q3 FY2026 Components revenue](https://www.theglobeandmail.com/investing/markets/stocks/COHR/pressreleases/1937682/lumentums-components-business-accelerates-more-upside-ahead/) — pump laser 出貨 +80% 驗證
- [Photoncap: 8 companies behind Lumentum's $808M quarter](https://photoncap.net/p/the-8-companies-behind-lumentums) — 元件供應鏈拆解

## 相關連結

- [[CPO 供應鏈圖譜]]
- [[Jevons Paradox（投資版）]]
- [[控制點轉移（投資版）]]
- [[半導體基礎建設化]]
- [[賣水人選股邏輯（投資版）]]
- [[TGV × CPO 依賴圖]]
- [[SiTime]]（MEMS）+ [[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]]（石英陣營五家、2026-06-09 #H1、**NDK 光學晶振 niche differentiator**）
- [[預期差]]

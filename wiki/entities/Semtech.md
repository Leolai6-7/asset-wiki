---
title: Semtech
aliases: [SMTC, Semtech Corporation, CopperEdge, FiberEdge, LoRa]
type: entity
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-12-10
sources:
  - https://www.theglobeandmail.com/investing/markets/stocks/SMTC/pressreleases/2161175/semtech-reports-record-q1-fiscal-2027-revenue-growth/
  - https://seekingalpha.com/news/4597199-semtech-forecasts-328m-q2-revenue-as-it-targets-35-percent-sequential-data-center-growth
  - https://www.fool.com/earnings/call-transcripts/2026/03/16/semtech-smtc-q4-2026-earnings-call-transcript/
  - https://www.stocktitan.net/sec-filings/SMTC/10-k-semtech-corp-files-annual-report-38ea86faac6a.html
  - https://www.tradingview.com/news/reuters.com,2025:newsml_L4N3P10R0:0-semtech-drops-after-lowering-copperedge-forecasts/
  - https://www.semtech.com/company/press/amphenol-semtech-introduce-1.6t-active-copper-cable-ofc-2025
  - https://stockanalysis.com/stocks/smtc/
tags: [標的, US, NASDAQ, 銅纜, ACC, redriver, linear TIA, LPO, LoRa, IoT, AI 數據中心, SemiAnalysis 銅纜受惠, CPO 延期受惠, #P1]
confidence: medium
---

# Semtech（NASDAQ: SMTC）

## 1. 一句話定位

**「光＋銅雙邊互連前端 IC 賣水人」**——FiberEdge linear TIA／laser driver（800G 主力、LPO/LRO 已過多家 hyperscaler 與模組廠認證）＋ CopperEdge 224G/lane ACC redriver（與 [[Amphenol]] 合推 1.6T OSFP ACC、號稱比 DSP 方案省 ~90% 功耗）＋ 自有 LoRa radio IP；FY2026 data center 營收 **$223M（+58% YoY）**、FY2027 公司目標**再 +50%+**；2025-02-10 曾因 [[NVDA]] rack 架構改版把 CopperEdge FY26 預期砍到 $50M floor 以下、**單日 -31%**（市值蒸發 $1.4B）、2026 以「某 hyperscaler 1.6T ACC + 1.6T FiberEdge」回血；[[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告]]銅纜板塊受惠名單**直接點名（Amphenol／Semtech／MACOM）**。

## 2. 三層 thesis

### 產業層
- CPO scale-up 推遲 2029+（綁 Feynman）→ **銅纜＋可插拔主流延長至 2028**：Semtech 兩邊都賣——銅（CopperEdge ACC）＋光可插拔前端（FiberEdge TIA/driver、LPO/LRO）= 報告受惠名單裡少數「光銅雙吃」者
- 224G SerDes 世代 passive DAC reach 縮短 → rack 內／鄰 rack 銅互連需要 ACC（redriver、低功耗低延遲）或 AEC（retimer、Credo 路線）補 reach = CopperEdge 的結構性 TAM
- LPO/LRO 若起量 = 去 DSP 化 → linear TIA／driver 價值上升（與 [[MACOM Technology]] 雙頭競爭）

### 目的層
- 營收結構（FY2026）：Industrial 55%／Infrastructure 30%／High-End Consumer 15%；三報告段（Signal Integrity／Analog Mixed Signal & Wireless／IoT Systems & Connectivity）各 >$300M
- **Data center 是唯一高速成長引擎**：FY2026 $223M（21% 營收）→ Q1 FY2027 $71.6M 創新高（24.6% 營收）→ Q2 guide 隱含 **+35% QoQ（~$97M）**
- LoRa = 自有 IP 年金（Q1 FY2027 LoRa-enabled +$5.7M YoY、第四代 LoRa Plus 平台）、成長慢但客戶長尾極分散

### 供應層
- CopperEdge 出貨路徑：IC → cable 廠（[[Amphenol]] 1.6T OSFP ACC、OFC 2025 合推）→ hyperscaler；**非 NVDA reference design**——2025 教訓：rack 架構單一決策可整段 design-out（GB200 改版後 passive copper 夠用）
- Q4 FY2026 法說（2026-03-16）：CopperEdge 1.6T ACC 開始對一家 hyperscaler 出貨、FY2027 H2 與 1.6T FiberEdge 同步加速；NVDA 鏈 design-in 實績**至今無公開證據（待補）**
- 競爭：ACC redriver vs Credo AEC（全 retimer）vs [[Marvell]]/Broadcom DSP-DAC；linear TIA vs [[MACOM Technology]]；自有 HieFo InP photonics 產線補光端

## 3. 財務快照（As of 2026-06-10）

| 指標 | 數值 |
|---|---|
| 股價／市值 | $157.52／**$14.67B**（52 週 $38.14–172.36） |
| Forward PE | **~53x**（GAAP TTM EPS -0.38 仍虧、non-GAAP 已獲利） |
| FY2026 營收（至 2026-01） | **$1,050M（+15.5% YoY）** |
| FY2026 data center | **$223M（+58% YoY）**、Q4 $63M 創高 |
| Q1 FY2027（至 2026-04） | **$291M（+16% YoY）**、non-GAAP GM 53.0%、non-GAAP EPS $0.51（+34%） |
| Q1 FY2027 data center | **$71.6M 創高**（800G 主力＋1.6T/LPO/LRO/CopperEdge 早期放量） |
| Q2 FY2027 guidance | **$328M ±$5M**（+13% QoQ）、EPS $0.61、data center 隱含 +35% QoQ |
| FY2027 公司目標 | data center **+50%+ YoY** |
| 分析師共識 | Strong Buy、目標價 $204.83（+30%） |

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | **4** | 光＋銅雙路線都賣＋LoRa/類比 55% 在 AI 外；但 2025-02 單日 -31% 證明銅端對單一 rack 決策極脆弱 |
| 站別關鍵 | **3** | linear TIA 與 MACOM 雙頭、ACC redriver 可被 passive DAC／AEC／DSP 繞過（2025 已演示一次） |
| 耗材 | **3** | per-link IC 隨每代 BOM 增、但單價低、data center 僅 ~25% 營收 |
| IP | **3-4** | LoRa radio IP 獨有＋linear equalizer 類比 IP＋HieFo InP；互連 IC 站競爭者多 |
| 客戶分散 | **4** | 三段各 >$300M、LoRa 長尾極散；惟成長引擎集中少數 hyperscaler |

**總分：17-18/25**（同級：[[AAOI]]／Innolight／[[鴻勁 7769]]／[[致茂 2360]] tier）

## 監控指標

| 指標 | 觸發行動 |
|---|---|
| Q2 FY2027（2026-08 法說）data center 是否達 ~$97M（+35% QoQ） | miss → FY2027 +50% 目標存疑、降 confidence |
| CopperEdge hyperscaler ACC 出貨 ramp（FY2027 H2 加速承諾） | H2 未加速 → 重演 2025「design win ≠ revenue」、砍銅端 thesis |
| NVDA Rubin/Kyber rack 互連選型（passive／ACC／AEC） | 納入 ACC → 站別關鍵上修；再次 design-out → 路線敏感降 1 |
| Credo AEC vs ACC redriver 份額 | AEC 全面壓倒 → CopperEdge TAM 收縮 |
| CPO 時程（基線 2029+ 綁 Feynman） | 提前 → FiberEdge 可插拔 TIA 受壓；再延 → 光銅雙受惠 |
| Forward PE ~53x vs data center 佔比僅 ~25% | data center 成長 <30% YoY → [[PE 壓縮公式]] 風險 |

## 相關連結

- [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]（銅纜受惠名單點名來源）
- [[CPO 供應鏈圖譜]]／[[賣水人選股邏輯（投資版）]]／[[Bottleneck Theory（瓶頸論）]]
- [[Amphenol]]（1.6T ACC 合作夥伴）／[[MACOM Technology]]（TIA＋銅雙線直接對手）／[[Marvell]]（DSP 路線對照）
- [[NVDA]]（2025 rack 改版 = 路線敏感活案例）／[[AAOI]]／[[Lumentum]]／[[Coherent]]（可插拔同受惠 cluster）
- [[資訊擴散四階段]]／[[市場四階段：懷疑／驗證／共識／反轉]]／[[Re-rate 捕捉法]]

## Sources

- [Semtech Q1 FY2027 業績（2026-05-26、Globe and Mail）](https://www.theglobeandmail.com/investing/markets/stocks/SMTC/pressreleases/2161175/semtech-reports-record-q1-fiscal-2027-revenue-growth/)
- [Q2 FY2027 guide $328M、data center +35% QoQ（Seeking Alpha）](https://seekingalpha.com/news/4597199-semtech-forecasts-328m-q2-revenue-as-it-targets-35-percent-sequential-data-center-growth)
- [Q4 FY2026 法說逐字稿（2026-03-16、Motley Fool）](https://www.fool.com/earnings/call-transcripts/2026/03/16/semtech-smtc-q4-2026-earnings-call-transcript/)
- [FY2026 10-K：營收 $1,050M、三段各 >$300M（StockTitan）](https://www.stocktitan.net/sec-filings/SMTC/10-k-semtech-corp-files-annual-report-38ea86faac6a.html)
- [Q1 FY2027 8-K（SEC）](https://www.sec.gov/Archives/edgar/data/0000088941/000008894126000009/smtc-04262026x8k991.htm)
- [2025-02 CopperEdge 下修 <$50M floor（Reuters/TradingView）](https://www.tradingview.com/news/reuters.com,2025:newsml_L4N3P10R0:0-semtech-drops-after-lowering-copperedge-forecasts/)
- [2025-02-10 單日 -31%、NVDA 改版歸因（MarketScreener）](https://www.marketscreener.com/quote/stock/NVIDIA-CORPORATION-57355629/news/Semtech-Stock-Sinks-After-Nvidia-Configuration-Change-49011720/)
- [CEO 承認 CopperEdge 延遲＋投資人訴訟（Hagens Berman）](https://www.kxnet.com/business/press-releases/globenewswire/9423706/semtech-smtc-ceo-acknowledges-copperedge-delays-amid-investor-lawsuit-hagens-berman/)
- [Amphenol × Semtech 1.6T OSFP ACC（OFC 2025）](https://www.semtech.com/company/press/amphenol-semtech-introduce-1.6t-active-copper-cable-ofc-2025)
- [CopperEdge 800G/1.6T 低功耗組合](https://www.semtech.com/company/press/copperedge-portfolio-low-power-800g-ai-data-centers)
- [OFC 2026：光＋主動銅纜雙線（Semtech blog）](https://blog.semtech.com/ofc-2026-semtech-advances-the-future-of-ai-data-center-optical-and-active-copper-interconnects)
- [DesignCon 2026：200G/lane linear interconnect（Semtech blog）](https://blog.semtech.com/designcon-2026-semtech-leads-the-charge-toward-200g-and-the-linear-interconnect-future)
- [SMTC 估值快照（StockAnalysis）](https://stockanalysis.com/stocks/smtc/)
- [Roth 會議：FY2027 data center +50% 目標（Yahoo Finance）](https://finance.yahoo.com/markets/stocks/articles/semtech-highlights-fy2026-surge-targets-131944091.html)
- [Q1 FY2027 deep dive（StockStory）](https://markets.financialcontent.com/stocks/article/stockstory-2026-5-27-smtc-q1-deep-dive-data-center-and-iot-momentum-drive-upside-capacity-expansion-in-focus)

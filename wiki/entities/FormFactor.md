---
title: FormFactor
aliases: [FormFactor, FORM, NASDAQ:FORM]
type: entity
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2027-02-15
sources:
  - https://www.stocktitan.net/news/FORM/form-factor-inc-reports-2026-first-quarter-ptznafssjeh9.html
  - https://www.globenewswire.com/news-release/2026/02/04/3232457/0/en/FormFactor-Inc-Reports-2025-Fourth-Quarter-Results.html
  - https://www.fool.com/earnings/call-transcripts/2026/04/29/formfactor-form-q1-2026-earnings-transcript/
  - https://www.stocktitan.net/sec-filings/FORM/10-q-formfactor-inc-quarterly-earnings-report-fd4f2595365c.html
  - https://www.kavout.com/market-lens/why-did-formfactor-stock-plummet-despite-record-q1-earnings
  - https://www.formfactor.com/press-release/formfactor-and-advantest-partner-on-silicon-photonics-wafer-level-test-cell-to-enable-high-volume-manufacturing/
  - https://www.globenewswire.com/news-release/2025/12/15/3205831/0/en/FormFactor-Expands-Silicon-Photonics-Test-Capabilities-With-Acquisition-of-Keystone-Photonics.html
  - https://www.thelec.net/news/articleView.html?idxno=5553
  - https://www.mordorintelligence.com/industry-reports/probe-card-market
  - https://www.gurufocus.com/term/forward-pe-ratio
tags: [標的, 美股, 半導體測試, 探針卡, probe card, MEMS, HBM, DRAM, CPO 測試, 矽光子, 量子, 檢測賣水人]
thesis_dependency: AI-capex
confidence: medium
---

# FormFactor（NASDAQ: FORM）

## 1. 一句話定位

**全球先進探針卡 #1（share ~23-28.5%、口徑不一）+ HBM wafer 級探針卡主導供應商 + CPO 雙面 probing 先行者**——SmartMatrix MEMS 卡通吃 SK hynix／Samsung／[[Micron]] 三家 HBM 廠；2024-11 與 [[Advantest]] 共建 SiPh wafer-level test cell（早 [[Teradyne]] Photon 100 約 16 個月）、2025-12 再併 Keystone Photonics；FY2025 營收 **$785.0M（+2.8%、歷史新高）**、Q1 2026 拐點放量 **$226.1M（+32% YoY）**、non-GAAP 毛利率 **49.0% 創高**（歷史長期卡在低 40s）。⚠️ 12M 股價約 **+3〜3.5 倍**（5/1 口徑 +354%）、Forward PE **~50x** = C 軸紅燈；SK hynix 單一客戶 **29.5%**。

## 2. 三層 thesis

| 層 | 內容 |
|---|---|
| 產業層 | HBM 堆疊層數↑ → known-good-stack 經濟學讓 wafer sort 強度結構性上升（HBM 卡最高 15 萬針、單價是 NAND 卡 2-3 倍）；探針卡是「ATE 與晶圓之間的介面耗材」、晶片每改版必換新卡 = [[檢測賣水人 pattern（良率地獄賣檢測）]] 的耗材版；[[AI 記憶體結構性供給短缺]] 下三家 HBM 廠同時擴產、卡需求齊升 |
| 目的層 | 路線中立三重保險：HBM 三家誰贏都買 FORM 卡（SmartMatrix 三家通吃）；F&L 端 GPU／ASIC／networking 誰贏都要 probe（Q1 26 F&L +YoY 大增靠 networking 卡、NVDA 首成 10% 客戶）；CPO vs pluggable 誰主流——CPO 贏則光電 probing 大爆發、延期則 HBM 基本盤照收（test insertion 1 = wafer 級 probe 被驗證為唯一 production-ready 插入點，insertion 2 客戶做不動） |
| 供應層 | **雙重角色 anchor**：與 Advantest＋Tokyo Electron 共同開發 Triton CPO 量產測試系統（2026 ramp 中）、同時探針卡本身 ATE 中立——Teradyne Photon 100 生態的 wafer probing 同樣繞不開雙面 probing 關鍵方。vs [[旺矽 6223]] 分工：FORM 吃 memory/HBM wafer 級 + IDM／NVDA F&L 大單，旺矽吃 CSP 委外 AI ASIC（>70%）+ CPC/VPC 細分。風險：韓系低價進攻（TSE 卡便宜 80%、Korea Instrument 過 Samsung DRAM/HBM 認證）、Technoprobe 在亞洲 foundry 帳戶搶份額 |

## 3. 財務快照（As of 2026-06-10）

| 指標 | 數值 | 備註 |
|---|---|---|
| FY2025 營收（至 2025-12）| **$785.0M（+2.8%）** | 歷史新高；全年平、Q4 起拐點（FY2024 $763.6M、+15.2%）|
| Q1 2026 營收 | **$226.1M（+32.0% YoY、+5.1% QoQ）** | 連兩季創高；Probe Cards $198.2M（**+45% YoY**）／Systems $27.9M（-19.9%）|
| Q1 2026 毛利率 | non-GAAP **49.0%（+510bps QoQ、創高）** | Probe Cards 段 50.5%；歷史長期低 40s = margin 壓力史，結構上移待確認 |
| Q1 2026 EPS | non-GAAP **$0.56**（GAAP $0.26、含 $23.3M 重組費）| vs Q1 25 $0.23 |
| 市場別（Q1 26）| F&L $111.2M（49%）／DRAM $82.9M（37%、**+69.7% YoY**）／Flash $4.1M／Systems 12% | DRAM 創紀錄 = HBM＋DDR4/DDR5 雙引擎 |
| HBM 營收 | Q3 2025 約 **$40M／季**；FY2024 全年成長 **4 倍**；FY2025 全年總額待補 | SmartMatrix 在三家 HBM 廠全數放量 |
| CPO 營收 | 2026 全年 guidance **$10-20M 區間高端**（公司口徑）| Triton（與 Advantest/TEL）ramp 中 |
| 客戶集中 | **SK hynix 29.5%＋NVIDIA 10.2%（Q1 26）**；FY2025 SK hynix 22.9%；Intel 已降 <10% | 微處理器 IDM 退位、記憶體集中度升 |
| Q2 2026 guidance | $240M ±$5M／GM 49.5% ±150bps／EPS $0.61 ±$0.04 | 續創高軌道 |
| 股價／估值 | ~$125（2026-06-08）；52 週高 $159.09（回檔 ~21%）；12M 約 +3〜3.5 倍（2026-05-01 口徑 +354%）；Forward PE **~50x**（trailing GAAP ~150x）| C 軸紅燈主證據 |
| 全球探針卡市佔 | **#1、~23-28.5%**（口徑不一；Technoprobe ~16.5-19%、MJC ~10-12%、JEM/MPI 各 4-6%）| TechInsights 客戶滿意度連 11 年第一 |

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感（逆向）| 4 | HBM 三家誰贏／GPU vs ASIC／CPO vs pluggable——誰贏都要 probe；扣 1：DRAM 週期與 AI capex 總量單一暴露 |
| 站別關鍵 | 4 | Wafer sort/CP = KGD 良率 gate；HBM wafer 級探針卡 dominant supplier（韓媒口徑）；CPO insertion 1 被驗證為唯一 production-ready 測試插入點 |
| 耗材 recurring | 5 | 探針卡 = design-specific 耗材（改版即換＋磨耗更換）、佔營收 ~88%；HBM 換代（HBM3E→HBM4→4E）即全面換卡、單價 2-3 倍於 NAND 卡 |
| IP | 4 | 全球 #1＋MEMS/SmartMatrix 三家 HBM 通吃＋Pharos/Apollo/Keystone 光電 probing 縱深；扣分：GM ~49% 低於旺矽 59%、Technoprobe＋韓系（TSE -80% 價格）低價進攻證明壁壘非鐵壁 |
| 客戶分散 | 3 | 跨 memory/F&L/Flash/Systems 多市場、Intel 退位後更多元；但 SK hynix 29.5% 單一暴露、前二客戶合計 39.7% |

**總分 = 20/25**（confidence: medium、單輪研究）——高於 [[旺矽 6223]] 19（耗材純度＋HBM 主導地位）、與 [[Advantest]] 20-21 同級、低於村田/Disco 24 級。⚠️ [[投資四元問題框架（ABCD）]]：A 成立；C 紅燈（12M +3 倍、Forward PE ~50x）；B 已過驗證期進共識期——用途偏記分板對照與回檔觀察名單、非追價標的。

## 監控指標

| 指標 | 觸發行動 |
|---|---|
| SK hynix 集中度（Q1 26 = 29.5%）| 突破 35% 或 HBM 砍單訊號 → 客戶分散軸 3→2、檢查 DRAM 週期頂 |
| CPO 訂單歸屬：Triton（FORM+Advantest+TEL）vs Teradyne Photon 100 | 誰拿 NVDA／TSMC COUPE 量產認證誰上修——[[CPO 供應鏈圖譜]] 第 9 層更新；FORM 探針卡兩邊都可能贏（雙重角色驗證點）|
| 2026 CPO 營收落點（guidance $10-20M 高端）| 達標＋2027 上修 → SiPh thesis 確認；跳票 → 回 HBM 基本盤估值 |
| 毛利率 49% 持續性（歷史低 40s）| 連兩季 <46% → margin 結構上移證偽、IP 軸降 1 |
| 韓系（TSE／Korea Instrument）＋Technoprobe 在 HBM/foundry 份額 | 韓廠切入 wafer 級 HBM 卡（現只在 diced-die 段）→ 競爭警報 |
| HBM4/4E 換代節奏與記憶體 capex | 換代＝換卡浪潮（上修）；memory capex 下行＝卡需求同步down（週期警報）|
| 旺矽 6223 法說對照 | 兩家 AI 探針卡動能背離 → 檢查 memory vs ASIC 段節奏差或份額移轉 |

## 相關連結

- [[檢測賣水人 pattern（良率地獄賣檢測）]]／[[賣水人選股邏輯（投資版）]]（選股邏輯母節點）
- [[CPO 供應鏈圖譜]]（第 9 層測試——wafer 級光電 probing 關鍵方）
- [[Advantest]]（Triton test cell 共同開發方）／[[Teradyne]]（Photon 100 對手盤、但 probing 仍可能用 FORM）
- [[旺矽 6223]]（探針卡台廠對照：memory/IDM vs CSP ASIC 分工）／[[穎崴 6515]]（封裝後 socket 端鏡像）
- [[SK Hynix]]／[[Micron]]（最大客戶群）／[[AI 記憶體結構性供給短缺]]（HBM 需求母題）
- [[投資四元問題框架（ABCD）]]（A 強 C 紅燈判定）

## Sources

- [FormFactor Q1 2026 earnings release：營收 $226.1M、non-GAAP EPS $0.56、GM 49%（StockTitan 2026-04-29）](https://www.stocktitan.net/news/FORM/form-factor-inc-reports-2026-first-quarter-ptznafssjeh9.html)
- [FormFactor Q4/FY2025 results：全年 $785.0M 創高（GlobeNewswire 2026-02-04）](https://www.globenewswire.com/news-release/2026/02/04/3232457/0/en/FormFactor-Inc-Reports-2025-Fourth-Quarter-Results.html)
- [Q1 2026 earnings call：CPO 2026 營收 $10-20M 高端、Triton 與 Advantest/TEL、Keystone 整合、insertion 1 vs 2（Motley Fool）](https://www.fool.com/earnings/call-transcripts/2026/04/29/formfactor-form-q1-2026-earnings-transcript/)
- [Q1 2026 10-Q：SK hynix 29.5%、NVIDIA 10.2%、市場別 breakdown（StockTitan）](https://www.stocktitan.net/sec-filings/FORM/10-q-formfactor-inc-quarterly-earnings-report-fd4f2595365c.html)
- [Kavout：Q1 創高但股價回檔——12M +354%、trailing PE ~156x、52 週高 $159.09（2026-05-01）](https://www.kavout.com/market-lens/why-did-formfactor-stock-plummet-despite-record-q1-earnings)
- [FormFactor × Advantest SiPh wafer-level test cell（2024-11-07 官方新聞稿）](https://www.formfactor.com/press-release/formfactor-and-advantest-partner-on-silicon-photonics-wafer-level-test-cell-to-enable-high-volume-manufacturing/)
- [FormFactor 併購 Keystone Photonics 擴 SiPh/CPO 光學 wafer test（2025-12-15）](https://www.globenewswire.com/news-release/2025/12/15/3205831/0/en/FormFactor-Expands-Silicon-Photonics-Test-Capabilities-With-Acquisition-of-Keystone-Photonics.html)
- [THE ELEC：TSE 切入 HBM probe card（便宜 80%）、FormFactor 為 HBM wafer 級卡 dominant supplier](https://www.thelec.net/news/articleView.html?idxno=5553)
- [Mordor Intelligence：2025 探針卡市佔 FormFactor ~28.5%／Technoprobe ~16.5%／MJC ~10.2%](https://www.mordorintelligence.com/industry-reports/probe-card-market)
- [GuruFocus：FORM Forward PE 51.46（2026-06）](https://www.gurufocus.com/term/forward-pe-ratio)；[Q3 2025 call：HBM 單季約 $40M（Motley Fool 2025-10-29）](https://www.fool.com/earnings/call-transcripts/2025/10/29/formfactor-form-q3-2025-earnings-call-transcript/)

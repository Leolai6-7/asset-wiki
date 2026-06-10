---
title: Astera Labs
aliases: [ALAB, NASDAQ:ALAB, Astera, Astera Labs Inc]
type: entity
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-11-15
sources:
  - https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-first-quarter-2026-financial-results
  - https://www.fool.com/earnings/call-transcripts/2026/05/05/astera-labs-alab-q1-2026-earnings-transcript/
  - https://stockanalysis.com/stocks/alab/statistics/
  - https://www.gurufocus.com/term/forward-pe-ratio/ALAB
  - https://www.theglobeandmail.com/investing/markets/stocks/ALAB/pressreleases/167545/astera-labs-grants-amazon-strategic-performance-based-warrant-investment/
tags: [標的, 美股, 互連, PCIe, retimer, AEC, 銅纜, scale-up, fabric switch, CXL, NVDA, AWS, CPO延期受惠]
thesis_dependency: AI-capex
confidence: medium
---

# Astera Labs（ALAB）

## 1. 一句話定位

**AI scale-up「銅纜時代的互連賣水人」**——2017 ex-TI 團隊創立（San Jose）、2024-03 IPO；四產品線 **Aries**（PCIe 6 retimer、AI 伺服器市佔壟斷級）＋ **Taurus**（Ethernet AEC 主動銅纜）＋ **Scorpio**（PCIe fabric switch、X-Series 320-lane 專為 hyperscaler 自研 ASIC scale-up）＋ **Leo**（CXL）；Q1 2026 營收 **$308.4M（YoY +93%）**、non-GAAP 毛利 **76.4%**；protocol 五路全押（PCIe／Ethernet／CXL／[[NVDA]] NVLink Fusion／UALink board member）；[[AMZN]] 2026-02 warrant 綁 **$6.5B 累計採購至 2033**；[[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告]]「銅纜＋可插拔受惠」名單成員——scale-up 銅互連主流延長至 2028 = retimer／AEC／fabric switch TAM 窗口直接拉長；**但 Forward PE 102–121x、12M ~+250%、分析師平均目標價 $245 低於現價 28% = 本 wiki C 軸警示最強標的之一**。

## 2. 三層 thesis

### 產業層
- Scale-up（GPU↔GPU back-end）互連是 AI infra 成長最快的賽道；訊號速率上 PCIe 6（64GT/s）／224G SerDes 後，**被動銅纜 reach 不夠 → retimer＋AEC 變成剛需**
- SemiAnalysis 延期報告 ✅：銅纜＋可插拔主流至 2028、scale-up CPO 2029+（綁 Feynman）→ **Astera 的銅窗口被拉長、不是被取代**（與 [[Marvell]]／[[Amphenol]]／[[MACOM Technology]] 同組受惠）
- Protocol 路線戰（NVLink Fusion vs UALink vs PCIe／Ethernet scale-up）誰贏都要 signal conditioning ＝ [[賣水人選股邏輯（投資版）]] 教科書案例
- [[市場四階段：懷疑／驗證／共識／反轉]]：「驗證 → 共識」段；[[資訊擴散四階段]] 已到共識段（券商全覆蓋、散戶熟知）

### 目的層
- 不押哪家加速器贏：NVDA 平台（Aries retimer 進 reference design）＋ AWS Trainium（Scorpio X）＋ AMD／custom ASIC（UALink／PCIe fabric）全吃
- 真正押的是「**第三方互連晶片不被整合掉**」：NVDA 自家 NVLink switch、[[AVGO]] SUE（Scale-Up Ethernet）都是把 Astera 夾掉的路線
- [[投資四元問題框架（ABCD）]]：A（結構受惠）✅、B（時程）銅窗口至 2028 ✅、**C（價格 vs 預期）⚠️ 最大破口**——Forward PE 102–121x（半導體中位數 36、高 ~200%+）已 price in 多年完美執行

### 供應層
- Fabless（[[TSMC]] 投片）；護城河 = PCIe 6 first-mover＋COSMOS 軟體（fleet telemetry、hyperscaler 黏著）＋與自研 ASIC 陣營共同設計
- Scorpio X：2026-05 發布 320-lane、初始出貨中、**2H26 量產 ramp、管理層預期年底成為最大產品線**；analyst 估 AWS scale-up switch 機會 ~$2.5B（2026-29）
- AWS warrant（2026-02-05）：3.26M 股 @ $142.82、vest 條件 = fabric switch＋signal conditioning＋**optical engine** 累計採購 $6.5B 至 2033 → 注意 warrant 文字已含光引擎 = Astera 自己也在鋪 optics 路線 hedge
- 競爭：[[AVGO]]（PEX switch + 2025 起新 retimer 反攻 + SUE）、[[Marvell]]（Alaska retimer、AEC DSP）、Credo（AEC 對手）、瀾起／Parade（低階）

## 3. 財務快照（As of 2026-06-10）

| 指標 | 數值 |
|---|---|
| 股價 | $341.70（2026-06 初） |
| 市值 | ~$58.6B |
| 52 週區間 | $84.78 – $372.37 |
| 12 個月漲幅 | **~+250%**（52 週低點以來 +303%） |
| Trailing PE | ~231x |
| **Forward PE** | **102–121x**（不同源；半導體中位數 36x）⚠️ |
| 分析師平均目標價 | $244.97 = **低於現價 28%**（Buy 共識但價格跑在前面）⚠️ |
| Beta | 3.96（高波動） |
| FY2025 營收 | **$852.5M（YoY +115%）**；Q4 2025 $271M（+92%） |
| Q1 2026 營收 | **$308.4M（YoY +93%、QoQ +14%）**、超 consensus $292M |
| Q1 2026 non-GAAP 毛利率 | **76.4%**（YoY +150bps） |
| Q1 2026 non-GAAP OP margin | 36.2%（YoY +250bps）；non-GAAP EPS $0.61 |
| Q2 2026 指引 | 營收 $355–365M（QoQ +15–18%）、non-GAAP EPS $0.68–0.70 |
| 產品 mix | PCIe Gen 6 占營收 >1/3；FY2025 Scorpio >15%、Scorpio＋Taurus 合計 ~30% |
| 客戶集中 | Q1 2026 兩客戶各 12%（前一年單一客戶 23% → 改善中）；終端 hyperscaler 集中度仍高 |

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | 4 | Protocol 五路全押（PCIe／Ethernet／CXL／NVLink Fusion／UALink）= 真 route-agnostic；扣分：media 層押銅纜窗口（2028 後 optics 滲透 scale-up 是結構風險、optical engine 佈局尚未兌現） |
| 站別關鍵 | 4 | PCIe retimer AI 伺服器壟斷級市佔＋Scorpio X 是 custom ASIC scale-up 先行 fabric switch；扣分：NVDA in-house NVLink＋[[AVGO]] SUE 都能把這站整合掉 |
| 耗材 recurring | 3 | 晶片隨每顆加速器 attach、每代平台（Gen 5→6→7）重新 design-win；AEC 線纜半耗材；非真消耗品 |
| IP | 4 | PCIe 6 first-mover（端到端互通最早）＋COSMOS 軟體黏著＋PCIe 7 路線圖；扣分：SerDes 底層 IP 對 AVGO／MRVL 無代差 |
| 客戶分散 | 2 | Hyperscaler 高度集中、AWS warrant 加深綁定（蜜糖＋枷鎖）；帳面兩大客戶各 12% 是 ODM 出貨遮蔽、終端集中更高 |

**總分：17/25**（不確定區間 **17–18**：若 Scorpio X 放量帶動客戶分散 2→3 則 18）——與 [[AAOI]]／[[鴻勁 7769]]／[[致茂 2360]] 同層（17–18 tier）、低於 [[Teradyne]]／[[SiTime]] 19–20 層。**結構分不低、問題全在 C 軸（價格）**。

## 監控指標

| 指標 | 觸發行動 |
|---|---|
| Scorpio X 2H26 量產 ramp、年底是否成最大產品線 | Q3 法說未確認 → thesis 時程下修、區間取下緣 17 |
| AWS Trainium 3 放量／warrant vest 進度（10-Q） | Trainium 砍單 → 大利空、客戶分散軸重評 |
| NVLink Fusion custom 案營收兌現時點（2027+） | 法說首次給出 design-win 營收 → 路線敏感軸加分 |
| AVGO 新 retimer／SUE 在 hyperscaler 第二供應商導入 | 確認導入 → 站別關鍵 4→3、總分降至 16 |
| Scale-up CPO 提前（Feynman 前倒至 2028） | 銅窗口縮短 → 整體 thesis 重評（對照 SemiAnalysis 追蹤） |
| 營收 YoY 成長跌破 ~50% 而 Forward PE 仍 >80x | [[PE 壓縮公式]] C 軸出場訊號、參考 [[Re-rate 捕捉法]] 反向 |
| Aries 7（PCIe 7）sampling → 量產時點 | 落後對手 → IP 軸 first-mover 證據失效 |

## 相關連結

- [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]（銅纜＋可插拔受惠組：與 [[Marvell]]、[[Amphenol]]、[[MACOM Technology]] 同列）
- [[賣水人選股邏輯（投資版）]]／[[投資四元問題框架（ABCD）]]／[[PE 壓縮公式]]／[[Re-rate 捕捉法]]
- [[CPO 供應鏈圖譜]]（CPO 2029+ 兌現前、Astera 是「銅的對價」）／[[NVDA 網路 stack map]]
- [[市場四階段：懷疑／驗證／共識／反轉]]／[[資訊擴散四階段]]
- [[NVDA]]（NVLink Fusion 生態＋整合風險雙面）／[[AVGO]]（最直接競爭者）／[[AMZN]]（warrant 綁定）／[[AMD]]（UALink 陣營）／[[TSMC]]

## Sources

- [Astera Labs Reports First Quarter 2026 Financial Results（IR, 2026-05）](https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-reports-first-quarter-2026-financial-results)
- [Astera Labs (ALAB) Q1 2026 Earnings Transcript（Motley Fool, 2026-05-05）](https://www.fool.com/earnings/call-transcripts/2026/05/05/astera-labs-alab-q1-2026-earnings-transcript/)
- [Astera Labs Q1 FY 2026 Earnings Show Scale-Up Switching Ramp（Futurum）](https://futurumgroup.com/insights/astera-labs-q1-fy-2026-earnings-highlight-scale-up-switching-ramp/)
- [ALAB Q1 2026 Earnings Call — 93% Revenue Surge to $308.4M（BigGo Finance, 2026-05-05）](https://finance.biggo.com/news/US_ALAB_2026-05-05)
- [Earnings call transcript: Astera Labs beats Q1 2026 estimates（Investing.com）](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-beats-q1-2026-estimates-shares-rise-93CH-4677421)
- [Astera Labs ALAB Q4 2025 Earnings Call Transcript（Motley Fool, 2026-02-10）](https://www.fool.com/earnings/call-transcripts/2026/02/10/astera-labs-alab-q4-2025-earnings-call-transcript/)
- [Astera Labs Revenue More Than Doubled in 2025（TIKR）](https://www.tikr.com/blog/astera-labs-revenue-more-than-doubled-in-2025-is-the-stock-still-cheap)
- [Astera Labs Expands Collaboration with NVIDIA to Advance NVLink Fusion Ecosystem（GlobeNewswire, 2025-05-19）](https://www.globenewswire.com/news-release/2025/05/19/3084050/0/en/Astera-Labs-Expands-Collaboration-with-NVIDIA-to-Advance-NVLink-Fusion-Ecosystem.html)
- [Astera Labs Expands Connectivity Portfolio with Custom Solutions（Astera Labs）](https://www.asteralabs.com/news/astera-labs-expands-connectivity-portfolio-with-custom-solutions/)
- [Astera Labs Grants Amazon Strategic Performance-Based Warrant Investment（Globe and Mail, 2026-02）](https://www.theglobeandmail.com/investing/markets/stocks/ALAB/pressreleases/167545/astera-labs-grants-amazon-strategic-performance-based-warrant-investment/)
- [Astera Labs (ALAB) Enters Agreement with Amazon（GuruFocus, 2026-02）](https://www.gurufocus.com/news/8603443/astera-labs-alab-enters-agreement-with-amazon-for-significant-stock-acquisition)
- [ALAB Statistics & Valuation（stockanalysis.com, 2026-06）](https://stockanalysis.com/stocks/alab/statistics/)
- [ASTERA LABS Forward PE Ratio: 120.60（GuruFocus, 2026-06-05）](https://www.gurufocus.com/term/forward-pe-ratio/ALAB)
- [Astera Labs Battles Nvidia And Broadcom As AI Chip Market Heats Up（Benzinga, 2025-10）](https://www.benzinga.com/analyst-stock-ratings/initiation/25/10/48025202/astera-labs-battles-nvidia-and-broadcom-as-ai-chip-market-heats-up)
- [Broadcom Fires a Shot at Astera Labs with New PCIe and CXL Retimers（ServeTheHome）](https://www.servethehome.com/broadcom-fires-a-shot-at-astera-labs-and-more-with-new-pcie-and-cxl-retimers/)

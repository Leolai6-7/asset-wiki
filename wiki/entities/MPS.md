---
title: MPS
aliases: [MPWR, Monolithic Power Systems, "Monolithic Power Systems MPS", Monolithic Power, 美國芯源, NASDAQ:MPWR]
type: entity
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2026-11-15
sources:
  - WebSearch 2026-06-08（Q1 2026 earnings / NVIDIA Vera Rubin share / valuation）
tags: [標的, 美股, 半導體, 電源管理, CPO 第7層, AI 基礎建設, NVDA 供應鏈, 賣水人, 高估值]
thesis_dependency: AI-capex
confidence: medium
---

# MPS（Monolithic Power Systems / MPWR）

## 1. 一句話定位

**AI 資料中心電源管理 IC（PMIC）「最薄但最關鍵」站位**——半導體電源類比 IC 設計商，BCD（Bipolar-CMOS-DMOS）製程整合 + 模組化 power module 雙產品線，**直接卡在 NVDA GPU / hyperscaler AI server 的「最後一吋電源轉換」**；Q1 2026 營收 **$804.2M（YoY +26.1%、QoQ +7.1%）**、Enterprise Data 段 **YoY +97.7%**（指引下半年該段成長下限拉到 +85%）；NVDA Blackwell 平台**部分流失**給 Infineon / Renesas（市佔 60-70% 給 Infineon），但 KeyBanc 供應鏈研究顯示**下世代 Vera Rubin（VR200 NVL144 / R200 HGX）拿回 ~70% 市佔**、預估 2026 增收 $100M+、2027 年化 ~$420M、EPS 增 $4+；CPO 第 7 層電源 + 光模組 power 雙位置（光模組 power 已寫進 Q1 法說會）；股價 **$1,624.99（2026-06-02）**、市值 **~$81-83B**、Forward PE **52-68 倍**（GF Value 仍判定「overvalued 54%」）；五軸 **17/25**——是 CPO 七層裡「中性受惠 + 不依賴單一光路線」的賣水人，但**單一客戶 NVDA 集中度高 + 競爭重新洗牌**是中期最大風險。

## 2. 三層 thesis

### 產業層

- AI 資料中心電源管理在 [[市場四階段：懷疑／驗證／共識／反轉]] **「驗證 → 共識」加速段**：
  - 800V 直流匯流排（HVDC）+ 48V → 12V → 0.8V 多段降壓 + vertical power delivery（VPD）→ AI GPU 功耗從 700W 攀升到 1.4kW、3.6kW（Rubin Ultra 預計）
  - GPU 越大、power IC 用量越多（每 GPU 約 30-50 顆電源 IC）
  - 1.4kW Blackwell B200、1.8kW B300、2.7kW Rubin、5.7kW Rubin Ultra → **power IC BOM 三倍 → 五倍放大**
- AI Server 電源需求 = TAM 多年高速成長：
  - Enterprise Data 段 Q1 2026 +97.7% YoY、指引下半 +85% 下限（公司原指引 +50%）
  - 整體 power IC TAM CAGR 估 20%+（含 GPU + 光模組 + 交換器電源）
- [[資訊擴散四階段]]：MPWR 12 個月 +70%（vs NVDA、AVGO 同期），**已過散戶看到階段**、進入共識段
- 競爭格局**重新洗牌**：
  - **Blackwell 失分**：Infineon 拿 60-70% 主流市佔、Renesas 切入 digital power
  - **Vera Rubin 拿回**：MPS 70% 市佔（KeyBanc 供應鏈研究 2025-10）
  - → 不是「失敗 → 退出」、是「**份額洗牌 + Rubin 反攻**」
- 競爭對手：Infineon（IFNNY、德商）、Renesas（東京）、Texas Instruments（TXN）、ADI

### 目的層

- **業務 mix**（Q1 2026，2026-04 法說會）：
  - **Enterprise Data ~31% 營收**（$247M、YoY +97.7%）—— AI 主驅動
  - Storage & Computing ~16%（與 Enterprise Data 部分重疊）
  - Communications ~14%
  - Industrial ~14%
  - Automotive ~16%
  - Consumer ~9%
- **「不押 GPU 誰贏、押 GPU 一定要電源」的賣水人**：
  - vs [[NVDA]]：MPS 是 NVDA GPU 供應鏈核心 PMIC 廠（每 Blackwell GPU 用 30+ MPS 電源 IC）
  - vs AMD MI300/MI355：MPS 也供應
  - vs Custom XPU（AWS Trainium / MSFT Maia / Google TPU）：MPS 為 hyperscaler ODM 配套
- **「電源 IP 護城河」邏輯**：
  - BCD 製程整合 + 高功率密度封裝（QFN、power module、VPD）= 對手難以快速複製
  - 模組化（power module）降低客戶設計門檻 = sticky
  - 光模組電源切入：1.6T 光模組功耗 20-30W、需要多顆高效電源 IC → MPS Q1 2026 法說會已揭露「optical modules」是 enterprise data 成長驅動之一
- **NVDA 客戶集中度（單一最大風險）**：
  - NVDA 預估占營收 15-25%（公司未拆解、市場估算）
  - Blackwell 流失 → Vera Rubin 反攻 = NVDA 端營收 2026 中低空、2027 反彈
- 商業模式：
  - 半導體 IC 設計 + 模組封裝、Fab-light（晶圓代工 TSMC + SMIC + GlobalFoundries 多家）
  - 高毛利（公司 GAAP 毛利 55-56%）= 類 ADI / TXN 結構但成長率高
- → 連 [[賣水人選股邏輯（投資版）]]：**「不押 hyperscaler 誰贏、不押 GPU 誰贏、押 GPU + AI server 電源一定要用」**

### 供應層

- 跟 [[NVDA]] 關係（**最重要也最危險**）：
  - **Blackwell B200/B300 流失** → Infineon 拿 60-70%（2025-04 起被市場 price out）
  - **Vera Rubin（VR200 NVL144 / R200 HGX）反攻** → KeyBanc 估 70% 市佔
  - 反映「**vertical power delivery（VPD）路線**MPS 起步早、Infineon 急起直追」
  - 下一個觀察點：2026 Q3 / Q4 Rubin Sample 時點、2027 量產
- 跟 [[AVGO]] 關係：
  - AVGO 80% Ethernet switch ASIC + 70% custom AI ASIC → 需要配套電源 → MPS / Renesas / Infineon 三家分食
  - AVGO 自研 CPO 光引擎 → 配套光模組電源 → MPS Q1 2026 法說會點名「光模組」成長驅動 = 切到 CPO 第 7 層
- 跟 [[Lumentum]] / [[Coherent]] 關係：
  - 光模組 + 光引擎需要高效低噪電源 → MPS 切入該段（Q1 2026 法說會）
  - 不是直接客戶（透過 OEM、模組廠如旭創、新易盛、Innolight）
- 跟 [[Marvell]] 關係：
  - Marvell Teralynx T100 + Ara DSP + custom XPU → 配套電源 → MPS / 競品
- 跟 [[TSMC]] 關係：
  - 製程主要走 TSMC + SMIC + GlobalFoundries
  - BCD 整合製程多年深耕
- 護城河：
  - **BCD 製程 IP**（高壓 + 低壓整合）
  - **VPD（vertical power delivery）IP 領先 Infineon 約 1-2 年**
  - **High power density module 封裝**（power module 一站式）
  - 多代 GPU / AI server 設計 lock-in（每代設計 lead time 12-18 個月）
- 風險：
  - **NVDA 客戶集中度**（估 15-25% 營收）+ Blackwell 流失 = 短期業績壓力
  - **Infineon / Renesas 競爭力急起直追**（Blackwell 60-70% 流失給 Infineon 證明）
  - **Forward PE 52-68 + 12 月 +70%**——估值已 price in Rubin 反攻
  - **中國市場曝險**（早年 SMIC 代工 + 中國汽車 / 工業客戶）
  - **過度依賴 AI server CapEx**（Enterprise Data 30%+ 營收）
  - GF Value 判定「overvalued 54%」、$1,053 公允價值 vs $1,625 股價
- → 連 [[控制點轉移（投資版）]]：拿到「**高功率密度 power IC + VPD 控制點**」、未拿光引擎 / DSP 控制點

## 3. 財務狀態快照（As of 2026-06-08）

| 指標 | 數值 |
|---|---|
| 股價 | $1,624.99（2026-06-02） |
| 12 個月漲幅 | **+70% YTD 2026** |
| 市值 | **~$81-83B** USD |
| Forward PE | **52-68 倍**（vs semi 中位 34.68 = 高 50-95%） |
| GF Value | $1,053（判定 overvalued 54%） |
| Q1 2026 營收 | **$804.2M**（YoY +26.1%、QoQ +7.1%、創高） |
| Q1 2026 EPS | $5.10（beat 預期） |
| Q1 2026 Enterprise Data 段 | YoY **+97.7%** |
| Q2 2026 指引營收 | **$890-910M** |
| Enterprise Data 年成長下限指引 | 從 +50% 拉高到 **+85%**（公司主動上修） |
| 製造產能目標 | $6B（從原本指引上修） |
| GAAP 毛利率 | ~55-56% |
| 主要客戶 | NVDA（最大）、AMD、hyperscaler ODM（廣達、鴻海、緯穎）、光模組廠 |
| NVDA Blackwell 市佔 | 流失（Infineon 60-70%） |
| NVDA Vera Rubin 市佔（KeyBanc 估）| **70%** |
| Rubin 預估增收（KeyBanc） | 2026 $100M+、2027 年化 $420M、EPS +$4 |

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ Enterprise Data +97.7%、Q1 創高、Q2 指引再加速、製造產能上修 $6B |
| 毛利率 | ⚠️ GAAP 55-56% 健康但 mix shift 對純 IC vs 模組毛利結構待觀察 |
| OpEx | ⚠️ Rubin 設計贏單 + 光模組電源切入 = R&D 投入加重 |
| 營業利益 | ✅ Beat 預期 EPS $5.10、Q2 指引 $890-910M 加速 |

→ **Re-rate 三角形 2/4**——成長指標健康，但 Forward PE 52-68 + GF Value overvalued 54% = 估值高度 price in Rubin 反攻 + 光模組電源切入完美執行。

### ✅ 催化

- **Vera Rubin 反攻**：2026 Q3-Q4 Rubin sample、2027 量產 = NVDA 端 70% 市佔回歸
- **Enterprise Data +85% 下限指引**（vs 原 +50%）= 公司主動上修 = 訂單能見度提升
- **光模組電源切入**（Q1 2026 法說會明點）= CPO 第 7 層卡位
- **製造產能 $6B 目標**（上修）= 為 Rubin 量產做準備
- VPD（vertical power delivery）技術領先 Infineon
- 1.6T 光模組 BOM 用量翻倍 → power IC 配套需求倍增
- Hyperscaler 800V HVDC 直流匯流排升級 = 多級電源 IC 用量倍增
- **半導體基礎建設化**（[[半導體基礎建設化]]）= 從週期股轉結構性成長股
- AMD MI355、Custom XPU 配套電源用量也成長
- 模組化 power module 產品 sticky、降低客戶設計 ramp 阻力

### ⚠️ 風險

- **NVDA 客戶集中度**（估 15-25% 營收）= 任何 NVDA 訂單調整影響大
- **Blackwell 60-70% 流失給 Infineon**——重新洗牌證明 MPS 護城河不是不可破
- **Forward PE 52-68 + GF Value overvalued 54%**——估值 price in 多年完美執行
- **競爭重洗**：Infineon 在 VPD 急起直追、Renesas 切入 digital power
- **Renesas 拿到 NVDA digital power 部分份額**（2025 起）
- **Rubin 反攻是 2027 後才完整顯現**——2026 中段業績壓力（Blackwell 流失 vs Rubin 未量產的空窗）
- **過度依賴 AI server CapEx**（Enterprise Data 30%+ 營收 + 集中度高）
- **中國市場曝險**（早年 SMIC 代工 + 中國工業 / 汽車客戶 ~15-20%）
- **股價 $1,625 + 市值 $83B**——進場區間壓力大
- 半導體景氣循環（Automotive + Industrial 30%+ 仍受 macro 影響）

## ⭐ 對 [[CPO 供應鏈圖譜]] 的意義（第 7 層）

MPS 在 CPO 圖譜的位置：

- **第 7 層 電源**：CPO 模組與光引擎需要高效、低噪聲、緊密電源 IC 整合
  - MPS 主要對手 Renesas、ADI、TXN
  - **中性受惠**：不押 [[Lumentum]] vs [[Coherent]] vs 博通自研 = 都用電源 IC
- **第 7 層 vs 第 4 層 timing**（[[SiTime]]）的對比：
  - 兩者都是「中性賣水人」、不依賴光引擎誰贏
  - **timing** 是平方放大（量 × 規格升級）= [[SiTime]] 最強催化
  - **電源** 是線性放大（GPU/光模組數量 × 每顆功耗）= MPS 催化稍弱於 timing
- **vs 第 6 層 connector**（[[Amphenol]]）：
  - connector = 物理被動元件、低風險、低成長
  - power = 主動 IC 設計、高風險、高成長
- **光模組電源切入是 2026 Q1 新增驅動**：CPO 第 7 層位置明確化

對 [[CPO 供應鏈圖譜]] 的補強：
- 第 7 層 power 更新：MPS Q1 2026 法說會點名「光模組」= 從「外圍 CPO」變「直接 CPO 配套」
- 強調 MPS 與 [[SiTime]] 是 CPO「**雙中性賣水人**」、但 timing 平方放大 > power 線性放大

## ⭐ 對台股 / 美股 AI 半導體基礎建設的意義

對 [[NVDA]]：
- MPS 是 NVDA 配套電源核心廠之一、Vera Rubin 拿回 70% 市佔 = NVDA 仍需要 MPS
- Blackwell 流失證明 NVDA 不會被單一電源廠綁架（議價力)

對 [[AVGO]]：
- AVGO CPO 光引擎模組 → 需要 MPS / Renesas / Infineon 配套電源
- AVGO 自研 ASIC + Tomahawk → 配套 server 電源也用 MPS

對 [[Lumentum]] / [[Coherent]]：
- 光模組 / 光引擎電源需求 → MPS Q1 2026 法說會點名「optical modules」= 中性切入
- 不是直接客戶（透過 OEM / 模組廠）

對台廠：
- 鴻海 / 廣達 / 緯穎 ODM AI server → MPS 是配套電源 IC 供應商（透過台廠 ODM 採購）
- 台達電 / 光寶為「電源系統」廠（PSU + server power），MPS 是「電源 IC」（PMIC、point-of-load）—— 兩者層級不同、無直接競爭
- 國巨、信昌電被動元件配套但無直接影響

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | 3 | 雙路線（GPU power + 光模組 power），中性受惠，但 Blackwell 流失證明不是不可破 |
| 站別關鍵 | 4 | VPD + BCD 製程領先 1-2 年、模組化 power module sticky |
| 耗材 | 3 | 半導體 IC + power module = 每代 GPU / server 都換新、類耗材 |
| IP | 3 | BCD 製程 IP + VPD IP 領先但 Infineon 急起直追 = 護城河有壓力 |
| 客戶分散 | 4 | Enterprise Data + Storage + Comm + Industrial + Auto + Consumer 六大段、單一客戶集中度估 15-25% |

**總分：17/25**

### vs [[SiTime]] 五軸對照（CPO 「雙中性賣水人」對比）

| 軸 | MPS | SiTime | 說明 |
|---|---|---|---|
| 路線敏感 | 3 | **5** | SiTime 完全中性（誰贏 timing 都要用、不會被替代）、MPS Blackwell 流失證明可被替代 |
| 站別關鍵 | 4 | 4 | 打平，雙方都關鍵 |
| 耗材 | 3 | **4** | SiTime 量 × 規格升級平方放大、MPS 線性放大 |
| IP | 3 | **4** | SiTime MEMS 時脈 IP 護城河更深（vs 傳統石英晶振）、MPS BCD/VPD 競爭壓力較大 |
| 客戶分散 | 4 | 4 | 打平（雙方都多段業務） |
| **總分** | **17/25** | **21/25** | SiTime 全方位領先 4 分 |

→ **MPS vs SiTime 共存 + SiTime 為 CPO 純度首選**：
- SiTime 21/25 = CPO 中性賣水人最純（平方放大 + 不可替代）
- MPS 17/25 = AI server 電源 + CPO 配套（線性放大 + 可替代）
- 都不押光引擎誰贏，但 SiTime 抗替代性更強

### vs [[Marvell]] 五軸對照（DSP 整合風險 vs 電源 power IC 替代風險）

| 軸 | MPS | Marvell | 說明 |
|---|---|---|---|
| 路線敏感 | 3 | 4 | Marvell 四路線、MPS 雙路線（GPU power + 光模組 power）|
| 站別關鍵 | 4 | 4 | 打平 |
| 耗材 | 3 | 3 | 打平 |
| IP | 3 | 4 | Marvell IP 護城河深、MPS 競爭壓力大 |
| 客戶分散 | 4 | 3 | MPS 六大段、Marvell 三家集中 |
| **總分** | **17/25** | **18/25** | Marvell 領先 1 分（IP + 路線數） |

## ⭐ Rubin 反攻時程與 alpha 視角

```
2026 Q1-Q2：黃金期（Enterprise Data +97.7%、Q2 指引 +85%、市場 price in Rubin 反攻）
    │
2026 Q3-Q4：Rubin Sample（Blackwell 流失影響開始顯現、空窗期）
    │
2027 H1：Rubin 量產（KeyBanc 估 70% 市佔回歸、年化 +$420M）
    │
2027 H2：Rubin Ultra Sample（5.7kW GPU = power IC BOM 三倍放大）
    │
2028+：Vera Rubin Next / Custom XPU power 配套加碼
```

**Alpha 視角**：
- **2026 Q3-Q4 空窗期**可能造成股價波動（Blackwell 流失影響顯現、Rubin 未量產）
- **2027 H1 Rubin 量產**是大催化、市場早已 price in（Forward PE 52-68 反映）
- **2027 H2 Rubin Ultra**才是真正 alpha（5.7kW GPU 配套電源 IC 三倍放大）
- → **進場區間敏感**：$1,625 + 市值 $83B 不是 alpha 進場區間、$1,053（GF Value）才是

## 跟其他 wiki 概念連結

- [[CPO 供應鏈圖譜]]：第 7 層電源（與 Renesas、ADI、TXN 同層）
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：高功率 GPU 配套電源 IC BOM 倍增
- [[AI infra CapEx 三階段論]]：第二/三階段電源配套 IC 倍增
- [[賣水人選股邏輯（投資版）]]：不押 GPU 誰贏、不押光引擎誰贏，押電源一定要用
- [[半導體基礎建設化]]：從週期股轉結構性成長股的潛在轉型
- [[市場四階段：懷疑／驗證／共識／反轉]]：在「驗證 → 共識」加速段
- [[資訊擴散四階段]]：12 月 +70% 已過散戶看到階段、進入共識段
- [[控制點轉移（投資版）]]：拿到 power IC + VPD 控制點、未拿光引擎 / DSP 控制點
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 強制格式
- [[NVDA]]：最大單一客戶、Blackwell 流失 + Rubin 反攻的雙刃劍
- [[AVGO]]：AVGO ASIC / 光引擎配套電源
- [[Lumentum]]、[[Coherent]]：光模組 / 光引擎電源切入
- [[Marvell]]：custom XPU / DSP 配套電源
- [[SiTime]]：CPO「雙中性賣水人」對照組
- [[TSMC]]：晶圓代工夥伴

## 相關連結

- [[CPO 供應鏈圖譜]]
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]
- [[AI infra CapEx 三階段論]]
- [[賣水人選股邏輯（投資版）]]
- [[半導體基礎建設化]]
- [[控制點轉移（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[NVDA]]、[[AVGO]]、[[Lumentum]]、[[Coherent]]、[[Marvell]]、[[SiTime]]、[[TSMC]]

## Sources

- [Monolithic Power Systems Q1 2026 earnings 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001280452/000143774926014182/ex_929254.htm)
- [Monolithic Power Systems Q1 2026 10-Q (SEC)](https://www.sec.gov/Archives/edgar/data/0001280452/000143774926014647/mpwr20260331_10q.htm)
- [Monolithic Power Systems (MPWR) Q1 2026 earnings review (Finsee)](https://finsee.ai/earnings/mpwr/2026/q1/en/)
- [Monolithic Power Systems Exceeds Q1 2026 Expectations (MLQ News)](https://mlq.ai/news/v2/monolithic-power-systems-exceeds-q1-2026-expectations-with-robust-revenue-growth/)
- [Did Analyst Optimism on NVIDIA's Vera Rubin GPU Just Shift MPWR's Investment Narrative? (Yahoo Finance)](https://finance.yahoo.com/news/did-analyst-optimism-nvidia-vera-081241006.html)
- [Why is Monolithic Power Systems (MPWR) Surging in 2026 (Kavout)](https://www.kavout.com/market-lens/why-is-monolithic-power-systems-mpwr-surging-in-2026)
- [Nvidia Stock Dips As Monolithic Power Crashes On Concerns of Supplier Allocation For Blackwell AI Chips (Stocktwits)](https://stocktwits.com/news-articles/markets/equity/nvidia-monolithic-power-infineon-renesas-on-blackwell-chip-supplier-concerns/cJ4gxWfROI)
- [MPWR (Monolithic Power Systems) Forward PE Ratio (GuruFocus)](https://www.gurufocus.com/term/forward-pe-ratio/MPWR)
- [Monolithic Power Systems Inc (MPWR) Stock Up 5.4% but GF Value Says Overvalued (GuruFocus)](https://www.gurufocus.com/news/8897070/monolithic-power-systems-inc-mpwr-stock-up-54-but-gf-value-says-overvalued-gf-score-93100)
- [Monolithic Power Systems (MPWR) Statistics & Valuation (Stockanalysis)](https://stockanalysis.com/stocks/mpwr/statistics/)
- [Vertical Power Delivery for Emerging Packaging and Integration Platforms (arXiv)](https://arxiv.org/pdf/2309.10141)
- [Your datacenter's power architecture called. It's not happy (The Register, 2026-03)](https://www.theregister.com/2026/03/11/your_datacenters_power_architecture_called/)

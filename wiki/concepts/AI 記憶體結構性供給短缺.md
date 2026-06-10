---
title: AI 記憶體結構性供給短缺
aliases: [AI 記憶體結構性短缺, 記憶體 infra 化, HBM 結構性需求, 結構性短缺 vs 景氣循環, 記憶體 NVDA 綁定論]
type: concept
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2027-01-15
expires_on: 2027-12-31
sources:
  - raw/2026-06-08_Leo-黃仁勳定調記憶體結構性短缺-SK-Hynix-合約.md
evidence_url: https://news.skhynix.com/multi-year-tech-partnership-with-nvidia/
tags: [記憶體, HBM, AI infra, 結構性短缺, NVDA, SK Hynix, 估值範式, Re-rate]
thesis_dependency: none（可遷移方法）
confidence: medium
---

# AI 記憶體結構性供給短缺

黃仁勳 2026-06-08 訪韓定調：「**市場還在用景氣循環角度看記憶體，但這次是結構性供給短缺**」（[CNBC 2026-06-07](https://www.cnbc.com/2026/06/07/nvidia-sk-to-detail-cooperation-plan-amid-prolonged-chip-shortage.html)、[Yahoo Finance 2026-06-07](https://finance.yahoo.com/sectors/technology/articles/nvidia-sk-hynix-partner-jensen-151942177.html)）。本 concept = **對抗 [[PB 估值法（記憶體週期）]] 的新估值範式**。

## 一句話

> 記憶體不再是純週期股——AI 路線圖綁定 + 物理產能限制 + 封裝瓶頸 = 結構性供給短缺。

## thesis vs 對手 thesis

| | 景氣循環論（[[PB 估值法（記憶體週期）]]）| **結構性短缺論（本 concept）** |
|---|---|---|
| 估值 | PB（淨資產錨點） | **雙引擎：PB（傳統 DRAM）+ Forward PE / DCF（HBM）** |
| 週期長度 | 3-4 年 | **多年（2026-2030+，SK Group Chey 直接說「至少到 2030」）** |
| 操作 | 逆週期（高賣低買） | **賣水人 long bias + 跟隨 NVDA 路線圖節奏** |
| 觸發 | 供給過剩（廠商擴產追上需求） | NVDA 路線圖 multi-year commit + 封裝/晶圓物理限制 |
| 風險 | 供給追上、價格崩 | **AI 需求結構性放緩、模型效率躍進（DeepSeek 2.0）、政策干預** |
| 預付訂單意義 | 週期中段警訊 | sticky design-in、多年能見度 anchor |
| LTA 角色 | 鎖供給不鎖價（穩出貨量） | **鎖製程協同 + co-design**，價格自然站穩 |

## 結構性短缺三大物理 driver

### 1. HBM 消耗晶圓產能遠高於一般 DRAM（**3 倍 / GB**）

**Verified**：
- 每 GB HBM 約消耗 DDR5 三倍 wafer 容量（[Tom's Hardware 2026-06](https://www.tomshardware.com/pc-components/ram/hbm-is-eating-your-ram)、[TechTimes 2026-06-04](https://www.techtimes.com/articles/317789/20260604/ddr5-ram-hits-375-floor-pc-builders-hbm-takes-three-times-more-wafers.htm)）
- HBM 佔 DRAM bit 出貨 ~10%、但**佔 wafer 產能 ~15-23%**（["Memory Chip Shortage 2026" tech-insider.org](https://tech-insider.org/memory-chip-shortage-2026-ai-consumer-electronics/)）
- HBM 每 wafer 營收 = DDR5 的 3-5 倍 → 廠商**經濟誘因強迫切走產能**

**機制**：
- HBM 12-Hi / 16-Hi 堆疊 → 縱向 die 數倍化、TSV 製程 → 良率損失
- → 同一片 wafer 切到 HBM = 同等容量的 DDR5 wafer 數量倍增

**Lock-in 後果**：Samsung、SK Hynix、Micron 三巨頭已將**93% 合計產能**重新分配至 HBM（[Astute Group 2026](https://www.astutegroup.com/news/memory-shortages/memory-supply-constraints-stretch-toward-2030-as-ai-demand-reshapes-dram-production/)）→ 一般 DRAM 結構性缺貨外溢、PC/手機市場 BOM 衝擊。

### 2. 先進封裝瓶頸（CoWoS / SoIC）

**Verified**：
- TSMC CoWoS 產能 2024 年底 35 kwpm → 2026 年底 ~125-130 kwpm → 2027 年底 170 kwpm（[FinancialContent 2026](https://markets.financialcontent.com/wral/article/tokenring-2026-1-1-the-great-packaging-pivot-how-tsmc-is-doubling-cowos-capacity-to-break-the-ai-supply-bottleneck-through-2026)、[Silicon Analysts Q1 2026](https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026)）
- 即使翻倍擴產，CoWoS 訂單**仍 sold out 至 2026 H2、能見度延伸到 2027**（[Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/intel-gains-ground-in-ai-packaging-as-cowos-capacity-remains-stretched)）
- HBM 必須先進封裝才能跟 GPU 整合 → DRAM 廠擴 capacity 解不了瓶頸
- 黃仁勳本人在韓國說「**從 wafer 到 cable connector 全部短缺**」（[Seoul Economic Daily 2026-06-07](https://en.sedaily.com/finance/2026/06/07/nvidias-jensen-huang-everything-from-wafers-to-cable)）

**結構含意**：
- 即使 SK Hynix 五年內 wafer 產能翻倍（[Tom's Hardware](https://www.tomshardware.com/pc-components/dram/sk-hynix-to-double-memory-wafer-capacity-over-five-years)），CoWoS 撐不撐住是另一條獨立瓶頸
- → 整合方（[[日月光 ASE]] / [[Amkor]] / [[Powertech 力成]]）拿到談判權、玻璃中介層（[[Absolics]]）2026-2028 qualification phase 也吃到溢出

### 3. NVDA 路線圖綁定（4 產品線多年合約）

2026-06-08 SK Hynix x NVDA 簽**多年技術合作協議**——**不只 HBM**，覆蓋四條路線的 design-in（[SK hynix Newsroom](https://news.skhynix.com/multi-year-tech-partnership-with-nvidia/)、[Tom's Hardware](https://www.tomshardware.com/pc-components/dram/nvidia-and-sk-hynix-ink-multi-year-memory-co-development-and-supply-agreement-seeks-to-address-extended-development-cycles)、[TrendForce 2026-06-08](https://www.trendforce.com/news/2026/06/08/news-sk-hynix-to-supply-memory-for-nvidia-vera-cpu-as-partnership-deepens-samsung-meeting-on-june-8-in-spotlight/)）：

| 產品線 | 記憶體規格 | 規模 |
|---|---|---|
| **Vera Rubin AI 超級電腦** | HBM4 + LPDDR5X + 3D NAND | 每 GPU **288 GB HBM4 / 22 TB/s**；NVL72 rack 共 **20.7 TB HBM4 + 54 TB LPDDR5X**（[wccftech](https://wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/)）|
| **Vera CPU**（standalone Arm 88 核） | LPDDR5X（2nd gen，**1024-bit interface / 8 SOCAMM**） | **1.5 TB capacity / 1.2 TB/s bandwidth**（[NVIDIA Vera CPU page](https://www.nvidia.com/en-us/data-center/vera-cpu/)、[NVIDIA Developer Blog](https://developer.nvidia.com/blog/nvidia-vera-cpu-delivers-high-performance-bandwidth-and-efficiency-for-ai-factories/)）|
| **RTX Spark AI PC**（GB10 Superchip） | LPDDR5X（256-bit）+ 3D NAND | **128 GB / 9400 MT/s / 301 GB/s**（[Tom's Hardware Computex 2026](https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory)、[NVIDIA RTX Spark page](https://www.nvidia.com/en-us/products/rtx-spark/)）|
| **Jetson Thor 機器人平台** | LPDDR5X（256-bit）+ 3D NAND | **128 GB / 4266 MHz / 273 GB/s**、120 W TDP（[NVIDIA Jetson Thor page](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)、[RidgeRun Wiki](https://developer.ridgerun.com/wiki/index.php/NVIDIA_Jetson_Thor:_Powering_the_Future_of_Physical_AI)）|

**每條路線都是 multi-year design-in，不是 spot 訂單**——記憶體廠跟著 NVDA 兩年 cadence（Rubin → Rubin Ultra → Feynman）綁死。

### 一張 rack 的記憶體經濟（震撼數字）

- Vera Rubin NVL72 rack 總 BOM **$7.8M**（前代 Grace Blackwell 約 $3.9M）
- 其中**記憶體 = $2M（26% of total）**，比前代 $373K **暴增 435-485%**（[wccftech](https://wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/)、[Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-memory-costs-soar-485-percent-latest-ai-systems-now-cost-usd7-8-million-to-build-memory-now-comprises-25-percent-of-the-total-cost-rubin-gpus-a-mere-usd50-000-apiece)）
- GPU 本身 $50K × 72 = $3.6M、但記憶體已**追上 GPU 為 BOM 主導項**
- → 記憶體不再是「GPU 旁邊的配角」，是 NVDA AI 系統的**核心 BOM 槓桿點**

## 黃仁勳定調事件（2026-06-08）

- SK Hynix x NVDA **multi-year technology cooperation**（[SK hynix Newsroom](https://news.skhynix.com/multi-year-tech-partnership-with-nvidia/)）
- 「AI 相關股票其實很便宜」（黃仁勳語、Yahoo Finance 引述）
- 黃仁勳警告短缺「**可能持續多年**」（[24/7 Wall St.](https://247wallst.com/investing/2026/06/07/nvidia-and-sk-hynix-partner-as-jensen-huang-warns-memory-shortage-could-last-for-years/)）
- 同日：**KOSPI 8.29% 熔斷**（[BBN Times](https://www.bbntimes.com/global-economy/south-korea-s-stock-market-today-kospi-crashes-8-29-to-7-484-triggers-circuit-breaker-as-chip-rout-fed-fears-and-iran-missiles-converge)、[EBC Financial Group](https://www.ebc.com/forex/kospi-crash-korea-trading-halt-ai-june-2026)），Samsung -10.18% / SK Hynix -7.68%
  - **驅動三因**：Broadcom 指引失望（AI chip rout）+ Fed 升息預期（5 月就業報告）+ 以色列伊朗衝突
  - **散戶恐慌訊號**：1.02 億韓國股民帳戶單日熔斷，符合 [[資訊擴散四階段]] 末段警訊
  - 黃仁勳同日宣布合作 → **熔斷 vs 多年合約 = 短期恐慌 vs 多年訂單能見度的對峙**

## 對 wiki 既有 thesis 的校準

### 跟 [[PB 估值法（記憶體週期）]]：對峙 vs 整合？

**對峙觀點**：本 concept 直接挑戰 PB 派的「週期不會消失」核心預設。

**整合觀點（推薦操作框架）**：**雙引擎結構**——
- **HBM / AI 記憶體** = 結構性 infra（用 Forward PE / DCF）
- **傳統 DRAM / NAND** = 仍是週期（用 PB）
- → SK Hynix / Samsung / Micron **估值要拆兩段**

**實務問題：雙引擎可不可行？**

雙引擎的**現實挑戰**：
1. **財報分段揭露不夠細**——HBM 與 DRAM segment 同一條 P&L，外部分析師難以直接拆段定價
2. **產能可流動**——廠商可在 HBM 與 DRAM 間動態切換（93% 已切 HBM），削弱「兩個獨立週期」假設
3. **客戶集中度高**：HBM 50%+ 訂單來自 NVDA + Hyperscaler，單一客戶 thesis 失靈一夕影響全段

**可行路徑（已有先例）**：
- [[宋分（美股送分題）]] / [[HBM iPhone moment]] 已開啟 segment 拆估值的敘事
- SK Hynix 自家 IR 開始分 HBM segment 揭露 wafer share、ASP
- 操作上：**用「HBM 營收占比」+ 「ASP 趨勢」做雙引擎的代理指標**，不必等財報拆分
- 進場時點：HBM 比重 > 40% + ASP YoY > 30% → 切到 Forward PE 框架
- 退場時點：HBM ASP 連續兩季 QoQ 負成長 → 退回 PB 框架

→ 雙引擎**不是嚴格分段 valuation，而是 thesis switching trigger**——這是務實版可行。

### 跟 [[HBM iPhone moment]]

- HBM iPhone moment 是早期 re-rate 假說（2026 Q1 提出）
- 本 concept = **anchor 確認版**：NVDA 多年合約 = sticky design-in、把 thesis 從「可能」升級到「合約鎖死」
- 兩 concept 互相強化、不衝突

### 跟 [[CapEx 見頂辯論]] / [[FCF 拐點]]

- 結構性短缺 = CapEx **不會見頂**、FCF **不會輕易拐點**
- 對「FCF 拐點即將」的多方敘事是直接挑戰
- 同步補強：[[宋分備忘錄 ＃1 — CSP-AI 通縮]] 提到的「Hyperscaler 預付 HBM 訂單到 2028」現有 ANCHOR 確認：
  - 2025-10 OpenAI Stargate x Samsung + SK Hynix LOI = 900K wafer/月（全球 DRAM 40%）（[Tom's Hardware](https://www.tomshardware.com/pc-components/dram/openais-stargate-project-to-consume-up-to-40-percent-of-global-dram-output-inks-deal-with-samsung-and-sk-hynix-to-the-tune-of-up-to-900-000-wafers-per-month)）
  - Micron 已簽**史上首次 5 年合約**（[Micron press 2026](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)）
  - SK Hynix 2026 HBM **全部 sold out**、訂單延伸到 2027（[TechSpot](https://www.techspot.com/news/110058-sk-hynix-completely-sells-out-semiconductor-supply-ai.html)、[ITdaily](https://itdaily.com/news/business/sk-hynix-hbm-2026-sold-out/)）
  - SK Group Chey 直接說「shortage 持續至 2030」（[Tom's Hardware](https://www.tomshardware.com/pc-components/dram/sk-hynix-to-double-memory-wafer-capacity-over-five-years)）
  - **結論**：宋分備忘錄 #1 的「2028 預付」假設被現實 over-shoot 到「2030 結構性短缺」+「multi-year design-in」

### 跟 [[控制點轉移（投資版）]]

- NVDA 拿到**記憶體鏈控制權**——從買方變綁定者、從 spot procurement 變 co-design partner
- SK Hynix 成為 **NVDA 的記憶體 second source-locked**（[FourWeekMBA "NVIDIA is now the OS of the fab"](https://fourweekmba.com/ai-sk-hynix-nvidia-multi-year-partnership-analysis/)）
- 控制點從記憶體廠 → NVDA + **整合方（OSAT / 封裝 / 玻璃）**
- 對應 [[半導體基礎建設化]]：HBM 是六大重新定價指標的**集大成案例**（合約結構改 ✓、客戶關係改 ✓、現金流穩定 ✓）

### 跟 [[Jevons Paradox（投資版）]]

- 效率提升（HBM 容量、頻寬翻倍）不會減少需求，反而 unlock 更大模型訓練/推理場景 → 需求暴增
- DeepSeek case 已驗證：模型效率提升 → token 經濟誘因擴散 → 推理需求倍增
- 本 concept 在 Jevons 邏輯上 = HBM 是 cost-bound 的瓶頸資源、需求彈性極大、無 saturation

### 跟 [[資訊擴散四階段]] / [[市場四階段：懷疑／驗證／共識／反轉]]

- 韓股熔斷 + 1.02 億散戶帳戶 → 已進入**階段 3（共識）/ 4（反轉警示）**
- 但黃仁勳同日 anchor 確認多年訂單 = **基本面 vs 情緒分歧**
- 對逆向投資者：恐慌中找錨點 = [[預期差]] 機會

### 跟 [[宋分備忘錄 ＃1 — CSP-AI 通縮]]：補強 vs 反面

| 主題 | 宋分備忘錄 #1 立場 | 本 concept 補強 |
|---|---|---|
| Hyperscaler 預付到 2028 | 暗示 CapEx 不見頂 | **2025-10 OpenAI 900K wafer/月 LOI + Micron 5 年合約 + SK 2030 預警**——anchor over-shoot |
| AI 通縮 vs CSP 永動機 | 通縮可能讓寬鬆延長 | 本 concept = AI **infra 結構性需求**，CSP 永動機**燃料**就是 HBM/LPDDR5X 上漲訂單 |
| FCF 拐點 | 仍可能出現 | 結構性短缺 + multi-year contract → FCF 拐點被推遲 12-24 月 |

**核心校準**：宋分備忘錄 #1 提出「2028 預付」當作 CSP 永動機的延長子彈，**本 concept = 上膛驗證版**——子彈不只到 2028、且 NVDA 路線圖綁定到 2030+。

## ⭐ 中國市場對沖 anchor（[[中國半導體國產替代（投資對沖視角）]]）

> 本 thesis 的「**全球 HBM / DRAM 結構性短缺到 2030**」假設、需要被「**中國市場 25-30% 全球需求被 [[CXMT]] / YMTC 接管**」對沖反證。

### 對沖三條 anchor

```
anchor 1：HBM 中國市場接管（CXMT）→ SK Hynix / Samsung / Micron 中國 DRAM 收入 -30 至 -50%
anchor 2：3D NAND 中國市場接管（YMTC）→ Kioxia / SanDisk / WDC 中國敞口削弱
anchor 3：AI 算力中國市場接管（華為昇騰）→ NVDA China revenue 20% → < 5%（已發生）
```

### [[CXMT]] 是 HBM 對沖 anchor 的記憶體 entity（2026-06-09 ingest）

- DRAM 全球 #4（7.67% Q4 2025，12 個月翻倍）+ FY2025 營收 YoY **+700%**
- HBM3 樣品交付華為昇騰 / 寒武紀 / 海光、**2026 H2 - 2026 年底量產**
- 規劃 20% 總產能（~60k wafer/月）切 HBM3
- DDR5-8000 / LPDDR5X-10667 量產、中國消費 + server 市場接管 Samsung / SK / Micron 退出空間
- 2026-05 上交所科創板 IPO 審核通過、擬募 USD ~4.2B

### 對三巨頭中國敞口衝擊量化

| 維度 | SK Hynix | Samsung | Micron |
|---|---|---|---|
| 中國 DRAM 營收佔比（2024 估）| 30-35% | 25-30% | 15-20% |
| 中國 HBM 營收佔比（2025 估）| < 5% | 5-10% | < 5% |
| CXMT 接管後 2027-2030 假設 | 中國 DRAM 收入 **-30 至 -50%** | 中國 DRAM 收入 **-20 至 -30%** | 中國 DRAM 收入 **-30 至 -40%** |
| 整體營收衝擊 | 約 **-10 至 -15%** | 約 **-7 至 -10%** | 約 **-5 至 -8%** |

### 估值校準（雙情境）

```
Bull case（原 thesis 維持）：Forward PE 15-25x infra 級、全球壟斷溢價滿配
Base case（中國分裂、本對沖視角）：Forward PE 12-20x infra 級、上限打 8 折
Bear case（中國全閉環 + 西方需求放緩）：Forward PE 8-15x、PB 派部分回歸
```

→ **本 thesis 仍成立**、但**估值上限被裁切 ~15-20%**。對沖視角的真正功能 = **給多頭 thesis 加上限、不是反向操作**。

### 監控指標（補完原監控清單）

- CXMT HBM3 量產進度（2026 H2 - 2026 年底是否兌現）
- CXMT IPO 後 A 股表現 + 估值揭露
- YMTC NAND market share 變化（13% → 15-18%）
- NVDA China revenue % 持續萎縮 / 反彈
- 華為昇騰 950PR / 950DT / 960 / 970 出貨量
- SK Hynix / Samsung / Micron 中國 segment YoY 衰退率（Q4 2026 + Q1 2027 揭露）
- BIS Entity List 新增 / 變動

### 為什麼需要對沖視角

本 concept 原版以「**全球 HBM 結構性短缺到 2030**」為核心 thesis、但**全球 = 西方 + 中國**。當中國市場 25-30% 全球需求被 [[CXMT]] / YMTC 接管：
- 西方 thesis 仍成立、但 SK / Samsung / Micron **不再壟斷全球**
- 「結構性短缺」精準描述應為 **「西方 hyperscaler / 主權 AI 結構性短缺」**
- [[效率→安全切換]] 在中國半導體自主路徑的極端化 = anchor 1-3 的長期 driver

→ 跟 [[宋分備忘錄 ＃1 — CSP-AI 通縮]] 對接：CSP 自研晶片（西方賣水人受惠長期張力）+ 中國國產替代（西方賣水人短期張力）= **雙引擎張力**。

## ⚠️ 風險（thesis 失效情境）

### 1. 模型效率躍進（DeepSeek 2.0）
- DeepSeek MLA + MoE 已示範記憶體效率倍增（KV cache 壓縮、稀疏激活）
- 若下一代模型把 HBM 需求**降回 spot 規格**，多年合約會被重新議價
- 但 [[Jevons Paradox（投資版）]] 提示：效率提升 → 部署擴散 → 整體需求反而暴增（DeepSeek 已驗證一次）

### 2. AI 需求結構性放緩
- CSP CapEx 達物理上限（電力、土地）
- 企業 token spend 觸頂（unit economics 跑不通）
- 若 CSP 取消 2027+ 訂單 → 記憶體廠面對 first-mover oversupply 風險（Micron Idaho fab 2027 mid + 2028 end = bear case 時間錨）（[Investing.com](https://www.investing.com/analysis/microns-soldout-hbm-supply-makes-the-bull-case-hard-to-dismiss-200681391)）

### 3. 替代記憶體技術
- STT-MRAM、HBF（High-Bandwidth Flash）、glass interposer + HBM4E（2028 路線）
- 替代品如改變 HBM 寡占結構 → 三巨頭定價權削弱

### 4. 反壟斷干預
- 韓國公平交易委員會 / 美國 DOJ 對 NVDA-SK Hynix multi-year 合約的審查
- 歷史先例：2002 DRAM 反壟斷罰款 USD 6 億
- 若 NVDA 被迫 multi-sourcing → SK Hynix 的「事實壟斷」溢價被砍

### 5. 韓國勞工 / 地緣風險
- 2026-05 Samsung 4.5 萬人罷工威脅（[Fortune 2026-05-17](https://fortune.com/2026/05/17/labor-strike-samsung-ai-hbm-chips-dividend-revolution-memory/)）
- 對台戰爭 / 北韓事件 → 記憶體供應鏈集中地理風險

### 6. 散戶過度進場（已是訊號）
- 韓股 1.02 億帳戶 + 6/8 熔斷 = [[資訊擴散四階段]] 末段
- 短期 thesis price-in 嚴重、需等回檔

## 雙引擎估值實務操作

### 進場時點（thesis 切到結構性短缺框架）
- HBM segment 營收占比 > 40% ✓（[[HBM iPhone moment]] 已驗證 2026 H1）
- ASP YoY > 30% ✓（DRAM 價格 2025-2026 翻倍）
- 客戶結構：NVDA + Hyperscaler 占 50%+ 且 multi-year contract ✓
- → **2026 Q2 已確認三項滿足，框架切換成立**

### 持有期內監控（thesis 維持 anchor）
- SK Hynix / Samsung / Micron 季度 HBM segment 揭露
- CoWoS / OSAT capacity utilization
- NVDA quarterly call 對 Rubin / Vera ramp 進度
- DeepSeek 類效率躍進事件監測（黑天鵝 catalyst）

### 退場時點（thesis 失效）
- HBM ASP 連續兩季 QoQ 負成長
- NVDA 取消或推遲 Rubin Ultra / Feynman 路線
- 三巨頭其中一家發出「需求疲軟」guidance
- → 回退到 PB 框架（舊景氣循環論）

## 投資受惠鏈

### Tier 1（記憶體三巨頭、直接受惠）
- [[SK Hynix]] — HBM 主供 ~60-70% Vera Rubin 份額、Forward PE 5.92 仍極低、9x 漲幅來自 EPS 而非 multiple expansion → **未完全 re-rate**
- [[Samsung Electronics]] — HBM 50% 擴產（170K → 250K wafer/月 2026 年底）、HBM4 量產追上
- [[Micron]] — HBM4 15K wafer/月 + **首次 5 年合約**、Idaho fab 2027/2028 ramp、bear case 是 first-mover oversupply

### Tier 2（HBM 先進封裝整合方）
- [[TSMC]] — CoWoS 龍頭、產能 125-170 kwpm 仍 sold out
- [[日月光 ASE]] — OSAT 委外 + CoWoP 雙頭
- [[Amkor]] — Intel EMIB + 玻璃基板「3 年內商業化」
- [[Powertech 力成]] — Micron 獨家 HBM packaging + FOPLP 領先 → **OSAT 中最 pure-play HBM**

### Tier 3（賣水人 + 玻璃中介層）
- HBM 設備鏈：ASML、AMAT、KLA、LRCX
- 玻璃基板（HBM4E+ 2028 路線）：[[Corning]]、[[AGC]]、[[Absolics]]、[[Samsung Electro-Mechanics]]
- ABF 載板：[[IBIDEN]]、[[欣興]]、[[南電]]、[[景碩]]

### Tier 4（MLCC / 被動元件、AI server 嵌入）
- [[村田 Murata]]、[[太陽誘電 Taiyo Yuden]]、[[TDK]]、[[國巨]]、[[信昌電]]

## 跟其他 wiki 概念連結

- [[PB 估值法（記憶體週期）]]：對抗 / 整合的對手 thesis（雙引擎結構建議）
- [[HBM iPhone moment]]：前身 thesis 的 anchor 確認版
- [[半導體基礎建設化]]：本 concept 是 HBM 子領域的具體實現
- [[Forward PE 估值法]] / [[DCF vs PE]]：新估值範式工具
- [[控制點轉移（投資版）]]：NVDA 拿到記憶體鏈控制權的具體案例
- [[CapEx 見頂辯論]] / [[FCF 拐點]]：結構性短缺挑戰見頂論
- [[資訊擴散四階段]] / [[市場四階段：懷疑／驗證／共識／反轉]]：韓股熔斷是末段警訊
- [[Jevons Paradox（投資版）]]：HBM 效能提升 → 需求暴增的學術根基
- [[宋分備忘錄 ＃1 — CSP-AI 通縮]]：本 concept 是「2028 預付」假設的 over-shoot 驗證版
- [[賣水人選股邏輯（投資版）]]：Tier 3-4 受惠路徑
- [[預期差]]：韓股熔斷恐慌中找 anchor 的逆向機會

## 主要佐證來源

- [SK hynix Newsroom — Multi-year Tech Partnership with NVIDIA](https://news.skhynix.com/multi-year-tech-partnership-with-nvidia/) — 第一手公告
- [CNBC 2026-06-07 — Nvidia, SK to detail cooperation plan amid prolonged chip shortage](https://www.cnbc.com/2026/06/07/nvidia-sk-to-detail-cooperation-plan-amid-prolonged-chip-shortage.html) — 黃仁勳定調
- [24/7 Wall St. — Memory Shortage Could 'Last for Years'](https://247wallst.com/investing/2026/06/07/nvidia-and-sk-hynix-partner-as-jensen-huang-warns-memory-shortage-could-last-for-years/)
- [Seoul Economic Daily — 'Everything from wafers to cable connectors in short supply'](https://en.sedaily.com/finance/2026/06/07/nvidias-jensen-huang-everything-from-wafers-to-cable)
- [Tom's Hardware — HBM is coming for your PC's RAM (3x wafer ratio)](https://www.tomshardware.com/pc-components/ram/hbm-is-eating-your-ram)
- [Tom's Hardware — Nvidia & SK hynix ink multi-year co-development agreement](https://www.tomshardware.com/pc-components/dram/nvidia-and-sk-hynix-ink-multi-year-memory-co-development-and-supply-agreement-seeks-to-address-extended-development-cycles)
- [Tom's Hardware — SK hynix to double wafer capacity, shortage until 2030](https://www.tomshardware.com/pc-components/dram/sk-hynix-to-double-memory-wafer-capacity-over-five-years)
- [Tom's Hardware — Samsung & SK warn shortages could last until 2027 and beyond](https://www.tomshardware.com/tech-industry/artificial-intelligence/samsung-and-sk-hynix-warn-ai-driven-memory-shortages-could-last-until-2027-and-beyond-as-hbm-demand-explodes-customers-already-reserving-supply-years-ahead-while-the-wider-dram-market-begins-to-tighten)
- [Tom's Hardware — Memory costs 26% of Vera Rubin BOM (435% surge)](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-memory-costs-soar-485-percent-latest-ai-systems-now-cost-usd7-8-million-to-build-memory-now-comprises-25-percent-of-the-total-cost-rubin-gpus-a-mere-usd50-000-apiece)
- [Tom's Hardware — RTX Spark Superchip at Computex 2026](https://www.tomshardware.com/laptops/nvidia-unveils-rtx-spark-superchip-at-computex-2026-new-platform-promises-to-turn-windows-into-an-agentic-ai-os-with-arm-cpu-blackwell-gpu-and-128gb-unified-memory)
- [Tom's Hardware — OpenAI Stargate 900K wafer/月 LOI](https://www.tomshardware.com/pc-components/dram/openais-stargate-project-to-consume-up-to-40-percent-of-global-dram-output-inks-deal-with-samsung-and-sk-hynix-to-the-tune-of-up-to-900-000-wafers-per-month)
- [NVIDIA — Vera CPU product page](https://www.nvidia.com/en-us/data-center/vera-cpu/)
- [NVIDIA Developer Blog — Vera CPU LPDDR5X 1.2 TB/s](https://developer.nvidia.com/blog/nvidia-vera-cpu-delivers-high-performance-bandwidth-and-efficiency-for-ai-factories/)
- [NVIDIA — Jetson Thor 128GB LPDDR5X](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
- [NVIDIA — RTX Spark product page](https://www.nvidia.com/en-us/products/rtx-spark/)
- [Micron — HBM4 Vera Rubin + 5-year contract](https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin)
- [TrendForce 2026-06-08 — SK hynix Vera CPU memory supply](https://www.trendforce.com/news/2026/06/08/news-sk-hynix-to-supply-memory-for-nvidia-vera-cpu-as-partnership-deepens-samsung-meeting-on-june-8-in-spotlight/)
- [Astute Group — Memory Supply Constraints Stretch to 2030](https://www.astutegroup.com/news/memory-shortages/memory-supply-constraints-stretch-toward-2030-as-ai-demand-reshapes-dram-production/)
- [BBN Times — KOSPI 8.29% Circuit Breaker 2026-06-08](https://www.bbntimes.com/global-economy/south-korea-s-stock-market-today-kospi-crashes-8-29-to-7-484-triggers-circuit-breaker-as-chip-rout-fed-fears-and-iran-missiles-converge)
- [TradingKey — Korean retail "national stock frenzy"](https://www.tradingkey.com/analysis/stocks/more/261951350-kospi-crash-circuit-breaker-samsung-sk-hynix-broadcom-guidance-fed-hikes-retail-leverage-krw-outflow-tradingkey)
- [SemiAnalysis — Vera Rubin Extreme Co-Design](https://newsletter.semianalysis.com/p/vera-rubin-extreme-co-design-an-evolution)
- [FourWeekMBA — NVIDIA is now the OS of the fab](https://fourweekmba.com/ai-sk-hynix-nvidia-multi-year-partnership-analysis/)
- [Modern Value Investing — SK Hynix still cheap after 9x move (FP/E 5.8)](https://modernvalueinvesting.substack.com/p/sk-hynix-still-cheap-after-a-9x-move)
- [Silicon Analysts — TSMC CoWoS 50+ weeks lead time Q1 2026](https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026)
- [FinancialContent — TSMC CoWoS 35→130K wafer/月](https://markets.financialcontent.com/wral/article/tokenring-2026-1-1-the-great-packaging-pivot-how-tsmc-is-doubling-cowos-capacity-to-break-the-ai-supply-bottleneck-through-2026)
- [Memory supercycle through 2028 — Blocks & Files](https://www.blocksandfiles.com/ai-ml/2026/01/21/memory-semiconductor-supercycle-set-to-run-through-2028/4090501)
- [PC Gamer — Memory crisis could run past 2028 ("minimize oversupply risk")](https://www.pcgamer.com/hardware/memory/memory-crisis-and-sky-high-dram-prices-could-run-past-2028-as-samsung-and-sk-hynix-opt-to-minimize-the-risk-of-oversupply/)
- [wccftech — Vera Rubin rack memory price 435% surge](https://wccftech.com/nvidia-vera-rubin-rack-hit-with-memory-price-surge-pushing-hbm4-lpddr5x-bill-to-2m-of-7-8m-total/)
- [DeepSeek paradigm shifts arXiv](https://arxiv.org/pdf/2507.09955) — 模型效率 vs 記憶體需求 tension
- [Fortune 2026-05-17 — Samsung 45K labor strike threat](https://fortune.com/2026/05/17/labor-strike-samsung-ai-hbm-chips-dividend-revolution-memory/)

## 相關連結

- [[PB 估值法（記憶體週期）]]
- [[HBM iPhone moment]]
- [[半導體基礎建設化]]
- [[Forward PE 估值法]]
- [[DCF vs PE]]
- [[控制點轉移（投資版）]]
- [[CapEx 見頂辯論]]
- [[FCF 拐點]]
- [[資訊擴散四階段]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[Jevons Paradox（投資版）]]
- [[宋分備忘錄 ＃1 — CSP-AI 通縮]]
- [[賣水人選股邏輯（投資版）]]
- [[預期差]]
- [[NVDA]]
- [[TSMC]]
- [[Powertech 力成]]
- [[日月光 ASE]]
- [[Amkor]]
- [[IBIDEN]]
- [[Corning]]
- [[AGC]]
- [[Absolics]]
- [[Samsung Electro-Mechanics]]

---
title: Lumentum
aliases: [LITE, Lumentum Holdings, Lumentum Holdings Inc, 流明, NASDAQ:LITE]
type: entity
created: 2026-06-05
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-12-05
sources:
  - raw/2026-06-05_Leo-DCI-Hyper-Rail-CIEN-COHR-LITE-NOK.md
  - raw/2026-06-08_Leo-AI-infra-CapEx-三階段論-1.6T-光模組-InP.md
  - raw/2026-06-09_SemiAnalysis-800VDC-CPO-延期-機構報告中文摘要.md
tags: [標的, 美股, 光通訊, 光引擎, CPO, pump laser, EML, InP, DCI, foreign_competitor, NVDA]
confidence: high
---

# Lumentum（LITE）

## 1. 一句話定位

**全球光通訊「laser 純度最高」的光引擎廠**——2015 年從 JDSU 拆分、總部 San Jose；做 InP（indium phosphide）半導體雷射晶片 + 雷射模組為核心，旗下 **EML（Electro-absorption Modulated Laser）** 是 1.6T 光模組的關鍵元件、**pump laser** 是 EDFA 光放大器與 [[Hyper Rail / Multi-Rail（光通訊整合技術）]] 共用光源、**OCS（Optical Circuit Switch）** 是 Google AI fabric 唯一商業化的光交換機；FY2026 Q3 營收 **$808M（YoY +90%）**、Q4 自家指引 **$960M-$1.01B（再創高）**、是 [[CPO 供應鏈圖譜]] 第 2 層光引擎「純度首選」（vs [[Coherent]] 還有 SiC + 工業雷射混在一起）；2026-03-02 拿到 [[NVDA]] **$2B 戰略投資 + 多年購買承諾 + 未來產能優先權**（與 [[Coherent]] 同日同額對倒），管理層稱目前**供需缺口 >30%**（EML / pump laser 雙瓶頸）。

## 2. 三層 thesis

### 產業層

- 光通訊 / 光引擎 [[市場四階段：懷疑／驗證／共識／反轉]] 處於「**驗證 → 共識**」加速段
  - 全球 AI 光收發器市場 2026 估 **USD $260 億**（TrendForce 2026-04）
  - 1.6T 模組需求 **2025 1.8M units → 2026 30M+ units**（17 倍增量）
  - 1.6T 模組中 [[NVDA]] 占 **>60%** 需求、Google + Meta 補齊
  - NVDA GB300 機櫃單台需要 **162 個 1.6T 模組**
- DCI（Data Center Interconnect）賽道進入 [[Hyper Rail / Multi-Rail（光通訊整合技術）]] 過渡期
  - [[Ciena]] Hyper Rail 確定 **2027 部署**（CIEN 法說逐字稿）
  - [[Nokia]] 1830 GX Multi-Rail OLS **2026 H2** 出貨
  - 兩者都需要**高品質 pump laser** + 高密度光元件
- CPO（[[CPO 供應鏈圖譜]] 第 2 層）2026 H2 NVDA Spectrum-X Photonics 開始出貨
- 跟 [[Jevons Paradox（投資版）]] 直接相關：
  - Hyper Rail / CPO 提升光元件使用效率 → 直覺上 pump laser / EML 用量減少
  - 反直覺結果：CSP 更大規模部署 → 元件**總用量反而上升**（與 Leo 原 thesis 一致）

### 目的層

- 業務 mix（FY2026 Q3）：
  - **Components = 66% 營收**（$533M、YoY +77%）：
    - Narrow linewidth lasers：**YoY +120%**
    - Pump lasers：**YoY +80%**
    - EML：**單季 200G EML 營收環比 +100%+**
    - **全球唯一 200G EML 大量出貨者**
  - **Systems = 34% 營收**（$275M、YoY +121%）：
    - Cloud transceivers 環比 +40%
    - OCS（optical circuit switch）backlog **>$400M**
- **「純光通訊曝險」**：跟 [[Coherent]] 對比，LITE **沒有 SiC、沒有工業雷射主導業務**
  - 商業雷射 / 3D sensing 殘留：占比 <10% 且不是成長引擎
  - → 與 [[Coherent]] Industrial 25% / Datacenter & Communications 75% 形成對照
  - **AI / 光通訊純度 ~85-90%**（vs COHR ~75%）
- 客戶結構：
  - [[NVDA]] = **strategic anchor** 客戶（$2B 投資 + 多年承諾）
  - 其他 AI infra 客戶：[[Microsoft]]、[[Meta]]、[[Google]]、[[AMZN]] 透過 OEM 端拿模組
  - Hyperscaler 直接拿 OCS：Google 是 OCS 商業化最大客戶
  - OEM 中間商：Innolight、新易盛、Coherent 自己（買 LITE EML die）轉模組
- → 連 [[賣水人選股邏輯（投資版）]]：**「laser die 賣水人」**
  - 不押 OEM 模組廠誰贏（Innolight / Coherent transceiver / Eoptolink 都需要 EML / pump laser）
  - 押**最上游 InP 半導體雷射 die**（全球僅 2-3 家有量級供應）

### 供應層

- 跟 [[NVDA]] 路線：**2026-03-02 戰略投資 $2B（與 Coherent 同日同額對倒）**
  - 非獨家、但含**多年購買承諾**（multi-billion dollar）+ **未來雷射元件產能優先權**
  - **Greensboro, NC 新廠**（240,000 sqft、向 Qorvo 收購、retrofit 為 6-inch InP 線）
    - NVDA 是 anchor 客戶
    - **2028 中量產**
    - 美國產能 = 抗中美光通訊技術脫鉤
  - Spectrum-X Photonics（2026 H2 開始出貨）= NVDA 第一代 CPO 整合 switch
- 跟 [[Ciena]] Hyper Rail（2027 部署）：
  - Hyper Rail 把 pump laser 整合為「**多條光纖共用 single pump source**」= LITE pump laser 是核心元件
  - Ciena 提供 WaveLogic chipset 給 LITE / NeoPhotonics / Oclaro 製作 coherent 光模組
- 跟 [[Nokia]] Multi-Rail OLS（2026 H2）：
  - Nokia 多 rail ILA 達 **160 fiber pairs/rack**（vs 當前 4 fiber pairs/rack、40 倍密度增加）
  - 需要 pump laser **體積縮小 + 數量增加** = LITE 受惠（單台 ILA pump 用量 ~30+）
- pump laser 競爭地位：
  - 全球 single-mode pump laser 主要玩家：**Lumentum、Coherent、Furukawa Electric、Anritsu**
  - LITE 在 pump laser / EDFA 元件全球**前三**
  - **pump laser YoY +80%** = 供需缺口 + 漲價傳導
- EML 競爭地位：
  - **全球唯一 200G EML 量產者**（next-gen 1.6T 模組關鍵）
  - 200G EML ASP 從 $14 漲到 $20（2026）= 漲價持續
  - COHR 用 **6-inch InP 線**追趕（單 wafer 更多 die、單 die 成本更低）
- OCS 競爭地位：
  - Google AI fabric 商業化唯一 OCS 供應商
  - backlog >$400M
- 護城河：
  - **InP 半導體雷射 IP**（從 JDSU 1980s 累積）
  - **EML 良率**（200G EML 真正能量產的家族）
  - 與 [[NVDA]] $2B 戰略綁定 = AI 算力時代雷射控制點
- 風險：
  - **單一客戶 NVDA 依賴**（2-3 年 ramp 期高度集中）
  - COHR 用 6-inch InP 在 EML 端追趕（單 die 成本更低）
  - CPO 走入 NVDA Spectrum-X 後可能架構改變、外採模式可能變
  - Greensboro 廠 2028 中才量產 = 短期產能仍受限
- → 連 [[控制點轉移（投資版）]]：LITE 在 **「InP 雷射 die 層」拿到控制點**，但**模組層被 OEM 切走**

## 3. 財務狀態快照（As of 2026-06-05）

| 指標 | 數值 |
|---|---|
| 股價 | $900.00（2026-06-05） |
| 52 週區間 | $79.50 → $1,085.68 |
| 12 個月漲幅 | **+1,542%**（thematic 行情完整一段） |
| 市值 | **$64-73B** USD（不同源略異） |
| Forward PE | **52-59 倍**（vs hardware median 25.49）= 高 104% |
| FY2026 Q3 營收 | **$808.4M**（YoY +90.1%） |
| FY2026 Q3 GAAP OP margin | **21.6%**（從去年負值翻正） |
| FY2026 Q3 Non-GAAP OP margin | **32.2%** |
| FY2026 Q3 Non-GAAP 毛利率 | **47.9%** |
| Components 營收 | $533M（+77%、占 66%） |
| Systems 營收 | $275M（+121%、占 34%） |
| Q4 FY2026 自家指引營收 | **$960M-$1.01B**（再創高）|
| Q4 FY2026 自家指引 OP margin | **35-36%** |
| Q4 FY2026 自家指引 Non-GAAP EPS | **$2.85-$3.05** |
| 全年 YoY 成長 | **>85%**（自家指引）|
| 供需缺口 | **>30%**（CEO 揭露）|
| OCS backlog | **>$400M** |
| CPO 增量訂單 | 多億美元、2027 H1 交付 |
| EML（200G）出貨 | **單季環比 +100%**、全球唯一量產者 |
| 12 月季度 EML unit 預期 | **YoY +50%**（自家指引）|
| Greensboro NC InP fab | 240k sqft、2028 中量產 |

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ NVDA $2B 戰略投資 + 多年購買承諾、AI / 光通訊純度 ~85-90% |
| 毛利率 | ✅ 非 GAAP 毛利 47.9%、200G EML / pump laser 漲價傳導 + 供不應求 |
| OpEx | ⚠️ Greensboro 廠 retrofit + R&D 加重、2028 中才量產 |
| 營業利益 | ✅ GAAP OP 21.6%（從負值翻正）、Non-GAAP 32.2%、Q4 指引 35-36% = 營業槓桿全開 |

→ **Re-rate 三角形 3/4**——是 AI 光通訊「第一象限」最純度的受惠者，但 Forward PE 52-59 + 12 個月 +1,542% 已 price in 多年 ramp + NVDA 綁定 option value。

### ✅ 催化

- 🆕 **2026-06-08 InP 供應緊繃 anchor**（Leo 2026-06-08 筆記）：Lumentum 法說揭露**供應限制延伸到 2026 全年**、EML 供需缺口從上季 30%+ 持續擴大、日本 wafer fab fully allocated + premium pricing——跟 [[Coherent]] InP delivery **>26 週** + [[IQE]] £81M 融資 + FY 2026 **>20% 成長**指引**同月（2026-05）4 週內同步揭露**、整鏈瓶頸**時序高度收斂、不是巧合**
- 對 [[AI infra CapEx 三階段論]] 第三階段是最強訊號
- 1.6T 模組需求 2025→2026 從 1.8M units 跳到 30M+ units（17 倍增量、NVDA 占 60%）
- 200G EML 全球唯一量產者 + ASP 漲價（$14 → $20）持續
- pump laser 受 [[Hyper Rail / Multi-Rail（光通訊整合技術）]] 拉動（Ciena 2027 / Nokia 2026 H2 雙催化）
- OCS backlog >$400M、Google AI fabric 商業化
- CPO 訂單多億美元 2027 H1 交付（NVDA Spectrum-X Photonics 第一代）
- Greensboro NC 6-inch InP 廠 retrofit 中（2028 中量產 = NVDA anchor + 美國產能政治紅利）
- 供需缺口 >30%（CEO 揭露）= 漲價週期未完
- FY2026 全年 YoY >85% 成長（自家指引）
- 半導體基礎建設化（[[半導體基礎建設化]]）= 從週期股轉結構性成長股

### ⚠️ 風險

- **單一客戶 NVDA 依賴**（$2B 戰略 + 多年承諾 = 蜜糖也是枷鎖）
- **Forward PE 52-59 + 12 個月 +1,542%**——估值已 price in 多年 ramp 完美執行
- [[Coherent]] 用 6-inch InP 線追趕、單 die 成本更低 = EML 中長期競爭壓力
- Greensboro NC 廠 2028 中才量產 = 短期產能仍受限、若 NVDA 拉 ramp 來不及做不出
- NVDA 自研雷射 die / 整合 CPO 後改變外採模式（低機率但要追蹤）
- 中美技術脫鉤、InP 原料 / 設備受限（低機率）
- CPO 標準若延遲、光通訊整體 TAM 推延
- Ceramics / 商業雷射 / 3D sensing 殘留業務拖後腿（占比 <10% 但毛利稀釋）

## ⭐ 對 [[CPO 供應鏈圖譜]] 第 2 層的意義（光引擎）

LITE 在 CPO 第 2 層的地位：

- **InP 雷射 die 層**：全球僅 2-3 家、LITE 是 200G EML 唯一量產者
- **第 7 層雷射光源層**：與 [[Coherent]] 並列龍頭（pump laser 全球前三）
- **跨第 2 + 第 7 兩層**：LITE 不只賣模組，也賣裡面的 laser die 給其他 OEM（包括 COHR 自己也買）= **「laser 純度最高 + 兩層同時拿」**

對 [[CPO 供應鏈圖譜]] 第 2 層的補強：
- LITE / COHR 都是「光引擎」候選贏家
- **LITE 路徑：純 InP die 領先**（vs COHR 多軌全包）
- 兩家若 NVDA 同時投資 = NVDA **想「從 scale up 到 scale across 都包下來」**（Leo 原 thesis）

## ⭐ 對台股 CPO 供應鏈的意義

對 [[SiTime]]（timing）、[[AVGO]]（交換 ASIC）、[[Marvell]]、[[TSMC]]：

**Bull case**：
- LITE 強（laser die 純度）→ 全球光模組 ramp 順利 → CPO 整體 TAM 擴大 → [[SiTime]] timing 三倍 BOM 受惠
- LITE EML / pump laser 供應充足 → [[AVGO]] Tomahawk + Jericho CPO 模組順利出貨 → AVGO ASIC TAM 擴張
- LITE 美國產能 = NVDA / hyperscaler 美系供應鏈穩定 → 台廠 CPO 設備（[[鈦昇]]、[[弘塑]]、[[萬潤]]）有訂單能見度

**Bear case**：
- LITE / COHR 兩家高度集中 NVDA $2B → 整合度太高、上下游空間被擠壓
- LITE 走入 CPO 整合方向 → 模組層被吃掉 = 台廠 OEM 模組廠（旭創、新易盛、海信）模組生意分流
- LITE Greensboro 廠 2028 才量產 → 短期產能仍 bottleneck → 1.6T ramp 可能延遲 → CPO 整體 TAM 確認延後

對 [[CPO 供應鏈圖譜]] 第 2 層的影響：
- 過去寫「**不押光引擎誰贏**」（因為 LITE vs COHR vs 博通自研 不確定）
- 校準後：LITE = laser die 純度首選、COHR = scale + SiC 第二曲線
- 押法：**不單押 LITE 一家**（NVDA 同時投兩家 = 兩家都會受惠）、**改押 LITE + COHR 一籃子**（更接近 Leo 個人決策的思路）

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | 4 | NVDA $2B 戰略綁定 + Hyper Rail / Multi-Rail / CPO 三路徑都吃 |
| 站別關鍵 | 5 | 200G EML **全球唯一量產者** + pump laser 全球前三 + OCS Google 唯一商業化 = **絕對站別關鍵** |
| 耗材 | 3 | InP 雷射 die 是耗材但 ASP 高、單 die 數量有限（不像 Murata MLCC 每年百億顆量） |
| IP | 5 | InP 半導體雷射 IP（從 JDSU 1980s 累積 40+ 年）+ EML 良率護城河 |
| 客戶分散 | 2 | NVDA 戰略獨家（$2B 投資 + 多年承諾）= 集中度高、短期是優勢長期是風險 |

**總分：19/25**

### vs [[Coherent]] 五軸對照

| 軸 | LITE | COHR | 說明 |
|---|---|---|---|
| 路線敏感 | 4 | 4 | NVDA 兩家同時投、CPO + Hyper Rail 同時吃，打平 |
| 站別關鍵 | **5** | 4 | LITE 200G EML 唯一量產 = 略勝 |
| 耗材 | 3 | 3 | InP 雷射 die 兩家差不多、SiC wafer 是 COHR 額外加分但耗材性質不同 |
| IP | **5** | 4 | LITE InP 純度更高 = 略勝 |
| 客戶分散 | 2 | **4** | COHR Industrial 25% + 工業雷射 + SiC 客戶分散得多 |
| **總分** | **19/25** | **19/25** | **打平**——LITE 純度 + IP 勝、COHR 客戶分散 + 多元 hedge 勝 |

→ **校準 Leo 原 thesis**：「LITE 純度首選 + COHR SiC 後來成優勢」**完全成立**——五軸總分打平、各有勝場、NVDA 同時投兩家、Leo「LITE + COHR 一籃子」的隱含思路是對的。

→ 跟 [[IBIDEN]] 19/25 + [[欣興]] 19/25 並列「**AI 半導體基礎建設四大 19 分組**」。

## #P1 SemiAnalysis CPO 延期校準（2026-06-10）

SemiAnalysis 2026-06-09 機構報告把 LITE 列「高度依賴 CPO 大規模量產論述」受壓組、2026-06-09 光通訊板塊賣壓（[[AAOI]] -14% 領跌）。校準拆解（[[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|驗證 summary]]）：

- **受壓的是 CPO 敘事溢價段**：scale-up CPO 2029+（綁 Feynman）、Spectrum-X Photonics（SN6810）板級插損問題（⚪ channel check）——LITE 的 CPO 外部光源／光引擎故事兌現推遲
- **本業反而受惠**：可插拔主流延長至 2028+ → EML（200G 唯一量產）／pump laser 缺口 >30% 的供需結構**更久**；1.6T 可插拔 17 倍增量不受 CPO 延期影響
- **NVDA $2B（2026-03）+ 多年購買承諾 = 「延後≠取消」的結構反證**——NVDA 不會對 2029 才兌現的賽道現在就鎖產能、除非結構必然
- **19/25 維持**——敘事權重從「CPO 第 2 層」移回「EML／pump laser 缺口 + Greensboro 2028 量產」；Forward PE 52-59x 對敘事修正的敏感度要監控（12M +1,542% 是板塊內回檔彈性最大的）

## 跟其他 wiki 概念連結

- [[CPO 供應鏈圖譜]]：第 2 層 + 第 7 層光源「光引擎純度首選」
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：Ciena Hyper Rail 2027 + Nokia 1830 GX Multi-Rail 2026 H2 雙催化
- [[Jevons Paradox（投資版）]]：Hyper Rail 提升效率 → 反而 pump laser / EML 總用量上升
- [[賣水人選股邏輯（投資版）]]：**「laser die 賣水人」**——不押模組廠誰贏、押最上游 InP die
- [[半導體基礎建設化]]：從週期股 → 結構性成長股的最清楚案例（OP margin 從負值翻 32.2%）
- [[控制點轉移（投資版）]]：拿到「InP 雷射 die 層」控制點、模組層被 OEM 切走
- [[市場四階段：懷疑／驗證／共識／反轉]]：光通訊在「驗證 → 共識」加速段
- [[資訊擴散四階段]]：12 個月 +1,542% 已過散戶看到階段、進入「共識」段
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 強制格式
- [[NVDA]]：$2B 戰略投資 + 多年購買承諾 + 未來產能優先權（與 COHR 同日同額對倒）
- [[Coherent]]：直接對手、NVDA 同日同額投資、Leo 隱含「LITE + COHR 一籃子」
- [[Ciena]]（CIEN）：Hyper Rail 2027 部署、WaveLogic chipset 給 LITE 製作 coherent 模組
- [[Nokia]]（NOK）：1830 GX Multi-Rail OLS 2026 H2、訂單外溢承接
- [[AVGO]]：Tomahawk 8 / Jericho CPO 模組需要 LITE EML / pump laser
- [[SiTime]]：CPO 三倍 BOM timing 與 LITE EML 雙協同
- [[Corning]]：NVDA 同時投資 Corning 玻璃纖維（$3.2B）+ LITE / COHR laser = NVDA 光通訊全堆疊投資
- [[IQE]]：純 play 化合物半導體 epi foundry、LITE 自家 InP fab（日本 fully allocated + Greensboro NC 2028 中量產）的**外部 epi 補位** + IQE 6" InP DFB 平台 industry-first 對 LITE 主流 4" 線是 IP 壓力、未來 LITE Greensboro 廠 2028 上線可能去 IQE 庫存

## 相關連結

- [[CPO 供應鏈圖譜]]
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]
- [[Jevons Paradox（投資版）]]
- [[賣水人選股邏輯（投資版）]]
- [[半導體基礎建設化]]
- [[控制點轉移（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[Coherent]]、[[NVDA]]、[[AVGO]]、[[SiTime]]、[[Corning]]
- [[Ciena]]、[[Nokia]]
- [[IQE]]、[[AI infra CapEx 三階段論]]

## Sources

- [Lumentum (NASDAQ: LITE) Q3 2026 revenue jumps 90% with stronger margins and Q4 outlook (StockTitan, 2026-05)](https://www.stocktitan.net/sec-filings/LITE/8-k-lumentum-holdings-inc-reports-material-event-71c29c340aa4.html)
- [Lumentum Q3 2026 Earnings Transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/05/06/lumentum-lite-q3-2026-earnings-transcript/)
- [LITE Q3 2026 Earnings Call — Revenue Surges 90% to Record $808M (BigGo Finance)](https://finance.biggo.com/news/US_LITE_2026-05-05)
- [Lumentum's quarterly revenue grows 90% YoY to $808.4m (Semiconductor Today, 2026-05)](https://www.semiconductor-today.com/news_items/2026/may/lumentum-140526.shtml)
- [NVIDIA Announces Strategic Partnership With Lumentum (NVIDIA Newsroom, 2026-03)](https://nvidianews.nvidia.com/news/nvidia-announces-strategic-partnership-with-lumentum-to-develop-state-of-the-art-optics-technology)
- [Nvidia to invest $4 billion into photonics companies Coherent and Lumentum (CNBC, 2026-03-02)](https://www.cnbc.com/2026/03/02/nvidia-investment-coherent-lumentum.html)
- [NVIDIA Commits $2 Billion Investment and Purchase Deal to Lumentum (mlq.ai)](https://mlq.ai/news/nvidia-commits-2-billion-investment-and-purchase-deal-to-lumentum-for-ai-optics-expansion/)
- [Lumentum to establish new US plant to manufacture InP lasers for AI data centers (Semiconductor Today, 2026-03)](https://www.semiconductor-today.com/news_items/2026/mar/lumentum-260326.shtml)
- [Lumentum to Build North Carolina Fab for InP Lasers (Converge Digest)](https://convergedigest.com/lumentum-to-build-north-carolina-fab-for-inp-lasers/)
- [Lumentum's AI Laser Chip Momentum Builds: More Upside Ahead? (Zacks via TradingView)](https://www.tradingview.com/news/zacks:ed0d49ad7094b:0-lumentum-s-ai-laser-chip-momentum-builds-more-upside-ahead/)
- [The Lumentum Series Part 2: Co-Packaged Omnipotence (jasonschips Substack)](https://jasonschips.substack.com/p/the-lumentum-series-part-2-co-packaged)
- [NVIDIA's $4B Photonics Play: Lumentum vs Coherent 2026 (tech-insider.org)](https://tech-insider.org/nvidia-silicon-photonics-lumentum-coherent-ai-data-center-2026/)
- [NVIDIA's $4B Optics Bet Signals Photonics as AI's Next Bottleneck (Futurum)](https://futurumgroup.com/insights/nvidias-4b-optics-bet-signals-photonics-as-ais-next-bottleneck/)
- [Ciena Solidifies AI Networking Leadership (Ciena Press, 2026)](https://www.ciena.com/about/newsroom/press-releases/ciena-solidifies-ai-networking-leadership-unveils-new-innovations-for-high-speed-connectivity)
- [What is multi-rail / hyper-rail? (Ciena Insights)](https://www.ciena.com/insights/what-is/what-is-hyper-rail-or-multi-rail)
- [Ciena Expands Distribution Channel for WaveLogic to Lumentum (Ciena Press)](https://www.ciena.com/about/newsroom/press-releases/Ciena-Expands-Addressable-Market-by-Opening-Global-Distribution-Channel-for-WaveLogic-Coherent-Technology.html)
- [Global AI Optical Transceiver Market to Reach US$26 Billion in 2026 (TrendForce 2026-04)](https://www.trendforce.com/presscenter/news/20260420-13017.html)
- [LITE Forward PE Ratio: 52.02 (GuruFocus, 2026-06)](https://www.gurufocus.com/term/forward-pe-ratio/LITE)
- [Lumentum Holdings (LITE) Stock Price (Yahoo Finance)](https://finance.yahoo.com/quote/LITE/)
- [What is Competitive Landscape of Lumentum Company (PortersFiveForce)](https://portersfiveforce.com/blogs/competitors/lumentum)
- [Lumentum Pump Lasers product page](https://www.lumentum.com/en/optical-communications/products/pump-lasers)

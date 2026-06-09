---
title: Ciena
aliases: [Ciena, CIEN, CIEN.US, Ciena Corp]
type: entity
created: 2026-06-05
updated: 2026-06-05
as_of: 2026-06-05
check_after: 2026-12-05
sources:
  - raw/2026-06-05_Leo-DCI-Hyper-Rail-CIEN-COHR-LITE-NOK.md
tags: [標的, 美股, DCI, 光通訊, 設備商, foreign_competitor, AI 基礎設施, hyperscaler]
confidence: high
---

# Ciena（CIEN）

## 1. 一句話定位

**DCI（Data Center Interconnect）光網路設備絕對龍頭 + AI 算力「scale across」物理基礎建設**——成立 1992 年的馬里蘭州 coherent 光網路廠、WaveLogic DSP 連續六代領先（最新 WaveLogic 6 Extreme 支援單載波 1.6 Tb/s）、推 **HyperRail / Multi-Rail RLS** 整合式光學線路系統（co-developed with hyperscalers）；FY2026 H1 雲端客戶（CSP / hyperscaler）營收占比已從一年前的個位數跳到 **46%**（YoY +70%）、單季 backlog **$7.7B**（QoQ +$600M）、FY2026 營收指引 $6.3B（+32% YoY）；HyperRail **2027 H1 開始部署**（已拿到「industry's first multi-rail order」、單筆合約「hundreds of millions」級別、跨多年）；目前**供應跟不上需求**、訂單外溢給 [[Nokia]] 的可能性已被法說會本人證實「constrained supply environment」。

## 2. 三層 thesis

### 產業層

- DCI 賽道 [[市場四階段：懷疑／驗證／共識／反轉]] 在「**驗證 → 共識加速**」段——四大 hyperscaler（AWS / Microsoft / Google / Meta）2026 CapEx 合計 **>$600B**、其中越來越大比例砸進「**AI 訓練要把資料中心連起來**」這條物理瓶頸
- 重新定義的 DCI 範圍（Ciena 2026-Q2 法說會）：
  - **scale up**（chip-to-chip 在 rack 內）→ [[NVDA]] NVLink、CPO 主場
  - **scale out**（rack-to-rack 在同 DC 內）→ AVGO / Marvell 交換 ASIC 主場
  - **scale across**（DC-to-DC 跨百-千 km）→ **CIEN HyperRail 主場**
  - **submarine**（跨海）→ CIEN + Nokia 雙頭
- TAM 重估：原本 DCI 是「電信 metro/long-haul 子集」、現在 **AI training facility 跨 site 互連** 把 DCI 從「電信外圍」拉成「**AI infra 必經之路**」、TAM 估值倍數 re-rate（CIEN PE 已反映：Forward PE 80-91x、Hardware median 25x、高 200%+）
- 競爭格局：
  - **CIEN**：DCI 純度最高（光網路 + DSP + 線路系統垂直整合、無無線業務拖累）
  - [[Nokia]]：DCI 是 Network Infrastructure 一支（光網路 / IP / 固網），整體還有無線業務、純度較低但「9 of top 10 hyperscaler 都用 Nokia 光網路」基數深
  - [[Cisco]]：交換 ASIC + 路由器主場、DCI 是補強（[[FOMO SOC]] #48 列為對沖位、付費牆擋住具體 thesis）
  - 中國 Huawei + 中興：被美 entity list 排除在西方 hyperscaler 外
- → DCI 賽道在「**雙頭 + 寡占**」：CIEN（純度王）vs Nokia（廣度王）

### 目的層

- 主業 mix（FY2026 Q2、截至 2026-05-02）：
  - **Networking Platforms（含 Optical Networking）= 主體** ≈ 72% 營收（Q1 數字）→ Q2 光網路 YoY **>+40%**
  - **Platform Software & Services** + **Global Services** = 餘下、margin 較穩
  - 從產品線看：RLS（HyperRail 平台）、Waveserver、6500 reconfigurable line system 各自 YoY +50%、路由 + 交換 +88%（DCOM out-of-band management ramp）
- 客戶結構（FY2026 Q2）：
  - **Cloud（hyperscaler 直銷）= 46% 營收**（YoY +70%）、其中**兩家 cloud 客戶各占 >10%**（合計 34%）= 集中度極高、A 客戶單季 $321M、B 客戶單季 $212M
  - **Service Provider（電信 CSP）= 餘下大宗**（YoY +28%、印度地區 YoY +>100%）
  - **政府 / 國防**：少數但毛利穩定
  - 預估 cloud / service provider 比例會繼續往 cloud 移動（hyperscaler AI CapEx > 電信 CapEx）
- 商業模式：**ASP 倍增 + 量倍增**雙引擎
  - WaveLogic 6 Extreme 從 800G → 1.6T、單載波 ASP 結構性提升
  - HyperRail 把 pump laser + amplifier + WSS 整合進**單一 sled**、ASP 比傳統 OLS 高（co-designed with hyperscaler、custom 化議價力強）
  - **128 fiber pairs / rack**（vs 傳統 4 pairs）= 32x 密度、power -75%、space -85% → hyperscaler 願意溢價買
- → 連 [[賣水人選股邏輯（投資版）]]：AI scale across **唯一純度玩家**、不押誰 win 訓練（CIEN 賺所有 hyperscaler 之間連線的水）

### 供應層

- 跟 hyperscaler 路線：HyperRail **與 hyperscaler co-developed**（Ciena 法說會原話）= 拿到 design partner 位、設計鎖死
  - **2026 standardization** → **2027 deployment ramp** → 多年合約
  - 已收「industry's first multi-rail order」、單筆 hundreds of millions、跨多年
- 跟 [[Lumentum]]（LITE）/ [[Coherent]]（COHR）關係：**CIEN 是 pump laser 採購方**
  - HyperRail 把「**幾條光纖共用一個 pump laser**」做成主架構（[[raw 筆記]] 校準正確）
  - Ciena Q2 2026 法說會明確：「continues to work on pump lasers that go into amplifiers and line systems on a daily basis across its supply chain, making investments and putting capacity in place」
  - Ciena 自身 supply chain 緊張、暗示 pump laser 上游也在搶產能 = LITE / COHR 受惠
  - **COHR 法說會反向證實**：Q3 FY2026「secured a multiyear design win with a leading DCI OEM using Coherent's uncooled 3-pin micropump」→ 業界僅 CIEN / Nokia 兩家有「DCI OEM」量級、極大概率指 CIEN 或 Nokia
- 跟 [[NVDA]] 關係：間接受惠
  - NVDA 投資 [[Coherent]] $2B、跟 CIEN **沒直接股權關係**
  - 但 NVDA 蓋 AI factory 必然要把 AI factory 跨 site 連起來 → CIEN HyperRail / Nokia 1830 GX 二選一（或都選）
- 跟 [[AVGO]]、Marvell 關係：賽道不同
  - AVGO / Marvell 是 DC 內 scale out（switching ASIC）
  - CIEN 是 DC 之間 scale across（coherent optical）
  - **彼此 stackable** 而非競爭
- 護城河：
  - **WaveLogic DSP 6 代累積、單載波 1.6T 全球第一**
  - HyperRail co-developed with hyperscaler、design lock-in 5-7 年
  - 純 DCI 玩家、無 mobile network 包袱（vs Nokia 多元、[[Cisco]] 分心）
  - Backlog $7.7B = ~1.2 年營收能見度
- 風險：
  - **客戶集中度極高**（兩家 hyperscaler 占 34%）= 單一客戶削單 / CapEx 縮就重傷
  - **Forward PE 80-91x**（GuruFocus GF Value 估 $79、現價 $500+ = 「overvalued 532%」）= 估值已 price in 多年 ramp
  - **供應跟不上需求** = 短期營收上限被卡（CFO 已坦承 Q1 supply constraint 削減營收）→ 訂單外溢給 Nokia（Leo 原 thesis 校準正確）
  - HyperRail 2027 ramp 延後 → 多年合約遞延入帳
  - hyperscaler 自製 / [[NVDA]]+[[Coherent]] / [[NVDA]]+ 第三方 OLS 整合方案威脅（潛在）
- → 連 [[控制點轉移（投資版）]]：CIEN 拿到「**scale across 物理層唯一純度控制點**」、但 hyperscaler 直接 design partner 風險 = 議價權部分讓渡

## 3. 財務狀態快照（As of 2026-06-04）

| 指標 | 數值 |
|---|---|
| 股價 | $500-627（2026-06-02 至 06-04 區間，波動大）|
| 市值 | 約 $70-90B（估算範圍）|
| Forward PE | **80.60x**（vs Hardware median 25.49 = +216%）/ GuruFocus 報 91.53x |
| GF Value 評估 | $79.47（**現價 532% 高於 fair value**）|
| FY2026 H1 營收（Q1+Q2）| ~$3.0B |
| Q2 FY2026 營收 | **$1.57B**（YoY **+40%**）|
| Q2 FY2026 毛利率 | 44.0% |
| Q2 FY2026 淨利 | $218M |
| Cloud 客戶營收占比（Q2）| **46%**（YoY +70%）|
| Cloud 客戶集中度 | 兩家各 >10%、合計 **34%** 營收（A: $321M、B: $212M）|
| Backlog（Q2 末）| **$7.7B**（QoQ +$600M）= ~1.2 年營收能見度 |
| FY2026 全年指引 | **$6.3B ± $100M**（YoY **+32%**）|
| Q3 FY2026 指引 | ~$1.625B |
| HyperRail 部署時點 | 2026 standardization → **2027 deployment ramp** |
| HyperRail 首單 | 「industry's first multi-rail order」、hundreds of millions、跨多年 |
| 供應狀態 | **Supply constrained**（CFO 法說會明示）|

> ⚠️ **股價 12 個月波動大、估值已 price in HyperRail 2027 ramp + AI scale across 多年合約**。Forward PE 80-91x 是「假設 HyperRail 在 2027-2030 完美交付」的估值。任何 ramp 延後或 hyperscaler CapEx 縮 → 重 de-rating。

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ Cloud 46%（YoY +70%）+ backlog $7.7B + HyperRail 2027 ramp 鎖死 |
| 毛利率 | ✅ Q2 GM 44%、ASP 升級（800G → 1.6T）+ HyperRail 客製化議價權 |
| OpEx | ⚠️ Supply chain 緊張 → 額外採購成本 + R&D 加大（WaveLogic 7 已在路上）|
| 營業利益 | ✅ Q2 淨利 $218M、Re-rate 全速 |

→ **Re-rate 三角形 3/4**——「HyperRail 2027 ramp + AI scale across TAM 重估」是核心 thesis、但 Forward PE 80-91x 已遠超 fair value、estimates 進場時點需用 [[修正三階段]] 框架重檢。

### ✅ 催化

- **HyperRail 2026 standardization 確認 + 2027 deployment ramp**（已拿首單）
- WaveLogic 6 Extreme 1.6T 單載波 ramp（ASP +）
- Backlog 持續成長（Q2 末 $7.7B vs Q1 末 $7B）→ 能見度延長
- 第二家 hyperscaler 跟進採購 HyperRail（目前僅一家拿首單、多家在談）
- Service Provider 段印度市場翻倍、東南亞 / LATAM 跟進
- DCOM（data center out-of-band management）routing+switching ramp +88%
- 供應鏈鬆動 → 解鎖被 supply constraint 卡住的 backlog

### ⚠️ 風險

- **Forward PE 80-91x / GF Value 顯示 532% overvalued**——估值已 price in 多年完美交付、ramp 延後或 hyperscaler CapEx 削就重 de-rating
- **客戶集中度**：兩家 hyperscaler 占 34% 營收 → 單一客戶削單 / 換供應商重傷
- **供應跟不上需求**（CFO 證實）→ 訂單外溢給 [[Nokia]]、CIEN 短期營收上限被卡
- HyperRail 2027 ramp 延後 → 估值重檢
- [[NVDA]] + [[Coherent]] $2B 戰略合作可能孕育「**NVDA 自做或指定 OLS 整合方案**」→ CIEN scale across 控制權削弱
- hyperscaler 內製 / 找 ODM（如 Wistron / Quanta）做 white-box OLS
- Submarine cable 業務地緣風險（中俄、紅海）
- Service Provider 段電信業者 CapEx 縮（5G 進入 maintenance phase）

## ⭐ DCI 賽道 thesis 校準（Leo 原 thesis 對比）

**Leo 原文觀察（2026-06-05 raw 筆記）**：
- CIEN: Hyper Rail 2027 部署、供應跟不上需求
- NOK: Multi-Rail 2026 H2 出貨、訂單外溢承接者
- 「在 DCI 的技術發展上，NOK 沒有落後」
- 「Hyper Rail 跟 Multi-Rail 概念相同、細節有差異」

**實證驗證（2026-06 WebSearch 抓取）**：

| Leo 判斷 | 實證結果 | 校準 |
|---|---|---|
| Hyper Rail 2027 部署 | ✅ **完全正確**——CIEN Q2 FY2026 法說會明示「2026 standardization → 2027 ramp」、industry's first multi-rail order 已收 | high confidence |
| 供應跟不上需求 | ✅ **完全正確**——CFO 明示「supply constrained」、Q1 supply constraint 削減營收、Q2 backlog $7.7B（QoQ +$600M） | high confidence |
| 訂單外溢給 NOK | ✅ **方向正確、可量化**——Nokia Q1 2026 接 hyperscaler 訂單 €1B（YoY +49%）、Optical Networks +20%、明顯承接 CIEN 卡住的需求 | medium confidence（無法 1:1 對應「外溢量」）|
| Hyper Rail vs Multi-Rail「概念同、細節有差異」 | ✅ **完全正確**——兩家都是「multi-fiber-pair 共用 amplifier / pump laser」整合架構、目標都是 hyperscale DCI 密度。CIEN HyperRail = 128 fiber pairs/rack + 32x 密度。Nokia 1830 GX RD66/D2ILA = 160 fiber pairs/rack + 51.2 Tb/s (800G) - 76.4 Tb/s (1.2T) per fiber + C+L band 全整合。**架構哲學完全相同、規格細節 Nokia 略勝（160 vs 128 fiber pairs）**| high confidence |
| 「NOK 沒落後」 | ✅ **正確、甚至樂觀有理**——Nokia 1830 GX RD66 已產品化、D2ILA 整合更完整、Q1 2026 Optical Networks +20% / AI&Cloud +49% / €1B 季訂單 / 9 of top 10 hyperscaler 都用 Nokia 光網。**唯一 timing 差異：CIEN 拿到「首張 multi-rail order」、Nokia 1830 GX 自家路線 2025 已產品上市、看誰拿到第二、三張單。**| high confidence |

**新增校準**：
- **CIEN 純度王、Nokia 廣度王**：CIEN 100% 純光網路、Nokia DCI/Optical 是 Network Infrastructure 一支（整體還有 Mobile Networks 拖累）→ 同樣看好 DCI 賽道時、CIEN 對 thesis 槓桿更高、Nokia 對 thesis 槓桿較低但其他段穩
- **CIEN 估值已 price in、Nokia 估值還沒**：CIEN Fwd PE 80-91x、Nokia Fwd PE 43x（也偏貴但比 CIEN 折價一半）
- **訂單外溢「方向對、量化難」**：兩家都拿到大單、CIEN 供應卡住、Nokia 接得到、但業界沒公布「哪家 hyperscaler 把 CIEN 的單轉給 Nokia」具體案例

## 跟 [[Lumentum]] / [[Coherent]] 採購關係

CIEN HyperRail 把 **pump laser + amplifier** 整合進 sled、是 LITE / COHR 兩家光元件大客戶之一：

| 採購項 | 來源 |
|---|---|
| **EDFA pump laser** | [[Lumentum]] 980nm 主導（5200 series + D2 series）、[[Coherent]] uncooled 3-pin micropump 直接拿 design win |
| **Coherent DSP** | CIEN 自研 WaveLogic 6 Extreme（不外採）|
| **WSS（Wavelength Selective Switch）**| [[Lumentum]] / [[Coherent]] / II-VI 三家寡占 |
| **Coherent receiver / driver IC** | [[Lumentum]] / [[Coherent]] 雙供 |
| **Submarine repeater 整合**| 給海纜段加碼採購 |

**反向驗證**（COHR Q3 FY2026 法說會原話）：
> 「Secured a multiyear design win with a leading DCI OEM using Coherent's uncooled 3-pin micropump」
> 「Secured an exceptionally large purchase order from a market-leading AI datacenter customer for a solution anchored by a new high-power CW laser produced on its 6-inch InP line」

「leading DCI OEM」業界僅 CIEN / Nokia 兩家有量級、「multiyear design win」匹配 CIEN HyperRail 2027 ramp 時程、**極大概率 CIEN 是 COHR 該 micropump 的 design win 客戶**（也可能是 Nokia 或兩家都拿）。

→ **CIEN ramp = LITE/COHR pump laser ramp（量 + ASP 雙引擎）**——Jevons Paradox 確認（pump laser 整合化 → 單元件 ASP +、整體出貨量 + > 整合節省的量）。

→ 連 [[CPO 供應鏈圖譜]] 第七層「電源 / 雷射」：CIEN scale across 把 hyperscale DCI 從「pump laser 散買」轉成「pump laser 整合到 sled、design lock-in」→ [[Lumentum]] / [[Coherent]] 從「賣零件」升級成「**設計合作夥伴 + 多年合約**」。

→ 連 [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：CIEN 是 Hyper Rail 概念**創造者** + 命名者 + 首發部署廠。

## 跟其他 wiki 概念連結

- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：CIEN 是 Hyper Rail 創造者 + 首單拿到方
- [[Jevons Paradox（投資版）]]：pump laser 整合化反而拉高總量（Leo 原 thesis 校準正確）
- [[CPO 供應鏈圖譜]]：CIEN scale across 是 CPO 之外「DC 之間」對應的物理基礎建設（CPO 是 DC 內 chip-to-chip、CIEN 是 DC 之間）
- [[Lumentum]]、[[Coherent]]：pump laser / coherent component 上游供應商、CIEN ramp = 兩家 ramp
- [[半導體基礎建設化]]：scale across 是 AI infra 重估的細項（DCI TAM 從「電信外圍」→「AI infra 必經之路」）
- [[控制點轉移（投資版）]]：CIEN 拿到「scale across 物理層控制點」、但 hyperscaler co-design 風險 = 議價權部分讓渡
- [[NVDA]]：間接受惠（NVDA 蓋 AI factory → CIEN 連 site）、無直接股權
- [[AVGO]]：賽道分工（AVGO 在 DC 內 scale out、CIEN 在 DC 之間 scale across、stackable）
- [[賣水人選股邏輯（投資版）]]：AI scale across **唯一純度玩家**、不押誰 win
- [[市場四階段：懷疑／驗證／共識／反轉]]：DCI 賽道在「驗證 → 共識」加速段、CIEN 是受惠主角但估值已 price in
- [[資訊擴散四階段]]：機構 + 賣方圈正在 price in、media 已開始大規模報導、散戶尚未大舉
- [[五層損益表（營業槓桿）]]：FY2026 +32% YoY、cloud YoY +70%、營業槓桿全開
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 標準三段式

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | 5 | **DCI 純度王**：scale across 唯一純玩家、無 mobile / 多元業務稀釋、hyperscaler AI CapEx 100% 槓桿 |
| 站別關鍵 | 5 | **scale across 物理層絕對龍頭**：industry's first multi-rail order、WaveLogic 6 全球第一、128 fiber pairs/rack 自家規格、2027 ramp 鎖死 |
| 耗材 | 3 | pump laser / WSS / amplifier 外採（[[Lumentum]]/[[Coherent]] 議價）+ 自研 WaveLogic DSP（IP 強但毛利讓渡有限）|
| IP | 5 | **WaveLogic DSP 六代累積**、HyperRail 是 Ciena co-designed-with-hyperscaler 自家規格、design lock-in 5-7 年 |
| 客戶分散 | 1 | **兩家 hyperscaler 占 34% 營收**、cloud 46% / SP 28% / 政府餘下 = 風險集中度 ABF 三雄等級的「[[南電]] 模式」 |

**總分：19/25**

### vs Nokia 對照（同 DCI 賽道）

| 公司 | 五軸總分 | 路線敏感 | 站別關鍵 | 耗材 | IP | 客戶分散 |
|---|---|---|---|---|---|---|
| **Ciena** | **19/25** | **5** | **5** | **3** | **5** | **1** |
| [[Nokia]] | 16/25 | 3 | 4 | 3 | 4 | 2 |

→ **Ciena 在「路線敏感 / 站別關鍵 / IP」三軸壓制 Nokia**：純度王 + 首單拿到 + WaveLogic DSP 自研
→ **Ciena 在「客戶分散」遠輸 Nokia**：兩家 hyperscaler 占 34% vs Nokia 9 of top 10 都用 + 全球 CSP/政府/電信廣布
→ **意義**：CIEN 是「**高槓桿、高估值、高客戶集中度**」三高 entity——對應 thesis 對的時候槓桿大、thesis 翻轉時受傷也大。Nokia 是「廣度王、估值便宜一半、業務多元緩衝」、適合「DCI 賽道對但不確定哪家拿單」的對沖配置。

## 相關連結

- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]
- [[Jevons Paradox（投資版）]]
- [[CPO 供應鏈圖譜]]
- [[Lumentum]]
- [[Coherent]]
- [[Nokia]]
- [[NVDA]]
- [[AVGO]]
- [[半導體基礎建設化]]
- [[控制點轉移（投資版）]]
- [[賣水人選股邏輯（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[資訊擴散四階段]]
- [[五層損益表（營業槓桿）]]
- [[修正三階段]]

## Sources

- [Ciena Q2 FY2026 Earnings Release (SEC 8-K, 2026-06)](https://www.sec.gov/Archives/edgar/data/0000936395/000162828026040614/ex9912026q2earningspressre.htm)
- [Ciena Q2 FY2026 Earnings Presentation (SEC 8-K, 2026-06)](https://www.sec.gov/Archives/edgar/data/0000936395/000162828026040614/ex9922026q2earningsprese.htm)
- [Ciena Q2 FY2026 10-Q (SEC, 2026-06)](https://www.sec.gov/Archives/edgar/data/0000936395/000162828026040767/cien-20260502.htm)
- [Ciena (CIEN) Q1 FY2026 Earnings Call Transcript (Globe and Mail)](https://www.theglobeandmail.com/investing/markets/stocks/CIEN/pressreleases/585966/ciena-cien-q1-2026-earnings-call-transcript/)
- [Ciena Q2 FY2026 Earnings Call Highlights (GuruFocus)](https://www.gurufocus.com/news/8901850/ciena-corp-cien-q2-2026-earnings-call-highlights-record-revenue-growth-and-strategic-wins)
- [Ciena Q2 2026 Earnings Call Transcript (Investing.com)](https://www.investing.com/news/transcripts/earnings-call-transcript-ciena-q2-2026-beats-forecasts-but-stock-dips-93CH-4726909)
- [Ciena reports Q2 2026 revenue of $1.57B, up 40% YoY (Fierce Network)](https://www.fierce-network.com/broadband/ciena-reports-q2-2026-revenue-157b-40-yoy)
- [Ciena (NYSE: CIEN) posts 40% Q2 revenue growth and lifts 2026 outlook (StockTitan)](https://www.stocktitan.net/sec-filings/CIEN/8-k-ciena-corp-reports-material-event-26f71311f5b9.html)
- [Ciena's AI Optical Rail Faces Supply Chain Test as $7 Billion Backlog Ramps (AInvest)](https://www.ainvest.com/news/ciena-ai-optical-rail-faces-supply-chain-test-7-billion-backlog-ramps-2603/)
- [Ciena reports $7B in Q1 2026 order backlog as supply chain constraints persist (Fierce Network)](https://www.fierce-network.com/broadband/ciena-reports-7b-q1-2026-order-backlog-supply-chain-constraints-persist)
- [Ciena Solidifies AI Networking Leadership, Unveils New Innovations (Ciena Newsroom)](https://www.ciena.com/about/newsroom/press-releases/ciena-solidifies-ai-networking-leadership-unveils-new-innovations-for-high-speed-connectivity)
- [What is multi-rail / hyper-rail? (Ciena Insights)](https://www.ciena.com/insights/what-is/what-is-hyper-rail-or-multi-rail)
- [What does DCI really mean today? From scale across to submarine (Ciena Insights, 2026)](https://www.ciena.com/insights/blog/2026/what-does-dci-really-mean-today-from-scale-across-to-submarine)
- [What is scale across? The optical innovations enabling a new AI architecture (Ciena Insights, 2026)](https://www.ciena.com/insights/blog/2026/developing-the-first-tailored-optical-solutions-for-scale-across-ai-applications)
- [Ciena's 6500 Reconfigurable Line System (RLS) Product Page](https://www.ciena.com/products/6500-reconfigurable-line-system)
- [1.6T WaveLogic 6 Extreme MOTR Module (Ciena Data Sheet)](https://www.ciena.com/insights/data-sheets/1-6t-wavelogic-6-extreme-motr-module)
- [Ciena Forward PE 91.53 (GuruFocus, 2026-06-01)](https://www.gurufocus.com/term/forward-pe-ratio/CIEN)
- [Ciena PE Ratio Historical (MacroTrends)](https://www.macrotrends.net/stocks/charts/CIEN/ciena/pe-ratio)
- [Ciena Corp (CIEN) Stock Up 10.1% but GF Value Says Overvalued (GuruFocus)](https://www.gurufocus.com/news/8897058/ciena-corp-cien-stock-up-101-but-gf-value-says-overvalued-gf-score-72100)
- [Coherent Q2 FY2026 Earnings (futurumgroup)](https://futurumgroup.com/insights/coherent-q2-fy-2026-ai-datacenter-demand-lifts-revenue-and-margins/)
- [Coherent Q3 FY2026 Earnings (futurumgroup)](https://futurumgroup.com/insights/coherent-q3-fy-2026-ai-data-center-demand-accelerates-optical-growth/)
- [Lumentum Pump Lasers product page](https://www.lumentum.com/en/products/dci-metro-long-haul-submarine/pump-lasers)
- [Lumentum 980nm EDFA Pump Laser product spec](https://www.lumentum.com/en/optical-communications/products/pump-lasers)
- [NVIDIA Coherent Strategic Partnership announcement (NVIDIA Newsroom, 2026-03)](https://nvidianews.nvidia.com/news/nvidia-and-coherent-announce-strategic-partnership-to-develop-optics-technology-to-scale-next-generation-data-center-architecture)

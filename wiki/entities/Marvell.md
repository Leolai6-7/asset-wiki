---
title: Marvell
aliases: [MRVL, Marvell Technology, Marvell Tech, NASDAQ:MRVL, 美滿電子]
type: entity
created: 2026-06-08
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-12-09
sources:
  - raw/2026-06-08_Leo-AI-infra-CapEx-三階段論-1.6T-光模組-InP.md
  - raw/2026-05-30_FOMOSOC-KP44-Tesla-SpaceX-Marvell-Snowflake-Dell-Anthropic.md
tags: [標的, 美股, ASIC, 光通訊, DSP, CPO, 交換 ASIC, custom silicon, foreign_competitor, NVDA, AMZN, Interconnect 寡占, 光 DSP 60%, KP44 narrative shift, Celestial AI, XConn, Polariton, scale up, scale out, scale across]
confidence: high
---

# Marvell（MRVL）

## 1. 一句話定位

**全球第二大 AI 半導體基礎建設「四路全包」公司**——做 (1) **custom XPU**（為 AWS Trainium 2/3/4、Microsoft Maia、Google 部分 TPU 設計 SoC、AVGO 之外**唯一的 hyperscaler 客製化 ASIC 設計商**）、(2) **PAM4 optical DSP**（**全球 70% 市佔**、Inphi 收購遺產、Ara 3nm 為 1.6T 模組首發）、(3) **Teralynx 交換 ASIC**（T100 2026-06-01 發布、102.4Tbps、3nm、對打 [[AVGO]] Tomahawk 6）、(4) **coherent DSP**（Orion 800ZR、Ciena/Nokia/Cisco 都在自做 → 高端 OEM 自研壓縮空間）；FY2027 Q1 營收 **$2.418B（YoY +28%、創高）**、Data center 占 **76%**、$1.83B（YoY +27%）；FY2027 全年指引營收 **$11.5B（+40%）**、FY2028 **$16.5B（+45%）**；Forward PE **58-66 倍**（vs 半導體中位 34.68 = 高 89%）、市值 **~$230B**；2025-08 收購 [[Celestial AI]]（光互連初創）+ 2026-01 收購 XConn（CXL switch、UALink 對打 NVLink）= 兩個關鍵 M&A 補完 scale-up 光互連 + 開放標準 fabric；但 **DSP 業務有 CPO 整合消失的中長期風險**（CPO 把 DSP 整合進光引擎、外掛 DSP 部分萎縮）。

## 2. 三層 thesis

### 產業層

- AI 半導體基礎建設四條獨立物理路徑都吃（[[市場四階段：懷疑／驗證／共識／反轉]] 在「**驗證 → 共識**」加速段）
  - **Custom XPU**：3 hyperscaler（Amazon / Microsoft / Google）+ Marvell 拿到的 **20+ 新 design wins** 等 FY2028-FY2029 量產
  - **Optical DSP**：800G/1.6T PAM4 70% 市佔、Inphi 領先 1-2 季（Ara 3nm 首發）
  - **Teralynx 交換 ASIC**：T100（102.4Tbps、3nm、purpose-built for AI、512-port、<1000W = vs AVGO 省 25% 功耗）
  - **Coherent DSP**：Orion 800ZR / 500km DCI、Marvell 是 400G→800G 兩代龍頭
- AI 光通訊 + scale-up + custom silicon 三波同時受惠：
  - 1.6T 模組 2025 1.8M → 2026 30M+ units（17x）→ Ara DSP 受惠（Tier 1 多家 design-in）
  - Custom XPU 對抗 [[NVDA]] 通用 GPU = hyperscaler 想自主控制（[[控制點轉移（投資版）]] 邏輯）
  - Teralynx T100 對抗 [[AVGO]] Tomahawk 6 = 102.4Tbps 雙雄賽局正式開打
- **DSP 業務的 CPO 整合風險**：
  - CPO 把光引擎 + DSP 整合進 ASIC 旁邊封裝 → 外掛 PAM4 DSP 模組需求**部分萎縮**（但不是全部消失）
  - 但 CPO 主要打 **scale-up（intra-rack）短距離**、800G/1.6T **scale-out（DC 內 / DCI 跨樓）** 仍需 PAM4 DSP
  - → 風險時程：**~2028 起 NVDA Spectrum-X Photonics 量產後**逐步影響、2026-2027 仍是 PAM4 DSP 黃金期

### 目的層

- **業務 mix**（FY2027 Q1，2026-05-28 法說會）：
  - **Data center = 76% 營收**（$1.83B、YoY +27%）
    - **Custom silicon (XPU)**：FY2026 全年 **$1.5B**、FY2027 預估 +20%+ → **~$1.8-2.0B**
    - **PAM4 optical DSP**：Ara 3nm 1.6T DSP 量產進入 FY2026 下半、Tier 1 多家
    - **Teralynx 交換 ASIC**：T100 量產時點 2027 量產（樣品 mid-2026）
    - **Coherent DSP**：Orion 800ZR 量產中
    - **CXL / UALink switching**（XConn 收購）：FY2028 開始貢獻
  - **Communications & other = 24% 營收**（$585M、YoY +29%）
    - 5G / wireless infra（傳統業務）
    - Carrier、enterprise networking
- **「Custom XPU 第二把交椅」+「Optical DSP 龍頭」雙引擎**：
  - vs [[AVGO]] 全方位：AVGO 70% custom AI ASIC + 80% Ethernet switch ASIC + CPO 模組龍頭、Marvell 是「**對抗者 + 補位者**」
  - vs Lumentum / Coherent：Marvell 在 DSP / ASIC 矽端、不直接做雷射 / 光引擎，是**矽 + 模組的橋樑**
- **客戶結構**（vs [[AVGO]]）：
  - **AWS Trainium 2/3/4** = Marvell 設計（vs AVGO 設計 Google TPU、Meta MTIA）
  - **Microsoft Maia** = Marvell 設計（與 AVGO 並列 design-in）
  - **Google** = 次世代 TPU 部分轉 Marvell（**結束 AVGO 對 Google 的獨佔**）
  - 其他 AI infra：Tier 1 OEM 模組廠（Innolight、新易盛、Coherent、Lumentum、Eoptolink）用 Marvell Ara DSP / Orion DSP
  - 通訊客戶：Ciena、Nokia 既是客戶（買 Orion DSP）也是對手（自研 800ZR DSP）
- 商業模式：
  - **Custom silicon = NRE + per-chip royalty + foundry 中間商**（沒有資產但拿到 design ownership）
  - **DSP / Switch ASIC = 半導體 IP 路徑**（標準產品、毛利高）
- → 連 [[賣水人選股邏輯（投資版）]]：**「Custom silicon 設計賣水人 + DSP IP 賣水人」**
  - 不押 hyperscaler 誰贏（AWS / Microsoft / Google）= Marvell 都受惠
  - 不押光模組 OEM 誰贏（Innolight / Coherent / Lumentum）= Marvell DSP 都裝進去

### 供應層

- 跟 [[AVGO]] 競爭關係：
  - **Custom AI ASIC**：AVGO 70% / Marvell 25%（兩家寡占、Marvell 從 0 拿到 Google TPU 一塊）
  - **Ethernet switch ASIC**：AVGO Tomahawk 80% 市佔、Marvell Teralynx T100 對打中（Marvell 訴求 25% 省電 + AI-native 架構）
  - **CPO**：AVGO 自研光引擎 + 50,000+ CPO 模組已出貨 = AVGO 領先、Marvell 透過 [[Celestial AI]] 收購（光互連 photonic fabric）追趕
- 跟 [[NVDA]] 關係：
  - **NVLink vs UALink**：Marvell 2026-01 收購 XConn（CXL switch 龍頭）切入 UALink scale-up fabric = 開放標準對抗 NVLink 閉門
  - **Marvell 直接是 NVDA 模組鏈賣方**：Ara DSP 進 NVDA 配套光模組
  - **NVDA 透過 Series E 戰略入股 Ayar Labs**（2026-05、跟投人非收購方、據 SEC 8-K）= 光互連 strategic alignment 而非閉門收購、Celestial AI 同類技術仍有獨立 alpha
- 跟 [[CIEN]] / [[Nokia]] 關係：
  - 既是客戶（買 Orion DSP / Ara DSP 做 transceiver）
  - 也是對手（Ciena 自研 WaveLogic DSP、Nokia 自研 PSE-V DSP）
  - → **DCI / coherent 端 Ciena 自研壓縮 Marvell 空間**（中期）
- 跟 [[TSMC]] 關係：
  - 3nm 製程（Teralynx T100 + Ara DSP）depend on TSMC
  - Custom XPU 也走 TSMC CoWoS 先進封裝
- 收購策略（補強 scale-up + 光互連）：
  - **2021 Inphi**（$10B）：PAM4 DSP 70% 市佔來源、定義今天 800G/1.6T 龍頭地位
  - **2021 Innovium**（$1.1B）：Teralynx 交換 ASIC 來源、3 年磨成 T100
  - **2025-08 Celestial AI**：photonic fabric / scale-up 光互連
  - **2026-01 XConn**（$540M）：CXL switch、UALink scale-up
- 護城河：
  - **PAM4 DSP IP**（Inphi 累積、3nm Ara 領先 1-2 季）
  - **Custom silicon design service IP + 客戶綁定**（多年設計流程 lock-in）
  - **20+ FY2028-2029 design wins**（已 booked）
- 風險：
  - **DSP 業務被 CPO 整合的中期消失風險**（2028+）
  - **Teralynx vs AVGO Tomahawk 6 落後 1-2 季**（102.4Tbps tier 起跑線比 AVGO 晚）
  - **Forward PE 58-66 + 12 月 +100%**——估值已 price in 完美執行
  - **3 家客戶 AWS/MSFT/Google 高度集中**——若任一家轉 in-house 或轉 AVGO 影響大
  - 半導體景氣循環（即使 AI 強，傳統 communications 24% 仍受 5G CapEx 影響）
- → 連 [[控制點轉移（投資版）]]：拿到「**PAM4 DSP 控制點 + custom XPU 設計 IP 控制點**」、未拿光引擎 / 雷射 die 控制點（LITE / COHR 拿）

## 3. 財務狀態快照（As of 2026-06-08）

| 指標 | 數值 |
|---|---|
| 股價 | $263.47（2026-06-07） |
| 12 個月漲幅 | **+100%**（2026 YTD） |
| 市值 | **$230B** USD |
| Forward PE | **58.13-65.69**（vs semi 中位 34.68 = 高 68-89%） |
| FY2027 Q1 營收 | **$2.418B**（YoY +28%、創高） |
| FY2027 Q1 Data center 營收 | $1.83B（YoY +27%、占 76%） |
| FY2027 Q1 Communications | $585M（YoY +29%、占 24%） |
| FY2026 全年 custom silicon | **$1.5B**（公司揭露） |
| FY2027 custom silicon 預估 | $1.8-2.0B（+20%+） |
| FY2027 自家指引營收 | **$11.5B（+40%）** |
| FY2028 自家指引營收 | **$16.5B（+45%）**（加速成長）|
| Custom silicon 設計贏單 | **20+ 案 FY2028-2029 量產**（公司揭露） |
| PAM4 optical DSP 市佔 | **70% 全球**（>60% 在 800G+） |
| Teralynx T100 | 2026-06-01 發布、3nm、102.4Tbps、512 port、<1000W |
| Ara DSP | 2026-05 1.6T 量產、3nm、20%+ 省功耗 |
| 主要客戶 | AWS Trainium 2/3/4、Microsoft Maia、Google TPU（部分）|
| 員工 | ~7,500 |
| 專利 | 10,000+ 全球 |

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ Data center 76% / +27%、custom silicon 高黏性、AWS/MSFT/Google 多年設計綁定 |
| 毛利率 | ⚠️ Custom silicon 毛利 vs 標準 DSP / 交換 ASIC 較低、mix shift 對毛利稍壓 |
| OpEx | ⚠️ XConn / Celestial AI 整合 + 3nm Teralynx R&D 重 |
| 營業利益 | ✅ FY2027 +40% / FY2028 +45% 加速成長、營業槓桿開始顯現 |

→ **Re-rate 三角形 2/4**（被「custom silicon 毛利稀釋 + 整合 OpEx」拉低 2 個）——雖然成長很猛，但毛利結構不如 AVGO 健康（AVGO 68% EBITDA margin vs Marvell 較低）。Forward PE 58-66 已 price in 多年完美執行 + DSP 不被 CPO 蠶食的樂觀情境。

### ✅ 催化

- 1.6T 模組需求 17x 增量（2025 1.8M → 2026 30M+ units）= Ara DSP 量產加速
- Teralynx T100 2026-06-01 發布、AWS / Microsoft 多家 hyperscaler 進入 qualification
- 20+ custom silicon design wins FY2028-FY2029 量產（已揭露）
- FY2027 +40% / FY2028 +45% 加速成長指引（不是減速）
- Google TPU 部分轉 Marvell = 結束 AVGO 對 Google 的獨佔（市場心理大撫慰）
- AWS Trainium 3/4 順利 ramp（與 Marvell 設計）
- Microsoft Maia 內部使用率提升 = Maia chips 收入加速
- Celestial AI 整合補完 scale-up 光互連（vs NVDA Series E 戰略入股 Ayar Labs 對倒）
- XConn UALink scale-up switch FY2028 開始貢獻營收
- 半導體基礎建設化（[[半導體基礎建設化]]）= 從週期股轉結構性成長股

### ⚠️ 風險

- **DSP 業務被 CPO 整合消失的中期風險**（時程 ~2028 NVDA Spectrum-X Photonics 全面量產後）
  - 短期 2026-2027 仍是 PAM4 DSP 黃金期
  - 中期 scale-up 內部互連會吃掉外掛 DSP 部分需求
  - 長期 scale-out / DCI 仍需 DSP（不會全部消失）
- **Teralynx T100 落後 AVGO Tomahawk 6 約 1 年**（Tomahawk 6 2025-06 出、T100 2026-06 出）
  - 12-18 個月生態系統落差
  - Marvell 需要在 power efficiency + AI-native 上找差異化
- **Forward PE 58-66 + 12 月 +100%**——估值 price in 多年完美執行 + DSP 不被 CPO 蠶食
- **客戶集中度**：AWS / Microsoft / Google 三家貢獻 custom silicon 大部分
  - 任一家轉 in-house 或轉 AVGO 影響大
- **Ciena / Nokia 自研 coherent DSP**（WaveLogic、PSE-V）= 高端 DCI Orion DSP 中期被擠
- **整合複雜度**（Inphi + Innovium + Celestial AI + XConn 四家整合）
- Communications 24% 受 5G CapEx 影響、傳統 semi 景氣循環
- 半導體景氣風險（即使 AI 強，traditional comm 仍受 mature CapEx 影響）

## ⭐ 對 [[CPO 供應鏈圖譜]] 的意義（第 1 + 第 3 層）

Marvell 在 CPO 圖譜的位置：

- **第 1 層交換 ASIC**：Teralynx T100 = 100Tbps 對打 AVGO Tomahawk 6
  - 兩家寡占成形：AVGO 80% / Marvell 落後 1 年但 AI-native 訴求
  - 市場結構從 AVGO 獨佔 → **AVGO + Marvell 雙寡占**
- **第 3 層 DSP**：Ara 3nm 1.6T DSP / Orion 800ZR coherent DSP = 70% 市佔龍頭
  - **CPO 反向風險最大的玩家**：CPO 整合光引擎 + DSP 進 ASIC → 外掛 DSP 部分需求萎縮
  - 但 scale-out 仍需、DCI 仍需 = 不會全部消失、是「**部分萎縮 + scale-up 端整合消失**」
- **scale-up 光互連**（Celestial AI 收購）：對打 NVDA 收 Ayar Labs

對 [[CPO 供應鏈圖譜]] 的補強：
- 第 1 層更新：「AVGO Tomahawk / Marvell Teralynx **雙寡占**」（不再是 AVGO 獨大）
- 第 3 層更新：Marvell DSP 是 CPO 反向風險最大的玩家、寫進「DSP 被整合消失」風險時程
- 新加：「Marvell scale-up 互連線（Celestial AI 收購）」vs NVDA Ayar Labs 對倒

## ⭐ 對台股 / 美股 AI 半導體基礎建設的意義

對 [[AVGO]]：
- Marvell Teralynx T100 = AVGO 第一個真正對手（Tomahawk 6 之後）= AVGO 80% 市佔有壓力
- Custom AI silicon：AVGO 70% → 可能掉到 50-60%（Marvell 從 Google 切一刀）
- 但 AVGO 毛利 68% EBITDA、Marvell 較低 = AVGO 仍有 quality compounder 優勢

對 [[Lumentum]] / [[Coherent]]：
- 光模組層 + DSP 層相互配套（Marvell DSP 進 LITE / COHR transceiver）
- CPO 後光引擎 + DSP 整合 → Marvell 部分需求被 LITE / COHR 內部吃掉
- 短期合作關係、中期競合關係

對 [[TSMC]]：
- Marvell 3nm Teralynx / Ara DSP / custom XPU 全走 TSMC = TSMC 受惠
- CoWoS 先進封裝多 一個大客戶

對台廠 OEM：
- Marvell custom XPU → AWS / Microsoft 走 ODM 路線 → 鴻海 / 廣達 / 緯穎承接 server
- 不直接影響台廠模組廠（旭創、新易盛）= 反而 Marvell DSP 進台廠模組

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | 4 | 4 路線（custom XPU + DSP + 交換 ASIC + coherent DSP）全包、但 DSP 有中期 CPO 風險 |
| 站別關鍵 | 4 | PAM4 DSP 70% 市佔站別關鍵、custom XPU 設計 IP 拿到、Teralynx 落後 AVGO 1 年 |
| 耗材 | 3 | 半導體 IC = 非耗材性質、但每代 AI server 都換新晶片 = 類耗材 |
| IP | 4 | Inphi PAM4 IP + Innovium Teralynx 架構 + 20+ design wins booked |
| 客戶分散 | 3 | AWS / Microsoft / Google 三家高度集中（vs LITE 只有 NVDA 集中、AVGO 4-5 家） |

**總分：18/25**

### vs [[AVGO]] 五軸對照

| 軸 | AVGO | Marvell | 說明 |
|---|---|---|---|
| 路線敏感 | **5** | 4 | AVGO 5 路線（switch ASIC + custom ASIC + CPO 光引擎 + 雷射 + 軟體 VMware）、Marvell 4 路線 |
| 站別關鍵 | **5** | 4 | AVGO 80% Ethernet ASIC + 70% custom AI、Marvell 70% PAM4 DSP（站別都很強但 AVGO 數字大）|
| 耗材 | 3 | 3 | 半導體 IC 性質、打平 |
| IP | 4 | 4 | 打平、AVGO Tomahawk 領先 1 年、Marvell Inphi DSP 領先 |
| 客戶分散 | **4** | 3 | AVGO 4-5 家客戶（Google + Meta + Apple + AWS + Microsoft）、Marvell 3 家集中 |
| **總分** | **21/25** | **18/25** | AVGO 全方位領先 3 分 |

→ **Marvell vs AVGO 共存 + Marvell 為對抗者第二位**：
- AVGO 21/25 = ASIC 全場最強（兩種 ASIC 都領先）
- Marvell 18/25 = DSP 全場最強 + custom XPU 第二位
- 不是「Marvell 取代 AVGO」、是「Marvell 從 AVGO 切一刀 + 雙寡占成形」
- Leo 隱含「兩家共存、AVGO 仍是 quality compounder」**完全成立**

## ⭐ DSP 被整合消失的風險時程（重要）

```
2026-2027：黃金期（PAM4 DSP 量產加速、Forward PE 高估值能維持）
    │
2028：第一波 CPO 量產（NVDA Spectrum-X Photonics 全面量產）
    │
2028-2029：scale-up 端外掛 DSP 部分萎縮（10-20% 需求消失）
    │
2030+：scale-out / DCI 仍需 DSP（不會全部消失）
```

**校準 Leo 原 thesis**：
- 「Marvell DSP 業務可能被整合消失」**部分成立**：
  - **scale-up 端確實會萎縮**（CPO 整合光引擎 + DSP 進 ASIC）
  - **scale-out 端不會消失**（800G/1.6T 模組仍需 PAM4 DSP）
  - **DCI 端 Coherent DSP** 不受 CPO 影響（跨樓 / 跨 DC 距離仍需 coherent）
- → 估計 **DSP 業務中期（2028-2030）損失 20-30% TAM**、非全部消失
- → Marvell 護城河需要靠 custom XPU + Teralynx 補位

## 跟其他 wiki 概念連結

- [[CPO 供應鏈圖譜]]：第 1 層（Teralynx ASIC）+ 第 3 層（DSP）雙位置、CPO 反向風險最大的玩家
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：Marvell Orion 800ZR DSP 進 Ciena / Nokia 模組
- [[Jevons Paradox（投資版）]]：DSP 雖被 CPO 整合風險、但總模組量爆增反向放大 Marvell DSP 總用量
- [[賣水人選股邏輯（投資版）]]：custom silicon + DSP 雙賣水人路徑（不押 hyperscaler 誰贏）
- [[半導體基礎建設化]]：四路線都是 AI infra 物理瓶頸
- [[控制點轉移（投資版）]]：拿到 PAM4 DSP + custom XPU 設計 IP 控制點
- [[市場四階段：懷疑／驗證／共識／反轉]]：在「驗證 → 共識」加速段
- [[資訊擴散四階段]]：12 個月 +100% 已過散戶看到階段、進入共識段
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 強制格式
- [[AVGO]]：直接競爭對手（Tomahawk vs Teralynx、custom AI ASIC 70% vs 25%）
- [[NVDA]]：Ara DSP 進 NVDA 配套光模組、NVLink vs UALink（XConn）競爭
- [[Lumentum]] / [[Coherent]]：光模組層配套（Marvell DSP 進 LITE / COHR transceiver）= 短期合作中期競合
- [[Ciena]]：Orion DSP 客戶 + WaveLogic 自研 DSP 對手雙重關係
- [[Nokia]]：類似 Ciena 雙重關係（買 Orion 也自研 PSE-V）
- [[TSMC]]：3nm + CoWoS 先進封裝大客戶
- [[SiTime]]：CPO 三倍 BOM timing 與 Marvell Teralynx / DSP 雙協同

## 相關連結

- [[CPO 供應鏈圖譜]]
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]
- [[賣水人選股邏輯（投資版）]]
- [[半導體基礎建設化]]
- [[控制點轉移（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[AVGO]]、[[NVDA]]、[[Lumentum]]、[[Coherent]]、[[TSMC]]
- [[Ciena]]、[[Nokia]]、[[SiTime]]

## ⚠️ 2026-06-09 校準

**訛傳修正**：原文（建檔 2026-06-08）誤寫「NVDA 收購 Ayar Labs（2026-05、$6.5B）」。**SEC 8-K 確認 NVDA 是 Ayar Labs 的 Series E 跟投人，不是收購方**——是策略性入股而非併購。

影響：
- Ayar Labs **仍為獨立公司**（未閉門）= [[POET Technologies]]、[[Celestial AI]] 邊緣化壓力**沒有想像中強**
- NVDA Ayar Labs 戰略 alignment ≠ 把光互連技術全閉門 = 開放矽光初創仍有獨立空間
- Marvell 收購 [[Celestial AI]] 的 strategic value **不下修**（自家 scale-up 互連配置不受影響）
- 「NVDA 把光互連封閉化」這個論述應改為「NVDA 加強光互連戰略 alignment」

連動修正項：
- 2 (供應層 — NVDA 關係段) 已改寫為 Series E 戰略入股
- 催化清單已改 Celestial AI 對照敘述

## Sources

- [Marvell Q1 FY 2027 Raises Full-Year Outlook on AI Data Center Demand (Futurum, 2026-05)](https://futurumgroup.com/insights/marvell-q1-fy-2027-raises-full-year-outlook-on-ai-data-center-demand/)
- [Marvell Technology Q1 FY2027 8-K (SEC)](https://www.sec.gov/Archives/edgar/data/0001835632/000183563226000014/q127_8kx522026ex-991.htm)
- [Marvell Launches Teralynx T100, 102.4 Tbps AI Switch on 3nm (mlq.ai 2026-06)](https://mlq.ai/news/marvell-launches-teralynx-t100-a-1024-tbps-ai-switch-silicon-on-3nm/)
- [Marvell Teralynx T100 Explained: 102.4 Tbps AI Switch (nerdyinfo 2026)](https://nerdyinfo.com/marvell-teralynx-t100/)
- [Broadcom vs Marvell: Custom AI Silicon Battle 2026 (heygotrade)](https://www.heygotrade.com/en/blog/broadcom-vs-marvell-custom-ai-silicon-battle-2026/)
- [Better Semiconductor Stock: Broadcom vs Marvell (Motley Fool 2026-03)](https://www.fool.com/investing/2026/03/21/better-semiconductor-stock-broadcom-vs-marvell-tec/)
- [Marvell Ushers in the 1.6T Era with Expanded Optical DSP Platform (StorageNewsletter 2026-04)](https://www.storagenewsletter.com/2026/04/03/marvell-ushers-in-the-1-6t-era-with-expanded-optical-dsp-platform-portfolio-redefining-ai-data-center-end-to-end-connectivity/)
- [AI Optical Interconnect Landscape 2026: Marvell, Broadcom, Credo, Lumentum (bepresearch Substack)](https://bepresearch.substack.com/p/the-quiet-architect)
- [Copper Wall, Age of Light — Dissecting Marvell's FY2026 & 1.6T Optics Chain (photoncap)](https://photoncap.net/p/copper-wall-age-of-light-dissecting)
- [Marvell's Custom XPU Pipeline Is A Declaration Of AI Independence (Next Platform 2025-09)](https://www.nextplatform.com/2025/09/03/marvells-custom-xpu-pipeline-is-a-declaration-of-ai-independence/)
- [Marvell Technology's AI Strategy: Dominance in Data Infrastructure AI (Klover.ai)](https://www.klover.ai/marvell-technology-ai-strategy-analysis-of-dominance-in-data-infrastructure-ai/)
- [Marvell Optical DSPs | Powering the Future of AI Infrastructure (Marvell)](https://www.marvell.com/solutions/data-center/optical-dsp.html)
- [Marvell, Lumentum and Coherent Demonstrate Industry's First 800G ZR/ZR+ Pluggable Modules (Marvell Newsroom)](https://www.marvell.com/company/newsroom/marvell-800g-zr-zrplus-pluggable-modules-for-500km-data-center-interconnects.html)
- [Marvell to Acquire Innovium (PRNewswire 2021)](https://www.prnewswire.com/news-releases/marvell-to-acquire-innovium---accelerates-cloud-growth-with-expanded-ethernet-switching-portfolio-301346705.html)
- [MARVELL TECHNOLOGY Forward PE Ratio: 65.69 (GuruFocus 2026-06)](https://www.gurufocus.com/term/forward-pe-ratio/MRVL)
- [Marvell Technology (MRVL) Statistics & Valuation (Stockanalysis)](https://stockanalysis.com/stocks/mrvl/statistics/)
- [Tracking the Coherent DSP Supply Chain 2026 (Cignal AI)](https://cignal.ai/2026/04/tracking-the-coherent-dsp-supply-chain-2026/)
- [FinancialContent — Marvell Technology (MRVL): The AI Interconnect King Faces a March 2026 Turning Point](https://markets.financialcontent.com/stocks/article/finterra-2026-3-5-marvell-technology-mrvl-the-ai-interconnect-king-faces-a-march-2026-turning-point)
- [Marvell Technology Stock Surge: $2.2B Revenue and AI Chip Boom 2026 (tech-insider.org)](https://tech-insider.org/marvell-technology-stock-surge-custom-ai-chip-2026/)

---
title: SK Hynix
aliases: [SK Hynix, SK hynix, SK 海力士, 000660.KS, KRX:000660, KOSE:A000660, 하이닉스, SKHX]
type: entity
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2026-12-08
expires_on: 2027-06-08
sources:
  - raw/2026-06-08_Leo-黃仁勳定調記憶體結構性短缺-SK-Hynix-合約.md
tags: [標的, 韓國, 記憶體, HBM, DRAM, foreign_competitor, NVDA 合約, AI infra, 結構性短缺]
confidence: high
---

# SK Hynix（KRX: 000660 / 韓國交易所）

## 1. 一句話定位

**HBM 全球絕對龍頭（市佔 50-62%）+ NVDA 多年合約綁定 anchor**——2026-06-08 與 [[NVDA]] 正式簽署 **multi-year technology partnership**，不只是 HBM 供應，而是綁定 NVIDIA **未來幾乎全部 AI 路線圖的記憶體供應**：Vera Rubin AI 超級電腦（HBM4 + LPDDR5X + 3D NAND）+ Vera CPU（LPDDR5X）+ RTX Spark AI PC（LPDDR5X + 3D NAND）+ Jetson Thor 機器人平台（LPDDR5X + 3D NAND）。MR-MUF 製程護城河 + HBM4 領先 2-3 季 + Q1 2026 營收 KRW 52.6T / OP margin **72%** / YoY +198% → 已具備 [[半導體基礎建設化]] 的「AI infra 等級」估值資格，但 KOSPI 仍以景氣循環 PE 折價（Forward PE **5.9-6.4x** vs Micron 7.8-9x），是 [[HBM iPhone moment]] thesis 的核心 anchor。

## 2. 三層 thesis

### 產業層

- **HBM TAM 結構性放量、不是景氣**：
  - HBM 消耗的晶圓產能是一般 DDR5 的 **3 倍**（每 GB）
  - SK Hynix 已將 ~30% DRAM 產能轉去做 HBM、2027 將近 40%
  - → HBM 擴產 = 直接擠壓 conventional DRAM 供給 → 雙重結構性短缺（HBM + 一般 DRAM）
  - Macquarie：2027 年 HBM 合約價可能漲 **>50%**
  - SK 集團主席 Chey Tae-won：「記憶體短缺持續到 2030」
- 賽道位置：[[市場四階段：懷疑／驗證／共識／反轉]] = **「驗證 → 共識」過渡期**
  - 驗證已強烈：NVDA 多年合約、Hyperscaler 預付到 2028、客戶提議買 EUV 機器並出資建廠
  - 共識未完成：KOSPI 仍給景氣股 PE 6x、市場仍用「[[PB 估值法（記憶體週期）]]」框架定價
- [[資訊擴散四階段]] = **階段 3（媒體擴散）**——2026-06-08 韓股熔斷 + KOSPI 8.29% 暴跌 = 機構/賣方/媒體三階段擴散完成但散戶恐慌進場、典型 [[散戶 vs 機構買股差異]]
- TAM：HBM 將佔 DRAM 總營收 ~40%（vs 2024 ~20%），TAM CAGR 40%+（2026-2030）

### 目的層

- **三軌記憶體一體化平台**：
  - **HBM**（AI infra 引擎）：50-62% 全球市佔、NVDA 兩家最大供應商之首、Q2 2025 高峰 62%、Q3 2025 53%
  - **DRAM 主體**（含 HBM）：2025 Q1 短暫超越 [[Samsung Electronics]] 成全球 #1（36% vs Samsung），Q4 2025 Samsung 收復（38.5% vs SK 28.8%）
  - **NAND**（補位現金流）：Solidigm（2021 收購自 Intel）+ 自有 NAND，2025 NAND 全球 #2
- 真實角色：**NVDA 的「優先存取記憶體供應商」+ AI infra 鏈被綁定最深的記憶體廠**
  - NVDA HBM4 訂單分配：**SK Hynix ~70% / Samsung 25-30% / Micron 5-10%**（2026 UBS / TrendForce 估計）
  - 同時拿 LPDDR5X（Vera CPU + RTX Spark + Jetson Thor）+ 3D NAND 多軌
  - 2026-06-08 NVDA-SK Hynix 公告同步揭露 NVDA 把 **CUDA-X / Omniverse / cuOpt** 注入 SK Hynix fab → 雙向技術綁定
- 商業模式核心：**「跟客戶共同設計 + 多年合約鎖供給 + 規模 + 製程 know-how」四重綁定**——客戶換不動
- [[控制點轉移（投資版）]]：拿到「AI 推理 / 訓練的記憶體控制點」+「NVDA 路線圖內嵌記憶體規格定義權」

### 供應層

- **不是賣水人、是 AI infra 的「記憶體核心節點」**——是 [[賣水人選股邏輯（投資版）]] 的進階版：賣的不是水，是「水 + 共設管線 + 多年合約」三合一
- **護城河四層**：
  - **製程護城河**：**MR-MUF（Mass Reflow Molded Underfill）** 比 Samsung/Micron 的 TC-NCF 良率高 **~20%**、熱管理 dummy bumps 多 **4 倍**、Advanced MR-MUF 熱散逸進化 1.6x
  - **HBM 量產時程護城河**：HBM3E 全球首批量產（2024）+ HBM4 全球首發 16-layer 48GB / 2 TB/s 量產 2026 Q3 + HBM4E sample 2026 H2 / 量產 2027
  - **客戶 lock-in**：NVDA 多年合約（H/B 系列 → Rubin → Feynman 全綁定）+ Google TPU + AMD MI400 = AI ASIC 鏈最廣
  - **規模 + CapEx 護城河**：Cheongju M15X（HBM4 主力、2026 H2 ramp 至 40k wafer/月）+ Yongin 韓國史上最大 fab cluster（KRW 120T 投資、2027 H1 啟動）+ Indiana 西拉法葉廠（USD 3.87B、2028 啟動、美國首條 HBM 後段封裝線）
- 對 [[Samsung Electronics]] 領先程度：**HBM 2-3 季、製程 1 代**（Samsung 2026-02 才量產 HBM4、SK Hynix 2024 已開始 HBM3E）
- 對 [[Micron]] 領先程度：**規模 5x+、HBM4 16-Hi 領先 1-2 季**（但 Micron 在 NVDA Vera CPU LPDDR5X 切走部分份額）
- 跟 [[Amkor]] 關係：**間接、不是直接合作方**——Amkor 是 TSMC CoWoS 後段封裝商、SK Hynix 跟 [[TSMC]] 自己合作 CoWoS-2（HBM4 base die 用 TSMC 邏輯製程），美國端 SK Hynix 自建 Indiana 廠不依賴 Amkor

## 3. 財務狀態快照（As of 2026-06-08）

| 指標 | 數值 |
|---|---|
| 股價 | **KRW 1,911,000**（2026-06-08 收盤、-7.68% 當日，KOSPI 熔斷後） |
| 52 週區間 | KRW ~530,000 – 2,407,000（**52 週 +260%+**） |
| 市值 | **KRW 1,361.97 兆**（約 USD 1.0T、剛跨 $1 兆估值門檻）|
| Trailing PE | **18-19.6**（Yahoo/stockanalysis） |
| **Forward PE** | **5.9-6.4x** ⭐（**vs Micron 7.8-9x = SK Hynix 折價 25-30%**，Korea Discount）|
| 賣方目標價（平均） | KRW 2,076,603（+8.7% upside） |
| 賣方目標價（fair value upgrade） | KRW 2,264,946 → 3,326,818（+19% → +74%） |
| Consensus rating | **Strong Buy** |
| 2025 全年營收 | ~KRW 78T（YoY +60%） |
| **Q1 2026 營收** | **KRW 52.58T**（QoQ +60%、**YoY +198%**、史上首破 50T） |
| **Q1 2026 OP** | **KRW 37.61T**（OP margin **72%**、QoQ +96%、YoY +500%+） |
| Q1 2026 淨利 | KRW 40.35T（淨利率 77%）|
| Q1 2026 DRAM ASP | **+mid 60% QoQ** |
| Q1 2026 NAND ASP | +mid 70% QoQ（NAND 出貨 -10% 但 ASP 漲贏） |
| HBM4 量產時程 | **2026 Q3** ramp 至 15k wafer/月 by 年底 |
| HBM4E sample | 2026 H2，量產 2027 |
| DRAM wafer 入料 | 2026 H2 推進至 600k+/月 |
| CapEx | 2026 KRW ~30T+（M15X + Yongin + Indiana 並進）|

### Re-rate 三角形（As of 2026-06-08）

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅✅ Q1 YoY +198% / 史上首破 50T / NVDA 多年合約 anchor / HBM 訂單能見度到 2028 = **歷史最強 inflection** |
| 毛利率 / OP margin | ✅✅ Q1 OP margin **72%** / 淨利率 77% = AI infra 等級獲利力（TSMC 50% / Lumentum 45% 都望塵莫及）|
| OpEx | ✅ M15X + Yongin + Indiana 三廠並進 CapEx ~KRW 30T/yr，但 OP 跑得更快 |
| 營業利益 | ✅✅ Q1 OP +500% YoY、72% margin = Re-rate 完整 |

→ **Re-rate 三角形 4/4 滿**——但 Forward PE 仍 5.9-6.4x、市場仍用景氣股框架定價 = **典型 [[PB 估值法（記憶體週期）]] vs [[HBM iPhone moment]] 二選一的 Re-rate 期權**。

### ✅ 催化

- **2026-06-08 NVDA multi-year partnership 簽訂**：covers HBM4 + LPDDR5X + 3D NAND across Vera Rubin / Vera CPU / RTX Spark / Jetson Thor 四產品線
  - `as_of: 2026-06-08, expires_on: 不適用（多年合約結構性 catalyst）`
- **HBM4 全球首發量產 2026 Q3**：16-Hi、48GB、2 TB/s、NVDA Rubin 70% 訂單
  - `as_of: 2026-06-08, check_after: 2026-12-08, expires_on: 2026-12-31`
- **Cheongju M15X 2026 H2 ramp**：HBM4 主力產線、40k wafer/月 → 2027 80k
  - `as_of: 2026-06-08, check_after: 2026-12-08`
- **Yongin Cluster 2027 H1 啟動**：第一座 fab 6 cleanroom、每 6 個月加 60k wafer、最終 360k/月、總投資 KRW 120T
  - `as_of: 2026-06-08, check_after: 2027-06-08`
- **Indiana 西拉法葉廠 2028 啟動**：USD 3.87B、美國首條 HBM 後段封裝、CHIPS Act 受惠
  - `as_of: 2026-06-08, check_after: 2027-12-08`
- **HBM4E 量產 2027**：第 7 代、2026 H2 樣品
- **客戶提議買 EUV 機器 + 出資建廠**：產業內部訊號 = 供給結構性短缺到 2028+
- **Hyperscaler 5 年 LTA**：Macquarie 解讀 = 客戶不期望 2028 前緩解
- 2025 Q1 短暫超越 Samsung 成全球 DRAM #1（30 年來首次）= 結構性遞延信任

### ⚠️ 風險

- **2026-06-08 KOSPI 熔斷**：-8.29% 至 7,484、SK Hynix 當日 -7.68%、Samsung -10.18%
  - 觸發原因：Broadcom AI 晶片 guidance miss + 聯準會升息恐慌（5 月 NFP 過熱）+ 伊朗對以色列導彈衝突
  - 短期：散戶恐慌進場 / 機構靜觀（典型 [[資訊擴散四階段]] 階段 3-4）
  - 長期：thesis 不變、估值反而便宜（Forward PE 5.9x 已歷史低點區間）
- **Samsung HBM4 追趕**：2026-02 量產 HBM4、UBS 預期 NVDA 訂單 SK Hynix 70% → Samsung 在 16-Hi 早交付若良率穩定可能切走份額
- **Micron LPDDR5X 切位**：NVDA 把 Vera Rubin 部分 LPDDR5X 配給 Micron（多供應商策略）
- **2025 Q4 Samsung 收復 DRAM #1**：38.5% vs SK 28.8%（Samsung 大廠規模 + 漲價週期 beta）
- **HBM 良率追趕**：Samsung 已過 NVDA HBM3E 認證（2025 Q4 + 2026-02）= 雙頭格局確認、SK Hynix 不再獨佔
- **Korea Discount**：散戶主導、公司治理透明度差、地緣風險 → Forward PE 結構性比 Micron 折價 25-30%
- **景氣循環論派持續用 [[PB 估值法（記憶體週期）]] 唱空**：歷史每次「這次不一樣」幾乎都被證偽
- **TSV / Hybrid Bonding 製程顛覆**：2027+ Hybrid Bonding 若被 Samsung/Micron 先掌握 → MR-MUF 護城河被繞過
- **Indiana 廠 CHIPS Act 補助延遲**：Tom's Hardware 報 NIMBY + 2 年許可、每日 $5M 延遲成本（與 Amkor、Micron 共同曝險）

## ⭐ NVDA 多年合約細節（2026-06-08 公告）

| 產品線 | 記憶體規格 | 量產時程 | SK Hynix 角色 |
|---|---|---|---|
| **Vera Rubin AI 超級電腦** | **HBM4 + LPDDR5X + 3D NAND**（R100 GPU 288GB HBM4 @ 22 TB/s、2.75x Blackwell）| 2026 Q3 ramp / **2027 H1 platform launch** | **HBM4 ~70% 訂單**、與 Samsung 25-30% / Micron 5-10% 共 supply |
| **Vera CPU** | **LPDDR5X**（1.5TB capacity @ 1.2 TB/s、<30W、~2x DDR5）| 2027 H1 launch | **SOCAMM2 192GB LPDDR5X 模組已量產**（NVDA 公告 SK Hynix 為主供）|
| **RTX Spark AI PC** | **LPDDR5X + 3D NAND**（128GB 統一記憶體 @ 300 GB/s）| 已上市（搭 Grace CPU + Blackwell GPU）| LPDDR5X + 3D NAND 主供 |
| **Jetson Thor 機器人** | **LPDDR5X + 3D NAND**（128GB @ 273 GB/s、256-bit bus、4266 MHz）| 已上市 / 2025 Q4 量產 | LPDDR5X + 3D NAND 主供 |

**合約結構特殊性**（vs 一般供應合約）：
1. **不是純採購、是 co-development**——NVDA 把 CUDA-X / PhysicsNeMo / Omniverse / cuOpt 注入 SK Hynix fab，做 autonomous fab + 半導體模擬加速
2. **不只 HBM、是「全記憶體棧」**——HBM + LPDDR5X + 3D NAND 三軌全綁
3. **時程跨多年、不限 Rubin**——Rubin Ultra（2028）/ Feynman（2029）路線圖內嵌
4. **金額未揭露、Volume 未揭露**——但 NVDA 公告用詞「priority access for years, not quarters」= 結構性綁定
5. **Samsung 同日（2026-06-08）也與 NVDA 召開類似會議**——SK Hynix 仍是 primary anchor

## ⭐ 對 [[PB 估值法（記憶體週期）]] thesis 的挑戰

| 維度 | PB 派（景氣循環論） | SK Hynix 案（結構性短缺論） |
|---|---|---|
| 框架 | 記憶體仍是週期商品、看 PB 守底 | HBM 已是 AI infra 元件、看現金流 + 客戶綁定 |
| LTA 解讀 | LTA 鎖供給不鎖價、價格仍跟現貨走 | NVDA 多年合約 + co-development = 結構性鎖綁 |
| 三巨頭分散 | 競爭最終會把 margin 打回 ROIC | MR-MUF 護城河 + Samsung 落後 2-3 季 = 結構性領先 |
| 預付訂單訊號 | 通常出現在週期中段、後段供給追上反轉 | Hyperscaler 預付到 2028 + 客戶出資建廠 = 供需失衡規模史無前例 |
| 估值方法 | PB 1.5-3x 區間 | Forward PE 6.4x 仍嚴重低估、應 re-rate 至 15-25x infra 等級 |
| 歷史對照 | 2017 資料中心超級週期最終供給追上 | 但 HBM 三倍 wafer 消耗 + 先進封裝 + EUV 缺貨 = 物理性追不上 |

→ **混合估值法（hybrid valuation）**：
- 一般 DRAM 部分（~40% 營收）：仍按 [[PB 估值法（記憶體週期）]]
- HBM + AI infra 部分（~60% 營收）：應按 [[Forward PE 估值法]] 給 infra 級倍數
- **加權公平 PE：~10-15x**（vs 當下 6.4x = 50-130% upside）
- 不是「PB 派錯」、是「PB 派只算對了一半」

## ⭐ 韓股熔斷 2026-06-08 含義

| 時間軸 | 事件 |
|---|---|
| 2026-06-05 | 韓交所活化 sell-side sidecar（KOSPI200 期貨 -6.26% 觸發、KOSPI 中午 -5.1%）|
| 2026-06-08 09:03:42 | **KOSPI 開盤 3 分 42 秒觸發 Level 1 circuit breaker**（-8.40% 至 7,474）|
| 2026-06-08 收盤 | KOSPI -8.29% 至 7,484.41（**史上第 9 次**熔斷）|
| 2026-06-08 SK Hynix | -7.68% 收 KRW 1,911,000（盤中曾 -10%）|
| 2026-06-08 Samsung Electronics | -10.18% 收 KRW 295,500 |
| 同日 | NVDA + SK Hynix + LG + Naver 在韓宣布 AI 合作 |

**三角觸發因素**：
1. Broadcom AI 晶片 guidance miss → AI 鏈 derisking
2. 5 月美國 NFP 數據過熱 → Fed 升息恐慌
3. 伊朗對以色列導彈攻擊 → 中東衝突 risk-off

**對 SK Hynix 估值影響**：
- **短期（1-3 月）**：散戶恐慌進場 / [[資訊擴散四階段]] 階段 3-4 警訊 → 波動加劇、但相對 NVDA 路線圖結構性綁定的 thesis 不變
- **中期（6-12 月）**：HBM4 量產 + Q3 2026 財報 + NVDA Rubin platform launch → 機構/賣方目標價 KRW 2.07M → 3.33M（+8% → +74%）
- **長期（2027-2030）**：Yongin + Indiana 雙廠 + HBM4E + NVDA Feynman 路線圖綁定 → infra 等級估值 re-rate

**[[散戶 vs 機構買股差異]] 視角**：
- 散戶：恐慌賣出（已上漲 +260% → 「停利避險」）
- 機構：靜觀後加倉（Macquarie 上調目標價 / 預期 2027 HBM 合約價漲 >50%）
- **典型「散戶在後段恐慌、機構在後段加碼」格局**

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| **賽道** | **5/5** | HBM 是 AI infra 最稀缺元件、結構性短缺到 2028-2030 |
| **路線** | **5/5** | MR-MUF + HBM4 16-Hi + Hybrid Bonding 12-Hi 驗證 + LPDDR5X + 3D NAND 多軌（製程護城河寬厚）|
| **IP / 站別** | **5/5** | HBM3E/HBM4 全球首發、NVDA 共同設計、TSMC CoWoS-2 戰略合作（製程定義者位階）|
| **客戶分散** | **3/5** | NVDA 集中度高（HBM ~50%+）、但同時供應 Google TPU + AMD MI400 + 全 hyperscaler，比 Lumentum 純度高、比 Murata 集中（NVDA 是頭部）|
| **時點 / 估值** | **5/5** | Forward PE 6.4x = 同業（Micron 9x）顯著折價、Re-rate 三角形 4/4、Korea Discount 提供安全邊際、KOSPI 熔斷後估值更低 |

**總分 23/25**——與 [[村田 Murata]]（24/25）、[[Lumentum]]（19/25）、[[IBIDEN]]（19/25）對照，是 asset-wiki 中分數最高的標的之一。**唯一扣分在客戶集中度**（NVDA 議價力 + Samsung 雙供應策略 risk），但 NVDA 路線圖綁定深度補回 1 分。

## 跟其他 wiki 概念連結

- [[AI 記憶體結構性供給短缺]]：**本 entity 是這個 concept 的最大 anchor**（2026-06-08 黃仁勳定調事件的主角）
- [[HBM iPhone moment]]：**核心 anchor**——SK Hynix 是這個 thesis 的最大 beneficiary、2026-06-08 NVDA 合約驗證 thesis
- [[PB 估值法（記憶體週期）]]：**正面挑戰**——SK Hynix Q1 OP margin 72% / Forward PE 6.4x 的張力，是 PB 派 vs HBM iPhone moment 派的決勝點
- [[半導體基礎建設化]]：HBM 從週期商品變 AI infra 元件、是 [[TSMC]] 模式的記憶體版本
- [[賣水人選股邏輯（投資版）]]：SK Hynix 是「進階版賣水人」——不只賣水、賣「水 + 共設管線 + 多年合約」三合一
- [[控制點轉移（投資版）]]：拿到「AI 推理/訓練的記憶體控制點」+「NVDA 路線圖內嵌規格定義權」
- [[資訊擴散四階段]]：2026-06-08 韓股熔斷 = 散戶在階段 3-4 恐慌、機構繼續加倉
- [[散戶 vs 機構買股差異]]：KOSPI 熔斷後散戶停利 vs 機構等回檔加倉
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 遵循此模板
- [[時效 metadata schema（lint 規範）]]：本 entity 套用完整時效 metadata（as_of / check_after / expires_on）

## 跟其他 wiki entity 連結

- [[NVDA]]：核心客戶 + 戰略合作方、2026-06-08 multi-year partnership anchor
- [[TSMC]]：HBM4 base die 製程合作 + CoWoS-2 整合（協力關係）
- [[Samsung Electronics]]（待建）：HBM 二供 + DRAM 主競爭、2025 Q4 收復 DRAM #1
- [[Micron]]：HBM 三供（美國本土）、Forward PE 8.45 vs SK 6.4x 對照（美股 vs Korea Discount）；NVDA Vera CPU LPDDR5X / SOCAMM2 首發認證方；CHIPS Act USD 6.4B anchor
- [[Samsung Electro-Mechanics]]：Samsung 集團子（不同公司）、跑 ABF + 玻璃基板賽道（不直接競爭）
- [[Powertech 力成]]：台廠 HBM 後段封裝（Micron 獨家）= 跟 SK Hynix 間接競爭（透過 Micron）
- [[Amkor]]：間接關係，TSMC CoWoS 後段封裝商；SK Hynix Indiana 廠自建不依賴
- [[Intel]]：曾收購 Intel NAND（2021 Solidigm）= 集團整合受惠 / 但 Intel 自建 EMIB 不依賴 SK
- [[Absolics]]：韓國同陣營但跑玻璃基板賽道（SKC 子）= SK 集團其他軌道
- [[AVGO]] / [[Google]]：客戶端 ASIC（custom AI accelerator）對 HBM 需求

## 跟 [[宋分（美股送分題）]] framework 對照

宋分備忘錄 #2 提出 [[HBM iPhone moment]]、Note #07 提出 [[PB 估值法（記憶體週期）]]——兩個 framework 同源、但在 SK Hynix 身上首次撞出 **「混合估值」需求**。Leo 2026-06-08 觀察黃仁勳定調 = 宋分備忘錄 #2 兩年後的 anchor 驗證。

## 相關連結

- [[NVDA]]
- [[Micron]]
- [[AI 記憶體結構性供給短缺]]
- [[HBM iPhone moment]]
- [[PB 估值法（記憶體週期）]]
- [[半導體基礎建設化]]
- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[資訊擴散四階段]]
- [[散戶 vs 機構買股差異]]
- [[TSMC]]
- [[Amkor]]
- [[CoWoS 三傑差異化]]
- [[Samsung Electro-Mechanics]]
- [[Powertech 力成]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[時效 metadata schema（lint 規範）]]
- [[宋分（美股送分題）]]
- [[宋分備忘錄 #2 — HBM iPhone Moment-Meta-軟體 PE]]

## Source URLs

- NVIDIA + SK Hynix multi-year partnership 公告（NVIDIA Newsroom）: https://nvidianews.nvidia.com/news/sk-hynix-ai-factory
- NVIDIA Investor Relations 公告: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-SK-hynix-Announce-Multiyear-Technology-Partnership-to-Advance-Memory-for-AI-Factories/default.aspx
- SK Hynix Newsroom 公告: https://news.skhynix.com/multi-year-tech-partnership-with-nvidia/
- TrendForce SK Hynix Vera CPU LPDDR5X 供應分析: https://www.trendforce.com/news/2026/06/08/news-sk-hynix-to-supply-memory-for-nvidia-vera-cpu-as-partnership-deepens-samsung-meeting-on-june-8-in-spotlight/
- TrendForce HBM4 SK Hynix 兩公司供應分析: https://www.trendforce.com/news/2026/01/28/news-sk-hynix-reportedly-to-supply-about-two-thirds-of-nvidia-hbm4-samsung-targets-early-delivery/
- SK Hynix Q1 2026 Earnings 公告（PR Newswire）: https://www.prnewswire.com/news-releases/sk-hynix-announces-1q26-financial-results-302750959.html
- SK Hynix Q1 2026 CNBC 報導: https://www.cnbc.com/2026/04/23/sk-hynix-earnings-ai-memory-shortage-hbm-demand.html
- SK Hynix HBM4 全球首發完成（SK Hynix Newsroom）: https://news.skhynix.com/sk-hynix-completes-worlds-first-hbm4-development-and-readies-mass-production/
- SK Hynix MR-MUF 製程技術: https://news.skhynix.com/rulebreaker-revolutions-mr-muf-unlocks-hbm-heat-control/
- KOSPI 2026-06-08 熔斷報導（TradingKey）: https://www.tradingkey.com/analysis/stocks/more/261951350-kospi-crash-circuit-breaker-samsung-sk-hynix-broadcom-guidance-fed-hikes-retail-leverage-krw-outflow-tradingkey
- KOSPI 7,484 熔斷分析（BBN Times）: https://www.bbntimes.com/global-economy/south-korea-s-stock-market-today-kospi-crashes-8-29-to-7-484-triggers-circuit-breaker-as-chip-rout-fed-fears-and-iran-missiles-converge
- SK Hynix DRAM 雙倍產能 5 年計畫（Tom's Hardware）: https://www.tomshardware.com/pc-components/dram/sk-hynix-to-double-memory-wafer-capacity-over-five-years
- SK Hynix Yongin DRAM Capacity Roadmap（TechTimes）: https://www.techtimes.com/articles/317859/20260606/sk-hynix-dram-capacity-roadmap-revealed-yongin-alone-adds-360k-wafers-monthly.htm
- HBM vs DDR5 wafer 3:1 比率: https://www.techtimes.com/articles/317789/20260604/ddr5-ram-hits-375-floor-pc-builders-hbm-takes-three-times-more-wafers.htm
- SK Hynix Indiana 廠 $3.87B 投資（The Register）: https://www.theregister.com/2026/04/22/sk_hynix_indiana/
- SK Hynix vs Micron 估值對照（Benzinga）: https://www.benzinga.com/markets/tech/26/05/52811262/micron-vs-sk-hynix-best-memory-stock-2026
- HBM 市占 Counterpoint Research: https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share
- HBM 市占 SK 62% 分析（Astute Group）: https://www.astutegroup.com/news/general/sk-hynix-holds-62-of-hbm-micron-overtakes-samsung-2026-battle-pivots-to-hbm4/
- SK Hynix TSMC HBM4 CoWoS-2 合作: https://news.skhynix.com/sk-hynix-partners-with-tsmc-to-strengthen-hbm-technological-leadership/
- Macquarie 2027 HBM 合約價 +50% 預測: https://www.investing.com/news/stock-market-news/sk-hynix-stock-target-lifted-at-macquarie-on-worsening-memory-shortage-4687693
- SK Hynix 客戶提議買 EUV / 出資建廠: https://www.tomshardware.com/tech-industry/sk-hynix-customers-offer-to-buy-its-euv-machines-and-fund-new-fab-lines-as-memory-capacity-hits-zero
- SK Hynix Forward PE / 股價 Yahoo Finance: https://finance.yahoo.com/quote/000660.KS/
- 黃仁勳 Vera CPU SK Hynix 公告（Bloomberg）: https://www.bloomberg.com/news/articles/2026-06-07/nvidia-s-ceo-says-new-vera-chip-will-use-sk-hynix-s-memory-chips
- Vera Rubin HBM4 規格（NVIDIA Tech Blog）: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
- Jetson Thor 128GB LPDDR5X 規格（NVIDIA / Yahboom）: https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/
- SK Hynix 192GB SOCAMM2 量產（OC3D）: https://overclock3d.net/news/memory/sk-hynix-starts-mass-production-on-192gb-socamm2-modules-for-nvidia-vera-rubin/

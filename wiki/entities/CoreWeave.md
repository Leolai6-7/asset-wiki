---
title: CoreWeave
aliases: [CoreWeave, CRWV, CoreWeave Inc, neocloud, Cloud Inc]
type: entity
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-12-09
sources:
  - raw/2026-06-08_Leo-AI-infra-CapEx-三階段論-1.6T-光模組-InP.md
  - raw/2026-05-16_FOMOSOC-KP42-Cerebras上市WSE-3對NVDA啟示.md
tags: [標的, 美股, neocloud, AI 雲端, GPU 雲, NVDA 戰略客戶, NVDA 投資, 循環投資, 1.6T 光模組, CapEx 三階段, 高槓桿利潤率陷阱, Q2 miss]
confidence: high
---

# CoreWeave（CRWV）

## 1. 一句話定位

**neocloud 龍頭 + NVDA 戰略客戶兼投資人 + 1.6T 光模組首批採購者**——2017 起源（前身 Atlantic Crypto，原以太坊礦工）、2019 重 pivot 為 GPU 雲、2024-04 與 NVDA 簽 four-year contract、**2025-03-28 IPO** at $40 上市 NASDAQ；公司「**全棧 AI 雲端**」（從 NVIDIA H100 / H200 / GB200 / GB300 到 Blackwell Ultra 全代次採購）、**vs hyperscaler 三大差異**：(1) **only-GPU specialty**（不做 general purpose cloud、不做存儲業務外溢）、(2) **NVDA-aligned reference architecture**（NVDA Spectrum-X + Quantum-X 全棧首批量產部署）、(3) **跨多年合約模式**（與 Microsoft / Meta / OpenAI / IBM 簽長約 backlog $50B+）；**循環投資典型樣本**——NVDA 投資 CoreWeave $250M（IPO 前）+ CoreWeave 訂 NVDA GPU + CoreWeave 出租算力給 OpenAI / Microsoft / Meta，形成 [[循環投資（CSP-Model 互鎖）]] 五角閉環；**[[AI infra CapEx 三階段論]] 第三階段 anchor 客戶**——1.6T 光模組首批採購者之一（其他：[[Meta]] / [[Microsoft]] / Lambda / Oracle）+ Spectrum-XGS 首批 CoreWeave 跨 DC 部署（2026 H2）；獨立 cloud（亦稱 GPU-as-a-Service）二線打贏一線、市值 **~$70B（2026-06-09）**。

## 2. 三層 thesis

### 產業層

- neocloud 賽道 [[市場四階段：懷疑／驗證／共識／反轉]] 「**驗證 → 共識**」加速段——hyperscaler 自研晶片（Trainium / TPU / MAIA / Cobalt）擠壓 NVDA、但 CoreWeave 是 NVDA stack 的**親緣陣營**（[[NVDA 網路 stack map]] 全棧首批採購者）
  - 不做 general purpose cloud（vs AWS / Azure / GCP）
  - 不做 retail（vs AWS 消費端 EC2 等業務）
  - 只做 GPU 算力 + 配套 networking + storage（**only-GPU specialty**）
- vs hyperscaler 三大結構性差異：
  - **採購節奏**：CoreWeave 拿最早一批 NVDA GPU、Blackwell Ultra / Rubin first wave 都是 CoreWeave 領先（hyperscaler 自己有 ASIC 競爭、採購節奏被內部排擠）
  - **網路 reference architecture**：CoreWeave 全棧 Spectrum-X（不是混搭 Arista / Cisco）= NVDA Photonics、Quantum-X HPC、NVLink Fusion ecosystem first adopter
  - **租賃模式**：CoreWeave 不賣 retail、純 fleet 出租 / long-term contract、客戶 churn 風險小（已簽 $50B+ backlog 蓋 5 年能見度）
- **「Cloud 二線打贏一線」結構性論點**：
  - **2025 GPU 算力 TAM 估 ~$60B+**（vs 2020 cloud 約 ~$200B）
  - 三巨頭 hyperscaler 因自家 ASIC（Trainium / TPU / MAIA）擠壓 NVDA、CoreWeave 拿到 NVDA「戰略客戶」位
  - **NVDA $6.3B backstop**（2025-09-23 公告）：若 CoreWeave 無法在 2032 前找到客戶填產能、NVDA 親自買回算力 → 結構性風險 hedge
- 賽道 timing：
  - [[資訊擴散四階段]] 階段 3-4（IPO 後機構持股已普及、ARK Invest 大舉買入、CRWV 12 月漲幅 +95%+）
  - [[Hyper Rail / Multi-Rail（光通訊整合技術）]] / [[CPO 供應鏈圖譜]] 第 1-2 層 anchor 客戶
  - **2026 Q3** Rubin 平台首批出貨：CoreWeave + [[Meta]] + Oracle Spectrum-X 部署、Spectrum-XGS 首批 CoreWeave 跨 DC 部署
- vs Lambda / Crusoe / Nebius / Vast.ai 等 neocloud 同業：
  - **CoreWeave = neocloud 全球 #1**（vs Lambda 第二、Crusoe / Nebius / Vast.ai 屬第三梯）
  - 市值差距：CoreWeave $70B（已上市）vs Lambda 私募估值 $4B+（2025-06 Series D、2026-04 IPO 暫止）vs Nebius 公開股 $2-3B
  - 護城河：CoreWeave 拿到 NVDA 首批採購權 + 多年合約 backlog + IPO 後資本可循環

### 目的層

- 業務 mix（FY2025、Q3 報告）：
  - **Compute（GPU 出租）= 95%+ 營收主軸**
    - Blackwell Ultra / GB200 / H200 mix shift 中
    - 客戶 prepay + 長約模式（multi-year contract）
  - **Networking + Storage = 補強**（必賣套餐）
  - **NCP（NVIDIA Cloud Partner）認證所綁定**——CoreWeave 是 NVDA Cloud Partner Platinum tier 之一（與 Lambda 並列）
- 客戶結構（極度集中）：
  - **Microsoft = 唯一最大客戶**（>60% 營收）= 集中度風險極高
  - **Meta**（簽 $14.2B 五年合約 2025-09）
  - **OpenAI**（簽 $11.9B 五年合約 2025-03，IPO 前一週簽下、催化關鍵）
  - **IBM**（IBM Granite 模型 cluster）
  - **新增 Mistral AI**（2025-06 第一個歐洲大客戶）
  - **Backlog 結構**：$50B+ 含 OpenAI + Meta + Microsoft + IBM + 多家 AI native；2025-Q3 RPO（Remaining Performance Obligations）$54B
- 商業模式 = **「GPU-as-a-Service + 長約 + 抵押融資」**：
  - 客戶簽長約 → CoreWeave 拿合約做債券抵押（**$23B debt 用 GPU 抵押 + 合約現金流支撐**）
  - 客戶簽長約 → CoreWeave 拿 NVDA prebooking → NVDA 拿 CoreWeave 訂單預估 → CoreWeave 拿錢蓋 DC → 循環
  - **單位經濟**：GPU 成本回收期 **2.5-3 年**（vs hyperscaler 4-5 年）、但客戶綁定 5-7 年 → 第 4-7 年淨現金流是高利潤
- → 連 [[賣水人選股邏輯（投資版）]]：**GPU 雲端「結構性受惠者」**——不押 Anthropic / OpenAI / DeepSeek 誰贏、押所有人都需要的 GPU 算力背後的雲端供應商
  - 比押模型公司更上游、客戶分散度比 hyperscaler 弱（但 backlog 鎖死、churn 風險小）
- [[控制點轉移（投資版）]]：拿到「**NVDA 首批採購權 + reference architecture co-developer + NVDA $6.3B backstop + Spectrum-X / XGS first adopter**」四重控制點 = **NVDA-aligned 半官方** 雲

### 供應層

- 跟 [[NVDA]] 關係（循環投資 anchor）：
  - **NVDA 投資 $250M**（2024 Series C pre-IPO、IPO 後仍持股 ~5%）
  - **NVDA $6.3B backstop**（2025-09-23、若 CoreWeave 無法在 2032 前找到客戶填產能、NVDA 親自買回算力）
  - **NVDA 首批 Spectrum-X 部署**（2026 H2 Rubin 平台首批採購）
  - **NVDA Spectrum-XGS 跨 DC scale across 首批客戶**（2026-08 GA）
  - = **NVDA 把 CoreWeave 視為「NVDA Stack reference customer」**、把獨家規格鎖在 CoreWeave、其他雲廠跟著買 = NVDA 把 CoreWeave 變成銷售管道
- 跟 OpenAI 關係：
  - **$11.9B 五年合約**（2025-03 簽、IPO 前一週公告催化）
  - **OpenAI 持股 ~$350M**（IPO 後 5.4M 股）
  - OpenAI Stargate 多 site 部署、CoreWeave 是 Stargate 的「快交付組件」（Oracle 是「主力 DC 建商」）
- 跟 [[Microsoft]] 關係（**>60% 營收集中度極端風險**）：
  - Microsoft 是 CoreWeave 最大客戶
  - Microsoft 主要租 CoreWeave 給 OpenAI 用（Microsoft 對 OpenAI 算力承諾的部分外包）
  - **2024-04 Microsoft 揭露已取消「部分」CoreWeave 合約**（Financial Times 報導）→ 客戶集中度反向風險警示
- 跟 [[Meta]] 關係：
  - **$14.2B 五年合約**（2025-09）= 第二大長約客戶
  - Meta 自家 MTIA ASIC 平行擴張、但 NVDA GPU 仍是主力訓練 fleet
- 跟 [[AVGO]] 關係：
  - CoreWeave 部分 fleet 採用 Tomahawk 6（非 NVDA Spectrum-6）= multi-source hedge
  - 但 reference architecture 仍以 NVDA Spectrum-X 為主
- 護城河：
  - **NVDA 戰略客戶位 + NVDA $6.3B backstop**（其他雲廠無此安全網）
  - **AI native 客戶 backlog $50B+**（OpenAI + Meta + Microsoft + IBM）
  - **NVL72 + Rubin / Blackwell Ultra first-mover** 部署能力
  - **網路 reference architecture co-developer**（Spectrum-X + Quantum-X + XGS）
- 風險：
  - **客戶集中極端**：Microsoft 60%+、Top 3（MSFT + Meta + OpenAI）90%+
  - **$23B debt + 利率敏感**：用 GPU + 合約抵押融資、利率上升 / 客戶削減合約 → 槓桿斷裂
  - **Microsoft 取消部分合約風險**（已有 2024-04 案例）
  - **hyperscaler 自家 ASIC（Trainium / TPU / MAIA / Cobalt）擠壓 NVDA 採購、CoreWeave 連動受壓**
  - **GPU 折舊速度**：Blackwell → Rubin → Feynman 每 2 年世代躍遷、舊 fleet 折舊 risk
  - **Stock-Based Compensation 巨額**（IPO 後 CEO Mike Intrator 個人 SBC 預估 5 年 $1B+）
  - **CapEx 巨量**：FY2025 CapEx $20-23B（vs 營收 $5-7B）= 槓桿極高
- → 連 [[控制點轉移（投資版）]]：拿到「**NVDA-aligned 半官方雲 + 長約 backlog $50B**」雙重 anchor、但「客戶集中 + 槓桿 + GPU 折舊」三重風險疊加

## 3. 財務狀態快照（As of 2026-06-09）

| 指標 | 數值 |
|---|---|
| 股價 | $145-160 區間（2026-06 月初波動）|
| 52 週區間 | $40 IPO → $200+ 高點 → 目前 $145-160 |
| 12 個月漲幅 | **+95%+**（自 2025-03-28 IPO $40 上市以來）|
| 市值 | **~$70-80B**（流通股 ~485M）|
| Forward PE | **n/a**（仍淨損、FY2026 預估 narrow 轉盈）|
| EV / Sales（FY2026E）| ~5-7x（vs hyperscaler 4-5x、neocloud 同業 8-10x = 折價）|
| FY2025 Q3 營收 | **$1.36B**（YoY +192%、估算）|
| FY2025 全年營收（推估）| **$5.5-7.0B**（自家指引 $5.05-5.15B + 上修）|
| FY2026 自家指引營收 | **$15-18B**（YoY +200%+、Q1 法說會 anchor）|
| FY2025 Q3 RPO | **$54B**（remaining performance obligations）= 4-5 年 backlog 能見度 |
| FY2025 Q3 淨損 | -$361M（vs 營收 $1.36B）|
| FY2025 CapEx | **$20-23B**（推測、CoreWeave 沒完全揭露）|
| 主要客戶 | Microsoft 60%+、Meta、OpenAI、IBM、Mistral AI |
| 員工人數 | ~1,000-1,200 |
| DC 規模 | **>250MW operational + 1.5GW pipeline by 2026 H2**（自家自建 + co-located）|
| 主要競爭 | Lambda（私募）、Nebius（NBIS）、Crusoe、Together AI、Vast.ai、傳統 hyperscaler |
| NVDA 持股 | ~5%（IPO 後）|
| NVDA backstop | **$6.3B**（2032 前若客戶不足、NVDA 親自買回算力）|

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ Q3 +192%、RPO $54B 鎖死 4-5 年能見度、FY2026 指引 +200%+ |
| 毛利率 | ⚠️ GPU 折舊 + DC OpEx 重、Q3 GM ~73-75%（含 SBC + D&A）/ adjusted GM 偏低 |
| OpEx | ⚠️ CapEx $20-23B + R&D 加大 + DC 蓋建期間負擔重、$23B debt 利息壓力 |
| 營業利益 | ⚠️ FY2025 淨損仍 -$1B+ 級、FY2026 narrow 轉盈是 thesis、Re-rate 主要靠 backlog |

→ **Re-rate 三角形 1/4**——**結構性成長股 + 需要時間驗證**：營收高速成長 ✅、其他三軸是「指引 + 結構性 thesis」。CoreWeave 是「**槓桿 backed AI infra growth bet**」（vs hyperscaler 是「穩定現金流 + AI hedge」）。

### ✅ 催化

- 🆕 **2026-06-09 1.6T 光模組首批採購者 anchor**（Leo 2026-06-08 筆記）：與 [[Meta]] / [[Microsoft]] / Lambda / Oracle 並列五大首批採購者、佔 2026 估 3,000 萬顆 60%+ 的最大買方之一
- **2026 Q3 Rubin 平台首批出貨**：CoreWeave + Meta + Oracle Spectrum-X 部署、CoreWeave first wave
- **2026-08 Spectrum-XGS 首批 CoreWeave 跨 DC 部署**（NVDA Newsroom 已揭、跨 DC scale across first adopter）
- **2025-09 NVDA $6.3B backstop**：結構性風險 hedge 已落地
- **$50B+ backlog**：OpenAI $11.9B + Meta $14.2B + Microsoft + IBM + Mistral AI
- **2026 FY 指引 $15-18B 營收 (+200%+)**
- **DC pipeline 1.5GW by 2026 H2**：擴張能見度
- 對應 [[AI infra CapEx 三階段論]] 第三階段 anchor 客戶

### ⚠️ 風險

- **客戶集中極端**：Microsoft 60%+、Top 3 90%+、單一客戶削單即重傷（2024-04 Microsoft 取消部分合約案例）
- **$23B debt + GPU 抵押融資**：利率上升 / 客戶 churn → 槓桿斷裂、CoreWeave 沒有 hyperscaler 級別資本緩衝
- **GPU 折舊速度**：Blackwell → Rubin → Feynman 每 2 年世代、舊 fleet 折舊 risk 高
- **hyperscaler 自家 ASIC 擠壓 NVDA 採購**：Trainium / TPU / MAIA / Cobalt 量產加速、間接影響 NVDA stack 採購節奏
- **NVDA $6.3B backstop 是「上限」not 保證**：超過 backstop 範圍仍有風險
- **股價估值已 price in 多年完美 ramp**：12 月 +95%+ 後 valuation 拉滿、any miss 都是劇烈回檔
- **創投退場**：早期 Magnetar Capital、Hound Partners 等 IPO 後賣壓
- **OpenAI 自家算力（Stargate）擴張**：長期 OpenAI 可能轉向自建 → backlog 風險

## ⭐ neocloud vs hyperscaler 兩種採購者差異（為什麼 CoreWeave 是 Cloud 二線打贏一線）

| 維度 | hyperscaler（AWS / Azure / Google / Meta） | neocloud（CoreWeave / Lambda） |
|---|---|---|
| 採購節奏 | 受自家 ASIC 排擠（Trainium / TPU / MAIA / Cobalt）| **NVDA first wave、Spectrum-X 全棧 reference customer** |
| 業務分散 | General purpose cloud + retail + 儲存 + AI | **only-GPU specialty + AI native 客戶長約** |
| 採購模式 | 多 source（Arista / Cisco / AVGO + NVDA）| **NVDA reference architecture 全棧** |
| 客戶結構 | 百萬企業 + 政府 + retail | **少數 AI native（OpenAI / Meta / Microsoft / IBM）長約 backlog $50B+** |
| 資本結構 | 上千億淨現金 + retained earnings | **$23B debt + GPU 抵押融資 + NVDA $6.3B backstop** |
| 採購量倍數 | 大、但被自家 ASIC 稀釋 | **小、但 100% NVDA stack** |
| **1.6T 光模組 採購順位** | Meta + Microsoft（混搭採購）| **CoreWeave first wave（NVDA Spectrum-X / XGS first adopter）** |
| 對 NVDA 槓桿 | 弱（自家 ASIC 平行）| **強（NVDA Stack 純度高、NVDA-aligned）** |

**結論**：CoreWeave 不是「贏 hyperscaler」、是「**選擇成為 NVDA 的銷售管道**」——NVDA 把 CoreWeave 變成 reference customer、把獨家規格鎖在 CoreWeave、其他雲廠跟著買。CoreWeave 不需要打贏 AWS / Azure / GCP、只需要當「NVDA 半官方雲」就拿到 NVDA stack 全部世代躍遷的優先採購權。**這是 [[控制點轉移（投資版）]]「靠攏 NVDA 拿到 NVDA 控制點外溢」的典型樣本**。

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | **3** | 100% NVDA stack 押 NVDA 路線、若 AMD MI400 / 自家 ASIC 切走 NVDA → CoreWeave 直接受壓 |
| 站別關鍵 | **4** | NVDA-aligned reference customer + Spectrum-X / XGS first adopter = 站別不可繞過、但 Lambda / Crusoe / Nebius 同 niche 可被替代 |
| 耗材 | **2** | GPU 雲是訂閱（長約 5-7 年）、有 recurring 性質、但 GPU 折舊每 2 年世代是「重蓋」非「耗材」 |
| IP | **2** | 沒有自研 IP（自研 Mission Control 軟體 + 部分網路優化、但與 NVDA Mission Control 重疊）、Mass Compute / Weights & Biases 收購補強 |
| 客戶分散 | **1** | Microsoft 60%+、Top 3 90%+ = 客戶集中度極端高、2024-04 Microsoft 取消部分合約是 binary 風險 |

**總分：12/25**

→ **「NVDA-aligned 結構性受惠 + 客戶極度集中」雙面性**：CoreWeave 五軸總分不高（vs neocloud 同業 IQE 17 / Coherent 19 / Lumentum 19），但其「**NVDA 半官方雲身份 + $6.3B backstop + 1.6T 光模組首批採購 + Spectrum-XGS first adopter**」structural anchor 是賽道唯一。**vs Lambda（私募估值 ~$4B、未上市）**：CoreWeave 是 neocloud 賽道唯一可直接押注 entity。

## ⭐ 對 [[NVDA]] / [[Microsoft]] / [[Meta]] / 三階段論的意義

對既有 wiki entity：

### Bull case

- **1.6T 光模組首批採購者**：CoreWeave 拿到 NVDA stack 全棧優先採購權 = NVDA / [[Lumentum]] / [[Coherent]] / [[IQE]] / [[Ciena]] / [[Nokia]] 全鏈受惠
- **Spectrum-XGS 首批跨 DC 部署**（2026-08）= 把 NVDA scale across thesis 驗證、[[Ciena]] Hyper Rail / [[Nokia]] Multi-Rail 順帶受惠
- **OpenAI Stargate 補位**：CoreWeave 是 Stargate 多 site 快交付組件、Oracle 是主力 DC 建商
- **NVDA 賣 GPU + CoreWeave 出租 + AI 公司租用** = [[循環投資（CSP-Model 互鎖）]] 五角閉環的 anchor 樣本

### Bear case

- CoreWeave 客戶集中 + 槓桿斷裂 → NVDA stack 採購順延 → [[AI infra CapEx 三階段論]] 第三階段 narrative 失效
- Microsoft 全面取消合約 → backlog $50B 重估 → 雲端二線 thesis 崩塌
- hyperscaler 自家 ASIC 量產加速 → NVDA 採購整體被擠壓 → CoreWeave 連動

→ **校準 Leo 三階段論第三階段**：1.6T 光模組 2026 年 3,000 萬顆需求（vs 2025 180 萬顆 = 17 倍跳升）的最大買方包括 CoreWeave 在內五家、CoreWeave 不是「最大」單獨買方但是「**最強 NVDA-aligned**」買方。

## 跟其他 wiki 概念連結

- [[AI infra CapEx 三階段論]]：本 entity 是第三階段 anchor 客戶之一（1.6T 光模組首批採購者）
- [[循環投資（CSP-Model 互鎖）]]：NVDA → CoreWeave → 訂 NVDA GPU + AI 公司租用 → NVDA 受益的 anchor 樣本
- [[NVDA 網路 stack map]]：Spectrum-X + Quantum-X + XGS 全棧 first adopter
- [[CPO 供應鏈圖譜]]：第 1 + 2 + 8 層 anchor 客戶（NVDA Photonics 部署最早）
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：Spectrum-XGS 跨 DC scale across 首批客戶 = Hyper Rail / Multi-Rail 順帶受惠
- [[Jevons Paradox（投資版）]]：CoreWeave 出租價下降 → AI workload 需求暴增 → 又拉動 GPU 採購
- [[控制點轉移（投資版）]]：拿到「NVDA-aligned 半官方雲」控制點外溢
- [[賣水人選股邏輯（投資版）]]：GPU 雲端結構性受惠者、不押模型公司誰贏
- [[資訊擴散四階段]]：IPO 後 +95% 12 月、機構持股普及階段 3-4
- [[市場四階段：懷疑／驗證／共識／反轉]]：neocloud 賽道在驗證 → 共識加速段
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 強制格式
- [[NVDA]]：戰略客戶 + 投資人 + reference customer 三位一體
- [[Microsoft]] / [[Meta]] / [[OpenAI]]：Top 3 backlog 客戶
- [[AVGO]] / [[Marvell]]：scale out 部分 multi-source 採購

## 相關連結

- [[AI infra CapEx 三階段論]]
- [[循環投資（CSP-Model 互鎖）]]
- [[NVDA 網路 stack map]]
- [[NVDA]]、[[Microsoft]]、[[Meta]]、[[OpenAI]]
- [[Lumentum]]、[[Coherent]]、[[IQE]]
- [[Ciena]]、[[Nokia]]
- [[控制點轉移（投資版）]]
- [[賣水人選股邏輯（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]

## ⭐ Q2 2026 指引 miss — 高槓桿利潤率陷阱訊號（2026-05-16 KP42）

→ 完整 framework 見 [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]

### Q2 指引矛盾

| 指標 | 指引 | 市場預期 | 落差 |
|---|---|---|---|
| Q2 營收 | $25.3 億 | $26.9 億 | **miss** |
| Q2 營業利潤 | $30-90M | $154M | **miss** |

### 利潤率陷阱結構

| 指標 | 現況 |
|---|---|
| **EBITDA 利潤率** | **56%**（高、產能擴張中）|
| **營業利潤率** | **1%**（vs Q4 6%、去年 17%）⚠️ |
| **折舊 + 利息壓力** | 持續攀升（$23B debt）|
| **客戶集中** | Microsoft 60%+ |

### vs [[Nebius]] 對照

- CoreWeave 高槓桿擴張 EBITDA 56% / 營益 1%
- Nebius 預售模式 EBITDA 45% / 營益 較穩健
- → neocloud 兩種模式分歧

### 對 [[NVDA]] 傳導意義

- CoreWeave 利潤率陷阱 = **neocloud 整體營運壓力訊號**
- 但 NVDA 仍享 backlog 緩衝（$50B backlog 即使部分延後仍要採購）

## 跟既有 wiki 概念連結

- [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]（KP42 framework）
- [[CapEx 見頂辯論]]
- [[FCF 拐點]]
- [[FOMO SOC]]（KP@FOMOSoc KOL 來源、待建）

## Source URLs

- CoreWeave IPO Filing S-1（2025-03-03、SEC）: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0002030781&type=S-1
- CoreWeave Q3 2025 Earnings Press Release: https://investors.coreweave.com/news-releases
- CoreWeave NVDA $6.3B Backstop Agreement（2025-09-23）: https://www.theinformation.com/articles/nvidia-coreweave-backstop
- CoreWeave Meta $14.2B 5-Year Contract（2025-09）: https://www.coreweave.com/blog/meta-coreweave
- CoreWeave OpenAI $11.9B 5-Year Contract（2025-03、IPO 前一週）: https://www.bloomberg.com/news/coreweave-openai
- CoreWeave Spectrum-XGS First Adopter（NVDA Newsroom 2025）: https://nvidianews.nvidia.com/news/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories
- CoreWeave NCP Platinum Tier（NVDA Cloud Partner）: https://www.nvidia.com/en-us/data-center/cloud-providers/coreweave/
- CoreWeave Wikipedia: https://en.wikipedia.org/wiki/CoreWeave
- CoreWeave 1.6T 光模組首批採購者（Leo 2026-06-08 ingest）: raw/2026-06-08_Leo-AI-infra-CapEx-三階段論-1.6T-光模組-InP.md

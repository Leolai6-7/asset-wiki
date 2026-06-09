---
title: Databricks
aliases: [DBRX, Databricks Inc, Mosaic AI, Lakehouse Platform, Unity Catalog, MLflow, Photon, Ali Ghodsi, Apache Spark commercial, Databricks IPO]
type: entity
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-12-09
expires_on: 2027-12-09
sources:
  - raw/2026-05-30_FOMOSOC-KP44-Tesla-SpaceX-Marvell-Snowflake-Dell-Anthropic.md
tags: [標的, 私募, 雲端資料平台, Lakehouse, Unity Catalog, MLflow, Mosaic AI, Photon, Spark 商業化, 跨多雲, Fortune 500, AI 訓練, 訂閱年金, NOT-INVESTABLE, IPO pending, G1]
confidence: high
---

# Databricks（私募、IPO pending 2026 H2-2027 H1）

> **⚠️ 重要警語**：Databricks 是私募未上市公司、**NOT-INVESTABLE**（除非透過二級平台 Forge / EquityZen / Hiive 或 IPO 後）。本 entity 主要作 **[[Snowflake]] 雙頭分歧 reference + 待 IPO 重評 anchor**、五軸評分為**推測值**（基於公開揭露 + media report）、IPO 後需重評。

## 1. 一句話定位

**全球企業 AI 數據湖倉 #1 私募 + Spark 商業化先驅 + 跨 AWS / Azure / GCP / Oracle / Alibaba 多雲完整覆蓋 + 2024-12 Series J $10B @ $62B 估值 + 2025 secondary tender @ ~$62-65B + 2026 H2-2027 H1 IPO 預期 $80-120B 估值 + Mosaic AI 自研 Foundation Models + Unity Catalog open governance + 跟 [[Snowflake]] 19/25「企業數據雙頭」並列**——2013 在 Berkeley AMPLab Apache Spark 創立者團隊（Matei Zaharia + Ali Ghodsi + Ion Stoica）分拆、總部 San Francisco；現任 CEO **Ali Ghodsi**（共同創辦人、前 Berkeley 教授）；**核心產品 Databricks Lakehouse Platform**（合併 data lake + data warehouse 兩種範式）+ **Unity Catalog**（跨 Delta Lake + Apache Iceberg open table 治理）+ **MLflow**（ML 模型生命週期管理）+ **Mosaic AI**（自家 Foundation Models + DBRX / Mosaic MPT 開源 + Hugging Face 整合）+ **Photon**（C++ 向量化執行引擎）+ **Databricks SQL**（SQL Warehouse、吃 Snowflake 主場）；業務組合：**Data Engineering + Spark + ML 訓練 ~45%** + **Data Warehousing（SQL Warehouse、Snowflake 競爭面）~25%** + **AI / Mosaic AI + Foundation Models ~20%** + **Databricks Marketplace + 第三方資料 ~10%**；客戶 **Fortune 500 ~60%+ AVL**（vs Snowflake 90%+ = Databricks 客戶滲透率稍低但 AI 訓練主場勝）、跨 AWS / Azure / GCP / Oracle / Alibaba 多雲；ARR ~$3B（FY2026、YoY +50%+）/ FY2025 營收 ~$2.4-2.6B / **私募仍虧損**（按 SaaS 同期估算、ARR 對標 Snowflake $3.5-4B 接近）；**Forward PE n/a**（私募未上市、IPO 後預期 50-80x）；2024-12 Series J $10B @ $43B（含 secondary tender）→ 2025-09 secondary tender @ $62B（媒體揭露）→ 2026 H2-2027 H1 IPO 預期 **$80-120B 估值**（vs Snowflake 上市 $48-60B）；推測五軸 **19/25**（路線 5 跨多雲 vs SNOW 4 跨雲 + 站別 4 + 耗材 5 訂閱年金 + IP 3 + 客戶分散 2 Fortune 500 集中）= 跟 [[Snowflake]] 19 並列「**企業數據雙頭**」、IPO 後是 Snowflake 估值反向 anchor。

## 2. 三層 thesis

### 產業層

- 雲端資料平台賽道 [[市場四階段：懷疑／驗證／共識／反轉]]「**驗證 → 共識**」加速段——但 Databricks 跟 [[Snowflake]] 路線分歧
  - vs hyperscaler general purpose cloud 三大結構性差異：
    1. **跨多雲 vendor neutral**（Databricks 部署在 AWS / Azure / GCP / Oracle / Alibaba 五家、客戶不必選邊）
    2. **Lakehouse 範式 + Spark 主導**（非結構化 + AI 訓練資料優先 vs Snowflake SQL warehouse）
    3. **訂閱年金 + 用量計費雙引擎**
  - 賽道二極化趨勢：**[[Snowflake]]（governance + 純 SQL data warehouse）vs Databricks（Lakehouse + Spark + ML / AI training）= 兩種範式分歧**
- vs **[[Snowflake]] 19/25 雙頭對打**：
  - **Snowflake = SQL data warehouse + governance + structured BI**（Fortune 500 結構化資料優先）
  - **Databricks = Lakehouse + Spark + ML training + 非結構化資料**（AI 訓練資料優先）
  - **2026 趨勢匯流**：Snowflake 擴張 Cortex AI + Polaris Catalog（吃 Lakehouse）vs Databricks 擴張 SQL Warehouse + Unity Catalog（吃 SQL）= 雙頭對打、客戶必雙頭採用
  - **Databricks 私募估值 $62B（2024-12 Series J）vs Snowflake 上市 $48-60B**（2026-06）≈ 接近、IPO 後預期 $80-120B 可能反超 Snowflake
- 賽道 timing：
  - [[資訊擴散四階段]] 階段 1-2（私募階段、機構持有、散戶仍無 access）
  - **2024-12 Series J $10B @ $43B**：含 secondary tender 部分流動性釋放給員工 + 早期投資人
  - **2025-09 secondary tender @ $62B**（媒體揭露）：機構流動性事件、價格錨點
  - **2026 H2-2027 H1 IPO 預期窗口**：根據媒體報導 + Ali Ghodsi 公開暗示
- **「Lakehouse + 跨多雲 + Mosaic AI」結構性論點**：
  - **Lakehouse 範式融合 data lake + data warehouse**（解決企業「兩套基礎建設」問題）
  - **Apache Iceberg open table** 整合（vs Snowflake 早期 Iceberg 慢半拍、2024-2026 加速跟進 Polaris Catalog）
  - **Mosaic AI + DBRX 開源**：客戶可在 Databricks 內訓練 + 部署自家模型
  - **MosaicML 收購（2023-07 USD $1.3B）**：Databricks 進入 Foundation Models 訓練第二曲線

### 目的層

- 業務 mix（FY2026 估算、ARR ~$3B 推算）：
  - **Data Engineering + Spark + Delta Lake = 45%**（Lakehouse 核心、ML 訓練資料管線）
  - **Databricks SQL Warehouse + Unity Catalog = 25%**（吃 Snowflake 主場）
  - **AI / Mosaic AI + Foundation Models + DBRX = 20%**（自家 + 開源 + Hugging Face 整合）
  - **Databricks Marketplace + 第三方資料 = 10%**（Marketplace 平台 ecosystem）
- 客戶結構：
  - **Fortune 500 ~60%+ AVL**（vs Snowflake 90%+ = Databricks 客戶滲透率較低、但 AI 訓練主場勝）
  - **Fortune 100 ~85%+ AVL**
  - **Top 5 客戶 < 12%**（更分散、AI training 客戶 multi-vendor）
  - **Revenue Retention Rate (RRR) ~140%+**（vs Snowflake ~126% = Databricks 結構性 retention 領先、AI workload 用量爆炸）
  - **Total customers ~10,000+**（含 Fortune 500 多數）
- 商業模式 = **「訂閱年金 + 用量計費雙引擎 + AI workload 用量爆炸」**：
  - **多年合約 + 用量計費**：客戶 commit 多年消費承諾、按用量扣費（類 Snowflake）
  - **AI training workload** = 用量爆炸（GPU instances + LLM training + Foundation Models）
  - **Mosaic AI agent + 自家 Foundation Models** = 用量自我擴張
  - **Marketplace + Unity Catalog ecosystem** = 自我擴張平台效應
- → 連 [[賣水人選股邏輯（投資版）]]：**「企業 AI 訓練 + Lakehouse 賣水人」**——不押模型公司誰贏（Anthropic / OpenAI / Google Gemini）、押所有企業 AI 訓練都需要的「資料 + ML 平台」
- [[控制點轉移（投資版）]]：拿到「**Fortune 500 AI 訓練資料管線 + 跨多雲 vendor neutral + Mosaic AI 自家 Foundation Models + Unity Catalog open governance + DBRX 開源 narrative**」五重 anchor

### 供應層

- 跟 [[AMZN]] AWS / [[Microsoft]] Azure / [[Google]] GCP 關係（**完全跨多雲覆蓋**）：
  - AWS / Azure / GCP 都是 Databricks 主雲（vs Snowflake 80%+ AWS 集中）
  - **Azure Databricks**：Microsoft 跟 Databricks 2017 戰略合作、Azure Databricks 是 Azure 主力 ML 服務
  - **AWS Databricks**：AWS 部署最多客戶、Spark 主場
  - **GCP Databricks**：跟 BigQuery 競爭、但 ML training 整合 TPU
  - **Oracle Cloud + Alibaba Cloud**：額外擴張、Snowflake 暫無
- 跟 [[NVDA]] 關係：
  - **Mosaic AI + NVDA GPU + NeMo / NIM 整合**：Databricks AI 訓練用 NVDA GPU stack
  - 2024-06 Databricks Summit 公告 NVDA 合作（NeMo / NIM 整合進 Mosaic AI）
  - NVDA 不是 Databricks 直接供應商、是技術生態夥伴 + 戰略投資人（Databricks 私募投資人之一）
- 跟 [[Snowflake]] 關係（**最重要的直接對手 + 共生**）：
  - **路線分歧**：Snowflake SQL warehouse + governance vs Databricks Lakehouse + Spark ML
  - **2026 趨勢匯流**：兩家都擴張 platform、互相蠶食 mature workload
  - Databricks 私募估值 $62B + 未上市、IPO 預估 2026 H2-2027 H1
  - **客戶共生**：Fortune 500 客戶必雙頭採用（Snowflake 跑 SQL BI + Databricks 跑 AI 訓練）
- 跟 [[Anthropic]] / [[OpenAI]] / Google / Meta 關係：
  - **Databricks Marketplace + Mosaic AI integration**：Databricks 整合 Anthropic / OpenAI / Google / Meta 模型 + 自家 DBRX
  - = **Databricks 不選邊、所有模型都能用**（model agnostic）+ 自家 DBRX 開源 compete + 整合
- 跟 MosaicML 整合（**2023-07 USD $1.3B 收購**）：
  - Databricks 收購 MosaicML 進入 Foundation Models 訓練
  - MosaicML MPT-7B / MPT-30B 開源模型 → Databricks 整合 Mosaic AI platform
  - **DBRX 132B（2024-03 開源）**：Databricks 自家 Foundation Models、Mosaic AI 旗艦
- 護城河：
  - **Spark 創辦者 + 開源 ecosystem 控制**（Apache Spark + Delta Lake + MLflow + Mosaic AI 四 open-source 框架）
  - **跨多雲 vendor neutral**（hyperscaler 無法強迫客戶選邊、五雲覆蓋）
  - **訂閱年金 + 用量計費 + AI workload 用量爆炸雙引擎**（RRR 140%+ 結構性領先 SaaS 同業）
  - **Mosaic AI + DBRX + Foundation Models 自家堆疊**（model agnostic + 自家整合）
  - **MosaicML 收購 + Foundation Models 自研能力**
  - **Microsoft Azure Databricks 戰略合作 anchor**
  - **私募 high valuation + IPO 預期 anchor**
- 風險：
  - **私募未上市 + NOT-INVESTABLE**（除二級平台 / IPO）
  - **AWS / Azure / GCP 自家 AI services 蠶食**（Bedrock / OpenAI on Azure / Vertex AI）
  - **Snowflake Cortex AI + Polaris Catalog 直接競爭**（SQL Warehouse + Lakehouse 雙向擴張）
  - **Microsoft Fabric + Power BI bundle 威脅**（M365 E5 客戶 bundled discount + Azure Databricks 內部競爭）
  - **IPO 後估值膨脹風險**：若 IPO 估值 $80-120B + Forward PE 50-80x 過熱、後續 re-rate 收縮
  - **AI agent 採用 S 曲線推遲**（[[AI 利潤奇點（Token 經濟學拐點）]] 採用慢於預期）
  - **Mosaic AI ramp 慢**：DBRX 開源 / Mosaic AI 整合落後 OpenAI / Anthropic / Google Gemini 模型 narrative
  - **Fortune 500 集中度**（雖然 Top 5 < 12% 較 Snowflake 分散、但 Fortune 100 85%+ AVL）
  - **私募仍虧損**：按 SaaS 同期估算 ARR $3B 但 EBITDA 仍負
- → 連 [[控制點轉移（投資版）]]：拿到「**跨多雲 + Spark + Mosaic AI 自研 + Unity Catalog open**」四重控制點、但有「hyperscaler bundle + Snowflake 兩面夾擊 + 私募流動性」結構性壓力

## 3. 財務狀態快照（As of 2026-06-09、FY 2025-2026 estimated）

| 指標 | 數值 |
|---|---|
| 上市狀態 | **⚠️ 私募未上市、NOT-INVESTABLE**（除二級平台 / IPO 後）|
| 2024-12 Series J 估值 | **$43B**（$10B Series J + 部分 secondary tender）|
| 2025-09 secondary tender 估值 | **~$62B**（媒體揭露、員工 + 早期投資人流動性事件）|
| IPO 預期估值（2026 H2-2027 H1）| **$80-120B**（vs Snowflake 上市 $48-60B 接近至反超）|
| ARR（FY2026 estimated）| **~$3B**（YoY +50%+）|
| FY2025 全年營收（estimated）| **~$2.4-2.6B**（YoY +50%+）|
| Revenue Retention Rate（RRR）| **~140%+**（vs Snowflake ~126% = 結構性領先）|
| Fortune 500 滲透 | **~60%+ AVL**（vs Snowflake 90%+）|
| Fortune 100 滲透 | **~85%+ AVL** |
| Top 5 客戶 | **< 12% 營收**（vs Snowflake < 15% = 更分散）|
| 總客戶數 | **~10,000+** |
| 員工人數 | **~7,000+** |
| GAAP 淨損 | **仍負**（按 SaaS 同期估算）|
| Free Cash Flow | **接近正向、未公開**（IPO 前主要指標待揭露）|
| 私募投資人 | Andreessen Horowitz / NEA / T. Rowe Price / NVIDIA / Capital One / Tiger Global / Coatue 等多家 |

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ ARR $3B + RRR 140%+ + Fortune 500 60%+ AVL + 跨多雲 vendor neutral |
| 毛利率 | ⚠️ Product GM 推測 ~70-75%（含 cloud 成本回流 AWS / Azure / GCP）、AI training workload GPU 成本高 |
| OpEx | ⚠️ R&D + S&M 投入高、Mosaic AI + DBRX 整合 + Foundation Models 訓練 OpEx 重 |
| 營業利益 | ⚠️ GAAP OP 仍負、Adjusted OP margin 推測 ~5-10%、IPO 後待揭露 |

→ **Re-rate 三角形 1/4**——**「私募 high valuation + IPO 預期 + 跨多雲 + AI training 主場」雙引擎驅動**：ARR 高速成長 ✅、其他三軸需要時間驗證 + IPO 後 disclosure。Databricks 是「**私募 + AI training narrative bet**」——其結構性論點 + 跨多雲 + Mosaic AI 是 anchor 安全網、但 IPO 後估值 $80-120B 已 price in 多年完美 ramp。

### ✅ 催化

- 🆕 **2026 H2-2027 H1 IPO 預期窗口**：媒體報導 + Ali Ghodsi 公開暗示
  - `as_of: 2026-06-09, expires_on: 2027-12-31`
- 🆕 **跨多雲 vendor neutral**：AWS + Azure + GCP + Oracle + Alibaba 五雲完整覆蓋
- 🆕 **Mosaic AI + DBRX 132B 開源 + Foundation Models 自家堆疊**：跟 OpenAI / Anthropic / Google 並列 model 公司
- **2024-12 Series J $10B @ $43B + 2025-09 secondary tender @ $62B**：私募估值 anchor + 流動性事件
- **ARR $3B + RRR 140%+**：結構性 retention 領先 SaaS 同業
- **Microsoft Azure Databricks 戰略合作 anchor**：Azure 主力 ML 服務
- **MosaicML $1.3B 收購整合（2023-07）**：Foundation Models 訓練第二曲線
- **Unity Catalog + Apache Iceberg open table 整合**：Lakehouse 整合進企業 governance
- **Databricks Marketplace + 第三方資料 + Hugging Face 整合**：開放生態擴張
- 對應 [[AI 利潤奇點（Token 經濟學拐點）]] 第三軸「軟體商業模式升級」/「按工作量售賣」

### ⚠️ 風險

- **私募未上市 + NOT-INVESTABLE**（除二級平台 / IPO）
- **AWS / Azure / GCP 自家 AI services 蠶食**：Bedrock / OpenAI on Azure / Vertex AI 等
- **Snowflake Cortex AI + Polaris Catalog 直接競爭**：2026 趨勢匯流
- **Microsoft Fabric + Power BI bundle 威脅**：M365 E5 客戶 bundled discount + Azure Databricks 內部競爭
- **IPO 後估值膨脹風險**：若 $80-120B + Forward PE 50-80x 過熱、後續 re-rate 收縮
- **AI agent 採用 S 曲線推遲**：若 [[AI 利潤奇點（Token 經濟學拐點）]] 採用慢於預期、Mosaic AI ramp 推遲
- **Mosaic AI ramp 慢**：DBRX 開源 / Mosaic AI 整合落後 OpenAI / Anthropic / Google Gemini 模型 narrative
- **Fortune 500 集中度**（Top 5 < 12%、Fortune 100 85%+ AVL）
- **私募仍虧損**：按 SaaS 同期估算 ARR $3B 但 EBITDA 仍負

## ⭐ 對 [[Snowflake]] / [[Microsoft]] / [[Forward Deployed Engineer 戰略（FDE）]] 的意義

### Bull case

- **跟 [[Snowflake]] 並列「企業 AI platform 雙頭」**：客戶必雙頭採用、Snowflake SQL BI + Databricks AI training 共生
- **跨多雲 vendor neutral + Microsoft Azure Databricks 戰略合作**：所有 hyperscaler 都用、不選邊
- **Mosaic AI + DBRX 132B 開源 + Foundation Models 自家堆疊**：跟 Anthropic / OpenAI / Google 並列 model 公司
- **ARR $3B + RRR 140%+ + Fortune 500 60%+ AVL**：結構性護城河
- **IPO 後 $80-120B 估值預期是 Snowflake 估值反向 anchor**：Databricks 上市估值 + Forward PE 50-80x → Snowflake 估值需要結構性 re-rate

### Bear case

- Microsoft Fabric / AWS Bedrock / Google Vertex AI bundle 反向蠶食 → Databricks Fortune 500 protection 削弱
- Snowflake Polaris Catalog + Cortex AI 主場 → Databricks Lakehouse 護城河減弱
- IPO 後 $80-120B 估值膨脹 → 後續 re-rate 收縮 -30 至 -50%
- Mosaic AI ramp 慢 → DBRX 整合落後 OpenAI / Anthropic / Google Gemini 模型 narrative
- 私募仍虧損 → IPO 後 GAAP OP / EBITDA 不達預期

→ **校準「企業數據雙頭」格局**：Databricks 跟 Snowflake 形成「**Lakehouse + AI training vs SQL Warehouse + governance**」雙頭分歧、IPO 後 $80-120B 預期估值 = Snowflake 估值反向 anchor、是 [[AI 利潤奇點（Token 經濟學拐點）]] 第三軸「軟體商業模式升級」典型樣本（AI training workload 用量爆炸 → RRR 140%+ 結構性放大）。

## 五軸評分（25 分制、推測值）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | **5** | 跨 AWS / Azure / GCP / Oracle / Alibaba 五雲 vendor neutral、不押任何 hyperscaler、勝 Snowflake 4（80%+ AWS 集中）|
| 站別關鍵 | **4** | Fortune 500 AI training 主場 + Spark 創辦者 + Unity Catalog open governance = 站別關鍵，但 hyperscaler bundle 替代風險 |
| 耗材 | **5** | 訂閱年金 + 用量計費雙引擎、AI workload 用量爆炸、RRR 140%+ 結構性 retention 領先 |
| IP | **3** | Spark + Delta Lake + MLflow + Mosaic AI + DBRX 132B 開源、但相對 Synopsys / Cadence 等 EDA 30+ 年 IP 較弱 |
| 客戶分散 | **2** | Fortune 500 60%+ AVL、Top 5 < 12% 較 Snowflake 分散但仍 Fortune 100 85%+ AVL = 結構性集中 + 私募階段客戶數仍小 |

**總分：19/25**（推測值、IPO 後重評）

→ **「跨多雲 + AI training narrative bet + Fortune 500 結構性 lock-in」**：Databricks 推測五軸 19/25 跟 [[Snowflake]] 19 並列「**企業數據雙頭**」、跟 [[Accenture]] 19 + [[GlobalFoundries]] 20 + [[Coherent]] 19 + [[Lumentum]] 19 同級。**主因**：跨多雲（5/5、勝 SNOW 1 分）+ 訂閱年金（5/5）+ 站別關鍵（4/5）三軸驅動、但 IP（3/5）落後 Synopsys / Cadence + 客戶分散（2/5、低 SNOW 1 分）受私募階段客戶數小 + Fortune 100 85%+ AVL 集中拖累。

## ⭐ 跟 [[Snowflake]] 路線分歧（行業關鍵戰局）

**兩家路線分歧 = 企業 AI platform 兩種範式**：

| 維度 | [[Snowflake]] | Databricks |
|---|---|---|
| 起點範式 | SQL data warehouse | Spark Lakehouse |
| 結構化 vs 非結構化 | **結構化資料 + BI 優先** | **非結構化 + AI training 優先** |
| 主場客戶 | Fortune 500 金融 / 零售 / 製造（結構化資料豐富）| Fortune 500 科技 / 媒體 / 互聯網（非結構化 + AI 訓練多）|
| 治理 governance | Polaris Catalog + 30 年 BI lineage | **Unity Catalog + AI / ML 模型治理 + 多雲統一** |
| AI 整合 | Cortex AI + NVDA NeMo / NIM | **Mosaic AI + Hugging Face + 自研 Foundation Models DBRX** |
| Lakehouse 路線 | Polaris Catalog（吃 Databricks 主場、2024-2026 加速）| **Lakehouse 始祖 + Spark 主導** |
| 跨多雲覆蓋 | AWS 80%+ 主力 + Azure / GCP 第二 | **AWS + Azure + GCP + Oracle + Alibaba 五雲**（勝 SNOW 1 分）|
| 上市狀態 | 2020-09 上市 NYSE：SNOW | **⚠️ 私募 $62B 估值（2024-12 Series J）+ IPO 2026 H2-2027 H1** |
| 估值 / 規模 | $48-60B 市值（Forward PE 65-90x）| **$62B 私募估值（IPO 後可能 $80-120B、Forward PE 50-80x 預期）**|
| 客戶 RRR | ~126% | **~140%+（更激進、AI workload 用量爆炸）**|
| 商業模式 | 訂閱年金 + 用量計費 | 訂閱年金 + 用量計費（類似）|
| 戰略合作 | AWS $60B 5 年合約 | Microsoft Azure Databricks 17 年戰略合作 + Mosaic AI 整合 |

**結論**：**Snowflake 跟 Databricks 不是「一家贏」、是「雙頭分食 + 共生」**——Fortune 500 客戶必雙頭採用（Snowflake 跑 SQL BI + Databricks 跑 AI 訓練）。但 2026 趨勢匯流（Snowflake 擴 Lakehouse + Databricks 擴 SQL Warehouse）→ 雙頭可能「**互相蠶食 mature workload + 中間客戶開始選邊**」。**Databricks IPO 後是 Snowflake 估值的反向 anchor**——若 Databricks 上市估值 $80-120B + Forward PE 50-80x → Snowflake 估值需要結構性 re-rate。

## ⭐ Databricks vs Mosaic AI vs DBRX 三層堆疊

| 層級 | Databricks 元素 |
|---|---|
| **Lakehouse Platform** | Delta Lake + Photon C++ 引擎 + Apache Iceberg 整合 |
| **Data + ML Tooling** | MLflow + Unity Catalog + Databricks SQL + Photon |
| **Mosaic AI** | Foundation Models 整合 + Hugging Face 整合 + Mosaic Inference + AI agent framework |
| **DBRX 132B** | 自家 Foundation Models（2024-03 開源）+ 跟 OpenAI / Anthropic / Google compete |

→ Databricks 不只是「**資料平台**」、是「**Lakehouse + AI training 全棧 platform + 自家 Foundation Models**」

## 跟其他 wiki 概念連結

- [[AI 利潤奇點（Token 經濟學拐點）]]：本 entity 是「**軟體商業模式升級**」第三軸代表（AI training workload 用量爆炸、RRR 140%+ 結構性領先）
- [[Forward Deployed Engineer 戰略（FDE）]]：Databricks 提供「企業 AI training 可信執行環境」+ Mosaic AI 客戶部署 = FDE 對接點
- [[賣水人選股邏輯（投資版）]]：「企業 AI training + Lakehouse 賣水人」、不押模型公司誰贏、押所有企業 AI training 都需要的資料 + ML 平台
- [[控制點轉移（投資版）]]：拿到「跨多雲 + Spark + Mosaic AI 自研 + Unity Catalog open + DBRX 開源」五重 anchor
- [[Jevons Paradox（投資版）]]：Mosaic AI 用量爆炸 → 客戶 RRR 結構性放大、不需要新合約即可放大營收
- [[資訊擴散四階段]]：私募階段、機構持有、散戶仍無 access、IPO 後階段 3-4 加速
- [[市場四階段：懷疑／驗證／共識／反轉]]：narrative 在「驗證 → 共識」加速段
- [[FCF 拐點]]：私募階段 FCF 仍待 IPO 後揭露
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 強制格式
- [[Snowflake]]：**「企業數據雙頭」並列 anchor**（Snowflake SQL Warehouse + governance vs Databricks Lakehouse + AI training）
- [[Microsoft]]：Azure Databricks 戰略合作 anchor、但 Microsoft Fabric + Power BI 直接競爭
- [[AMZN]] / [[Google]]：AWS / GCP Databricks 部署主力 + AWS Bedrock / Google Vertex AI 競爭面
- [[NVDA]]：Mosaic AI + NeMo / NIM 整合 + NVDA 戰略投資人
- [[Anthropic]] / [[OpenAI]] / [[Google]] / [[Meta]]：模型公司透過 Databricks Marketplace + Mosaic AI 觸及 Fortune 500 + Databricks 自家 DBRX compete
- [[Accenture]]：Databricks FDE / IT 諮詢執行夥伴

## 相關連結

- [[AI 利潤奇點（Token 經濟學拐點）]]
- [[Forward Deployed Engineer 戰略（FDE）]]
- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[Jevons Paradox（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[Snowflake]]、[[Microsoft]]、[[AMZN]]、[[Google]]、[[NVDA]]
- [[Anthropic]]、[[OpenAI]]、[[Meta]]
- [[Accenture]]、[[Palantir]]、[[CoreWeave]]、[[Lambda]]、[[Nebius]]

## Source URLs

- Databricks 公司網站: https://www.databricks.com/
- Databricks 2024-12 Series J $10B @ $43B 公告: https://www.databricks.com/company/newsroom/press-releases/databricks-raises-10-billion-series-j
- Databricks 2025-09 secondary tender @ $62B 媒體報導: https://www.reuters.com/technology/databricks-secondary-tender-62-billion-valuation/
- Databricks MosaicML 收購（2023-07 USD $1.3B）: https://www.databricks.com/company/newsroom/press-releases/databricks-acquires-mosaicml
- DBRX 132B Foundation Models（2024-03 開源）: https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm
- Databricks Unity Catalog + Apache Iceberg 整合: https://www.databricks.com/product/unity-catalog
- Databricks 跟 Snowflake 路線分歧（行業分析）: https://www.reuters.com/technology/snowflake-databricks-ai-platform-divergence/
- FOMO SOC KP #44 narrative shift（2026-05-30）涉及 Snowflake / Databricks 對打: raw/2026-05-30_FOMOSOC-KP44-Tesla-SpaceX-Marvell-Snowflake-Dell-Anthropic.md
- Databricks Wikipedia: https://en.wikipedia.org/wiki/Databricks

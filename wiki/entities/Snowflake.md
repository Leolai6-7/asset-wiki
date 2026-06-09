---
title: Snowflake
aliases: [SNOW, Snowflake Inc, NYSE:SNOW, Snowflake Data Cloud, Frank Slootman, Sridhar Ramaswamy]
type: entity
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-12-09
sources:
  - raw/2026-05-30_FOMOSOC-KP44-Tesla-SpaceX-Marvell-Snowflake-Dell-Anthropic.md
tags: [標的, 美股, 雲端資料平台, Data Cloud, Cortex AI, Snowpark, AWS $60B, 企業 AI 可信執行環境, FY2025, 訂閱年金, Fortune 500, multi-cloud]
confidence: high
---

# Snowflake（SNOW）

## 1. 一句話定位

**全球企業數據雲 #1 純 play + 跨 AWS / Azure / GCP 多雲 + AWS 5 年 $60B 合約（2.4x 前合約）+ FOMO SOC KP #44「企業 AI agent 可信執行環境」narrative 180 度翻轉 anchor**——2012 起源（Benoit Dageville + Thierry Cruanes 創辦於 San Mateo California、原 Oracle 資料庫工程師團隊）、2020-09 IPO at $120 上市 NYSE（當時史上最大軟體 IPO）、Frank Slootman 任 CEO 至 2024 Q1、現任 Sridhar Ramaswamy（前 Google ads SVP + Neeva 創辦人）；**核心產品 = Snowflake Data Cloud**（**Snowflake 1.0** = 雲端資料倉儲 / Cloud Data Warehousing、**Snowflake 2.0** = Data Platform 跨 ingestion + transformation + ML + AI agent）；業務組合：**Data Warehousing 60%** + **Data Engineering（Snowpark）+ Cortex AI + Snowflake Marketplace + Streamlit + Snowsight + Polaris Catalog（Apache Iceberg open table）**；客戶 **Fortune 500 90%+ AVL**（vs Databricks Fortune 500 60%+ = Snowflake 客戶滲透率更深）；FY2025 全年產品營收 **~$3.5-4B**（YoY +25-30%）+ Cortex AI agent 加速 + AWS $60B 五年合約 anchor；Forward PE **65-90x**（雲端 SaaS 估值 premium）+ 12 月 +30-60%；五軸 **19/25**（路線 4 + 站別 4 + 耗材 5 訂閱年金 + IP 3 + 客戶分散 3 Fortune 500 集中）；跟 [[Databricks]]（待建）對打 + [[Oracle]] 18 對比；**「企業 AI 可信執行環境」narrative shift**：從 legacy 資料倉儲被 cloud giants AI services 威脅 → **企業 AI agent 部署的安全 + on-premise data access anchor**。

## 2. 三層 thesis

### 產業層

- 雲端資料平台賽道 [[市場四階段：懷疑／驗證／共識／反轉]]「**驗證 → 共識**」加速段——但 narrative 經歷 180 度翻轉（2024 H1 被 AWS Redshift / Azure Synapse / Google BigQuery + cloud-native AI services 威脅 → **2025-2026 變成「企業 AI agent 可信執行環境」anchor**）
  - vs hyperscaler general purpose cloud 三大結構性差異：
    1. **跨多雲 vendor neutral**（Snowflake 部署在 AWS / Azure / GCP 三家、客戶不必選邊）
    2. **企業 data governance 純度**（Fortune 500 已建立的 data lineage + security + compliance lock-in）
    3. **訂閱年金 + 用量計費雙引擎**（vs hyperscaler 純用量計費）
  - 賽道二極化趨勢：**Snowflake（governance + 純 SQL data warehouse）vs Databricks（Lakehouse + Spark + ML / AI training）= 兩種範式分歧**
- vs **[[Databricks]]（待建私募）**兩條路線分歧（行業關鍵戰局）：
  - **Snowflake = SQL data warehouse + governance + structured BI**（Fortune 500 結構化資料優先）
  - **Databricks = Lakehouse + Spark + ML training + 非結構化資料**（AI 訓練資料優先）
  - **2026 趨勢匯流**：Snowflake 擴張 Cortex AI + Polaris Catalog（吃 Lakehouse）vs Databricks 擴張 SQL Warehouse + Unity Catalog（吃 SQL）= 雙頭對打、客戶必雙頭採用
  - **Databricks 私募估值 $62B（2024-12 Series J）vs Snowflake 上市 $48-60B**（2026-06）≈ 接近、但 Databricks 仍未上市
- 賽道 timing：
  - [[資訊擴散四階段]] 階段 3-4（IPO 後機構持股普及、12 月 +30-60% 已過散戶看到階段）
  - **2025-12 AWS $60B 五年合約 anchor 事件**：Snowflake 跟 AWS 新合約價值 $60B（vs 前合約 ~$25B = 2.4x 跳升）= 結構性 lock-in AWS 主雲伴侶
  - **2026 Cortex AI agent + Snowpark Container Services** 量產加速
- **「企業 AI agent 可信執行環境」結構性論點**（FOMO SOC KP #44 anchor）：
  - 企業 AI agent 需要訪問**內部敏感資料**（薪資、HR、財務、客戶資料）= 不能放在 hyperscaler 通用 cloud
  - Snowflake = **企業已建立的 data lineage + security + governance 環境** = AI agent 部署的「**可信邊界**」
  - 跟 [[Forward Deployed Engineer 戰略（FDE）]] 互補：FDE 解決 deployment、Snowflake 提供「**安全執行容器**」

### 目的層

- 業務 mix（FY2025、Q4 January 2026）：
  - **Product Revenue（含 Compute + Storage + Cloud Services）= 95%+ 營收主軸**
    - **Compute + Storage（Data Warehousing 核心）= 60%**
    - **Data Engineering（Snowpark + Cortex AI + ML）= 25%+ 加速**
    - **Cortex AI agent + Polaris Catalog + Streamlit + 開放生態 = 10-15%**
  - **Professional Services = 5%**（不收高、目的是 land + expand）
- 客戶結構：
  - **Fortune 500 ~90%+ AVL**（vs Databricks ~60%）
  - **Fortune 100 ~95%+ AVL**
  - **Top 5 客戶 < 15%**（high concentration、Capital One + Adobe + Salesforce + AT&T + Sony 等）
  - **Revenue Retention Rate (RRR) ~125-135%**（vs SaaS 同業 110-120% = Snowflake 結構性 retention 領先）
  - **Total customers ~10,000+**（含 Fortune 500 多數）
- 商業模式 = **「訂閱年金 + 用量計費雙引擎」**：
  - **多年合約 + 用量計費**：客戶 commit 多年消費承諾、按用量扣費（vs Salesforce / Workday 純訂閱）
  - **RPO (Remaining Performance Obligations) FY2025 Q4 $6.34B**（鎖死 2-3 年能見度）
  - **Cortex AI + AI agent workload** = 用量爆炸 → 不需新合約自然放大營收
  - **Marketplace + Snowpark ecosystem** = 自我擴張平台效應
- → 連 [[賣水人選股邏輯（投資版）]]：**「企業 AI 可信執行環境」賣水人**——不押模型公司誰贏（Anthropic / OpenAI / Google Gemini）、押所有企業 AI agent 部署都需要的「安全資料邊界」
- [[控制點轉移（投資版）]]：拿到「**Fortune 500 data lineage + governance lock-in + 跨多雲 vendor neutral + Cortex AI agent 整合 + AWS $60B 五年戰略結盟**」五重 anchor

### 供應層

- 跟 [[AWS]] / [[Amazon]] 關係（**$60B 五年合約 anchor**）：
  - **2025-12 AWS $60B 五年 infrastructure 合約**（vs 前合約 ~$25B = 2.4x 跳升）
  - = AWS 主力雲合作（FY2025 estimate AWS 占 Snowflake 雲 spend ~85%）
  - **AWS Graviton ARM CPU + NVIDIA GPU 雙路採購**：Snowflake 透過 AWS 接觸到 Graviton CPU optimization + GPU 推理
  - **意義：證明 custom ARM chips 生產可行**（KP #44 anchor）
- 跟 [[Microsoft]] Azure 關係：
  - Azure 是 Snowflake 第二大雲（FY2025 ~10-12% 雲 spend）
  - Microsoft Fabric 直接競爭 Snowflake，但 Snowflake 跨多雲策略允許客戶共用
- 跟 [[Google]] GCP 關係：
  - GCP 是 Snowflake 第三大雲（FY2025 ~3-5% 雲 spend）
  - Google BigQuery 直接競爭、但 Snowflake 在 GCP 仍有部分企業客戶
- 跟 [[NVDA]] 關係：
  - **Cortex AI + NVIDIA NeMo / NIM 整合**：Snowflake AI agent 用 NVDA GPU 推理 stack
  - 2024-06 Snowflake Summit 公告 NVDA 合作（NeMo / NIM 整合進 Cortex）
  - NVDA 不是 Snowflake 直接供應商、是技術生態夥伴
- 跟 [[Databricks]] 關係（**最重要的直接對手**）：
  - **路線分歧**：Snowflake SQL warehouse + governance vs Databricks Lakehouse + Spark ML
  - **2026 趨勢匯流**：兩家都擴張 platform、互相蠶食 mature workload
  - Databricks 私募估值 $62B + 未上市、IPO 預估 2026 H2-2027 H1
- 跟 [[Anthropic]] / [[OpenAI]] / Google / Meta 關係：
  - **Snowflake Marketplace + Cortex AI integration**：Snowflake 把多個模型公司整合進 Cortex
  - = **Snowflake 不選邊、所有模型都能用**（model agnostic）
- 護城河：
  - **Fortune 500 data lineage + governance 30 年累積**
  - **跨多雲 vendor neutral**（hyperscaler 無法強迫客戶選邊）
  - **訂閱年金 + 用量計費雙引擎**（FCF strong）
  - **Cortex AI + AI agent 整合**（企業 AI 可信執行環境 anchor）
  - **AWS $60B 五年合約**（結構性結盟）
- 風險：
  - **AWS / Azure / GCP 自家 AI services 蠶食**（Bedrock / OpenAI on Azure / Vertex AI）
  - **Databricks Lakehouse + Unity Catalog 直接競爭**（AI training + 非結構化資料勝勢）
  - **Microsoft Fabric + Power BI bundle 威脅**（M365 E5 客戶 bundled discount）
  - **Forward PE 65-90x 已 price in 完美 Cortex AI 兌現**
  - **Fortune 500 集中度**（Top 5 客戶 < 15%、但 Fortune 100 95%+ AVL = 客戶數有上限）
  - **AI agent 採用 S 曲線推遲**（[[AI 利潤奇點（Token 經濟學拐點）]] 採用慢於預期）
  - **$60B AWS 合約執行風險**（5 年內若 AWS 自家 Redshift / Bedrock 反向蠶食客戶）
- → 連 [[控制點轉移（投資版）]]：拿到「**Fortune 500 data lineage 控制點 + 多雲 vendor neutral**」雙引擎控制點、但有「hyperscaler bundle + Databricks 兩面夾擊」結構性壓力

## 3. 財務狀態快照（As of 2026-06-09）

| 指標 | 數值 |
|---|---|
| 股價 | $190-220 區間（2026-06 月初波動） |
| 52 週區間 | $115-$245 |
| 12 個月漲幅 | **+30-60%**（2025-2026 narrative shift 推升）|
| 市值 | **~$60-75B** USD |
| Forward PE | **65-90x**（vs Databricks 私募估值 $62B 接近、雲端 SaaS 估值 premium）|
| EV / Sales（FY2026E）| 13-17x |
| FY2025 全年 Product Revenue | **~$3.5-4B**（YoY +25-30%）|
| FY2025 Q4 Product Revenue | **$987M**（YoY +28%）|
| FY2025 Q4 RPO | **$6.34B**（2-3 年能見度）|
| FY2025 Q4 Revenue Retention Rate | **~126%** |
| FY2025 GAAP 淨損 | **-$1.3B**（含 SBC）|
| FY2025 Free Cash Flow | **~$800M**（含 SBC adjustments）|
| Cortex AI 客戶數 | **>4,000 客戶 + 跨數百企業正式部署** |
| AWS 五年合約 | **$60B**（2025-12 公告、vs 前合約 ~$25B = 2.4x 跳升）|
| Fortune 500 滲透 | **~90%+ AVL** |
| Fortune 100 滲透 | **~95%+ AVL** |
| 總客戶數 | **~10,000+** |
| 員工人數 | ~7,500 |

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ FY2025 +25-30%、RRR 126%、RPO $6.34B、AWS $60B 五年 anchor |
| 毛利率 | ⚠️ Product GM ~75-80%（含 cloud 成本回流 AWS）、Cortex AI ramp 期 GM 有壓 |
| OpEx | ⚠️ R&D + S&M 投入高、Cortex AI 量產 + Snowpark 整合 OpEx 重 |
| 營業利益 | ⚠️ GAAP OP 仍負、Adjusted OP margin ~5-8%、FCF margin 20%+ |

→ **Re-rate 三角形 1/4**——**「narrative 翻轉 + 結構性結盟」雙引擎驅動**：營收 ✅、其他三軸需要時間驗證。Snowflake 是「**訂閱年金 + AI agent narrative shift bet**」——其結構性論點 + AWS $60B 合約是 anchor 安全網、但 Forward PE 65-90x 已 price in 多年完美 ramp。

### ✅ 催化

- 🆕 **2025-12 AWS $60B 五年合約**：vs 前合約 ~$25B = 2.4x 跳升、結構性結盟 anchor
- 🆕 **FOMO SOC KP #44「企業 AI agent 可信執行環境」narrative shift**：從 legacy 資料倉儲 → 企業 AI 部署核心
- **Cortex AI + AI agent 量產加速**：4,000+ 客戶在用、AI agent 部署 unit economics 開始正向
- **Polaris Catalog (Apache Iceberg open table) launch**：Lakehouse 整合進 Snowflake、吃 Databricks 主場
- **Snowpark Container Services + Snowflake AI Hub**：開放 ML / AI 工具整合
- **Marketplace 平台 ecosystem 擴張**：第三方資料 + AI 模型在 Snowflake 內銷售
- **Sridhar Ramaswamy 三軌 CEO 領導**（前 Google ads SVP + Neeva 創辦人 + Snowflake AI 戰略）
- **Cortex AI / Embedding / Vector Search 全棧**：跟 [[Databricks]] 並列「企業 AI platform 雙頭」
- **Fortune 500 90%+ AVL + Revenue Retention 126%** = 結構性護城河
- 對應 [[AI 利潤奇點（Token 經濟學拐點）]] 第三軸「軟體商業模式升級」/「按工作量售賣」

### ⚠️ 風險

- **AWS / Azure / GCP 自家 AI services 蠶食**：Bedrock / OpenAI on Azure / Vertex AI 等
- **Databricks Lakehouse + Unity Catalog 直接競爭**：AI training + 非結構化資料勝勢、2026 Q3-Q4 預期 IPO
- **Microsoft Fabric + Power BI bundle 威脅**：M365 E5 客戶 bundled discount
- **Forward PE 65-90x 已 price in 完美 Cortex AI 兌現**
- **AI agent 採用 S 曲線推遲**：若 [[AI 利潤奇點（Token 經濟學拐點）]] 採用慢於預期、Cortex AI ramp 推遲
- **$60B AWS 合約執行風險**：5 年內若 AWS 自家 Redshift / Bedrock 反向蠶食客戶
- **大量 infrastructure 承諾 + 客戶 underutilization 風險**：KP #44 提示「若企業 AI 採用速度低於預期 → 財務拖累」
- **Sridhar Ramaswamy 整合期管理風險**（2024 Q1 接 Slootman 後續觀察）

## ⭐ 對 [[Databricks]] / [[Oracle]] / [[Forward Deployed Engineer 戰略（FDE）]] 的意義

對既有 wiki entity / concept：

### Bull case

- **Cortex AI + AWS $60B 五年合約** → Snowflake 變成「企業 AI agent 可信執行環境」anchor、結構性 narrative shift
- **跟 [[Oracle]] 18 對比**：Oracle 走「Database 30 年護城河 + AI cloud growth bet」、Snowflake 走「Data Cloud + 跨多雲 vendor neutral + Cortex AI」= 兩種企業 AI cloud 範式
- **跟 [[Forward Deployed Engineer 戰略（FDE）]] 互補**：FDE 解決 deployment 困難、Snowflake 提供「安全執行容器」
- **跟 [[Databricks]]（待建）對打**：FY2026 雙頭並列、客戶必雙頭採用、共生 + 競爭結構

### Bear case

- Microsoft Fabric / AWS Bedrock / Google Vertex AI bundle 反向蠶食 → Snowflake Fortune 500 protection 削弱
- Databricks Lakehouse + AI training 主場 → Snowflake AI agent 主場相對被擠
- $60B AWS 合約執行不順 → 客戶 underutilization → 財務拖累
- Cortex AI ramp 慢 → Forward PE 估值收縮（-30 至 -50%）

→ **校準 KP #44 narrative shift**：Snowflake 從「被威脅的 legacy」→「**企業 AI agent 可信執行環境**」180 度翻轉、是 [[AI 利潤奇點（Token 經濟學拐點）]] 第三軸「軟體商業模式升級」典型樣本（從「按人頭售賣」→「按工作量售賣」）。

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感 | **4** | 跨多雲 vendor neutral、不押任何 hyperscaler，但 AWS $60B 五年合約使路線敏感度略升 |
| 站別關鍵 | **4** | Fortune 500 data lineage 30 年累積、企業 AI agent 部署可信邊界 = 站別關鍵，但 hyperscaler bundle 替代風險 |
| 耗材 | **5** | 訂閱年金 + 用量計費雙引擎、RPO $6.34B 鎖死、RRR 126% 結構性 retention 領先 |
| IP | **3** | Cortex AI + Polaris Catalog + Snowpark IP，但相對 Synopsys / Cadence 等 EDA / Database 30 年 IP 較弱 |
| 客戶分散 | **3** | Fortune 500 90%+ AVL（客戶數總體分散），但 Top 5 < 15%、Fortune 100 95%+ AVL = 結構性集中 |

**總分：19/25**

→ **「訂閱年金 + AI agent narrative shift bet + Fortune 500 結構性 lock-in」**：Snowflake 五軸 19/25 跟 [[Accenture]] + [[GlobalFoundries]] 20 + [[Coherent]] 19 + [[Lumentum]] 19 同級、低於 [[Oracle]] 18 + [[Accenture]] 19 + 高於 [[CoreWeave]] 12 + [[Lambda]] 13。**主因**：訂閱年金（5/5）+ 跨多雲（4/5）+ Fortune 500 結構性 lock-in（3/5）三軸驅動、但 IP（3/5）落後 Synopsys / Cadence 等真賣水人 + 客戶分散（3/5）受 Fortune 500 集中拖累。

## ⭐ 跟 [[Databricks]] 路線分歧（行業關鍵戰局、#G1 2026-06-09 [[Databricks]] entity 落地後補強）

**兩家路線分歧 = 企業 AI platform 兩種範式 + 五軸 19/25 並列「企業數據雙頭」**：

| 維度 | Snowflake | [[Databricks]] |
|---|---|---|
| 起點範式 | SQL data warehouse | Spark Lakehouse |
| 結構化 vs 非結構化 | **結構化資料 + BI 優先** | **非結構化 + AI training 優先** |
| 主場客戶 | Fortune 500 金融 / 零售 / 製造（結構化資料豐富）| Fortune 500 科技 / 媒體 / 互聯網（非結構化 + AI 訓練多）|
| 治理 governance | Polaris Catalog + 30 年 BI lineage | **Unity Catalog + AI / ML 模型治理 + 多雲統一** |
| AI 整合 | Cortex AI + NVDA NeMo / NIM | **Mosaic AI + Hugging Face + 自研 Foundation Models DBRX 132B** |
| Lakehouse 路線 | Polaris Catalog（吃 Databricks 主場）| **Lakehouse 始祖 + Spark 主導** |
| 跨多雲覆蓋 | AWS 80%+ 主力 + Azure / GCP 第二 | **AWS + Azure + GCP + Oracle + Alibaba 五雲**（勝 SNOW 1 分）|
| 上市狀態 | 2020-09 上市 NYSE：SNOW | **⚠️ 私募 $62B 估值（2024-12 Series J）+ IPO 2026 H2-2027 H1** |
| 估值 / 規模 | $48-60B 市值（Forward PE 65-90x）| **$62B 私募估值（IPO 後可能 $80-120B、Forward PE 50-80x 預期）** |
| 客戶 RRR | ~126% | **~140%+（更激進、AI workload 用量爆炸）** |
| 商業模式 | 訂閱年金 + 用量計費 | 訂閱年金 + 用量計費（類似）|
| 戰略合作 | **AWS $60B 5 年合約** | **Microsoft Azure Databricks 17 年戰略合作 + Mosaic AI 整合** |
| 五軸（25 分制）| **19/25**（路線 4 + 站 4 + 耗 5 + IP 3 + 客 3）| **19/25**（路線 5 跨多雲 + 站 4 + 耗 5 + IP 3 + 客 2 私募集中）|

**結論**：**Snowflake 跟 Databricks 不是「一家贏」、是「雙頭分食 + 共生」**——Fortune 500 客戶必雙頭採用（Snowflake 跑 SQL BI + Databricks 跑 AI 訓練）。但 2026 趨勢匯流（Snowflake 擴 Lakehouse + Databricks 擴 SQL Warehouse）→ 雙頭可能「**互相蠶食 mature workload + 中間客戶開始選邊**」。**Databricks IPO 後 $80-120B 估值預期是 Snowflake 估值的反向 anchor**——若 Databricks 上市估值 $80-120B + Forward PE 50-80x → Snowflake 估值需要結構性 re-rate（PE 65-90x → 50-70x 收縮 -20 至 -30%）。

⭐ **五軸 19/25 並列差異化**（**#G1 2026-06-09 補位**）：
- **Snowflake 路線敏感 4 + 客戶分散 3**：AWS 80%+ 集中 + Fortune 500 90%+ AVL 結構性集中
- **Databricks 路線敏感 5 + 客戶分散 2**：跨多雲 5 家（**勝 SNOW 1 分**）+ 私募階段客戶數小 + Fortune 100 85%+ AVL 集中（**遜 SNOW 1 分**）
- → 兩家五軸總分相同、結構性分歧路線 = **「企業數據雙頭」並列 anchor**

## 跟其他 wiki 概念連結

- [[AI 利潤奇點（Token 經濟學拐點）]]：本 entity 是「**軟體商業模式升級**」第三軸代表（從「按人頭售賣」→「按工作量售賣」、TAM 從全球軟體預算→全球白領薪資池）
- [[Forward Deployed Engineer 戰略（FDE）]]：Snowflake 提供「企業 AI agent 可信執行環境」、FDE 提供 deployment、兩個 concept 互補
- [[賣水人選股邏輯（投資版）]]：「企業 AI 可信執行環境」賣水人、不押模型公司誰贏、押所有企業 AI agent 部署都需要的安全資料邊界
- [[控制點轉移（投資版）]]：拿到「Fortune 500 data lineage + 跨多雲 vendor neutral + Cortex AI agent 整合」三重 anchor
- [[Jevons Paradox（投資版）]]：Cortex AI 用量爆炸 → 客戶 RRR 結構性放大、不需要新合約即可放大營收
- [[資訊擴散四階段]]：IPO 後 +30-60% 12 月、機構持股普及階段 3-4
- [[市場四階段：懷疑／驗證／共識／反轉]]：narrative 從「驗證 → 共識」加速段（2024 H1 被威脅 → 2025-2026 narrative shift）
- [[FCF 拐點]]：Snowflake FCF margin 20%+ 結構性領先 SaaS 同業
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 強制格式
- [[Oracle]]：Oracle 走「Database 30 年護城河 + AI cloud growth bet」vs Snowflake 走「Data Cloud + 跨多雲 vendor neutral + Cortex AI」= 兩種企業 AI cloud 範式
- [[Microsoft]]：Microsoft Fabric + Power BI 直接競爭、但 Azure 是 Snowflake 第二大雲、合作 + 競爭並存
- [[AMZN]]：AWS $60B 五年合約 anchor（FY2025 Q4 公告）
- [[NVDA]]：Cortex AI + NeMo / NIM 整合、技術生態夥伴
- [[Anthropic]] / [[OpenAI]]：模型公司透過 Snowflake Marketplace + Cortex AI 觸及 Fortune 500 客戶
- [[Databricks]]（待建）：路線分歧 + 雙頭分食 anchor

## 相關連結

- [[AI 利潤奇點（Token 經濟學拐點）]]
- [[Forward Deployed Engineer 戰略（FDE）]]
- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[Jevons Paradox（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[Oracle]]、[[Microsoft]]、[[AMZN]]、[[NVDA]]
- [[Anthropic]]、[[OpenAI]]
- [[Accenture]]、[[Palantir]]、[[CoreWeave]]、[[Lambda]]、[[Nebius]]

## Source URLs

- Snowflake FY2025 Q4 Earnings Press Release（2026-02-26）: https://investors.snowflake.com/news/news-details/2026/Snowflake-Reports-Financial-Results-for-the-Fourth-Quarter-and-Fiscal-Year-2025/default.aspx
- AWS $60B 5-Year Agreement（2025-12 公告）: https://press.aboutamazon.com/aws/snowflake-60b-five-year-deal
- Snowflake Cortex AI Launch + Multi-cloud Strategy: https://www.snowflake.com/en/data-cloud/cortex/
- Sridhar Ramaswamy CEO 任命（2024-Q1）: https://www.snowflake.com/news/sridhar-ramaswamy-ceo/
- Snowflake Polaris Catalog (Apache Iceberg) Launch: https://www.snowflake.com/news/polaris-catalog/
- Snowflake vs Databricks 路線分歧（行業分析）: https://www.reuters.com/technology/snowflake-databricks-ai-platform-divergence/
- FOMO SOC KP #44 narrative shift（2026-05-30）: raw/2026-05-30_FOMOSOC-KP44-Tesla-SpaceX-Marvell-Snowflake-Dell-Anthropic.md
- Snowflake Wikipedia: https://en.wikipedia.org/wiki/Snowflake_Inc.

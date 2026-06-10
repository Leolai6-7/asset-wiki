---
title: Cerebras
aliases: [Cerebras Systems, CBRS, WSE-3, 晶圓級晶片廠]
type: entity
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-05-16
check_after: 2026-09-15
sources:
  - raw/2026-05-16_FOMOSOC-KP42-Cerebras上市WSE-3對NVDA啟示.md
evidence_url: https://www.fomosoc.com/p/cerebrasnvidia-kp42
tags: [標的, 美股, AI ASIC, 晶圓級晶片, WSE-3, OpenAI 客戶, TSMC 5nm 單一 fab, 推論 niche, IPO 2026-05, SRAM 推論架構]
thesis_dependency: AI-capex
confidence: high
---

# Cerebras（CBRS）

## 1. 一句話定位

**全球唯一晶圓級 AI 晶片廠 + OpenAI $200 億單一最大客戶 + TSMC 5nm 唯一晶圓代工 = 推論 niche 高純度期權**——2016 起源（Andrew Feldman / Gary Lauterbach / Michael James / Sean Lie / Jean-Philippe Fricker、Sunnyvale 加州、原 SeaMicro 創始人團隊）、產品 **WSE-3 晶圓級晶片**（4 兆電晶體 + 44 GB SRAM + 21 PB/s 記憶體頻寬 = NVDA H100 的 **2,600 倍**）、商業模式從「**賣推論系統**」（CS-3 整套）轉向「**雲端推論服務**」（與 AWS Bedrock 分銷整合）；**2026-05 IPO** 發行估值 $560 億、首日飆漲至 ~$1,000 億；FY2025 營收 $5.10 億（YoY +76%）+ 淨利 $2.37 億（翻黑為紅）+ Backlog $246 億；**vs NVDA / AMD / Groq 三大結構性差異**：(1) **晶圓級單晶片**（不用 Chiplet 整合、不用 HBM 外掛）、(2) **SRAM 取代 HBM**（44 GB 上限、高頻寬但容量受限）、(3) **TSMC 5nm 單一 fab**（不像 NVDA 雙頭策略）；**定位是「高吞吐量推論 niche 期權」**——不是 NVDA 殺手、訓練主場仍 NVDA、CUDA 護城河 + Chiplet 靈活性 + 多 fab 對沖；公司類型：**ASIC pure-play 期權**（推測五軸 19/25 等級、客戶集中度低分但 IP / 站別關鍵高分）。

## 2. 三層 thesis

### 產業層

- **AI 推論市場結構性分裂賽道**：[[市場四階段：懷疑／驗證／共識／反轉]]「**驗證 → 共識**」加速段——機構快速給「下一個 NVDA」估值溢價、首日 $560B → $1,000B 是訊號
  - 推論市場 2025 ~$15-20B、2030 ~$50-80B（推測、SemiAnalysis 估）
  - 推論細分為「**訓練模型推論**」（HBM 主導）+「**高吞吐量推論**」（SRAM 可介入）+「**邊緣推論**」（Apple A 系列 NPU + 行動端）
  - Cerebras 鎖在「高吞吐量推論」niche、跟 Groq LPU（低延遲）形成差異化
- **晶圓級晶片 vs Chiplet 架構之爭**：
  - **晶圓級**（WSE）：一片完整晶圓做巨晶片、頻寬極高、良率挑戰
  - **Chiplet + 先進封裝**（NVDA / AMD）：多小晶片整合、靈活性高、生態成熟
  - 未定論：晶圓級會否成為下一代架構流派？或被 Chiplet 蠶食？需追蹤 5-10 年
  - 詳見 [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]
- **SRAM 記憶體架構興起 vs HBM 主流**：
  - SRAM 44 GB 上限 = 推論場景限制
  - 但 21 PB/s 頻寬（NVDA 的 2,600 倍）= 高吞吐量推論優勢
  - **對 SK Hynix / Samsung / Micron HBM thesis 是長期反證候選**（推論市場可能部分流失）
  - 詳見 [[AI 記憶體結構性供給短缺]] 對沖反證段
- 賽道 timing：
  - [[資訊擴散四階段]] 階段 2-3（IPO 後機構持股普及、ARK 等基金大舉買入、首日漲幅 78%）
  - 2026-2027 是 Backlog $246 億兌現的關鍵窗口
  - **NVDA Rubin / Feynman 若優化推論性能** → Cerebras niche 收窄

### 目的層

- 業務 mix（FY2025）：
  - **CS-3 系統銷售 = ~80% 營收**（推測、含 WSE-3 晶片 + 系統機箱 + 互連）
  - **雲端推論服務 = ~15% 營收**（與 AWS Bedrock 整合、推論 API）
  - **政府 + 國防客戶 = ~5% 營收**（推測、含 Argonne / Lawrence Livermore）
- 客戶結構（**極度集中**）：
  - **OpenAI = 最大客戶**（**$200 億訂單**、佔 Backlog 81%）
  - **AWS Bedrock = 分銷通道**（推論 API 銷售合作）
  - **政府客戶**：Argonne National Lab / Lawrence Livermore / Mayo Clinic 等
  - **新增企業客戶**：少數 hyperscaler 試點（不公開）
  - **客戶分散度 = 1-2 分**（五軸最低分、嚴重風險）
- 商業模式 = **「賣系統 + 雲端推論 + 訂單預付」**：
  - 客戶簽 multi-year 大單 → Cerebras 拿訂單做 TSMC 5nm 預付 → 客戶部署 → recurring 推論流量
  - 單位經濟：系統毛利 40-50%（推測、含 TSMC wafer + 互連 + 系統工程）、雲端服務毛利 60%+
- → 連 [[賣水人選股邏輯（投資版）]]：**ASIC pure-play 期權分類**
  - 路線敏感度 4/5（押 SRAM 推論架構勝出、半 binary）
  - 站別關鍵度 5/5（高吞吐量推論 niche 唯一玩家）
  - 耗材 recurring 2/5（系統銷售為主、recurring 弱）
  - IP 控制 5/5（晶圓級設計 + 缺陷管理 IP 持有）
  - 客戶分散 1/5（OpenAI 81% 集中度）
  - **推測五軸總分 17-19/25**（屬中段期權型）

### 供應層

- 跟 [[TSMC]] 關係（**單一 fab 風險**）：
  - **TSMC 5nm 唯一晶圓代工**（沒有 Samsung / Intel 對沖）
  - **產能單點失效風險**：若 TSMC 5nm 產能緊張、Cerebras 交付能力受限
  - 對照 [[Bottleneck Theory（瓶頸論）]]：Cerebras 自身就是 Hormuz 海峽案例
- 跟 [[OpenAI]] 關係（**最大客戶 + 同盟結構**）：
  - **$200 億訂單**（Backlog 81%）
  - OpenAI 是 Cerebras 「**生死客戶**」——一旦 OpenAI 削減訂單 → 估值崩塌
  - OpenAI 同時跟 [[NVDA]] / [[Oracle]] / [[CoreWeave]] / [[AVGO]] 多重採購、Cerebras 是「推論 niche 補強」而非全棧依賴
- 跟 [[NVDA]] 關係（**競爭 + 互補**）：
  - 推論細分競爭：Cerebras 高吞吐量推論 niche vs NVDA 通用推論主場
  - **CUDA 護城河 + Chiplet 靈活性**：NVDA 結構性優勢不易動搖
  - Cerebras 只在 niche 勝出、不威脅 NVDA 整體市場
- 跟 [[AWS]] 關係（**雲端分銷通道**）：
  - AWS Bedrock 整合 Cerebras 推論 API
  - 對 AWS 是 multi-source 策略（GPU + Trainium + Cerebras）
  - 對 Cerebras 是分銷觸達 hyperscaler 客戶池
- 跟 [[SK Hynix]] / [[Samsung Electronics]] / [[Micron]] 關係（**HBM 對沖反證**）：
  - Cerebras 用 SRAM 取代 HBM、不直接採購記憶體三巨頭
  - 若 SRAM 推論架構擴張 → 三巨頭 HBM 推論收入長期受擠壓
  - 對沖反證 [[AI 記憶體結構性供給短缺]]
- 護城河：
  - **晶圓級設計 IP 持有**（缺陷管理 + 超小核心 + 智慧互連 = 工程突破）
  - **OpenAI $200 億訂單 anchor**（短期生死客戶、長期 reference customer 角色）
  - **AWS Bedrock 分銷通道**（hyperscaler 觸達）
  - **TSMC 5nm 首批產能 lock-in**（先進 fab 採購權）
- 風險：
  - **客戶集中極端**（OpenAI 81%、其他客戶 < 10%）
  - **TSMC 5nm 單一 fab**（產能單點失效）
  - **SRAM 44 GB 上限**（推論場景限制、無法擴展訓練）
  - **NVDA 推論競爭**（Rubin / Feynman 若優化推論 → niche 收窄）
  - **首日估值 $1,000 億 = 高估**（PS ~196x、PE ~422x）

## 3. 財務狀態快照（as_of: 2026-05-16）

### Re-rate 三角形

| 維度 | 現況 | 觸發 |
|---|---|---|
| **g（成長）** | FY2025 YoY +76%、Backlog $246 億（4.8 年覆蓋）| **OpenAI Backlog 兌現速度 + 新客戶簽約** |
| **r（折現率）** | 利率敏感（IPO 估值 PS ~196x）+ 客戶集中極端 | **十年美債 4.5%+ + 三十年破 5%** → 估值壓力 |
| **市場視角** | 「下一個 NVDA」溢價 + 機構共識看多 | **能否在訓練市場破局** → 決定通用 ASIC vs niche 期權 |

### 估值快照

| 指標 | 數字 |
|---|---|
| IPO 發行估值 | $560 億 |
| **首日估值** | **~$1,000 億** |
| **PS（TTM）** | **~196x**（$1,000B / $5.1B）|
| **PE（TTM）** | **~422x**（$1,000B / $2.37 億）|
| **EV / Backlog** | **~4.1x**（$1,000B / $246B）|

### 催化清單

| 催化 | 時點 | expires_on |
|---|---|---|
| Q3 2026 財報（首份）| 2026-08 | 2026-12-09 |
| WSE-4 揭示（推測）| 2027 H1 | 2027-06-09 |
| OpenAI 訂單環比兌現 | 每季 | 持續監控 |
| AWS Bedrock 推論流量 | 每季 | 持續監控 |
| TSMC 5nm 產能利用率 | 每季 | 持續監控 |

### 風險清單

| 風險 | expires_on |
|---|---|
| OpenAI 削減訂單 | 持續監控 |
| TSMC 5nm 產能瓶頸 | 持續監控 |
| NVDA Rubin / Feynman 優化推論性能 | 2027-12-09 |
| SRAM 44 GB 上限未突破 | 2027-12-09 |
| 首日估值 $1,000 億 = 高估反向 | 2026-12-09（半年內財報驗證）|

## 跟其他 wiki 概念連結

- [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]] — 本 entity 對應的 concept anchor
- [[AI 記憶體結構性供給短缺]] — SRAM 對沖反證
- [[賣水人選股邏輯（投資版）]] — ASIC pure-play 期權分類
- [[Bottleneck Theory（瓶頸論）]] — TSMC 5nm 單一 fab chokepoint
- [[控制點轉移（投資版）]] — SRAM 架構繞過 HBM 控制點
- [[市場四階段：懷疑／驗證／共識／反轉]] — IPO 首日「驗證 → 共識」訊號
- [[CapEx 見頂辯論]] — AI infra 第二曲線案例
- [[NVDA]]、[[TSMC]]、[[OpenAI]]、[[CoreWeave]]、[[SK Hynix]]、[[Samsung Electronics]]、[[Micron]]、[[AMD]]
- [[FOMO SOC]]（KP@FOMOSoc KOL 來源 / 待建）

## 相關連結

- [[FOMO SOC KP42]] — 本 entity 主要素材
- [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]
- [[NVDA]]、[[TSMC]]、[[OpenAI]]

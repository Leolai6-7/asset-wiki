---
title: FOMO SOC KP42 — Cerebras 上市 WSE-3 對 NVDA / 台積電 / 記憶體廠啟示
aliases: [KP42, KP 第 42 期, KP 42, Cerebras IPO, WSE-3, SRAM vs HBM 推論架構, neocloud 對比, CoreWeave Nebius, 美債殖利率]
type: summary
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-05-16
check_after: 2026-12-09
sources:
  - raw/2026-05-16_FOMOSOC-KP42-Cerebras上市WSE-3對NVDA啟示.md
evidence_url: https://www.fomosoc.com/p/cerebrasnvidia-kp42
tags: [FOMO SOC, KP 思考筆記, Cerebras, WSE-3, 晶圓級晶片, SRAM 推論架構, HBM, NVDA, 台積電, CoreWeave, Nebius, 美債殖利率, Hormuz 海峽, 通膨, 長端利率, ASIC pure-play 期權]
confidence: high
---

# FOMO SOC KP42 — Cerebras 上市 WSE-3 對 NVDA / 台積電 / 記憶體廠啟示

**作者**：KP@FOMOSoc
**發布**：2026-05-16
**來源**：[FOMO SOC 思考筆記第 42 期](https://www.fomosoc.com/p/cerebrasnvidia-kp42)
**性質**：全文公開、無付費牆

## 重點

> 三主題：
> 1. **美債長端**：十年 4.5%+、三十年 5%+（2007 來首次）→ Hormuz 海峽 + 油價 + 通膨難快速下行 → 成長股估值壓力
> 2. **Cerebras IPO**：WSE-3 晶圓級晶片 4 兆電晶體 + 44GB SRAM + 21 PB/s 頻寬（NVDA 的 **2,600 倍**）、首日估值 ~$1,000 億、但訓練主場仍 NVDA
> 3. **CoreWeave vs Nebius**：高槓桿 EBITDA 56% / 營益 1% vs 預售模式 EBITDA 45% / 較穩健 = neocloud 模式分歧

## Cerebras 關鍵數字

| 指標 | 數字 |
|---|---|
| 2025 營收 | **$5.10 億**（YoY +76%）|
| 2025 淨利 | $2.37 億（翻黑為紅）|
| **未來訂單 Backlog** | **$246 億** |
| IPO 估值 | $560 億 → 首日 ~$1,000 億 |
| WSE-3 電晶體 | **4 兆**（vs H100 800 億）|
| WSE-3 SRAM | **44 GB**（vs H100 60 MB）|
| WSE-3 記憶體頻寬 | **21 PB/s**（vs H100 8 TB/s、~2,600x）|
| WSE-3 功耗 | 23-25 kW |
| **OpenAI 訂單** | **$200 億**（最大客戶）|

## 工程突破（缺陷管理）

**三大設計創新**讓「製造缺陷從致命瑕疵變成可控 7% 性能開銷」：
1. **超小核心**（0.05 mm²）→ 缺陷影響範圍小
2. **97 萬核心冗餘設計**（造 100 萬保留 90 萬）
3. **智慧互連網路**

## 三大產業啟示

### 1. 記憶體架構分裂
- **SRAM**（Cerebras）= 高頻寬 niche、限 44 GB
- **HBM**（NVDA）= 訓練 + 大模型、大容量
- **長期影響**：HBM 訓練主場穩固、推論可能**部分轉向 SRAM** → **記憶體三巨頭（SK Hynix / Samsung / Micron）長期產品組合風險**

### 2. 晶圓級 vs Chiplet 架構之爭
- 晶圓級 WSE = 完整晶圓做一顆巨型晶片（Cerebras）
- Chiplet + 先進封裝 = 多小晶片整合（NVDA / AMD）
- 未定論：晶圓級會否成為下一代架構流派？或被 Chiplet 蠶食？

### 3. 融資 + 產能風險
- CoreWeave 高槓桿 → 利率上升 + 折舊壓力 = 利潤率陷阱
- Cerebras 依賴**台積電單一晶圓廠**（5nm）= 產能單點失效風險
- Nebius 預售模式 = 相對低風險、成長受限

## CoreWeave Q2 指引矛盾

| 指標 | 指引 | 市場預期 |
|---|---|---|
| Q2 營收 | $25.3 億 | **$26.9 億**（miss）|
| Q2 營業利潤 | $30-90M | **$154M**（miss）|

→ 市場開始質疑 CoreWeave 高槓桿擴張可持續性。

## 跟 wiki 概念的深度連結

### ⭐ 新概念落地：**[[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]** ⭐
- 晶圓級晶片 + SRAM 取代 HBM 推論架構 = 對 HBM thesis 的反證候選
- 對應 [[AI 記憶體結構性供給短缺]] 的對沖視角（SRAM 推論架構若擴張 → HBM 估值上限被裁切）
- 對應 [[控制點轉移（投資版）]]：架構層繞道 HBM 控制點

### 強化 [[AI 記憶體結構性供給短缺]]
- **新增「SRAM 推論架構對沖」段**：Cerebras WSE = HBM thesis 的反證候選
- → 三巨頭估值上限再打折扣（除了 [[中國半導體國產替代（投資對沖視角）]] 的 CXMT 對沖 8 折之外）

### 強化 [[賣水人選股邏輯（投資版）]]
- **Cerebras = ASIC pure-play 期權**（19/25 推測、客戶集中 OpenAI $200 億）
- 跟 [[Kioxia]] 19 / [[SanDisk]] 18 / [[GlobalWafers 6488]] 18 同等級

### 強化 [[Bottleneck Theory（瓶頸論）]]
- Cerebras = 台積電 5nm 單一供應商 chokepoint
- NVDA = 雙頭 fab 策略（TSMC + Samsung）對沖
- → 單點失效風險評估的具體案例

### 強化 [[CapEx 見頂辯論]]
- CoreWeave Q2 miss = neocloud 利潤率陷阱微觀證據
- 但 NVDA backlog 緩衝（CoreWeave $50B backlog 即使部分延後仍要採購）

### 強化 [[市場四階段：懷疑／驗證／共識／反轉]]
- Cerebras IPO 首日 $560B → $1,000B = **驗證→共識** 切換訊號
- 美債 4.5%+ + 三十年破 5% = **成長股估值反轉**前兆
- → KP 暗示 2026 H2 警惕

### 對接 [[效率→安全切換]]
- 長端利率上升 driver = Hormuz 海峽 + 油價 = **能源安全溢價**

### 對接 [[控制點轉移（投資版）]]
- Cerebras 用 SRAM 繞過 HBM 控制點 = **架構層繞道**
- 但仍受限 TSMC 晶圓代工 chokepoint

## 受影響 entity

- 待建 [[Cerebras]] entity — ASIC pure-play 期權、TSMC 5nm 單一 fab、OpenAI $200 億單一最大客戶、WSE-3 規格 anchor
- [[NVDA]] — 補強「Cerebras 是推論 niche 競爭者、訓練主場仍 NVDA、CUDA 護城河 + Chiplet 靈活性」
- [[TSMC]] — 補強「Cerebras 唯一晶圓代工 + 5nm 製程」
- [[CoreWeave]] — 補強「Q2 指引 miss + 利潤率陷阱訊號 + 客戶集中 Microsoft 60%+」
- 待建 [[Nebius]] entity — 預售模式 + EBITDA 45% + 較穩健的 neocloud 對照組
- [[SK Hynix]] / [[Samsung Electronics]] / [[Micron]] — 補強「SRAM 推論架構長期產品組合風險」

## 相關連結

- [[FOMO SOC]]（KOL 來源、待建 entity）
- [[Cerebras]]（本篇 ingest 新建 entity）
- [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]（本篇 ingest 新建 concept）
- [[AI 記憶體結構性供給短缺]]
- [[賣水人選股邏輯（投資版）]]
- [[Bottleneck Theory（瓶頸論）]]
- [[CapEx 見頂辯論]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[效率→安全切換]]
- [[控制點轉移（投資版）]]
- [[NVDA]]、[[TSMC]]、[[CoreWeave]]、[[SK Hynix]]、[[Samsung Electronics]]、[[Micron]]、[[OpenAI]]

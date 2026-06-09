---
title: 長端利率上升怎麼辦？Cerebras 上市對 Nvidia、台積電、記憶體廠有甚麼啟示？— KP 思考筆記第 42 期
author: KP@FOMOSoc
source: https://www.fomosoc.com/p/cerebrasnvidia-kp42
date: 2026-05-16
type: raw / KOL 產業文（全文公開、無付費牆）
標的: [Cerebras, NVIDIA, Groq, OpenAI, AWS, 台積電, 三星, SK海力士, CoreWeave, Nebius, AMD]
資料來源: Cerebras IPO 招股書 + Q1 2026 財報 + KP@FOMOSoc 整合
evidence_url: https://www.fomosoc.com/p/cerebrasnvidia-kp42
paywalled: 否（全文公開）
---

# 長端利率上升怎麼辦？Cerebras 上市對 Nvidia、台積電、記憶體廠有甚麼啟示？— KP 思考筆記第 42 期

**作者**：KP@FOMOSoc
**發布**：2026-05-16
**分類**：深入分析第 42 期 — 長端利率 + Cerebras IPO + neocloud 對比

## 核心 thesis

> 三主題互動：
> 1. **十年美債破 4.5%、三十年破 5%** → 反映 Hormuz 海峽地緣阻塞 + 油價高位 → 通膨難快速下行
> 2. **Cerebras 用 SRAM 取代 HBM 推論架構**，記憶體頻寬達 NVDA 的 **2,600 倍**、但受限 SRAM 容量、只是 niche
> 3. **CoreWeave vs Nebius**：前者高 EBITDA（56%）低營益率（1%、產能快速擴張壓縮）/ 後者 EBITDA 45% 但更穩健（預售模式）

---

## 主題一：美債殖利率上升

| 指標 | 數字 | 解讀 |
|---|---|---|
| 十年美債殖利率 | **4.5%+** | 反映通膨難快速下行 |
| 三十年美債殖利率 | **5%+**（2007 來首次）| 長端流動性溢價急升 |
| 4 月 PPI YoY | **+6%** | 製造端通膨重燃 |
| 4 月 PPI MoM | **+1.4%**（2022 來最強）| — |
| 4 月 CPI | **3.8%** | 通膨仍黏 |

**關鍵 driver**：Hormuz 海峽持續受阻 + 油價維持高位 → 通膨難快速下行 → 長端利率被迫上升 → **成長股估值壓力**。

---

## 主題二：Cerebras IPO

### 基本財務

| 指標 | 數字 |
|---|---|
| 2025 營收 | **$5.10 億**（YoY +76%）|
| 2024 淨損 | $4.8 億 |
| **2025 淨利** | $2.37 億（**翻黑為紅**）|
| **未來訂單（Backlog）** | **$246 億** |
| IPO 發行估值 | $560 億 |
| 首日飆漲至 | **~$1,000 億** |

### WSE-3 規格（晶圓級晶片）

| 指標 | Cerebras WSE-3 | NVIDIA H100 對比 |
|---|---|---|
| 電晶體 | **4 兆** | 800 億 |
| 運算核心 | **90 萬**（含 7% 冗餘）| ~16,000 |
| **晶片內 SRAM** | **44 GB** | 60 MB |
| **記憶體頻寬** | **21 PB/s** | 8 TB/s |
| 功耗 | 23-25 kW | 700W |

**頻寬比**：21 PB/s ÷ 8 TB/s = **~2,600 倍** ⭐

### 客戶 / 通路

| 客戶 / 通路 | 內容 |
|---|---|
| **OpenAI** | 最大客戶（**$200 億訂單**）|
| **AWS Bedrock** | Cerebras 系統的分銷通道 |
| **台積電** | **唯一晶圓代工廠**（5nm）|
| **三星 / SK 海力士** | HBM 但 Cerebras 用 SRAM 取代 |

### 工程突破：把製造缺陷變成可控

**三大設計創新**：
1. **超小核心**（0.05 mm²）→ 缺陷影響小
2. **97 萬核心冗餘設計**（造出 100 萬、保留 90 萬）
3. **智慧互連網路**

→ **製造缺陷從致命瑕疵變成可控的 7% 性能開銷**。

### 為什麼是 niche、不是 NVDA 殺手

| 角度 | 內容 |
|---|---|
| **SRAM 架構優勢** | 推論時延極低（書桌邊書架 vs 圖書館）|
| **SRAM 容量限制** | 44 GB 上限、只適合**特定推論場景** |
| **訓練主場仍 NVDA** | CUDA 生態 + Chiplet 靈活性 |
| **產能瓶頸** | 受限台積電單一晶圓廠 |
| **系統成本難攤** | 23-25 kW + 整套系統 |

→ Cerebras 「**高吞吐量推論**」勝過 Groq 等「低延遲」競品、但**訓練 + 通用推論主場仍 NVDA**。

---

## 主題三：CoreWeave vs Nebius 對比

### 商業模式差異

| 指標 | **CoreWeave** | **Nebius** |
|---|---|---|
| 模式 | **大規模產能擴張 + 高槓桿** | **產能預售 + 訂單驅動** |
| EBITDA 利潤率 | **56%** ⭐ | 45% |
| **營業利潤率** | **1%** ⚠️（Q4 6%、去年 17%）| 較穩健 |
| 折舊 + 利息 | **壓力大** | 較小 |
| 客戶集中 | Microsoft 60%+ | 較分散 |

### CoreWeave Q2 指引矛盾

| 指標 | 指引 | 市場預期 |
|---|---|---|
| Q2 營收 | $25.3 億 | **$26.9 億**（miss）|
| Q2 營業利潤 | $30-90M | **$154M**（miss）|

→ **市場開始質疑 CoreWeave 高槓桿擴張的可持續性**。

### 對 NVDA 的傳導意義

- CoreWeave / Nebius 都是 NVDA GPU 大買家
- CoreWeave 利潤率陷阱 = **neocloud 整體營運壓力訊號**
- 但 NVDA 仍享 backlog 緩衝（CoreWeave $50B backlog 即使部分延後仍要採購）

---

## ⭐ 三大產業啟示

### 1. 記憶體架構轉變

| 架構 | 推論場景 | 容量 |
|---|---|---|
| **SRAM**（Cerebras）| 高頻寬 niche | 限 44 GB |
| **HBM**（NVDA）| 訓練 + 大模型 | 大容量 |

**長期影響**：HBM 需求在訓練 / 超大模型中**持續穩固**、但推論市場可能**部分轉向 SRAM 密集型** → **記憶體廠（SK Hynix / 三星 / Micron）長期存在產品組合風險**。

### 2. 晶圓級設計 vs Chiplet + 先進封裝

- 晶圓級（Cerebras WSE）= 一片完整晶圓做一顆巨型晶片
- Chiplet（NVDA / AMD）= 多顆小晶片透過先進封裝整合
- 是「下一代架構流派」競爭 / 還是 Cerebras 終將被 Chiplet 蠶食？**未定論**

### 3. 融資 + 產能風險

- CoreWeave 高槓桿 → 利率上升 + 折舊壓力 = 利潤率陷阱
- Cerebras 依賴單一晶圓廠（台積電）= **產能單點失效風險**
- Nebius 預售模式 = 相對低風險、但成長速度受限

---

## 跟既有 wiki 連結

### 強化 [[賣水人選股邏輯（投資版）]]
- **Cerebras 補位「ASIC pure-play 期權」分類**——跟 NVDA 通用 GPU 賽道分離
- 客戶集中 OpenAI $200 億 = 客戶分散度低、屬「期權型」

### 強化 [[AI 記憶體結構性供給短缺]]
- Cerebras SRAM 架構 = **HBM thesis 的反證候選**——若 SRAM 在推論市場擴張 → SK Hynix / 三星 / Micron 估值上限被裁切
- 對應 [[HBM iPhone moment]]

### 強化 [[Bottleneck Theory（瓶頸論）]]
- Cerebras = **台積電單一供應商 chokepoint**（5nm 晶圓代工）
- 對比 NVDA 雙頭 fab 策略（TSMC + Samsung）

### 對接 [[CapEx 見頂辯論]]
- CoreWeave Q2 miss = neocloud 利潤率陷阱訊號 = CapEx 見頂辯論的微觀證據

### 對接 [[控制點轉移（投資版）]]
- Cerebras 用 SRAM 繞過 HBM 控制點 = **架構層繞道**（如同 NVDA 用 InfiniBand 繞過 ASIC 標準化）
- 但仍受限晶圓代工 chokepoint（TSMC）

### 對接 [[市場四階段：懷疑／驗證／共識／反轉]]
- Cerebras IPO 首日 $560B → $1,000B = **驗證→共識** 切換的訊號
- 美債 4.5%+ + 三十年破 5% = **成長股估值反轉**前兆
- → KP 暗示 2026 H2 需警惕

### 對接 [[效率→安全切換]]
- 長端利率上升的 driver = Hormuz 海峽 + 油價 = **能源安全溢價**

### 新 wiki 角色：[[Cerebras]] entity 待建
- Type: ASIC pure-play 期權
- 主要客戶：OpenAI $200B
- 主要 fab：TSMC 5nm
- 產品：WSE-3 晶圓級 4 兆電晶體 90 萬核心 44GB SRAM
- 估值首日 $1,000B

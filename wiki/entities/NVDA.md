---
title: NVDA
aliases: [Nvidia, 輝達, NVIDIA]
type: entity
created: 2026-06-04
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-09-15
sources:
  - raw/美股送分題-06-備忘錄1-CSP-AI通縮-2026-03-09.md
  - raw/美股送分題-09-備忘錄2-HBM-Meta-私募-2026-03-16.md
  - raw/美股送分題-notes-市場解碼與估值筆記-2026-02至04.md
  - raw/2026-05-02_FOMOSOC-KP40-五大巨頭Q1財報AI變現分歧.md
  - raw/2026-05-16_FOMOSOC-KP42-Cerebras上市WSE-3對NVDA啟示.md
  - raw/2026-05-30_FOMOSOC-KP44-Tesla-SpaceX-Marvell-Snowflake-Dell-Anthropic.md
  - raw/2026-06-06_FOMOSOC-KP45-AI-PC-RTX-Spark-Windows-CUDA-Intel-Alphabet-Microsoft-Build.md
tags: [標的, 美股, AI, 半導體, GPU, M7, CUDA, Chiplet, 訓練主場, Google TPU 競爭, Cerebras niche 競爭, RTX Spark, Vera Rubin, AI PC, 水電公司, 三層記憶體架構]
thesis_dependency: AI-capex
confidence: medium
---

# NVDA

AI GPU 龍頭，M7 之一。從賣晶片的硬體公司轉型為平台公司（CUDA + TensorRT）。

## 估值定位（宋分 2026 Q1 觀察）

- **M7 裡「第一名便宜的」**（Note #4）
- **PEG = 0.37**（Note #10）— 不代表便宜，市場把它**當循環股而非成長股**
- **38% 盈利成長但股價持平**（備忘錄 #1）— 市場已提前定價，符合預期 = 沒有新資訊
- **赤字是「時間」**（Note #10）— 需要把需求可見度延伸到 2027 以後

## 催化劑追蹤（Note #4）

- **Groq 收購** → 擴展推理能力
- **CFO 暗示 $500B 訂單仍保守**（華爾街只估 $330B）
- **H200 中國需求未入模型**
- **回購價 $183**

## 風險

- **Rubin 架構延遲**（Note #4）
- **Hyperscaler 預付 HBM 訂單到 2028**（備忘錄 #1）
  - 暗示 CapEx 不會短期見頂
  - 但對「[[FCF 拐點]] 即將到來」的多方期待是挑戰

## 護城河

- **平台轉型**：從賣晶片 → 建生態（CUDA、TensorRT）
- **推理市場定位**：Note #8 提到 AI 競爭優勢從「算力」轉向「可預測延遲」，NVDA 用平台路徑回應

## 跟既有 concept 的關係

- 用 [[Forward PE 估值法]]、[[PEG Ratio 警告]] 解讀股價持平
- 是 [[CapEx 見頂辯論]] 的核心受惠 / 受害者
- [[HBM iPhone moment]] 直接影響 Rubin ramp 速度
- [[AI 受惠路徑：集中→擴散]] 中 NVDA 是「集中」的代表

## ⭐ Cerebras WSE 推論競爭格局（2026-05-16 KP42）

→ 完整 framework 見 [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]

### 推論市場分裂結構

| 場景 | 主導 |
|---|---|
| **訓練 + 大模型** | **NVDA 主場**（CUDA + HBM + Chiplet 靈活性）|
| **高吞吐量推論 niche** | [[Cerebras]] WSE-3（44 GB SRAM + 21 PB/s 頻寬 = NVDA 2,600x）|
| **低延遲推論 niche** | Groq LPU |
| **邊緣推論** | Apple A 系列 NPU |

### NVDA 護城河仍穩固

- **CUDA 生態 + Chiplet 靈活性**（vs Cerebras 晶圓級單晶片）
- **多 fab 策略**（TSMC + Samsung vs Cerebras TSMC 5nm 單一）
- **訓練 + 通用推論主場**不易被動搖

## ⭐ Google TPU 2027 對外銷售（2026-05-02 KP40）

→ 完整 framework 見 [[AI 變現能見度分歧（證明給我看階段）]]

### hyperscaler 自研晶片擠壓

- **Google TPU 對外銷售**（2027 戰略升級、貢獻「有意義」營收）
- **AWS Trainium / Graviton** $200 億年化（YoY 三位數）
- **Microsoft MAIA**（仍在內部試點）
- → hyperscaler 把控制點上移到「晶片」、跟 NVDA 直接競爭

### NVDA 應對策略

- **NVDA $6.3B [[CoreWeave]] backstop** = neocloud 同盟結構
- **Spectrum-X + Quantum-X + NVLink Fusion** = 全棧鎖定
- **CUDA 護城河** = 開發者生態 lock-in

## ⭐ NVDA RTX Spark AI PC + Vera Rubin 三層記憶體 + 「水電公司」隱喻（2026-06-09 KP45 補強）

→ 完整 framework 見 [[FOMO SOC KP #45 — AI PC + Windows × CUDA + Intel Xeon orchestration + Alphabet 史上最大融資 + Microsoft Build 2026 + 三層記憶體架構]]

### KP45「水電公司」隱喻 — 控制點轉移到 utilities provider 等級

> 「**NVIDIA 變成了所有租客都必須打交道的水電公司**」

- **隱喻位階**：從「賣 GPU 的公司」→「整個 AI 生態的 utilities provider」→ 終端使用者（Apple / Microsoft / OpenAI / Anthropic / hyperscaler / 企業 / 消費者）**全部繞不過 NVDA 任一層**
- 對接 [[控制點轉移（投資版）]]：控制點從晶片 → 平台 → utilities provider 三層升級
- 對接 [[賣水人選股邏輯（投資版）]]：NVDA 已從「賣水人之一」→「**所有賣水人都依賴的水電公司**」（架構級 anchor）
- 跟 [[Apple]] Edge AI infra anchor 結構性對沖：兩家共同 reshape AI 生態的「平台 + utilities」位階

### RTX Spark AI PC 平台（KP45 五軌混戰之一）

**N1 / N1X 晶片**（premium AI notebooks、ARM 架構）：
- **Microsoft 深度技術整合**（超越傳統模組化）= CUDA 作為 Windows 系統的 de facto compute layer
- **CUDA 生態擴展到消費 PC** = 戰略「**特洛伊木馬**」（從資料中心 → AI PC 跨界）
- OEM partners：[[Dell]] / Lenovo / ASUS / MSI / HP / Microsoft Surface 六家共同 OEM

**AI PC 五軌混戰**：
| 軌 | 公司 | 路線 |
|---|---|---|
| 1 | **NVDA RTX Spark N1/N1X** | ARM 架構 + CUDA on Windows + premium |
| 2 | [[Intel]] Xeon AI PC | x86 + Xeon orchestration layer + 18A |
| 3 | [[Apple]] M-series | Apple Silicon + macOS + unified memory |
| 4 | Qualcomm Snapdragon X Elite | ARM + Windows + Copilot+ PC |
| 5 | AMD Strix Halo | x86 + Radeon AI + 軟體生態落後 NVDA |

→ NVDA RTX Spark = AI PC「**CUDA 路線**」純度型 OEM anchor、Dell 是純 NVDA OEM partner（vs Lenovo / HP 雙軌）

### Vera Rubin 三層記憶體架構（KP45 + KP44 補強）

| Tier | 角色 | 元件 | 受惠廠商 |
|---|---|---|---|
| **Hot** | GPU on-package | **HBM4** | [[SK Hynix]] 60-70% + [[Samsung Electronics]] 25-30% + [[Micron]] 10-20% |
| **Warm** | CPU side | **LPDDR5X** | Samsung + SK Hynix + Micron 三家分食 |
| **Cold** | Storage | **SSD（NAND）** | [[Kioxia]] / [[SanDisk]] / [[Samsung Electronics]] / [[Micron]] / Solidigm 5 家分食 |

⭐ **Vera Rubin NVL72 LPDDR5X 配置減少 ~50%**（KP45 細節）：
- **戰術決策**：優先快速量產 vs 規格極致
- 供應鏈瓶頸緩解、單櫃 TCO 降低 **USD $800k**
- = NVDA 用「規格降配 + 快速量產」trade-off 對沖 HBM 結構性短缺 + LPDDR5X 採購壓力
- 但「總 bit 消耗仍強勁」（unit volumes 增加、非需求毀滅）→ Samsung / SK Hynix / Micron 三家受惠不變

⭐ **跟 ICMS 1,152TB/rack 連結**：NVDA Vera Rubin SSD（NAND）BOM = 三層記憶體完整鏈條
- 對接 [[AI infra 3D NAND 戰場]] + [[AI 記憶體結構性供給短缺]] thesis

### Marvell narrative shift（KP44 補強 — 對 NVDA 影響）

→ 完整 framework 見 [[Marvell]] entity

**過去敘事（錯誤）**：Marvell = 「第二名 ASIC 公司」、跟 [[AVGO]] 競爭 custom silicon

**新敘事**：
- **Interconnect（光網路）成 Marvell 資料中心最大 segment、YoY +70%**
- 區分「**computing（ASIC / Custom）**」vs「**connecting（Interconnect）**」
- 光互連 = AI cluster 真正瓶頸（GPU 間資料傳輸）
- **Marvell 光 DSP 市占 ~60%** → distinct dominance

**對 NVDA 影響**：
- NVDA NVLink + Spectrum-X + Quantum-X = NVDA 自家 networking 直接競爭 Marvell
- 但 NVDA 鏈條（[[Dell]] PowerEdge + [[CoreWeave]] + hyperscaler）廣泛採購 Marvell 光 DSP
- = **Marvell 是 NVDA 鏈條間接受惠者**（vs 直接競爭）= 不影響 NVDA 主場 thesis
- NVDA 收購戰略：Celestial AI / XConn / Polariton 整合「scale-out + scale-up + scale-across」全棧

### NVDA 五軸是否重評（2026-06-09 校準）

**結論**：NVDA 仍維持 21-22/25 推估、**RTX Spark + Vera Rubin + 水電公司隱喻不改變五軸定位**
- 路線敏感（逆向）：**5**（不押任何單一賽道、訓練 + 推理 + AI PC + 自駕 + Edge AI 全棧覆蓋）
- 站別關鍵：**5**（必經之路、所有 AI 算力都繞不過）
- 耗材 recurring：**4**（CUDA 生態 + 開發者 lock-in、但 GPU 仍是一次性硬體扣 1 分）
- IP：**5**（CUDA + Chiplet + Spectrum-X / Quantum-X + NVLink + 整廠 platform）
- 客戶分散：**3**（hyperscaler 5 家 + neocloud + Apple / Microsoft / Google + Anthropic / OpenAI 多元、但 hyperscaler 4 家集中度 60%+ 扣 2 分）

**總分：22/25** ⭐ → 跟 [[Apple]] 22 / [[Cadence]] 22 / [[Eaton]] 22 / [[Schneider Electric]] 22 / [[Hitachi]] 22 同分但「**AI infra 算力 chokepoint 純度最高**」（vs Apple Edge AI / Eaton 電力 / Cadence EDA / 等不同戰場）

## 相關連結

- [[宋分（美股送分題）]]
- [[Forward PE 估值法]]
- [[PEG Ratio 警告]]
- [[FCF 拐點]]
- [[CapEx 見頂辯論]]
- [[HBM iPhone moment]]
- [[AI 變現能見度分歧（證明給我看階段）]]（KP40）
- [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]（KP42）
- [[Cerebras]]、[[CoreWeave]]、[[Oracle]]、[[Google]]、[[Microsoft]]、[[AMZN|Amazon]]、[[Apple]]
- [[AVGO]]、[[AMD]]、[[Intel]]、[[TSMC]]
- [[Dell]]（RTX Spark OEM partner + Rubin first wave + Spectrum-X 三軌 lock-in）
- [[ARM]]（NVDA Grace + RTX Spark N1/N1X 全 ARM Neoverse 架構）
- [[Marvell]]（光 DSP 60% 市佔、NVDA 鏈條間接受惠）
- [[SK Hynix]]、[[Samsung Electronics]]、[[Micron]]、[[Kioxia]]、[[SanDisk]]（Vera Rubin 三層記憶體受惠廠商）
- [[賣水人選股邏輯（投資版）]]：NVDA 「水電公司」隱喻 = 從「賣水人之一」→「所有賣水人都依賴的水電公司」架構級 anchor
- [[控制點轉移（投資版）]]：控制點從晶片 → 平台 → utilities provider 三層升級
- [[AI infra CapEx 三階段論]]：NVDA 跨越三階段、全鏈受惠
- [[6 戰場交集圖譜]]：NVDA 跨「算力 + AI PC + 1.6T 採購 + 三層記憶體」多戰場 anchor
- [[FOMO SOC]]（KP@FOMOSoc KOL 來源、待建）
- [[公司 Entity 模板（Step 1-3 三段式）]]

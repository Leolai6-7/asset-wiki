---
title: NVDA
aliases: [Nvidia, 輝達, NVIDIA]
type: entity
created: 2026-06-04
updated: 2026-06-09
sources:
  - raw/美股送分題-06-備忘錄1-CSP-AI通縮-2026-03-09.md
  - raw/美股送分題-09-備忘錄2-HBM-Meta-私募-2026-03-16.md
  - raw/美股送分題-notes-市場解碼與估值筆記-2026-02至04.md
  - raw/2026-05-02_FOMOSOC-KP40-五大巨頭Q1財報AI變現分歧.md
  - raw/2026-05-16_FOMOSOC-KP42-Cerebras上市WSE-3對NVDA啟示.md
tags: [標的, 美股, AI, 半導體, GPU, M7, CUDA, Chiplet, 訓練主場, Google TPU 競爭, Cerebras niche 競爭]
confidence: high
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

## 相關連結

- [[宋分（美股送分題）]]
- [[Forward PE 估值法]]
- [[PEG Ratio 警告]]
- [[FCF 拐點]]
- [[CapEx 見頂辯論]]
- [[HBM iPhone moment]]
- [[AI 變現能見度分歧（證明給我看階段）]]（KP40）
- [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]（KP42）
- [[Cerebras]]、[[CoreWeave]]、[[Oracle]]、[[Google]]、[[Microsoft]]、[[Amazon]]
- [[AVGO]]、[[AMD]]、[[Intel]]、[[TSMC]]
- [[FOMO SOC]]（KP@FOMOSoc KOL 來源、待建）

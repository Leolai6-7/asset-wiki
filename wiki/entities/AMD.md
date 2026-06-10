---
title: AMD
aliases: [AMD, Advanced Micro Devices]
type: entity
created: 2026-06-04
as_of: 2026-06-04
check_after: 2027-01-15
updated: 2026-06-09
sources:
  - raw/美股送分題-notes-市場解碼與估值筆記-2026-02至04.md
  - raw/2026-05-09_FOMOSOC-KP41-AI利潤奇點CPU復興FDE.md
tags: [標的, 美股, AI, 半導體, GPU, CPU, EPYC, 伺服器 CPU, Meta, 2030 市場翻倍]
thesis_dependency: AI-capex
confidence: medium
---

# AMD

NVDA 之外的第二大 GPU 玩家。MI300X 系列在 hyperscaler 推理市場逐步累積份額。**2026-05 FOMO SOC KP41 補位**——AMD 伺服器 CPU 進入 AI 驅動結構性復興期。

## 估值定位（Note #5）

**2026-02-05 單日跌 17%**

- Forward PE：34x → 30x（今年）
- Forward PE：22x → 19x（明年）
- 估值溫度計：**偏左（偏便宜）**

## 內部訊號

- **過去三個月公司沒回購**
- 上次回購價 **$154**
- 回購暫停 = 公司管理層**對當前價位無信心**訊號（但要小心也可能是其他原因）

## Meta 6GW 交易實戰估算（Note #12）

宋分用 AMD × Meta 6GW 案例展示**新聞→EPS 估算流程**：

```
新聞:    6GW 訂單（5 年）
營收:    1GW ≈ $17.5B AMD 營收 → 6GW = $105B
淨利:    $56.7B × 23.5% margin = $13.3B
稀釋:    AMD 發行 3.2 億 warrants → 股數 16.3 → 16.8 億
EPS:     2026 $7.90 vs 共識 $6.65
        2027 $11.76（成長率 89% → 49%，PE 自然壓縮）
```

## 跟既有 concept 的關係

- 跌 17% 後落入 [[Forward PE 估值法]] 「偏便宜」區
- 估值跌 + 回購暫停 = [[散戶 vs 機構買股差異]] 中需要警惕的訊號衝突
- 2027 PE 自然壓縮 = [[PE 壓縮公式]] 的 g 下降案例

## 風險

- Meta warrants 稀釋是真實成本
- TPU/ASIC 持續搶 GPU 推理份額
- NVDA Rubin ramp 後可能擴大優勢

## ⭐ Q1 2026 財報 — 伺服器 CPU 結構性復興（2026-05-09 KP41）

→ 完整 framework 見 [[AI 利潤奇點（Token 經濟學拐點）]]

### CPU 復興量化錨點

| 指標 | 數字 |
|---|---|
| 資料中心營收 YoY | **+57%** |
| 伺服器 CPU 連續創紀錄季度 | **4 季** |
| **2030 伺服器 CPU 市場預測** | **$600 億 → $1,200 億**（**翻倍**）|
| **2030 CAGR** | **35%** |
| **Q2 指引伺服器 CPU YoY** | **+70%+** |
| 強勁延續至 | **2027** |

### x86 vs ARM 結構性分工

- **x86（AMD / Intel）** = 現存生態系遷移強項
- **ARM** = 雲端原生新應用強項
- → **近期矛盾統一於「供不應求」——產能全開仍不夠**

### 跟 [[Intel]] / [[ARM]] 三家共同驗證

- AMD 數據中心 +57% + Intel Xeon 供不應求 + ARM 資料中心版稅 +100%+
- = AI 驅動 CPU 結構性復興、不是零和競爭

## 相關連結

- [[宋分（美股送分題）]]
- [[Forward PE 估值法]]
- [[PE 壓縮公式]]
- [[AI 利潤奇點（Token 經濟學拐點）]]（KP41 framework）
- [[AI infra CapEx 三階段論]]
- [[Jevons Paradox（投資版）]]
- [[Meta]]、[[NVDA]]、[[AVGO]]、[[Intel]]
- [[FOMO SOC]]（KP@FOMOSoc KOL 來源、待建）

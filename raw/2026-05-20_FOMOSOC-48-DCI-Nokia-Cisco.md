---
source: FOMO SOC（KP@FOMOSoc）
url: https://www.fomosoc.com/p/dci-48nokiacisco
date: 2026-05-20
title: 被遺忘的巨人重返巔峰？跨資料中心互連（DCI）成下一重點？— 深入分析第 48 期：Nokia + Cisco
fetched_by: WebFetch
fetched_on: 2026-06-09
paywall: 約 30% — Cisco 具體分析（DCI 產品線、市佔、Forward PE、與 Nokia 對標）擋住、Nokia 可見約 70%
---

# FOMO SOC 第 48 期 — DCI + Nokia + Cisco（KP@FOMOSoc）

## 一句話 thesis

> Scale-Across 網路基礎設施成為 AI 算力時代的**新瓶頸**——Nokia 與 Cisco 因其電信 / 網路遺產突然成為**被動的受惠者**。

## 核心論點

### DCI 新生 — 單一 DC 無法容納百萬 GPU

需要跨 DC 互連形成「**超級電腦**」、催生 AI 網路三層架構：

| 層 | 範圍 | 廠商主場 |
|---|---|---|
| Scale-up | 機架內 GPU 互連 | NVDA NVLink |
| Scale-out | 機房內互連 | AVGO / Marvell ASIC |
| **Scale-across** ⭐ | 資料中心間互連 | **CIEN / Nokia / Cisco（新戰場）** |

AI 訓練流量「**牽一髮而動全身**」、對延遲 / 無損傳輸要求遠超人類流量。

## Nokia 故事線（完整可見）

### 失落年代背景

| 年 | 事件 |
|---|---|
| 2007 | 手機帝國高峰、市值 **$150B** |
| 2011 | 「燃燒的平台」信件、轉 Windows Phone 失敗 |
| 2014 | 手機業務售予 Microsoft（**$7.2B**） |
| 2016 | 併購 Alcatel-Lucent（**$16.6B**）但 5G ROI 低迷 |
| 2023 | 股價困頓於 €3-4 |

### 三張牌轉折（2024-2025）

**第一張牌：Infinera 併購（2024、$2.3B）**
- 取得直連 hyperscaler 的光纖 DCI 技術
- 客戶從電信營運商轉向 Google / Meta / Microsoft

**第二張牌：NVDA 戰略投資（2025、$1B）**
- AI-RAN 概念：GPU 直入基地台
- 電信資產獲第二變現路徑
- **2026 商業試點、2027 商用版本**

**第三張牌：資料中心交換器 7220 IXR-H6**
- **102.4 Tb/s 吞吐量**、符合 Ultra Ethernet 規範
- 直接對標 **Cisco / Arista**
- **FY2026 Network Infrastructure 成長指引調升至 12-14%**（原 6-8%）

### Nokia 定位

> KP：「**被動式轉型**——時代找上門、而非主動出擊」

## Cisco 部分（付費牆前內容）

### 背景

- **2000 年 3 月**短暫成為全球市值第一公司（**$550B 盤中估值**、3 月 27 日）
- **衰退根源**：企業向雲端遷移、客戶結構從「**萬家企業 IT 部門**」→「**少數 hyperscaler**」

### 三股威脅開頭（可見部分）

- 雲端巨頭採購邏輯截然不同：**要求低價、開放、大量**

> **被遮蔽**：具體 DCI 佈局、產品線對標、市佔數據、Forward PE 均不可見

## 數據 anchor

| 指標 | 數值 |
|---|---|
| Nokia 手機巔峰市值 | **$150B**（2007）|
| Cisco 全球市值第一日 | **2000-03-27** |
| Cisco 盤中估值（當日）| **$550B** |
| Infinera 併購價 | **$2.3B**（2024）|
| NVDA 入股 Nokia | **$1B**（2025）|
| Nokia FY2026 NI 成長指引 | **12-14%** |
| 7220 IXR-H6 吞吐量 | **102.4 Tb/s** |

## 隱含對手陣營

- **Arista Networks**（資料中心交換器直接對手）
- **Ciena**（暗示對比對象、未深展）
- Lumentum / Coherent / Marvell（推測光元件供應商、未詳述）

## 風險 / 自警惕（隱含）

1. **AI-RAN 仍在概念階段** — 電信採購遠慢於雲端（2027 商用才算開始）
2. **Nokia 轉型非戰略先見** — 更多是被動搭上 AI 浪潮
3. **付費牆設計** — Cisco 核心分析隱藏、無法完整判斷雙頭論證強度

## KP 隱含立場推測

- **Nokia 為主推**（完整故事曝光、三張牌敘事完整）
- **Cisco 為對沖 / 陪襯**（故事被截斷、未呈現具體競爭力）
- Nokia「邊緣玩家反轉」敘事力更強

## 付費牆狀態

- 可見：~70%（Nokia 完整 + DCI 概念 + 三層架構 + Cisco 背景）
- 擋住：Cisco DCI 具體 thesis + 三股威脅深展 + 對標 Nokia + 估值

## 與 wiki 既有概念連結 hints

- [[Hyper Rail / Multi-Rail（光通訊整合技術）]] 直接強化（Nokia Multi-Rail + Cisco 暫無 entity）
- [[Nokia]] entity 18/25 既有（FY2026 NI 12-14% 指引 + NVDA $1B 投資 + Infinera $2.3B 已涵蓋、可補強 AI-RAN 時程）
- [[Ciena]] entity 19/25 既有（Scale-across 純度王）
- [[CPO 供應鏈圖譜]] / [[NVDA 網路 stack map]] 強化第三層

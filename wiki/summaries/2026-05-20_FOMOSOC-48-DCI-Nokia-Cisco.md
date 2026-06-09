---
title: FOMO SOC #48 — DCI + Nokia + Cisco（Scale-Across 新瓶頸 + Nokia 三張牌）
type: summary
created: 2026-06-09
updated: 2026-06-09
sources:
  - raw/2026-05-20_FOMOSOC-48-DCI-Nokia-Cisco.md
evidence_url: https://www.fomosoc.com/p/dci-48nokiacisco
tags: [DCI, Scale-Across, Nokia, Cisco, NVDA AI-RAN, Infinera, 7220 IXR-H6, Arista, Hyper Rail, Multi-Rail, 被動受惠者]
confidence: high
---

# FOMO SOC #48 — DCI + Nokia + Cisco（KP@FOMOSoc 2026-05-20）

## 一句話

> **Scale-Across 網路基礎設施成為 AI 算力時代的新瓶頸**——Nokia 與 Cisco 因其電信 / 網路遺產突然成為**被動的受惠者**；Nokia 三張牌（Infinera + NVDA + 7220 IXR-H6）完整曝光、Cisco 具體 DCI thesis 擋付費牆。

## 核心 thesis

### AI 網路三層架構（強化 [[Hyper Rail Multi-Rail（光通訊整合技術）]]）

| 層 | 範圍 | 廠商主場 |
|---|---|---|
| Scale-up | 機架內 GPU 互連 | NVDA NVLink |
| Scale-out | 機房內互連 | AVGO / Marvell ASIC |
| **Scale-across** ⭐ | **資料中心間互連（新戰場）** | **[[Ciena]] / [[Nokia]] / Cisco** |

> 單一資料中心無法容納百萬 GPU、需跨 DC 互連形成「**超級電腦**」；AI 訓練流量**牽一髮而動全身**、對延遲 / 無損傳輸要求遠超人類流量。

## Nokia 三張牌（完整可見 ~70%）

### 失落年代背景

| 年 | 事件 | 數字 |
|---|---|---|
| 2007 | 手機帝國高峰 | 市值 **$150B** |
| 2011 | 「燃燒的平台」信件、轉 Windows Phone 失敗 | - |
| 2014 | 手機業務售予 Microsoft | **$7.2B** |
| 2016 | 併購 Alcatel-Lucent | **$16.6B** |
| 2023 | 股價困頓 | €3-4 |

### 三張牌

**第一張牌：Infinera 併購（2024、$2.3B）**
- 取得直連 hyperscaler 的光纖 DCI 技術
- 客戶從電信營運商 → Google / Meta / Microsoft

**第二張牌：NVDA 戰略投資（2025、$1B）**
- AI-RAN 概念：GPU 直入基地台
- 電信資產獲第二變現路徑
- **2026 商業試點、2027 商用版本**

**第三張牌：7220 IXR-H6 資料中心交換器**
- **102.4 Tb/s 吞吐量** + Ultra Ethernet 規範
- 直接對標 Cisco / **Arista**
- **FY2026 Network Infrastructure 成長指引調升至 12-14%**（原 6-8%）

### Nokia 定位

> KP：**「被動式轉型」**——時代找上門、而非主動出擊

## Cisco 部分（付費牆前內容 ~30%）

### 背景

- **2000-03-27** 短暫成為全球市值第一公司（盤中 **$550B**）
- **衰退根源**：企業向雲端遷移、客戶結構從「萬家企業 IT 部門」→「少數 hyperscaler」

### 三股威脅開頭（可見）

- 雲端巨頭採購邏輯：**低價、開放、大量**

### 擋付費牆

- Cisco 具體 DCI 佈局 + 產品線對標 + 市佔 + Forward PE + 與 Nokia 完整對標

## 數據 anchor 整理

| 指標 | 數值 |
|---|---|
| Nokia 手機巔峰市值 | **$150B**（2007）|
| Cisco 全球市值第一 | **2000-03-27**（盤中 $550B）|
| Infinera 併購價 | **$2.3B**（2024）|
| NVDA 入股 Nokia | **$1B**（2025）|
| Nokia FY2026 NI 成長指引 | **12-14%**（從 6-8% 調升）|
| Nokia 7220 IXR-H6 吞吐量 | **102.4 Tb/s** |

## 對既有 wiki entity 的補強

### 1. ⭐ [[Nokia]] entity 18/25 補強段

既有 entity 涵蓋：
- Infinera $2.3B 併購、2025-02 完成 ✅
- NVDA AI-RAN 戰略合作 ✅（未標具體金額）
- 1830 GX RD66 Multi-Rail 2026 H2 出貨 ✅
- FY2026 NI 指引 +12-14% comparable ✅

**本次新增 anchor**：
- **NVDA $1B 戰略投資（2025）具體金額點出**——既有 entity 提「5G/6G AI-RAN 戰略合作」、未具體金額化、本次補入
- **AI-RAN 商業時程**：2026 商業試點 / **2027 商用版本**——既有 entity 提「商業化時程不明」、本次具體化
- **7220 IXR-H6 資料中心交換器 102.4 Tb/s** + Ultra Ethernet 規範——既有 entity 未涵蓋這條獨立成長線、本次補入「**直接對標 Cisco + Arista 交換器市場**」
- **NI 指引 +12-14% 來源**：既有 entity 標「+12-14% comparable」、本次補「**從 6-8% 調升而來**」= 上修動能 anchor

### 2. ⭐ 新建 [[Cisco]] entity（本次補位）

既有 wiki 提到 Cisco 多次但無 entity：
- [[Nokia]] entity 提：「Cisco：交換 ASIC + 路由 + DCI 子業務、AI 槓桿低」
- [[Ciena]] entity 提：「Cisco：交換 ASIC + 路由器主場、DCI 是補強」
- [[Hyper Rail Multi-Rail（光通訊整合技術）]] 未提 Cisco
- [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]] 未列 Cisco（傳統 firewall 已被 PANW / Cloudflare 取代）

**本次新建 Cisco entity** —— KP 雖然 Cisco 段擋付費牆、但既有 wiki 整合 + Cisco 公開資料可建檔；定位「**傳統網路設備龍頭轉型 AI infra + DCI 對沖位 + Nexus 9k 資料中心交換 + Silicon One 自研 ASIC + Splunk 收購 SecOps**」

### 3. ⭐ [[Ciena]] entity 19/25 補強連結

既有 entity 完整 + 本次 KP 把 CIEN 列為 Scale-Across 第三層的主場 anchor 之一 = 強化 CIEN 在 KP 框架中的地位。

## 對既有 wiki concept 的補強

### 強化 [[Hyper Rail Multi-Rail（光通訊整合技術）]]

- 補入 KP「**AI 網路三層架構**」術語：scale-up（NVDA NVLink）+ scale-out（AVGO/Marvell ASIC）+ scale-across（CIEN/Nokia/Cisco）
- 補入「**單一 DC 無法容納百萬 GPU**」物理瓶頸 anchor
- 補入「**AI 訓練流量牽一髮而動全身**」延遲 / 無損傳輸需求
- KP 把 Nokia 7220 IXR-H6 102.4 Tb/s 列為「**交換器層 vs Cisco/Arista 直接對標**」——既有 concept 主要聚焦 line system（CIEN HyperRail + Nokia Multi-Rail）、本次擴展到交換器層

### 強化 [[NVDA 網路 stack map]]

- 補入 Nokia $1B 入股 + AI-RAN 2027 商用 anchor
- 強化「Cisco 在 DCI / AI infra 是補強位、傳統客戶結構流失給 Arista / Nokia」trend

### 強化 [[控制點轉移（投資版）]]

- DCI 賽道從電信 CSP 主場 → hyperscaler 直接客戶（控制點轉移）
- Nokia 透過 Infinera 拿到 hyperscaler 直連、繞過傳統電信中介

### 強化 [[賣水人選股邏輯（投資版）]]

- 「Scale-Across 唯一純玩家 = CIEN（純度王）+ Nokia（廣度王）+ Cisco（補強位）」三家分食
- 但 KP 把 Nokia 列為「**被動受惠者**」= 不是主動戰略 alpha、而是時代紅利吃下

### 強化 [[市場四階段：懷疑／驗證／共識／反轉]]

- Scale-Across 賽道從「驗證」加速 → 「共識」段
- Nokia 故事「失落年代 → 三張牌反轉」= 經典市場四階段 anchor

## ⚠️ 自警惕（KP 隱含）

1. **AI-RAN 仍在概念階段** — 電信採購遠慢於雲端（2027 商用才算開始）
2. **Nokia 轉型非戰略先見** — 更多是被動搭上 AI 浪潮、時代找上門
3. **付費牆設計** — Cisco 核心分析隱藏、無法完整判斷雙頭論證強度
4. **Cisco 客戶結構流失**：從萬家企業 IT → 少數 hyperscaler、採購邏輯翻轉（低價 / 開放 / 大量）

## KP 隱含立場

- **Nokia 為主推**（完整故事 + 三張牌敘事 + +12-14% 上修指引）
- **Cisco 為對沖 / 陪襯**（故事被截斷、付費牆後可能揭示「**Cisco 雖然 AI 槓桿低、但估值便宜 + Splunk SecOps 整合 + Silicon One 自研 ASIC**」對沖邏輯）
- 整體框架：「Scale-Across 三家分食、Nokia 廣度 + Cisco 估值對沖 + Ciena 純度」三軸組合

## 跟其他 FOMO SOC 篇章對照

| 期 | 主題 | KP 主推 anchor |
|---|---|---|
| #45（2026-04-29）| AI 被動元件 K 型復甦 | MLCC + 鉭電容 + TLVR + 三道防線 |
| #46（2026-06-09）| 800V HVDC 物理鐵壁 | 自來水隱喻 + 灰白區重劃 |
| #47（2026-05-13）| Cloudflare agentic AI | Network as Control Plane |
| **#48（2026-05-20）** | **DCI + Nokia + Cisco** | **Scale-Across 新瓶頸 + Nokia 三張牌 + Cisco 對沖** |
| #49（2026-05-27）| GlobalFoundries 量子計算 | 量子計算「混凝土裡的鋼筋」+ 多平台基礎設施 |

→ KP@FOMOSoc 五期主題對應 AI infra 五大新瓶頸：被動元件 / 電力 / 邊緣 AI / DCI / 半導體基礎建設。

## 待 ingest 延伸

- entity [[Cisco]]（本次新建）= DCI 對沖 + Splunk SecOps + Silicon One
- 更新 [[Nokia]] entity 補入 NVDA $1B 具體金額 + AI-RAN 2027 時程 + 7220 IXR-H6 102.4 Tb/s 三條 anchor

## 相關連結

- [[Hyper Rail Multi-Rail（光通訊整合技術）]]
- [[Nokia]]
- [[Ciena]]
- [[Cisco]]（本次新建）
- [[NVDA 網路 stack map]]
- [[CPO 供應鏈圖譜]]
- [[控制點轉移（投資版）]]
- [[賣水人選股邏輯（投資版）]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[FOMO SOC]] / KP@FOMOSoc（KOL 來源、待建）

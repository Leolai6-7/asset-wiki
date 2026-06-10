---
title: TXC 3042 MEMO — Photo Die + 1.6T 312.5MHz + 石英 sub-30fs vs MEMS
type: summary
created: 2026-06-10
updated: 2026-06-10
sources:
  - raw/2026-06-09_TXC-3042-MEMO-法說-Photo Die-1.6T 312.5MHz.md
tags: [TXC, 晶技, 3042, 石英 timing, Photo Die, 1.6T 光模組, SiTime MEMS 對打, 車用 ADAS, sub-30fs, 物理 chokepoint]
confidence: medium
---

# TXC 3042 MEMO 2026-06-09 摘要

**性質**：公司法說 / 業務報告（management guidance + Leo 整理）

## 一句話

> 石英在 **sub-30fs** 物理 chokepoint **不可被 SiTime MEMS 取代** + Photo Die 製程升級 + 1.6T 312.5MHz 通過驗證 + 50-60% 鎖光通訊 + AI/車用 45% 佔比 = **結構性 re-rate trigger**

## 三條核心 anchor

### 1. ⭐⭐ 石英 sub-30fs 物理 chokepoint 確認
| 指標 | 石英 (TXC) | Silicon MEMS (SiTime) |
|---|---|---|
| 抖動值 | **< 30fs** | **30fs × 2-3 倍** |
| AI server 高速網卡 | ✅ 不可替代 | ⚠️ 部分不達標 |
| 光模組市佔 | 20-30% → 目標 **>30%** | 主力但 sub-30fs 段被擠 |

→ **校準 H1 「石英 vs MEMS 雙軌」框架**：原預設 MEMS 高端勝、實際 sub-30fs 物理 chokepoint 石英勝 = TXC 在最高階光模組賽道有結構性護城河

### 2. ⭐⭐ Photo Die 製程升級 + 產能 5x 跳階
| 時點 | Photo Die 月產能 |
|---|---|
| 目前 | **8KK** |
| 2026 年底 | **24KK**（3x）|
| 2027（明年）| **40KK**（5x） |

- CAPEX：**11 億（2026）+ 15 億+（2027）**
- **50-60% 鎖光通訊**（毛利 >40%、高階逼近 50%）
- 剩餘 40-50% 靈活調配（規避單一應用風險）
- Photo Die 光通訊製作難度比手機高 **1:4 產出比**
- 拉開二線廠技術差距

### 3. ⭐⭐ 1.6T 312.5MHz 通過驗證 + 應用佔比結構升級
| 規格 | 進度 |
|---|---|
| 800G 156.25MHz | ✅ 已放量 |
| **1.6T 312.5MHz** | ✅ **已通過驗證、2027 放量** |
| 3.2T 625MHz | 🔄 積極開發中 |

| 應用 | 2025 | 2026 預估 |
|---|---|---|
| AI | 10% | **16%** |
| 車用 | 26% | **29%** |
| 網通 | 6% | **8%** |
| **AI+車用** | 36% | **45%** ⭐ |

## ⭐ 對 [[TXC 3042|TXC]] entity 校準（H1 18/25 → N1 21/25 升級）

| 軸 | H1 18/25 | **N1 校準後 21/25** | 變動理由 |
|---|---|---|---|
| 路線敏感（逆向）| 4 | **4** | 持平（MEMS 替代風險 vs sub-30fs 護城河平衡）|
| 站別關鍵 | 4 | **5** ⭐ | **升 1**（1.6T 312.5MHz 驗證通過 + Photo Die 製程護城河）|
| 耗材 recurring | 5 | **5** | 持平（大宗 timing recurring）|
| IP | 3 | **4** ⭐ | **升 1**（Photo Die 半導體製程升級 + 30fs 領先 MEMS 2-3x 物理 IP）|
| 客戶分散 | 4 | **3** ⚠️ | **降 1**（Apple 客戶 Q3 流失 2-3 顆 + 中系車用 5 成集中度）|
| **總分** | **18/25** | **21/25** ⭐ | **+3 結構性升級** |

→ **跟 [[Lam Research]] 21 同分**

## ⭐⭐ 對 [[SiTime]] 20/25 thesis 校準

| 維度 | SiTime（MEMS）| TXC（石英）|
|---|---|---|
| 高端 < 30fs 光模組 | ⚠️ **物理達不到** | ✅ **物理護城河** |
| 中端時鐘 | ✅ 高 ASP（4-6x）+ 抗震小型化 | 大宗 |
| 客戶分散 | 5/5 | 3/5（Apple + 中系車用集中）|
| Forward PE | 75-100x（stretch）| 12-18x（折價）|

→ 校準：「**MEMS 全面取代石英**」是錯誤敘事
→ 實際 = **兩條共存路線**：MEMS 攻中端高 ASP、石英守高端 < 30fs chokepoint
→ TXC 在最高階光模組賽道反而是 **SiTime 的「反向 hedge」**（同投資 timing 賽道兩家）

## ⭐ 跟 wiki 既建 concept 深度連結

### 強化 [[Bottleneck Theory（瓶頸論）]]
- TXC 補位 **L4 Laser Sources 跨 L5 Optical Transceivers** 之間的 **timing chokepoint**
- sub-30fs 物理護城河 = 7 層之外的「**timing 層**」chokepoint

### 強化 [[CPO 供應鏈圖譜]]
- 第 4 層 timing（#P10 修正、原誤植第 7 層）：[[SiTime]]（MEMS 中端）+ [[TXC 3042|TXC]]（石英高端 sub-30fs）並列
- 跟 [[NVDA 網路 stack map]] 補入 TXC sub-30fs 護城河

### 強化 [[賣水人選股邏輯（投資版）]]
- TXC 21/25 升級（跟 Lam Research 21、Vistra 23 之間）
- 跟 SiTime 20 + Kyocera 20 + Epson 19 並列「**石英陣營 + MEMS 雙軌**」完整圖譜

### 對應 [[Re-rate 捕捉法]]
- ✅ **營收品質改變**：手機 → AI/車用 45% 佔比
- ✅ **毛利率結構改變**：低單價 Crystal → 高單價 XO + Photo Die 50%+ 鎖光通訊
- ⚠️ **OpEx 紀律**：CAPEX 11 → 15 億 / 年（擴張期、不是規模效應）
- ⚠️ **營業利益拐點**：2027 H1 待 1.6T 312.5MHz 放量驗證
- → **Re-rate 三角形 2.5/4** = 結構性 re-rate 啟動中、未完全 price in

### 對應 [[AI infra CapEx 三階段論]]
- 第三階段 1.6T 光模組爆增 anchor
- TXC 312.5MHz 通過驗證 = 跟 [[Lumentum]] 19 + [[Coherent]] 19 + [[AAOI]] 18 整鏈受惠
- 光模組市佔 20-30% → 30%+ 確認

## ⚠️ Thesis 自警惕

### 1. 公司法說 management guidance 偏樂觀
- 全年 YOY >5% 是 management target
- 1.6T 312.5MHz 放量配合「光模組廠拉貨節奏」= 客戶端確認需求
- 明年市佔 30%+ 是目標、非已實現
- → confidence: **medium**（J2 confidence gate framework）

### 2. Apple 客戶結構性流失
- Q3 有 **2-3 顆元件被 MEMS 取代**
- 整體 ~7 顆今明兩年穩定
- 但中長期 Apple = SiTime 直接 design-in 風險

### 3. 中系車用 5 成集中
- 5 成車用客戶在中系（總營收 ~5%）
- 國際 Tier 1 認證帶動成長、但 ramp 速度未驗證

### 4. CAPEX 高位 + 設備交期 8-12 個月
- 光通訊製作難度比手機高 1:4 產出比
- 高 CAPEX 期 = 自由現金流壓力
- 設備交期長 = 產能擴張延後風險

### 5. SiTime 反向 hedge 可能性
- 如 TXC 護城河被 MEMS 全面突破（**sub-30fs 物理被改善**）→ 兩者投資邏輯崩塌
- 監控指標：SiTime / Microchip / Silicon Labs 下一代 MEMS 抖動值是否 <30fs

## 監控指標（每季校準）

| 指標 | 觸發行動 |
|---|---|
| Photo Die 產能達 24KK（年底）| 確認 thesis ramp |
| 1.6T 312.5MHz 客戶下單 | 進入 [[市場四階段]] 驗證期 |
| 光模組市佔破 30%（2027 H2）| Re-rate 三角形 4/4 滿、estimate up |
| 國際 Tier 1 車廠 ramp | 客戶分散度 3 → 4 重評 |
| Apple 元件流失 >5 顆 | thesis 重評 |
| SiTime / MPS / Microchip MEMS 下一代 sub-30fs | 結構性護城河破口、五軸大幅 derate |

## ⭐ 跟 H1 石英陣營 5 家對照（最終評分排序）

| Rank | Entity | 五軸 | 角色 |
|---|---|---|---|
| 🥇 | **TXC 3042** ⭐ N1 升級 | **21/25** | **石英 sub-30fs chokepoint + Photo Die 護城河 + AI/車用 45%** |
| 🥈 | Kyocera 6971.JP | 20/25 | 跨戰場 conglomerate（含 AVX 鉭電容）|
| 🥉 | Epson 6724.JP | 19/25 | TCXO 全球 #1 多軌組合 |
| 4 | NDK 6779.JP | 17/25 | 日本石英 #1、Apple 集中 |
| 5 | Rakon NZX:RAK | 15/25 | 紐西蘭 niche |

→ **TXC 從 H1 第 3 名（18/25）躍升至 N1 第 1 名（21/25）**

## 相關連結

- [[TXC 3042|TXC]]
- [[SiTime]] 20 / [[Kyocera]] 20 / [[Epson]] 19 / [[NDK]] 17 / [[Rakon]] 15（H1 石英陣營完整對照）
- [[Bottleneck Theory（瓶頸論）]]（timing chokepoint 補位）
- [[CPO 供應鏈圖譜]] 第 7 層 timing
- [[Re-rate 捕捉法]] 三角形 2.5/4
- [[AI infra CapEx 三階段論]] 第三階段 1.6T anchor
- [[賣水人選股邏輯（投資版）]] master 表（H1 升級）
- [[Lumentum]] 19 / [[Coherent]] 19 / [[AAOI]] 18（1.6T 光模組整鏈）
- [[Apple]] 22（Q3 元件流失 2-3 顆）
- [[NVDA 網路 stack map]] timing 層
- [[控制點轉移（投資版）]]（石英 vs MEMS 替代結構）

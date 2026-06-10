---
title: KOL source reliability（KOL 來源可靠度評估）
aliases: [KOL source reliability, KOL 來源可靠度, KOL 評估框架, KOL thesis 評分]
type: concept
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-11-15
sources: []
tags: [Meta 框架, KOL 評估, 來源可靠度, thesis 評分, 訊息蛻變]
thesis_dependency: none（可遷移方法）
confidence: medium
---

# KOL source reliability（KOL 來源可靠度評估）

asset-wiki 用**結構性 framework** 評估 KOL 內容的 thesis 強度 / 命中率 / 訊息蛻變速度——避免「KOL X 說了什麼 → 直接 ingest」的盲目膜拜、也避免「KOL 都不可信」的反向偏誤。

## 一句話

> KOL ≠ 訊號源、而是「**結構性 thesis 提供者**」——評估的不是預測準度、是 thesis 框架的結構性深度 + 命中率 + 訊息蛻變速度。

## 為什麼需要 KOL 評估框架

asset-wiki 目前 ingest 三類 KOL：
- [[FOMO SOC]]（Substack 中文付費）— 物理鐵壁論 / K 型復甦 / 電力戰場
- [[Serenity]]（X / Reddit）— Bottleneck Theory / 光電 chokepoint
- [[宋分（美股送分題）]]（Substack）— 估值教學 + 月度宏觀備忘錄

每個 KOL 有不同：
- thesis 框架深度（從 narrative 到結構性 framework）
- 命中率（過去預測對的比例）
- 訊息蛻變速度（從 KOL 一手到媒體 → 散戶的時間）

→ 沒有框架就只能憑感覺、容易踩坑。

## 三軸評估

### 軸 1：thesis 框架結構性深度（5 分）

**衡量**：KOL 提的是「narrative 故事」還是「結構性 framework」？

| 分數 | 內容 |
|---|---|
| 5 | 提出全新 framework + 多層解釋（如 [[FOMO SOC]] 物理鐵壁論的「自來水五站隱喻」+ P=VI + 灰白區重劃）|
| 4 | 應用既有 framework + 新數據（如 [[Serenity]] 把瓶頸論套到光電）|
| 3 | 重述既有 thesis + 補充細節 |
| 2 | narrative 故事為主 + 少量結構性 |
| 1 | 純情緒 / 主觀 / 無框架 |
| 0 | 反框架（為說而說、為流量而戰）|

### 軸 2：命中率（5 分）

**衡量**：過去 12-24 個月，KOL 的明確預測有多少兌現？

| 分數 | 內容 |
|---|---|
| 5 | 80%+ 預測兌現 + 大事件提前 6+ 個月命中（如 [[宋分（美股送分題）]] HBM iPhone Moment 2024-Q2 → 2025-Q2 SK Hynix re-rate 兌現）|
| 4 | 60-80% 兌現 |
| 3 | 50-60% 兌現（中性）|
| 2 | 30-50% 兌現 |
| 1 | < 30% 兌現 |
| 0 | 明顯反指（多數預測反向）|

⚠️ **要看「明確時間 + 明確標的 + 明確方向」三要素都全的預測**——不算「我覺得 AI 很重要」這類模糊話。

### 軸 3：訊息蛻變速度（5 分逆向）

**衡量**：KOL 一手 → 媒體 → 散戶 → ETF 蛻變速度——速度越快、alpha 窗口越小。

| 分數 | 內容 |
|---|---|
| 5 | 一手到散戶 4+ 週（小眾、深度、付費牆）→ alpha 窗口大（如 [[FOMO SOC]] 付費 Substack、第 45 期被動元件第三次週期未被主流引用）|
| 4 | 2-4 週（X 中等流量）|
| 3 | 1-2 週（X 高流量 + 媒體引用）|
| 2 | < 1 週（X 病毒 + 媒體連發）|
| 1 | 24 小時（病毒級、頂層 KOL）|
| 0 | 訊息已是 mainstream consensus（如 [[宋分（美股送分題）]] 部分 thesis 被主流引用後 alpha 消失）|

→ 訊息蛻變慢 = alpha 窗口大 = 更值得 ingest 進 wiki

## 三 KOL 評分

| KOL | thesis 框架深度 | 命中率 | 訊息蛻變慢 | **總分** | 定位 |
|---|---|---|---|---|---|
| **[[FOMO SOC]]** | 5（自來水五站隱喻 + 物理鐵壁論 + K 型復甦三道防線 framework）| 4（KP @FOMOSoc 約 60-80% 兌現、Vera Rubin 機櫃 44 萬顆 MLCC 已驗證）| 5（付費牆 + 中文 + Substack 訊息蛻變慢）| **14/15** | **結構影響 22-24**（範圍依 thesis 框架穩定度）+ 可投資 n/a |
| **[[Serenity]]** | 4（Bottleneck Theory 改造瓶頸論套光電）| 4（玻璃基板時間線 2025-Q1 anchor 已被多家引用兌現）| 3（X 中等流量 + 中文圈現象級、訊息蛻變中等）| **11/15** | **結構影響 18-20**（Bottleneck Theory 主 framework 提供者）+ 可投資 n/a |
| **[[宋分（美股送分題）]]** | 5（#20 三標準 + #2 HBM iPhone Moment + #3 AI 半導體受惠者擴散 framework）| 5（HBM iPhone Moment 2024-Q2 → 2025-Q2 SK Hynix re-rate 兌現、估值教學經典）| 2（中文 Substack 高流量 + 部分 thesis 已被主流引用）| **12/15** | **結構影響 20-22**（thesis 經典 + 命中率高、訊息蛻變較快、alpha 窗口縮）+ 可投資 n/a |

## thesis 衰退判斷

KOL thesis 也會衰退、需要追蹤指標：

| 指標 | 應對 |
|---|---|
| **重複自己**（同一 framework 反覆套用）| 結構性深度 -1 |
| **命中率下降**（最近 12 個月明確預測兌現 < 50%）| 命中率 -1 |
| **訊息蛻變加速**（被主流媒體 / ETF 開始引用）| 訊息蛻變 -1 |
| **轉向流量導向**（標題黨 / 情緒化）| thesis 框架深度 -2 |

→ 每季 lint 時自動重評。

## 操作流程

當 ingest KOL 內容：
1. 確認本 concept 是否在 entity（如 [[FOMO SOC]]）裡引用
2. 看 thesis 框架深度、引用其他 entity 的 reuse 是否有結構性深度
3. 命中率追蹤：在 entity 內加「**命中事件清單**」（時間 + 預測 + 兌現狀態）
4. 訊息蛻變追蹤：在 entity 內加「**蛻變指標**」（主流媒體引用 / ETF 重倉 / 散戶討論密度）

## 何時不該 ingest KOL 內容

- 純 narrative 無 framework
- 命中率 < 30%
- 訊息已是 mainstream consensus（無 alpha 窗口）
- KOL 利益衝突（持倉鼓吹）

→ 篩掉這四類後、KOL 內容才有結構性價值。

## 跟既有 concept 對接

- [[結構影響分 vs 可投資五軸分（雙評分體系）]]：KOL 結構影響分高、可投資 n/a
- [[資訊擴散四階段]]：KOL 是「機構 → 賣方 → 媒體 → ETF」的「機構」端、訊息蛻變速度越慢 alpha 越大
- [[預期差]]：KOL 提供新 framework = 新預期差來源
- [[公司 Entity 模板（Step 1-3 三段式）]]：KOL entity 不適用 Step 3 財務快照、改用「framework 矩陣 + 命中事件清單」
- [[看錯三類型]]：KOL 也會看錯、需要 framework 篩

## 三 KOL 互補不互相取代

| 戰場 | 主要 KOL | 為什麼 |
|---|---|---|
| 電力 + 散熱 + 被動元件 | [[FOMO SOC]] | 物理鐵壁論 + K 型復甦 framework |
| 光電 + 玻璃基板 + 瓶頸論 | [[Serenity]] | Bottleneck Theory + 7 層覆蓋 |
| 估值 + 宏觀 + M7 / 半導體 | [[宋分（美股送分題）]] | 估值教學 + 月度備忘錄 |

→ Leo 可同時追蹤三家、互相校準 thesis。

## KOL 評估的元規則

本 concept 是「**評估 KOL 的 KOL**」——asset-wiki 自身就是評估框架的提供者、需要對自己有元評估：
- 結構性 framework 深度：每季新增 1-2 個 framework 是健康訊號
- 命中率：每季追蹤 thesis 兌現
- 訊息蛻變：本 wiki 不對外發布（disclaimer）= 訊息蛻變 = 0、alpha 窗口最大

## 相關連結

- [[FOMO SOC]] — 物理鐵壁論 + K 型復甦 KOL
- [[Serenity]] — Bottleneck Theory KOL
- [[宋分（美股送分題）]] — 估值教學 + 宏觀備忘錄 KOL
- [[結構影響分 vs 可投資五軸分（雙評分體系）]] — KOL 結構影響分 vs 可投資 n/a
- [[資訊擴散四階段]] — KOL 在擴散階段的位置
- [[預期差]] — KOL 提供新預期差來源
- [[公司 Entity 模板（Step 1-3 三段式）]] — KOL entity 變體
- [[看錯三類型]] — KOL 也會看錯
- [[賣水人選股邏輯（投資版）]] — KOL 推薦的標的進可投資 ranking 前要過五軸


## ⚠️ #P11 認識論審核後的凍結聲明（2026-06-10）

- **本檔所有「命中率」子分數與 reliability 總分、即日起標記為「未計算」**——原分數基於精選名場面（n=1-2）、無分母、無失誤紀錄、違反本庫自己的「未滿 10 筆不給分」紀律（認識論紅隊：KOL entity 內「失誤」字串出現 0 次）
- 恢復給分條件：per-KOL 全量帶時間戳 call ledger（n≥20 已結）＋失誤紀錄段
- 「思維強度」子分數保留（它評的是框架品質、不是預測戰績）
- 在此之前、KOL 權重僅用於 ingest 排序、**不得作為 thesis 信心的輸入**

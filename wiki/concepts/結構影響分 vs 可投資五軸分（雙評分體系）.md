---
title: 結構影響分 vs 可投資五軸分（雙評分體系）
aliases: [雙評分體系, 結構影響分, 可投資五軸分, dual scoring, scoring split]
type: concept
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2027-06-09
sources: []
tags: [Meta 框架, 評分體系, 投資方法論, 五軸評分, 結構影響]
confidence: high
---

# 結構影響分 vs 可投資五軸分（雙評分體系）

asset-wiki 的**評分體系拆分原則**。codex 最強質疑落地：**「結構重要 ≠ 預期報酬」**——把「結構性影響」跟「可投資 alpha」拆成兩套分數，避免不可投資 entity（如 [[Imec]] / [[FOMO SOC]] / [[Cameron LNG]] / [[Tellurian]]）混進可投資 ranking 池造成 thesis 矛盾。

## 一句話

> 結構性影響大不代表你能買、可投資 alpha 高不代表結構性最關鍵——必須拆兩套分數。

## 問題：原五軸體系的 thesis 矛盾

原本 wiki 用單一 25 分制五軸評分（[[賣水人選股邏輯（投資版）]]）排序所有 entity。問題：

| Entity | 五軸 | 為什麼矛盾 |
|---|---|---|
| [[Imec]] | 24/25 | R&D consortium 非上市、不可投資、但跟 [[Disco Corp]] 24 / [[村田 Murata]] 24 並列 |
| [[Cameron LNG]] | n/a | Sempra LNG 子公司、不可獨立投資、但結構性是 LNG 出口 anchor |
| [[FOMO SOC]] | n/a | KOL Substack、結構性影響高（提供 thesis 框架）、但完全不可投資 |
| [[Tellurian]] | n/a | 2024-10 被 [[Woodside Energy]] 收購、已下市、但結構性影響 Driftwood 仍重要 |

→ 把這些塞進「可投資 ranking 池」會讓「ranking 第一」失去意義。

## 解決：拆兩套分數

### 結構影響分（25 分制、適用所有 entity）

**衡量**：這家 entity 對 wiki 整體 thesis / 知識圖譜的結構性貢獻有多大。

五軸：
1. **產業 thesis 制定者**（5）= 是否定義產業 narrative（如 FOMO SOC 提供 thesis 框架）
2. **chokepoint / 不可繞過**（5）= 製造 / 設計 / R&D / 物流是否必經
3. **跨戰場滲透**（5）= 是否同時影響多個戰場
4. **路線中立 / 多軌受惠**（5）= 不押任何單一商業路線
5. **lock-in / IP / 標準制定**（5）= 是否擁有結構性護城河

**適用範圍**：所有 entity（含不可投資的 KOL / consortium / 私募 / 已下市 / 子公司）

### 可投資五軸分（25 分制、只適用上市可投資 entity）

**衡量**：這家公司作為**可買進標的**的 alpha 品質。

五軸（沿用既有）：
1. **路線敏感度（逆向）**（5）= 路線分歧曝險
2. **站別關鍵度**（5）= 製程鏈不可繞過
3. **耗材 recurring**（5）= 重複性收入
4. **IP 控制**（5）= 專利 / 標準
5. **客戶分散**（5）= 客戶結構

**適用範圍**：只限上市 + 可獨立投資 entity（**排除**：KOL / consortium / 私募未 IPO / 已下市 / 子公司無獨立 ticker）

## Entity 分類矩陣

| 類別 | 結構影響分 | 可投資五軸 | 範例 |
|---|---|---|---|
| **可投資 + 高結構影響** | 22+ | 22+ | [[ASML]] 25/25 + 25/25 / [[Synopsys]] 24/24 / [[村田 Murata]] 24/24 |
| **可投資 + 中結構影響** | 18-22 | 18-22 | [[欣興]] 19/19 / [[弘塑]] 19/19 / [[景碩]] 17/17 |
| **可投資 + 低結構影響** | <18 | <18 | [[華新科]] 13/13 / [[南電]] 9/9 |
| **不可投資 + 高結構影響** | 22+ | **n/a** | [[Imec]] 24/n.a / [[FOMO SOC]] 22/n.a / [[Cameron LNG]] 19/n.a / [[Tellurian]] 18/n.a |
| **私募待 IPO** | 18-22 | **TBD** | [[Wiz]] 20/TBD / [[Databricks]] 19/TBD / [[Lambda]] 13/TBD |

## 為什麼不能合併

合併會造成三大問題：

1. **Ranking 失真**：[[Imec]] 24 跟 [[村田 Murata]] 24 並列頂級——但前者不可投資、後者可。Leo 排可投資 ranking 看到 Imec 第一名沒用。
2. **Thesis 混淆**：「結構性 anchor」跟「投資首選」不是同件事。FOMO SOC 提供 thesis 框架（結構性高）、不是投資標的（不可投資）。
3. **新讀者誤判**：看到「Imec 24/25」會誤以為這是可買標的，跟 [[ASML]] 25/25 同類。

## 落地：master 表分區

[[賣水人選股邏輯（投資版）]] master 表加雙評分欄位：

```markdown
| 公司 | 結構影響 | 可投資五軸 | 路線敏感 | ... | 定位 |
|---|---|---|---|---|---|
| **[[ASML]]** | **25** | **25/25** | 5 | ... | 頂級真賣水人 #1 |
| **[[Imec]]** | **24** | **n/a**（R&D consortium）| 5 | ... | 結構性 R&D 公共財 |
| **[[村田 Murata]]** | **24** | **24/25** | 5 | ... | 被動元件全鏈寡占 |
| **[[FOMO SOC]]** | **22** | **n/a**（KOL）| — | ... | thesis 框架提供者 |
| **[[Cameron LNG]]** | **19** | **n/a**（Sempra 子公司）| — | ... | 結構性 LNG 出口 anchor |
| **[[Tellurian]]** | **18** | **n/a**（已下市）| — | ... | Driftwood Phase 1 reference |
```

→ 兩欄並列、`n/a` 自動排除可投資 ranking 池。

## 對應 codex 質疑

codex 之前指出：「IQE 89% CAGR claim」假精度問題 + 「Imec 不可投資卻跟 Murata 並列」結構性錯誤。本 concept 落地：

- **Imec**：結構影響 24、可投資 n/a → 不再進可投資 ranking
- **FOMO SOC**：結構影響 22（KOL thesis 框架制定者）、可投資 n/a → 不再進可投資 ranking
- **Cameron LNG / Tellurian**：結構影響 19 / 18、可投資 n/a → 不再進可投資 ranking
- **可投資 ranking 池**：[[ASML]] 25 / [[Disco Corp]] 24 / [[村田 Murata]] 24 / [[Synopsys]] 24 / [[SUMCO]] 24 / [[信越化學]] 24 = **可投資頂級 6 家**（去掉 Imec）

## 跟既有 concept 對接

- [[賣水人選股邏輯（投資版）]]：master 表加雙評分欄位（n/a 標記不可投資）
- [[五軸分數 confidence gate（低信心給區間 + thesis-dependent flag）]]：低信心 entity 給區間而非單一分數
- [[公司 Entity 模板（Step 1-3 三段式）]]：entity 模板強制加「結構影響 vs 可投資」分區註明
- [[6 戰場交集圖譜]]：跨戰場 anchor 用結構影響分排序、不用可投資分

## 何時用哪套分數

| 情境 | 用哪套 |
|---|---|
| 排可投資 ranking、選買進標的 | 可投資五軸 |
| 排結構性 anchor、看 thesis 完整度 | 結構影響 |
| 評估 KOL / consortium 重要性 | 結構影響 |
| 評估私募待 IPO 公司 | 結構影響（先記）+ 可投資 TBD（IPO 後補） |
| 跨戰場 anchor 矩陣 | 結構影響（避免投資導向偏誤）|

## 操作流程

新增 entity 時：
1. 先給結構影響分（必填）
2. 判斷是否可投資（上市 + 獨立 ticker + 非子公司）
3. 可投資 → 補可投資五軸分
4. 不可投資 → 五軸欄位填 `n/a` + 註明原因（KOL / consortium / 子公司 / 已下市 / 私募）

## 相關連結

- [[賣水人選股邏輯（投資版）]] — 主 ranking 表
- [[五軸分數 confidence gate（低信心給區間 + thesis-dependent flag）]] — 低信心給區間
- [[公司 Entity 模板（Step 1-3 三段式）]] — entity 強制格式
- [[Imec]] — 結構影響 24、可投資 n/a 標竿
- [[FOMO SOC]] — KOL thesis 框架制定者
- [[Cameron LNG]] — 子公司結構性 anchor
- [[Tellurian]] — 已下市 reference entity
- [[6 戰場交集圖譜]] — 跨戰場用結構影響排序

---
title: 跨庫對照（asset-wiki ↔ llm-wiki）
aliases: [跨庫對照, asset-wiki llm-wiki, 跨 vault 對照]
type: concept
created: 2026-06-05
as_of: 2026-06-05
check_after: 2027-01-15
updated: 2026-06-05
sources: []
tags: [Meta 框架, 跨庫, llm-wiki, 對照表]
thesis_dependency: none（可遷移方法）
confidence: medium
---

# 跨庫對照（asset-wiki ↔ llm-wiki）

Leo 有兩個並行 wiki：
- **`llm-wiki`**（`/Users/laihaoqian/llm-wiki/`）：AI / agent 觀點
- **`asset-wiki`**（`/Users/laihaoqian/asset-wiki/`）：投資 / 市場研究觀點

**同一個概念在兩邊有不同切法**——本 concept = **對照表 + 何時跨庫查詢的指引**。

→ 解決 codex P3 「llm-wiki 既有 concept 未橋接到 asset-wiki」

## 一句話

> wikilink 不能跨 vault，但**人類可以記住對照關係 + 在需要時跨庫查**。

## 對照表（核心 concept）

| asset-wiki | llm-wiki | 切角差異 |
|---|---|---|
| [[控制點轉移（投資版）]] | [[控制點轉移]] | 投資估值 vs AI 產業權力結構 |
| [[賣水人選股邏輯（投資版）]] | [[賣水人選股邏輯]] | 投資 framework vs 概念定義 |
| [[開源作為武器（投資版）]] | [[開源作為武器]] | 商業策略 vs AI 產業觀察 |
| [[CPO 供應鏈圖譜]] | [[CPO（共同封裝光學）]] | 賣水人位階 vs 技術 anchor |
| [[TGV 製程鏈圖譜]] | [[AI 供應鏈]] | TGV 具體製程 vs 全鏈條總覽 |
| [[半導體基礎建設化]] | [[Re-rate 捕捉法]] | sub-thesis vs 估值方法 |
| [[公司 Entity 模板（Step 1-3 三段式）]] | [[七件事快篩]] | wiki schema vs 研究方法 |
| [[預期差]] | （無對應） | asset-wiki 獨有 |
| [[五層損益表（營業槓桿）]] | [[營業槓桿拆解（五層損益表）]] | 同主題、不同 wiki 版本 |
| [[修正三階段]] | （無對應） | asset-wiki 獨有 |
| [[AI 通縮三路徑]] | （部分對應 [[AI 自主迭代模式]]） | 經濟視角 vs AI 系統視角 |
| [[政府風險溢價（AI 公司）]] | [[AI 立法與監管]]、[[責任歸屬]] | 估值 vs AI 治理 |
| [[AI 廣告信任危機]] | [[AEO]]、[[SEO]]、[[社群演算法]] | 估值衝擊 vs AI 產品分析 |
| [[AI 訂閱制 unit economics]] | [[AI 訂閱制與用量制]] | unit economics vs AI 計價模式 |
| [[AI 資安攻防成本曲線]] | [[AI 資安研究]] | 賽道投資 vs AI 安全研究 |
| [[控制點轉移（投資版）]] | [[Agent 商品化]] | 控制點傳導 vs Agent 層商品化 |
| [[接口控制權]] | [[MCP（Model Context Protocol）]] | 估值範式 vs 技術協議 |

## 對照表（核心 entity）

| asset-wiki | llm-wiki | 切角差異 |
|---|---|---|
| [[宋分（美股送分題）]] | （llm-wiki 也有，同名） | 同 entity 雙 wiki 並存 |
| [[sennn.nnna]] | （無對應，asset-wiki 獨有） | KOL 屬投資側 |
| [[Anthropic]] | （llm-wiki 也有，同名） | 投資視角 vs AI 公司技術／產品 |
| [[OpenAI]] | （llm-wiki 也有，同名） | 同上 |
| [[Microsoft]] | （llm-wiki 也有，同名） | 同上 |
| [[Google]] | （llm-wiki 也有，同名） | 同上 |
| [[NVDA]] | [[NVIDIA]] | 名稱不同 / 投資 vs AI 硬體 |
| [[幻方量化]] | [[幻方量化]] | 雙 wiki 並存 |
| [[華為]] | [[華為]] | 雙 wiki 並存 |
| [[DeepSeek]] | [[deepseek]] | 名稱大小寫不同 |
| [[SiTime]] | [[SiTime（SITM）]] | 名稱前綴不同 |
| [[wallstengine]] | [[wallstengine]] | 雙 wiki 並存 |
| [[Meta]] | [[Meta]] | 雙 wiki 並存 |

## 何時跨庫查詢

### 場景 1：找方法論補強
- 在 asset-wiki 寫 entity 三段式 → 需要 [[七件事快篩]] → 開 llm-wiki

### 場景 2：找 AI / 技術背景
- 在 asset-wiki 寫 [[Anthropic]] entity → 需要 MCP 技術細節 → 開 llm-wiki [[MCP（Model Context Protocol）]]

### 場景 3：找 KOL 觀點
- 在 asset-wiki 看 [[宋分（美串送分題）]] 投資 thesis → 想知道他在 AI 議題怎麼看 → 開 llm-wiki

### 場景 4：tag-based query
- llm-wiki 用 [[AI 供應鏈]] 通用標 → asset-wiki 用具體賽道（[[TGV 製程鏈圖譜]] / [[CPO 供應鏈圖譜]]）

## 同名 entity 的更新政策

asset-wiki 跟 llm-wiki 各自獨立維護（**不自動同步**）：
- 同名 entity 兩邊內容可以不同（不同切角）
- 更新時：若新 finding 適用兩邊，**手動 sync**
- 衝突時：**asset-wiki 信投資側、llm-wiki 信 AI 側**

## 跟其他 concept 連結

- [[公司 Entity 模板（Step 1-3 三段式）]]：asset-wiki 獨有的 entity schema
- [[Wiki Ritualization Risk]]（llm-wiki）：兩邊都要警惕的失敗模式

## 相關連結

- llm-wiki 本身：`/Users/laihaoqian/llm-wiki/`
- llm-wiki CLAUDE.md：`/Users/laihaoqian/llm-wiki/CLAUDE.md`

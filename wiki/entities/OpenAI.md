---
title: OpenAI
aliases: [OpenAI, ChatGPT]
type: entity
created: 2026-06-04
as_of: 2026-06-04
check_after: 2026-10-15
updated: 2026-06-09
sources:
  - raw/2026-04-06_OpenAI拿了1220億——但這筆錢不是你以為的那種錢.md
  - raw/2026-05-09_FOMOSOC-KP41-AI利潤奇點CPU復興FDE.md
  - raw/2026-05-16_FOMOSOC-KP42-Cerebras上市WSE-3對NVDA啟示.md
tags: [標的, AI, 模型公司, 私募, IPO, Microsoft, FDE 戰略, Deployment Company, Cerebras 200 億訂單]
thesis_dependency: AI-capex
confidence: medium
---

# OpenAI

全球最大 AI 模型公司。2026 Q2 估值 **$852B**、年虧 **$14B**、單位經濟每賺 1 元燒 1.69 元。**靠循環投資與條件資本續命**——但 IPO 被合約鎖死成為「**必發生事件**」。

## 估值定位（2026 Q1-Q2）

- 估值 $852B
- 年虧 $14B
- **單位經濟負面**：每賺 1 元燒 1.69 元
- $1,220 億融資的**真實意義**：不是傳統 VC，是條件資本（compute commitment、AGI tripwire、IPO 條件）

## 三條商業模式撞牆（2026 Q1）

1. **融資路**：1,220 億只夠 ~1 年
2. **訂閱路**：被 [[微軟]] Copilot NPS -19.8、滲透率卡 3.3% 證明 SaaS 不 work
3. **廣告路**：聊天廣告利益衝突未解（→ [[AI 廣告信任危機]]）

## 跟既有 concept 的關係

- [[AI 融資結構（條件資本）]]：OpenAI 的 1220 億是這個概念的最大實驗
- [[循環投資（CSP-Model 互鎖）]]：OpenAI ↔ Microsoft Azure 是經典案例
- [[模型商品化]]：DeepSeek 用 $0.28/M token 壓制 OpenAI 定價
- [[政府風險溢價（AI 公司）]]：vs Anthropic 的對比

## 護城河測試

| 項目 | 現狀 |
|---|---|
| 模型品質 | 領先持續收窄（vs Claude、Gemini） |
| 分發護城河 | 弱（不擁有 CSP，靠 Microsoft Azure） |
| 接口控制 | **輸給 Anthropic 的 MCP** |
| 訂閱黏性 | NPS 為負 |

## 風險

- **DeepSeek 結構性破壞**：算力本業派可以無限制降價
- **Microsoft 雙重曝險**：持股 27% + Azure 最大 CSP = 任何 OpenAI 危機都會傳導
- **AGI tripwire 條款**：定義模糊、變更控制權風險

## ⭐ FDE 戰略 — The Deployment Company $100 億合資（2026-05-09 KP41）

→ 完整 framework 見 [[Forward Deployed Engineer 戰略（FDE）]]

### OpenAI FDE 規模化執行

| 元素 | 內容 |
|---|---|
| **The Deployment Company** | 估值 **$100 億**合資企業 |
| **背後私募基金** | 控制**數千投資組合公司**（直接客戶池）|
| **目標** | 解決企業 70-90% POC 卡死的「試點煉獄」|

### 三軌商業模式（FDE 落地後）

| 軌 | 內容 |
|---|---|
| ChatGPT consumer | $20/月 + Plus 訂閱 |
| ChatGPT Enterprise | 高 ACV API + enterprise pricing |
| **OpenAI + Deployment Company** | FDE 派駐 + 私募基金 portfolio companies 觸達 |

→ 從「API 用量」轉向「API + 高價值服務」、強化客戶黏性 + 護城河

## ⭐ Cerebras 戰略客戶（2026-05-16 KP42）

- **OpenAI $200 億訂單**（Cerebras Backlog 81% 集中）
- 用於高吞吐量推論場景（vs HBM 訓練主場仍 NVDA）
- 是 [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]] 商業化的關鍵 anchor
- → 連 [[控制點轉移（投資版）]]：OpenAI 在訓練（NVDA + AMD）+ 推論（Cerebras + AVGO + Oracle）多源策略

## 相關連結

- [[AI 融資結構（條件資本）]]
- [[循環投資（CSP-Model 互鎖）]]
- [[Forward Deployed Engineer 戰略（FDE）]]（KP41 framework）
- [[AI 利潤奇點（Token 經濟學拐點）]]（KP41 同源）
- [[Cerebras WSE 架構（SRAM vs HBM 推論分裂）]]（KP42 framework）
- [[Cerebras]]（KP42 entity）
- [[控制點轉移（投資版）]]
- [[Microsoft]]
- [[Anthropic]]
- [[DeepSeek]]
- [[政府風險溢價（AI 公司）]]
- [[CoreWeave]]、[[Oracle]]、[[AVGO]]、[[NVDA]]
- [[FOMO SOC]]（KP@FOMOSoc KOL 來源、待建）
- [[宋分（美股送分題）]]

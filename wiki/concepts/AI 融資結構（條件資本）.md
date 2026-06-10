---
title: AI 融資結構（條件資本）
aliases: [AI 融資結構, 條件資本, AI Financing, AGI tripwire]
type: concept
created: 2026-06-04
as_of: 2026-06-04
check_after: 2026-12-15
updated: 2026-06-04
sources:
  - raw/2026-04-06_OpenAI拿了1220億——但這筆錢不是你以為的那種錢.md
tags: [融資, 條件資本, 私募, OpenAI, AGI, IPO]
thesis_dependency: AI-capex
confidence: medium
---

# AI 融資結構（條件資本）

[[OpenAI]] 1220 億融資揭示的**新融資範式**：不是傳統 VC，是**閉環內部記帳的條件資本**。

## 三個結構性特徵

### 1. 條件資本（Conditional Capital）
- 錢不是無條件給的
- 條件：compute commitment（買 Azure）+ AGI tripwire + IPO 條件
- **錢用完還是花在投資人自己的產品線上**

### 2. 循環投資
→ 完整見 [[循環投資（CSP-Model 互鎖）]]

```
Microsoft 投資 OpenAI $100B
  ↓
OpenAI 用這筆錢買 Azure 算力
  ↓
Microsoft 認列 Azure 營收 $100B
  ↓
循環！
```

= 看起來是融資，其實是**內部記帳 + Azure 預付**。

### 3. IPO 鎖定（「必發生事件」）
- 1220 億有合約條款綁定 IPO 時程
- OpenAI **沒有不上市的選項**
- → 對市場是「**必發生事件**」，可定價

## AGI tripwire

合約條款：「達到 AGI 觸發」→ 變更控制權

問題：
- **定義模糊**（什麼算 AGI？）
- 變更控制權的具體機制不透明
- 對所有持股者是長期不確定性

## 投資意涵

### 對 [[OpenAI]] 估值
- 1220 億只夠 ~1 年
- IPO 鎖定 → 必須 IPO，會發生折價
- AGI tripwire → 結構性折價

### 對 [[Microsoft]] 估值
- 27% 持股 + Azure 預付 → **雙重曝險**
- OpenAI 危機 → Microsoft 兩端受傷
- 但 Azure 營收 = 1220 億的一部分 → 短期 boost

### 對 AI 模型公司估值範式
- 條件資本不是免費的錢
- 真實 burn rate 需要剝離「循環部分」才看得清
- [[DCF vs PE]] 中的「確定性」要打折扣

## 跟 [[宋分備忘錄 ＃1 — CSP-AI 通縮]] 的連結

- 宋分的「CapEx 不會短期見頂」+ OpenAI 1220 億都指向**循環不會自動結束**
- 但**單位經濟（每賺 1 元燒 1.69 元）**是真實的 burn rate
- [[FCF 拐點]] 對 OpenAI 是「**不存在**」（沒上市，沒 FCF 公開）

## 待 ingest 延伸

- [[Anthropic]] 的融資結構（vs OpenAI 模式）
- 其他大融資（xAI、Mistral、Perplexity）
- 中國 AI 公司（[[幻方量化]] 不需融資是反例）

## 相關連結

- [[循環投資（CSP-Model 互鎖）]]
- [[OpenAI]]
- [[Microsoft]]
- [[政府風險溢價（AI 公司）]]
- [[模型商品化]]
- [[CapEx 見頂辯論]]
- [[FCF 拐點]]

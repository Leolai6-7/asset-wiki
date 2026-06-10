---
title: AI 資安 — DeepSeek 資安風險調查
aliases: [DeepSeek 資安風險, DeepSeek 資料外洩, 中國 AI 資安風險]
type: summary
created: 2026-06-04
as_of: 2026-06-04
check_after: 2027-01-15
updated: 2026-06-04
sources:
  - raw/2026-04-07_DeepSeek資安風險調查.md
tags: [AI 資安, 中國 AI, DeepSeek, Wiz, 資料主權, 國家安全]
thesis_dependency: AI-capex
confidence: medium
---

# AI 資安 — DeepSeek 資安風險調查

**一句話核心**：DeepSeek 便宜 50 倍的 API 背後，是資料主權、跨境傳輸與政府調閱的隱性成本——這不是技術問題，是資安產業重新定價「中國 AI 風險」的起點。

## 重點摘要

### 三個關鍵事件（2025 Q1）

| 事件 | 揭露者 | 風險面 |
|---|---|---|
| ClickHouse 資料庫完全公開（無認證） | Wiz Research | 100 萬條日誌 + 用戶明文聊天 + API 密鑰外洩 |
| 連接騰訊雲/字節跳動雲、建立用戶數位指紋 | 台灣 NICS 資安院 | 跨境資料傳輸 + 跨網站追蹤 |
| 公務機關全面禁用 | 台灣數位發展部 | 法律依據：2019 行政院危害國安資通產品限制原則 |

全球同步應對：美、日、韓、加、荷、澳、印度均採限制或警告措施。

### 結構性風險：中國《國家情報法》第七條

任何組織與公民「應當依法支持、協助和配合國家情報工作」。意味著任何處理敏感商務資料的境外企業，使用 DeepSeek 即承擔合規風險——這不是技術 bug，是制度設計。

## 產業/供應鏈延伸調查

### 1. 誰受惠：雲端資安「賣水人」

Wiz 一篇 blog 引爆了三件事——政府禁令、媒體 wave、企業 procurement review。這就是 **資安公司商業模式的入口流量**：

- **Wiz**（Google 將以 $32B 收購中）：雲端 CSPM/CNAPP 龍頭，DeepSeek 事件是教科書級 PR
- **CrowdStrike (CRWD)**：端點 + 威脅情報，企業會收到「審查所有第三方 AI 服務」的合規需求 → 直接拉 ARR
- **Palo Alto Networks (PANW)**：Prisma Cloud + AI Access Security，已推出針對 LLM API 流量的 DLP
- **Cloudflare (NET)**：AI Gateway 產品讓企業集中監控 LLM 呼叫 → 風險可視化
- **Zscaler (ZS)**：SSE 廠商，可在邊界阻擋 DeepSeek 等高風險 endpoint

關鍵供應鏈洞察：**「中國 AI 風險」變成資安採購清單的新品項**，AI Security Posture Management (AI-SPM) 是 2026 新興 SKU。

### 2. 誰受害：中國模型的 enterprise 通路

- DeepSeek 即使技術上能與 GPT-5/Claude Opus 4.6 並列，西方財星 500 強 procurement 已封閉
- 中國模型的可滲透市場退守到：(a) 中國境內 (b) 一帶一路國家 (c) 開源權重自架（規避雲端 API 路徑）
- **真正贏家**：開源權重的本地部署生態（NIM、vLLM 廠商、本地 GPU 雲）反而從這個禁令受惠——「我們不用 DeepSeek 的 API，我們自己跑權重」

### 3. AI Liability 開始定價

- 企業客戶不再問「這個模型多便宜」，而是問「資料主權、模型責任歸屬、合規 SLA」
- → 高定價模型（[[Anthropic 提案]]、OpenAI）的「企業安全溢價」獲得結構性支撐
- 對 [[AVGO]]、[[NVDA]] 的 sovereign AI 敘事（每個國家要自己的模型/雲）是強催化

## 與 wiki 概念的深度連結

| 主題 | concept |
|---|---|
| 跳出 DeepSeek 個案看資安產業 | [[跳出個股看三層：產業、目的、供應]] |
| 「便宜 50 倍」的表面 vs 資料主權的賭注 | [[預期差]]（市場一開始只 price-in 性能/價格） |
| 政府禁令→企業合規→ARR 拉升的擴散路徑 | [[資訊擴散四階段]] |
| 從「成本優先」轉向「安全優先」 | [[效率→安全切換]] |
| 風險指標的新項目：地緣 AI 風險 | [[三個風險指標]] 應擴張 |

## 提案的新節點（主 agent 落地）

- entity：[[DeepSeek]]、[[幻方量化]]、[[Wiz]]、[[CrowdStrike]]、[[Palo Alto Networks]]、[[Cloudflare]]、[[Zscaler]]
- concept：[[中國 AI 風險定價]]、[[AI Liability]]、[[Sovereign AI]]

## 相關連結

- [[AI 資安 — 紅藍隊分離與商業模式]]
- [[AI 資安 — 幻方量化與 DeepSeek 關係]]
- [[AI 資安 — Claude 4000 美元找到 22 個 Firefox 漏洞]]
- [[跳出個股看三層：產業、目的、供應]]
- [[效率→安全切換]]

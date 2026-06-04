---
title: AI 資安 — 幻方量化與 DeepSeek 關係
aliases: [幻方量化, High-Flyer, DeepSeek 商業模式, 開源作為武器]
type: summary
created: 2026-06-04
updated: 2026-06-04
sources:
  - raw/2026-04-06_幻方量化-deepseek關係.md
tags: [DeepSeek, 幻方量化, 中國 AI, 開源策略, 商業模式, 競爭結構]
confidence: high
---

# AI 資安 — 幻方量化與 DeepSeek 關係

**一句話核心**：DeepSeek 能免費開源並把 API 壓到 $0.28/M token，不是因為效率優勢，而是「母公司不靠模型賺錢」的結構性自由——這對 OpenAI/Anthropic 是直接的定價壓制，對中國 AI 是地緣資安籌碼。

## 重點摘要

### 幻方 = 量化基金（不是 AI 公司）

| 項 | 資料 |
|---|---|
| 全名 | 浙江九章資產管理（幻方量化 / High-Flyer） |
| 成立 | 2015 |
| 創辦人 | 梁文鋒 |
| 本業 | 量化對沖基金 |
| 基礎建設 | 「螢火超算」萬卡級 GPU |
| DeepSeek 分拆 | 2023/5，首期投資 30 億人民幣（約 $4 億）自有資金 |

DeepSeek **截至 2026 年仍拒絕外部融資**（包括阿里）——這是商業模式核心，不是傲慢。

### 為什麼能免費開源（結構性，不是技術）

1. 幻方的本業是量化交易，不是賣 AI
2. DeepSeek 模型反向服務幻方量化策略 → 內部 ROI 已回收
3. 幻方提供算力、資金、數據；DeepSeek 維持獨立研發
4. → 不需要靠模型營收活 → 可以把前沿模型免費開源

### 對比 OpenAI / Anthropic

| | DeepSeek | OpenAI | Anthropic |
|---|---|---|---|
| 模型營收依賴 | **不需要** | 核心收入 | 核心收入 |
| 能否免費開源 | **可以** | 不行（會摧毀自己） | 不行 |
| 資金來源 | 母公司自有 | 外部融資 $1,220 億 | 外部融資 |
| API 定價 | $0.28/M token | $15/M token | $15/M token |

### 「開源作為武器」模式

> 不靠 X 賺錢的公司把 X 免費送出去 → 壓縮靠 X 賺錢的公司

- Google 不靠模型 → 開源 Gemma → 壓縮付費模型
- Netflix 不靠工具 → 開源 VOID → 壓縮 Runway / Adobe
- **幻方不靠模型 → 開源 DeepSeek → 壓縮 OpenAI / Anthropic 的 API 定價**

### V4 訓練成本（2026）

- V3 訓練成本 **$520 萬**（業界同級數億美元）
- V4 改用**華為昇騰**晶片，降低對 NVIDIA 依賴
- 極低訓練成本 + 不需要營收回收 = **雙重結構性優勢**

## 產業/供應鏈延伸調查

### 1. 對美國 AI stack 的定價壓制

- **直接受害**：OpenAI / Anthropic 的 API 定價有「DeepSeek 比價」天花板
- **間接受害**：以「AI 推論單價」估值的軟體股——Salesforce Agentforce、ServiceNow Now Assist 等如果用內部模型，毛利率被預期下修
- **意外受惠**：Hyperscaler（[[AMZN]] AWS Bedrock、Azure OpenAI、Google Vertex）成為「模型 commodity 化的承載層」——分發護城河 > 模型護城河

### 2. 華為昇騰：中國 AI 算力供應鏈獨立

- DeepSeek V4 用昇騰訓練 = 中國驗證了 non-NVIDIA 訓練路徑可行
- 對 [[NVDA]] 中國市場 TAM 是長期下修壓力（但短期被出口管制鎖死，差異不明顯）
- 對 [[TSMC]]：昇騰晶片由中芯（SMIC）N+2 製程做，TSMC 的 China revenue 暴露已極小
- 真正的問題是 **non-China 國家** 是否會「想試試昇騰」——目前看不到，但要監控

### 3. 量化基金本業的 GPU 算力 → 兼差 AI 公司

這個 path 全球只有兩個典範：
- **幻方 → DeepSeek**（中國）
- **Renaissance / Two Sigma**（美國，但封閉用）

啟示：**GPU 算力 + 不依賴模型營收 = 開源破壞者的結構配方**。下一個破壞者可能來自：
- 不靠軟體賺錢的硬體巨頭（NVIDIA 自己？Cerebras？）
- 不靠 AI 賺錢的雲端（AWS Bedrock 自有 Nova 系列、Meta Llama）
- 不靠模型賺錢的科學機構（NIH、CERN）

### 4. 資安層的代價

- DeepSeek 的低定價不是「免費的午餐」——資料主權、跨境傳輸、政府調閱風險見 [[AI 資安 — DeepSeek 資安風險調查|DeepSeek 風險調查]]
- 對企業客戶：「便宜 50 倍」要扣除「合規 + 資安 + audit cost」
- 對國家：DeepSeek 開源權重在本地跑 = 中國 AI 軟實力擴散的免費通路（與 TikTok 對應）

## 與 wiki 概念的深度連結

| 主題 | concept |
|---|---|
| 跳出 DeepSeek 個案看「開源作為武器」的結構 | [[跳出個股看三層：產業、目的、供應]] |
| 為什麼市場一開始只看到「便宜 50 倍」是表面 | [[預期差]]、[[資訊擴散四階段]] |
| OpenAI 估值 $5,000 億是否撐得起 | [[PE 壓縮公式]]、[[Forward PE 估值法]] |
| Hyperscaler 受惠於 model commoditization | [[AI 通縮三路徑]] 的「商品化」一條 |
| 中國 AI 自主供應鏈（昇騰 + 中芯） | [[半導體基礎建設化]] 的中國版本 |

## 提案的新節點（主 agent 落地）

- entity：[[DeepSeek]]、[[幻方量化]]、[[華為昇騰]]、[[中芯（SMIC）]]、[[OpenAI]]、[[Anthropic]]
- concept：[[開源作為武器]]、[[模型商品化]]、[[中國 AI 風險定價]]、[[算力本業派 AI 公司]]

## 相關連結

- [[AI 資安 — DeepSeek 資安風險調查]]
- [[AI 資安 — Claude 4000 美元找到 22 個 Firefox 漏洞]]
- [[AI 通縮三路徑]]
- [[跳出個股看三層：產業、目的、供應]]
- [[預期差]]

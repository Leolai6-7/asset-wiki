---
title: 接口控制 — MCP 九千七百萬次安裝
aliases: [MCP 接口控制, Anthropic 搶接口, Model Context Protocol 投資視角]
type: summary
created: 2026-06-04
as_of: 2026-06-04
check_after: 2026-10-15
updated: 2026-06-04
sources:
  - raw/2026-04-06_MCP九千七百萬次安裝——Anthropic不是在賣模型是在搶接口.md
tags: [Anthropic, MCP, 接口控制, 協議層, 控制點轉移, AI 資安, Agent]
thesis_dependency: AI-capex
confidence: medium
---

# 接口控制 — MCP 九千七百萬次安裝

**一句話核心**：MCP 已不是技術標準競爭，是 **Anthropic 用開源協議拿下「AI 連接外部世界」的接口控制權**——所有 AI agent 要呼叫外部工具，都繞不開 Anthropic 定義的框架，但同時也讓 Anthropic 變成「9,700 萬個攻擊面的責任人」。

## 重點摘要

### 數字

- **2026-03**：9,700 萬次安裝（16 個月內，從零）
- **5,800 個社區伺服器**、**10,000 個生產環境伺服器**
- 全部支援：**OpenAI、Google、Microsoft、Salesforce**
- 捐給 Linux Foundation 底下的 **Agentic AI Foundation**（共同創辦人：Block、OpenAI；背後：AWS、Google、Microsoft、Snowflake）

### 控制點轉移：Anthropic 做了什麼

| 維度 | 前 | 後 |
|---|---|---|
| OpenAI function calling 地位 | 封閉、綁定自家 API、定義標準者 | 變成「也支援 MCP」的跟隨者 |
| Anthropic 自身地位 | AI 模型公司 | 協議層 + 模型層雙重控制 |
| 工具連接 | 各家各做、缺通用標準 | 全部說 MCP 的語言 |

> 類比：**Google 把 Chrome 開源（Chromium），Mozilla 用 Google 引擎、Edge 用 Google 引擎——「開源」不是放棄控制，是把控制點從產品層拉到協議層**。Anthropic 對 MCP 做了一樣的事。

### 風險：9,700 萬個攻擊面

- OWASP 已草擬 **「MCP Top 10 安全風險」清單**
- 核心架構問題：**AI 分不清「內容」和「指令」**——MCP 從外部抓郵件，郵件裡的惡意指令會被 AI 當成正常輸入處理
- 真實案例：**Postmark MCP 套件被植入後門**，一行程式碼讓所有透過套件發的郵件密送給攻擊者（密碼重置信、發票、內部備忘錄全外洩）
- **影子 MCP 伺服器**：極易部署、極難追蹤、IT 部門看不到→更新不了
- 「MCP 的安全問題不是能修補的——它們在架構層面」（Dark Reading）

## 產業／供應鏈延伸調查

### 1. MCP 生態的「真贏家」分層

| 層 | 角色 | 真贏家候選 | 投資推論 |
|---|---|---|---|
| **協議層** | 定義標準 | **Anthropic** | 已贏，但承擔系統性風險責任 |
| **執行層** | 連接、調度 tool call | 「tool scheduling」新賽道——callmux 類產品、agent OS | 早期，看誰先建護城河 |
| **應用層** | 用 MCP 接 SaaS 賣服務 | Notion、Asana、Block、Salesforce | 既有 SaaS 領導者直接受惠（用 MCP 鞏固生態） |
| **安全層** | MCP 資安 | **Wiz、CrowdStrike、Palo Alto、Cloudflare、Zscaler** | **「AI-SPM（AI Security Posture Management）」是 2026 新 SKU**——MCP 的攻擊面=這些公司的新 ARR 來源 |
| **基礎建設層** | 跑 MCP 的算力 | NVDA、AMD、TSMC、雲端（AWS、Azure、GCP） | 既有受惠者，與 MCP 普及正向相關 |

### 2. Anthropic 自身的三層控制點（投資視角）

從 raw 收集的 Anthropic entity（llm-wiki）已揭示其戰略：

| 層 | 控制點 | 商業變現 |
|---|---|---|
| ① 協議層 | MCP（9,700 萬安裝、產業標準） | 帶 Claude 流量 + 形塑 agent 生態語言 |
| ② 執行層 | Claude Managed Agents（Session/Harness/Sandbox 三層解耦） | $0.08/hr session 費，首批 Notion、Rakuten、Asana |
| ③ 客戶層 | 1,000+ 企業年付 >$1M | 年化營收 **$30B**（超越 OpenAI $25B） |

→ 對標：這是「**AI 作業系統公司**」估值模型，不是「AI 模型公司」。IPO 最早 10 月。

### 3. 對其他 AI 公司的競爭含義

- **OpenAI**：function calling 從「定義者」變「跟隨者」，戰略性讓步；估值 $852B 但 2026 虧 $140 億
- **Google**：自有 Gemini + Workspace 接口，但要在 MCP 框架內競爭，**生態主導力下降**
- **Microsoft**：Copilot 已支援 MCP，但策略上更靠 Azure infra 收費 → MCP 普及對 Azure 是中性偏正
- **Salesforce / 企業 SaaS**：透過 MCP 開放 Agentforce → 把自己的工具變成 agent 可呼叫對象，**鞏固而非削弱護城河**

### 4. 9,700 萬攻擊面 → 資安 ARR 大池

連結 [[AI 資安 — DeepSeek 資安風險調查]] 的延伸邏輯：

- 企業 procurement 開始問：「我們連了幾個 MCP？權限管理是否合規？」
- → 直接拉抬：
  - **Wiz**（Google 將以 $32B 收購）：CSPM 已在涵蓋 MCP 部署
  - **CrowdStrike (CRWD)**：威脅情報 + 端點，**AI agent 行為監控**新賽道
  - **Palo Alto Networks (PANW)**：Prisma Cloud + AI Access Security
  - **Cloudflare (NET)**：AI Gateway 集中監控 LLM/MCP 呼叫
  - **Zscaler (ZS)**：SSE 廠商，邊界阻擋高風險 MCP endpoint

- 投資推論：「**AI agent 普及 → 資安 ARR 結構性成長**」，這是 [[效率→安全切換]] 的清楚案例

### 5. 真正的尾部風險：一次大規模 MCP 安全事件

> 如果接下來 12 個月出現大規模 MCP 安全事件（不是理論風險，是真有公司因 MCP 漏洞丟客戶資料）——「AI 安全」這四個字的含義會徹底重新定義。

對市場的潛在衝擊：
- Anthropic 的「協議擁有者」聲譽風險
- 整個 agent 賽道的法規介入（EU AI Act 已有相關討論）
- **資安公司股價短期受惠**（恐慌驅動 ARR），但長期需要看法規方向
- 連結 [[三個風險指標]]：應將「AI agent 攻擊事件頻率」納入新指標

## 與 wiki 概念的深度連結

| 主題 | concept |
|---|---|
| 開源協議 = 把控制點從產品拉到協議層 | [[控制點轉移]]（Anthropic 是教科書案例） |
| 開源策略可持續性 | [[開源作為武器]]（Anthropic 模式 vs Meta 失敗模式） |
| 安全溢價驅動企業採購 | [[效率→安全切換]] |
| MCP 普及 = 對話接口取代搜尋排序 | [[AI 通縮三路徑]]（去中介化） |
| Anthropic 三層控制點是估值新模型 | [[Forward PE 估值法]]、[[DCF vs PE]] |
| 9,700 萬攻擊面是新「風險指標」 | [[三個風險指標]]（應擴張） |
| Agent 普及驅動賣水人 | [[賣水人選股邏輯]]、[[半導體基礎建設化]] |

## 提案的新節點（主 agent 落地）

- entity：Anthropic、MCP（Model Context Protocol）、Linux Foundation / AAIF、Wiz、CrowdStrike、Palo Alto Networks、Cloudflare、Zscaler
- concept：[[接口控制權]]、[[Agent 商品化]]（投資版）、[[AI 作業系統公司]]、[[AI Liability]]、[[AI-SPM（AI 安全態勢管理）]]

## 相關連結

- [[開源戰略 — Meta-Llama 帝國]]
- [[開源戰略 — Meta Muse Spark 閉源轉折]]
- [[開源戰略 — Netflix 第一個開源 AI 模型]]
- [[AI 資安 — DeepSeek 資安風險調查]]
- [[跳出個股看三層：產業、目的、供應]]
- [[效率→安全切換]]
- [[賣水人選股邏輯]]

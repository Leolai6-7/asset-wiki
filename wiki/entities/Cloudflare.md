---
title: Cloudflare
aliases: [Cloudflare, NET, NYSE:NET, Cloudflare Inc., Cloudflare Workers, Cloudflare One, Workers AI, R2, NET stock]
type: entity
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2026-12-09
expires_on: 2027-06-09
sources:
  - raw/2026-05-13_FOMOSOC-47-Cloudflare-agentic-AI-edge-control.md
  - https://www.fomosoc.com/p/aiagentic-ai-47cloudflare
  - https://www.cloudflare.com/
  - https://investors.cloudflare.com/
tags: [標的, 美股, AI 資安, Network 軌, SASE, Zero Trust, edge AI, Workers AI, R2, CDN, agentic AI, Network as Control Plane, 接口控制權]
confidence: medium
---

# Cloudflare（NYSE: NET）

## 1. 一句話定位

**全球 ~300 城市邊緣節點 + ~20% 全球網站流量通道 + 從 CDN/DDoS → Zero Trust → 邊緣 GPU 推論平台四階段演進 + 唯一橫跨 [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]] Network 軌 + 邊緣 AI 雙軌的「Network as Control Plane」anchor**——KP@FOMOSoc 第 47 期定位「**Cloudflare 是 AI 時代的神經網路**」：透過 330 個邊緣節點部署 GPU 直接執行 Llama / Stable Diffusion 等模型、把 agentic AI 從「**集中式大腦**」變成「**分散式全身反射弧**」；產品線從 **Workers**（邊緣運算引擎）→ **Workers AI**（邊緣 GPU 推論）→ **R2**（零傳出費儲存、打破 AWS egress 綁架）→ **Cloudflare One**（Zero Trust 架構）→ **Vectorize / Browser Rendering** 橫跨資安 + 邊緣 AI；對 [[CrowdStrike]] / [[Palo Alto Networks]] 是 platform 化整合的 Network 軌補位、對 [[Zscaler]]（SSE 市佔 34%、Cloudflare 不在前六）是純度落差；高盛 AI infra 報告列首選、但 **Q1 2026 後股價單日修正 -24%** = 市場分歧大、付費牆擋住具體商業化路徑 = confidence: medium。

## 2. 三層 thesis

### 產業層

- AI 資安賽道 [[市場四階段：懷疑／驗證／共識／反轉]] 在「**驗證 → 共識**」加速段、Cloudflare 在 Network 軌處於**獨特對沖位**：
  - 2010-2020：CDN + DDoS + WAF 為主（Akamai / Cloudflare 雙頭、Cloudflare 自由派 anchor）
  - 2020-2024：Zero Trust 興起（[[Zscaler]] SSE 龍頭 34%、Cloudflare + [[Palo Alto Networks]] 補位）
  - **2024-2026**：agentic AI 興起 + 邊緣推論需求爆炸 + Cloudflare Workers AI ramp + **R2 直接挑戰 AWS S3 egress fee**
  - **2026-2030**：「Network as Control Plane」隱含 thesis 驗證、Cloudflare 拿到 agentic AI 邊緣推論 API 標準制定權（若成立）
- AI 資安市場 ~$300B（2030）+ CAGR 12-15% [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]]
- **Cloudflare 跨兩個賽道**：
  - **Network 軌**（Zero Trust + SASE）：vs [[Zscaler]] SSE 34% / Cloudflare 不在前六 = **純度上落差大**
  - **邊緣 AI 軌**（Workers AI + R2）：vs AWS / Google Cloud 集中式 GPU = **物理優勢勝**
- 跟 [[接口控制權]] concept：Cloudflare 是「**物理層接口控制權**」投資側 anchor、[[接口控制權]] 原本以 MCP（協議層）為主例、Cloudflare 補位「**邊緣節點接口**」控制權
- 跟 [[控制點轉移（投資版）]]：三段控制點轉移
  - 第一階段：資料中心（AWS / Google 集中算力）
  - 第二階段：網路接口（Cloudflare CDN 最後一哩）
  - **第三階段：邊緣 GPU 節點（Cloudflare Workers AI）= agentic AI 主場**
- 跟 [[賣水人選股邏輯（投資版）]]：邊緣 GPU 推論 = agentic AI 賣水人（不押誰贏 agentic AI）、但 SSE 純度上 Zscaler 更接近 Zero Trust 賣水人首選
- 在 [[資訊擴散四階段]]：機構（高盛 AI infra 報告首選）→ 賣方（部分券商開始覆蓋邊緣 AI thesis）→ 媒體（agentic AI 邊緣推論未爆紅）→ ETF（CIBR / IHAK 部分持有但占比低）= **媒體層之前**，未進共識

### 目的層

- **核心業務結構**（FY2025 推估、付費牆擋住精確數字）：
  - **Subscription Revenue ~95%**（recurring、ARR 推估 $1.7B+ 對應 Forward 80-120x PE）
  - **Performance（CDN）**：傳統 base、毛利率最高、市佔穩定
  - **Security（Zero Trust + WAF + DDoS）**：核心成長段、跟 [[Zscaler]] 競合
  - **Developer Platform（Workers + R2 + Vectorize）**：高成長段、跟 AWS Lambda / S3 直接挑戰
  - **Workers AI**：2024-2026 ramp、ARR 占比待擴大、付費牆擋住具體數字
- **產品線詳細**：
  - **Workers**：邊緣運算引擎、330 城市部署、開發者首選邊緣 serverless
  - **Workers AI**：邊緣 GPU 推論、Llama / Stable Diffusion 預載、毫秒級回應
  - **R2**：**零傳出費（egress-free）**雲端儲存、明確 anchor「**打破 AWS 資料綁架**」
  - **Cloudflare One**：Zero Trust 架構、跟 [[Zscaler]] 競合
  - **Vectorize**：向量資料庫、agentic AI memory layer
  - **Browser Rendering**：headless browser API、agentic AI / scraping 受惠
  - **AI Gateway**：LLM 流量路由 + 監控、跟 LiteLLM 競合
- **客戶結構**：
  - SMB + 開發者 base（自由派 anchor）+ Fortune 500 大企業 Zero Trust 採購
  - 全球 ~300 城市覆蓋（含中國以外、地緣分散）
  - 政府 / 媒體 / 加密貨幣交易所 / SaaS 平台多元
- **2024-2026 量化 anchor**（KP 可見數字）：

| 指標 | 數值 | 意義 |
|---|---|---|
| 全球邊緣節點 | **~300 城市** | 物理結構性護城河、AWS 十多個 region 對比 |
| 全球流量通道 | **~20%** | 數據飛輪 anchor（攻擊數據訓練防禦）|
| Zscaler SSE 市佔 | **34%**（Cloudflare 不在前六）| Network 軌純度上落差 |
| 高盛 AI infra 報告定位 | **首選** | 機構共識的早期訊號 |
| Q1 2026 後股價單日修正 | **-24%** | 市場分歧大、Forward PE 80-120x 對 ramp 預期敏感 |

- 商業模式核心：
  - **「**邊緣節點密度 + 數據飛輪 + Zero Trust + Workers AI + R2 egress-free**」**五軸護城河
  - **數據飛輪**：免費用戶攻擊數據 → 訓練防禦 → 升級付費客戶安全等級（核心 anchor）
  - **物理結構**：300 城市邊緣節點是 5-10 年累積 CapEx、competitor 短期無法複製
  - **訂閱 recurring**：~95% subscription + 開發者 self-serve 黏性 + 企業 multi-year Zero Trust 合約
- 對應 [[賣水人選股邏輯（投資版）]]：**跨資安 + 邊緣 AI 雙軌賣水人**（不押誰贏 agentic AI、押所有 agentic AI 部署都需要邊緣推論）
- 對應 [[控制點轉移（投資版）]]：拿到「**邊緣節點接口 + Workers serverless 標準 + R2 egress-free anchor**」三段控制點、但**未拿到 Zero Trust 龍頭（Zscaler 34% 領先）**

### 供應層

- 跟 [[Zscaler]] 路線（**Zero Trust 直接對手 + Network 軌純度王**）：
  - **Zscaler SSE 市佔 34% vs Cloudflare 不在前六**（Dell'Oro 報告）= 純度上 Zscaler 勝
  - **Cloudflare One vs Zscaler ZTNA**：產品功能接近、Cloudflare 多了開發者 base + 邊緣節點密度
  - **客戶差異**：Zscaler 主打大企業 Fortune 500、Cloudflare 跨 SMB + Fortune 500 雙軌
  - **未來變數**：邊緣 AI ramp 後、Cloudflare 可能用「**Workers AI + Cloudflare One 整合**」差異化（Zscaler 無邊緣 GPU 能力）
- 跟 [[CrowdStrike]] 路線（**Endpoint 龍頭、跨軌 platform 整合**）：
  - CRWD Endpoint 30-32% + Charlotte AI agentic SOC、純度高
  - Cloudflare Endpoint 弱（無 endpoint agent）、Network 補位
  - **CRWD + Cloudflare 結構性互補**：CRWD endpoint + Cloudflare network 是 Fortune 500 客戶常見組合（vs Microsoft Defender + Microsoft 365 bundled）
- 跟 [[Palo Alto Networks]] 路線（**三軌全覆蓋對手**）：
  - PANW 三軌全覆蓋（Endpoint + Cloud + Network）+ Cortex XSIAM agentic SOC
  - Cloudflare Network 軌 + 邊緣 AI 補位
  - **PANW vs Cloudflare**：PANW 大企業 NGFW 30-35% 領先、Cloudflare SMB + 開發者 base 領先、估值上 PANW Forward PE 50-60x vs Cloudflare 80-120x = Cloudflare 純度溢價 + 成長預期
- 跟 [[Microsoft]] Defender / Azure Front Door 路線（**bundle 威脅**）：
  - Microsoft Azure Front Door + Microsoft Defender bundled 進 Azure = Microsoft 客戶優先選 Microsoft
  - Cloudflare 護城河：**獨立 + 多雲（不綁定 Azure / AWS / GCP）**、SMB / 開發者 / 加密貨幣 base 強
- 跟 AWS 路線（**多軌競合**）：
  - AWS Lambda@Edge + Wavelength 已在邊緣部署 = **AWS 反擊邊緣 AI 主場**
  - R2 直接挑戰 AWS S3 egress fee（核心對撞 anchor）
  - **AWS 護城河**：GPU 集中算力 + AI training 主場、Cloudflare 邊緣推論差異化
  - **客戶差異**：AWS Fortune 500 大企業集中、Cloudflare SMB + 開發者 base 強
- 跟 Akamai 路線（**傳統 CDN 對手、被打敗**）：
  - Akamai 老牌 CDN、傳統 enterprise 客戶
  - Cloudflare 開發者友善 + 自由派 anchor + 數據飛輪 → 對 Akamai 結構性勝
- 跟 Fastly 路線（**邊緣運算二線玩家**）：
  - Fastly Compute@Edge + 開發者 base、規模小
  - Cloudflare 規模 + 物理結構 + 多元產品線勝
- 護城河：
  - **300 城市邊緣節點物理結構**（5-10 年 CapEx 累積、competitor 短期無法複製）
  - **數據飛輪**（免費用戶攻擊數據 → 訓練防禦 → 付費客戶安全升級）
  - **R2 egress-free**（打破 AWS 資料綁架的 anchor 產品）
  - **Workers AI 邊緣 GPU 部署**（agentic AI 物理優勢）
  - **獨立多雲**（不綁定 Azure / AWS / GCP、地緣政治 + 客戶選擇度勝）
- 風險：
  - **Zscaler SSE 34% 純度領先 + Cloudflare 不在前六**：Network 軌純度落差大
  - **AWS Lambda@Edge + Wavelength 反擊**：AWS 在邊緣 AI 直接競爭
  - **agentic AI 商業化進程不透明**（KP 付費牆後才揭示具體 monetize 路徑）
  - **Forward PE 80-120x 高估值**：對 ramp 預期敏感、Q1 後 24% 修正反映市場分歧
  - **Workers AI GPU 邊際成本結構不透明**：GPU 密集、毛利率可能下行
  - **Microsoft Azure Front Door bundle 威脅**：大企業 Azure 客戶優先選 Microsoft
  - **股價波動率高**：自由派 anchor + 加密貨幣交易所客戶 + agentic AI narrative = 多重波動因素疊加

## 3. 財務狀態快照（As of 2026-06-09，付費牆擋住精確數字 → 多項推估）

| 指標 | 數值 |
|---|---|
| 股價（推估） | USD ~70-100（Q1 後從 ~$130 修正 -24% 至 ~$100、再回升至 ~$80-100 區間）|
| 市值（推估） | **USD ~25-35B** |
| 上市場別 | NYSE（NET）|
| FY2025 全年營收（推估） | **USD ~1.7B**（YoY +25-30%）|
| FY2025 全年 OP 利潤率（推估） | 5-10%（投資期）|
| ARR（推估） | **USD ~1.7B**（YoY +25-30%）|
| Forward PE（推估） | **80-120x**（high growth + agentic AI 預期）|
| 12M 漲幅 | +30-80%（波動大、Q1 後 -24% 單日修正後回升）|
| 全球邊緣節點 | **~300 城市** |
| 全球流量通道 | **~20%** |
| 高盛 AI infra 報告定位 | **首選** |
| Zscaler SSE 市佔對比 | Cloudflare 不在前六（SSE 34% by Zscaler）|

> ⚠️ **付費牆擋住具體 ARR / Forward PE / Workers AI 業務拆分**——上表 ARR / Forward PE 為推估、需後續確認。建議查 NET investor relations IR 頁與 10-Q / 10-K 更新數據。

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ Subscription ~95% + recurring + 多元產品線 + 開發者 base 黏性 |
| 毛利率 | ⚠️ Workers AI GPU 邊際成本不透明、可能下行（需確認）|
| OpEx | ⚠️ 300 城市邊緣節點 CapEx + Workers AI GPU 部署 + R&D 投入大 |
| 營業利益 | ⚠️ OP 5-10% 仍在投資期、Forward PE 80-120x 已 price in 多年 ramp |

→ **Re-rate 三角形 2/4 滿** —— 跟 [[GlobalFoundries]] 2/4 / [[Amkor]] 2/4 / [[南電]] 2/4 同級；**buy 的是「**300 城市邊緣節點 + 數據飛輪 + Workers AI agentic AI 賣水人 + R2 egress-free anchor**」結構性護城河**、不是當下財務 quality。

### ✅ 催化

- **Workers AI ARR ramp**（agentic AI 邊緣推論商業化）
- **R2 egress-free 客戶遷移 AWS S3 加速**（成本對撞 anchor）
- **Cloudflare One Zero Trust 大企業合約滲透**（vs Zscaler 純度競爭）
- **AI Gateway 成為 LLM 路由標準**（潛在 chokepoint）
- **agentic AI 邊緣 GPU 推論 ramp 驗證物理優勢**
- **高盛 AI infra 首選持續性確認 + 賣方覆蓋擴大**
- **股價 Q1 後 24% 修正 + 反彈 = 市場分歧期反向 alpha 機會**（純市場觀察、非交易判斷）

### ⚠️ 風險

- **Zscaler SSE 34% 純度領先 + Cloudflare 不在前六**：Network 軌純度落差大
- **AWS Lambda@Edge + Wavelength 邊緣反擊**：AWS 在邊緣 AI 直接競爭
- **agentic AI 商業化進程不透明**（KP 付費牆擋住具體 monetize 路徑）
- **Forward PE 80-120x 高估值**：對 ramp 預期敏感、未來 1-2 個季報 miss 即重 de-rating
- **Workers AI GPU 邊際成本結構**：GPU 密集毛利率下行風險
- **Microsoft Azure Front Door bundle**：Azure 客戶優先選 Microsoft
- **股價波動率高**：Q1 後 24% 單日修正反映市場分歧大、適合長期 buy-and-hold 而非短期 swing
- **Cloudflare 自由派 anchor 客戶結構**（加密貨幣交易所 / 媒體）地緣政治敏感

## ⭐ Network as Control Plane（KP 隱含核心 anchor）

### 三段控制權轉移

| 時代 | 控制權位置 | 代表 | 估值溢價 |
|---|---|---|---|
| 傳統雲端 | **資料中心**（最大運算）| AWS / Google | 已 price in（大 PE）|
| 邊緣 | **網路接口**（最後一哩）| **Cloudflare CDN/Zero Trust** | 已 price in（PE ~80x）|
| **Agentic AI** | **邊緣 GPU 推論節點**（毫秒級決策）| **Cloudflare Workers AI** | **未 price in**（KP 隱含 alpha 來源）|

→ AI agent 需要毫秒級決策、不能每次都往美國跑 → Cloudflare 330 城市 GPU 節點直接在邊緣「思考」 = 把神經網路從**集中式大腦**變成**分散式全身反射弧**。

> 「**誰能在用戶最近的地方提供最低延遲的 AI 推論、誰就能決定下一代互聯網應用的 API 標準、資料格式、安全規則**」—— KP 隱含 thesis

### 為什麼這是新控制點

1. **物理優勢**：銅互聯 / 集中式 GPU 無法滿足毫秒級延遲、邊緣 GPU 是物理唯一解
2. **數據飛輪**：300 城市邊緣節點 = 全球 20% 流量數據 = 訓練邊緣模型優勢
3. **獨立多雲**：Cloudflare 不綁定 Azure / AWS / GCP = 客戶選擇度勝
4. **R2 egress-free + Workers AI 邊緣推論**：成本 + 物理雙重結構優勢

### 對應 [[接口控制權]] concept

- [[接口控制權]] 原本以 MCP（協議層）為主例
- Cloudflare = **物理層接口控制權**投資側對應
- 兩者互補：協議層（MCP）+ 物理層（Cloudflare）= AI 時代接口控制權雙軌

## ⭐ AI 資安戰場 Network 軌補位

### Network SASE/NGFW 軌完整地圖（補強 [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]]）

| 思路 | 標的 | 五軸（推估）|
|---|---|---|
| 三平台整合 + NGFW 始祖 | **[[Palo Alto Networks]]**（PANW）⭐ | 20/25 |
| SSE pure-play | **[[Zscaler]]**（ZS）| 待建（推估 18-19/25）|
| **邊緣網路 + AI Gateway + Workers AI** ⭐ | **[[Cloudflare]]**（NET）⭐ 本次新建 | **本次評分 16/25** |
| NGFW 中小企業 | Fortinet（FTNT）| 待建 |

→ **Cloudflare Network 軌補位完成、但純度上不如 Zscaler、廣度上不如 PANW、邊緣 AI 上獨佔**

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| **路線敏感度（逆向）** | **3 / 5** | agentic AI + Zero Trust + 邊緣 AI 多軌曝險、但 Zero Trust 純度上 Zscaler 領先、agentic AI 商業化未驗證 |
| **站別關鍵度** | **3 / 5** | 300 城市邊緣節點物理結構性護城河 + 20% 全球流量、但 SSE 市佔不在前六、Workers AI 邊緣 GPU ramp 未驗證 |
| **耗材 recurring** | **5 / 5** ⭐ | Subscription ~95% + 開發者 self-serve 黏性 + 企業 multi-year Zero Trust 合約 + R2 / Workers usage-based |
| **IP 控制** | **2 / 5** | Workers serverless 標準 + R2 egress-free anchor、但無深度 IP chokepoint（vs Cisco 路由 IP / [[Coherent]] InP fab）|
| **客戶分散** | **3 / 5** | SMB + 開發者 + Fortune 500 多元、無單一 > 10%、但自由派 anchor 客戶（加密貨幣 / 媒體）地緣風險 |

**總分 = 16 / 25** —— 跟 [[國巨]] 18 / [[Nokia]] 18 略低、跟 [[CrowdStrike]] 21 / [[Palo Alto Networks]] 20 落差明顯；**Network 軌補位 anchor**（agentic AI 邊緣推論獨佔切角）、但**純度上 Zscaler / 廣度上 PANW / 估值上 Forward PE 80-120x 高位** 三軸壓制。

### vs Zscaler / Palo Alto Networks / CrowdStrike 對照（三軌核心對比）

| 玩家 | 主軌 | 五軸總分 | Forward PE | ARR | 關鍵差異 |
|---|---|---|---|---|---|
| [[CrowdStrike]] | Endpoint EDR/XDR | **21/25** ⭐ | 60-80x | $4.2B | endpoint 純度王 + Charlotte AI |
| [[Palo Alto Networks]] | Network NGFW/SASE | **20/25** ⭐ | 50-60x | $4.5B | 三軌全覆蓋唯一 + Cortex XSIAM first-mover |
| Zscaler（待建）| Network SSE | 推估 18-19 | 50-70x | ~$2.3B | SSE 純度王 34% |
| **Cloudflare** | **Network + Edge AI** | **16/25** | **80-120x** | **~$1.7B** | **agentic AI 邊緣推論獨佔 + R2 egress-free** |

→ **Cloudflare 五軸總分 16 在三軌中最低**、但「**Network as Control Plane**」隱含 thesis 若驗證 → Forward PE 80-120x 可能成立、否則 Q1 後 24% 修正可能延續。

## 跟其他 wiki 概念連結

- [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]]：**Network SASE/NGFW 軌補位 anchor**（之前列名、本次正式建檔）
- [[接口控制權]]：**物理層接口控制權**投資側對應（vs MCP 協議層）
- [[控制點轉移（投資版）]]：三段控制點轉移（資料中心 → 網路接口 → 邊緣 GPU 節點）
- [[賣水人選股邏輯（投資版）]]：跨資安 + 邊緣 AI 雙軌賣水人
- [[Jevons Paradox（投資版）]]：邊緣推論成本下降 → agentic AI 部署密度上升 → 邊緣 GPU 節點用量爆炸
- [[半導體基礎建設化]]：邊緣 GPU 節點 = AI infra 邊緣層基礎建設
- [[市場四階段：懷疑／驗證／共識／反轉]]：Cloudflare 在「**驗證 → 共識**」加速段、媒體層之前
- [[資訊擴散四階段]]：機構（高盛 AI infra 首選）→ 賣方擴大覆蓋 → 媒體未爆紅 → ETF 部分持有
- [[CrowdStrike]] / [[Palo Alto Networks]] / [[Microsoft]]：三軌互補 / 對手
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 完整套用三段式

## 相關連結

- [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]]
- [[接口控制權]]
- [[控制點轉移（投資版）]]
- [[賣水人選股邏輯（投資版）]]
- [[Jevons Paradox（投資版）]]
- [[半導體基礎建設化]]
- [[CrowdStrike]]
- [[Palo Alto Networks]]
- [[Microsoft]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[資訊擴散四階段]]
- [[FOMO SOC]] / KP@FOMOSoc（KOL 來源、待建）

## Sources

- [Cloudflare 官網](https://www.cloudflare.com/)
- [Cloudflare Investor Relations](https://investors.cloudflare.com/)
- [FOMO SOC 第 47 期：Cloudflare（2026-05-13）](https://www.fomosoc.com/p/aiagentic-ai-47cloudflare)

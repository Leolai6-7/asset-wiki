---
title: CrowdStrike
aliases: [CRWD, CrowdStrike Holdings, NASDAQ:CRWD, Falcon, Charlotte AI, NASDAQ CRWD]
type: entity
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2027-01-15
expires_on: 2027-06-09
sources:
  - https://www.crowdstrike.com/
  - https://ir.crowdstrike.com/
  - https://www.crowdstrike.com/en-us/blog/falcon-platform-charlotte-ai/
tags: [標的, 美股, AI 資安, EDR, XDR, SIEM, agentic SOC, Charlotte AI, Falcon, cloud security, identity, Microsoft Defender, Wiz, AI-SPM, NASDAQ, Mega Cap]
thesis_dependency: AI-capex
confidence: high
---

# CrowdStrike（NASDAQ: CRWD）

## 1. 一句話定位

**雲原生 EDR / XDR 龍頭 + Falcon 單一 agent 多模組 platform 開創者 + Charlotte AI agentic SOC 龍頭 + 2024-07 Microsoft Windows 全球當機事件後從信任低谷完成股價 recovery + Fortune 500 60%+ AVL**——總部 Austin TX、創立 2011、2019-06 IPO；旗艦產品 **Falcon platform**：單一 lightweight agent + 28+ 模組（EDR / XDR / NGAV / Identity Protection / Cloud Workload / SIEM Next-Gen / Vulnerability Management / Charlotte AI 等），透過 **Threat Graph**（每天 trillion+ events）做行為基線；訂閱制 ARR $4.2B+（FY2026 Q4）+ NRR 110%+ + free cash flow margin 30-35%；2024-07-19 **Falcon Sensor 7.11 配置檔錯誤推送導致全球 8.5M Windows 機器藍屏當機 + $10B 損失 + Delta Airlines $500M 索賠官司** → 一度動搖「single agent platform 信任前提」、但 12-15 個月後客戶留存率 **97%+ 不變** + 股價從低點 $200 區間回升到 $400-500 區間；**Charlotte AI**（GenAI 助手、2023 GA、2025-2026 升級到 agentic SOC）= alert triage 自動化 + investigation prompt + IR playbook generation 三軌；對手競爭加劇：**Microsoft Defender for Endpoint**（已 bundled 進 M365 E5）+ **SentinelOne**（純 EDR pure-play + 開源 telemetry friendly）+ **Wiz**（Cloud Security + Google $32B 收購 anchor）= 三線壓力但 CRWD 護城河仍是 **single agent + Threat Graph 數據規模 + Falcon Foundry**；[[AI 資安攻防成本曲線]] **Endpoint / XDR 賽道核心 anchor**、[[賣水人選股邏輯（投資版）]] AI 資安賽道（CRWD / PANW / NET / ZS / Wiz）首推。

## 2. 三層 thesis

### 產業層

- AI 資安市場 [[市場四階段：懷疑／驗證／共識／反轉]] 處於「**驗證 → 共識**」加速段：
  - 2010-2020：傳統 SIEM + perimeter firewall 主導（Cisco / Check Point / FireEye）
  - 2020-2024：cloud 化 + EDR 興起、CRWD / S / Microsoft Defender 三家分食 endpoint 60%+ 市佔
  - **2024-2026**：AI 加速 SOC 自動化 + agentic SOC 興起 + Microsoft Defender 平台化威脅升級 + Wiz $32B anchor + 資安市場進入「**AI 重構期**」
  - **2026-2030**：AI 加速攻防雙引擎（GenAI 釣魚 + LLM 漏洞發現）→ 資安總支出**結構性 ↑**（非降）= [[AI 資安攻防成本曲線]] 核心 thesis
- AI 資安市場 ~$300B（2030）+ CAGR 12-15%（Gartner）= AI 半導體 ~$1T 市場的 1/3 規模、被遺忘的 AI 受惠者
- **三軌分食格局**：
  - **Endpoint EDR / XDR**：CRWD / SentinelOne / Microsoft Defender（CRWD 仍 30-35% endpoint 市佔龍頭）
  - **Cloud Security CSPM**：Wiz（私募）/ Lacework / Sysdig / Prisma Cloud（PANW 子）
  - **Network SASE / NGFW**：PANW / Zscaler / Cloudflare / Fortinet
- 三軌玩家**會逐漸平台化整合**（CRWD Falcon = endpoint + cloud + identity / PANW = 三平台 + SecOps Cortex / Microsoft Defender = bundled）= 客戶「3-5 家整合方 + niche AppSec」格局
- 對應 [[效率→安全切換]]：資安從「奢侈品」變「剛需」、ARR 長期不可逆 + 平台化 lock-in 增加
- 對應 [[賣水人選股邏輯（投資版）]]：**AI 資安賽道是「中性受惠 AI CapEx 擴張的賣水人」**——不押 LLM / agent 誰贏、押所有 AI 部署都需要資安覆蓋
- 跨庫對接 llm-wiki [[AI 資安研究]] + [[責任歸屬（AI Liability）]]：CRWD Falcon 是「**model layer 守毛利的下游基礎建設**」——LLM 漏洞 / 釣魚加速攻擊 → CRWD 防守側 ARR 暴增
- 在 [[資訊擴散四階段]]：機構（已大量持倉）→ 賣方（高盛 / 摩根士丹利 / 摩根大通持續推薦）→ 媒體（2024-07 當機事件後再度焦點）→ ETF（CIBR / IHAK / HACK 已重倉）= 多階段資訊已擴散、但 12-15 個月後的 Microsoft Defender / Wiz 路線分歧仍未完全 price in

### 目的層

- **核心業務結構**（FY2026 → FY2027 推估）：
  - **Subscription Revenue**：**~95% 營收**（ARR $4.2B+ FY2026 Q4、訂閱制 100% high gross margin 80%+）
  - **Professional Services + Training**：~5% 營收（IR 應變、訓練、認證）
- **Falcon platform 模組分布**（27+ modules、FY2026 Q4）：
  - **Falcon Insight（EDR / XDR）**：核心 anchor 模組、ARR 估 $1.5B+
  - **Falcon Prevent（NGAV）**：endpoint 基礎防護
  - **Falcon Identity Protection**：身份是新邊界、$200M+ ARR、跟 Okta / CyberArk 競合
  - **Falcon Cloud Security**：CSPM + CWPP、$500M+ ARR、跟 Wiz / Prisma Cloud 競爭
  - **Falcon LogScale（SIEM Next-Gen / Humio 併購）**：Splunk 直接競爭、$200M+ ARR
  - **Falcon Charlotte AI（GenAI 助手）**：alert triage + investigation + IR playbook 三軌、嵌入所有模組
  - **Falcon Foundry（cloud workload 防護）**：2025 新發布、跟 Wiz 直接競爭
- **客戶結構**：
  - **Fortune 500 60%+ AVL**（業界最高）+ Fortune 100 70%+
  - 政府 / 國防（US DoD + 多國 5 Eyes）+ Financial Services + Healthcare 三大垂直
  - **客戶分散**：Top 10 客戶 < 10% 營收、無單一客戶 > 2%、結構性護城河
  - **訂閱黏性**：NRR **110%+**（業界中等偏高）+ 客戶留存率 **97%+**（2024-07 當機事件後仍維持）
- **2024-07 全球當機事件影響**：
  - **2024-07-19 凌晨 04:09 UTC**：Falcon Sensor 7.11 配置檔（Channel File 291）錯誤推送
  - **影響**：全球 8.5M Windows 機器藍屏（Crowdscope Blue Screen of Death）
  - **直接損失**：$10B+ 全球（航空 / 醫療 / 銀行 / 物流大規模停擺）
  - **Delta Airlines $500M 索賠官司**（仍進行中、2026 H2 預期庭審）
  - **股價影響**：當日 -11% / 4 週累計 -40%（$345 → $200）/ 12 個月後回升 $400+ / 18 個月後 recovery 完成
  - **客戶留存率 97%+ 不變**：核心 thesis「**single agent + Threat Graph 規模 lock-in 太深、客戶無法 switch out**」驗證
  - 政策成本：CRWD 增加 **staged rollout + canary testing + 客戶可控制 update 速度**（補強流程）
- **2026 全年 guidance**（管理層）：
  - **ARR FY2026 末 $4.7-4.9B**（YoY +18-22%）
  - **Revenue FY2026 $4.45-4.55B**（YoY +20-22%）
  - **Subscription Revenue Growth FY2026 +22-25%**
  - **Free Cash Flow Margin 30-35%**（業界頂級）
  - **NRR 110%+ 維持**
- 商業模式核心：
  - **「**Single Agent + Multi-Module Platform + Threat Graph Data + Charlotte AI 自動化**」**四軸護城河
  - **規格控制權**：endpoint 內 lightweight agent + cloud-based Threat Graph 處理 = 競爭對手要做 single agent 需重建整個架構（Microsoft Defender 雖 bundled 但 multi-agent + perimeter）
  - **數據護城河**：Threat Graph 每天 trillion+ events 訓練行為基線 = AI 模型品質**領先 SentinelOne 1-2 年**
  - **訂閱 recurring**：ARR 主體 + NRR 110%+ + 客戶留存 97%+ = 長期現金流可預測
  - **平台 lock-in**：客戶從 1-2 個模組 → 5-7 個模組（CRWD 「modules per customer」每年穩定增長）
- 對應 [[賣水人選股邏輯（投資版）]]：**AI 資安賣水人**（不押 LLM 誰贏、押所有 AI 部署都需要 endpoint 防護）
- 對應 [[控制點轉移（投資版）]]：拿到「**endpoint single agent 規格定義 + Threat Graph 數據規模 + Charlotte AI agentic SOC 標準**」三段控制點

### 供應層

- 跟 [[Microsoft]] Defender 路線（**最直接對手 + 平台 lock-in 威脅**）：
  - **Microsoft Defender for Endpoint** bundled 進 M365 E5 = **零邊際成本**（Microsoft 客戶可選 bundled = CRWD 失去新單機會）
  - **2024-2026 Microsoft Defender 滲透率提升**：E5 E5 自從 2024 拿到 endpoint 市佔 25-30%、CRWD 從 35% 略下滑到 30-32%
  - **CRWD 反擊策略**：(1) Falcon Foundry cloud workload 防護（Microsoft Defender 弱項）+ (2) Charlotte AI agentic SOC（Microsoft Security Copilot 平行賽道）+ (3) Threat Graph 數據規模（Microsoft Defender 仍弱於 CRWD 數據護城河）
  - **競爭結果**：**雙頭格局**（CRWD 30-32% / Microsoft Defender 25-30%）+ SentinelOne 10-15% 第三 = 三家分食 70%+
  - **CRWD 路線敏感度扣分**：Microsoft Defender bundle 是 CRWD 五軸「路線敏感」失分主因
- 跟 [[Palo Alto Networks]] 路線（**平台化競合 + 估值對照**）：
  - **PANW 三平台策略**：Network Security（NGFW + SASE Prisma）+ Cloud Security（Prisma Cloud）+ SecOps（Cortex XDR + XSIAM）
  - **CRWD vs PANW**：CRWD endpoint pure-play + 純度高 / PANW 三平台廣度 + 多軌覆蓋
  - **估值對比**：CRWD Forward PE **60-80x** vs PANW Forward PE **50-60x**（CRWD 純度溢價）
  - **客戶重疊**：Fortune 500 客戶 90%+ 同時使用 CRWD endpoint + PANW NGFW/SASE = **互補而非零和**
- 跟 [[Wiz]] 路線（**Cloud Security 收購 anchor + 私募估值上限**）：
  - **Wiz 私募估值**：2025-09 Google $32B 全額收購（cash deal）= 雲端 CSPM 市場 anchor 估值（vs PANW Prisma Cloud / CRWD Falcon Cloud Security 對標）
  - **CRWD Falcon Cloud Security**：$500M+ ARR、跟 Wiz 直接競爭、但 Wiz 純度更高（cloud-only）
  - **Wiz 整合進 Google Cloud 後**：CRWD 在 Google Cloud 客戶端劣勢增加、但 Microsoft Azure / AWS 客戶 CRWD 優勢仍在
  - **對 CRWD 估值影響**：Wiz $32B 是 CRWD Cloud Security 業務的 valuation anchor、隱含 CRWD 整體市值有 SoP 折價空間
- 跟 SentinelOne（NYSE: S）對比（**EDR pure-play 對手**）：
  - **規模**：CRWD ARR $4.2B vs S ARR $850M（**CRWD 5x 規模**）
  - **客戶**：CRWD Fortune 500 60%+ AVL vs S Fortune 500 30%+ AVL
  - **開源 telemetry**：S 開源 telemetry friendly + Snowflake 整合（CRWD Threat Graph 是封閉黑盒）= S niche 角度
  - **結果**：S 是 CRWD 的「窮人版替代品 + 開源 friendly」、雙方在中型企業 / 政府客戶有競爭
- 跟 [[Cloudflare]] / [[Zscaler]] 對比（**SSE / SASE 互補關係**）：
  - NET / ZS 是「網路邊界 + SSE」、CRWD 是「endpoint」= **不同層級互補**
  - 客戶通常會「**CRWD endpoint + ZS/NET SSE + PANW NGFW**」組合（3-4 家賣水人）
- 跟 Splunk（Cisco 子）/ Datadog 對比（**Security Analytics 重疊**）：
  - CRWD Falcon LogScale 直接競爭 Splunk SIEM（Cisco 2024 完成併購 Splunk）
  - Datadog observability 偏 DevOps、跟 CRWD 互補大於競爭
- 跟 [[Okta]] / CyberArk 對比（**Identity Protection 競合**）：
  - CRWD Falcon Identity Protection（Preempt 2020 併購）→ 跟 Okta / CyberArk 部分競爭
  - Okta 純度更高（identity pure-play）+ Workforce Identity 龍頭、CRWD 在 endpoint + identity 整合有獨家優勢
- 護城河：
  - **Single agent 架構**：lightweight agent + cloud 處理 = 無對手能複製（Microsoft Defender 仍 multi-agent）
  - **Threat Graph 數據規模**：trillion+ events/day + 行為基線 AI 模型 = 訓練數據護城河
  - **客戶留存 97%+ + NRR 110%+**：訂閱黏性 + 平台 lock-in
  - **Charlotte AI / Falcon Foundry**：agentic SOC + cloud workload 兩條新增成長軌
  - **Fortune 500 60%+ AVL**：業界最高 AVL = 高黏性高客單價
- 風險：
  - **Microsoft Defender 平台 lock-in 威脅**（最大風險、五軸路線敏感扣分主因）
  - **Wiz 整合進 Google Cloud 後 Cloud Security 競爭加劇**
  - **2024-07 當機事件 Delta $500M 官司**（仍進行中、2026 H2 庭審、賠償金額不確定）
  - **估值已 price in**（Forward PE 60-80x、Re-rate 已多走）+ 任何 NRR / 客戶留存率 / ARR 增長放緩都會引發 PE 壓縮
  - **AI 攻防雙引擎雙刃劍**：GenAI 加速攻擊（CRWD ARR ↑）+ GenAI 加速 IR / SOC 自動化（CRWD 高黏性 ↑）但同時 hyperscaler agentic SOC（Microsoft Security Copilot）會搶 SOC 訂閱
  - **agentic SOC 戰場進入 2026 高峰**：Charlotte AI vs Microsoft Security Copilot vs PANW Cortex XSIAM 三方混戰、CRWD 須證明 Charlotte AI 領先

## 3. 財務狀態快照（As of 2026-06-09，FY2026 Q4 法說會 anchor）

| 指標 | 數值 |
|---|---|
| 股價（推測）| ~$400-500（2026 上半年區間，**Forward PE 60-80x**）|
| 市值（推測）| **~$110-130B**（Mega Cap） |
| 上市場別 | NASDAQ |
| FY2026 Q4 ARR | **$4.2B+**（YoY +20-22%）|
| FY2026 Revenue | **$4.45-4.55B**（guidance、YoY +20-22%）|
| FY2026 Subscription Growth | **+22-25%** |
| FY2026 末 ARR guidance | **$4.7-4.9B**（YoY +18-22%）|
| **NRR** | **110%+** |
| **Free Cash Flow Margin** | **30-35%**（業界頂級）|
| **客戶留存率** | **97%+**（2024-07 當機事件後仍維持）|
| **Fortune 500 AVL** | **60%+**（業界最高）|
| **Modules per customer** | **多模組客戶 65%+**（4+ modules）|
| 員工數 | 8,500+（FY2026 Q4）|
| 累計虧損 | 已轉盈（FY2024 GAAP 淨利轉正）|

### Re-rate 三角形

| 項目 | 狀態 |
|---|---|
| 營收品質 | ✅ ARR $4.2B + NRR 110%+ + 客戶留存 97%+ + Fortune 500 60%+ AVL + 訂閱 95% |
| 毛利率 | ✅ 訂閱毛利率 80%+（雲端 SaaS 業界頂級）|
| OpEx | ⚠️ Charlotte AI + Falcon Foundry R&D 加碼 + 銷售費用維持 30%+ |
| 營業利益 | ✅ GAAP 轉正 + Free Cash Flow Margin 30-35% + 營業槓桿釋放中 |

→ **Re-rate 三角形 3/4 滿** —— 跟 [[Vertiv]] / [[Ciena]] / [[Bloom Energy]] 等成長型 anchor 同級、**buy 的是「endpoint single agent 龍頭 + Charlotte AI agentic SOC 規格參與權 + 2024-07 當機事件後信任 recovery + ARR + NRR + 客戶留存三軸全綠」三軸結構性 anchor**。

### ✅ 催化

- **2026 H2 Charlotte AI 升級** ⭐：agentic SOC 全棧自動化（alert triage → investigation → IR playbook → remediation）、嵌入所有 28+ 模組、跟 Microsoft Security Copilot / PANW Cortex XSIAM 三方混戰
- **2026 H2 Falcon Foundry 量產** ⭐：cloud workload 防護、跟 Wiz / Prisma Cloud 直接競爭、$200M+ ARR 預期
- **2026 H2 - 2027 H1 Fortune 500 AVL 從 60% → 65%+**：新進產業客戶（製造 / 能源 / 公用）
- **2026 H2 Identity Protection ARR 從 $200M → $300M+**：跟 Okta / CyberArk 競爭加劇
- **2026 Q4 - 2027 Q1 Microsoft Defender 反擊**：CRWD 從 SMB 端 + agentic SOC 雙線守住 Fortune 500
- **2027 Delta Airlines $500M 官司結案**：若賠償 < $200M = 股價催化、若 > $500M = 股價壓力

### ⚠️ 風險

- **Microsoft Defender bundle**（M365 E5 bundled、SMB 端 + Fortune 500 端雙頭壓力）— 路線敏感主因
- **Wiz 整合進 Google Cloud**（CRWD Falcon Cloud Security 市佔流失到 GCP 客戶）
- **Delta Airlines $500M 官司**（2026 H2 庭審、賠償金不確定）
- **估值已 price in**（Forward PE 60-80x、Re-rate 已多走、ARR 任何放緩會引發 PE 壓縮 20-30%）
- **AI 攻擊端 LLM 釣魚 / 漏洞發現加速**（短期 ARR ↑、長期防守側「捕捉勝率」可能下滑）
- **agentic SOC 戰場 2026-2027 競爭白熱化**：Charlotte AI vs Microsoft Security Copilot vs PANW Cortex XSIAM 三方混戰

### 五軸打分（賣水人選股邏輯 25 分制）

| 軸 | 分數 | 說明 |
|---|---|---|
| **路線敏感度（逆向）** | **3** | Microsoft Defender bundle 威脅 + endpoint single agent 路線分歧（vs SentinelOne 開源 telemetry） |
| **站別關鍵度** | **5** | endpoint EDR / XDR 是 AI 資安最必經之路（所有 AI 部署都需要） |
| **耗材 recurring** | **5** | ARR 95% 訂閱 + NRR 110%+ + 客戶留存 97%+ + Modules per customer 多模組 65%+ |
| **IP 控制** | **4** | Falcon single agent 架構 + Threat Graph 數據護城河 + Charlotte AI agentic SOC，但非「規格定義權」 |
| **客戶分散** | **4** | Fortune 500 60%+ AVL + Top 10 客戶 < 10% 營收、無單一客戶 > 2%，極端分散 |
| **總分** | **21/25** ⭐ | **AI 資安賽道 Endpoint EDR/XDR 第一 anchor** |

→ 跟 [[Eaton]] 22 / [[Vertiv]] 22 / [[Schneider Electric]] 22 / [[CrowdStrike]] 21 / [[Palo Alto Networks]] 20 / [[Vistra]] 23 / [[Synopsys]] 24 / [[SUMCO]] 24 等 anchor 同級。

## 跟 wiki 既有概念連結

- [[AI 資安攻防成本曲線]]：CRWD 是「**防守側 agentic SOC 龍頭 + ARR 受惠攻擊端 AI 加速**」實踐 anchor
- [[賣水人選股邏輯（投資版）]]：CRWD 是「AI 資安賽道（CRWD / PANW / NET / ZS / Wiz）」第一 anchor
- [[效率→安全切換]]：CRWD 是「資安從奢侈品變剛需」實踐 anchor、ARR 長期不可逆
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 套用三段式
- [[控制點轉移（投資版）]]：CRWD 拿到 endpoint single agent 規格定義 + Threat Graph 數據 + Charlotte AI agentic SOC 三段控制點
- [[Microsoft]]：Microsoft Defender 平台 lock-in 威脅、最直接對手
- [[宋分備忘錄 ＃3 — AI 半導體受惠者擴散]]：CRWD 是「**被遺忘的 AI 受惠者**」放大版（資安平台是 AI 之後的剛需 service）

## 跟 llm-wiki 跨庫連結

- [[AI 資安研究]]：CRWD 是「model layer 守毛利的下游基礎建設」實踐
- [[責任歸屬（AI Liability）]]：CRWD Charlotte AI agentic SOC = LLM 攻擊增加後的責任歸屬窗口期防守工具
- [[Wiz]]：跟 CRWD Falcon Cloud Security 對手位（Google $32B 收購 anchor）

## 相關連結

- [[Palo Alto Networks]] — 三平台對照（PANW NGFW + SASE + Cortex XSIAM vs CRWD Falcon 28+ modules）
- [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]] — CRWD 是 Endpoint EDR/XDR 軌龍頭
- [[Microsoft]] — 平台 lock-in 競爭威脅
- [[AI 資安攻防成本曲線]] — 攻防雙引擎核心 thesis
- [[賣水人選股邏輯（投資版）]] — AI 資安賽道核心 anchor
- [[效率→安全切換]] — 資安從奢侈品變剛需
- [[宋分備忘錄 ＃3 — AI 半導體受惠者擴散]] — 被遺忘的 AI 受惠者放大版
- [[公司 Entity 模板（Step 1-3 三段式）]]

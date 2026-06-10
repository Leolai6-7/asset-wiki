---
title: AI 模型公司 — 微軟 Copilot 條款僅供娛樂
aliases: [Copilot 僅供娛樂, Copilot 條款, Copilot NPS, AI 訂閱制]
type: summary
created: 2026-06-04
as_of: 2026-06-04
check_after: 2027-01-15
updated: 2026-06-04
sources:
  - raw/2026-04-06_微軟每月收你30美元用Copilot——但條款寫著僅供娛樂.md
tags: [Microsoft, Copilot, SaaS, 訂閱制, unit economics, AI 責任, NPS]
thesis_dependency: AI-capex
confidence: medium
---

# AI 模型公司 — 微軟 Copilot 條款僅供娛樂

## 一句話核心

Copilot 每月收企業用戶 $30 卻在條款寫「僅供娛樂、不要依賴」——這不是文字錯誤，是律師精心設計的「**營收歸微軟、風險歸用戶**」結構；它同時揭穿 AI 訂閱制 unit economics 的真實面：**滲透率僅 3.3%、NPS -19.8、44% 流失用戶因不信任離開**。

## 重點摘要

- **「僅供娛樂」條款**：Copilot ToS 寫明「僅供娛樂用途，可能犯錯，不要依賴於重要建議」。2025-10 更新，2026-04 才被廣泛注意到（TechCrunch、The Register、XDA）。
- **價格結構**：企業用戶 $30/月、綁年約、疊在既有 M365 訂閱上。
- **TAM 數學**：M365 有 4.5 億座位，若 5-16% 加購 → 年營收 $50-160B。
- **滲透率實況**：付費滲透率僅 **3.3%**，即 1,500 萬人付費（離 50-160B 的「理論 TAM」遙遠）。
- **NPS -19.8**（負！）：44.2% 流失用戶說「不信任答案」。
- **法律保護分層**：
  - 商業版（E3/E5）：微軟承擔侵權責任，但**不包括建議錯誤導致的損失**
  - 免費 / 個人版：完全無保護、「使用風險自負」（大寫粗體）
- **三家公司、三種責任處理**：
  - Anthropic 承擔代價（畫紅線）
  - OpenAI 模糊地帶（簽約、自我約束無執行）
  - Microsoft 法律免責（條款寫死）
- → **沒有任何 AI 公司真的相信自己產品可靠到能承擔法律責任。**

## 產業/供應鏈延伸調查（重點）

### 一、AI 訂閱制 unit economics 的真實樣貌

把 Copilot 的 $30/月 拆開看：

| 項目 | 估算 | 來源 |
|---|---|---|
| 用戶月費 | $30 | Microsoft 公告 |
| 每用戶每月推論成本 | $10-20（重度用戶可能更高） | 多家分析 |
| 毛利率 | 30-65% | SAMexpert |
| 但對比 M365 本身毛利率 | 70%+ | Microsoft 財報 |
| → Copilot 拉低整體 SaaS 毛利率 | 是 | 結構性問題 |

**重點**：傳統 SaaS（M365、Adobe、Salesforce）毛利率 70-85%、邊際成本接近零、可無限 scale。**AI 訂閱制的邊際成本不是零**，每次推論都消耗 GPU 算力——這是 SaaS 30 年來沒遇過的結構性變化。

→ 若 Copilot 真的滲透到 5-16% 座位 = $50-160B 營收，**毛利率會被推論成本壓到 30-50%**（傳統 SaaS 是 70-85%）→ **Microsoft 整體 PE 倍數要重估**。

### 二、滲透率為什麼卡在 3.3%

Recon Analytics 數據揭穿了「Copilot 滲透率天花板」的真實原因：

| 拒絕 / 流失原因 | 比例 |
|---|---|
| 不信任答案 | 44.2% |
| 沒用到工作流程 | 32% |
| 價格太高 | 18% |
| 其他 | 5.8% |

→ **「不信任」才是最大障礙，不是價格**。微軟條款寫「僅供娛樂」剛好強化用戶不信任。**ToS 與行銷的矛盾本身就在壓制滲透率**。

### 三、SaaS 定價邏輯被 AI 打斷

| 維度 | 傳統 SaaS（M365、Salesforce） | AI 訂閱制（Copilot） |
|---|---|---|
| 邊際成本 | ~0 | $10-20/月（推論） |
| 毛利率 | 70-85% | 30-65% |
| 規模效應 | 越大越賺 | 越大算力 bill 越大 |
| 客戶 LTV | 高（黏著） | 待證明（NPS 為負）|
| 定價權 | 強（提價空間大） | 弱（用戶質疑價值） |
| 責任條款 | 商業 SLA | 免責「僅供娛樂」 |

→ 對 Microsoft 估值含義：**AI 業務拉動營收成長但壓縮毛利**，整體 EBITDA Margin 有結構性下行壓力。Forward PE 給 35x 的假設要重新檢視 → [[Forward PE 估值法]]、[[PE 壓縮公式]]。

### 四、產業傳導：所有 AI SaaS 都會面對的問題

- **Salesforce Agentforce、ServiceNow Now Assist、Adobe Firefly**：定價模式相似、毛利結構相似、unit economics 風險相似。
- **OpenAI ChatGPT Enterprise（$60/seat/月）、Anthropic Claude for Enterprise**：同樣問題。
- **GitHub Copilot（$19-39/月）**：滲透率較高（開發者社群高接受度）、但 NPS 和產品價值更可驗證。
- → **2026 下半年市場會開始質疑「AI 訂閱制」整體的可持續性**。對應 [[AI 通縮三路徑]] 的「商品化」路徑——AI 能力商品化後，加價賣 AI 訂閱的窗口可能比預期短。

### 五、投資啟示（asset-wiki 角度）

1. **Microsoft 不是無傷的 AI 受惠者**：Copilot 是 Azure 增長的「主要 demand creator」，但同時是毛利稀釋者。長期看 Azure 仍是真贏家、Copilot 則需證明 unit economics。
2. **AI SaaS 倍數要分層看**：純基礎設施型（Azure、AWS）vs 應用 AI 型（Copilot、Salesforce AI）。後者倍數有壓縮風險。
3. **GPU / HBM / 電力**仍是最安全的賣水人：因為**不管哪家 AI 訂閱賺不賺錢，他們都要燒推論算力**。 → [[半導體基礎建設化]]、[[HBM iPhone moment]]
4. **法律免責是雙刃劍**：保護微軟法律風險、但同時壓制 NPS 與滲透率。**「僅供娛樂」會被引用做集體訴訟的證據**——如果有用戶因 Copilot 錯誤受損，這條條款反而證明了微軟「明知產品不可靠仍以高價販售」。
5. **AI 廣告化的壓力**：訂閱制天花板若卡在 3-5% 滲透 → 模型公司會被迫走廣告路線 → 連到 [[AI 行業 — AI 廣告信任危機]]。

## 與 wiki 概念的深度連結

| 主題 | concept |
|---|---|
| AI 訂閱 unit economics | （新提案）[[AI 訂閱制 unit economics]] |
| Microsoft 毛利結構 | [[五層損益表（營業槓桿）]]、[[Forward PE 估值法]] |
| 估值倍數風險 | [[PE 壓縮公式]]、[[修正三階段]] |
| AI 通縮 | [[AI 通縮三路徑]]（商品化路徑） |
| 真贏家 vs 模型層 | [[跳出個股看三層：產業、目的、供應]]、[[半導體基礎建設化]] |
| 三家 AI 公司責任分歧 | [[AI 模型公司 — Anthropic 被列為國安威脅]]、[[AI 模型公司 — OpenAI 1220 億融資結構]] |

## 相關連結

- [[AI 模型公司 — OpenAI 1220 億融資結構]]
- [[AI 模型公司 — Anthropic 被列為國安威脅]]
- [[AI 行業 — AI 廣告信任危機]]
- [[AI 行業 — 成長中裁員與資本重分配]]
- [[AI 通縮三路徑]]
- [[Forward PE 估值法]]
- [[PE 壓縮公式]]
- [[半導體基礎建設化]]

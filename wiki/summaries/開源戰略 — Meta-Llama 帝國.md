---
title: 開源戰略 — Meta-Llama 帝國
aliases: [Meta Llama 帝國, Llama 開源倒戈, 開源冠軍倒戈]
type: summary
created: 2026-06-04
as_of: 2026-06-04
check_after: 2027-02-15
updated: 2026-06-04
sources:
  - raw/2026-04-11_開源冠軍倒戈-Meta-Llama帝國.md
tags: [Meta, LLaMA, 開源戰略, 廣告, AVGO, AMD, 投資視角]
thesis_dependency: AI-capex
confidence: medium
---

# 開源戰略 — Meta-Llama 帝國

**一句話核心**：開源是武器不是信仰，**武器有保質期**——當主營收（廣告）跟開源產品（LLaMA）無關，開源就只是「燒錢的市佔率投資」，遲早被 ROI 壓力收回成閉源。

## 重點摘要

### 倒戈時間軸

- **2023–2025**：LLaMA 系列累計 **1.2B+ 下載**，史上最成功開源 LLM
- **2025-06**：Meta 以 **$14.3B** 收購 Scale AI 49%，挖角 Alexandr Wang 任首席 AI 官
- **2026-04-08**：Muse Spark 發布，**完全閉源、僅私人 API 預覽**，標誌 Meta 從開源冠軍轉向

### 為什麼倒戈：開源 vs 閉源的 ROI 拐點

| 維度 | LLaMA 開源邏輯 | Muse Spark 閉源邏輯 |
|---|---|---|
| 商業目標 | 建生態壓低自身 AI 開發成本（廣告機器升級） | 直接 API 變現 + 整合進 IG/WhatsApp/Ray-Ban |
| 投資規模 | 開源前 R&D 較低 | $14.3B + 數億美元挖角包 |
| 護城河 | 下載量未轉化為 API 營收／生態鎖定 | 閉源 + 多模態 + 工具整合 = 控制使用情境 |

### 開源可持續性條件表（Leo 提出的）

| 公司 | 開源什麼 | 主營收 | 可持續？ |
|---|---|---|---|
| Google | Gemma | Cloud + Android | OK |
| 幻方/DeepSeek | DeepSeek | 量化交易 | OK |
| Netflix | VOID | 串流訂閱 | OK |
| Anthropic | MCP | API 服務 | OK |
| **Meta** | LLaMA → Muse Spark 閉源 | **廣告（不直接受益於模型開源）** | **NG** |

> **規則**：開源策略可持續性 = 公司是否有獨立於被開源產品的營收來源。**賺的錢離開源產品越遠，武器越耐用**。

## 產業／供應鏈延伸調查

### 1. Meta 廣告機器的真實受惠路徑（這是「目的層」）

Meta 95% 營收來自廣告。AI 投資的真實 ROI 不是「賣 AI 模型」，而是廣告 funnel 的三段強化（見 [[Meta]]）：

```
AI 改善投放精準度  → 廣告主 ROI 上升 → 預算流入
AI 生成創意       → 製作成本下降   → 利潤率上升
AI 優化用戶體驗   → 停留增加       → 廣告庫存增加
```

→ 衡量 Meta AI 投資正確指標：**廣告營收效率（ARPU、CPM）的提升斜率**，不是 AI 產品營收。LLaMA 是「廣告機器的訓練平台」，Muse Spark 則進一步走「個人 AI 助理」這條直接變現路徑。

### 2. AMD 6GW 訂單視角：Meta 的硬體採購多元化（賣水人受惠）

- Meta 與 [[AMD]] 簽 **6GW 採購意向**，估算 **$105B 規模（5 年）**
- 對 AMD 是巨單，對 Meta 是 **減少對 [[NVDA]] 單一依賴**
- 同時 Meta 是 [[AVGO]] ASIC 客戶之一（自研 MTIA 晶片）——AVGO ASIC 客戶 3→9 家的擴張路徑
- 投資推論：Meta 閉源轉向不影響它「燒 CapEx 蓋 AI infra」的事實，**真正受惠的賣水人是 AMD/AVGO/TSMC，不是 Meta 自己**

### 3. Scale AI 收購的供應鏈含義

- $14.3B 不是買技術，是買**資料標註基礎建設 + 人才 + 客戶通路**
- Scale AI 客戶包括美國國防部 → Meta 切入 sovereign AI / 軍工 AI 賽道
- 對 Scale AI 同業（Surge AI、Snorkel）是估值地板（PE 收購溢價示範）

### 4. 真正風險：開源燒掉的市佔率收不回來

- LLaMA 1.2B 下載量裡，**真正升級到 Muse Spark API 的轉換率未知**
- 開源用戶習慣免費 → 切換到「私人 API 預覽」的阻力極高
- 比較：Anthropic 從未開源 Claude，卻能達到 $30B ARR、企業客戶 1,000+；Meta 開源換來下載量但企業變現 0
- **教訓**：開源換來的是社群心智份額，**不是付費客戶**

## 與 wiki 概念的深度連結

| 主題 | concept |
|---|---|
| 表面看 AI / 本質看廣告 | [[跳出個股看三層：產業、目的、供應]]（「目的層」範例） |
| 市場對 LLaMA → Muse Spark 的反應 | [[預期差]]（市場可能還在用「開源領袖」估值 Meta） |
| Meta 在 AI 賽道的角色變化 | [[控制點轉移]]（從生態主到應用層直接競爭者） |
| 開源的策略性使用 | [[開源作為武器]]（這次延伸到投資版） |
| 蓋 AI infra 的真正受惠 | [[半導體基礎建設化]]、[[AI 通縮三路徑]] |
| 衡量 AI 投資回報 | [[Forward PE 估值法]]（不該用 AI 產品 ARR） |

## 提案的新節點（主 agent 落地）

- entity：Muse Spark、Scale AI、Alexandr Wang
- concept：[[開源作為武器]]（投資版）、[[開源 vs 閉源決策框架]]
- 已有 entity 更新：[[Meta]] 增補 Muse Spark 段落 + 與 AMD 6GW 連結

## 相關連結

- [[開源戰略 — Meta Muse Spark 閉源轉折]]
- [[開源戰略 — Netflix 第一個開源 AI 模型]]
- [[接口控制 — MCP 九千七百萬次安裝]]
- [[Meta]]
- [[AMD]]、[[AVGO]]、[[NVDA]]
- [[跳出個股看三層：產業、目的、供應]]
- [[宋分備忘錄 ＃2 — HBM iPhone Moment-Meta-軟體 PE]]

---
source: FOMO SOC（KP@FOMOSoc）
url: https://www.fomosoc.com/p/aiagentic-ai-47cloudflare
date: 2026-05-13
title: 邊緣 AI 的贏家？Agentic AI 的受惠者？是資安還是網路基礎設施公司？— 深入分析第 47 期：Cloudflare
fetched_by: WebFetch
fetched_on: 2026-06-09
paywall: 部分擋住第 5 章「AI 時代的典範轉移」核心段落（agentic AI 邊緣推論物理瓶頸、商業化路徑、Forward PE / ARR）
---

# FOMO SOC 第 47 期 — Cloudflare（KP@FOMOSoc）

## 一句話 thesis

> Cloudflare 透過十多年來鋪設的全球邊緣網路基礎設施，正成為 AI 時代的**神經網路**——關鍵優勢在於**網路接口的控制權**與**邊緣推論的物理優勢**。

## 核心論點

### 四階段演進

1. 保護網站（DDoS / CDN / WAF）
2. 邊緣運算（Workers）
3. 企業資安（Cloudflare One / Zero Trust）
4. 雲端生態系（R2 / Vectorize / Browser Rendering / Workers AI）

### 結構優勢

- 全球近 300 個城市有邊緣節點
- 掌控全球 ~20% 網站流量的通道
- 邊緣節點 = agentic AI 即時決策 + 低延遲推論的物理基礎

### Network as Control Plane（隱含但未明確標籤化）

| 時代 | 控制權位置 | 代表 |
|---|---|---|
| 傳統雲端 | 資料中心（最大運算） | AWS / Google |
| 邊緣 | 網路接口（最後一哩） | **Cloudflare** |
| Agentic AI | 邊緣 GPU 推論節點（毫秒級決策） | Cloudflare Workers AI |

> AI agent 需要毫秒級決策、不能每次都往美國跑——Cloudflare 在全球 330 個節點有 GPU、可直接在邊緣「思考」、相當於把神經網路從集中式大腦變成分散式「全身反射弧」。

> 誰能在用戶最近的地方提供最低延遲的 AI 推論、誰就能決定下一代互聯網應用的 **API 標準、資料格式、安全規則**。

## 產品線（可見部分）

- **Workers**：邊緣運算引擎、可在 330 個城市同時執行
- **Workers AI**：邊緣節點部署 GPU、直接呼叫 Llama / Stable Diffusion
- **R2**：零傳出費（egress-free）雲端儲存、打破 AWS 資料綁架
- **Cloudflare One**：零信任安全架構
- **Browser Rendering / Vectorize**：付費牆後提及但未深入

## 競爭格局

| 對手 | 競爭領域 |
|---|---|
| **AWS** | 核心雲端服務 + 資料成本控制 |
| Akamai | 老牌 CDN |
| **Zscaler** | 零信任安全（**SSE 市佔 34% vs Cloudflare 不在前六**、Dell'Oro 報告） |
| Palo Alto Networks | 傳統防火牆 + 資安 |
| Google Cloud | 通用雲端 |

## 數據 anchor（可見部分）

- 全球流量 ~**20%** 經過 Cloudflare
- 全球 ~**300 個城市**邊緣節點
- Zscaler SSE 市佔 **34%**（Cloudflare 不在前六）
- Q1 2026 財報後股價單日修正近 **24%**
- 高盛最新 AI 基礎設施報告將 Cloudflare 列為**首選**

> 缺失（付費牆後）：Forward PE / ARR / specific growth rates

## High-Confidence 要點

1. 邊緣節點密度優勢無與倫比（300 城市 vs AWS 十多個 region）
2. 數據飛輪已成立（免費用戶攻擊數據 → 訓練防禦 → 升級付費客戶安全等級）
3. 從資安向邊緣 AI 自然延伸（技術 + 商業邏輯貫通）
4. 企業遠距工作常態化 → Zero Trust 結構性需求

## 風險點

1. **Zscaler 仍是零信任領導者**（SSE 34% vs Cloudflare 不在前六）
2. AWS 反擊（Lambda@Edge、Wavelength 已在邊緣部署）
3. **Agentic AI 商業化進程不透明**（付費牆後才揭示真正盈利路徑）
4. 邊緣 AI 推論成本結構（GPU 密集、邊際成本未透明）
5. **股價波動率高**（Q1 後 24% 單日修正反映市場分歧）

## KP 隱含立場

- 把 Cloudflare 定位為**「Network as Control Plane」**創新者、未來互聯網基礎設施標準制定者
- 採用「故事化 + 物理比喻」（保鑣 / 快遞員 / 蜜罐）
- 時機點強調「高盛報告 + Q1 修正 = 價格與價值鏡像期」

## 付費牆狀態

- 可見：第一至四章完整 + 第五章「AI 時代的典範轉移」前段
- 擋住：agentic AI 邊緣推論的物理瓶頸詳論、商業化路徑、Cloudflare 具體 thesis 評價、估值區間

## 與 wiki 既有概念連結 hints

- [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]] Network SASE/NGFW 軌補位（Cloudflare 暫未建 entity）
- [[接口控制權]]（concept、已建）= Network as Control Plane 的投資側對應
- [[控制點轉移（投資版）]] 從資料中心 → 網路接口 → 邊緣節點三段轉移
- [[賣水人選股邏輯（投資版）]] 邊緣 GPU + Workers AI 是賣水人路線
- [[CrowdStrike]] / [[Palo Alto Networks]] / [[Zscaler]] 三軌玩家中 Network 軌的潛在補位

---
title: AI infra 散熱戰場
aliases: [AI infra 散熱, 散熱戰場, AI 散熱, AI 液冷戰場, AI 機櫃散熱]
type: concept
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2026-12-08
expires_on: 2027-12-31
sources:
  - https://thecoolingreport.com/intel/nvidia-rubin-liquid-cooling-standard-not-optional
  - https://www.datacenterdynamics.com/en/news/nvidia-prepares-data-center-industry-for-1mw-racks-and-800-volt-dc-power-architectures/
  - https://news.cnyes.com/news/id/6423986
  - https://www.sinotrade.com.tw/richclub/hotstock/%E6%B6%B2%E5%86%B7%E6%89%93%E7%A0%B4%E7%99%BD%E5%8D%80%E8%88%87%E7%81%B0%E5%8D%80%E7%95%8C%E7%B7%9A-%E5%8F%B0%E9%81%94%E9%9B%BB-2308--%E9%9B%99%E9%B4%BB-3324--%E5%A5%87%E9%8B%90-3017--%E4%B8%89%E5%A4%A7%E5%9F%BA%E5%BB%BA%E9%9C%B8%E4%B8%BB%E5%85%A8%E9%9D%A2%E6%BB%B2%E9%80%8F-AI-%E8%B3%87%E6%96%99%E4%B8%AD%E5%BF%83-%E7%94%A2%E6%A5%AD%E7%86%B1%E8%A9%B1-6964b77480fc0a261b354593
  - https://www.guru3d.com/story/rubin-ultra-gpu-to-use-advanced-microchannel-cooling-for-its-2300w-tdp/
  - https://news.futunn.com/en/post/62092203/new-direction-for-liquid-cooling-nvidia-requests-suppliers-to-develop
tags: [Meta 框架, AI infra, 散熱, 液冷, CDU, cold plate, manifold, QD, NVDA Rubin, 800V HVDC, 第六戰場]
confidence: high
---

# AI infra 散熱戰場

**AI infra 第 6 戰場**——跟 [[AI infra 電力戰場]] 是孿生戰場。NVDA Rubin 1MW 機櫃（GB200 的 ~7.5x、GB300 的 ~6x）讓**氣冷物理上做不了 AI infra**、液冷從「可選」變「強制」。

→ 對應 [[AI infra CapEx 三階段論]]：散熱是「從 NVDA 設備往下游機櫃 / 資料中心傳導」的 BOM 倍增戰場、單機櫃散熱 BOM 翻倍速度 ≈ 機櫃功耗成長速度。

## 一句話

> 機櫃功率密度 5 年從 30kW → 1MW（**33x**）= 散熱 BOM 不只放量、是**結構性換軌**（氣冷 → 液冷 → 浸沒），**台廠在 cold plate / manifold / 真空硬銲熱交換器三個 niche 有強勢**。

## 為什麼是第 6 戰場

AI infra 戰場圖譜（codex 校準）：

| # | 戰場 | 代表玩家 | 階段 |
|---|---|---|---|
| 1 | 算力（GPU / ASIC）| [[NVDA]] / [[AVGO]] / [[AMD]] | 共識 |
| 2 | 記憶體（HBM）| [[SK Hynix]] / [[Micron]] / [[Samsung Electronics]] | 共識 → 反轉前 |
| 3 | 光通訊（DCI / 1.6T 光模組）| [[Ciena]] / [[Lumentum]] / [[Coherent]] / [[IQE]] | 驗證 → 共識 |
| 4 | 先進封裝（CoWoS / 玻璃基板）| [[TSMC]] / [[IBIDEN]] / [[Absolics]] | 驗證 |
| 5 | 被動元件嵌入式（MLCC）| [[村田 Murata]] / [[太陽誘電 Taiyo Yuden]] / [[信昌電]] | 懷疑 → 驗證 |
| **6** | **散熱**（液冷 / cold plate / CDU）| [[Vertiv]] / [[台達電]] / [[雙鴻]] / [[高力 8996|高力]] | **懷疑 → 驗證**（**比第 5 戰場滯後 1 步、但物理強制度最高**）|
| 7? | 電力（800V HVDC / 電源 / 電網）| [[AI infra 電力戰場]] entity | 驗證 |

**散熱戰場的特殊性**：
1. **物理強制度 100%**——不像被動元件嵌入式（時程未定）、散熱**不上液冷就跑不了 Rubin 機櫃**，沒有「等等看」選項
2. **跟電力戰場孿生**——同一份 CapEx 同時砸電力 + 散熱、且**整合方相同**（[[Vertiv]] / [[台達電]] / Schneider 都做 power + cooling 雙軌）
3. **台廠 niche 強勢**——cold plate / manifold / 真空硬銲熱交換器（[[高力 8996|高力]] 9 成市佔）三個 niche，台廠擠進國際前段班

## 三階段轉變（氣冷 → 液冷 → 浸沒）

```
氣冷時代               液冷時代               浸沒時代（觀察）
（2010-2023）          （2024-2030）          （2030+）

機櫃功率: 5-30kW    →   30-1,000kW         →   1MW+ (未知上限)
冷卻方式: 風扇 +      →  cold plate 直接   →   整機泡液 (single-phase
         CRAC          觸晶 + L2L CDU         + two-phase 兩派)
熱介質:  空氣        →  水/丙二醇 (D2C)    →  介電液 (3M Fluorinert
                                              / Submer SmartCoolant)
PUE:    1.6-1.8     →  1.1-1.3            →  <1.05
玩家:   傳統 HVAC     →  Vertiv / 台達 /    →  Submer / GRC /
        (Schneider     雙鴻 / 奇鋐 / 高力      LiquidStack / Intel
        / Vertiv)      / Boyd / CoolIT       開源 SAM
```

### 階段 1：氣冷（2010-2023，正在退場）
- CRAC / CRAH（room cooler）+ rack-level fan
- 上限 ~30-50kW / rack（physical limit of air heat transfer）
- 玩家：Schneider Electric、Vertiv、Stulz、Munters
- **GB200 NVL72 132kW = 氣冷物理上不可能** → 強制換軌

### 階段 2：液冷（2024-2030，**現在**）
- **D2C（Direct-to-Chip）cold plate** 是 NVDA Blackwell / Rubin 標配
- L2L（liquid-to-liquid）+ L2A（liquid-to-air）兩種 CDU 架構
- 機櫃功率 30kW → 1MW（Rubin）
- 玩家：[[Vertiv]] / [[台達電]] / Schneider / Boyd（Eaton 2026-03 併購）/ CoolIT / [[雙鴻]] / 奇鋐 / [[高力 8996|高力]]

### 階段 3：浸沒式（2030+，觀察）
- 整機伺服器泡介電液
- single-phase（不沸騰）vs two-phase（沸騰相變、效率更高但複雜）
- PUE 可壓到 1.05 以下
- 玩家：Submer、GRC、LiquidStack、Intel 開源 SAM
- **NVDA Rubin 未強制浸沒、Rubin Ultra 2027+ 可能評估**

## 四大組件分工

液冷系統的四大核心組件（codex 校準、跟 [[CPO 供應鏈圖譜]] 結構類比）：

| 組件 | 角色 | 代表玩家 | 台廠位置 |
|---|---|---|---|
| **Cold Plate（冷板）** | 直接觸 GPU/CPU 晶片背蓋的銅板、內走冷卻液、最關鍵 | [[Vertiv]]（Strategic Thermal Labs 2026-04 併購）/ Boyd / CoolIT / [[雙鴻]] / 奇鋐 | **強**——雙鴻 / 奇鋐合計拿 GB200 cold plate ~70% 市佔 |
| **Manifold（分流管）** | 把 CDU 出來的冷卻液分配到每個 cold plate 的管路系統 | [[雙鴻]] / 奇鋐 / Boyd | **強**——奇鋐 4 大 CSP CDM 主供、雙鴻 27% rack manifold 市佔 |
| **CDU（Coolant Distribution Unit）** | 機櫃間 / 機房級的冷卻液分配 + 二次回路熱交換、心臟 | [[Vertiv]] / [[台達電]] / Schneider / CoolIT / [[雙鴻]] / [[高力 8996|高力]] | **中等**——台達電 2.4MW/3MW CDU 切入 NVDA、雙鴻 1.6MW L2L CDU、高力 BPHE 是 CDU 心臟（9 成市佔）|
| **QD（Quick Disconnect）/ 接頭** | 漏液關鍵點、universal QD 是 Rubin 互通性的前提 | Parker Hannifin / Staubli / CPC（Colder Products）/ Eaton（Boyd 整合）| **弱**——主要外商寡占、無台廠強勢玩家 |

額外組件：
- **真空硬銲板式熱交換器（BPHE）**：CDU 的心臟、[[高力 8996|高力]] 全台唯一、**全球少數**能做高品質量產 + 9 成台灣市佔
- **背門熱交換器（Rear Door Heat Exchanger, RDHx）**：在機櫃背後做空對液、混合過渡架構
- **Sidecar / In-Row CDU**：放機櫃旁、密度較低、台達電原本強項

## ⭐ NVDA Blackwell / Rubin 液冷強制要求

### Blackwell（GB200 NVL72）
- TDP **per GPU**：1,000W → GB300 **1,400W**
- 機櫃功率：**132kW**
- **液冷強制**（air 無解）
- cold plate：每 compute tray **6 個獨立小 cold plate**（GB300 改設計）→ 漏液點多
- **單機櫃散熱系統成本 ~$50,000**（NVL72）

### Rubin（Vera Rubin NVL144）
- TDP **per GPU**：**1,800W**（推測）
- 機櫃功率：**1,000kW（1MW）= GB200 的 ~7.5x**
- 液冷：**標準配備、不再可選**（NVDA 2026-03 GTC 宣告）
- cold plate：**回大 cold plate 設計 + 微通道（microchannel）**——雷射熔接奈米級流道、平衡散熱效率與簡化接頭數
- 機櫃冷卻液 **45°C**（從 32°C 升、減少 chiller 負擔、PUE 降）
- universal QD：**標準化、可互通**（不同 OEM 機櫃可共用 cold plate）
- **單機櫃散熱系統成本 ~$57,000**（NVL144）

### Rubin Ultra（2027+）
- TDP **per GPU**：**2,300W**（部分傳聞 3,600W 是 4 compute + 16 HBM4E chiplet 整 package）
- **MLCP（Micro Liquid Cold Plate）新技術**——成本是現有方案 **3-5 倍**（NVDA 已向供應商請求開發）
- 觀察：是否強制浸沒（目前仍走 D2C + microchannel）

### 戰場時序
```
2024 H2  GB200 量產（液冷強制起點）
2025     液冷滲透率 ~30-40%
2026 H2  Rubin NVL144 出貨（1MW、45°C、universal QD）
2027     液冷滲透率衝 76%（鉅亨網引券商估）
2028+    Rubin Ultra（MLCP / 2,300W per GPU）
2030+    可能浸沒式 ramp
```

## 台廠 niche 強勢圖譜

跟玻璃基板（台廠在材料 / 設備 layer 落後）、MLCC 嵌入式（台廠完全缺席）對比——**散熱是台廠在 AI infra 戰場 niche 最強的一張牌**。

| 層 | 玩家 | 角色 / niche | 五軸（待校準） |
|---|---|---|---|
| **整合 turnkey** | [[Vertiv]] / Schneider / [[台達電]] | power + cooling 雙軌、Vertiv 是 pure-play 龍頭 | Vertiv 高 / 台達多角化 |
| **Cold Plate** | [[雙鴻]] / 奇鋐 3017 / Boyd / CoolIT | GB200 cold plate ~70% 台廠拿（雙鴻 15-20% + 奇鋐 50%+）| 雙鴻 19 / 奇鋐 19-20 |
| **Manifold / CDM** | 奇鋐 3017 / [[雙鴻]] | 奇鋐 4 大 CSP CDM 主供 / 雙鴻 27% rack manifold | 同上 |
| **CDU** | [[台達電]] / [[雙鴻]] / [[高力 8996|高力]] | 台達 2.4MW/3MW L2L、雙鴻 1.6MW、高力 BPHE 心臟 | 台達高 / 雙鴻高 / 高力中高 |
| **真空硬銲熱交換器（BPHE）** | [[高力 8996|高力]] | 全台唯一、9 成台灣市佔、CDU 心臟 | 高力強 niche |
| **接頭 / QD** | （無台廠強勢）| Parker / Staubli / CPC 寡占 | — |
| **沉浸式槽 / 介電液** | 緯穎（Wiwynn）/ 鴻佰 / 廣達 | 整機代工 + 過渡架構 | 觀察 |

## 跟其他戰場連結

### 跟 [[AI infra 電力戰場]]（孿生戰場）
- **同一份 CapEx**：機櫃 1MW 同時要餵電 + 散熱、整合方愈來愈傾向 turnkey
- **整合方重疊**：[[Vertiv]] 同時做 power + cooling、[[台達電]] power + cooling 雙軌、Schneider 同上
- **800V HVDC 直接帶動**：機櫃從 ±400V → 800V（NVDA Kyber 架構）= [[信昌電]] / [[華新科]] 中高壓 MLCC + Vertiv/台達 PSU 同步受惠
- **arbitrage**：純散熱玩家（雙鴻 / 奇鋐 / 高力）vs 雙軌整合方（Vertiv / 台達），前者純度高 + 後者議價權強

### 跟 [[AI infra CapEx 三階段論]]
- 第三階段（光通訊 + 上游材料爆掉）**同步發生散熱戰場主升段**
- 散熱滯後光通訊 1-2 季（光通訊 2025 H2 ramp / 散熱 2026 H1 全面 ramp）
- 第四階段（hyperscaler 全面跟進）= 散熱戰場 anchor 鎖死

### 跟 [[賣水人選股邏輯（投資版）]]
- **散熱是「賣水人之中的賣水人」候選**：NVDA / AMD / Trainium 誰贏都要液冷
- 五軸高分候選：[[Vertiv]]（站別關鍵 + 客戶分散）/ [[雙鴻]]（耗材 cold plate + IP）/ [[高力 8996|高力]]（IP 真空硬銲 + 站別 CDU 心臟）

### 跟 [[控制點轉移（投資版）]]
- NVDA 已介入 Rubin 散熱**規格定義**（universal QD、45°C 標準）→ 控制點往散熱延伸
- 散熱供應商**沒有定義權**、是 NVDA 規格的執行者（vs 光通訊 [[Ciena]] / [[Nokia]] 有 Hyper Rail 定義權）
- → 散熱玩家估值溢價來自「**製造 + 良率**」而非「IP 定義權」（差於光通訊純度玩家）

### 跟 [[信昌電]] 800V HVDC niche
- 信昌電：800V HVDC PSU + BBU 大尺寸高壓 MLCC（10K+ 顆 / Rubin 機櫃）
- 散熱：800V HVDC 後的熱處理（cold plate + CDU）
- **800V HVDC 是孿生戰場的共同 trigger**——MLCC（信昌電）+ 散熱（雙鴻 / 高力）+ 電源（台達 / Vertiv）都因 800V 同步放量
- → 信昌電 + 高力 8996 + 雙鴻 = 「**800V HVDC 三角賣水人**」

## ⚠️ 風險（thesis 失效情境）

### 1. NVDA 規格收斂
- universal QD + 標準化 cold plate → 供應商**互通**= 降低單一玩家定價權
- 雙鴻 / 奇鋐 cold plate 可能被替代（不像 [[Disco Corp]] 切割壟斷）

### 2. 整合方下吃零件廠
- Vertiv / 台達 turnkey 趨勢 → 純零件廠（雙鴻 / 奇鋐）被夾在中間
- 但反向：純零件廠 IP（雙鴻 1.6MW L2L CDU）也可能 displacement 整合方

### 3. 浸沒式跨越 D2C
- 若 Rubin Ultra（2027+）直接跳浸沒式 → cold plate 玩家 thesis 失效
- 目前判斷 D2C + microchannel 還能撐到 2030+

### 4. 漏液事件
- GB300 6 個獨立 cold plate 漏液點多 → 已有早期漏液事件（內部報告）
- Rubin 回大 cold plate 設計部分緩解、但 universal QD 仍是潛在風險點

### 5. 估值已 price in
- Vertiv Forward PE 40+、雙鴻 PE 18 + 2026 EPS 上修預期、奇鋐高估值
- 散熱題材 2025-2026 已上頭條 → [[資訊擴散四階段]] 階段 3-4

## 三家入選 entity（本次 ingest）

按 NVDA Rubin 1MW 機櫃曝險排序：

| 公司 | 散熱戰場位置 | NVDA Rubin 曝險 | 五軸（25 分制）|
|---|---|---|---|
| **[[Vertiv]]**（VRT）| 整合 turnkey（cooling + power）、Strategic Thermal Labs + ThermoKey 雙併購 | $15B backlog、NVDA 800V DC 架構協同開發 | **22/25**（純度 + 站別 + 客戶分散三高）|
| **[[台達電]]**（2308.TW）| 雙軌整合（power 60% AI server + 液冷 8% 衝 11%）、2.4MW / 3MW L2L CDU | NVDA GTC 2026 共展 800V DC + GB300 NVL72 In-Rack CDU | **20/25**（多元組合分散）|
| **[[雙鴻]]**（3324.TW）| Cold Plate + Manifold + CDU 全鏈、台廠液冷代表 | Rubin sample 驗證中、2026 液冷占比 55%、營收目標上修 70% | **19/25**（純度 + 客戶分散弱）|

漏網但提及（不建 entity，本次）：
- **奇鋐**（3017.TW）：cold plate 50%+ 市佔、CDM 4 大 CSP 主供——下一波應補建
- **[[高力 8996|高力]]**（8996.TW）：BPHE 9 成台灣市佔 + CDU 心臟、niche specialist——下一波應補建
- **川湖**（2059.TW）：機櫃滑軌、漏網提及

## 散熱戰場 anchor 排名（推測，2026-06-08）

按 Leo 「結構性受惠 + 五軸 + 估值合理性」標準推測：

1. **[[Vertiv]]（VRT）** — anchor #1：**整合 turnkey 龍頭 + $15B backlog + NVDA 800V DC 雙軌共開發**——比信昌電位階更高（power + cooling 雙軌） + 比雙鴻位階更高（規模 + 客戶分散）
2. **[[雙鴻]]（3324）** — anchor #2：**台廠液冷純度首選 + Rubin 全鏈 + 1.6MW L2L CDU IP**——比奇鋐位階略高（CDU + manifold + cold plate 三鏈完整、奇鋐強在 cold plate 50%+ 市佔但 CDU 弱）
3. **[[台達電]]（2308）** — anchor #3：**雙軌 power + cooling + 800V HVDC 護城河**——多元組合稀釋（電動車 / 5G / 家電混合）但**現金流 + 規模**勝
4. （**奇鋐 3017** 待建——cold plate 市佔最高但 CDU 弱、IP 略遜雙鴻 1.6MW CDU）
5. （**高力 8996** 待建——BPHE niche 9 成市佔 + CDU 心臟、純度高但市值小）

→ **若只能買 3 家** = Vertiv + 雙鴻 + 台達電（涵蓋整合 / 純度 / 雙軌三軸）
→ **若可以買 5 家** = +奇鋐 + 高力（補 cold plate 市佔王 + BPHE niche specialist）

## 跟其他 wiki 概念連結

- [[AI infra 電力戰場]]：散熱的孿生戰場、整合方重疊
- [[AI infra CapEx 三階段論]]：散熱是第三階段同步爆發的物理層
- [[賣水人選股邏輯（投資版）]]：散熱是「不押誰贏」的最強候選之一
- [[控制點轉移（投資版）]]：NVDA Rubin 規格收斂 = 散熱玩家無 IP 定義權
- [[半導體基礎建設化]]：散熱從零件升級為基礎建設層
- [[市場四階段：懷疑／驗證／共識／反轉]]：散熱在「懷疑 → 驗證」加速段
- [[資訊擴散四階段]]：散熱題材已進入媒體層、ETF 階段尚未
- [[信昌電]]：800V HVDC 孿生兄弟（MLCC vs 散熱、同 trigger）
- [[CPO 供應鏈圖譜]]：cold plate / manifold / CDU / QD 四層分工跟 CPO 七層分工結構類比

## 相關連結

- [[AI infra 電力戰場]]
- [[AI infra CapEx 三階段論]]
- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[半導體基礎建設化]]
- [[信昌電]]
- [[NVDA]]
- [[Vertiv]]、[[台達電]]、[[雙鴻]]
- [[高力 8996|高力]]（待補 entity）
- [[CPO 供應鏈圖譜]]

## Sources

- [Nvidia Just Made Liquid Cooling Standard on Rubin（The Cooling Report）](https://thecoolingreport.com/intel/nvidia-rubin-liquid-cooling-standard-not-optional)
- [Nvidia prepares data center industry for 1MW racks and 800-volt DC（DCD 2026-03）](https://www.datacenterdynamics.com/en/news/nvidia-prepares-data-center-industry-for-1mw-racks-and-800-volt-dc-power-architectures/)
- [2026 液冷滲透率直衝 76%！單櫃產值跳升 4 倍（鉅亨網 2026）](https://news.cnyes.com/news/id/6423986)
- [液冷打破白區與灰區界線 三大基建霸主（豐雲學堂 2026-06）](https://www.sinotrade.com.tw/richclub/hotstock/%E6%B6%B2%E5%86%B7%E6%89%93%E7%A0%B4%E7%99%BD%E5%8D%80%E8%88%87%E7%81%B0%E5%8D%80%E7%95%8C%E7%B7%9A-%E5%8F%B0%E9%81%94%E9%9B%BB-2308--%E9%9B%99%E9%B4%BB-3324--%E5%A5%87%E9%8B%90-3017--%E4%B8%89%E5%A4%A7%E5%9F%BA%E5%BB%BA%E9%9C%B8%E4%B8%BB%E5%85%A8%E9%9D%A2%E6%BB%B2%E9%80%8F-AI-%E8%B3%87%E6%96%99%E4%B8%AD%E5%BF%83-%E7%94%A2%E6%A5%AD%E7%86%B1%E8%A9%B1-6964b77480fc0a261b354593)
- [Rubin Ultra GPU to Use Advanced Microchannel Cooling for its 2300W TDP（Guru3D）](https://www.guru3d.com/story/rubin-ultra-gpu-to-use-advanced-microchannel-cooling-for-its-2300w-tdp/)
- [New Direction for Liquid Cooling? NVIDIA MLCP 3-5x cost（Futunn）](https://news.futunn.com/en/post/62092203/new-direction-for-liquid-cooling-nvidia-requests-suppliers-to-develop)
- [Inside the NVIDIA Vera Rubin Platform（NVIDIA Developer Blog）](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/)
- [Vertiv strengthens liquid-cooling system with Strategic Thermal Labs（Vertiv 2026-04-27）](https://www.vertiv.com/en-us/about/news-and-events/corporate-news/2026/vertiv-strengthens-liquid-cooling-system-capability-with-acquisition-of-strategic-thermal-labs/)
- [Delta Power, Cooling and Microgrid at NVIDIA GTC 800 VDC（PR Newswire 2026-03）](https://www.prnewswire.com/news-releases/deltas-power-cooling-and-microgrid-solutions-showcased-at-nvidia-gtc-to-bolster-the-800-vdc-architecture-of-next-gen-ai-factories-302714372.html)

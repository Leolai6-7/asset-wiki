---
title: AI infra 電力戰場
aliases: [電力戰場, AI 電力, AI infra power, AI data center power, 800V HVDC, Power Battlefield, 第六戰場]
type: concept
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2026-12-08
expires_on: 2027-06-08
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
  - raw/2026-06-08_Leo-AI-infra-CapEx-三階段論-1.6T-光模組-InP.md
tags: [Meta 框架, AI 基礎建設, 電力, HVDC, Rubin, 核電, 賣水人, 第六戰場, Capex anchor]
confidence: high
---

# AI infra 電力戰場

asset-wiki 第六戰場（前五波：第一光通訊 / DCI、第二 MLCC 嵌入式、第三 TGV 玻璃基板、第四 ABF 載板 displacement、第五 InP 上游 epi）——**電力**現在被獨立列為 anchor 戰場，不再附屬在 [[賣水人選股邏輯（投資版）]] 或 [[MLCC 嵌入式基板賽道]] 的子段。

> 因為 NVDA Rubin 1MW 機櫃 vs GB200 132kW = **電力需求暴增 7.5x**，這已經不是「機櫃內的元件題」，是「機櫃外的電網題」。
>
> → 電力戰場是 [[AI infra CapEx 三階段論]] **第三階段下半場真正的剛性 trigger**。

## 一句話

> AI infra 五年 $5.3 兆 CapEx 不會均勻撒——**「機櫃外的電」是最後一公里被忽視的瓶頸**，這層決定 AI 算力 ramp 的真實上限。

## 為什麼這是第六戰場（codex P1-3 校準）

**Codex 對抗審核 P1-3** 指出：

> AI infra 戰場缺「電力 / 散熱」主戰場；賣水人頁已有電力鏈，MLCC/信昌電頁也反覆提 1MW rack / 800V HVDC → 建議：新增 Power + Thermal battlefield，不要只放在 MLCC 附屬敘事

**Rubin vs GB200 量化比較**（信昌電法說 2026-05-21 + Schneider Electric 2025-10 揭露）：

| 機櫃 | 功率 | 倍數 |
|---|---|---|
| GB200 NVL72（現役）| **132 kW** | 1x |
| Rubin Ultra Kyber（2027 量產）| **600-1,000 kW（~1MW）** | **~5-8x** |
| **真實 8x 電力需求** | | **= GPU + HBM + 光模組同時暴漲** |

→ 過去 NVDA 出 GPU、CSP 自己想辦法上電；現在 NVDA 自己定 **800V HVDC architecture standard** + 拉 **31 家供應鏈伙伴**做生態（ABB / Eaton / Schneider / Vertiv / Infineon / STM / Navitas / Vistra / Constellation / GE Vernova / Talen），這已經是**接口控制權延伸到電網**。

→ 連 [[控制點轉移（投資版）]]：NVDA 把控制點從晶片 → 機櫃 → **電網** 一路推上去。

## 三層分工（沿用 [[CPO 供應鏈圖譜]] 七層分工的框架）

### 第一層：電力產生（Generation）

把電做出來——**核電 / 氣電 / 再生能源**。

| 玩家 | 類型 | 規模 | 對 AI infra anchor |
|---|---|---|---|
| **[[Constellation Energy]]**（CEG）| **核電 #1 美國** | 32.4 GW 核電 + Calpine 併購後 26 GW 氣電 | **Microsoft Three Mile Island 20 年 PPA 835MW**（2024-09 簽、2026 啟動、2028 上線） |
| **[[Vistra]]**（VST）| **核電 #2 美國 + 氣電** | ~41 GW（核電 6.4GW + 氣電 30GW+ + Cogentrix 5.5GW 待併）| **Meta 20 年 PPA 2.6GW**（2026-01 簽、跨 PJM 三廠核電 + uprate）+ **AWS PPA**（多年合約）|
| Talen Energy（TLN）| 核電 + 氣電 | 2.5 GW 核電（Susquehanna）| **Amazon $18B 17 年 PPA 1.92GW**（2025-06 簽）（⚠️ 待 ingest）|

→ **核電 = 24/7 carbon-free baseload**、是 hyperscaler **AI 永續承諾 + 政治正確雙頭過關**的唯一答案

### 第二層：電力傳輸（Transmission）

把電送到 data center——**變壓器 / 開關 / EMS（能源管理系統）/ HVDC 設備**。

| 玩家 | 類型 | 規模 | 對 AI infra anchor |
|---|---|---|---|
| **[[GE Vernova]]**（GEV）| **變壓器 + 燃氣輪機 + 電網設備**（power-to-rack 整合）| backlog $163B（Q1 2026）| Prolec GE 併購（$5.275B、2026-02 完成）= 北美變壓器龍頭、Electrification 段 Q1 2026 拿 **$2.4B data center 訂單**（>整個 2025 全年）|
| ABB（瑞士）| HVDC 高壓設備、開關 | （未 ingest）| 跟 NVDA 共同制定 800V HVDC 標準 |
| Siemens Energy（德） | 變壓器、輸電 | （未 ingest）| 歐洲電網 anchor |

→ 變壓器全球緊缺 = **gas turbine production slots 排到 2030**（GEV 法說 Q1 2026），是真正的物理性瓶頸

### 第三層：電力分配（Distribution）

機房內配電——**UPS / PDU / 800V HVDC power module / 機架內電源**。

| 玩家 | 類型 | 規模 | 對 AI infra anchor |
|---|---|---|---|
| Schneider Electric（法）| UPS + PDU + EcoStruxure 整合平台 | 全球 #1 data center power | NVDA 800V HVDC 31 家伙伴之一 |
| Eaton（美 / 愛爾蘭）| UPS + 配電 | 2025-10 首發 800V DC reference architecture | NVDA 共同制定者 |
| Vertiv（VRT、美）| 機房液冷 + 配電 | （部分未 ingest）| 800V DC 產品線 H2 2026 上市 |
| **[[信昌電]]**（6173.TW）| 中高壓 MLCC（電源 PSU + BBU）| 機櫃用量 GB200 3-4K → Rubin **10K+ 顆** | NVDA Rubin AVL via 電源大廠（**現有 entity**）|
| STMicroelectronics（STM）| 800V→12V/6V GaN power module | 跟 NVDA 共同開發 | NVDA 共同制定者 |
| Texas Instruments（TXN）| 800V→6V GaN bus converter | 97.6% peak efficiency | NVDA 共同制定者 |
| Navitas（NVTS）| GaN 10kW DC-DC platform 98.5% 效率 | 全球 GaN pure-play | 800V HVDC IC 設計純度首選 |
| Infineon（IFX）| SiC + GaN power semi | （未 ingest）| HVDC 高壓段主力 |

→ **800V HVDC = NVDA 自己定義的 architecture standard**、把過去 Schneider / Eaton / ABB 各家方案統一成一條供應鏈

## 800V HVDC 為什麼 anchor？

**過去（54V rack）的物理極限**：

> 若 rack power 從 132kW 升到 700kW-1MW、用 54V 配電 → 需要 **64U 銅排空間**（接近整個 rack）+ **200 kg 銅 / rack** → 物理上不可能

**800V HVDC 解法**：

- 電壓提高 14.8 倍 → 銅用量減少 **45%**
- 端對端效率提升 **5%**（鎖定全棧能源損耗）
- 機櫃內回到 ~10U 配電空間
- **整條供應鏈 IC 廠（STM / TI / Navitas / Infineon）+ 系統廠（Eaton / Schneider / ABB / Vertiv）一起切到 GaN / SiC 新製程**

→ 連 [[控制點轉移（投資版）]]：800V 不是漸進升級，**是 NVDA 把整個 data center 電力 architecture 重新定義一次**

## 跟 [[宋分備忘錄 #3 — AI 半導體受惠者擴散]] 的對接

> 宋分 #3 點名「**類比 IC 是被遺忘的 AI 受惠者**」（TXN / ADI）—— 因為「AI 資料中心電源管理需求正爆發、估值仍按傳統景氣循環定價 → 結構性低估」

**電力戰場 = 宋分 #3「被遺忘的 AI 受惠者」的最大化版本**：

| 宋分 #3 觀察（類比 IC）| 電力戰場放大版 |
|---|---|
| TXN / ADI 估值仍按景氣循環 | Vistra / Constellation **直到 2024-09 Three Mile Island 簽約**才開始被 re-rate（兩家 12 個月漲幅 +200-400%）|
| AI 占類比 IC 營收悄悄上升 | 電力公司本身**從 stranded asset（核電被當包袱）→ AI 必需資產**完全轉性 |
| 結構性低估 | GEV backlog 從 $80B → **$163B / 17 個月**完整 re-rate，但**仍只反映前 5-7 年 backlog**（hyperscaler 已 booking 到 2030+）|

→ 電力戰場是「AI 受惠擴散」最強驗證：**不是製造 AI，而是 AI 製造完之後沒這個跑不動**

## 跟 [[宋分 #20 — 能源結構性剛需]] 的對接

宋分 #20 提出**結構性重估三標準**：

| 條件 | 電力戰場滿足 ✅/❌ | 證據 |
|---|---|---|
| **1. 長期供給結構改變** | ✅ **完全滿足** | 核電從「stranded asset」→「AI baseload」、Three Mile Island 復役（**首次**美國退役核電廠為單一商業客戶復役）、GE Vernova gas turbine slot 排到 2030 |
| **2. 持續性 CapEx** | ✅ **完全滿足** | 五年 $5.3 兆 hyperscaler CapEx 中電力 anchor、Vistra 一年內 PPA + Cogentrix $4.7B 收購、CEG $26.6B 併 Calpine、GEV $5.275B 併 Prolec |
| **3. 可持續現金流** | ✅ **完全滿足** | 20 年 PPA + 17 年 PPA 鎖定（CEG 5,650MW、VST 2.6GW、TLN 1.92GW）= 利率敏感性 < 純太陽能 / 風電 |

→ **三標準全滿** = 電力戰場是宋分 thesis 中**最完整的結構性重估個案**（vs 油氣需戰爭 catalyst、太陽能仍補貼依賴）

## 跟 [[賣水人選股邏輯（投資版）]] 的對接

電力戰場 = 「**賣水人之中的賣水人**」（不依賴任何 AI 技術路徑）：

- ✅ **不需賭誰贏**（OpenAI vs Anthropic？NVDA vs AMD？通通要 1MW rack）
- ✅ **量放大**：CapEx ↑ → 電力需求 ↑
- ✅ **規格升級**：132kW → 1MW → ?
- ✅ **平方放大**：量 × 規格升級 = **8x 電力需求 / 機櫃**

但跟一般「賣水人」不同：

| 一般賣水人（如 [[SiTime]] timing）| 電力戰場 |
|---|---|
| TAM 跟 AI CapEx 比例放大 | TAM **超比例放大**（132kW → 1MW = 8x，而模組數量也增加）|
| 進入障礙 = 技術 IP | 進入障礙 = **物理資產**（核電廠執照、土地、變壓器產線）|
| ramp 速度 = 製程開發週期 | ramp 速度 = **法規 + 工程建設**（核電廠復役 4-5 年、變壓器交期 2-3 年）|
| 競爭格局 = 多家 | 競爭格局 = **寡占 + 政治正確過濾**（核電 / 氣電 / 再生）|

## 跟 [[AI infra CapEx 三階段論]] 的對接

**電力 = 第三階段下半場 trigger**：

| 階段 | 內容 | 時點 |
|---|---|---|
| 第一階段 | CSP 講 CapEx（Google / Meta / MSFT / AMZN）| 已過 |
| 第二階段 | NVDA 設備落地 + ASIC 接力 | 已過 / 進行中 |
| 第三階段 ⭐ | 上游材料（InP / 1.6T 光模組）爆掉 + **電力** anchor 同時 | 2026 中（**現在**）|

**電力的特殊位置**：跟光通訊不同，**電力建設是真正的物理瓶頸**——

- 光通訊：產能 6-12 個月可雙倍化（半導體 fab 擴產）
- 電力：核電廠復役 **4-5 年**、變壓器 **2-3 年**、800V HVDC 標準化 **2027 才量產**

→ 這代表**第三階段下半場（2026 H2 - 2028）電力是 AI ramp 真正的卡點**

## 跟 [[效率→安全切換]] 的對接

電力戰場是「效率→安全」最強範例：

| 過去（效率）| 現在（安全）|
|---|---|
| Hyperscaler 從電網買電（cheapest spot price）| **20 年 PPA 鎖死 baseload**（MSFT-CEG / Meta-VST / AMZN-TLN）|
| 再生能源 + 電網平衡 | **核電 + 氣電 firm power**（24/7 dispatchable）|
| 全球分散 data center | **電力供應地優先**（北美核電 hub 集中） |

→ AI 公司不只是要算力，**要「24/7 不會斷」的算力** = 電力安全 > 電力成本

## 受惠玩家三層 anchor 排名

| 排名 | 玩家 | 戰場位置 | Anchor 強度 | 為什麼 |
|---|---|---|---|---|
| #1 | **[[Constellation Energy]]**（CEG）| 電力產生 / 核電 | 🟢 **最強** | Microsoft 20 年 PPA 直接、Calpine $26.6B 併購補氣電 firm power、32.4GW 核電 + 26GW 氣電 = 美國 IPP 龍頭 |
| #2 | **[[GE Vernova]]**（GEV）| 電力傳輸 / 變壓器 + 燃氣輪機 | 🟢 **最強** | backlog $163B、Prolec GE 併購、power-to-rack 全棧、Q1 2026 data center 訂單 $2.4B（>2025 全年）、gas turbine 100GW backlog 排到 2030 |
| #3 | **[[Vistra]]**（VST）| 電力產生 / 核電 + 氣電 | 🟢 **強** | Meta 20 年 2.6GW PPA、Cogentrix 5.5GW 待併、AWS PPA、Trump 政府支持 |
| #4 | Talen Energy（TLN，⚠️ 待 ingest）| 電力產生 / 核電 | 🟡 中強 | Amazon $18B 17 年 1.92GW PPA |
| #5 | Eaton（ETN，⚠️ 待 ingest）| 電力分配 / 800V HVDC reference architecture | 🟡 中強 | 2025-10 首發 800V DC ref architecture、NVDA 共同制定 |
| #6 | ABB（瑞，⚠️ 待 ingest）| 電力傳輸 + 分配 / HVDC | 🟡 中強 | NVDA 共同制定 800V HVDC 標準、歐洲 anchor |
| #7 | Schneider Electric（法，⚠️ 待 ingest）| 電力分配 / 機房 UPS + PDU | 🟡 中 | EcoStruxure 整合平台、800V DC NVDA 31 家伙伴之一 |
| #8 | Vertiv（VRT，⚠️ 待 ingest）| 電力分配 + 散熱 | 🟡 中 | 機房液冷 + 800V DC H2 2026 上市 |
| #9 | Navitas（NVTS，⚠️ 待 ingest）| 電力分配 / GaN power IC | 🟡 中（高 alpha） | 10kW 98.5% 效率、GaN pure-play、800V HVDC 純度首選 |
| #10 | **[[信昌電]]**（6173.TWO）| 電力分配 / 中高壓 MLCC（機櫃內 PSU + BBU） | 🟡 中 | NVDA Rubin 機櫃 MLCC 3-4K → 10K+ 顆（**現有 entity**）|

⭐ **anchor 排名邏輯**：
1. **PPA 鎖定**（20 年 firm contract）> backlog 訂單 > spot 出貨
2. **Hyperscaler 直接合約** > 透過代工 / 機櫃廠
3. **物理資產護城河**（核電執照 / 變壓器產線）> IP 護城河
4. **政治正確過濾**（核電 + 氣電 firm power）> 純再生能源（依賴補貼）

## ⭐ 800V HVDC 純度玩家 vs 多元組合

| 純度玩家 | 多元組合 |
|---|---|
| Navitas（NVTS）= GaN pure-play | STM、TI、Infineon = 半導體大廠多軌 |
| Talen Energy = 純 IPP 核電 | Constellation = 核電 + Calpine 氣電 + retail（更穩）|
| Eaton = 800V DC 首發 | Schneider = 整合平台多軌 |

→ **純度玩家高 alpha + 高波動**、**多元組合穩 + 估值合理**

## 跨庫對照（asset-wiki ↔ llm-wiki）

> llm-wiki 「Sovereign AI」概念中已提電力 / 能源安全。但 **asset-wiki 視角**獨立：
> - llm-wiki：AI 自主性與能源主權的因果連結
> - **asset-wiki：電力公司 P/L re-rating + 20 年 PPA 現金流鎖定的投資機會**

## ⚠️ 風險

### 1. 核電廠復役 / 新建延宕
- Three Mile Island 2028 上線、若延後 → MSFT 算力 ramp 延遲、CEG re-rate 部分回吐
- 新建核電廠 SMR（small modular reactor）2030+ 才可能商業化

### 2. CSP 自建電力
- Microsoft + Amazon **都已開始自建變壓器 / 自簽核電 PPA** = 把中間電力公司角色擠壓
- 連 [[CapEx 見頂辯論]]：CSP 垂直整合到電力後，傳統電力公司議價權弱化

### 3. 再生能源衝擊
- 若 SMR 2030 真的量產 → 傳統核電廠估值上限
- 大規模儲能技術突破 → 太陽能 + 儲能可取代部分 firm power

### 4. 變壓器供給追上
- GE Vernova 大規模擴產（CapEx +¥3,700 億）+ ABB / Siemens Energy 追進 → 2028+ 供需可能反轉
- 連 [[PB 估值法（記憶體週期）]]：物理瓶頸最終會被供給追上

### 5. 政治風險
- Trump 政府支持核電（CEG $1B 貸款）= 政治紅利
- 若 2028 政權更替、政策反轉 → 核電 anchor 動搖

## 跟其他 wiki 概念連結

- [[AI infra CapEx 三階段論]]：本 concept 是第三階段下半場「電力 anchor」獨立化
- [[賣水人選股邏輯（投資版）]]：電力戰場 = 「賣水人之中的賣水人」純度最高版本
- [[宋分備忘錄 #3 — AI 半導體受惠者擴散]]：電力戰場 = 「被遺忘的 AI 受惠者」放大版
- [[宋分 #20 — 能源結構性剛需]]：電力戰場 = 結構性重估三標準**全滿**個案
- [[效率→安全切換]]：電力戰場 = AI 公司「要 24/7 不斷算力」的安全代價
- [[控制點轉移（投資版）]]：NVDA 800V HVDC 把控制點從晶片推到電網
- [[半導體基礎建設化]]：電力公司也走同一路徑（從週期股 → 結構性成長股）
- [[MLCC 嵌入式基板賽道]]：[[信昌電]] 中高壓 MLCC 在第三層分配（機櫃內 PSU）受惠
- [[CapEx 見頂辯論]]：電力公司是「CapEx 不會見頂」的物理證據
- [[Re-rate 捕捉法]]：CEG / VST / GEV 12 個月 +200-400% 是 re-rate 完整週期範例

## 待 ingest 玩家延伸

### 美系電力 anchor
- Talen Energy（TLN）— Amazon Susquehanna 1.92GW PPA
- NRG Energy（NRG）— ERCOT 氣電 + retail
- Public Service Enterprise（PEG）— 紐約核電
- Duke Energy（DUK）— 美南電網 + 核電

### 變壓器 / 電網設備
- ABB（瑞士）— HVDC 高壓設備
- Siemens Energy（德國）— 變壓器、輸電
- Eaton（ETN，愛爾蘭）— UPS + 配電
- Schneider Electric（法）— EcoStruxure 整合平台
- Vertiv（VRT）— 機房液冷 + 配電
- Hubbell（HUBB）— 配電設備

### 800V HVDC power IC（高 alpha 區）
- Navitas Semiconductor（NVTS）— GaN pure-play
- Infineon（IFX）— SiC + GaN
- Wolfspeed（WOLF）— SiC pure-play（已破產 risk）
- onsemi（ON）— SiC + 類比 IC

### 散熱（power 戰場姊妹題、codex P1-3 同時提到）
- 待獨立建 [[AI infra 散熱戰場]] concept
- Vertiv、Asetek、Modine Manufacturing、Schneider

## 相關連結

- [[AI infra CapEx 三階段論]]
- [[賣水人選股邏輯（投資版）]]
- [[宋分備忘錄 #3 — AI 半導體受惠者擴散]]
- [[宋分 #20 — 能源結構性剛需]]
- [[效率→安全切換]]
- [[控制點轉移（投資版）]]
- [[半導體基礎建設化]]
- [[Re-rate 捕捉法]]
- [[Constellation Energy]]
- [[Vistra]]
- [[GE Vernova]]
- [[信昌電]]
- [[NVDA]]、[[Microsoft]]、[[Meta]]、[[AMZN]]、[[Google]]、[[OpenAI]]

## Sources

- [Microsoft / Constellation Three Mile Island 20 年 PPA（FinancialContent 2026-01-01）](https://markets.financialcontent.com/wral/article/tokenring-2026-1-1-the-nuclear-option-microsoft-and-constellation-energys-resurrection-of-three-mile-island-signals-a-new-era-for-ai-infrastructure)
- [Constellation Energy 2026-06-01 FERC 760MW Capacity Interconnection Rights 轉移核准（Utility Dive 2026-06）](https://www.utilitydive.com/news/constellation-three-mile-island-crane-nuclear-ferc-waiver/821836/)
- [Trump 政府 $1B 貸款 Three Mile Island 復役（CNBC 2025-11-18）](https://www.cnbc.com/2025/11/18/trump-nuclear-three-mile-island-crane-loan-constellation-ceg.html)
- [Vistra 20 年 Meta 2.6GW PPA（Yahoo Finance / Enverus 2026）](https://www.enverus.com/blog/vistra-doubles-down-on-data-centers/)
- [Vistra Cogentrix $4.7B 5.5GW 收購（Power Magazine / Utility Dive 2026-01-05）](https://www.utilitydive.com/news/vistra-cogentrix-natural-gas-energy-deal-data-centers/808854/)
- [GE Vernova Q1 2026 8-K（SEC 2026-04-22）](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000063/gevpressrelease1q26.htm)
- [GE Vernova Prolec GE 收購 $5.275B（2026-02-02 完成）](https://www.tikr.com/blog/ge-vernova-is-sold-out-and-scaling-up-why-its-83-gigawatt-backlog-points-to-a-potential-25-share-price-increase)
- [GE Vernova 100GW gas turbine backlog + 數據中心訂單（mgrid 2026-04-22）](https://mgrid.org/2026/04/22/ge-vernovas-gas-turbine-backlog-hits-100-gw-as-data-centers-drive-4-billion-in-q1-orders/)
- [NVIDIA 800V HVDC architecture 31 家伙伴（China Energy Storage 2025-11-25）](http://en.cnesa.org/latest-news/2025/11/25/nvidias-800v-architecture-reshapes-ai-data-centers-31-core-industry-chain-companies-unveiled)
- [NVIDIA 800V Architecture for AI Factories（NVIDIA Dev Blog）](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- [Schneider Electric: The 1 MW AI IT rack is coming（2025-10-16）](https://blog.se.com/datacenter/2025/10/16/the-1-mw-ai-it-rack-is-coming-and-it-needs-800-vdc-power/)
- [Talen Energy + Amazon $18B 17 年 PPA（Power Magazine 2025-06）](https://www.powermag.com/talen-amazon-launch-18b-nuclear-ppa-a-grid-connected-ipp-model-for-the-data-center-era/)
- [Constellation $16.4B Calpine 收購 + 26GW 氣電（FinancialContent 2026-03）](https://www.financialcontent.com/article/marketminute-2026-3-10-constellation-energy-finalizes-164-billion-calpine-acquisition-solidifying-lead-in-ai-data-center-power-race)
- [STMicroelectronics 800V DC NVDA 12V/6V architecture（ST Newsroom）](https://newsroom.st.com/media-center/press-item.html/t4766.html)
- [Navitas 10kW 98.5% GaN 800V DC platform](https://navitassemi.com/navitas-unveils-breakthrough-10-kw-dc-dc-platform-delivering-98-5-efficiency-for-800-vdc-next-gen-ai-data-centers/)
- [TI 800V DC architecture with NVIDIA（TI Newsroom 2026-03-16）](https://www.ti.com/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers.html)

---
title: MLCC 嵌入式基板賽道
aliases: [MLCC 嵌入式基板, 嵌入式被動元件, embedded passives, ECP, LSC, embedded MLCC, embedded silicon capacitor, iPaS, SESUB]
type: concept
created: 2026-06-05
updated: 2026-06-05
as_of: 2026-06-05
check_after: 2026-12-05
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [MLCC, 嵌入式基板, ABF, 被動元件, 載板, IBIDEN, SEMCO, 村田, 國巨, silicon capacitor]
confidence: medium
---

# MLCC 嵌入式基板賽道

「**第二戰場**」——AI 載板的下一波 displacement，**嵌入式被動元件**取代板上分立 MLCC。賽道結構跟 [[玻璃基板與 FOPLP 賽道]] 平行：載板廠主導 + 元件廠供應 + 台廠落後最大。

## 一句話

> 把 MLCC 從板面上嵌進載板內 = ABF 廠主場 + MLCC 廠淪供應方。

## 為什麼這個賽道重要

- **物理瓶頸**：AI 載板 power delivery 路徑越短、訊號完整性越好——板面 MLCC 距 IC 太遠、嵌入式靠近 die 直接降低 ESL/ESR 100 倍以上（[passive-components.eu 2026-05](https://passive-components.eu/samsung-electro-mechanics-signs-1-5t-krw-silicon-capacitor-ai-contract/)）
- **NVDA Rubin 1MW 機櫃**：機櫃用 MLCC 從現行 3,000-4,000 顆倍增至 **逾 10,000 顆**（信昌電法說 2026-05，[BigGo 2026-05-21](https://finance.biggo.com.tw/news/TW_6173.TW_2026-05-21)）
- **VR200 NVL72 機櫃 MLCC BOM**：USD 4,320（GB300 1,530 → +182%）（[EE Times 2026](https://www.eetimes.com/power-integrity-for-nvidia-h200-based-ai-servers-the-role-of-capacitors-in-system-reliability/) / [Big News Network 2026](https://www.bignewsnetwork.com/news/279099682/nvidia-vera-rubin-boosts-demand-for-ai-server-capacitors-creates-opportunity-for-samsung-electro-mechanics)）
- **載板層數越多 → 板面空間越貴**：嵌入式釋放板面 → 給其他元件 / 散熱
- **IBIDEN ¥5,000 億 CapEx 含嵌入式產線**（[Digitimes 2026-04](https://www.digitimes.com/news/a20260430VL217/embedded-substrate-unimicron-semco-ibiden.html)）
- **這是 ABF 廠對 [[玻璃基板與 FOPLP 賽道]] displacement 的對應策略**——「向外」走玻璃化、「向內」走嵌入化

## 技術分類

賽道內**三條路線並行**、不是 binary winner：

### 1. 嵌入式 MLCC（Embedded MLCC / ECP）

- 把分立 MLCC 直接埋入 ABF 載板內、靠近 die
- **[[太陽誘電 Taiyo Yuden]]** 2025 量產**世界首發** 1005 size 22μF + 2012 size 100μF（[Passive Components 2025](https://passive-components.eu/taiyo-yuden-releases-22uf-mlcc-in-0402-size-for-ai-servers/) / [ntclcr.com](https://www.ntclcr.com/taiyo-yuden-achieves-mass-production-of-1005-sized-high-capacitance-mlc)）
- **[[Samsung Electro-Mechanics]]** 越南廠 2026-04 宣布 MLCC 嵌入式專線（[Digitimes 2026-04](https://www.digitimes.com/news/a20260414PD221/semco-mlcc-embedded-substrate-packaging.html) / [Seoul Economic Daily 2026-04](https://en.sedaily.com/finance/2026/04/14/samsung-electro-mechanics-to-invest-12-billion-in-vietnam)）
- 技術重點：carve 載板凹槽精準放 MLCC + 嵌入後直接接 die

### 2. 嵌入式矽電容（Embedded Silicon Capacitor）⭐ 高階主流

- **完全不同類別**——不是 ceramic，是 silicon-based、製程跟晶圓接近
- **ESL/ESR 比 MLCC 低 100 倍**（[Tech Times 2026-05](https://www.techtimes.com/articles/316907/20260521/samsung-electro-mechanics-wins-1b-silicon-capacitor-deal-murata-tsmc-duopoly-faces-new-rival.htm)）
- 市場 2025 USD 1.8B → 2035 USD 3.4B（CAGR ~6.5%）
- **歷史寡占**：[[村田 Murata]] + [[TSMC]] 兩家壟斷
- **[[Samsung Electro-Mechanics]] 2026-05 拿 1.5 兆韓元（USD 10 億）合約**（客戶未揭露、推測 NVDA / AMD / AWS / Marvell 之一）= 寡占破局訊號（[Asia Business Daily 2026-05](https://www.asiae.co.kr/en/article/2026052014402953882)）
- 2027-01 起到 2028-12 兩年交期

### 3. 嵌入式電感（Embedded Inductor）+ Integrated Module

- **[[村田 Murata]] iPaS™**（Integrated Package Solution）：薄片鋁電解電容 + 平面 coil 整合（[Murata 官方](https://corporate.murata.com/en-us/technology/technology-applications/integrated-package-solution)）
- 可承受 >100A 大電流、為 Vertical Power Delivery (VPD) 設計
- 主要客戶：AI 數據中心 power module + AI accelerator package
- **[[TDK]] SESUB**（Semiconductor Embedded in SUBstrate）：把 IC + passives 一起埋進 300μm 厚基板
- 都偏向「power supply 模組」、不是純 MLCC 替代

### 4. Land Side Capacitor (LSC) — 邊界戰場

- 不是嵌入式、是貼在 substrate **背面 die 投影下**（[WikiChip](https://en.wikichip.org/wiki/land-side_capacitor)）
- 提供 1-10 MHz 頻段的快速電流響應（PDN 穩壓）
- NVDA / AMD 旗艦封裝都用 LSC + embedded 雙線並行
- 因 package 越大、LSC 空間反而被擠 → 推動嵌入式取代

## 兩大主導陣營（誰在做）

### A 陣營（載板廠主導，把被動元件「吃進來」）

| 玩家 | 進度 | 動作 |
|---|---|---|
| **[[Samsung Electro-Mechanics]]** | **先發 #1** | 越南新廠 2026 H2 量產 + 矽電容 USD 10 億合約（2027-01 起）+ 智慧型手機模組 10 年累積經驗 |
| **[[IBIDEN]]** | **追擊 #2** | ¥5,000 億 CapEx 涵蓋嵌入產線、2027 量產 |
| **[[Unimicron]] 興進** | 跟進 #3 | Digitimes 點名「準備進入」 |
| **[[欣興]]** | 跟進 #4 | 評估中、揭露少 |
| **[[南電]] / [[景碩]]** | 觀望 #5-6 | 點名但無公開動作 |

### B 陣營（MLCC 廠跟進，避免被「吃進去」）

| 玩家 | 全球地位 | 嵌入式動作 |
|---|---|---|
| **[[村田 Murata]]**（6981.JP） | MLCC #1（40%+ 市佔） | **iPaS™ 已商業化** + 矽電容歷史寡占（與 TSMC 並列） |
| **[[太陽誘電 Taiyo Yuden]]** | MLCC top 4 | **世界首發** 嵌入式 MLCC（2025、1005 size 22μF） |
| **[[TDK]]** | MLCC top 3 | SESUB 模組（IC + passives 整合） |
| **[[Samsung Electro-Mechanics]]** | MLCC #2（同時是載板廠） | **雙陣營玩家**——既做 MLCC、又自做嵌入式載板 |
| **[[國巨]]**（2327.TW） | MLCC #3 | 高壓 MLCC 切 AI、嵌入式產品線**未公開揭露** |
| **[[華新科]]**（2492.TW） | MLCC top 5 | X6S + 中高壓 MLCC 切 AI 鏈、嵌入式**未揭露** |
| **[[信昌電]]**（6173.TW，華新科子公司）| 高壓 MLCC 利基 | NVDA Rubin 機櫃高壓單一規格放量、嵌入式**未明確披露** |

## 為什麼「台廠落後最大」（IBIDEN subagent 結論校準）

- **嵌入式技術需要載板廠 + MLCC 廠雙領域整合 know-how**
  - 載板廠要會 carve 凹槽 + 流程整合
  - MLCC 廠要會做超薄、超高密度、能適應載板熱應力的元件
  - 兩家之間 yield、料件搭配、應用方案是黑盒子

- **日韓有本土整合優勢**：
  - 日陣營：[[IBIDEN]] + [[村田 Murata]]（同國）+ [[太陽誘電 Taiyo Yuden]] + [[TDK]] = **MLCC 三大全日本** + 載板龍頭日本 = 國家級垂直整合
  - 韓陣營：[[Samsung Electro-Mechanics]] 自己「既是載板廠又是 MLCC 廠」+ Samsung Display panel 加工 + Samsung Foundry = **集團內整合鏈閉環**

- **台廠 ABF（[[欣興]] / [[南電]] / [[景碩]]）+ MLCC（[[國巨]] / [[華新科]] / [[信昌電]]）沒有共同集團整合**
  - 兩個產業在台灣是**分開的供應鏈**
  - 載板廠跟 MLCC 廠之間沒有 cross-licensing、沒有共同 R&D
  - → 過渡期可能買日韓嵌入式方案、自做有時間差

- → **押賽道的台廠選擇有限**（只有 ABF 三雄是「自做選項」、MLCC 純廠很可能淪賣料）

## 投資啟示

### 真贏家

| 公司 | 為什麼 |
|---|---|
| **[[Samsung Electro-Mechanics]]** | 雙陣營玩家、唯一「載板 + MLCC + silicon capacitor」三軌、先發 +越南產線 + USD 10 億合約已 lock-in |
| **[[村田 Murata]]** | MLCC #1 + 矽電容寡占 + iPaS 已商業化 = **嵌入式潮流自己也吃得到、不被取代** |
| **[[IBIDEN]]** | ¥5,000 億 CapEx 砸下去、有底氣追擊 + NVDA/Intel/Apple 客戶綁定 = 嵌入式產線會被 design-in |
| **[[太陽誘電 Taiyo Yuden]]** | 嵌入式 MLCC 世界首發、IP 領先 + 日陣營協同 |

### 受壓

| 公司 | 風險 |
|---|---|
| **純 MLCC 廠 [[國巨]] / [[華新科]]** | 嵌入式破壞「賣分立 MLCC」模式、若無嵌入式產品線會被擠 |
| **[[信昌電]]** | 高壓 MLCC 利基目前受惠 NVDA Rubin 1MW、但嵌入式滲透若擴散到高壓會被切 |
| **[[南電]] / [[景碩]]** | 嵌入式進度落後 SEMCO/IBIDEN、外溢訂單也未明朗 |

### 觀察點

- **[[欣興]] 是否跟進嵌入式**：跟玻璃化進度一起看、不跟就只剩 ABF 老本
- **[[國巨]] 是否做嵌入式 MLCC 或矽電容**：是 → 雙陣營雙押 / 否 → 純被切
- **NVDA Rubin Ultra 的封裝方案揭露**（2027 H1）：選用「分立 MLCC + embedded silicon capacitor 雙線」還是「全 embedded」會決定純 MLCC 廠 2028+ 命運

## ⭐ 2026-06-09 KP@FOMOSoc 補強：被動元件第三次週期（K 型復甦）

→ 詳細 [[被動元件第三次週期（K 型復甦 + 三道防線）]]

KP@FOMOSoc 2026-04-29 補強框架——本 concept 描繪賽道結構，KP 補入**歷史週期 + K 型復甦 + 2026 Q3 轉折點預測**：

| 維度 | KP 補強 anchor |
|---|---|
| **歷史週期** | 第一次（2017-18 普遍性缺貨、國巨淨利 +583%）+ 第二次（2019-24 漫長去庫存、國巨營收 -40%）+ **第三次（2025-26 K 型結構性缺貨）** |
| **K 型復甦** | 高階 MLCC 一貨難求（交期 24-32 週）vs 中低端殺價競爭、村田 95% / 三星電機 92% 稼動率、庫存天數 30 天（健康 40 天） |
| **2026 Q3 轉折點預測** | Vera Rubin 量產 + IT 旺季疊加 = 引爆「恐慌性下單」 |
| **三道防線設計** | MLCC（陶瓷工藝）+ 聚合物鋁電容（電化學）+ 鉭電容（化學冶金）= **無法贏者全拿** |
| **NVL72 機櫃 MLCC 量化** | 傳統 server 2-3K 顆 → **NVDA NVL72 機櫃 44 萬顆**（~150-200x 暴增）|

→ 「**這次不一樣**」三大差異（vs 2018）：(1) 結構性缺貨 vs 普遍性 + (2) CSP 長期協議 vs 恐慌訂單 + (3) 供應側微調 vs 新建工廠

→ 對應 [[800V HVDC 灰白區重劃（物理鐵壁論）]]（同 KP@FOMOSoc 來源）：兩篇對應 NVDA Vera Rubin / NVL72 機櫃**兩個物理結構維度**——機櫃外電力升 800V HVDC + 機櫃內電容降 0.8-1V 三道防線

## 跟其他 wiki 概念連結

- [[被動元件第三次週期（K 型復甦 + 三道防線）]]（2026-06-09 KP@FOMOSoc 補強）
- [[玻璃基板與 FOPLP 賽道]]：對應的「向外擴張」displacement——載板廠「向內」走嵌入化 + 「向外」走玻璃化雙線策略
- [[ABF 載板 vs 玻璃基板 displacement]]：第一戰場、本 concept 是第二戰場
- [[控制點轉移（投資版）]]：載板廠想拿被動元件控制權、MLCC 廠想守住分立元件 BOM
- [[半導體基礎建設化]]：載板廠估值重估的另一個維度——除了玻璃 option、嵌入式是「BOM 上升 + 控制點上移」
- [[賣水人選股邏輯（投資版）]]：MLCC 廠**過去是純賣水人**（不管誰贏都賣料）、嵌入式破壞了這個地位（載板廠把料件吃進來、MLCC 廠淪 OEM）
- [[預期差]]：台廠 MLCC 廠的嵌入式曝險**未被市場討論**（市場仍在用「AI server MLCC BOM 倍增」敘事、沒在 price in displacement）
- [[資訊擴散四階段]]：本 concept 在「機構→賣方」之間（Digitimes / Korea Herald 揭露、但西方 sellside 尚未系統性報告）

## 跟第一戰場（玻璃化）的結構性差別

| 維度 | 第一戰場（玻璃化） | 第二戰場（嵌入式 MLCC） |
|---|---|---|
| **改變的東西** | 基板材料：有機 → 玻璃 | BOM 結構：分立 → 嵌入 |
| **驅動方** | Intel / Samsung / Apple chip 設計方 | 載板廠 + 客戶共同推 |
| **位移幅度** | 極端（整片基板換掉） | 漸進（部分高頻 path 先嵌） |
| **TAM 影響** | 玻璃 TAM 從零起、ABF TAM 被切 | MLCC TAM 結構性變化、嵌入式 TAM 新增 |
| **誰先發** | [[Absolics]] / [[Samsung Electro-Mechanics]] 韓國雙頭 | [[Samsung Electro-Mechanics]] 韓國 + [[太陽誘電 Taiyo Yuden]] 日本 |
| **台廠位置** | 設備鏈（[[鈦昇]] / [[雷科]] 等）拿到 first-mover；ABF 廠落後 | 設備鏈**沒有獨立空間**（嵌入式凹槽用既有雷射 / 蝕刻設備）；ABF 廠 + MLCC 廠全落後 |
| **被切的台廠** | ABF 三雄部分高階產品線 | MLCC 三雄（國巨 / 華新科 / 信昌電）+ 部分 ABF |
| **時程** | 2026 sample → 2028+ 主流 | 2026 量產 → 2028 滲透高階 |
| **進入門檻** | 玻璃材料 + TGV 鑽孔技術（明確） | 載板廠 + MLCC 廠 know-how 整合（模糊） |

→ **整合啟示**：玻璃化是「換零件、台廠設備鏈受惠」；嵌入式是「換結構、台廠雙線受壓」。**第二戰場對台廠**真實**更不利**（設備鏈、零件鏈、整合鏈三線都沒拿到 first-mover）。

## 待 ingest 延伸

- ✅ [[村田 Murata]]（已建、entity）
- ✅ [[太陽誘電 Taiyo Yuden]]（已建 2026-06-05、entity）：嵌入式 MLCC 世界首發（1005M 22μF + 2012 100μF lineup 完整）、IP first-mover、五軸 19/25（IP 5 / 客戶分散 1）
- ✅ [[TDK]]（已建 2026-06-05、entity）：SESUB 模組獨家 + Apple iPhone 電池 + 鋁電解 AI PSU + HDD 多元組合、CEO 宣告 AI data center 用被動 10 倍成長 by FY2031、五軸 19/25
- ✅ [[國巨]] / [[華新科]] / [[信昌電]]（已建，2026-06-05）：台廠 MLCC 三角的嵌入式曝險具體量化
  - [[國巨]]：MLCC #3 + 全品線、嵌入式落後（無 embedded MLCC、無載板廠盟友）、Re-rate 4/4
  - [[華新科]]：大中華 #1 + 中階通用、嵌入式完全缺席（規模 + 技術 + 通路三缺）、Re-rate 2/4
  - [[信昌電]]：中高壓 niche specialist（粉末自製 + 大尺寸 1206-2220 + Mega Cap）、嵌入式**短期不切、2029+ 時程賽跑**（村田 1.25kV C0G 1210 已量產）、Re-rate 3/4、五軸 19/25
- 嵌入式被動元件 vs 分立元件**單機 BOM 成本曲線**（追蹤 NVDA Rubin → Rubin Ultra 用量變化）

## 相關連結

- [[玻璃基板與 FOPLP 賽道]]
- [[ABF 載板 vs 玻璃基板 displacement]]
- [[控制點轉移（投資版）]]
- [[半導體基礎建設化]]
- [[賣水人選股邏輯（投資版）]]
- [[預期差]]
- [[資訊擴散四階段]]
- [[IBIDEN]]、[[Samsung Electro-Mechanics]]、[[欣興]]、[[南電]]、[[景碩]]
- [[村田 Murata]]、[[Absolics]]
- [[NVDA]]、[[Intel]]、[[Apple]]、[[AVGO]]、[[AMD]]
- [[sennn.nnna]]

## Sources

- [Embedded substrates draw AI chip interest as packaging turns strategic (Digitimes 2026-05)](https://www.digitimes.com/news/a20260522PD220/embedded-packaging-ai-chip-nvidia-intel.html)
- [AI chip demand ignites embedded substrate race among Samsung, Ibiden, Unimicron (Digitimes 2026-04)](https://www.digitimes.com/news/a20260430VL217/embedded-substrate-unimicron-semco-ibiden.html)
- [Samsung Electro-Mechanics reportedly to expand AI packaging with MLCC embedded substrate line in Vietnam (Digitimes 2026-04)](https://www.digitimes.com/news/a20260414PD221/semco-mlcc-embedded-substrate-packaging.html)
- [Samsung Electro-Mechanics to Invest $1.2 Billion in Vietnam (Seoul Economic Daily 2026-04)](https://en.sedaily.com/finance/2026/04/14/samsung-electro-mechanics-to-invest-12-billion-in-vietnam)
- [Samsung Electro-Mechanics Wins $1B Silicon Capacitor Deal (Tech Times 2026-05)](https://www.techtimes.com/articles/316907/20260521/samsung-electro-mechanics-wins-1b-silicon-capacitor-deal-murata-tsmc-duopoly-faces-new-rival.htm)
- [Samsung Electro-Mechanics Signs 1.5T KRW Silicon Capacitor AI Contract (Passive Components 2026-05)](https://passive-components.eu/samsung-electro-mechanics-signs-1-5t-krw-silicon-capacitor-ai-contract/)
- [Samsung Electro-Mechanics Wins Major 1.5 Trillion Won Silicon Capacitor Order (Asia Business Daily 2026-05)](https://www.asiae.co.kr/en/article/2026052014402953882)
- [Samsung Electro-Mechanics pours W1tr into AI substrates (Korea Herald 2026)](https://www.koreaherald.com/article/10709586)
- [ABF 載板之後，下一個戰場 MLCC 嵌入式基板 Semco vs Ibiden vs 欣興 (豐雲學堂 2026-06)](https://www.sinotrade.com.tw/richclub/hotstock/ABF-%E8%BC%89%E6%9D%BF%E4%B9%8B%E5%BE%8C-%E4%B8%8B%E4%B8%80%E5%80%8B%E6%88%B0%E5%A0%B4%E6%98%AF%E9%80%99%E5%80%8B-MLCC-%E5%B5%8C%E5%85%A5%E5%BC%8F%E5%9F%BA%E6%9D%BF-Semco-%E7%9A%84%E5%85%88%E7%99%BC%E5%84%AA%E5%8B%A2-Ibiden-%E5%92%8C%E6%AC%A3%E8%88%88%E7%9C%9F%E7%9A%84%E8%BF%BD%E5%BE%97%E4%B8%8A-%E2%94%82%E8%82%A1%E5%B8%82%E8%A9%B1%E9%A1%8C-69f81429b73b6300a0da7c87)
- [Taiyo Yuden Mass Produces World's First 1005-Sized 22μF Embedded MLCC (Passive Components 2025)](https://passive-components.eu/taiyo-yuden-releases-22uf-mlcc-in-0402-size-for-ai-servers/)
- [Murata iPaS Technology Application (Murata Corporate)](https://corporate.murata.com/en-us/technology/technology-applications/integrated-package-solution)
- [Land-Side Capacitor (LSC) (WikiChip)](https://en.wikichip.org/wiki/land-side_capacitor)
- [Power Integrity for NVIDIA H200-Based AI Servers (EE Times)](https://www.eetimes.com/power-integrity-for-nvidia-h200-based-ai-servers-the-role-of-capacitors-in-system-reliability/)
- [Nvidia's Vera Rubin boosts demand for AI server capacitors (Big News Network)](https://www.bignewsnetwork.com/news/279099682/nvidia-vera-rubin-boosts-demand-for-ai-server-capacitors-creates-opportunity-for-samsung-electro-mechanics)
- [信昌電 FY2026 Q1 法說會 (BigGo 2026-05)](https://finance.biggo.com.tw/news/TW_6173.TW_2026-05-21)
- [Passive Embedding TDK SESUB (TDK Electronics)](https://www.tdk-electronics.tdk.com/en/374108/tech-library/articles/products-technologies/products-technologies/passive-embedding/1109486)
- [Empower Extends Embedded Silicon Capacitors for AI (Passive Components)](https://passive-components.eu/empower-extends-embedded-silicon-capacitors-for-ai/)
- [AMD Announces More Than $10 Billion in Taiwan Ecosystem Investments (AMD 2026-05)](https://www.amd.com/en/newsroom/press-releases/2026-5-20-amd-announces-more-than-10-billion-in-taiwan-ecos.html)

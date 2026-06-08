---
title: HBM4E × Glass Interposer × TGV 交會
aliases: [HBM4E 玻璃中介層交會點, 三戰場 2028 anchor, HBM4E TGV anchor, 記憶體 × 玻璃 × 封裝交會]
type: concept
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2026-12-08
expires_on: 2028-12-31
sources:
  - WebSearch 2026-06-08（HBM4E / CoPoS / Intel glass / Absolics 五查詢綜整）
evidence_url: https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/
tags: [HBM4E, 玻璃中介層, TGV, 先進封裝, 2028 anchor, AI 記憶體, SK Hynix, Samsung, Micron, TSMC CoPoS, Intel, Absolics, 交叉概念]
confidence: medium
---

# HBM4E × Glass Interposer × TGV 交會

**2026-06 codex P1-6 補位**——把散落在 [[AI 記憶體結構性供給短缺]] Tier 3 與 [[玻璃基板與 FOPLP 賽道]] 時間線的「**HBM4E + 玻璃中介層 + TGV 三戰場 2028 anchor**」收束成單一交叉 concept。

## 一句話

> **2027 H2 → 2028 是 AI 半導體三個獨立戰場（記憶體 / 中介層 / 載板）首次在同一時間窗交會**——HBM4E 量產 + TSMC CoPoS 玻璃中介層 ramp + Intel Rio Rancho 玻璃載板量產，三條曲線收斂到同一個 SKU（NVDA Rubin Ultra 級 GPU）。這是 [[市場四階段：懷疑／驗證／共識／反轉]] 從「驗證」進「共識」的 anchor。

## 為什麼 2028 是 anchor（三戰場同時就位）

### 戰場 1：記憶體（HBM4E）

HBM4E 是 HBM4 的客製化 + 容量升級版（16-Hi、20 Gbps/pin），三巨頭 2026 H1 完成開發、2027 量產、**2027 H2 → 2028 全面 ramp**：

| 廠商 | HBM4E sample / 開發完成 | 量產時點 | 來源 |
|---|---|---|---|
| **SK Hynix** | 2026 H2 sample（[Seoul Economic Daily 2026-04-23](https://en.sedaily.com/finance/2026/04/23/sk-hynix-to-ship-hbm4e-samples-in-h2-begin-mass-production)）| **2027** | Yongin Cluster 2027 投產，先打 HBM4 / HBM4E |
| **Samsung** | 2026-06-01 首發 sample（[[AI 記憶體結構性供給短缺]] 已記）+ HBM4E 上 HPB 散熱（[Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/samsung-shows-first-hbm5-mockup-at-computex-with-heat-path-block-cooling)）| **2027** | P5 fab 2028 投產，承接 HBM4E 放量 |
| **Micron** | 2026 H1 sample（[TrendForce 2026-01-23](https://www.trendforce.com/news/2026/01/23/news-samsungs-custom-hbm4e-design-reportedly-aimed-for-mid-2026-parallels-sk-hynix-and-micron/)）| **2027-2028** | Singapore HBM packaging 廠 2027 ramp、Idaho fab #1 2027 mid 出片、#2 2028 末投產（[TrendForce 2026-05-27](https://www.trendforce.com/news/2026/05/27/news-inside-microns-1-trillion-market-cap-leap-a-global-fab-expansion-overview-across-the-u-s-and-asia/)）|

**結構性意涵**：HBM4E 是**自 HBM 誕生以來第一次三巨頭時程完全收斂**（差距 < 6 個月）——TSV stacks 從 12-Hi 走向 16-Hi、bandwidth 上看 2 TB/s/stack，**對中介層的物理需求超過矽 interposer 良率上限**。

### 戰場 2：玻璃中介層（TSMC CoPoS）

[[TSMC]] CoPoS（**Chip-on-Panel-on-Substrate**）= CoWoS 玻璃中介層演化版，2026-04 已確認時程（[TrendForce 2026-04-13](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)）：

| 階段 | 時點 | 細節 |
|---|---|---|
| Pilot line（VisEra） | **2026-06 完成** | 310×310 mm 玻璃 panel、trial yield 90%（透過 Xintec） |
| Small-volume trial | **2027** | NVDA Rubin / AMD MI400+ 樣品階段 |
| **Mass production** | **2028-2029 ramp** | 全速放量、315×510 mm panel 升級規劃 |

**panel 級面積效率**：圓形 wafer 利用率 57% → 矩形 panel 87%（[TechPowerUp](https://www.techpowerup.com/337960/tsmc-prepares-copos-next-gen-310-x-310-mm-packages)），**單 panel 算力比 wafer 高 53%**。

**和 HBM4E 的鎖死關係**：CoPoS 玻璃中介層厚度 ~400 µm、CTE 比 wafer 更精準（[TrendForce 2026-04-13](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)）——**是 HBM4E 16-Hi 唯一能撐得起的中介層方案**（矽 interposer 在 12-Hi 已撞翹曲與良率牆）。

### 戰場 3：玻璃載板（Intel Rio Rancho / SEMCO Sejong / Absolics Georgia）

| 玩家 | 廠地 | 量產時點 | 客戶 anchor | 來源 |
|---|---|---|---|---|
| **[[Absolics]]** | Georgia Covington | **2026 H2 ramp** | [[AMD]] MI400 volume sample（[Elec 2026](https://www.thelec.net/news/articleView.html?idxno=5476)）+ AWS Trainium + AVGO 通訊 | [[玻璃基板與 FOPLP 賽道]] |
| **[[Samsung Electro-Mechanics]]** | Sejong + Pyeongtaek（Sumitomo 廠地）| **2027 H2** | Apple Baltra / AVGO / 大型雲端（[Digitimes 2026-04](https://www.digitimes.com/news/a20260414VL204/chips-glass-substrate-demand-intel-production-semco.html)）| [[玻璃基板與 FOPLP 賽道]] |
| **[[Intel]]** | **Rio Rancho NM**（crown jewel）+ Chandler AZ pilot | **2030**（with CPO 共商業化）| Intel Foundry / 第三方 OSAT 委外 | [TrendForce 2026-05-26](https://www.trendforce.com/news/2026/05/26/news-intel-reportedly-eyes-worlds-first-glass-substrate-output-at-rio-rancho-offers-silicon-photonics-to-customers/)、[WCCFTech](https://wccftech.com/intel-foundry-rio-rancho-facility-crown-jewel-in-production-of-glass-substrates/) |
| **[[TSMC]] CoPoS** | VisEra → 中科 / 南科 | **2028-29 ramp** | NVDA Rubin Ultra + 全 OSAT 客戶 | 上表 |

### 三戰場交會的物理鎖死關係

```
HBM4E 16-Hi（2027-2028 ramp）
    │
    ▼ 必須堆在
玻璃中介層（TSMC CoPoS / Absolics、SEMCO）— 2026 H2 → 2028 ramp
    │
    ▼ 必須鋪在
玻璃載板（SEMCO 2027 H2、Intel 2030）+ TGV（[[TGV 製程鏈圖譜]]）八站製程
    │
    ▼ 鏈到 GPU
NVDA Rubin Ultra（2027 H2，NVL576 600kW Kyber rack）+ AMD MI500（2028）+ AVGO ASIC
```

**鎖死意涵**：三戰場**不是平行的賽道**，是**同一個 SKU 的三層垂直 stack**——HBM4E 沒有玻璃中介層撐不起 16-Hi 良率、玻璃中介層沒有 TGV 八站做不出 1mm pitch、TGV 沒有玻璃載板就沒有客戶要它。**三戰場必須同時 ramp，缺一個整個 stack 推遲**。

## 投資受惠玩家（按戰場分層）

### 戰場 1：HBM4E 三巨頭

| 公司 | HBM4E 位階 | wiki 既有評分 |
|---|---|---|
| [[SK Hynix]] | NVDA Rubin Ultra HBM4E **70% 訂單**、MR-MUF 製程領先 | 五軸 23/25 ⭐ |
| [[Samsung Electronics]] | HBM4E 首發 sample + HPB 散熱、Google TPU 60% 主供 | 五軸 21/25 |
| [[Micron]] | NVDA HBM4 10-20%、Singapore + Idaho 雙軌但落後 | 五軸 20/25 |

### 戰場 2：玻璃中介層整合方

| 公司 | 角色 | wiki 既有評分 |
|---|---|---|
| [[Absolics]] | **2026 H2 全球首條商業化** + AMD MI400 design-in | SKC 母公司 KRW 5.31T，2025 淨損 KRW 734B（仍燒錢期） |
| [[Samsung Electro-Mechanics]] | 2027 H2 量產、Apple Baltra sample 已交、SEMCO + Sumitomo JV | 五軸 19/25（[[玻璃基板與 FOPLP 賽道]]）|
| [[TSMC]] | CoPoS 2028-29 mass production、VisEra pilot 2026-06 完成 | 賣水人中性玩家 |
| [[日月光 ASE]] | SPIL 2026 Q3 TGV pilot、CoWoP 委外 | 五軸 4/4 Re-rate |
| [[Amkor]] | Intel EMIB 三地外包獨家、玻璃基板「3 年內商業化」 | Re-rate 2/4 |

### 戰場 3：玻璃材料 + TGV 製程

| 公司 | 角色 |
|---|---|
| **材料**：[[Corning]] | Glass core 25% 市佔、Nvidia $3.2B 戰略投資 |
| **材料**：[[AGC]] | EN-A1 規格 / 510×515 mm panel 揭露最完整、Forward PE 14.45（三巨頭最便宜）|
| **材料**：[[SCHOTT]] | HermeS 預製 TGV wafer + LPKF LIDE 整合 |
| **材料**：[[Sumitomo Chemical]] | SEMCO 韓系玻璃 core 鏈 + Dongwoo Pyeongtaek 廠地 |
| **TGV 製程**：[[鈦昇]] | LPKF 雷射改質 first-mover、Intel Clearwater Forest design-in |
| **TGV 製程**：[[雷科]] | 雷射打孔 + AMD/NVDA 認證 2026 Q1 定案 |
| **TGV 製程**：[[弘塑]]、[[辛耘]]、[[德律]]、[[萬潤]] | 蝕刻 / 電鍍 / CMP / AOI / AXI 中性賣水人 |

## alpha 點（時間窗 + 訂單能見度）

### 短週期 alpha（2026 H2 → 2027 H1）

1. **Absolics ramp first-mover**：2026 H2 全球首條量產玻璃中介層，AMD MI400 + AWS Trainium 已下 design-in。如 ramp 順利、Absolics 將成為**第一個有 P&L 證明玻璃中介層商業化可行**的案例 → 重估整鏈
2. **TSMC CoPoS pilot 完成**：2026-06 VisEra pilot 已完成，trial yield 90%（[Xintec 揭露](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)），下一個 anchor 是 2027 H1 first customer engagement——若是 NVDA Rubin Ultra confirm、整鏈 re-rate
3. **HBM4E first-to-mass-production race**：SK Hynix vs Samsung vs Micron，第一家 NVDA 大量採購的得「2028 anchor 優先供應商」溢價

### 中週期 alpha（2027 H2 → 2028）

4. **三戰場同時 ramp 的「complete stack」溢價**：當 HBM4E + 玻璃中介層 + 玻璃載板 都齊備、首批 NVDA Rubin Ultra（NVL576 600kW Kyber rack）出貨——市場才會把「先進封裝壟斷」price-in 到 OSAT 估值
5. **Samsung Electro-Mechanics 2027 H2 量產 ＝ 韓陣營全鏈閉環**：SK Hynix HBM4E + SEMCO 玻璃載板 + Sumitomo / Dongwoo 化學材料 = 韓系 panel-level glass stack 完成，可挑戰 TSMC + 日陣營（Corning + AGC）

### 長週期 alpha（2028+）

6. **Intel Rio Rancho 2030 量產 = 美國本土 fab + 玻璃載板雙引擎**：CHIPS Act 2.0 + Trump tariff 政策下，**美國境內玻璃封裝產線**有政府溢價。Amkor Arizona + Intel Rio Rancho + Absolics Georgia 形成「**美洲玻璃封裝鐵三角**」
7. **TGV 製程八站全鏈受惠**：[[TGV 製程鏈圖譜]] 八站每站都有玩家受惠、台廠**鈦昇 / 雷科 / 弘塑 / 辛耘 / 德律** 是純度最高的賣水人

## 風險（thesis 失效情境）

### 1. HBM4E 三家時程錯位 → 中介層需求遞延

- 若 Samsung HBM4 量產持續 NVDA 認證受阻（[[Samsung Electronics]] 已記載 HBM4 NVDA share 從 60-70% 退到 25-30%），HBM4E 訂單可能延一年
- TSMC CoPoS 2028 ramp 預設「2027 已有 HBM4E 客戶」，若遞延 → CoPoS 直接 ramp 不到位

### 2. Hybrid Bonding 跳過 TGV

- TSMC SoIC 與 Intel Foveros direct 3D 堆疊 → 不需要 TGV interposer
- 若 Hybrid Bonding 在 HBM4E 時代成熟（如 Samsung X-Cube 路線）、TGV TAM 縮 30-50%
- [[先進封裝互聯路線圖]] 已記三軌並存風險

### 3. 玻璃翹曲與 CTE 良率撞牆

- [[玻璃翹曲與 CTE mismatch]] 是已記載 risk
- 16-Hi HBM4E + panel-level glass = 物理層級複合應力，良率可能在 2027 trial 階段卡住
- 若 Absolics / SEMCO 良率長期停在 < 60%、整鏈 ramp 推遲

### 4. Intel Rio Rancho 2030 卡關

- Intel IDM 2.0 多次推遲（[[Intel]] entity 已記）
- 若 Rio Rancho 玻璃載板無法 2030 量產、美國境內玻璃封裝鐵三角少一角
- 但這 risk 對 Intel 之外的玩家影響小

### 5. NVDA 路線圖變更

- 若 NVDA Rubin Ultra 跳過 CoPoS 直接走 CoWoS-L（矽 interposer + 玻璃 fan-out）
- 整個 CoPoS thesis 推遲到 Feynman（2028+）
- 替代風險：Hybrid Bonding 取代 TGV

### 6. 反壟斷干預

- 韓國 / 美國對 NVDA-SK Hynix-Absolics 多年合約的審查
- 若強制 multi-sourcing → HBM4E 結構性短缺溢價被砍

## 觀察訊號（季度級 anchor）

| 季度 | 訊號 | 受惠玩家 |
|---|---|---|
| **2026 Q3** | Absolics Georgia 首批量產數量、Phase 2 expansion 12K → 72K m²/年 timeline | Absolics、SKC、AMAT |
| **2026 Q3** | SEMCO + Sumitomo + Dongwoo Glass Core JV 正式合約簽訂 | SEMCO、Sumitomo Chemical |
| **2026 Q4** | TSMC 法說會：CoPoS first customer engagement、qual sample 2027 H1 | TSMC、NVDA |
| **2027 Q1** | SK Hynix HBM4E first sample 出貨 NVDA | SK Hynix |
| **2027 Q2** | Samsung HBM4E NVDA 認證進度（追 HBM4 share） | Samsung |
| **2027 H2** | Samsung Electro-Mechanics Sejong 量產 + Apple Baltra ship | SEMCO、Apple |
| **2027 H2** | NVDA Rubin Ultra NVL576 600kW Kyber rack 首批出貨 | NVDA、TSMC CoPoS、HBM4E 三巨頭 |
| **2028 H1** | Micron Idaho fab #2 + Singapore HBM packaging 全產能 | Micron |
| **2028 H1** | TSMC CoPoS mass production ramp | TSMC、台 OSAT 鏈 |
| **2030** | Intel Rio Rancho 玻璃載板量產 + CPO 共商業化 | Intel、Amkor |

## 跟其他 wiki 概念連結

- [[HBM iPhone moment]]：HBM4E 是 iPhone moment 的「結構性升級版」、anchor 從 2026 多年合約推到 2027-2028 物理交會
- [[AI 記憶體結構性供給短缺]]：本 concept 補完 Tier 3「玻璃中介層」的時間軸與物理鎖死關係
- [[玻璃基板與 FOPLP 賽道]]：本 concept 是賽道的「2028 anchor 收束」具體 SKU 案例
- [[TGV 製程鏈圖譜]]：本 concept 在 2028 anchor 時點啟動八站全鏈
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]：鈦昇 vs 雷科 binary outcome 在 2027 樣品階段定生死
- [[TGV × CPO 依賴圖]]：CPO 需要 TGV、本 concept 是「HBM4E 也需要 TGV」的補充證明
- [[CoWoS 三傑差異化]]：弘塑 / 辛耘 / 萬潤 在 CoPoS 時代角色升級
- [[先進封裝互聯路線圖]]：CoPoS / Hybrid Bonding / RDL Fan-Out 多軌風險
- [[ABF 載板 vs 玻璃基板 displacement]]：欣興 / 南電 / 景碩 displacement 命運 → 2028 anchor 揭曉
- [[半導體基礎建設化]]：本 concept 是「先進封裝壟斷」的具體實現
- [[控制點轉移（投資版）]]：NVDA / TSMC / SK Hynix 多年合約 = 控制點往 stack 上下游延伸
- [[市場四階段：懷疑／驗證／共識／反轉]]：2026 H2 = 驗證、2028 = 共識
- [[Jevons Paradox（投資版）]]：HBM4E + CoPoS 帶來 token 經濟單位成本下降 → 推理需求暴增 → 二次 HBM 漲價
- [[CapEx 見頂辯論]]：2028 三戰場同時 ramp = CapEx 延長 anchor
- [[資訊擴散四階段]]：2026 H2 Absolics ramp = 第一階段「機構」訊號、2028 是「ETF / 散戶」階段

## 主要佐證來源

### HBM4E 時程
- [TrendForce 2025-11-13 — HBM4E 40% of 2027 market](https://www.trendforce.com/news/2025/11/13/news-hbm4e-seen-hitting-40-of-2027-market-samsung-sk-hynix-reportedly-aim-for-1h26-completion/)
- [Seoul Economic Daily 2026-04-23 — SK Hynix HBM4E sample H2 2026, mass production 2027](https://en.sedaily.com/finance/2026/04/23/sk-hynix-to-ship-hbm4e-samples-in-h2-begin-mass-production)
- [TrendForce 2026-01-23 — Samsung custom HBM4E mid-2026](https://www.trendforce.com/news/2026/01/23/news-samsungs-custom-hbm4e-design-reportedly-aimed-for-mid-2026-parallels-sk-hynix-and-micron/)
- [TrendForce 2024-12-23 — Micron HBM4E 2027-2028](https://www.trendforce.com/news/2024/12/23/news-micron-plans-hbm4-mass-production-in-2026-customized-hbm4e-to-launch-in-2027-2028/)
- [TrendForce 2026-05-27 — Micron Idaho + Singapore expansion](https://www.trendforce.com/news/2026/05/27/news-inside-microns-1-trillion-market-cap-leap-a-global-fab-expansion-overview-across-the-u-s-and-asia/)
- [TrendForce 2026-06-02 — Samsung HBM5 mockup at Computex, 2028 production](https://www.trendforce.com/news/2026/06/02/news-samsung-unveils-hbm5-model-for-the-first-time-at-computex-production-reportedly-seen-around-2028/)
- [Tom's Hardware — Samsung HBM5 Heat Path Block](https://www.tomshardware.com/tech-industry/semiconductors/samsung-shows-first-hbm5-mockup-at-computex-with-heat-path-block-cooling)

### TSMC CoPoS 時程
- [TrendForce 2026-04-13 — CoPoS pilot June 2026, 2028-29 ramp](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)
- [TrendForce 2026-05-19 — SCHMID flags TSMC PLP 310×310mm](https://www.trendforce.com/news/2026/05/19/news-equipment-maker-schmid-flags-tsmc-panel-level-packaging-push-310x310mm-progress-glass-integration-under-review/)
- [TechPowerUp — TSMC CoPoS 310×310 mm details](https://www.techpowerup.com/337960/tsmc-prepares-copos-next-gen-310-x-310-mm-packages)
- [TechPowerUp — TSMC 750×620 mm panel](https://www.techpowerup.com/339963/tsmc-prepares-cowos-to-copos-shift-with-750-x-620-mm-panels)
- [BigGo Finance — C.C. Wei 2-3 years to mass production](https://finance.biggo.com/news/kLg0kp4BrX5PFN7BKrXD)

### Intel 玻璃載板
- [TrendForce 2026-05-26 — Intel Rio Rancho glass substrate, silicon photonics](https://www.trendforce.com/news/2026/05/26/news-intel-reportedly-eyes-worlds-first-glass-substrate-output-at-rio-rancho-offers-silicon-photonics-to-customers/)
- [WCCFTech — Intel Rio Rancho crown jewel](https://wccftech.com/intel-foundry-rio-rancho-facility-crown-jewel-in-production-of-glass-substrates/)
- [TrendForce 2026-01-26 — Intel thick-core glass substrate with EMIB](https://www.trendforce.com/news/2026/01/26/news-intel-reportedly-presents-first-thick-core-glass-substrate-with-emib-targeting-ai-data-centers/)
- [Digitimes 2026-04-14 — Glass substrate Intel + SEMCO progress](https://www.digitimes.com/news/a20260414VL204/chips-glass-substrate-demand-intel-production-semco.html)

### Absolics
- [Elec — Absolics AMD approval glass](https://www.thelec.net/news/articleView.html?idxno=5476)
- [FinancialContent — Intel & Absolics breakthrough for AI super-chips](https://markets.financialcontent.com/wral/article/tokenring-2026-1-27-the-glass-substrate-age-intel-and-absolics-lead-the-breakthrough-for-ai-super-chips)

### Glass × HBM 物理鎖死
- [TrendForce Insights — Glass substrates breakthrough](https://insights.trendforce.com/p/glass-substrate-development)
- [TrendForce 2026-06-05 — Glass substrates 2027 launch, 2030 scale](https://www.trendforce.com/news/2026/06/05/news-glass-substrates-eye-2027-launch-scale-toward-2030-as-cowos-costs-rise-and-hyperscaler-demand-grows/)
- [Tom's Hardware — TSMC CoWoS Super Carrier 9-reticle 12 HBM4 stacks](https://www.tomshardware.com/tech-industry/tsmc-super-carrier-cowos-interposer-gets-bigger-enabling-massive-ai-chips-to-reach-9-reticle-sizes-with-12-hbm4-stacks)

## 相關連結

- [[HBM iPhone moment]]
- [[AI 記憶體結構性供給短缺]]
- [[玻璃基板與 FOPLP 賽道]]
- [[TGV 製程鏈圖譜]]
- [[TGV × CPO 依賴圖]]
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]
- [[先進封裝互聯路線圖]]
- [[ABF 載板 vs 玻璃基板 displacement]]
- [[CoWoS 三傑差異化]]
- [[玻璃翹曲與 CTE mismatch]]
- [[半導體基礎建設化]]
- [[控制點轉移（投資版）]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[Jevons Paradox（投資版）]]
- [[賣水人選股邏輯（投資版）]]
- [[SK Hynix]]、[[Samsung Electronics]]、[[Micron]]
- [[TSMC]]、[[Intel]]、[[Absolics]]、[[Samsung Electro-Mechanics]]
- [[日月光 ASE]]、[[Amkor]]、[[Powertech 力成]]
- [[Corning]]、[[AGC]]、[[SCHOTT]]、[[Sumitomo Chemical]]
- [[鈦昇]]、[[雷科]]、[[弘塑]]、[[辛耘]]、[[德律]]、[[萬潤]]、[[東捷]]、[[敘豐]]
- [[NVDA]]、[[AMD]]、[[AVGO]]

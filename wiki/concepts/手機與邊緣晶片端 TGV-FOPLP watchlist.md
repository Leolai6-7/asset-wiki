---
title: 手機與邊緣晶片端 TGV/FOPLP watchlist
aliases: [手機晶片 TGV, 邊緣 SoC 封裝, 手機端 watchlist, edge SoC 封裝路線]
type: concept
created: 2026-06-05
updated: 2026-06-05
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [TGV, FOPLP, Apple, Qualcomm, Samsung, ByteDance, MediaTek, Tesla, xAI, watchlist, 手機晶片, 邊緣 AI]
confidence: medium
---

# 手機與邊緣晶片端 TGV / FOPLP watchlist

[[TGV 製程鏈圖譜]] 的主要終端 thesis 押在 data center（[[Intel]] EMIB / [[AMD]] MI / [[AVGO]] ASIC），但**手機 / 邊緣端**是另一條獨立的採用曲線——更早採用 FOPLP/FOWLP、更晚採用 TGV，但量級更大、時間軸不同。

本 concept = **第二與第三條採用曲線的盲點補強**（codex P2 反饋），不建獨立 entity，重點是「對 TGV 賽道的意義」與「對台廠 thesis 的校準」。

## 為什麼這個 watchlist 重要

- sennn.nnna 原文：「在 FOPLP 的應用落地後，**中低階晶片與 PMIC 可能都會用上**」
- FOPLP/FOWLP 在手機端**已經 commercial**（Apple InFO 多年；Samsung 2026 Exynos 2600 業界首發 HPB-in-FOWLP）
- TGV 對手機 SoC 是**選項而非必經**——Hybrid Bonding、Cu Pillar、有機載板 + InFO 都可以替代
- **量級大、design-in 慢、但有 anchor 效應**：Apple Baltra（AI server 自研晶片）2026 已直接向 Samsung Electro-Mechanics 採玻璃基板樣品 → 從 server 端切入手機 SoC
- 與 data center thesis 構成**三條獨立曲線**（見下表）

## 各玩家分析（WebSearch 2026-06）

### Apple（A/M 系列 + Baltra AI server）

**現狀**：
- **手機 SoC（A 系列）/ Mac SoC（M 系列）**：長期使用 TSMC **InFO**（Integrated Fan-Out）+ Cu Pillar，FOWLP 路線已成熟商用多年
- **Baltra（自研 AI server 晶片）**：2026-04 證實 Apple 直接向 **Samsung Electro-Mechanics** 採玻璃基板樣品（不再透過 Broadcom 中介），TSMC 3nm N3E + chiplet 架構
- Samsung Electro-Mechanics 2025-11 與日本 Sumitomo Chemical 簽 MOU，2026 H2 成立玻璃核心 JV → 量產 anchor
- TSMC **WMCM**（Wafer-level Multi-Chip Module，InFO 升級版）為 Apple 擴產，AP3 Longtan + AP7 Chiayi 雙線，2026 底達 60K wpm、2027 翻倍 120K+ wpm

**路線預測**：
- Baltra = **手機端 → server 端 → 反向滲透 SoC** 的入口
- 短期：Apple Baltra 透過 FC-BGA + glass core（不是完整 TGV interposer）→ TGV 純度 low
- 中期（2027-2028）：M 系列若採 chiplet + glass interposer → TGV 進場

**對台廠影響**：
- WMCM 擴產 → TSMC AP3/AP7 設備鏈受惠（[[弘塑]] / [[辛耘]] / [[萬潤]] 中性）
- glass core 路線給 Samsung Electro-Mechanics → 韓系卡位，對台廠**中性偏負**（除非 [[鈦昇]] LIDE 路線打進 TSMC CoPoS）
- ⭐ **Baltra 是 server 不是 phone**，列入 watchlist 是因為 Apple 開了「自家 SoC 用玻璃」的先例

### Qualcomm（Snapdragon 8 Elite Gen 5 + AI ASIC 擴張）

**現狀**：
- **Snapdragon 8 Elite Gen 5（2026 Q1 量產）**：TSMC N3P + **iPoP**（integrated Package on Package，有機載板基礎）
- **FOPLP 未進主流 Snapdragon**——保守採用，仍以 FC-BGA + iPoP 為主
- **AI ASIC 擴張**：傳 ByteDance 將購買「數百萬顆」Qualcomm ASIC → Qualcomm 自研 ASIC 路線啟動

**路線預測**：
- 手機 SoC：FOPLP 採用慢於 Apple，**2027-2028 才可能換軌**
- ASIC：若 Qualcomm 在 data center ASIC 重押 → 走 TSMC CoWoS-S 為主、CoPoS 為輔（與 [[AVGO]] 同打法）

**對台廠影響**：
- 短期：手機端維持 FC-BGA → 對 TGV 賽道**中性**
- 中期：若 Qualcomm ASIC 上量 → 跟 [[AVGO]] thesis 同邏輯，CoWoS 三傑（[[弘塑]] / [[辛耘]] / [[萬潤]]）受惠

### Samsung（Exynos 2600 + Samsung Foundry + Samsung Electro-Mechanics）

**現狀**：
- **Exynos 2600**（2026-02 Galaxy S26 首發）：業界首顆 2nm GAA AP，採 Samsung Foundry 自製
- 封裝：**業界首發 HPB-in-FOWLP**（Heat Path Block + Fan-Out Wafer-Level Packaging）——銅製 HPB 直接置於 die 上方
- **未採 FOPLP / glass interposer**——FOWLP 為主
- **Samsung Electro-Mechanics**：玻璃基板供應商，已供樣 Apple + Broadcom（2026），是韓系 glass core 的核心節點

**路線預測**：
- 手機 SoC：FOWLP 為主，**TGV 暫不進手機**
- Foundry + 玻璃基板雙線整合：Samsung 是少數**晶圓 + 面板 + 封裝**垂直整合玩家，自家 Exynos + 對外供 glass core
- 2027-2028：Samsung Foundry 若 2nm/1.4nm 拿單 Qualcomm / NVIDIA → glass interposer 進場機率提升

**對台廠影響**：
- Samsung Electro-Mechanics 拿 Apple Baltra + Broadcom 訂單 → **韓系玻璃基板搶在台廠之前**
- 對 [[鈦昇]] LIDE 路線的壓力：若 LIDE 專利非獨家、Samsung 用自家蝕刻 + 雷射方案 → 鈦昇 design-in window 縮窄
- 對 [[雷科]] 影響中性（Samsung 切割仍可能用 Disco）

### ByteDance（自研 AI ASIC + Doubao 模型）

**現狀**：
- 2024 報導：ByteDance 委託 TSMC 代工 2 顆自研 AI 晶片（1 顆訓練、1 顆推論），**TSMC 5nm**，2026 量產
- 與 Broadcom 合作設計（類似 Google TPU 模式）
- 2026：傳購買「數百萬顆」Qualcomm ASIC → **混合策略**（自研 + 外購）
- ⚠️ **未公開封裝路線**：5nm 級 ASIC 在 2026 大概率走 CoWoS-S 或 CoWoS-L（矽中介層），TGV 直接 design-in 機率低

**是否有 TGV / 玻璃基板路線**：
- **目前無公開證據** ByteDance 自研 ASIC 採玻璃基板
- 但 ByteDance 量級夠大（數百萬顆）→ 若 CoWoS 容量擠不下，**有可能被 TSMC 推去 CoPoS（玻璃 panel）試線**
- **黑馬 option**：2027-2028 第二代 ASIC 可能直跳 CoPoS

**對台廠影響**：
- 短期：透過 CoWoS 受惠 → [[弘塑]] / [[辛耘]] / [[萬潤]] 三傑中性
- 中期：若 ByteDance 推 CoPoS → [[鈦昇]] / [[雷科]] 受惠（需確認 TSMC CoPoS 設備供應商名單）
- **binary upside**：ByteDance + Qualcomm + Apple 三方若同時在 2027 推 glass interposer → TGV 賽道從 thesis 變確認

### 其他玩家

**MediaTek（聯發科）**：
- 2026 旗艦 Dimensity 9500s / 8500 採 TSMC 3nm，**封裝以 FC-BGA + FOWLP 為主**，FOPLP/TGV 未進主流
- 路線：跟隨 Qualcomm，採用較晚

**Tesla Dojo（D1 / D2）**：
- D1 採 **TSMC InFO_SoW**（System-on-Wafer）——25 顆 D1 die 拼一片 wafer
- Musk 帝國轉向 Intel Terafab（德州）做 SpaceX / xAI / Tesla 客製封裝 → **逃離 TSMC 路線**
- TGV 採用：D2 路線未明，**Intel Terafab anchor 可能直推 EMIB + glass core**（跟 Intel Clearwater Forest 同邏輯）

**xAI**：
- Musk Terafab 客戶之一，**Intel 代工 + Intel EMIB + glass core** 路線高機率
- 跟 ByteDance 並列**新興 ASIC buyer 黑馬**

**小米玄戒 / 國產 SoC**：
- 仍在 7nm/5nm 攻堅，封裝以中低階 FC-BGA 為主
- 對 TGV 賽道**短期無關**，可能 2028+ 才接觸

## ⭐ 三條獨立採用曲線（核心結論）

| 玩家層 | FOPLP/FOWLP 採用 | TGV 採用 | 對台廠意義 |
|---|---|---|---|
| **Data center**（Intel / AMD / Broadcom） | 2026-2027 | **2026-2028（主菜）** | 主菜（高 ASP、強 thesis）— 押 [[鈦昇]] / [[雷科]] / 三傑 |
| **手機高端 + 自研 server**（Apple / Qualcomm / Samsung） | **已商用**（InFO/FOWLP 多年） | **2027+ 觀察**（Apple Baltra 開先例） | 早期受惠 FOPLP，TGV 看 cost down + Samsung Electro-Mechanics 競爭 |
| **邊緣 AI / 新興 ASIC**（ByteDance / Tesla / xAI / Qualcomm ASIC） | **2026-2028 自定義** | **可能直跳 TGV / CoPoS**（Musk Terafab + TSMC CoPoS 雙路線） | 黑馬 + binary outcome — 押對 supplier 翻倍 |

## Apple Baltra 是 anchor 中的 anchor

Apple 直接向 Samsung Electro-Mechanics 採玻璃基板樣品（2026-04 確認）= **「手機晶片設計者」首次跨入「自研 server + 玻璃基板」**

意義：
1. **Apple 開了 FOPLP-on-glass 的設計者先例**——其他 fabless（Qualcomm / MediaTek）有跟進壓力
2. **Samsung Electro-Mechanics 拿到 Apple + Broadcom**——韓系玻璃供應鏈卡位完成
3. **TSMC 必須加速 CoPoS**（pilot line 2026-06 完成 → 2028-29 量產）回應 Samsung 威脅
4. **台廠機會在 TSMC CoPoS 那一側**——若 [[鈦昇]] LIDE 進 TSMC CoPoS 設備清單 → thesis 確認

## 對 wiki 既有 thesis 的校準

- **不要把 TGV 賽道只押 data center**——手機 + 邊緣端是另兩條獨立曲線
- **FOPLP ≠ TGV 必須綁定**（再次校準 [[先進封裝互聯路線圖]] 的 mismatch #1）
- **Apple 是 FOPLP/FOWLP 已成熟 anchor**（InFO 多年），但**手機 SoC 短期不進 TGV**
- **Apple Baltra（AI server）才是 TGV 鏈第二根 anchor**——跟 Intel Clearwater Forest 並列
- **ByteDance 自研 ASIC** 是新興 buyer，封裝路線未公開 → high upside option
- **Samsung Electro-Mechanics 是韓系反擊**——對 [[LPKF]] LIDE 專利 + [[鈦昇]] 台廠路線是直接威脅
- **Musk Terafab（Intel 代工）= 邊緣 ASIC 黑馬路線**——跟 TSMC 路線正面對撞

## 投資啟示（與既有 thesis 整合）

| Tier | 押的事情 | 標的 | 信心 |
|---|---|---|---|
| **Tier 1**（既有 thesis 不動） | data center TGV 主菜 | [[鈦昇]] / [[雷科]] / [[弘塑]] / [[辛耘]] / [[萬潤]] | high |
| **Tier 2**（FOPLP 滲透手機高端 OSAT） | Apple/Qualcomm FOPLP 滲透加深 → OSAT 接單 | [[Powertech 力成]]（6239）、[[日月光 ASE]]（3711） | medium |
| **Tier 3**（邊緣 ASIC 黑馬路線） | ByteDance / xAI / Tesla 自研 ASIC 早期 supplier | ABF 載板廠（欣興/南電/景碩，見 [[ABF 載板 vs 玻璃基板 displacement]]）、Intel Terafab 設備供應鏈 | low（binary outcome） |
| **Tier 4**（對沖韓系玻璃反擊） | Samsung Electro-Mechanics 拿 Apple 訂單 → 韓系玻璃 vs 台廠 LIDE | 看 [[鈦昇]] 是否進 TSMC CoPoS 設備清單 | medium |

## 三條曲線中哪條最值得追蹤

**答案：Tier 1（data center 主菜）+ Tier 3（邊緣 ASIC 黑馬）—— 不押 Tier 2 手機 SoC TGV。**

理由：
1. **Tier 1 已有 anchor**（Intel Clearwater Forest 2026 H2、AMD MI 跟進、Broadcom ASIC 3.5D 量產）
2. **Tier 3 是 binary upside**——ByteDance + Musk Terafab 任一爆發都翻倍
3. **Tier 2 手機 SoC TGV 採用太慢**（2027-2028+ 才可能）且 Samsung Electro-Mechanics 卡位 → 對台廠**負面風險大於機會**
4. **Tier 4 是觀察**——看 [[鈦昇]] 是否拿到 TSMC CoPoS 入場券，每一次法說會都追

## ByteDance 路線驗證度

| 項目 | 公開資訊 | 信心 |
|---|---|---|
| ByteDance 自研 ASIC（2 顆） | 2024 確認，TSMC 5nm，2026 量產 | high |
| 與 Broadcom 設計合作 | 2024-2025 報導 | high |
| 2026 加碼購 Qualcomm ASIC | 2026 報導 | medium |
| **採用 TGV / 玻璃基板** | ❌ **無公開證據** | low |
| **採用 CoPoS pilot** | ❌ 無公開，但 TSMC CoPoS pilot line 2026-06 完成，ByteDance 量級夠大可能被推 | speculation |

→ **ByteDance 路線目前無法驗證**，需追蹤 TSMC CoPoS 設備供應商名單 + ByteDance 第二代 ASIC 規格

## 對台廠（鈦昇 / 雷科）的 thesis 補充

### 對 [[鈦昇]] 的補充
- **新風險**：Samsung Electro-Mechanics 拿 Apple Baltra → 韓系玻璃基板量產卡在 LIDE 之外
- **新機會**：TSMC CoPoS pilot line 2026-06 完成 → 鈦昇若拿到 TSMC 設備認證 = thesis 確認的最強訊號
- **追蹤訊號**：鈦昇法說會是否提 TSMC CoPoS / WMCM 認證進度

### 對 [[雷科]] 的補充
- **新機會**：Tesla / xAI Intel Terafab 路線若採玻璃 → 切割設備需求新增（雷科多刀流可進）
- **追蹤訊號**：雷科是否拿到 Intel Terafab 雷射切割 / 改質 design-in

### 新增追蹤標的
- **[[Powertech 力成]]**（6239）：FOPLP 主力，承接 Apple/Qualcomm 手機 SoC 滲透
- **[[日月光 ASE]]**（3711）：OSAT 龍頭，TSMC CoWoS 外包受惠（2026 起 TSMC 已外包部分封裝給 ASE/Amkor）
- **[[Samsung Electro-Mechanics]]**（009150.KS）：韓系玻璃基板核心，與 [[LPKF]] / [[鈦昇]] 直接競爭

## 跟其他 wiki 概念連結

- [[先進封裝互聯路線圖]]：本 watchlist 是該路線圖**手機 + 邊緣軌**的具體案例補強
- [[TGV 製程鏈圖譜]]：本 watchlist 是 TGV 終端 thesis 的**第二、第三條曲線補完**
- [[玻璃基板與 FOPLP 賽道]]：本 watchlist 是該賽道**終端客戶分析**的下位深化
- [[ABF 載板 vs 玻璃基板 displacement]]：手機端 ABF 載板廠（欣興 / 南電 / 景碩）是 Tier 3 投資載體
- [[CoWoS 三傑差異化]]：ByteDance / Qualcomm ASIC 走 CoWoS → 三傑（弘塑 / 辛耘 / 萬潤）中性受惠
- [[控制點轉移（投資版）]]：Apple 直接採 Samsung Electro-Mechanics 玻璃 = **晶片設計者奪材料控制權**
- [[賣水人選股邏輯（投資版）]]：手機端 FOPLP 是中性受惠（不押誰贏，押 FOPLP 滲透率）
- [[預期差]]：ByteDance / Musk Terafab 路線是市場尚未充分定價的 binary upside

## Sources（WebSearch 2026-06-05）

- [Apple Tests Glass Substrates for Its Next In-House AI Server Chip 'Baltra' — MacObserver](https://www.macobserver.com/news/apple-tests-glass-substrates-for-its-next-in-house-ai-server-chip-baltra/)
- [Apple's In-House AI Chip Strategy Advances: Direct Testing of Glass Substrates — BigGo Finance](https://finance.biggo.com/news/mKoybJ0Bq7sy_YQMy1gG)
- [Apple Reportedly Sources Glass Substrate Samples Directly — TrendForce 2026-04-08](https://www.trendforce.com/news/2026/04/08/news-apple-reportedly-sources-glass-substrate-samples-directly-signaling-further-in-house-ai-server-chip-push/)
- [Apple's self-designed AI server chip "Baltra" may be manufactured by TSMC — TechNode 2026-04-09](https://technode.com/2026/04/09/apples-self-designed-ai-server-chip-baltra-may-be-manufactured-by-tsmc-using-3nm-n3e-process/)
- [Qualcomm Snapdragon 8 Elite Gen 5 Advanced Packaging Quick Look — TechInsights](https://www.techinsights.com/blog/qualcomm-snapdragon-8-elite-gen-5-advanced-packaging-quick-look)
- [Samsung Unveils Exynos 2600: Industry-First 2nm GAA AP — TrendForce 2025-12-19](https://www.trendforce.com/news/2025/12/19/news-samsung-officially-unveils-exynos-2600-industry-first-2nm-gaa-ap-with-113-ai-performance-uplift)
- [Samsung offers coolest Exynos feature to Apple, Qualcomm — Sammy Fans](https://www.sammyfans.com/2025/12/11/samsung-exynos-hpb-invention-apple-qualcomm/)
- [Display to semiconductor: Panel makers weaponize large glass substrates for FOPLP — DigiTimes 2026-05-25](https://www.digitimes.com/reports/item.php?id=20260525RS400)
- [TikTok parent company ByteDance to have 2 custom AI chips made on TSMC 5nm process in 2026 — TweakTown](https://www.tweaktown.com/news/100585/tiktok-parent-company-bytedance-to-have-2-custom-ai-chips-made-on-tsmc-5nm-process-in-2026/index.html)
- [ByteDance Reportedly Turns to TSMC on in-house AI Chips — TrendForce 2024-09-18](https://www.trendforce.com/news/2024/09/18/news-bytedance-reportedly-turns-to-tsmc-on-self-developed-ai-chips-to-reduce-purchase-cost-on-nvidia/)
- [MediaTek and Qualcomm Race for Bigger AI Roles Through NVIDIA N1X, ASICs, and Dragonfly — TrendForce 2026-06-02](https://www.trendforce.com/news/2026/06/02/news-mediatek-and-qualcomm-race-for-bigger-ai-roles-through-nvidia-n1x-asics-and-dragonfly/)
- [Tesla Dojo - Unique Packaging and Chip Design — SemiAnalysis](https://newsletter.semianalysis.com/p/tesla-dojo-unique-packaging-and-chip)
- [Tesla's wafer-sized Dojo processor is in production — Tom's Hardware](https://www.tomshardware.com/tech-industry/teslas-dojo-system-on-wafer-is-in-production-a-serious-processor-for-serious-ai-workloads)
- [The custom AI ASIC state of play (May 2026) — Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia)
- [TSMC Advances Panel-Level Packaging, CoPoS Pilot Line Set for June Completion — TrendForce 2026-04-13](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/)
- [TSMC Speeds Advanced Packaging: AP7 Targets 2026 Output — TrendForce 2025-12-04](https://www.trendforce.com/news/2025/12/04/news-tsmc-speeds-advanced-packaging-ap7-targets-2026-output-arizona-p6-eyed-for-u-s-packaging-hub/)
- [TSMC Reportedly Expands WMCM Packaging for Apple — TrendForce 2026-01-20](https://www.trendforce.com/news/2026/01/20/news-tsmc-reportedly-expands-wmcm-packaging-for-apple-capacity-may-more-than-double-by-2027/)

## 相關連結

- [[TGV 製程鏈圖譜]]
- [[玻璃基板與 FOPLP 賽道]]
- [[先進封裝互聯路線圖]]
- [[ABF 載板 vs 玻璃基板 displacement]]
- [[CoWoS 三傑差異化]]
- [[控制點轉移（投資版）]]
- [[賣水人選股邏輯（投資版）]]
- [[預期差]]
- [[Intel]]、[[AMD]]、[[AVGO]]、[[TSMC]]、[[NVDA]]
- [[鈦昇]]、[[雷科]]、[[弘塑]]、[[辛耘]]、[[萬潤]]、[[LPKF]]、[[Disco Corp]]
- [[sennn.nnna]]

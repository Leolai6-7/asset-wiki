---
title: 檢測賣水人 pattern（良率地獄賣檢測）
aliases: [檢測賣水人, 良率地獄賣檢測, 測試賣水人 pattern, yield-hell 檢測 pattern]
type: concept
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-12-10
sources:
  - https://www.lasertec.co.jp/en/products/semiconductor/actis_a150.html
  - https://www.lasertec.co.jp/en/news/2025/20251031_3912.html
  - https://www.jaredwatkins.com/research/semiconductors/fabrication-equipment/lasertec/
  - https://www.gminsights.com/industry-analysis/euv-mask-inspection-market
  - https://www.oreateai.com/blog/lasertec-the-global-monopoly-in-euv-photomask-inspection/981a881b59881e5650513914c59b6694
  - https://www.aehr.com/2026/04/aehr-receives-record-41-million-production-order-from-lead-hyperscale-ai-customer-second-half-bookings-exceed-92-million/
  - https://www.aehr.com/2026/04/aehr-test-systems-reports-over-37-million-in-quarterly-bookings-driven-by-strong-ai-and-data-center-infrastructure-demand/
tags: [pattern, 檢測, 測試設備, 良率, 賣水人, AXI, burn-in, actinic, Lasertec, watchlist]
confidence: medium
---

# 檢測賣水人 pattern（良率地獄賣檢測）

## 1. 一句話

**新賽道一進入「良率地獄」（爬良率期 × 不可返修點）、檢測／測試設備商就先於賽道本身收錢、且賽道成敗都收錢**——此 pattern 已在 wiki 獨立出現兩次（TGV→AXI、CPO→known-good-engine 篩選）、本檔概念化、並以第三案例（[[AEHR]] burn-in）與第四案例（Lasertec actinic、~100% 壟斷）驗證跨賽道通用性。

## 2. 四案例對照（跨賽道驗證）

| # | 賽道 | 良率地獄在哪 | 不可返修點 | 篩選閘門 | 賣水人 | 站別深度 |
|---|---|---|---|---|---|---|
| 1 | TGV 玻璃基板 | 孔內斷路、2D 檢測看不到孔內 | 金屬化／疊層後 | AXI（3D X-Ray CT）唯一能逐層看孔內斷路 | [[德律]]（＋OmniMeasure）、YXLON、Nikon | 4（早期高門檻） |
| 2 | CPO | 貼裝良率上限 ~95%、Spectrum-6 = 32 顆 COUPE 連乘 → 系統良率 **0.95³² ≈ 19%** | 光引擎焊接後不可返修 | 組裝前篩 known-good-engine | [[Teradyne]]（Photon 100）、[[鴻勁 7769]]、[[致茂 2360]] | 3-4（多供應商） |
| 3 | SiC／AI ASIC／矽光子 | 長時間可靠性失效（MTTF）、模組組裝完才發現 = 損失放大 | 封裝／模組組裝後 | wafer 階段先 burn-in（WLBI） | [[AEHR]]（FOX-XP＋WaferPak 耗材）、Advantest、Cohu | 4-5（三家寡占） |
| 4 | EUV 微影 | mask 一顆缺陷複製到每片 wafer | mask 上機曝光後（缺陷量產化） | actinic（13.5nm 同波長）mask 檢測 | **Lasertec（6920.JP）~100% 壟斷** ⭐ | **5（單一壟斷、最強形態）** |

→ 四案例橫跨基板／光通訊／功率＋算力／微影四條互不重疊的賽道 = **pattern 跨賽道成立**。

## 3. 機制（為什麼一再出現）

| # | 機制 | 內容 | 案例證據 |
|---|---|---|---|
| ① | **良率越爛、測試強度越高** | 測試營收與良率負相關；多顆組裝 = 良率連乘 y^n、n 越大篩選越不可省 | CPO 系統良率 19% → 每顆 engine 組裝前全篩；TGV 沒過 AXI = 不知道斷路 = 良率天花板 |
| ② | **賽道延期、測試先收錢** | 量產前的爬良率期就要買檢測設備 → 檢測商營收領先賽道營收 1-2 年 | [[AEHR]] H2 bookings $92M+ vs 全年營收 guidance $45-50M（Book-to-Bill 3.5x+）；CPO 延期（[[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]）但測試設備先行下單 |
| ③ | **賽道成敗都收錢** | 成 = 量產測試量更大；敗 = 下一代技術再爬一輪良率、設備再買一輪 | AEHR：SiC EV 退潮（ON Semi 砍單、營收 YoY -44%）→ AI ASIC＋矽光子接棒、bookings 反創新高 |

## 4. 最強形態：檢測站本身變 chokepoint（Lasertec、watchlist 待建檔）

- **Lasertec（6920.JP）**：actinic EUV patterned mask 檢測 **~100% 市佔**（≤5nm 節點）、ACTIS A150（2019 全球首發）= 唯一商用 actinic 機、單價 **>$75M**
- 物理門檻：actinic = 用與曝光相同的 13.5nm 波長檢測 → 需自製 EUV 光源；KLA 的 DUV-based mask inspection 無法替代 actinic 段
- 2025-2026 狀態：High-NA 過渡推 ACTIS A300（URASHIMA 高亮度光源）＋ A200HiT（2025-10 發布）、先進 foundry／mask shop 需求強；FY2025（至 2025-06）營收 ¥251.5B（損益細節兩來源衝突、待建檔時驗證）
- 意義：檢測站從「服務良率的配角」升格為**賽道本身的 chokepoint**——mask 沒過 actinic 檢測 = 不能上機 = EUV 量產停擺
- **watchlist**：預估五軸 22-24/25 區間（村田／Disco 級候選、待逐軸驗證）；監控 High-NA A300 出貨節奏、KLA actinic 替代進展

## 5. 邊界與天花板

| 限制 | 內容 |
|---|---|
| 站別軸通常只有 3-4 | 檢測站多數**非** chokepoint：可被 ATE 平台整合（Advantest／Teradyne）或多供應商化（AOI 紅海：德律／致茂／牧德） |
| 壟斷是例外不是常態 | 只有 Lasertec 級「物理門檻擋住所有人」才到站別 5；深度排序：AOI 2-3 ＜ AXI 4 ＜ burn-in 4-5 ＜ actinic 5 |
| 下行週期先被砍 | 檢測設備 = high CAPEX、賽道共識破滅時訂單先被 push out（機制②的反面） |
| 客戶集中／內製化 | 利基檢測商常綁 2-3 家 lead customer（AEHR 客戶分散軸僅 2）；hyperscaler 理論可內製 burn-in（短期難度極高） |

→ 檢測賣水人是 [[賣水人選股邏輯（投資版）]]「賣水人之中的賣水人」**候選**、但站別深度必須逐案驗證、不能 pattern 成立就直接給高分。

## 6. Pattern 識別 checklist（新賽道出現時）

1. **找良率瓶頸站**：哪一站良率最爛、有沒有多顆組裝的連乘效應（y^n、n 越大越痛）
2. **找不可返修點**：焊接／鍵合／封裝／上機後不可拆 = 篩選被迫前移
3. **找該點前最後一道篩選**：known-good-X 閘門（die／engine／wafer／mask）
4. **查設備商**：誰賣那台機器——市佔、競爭家數、耗材年金（WaferPak／probe card）、IP 門檻
5. **評站別深度定操作**：多供應商化 = 只做 re-rate 段 trade（[[Re-rate 捕捉法]]）；Lasertec 級壟斷 = 可長持

## 相關連結

- [[賣水人選股邏輯（投資版）]]
- [[Bottleneck Theory（瓶頸論）]]
- [[CPO 供應鏈圖譜]]
- [[TGV 檢測分類 taxonomy]]
- [[德律]]、[[AEHR]]、[[Teradyne]]、[[鴻勁 7769]]、[[致茂 2360]]
- [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]

## Sources

- [Lasertec ACTIS A150 product page](https://www.lasertec.co.jp/en/products/semiconductor/actis_a150.html)
- [Lasertec ACTIS A200HiT release, 2025-10-31](https://www.lasertec.co.jp/en/news/2025/20251031_3912.html)
- [Lasertec deep dive (Jared Watkins)](https://www.jaredwatkins.com/research/semiconductors/fabrication-equipment/lasertec/)
- [EUV Mask Inspection Market (GMInsights)](https://www.gminsights.com/industry-analysis/euv-mask-inspection-market)
- [Lasertec: Global Monopoly in EUV Photomask Inspection (Oreate)](https://www.oreateai.com/blog/lasertec-the-global-monopoly-in-euv-photomask-inspection/981a881b59881e5650513914c59b6694)
- [AEHR record $41M production order PR, 2026-04](https://www.aehr.com/2026/04/aehr-receives-record-41-million-production-order-from-lead-hyperscale-ai-customer-second-half-bookings-exceed-92-million/)
- [AEHR $37M quarterly bookings PR, 2026-04](https://www.aehr.com/2026/04/aehr-test-systems-reports-over-37-million-in-quarterly-bookings-driven-by-strong-ai-and-data-center-infrastructure-demand/)

---
title: Advantest
aliases: [6857, 6857.JP, 6857.T, ATEYY, アドバンテスト, V93000]
type: entity
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-12-10
sources:
  - https://www.advantest.com/en/news/2026/a81o6o0000000hgw-att/E_FR_FY2025_FN.pdf
  - https://www.gyokaidigest.com/companies/advantest/report/2026-FY
  - https://stockexpress.jp/advantest20260427/
  - https://stockexpress.jp/advantest20260128/
  - https://www.formfactor.com/press-release/formfactor-and-advantest-partner-on-silicon-photonics-wafer-level-test-cell-to-enable-high-volume-manufacturing/
  - https://investors.teradyne.com/news-events/press-releases/detail/419/teradyne-unveils-magnum-7h---the-next-generation-memory-tester-for-high-bandwidth-memory-devices
  - https://uk.finance.yahoo.com/news/ai-growth-brings-tests-semi-140502874.html
  - https://valueinvesting.io/6857.T/metric/forward-pe
tags: [標的, 日股, 半導體測試, ATE, HBM, AI SoC, CPO 測試, 檢測賣水人, 對照組]
confidence: medium
---

# Advantest（6857.JP）

## 1. 一句話定位

**全球 ATE 雙寡頭老大（vs [[Teradyne]]、兩家合計 >85% 高階測試市場）+ AI SoC／HBM 測試雙主導者**——FY2025（至 2026-03）營收 **¥1兆1,286億（+44.7%）**、營業利益 **¥4,991 億（+118.8%、OPM ~44%）**雙創歷史新高；V93000 是 NVDA 鏈 AI SoC 主測平台、HBM 測試市佔 **>60%**（GPU 相關利基近 70%）；但 12M 股價 **約 +270%（~3.7 倍）**、Forward PE **~40-50x 級距** = A 軸質量極高、**C 軸（估值已 price in）紅燈**。

## 2. 三層 thesis

| 層 | 內容 |
|---|---|
| 產業層 | 晶片 complexity↑（AI SoC die size／HBM 層數／CoWoS 堆疊）→ 測試時間與測試強度結構性上升 = 測試 TAM 跑贏半導體大盤；「良率越爛測越多」與 [[Bottleneck Theory（瓶頸論）]] 同構 |
| 目的層 | GPU／ASIC 誰贏、HBM 三家誰贏、CPO 或 pluggable 誰主流——都要測。路線中立的檢測賣水人（[[賣水人選股邏輯（投資版）]]）；市場已給出「ASML of test」稱號（⚠️ 這本身是共識期語言） |
| 供應層 | SoC：V93000 EXA Scale（NVDA／AMD／ASIC、經 TSMC-OSAT 後段）；memory：T55xx／T58xx 系列、DRAM 佔 memory tester 銷售比 ~90%（HBM 驅動）；CPO：**2024-11 與 [[FormFactor]] 合作 SiPh wafer-level test cell**（Velox probe station + V93000）——比 Teradyne Photon 100（2026-03）早 16 個月卡位，「潛在進入者」其實已在場 |

## 3. 財務快照（As of 2026-06-10）

| 指標 | 數值 | 備註 |
|---|---|---|
| FY2025 營收（2025-04〜2026-03）| ¥1兆1,286億（+44.7%）| 歷史新高、年內三度上修 |
| FY2025 營業利益 | ¥4,991 億（+118.8%）、OPM ~44% | 歷史新高；純益精確值待補（1 月上修時預想 ¥3,285 億、實績應更高）|
| FY2026 guidance（至 2027-03）| 營收 ¥1.42 兆（+25.8%）／OP ¥6,275 億（+25.7%）／純益 ¥4,655 億（+24%）| 連三年新高預想 |
| 股價 | ~¥26,100（2026-06-09）；52 週低 ~¥7,200〜8,100（來源不一）／高 ¥32,400 | **12M 約 +270%**、距高點回檔 ~15-20% |
| Forward PE | **~40-53x**（2026-03-21 口徑 52.97；依公司 FY2026 guidance 粗算 ~41-44x）| C 軸警示主證據；vs Teradyne 級距待補 |
| 市值 | ~¥19-20 兆（粗估）| 日股 AI 行情領頭羊之一（Nikkei 68,000 行情）|
| ATE 市佔 | ~50-58%（第三方估計、口徑不一）；雙寡頭合計 >85% | HBM 測試 >60%（利基近 70%）|
| 產能 | SoC tester 年產能擴至 5,000 台以上（2027-03 前、法說）| 供不應求訊號 |

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感（逆向）| 5 | GPU／ASIC／HBM 三家／CPO vs pluggable——誰贏都要測、complexity 越高測越多；唯一單一暴露是「AI capex 總量」本身 |
| 站別關鍵 | 5 | ATE 雙寡頭老大、AI SoC 主測平台 + HBM 測試 >60%；known-good-die 是 HBM／CoWoS 堆疊不可繞過站 |
| 耗材 recurring | 3 | 設備為主；service／interface board／socket recurring 中等 |
| IP | 4 | V93000 平台生態 IP 深；但 Teradyne Magnum 7H（2025-08、宣稱 HBM wafer test time -40%）證明壁壘可被進攻、非鐵壁 |
| 客戶分散 | 4 | 跨 SoC／memory／車用類比，但 AI 複合體（NVDA 鏈 + 3 家 HBM 廠）營收集中度急升、FY2025 成長幾乎全靠 AI |

**總分 = 21/25**（confidence: medium）——高於 [[Teradyne]] 19（站別 +1、路線 +1、呼應 Teradyne 檔內「Advantest 在 AI SoC／HBM 測試居上風」）、低於村田 24／[[Infineon]] 22 級；若把「AI capex 單一總量週期」計入路線敏感扣 1 → 取 **20-21/25 區間**。

⚠️ **ABCD 判定：A 強、B／C 雙紅燈。** 依 [[投資四元問題框架（ABCD）]]：A（結構價值）20-21/25 成立；B（市場認知）已到 [[市場四階段：懷疑／驗證／共識／反轉]] 的**共識期**（「ASML of test」稱號流通＋Nikkei 領頭羊地位）；C（估值）12M +270% ＋ Forward PE 40-50x。**乘法規則下本檔用途 = [[Teradyne]] 19/25 call 的對手盤記分板對照組、非進場標的。**

## 監控指標

| 指標 | 觸發行動 |
|---|---|
| Teradyne Magnum 7H 拿下 SK hynix／Samsung／Micron 主力 HBM 訂單 | Advantest 站別關鍵 5→4 下修；同時是 [[Teradyne]] 19 分上修證據 |
| FY2026 guidance 上修節奏（FY2025 曾三度上修）停止或下修 | 動能轉折、共識期→反轉期訊號（先減後查）|
| Forward PE 壓縮至 ~25-30x 且 AI 測試需求未壞 | C 軸解除、重新評估進場（[[PE 壓縮公式]]＋[[Re-rate 捕捉法]] 反向應用）|
| CPO 量產測試訂單歸屬：FormFactor+Advantest test cell vs Teradyne Photon 100（NVDA／TSMC COUPE 認證）| 誰拿單誰上修——CPO 測試戰場雙寡頭直接對決、[[CPO 供應鏈圖譜]] 第 9 層更新 |
| HBM4 測試強度公開數據（test time／insertion 數 vs HBM3E）| 驗證「complexity↑=測試 TAM 擴張」產業層 thesis |

## 相關連結

- [[Teradyne]]（雙寡頭對手盤、wiki 記分板 19/25 原 call）
- [[CPO 供應鏈圖譜]]（第 9 層測試／檢測）
- [[賣水人選股邏輯（投資版）]]／[[投資四元問題框架（ABCD）]]
- [[鴻勁 7769]]／[[致茂 2360]]（CPO 測試 cluster；分選機／SLT 與 ATE 上下游同袍）
- [[市場四階段：懷疑／驗證／共識／反轉]]（B 軸定位：共識期）
- [[PE 壓縮公式]]／[[Re-rate 捕捉法]]（C 軸工具）
- [[NVDA]]／[[TSMC]]／[[AVGO]]／[[AMD]]（測試需求方）
- [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]（CPO 延期 = 爬良率堆測試階段、測試廠先收錢）

## Sources

- [Advantest FY2025 Consolidated Financial Results（2026-04-27）](https://www.advantest.com/en/news/2026/a81o6o0000000hgw-att/E_FR_FY2025_FN.pdf)
- [業界digest：アドバンテスト 2026年3月期決算（營收 +44.7%／OP +118.8%／來期 guidance）](https://www.gyokaidigest.com/companies/advantest/report/2026-FY)
- [STOCK EXPRESS：決算解說 2026-04-27（產能擴張）](https://stockexpress.jp/advantest20260427/)／[2026-01-28（三度上方修正）](https://stockexpress.jp/advantest20260128/)
- [FormFactor × Advantest SiPh／CPO wafer-level test cell（2024-11-07）](https://www.formfactor.com/press-release/formfactor-and-advantest-partner-on-silicon-photonics-wafer-level-test-cell-to-enable-high-volume-manufacturing/)
- [Teradyne Magnum 7H 發布（2025-08-04、HBM2E〜HBM4E）](https://investors.teradyne.com/news-events/press-releases/detail/419/teradyne-unveils-magnum-7h---the-next-generation-memory-tester-for-high-bandwidth-memory-devices)
- [Yahoo Finance：AI growth brings new tests for semi-test duopoly（雙寡頭 >85%）](https://uk.finance.yahoo.com/news/ai-growth-brings-tests-semi-140502874.html)
- [valueinvesting.io：6857.T Forward PE 52.97（2026-03-21）](https://valueinvesting.io/6857.T/metric/forward-pe)
- [TSPA Semiconductor：Advantest "ASML of the Test Industry"（HBM／SoC 市佔）](https://tspasemiconductor.substack.com/p/advantest-leading-the-ai-testing)
- [Seeking Alpha：Advantest／Teradyne market share shifts in this duopoly](https://seekingalpha.com/article/4837312-advantest-teradyne-market-share-shifts-in-this-duopoly)

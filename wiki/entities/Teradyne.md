---
title: Teradyne
aliases: [TER, Teradyne Inc, NASDAQ:TER, Photon 100]
type: entity
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-12-10
sources:
  - raw/2026-06-09_SemiAnalysis-800VDC-CPO-延期-機構報告中文摘要.md
  - https://investors.teradyne.com/news-events/press-releases/detail/436/teradyne-introduces-photon-100
tags: [標的, 美股, 半導體測試, ATE, CPO 測試, 矽光子, 檢測賣水人, robotics]
confidence: medium
---

# Teradyne（NASDAQ: TER）

## 1. 一句話定位

**全球 ATE（自動測試設備）雙寡頭之一（vs Advantest）+ 業界首發 CPO 光電合一量產測試平台 Photon 100**——SoC／memory／類比 ATE 主業 + Robotics（Universal Robots／MiR）第二曲線；2026-03-17 OFC 發布 **Photon 100**：支援 **wafer（單面＋雙面）／discrete optical engine／co-packaged module 三段測試 insertion** = 「光引擎在不可返修貼裝前先篩壞片」的商品化——正是 SemiAnalysis 良率數學（0.95³² ≈ 19% 系統良率）下「組裝前徹底檢測是唯一出路」的直接受惠者。

## 2. CPO 測試 thesis（#P1 核心）

- **良率地獄 → 測試強度結構性上升**：CPO 焊接後無法返修、一顆壞引擎拖垮整包 → known-good-engine 篩選變成必經站
- **SemiAnalysis 官方 X thread（2026-03-26）**：PIC wafer-level 測試需要全新「雙面光電 probing」、**新增測試設備支出全部集中在這裡**
- **時程 nuance（為什麼 CPO 延期對測試廠反而偏多）**：測試設備在量產**之前**的良率爬坡期就要採購、且良率越爛測試強度越高——CPO 延到 2029+ 表示 2026-2029 都在「爬良率、堆測試」的階段
- ⚪ **「輝達認證領先者」未證實**：Photon 100 官方稿零客戶名（無 NVIDIA／TSMC／出貨日期）——此說法僅見於 SemiAnalysis 機構報告轉述、待驗證
- 對照組：[[Advantest]] **20-21/25**（#P5 建檔——⚠️ **2024-11 已與 FormFactor 合作 SiPh wafer-level test cell、早 Photon 100 約 16 個月**：本檔「CPO 測試首發」修正為「首發**整合式**光電 ATE 平台」、對手已在場且 Magnum 7H 正攻 HBM）、[[FormFactor]]（雙面 probe card、watchlist）、[[致茂 2360]] 18（SLT＋光電量測）、[[鴻勁 7769]] 18（分選機＋溫控）、[[穎崴 6515]] 18／[[旺矽 6223]] 19（介面耗材端、#P5 建檔）

## 3. 財務／結構快照（As of 2026-06-10、粗粒度）

| 指標 | 數值 |
|---|---|
| 主業 | SoC／memory／類比 ATE + Robotics |
| ATE 格局 | 跟 Advantest 雙寡頭（合計 ~80-90% 高階 ATE）|
| Photon 100 | 2026-03-17 OFC 發布、CPO／矽光子量產測試平台首發 |
| 歷史風險 | mobile（Apple 鏈）測試週期波動、Robotics 成長不及預期 |

> ⚠️ 本檔為 #P1 驗證型 ingest 簡版建檔（confidence: medium）——財務細節（營收／Forward PE／市佔數字）待補一輪法說／10-K 校準後升級。

## 五軸評分（25 分制）

| 軸 | 分數 | 理由 |
|---|---|---|
| 路線敏感（逆向）| 4 | NVDA／ASIC／AMD 誰贏都要測；CPO 或 pluggable 誰主流都有測試需求（CPO 良率越爛測越多）|
| 站別關鍵 | 4 | ATE 雙寡頭 + Photon 100 三段 insertion 首發；但 Advantest 在 AI SoC／HBM 測試居上風 |
| 耗材 recurring | 3 | 設備為主、service／升級 recurring 中等 |
| IP | 4 | ATE 平台 IP 深 + 光電合一測試先行 |
| 客戶分散 | 4 | 跨 SoC／memory／類比／robotics、歷史上 mobile 集中度高峰已分散 |

**總分 = 19/25**（confidence: medium）——跟 [[Lumentum]] 19／[[Coherent]] 19／[[MACOM Technology]] 19 同級；「良率地獄賣檢測」= [[TGV 檢測分類 taxonomy]] AXI（[[德律]]）pattern 在 CPO 賽道的重演。

## 相關連結

- [[CPO 供應鏈圖譜]]（第 9 層測試／檢測）
- [[賣水人選股邏輯（投資版）]] 第十九波 #P1
- [[鴻勁 7769]]／[[致茂 2360]]（CPO 測試 cluster 同袍）
- [[德律]]（AXI 檢測賣水人同構）
- [[TGV 檢測分類 taxonomy]]
- [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]
- [[NVDA]]／[[TSMC]]（COUPE 測試需求方）

## Sources

- [Teradyne Introduces Photon 100（2026-03-17）](https://investors.teradyne.com/news-events/press-releases/detail/436/teradyne-introduces-photon-100)
- [SemiAnalysis X：CPO test flow（2026-03-26）](https://x.com/SemiAnalysis_/status/2037213323683319873)
- raw/2026-06-09_SemiAnalysis-800VDC-CPO-延期-機構報告中文摘要.md

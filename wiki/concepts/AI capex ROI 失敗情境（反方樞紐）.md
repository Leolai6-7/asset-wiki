---
title: AI capex ROI 失敗情境（反方樞紐）
aliases: [反方樞紐, AI capex 空方情境, ROI 失敗情境, AI bear case hub]
type: concept
created: 2026-06-10
updated: 2026-06-10
as_of: 2026-06-10
check_after: 2026-11-15
thesis_dependency: counter
sources:
  - https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
  - https://sequoiacap.com/article/ais-600b-question/
  - https://www.goldmansachs.com/insights/top-of-mind/gen-ai-too-much-spend-too-little-benefit
  - https://www.bain.com/about/media-center/press-releases/20252/$2-trillion-in-new-revenue-needed-to-fund-ais-scaling-trend---bain--companys-6th-annual-global-technology-report/
  - https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
  - https://www.cnbc.com/2025/11/14/ai-gpu-depreciation-coreweave-nvidia-michael-burry.html
  - https://www.bloomberg.com/news/articles/2025-03-26/microsoft-abandons-more-data-center-projects-td-cowen-says
  - https://www.cnbc.com/2025/02/08/tech-megacaps-to-spend-more-than-300-billion-in-2025-to-win-in-ai.html
  - https://introl.com/blog/hyperscaler-capex-600b-2026-ai-infrastructure-debt-january-2026
tags: [反方樞紐, ROI, capex, 失敗情境, 空方證據, regime 開關]
confidence: medium
---

# AI capex ROI 失敗情境（反方樞紐）

全庫 AI-capex thesis 的**結構化反方**。本庫多數 entity/concept 隱含「capex 持續成長」假設——本檔集中空方證據、算 ROI 數學、推演 capex 下修對六大戰場的傳導順序，並定義「從參考升級為行動」的觸發指標。空方數據本身 confidence: high（多來源）、傳導鏈排序是推演 confidence: low-medium。

## 一句話

> Hyperscaler 2023-2026 累計砸 ~$1.4T，AI 直接營收僅 ~$50-100B/年；若 ROI 持續不兌現，capex 下修的傳導順序是：載板新平台 → 測試 → 光通訊 → 散熱 → 記憶體 → 電力。

## 空方證據清單（2024-2026 真實研究）

| 來源（日期） | 核心數字 |
|---|---|
| **MIT NANDA《The GenAI Divide》**（2025-08） | **95% 企業 GenAI pilot 失敗**（無可測 P&L 影響）、僅 5% 達營收加速；150 訪談＋350 問卷＋300 部署；主因是 learning gap 而非模型能力 |
| **紅杉 David Cahn《AI's $600B Question》**（2024-06） | $200B 問題（2023-09）一年內升級為 **$600B 問題**；隱含營收要求 vs 實際 AI 營收缺口 **~$500B** |
| **Goldman《Gen AI: too much spend, too little benefit?》**（2024-06） | ~$1T capex「至今幾無回報」；Covello：AI 須解高複雜問題才回本、目前做不到；Acemoglu：10 年僅 25% AI 任務具自動化成本效益、累計 GDP 貢獻僅 **+0.9%** |
| **Bain Global Tech Report**（2025-09） | 2030 年 AI 算力需 **$2T 年營收**支撐、即使計入 AI 節省仍**短缺 $800B**；需 $500B 年 capex＋200GW 電力 |
| **Gartner**（2025-06 / 2026-04） | **>40% agentic AI 專案 2027 底前將被取消**（成本失控／價值不明／風控不足）；2026-04 再指 I&O AI 專案在 ROI 兌現前就停滯 |
| **IBM CEO Study**（2025） | 僅 **25%** AI 計畫達成預期 ROI |
| **Michael Burry 折舊質疑**（2025-11） | hyperscaler 用 5-6 年折舊掩蓋 2-3 年實際壽命 → 2026-2028 全行業**低估折舊 ~$176B**＝虛增獲利 |
| **TD Cowen／Microsoft 退租**（2025 Q1） | MSFT 取消數百 MW 租約、再放棄美歐 **~2GW** 專案——capex guidance 可在邊際被收回的先例 |

## ROI 數學

### Capex 累計 vs AI 直接營收

| 年度 | Big 4 capex（實際/指引） |
|---|---|
| 2023 | ~$150B（推估） |
| 2024 | **$230B**（實際，CNBC） |
| 2025 | **$388B**（實際） |
| 2026 | **$602-630B**（指引；含 Oracle 五家 $660-690B） |

**2023-2026 累計 ~$1.4T**。對照可查到的 AI 直接營收：OpenAI 2025 底 ARR ~$20B（2026-05 run-rate ~$33B）、Anthropic 2026 初 run-rate ~$9B（後續暴衝報導未經審計）、Microsoft AI 年化 $37B、AWS 自研晶片 $20B——**全部加總 ~$100B/年 vs 單年 capex $660B+**。

### 隱含回收要求（Cahn 算法）
capex ×2（GPU 僅佔 DC TCO 一半）×2（營運商需 ~50% 毛利）→ **2026 一年的 capex 隱含 ~$1.3T+ 年化終端營收要求**，與 Bain 的 2030 $2T 估算同向。當前營收/要求比 <10%。

### GPU 折舊年限爭議
- **會計面**：MSFT/GOOG/Oracle 用最長 6 年；2020-2024 全行業一路延長年限（墊高 EPS）
- **2025 出現分歧**：Amazon **縮短**部分伺服器年限、Meta 反而再延長
- **技術面空方**：NVDA 一年一代＝經濟壽命 2-3 年（Burry $176B 論）
- **反證**：CoreWeave 自 2023 即用 6 年制、2020 年 A100 仍滿租、H100 租價維持原價 ~95%——**二手租賃價是此爭議的可觀測裁判**

## 失敗情境傳導鏈（六戰場衝擊排序）

ROI 不兌現 → 市場懲罰「無變現證據的 capex」→ guidance 下修 → 訂單傳導。**誰先死誰後死**（推演、confidence: low-medium）：

| 順位 | 戰場 | 邏輯 |
|---|---|---|
| 1 先死 | **載板（玻璃/TGV）** [[玻璃基板與 FOPLP 賽道]] | 未量產的「下一代平台」期權，capex 緊縮第一個延後導入（庫內已標 thesis_dependency: AI-capex） |
| 2 | **測試** [[檢測賣水人 pattern（良率地獄賣檢測）]] | 設備是 capex 先行項目、新賽道檢測（TGV AXI／CPO KGD）隨新平台凍結；但「延期先收錢」機制讓既有檢測短期抗跌 |
| 3 | **光通訊** [[CPO 供應鏈圖譜]] | 800G→1.6T 升級週期可推遲、模組屬年度採購非長約＝高 beta；DCI（電信業務）有緩衝 |
| 4 | **散熱** [[AI infra 散熱戰場]] | 綁 rack 出貨量，但風冷→液冷滲透率上升部分對沖（量縮、content/rack 仍升） |
| 5 | **記憶體（HBM）** [[AI 記憶體結構性供給短缺]] | 預付長約到 2028 提供緩衝＝死得晚；但毀約/重議價時跌幅最劇（記憶體週期本質）＝死得重 |
| 6 後死 | **電力** [[AI infra 電力戰場]] | 變壓器/燃氣輪機 lead time 2-4 年、backlog 排到 2028-2029、且電氣化需求非純 AI；下修 12-18 個月後才傳導 |

## 與庫內多頭框架的正面對決

| 多頭框架 | 如果錯、會錯在哪一步 |
|---|---|
| [[AI 利潤奇點（Token 經濟學拐點）]] | 錯在「成本降 60-70% 必然轉化為毛利」——開源/價格戰可把售價降速拉到與成本同步、剪刀差閉合；且 2030 token 用量 25 倍是 forecast，MIT 95% pilot 失敗直接打擊企業端 24 倍成長的需求假設 |
| [[AI 變現能見度分歧（證明給我看階段）]] | 錯在把 RPO 當終端需求——RPO 裡的 AI lab 算力合約靠 VC 融資支撐＝**循環融資**；lab 融資斷則 backlog 變壞帳，「能見度」一夜蒸發 |
| [[半導體基礎建設化]] | 錯在資產壽命——基礎設施估值（30-50x）前提是 utility 級穩定現金流，但 GPU 折舊爭議顯示資產更像消費電子；一次 capex 下修就證偽、EPS 與 PE 雙殺退回 cyclical 倍數 |
| [[CapEx 見頂辯論]] | 本檔是其空方分支的執行版：「何時見頂」的提問本身已預設會見頂——失敗情境是「見頂＋急墜」而非高原 |

## 觸發指標（regime 開關接口）

接 [[規則層回測發現（V 型定理與曝險前緣）]]——反應式降險在 V 型崩盤雙輸，所以**本檔的用法是「賣在上漲中」的基本面前置訊號**，不是跌了才看：

1. 任一 hyperscaler **下修次年 capex guidance**（增速轉負＝最強訊號；2026 指引仍 +60%，未觸發）
2. TD Cowen 型退租再現且 **>2GW／多家同時**（2025 Q1 MSFT 先例＝半觸發過、後被增長吸收）
3. **RPO 增速連兩季放緩**，或 OpenAI/Anthropic 融資輪延遲／down round（循環融資斷裂訊號）
4. 任一 hyperscaler **縮短 GPU 折舊年限**（Amazon 2025 已部分縮短＝半觸發、看是否擴散）
5. NVDA data center 營收 **QoQ 轉負**或訂單能見度語言轉弱
6. **二手 H100/B200 租賃價跌破原價 50%**（CoreWeave 95% 為基線）
7. 企業 AI 預算 CIO survey **YoY 轉負**、或 Gartner 40% 取消率被實際數字上修

**判定規則**：每次 [[weekly-review]] 對照；任 2 項同時觸發 → 本檔從「參考」升級「行動」（降 AI-capex 曝險、對 thesis_dependency: AI-capex 標記之 entity 全面重評）。

## 相關連結

- [[CapEx 見頂辯論]]（本檔的母題、regime 開關的基本面版）
- [[AI 利潤奇點（Token 經濟學拐點）]]／[[AI 變現能見度分歧（證明給我看階段）]]／[[半導體基礎建設化]]（被對決的多頭框架）
- [[賣水人選股邏輯（投資版）]]（Covello 也承認泡沫破前賣水人先賺——但本檔說明賣水人不是免死金牌）
- [[6 戰場交集圖譜]]／[[AI infra CapEx 三階段論]]（傳導鏈的正面藍圖）
- [[AI infra 電力戰場]]／[[AI infra 散熱戰場]]／[[AI 記憶體結構性供給短缺]]／[[玻璃基板與 FOPLP 賽道]]／[[CPO 供應鏈圖譜]]／[[檢測賣水人 pattern（良率地獄賣檢測）]]
- [[規則層回測發現（V 型定理與曝險前緣）]]（為何觸發指標必須前置而非反應式）

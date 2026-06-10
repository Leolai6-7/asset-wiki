---
title: SemiAnalysis 800VDC 與 CPO 延期報告（機構版）中文摘要
source: SemiAnalysis 機構客戶限定報告（2026-06-09 或稍早分發）之中文摘要、Leo 提供
date: 2026-06-09
type: raw / 二手摘要（原報告付費牆後、不可得）
標的: [800VDC, CPO, NVIDIA, Vertiv, FPS, Wolfspeed, Navitas, Lumentum, Coherent, Himax, AAOI, Teradyne, 鴻勁, 致茂, Infineon, MPS, Murata, 國巨]
資料來源: Leo 2026-06-10 貼入、性質為機構報告的中文摘要轉述（含「」引註標記、疑似 NotebookLM 式整理）
驗證狀態: 已驗證 — 見 wiki/summaries/2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證.md
---

# SemiAnalysis 報告重點摘要：800VDC 與 CPO 的延期衝擊（Leo 提供之中文摘要、原文照錄）

這份由 SemiAnalysis 於 2026 年 6 月 9 日發布的報告指出，目前主導 AI 半導體市場敘事的核心題材——800VDC（高壓直流電）架構與 CPO（共封裝光學），在實際量產與採用時程上均面臨顯著延後。這將重新調整投資人的預期並引發市場資金的重新配置。

## 一、800VDC 架構全面推遲至 2028 年之後

- **量產時程延後**：由輝達（Nvidia）主導的原生單端（single-ended）800VDC 設計，其大規模量產與出貨時間已被推遲至 2028 年以後（原先市場預期為 2027 年）。
- **大型雲端服務商（Hyperscalers）的抵制**：業界消息指出，雲端服務商正在推遲採用 800VDC 架構。主要原因在於輝達新一代的 Rubin 晶片仍使用 50VDC 輸入，800VDC 並非必要條件。
- **效率疑慮**：雲端服務商認為，將電網的 350-450VDC 電力先升壓至 800VDC，再降壓至 50VDC 供給運算板（compute tray），這在能源轉換上非常缺乏效率。他們更傾向於直接以較高電壓輸送，並在靠近運算板時再行降壓。
- **±400VDC 仍按計畫進行**：與 800VDC 架構不同，主要用於雲端服務商自家自研 ASIC 部署的 ±400VDC 架構仍按原時程於 2026 年下半年推進。相關機櫃（sidecar）訂單預計於今年底落地，並於 2027 年第一季擴大生產。

## 二、CPO（共封裝光學）面臨技術與良率瓶頸

- **市場時程過於激進**：華爾街原先預期 Scale-up（縱向擴展）CPO 會在 2027 或 2028 年迎來大爆發，但報告指出真正的規模出貨要等到 2029 年以後（與 Feynman 晶片的量產同步）。在此之前，銅纜（Copper）與常規可插拔光學模組仍是主流。
- **殘酷的良率考驗（Yield Math）**：在 Scale-out（橫向擴展）CPO 交換器中，系統級整合是最大障礙。目前業界估計光學引擎的貼裝良率最高僅 95%。若一台交換器晶片（ASIC）需要連接 32 個 COUPE 光學引擎，複合下來的系統級良率僅有約 19%（0.95^32），且焊接後無法進行任何返修。若要讓大規模量產具備經濟效益，單個引擎的貼裝良率必須拉高至 99.5%（此時系統良率約 85%）。
- **首款測試遭遇挫折**：輝達首款 102.4T 搭載第二代 COUPE 的 Spectrum 6 CPO 交換器，在板級系統測試中出現大於 3.5 dB 的插入損耗（Insertion loss），耗盡了整個光通道預算，表現甚至比上一代 Spectrum 5 還差。目前輝達與台積電尚未找到根本原因，研發已轉向基礎組裝製程的重新設計。
- **InfiniBand CPO 狀況較佳**：輝達的 Quantum X3450 由於每個模組僅有 3 個 COUPE，壞片可以被篩選剔除，因此其經濟效益仍在可控範圍內。

## 三、供應鏈與個股市場影響（Read-Across）

隨之而來的時程推遲，導致原本市場熱捧的題材短期承壓，而原本被忽視的傳統方案供應商重新獲得青睞（近期贏家變短期輸家，反之亦然）：

### 偏向樂觀／受惠者（Incremental Positive）

- **傳統電氣與廠務設備商**：800VDC 的延後延長了低壓變壓器、低壓開關櫃及母線（busway）產品的生命週期與成長空間。受惠個股包括 Vertiv（同時延續其大型 UPS 業務壽命）、Forgent Power Solutions (FPS)、Legrand、Schneider Electric、Hammond Power Solutions、ABB。
- **銅纜與常規可插拔光學供應商**：CPO 的延後鞏固了銅纜與傳統可插拔光學模組（及 DSP）的市場。受惠者包含 Amphenol、Semtech、MACOM（銅纜板塊），以及 Marvell、Innolight（旭創）、Eoptolink（新易盛）、Astera Labs、Tower Semiconductor、STMicroelectronics。
- **CPO 測試設備商**：在系統良率極低的狀況下，組裝前的徹底檢測是唯一出路。受惠個股包含 Teradyne（輝達認證領先者）、Form Factor、Chroma（致茂）、Hon Precision（鴻勁）。
- **板級 VRM／電源半導體**：不論上游架構如何演變，降壓鏈條（48V 降至 sub-1V）皆不受影響。受惠個股包括 Infineon（英飛凌，布局最全面）、MPS、Renesas、Vishay，以及相關 MLCC 廠（Murata、SEMCO、Yageo 國巨、TDK）。

### 偏向保守／面臨壓力者（Incremental Negative）

- **第三代半導體（寬禁帶）純晶圓廠**：如 Wolfspeed (WOLF)、Navitas (NVTS)。因為 800VDC 是這類化合物半導體（如 SiC、GaN）產值爆發的核心催化劑，推遲意味著短期內缺乏能支撐當前高估值的有感催化劑。
- **高度依賴 CPO 大規模量產論述的公司**：如 Lumentum (LITE)、Coherent (COHR)、Himax (HIMX)、Applied Optoelectronics (AAOI)。雖然 CPO 在 2029-2030 年仍有光明前景，但短期的市場預期面臨修正。

---

**整理日期**：2026-06-10
**性質**：機構報告中文摘要（原報告不可公開取得）
**驗證備註**：逐條驗證結果見 summary——FPS／鴻勁／AAOI 歸類均經外部驗證屬實；「Spectrum 5」命名與「輝達認證領先者」說法無公開佐證。

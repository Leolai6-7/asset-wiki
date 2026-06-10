---
title: 研究方法 SOP（驗證型 ingest 與記分板閉環）
aliases: [研究方法 SOP, 研究方法, 驗證型 ingest, 記分板閉環]
type: concept
created: 2026-06-10
updated: 2026-06-10
sources:
  - 2026-06-10 方法論收口（P1 SemiAnalysis 驗證型 ingest 為範本）
tags: [Meta 框架, 研究方法, SOP, 驗證, 評分, 閉環, 方法論總綱]
confidence: medium
---

# 研究方法 SOP（驗證型 ingest 與記分板閉環）

**本庫的研究方法總綱**——知識怎麼進來、怎麼被驗證評分、怎麼保持新鮮、怎麼被結果校準。投資側的孿生總綱見 [[投資四元問題框架（ABCD）]]。

## 完整迴路

```
素材 → ①知識點 gate → ②兩層驗證 → ③summary → ④entity/concept 評分
                                                      ↓
⑧框架更新 ← ⑦記分板歸因 ← ⑥監控執行（每週檢視）← ⑤wikilink 圖＋index/log
```

## ① 知識點 gate（什麼配進庫）

> 把素材剝離個人情境後、能不能獨立成立並被引用？是 → wiki；否 → 不進庫。

來源優先序：**一手**（法說／10-K／規格書／OCP spec）＞ 機構報告（channel check）＞ KOL ＞ 媒體轉述。每來源過 [[KOL source reliability（KOL 來源可靠度評估）]]（15 分制 = 思維強度＋命中率＋訊息擴散階段）。

## ② 兩層驗證（驗證型 ingest、P1 範本）

每條 claim 拆兩層、分開標記：

- **(a) Attribution**：來源真的這樣說嗎？（轉述可能扭曲——P1 案例：中文摘要 vs SemiAnalysis 原文）
- **(b) Truth**：說法本身與公開資訊一致嗎？

四級標記：**✅ 雙層通過／🟡 業界一致但無法確認原文／❌ 與公開資訊矛盾／⚪ 無法驗證**。

鐵則（P1 教訓、記分板已結案 C2）：**read-across 名單一律外部驗證、不憑模型記憶判定**——「FPS 疑似轉錄錯誤」「AAOI 歸類誤植」兩個懷疑都被驗證打臉、模型記憶跑不贏新掛牌與當日行情。

## ③ Summary（每份 raw 一篇）

含：一句話、核心 anchor（帶數字）、**與既有概念的深度連結**、thesis 自警惕、監控指標。raw/ 不可變、只新增。

## ④ Entity／Concept 評分

- Entity 用 [[公司 Entity 模板（Step 1-3 三段式）]]：一句話定位／三層 thesis／財務快照
- 評分三件套：五軸 25 分（[[賣水人選股邏輯（投資版）]]）＋ [[結構影響分 vs 可投資五軸分（雙評分體系）]] ＋ [[五軸分數 confidence gate]]（低信心給區間＋flag）
- 時效 metadata（[[時效 metadata schema（lint 規範）]]）：`as_of`／`check_after`／`expires_on` 必填——知識有保鮮期
- **confidence 標準**：high＝多源確認／medium＝單源／low＝推測或過時

## ⑤ Wikilink 圖

wiki 是圖不是清單——[[wikilink]] 是結構化的邊（因果／從屬／對比）。每篇至少連 3 個既有節點；查詢時 grep 反向連結＋遍歷 1-2 層。index.md／log.md 每次必更。

## ⑥ 監控執行（把死表變活警報）

每個 entity 必附**監控指標表**（指標→觸發行動）；`check_after` 到期＋監控指標＋財報日曆 → 每週檢視產出「本週要看什麼」。監控指標沒有執行機制 = 死信。

## ⑦ 記分板歸因（把 wiki 當第四個 KOL 評分）

- **每個帶日期的評分 call 都是可檢驗的預測**、必須入記分板：+3／6／12 個月對標 benchmark
- 命中與失誤都歸因到 **ABCD 哪一軸**（A 結構誤判／B 擴散誤讀／C 估值滯後／D 執行紀律／驗證紀律）
- 未滿 10 筆已結 call、wiki 不給自己 reliability 分——**在此之前、五軸分是「結構化的意見」、不是「校準過的機率」**

## ⑧ 框架更新（錯誤是方法的原料）

已發生的範例：SNPS 失誤（C+B 軸）→ 催生雙評分體系；subagent 評分發散 → 催生 confidence gate；FPS／AAOI 誤判 → 催生「read-across 必外驗」鐵則。**每次歸因必須回答：哪條規則要改？** ⚠️ #P9 新增鐵則：**「未滿 10 筆」紀律擴張到所有框架級結論與新規則**——新規則上線預設 flag-only（可記錄、不可單獨改判／驅動交易）、通過預註冊歷史檢驗（n≥5 事件＋假陽性率）才升格 gate；修辭不得超過證據等級（定理／驗證／通過＝A-B 級專用詞）。

## 注碼跟隨研究深度（研究↔投資的接口規則）

> 集中投資的核心紀律：**注碼跟隨信心、信心來自研究深度。**

**深度檔 gate**（四項齊備 = 解鎖大注上限）：
1. entity 存在且套三段式模板
2. 五軸校準（含雙評分＋confidence）
3. **一手 anchor**（法說 MEMO／10-K 級、非 KOL 轉述）
4. triggers＋falsification 已綁定

四項齊備 → 單檔上限可至 20-25%；淺覆蓋（缺 2 項以上）→ 壓 10% 以下。**研究深度與注碼不匹配 = 最大部位裸奔**（部位內容在私有層、規則在此）。

## 庫的成長原則：決策驅動、不是素材驅動

ingest 的優先序由決策迴路拉動：**持倉的研究缺口 ＞ 記分板待驗 call 的證據 ＞ trigger 監控所需 ＞ 新素材**。「有趣但不接決策」的素材排最後。

## 相關連結

- [[投資四元問題框架（ABCD）]]（投資側總綱）
- [[賣水人選股邏輯（投資版）]]、[[結構影響分 vs 可投資五軸分（雙評分體系）]]、[[五軸分數 confidence gate]]
- [[KOL source reliability（KOL 來源可靠度評估）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]、[[時效 metadata schema（lint 規範）]]
- [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]（驗證型 ingest 範本）

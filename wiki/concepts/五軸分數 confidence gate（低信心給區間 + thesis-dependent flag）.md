---
title: 五軸分數 confidence gate（低信心給區間 + thesis-dependent flag）
aliases: [五軸 confidence gate, confidence gate, 低信心區間, thesis-dependent flag]
type: concept
created: 2026-06-09
updated: 2026-06-09
as_of: 2026-06-09
check_after: 2027-06-09
sources: []
tags: [Meta 框架, 評分體系, confidence, 假精度防範, 五軸評分]
thesis_dependency: none（可遷移方法）
confidence: medium
---

# 五軸分數 confidence gate（低信心給區間 + thesis-dependent flag）

asset-wiki 的**五軸評分置信度三級閘**。codex 質疑「IQE 19/25 是假精度」落地：confidence: low 不該給單一分數、必須給區間 + thesis-dependent flag 揭露不確定性。

## 一句話

> 評分精度應該跟資料品質匹配——高信心給單一分、低信心給區間 + 觸發條件、假精度比沒有分數更危險。

## 問題：假精度

原本 wiki 給所有 entity 單一分數（如 `IQE 19/25`），不論：
- 資料時效（最新財報 / 半年前 / 兩年前）
- 來源品質（一手 IR / 二手研究報告 / KOL 推測）
- 路線確定性（已商業化 / pilot / R&D 階段）

→ 19/25 看起來很精準、但實際可能是 16-21 區間內的中位數猜測。

**假精度危險**：
1. 新讀者誤判 confidence
2. Ranking 順序對假精度差 1 分極敏感（19 vs 18 在 100 家 entity 表中位置差很多）
3. 更新時不知道該調幅度

## 解決：三級 gate

### Gate 1：confidence high（精確分）

**條件**：
- 最新財報 + IR 一手資料
- 三個來源以上交叉確認
- 商業化已驗證 + 規格定義

**輸出**：
- 單一分數（如 `25/25`）
- 直接進 ranking

**範例**：
- [[ASML]] 25/25（EUV 100% 壟斷 + 50+ 年 R&D 一手資料 + 大量財報 + 5 年 High-NA 領先驗證）
- [[Disco Corp]] 24/25（雷射切割壟斷 + 耗材年金財報明確）
- [[村田 Murata]] 24/25（被動元件全鏈寡占 + 三線並進財報明確）

### Gate 2：confidence medium（精確分 + review trigger）

**條件**：
- 單一可靠來源 + 推測補
- 近期但未交叉驗證
- 商業化路徑明確但 ramp 未到

**輸出**：
- 單一分數（如 `19/25`）
- 註明 `review trigger`（下季財報 / pilot ramp / 競爭路線確認）

**範例**：
- [[GlobalWafers 6488]] 18/25 review trigger：CHIPS Act 補貼撥款進度
- [[Bloom Energy]] 19/25 review trigger：Oracle Stargate 多 GW 訂單交付節奏

### Gate 3：confidence low（區間 + thesis-dependent flag）⭐

**條件**：
- 二手資料 / KOL 推測 / 早期 thesis
- 超過半年未更新
- 商業化路線分歧 / pilot 階段 / 私募未 IPO
- 89% CAGR 類未驗證 claim 為基礎

**輸出**：
- **區間分數**（如 `15-19/25`）
- **thesis-dependent flag**：「**X 條件成立時 17、Y 條件成立時 19、Z 條件失敗時 15**」
- **expires_on** + **evidence_url** 強制

**範例（J4 已落地）**：
- [[IQE]] **15-19/25** thesis-dependent flag：
  - 飛利浦 GaAs design-in 確認 + MACOM 11.5% lock-in 延續 + Cardiff fab 量產 → **19**
  - 飛利浦 design-in 取消 + MACOM 入股稀釋 → **15**
  - 89% CAGR 假設半折（44%）→ **17 區間中位數**
  - expires_on: 2026-12-31（飛利浦 design-in 確認窗口）

## 區間給法規則

低信心 entity 五軸區間給法：

```markdown
**評分（低信心）**：

| 軸 | 區間 | thesis-dependent |
|---|---|---|
| 路線敏感 | 3-5 | 若押 GaAs 單一路線 = 3；若 SiC + GaN 多路線 = 5 |
| 站別關鍵 | 3-4 | 若飛利浦 design-in 確認 = 4；若被 MACOM 整合內製 = 3 |
| 耗材 | 2-3 | epi 一次性出貨 |
| IP | 4-5 | Cardiff 50+ 年 IP 累積 |
| 客戶分散 | 1-3 | 若飛利浦 + MACOM 雙頭 = 3；若 MACOM 獨家 = 1 |
| **總分區間** | **13-20/25** | thesis-dependent |
| **基準分**（中位數）| **17/25** | review trigger 飛利浦 design-in 確認 |
```

→ 讓 Leo 看到「不是 19、是 13-20 中位數 17、看 X 條件」一目了然。

## confidence ≠ 路線敏感度（不要混淆）

容易混淆的兩件事：

| 概念 | 衡量 |
|---|---|
| **confidence**（本 concept）| 資料 / 來源 / 時效品質 |
| **路線敏感度（五軸第一軸）** | 公司是否押單一商業路線 |

→ 一家公司可以是 `confidence: high` + 路線敏感度低分（押單一路線、但路線確定性高）。

範例：[[鈦昇]] confidence high + 路線敏感度 0/5（押雷射改質單一路線、五軸 7/25）= 不是 low confidence、是路線敏感度結構性低分。

## Lint 規則自動套用

每季 lint：
1. confidence: low entity 是否仍給單一分 → flag、改區間
2. expires_on 已過 → 自動降 confidence + 重評
3. evidence_url 失效 → flag
4. medium → high 條件達成（如下季財報確認）→ 升 confidence + 收區間

## 對應 [[時效 metadata schema（lint 規範）]]

本 concept 是時效 schema 的補完——時效 schema 管「何時要重檢」、本 concept 管「分數本身該怎麼給」。

兩者組合：
```yaml
---
as_of: 2026-06-09
check_after: 2026-12-09
expires_on: 2026-12-31              # thesis-dependent 觸發窗口
evidence_url: https://...
confidence: low                      # ← 觸發本 concept 區間規則
score_range: "13-20/25"             # ← 強制區間
score_baseline: 17                   # ← 中位數
thesis_dependent:                    # ← thesis 條件清單
  high_case: "飛利浦 GaAs design-in 確認、MACOM 11.5% 延續、89% CAGR 維持"
  low_case: "飛利浦 design-in 取消、MACOM 整合內製、CAGR 半折"
---
```

## 何時必須用 Gate 3

強制使用區間的情境：
1. **89% CAGR 類未驗證 claim** 為基礎（如 IQE / Innolux FOPLP）
2. **私募未 IPO**（如 [[Wiz]] / [[Databricks]] / [[Lambda]] 規模未公開）
3. **pilot 階段未量產**（如 [[Absolics]] / [[SKC]] glass interposer 2026 H2 量產 pending）
4. **路線分歧未定**（如 [[Cerebras]] SRAM vs HBM）
5. **超過半年未更新且無新財報** lint flag

## 對應雙評分體系

跟 [[結構影響分 vs 可投資五軸分（雙評分體系）]] 配合：
- 可投資五軸分先過 confidence gate
- 結構影響分如果 thesis 框架本身在變化、也要套用 gate（如 [[FOMO SOC]] 結構影響 20-24 區間、看 thesis 框架持續迭代品質）

## 跟既有 concept 對接

- [[賣水人選股邏輯（投資版）]] master 表：confidence low entity 改顯示區間
- [[時效 metadata schema（lint 規範）]]：補完 schema
- [[公司 Entity 模板（Step 1-3 三段式）]]：entity 模板加 confidence gate 提示
- [[看錯三類型]]：假精度是「自以為精確」型錯誤的典型

## 相關連結

- [[結構影響分 vs 可投資五軸分（雙評分體系）]] — 雙評分體系
- [[時效 metadata schema（lint 規範）]] — 時效管理
- [[賣水人選股邏輯（投資版）]] — 主 ranking
- [[公司 Entity 模板（Step 1-3 三段式）]] — entity 強制格式
- [[IQE]] — 區間給法標竿 entity
- [[看錯三類型]] — 假精度錯誤類型
- [[預期差]] — 假精度會放大預期差盲點

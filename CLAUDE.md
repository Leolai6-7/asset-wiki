# Asset Wiki

個人投資 / 市場研究知識庫。LLM 維護，人類餵素材與提問。

## 結構

```
raw/              ← 原始素材（財報、研究報告、新聞、X 貼文、podcast 字幕、圖表），不可修改
wiki/
  index.md        ← 全部文章索引，按分類整理
  log.md          ← 操作紀錄
  concepts/       ← 方法論（估值方法、賣水人、Re-rate、反脆弱、控制點轉移…）
  entities/       ← 標的/產業/分析師/事件（個股、產業鏈、KOL、財報季、Fed 決策…）
  summaries/      ← 素材摘要（每份 raw 一篇）
```

## 四大操作

### 1. Ingest（吸收素材）

觸發：用戶說「吸收 raw/xxx」或「ingest」

步驟：
1. 讀 raw/ 素材（PDF / markdown / 字幕 / 圖表）
2. wiki/summaries/ 寫摘要（含重點、來源、日期、**數據時效**）
3. 判斷涉及哪些**個股 / 產業 / 方法論 / 事件 / 分析師**
4. 更新或新建 concepts/、entities/ 相關文章
5. 加 [[wikilinks]] 反向連結
6. 更新 wiki/index.md
7. 追加 wiki/log.md

### 2. Query（查詢）

觸發：投資/市場問題、研究前查背景、定 thesis 前查方法論

步驟：
1. 讀 wiki/index.md 找相關頁
2. 讀目標頁
3. **跟著 wikilinks 遍歷 1-2 層**（方法論之間、方法↔標的、標的↔產業鏈、分析師↔方法）是圖的邊，不是裝飾
4. 綜合回答，附 [[來源]]
5. 有價值就寫回 wiki 成新文章

### 3. Update（更新既有文章）

觸發：新財報 / 新數據 / 觀點更新 / 倉位/止損狀態變化

步驟：
1. 找文章
2. 補新資訊（新段落 / 更新數據 / 調 confidence / **標更新日期**）
3. 更新 frontmatter updated
4. 新連結 → [[wikilinks]]
5. 追加 log.md

### 4. Lint（健康檢查）

觸發：用戶說「lint」或定期執行

檢查：
- 矛盾資訊
- **過時內容**（投資資料半年以上未更新需 flag）
- 孤立頁面（沒有任何連結指向）
- 缺反向連結
- confidence 與時效是否相符

## 文章格式

```markdown
---
title: 文章標題
aliases: [別名]
type: concept | entity | summary
created: 2026-06-04
updated: 2026-06-04
sources:
  - raw/xxx.md
tags: [投資, 產業, 標的, 方法論, 事件, 分析師]
confidence: high | medium | low
---

# 標題

內容…

## 相關連結
- [[相關方法]]
- [[相關標的]]
```

**confidence 標準（投資版重時效）**：
- **high**：多近期來源確認、第一手資料、數據 ≤ 3 個月
- **medium**：單一來源、近期、邏輯成立
- **low**：過時（半年以上）、推測、待驗證、二手資料

## 公司 Entity 三段式（強制格式）

公司 entity（個股、產業龍頭、平台）**必須**走以下三段式——詳見 [[公司 Entity 模板（Step 1-3 三段式）]]。

```
1. 一句話定位        ← 寫不出來就不是好 entity（六個月不變）
2. 三層 thesis      ← 產業 / 目的 / 供應（半年才變，sticky）
3. 財務狀態快照      ← Re-rate 三角形 + 時間戳（會 stale，必標日期）
   + 催化 / 風險清單
```

**不要 ingest 進公司 entity**（這些是 use wiki 時的判斷，不是 wiki 內容）：
- 此刻的 Forward PE / 預期差
- 你的進場價、退場條件、倉位
- 推薦買賣判斷

**Lint 時要 flag**：Re-rate 三角形快照若超過 6 個月未更新 → 需重新評估，標 confidence: low。

## 時效 metadata schema（lint 規範）

完整見 [[時效 metadata schema（lint 規範）]]。

Snapshot 與時點性 claim **必須**標註：

```yaml
---
as_of: 2026-06-05              # snapshot 適用日期（已有慣例）
check_after: 2026-12-05        # 何時要重檢（半年/年）
expires_on: 2026-12-31         # 過了自動降 confidence 至 low（適用具體時點 claim）
evidence_url: https://...      # 主要佐證來源
---
```

**適用範圍**：
- Entity Step 3 財務狀態快照 → `as_of` 強制 + `check_after` 強制（3-6m）
- Entity 催化清單時點（如「Intel 2026 H2 量產」） → `expires_on` 強制
- 89% CAGR 類未驗證 claim → `expires_on` + `evidence_url` 強制
- Concept 方法論 → `check_after` 建議（24m）

**Lint 規則（自動執行）**：
1. `check_after` 已過 → 列出需重檢
2. `expires_on` 已過 → 自動 `confidence: high → low` + flag
3. `evidence_url` 失效 → flag

## 跨庫對照

asset-wiki 跟 llm-wiki 各自獨立維護，**wikilink 不能跨 vault**。完整對照表見 [[跨庫對照（asset-wiki ↔ llm-wiki）]]。

**何時跨庫查詢**：
- 找方法論補強（如七件事快篩、研究方法五步）→ llm-wiki
- 找 AI/技術背景（MCP 協議、LLM 內部機制）→ llm-wiki
- 找 KOL 跨領域觀點 → 雙 wiki 對照

**同名 entity 政策**：
- 兩邊各自維護、**不自動同步**
- 同名 entity 兩邊內容可不同（不同切角）
- 更新時 manual sync 重要 finding
- 衝突時：**asset-wiki 信投資側、llm-wiki 信 AI 側**

## ⚠️ Disclaimer

此 wiki 為**個人研究筆記，非投資建議**。
- 所有觀點僅供個人決策參考
- 對外發布前必須人工 review
- 引用第三方分析須註明來源 + 時效

## 同步

跟 llm-wiki 同協議——目前是 local-only，未來接 remote 時自動套用：

**操作前**（如有 remote）：
```bash
git pull --rebase origin main
```

**操作後**（任何 wiki 變更）：
```bash
git add -A
git commit -m "<type>: <描述>"   # type = ingest / lint / query / update
git push origin main             # 如有 remote
```

## 檔案命名規則

- 檔名 = title + `.md`（如 `台積電 2330.md`）
- 禁 kebab-case（Obsidian wikilink 抓不到）
- title 中 `/` → `／`、`:` → `：`
- index.md 顯示名 ≠ 檔名時用 `[[檔名|顯示名]]`

## 規則

- wiki/ 由 LLM 維護，人類不手動編輯
- raw/ 不可變，只新增不修改
- 每次 ingest 都更新 index.md + log.md
- 文章之間盡量 [[wikilinks]]
- 繁體中文撰寫
- 風格：簡潔、可驗證、重點突出、**數據附時效**
- 每次修改後 git commit（push 看是否有 remote）
- **發布前 always 人工 review**（disclaimer）

## 知識導航

wiki/ 的 [[wikilink]] 就是可查的知識圖譜——grep `[[相關概念]]` 看哪些檔連到它，跟著走。不需要 graph 工具。

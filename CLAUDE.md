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

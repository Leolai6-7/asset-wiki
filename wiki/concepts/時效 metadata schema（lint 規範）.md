---
title: 時效 metadata schema（lint 規範）
aliases: [時效 metadata, lint metadata, snapshot 時效, expires_on, check_after]
type: concept
created: 2026-06-05
updated: 2026-06-05
check_after: 2027-06-05
sources: []
tags: [Meta 框架, ingest 慣例, schema, lint, 時效, snapshot]
confidence: high
---

# 時效 metadata schema（lint 規範）

asset-wiki 的 Re-rate 三角形、財務狀態快照、催化時點都是 **snapshot**——會 stale。本 concept 定義 **lint metadata 規範**，讓 wiki 知道什麼時候該重檢、什麼時候 confidence 自動降級。

→ 解決 codex P1 「時效 claim 沒 lint metadata」

## 一句話

> Snapshot 要標日期不夠，**還要標『何時失效』**——否則 stale 訊息會被當作 current。

## 三個關鍵欄位

### `as_of`（必填，已有慣例）
- 此 snapshot 適用的日期
- 已在所有 entity 三段式 Step 3 用「As of YYYY-MM-DD」
- **行為**：純標記、不觸發 lint

### `check_after`（新增）
- 何時要重新檢查這個 claim
- 短時效 claim（如 Re-rate 三角形）= 3-6 個月
- 長時效 claim（如商業模式、護城河）= 12 個月
- **行為**：到期 → lint 提示「需重檢」、不自動改 confidence

### `expires_on`（新增）
- 此 claim 的「死線」
- 過了就 **自動降 confidence 至 low**
- 適用：高時效具體 claim（如「Intel Clearwater Forest 2026 H2 量產」）
- **行為**：到期 → 自動 confidence: low + lint flag

### `evidence_url`（新增，建議）
- 主要佐證來源
- 一個 claim 至少有一個 evidence_url
- **行為**：lint 時驗證連結還活著

## Frontmatter 範本

```yaml
---
title: ...
created: 2026-06-05
updated: 2026-06-05
as_of: 2026-06-05            # snapshot 日期
check_after: 2026-12-05      # 半年後重檢
expires_on: 2027-06-05       # 一年後降 confidence
evidence_url: https://...    # 主要佐證
confidence: high
sources:
  - raw/xxx.md
tags: [...]
---
```

## 適用範圍（強制 vs 建議）

| 內容類型 | as_of | check_after | expires_on | evidence_url |
|---|---|---|---|---|
| **Entity Step 3 財務狀態快照** | ✅ 強制 | ✅ 強制（3-6m） | ⚠️ 建議 | ⚠️ 建議 |
| **Entity 催化清單**（如「Intel 2026 H2 量產」） | ✅ 強制 | ✅ 強制 | ✅ 強制（到時點） | ✅ 強制 |
| **Entity Step 1-2（一句話定位 + 三層 thesis）** | ⚠️ 建議 | ⚠️ 建議（12m） | ❌ 不適用 | ⚠️ 建議 |
| **Concept**（方法論） | ❌ 通常不需 | ⚠️ 建議（24m） | ❌ 不適用 | ⚠️ 建議 |
| **Summary** | ✅ 強制 | ✅ 強制（6m） | ⚠️ 建議 | ⚠️ 建議 |
| **89% CAGR 類 claim** | ✅ 強制 | ✅ 強制 | ✅ 強制（找到來源前） | ✅ 強制（找到後填） |

## Lint 規則（自動執行）

當人類或 LLM 執行 `lint` 命令時，檢查：

1. **Stale check**：`check_after` 已過 → 列出需重檢的檔
2. **Expiry**：`expires_on` 已過 → 自動將該檔 `confidence: high → low` + lint 報告 flag
3. **Evidence**：`evidence_url` 是否仍可達（HTTP 200）
4. **As_of 一致性**：Step 3 快照 `as_of` 跟 `updated` 是否一致

## 範例 1：高時效具體 claim

`/wiki/entities/鈦昇.md` 催化清單：

```yaml
---
催化:
  - claim: "Intel Clearwater Forest 2026 H2 量產（已宣告）"
    as_of: 2026-06-05
    expires_on: 2026-12-31    # 若 2026 年底還沒量產 → 自動降 confidence
    evidence_url: https://www.intel.com/content/www/us/en/products/...
---
```

## 範例 2：未具名研調 claim

```yaml
---
tags: [..., market_size_unverified]    # 已用，本 concept 補正式 schema
89_cagr_claim:
  source: "sennn.nnna 文章引用『研調機構』未具名"
  check_after: 2026-09-05
  expires_on: 2026-12-05    # 半年沒驗證 → 自動降 confidence
  evidence_url: null         # 找到後填
---
```

## 對既有 wiki 內容的回溯應用

**Priority 1**（馬上補）：
- [[鈦昇]] / [[雷科]] / [[弘塑]] / [[辛耘]] / [[萬潤]]：Step 3 快照加 `as_of` + `check_after`
- [[TGV 玻璃通孔賽道 — sennn.nnna 原文 + 7 家台股驗證]] summary：89% CAGR claim 加 `expires_on`

**Priority 2**（下次 lint）：
- 所有 entity 的催化清單加 `expires_on`
- 既有 concept 的時點 claim 加 `evidence_url`

## 跟 CLAUDE.md 的關係

[[CLAUDE.md]]（asset-wiki 規範）會 update：
- 文章格式段加入時效 metadata 規範
- Lint 操作加入「自動降 confidence」規則

## 跟其他 concept 連結

- [[公司 Entity 模板（Step 1-3 三段式）]]：本 concept 是它的 metadata 補強
- [[修正三階段]] / [[市場四階段]]：時點性 thesis 必須加 expires_on
- [[預期差]]：市場預期會隨時間變、必須追蹤時效

## 相關連結

- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[CLAUDE.md]]
- 所有公司 entity（待回溯應用）

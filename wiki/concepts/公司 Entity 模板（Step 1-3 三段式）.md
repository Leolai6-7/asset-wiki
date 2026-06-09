---
title: 公司 Entity 模板（Step 1-3 三段式）
aliases: [公司 Entity 模板, Entity 三段式, Entity 標準格式]
type: concept
created: 2026-06-05
updated: 2026-06-05
sources: []
tags: [Meta 框架, ingest 慣例, entity 格式, 研究流程]
confidence: high
---

# 公司 Entity 模板（Step 1-3 三段式）

asset-wiki 的**公司 entity 標準格式**。把研究流程的 Step 1-3 寫進 wiki、Step 4-7 用 wiki 時做（**不寫進去**）。

## 設計原則

> Wiki 存「公司結構性知識」（sticky、半年才變），**不**存「個人交易日誌」（每天變）。

→ 反 [[Wiki Ritualization Risk]]：wiki 退化成裝飾常常是因為塞了不該塞的東西。

## 三段式

### 1. 一句話定位（Step 1 產出）

來自 [[10-K 閱讀法（分析師底層 #1）]] 的 Item 1 Business + Risk Factors 30 分鐘快篩：

> {這家公司在哪個產業、做什麼、靠誰賺錢}

**測試**：寫不出來 = 不是好 entity，要嘛沒搞懂、要嘛公司本身沒清晰定位。

### 2. 三層 thesis（Step 2 產出）

來自 [[跳出個股看三層：產業、目的、供應]]：

```markdown
### 產業層
賽道在 [[市場四階段：懷疑／驗證／共識／反轉]] 哪一階段？
[[資訊擴散四階段]] 哪一階段？TAM、競爭格局。

### 目的層
公司在產業裡的真實角色（學 [[宋分備忘錄 #2 — HBM iPhone Moment-Meta-軟體 PE|宋分備忘錄 #2]] 對 Meta 的辨識：
不是 AI 公司是廣告公司）。商業模式核心。

### 供應層
[[賣水人選股邏輯（投資版）]] vs 淘金者？
[[控制點轉移（投資版）]] 拿到哪一層？
```

**測試**：三層都寫不出 thesis = 不該寫成 entity，只夠寫進別人 entity 的「相關」段落。

### 3. 財務狀態快照（Step 3 產出，**必標日期**）

來自 [[五層損益表（營業槓桿）]] 的 Re-rate 三角形檢查清單：

```markdown
**As of {YYYY-MM-DD}（{Q? 20XX 財報}）**：

| Re-rate 三角形 | 狀態 |
|---|---|
| 營收品質 | ✅/⚠️/❌ {內容} |
| 毛利率 | ✅/⚠️/❌ {內容} |
| OpEx | ✅/⚠️/❌ {內容} |
| 營業利益 | ✅/⚠️/❌ {內容} |

→ Re-rate 三角形 N/4 滿。
```

### 加碼：催化 / 風險清單

```markdown
- ✅ 催化：{客戶擴張、訂單能見度、新市場}
- ⚠️ 風險：{Risk Factors 新增、產業逆風、競爭}
```

## ⛔ **不寫進 entity** 的東西

| 不寫 | 為什麼 |
|---|---|
| 此刻 Forward PE 多少 | 每天變，stale 很快 |
| 預期差 | 隨市場每天變 |
| 進場價 / 持倉 | 個人帳戶 ≠ 知識庫 |
| 退場條件 | 個人交易紀律 |
| 推薦買賣判斷 | wiki 不替你做決定 |

→ 這些屬於 **use wiki** 的時刻產出，不是 **build wiki** 的內容。

## Snapshot vs Sticky 區分

| Sticky（寫進去、半年才變） | Snapshot（標日期、會 stale） |
|---|---|
| 一句話定位 | Re-rate 三角形狀態 |
| 三層 thesis | 財報數字 |
| 商業模式 | 客戶結構 |
| 結構性護城河 | 估值倍數 |
| 結構性風險 | 催化清單 |

**Snapshot 必須**：
1. 標日期（`As of YYYY-MM-DD`）
2. 標來源（哪份財報、哪份研報）
3. Lint 超過 6 個月未更新 → flag

## Update 策略

當公司有新財報 / 重大新聞時：
1. **Update 第 3 段**（snapshot）→ 重跑 Re-rate 三角形
2. 第 1-2 段除非結構性變化（如 Meta 主業變了），否則不動
3. 跑 [[Update（更新既有文章）]] 流程（add 新段落、標日期、commit）

## 範例

asset-wiki 既有的 [[AVGO]]、[[NVDA]]、[[Anthropic]] 都接近這個格式但部分段落欠統一。

**標竿 entity**（已套用 + 完整）待補。下次 update 既有 entity 時，逐步把它們對齊這個模板。

## 對應 ingest CLAUDE.md 的位置

`asset-wiki/CLAUDE.md` 「文章格式」段已加入「公司 Entity 三段式（強制格式）」子段，引用本 concept。

## 相關連結

- [[跳出個股看三層：產業、目的、供應]]
- [[10-K 閱讀法（分析師底層 #1）]]
- [[五層損益表（營業槓桿）]]
- [[Re-rate 捕捉法]]
- [[宋分（美股送分題）]]

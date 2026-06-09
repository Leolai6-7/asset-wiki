# asset-wiki

Leo 的個人 AI 基礎建設投資知識庫。用 Claude Code agent 維護的「**結構性投資 thesis**」+「**雙評分體系**」+「**framework anchor**」整合圖譜。

> 311 檔案 / 159 entity / 77 concept / 74 summary / 78 raw / 雙評分體系完整 / codex 對抗審核校準完成。

---

## 怎麼用（給 AI agent / Claude Code 用戶）

### 1. Clone + 開啟

```bash
git clone <repo-url>
cd asset-wiki
claude   # 在 repo root 開 Claude Code、會自動 load CLAUDE.md
```

CLAUDE.md 含完整 ingest / query / lint / update 四大操作規範。Agent 進入時會自動理解：
- 三段式 entity 模板（一句話定位 + 三層 thesis + 財務狀態快照）
- 五軸 25 分制（路線敏感 / 站別關鍵 / 耗材 / IP / 客戶分散）
- 雙評分體系（**結構影響分** vs **可投資五軸分**）
- KOL 來源可靠度 framework（15 分制）
- 跨庫對照（asset-wiki ↔ llm-wiki）

### 2. 查詢 framework

```
/ask 賣水人之中的賣水人有哪些？
/ask 800V HVDC 整鏈五站賣水人池
/ask AI infra 6 戰場圖譜
/ask FOMO SOC 跨期 framework
/ask 中國半導體國產替代對沖視角
```

Agent 會跟著 `[[wikilink]]` 遍歷 1-2 層、給整合回答。

### 3. 補建新 entity / concept

> 「補建 [[Cheniere Energy]] entity」
> 「ingest 這篇 FOMO SOC 文章 URL: https://...」

Agent 自動：
- 抓內容（WebFetch）
- 比對既有 wiki（避免重複）
- 三段式 + 五軸 25 分制 + 時效 metadata
- 補強相關 entity 雙向 wikilink
- 更新 master 表 + index + log
- commit

### 4. 推薦工作流

| 場景 | 指令 |
|---|---|
| 看新 KOL 文章 | 「ingest 這 URL」|
| 找投資標的 | 「CPO / 電力戰場 / AI 資安 最值得投資的是哪家」|
| 校準 thesis | 「對抗審核 wiki 整體缺口」|
| 補空連結 | 「lint stale 標記」|

---

## 怎麼用（給人類讀者）

### 入口三條
1. **[[wiki/index.md]]** — 全部文章索引、按戰場分類
2. **[[wiki/concepts/賣水人選股邏輯（投資版）]]** — master 表、五軸 25 分制完整評分
3. **[[wiki/concepts/6 戰場交集圖譜]]** — 跨戰場 anchor 矩陣

### Wiki 結構
```
raw/              ← 原始素材（KOL 文章、財報、新聞），不可修改
wiki/
  index.md        ← 全部文章索引
  log.md          ← 操作紀錄（ingest/lint/query 全部歷史）
  concepts/       ← framework / 戰場 / 圖譜（77 個）
  entities/       ← 公司 / KOL / 標的（159 個）
  summaries/      ← 素材摘要（74 個）
```

### 11 個戰場 concept（按 importance 排序）
- [[AI infra CapEx 三階段論]] — 整 wiki 主框架
- [[800V HVDC 灰白區重劃（物理鐵壁論）]] — 電力鐵壁
- [[被動元件第三次週期（K 型復甦 + 三道防線）]] — 機櫃內 MLCC/鉭/聚合物鋁
- [[CPO 供應鏈圖譜]] — 1.6T 光模組 + SiPho foundry
- [[Bottleneck Theory（瓶頸論）]] — Serenity 七層瓶頸論
- [[MLCC 嵌入式基板賽道]] — 嵌入式 vs 分立分歧
- [[AI infra 電力戰場]] — firm power 五選一
- [[AI infra 散熱戰場]] — 液冷 + 浸沒 + cold plate
- [[AI infra 3D NAND 戰場]] — HBF iPhone moment
- [[AI 資安戰場（CSP vs Endpoint vs Network 三軌）]]
- [[EDA 三巨頭分食（Synopsys／Cadence／Siemens EDA）]]

---

## ⭐ 三大核心 framework

### 1. 賣水人之中的賣水人（可投資頂級 6 家）
| Rank | Entity | 五軸 |
|---|---|---|
| 🏆 | ASML | **25/25** |
| 🥇 | Disco Corp / 村田 / 信越化學 / SUMCO / Synopsys | **24/25** |

→ [[賣水人選股邏輯（投資版）]]

### 2. 雙評分體系（codex 對抗審核落地）
- **結構影響分**（25 分制）：適用所有 entity（含 Imec、FOMO SOC、Cameron LNG 等不可投資）
- **可投資五軸分**（25 分制）：只適用上市可投資 entity

→ [[結構影響分 vs 可投資五軸分（雙評分體系）]] + [[五軸分數 confidence gate]]

### 3. 三大 KOL 來源完整對照
| KOL | 可靠度（15 分制）| 強項 |
|---|---|---|
| **FOMO SOC** | **14/15** | 跨期 framework + 平台級 narrative |
| **宋分（美股送分題）** | **12/15** | 估值方法論 + 機構視角擴散 |
| **Serenity** | 11/15 | 物理 chokepoint 7 層瓶頸論 + alpha |

→ [[KOL source reliability（KOL 來源可靠度評估）]]

---

## 重要規則（如果你 fork 維護）

1. **wiki/ 完全由 LLM agent 維護**、人類不需手動編輯
2. **raw/ 不可變**、只新增不修改
3. **個人交易判斷不寫進 wiki entity**（進場價 / 退場 / 倉位 / 推薦）
4. **檔名與 frontmatter title 完全一致**（Obsidian wikilink 關鍵）
5. **CLAUDE.md 是 single source of truth**、所有規範在那

---

## ⚠️ 投資警語

本 wiki 是「**結構性 framework**」+ **「公開研究素材」整合**，**不是投資建議**。

- 個人交易判斷請自負風險
- 五軸 25 分制是評分工具、不是 buy/sell signal
- KOL 來源（FOMO SOC / 宋分 / Serenity）有付費牆 / 訊息蛻變 / 過熱期等已知限制
- 中國 / 地緣 / 戰爭等變數可能瞬間 invalidate 個別 thesis

如果你要用這 wiki 做投資決策、**請至少**：
- 跟你的財務顧問討論
- 多重 KOL / 機構研報 cross-check
- 認識「結構重要 ≠ 預期報酬」（[[結構影響分 vs 可投資五軸分（雙評分體系）]]）

---

## 致謝

- **KOL 來源**：FOMO SOC（KP@FOMOSoc 12 篇）+ 宋分（45 篇 substack）+ Serenity（X 7 層瓶頸論）
- **infrastructure**：Anthropic Claude Code + Obsidian + git
- **codex 對抗審核**：B-grade 質疑 → 雙評分體系 + confidence gate 落地

---

## License

Wiki 內容：CC BY-NC-SA 4.0（非商業 + 必須 share-alike）
CLAUDE.md framework + 雙評分體系：MIT（可自由複用方法論）

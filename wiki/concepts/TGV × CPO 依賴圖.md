---
title: TGV × CPO 依賴圖
aliases: [TGV CPO 依賴, TGV CPO 關係, 玻璃基板 CPO]
type: concept
created: 2026-06-05
updated: 2026-06-10
check_after: 2026-09-05
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
  - raw/2026-05-07_wallstengine_SiTime-1.6T-CPO時脈元件三倍增量.md
tags: [TGV, CPO, 依賴圖, Intel, LPKF, LIDE, 玻璃基板, 光通訊]
confidence: medium
---

# TGV × CPO 依賴圖

asset-wiki 之前把 [[TGV 製程鏈圖譜]] 和 [[CPO 供應鏈圖譜]] 並列為「姊妹 thesis」——但 **LPKF entity 的 finding 揭露這不只是平行關係**：

> **「Intel 2023 專利明寫『LIDE-formed TGV 用於 CPO 架構』」**

→ TGV 是 CPO 的**底層使能技術**，不是替代或並列。

→ 解決 codex P3 「TGV × CPO 不只平行」

## 一句話

> CPO 是上層光通訊架構，TGV 是底層玻璃中介層 — **CPO 可能依賴 TGV 才能商用**。

## 三種關係（澄清）

### ❌ 舊認知：平行
```
TGV 賽道  ←→  CPO 賽道
   (互不依賴的姊妹 thesis)
```

### ✅ 新認知：依賴
```
       CPO 架構（光通訊）
            ↓
       需要 玻璃中介層
            ↓
       玻璃中介層需要 TGV（玻璃通孔）
            ↓
       TGV 需要 雷射改質 + 化學蝕刻
            ↓
       (LPKF LIDE / 鈦昇 / 雷科)
```

### 但不是 100% 依賴

CPO 也可能用矽中介層（TSV）做：
```
       CPO 架構
            ↓
   ┌────────┴────────┐
玻璃中介層           矽中介層
 (TGV)            (TSV, 既有)
```

→ TGV 是 CPO 的「**preferred path**」但不是「唯一」。

## 為什麼 Intel 選 TGV for CPO

- 光通訊高頻寬 → 需要低訊號損耗 → 玻璃 > 有機載板
- CPO 規格密集 → 需要高互聯密度 → TGV 通孔密度
- 熱管理需求 → 玻璃 CTE 適配
- Intel 2023 專利「**LIDE-formed TGV 用於 CPO 架構**」明確押 LIDE 路線

## 投資啟示（thesis 整合）

### Tier 1：押 CPO + TGV 雙暴露
- [[SiTime]]（CPO timing）+ TGV 都受惠 = 賣水人之中的賣水人
- [[萬潤]] 6187 CPO 矽光子設備 + WoS 後段（同時受 CoWoS 量 + CPO 量）

### Tier 2：押單一賽道
- 純 CPO：Lumentum、Coherent
- 純 TGV：[[鈦昇]]、[[雷科]]

### Tier 3：押更上游
- 玻璃材料：[[Corning]] / [[AGC]] / [[SCHOTT]]
- IP 持有：[[LPKF]]（LIDE）— **CPO 採 LIDE → LPKF 從 TGV 賽道穿透到 CPO 賽道**

## LPKF 的特別地位

LIDE 專利同時覆蓋：
- TGV 賽道（直接）
- **CPO 架構**（透過 Intel 2023 專利的引用）

→ LPKF 不只是「鈦昇對手」，是 **整個 CPO + TGV 賽道的 IP 上游**。
→ [[賣水人選股邏輯（投資版）]] 五軸評分中 LPKF 拿高分（9/15）有結構性原因。

## 對 [[CPO 供應鏈圖譜]] 的補強

原 [[CPO 供應鏈圖譜]] 七層分工沒提玻璃中介層 / TGV：
- 光引擎、DSP、Timing、Switch ASIC、封裝、連接器、電源

**校準後應該加第 8 層：玻璃中介層（TGV）**——CPO 的物理載體可能就是 TGV 玻璃基板。

## 對 [[TGV 製程鏈圖譜]] 的補強

TGV 製程鏈的終端應用不只 AI ASIC（Intel EMIB / AMD / Broadcom）：
- **CPO 架構**是另一條獨立的 TGV 採用驅動力
- → 給 TGV TAM 加碼

## 跟 wiki 概念連結

- [[CPO 供應鏈圖譜]]：本 concept 是它跟 TGV 的依賴關係補強
- [[TGV 製程鏈圖譜]]：CPO 是 TGV 的另一個終端
- [[LPKF]]：IP 上游、橫跨 TGV + CPO
- [[SiTime]]：CPO timing + 平方放大
- [[萬潤]]：CPO 矽光子設備 + WoS 後段
- [[控制點轉移（投資版）]]：CPO 架構定義 = 拿到光通訊控制點
- [[半導體基礎建設化]]：TGV + CPO 雙重 infra 重估

## 待 ingest / 校準

- [[CPO 供應鏈圖譜]] 加「第 8 層：玻璃中介層」更新
- Intel 2023 LIDE-CPO 專利全文（待找）
- 玻璃中介層 vs 矽中介層 for CPO 比較

## ⭐ #P1 時程校準（2026-06-10 SemiAnalysis）

- **CPO leg 推遲 2029+**（scale-up 綁 Feynman、SemiAnalysis《CPO Book》立場 + 對抗驗證 3-0）→ 「玻璃中介層 for CPO」這條 TGV 採用驅動力同步推遲——TGV TAM 加碼項要重標時點
- **AI ASIC 封裝 leg 不受影響**（Intel EMIB／AMD／Broadcom 路線獨立於 CPO 時程）
- Tier 1「CPO + TGV 雙暴露」標的（[[SiTime]]／[[萬潤]]）的 CPO 段兌現時點推遲、TGV 段不變
- 詳見 [[2026-06-09_SemiAnalysis-800VDC-CPO-延期報告-驗證|SemiAnalysis 延期報告驗證]]

## 相關連結

- [[CPO 供應鏈圖譜]]
- [[TGV 製程鏈圖譜]]
- [[LPKF]]
- [[SiTime]]
- [[萬潤]]
- [[Intel]]
- [[控制點轉移（投資版）]]
- [[sennn.nnna]]
- [[wallstengine]]

---
title: 半導體／算力供應鏈 — Intel TeraFab 與 Musk 晶片
aliases: [Intel TeraFab, Musk Terafab, Tesla AI5 AI6, Intel 18A Terafab]
type: summary
created: 2026-06-04
as_of: 2026-06-04
check_after: 2026-09-15
updated: 2026-06-04
sources:
  - raw/2026-04-11_intel-terafab-musk-chip.md
tags: [半導體, Intel, Tesla, xAI, SpaceX, 晶圓代工, 18A, 美國產能]
thesis_dependency: AI-capex
confidence: medium
---

# 半導體／算力供應鏈 — Intel TeraFab 與 Musk 晶片

> 2026-04-07 公告：Intel 以 $25B 加入 Musk 的 Terafab 計畫，提供 18A 製程；Terrestrial Fab 量產 Tesla AI5/AI6、Orbital Fab 做抗輻射晶片給 SpaceX Starlink。

## 一句話核心

**Musk 用 Intel 18A 把 AI 晶片從 NVIDIA + TSMC 的雙重外購中拉回自家車間**——這是 [[NVDA]] 最大客戶之一啟動「上游自建」的具體一步，也是 Intel 自 IDM 2.0 以來最關鍵的外部錨定客戶。

## 重點摘要

- **計畫主體**：Terafab 由 Tesla、xAI、SpaceX 三方聯合開發，2026-03-21 Musk 公布
- **規模口徑**：「每年生產超過 1 TW AI 算力」——是 capacity 而非單顆 spec，與 [[半導體基礎建設化]] 一致的口徑變遷
- **Intel 角色**：主要晶圓代工夥伴，**$25B** 投入垂直整合晶片廠，提供 18A 製程
- **兩座 Fab**：
  - **Terrestrial Fab**：Tesla AI5 / AI6（人形機器人、自動駕駛）
  - **Orbital Fab**：抗輻射晶片（Starlink AI 資料中心、軌道運算）
- **時程**：AI6 tape-out 2026 年底；量產 2027 年——3 年內無營收，是長線押注

## 產業／供應鏈延伸調查：美國半導體產能政治與 Foundry 競爭格局

### 1. Intel 為何接 Musk？三層意義

| 層次 | Intel 的算盤 |
|---|---|
| **產能填單** | Intel 18A 急需 anchor 客戶證明製程可量產，Musk 是 hyperscaler-grade 訂單 |
| **CHIPS Act 政治對齊** | 美國產能政策（Trump 2.0 工業政策 + CHIPS Act 第二輪）需要旗艦案例 |
| **AI / 國防雙線** | Orbital Fab 抗輻射晶片對接國防需求，Intel 拿到非民用航太晶圓代工入場券 |

### 2. Foundry 三強格局重定價

| 廠 | 旗艦製程 | AI/HPC 客戶 | 戰略風險 |
|---|---|---|---|
| **[[TSMC]]** | N2 (2026 量產)、A16 (2027) | NVDA、AVGO、AMD、Apple、Tesla AI5 上一代 | 地緣 + CoWoS 瓶頸 |
| **Intel** | 18A (2025-2026)、14A (2027+) | Microsoft、Amazon、**Musk Terafab (新)** | 製程良率與 IFS 信任 |
| **Samsung** | SF2 (2025) | 高通、特斯拉 HW4 等 | 良率落後、客戶持續流失 |

**Musk + Intel 18A 案的真實涵義**：Tesla 上一代 AI 晶片（HW3 → AI5）是 TSMC + Samsung 代工，這次明顯把核心 AI 算力訂單分給 Intel——TSMC 不會掉，但「Intel 重新進入 AI 算力代工池」這件事被市場低估。

### 3. 美國半導體產能政治：三條主線

- **CHIPS Act 1.0 兌現中**：TSMC Arizona、Samsung Texas、Intel Ohio 都在 2026-2028 上線，但**良率 + 客戶承諾** 仍是兌現變數
- **CHIPS Act 2.0（傳）**：Trump 政府傳出研擬第二輪，重點在「製造業關鍵零組件本土化」（封裝、光罩、化學品、特氣）
- **晶片出口管制收緊**：對中國半導體裝置、HBM、先進製程晶片出口管制持續加碼——拉動華為昇騰路線（見另一篇 summary）
- **垂直整合大客戶崛起**：Musk Terafab 是繼 Apple（M 系列）、Google（TPU）、Meta（MTIA）、Amazon（Trainium）、Microsoft（Maia）之後第六個**自研 AI 晶片並開始觸碰 fab 層**的超級買家

### 4. 控制點轉移視角

> Musk 繞過 NVIDIA + TSMC 雙重依賴，建立**從晶圓廠到終端產品的完整控制鏈**。

對照組：
- **華為昇騰** 走中芯國際代工的中國垂直整合（受出口管制壓制良率）
- **Musk Terafab** 走 Intel 18A 的美國垂直整合（受 Intel 製程可信度壓制時程）
- **共通邏輯**：AI 算力的戰略價值已超過晶圓代工的比較利益，買家願意自建以鎖控制權

對 [[NVDA]] 的潛在影響：
- **短期（2026-2027）**：無影響，Terafab 連 tape-out 都還沒
- **中期（2028+）**：Tesla / xAI 自研晶片如能跑通工程化，會擠出 NVDA 在 Tesla 體系的 share；但 hyperscaler 整體 GPU 採購仍會增長
- **真風險**：「Musk + Intel 18A 跑通」這件事的訊號價值——意味更多 AI 公司有第二代 fab 選項，鬆動 NVDA + TSMC 雙寡頭

## 與 wiki 概念的深度連結

- **[[跳出個股看三層：產業、目的、供應]]**：本案是「產業」層（AI 算力地緣重組）+「供應」層（自建 fab）兩層同步演化
- **[[CapEx 見頂辯論]]**：Musk $25B + Tesla / xAI 自研 fab 是 CapEx 結構**從 hyperscaler 外購擴散到垂直整合者**的訊號——CapEx 沒見頂，是換主角
- **[[效率→安全切換]]**：自建 fab 不是效率最大化（TSMC 代工成本更低），是控制權與安全——與宋分「效率→安全」世界觀切換一致
- **[[資訊擴散四階段]]**：Intel 重返 AI 算力代工池仍在「機構懷疑」階段，市場給 Intel 的估值未反映此可能
- **[[半導體基礎建設化]]**：1 TW 算力 / year 的口徑是基礎建設語言，不是傳統晶圓廠語言

## 投資啟示（快速）

- **Intel**：若 18A 在 Terafab 案兌現，是 IDM 2.0 重新被定價的最大催化；但 2026-2027 仍是燒錢期
- **[[NVDA]]**：本案的影響是 narrative 而非短期數字，短線無傷
- **[[TSMC]]**：訂單流失有限（Tesla 仍會用 TSMC 多代產品），但 Foundry「唯一選項」地位被稀釋
- **設備鏈**：ASML、AMAT、KLAC、LRCX——Intel 18A 擴產 + Terafab 是設備循環的隱形受惠
- **真正的金針標的**：Foundry 競爭加劇 → 製程化學品 / 光罩 / 特氣國產化（CHIPS Act 2.0 主題）

## 風險與失效情境

1. **Intel 18A 良率不達標**：Terafab 量產時程滑到 2028+
2. **Musk 政治風險**：與政府關係變化影響 CHIPS Act 補貼
3. **Tesla AI5/AI6 工程化失敗**：自研晶片未能跑通實戰，回頭採購 NVDA
4. **抗輻射晶片民用切割**：Orbital Fab 若被軍工專案綁定，民用收入有限

## 相關連結

- [[NVDA]]
- [[TSMC]]
- [[AVGO]]
- [[AMD]]
- [[跳出個股看三層：產業、目的、供應]]
- [[CapEx 見頂辯論]]
- [[效率→安全切換]]
- [[半導體基礎建設化]]
- [[資訊擴散四階段]]
- [[宋分備忘錄 ＃6 — 市場世界觀切換]]

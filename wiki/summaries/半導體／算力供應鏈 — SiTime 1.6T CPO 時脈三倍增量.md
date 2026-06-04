---
title: 半導體／算力供應鏈 — SiTime 1.6T CPO 時脈三倍增量
aliases: [SiTime 1.6T, SITM CPO timing, CPO 時脈三倍]
type: summary
created: 2026-06-04
updated: 2026-06-04
sources:
  - raw/2026-05-07_wallstengine_SiTime-1.6T-CPO時脈元件三倍增量.md
tags: [半導體, SITM, CPO, 光通訊, 時脈元件, 賣水人, 1.6T]
confidence: high
---

# 半導體／算力供應鏈 — SiTime 1.6T CPO 時脈三倍增量

> [[wallstengine]] 2026-05-07 轉述 SiTime 法說口徑：1.6T 振盪器 ASP step-up、CPO 交換器內 timing 內含值最高 3 倍、400G/800G 未來兩年無懸崖。

## 一句話核心

**SiTime（[[SiTime（SITM）]]）是 1.6T 光模組與 CPO 升級曲線上的「光通訊賣水人之中的賣水人」**——不論誰拿下光引擎，模組內都要 timing；單機 timing 內含值最高 3 倍是 BOM 級的結構性放大，不是出貨量單變數成長。

## 重點摘要

- **1.6T 顯著導入 = 2026**：Hyperscaler 頻寬升級驅動，**振盪器 ASP 高於 800G**，是量價齊揚而非價跌量增
- **400G/800G 非 sunset**：「未來至少兩年仍將維持強勁」——無懸崖、雙軌（base 升級 + 1.6T 新增）
- **CPO timing 三倍**：CPO 交換器單機 timing 內含值最高 3x，是模組內部 BOM 結構性放大
- **resilient performance** 關鍵字暗示客戶要的是高階 OCXO / TCXO，不是低階晶振——高 ASP 段

## 產業／供應鏈延伸調查：CPO（共同封裝光學）供應鏈圖譜

CPO 是「**把光引擎從可插拔模組搬進交換 ASIC 旁邊封裝**」的下一代資料中心光通訊架構。1.6T 是 CPO 落地的第一個 high-volume 規格節點。完整供應鏈四層：

| 層 | 角色 | 主要玩家 | 賣水人位階 |
|---|---|---|---|
| **交換 ASIC** | 流量大腦（Broadcom Tomahawk / Jericho、Marvell Teralynx、NVDA Spectrum） | [[AVGO]]、Marvell、[[NVDA]] | 一階（淘金者，輸贏分明） |
| **光引擎 / 矽光晶片** | 把電轉光，CPO 的物理核心 | Intel SiPh、Coherent (COHR)、Lumentum (LITE)、TSMC COUPE、Marvell | 一階（誰拿到 design-in 誰贏） |
| **DSP** | 訊號編碼/補償 | Marvell、Broadcom、MaxLinear | 一階（CPO 可能讓 DSP 失去插槽，反向風險） |
| **時脈元件（timing）** | 同步基準，所有 SerDes 都要 | [[SiTime（SITM）]]、TXC、京瓷、Epson、村田、Renesas | **二階（賣水給所有光引擎玩家）** |
| **封裝 / 測試** | CoWoS-L、CoUPE 級先進封裝 | [[TSMC]]、ASE、Amkor | 二階（與 HBM 共用產能，瓶頸效應） |
| **光纖耦合 / 連接器** | 光纖到晶片對位 | Senko、Sumitomo、US Conec、AFL | 二階 |
| **被動光元件 / EML 雷射** | 光源 | LITE、Coherent、AXT、Macom、Sumitomo | 二階 |
| **電源管理** | 板上電源 / VRM | MPS、ADI、TXN、Vicor | 二階（與類比 IC 受惠重疊） |

**真正的賣水人位置（避開光引擎輸贏判斷的玩家）：**
- **SiTime / TXC / 京瓷**：timing，不管哪家光引擎贏都要買
- **TSMC**：CPO 封裝產能（CoUPE / CoWoS-L），任何 CPO ASIC 都要用
- **MPS / ADI**：電源，類比 IC 結構性低估的延伸（見 [[宋分 #13 — 類比晶片結構性重估]]）

**SiTime 三倍 timing 增量的機制（為何不是線性成長）：**
1. **SerDes 通道數爆炸**：CPO 把 lane 數從 8/16 拉到 32/64+，每個 lane 都要 timing reference
2. **規格升級**：PAM4 + 更高頻 → jitter budget 更嚴 → 從晶振升級到 TCXO / OCXO（ASP 三倍）
3. **冗餘設計**：CPO 整合度更高，單顆 ASIC 故障代價更高 → 冗餘 timing 倍增

這是 [[賣水人選股邏輯]] 中典型「兩個維度同時成長」——量 × 規格升級 = 平方放大。

## 與 wiki 概念的深度連結

- **[[跳出個股看三層：產業、目的、供應]]**：本篇是「供應」層的完整實踐。SiTime 投資論點不是看公司財報，而是看 CPO 供應鏈裡誰避開光引擎輸贏的判斷
- **[[半導體基礎建設化]]**：光通訊從週期性零組件變成 hyperscaler CapEx 的剛性 BOM，timing 是被遺忘的次階受惠
- **[[資訊擴散四階段]]**：CPO timing 仍在「機構→賣方」階段，散戶尚未充分定價
- **[[預期差]]**：市場定 SiTime 為「8% 光模組成長 timing 供應商」，預期差在「CPO 三倍 BOM + 五條獨立放量曲線（衛星、機器人、自駕、PCIe 6.0、server）」
- **[[Forward PE 估值法]]**：若三倍 BOM 兌現，未來兩年 EPS 翻倍以上，當前 PE 是擴張投資型壓縮而非衰退型壓縮

## 投資啟示（快速）

- **直接標的**：[[SiTime（SITM）]]——但留意石英陣營（TXC、京瓷、Epson）是共生而非搶份，整個陣營應為 watchlist
- **配對玩法**：1.6T 光模組廠（COHR、LITE、AXTI）受惠光引擎放量，但有「誰拿到 design-in」的輸贏；SiTime 是不論誰贏都收稅的 hedge
- **長期反向**：PLL 整合進交換 ASIC 是 timing 外購最大威脅（5-10 年），但 OCXO 級高規仍難整合

## 相關連結

- [[SiTime（SITM）]]
- [[wallstengine]]
- [[AVGO]]
- [[NVDA]]
- [[TSMC]]
- [[跳出個股看三層：產業、目的、供應]]
- [[半導體基礎建設化]]
- [[資訊擴散四階段]]
- [[預期差]]
- [[Forward PE 估值法]]

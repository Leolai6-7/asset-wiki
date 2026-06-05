---
title: TGV 製程鏈圖譜
aliases: [TGV 製程鏈, TGV 供應鏈, 玻璃通孔製程, TGV 八站]
type: concept
created: 2026-06-05
updated: 2026-06-05
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [TGV, 玻璃通孔, 半導體, 先進封裝, 供應鏈, 賣水人]
confidence: high
---

# TGV 製程鏈圖譜

**Through-Glass Via（玻璃通孔）**= 貫穿玻璃中介層的互聯通道。製程 8 站，每站都有可投資的賣水人。

本 concept = **TGV 八站分工 + 賣水人位階表**，跟 [[CPO 供應鏈圖譜]] 並列為「賽道供應鏈映射方法論」。

## 為什麼 TGV 對 Leo 重要

- 對標 [[HBM iPhone moment]]——從週期商品 → AI 基礎設施元件
- 終端：Intel EMIB / AMD / Broadcom 的 data center AI ASIC
- **2026 樣品驗證 → 2027-2028 量產** = [[市場四階段]] 從「懷疑期」→「驗證期」
- 跟 [[CPO 供應鏈圖譜]] 是補充關係（CPO 解光通訊、TGV 解封裝互聯）

## 八站圖譜

| 站 | 內容 | 國際大廠 | 台股候選 |
|---|---|---|---|
| **1. 雷射改質 / 雷射打孔** | 飛秒雷射標記孔位（不是直接打孔） | LPKF (LIDE, 德國)、Trumpf、Disco | [[鈦昇]]（雷射改質）、[[雷科]]（雷射打孔）、[[東捷]]（聯盟） |
| **2. 化學蝕刻** | 把標記處融掉 | AMAT、TEL、LAM | [[辛耘]]（CoWoS 三傑）、[[弘塑]]、[[敘豐]]（VSP） |
| **3. 超音波清洗 + AOI** | 移除碎屑 + 孔距測量 | — | [[弘塑]]、[[辛耘]] |
| **4. PVD sputter（種子層）** | 鈦/鉻黏著層 + 銅靶材 | AMAT、ULVAC、Veeco | [[東捷]]（透過富臨整合） |
| **5. 銅電鍍** | 對接 → 填滿 | AMAT、Atotech (→MKS)、Ebara | [[弘塑]] |
| **6. AXI（3D X-Ray CT）** ⭐ **sennn.nnna 說「最重要檢測」** | 三維非破壞檢測 | YXLON (→Comet)、Nikon、Zeiss | [[德律]]（與 OmniMeasure 合作） |
| **7. CMP 研磨 + RDL** | 研磨入口銅殘留 + 重佈線 | AMAT、Ebara、Entegris | [[弘塑]] |
| **8. 雷射隱形切割** | 紅外光雷射 + 半導體膠帶 | Disco（壟斷）、Tokyo Seimitsu | [[雷科]]（挑戰 Disco） |

## 賣水人位階（從「押路線」到「中性受惠」）

```
高敏感（押誰贏） ────────────────────────────► 低敏感（誰贏都受惠）

[[鈦昇]] 雷射改質（押 LPKF LIDE 路線）
    │
[[雷科]] 雷射打孔（押日系直接打孔路線）
    │
[[敘豐]] VSP 蝕刻（押載板→玻璃延續）
    │
[[東捷]] 整線聯盟（押東捷+志聖+富臨）
    │
[[德律]] AXI 檢測（中性受惠但 TGV 純度低）
    │
[[辛耘]] 化學蝕刻（中性賣水人 + CoWoS 現金流）
    │
[[弘塑]] 跨蝕刻+電鍍+CMP（中性賣水人 + 化學品消耗品）
    │
**設備鏈**（ASML、AMAT、Disco）— 任何 fab 擴產都吃
```

## 兩個 anchor 時點（值得追蹤）

| 時點 | 事件 | 受惠 |
|---|---|---|
| **2026 H2** | Intel Clearwater Forest（Xeon 6+）採用玻璃核心基板 + EMIB 量產 | [[鈦昇]]（Intel design-in）、[[東捷]] |
| **2026 Q4** | NVIDIA 終端產品（含 [[雷科]] 認證設備） | [[雷科]]、[[德律]] |

## 三大風險（TGV 整體賽道）

| 風險 | 影響 |
|---|---|
| **Hybrid Bonding（銅柱巨轉）替代** | 跨過 TGV 直接 chip-to-chip → TGV TAM 縮 |
| **TSMC CoPoS 走不同鑽孔工法** | [[鈦昇]] LPKF 路線直接受傷 |
| **2026 樣品驗證不及預期** | 整個 89% CAGR 敘事推回起點 |

## 跟其他 wiki 概念連結

- [[CPO 供應鏈圖譜]]：賽道供應鏈映射的姊妹篇
- [[HBM iPhone moment]]：估值框架轉換的同型案例
- [[半導體基礎建設化]]：TGV 是其中一個 sub-thesis
- [[賣水人選股邏輯（投資版）]]：本 concept 是經典應用
- [[控制點轉移（投資版）]]：Intel/AMD 自建中介層 = 控制點往垂直整合移
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]：本 concept 第 1 站的深度展開
- [[玻璃基板與 FOPLP 賽道]]：本 concept 的上位賽道 thesis

## 待 ingest 延伸

- 國際大廠 entity：LPKF（德國，鈦昇對手）、Disco（雷科切割對手）、AMAT、TEL
- 台股漏網：群創（FOPLP 線轉型）、欣興/南電/景碩（ABF 載板廠）
- 已補：[[萬潤]]（6187，CoWoS 三傑第三家，WoS 後段點膠+散熱+AOI 近壟斷）— 對 TGV 中性、TGV 完成後仍要回到後段過萬潤機台
- 玻璃材料廠已 ingest：[[Corning]]、[[AGC]]、[[SCHOTT]]
- ⭐ **Absolics（SKC 子公司）**：Georgia 廠 2026 **全球首條商業化量產玻璃中介層** — 重要漏網
- Samsung SEMCO（2027 量產目標）、LG Innotek（Gumi pilot）

## llm-wiki 跨庫對應

- llm-wiki [[AI 供應鏈]]：全鏈條總覽視角
- llm-wiki [[CPO（共同封裝光學）]]：CPO 工程定義（透過 [[TGV × CPO 依賴圖]] 連通）
- 詳見 [[跨庫對照（asset-wiki ↔ llm-wiki）]]

## 相關連結

- [[CPO 供應鏈圖譜]]
- [[HBM iPhone moment]]
- [[半導體基礎建設化]]
- [[賣水人選股邏輯（投資版）]]
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]
- [[玻璃基板與 FOPLP 賽道]]
- [[鈦昇]]、[[雷科]]、[[弘塑]]、[[辛耘]]、[[德律]]、[[東捷]]、[[敘豐]]
- [[sennn.nnna]]
- [[Intel]]

---
title: SemiAnalysis 800VDC 與 CPO 延期報告 — 驗證與對撞分析
type: summary
created: 2026-06-10
updated: 2026-06-10
sources:
  - raw/2026-06-09_SemiAnalysis-800VDC-CPO-延期-機構報告中文摘要.md
tags: [SemiAnalysis, 800VDC, CPO, 延期, Feynman, COUPE, 良率, Mt. Diablo, 驗證型 ingest, CPO 測試, 預期差]
confidence: medium
---

# SemiAnalysis 800VDC＋CPO 延期報告 — 驗證與對撞分析（#P1）

**性質**：驗證型 ingest——Leo 提供機構報告中文摘要、deep-research（18 來源／89 claims）+ 補查驗證後落地。

## 一句話

> 報告真實存在（2026-06-09 機構限定、Computex 台北 channel checks）、**CPO 延期是 SemiAnalysis 既有立場的加碼而非轉向**（2026-01《CPO Book》已寫 Feynman 才是 CPO 注入點）；800VDC 部分一半是自家 5 月基線重述、新增量是「hyperscaler 抵制單端 800V」；中文摘要忠實度高（FPS／鴻勁／AAOI 歸類全部驗證屬實）。

## 報告身份（三份文件）

| 文件 | 日期 | 性質 | 角色 |
|---|---|---|---|
| 《CPO Book》 | 2026-01-01 | 付費公開 | CPO 延期立場源頭：「Feynman generation = focal point for CPO injection、Rubin Ultra 2027 too ambitious」 |
| 《Inside the 800VDC Revolution – Part 1》 | 2026-05-26 | 半公開 | 四階段時間表：Phase 2（800V 原生含 Kyber 放量）2027/2028、Phase 3（全廠）late 2028/2029、SST 規模採用 2029 初；winners/losers 在付費牆後 |
| **機構限定 bearish report** | **2026-06-09 或稍早** | 機構 only | Computex channel checks、觸發 6/9 美股光通訊賣壓（AAOI -14% 領跌、SeekingAlpha 歸因） |

## 逐條 verdict（四級標記）

### 800VDC

| Claim | Verdict | 關鍵證據 |
|---|---|---|
| Rubin tray 仍 50VDC 輸入、800V 非必要 | ✅ | SemiAnalysis 2026-02-25：VR NVL72 tray 經 busbar 吃 50VDC；Part 1：兩種 800V 架構都保留 800V→~50V 級 |
| 原生單端 800V 量產推遲 2028+ | 🟡 | 與 Part 1 基線方向一致（液冷 VR Ultra 版 late-2026 才 sampling）；「比基線再延」增量無公開佐證 |
| Hyperscaler 抵制 800VDC | 🟡 **過度簡化** | OCP Mt. Diablo（M$+Meta+Google、2026-03-01 生效 v0.7.0）= ±400V 三線制**但明文含 2-wire 800V 選項**——抵制的是 NVIDIA 單端 800V、不是反高壓 = 「**誰的 800V**」標準之爭（[[接口控制權]]） |
| ±400VDC 照常 2H26、sidecar 年底訂單 | ✅ 規格層／⚪ 訂單層 | 規格活躍演進 v0.5.0→v0.7.0、sidecar 正式定義 800kW-1MW+ |
| 低壓設備延壽 | 🟡 | Part 1 自家預測 power rack 市場 2028 峰值 ~$11B（過渡期生意）、SST ~$13B 在 2030 |

### CPO

| Claim | Verdict | 關鍵證據 |
|---|---|---|
| Scale-up CPO 2029+ 綁 Feynman | ✅ **3-0 全票** | 《CPO Book》原文雙引述（對抗驗證唯二全票通過） |
| 良率數學 0.95³²≈19%、需 99.5%→85% | 🟡 | 數學驗算正確；32 engine × 3.2T=102.4T 被 2 月文確認；「焊後壞一顆=全包報廢」=官方 X thread 立場；95%／99.5% 具體數字 ⚪ |
| Spectrum-6（SN6810）插損 >3.5dB、根因未明 | ⚪ | 純 channel check；產品識別 ✅（SN6810=102.4T、128×800G）；「Spectrum 5」命名公開對不上 ⚠️ |
| Quantum X3450 每模組 3 顆 COUPE | 🟡 | 《CPO Book》：Q3450 全機 72 顆 OE×1.6T＝24 個 OSA 模組×3 顆——OSA 粒度上成立；出貨 baseline：NVIDIA 2025-08 官方已推到 early 2026 |
| COUPE gen1 1.6T → gen2 3.2T | ✅ | 雙文確認 |
| 銅纜＋可插拔主流至 2028 | ✅ | SemiAnalysis 2 月：SN6600 可插拔版會比 CPO 版普及 |

### Read-across 個股

| 名字 | Verdict | 重點 |
|---|---|---|
| [[Forgent Power Solutions]] FPS | ✅ 真公司 | NYSE 新掛牌、MGM/PwrQ/States/VanTran 母品牌、低壓配電 engineered-to-order、~$18B 市值（⚠️ P/S ~15x） |
| [[鴻勁 7769]] = Hon Precision | ✅ | 全球 SoC FT 分選機龍頭、2025 營收 302.7 億 +166%、下一步攻 CPO 測試 |
| [[Teradyne]] Photon 100 | ✅ 產品／⚪ 認證 | 2026-03-17 OFC 發布、wafer／discrete OE／co-packaged 三段 insertion；「輝達認證領先者」無公開佐證 |
| [[致茂 2360]] | ✅ | 矽光子測試=成長引擎；產業共識「CPO 瓶頸在測試不在製造」（iST） |
| [[AAOI]] | ⭐ 活案例 | 6/9 盤中 **-14% 領跌**——但主業 800G 可插拔邏輯上受惠 CPO 延期 = [[預期差]] 板塊 beta 錯殺 candidate |
| A 股光模組 | 🟡 | 旭創 6/5 午後 -8%、新易盛 -4%+；亞洲先跌（6/5）→ 美股後跌（6/9）、吻合機構圈先行流通 |

## 與 [[800V HVDC 灰白區重劃（物理鐵壁論）]] 的同日多空對撞

FOMO SOC（2026-06-09、多方、物理層）vs SemiAnalysis（2026-06-09、空方、時程層）——**相容不互斥**：物理鐵壁（元問題 A）沒被推翻、變的是時程預期（元問題 B）與敘事溢價（元問題 C）。FOMO SOC 概念內建風險 #1「中間態 400V 取代 800V → SST 受惠者降級」**被逐字啟動**；其自警惕「不會一蹴而就」命中。

**五軸第一軸「路線敏感（逆向）」最強活驗證**：多空雙報告同日點名同一批人——Eaton／Schneider／ABB／Vertiv／Infineon／MPS／MLCC（村田・國巨・TDK）。多空雙方都說你受惠 = 「不論架構怎麼變都收錢」的定義本身。

## 對 wiki 的校準（#P1 落地清單）

- **強化**：[[TXC]] 21（可插拔延壽+旭創/新易盛=拉貨方）、[[Innolight]]／[[Eoptolink]]／[[Amphenol]]／[[MACOM Technology]]／[[Marvell]]／[[Tower Semiconductor]]、[[Vertiv]] 22（雙贏）、[[AI infra CapEx 三階段論]] 第三階段可插拔版
- **時程校準**：[[CPO 供應鏈圖譜]]（2029+／良率 gate／第 9 測試層）、[[TGV × CPO 依賴圖]]（CPO leg 推遲）、[[SiTime]] 20（CPO 三倍 BOM 段推遲）、[[Lumentum]]／[[Coherent]] 19（CPO 溢價修正、本業受惠、NVDA $2B=延後≠取消）
- **Flag**：[[Navitas Semiconductor]] 19 → thesis-dependent flag（催化劑 2028+、可投資 17-19 區間）；[[Wolfspeed]] 已 NOT-INVESTABLE 再添一刀
- **新建**：[[Teradyne]] 19／[[鴻勁 7769]] 18／[[致茂 2360]] 18／[[Forgent Power Solutions]] 14 = **CPO 測試／過渡期受惠 cluster**（跟 [[TGV 檢測分類 taxonomy]] AXI＝[[德律]] 同構：良率地獄裡賣檢測）
- **KOL 體系**：SemiAnalysis 立場一致（1 月空 CPO 時程）+ 實地 channel check + 機構限定→媒體報導 = [[資訊擴散四階段]] 第一→第二階段交界訊息

## 驗證強度自報

Rate limit 致對抗投票僅完成 2 條（均 3-0 通過）；其餘 claim 為一手來源引文支撐、未經三票對抗。表中 ✅ 為基於原文引述之人工判定。

## 主要來源

- [SemiAnalysis CPO Book（2026-01-01）](https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling)
- [Inside the 800VDC Revolution – Part 1（2026-05-26）](https://newsletter.semianalysis.com/p/inside-the-800vdc-revolution-part)
- [Vera Rubin Extreme Co-design（2026-02-25）](https://newsletter.semianalysis.com/p/vera-rubin-extreme-co-design-an-evolution)
- [OCP Diablo 400 v0.7.0 spec](https://www.opencompute.org/documents/ocp-specification-diablo-400-v0-7-0-final-pdf)
- [NVIDIA CPO 官方 blog（2025-08）](https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/)
- [SeekingAlpha：AAOI 領跌（2026-06-09）](https://seekingalpha.com/news/4601927-applied-optoelectronics-leads-networking-stocks-down-following-report-on-cpo-rollout-delay)
- [Teradyne Photon 100（2026-03-17）](https://investors.teradyne.com/news-events/press-releases/detail/436/teradyne-introduces-photon-100)
- [Forgent Power Solutions 官網](https://www.forgentpower.com/)
- [鴻勁 IPO（數位時代）](https://www.bnext.com.tw/article/84909/hon-precision-ipo)
- [iST：CPO 瓶頸在測試](https://www.istgroup.com/en/tech_20251216_siph-cpo/)
- [SemiAnalysis X：CPO 測試 thread（2026-03-26）](https://x.com/SemiAnalysis_/status/2037213323683319873)
- [旭創 6/5 大跌（新浪）](https://finance.sina.com.cn/money/fund/etf/2026-06-05/doc-iniaiusq2853891.shtml)

## 相關連結

- [[800V HVDC 灰白區重劃（物理鐵壁論）]]（同日多空對撞）
- [[CPO 供應鏈圖譜]]／[[TGV × CPO 依賴圖]]／[[NVDA 網路 stack map]]
- [[Teradyne]]／[[鴻勁 7769]]／[[致茂 2360]]／[[Forgent Power Solutions]]（#P1 新建）
- [[TXC]]／[[SiTime]]／[[Lumentum]]／[[Coherent]]／[[AAOI]]／[[Navitas Semiconductor]]／[[Vertiv]]（#P1 校準）
- [[接口控制權]]／[[預期差]]／[[資訊擴散四階段]]／[[結構影響分 vs 可投資五軸分（雙評分體系）]]／[[五軸分數 confidence gate]]
- [[賣水人選股邏輯（投資版）]] 第十九波
- [[FOMO SOC]]（KOL 對照）

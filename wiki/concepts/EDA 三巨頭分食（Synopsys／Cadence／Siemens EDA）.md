---
title: EDA 三巨頭分食（Synopsys／Cadence／Siemens EDA）
aliases: [EDA 三巨頭, EDA 三巨頭分食, EDA 寡占, EDA 全球市佔, EDA Big 3, Synopsys Cadence Siemens EDA]
type: concept
created: 2026-06-09
as_of: 2026-06-09
check_after: 2026-10-15
updated: 2026-06-09
sources:
  - WebSearch 2026-06-09（Gartner / IDC EDA 全球市佔報告 + Synopsys FY2025 法說 + Cadence FY2025 法說 + Siemens Digital Industries FY2025 + NVDA AI Foundation Models for Chip Design）
tags: [Meta 框架, EDA, 寡占, 賣水人之中的賣水人, AI 自動設計, 半導體設計, 控制點轉移, AI Copilot, AI agent for chip design]
thesis_dependency: none（可遷移方法）
confidence: medium
---

# EDA 三巨頭分食（Synopsys / Cadence / Siemens EDA）

## 一句話

> EDA 賽道 ~USD $15-18B（2025）+ CAGR 12-15%（AI 晶片驅動）+ 三巨頭 [[Synopsys]] ~33% + [[Cadence]] ~28% + [[Siemens]] EDA ~17% = **合計 78% 寡占**——所有 fab / fabless / IDM 晶片設計都繞不開三家、是「**賣水人之中的賣水人**」架構級 anchor。

## 三家差異化分工

| 維度 | [[Synopsys]]（SNPS）| [[Cadence]]（CDNS）| [[Siemens]] EDA |
|---|---|---|---|
| **全球 EDA 市佔（2026 推估）** | **~33%（#1）** | **~28%（#2）** | **~17%（#3）** |
| **核心強項** | **RTL synthesis / verification / DesignWare IP 業界標準** | **Custom IC / analog / Spectre simulator / Tensilica DSP IP** | **PCB design Xpedition / Calibre 驗證 / Mentor 工業軟體加值** |
| **AI 自動設計 first-mover** | **DSO.ai / AI.Copilot first-mover** | **Cerebrus / Verisium / Allegro X AI 跟進 first-mover** | Aprisa AI 跟進中 |
| **multiphysics 整合** | **✅ Ansys USD $35B 併購（2024-2025）** | ✅ BETA CAE 2024 Q4 + Hexagon D&E 2025（規模小於 SNPS） | ✅ Siemens 內部 Simcenter + NVDA Omniverse 工業數位孿生 |
| **跨產業擴張** | ✅✅✅（晶片 + 航太 + 汽車 + 工業） | ✅✅✅（晶片 + 航太 + 汽車 + 工業 + system simulation） | ✅✅✅（Siemens Xcelerator 工業生態 + NVDA Omniverse） |
| **IP 強項** | **DesignWare（USB / PCIe / DDR / Ethernet / SerDes 業界標準）** | **Tensilica DSP（audio / 通訊 / 影像 DSP 標準）+ Denali memory IP** | Mentor 較弱（Siemens 工業軟體強） |
| **市值（2026 推估）** | USD ~$90-110B | USD ~$85-105B | （Siemens 子公司、不獨立上市） |
| **Forward PE** | ~35-45x | ~40-50x（略貴） | — |
| **訂閱制收入** | ✅✅ ~70%+ | ✅✅ ~70%+ | — |
| **五軸（25 分制）** | **24/25** | **22/25** | （非獨立上市） |
| **歷史脈絡** | 1986 成立、納斯達克 | 1988 成立（SDA Systems + ECAD 合併）、納斯達克 | **2017 Siemens USD $4.5B 收購 Mentor Graphics 改名 Siemens EDA** |

### Synopsys 33%：digital flow + IP 廣度 + AI Copilot first-mover

**最強核心**：
- **RTL synthesis**：Design Compiler / Fusion Compiler 業界標準
- **Place & Route**：IC Compiler II / Fusion Compiler
- **Verification**：VCS simulator + Verdi debug 業界標準
- **DFT / signoff**：TetraMAX + PrimeTime 業界標準
- **DesignWare IP**：USB / PCIe / DDR / Ethernet / SerDes 業界標準授權
- **Ansys multiphysics**：USD $35B 巨型併購（業界最大 EDA 整合案）
- **DSO.ai / AI.Copilot**：生成式 AI 自動設計 first-mover

**TAM 槓桿**：Ansys 整合後跨晶片 / 航太 / 汽車 / 工業 multiphysics 擴張

### Cadence 28%：Custom IC + analog + Spectre + Tensilica DSP

**最強核心**：
- **Custom IC + analog 設計**：Virtuoso 業界標準（analog / mixed-signal / Custom IC 不可繞過）
- **Circuit simulator**：Spectre 業界標竿（analog IC 設計師必用）
- **Emulation**：Palladium 業界標竿（vs SNPS ZeBu）
- **DSP IP**：Tensilica audio / 通訊 / 影像 DSP 標準（Qualcomm / Apple / NVDA / Samsung / MediaTek 全授權）
- **Memory IP**：Denali DDR / LPDDR / HBM memory subsystem 業界標準之一
- **System simulation**：BETA CAE（2024 Q4）+ Hexagon D&E（2025）+ Allegro PCB + Spectre 整合
- **Cerebrus / Verisium / Allegro X AI**：AI agent for chip design 跟進 first-mover

**TAM 槓桿**：BETA CAE + Hexagon D&E 整合後跨晶片 / 航太 / 汽車 / 工業 system simulation 擴張（但規模小於 SNPS Ansys $35B）

### Siemens EDA 17%：Mentor + PCB Xpedition + 工業數位孿生

**最強核心**：
- **PCB design**：Xpedition 業界標準（vs CDNS Allegro PCB 雙頭）
- **Calibre DRC/LVS**：驗證流程業界標準（fab 認證標準工具）
- **Catapult HLS**：high-level synthesis 業界領先
- **整合 Siemens Xcelerator 工業軟體 + NX CAD + Teamcenter PLM + Simcenter multiphysics**
- **NVDA Omniverse + Siemens Xcelerator 合作**（2024-03 GTC）= **工業數位孿生 first-mover**
- **Aprisa AI**：跟進中 AI 自動設計

**TAM 槓桿**：跟 Siemens Digital Industries Software（PLM + CAD + low-code）整合 + 工業 metaverse 跨界 AI

**戰略劣勢**：vs SNPS + CDNS 雙頭壟斷、規模 / 設計工具廣度 / AI 自動設計都落後

## 客戶通常雙頭採用（SNPS + CDNS）

| 設計階段 | 主要工具廠 | 主要工具 |
|---|---|---|
| **RTL synthesis** | SNPS 主 / CDNS 次 | Design Compiler / Genus |
| **Place & Route** | SNPS 主 / CDNS 次 | IC Compiler II / Innovus |
| **Verification** | SNPS 主 / CDNS 次 / Siemens 部分 | VCS / Xcelium / Questa |
| **DFT / signoff** | SNPS 主 / CDNS 次 | TetraMAX / Modus |
| **Custom IC + analog** | **CDNS 主 / SNPS 次** | **Virtuoso / Custom Compiler** |
| **Circuit simulator** | **CDNS 主 / SNPS 次** | **Spectre / HSPICE** |
| **Emulation** | **CDNS 主 / SNPS 次** | **Palladium / ZeBu** |
| **PCB design** | **Siemens 主 / CDNS 次** | **Xpedition / Allegro** |
| **DRC/LVS 驗證** | **Siemens 主 / SNPS + CDNS 次** | **Calibre / IC Validator / Pegasus** |
| **HLS（high-level synthesis）** | **Siemens 主 / SNPS 次** | **Catapult / Stratus** |
| **DSP IP** | **CDNS 主 / SNPS 次** | **Tensilica / ARC** |
| **Memory IP** | SNPS / CDNS 雙頭 | DesignWare / Denali |
| **SerDes / PCIe / Ethernet IP** | **SNPS 主 / CDNS 次** | **DesignWare / 對應 CDNS IP** |

→ **沒有任何 fabless / IDM 只用一家 EDA 廠**——SNPS + CDNS 必雙頭採用、Siemens EDA 在 PCB + DRC/LVS + HLS 補位、三家形成完整設計流程閉環

## EDA TAM + 增速

| 年份 | EDA 全市場 | CAGR | 驅動 |
|---|---|---|---|
| **2024** | USD ~$14-15B | — | AI 晶片設計 ramp |
| **2025** | USD ~$15-18B | +12-15% | AI 晶片設計 + 自研 ASIC ramp |
| **2030E** | USD $30B+ | +12-15% CAGR | AI agent 自動設計 + multiphysics 擴張 + 跨產業 |

**TAM 翻倍可能**：純 EDA $15-18B → AI agent 自動設計可能再加 $5-10B（SNPS DSO.ai + CDNS Cerebrus + Siemens Aprisa AI 跟進三家共擴大）

## NVDA AI Foundation Models for Chip Design（2024 GTC）

**2024 GTC NVDA 公告**：
- **NVDA + SNPS + CDNS + Siemens EDA 三家都在做 AI agent for chip design 合作**
- NVDA 提供 **AI Foundation Models（NeMo / NIM）**
- EDA 廠提供 **工具整合**：SNPS DSO.ai / AI.Copilot / CDNS Cerebrus / Siemens EDA Aprisa AI
- 三家**技術路線競賽**：誰能讓 fabless / IDM 客戶用 AI agent 把晶片設計時間從 6-12 個月縮到 2-3 個月

⭐ **NVDA 是 EDA 三巨頭的「**共同上游 AI 模型供應商**」**——不是 EDA 競爭者、是 EDA 賦能者

⭐ **NVDA 自家晶片設計（Rubin / Vera / Blackwell）也用 SNPS + CDNS 雙頭工具 + Cerebrus / DSO.ai AI agent**

## EDA 是「賣水人之中的賣水人」結構性護城河

### 為什麼 EDA 是 chokepoint？

1. **任何晶片設計都繞不開**：fabless（NVDA / AMD / Apple / Qualcomm / MediaTek / Broadcom）+ IDM（Intel / Samsung / TI / Infineon）+ hyperscaler 自研 ASIC（Google TPU / AWS Trainium / Microsoft Maia / Meta MTIA）+ 中國自研（華為昇騰 / 寒武紀 / 海光）全部用 SNPS + CDNS 雙頭
2. **fab PDK 必支援 SNPS + CDNS**：TSMC 2nm / Samsung 2nm / Intel 18A / GlobalFoundries 22FDX 全 PDK 都用 SNPS + CDNS 雙頭、不雙頭認證 fab 工藝不算「ready」
3. **設計流程 deep integration**：fabless / IDM 設計流程 30+ 年累積、切換成本極高
4. **開源 EDA 仍是 RISC-V 社群實驗**：商業 fab / fabless 仍 100% 用 SNPS + CDNS（驗證 / DFT / sign-off 工具開源無法替代）
5. **訂閱制 + maintenance recurring**：70%+ 毛利、年金型 ARR

### 跟其他賣水人對比

| 賣水人類型 | 代表 | 控制點 | 戰略 |
|---|---|---|---|
| **EDA 設計工具** | **SNPS + CDNS + Siemens EDA** | **任何晶片設計都要用** | 訂閱制 + IP 授權 + AI agent |
| **微影設備** | ASML | 任何 fab 擴產都要 | EUV / High-NA EUV 壟斷 |
| **切割設備** | [[Disco Corp]] | 任何先進製程都要 | 切割研磨壟斷 + 耗材年金 |
| **矽晶圓** | [[信越化學]] + [[SUMCO]] | 任何 fab 都要矽 substrate | 雙頭壟斷 |
| **光阻劑** | [[信越化學]] + JSR + TOK | 任何曝光製程都要 | 三強分食 |
| **被動元件** | [[村田 Murata]] | 任何電子產品都要 | 全鏈寡占 |
| **R&D 公共財** | [[Imec]] | 任何先進製程突破前都要 R&D | pre-competitive 公共平台 |

→ **EDA 在「設計層」是最深的 chokepoint**——比矽晶圓 / 光阻劑 / 切割設備更上游（晶片還沒生產就先用 EDA 設計）、比 Imec R&D 更實作（Imec 是 pre-competitive R&D、SNPS + CDNS 是商業生產用工具）

## 三巨頭客戶矩陣

| 客戶 | SNPS | CDNS | Siemens EDA |
|---|---|---|---|
| **NVDA**（Rubin / Vera / Blackwell） | ✅✅✅ 主導 | ✅✅✅ Custom IC + analog 部分主導 | ✅ PCB + DRC/LVS |
| **AMD**（MI300 / MI400 / Genoa） | ✅✅✅ 主導 | ✅✅ analog mixed-signal 部分主導 | ✅ PCB + DRC/LVS |
| **AVGO**（Tomahawk 5/6） | ✅✅ 主導 | ✅✅ analog + DSP 部分 | ✅ PCB + DRC/LVS |
| **Marvell**（DSP / Inphi） | ✅✅ 主導 | ✅✅ DSP IP（Tensilica） | ✅ PCB + DRC/LVS |
| **Apple**（M / A 系列） | ✅✅ 部分 | ✅✅ analog / DSP / Custom IC 部分 | ✅ PCB |
| **Qualcomm**（Snapdragon） | ✅✅ 部分 | ✅✅✅ **Tensilica DSP IP 重度授權** | ✅ PCB |
| **Intel**（Core / Xeon / Gaudi 3） | ✅✅ 部分 | ✅✅ Custom IC + analog 部分 | ✅✅ Calibre |
| **Google TPU** | ✅✅✅ | ✅✅ | ✅ PCB |
| **AWS Trainium** | ✅✅✅ | ✅✅ | ✅ PCB |
| **Microsoft Maia** | ✅✅✅ | ✅✅ | ✅ PCB |
| **Meta MTIA** | ✅✅✅ | ✅✅ | ✅ PCB |
| **Samsung**（Exynos / Foundry） | ✅✅ | ✅✅ | ✅✅ Calibre |
| **MediaTek**（Dimensity） | ✅✅ | ✅✅ | ✅ PCB |
| **TSMC**（OIP 認證） | ✅✅✅ PDK | ✅✅✅ PDK | ✅✅ DRC/LVS |
| **GlobalFoundries**（22FDX / SiPho） | ✅✅ PDK | ✅✅ PDK | ✅ Calibre |
| **華為昇騰**（受 BIS 限制）| ⚠️ 限制中 | ⚠️ 限制中 | ⚠️ 限制中 |
| **寒武紀 / 海光**（中國 AI 晶片）| ⚠️ 限制中 | ⚠️ 限制中 | ⚠️ 限制中 |

⭐ **2024-2025 美 BIS 對中國 fabless 限制 EDA 出口**：CDNS + SNPS + Siemens EDA 對中國市場限制中、是三家共同風險（但 7B 全球市場中、中國占 ~10-12%、影響可控）

## 三巨頭 vs 開源 EDA

| 維度 | SNPS + CDNS + Siemens EDA | 開源 EDA（Yosys / Berkeley ABC / iVerilog / KLayout）|
|---|---|---|
| **覆蓋範圍** | **完整設計流程**（synthesis + P&R + verification + DFT + signoff + IP）| 部分（synthesis + simulation） |
| **fab PDK 認證** | **全 fab PDK 必認證** | RISC-V 社群部分支援 |
| **客戶** | **fabless + IDM + hyperscaler 100% 採用** | RISC-V 社群 + 學術界 |
| **驗證 / DFT / sign-off** | ✅✅✅ 必用 | ❌ 不夠強 |
| **AI 自動設計** | DSO.ai / Cerebrus / Aprisa AI | 弱 |
| **訂閱制 vs 免費** | 訂閱制 + maintenance | 免費 |

→ **開源 EDA 結構性威脅低**——商業 fab / fabless 仍 100% 用 SNPS + CDNS（驗證 / DFT / sign-off 工具開源無法替代）

## 跟其他 wiki 概念連結

- [[賣水人選股邏輯（投資版）]]：**「架構級『賣水人之中的賣水人』第二陣營 anchor」**（SNPS 24 + CDNS 22 + Imec 24 特殊評估三巨頭）
- [[控制點轉移（投資版）]]：EDA 是晶片設計 chokepoint、SNPS + CDNS 雙頭壟斷 EDA 全行業流量
- [[半導體基礎建設化]]：EDA 是「全行業設計基礎建設」、跟 ASML 微影設備 / 信越化學 / SUMCO 矽晶圓 / Disco Corp 切割設備並列「半導體基礎建設五大 chokepoint」
- [[Bottleneck Theory（瓶頸論）]]：設計鏈 chokepoint
- [[NVDA]]：AI Foundation Models for chip design（NeMo / NIM）+ EDA 廠工具整合
- [[Synopsys]]：EDA 全球 #1 anchor entity
- [[Cadence]]：EDA 全球 #2 anchor entity
- [[Siemens]]：含 Siemens EDA 第三 + NVDA Omniverse 工業數位孿生
- [[AI infra CapEx 三階段論]]：EDA 跨三個階段都受惠
- [[開源作為武器（投資版）]]：⚠️ EDA 三巨頭都是閉源 / 訂閱制、跟開源 EDA 對比反向
- [[公司 Entity 模板（Step 1-3 三段式）]]：三家 entity 都套用三段式

## 待 ingest 延伸

- 三巨頭跟自研 ASIC（hyperscaler）關係深化
- 中國 EDA 廠（華大九天 / 概倫電子 / Empyrean）跟三巨頭 chokepoint 對比
- AI agent for chip design 技術細節：Cerebrus vs DSO.ai vs Aprisa AI 對比
- EDA 廠跟 fab PDK 共生關係 + TSMC OIP 標準
- EDA 廠 + 自研 ASIC 訂單能見度 + AI 晶片設計週期縮短趨勢

## 相關連結

- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[半導體基礎建設化]]
- [[Bottleneck Theory（瓶頸論）]]
- [[Synopsys]]
- [[Cadence]]
- [[Siemens]]
- [[NVDA]]、[[AMD]]、[[AVGO]]、Marvell、Apple、Qualcomm
- [[TSMC]]、[[Samsung Electronics]]、[[Intel]]、[[GlobalFoundries]]
- [[Imec]]
- [[AI infra CapEx 三階段論]]
- [[開源作為武器（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]

## Sources

- [Gartner / IDC EDA 全球市佔報告（業界推估，2025-2026）]
- [Synopsys FY2025 法說 + Ansys USD $35B 併購公告](https://news.synopsys.com)
- [Cadence FY2025 法說 + BETA CAE / Hexagon D&E 收購公告](https://www.cadence.com/en_US/home/company/newsroom/press-releases.html)
- [Siemens Digital Industries Software portfolio + Siemens EDA](https://www.sw.siemens.com/en-US/)
- [NVDA AI Foundation Models for Chip Design 2024 GTC](https://blogs.nvidia.com/blog/chip-design-ai/)
- [TSMC OIP（Open Innovation Platform）認證](https://www.tsmc.com/english/dedicatedFoundry/services/oip)

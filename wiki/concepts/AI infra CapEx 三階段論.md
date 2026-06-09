---
title: AI infra CapEx 三階段論
aliases: [CapEx 三階段, AI 基礎建設三階段, 三階段論]
type: concept
created: 2026-06-08
updated: 2026-06-09
last_minor_update: 2026-06-09 中國光模組鏈條（Innolight + Eoptolink 雙頭）補位 + 2026-06-08 IQE entity 補完
as_of: 2026-06-09
check_after: 2026-12-09
expires_on: 2027-12-31
sources:
  - raw/2026-06-08_Leo-AI-infra-CapEx-三階段論-1.6T-光模組-InP.md
tags: [Meta 框架, CapEx, 階段論, AI 基礎建設, 光通訊, InP, Spectrum-X]
confidence: medium
---

# AI infra CapEx 三階段論

Leo 2026-06-08 提出的 framework：**追蹤 $5.3 兆 AI infra CapEx 的傳導順序**——從 CSP 講 CapEx → NVDA 設備落地 → 上游材料 + 光通訊爆掉。

→ 對應[[資訊擴散四階段]]（散戶/機構視角）+ [[市場四階段：懷疑／驗證／共識／反轉]]（估值階段）的「**實體傳導版**」

## 一句話

> $5.3 兆 CapEx 不會均勻撒到所有玩家——按物理供應鏈順序分批傳導，**第三階段是上游材料 + 光通訊真正爆掉**。

## 高盛 CapEx anchor

- Google + Meta + Microsoft + Amazon
- 2025-2030 合計 **$5.3 兆**
- 全砸 AI 資料中心 + 基礎建設

## 三階段傳導

### 第一階段：CSP 開始講 CapEx
- 雲廠商法說會把 AI CapEx framing 拉成多年期承諾
- 對應 [[宋分備忘錄 #1 — CSP-AI 通縮]] CSP CapEx 焦點轉移期
- **市場反應**：CSP 估值期權上升

### 第二階段：NVDA 設備 + 訂單全面落地
- NVDA Forward PE 反映 $500B 訂單可見度
- 對應 [[CapEx 見頂辯論]]、[[FCF 拐點]] 爭辯期
- **市場反應**：NVDA / [[AVGO]] 估值倍增、$NVDX 個股集中

### 第三階段 ⭐ ：上游材料 + 光通訊真正爆掉（**2026 中位置**）

物理供應鏈瓶頸**從 NVDA 往上游傳導**：
- 光模組（1.6T）量爆增
- 光引擎（[[Lumentum]] / [[Coherent]]）供應限制
- InP 晶圓（[[Lumentum]] / [[Coherent]] / [[IQE]]）整鏈緊繃
- 對應 [[Jevons Paradox（投資版）]]：技術升級 → 元件 TAM 暴增

## 第三階段具體判斷依據（2026-06-08 訊號）

### 訊號 1：1.6T 光模組量爆增 **十幾倍跳升**

| 年份 | 量 | NVDA 占比 |
|---|---|---|
| 2025 | ~180 萬顆 | 主力 |
| **2026** | **3,000 萬顆以上** | **60%+** |

**首批採購者已確認**：
- [[CoreWeave]]（已建 2026-06-09）
- [[Lambda]]（已建 2026-06-09、⚠️ 私募、未上市）
- [[Meta]]
- [[Microsoft]]
- [[Oracle]]（已建 2026-06-09）

### ⭐ 中國光模組鏈條（2026-06-09 補位 — Innolight + Eoptolink 中國 OEM 雙頭）

中國 OEM 雙頭 [[Innolight]] 300308.SZ（中國 #1、全球 transceiver 30%+ 市佔、LightCounting 連續 5 年 #1）+ [[Eoptolink]] 300502.SZ（中國 #2、全球 transceiver 8-12% 市佔）= **NVDA 1.6T 採購中**非中國替代**鏈條（[[Coherent]] / [[Lumentum]] / [[AAOI]] / Marvell 美系 vertical integration 之外）**——合計**中國 60-70% 市佔 + 全球 transceiver 40%+ 市佔**、共同壓制中國 OEM 第三梯隊（光迅 002281 + Accelink + 海信）。

| 公司 | 1.6T 量產時點 | 路線特色 | 客戶結構差異化 | 海外廠 hedge |
|---|---|---|---|---|
| [[Innolight]] 300308.SZ | **2026 H1 全球領先** | **全產品線 transceiver 規模型 + LPO 並重** | NVDA + 4 大 CSP + Ciena + Nokia **全 hyperscaler 直供**（純度型） | Thailand 單廠 |
| [[Eoptolink]] 300502.SZ | **2026 H2 追趕** | **LPO + Pluggable optics 純度型**（CPO 策略上謹慎） | NVDA + 4 大 CSP + **AT&T + Verizon + 中國電信運營商**（hyperscaler + 電信雙軌差異化）| **Thailand + Vietnam 雙廠**（多一層 hedge）|

⭐ **對 NVDA / CSP 1.6T 供應鏈分散化的地緣 hedge 意義**：
- **多源策略**：NVDA Rubin 1.6T 不會把採購全綁在美系 vertical integration 4 家（AAOI / LITE / COHR / Marvell）、中國 OEM 雙頭提供 **scale + cost + 多源供應鏈**反向 anchor
- **美中分離極化下的中位策略**：hyperscaler 仍會保留中國 OEM 採購（透過 Thailand + Vietnam 海外廠規避 ITAR / Section 301）、但比例會從 60-70% 降至 40-50%、美系 vertical integration 4 家從 30% 升至 50%+
- **互補不互相消滅**：Innolight 規模 hyperscaler 純度 + Eoptolink LPO + 電信 + 雙海外廠純度 = **中國 OEM 雙頭分歧路線、不會二選一**
- **跟美系 vertical integration 對沖意義**：[[AAOI]] / [[Lumentum]] / [[Coherent]] = **chokepoint 深度** + **美國本土 anchor**；Innolight + Eoptolink = **規模 + 成本 + 客戶分散** + **多海外廠 hedge** = 兩種**不同層級結構性 anchor**、可同時持有作為 1.6T 光模組賽道完整曝險

⭐ **跟 [[中國半導體國產替代（投資對沖視角）]] 連結**：中國 OEM 雙頭跟 [[CXMT]] / [[YMTC]] / [[華為]] 不同——CXMT / YMTC / 華為是「**中國市場閉環、國產替代美系**」、Innolight + Eoptolink 是「**中國產能服務全球 hyperscaler + 雙海外廠規避制裁**」開放型而非閉環型；前者打地緣分離 narrative、後者打全球供應鏈成本 + 規模 narrative。

### 訊號 2：InP 供應鏈三家**同時喊緊**（最關鍵）

整條鏈（**材料 → 雷射 → 晶圓**）同時 vintage：

| 公司 | 訊號 | 強度 |
|---|---|---|
| **[[Coherent]]** | InP delivery >26 週、影響 **15-20% 營收**（2026-05-06 法說） | 🔴 |
| **[[Lumentum]]** | 供應限制延伸到 **2026 全年**、EML 缺口 >30% / 日本 wafer fab fully allocated（2026-05-05 法說） | 🔴 |
| **[[IQE]]** | **£81M 融資**（MACOM £45M 戰略入股 11.5% + 長期供應協議）+ **FY 2026 >20% 成長**指引（2026-04 + 2026-05-28 公告） | 🔴 |

> 三家同時講一件事 = **不是巧合，整條鏈一起到瓶頸了**

### 訊號 3：NVDA 直接鎖供應鏈

- NVDA 對 [[Lumentum]] + [[Coherent]] 投資**超過 $40 億美元**（前面 wiki 紀錄是 $4B，校準上修）
- 推 [[Coherent]] **擴產翻倍**
- → **這不是投資，是把供應直接綁起來**
- 連 [[控制點轉移（投資版）]]：NVDA 從買方變綁定者

### 訊號 4：[[AVGO]] Tomahawk 6 CPO 跟 NVDA Spectrum-X 對打

- **不是概念市場了，是開始搶標準**
- 連 [[控制點轉移（投資版）]]、[[CPO 供應鏈圖譜]]

### 訊號 5：POET / Ayar Labs 生態加速

- ⚠️ POET（待 ingest）
- ⚠️ Ayar Labs（待 ingest）
- 融資 + 商業化雙加速
- 整鏈一起動

### 訊號 6：NVDA Spectrum-X 進入量產節奏

## 台灣鏈條對接

| 層 | 玩家（已建/待建） |
|---|---|
| 先進製程 | [[TSMC]] |
| 先進封裝 | [[日月光 ASE]] / ⚠️ 矽品（已併入 ASE）|
| AI server 系統落地 | [[鴻海 2317]]（GB200 NVL72 主代工 50-60%）/ [[廣達 2382]]（DGX 主代工 + GB200 30-40%）/ [[緯創 3231]]（GPU baseboard 30-40% + Wiwynn 緯穎 AI HPC）（三家已建 2026-06-09）|
| AI networking / switch | [[智邦 2345]]（Spectrum-X 主代工 + AVGO Tomahawk 6 multi-source、已建 2026-06-09）|

## ⚠️ 風險（thesis 失效情境）

### 1. 真正關鍵還在後面（Leo 自警惕）
- 現在比較像 **NVIDIA 自用 + 少數 early adopter** 在跑
- **AWS / Azure / Google 會不會全面跟上 = 下一段行情分水嶺**
- 若 hyperscaler 跟進緩慢 → 第三階段 narrative 失效

### 2. 上游瓶頸自解
- InP 產能擴張完成 → 短缺 narrative 失效
- 連 [[PB 估值法（記憶體週期）]] 邏輯（供給最終追上）

### 3. 替代技術
- 矽光子（CPO）取代 InP 雷射的部分需求
- 連 [[CPO 供應鏈圖譜]] 內部分歧

### 4. 散戶過度進場
- 1.6T 光模組十幾倍跳升已上頭條
- 連 [[資訊擴散四階段]] 階段 3-4

## 受惠鏈圖譜（按三階段排序）

### 第一階段（已過）
- CSP：[[Google]] / [[Meta]] / [[Microsoft]] / [[AMZN]]

### 第二階段（已過 / 進行中）
- 晶片：[[NVDA]] / [[AVGO]] / [[AMD]]
- 封裝：[[TSMC]] CoWoS / [[Amkor]] / [[日月光 ASE]]

### 第三階段（**現在**）
- 光通訊（美系 vertical integration / 第 5 層 chokepoint depth）：[[Lumentum]] / [[Coherent]] / [[AAOI]]
- 光通訊（**中國 OEM 雙頭** / 第 5 層 Beneficiary 規模 + LPO 純度型）：**[[Innolight]] 300308.SZ + [[Eoptolink]] 300502.SZ**（合計中國 60-70% 市佔 + 全球 transceiver 40%+ 市佔、Thailand + Vietnam 海外廠規避 ITAR、2026-06-09 補位）
- DCI / 接口：[[Ciena]] / [[Nokia]]（透過 Hyper Rail / Multi-Rail 傳導）
- InP 上游：[[IQE]] / ⚠️ Inrad
- 矽光生態：⚠️ POET / ⚠️ Ayar Labs

### 第四階段（**潛在下一段**，AWS/Azure/Google 全面跟進）
- 全面 hyperscaler 採購
- TPU / Trainium / Inferentia 自研晶片擴大
- 對應 [[資訊擴散四階段]] 階段 3-4

## 跟其他 wiki 概念連結

- [[資訊擴散四階段]]：本 concept 是「實體供應鏈傳導版」
- [[市場四階段：懷疑／驗證／共識／反轉]]：本 concept 是「估值階段對應的物理階段」
- [[Jevons Paradox（投資版）]]：第三階段 InP / 1.6T 爆增的理論基礎
- [[CapEx 見頂辯論]]：本 concept 反駁 CapEx 見頂論
- [[FCF 拐點]]：第三階段 CapEx 不會自動見頂 → FCF 拐點延後
- [[控制點轉移（投資版）]]：NVDA $40 億鎖 LITE/COHR = 控制點往上游延伸
- [[CPO 供應鏈圖譜]] / [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：第三階段受惠
- [[AI 記憶體結構性供給短缺]]：同時期的記憶體 anchor
- [[賣水人選股邏輯（投資版）]]：第三階段是賣水人的高光時刻
- [[宋分備忘錄 #1 — CSP-AI 通縮]] / [[宋分備忘錄 #5 — 複利測試]]：對照宋分的 CSP 思路

## 待 ingest 延伸（第三階段缺的玩家）

### InP / 光通訊上游
- ✅ **[[IQE]]**（已建 2026-06-08）：InP 晶圓 epi 代工龍頭、£81M 融資 + MACOM 11.5% 入股 + FY 2026 >20% 成長指引、6" InP DFB industry-first、五軸 17/25、alpha 最尖端但風險最濃
- **POET Technologies**（矽光整合）
- **Ayar Labs**（光晶片初創）

### Hyperscaler / 雲算力（✅ 2026-06-09 補位完成）
- ✅ **[[CoreWeave]]**（已建 2026-06-09）— neocloud 龍頭、NVDA 戰略客戶 + 投資人、NVDA $6.3B backstop、1.6T 光模組首批採購者、循環投資 anchor 樣本、五軸 12/25
- ✅ **[[Lambda]]**（已建 2026-06-09、⚠️ 私募、NOT-INVESTABLE）— neocloud #2、NVDA NCP Elite tier、Series D $480M @ $4-5B、IPO 時程 2026 H2 - 2027 H1 傳言、五軸 13/25
- ✅ **[[Oracle]]**（已建 2026-06-09）— 老牌資料庫龍頭 + Stargate 主力 + OpenAI $300B 五年合約 + 1.6T 光模組首批採購者、市值 $700-900B、五軸 18/25

### 台灣 AI server 系統（✅ 2026-06-09 補位完成）
- ✅ **[[鴻海 2317]]**（AI server #1 代工 50-60% market share）— NVDA reference design 主代工 + AI cloud / edge 雙引擎（Tesla Cybercab + Apple Vision Pro 第二代）、五軸 16/25
- ✅ **[[廣達 2382]]**（AI server #2 代工）— NVDA DGX 系列主代工 + Meta MTIA + NB 龍頭 + Apple Mac、五軸 15/25
- ✅ **[[緯創 3231]]**（GPU baseboard niche specialist）— NVDA HGX baseboard 主代工 30-40% + Wiwynn 緯穎 27.5% 持股子公司 AI HPC anchor、五軸 14/25
- ✅ **[[智邦 2345]]**（AI networking switch）— NVDA Spectrum-X 主代工 + AVGO Tomahawk 6 multi-source、白牌 OCP 規格全球 #1、AI networking pure-play 高毛利 25-30%、五軸 18/25

## 相關連結

- [[資訊擴散四階段]]
- [[Jevons Paradox（投資版）]]
- [[CPO 供應鏈圖譜]]
- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]
- [[AI 記憶體結構性供給短缺]]
- [[控制點轉移（投資版）]]
- [[NVDA]]、[[Lumentum]]、[[Coherent]]、[[IQE]]、[[AVGO]]、[[Ciena]]、[[Nokia]]
- [[TSMC]]、[[日月光 ASE]]、[[Amkor]]

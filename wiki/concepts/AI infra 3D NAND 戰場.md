---
title: AI infra 3D NAND 戰場
aliases: [AI 3D NAND 戰場, 3D NAND 賽道, NAND AI 戰場, Enterprise SSD 賽道, NVDA 3D NAND 供應鏈]
type: concept
created: 2026-06-08
updated: 2026-06-09
as_of: 2026-06-08
check_after: 2026-12-08
expires_on: 2027-06-08
sources:
  - raw/2026-06-08_Leo-黃仁勳定調記憶體結構性短缺-SK-Hynix-合約.md
evidence_url: https://www.tweaktown.com/news/109677/oh-no-nvidias-next-gen-vera-rubin-ai-systems-to-eat-up-millions-of-terabytes-of-ssds/index.html
tags: [記憶體, NAND, 3D NAND, Enterprise SSD, AI infra, NVDA 路線圖, 估值範式, QLC, HBF]
confidence: medium
---

# AI infra 3D NAND 戰場

3D NAND 在 AI infra 是「**第三條記憶體腿**」——跟 HBM（AI 加速器主記憶體）、LPDDR5X（系統記憶體）並列構成 NVDA 路線圖的「**全記憶體棧**」。本 concept 回答 codex P1-7 提的關鍵問題：**3D NAND 在 AI 是主戰場還是附屬 BOM？**

> 答：**「半主戰場 + 半附屬 BOM」**——以 NVDA Vera Rubin 的 ICMS（Inference Context Memory Storage）為轉折點，3D NAND 從「附屬 BOM」升級為「**結構性新需求軸**」，但獲利能見度與估值框架仍輸 HBM 一個量級。

→ 對應 [[AI 記憶體結構性供給短缺]] 的「**第三條腿**」、是 [[HBM iPhone moment]] 範式遲到一年的姊妹篇。

## 一句話

> HBM 是 AI 的記憶體；3D NAND 是 AI 的儲存——但在 Vera Rubin 之後，**NAND 開始長出 HBM 的形狀**（multi-year design-in + 結構性短缺 + 上游瓶頸）。

## 3D NAND 在 AI infra 的角色（vs HBM / DRAM）

| 維度 | HBM | LPDDR5X / DRAM | **3D NAND（Enterprise SSD）** |
|---|---|---|---|
| **位置** | 緊貼 GPU die（CoWoS 內） | CPU 旁主記憶體 | 主機板 + rack 內 SSD bay |
| **角色** | 模型權重 + 訓練 KV cache | 系統記憶體、Vera CPU 內存池 | **Inference Context Memory Storage（ICMS）** + 模型 checkpoint + 訓練資料集 + RAG 向量索引 |
| **AI 升級點** | 16-Hi 48GB / 2TB/s（HBM4）| 1.5TB capacity / 1.2TB/s（SOCAMM2）| **單系統 1,152TB SSD**（NVDA VR200 NVL72 ICMS）|
| **價格 / 容量** | $/GB 極高 | $/GB 中 | **$/GB 最低**（10-30× 便宜於 HBM）|
| **延遲** | ns 級 | ns 級 | μs 級（PCIe Gen5/Gen6）|
| **頻寬** | 2,048-bit @ 2TB/s+ | 256-1024-bit @ 273GB/s-1.2TB/s | PCIe Gen5 x4 @ 16GB/s（單顆）|
| **NVDA 路線圖綁定** | multi-year design-in（Rubin → Feynman）| multi-year design-in（Vera CPU + Spark + Thor）| **partial design-in**（Vera Rubin ICMS + Spark + Thor、Jetson Thor 已固定 lineup）|
| **競爭格局** | 寡占 3 家（SK / Samsung / Micron）| 寡占 3 家 + 中國 CXMT | **6 家分食**（Samsung / SK+Solidigm / Kioxia / Micron / SanDisk / YMTC）|
| **估值框架** | [[Forward PE 估值法]]（infra 級）| 混合 | **混合：PB（消費）+ Forward PE（enterprise SSD）** |
| **物理瓶頸** | HBM 製程 + CoWoS 封裝 | 一般 DRAM wafer | **3D 堆疊層數 + CMOS bonded array + QLC 良率** |

**核心差異**：HBM 物理綁進封裝、技術門檻拉開護城河 → 寡占 + infra 估值；3D NAND **物理可獨立採購**、客戶可換廠商、6 家分食 → **估值仍輸 HBM 一個量級**。

## 4 大玩家結構（Q1 2026 Counterpoint Research）

| 廠商 | 市佔（Q1 2026） | 上市狀態 | NAND 業務 mix | AI / Enterprise SSD 曝險 |
|---|---|---|---|---|
| **Samsung（NAND 部門）** | **29%** | 母公司 KRX 005930 上市（NAND 不分拆）| Consumer + Mobile + Enterprise + Foundry-bonded | 中（Enterprise SSD 拿 NVDA / Hyperscaler、但 HBM 才是主舞台）|
| **SK Hynix + [[Solidigm]]** | **22%**（合計）| SK Hynix KRX 上市；Solidigm 私有子公司 | **Solidigm 主打 Enterprise QLC SSD**、SK Hynix 主體混合 | **高**（Solidigm Enterprise SSD 100% AI 化、QLC market share 51%）|
| **[[Kioxia]]** | **14%** | TYO: 285A（2024-12 IPO、2025 Nikkei 225 納入）| BiCS 8 → BiCS 10 路線、SanDisk JV 分手後獨立 | **高**（FY2025 ¥2.34T 營收 / OP ¥876B，AI Enterprise SSD 是主成長）|
| **Micron（NAND 部門）** | **13%** | 美股 NASDAQ: MU 上市 | DRAM 主業 + NAND 配角 | 低（NAND 在 Micron 是 secondary、HBM 才是 anchor）|
| **[[SanDisk]]（前 WD Flash）** | **13%** | NASDAQ: SNDK（2025-02-24 spin-off）| 純 NAND（從 [[Western Digital]] 切出）| **高**（與 SK Hynix 合作 HBF 標準化、FY2026 Q3 datacenter +233%）|
| YMTC（長江存儲）| **13%** | 中國未上市 | 中國本土供應、被美制裁限 NVDA exposure | 低（中國國產替代）|

**關鍵變化（2025-2026）**：
- **2025-02-24 [[Western Digital]] 分拆 SanDisk**：WDC 變純 HDD 公司、SanDisk 接收所有 NAND 業務 → **WDC 變身 AI HDD 受惠者、不是 NAND 戰場玩家**
- **2024-12-18 [[Kioxia]] IPO**：1,455 yen 上市、2026-04 衝到 36,000 yen（**+2,400%**）= NAND 廠也跟 HBM 廠 re-rate 同步
- **Bain Capital 2026-03 減持至 <30%**：但仍最大股東、$3.5B 套現
- **SK Hynix 透過 [[Solidigm]] 全包 enterprise QLC**：QLC market share 從 2024 42% → 2025 51%（majority share）

## AI 用 NAND（Enterprise SSD） vs Consumer NAND 規格差

### 規格層面

| 維度 | Consumer SSD（手機 / PC）| Enterprise SSD（AI server）|
|---|---|---|
| **介面** | PCIe Gen4 為主、Gen5 滲透中 | **PCIe Gen5 量產 / Gen6 規劃 2027** |
| **容量單顆** | 256GB-2TB（QLC 為主）| **61TB → 245TB**（QLC、SK Hynix PS1012/PS1101）|
| **記憶體 cell** | QLC 為主（cost-down）| **eTLC**（耐用度）/ **大容量 QLC**（cost-density）|
| **耐用性 (DWPD)** | 0.3-1 DWPD | **1-3 DWPD**（read-intensive）/ **3-10 DWPD**（mixed）|
| **電源保護** | 無 PLP（power-loss protection）| **必備 PLP** |
| **散熱** | 被動 + heatsink | **液冷支援**（Solidigm liquid-cooled SSD）|
| **fail rate target** | 1-2 年 RMA | **5 年 24/7 沒翻車** |
| **典型客戶** | 三星手機、Dell PC、自組 | NVDA / Hyperscaler / NVIDIA Vera Rubin ICMS |

### 利潤 / wafer 經濟層面

> **「同一片 wafer 切到 enterprise = 切到 consumer 的 3-5 倍營收」**（TrendForce 2026 數據）

- Q1 2026 Client SSD 合約價 QoQ +40%
- Q1 2026 Enterprise SSD 合約價 QoQ **+60%**
- → 廠商集體把 wafer 從 Client 切到 Enterprise（Phison CEO 確認「2026 所有產能售罄」）
- 對 Consumer 市場後果：PC / 手機 NAND 結構性缺貨外溢、價格傳導到終端 BOM

→ 這個機制完全 mirror HBM 切走 DRAM 產能的物理邏輯（每 GB HBM 消耗 DDR5 三倍 wafer），但 NAND 上更直觀：**廠商不擴產的選擇 = 把 wafer 從消費市場切到 enterprise**。

## NAND 在 NVDA 路線圖的具體用量

### Vera Rubin AI 超級電腦（最大 NAND 用量）

- **每 GPU ~16TB 3D NAND**（local SSD pool）
- **每 NVL72 rack ~1,152TB SSD**（系統級 ICMS 用量）
- **每 rack 3D NAND BOM ~ USD $1M+**（從 GB200 NVL72 的「幾乎零」躍升）
- **2026 出貨估計 30,000 units → 34.6M TB NAND 需求 = 全球 2.8% NAND 產能**
- **2027 估計 100,000 units → 115.2M TB = 全球 9.3% NAND 產能**

> 這個量級是 NAND 廠當前**沒 price in** 的供給衝擊——HBM 廠都把 wafer 切去 HBM、原本要切到 Enterprise SSD 的 NAND 廠也要面對「規模史無前例的單客戶綁定」。

### Vera CPU（standalone Arm 88 核）

- **主要還是 LPDDR5X**（SOCAMM2 1.5TB 主記憶體）
- 3D NAND 用於 OS + checkpoint storage（非主軸）

### RTX Spark AI PC（GB10 Superchip）

- **128GB LPDDR5X 統一記憶體 + 3D NAND**（容量未揭露、推測 4-8TB SSD）
- 用途：本地推理模型權重存儲

### Jetson Thor 機器人平台

- **128GB LPDDR5X + 3D NAND**
- 用途：感測器資料 + 模型 checkpoint + RAG 向量索引（機器人「記憶」）

**綜合判斷**：NAND 在 NVDA 4 個產品中，**Vera Rubin 是主戰場**（每 rack $1M+ NAND BOM）、其他 3 個是 BOM 配角但量大（128GB 起跳）。

## 主戰場 vs 附屬 BOM 判斷

### 為什麼一度被認為「附屬 BOM」

1. **歷史脈絡**：在 2024 H1 之前，AI server 用的 SSD 量沒有結構性放量、屬於傳統 datacenter 需求疊加
2. **價格敏感**：QLC NAND $/GB 太便宜 → 估值不易拉到 infra 級
3. **客戶可換廠**：物理上沒有 design-in lock-in（HBM 是 die-bonded、NAND 是 hot-pluggable PCIe）
4. **NAND 廠分散**：6 家分食 → 無「SK Hynix 60-70% NVDA 份額」式的寡占錨點

### 為什麼 2026 起變「半主戰場」

1. **Vera Rubin ICMS 是結構性新需求**：1,152TB / rack 是過去 datacenter SSD 用量 5-10× 跳躍
2. **Enterprise SSD 已是 NAND 廠最大 application（2026 起）**（TrendForce 確認）
3. **2026 全球 NAND 售罄**（Phison CEO 確認 + Kioxia FY2026 Q1 outlook 升）
4. **HBF (High Bandwidth Flash) 第三條腿成形**：SanDisk + SK Hynix 合作標準化、推理 server 用、容量是 HBM 8-16× 但同成本、目標 2027 量產 → **NAND 開始長出 HBM 形狀**
5. **Solidigm / Kioxia 出現「multi-year design-in」訊號**：Solidigm 2026 營收估 KRW 11.8T / 淨利 1.4T、Kioxia FY2025 OP +95%

### Leo 的判斷

> **NAND 是「升級中的附屬 BOM」**——目前 60% 還是附屬 BOM、40% 已經是主戰場。
>
> 2027 H2 HBF 落地 + Vera Rubin 100K units 出貨後，會升到「60% 主戰場 + 40% BOM」。
>
> 但**永遠不會像 HBM 那樣 100% 主戰場**——物理性質決定（可獨立採購 + 6 家分食 + QLC commodity 屬性）。

## 跟 [[AI 記憶體結構性供給短缺]]：主戰場還是附屬 BOM？

| 主戰場（HBM 級）| 半主戰場（**3D NAND 級**） | 附屬 BOM（一般 NAND）|
|---|---|---|
| 寡占 3 家 | **6 家分食、CR3 65%** | 純通用市場 |
| die-bonded lock-in | **PCIe 可換、但 enterprise SSD 仍有 lock-in（耐用性 / qualification）** | hot-pluggable |
| co-design partner | **multi-year supply + enterprise SSD qualification cycle** | 純 spot |
| Forward PE 15-25x 上看 | **Forward PE 10-15x（Kioxia 已超 15x）** | PB 守底 |
| HBM4 預付到 2028 | **2026 全球售罄、Vera Rubin ICMS 2027 H2 ramp** | 通用 NAND 仍週期 |

→ **3D NAND 在 AI 角色是 [[AI 記憶體結構性供給短缺]] 的「第三條腿」**，但量級比 HBM 小一級、價格穩定性差一級、估值框架混合。

## 跟 [[PB 估值法（記憶體週期）]]：仍適用嗎？

### 短答案

> **適用、但需要「分段估值」改良版**。

### 分段邏輯

| NAND segment | 估值工具 | 監控指標 |
|---|---|---|
| **Consumer NAND**（手機 / PC）| **本 [[PB 估值法（記憶體週期）]] 框架** | 全球 PC 出貨、手機 cycle |
| **Mobile eMMC / UFS** | PB 框架 | 高通 / MediaTek 出貨 |
| **Enterprise SSD（datacenter）** | **混合：PB 守底 + Forward PE 10-15x** | Hyperscaler CapEx、SSD ASP |
| **AI Enterprise SSD（NVDA ICMS）** | **Forward PE 15-20x（infra 樣板）** | NVDA Vera Rubin ramp、HBF 標準化、Solidigm AI 營收 |

### Thesis switching trigger

- Enterprise SSD 營收占比 > 50% + ASP QoQ > 40% → 切到 Forward PE 框架（Kioxia FY2025 已過、SanDisk FY2026 Q3 已過）
- Enterprise SSD ASP 連續兩季 QoQ 負成長 → 退回 PB 框架

### 跟 HBM 估值的差異

- HBM iPhone moment 是「**全 segment re-rate**」（傳統 DRAM 都被拉上）
- 3D NAND 是「**分段 re-rate**」（Enterprise SSD 拉、Consumer NAND 仍週期）

## 跟 [[HBM iPhone moment]] 對照

| 維度 | HBM | **3D NAND（Enterprise SSD）** |
|---|---|---|
| **iPhone moment 觸發** | 2024（NVDA H100 / B200 ramp）| **2026 H2-2027 H1**（Vera Rubin ICMS 普及）|
| **anchor 事件** | 2026-06-08 NVDA-SK Hynix multi-year partnership | 2026-Q3 Vera Rubin 30K units 出貨 + HBF 標準化 |
| **re-rate 幅度** | Forward PE 5-6x → 15-25x | Forward PE 8-10x → **15-20x（infra 級半套用）** |
| **領頭 entity** | [[SK Hynix]]（NVDA 60-70% HBM4）| **[[Kioxia]]**（FY2025 OP +95%、Enterprise SSD 純度最高）+ **[[Solidigm]]**（透過 SK Hynix 子集團）|
| **主要風險** | DeepSeek 類效率躍進 | **HBF 取代效應**（NAND-based 替代 HBM 部分功能 → 對 HBM 是利空、對 NAND 是利多）|
| **物理瓶頸** | CoWoS 封裝 + HBM 製程 | **3D 堆疊層數 + QLC 良率 + CMOS bonded array** |

→ **3D NAND iPhone moment 比 HBM 慢 12-18 個月**——2026 H2 啟動、2027 H1 anchor 確認、2028 全 re-rate。

## NVDA 4 產品路線圖：3D NAND 具體配置

| 產品線 | 3D NAND 用量 | NAND 廠主供 | NAND BOM 占比 |
|---|---|---|---|
| **Vera Rubin AI 超級電腦**（NVL72）| **1,152TB / rack**（ICMS）| SK Hynix + Solidigm + Kioxia + SanDisk + Micron + Samsung 分食 | **$1M+ / rack BOM**（13% of $7.8M）|
| **Vera CPU** | OS + checkpoint（容量未揭露）| 主要 SK Hynix（合約綁定）| <5% BOM |
| **RTX Spark AI PC** | 4-8TB local SSD（推測）| SK Hynix（主供）+ 多家 | ~10% BOM |
| **Jetson Thor 機器人** | 128GB-1TB SSD（推測）| SK Hynix（主供）+ 多家 | ~10% BOM |

**綜合**：4 個產品中 **Vera Rubin ICMS 是唯一「主戰場」**、其他 3 個 NAND 是「BOM 配角但路線圖鎖死」。

## 投資受惠鏈

### Tier 1：NAND 純度最高 + AI 曝險最高
- **[[Kioxia]]**（TYO: 285A）— Enterprise SSD 純 play、Bain 仍 30% 持股、BiCS 8 218-layer 量產 + BiCS 10 332-layer 2026 加速、FY2025 OP +95%、IPO 後 +2,400%
- **[[Solidigm]]**（[[SK Hynix]] 100% 子）— Enterprise QLC SSD 龍頭、QLC 51% 市占、2026 估營收 KRW 11.8T、推 245TB PCIe Gen5 PS1101、AI 100% pivot（消費市場退出）

### Tier 2：NAND 純 + 但有 HDD 雙鏈
- **[[SanDisk]]**（NASDAQ: SNDK）— **2025-02-24 從 WDC spin-off 完成的美 NAND pure-play + HBF 規格定義權共持者**、與 SK Hynix 合作 HBF 標準化（2026-02-25 正式公告）、FY2026 Q3 整體營收 $5.95B（+97% QoQ）/ Datacenter +233% YoY、capex +40% YoY 同步 Kioxia、與 Kioxia 共用 Yokkaichi/Kitakami JV fab 但客戶分離 50/50、**五軸 18/25**
- **[[Western Digital]]**（NASDAQ: WDC）— **2025-02-24 spin-off 後變純 HDD 公司**、Q3 FY2026 營收 $3.34B / nearline +37% YoY / Cloud 89%、12M +880-970%、**3D NAND 已不在公司結構內**（但仍是「HDD-NAND 雙鏈 storage AI 受惠者」一員）

### Tier 3：母公司 NAND + 但 HBM 才是主戰場
- **[[SK Hynix]]**（KRX: 000660）— 主公司 HBM 主戰場、Solidigm 是 NAND 第二曲線
- **[[Samsung Electronics]]**（KRX: 005930）— NAND 市佔 #1（29%）但屬於整鏈閉環一段、HBM 才是再評價軸
- **[[Micron]]**（NASDAQ: MU）— NAND 是 secondary、HBM 才是 anchor

### Tier 4：上游瓶頸（NAND 製程設備）
- ASML（EUV）、AMAT（沉積 / CVD）、Lam Research（蝕刻、3D NAND 主受惠）、KLA（量測）、TEL（蝕刻）

## ⚠️ 風險（thesis 失效情境）

### 1. HBF 取代 vs 互補定論不明
- SanDisk + SK Hynix 2026-02 標準化 HBF：8-16× HBM 容量、1.6TB/s 頻寬、推理用
- 若 HBF 真能取代部分 HBM 角色 → 對 NAND 是利多、對 HBM 利空
- 但若市場接受度 < 預期（NAND 延遲仍比 HBM 高 1000×）→ HBF 只是 niche、3D NAND iPhone moment 拖延

### 2. NVDA Vera Rubin 出貨節奏
- 30K units 2026 假設 / 100K units 2027 → 任一節點 slip 都會打亂 ICMS 預期
- 對比 HBM 是「客戶等 12 個月也要拿到」、ICMS 是「客戶可削減 SSD 容量保 GPU 出貨」

### 3. QLC 良率瓶頸
- 245TB SSD 用 QLC NAND，良率 / 耐用度仍是工程挑戰
- 若 245TB SSD 普及不順 → 不是 60TB 規格的 4× 跳躍、是 4 顆 60TB 並聯 → BOM 經濟差

### 4. 中國 YMTC 國產替代
- YMTC 已拿到 13% 全球市佔（Q1 2026）= **3-5 年內成熟到能切 Enterprise SSD**
- 對 Tier 1 廠商造成中國市場分食壓力

### 5. NAND 廠擴產追上（傳統週期論）
- Phison 警告 2027 仍 sold out、但 2028+ Kioxia BiCS 11 + Samsung V10 + SK V9 全廠 ramp = 供給端可能在 2028 H2 追上
- 對 Forward PE re-rate 是時間限制

### 6. 2026-06-08 韓股熔斷情緒外溢
- KOSPI -8.29% 拖累 SK Hynix（Solidigm 母公司）-7.68%
- Solidigm 仍 private、估值需等 SK Hynix 母公司 re-rate

## 雙引擎估值實務操作

### 進場時點（thesis 切到「半主戰場」框架）

- Enterprise SSD 營收占比 > 50% ✓（Kioxia FY2025、SanDisk FY2026 Q3 已過）
- AI SSD ASP YoY > 40% ✓（TrendForce 2026 Q1 數據確認）
- HBF 標準化進度確認 ✓（2026-02-25 SanDisk + SK Hynix 公告）
- **→ 2026 Q2 已確認三項滿足，框架切換成立**

### 持有期內監控

- NVDA Vera Rubin 出貨節奏（30K → 100K 2026-2027）
- HBF 量產時程（2027 H1 預計）
- Kioxia / SanDisk / Solidigm 季度 Enterprise SSD segment 揭露
- Samsung NAND 部門 segment（隱於 DS 段）
- 中國 YMTC 進度

### 退場時點

- Enterprise SSD ASP 連續兩季 QoQ 負成長
- NVDA 取消或推遲 Vera Rubin ramp
- HBF 標準化失敗、NAND-as-DRAM 路線崩
- **→ 回退到 PB 框架（傳統景氣循環論）**

## 跟其他 wiki 概念連結

- [[AI 記憶體結構性供給短缺]]：本 concept 是它的「第三條腿」（HBM + LPDDR5X + 3D NAND）
- [[HBM iPhone moment]]：本 concept 是它遲到 12-18 個月的姊妹篇
- [[PB 估值法（記憶體週期）]]：本 concept 主張「分段估值」，Enterprise SSD 切 Forward PE / Consumer NAND 保 PB
- [[半導體基礎建設化]]：本 concept 是 NAND 子領域的具體化
- [[控制點轉移（投資版）]]：NVDA 在 3D NAND 拿到「規格定義權」（Vera Rubin ICMS = 標準化 application）
- [[賣水人選股邏輯（投資版）]]：6 家分食的 NAND 比 HBM 更接近純賣水人
- [[CapEx 見頂辯論]]：NAND 廠擴產追上時間表（2028 H2）是「CapEx 見頂」的時間錨
- [[Jevons Paradox（投資版）]]：HBF 突破 → AI 模型 context window 倍增 → NAND 需求倍增
- [[市場四階段：懷疑／驗證／共識／反轉]]：Enterprise SSD 賽道「驗證 → 共識」過渡期、Consumer NAND 仍「反轉前夕」
- [[資訊擴散四階段]]：Kioxia 12M +2,400% / WDC +880% = 已過「機構→賣方→媒體」進入 ETF 配置
- [[宋分備忘錄 #2 — HBM iPhone Moment-Meta-軟體 PE]]：本 concept 補完 NAND 軸
- [[公司 Entity 模板（Step 1-3 三段式）]]：4 entity（Kioxia / Solidigm / SanDisk / WDC）皆套用

## 主要佐證來源

- [TweakTown — Vera Rubin AI 系統需要 1,152TB SSD per rack](https://www.tweaktown.com/news/109677/oh-no-nvidias-next-gen-vera-rubin-ai-systems-to-eat-up-millions-of-terabytes-of-ssds/index.html)
- [Fudzilla — Vera Rubin SSD supply shock](https://fudzilla.com/vera-rubin-storage-plans-could-spark-an-ssd-supply-shock/)
- [Tom's Hardware — Kioxia BiCS10 332-layer 加速 2026](https://www.tomshardware.com/pc-components/ssds/kioxias-next-gen-3d-nand-production-gets-expedited-to-2026-report-claims-high-capacity-332-layer-bics10-devices-to-sate-growing-demand-from-ai-data-centers)
- [TechTimes — Kioxia BiCS 8 mass production 2026 update](https://www.techtimes.com/articles/317071/20260524/kioxia-nand-flash-mass-production-accelerates-bics10-target-puts-samsung-sk-hynix-edge.htm)
- [Counterpoint Research — Global NAND Q1 2026 Market Share](https://counterpointresearch.com/en/insights/global-nand-memory-market-share)
- [BigGo Finance — NAND Market AI Server Boom SK Hynix Narrows Gap to 6pp](https://finance.biggo.com/news/PlfbtZwBq7sy_YQMJYYc)
- [Sandisk Press — SanDisk + SK Hynix HBF Standardization 2026-02-25](https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf)
- [Tom's Hardware — HBF speedy NAND replace HBM AI inference](https://www.tomshardware.com/tech-industry/sandisk-and-sk-hynix-join-forces-to-standardize-high-bandwidth-flash-memory-a-nand-based-alternative-to-hbm-for-ai-gpus-move-could-enable-8-16x-higher-capacity-compared-to-dram)
- [TechRadar — SK Hynix 245TB PS1101 PCIe Gen5 SSD](https://www.techradar.com/pro/samsung-archrival-showcases-245tb-pcie-gen5-ssd-joining-kioxia-huawei-and-sandisk-with-solidigm-samsung-and-micron-expected-to-launch-similar-products-in-2026)
- [SK Hynix News — PS1012 U.2 245TB AI datacenter SSD](https://news.skhynix.com/sk-hynix-develops-ps1012-ssd-for-ai-data-centers/)
- [TrendForce — Memory makers prioritize server pricing Q1 2026](https://www.trendforce.com/presscenter/news/20260105-12860.html)
- [Tom's Hardware — Phison CEO confirms 2026 NAND sold out 2027 pricing apocalypse](https://www.tomshardware.com/pc-components/ssds/phison-ceo-confirms-nand-prices-have-more-than-doubled-and-will-continue-to-rise-all-2026-production-already-sold-out-ssds-facing-pricing-apocalypse-throughout-2027)
- [TrendForce — Kioxia + SanDisk capex +40% YoY 2026-06-01](https://www.trendforce.com/news/2026/06/01/news-japan-u-s-nand-alliance-steps-up-investment-as-kioxia-sandisk-capex-reportedly-rises-40-yoy/)
- [SK Hynix Solidigm 2026 outlook 11.8T won](https://www.globalnewstop.com/news/articleView.html?idxno=1639)
- [Solidigm QLC market share 42% → 51% 2024-2025](https://www.ainvest.com/news/resurgence-ssd-suppliers-2025-strategic-play-solidigm-sk-hynix-2510/)

## 相關連結

- [[AI 記憶體結構性供給短缺]]
- [[HBM iPhone moment]]
- [[PB 估值法（記憶體週期）]]
- [[Forward PE 估值法]]
- [[半導體基礎建設化]]
- [[控制點轉移（投資版）]]
- [[CapEx 見頂辯論]]
- [[賣水人選股邏輯（投資版）]]
- [[Jevons Paradox（投資版）]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[資訊擴散四階段]]
- [[NVDA]]
- [[SK Hynix]]
- [[Samsung Electronics]]
- [[Micron]]
- [[Kioxia]]
- [[Solidigm]]
- [[SanDisk]]
- [[Western Digital]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[時效 metadata schema（lint 規範）]]
- [[宋分備忘錄 #2 — HBM iPhone Moment-Meta-軟體 PE]]

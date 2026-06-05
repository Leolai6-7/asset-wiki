---
title: F&S Electron
aliases: [F&S Electron, FNS Electron, 에프앤에스전자, 에프엔에스전자, FnS Electron, F&S Electronics]
type: entity
created: 2026-06-05
updated: 2026-06-05
as_of: 2026-06-05
check_after: 2026-09-05
sources:
  - raw/2026-06-05_TGV-年度工事-sennn.nnna.md
tags: [標的, 韓國, 私募未上市, 玻璃基板, TGV, foreign_competitor, Absolics 供應商, 鈦昇對手, S.E.A. 子公司]
confidence: medium
---

# F&S Electron（에프앤에스전자，韓國未上市）

## 1. 一句話定位

**Absolics 2024-2026 H1「世界第一條商業化玻璃中介層產線」唯一 TGV 鑽孔 + Metallization (PVD) 製程外包商**，2021-05 由韓國 Incheon 一群 PCB/FPD/Semi 老兵成立，自 2024-05 起在 Songdo 廠把 510×515mm panel 玻璃做 TGV + 金屬化後**直接交付 Absolics Georgia 廠**。2025-11 被韓國 [[S.E.A. (Semiconductor Equipment Anyang)|S.E.A.]] 取得 majority stake 變垂直整合子公司——但**獨家 TGV 合約 2026-03 到期**後 [[Absolics]] 轉 dual sourcing，**second supplier slot 是台廠 [[鈦昇]] / 韓 Hana / 韓 Philoptics / [[LPKF]] 的潛在窗口**。

> ⚠️ **公開資料豐富度：medium**——公司結構、客戶關係、合約時點 high confidence；技術規格（laser 類型、孔密度、aspect ratio、yield）、財務數字（營收、員工以外的營運指標）、IP 持有現況、second supplier 是誰，都缺。Confidence 整體標 **medium**。

## 2. 三層 thesis

### 產業層

- **賽道位置**：[[TGV 製程鏈圖譜]] 第 **1 + 2 站合併** 玩家（雷射改質鑽孔 + Metallization PVD 一站式 contract manufacturer），不做設備、不做切割、不做後段。**唯一定位是「panel-level 加工外包」**——把 [[Corning]]/[[AGC]] 510×515mm 玻璃 sheet 變成已穿孔已金屬化的 substrate blank，交給 [[Absolics]] 做後續 RDL 製程
- **[[市場四階段：懷疑／驗證／共識／反轉]]**：「驗證 → 共識」過渡——2024-05 業界首發量產、2025 至今穩定供應 Absolics、2026-03 獨家合約到期是 verification milestone
- **[[資訊擴散四階段]]**：**機構 → 賣方階段**——只在韓國本土媒體（etnews、The Elec、Daum 金融）+ TrendForce 行業報告 + S.E.A. 母公司 IR 訪談（Worldfolio）出現；歐美主流財經未報導
- **TAM 視角**：F&S Electron 自己沒揭露營收，但 Absolics Phase 1 12,000 m²/年 = 全部交給 F&S Electron 處理 + Phase 2 60,000-72,000 m²/年（暫延）。若僅 Absolics 一個客戶 + 加工費約 USD 50-200/panel（推估，**未驗證**） → 年加工費 USD 5-50M 量級。F&S Electron 2024-05 自我宣告「目標 1 兆韓元（USD 720M）營收公司」，但**現實營收級距未公開**

### 目的層

- **不是 IP 公司**：F&S Electron 沒被報導握有獨立的 TGV 雷射核心專利（vs [[LPKF]] LIDE 整套專利 portfolio）。它的 know-how 是**整合 S.E.A. 設備 + Absolics 客製化規格 + 韓國本土 PCB/FPD 老兵 process engineering** 的工藝整合者
- **真實角色**：在 [[控制點轉移（投資版）]] 中卡的不是設備（買 S.E.A. 自家設備）、不是材料（買 Corning/AGC sheet），而是 **「panel-level TGV + Metallization 工藝外包服務」**——是 [[Absolics]] 把 fab 的「鑽孔 + 金屬化」這兩站**完全外包**給 F&S Electron 處理。商業模式類似台廠半導體 OSAT 對 fabless 的關係
- **2025-11 S.E.A. 取得 majority stake** 是關鍵結構變化：S.E.A.（年營收 USD 80M、89% 賣美國、CEO Jaeho Shin 三星貿易出身）把 F&S Electron 變成「**設備 + 服務雙層**」垂直整合單元——S.E.A. 賣設備 + F&S Electron 用同設備代加工。這跟 [[LPKF]] + Vitrion foundry 模式同構（[[LPKF]] 也是設備 + 自有 foundry 雙層押）
- 雙股東結構：**S.E.A.（에스이에이）+ Fuseimenix（후세메닉스）** 兩個母體，S.E.A. 主導工業整合、Fuseimenix 角色未公開（可能是早期 angel）

### 供應層

- **路線**：跟著 [[Absolics]] 用 [[Intel]] 授權的雷射改質 + 化學蝕刻路線（**未公開使用什麼雷射來源、是否買 [[LPKF]] LIDE 設備、是否與 LPKF IP 衝突**）。考慮到 [[Absolics]] 2024 起取得 [[Intel]] TGV licensing → F&S Electron 受惠**反射性 IP shield**：因為它是 Absolics 的契約代加工，受 Absolics 對外宣稱的 IP 範圍庇護
- **護城河三層**（弱）：
  - **客戶 lock-in**：Absolics 獨家供應商（2024 至 2026-03），三年 process tuning + cleanroom 設置 = 替換成本不低
  - **panel-level know-how**：510×515mm 大尺寸 + sub-10μm 線路精度，韓國境內**少數能量產的 contract fab**
  - **S.E.A. 設備整合**：垂直整合後設備 + 服務同步迭代
- **護城河缺口（致命）**：
  - **沒有自己的雷射 / 改質核心 IP**（vs LPKF 整套 LIDE patent portfolio）
  - **獨家客戶身分剛失去**——2026-03 起 Absolics 轉 dual sourcing
  - **客戶集中度極高**——Absolics 幾乎是唯一被報導的客戶
  - **未上市 + 不可投資**：對台股投資者只能是 thesis 校準對照，無法直接押注
- **競爭格局** vs Absolics dual sourcing 第二位候選：
  - **韓國 Philoptics**：[[Samsung Electro-Mechanics]] 玻璃 pilot line 的 LPKF 直接對手、雷射改質設備已驗證
  - **韓國 Hana Technology**：原電池設備轉戰半導體 TGV、2025-07 揭露已開發核心 TGV 工藝
  - **韓國 PNT**：original 電鍍設備，做 metallization side
  - **德國 [[LPKF]]**：直接賣 LIDE 設備給 Absolics
  - **台灣 [[鈦昇]]**：**極小機率但路徑存在**——若能繞 LPKF LIDE 專利範圍 + 提供 Songdo / 美國 Arizona 代加工能力

## 3. 公司結構快照（As of 2026-06-05）

| 指標 | 數值 / 狀態 |
|---|---|
| 成立日期 | **2021-05** |
| 公司形態 | **私募未上市**（韓國非公開） |
| 總部 | **Incheon, South Korea**（韓國仁川） |
| R&D 中心 | **Gumi**（2021 起） |
| 量產廠 | **Songdo cleanroom**（2024-05 啟用） |
| CEO | **Choi Byung-chul + Shin Jae-ho（雙首長）** |
| 員工數 | **36 人**（2026-04，YoY -5%） |
| 已註冊專利 | **4 件**（韓國，數量極少） |
| 母公司 | **S.E.A.（Semiconductor Equipment, Anyang）+ Fuseimenix** 雙股東 |
| 控股變化 | **2025-11 S.E.A. 取得 majority stake** |
| 唯一已公開客戶 | **[[Absolics]]**（Georgia Covington 廠） |
| 主力產品 | **TGV 雷射鑽孔 + Metallization (PVD) 一站式代加工** |
| 加工規格 | **510×515mm panel、sub-10μm 線路** |
| 業界首發 | **2024-05** 世界首個量產半導體玻璃基板（自我宣告） |
| 募資狀態 | **Series A**（~2024-Q3 估算，1.9 年前）|
| 自我宣告 valuation 目標 | **KRW 1 兆（USD 720M）**——成立 3 年內的口頭目標，**未驗證** |

### S.E.A. 母公司快照（推估垂直整合架構參考）

| 指標 | 數值 |
|---|---|
| S.E.A. 成立 | **~2010**（15 年前） |
| S.E.A. CEO | **Jaeho Shin**（前三星貿易部門 leader）|
| S.E.A. 公開狀態 | **未揭露**（疑似私募、未列韓國 KOSDAQ） |
| S.E.A. 2024 營收 | **USD 80M**（89% 從美國市場） |
| S.E.A. backlog | **USD 47M** |
| S.E.A. 2024-2025 成長預估 | **+30%** |
| S.E.A. 2026-2028 成長預估 | **3× 年成長** |
| S.E.A. 員工 | **~280 人**（半韓半海外） |
| S.E.A. 韓國四廠 | **Gumi R&D + Jeungpyeong production + Dongtan sales + Anyang HQ** |
| S.E.A. 海外廠 | **Malaysia 1 廠** |
| S.E.A. 累積出貨 | **550+ 台**生產設備（含太陽能、PCB、FPD、半導體） |

### Re-rate 三角形（不適用）

**F&S Electron 不可直接投資**——未上市 + 未揭露財報 + 無 ADR。Re-rate 三角形對此 entity 沒有意義，僅供結構性了解。S.E.A. 母公司同樣未揭露公開財務細節，無法投資對標。

### ✅ 結構性 thesis catalysts

- **S.E.A. 垂直整合（2025-11）**：設備 + 服務雙層收入，理論上提升 unit economics
- Absolics Phase 1 2026 量產正式 ramp → F&S Electron 訂單**可能在 2026-03 合約到期前先衝一波**
- **2024-05 業界首發已驗證 panel-level TGV 量產可行**，可複製到後續 Korean 客戶（[[Samsung Electro-Mechanics]] 不會用 F&S Electron，但 LG Innotek、Hana 可能會找 contract fab 補位）

### ⚠️ 結構性風險

- **Absolics 獨家合約 2026-03 到期 = thesis 最大威脅事件**——若 Absolics dual sourcing 讓 F&S Electron 從 100% share 變 50%，營收**直接腰斬**
- **客戶極度集中**——Absolics 幾乎是唯一已公開客戶
- **無核心 IP**——技術門檻來自 process tuning + S.E.A. 設備，但其他韓國設備商（Philoptics、Hana、PNT）都在追趕
- **公司規模迷你**（36 人、Series A 階段）——擴大 panel size 或量產 ramp 都有 execution risk
- **2025 員工 YoY -5%**——可能反映 Absolics Phase 2 暫延的下游需求壓力傳導
- **未上市無法投資**——對台股投資者只能是「了解 Absolics 鏈生態」的對照組

## ⭐ 對 [[鈦昇]] / 台廠 TGV 設備鏈的意義

### 鈦昇若想拿 Absolics dual sourcing 第二位 slot 的**四道障礙**

| 障礙 | 嚴重度 | 說明 |
|---|---|---|
| **IP 戰** | 🔴 binary risk | 鈦昇若雷射改質工法被認定落入 [[LPKF]] LIDE 專利 claim 範圍，Absolics 不可能採用（Absolics 是 Intel licensing 受惠者，不會冒 IP 風險）。EPO 2025-03 + KPCA 2025-09 + 中國執法已三線確認 LIDE 有效 |
| **地緣** | 🟠 high | Absolics 是「韓國 SK 集團 + 美國 Georgia 廠 + AMAT + CHIPS Act + NIST」的政治經濟組合，**第二供應商優先韓國本土**（Philoptics、Hana、PNT、LG Innotek）以維持供應鏈韓系完整性。台廠進場需克服「為什麼選台廠不選韓廠」的政治阻力 |
| **技術差距** | 🟡 medium | F&S Electron 已驗證的 510×515mm panel + sub-10μm 規格鈦昇能否對接是未知（鈦昇是「**設備供應商**」而非「**contract fab 玩家**」，業務模型不同）。若鈦昇做 設備 → Absolics 自做 fab，路徑可行；若 Absolics 要 contract fab 服務，鈦昇沒有這個能力 |
| **產能 + 客戶優先序** | 🟠 high | 鈦昇本身 anchor 是 [[Intel]] Clearwater Forest（2026 H2 量產），台積電 CoPoS pilot 也是 2026 同期。Absolics 即使做 dual sourcing 也要等到 2027 Q2+ 才有 second supplier 的真實量產需求。鈦昇可能會把產能優先給已 sign-off 的 Intel/TSMC 鏈 |

→ **總結**：鈦昇拿 Absolics second source slot **機率 < 15%**。最大障礙是 **IP 戰**（binary）+ **地緣**（高）。即使技術做出來、即使韓國本土三家追趕者都 yield 卡關，Absolics 仍可能選 [[LPKF]] LIDE 設備直接買進 + 自做加工（dual sourcing 的「dual」不一定指供應商國別，可能指 in-house + 外包雙軌）。

### 2026 Q1/Q2 追蹤訊號

| 時點 | 訊號 | 重要性 |
|---|---|---|
| **2026 Q2 法說會** | SKC（KRX: 011790）二季報是否揭露 Absolics second TGV supplier 名單 | 🔴 binary |
| **2026 Q2-Q3** | TrendForce / The Elec / etnews 等是否揭露 dual sourcing 第二位是 LPKF / Philoptics / Hana / PNT 之一 | 🔴 binary |
| **2026 Q3** | F&S Electron 員工人數（thevc.kr 可查）是否反彈或進一步衰退—反彈代表 dual sourcing 後仍維持訂單 | 🟠 high |
| **2026 H2** | Absolics Phase 2 擴產是否重啟（60,000-72,000 m²/年），重啟代表 F&S Electron 仍是核心供應商之一 | 🟠 high |
| **2026 H2** | S.E.A. 海外擴張（特別美國 Georgia 在地工廠設立傳聞）——若 S.E.A. 在 Georgia 設廠 = 確認 F&S Electron 角色維持 | 🟡 medium |
| **2026 H2** | 鈦昇法說會是否提 Absolics / SK 集團接觸 | 🟡 medium（極低機率但要追蹤）|
| **2027 Q1** | Absolics 公開 AMD MI400 量產的供應商鏈組合是否仍含 F&S Electron | 🔴 binary |

### 五軸評分（對 [[鈦昇]] / 對台廠設備）

⚠️ **注意**：F&S Electron 是 **contract fab 玩家**而非設備商，五軸框架（路線敏感/站別關鍵/耗材性/IP 護城河/客戶分散）對「設備商」設計，套用 contract fab 玩家會失準。以下評分**僅供 thesis 校準**，不要直接拿來跟 [[LPKF]] / [[Disco Corp]] / [[鈦昇]] 等設備商比較。

| 軸 | 分數 | 說明 |
|---|---|---|
| 路線敏感（embedding/non-embedding） | 3/5 | 跟 Absolics 雙軌走、適應力中等、但無自主路線決定權 |
| 站別關鍵（製程鏈位置） | 4/5 | 卡 TGV 鑽孔 + Metallization 兩站合一、**panel-level 工藝整合稀缺** |
| 耗材性（重複性需求） | 4/5 | contract fab 服務 = 每片 panel 都要收費、本質上類耗材 |
| IP 護城河 | 1/5 | **無自有核心專利**（僅 4 件韓國註冊）、技術仰賴 S.E.A. 設備 + Absolics 規格 |
| 客戶分散 | 1/5 | **Absolics 幾乎獨家客戶**、合約 2026-03 到期 = 一旦 dual sourcing 完成，立即面臨 50%+ 訂單流失風險 |

**F&S Electron 五軸 13/25**——比 [[Absolics]] 16/25 低，與五軸框架對未上市 contract fab 玩家的失準有關。**比較有意義的是「客戶分散 1/5」這個極端風險訊號**——對任何想拿 Absolics second source slot 的玩家而言，F&S Electron 之所以失去 100% share 就是因為**客戶高度集中導致 Absolics 議價權的反向放大**。鈦昇若拿到也會掉進同樣陷阱。

## 跟其他 wiki 概念連結

- [[TGV 製程鏈圖譜]] **第 1 + 2 站合併** 唯一 panel-level contract fab 玩家
- [[Absolics]]：**唯一客戶**（2024-2026-03 獨家、2026-03 後 dual sourcing）
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]：F&S Electron 走 Absolics 採用的雷射改質 + 化學蝕刻路線（[[Intel]] licensing 受惠路線）
- [[控制點轉移（投資版）]]：F&S Electron **不在控制點**——它是「Absolics 的 contract fab」，控制點在 [[Absolics]] 對下游 fabless（AMD/AVGO/AWS）的綁定，不在 F&S Electron 對 Absolics 的服務
- [[賣水人選股邏輯（投資版）]]：F&S Electron **不是賣水人**——它服務「賣水人 + fab 玩家」（Absolics）的代加工，本質上是 OSAT-like 模式而非賣水
- [[市場四階段：懷疑／驗證／共識／反轉]]：F&S Electron 的失去獨家 = panel-level glass interposer 賽道「驗證 → 共識」的關鍵 inflection——Absolics 已 derisk 到敢轉 dual sourcing 證明賽道已通過商業化驗證
- [[半導體基礎建設化]]：F&S Electron 不會自己擴成基建級玩家（規模太小、無 IP、客戶集中），但**它的存在證明韓國本土 contract fab 玩家可填補 fab 之間缺口**
- [[公司 Entity 模板（Step 1-3 三段式）]]：本 entity 走「foreign competitor、未上市」變體；Re-rate 三角形不適用，改用「公司結構快照」+「Catalysts/Risk」分段

## 相關連結

- [[Absolics]]（唯一客戶 + 合約到期事件中心）
- [[Samsung Electro-Mechanics]]（韓國同國 panel-level 對手平台、不會選用 F&S Electron）
- [[LPKF]]（設備路線可能直接取代 F&S Electron 的潛在第二位）
- [[Disco Corp]]（切割設備供應方、下游夥伴）
- [[Corning]] / [[AGC]] / [[SCHOTT]]（上游玻璃材料供應）
- [[鈦昇]]（理論可拿 Absolics second source slot 但 IP + 地緣 + 商業模式錯位三重障礙）
- [[雷科]]（同台廠設備鏈，不直接競爭 contract fab 賽道）
- [[Intel]]（Absolics licensing 來源、F&S Electron 反射性 IP shield）
- [[TGV 製程鏈圖譜]]
- [[TGV 路線分歧（雷射改質 vs 雷射打孔）]]
- [[控制點轉移（投資版）]]
- [[公司 Entity 模板（Step 1-3 三段式）]]
- [[sennn.nnna]]

## Source URLs

- THE VC F&S Electronics 企業檔案: https://thevc.kr/fnselectron
- THE VC Absolics 企業檔案: https://thevc.kr/absolics
- etnews 業界首發量產 TGV (2024-05-01): https://www.etnews.com/20240501000145
- Worldfolio S.E.A. 玻璃基板設備方案: https://www.theworldfolio.com/news/seas-advanced-equipment-solutions-revolutionizing-glass-substrates-for-semiconductor-packaging/5319/
- Worldfolio S.E.A. interview (Jaeho Shin CEO, 2025-12): https://www.theworldfolio.com/interviews/sea-interview/7233/
- TrendForce SKC 2026-05 mass production push: https://www.trendforce.com/news/2026/05/08/news-skc-said-to-speed-glass-substrate-mass-production-by-year-end-advances-new-non-embedding-tech-for-u-s-client/
- TrendForce 韓國挑戰 Intel 玻璃標準 (2026-04): https://www.trendforce.com/news/2026/04/15/news-korea-challenges-intel-on-glass-substrate-standards-as-absolics-samsung-accelerate-commercialization/
- TrendForce Korea-Based PNT TGV (2025-07): https://www.trendforce.com/news/2025/07/17/news-korea-based-pnt-to-make-inroads-in-chip-glass-substrate-field/
- Digitimes Hana cracks TGV glass: https://www.digitimes.com/news/a20250709PD230/south-korea-glass-substrate-packaging-technology.html
- PhotonCap 15 Companies Glass Substrate Cycle: https://photoncap.net/p/investment-map-15-companies-in-the
- Genzinvestor 0r LPKF Edition glass substrate process line: https://genzinvest0r.substack.com/p/the-glass-substrate-process-line

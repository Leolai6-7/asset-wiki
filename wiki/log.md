# Operation Log

每次 ingest / update / lint / query 的紀錄。

## 2026-06-04
- init: asset-wiki created (mirror of llm-wiki, 財經適配)
- cp: 40 raw materials migrated from llm-wiki/raw (Tier 1 宋分 24 + Tier 2 產業 3 + Tier 3 AI 行業 13)
- ingest: concept [[跳出個股看三層：產業、目的、供應]]（Leo 帶入金句，來源不詳）
- ingest: **第一波**骨架 7 篇 raw（6 備忘錄 + Notes 合輯）→ 14 concept + 6 entity + 7 summary
  - concepts: FCF 拐點、CapEx 見頂辯論、AI 通縮三路徑、效率→安全切換、Forward PE 估值法、DCF vs PE、PE 壓縮公式、PEG Ratio 警告、散戶 vs 機構買股差異、HBM iPhone moment、修正三階段、複利測試、三個風險指標
  - entities: 宋分（美股送分題）、NVDA、AVGO、AMD、AMZN、Meta
  - summaries: 6 篇備忘錄 + Notes 合輯
- ingest: **第二波**教學系列 17 篇 raw → 12 concept + 1 entity + 17 summary
  - concepts: 預期差、市場四階段（懷疑/驗證/共識/反轉）、資訊擴散四階段、確定性門檻模型、看錯三類型、PB 估值法（記憶體週期）、風險預算、五層損益表（營業槓桿）、半導體基礎建設化、抗跌清單、被動賣壓 vs 主動買盤、10-K 閱讀法（分析師底層 #1）
  - entities: TSMC
  - summaries: 宋分 #01–#23（編號 01-05, 07-08, 10-11, 13-15, 17-18, 20-21, 23）
- ingest: **第三波**產業/個股 + AI 行業 16 篇 raw（agent team 並行）→ 12 concept + 10 entity + 16 summary
  - method: 4 個 subagent 並行（半導體供應鏈 / AI 資安 / AI 模型公司 / 開源戰略），每個 agent 負責讀 raw + 寫 summary + 提案 entity/concept；主 agent 合併提案落地
  - concepts: 控制點轉移（投資版）、接口控制權、開源作為武器（投資版）、賣水人選股邏輯（投資版）、AI 融資結構（條件資本）、循環投資（CSP-Model 互鎖）、AI 訂閱制 unit economics、資本重分配（從人力到算力）、政府風險溢價（AI 公司）、AI 廣告信任危機、CPO 供應鏈圖譜、AI 資安攻防成本曲線
  - entities: OpenAI、Anthropic、Microsoft、Google、DeepSeek、幻方量化、華為、Intel、SiTime、MCP（Model Context Protocol）
  - summaries: 半導體 3 + AI 資安 4 + AI 模型公司 5 + 開源戰略 4 = 16 篇
- **40 篇 raw ingest 全部完成**：累計 38 concept + 17 entity + 40 summary
- 下一步：延伸 entity ingest（CPO 光引擎三巨頭、AI 資安賽道、電力供應鏈、影片 AI、Musk 帝國），詳見 index.md「待 ingest 延伸」段落

## 2026-06-05
- ingest: standardize 公司 entity 格式
  - CLAUDE.md 加入「公司 Entity 三段式（強制格式）」段落（在「文章格式」下）
  - 新 concept [[公司 Entity 模板（Step 1-3 三段式）]]
  - 三段式：1. 一句話定位（sticky） / 2. 三層 thesis（sticky） / 3. 財務狀態快照（snapshot，必標日期）
  - 不寫進 entity：此刻 PE、預期差、進場價、退場條件、推薦判斷
- ingest: **第四波 TGV 玻璃通孔賽道**（素材驅動 + agent team 並行）
  - method: 1 raw（sennn.nnna 原文）+ 3 subagent 並行快篩 7 家台股 + 1 deep-research workflow（failed，作廢）
  - subagent 任務：每 agent 處理 2-3 家公司，產 mini-snapshot（TGV 鏈位置 + 一句話定位 + 三層 thesis 草稿 + 深入建議）
  - 主 agent 合併報告 → Leo 選定 ✅ 4 家深入（鈦昇/雷科/弘塑/辛耘）+ ⚠️ 3 家觀察（德律/東捷/敘豐）
  - concepts: 3 個（TGV 製程鏈圖譜 / TGV 路線分歧 / 玻璃基板與 FOPLP 賽道）
  - entities: 5 個（sennn.nnna KOL + 鈦昇 / 雷科 / 弘塑 / 辛耘）— 全部走 [[公司 Entity 模板（Step 1-3 三段式）]]
  - summaries: 1 篇（原文 + 7 家驗證 + bull/bear thesis）
  - ⚠️ ticker 修正：原 sennn 文 + Leo 口頭「敘豐 6814」是錯的（路迦生醫），正確為 3485
  - 漏網：**萬潤**（CoWoS 三傑第三家，subagent 帶出）— 待補
  - 累計：42 concept + 22 entity + 41 summary
- ingest: **萬潤 6187 補完**（CoWoS 三傑第三家）— 單 entity 補建
  - entity [[萬潤]]（6187.TW）：WoS 後段點膠+散熱+AOI 近壟斷，[[TSMC]] CoWoS / [[ASE]] 客戶
  - Re-rate 三角形 2/4（毛利率 60% → 52% 稀釋是真實警訊；訂單能見度 2027 與 CPO 第二曲線是 thesis）
  - 高盛目標價軌跡：365（看空）→ 800（轉買）→ **1,800（買進，三次大幅上修）**
  - CPO 矽光子設備已進入客戶 sample testing，高盛預估 CPO 占比 2026 3% → 2028 69%
  - 三傑差異化定稿：弘塑（跨多站濕製程 + 化學品消耗）/ 辛耘（中段 + 晶圓再生 + 代理三條腿）/ **萬潤（WoS 後段近壟斷、訂單同步 CoWoS 出貨）**
  - 同步更新：index.md（移出待 ingest 清單）、TGV 製程鏈圖譜（標註已補）
  - 累計：42 concept + 23 entity + 41 summary
- ingest: **TGV 國際對手 2 家**（thesis 校準對照）— WebSearch 驅動建檔
  - entity [[LPKF]]（XTRA: LPK，德國）— LIDE 雷射改質專利擁有者，鈦昇路線祖宗
    - 市值 EUR 536-585M，52 週 EUR 5.35 → 30.00（5 倍 thematic 行情）
    - 2025 全年營收 EUR 115.3M（YoY -6.2%），Q1 2026 營收 EUR 17.1M（YoY -32.4%）但 book-to-bill 1.4 ✅
    - 專利戰略 escalate：EPO 2025-03 確認 + KPCA 2025-09 + 中國執法
    - Vitrion 自有 foundry = 設備 + 服務雙位
    - UTI / Unimicron / Fraunhofer 客戶鏈
  - entity [[Disco Corp]]（6146.JP）— 切割研磨 60-70% 壟斷，雷科直接威脅
    - 市值 JPY 7.59T（NT$1.5 兆，**對雷科 1200 倍體量差**）
    - FY2026 營收 JPY 436.89B（+11%），Q1 FY2026 指引 +18% / +20%+ 雙位數加速
    - Re-rate 三角形 **4/4**（已是 quality compounder，與鈦昇/雷科 0-2/4 對比強烈）
    - **DFD6080（2025-12 發表）支援 glass substrate + 樹脂 + lead frame 多材料、1.8 kW 主軸**
      → **Disco 正式插旗玻璃基板切割**的明確訊號
    - Stealth Dicing = SiC/GaN 事實標準工法
  - 同步更新：index.md（新增「TGV 國際對手」分類 + 待 ingest 清單打勾）
  - 思考重點：兩家國際對手都是「IP / Install Base / 估值」三維壓制，台廠 thesis 校準有 binary 風險
  - 累計：42 concept + **25 entity** + 41 summary
- ingest: **⚠️ 觀察 3 家升級 entity**（德律 3030 / 東捷 8064 / 敘豐 3485）— WebSearch 驅動建檔
  - entity [[德律]]（3030.TW）— AOI 全球第一 + AXI 坐二望一，NVIDIA Metropolis 智慧工廠夥伴
    - 市值 NT$963 億 / PE 35（同業均 42 → 折價）/ 2026 Q1 EPS 3.5 元（YoY +43%）
    - 毛利率 60.27%（與致茂 60.8% / 牧德 59.86% 並駕齊驅）
    - 業務：自動光學檢測 75% + 電路板測試 25%，網通伺服器佔比 10%→36%
    - **Re-rate 三角形 4/4 滿**：本業（AI 伺服器檢測）已 Re-rate 完成，但 **TGV 純度低（10-15%）** → 故事是「先進封裝檢測」而非 TGV 純題材
    - 透過轉投資歐美科技（OmniMeasure）卡 2026 後 TGV 量產（option value）
    - 競爭：擊敗 Koh Young 拿 AOI 全球第一、AXI 追日本 Omron
  - entity [[東捷]]（8064.TWO）— 面板廠轉型半導體+先進封裝整線設備
    - 市值 NT$290-318 億 / PE 74（已 price in 大量轉型期權）
    - 2026 Q1 EPS 0.35 元（YoY **+153%**，轉虧為盈）/ 2025 Q4 毛利率 38.45%（vs 2023 約 22%）
    - **志聖 2026-03 以 NT$50.88/股認購 2 萬張私募 = NT$10.18 億，持股 10.82% 成單一最大股東**
    - 梁又文（志聖總經理）接任董座、嚴瑞雄交棒 → 治理結構大改造
    - G2C+ 聯盟整線：志聖（壓膜+鍍膜）+ 均豪+均華（搬運+黃光）+ 東捷（雷射）+ 富臨（PVD）
    - TGV 雷射改質設備規格：每秒 10,000 孔 + ±5μm 精度（2026 Touch Taiwan 展出）
    - 已切入日月光、力成、群創（FOPLP）；**北美 IDM 直接訂單未揭露**（關鍵缺口）
    - **Re-rate 三角形 3/4 滿**：故事最完整、轉型已反映在數字、但 PE 74 + 北美未揭露
  - entity [[敘豐]]（3485.TWO）— 高階 IC 載板濕製程設備龍頭（剛上櫃）
    - 上櫃日 2026-05-06、市值 NT$138 億 / PE 56.97 / P/B 9.60
    - 主業 FCBGA/ABF 載板濕製程設備（**>90% 營收**）
    - 2026 Q1 EPS 1.69 元（YoY -30.17%）/ 毛利率 53.21%（vs 2025 全年 56% 含存貨回沖）
    - 訂單能見度到 **2027 年**（載板三雄 CapEx 調升受惠）
    - **客戶集中極高**：欣興 + 長安科技合計 **>90%**（binary risk）
    - VSP 複合蝕刻機（薄玻璃 <0.1mm 夾持系統）已在客戶端量產 + 台灣發明專利
    - MOON 軟體 3D 翹曲補償已打入「台系封測 + 美系晶片供應鏈」（**未具名揭露**）
    - **Re-rate 三角形 1/4 滿**：剛上櫃 + 客戶集中 + Q1 EPS 衰退 → 適合等 TGV 客戶名單揭露再加碼
  - 三家差異化一句話：**德律 = 檢測層中性受惠的「本業已 Re-rate 完成」option call**、**東捷 = G2C+ 聯盟整線的「治理改造 + 業務 mix 翻倍」轉型故事**、**敘豐 = 載板濕製程龍頭的「客戶集中 + 剛上櫃」追蹤候選**
  - 同步更新：index.md（移出待 ingest 清單、加入 TGV 製程鏈台股段）
  - 累計：42 concept + **28 entity** + 41 summary
- ingest: **手機 / 邊緣晶片端 TGV/FOPLP watchlist concept**（codex P2 盲點補完）— WebSearch 驅動建檔
  - concept [[手機與邊緣晶片端 TGV-FOPLP watchlist]]：Apple/Qualcomm/Samsung/ByteDance/Tesla/xAI/MediaTek 終端 thesis 校準
  - **核心結論：三條獨立採用曲線**
    1. **Data center**（Intel/AMD/Broadcom）2026-2028 TGV 主菜（既有 Tier 1）
    2. **手機高端 + 自研 server**（Apple/Qualcomm/Samsung）FOPLP/FOWLP 已商用、TGV 2027+ 觀察
    3. **邊緣 AI / 新興 ASIC**（ByteDance/Tesla/xAI）binary outcome，可能直跳 TGV/CoPoS
  - ⭐ **Apple Baltra 是第二根 anchor**：2026-04 確認直接向 Samsung Electro-Mechanics 採玻璃基板樣品，TSMC 3nm N3E + chiplet
  - ⚠️ **Samsung Electro-Mechanics 拿 Apple + Broadcom 雙訂單**：韓系玻璃供應鏈卡位完成，對 [[鈦昇]] LIDE 路線是直接威脅
  - ⚠️ **ByteDance 自研 ASIC 封裝路線未公開**：5nm CoWoS 為主，是否走 CoPoS 待 2027 第二代 ASIC 驗證
  - 不押 Tier 2（手機 SoC TGV 採用太慢 + 韓系玻璃卡位風險）；Tier 1 + Tier 3 + Tier 4（鈦昇 CoPoS 入場券追蹤）為投資焦點
  - **新追蹤訊號**：（a）TSMC CoPoS pilot line 2026-06 完成設備供應商名單、（b）鈦昇法說會 TSMC CoPoS / WMCM 認證進度、（c）雷科 Intel Terafab design-in、（d）ByteDance 第二代 ASIC 規格
  - 待 ingest 延伸：力成 6239 / 日月光 3711 / Samsung Electro-Mechanics 009150.KS
  - 同步更新：index.md（TGV 段新增）
  - 累計：**43 concept** + 28 entity + 41 summary

## 2026-06-05 — ingest: 先進封裝 OSAT 三家整合方 entity

- ingest: **3 家 OSAT entity**（日月光 ASE 3711 / Amkor AMKR / Powertech 力成 6239）— WebSearch 驅動建檔
  - 對應 TGV 製程鏈下游關鍵節點：**封裝整合誰做？**——三家 OSAT 是 [[TGV 製程鏈圖譜]] 8 站設備與化學品的下游客戶
  - 觸發角度：[[CoWoS 三傑差異化]] 講賣水人三家位置，但**整合方位**（誰用這些設備做產線）尚未覆蓋
  - 三家分工：
    1. **[[日月光 ASE]]**（3711.TW / NYSE: ASX）— 全球最大 OSAT + CoWoS 委外雙頭 + SPIL/NVDA CoWoP + TPK/2026 Q3 TGV pilot
       - 市值 NT$1.57 兆 / PE 57 / 2026 Q1 EPS NT$3.24（YoY +85%）/ 2026 LEAP 營收 guide **>$3.5B（YoY +118%）**
       - 2026 資本支出 **$85 億美元**（2 次上修，21% 增幅）
       - ATM 毛利率 26-27%（vs 同業 ~22%）/ LEAP 佔比 14%（2026）→ 33%（2027）= 第二波 re-rate
       - **Re-rate 三角形 4/4 滿**（跟 [[弘塑]]、[[德律]] 並列）
       - 跟 [[TSMC]] 是「**協力 + 分工 + 局部競爭**」三層關係（拿 60-80k CoWoS wafer 委外）
       - 多軌押注：CoWoP / FoCoS / FOPLP / TGV 四軌並進
    2. **[[Amkor]]**（NASDAQ: AMKR）— 美系 OSAT 第二大 + Intel EMIB 三地外包獨家 + Arizona $2B 廠（CHIPS Act）+ 玻璃基板「3 年內商業化」
       - 市值 $12.03B / 股價 $75.62 / 2026 Q1 EPS $0.33（beat consensus $0.22 by 50%）
       - 2026 Q1 營收 **$1.685B（YoY +27%）** = record / Q1 gross margin 14.2%
       - 2028 目標營收 $9.0B / 2030 $11B+ GM 22%+（Arizona ramp）
       - **Re-rate 三角形 2/4**（毛利率 14.2% 短期低 + OpEx Arizona 折舊壓力前置）
       - 跟 [[TSMC]] 是「**協力 + 補位**」二層關係（拿 180-190k CoWoS wafer = ASE 3 倍）
       - 跟 [[Intel]] EMIB 三地外包獨家：Korea Songdo K5（已量產）→ Portugal → Arizona
       - 玻璃基板「3 年內商業化」（Yoo Dong-soo 公開、暗示 2028-2029）
    3. **[[Powertech 力成]]**（6239.TW）— 台廠 FOPLP 主力 + 記憶體 HBM 龍頭（Micron 獨家）+ AMD Zen 7「**業界首例 2.5D panel-based interconnect**」共認證
       - 市值 NT$2,634 億 / 股價 NT$335-343（5 月 22 漲停 NT$283 → 6 月突破 NT$335）
       - **PE 13.7 倍（fwd）= 三家 OSAT 中最便宜、跟 [[弘塑]]/[[萬潤]] 60-67 倍差 5 倍**
       - 2026 Q1 營收 NT$213.14 億（YoY +37.6%）= record / EPS NT$2.50（YoY +58%）/ 毛利率 19.4% → Q2 guide >20%
       - FOPLP 良率 **>90%（接近 95%）**、2026 H2 客戶認證、2027 中量產
       - **3D 光引擎** EIC+PIC 整合驗證完成、**2026 年底量產**（CPO 真實 design-in）
       - 2026 資本支出 NT$500 億（從 NT$400 億 +25%，朝 NT$700 億方向）
       - **Re-rate 三角形 3/4**（OpEx Arizona 廠房友達接收前置）
       - 跟 [[TSMC]] 是「**分工 + 客戶切割**」二層關係（最 pure-play AI panel-level）
  - **三家 TGV / 玻璃中介層 design-in 強度排序**：Amkor > ASE > 力成
    - **Amkor**：跟 Intel 玻璃基板計畫**直接綁定 packaging 端**（玻璃 design-in 最強）
    - **ASE**：跟 TPK 中壢 pilot line（2026 Q3）= 第一條台灣 TGV 整線 + 跟 SPIL 主導 NVIDIA CoWoP
    - **力成**：FOPLP 不一定綁玻璃 + AMD Zen 7「2.5D panel」首例 + 3D 光引擎用 TSV（不是 TGV）
  - **跟 [[TSMC]] CoWoS 的關係**：
    - **ASE = 「協力 + 分工 + 局部競爭」三層**（CoWoS 60-80k 委外 + CoWoP 替代路線 + FoCoS-Bridge 同層）
    - **Amkor = 「協力 + 補位」二層**（CoWoS 180-190k 委外大頭 + 美國端區域補位）
    - **力成 = 「分工 + 客戶切割」二層**（panel-level vs wafer-level + AMD vs NVDA） — **最獨立於 TSMC**
  - **「TGV 量產真正受惠者」**（賺整合服務費）排序：
    - **第一**：**[[Amkor]]**——拿到 Intel 玻璃基板 packaging 端獨家（2028-2029 量產 anchor）+ TSMC CoWoS 委外 180-190k
    - **第二**：**[[日月光 ASE]]**——跟 TPK TGV pilot + SPIL/NVDA CoWoP + LEAP 2027 佔比 33%
    - **第三**：**[[Powertech 力成]]**——FOPLP 主軸（不必綁玻璃）+ AMD Zen 7 認證 + 3D 光引擎
    - 三家**都是設備買方**（給三傑、[[鈦昇]]、[[雷科]]、[[LPKF]]、[[Disco Corp]] 等下游訂單）+ 整合方
  - **bull / bear thesis**：
    - **Bull（三家整合方）**：TSMC CoWoS 產能瓶頸延續至 2027 + 玻璃基板 2027-2028 量產 + AI CapEx 持續 → 三家整合方都吃
    - **Bear（三家整合方）**：（a）TSMC 自己擴 CoWoS-L 把外包收回、（b）玻璃基板量產延後（如 2030+）、（c）AI CapEx 拐點（CSP 三大 cooling）→ 整合方先吃苦
    - **Bull（個股）**：
      - ASE：LEAP 2027 33% 佔比 + Q1 EPS YoY +85%
      - Amkor：Intel EMIB 獨家 + Arizona 2027 H2 量產 + CHIPS Act
      - 力成：FOPLP 良率 95% + AMD Zen 7 認證 + Micron HBM 獨家 + **PE 13.7 折價最大**
    - **Bear（個股）**：
      - ASE：PE 57 已部分 priced in + CapEx $85B 折舊壓力
      - Amkor：GM 14.2% 結構性低 + Arizona 2027-2028 ramp 風險
      - 力成：客戶集中度高（Micron + AMD + Intel 60%+）+ 記憶體週期性
  - 同步更新：index.md（新增「標的：先進封裝 OSAT」段、移出待 ingest 清單）
  - 累計：43 concept + **31 entity** + 41 summary

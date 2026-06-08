# Operation Log

每次 ingest / update / lint / query 的紀錄。

## 2026-06-08（continued）
- ingest: **codex P1-5 + P1-6 兩個盲點交叉 concept 落地（純設計，不建 entity）**
  - concept [[HBM4E × Glass Interposer × TGV 交會]]（P1-6 補位）—— 把散落在 [[AI 記憶體結構性供給短缺]] Tier 3 與 [[玻璃基板與 FOPLP 賽道]] 時間線的「2028 三戰場 anchor」收束成單一交叉概念
    - 三戰場：HBM4E（SK Hynix/Samsung/Micron 2027-2028 量產）+ TSMC CoPoS 玻璃中介層（pilot 2026-06、ramp 2028-29）+ 玻璃載板（Absolics 2026 H2 / SEMCO 2027 H2 / Intel Rio Rancho 2030）
    - 物理鎖死關係：HBM4E 16-Hi 需玻璃中介層撐良率、玻璃中介層需 TGV 八站、TGV 需玻璃載板客戶。三戰場必須同時 ramp，缺一個整 stack 推遲
    - alpha 分層：短週期（2026 H2-2027 H1）= Absolics ramp / CoPoS pilot / HBM4E first race；中週期（2027 H2-2028）= complete stack 溢價 / SEMCO 韓系閉環；長週期（2028+）= Intel Rio Rancho 美洲玻璃鐵三角 / TGV 八站全鏈
    - 5 個風險：HBM4E 時程錯位、Hybrid Bonding 跳過 TGV、玻璃翹曲撞良率牆、Intel Rio Rancho 卡關、NVDA 路線變更、反壟斷
    - 觀察訊號：10 個季度級 anchor（2026 Q3 → 2030）
    - WebSearch 8 query 驗證（HBM4E 量產 / CoPoS 時程 / Intel 2030 / Absolics / Samsung HBM5）
  - concept [[NVDA 網路 stack map]]（P1-5 補位）—— 釘死 NVDA 7 chip + NVLink Fusion 的層級關係
    - Rubin 平台 7 chip：Vera CPU + Rubin GPU + NVLink 6 Switch + ConnectX-9 SuperNIC + BlueField-4 DPU + Spectrum-6 Ethernet Switch + Quantum-X800/Photonics InfiniBand Switch + Spectrum-X Photonics + Spectrum-XGS + NVLink Fusion
    - scale up / scale out / scale across × NIC / Switch / OLS / DCI 一張表釘死
    - 回答 codex 4 個反饋：CX9 = ConnectX 7→8→9 命名後續（非新產品線）、Spectrum-X (Ethernet/Cloud) vs Quantum-X (InfiniBand/HPC) 客戶差異、NVDA 內部僅「銅 vs Photonics CPO」世代躍遷無真直接競爭、NVDA 不做 OLS → CIEN/NOK 互補非競爭
    - NVDA vs 對手：scale up vs UALink、scale out vs AVGO Tomahawk 6 + Marvell Teralynx、scale across 與 CIEN Hyper-Rail/NOK Multi-Rail 互補
    - CPO 第 1-2-4-8 層 anchor 客戶位置確認
    - WebSearch 7 query 驗證（ConnectX-9 / Spectrum-X / Quantum-X / NVLink 6 / Spectrum-XGS / BlueField-4 / NVLink Fusion）
  - 同步：index.md 在「光通訊 / DCI」加 [[NVDA 網路 stack map]] entry、在「TGV / 玻璃基板賽道」加 [[HBM4E × Glass Interposer × TGV 交會]] entry
  - 兩個 concept 都是純交叉設計，未建 entity（受惠玩家全部已存在於 wiki）
- ingest: **Serenity 重押光電 5 家逐一交付 — AAOI 第 1 家落地**
  - entity [[AAOI]]（NASDAQ: AAOI / Applied Optoelectronics）— **Bottleneck Theory 第 5 層 + 跨第 4 層 ELSFP**
  - 一句話定位：全球少數 laser chip → epi → 模組組裝全垂直整合的光模組廠、北美 hyperscaler 唯一非中國 1.6T LPO 量產商（Sugar Land Texas）
  - Serenity reasoning：公開 7x 報酬、原推「frontran institutions with photonics with names like $AAOI, $AXTI, $LITE, $COHR」、vertical integration 純度 = 第 5 層最深 chokepoint、ELSFP 跨第 4 層 hedge
  - 五軸 **18/25**（路線 5 滿、客戶分散 1 慘）vs IQE 17 / LITE 19 / COHR 19
  - Re-rate 三角形 1-2/4（營收已驗證 ✅、毛利 / OpEx / 營業利益仍 thesis）
  - 催化：Q1 2026 +51% YoY、$200M 1.6T 訂單、CEO 揭露 actual demand $1.4-1.5B、Sugar Land 2027 擴 350%
  - 風險：客戶集中 Top1>40%、Top2>70%、Forward PE 226.58、GF Value 估值 912% 高估
  - 同步：index.md 新增「Serenity 重押光電 5 家（第七波）」段落
- ingest: **Serenity 重押光電 5 家逐一交付 — TSEM（Tower Semiconductor）第 2 家落地**
  - entity [[Tower Semiconductor]]（NASDAQ: TSEM）— **Bottleneck Theory 跨第 4-5 層 SiPho PIC foundry**
  - 一句話定位：全球領導級 specialty foundry、矽光子 PIC foundry 龍頭、AI 光通訊鏈跨層 SiPho 平台「賣水人之中的賣水人」（Migdal Haemek 以色列）
  - Serenity reasoning：與 Soitec ($SOI) 並列「**Safest Longs**」defensible compounder、低 beta、跨第 4-5 層多客戶 anchor（NVDA + Coherent + Marvell + Cisco + Lumentum 同時綁定）
  - 五軸 **22/25**（耗材 + 客戶分散雙滿）vs AAOI 18 / IQE 17 / LITE 19 / COHR 19 = **5 家中最高分**
  - Re-rate 三角形 **3/4**（營收 + 毛利 + 營業利益實質驗證、OpEx 偏重但被 SiPho 抵銷）
  - 催化：2026-02 NVDA 1.6T SiPho partnership、2026-03 Coherent 400Gbps/lane demo、Q1 2026 SiPho +3x YoY、客戶預付款 $290M、Q2 guidance +22%、Intel 2024 起角色反轉變 300mm 容量供應商
  - 風險：NVDA / TSMC / GF SiPho 擴張、以色列地緣風險、Forward PE 69.93 / 12M +580% 估值偏高
- ingest: **Serenity 重押光電 5 家逐一交付 — AEHR（Aehr Test Systems）第 3 家落地**
  - entity [[AEHR]]（NASDAQ: AEHR / Aehr Test Systems）— **Bottleneck Theory 第 6 層 Testing & Qualification 唯一 anchor**
  - 一句話定位：全球少數能做 wafer-level burn-in（WLBI）+ package-level burn-in（PLBI）+ 矽光子早期 burn-in 整合平台、SiC + AI processor + 矽光子三腳鼎立 hyperscaler 設備商
  - Serenity reasoning：原推「**$AEHR +14.28% / 矽光子下個瓶頸的中心、$1.1B、tons of hyperscalers qualifying it / Was kind of undervaluing it**」、Serenity 承認低估
  - 五軸 **20/25**（站別 5 + 耗材 5 雙滿、客戶分散 2 拖累）vs TSEM 22 / LITE 19 / COHR 19 / AAOI 18 / IQE 17 = **5 家中第二高**
  - Re-rate 三角形 0-1/4（仍 thesis 階段、bookings $92M+ + Book-to-Bill 3.5x+ anchor 強、但實質營收 ramp 尚未驗證）
  - 催化：Q3 lead AI accelerator $14M follow-on（9 顆 300mm wafer 平行）+ Q3 lead silicon photonics customer follow-on（sample → 量產）+ Q3 Taiwan SiC FOX-XP + Q4 $41M record AI 訂單 + Q4 預期回到 non-GAAP profitability
  - 風險：FY 2026 H1 ON Semi 下滑營收 YoY -44%、Advantest / Cohu 規模競爭、客戶集中、Forward PE 2,106 估值無 anchor
  - 累計：waiting for AXTI/SIVE 落地後總計

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
- ingest: **TGV 玻璃材料三巨頭**（Corning / AGC / SCHOTT，國際）— WebSearch 驅動建檔
  - entity [[Corning]]（NYSE: GLW，美國）— 玻璃材料 + AI 光纖雙引擎
    - 市值 USD 166.1B / Forward PE **55.99**（AI 期權已 price in）/ 2025 全年營收 USD 15.63B（+19.14% YoY）
    - **Glass core substrate 市佔約 25%**（三巨頭中第一梯隊）
    - **Nvidia $3.2B 戰略投資（2026-05-06）**：$500M pre-funded + $2.7B warrants、3 座光纖工廠（北卡+德州）、光連接器產能 10x
    - Meta $6B 光纖長約（2026-01）+ TSMC 台灣廠 CoWoS 玻璃載板合作
    - Hemlock Semiconductor 美國 wafer 廠 2025 Q4 commission、1M wafer/day、2GW/年
    - Advanced Packaging Glass Carriers / Semiconductor Glass Wafers 已商業化
    - 主要 takeaway：**對台廠「背書 thesis、不創造威脅」**——Corning 不做下游 TGV 加工、不搶台廠 8 站設備
  - entity [[AGC]]（5201.JP，旭硝子，日本）— 玻璃 + EUV mask blank + CMP slurry 三軌
    - 市值 JPY 1.19T / Forward PE **14.45**（三巨頭中最便宜）/ 52 週 JPY 4,180 → 8,294
    - FY2024 Electronics 段營收 JPY 364.5B + 營業利益 JPY 54.5B
    - **Electronic Materials JPY 183.6B 首度超 Display**（EUV mask blank 驅動、YoY +50%）
    - **TGV 玻璃規格揭露最完整**：EN-A1 / 20-150μm / 0.1-1.0mm / panel 510×515mm
    - 應用直接點名 Chiplet + CPO substrate + RF
    - low-CTE 硼矽 sheet 供 Intel Arizona pathfinding line
    - 全球僅 3 家 EUV mask blank 供應商之一
    - 主要 takeaway：**Forward PE 14 沒反映 EUV + 玻璃雙引擎 → 潛在 re-rate trigger**
  - entity [[SCHOTT]]（德國非上市，Carl Zeiss Foundation 100% 持有）— HermeS 預製 TGV wafer
    - **無法直接押注**（Foundation 章程禁 IPO）
    - 2024/2025 集團營收 EUR 2.83B / 2023/2024 EBIT EUR 400M / EBIT margin ~14%
    - 半導體業務估算 2025 營收 USD 150-180M（占集團 ~5-6%）
    - **HermeS Glass Wafer with TGV** 2014 起商業化（MEMS 為主、現擴至先進封裝）
    - 超短脈衝雷射 TGV 鑽孔專利（與 LPKF LIDE 不同路徑 → 兩家專利不衝突）
    - 2024-08 成立半導體事業部（Dr. Christian Leirer 領銜、15 年半導體經驗）
    - 2025-01 收購 QSIL GmbH（強化石英玻璃）
    - 主要 takeaway：**對台廠是「TGV 技術可行性 derisk」的對照組**，不是可投資標的
  - **三家在 TGV 玻璃基板 design-in 證據強度排序**：
    1. **Corning**（Nvidia / Meta / TSMC 三巨頭資本綁定 + Glass core 25% 市佔）
    2. **AGC**（規格揭露最完整 + Intel Arizona pathfinding low-CTE sheet + EUV mask blank 半導體深度）
    3. **SCHOTT**（HermeS 已商業化但 chipmaker 大客戶 commitment 未具名）
  - **真正 bottleneck 結論**（Yole 2025 + TrendForce 確認）：**設備 / 加工 ecosystem（LPKF TGV 雷射、Disco 切割、CMP、metrology、carrier cleaning）**——**不在材料端**。Corning + AGC + SCHOTT + NEG 控 90%+ 低 CTE 玻璃配方、供應充足
  - **對台廠 bull thesis**：玻璃材料供應**不會成為** TGV 賽道 bottleneck（三巨頭鼎立 + 韓國 KCC/LX Glass 追趕中）→ 台廠 8 站下游加工生意不受材料端壓縮
  - **對台廠 bear thesis**：但**下游 interposer fabrication（Absolics、Samsung SEMCO、LG Innotek）+ 設備（LPKF、Disco）**才是真正 binary risk；Corning 與 TSMC 直接合作 panel-level 載板可能搶 FOPLP 加工層機會給 [[東捷]] 等台廠
  - **三家對台股設備廠最大訊息**：玻璃材料供應充足、不創造威脅；下游 LPKF（雷射改質 IP）+ Disco（切割壟斷）+ Absolics（KR interposer 量產第一）才是 binary 風險源
  - 同步更新：index.md（新增「TGV 玻璃材料」分類段 + 待 ingest 清單打勾）
  - 累計：43 concept + **34 entity** + 41 summary
- ingest: TGV 國際對手 韓國陣營 entity（subagent 並行）
  - entity [[Absolics]]（SKC 子公司、母公司 KRX: 011790、未上市子公司）— **全球第一條商業化量產玻璃中介層**
    - 母公司 SKC 70.1% + Applied Materials 29.9% 策略入股、Georgia Covington 廠
    - 補貼累積：CHIPS Act USD 75M + NAPMP USD 100M + Georgia 州補貼 + AMAT USD 39M 入股 = USD 200M+ 政府補貼背書
    - **客戶 design-in 揭露排序**（強→弱）：
      1. **[[AMD]]**（最具體）：2026 Q1 起 MI400-series AI accelerator volume sample、Q3 2025 AMD approval announcement、prototype validation 完成
      2. **[[AMZN]] AWS**（中等）：Trainium / Graviton 入測但**quality test 延後**、節奏不可控
      3. **[[AVGO]]/Marvell**（low）：non-embedding 路徑「美國通訊半導體公司」第二代產品線、客戶身分未公開（疑似 AVGO 或 Marvell）
      4. **[[Intel]]**（間接）：2025-08 Intel licensing 開啟、Absolics 是受惠者非客戶
      5. **[[NVDA]]**（未具體）：無公開 design-in
    - 雙軌路線：**Embedding**（玻璃內嵌 IPD 被動元件，AI 高階）+ **Non-Embedding**（純玻璃載板、商業化更快，2026 內可能先量產）
    - F&S Electron 獨家 TGV 設備合約 **2026-03 到期** → 轉 dual sourcing → **第二供應商 slot 空出**（鈦昇潛在窗口）
    - Phase 1 12,000 m²/年完工 + Phase 2 60,000-72,000 m² 暫延（管理層承認 demand 未爆發）
    - SKC 2025 全年淨損 KRW -734B、Q1 2026 OP +76.2B（10 季首正）、Rights Offering KRW 1.17T 募資
    - 主要 takeaway：**對台廠設備是「中性 demand creator」**（不做設備、不做切割），**但對台廠 OSAT 是 Intel/AMD 鏈 fab 服務層分食者**
  - entity [[Samsung Electro-Mechanics]]（KRX: 009150 / 삼성전기）— Samsung 集團 panel-level 載板平台
    - Samsung 集團旗下、與 Samsung Electronics 主體分離上市（**可賣集團外**）→ 拿 Apple Baltra + AVGO 訂單關鍵
    - 市值 **KRW 126.4T（USD 92B）**、Forward PE 78.7、Q1 2026 史上首破 3T 韓元單季營收
    - Q1 2026 Package Solutions 段（FC-BGA）KRW 725B、**YoY +45%**、OP +40%
    - 2026 ABF 載板**全年產能售罄**、客戶名單：Alphabet（Google TPU）+ Tesla + Apple + AWS + AVGO
    - 玻璃基板：Sejong pilot line + Sumitomo Chemical/Dongwoo Fine-Chem JV（2025-11 MOU、2026 H2 簽正式合約）+ 2027 量產目標
    - **Apple Baltra**（AI server chip 代號）glass substrate sample 已交付（2025 至今）—— TSMC N3E 製造、chiplet 架構、2027 量產
    - 與 AVGO Broadcom：Sample 2025 起、Broadcom OpenAI USD 10B 訂單→ 載板需求倍增
    - Samsung **Triple Alliance**：Samsung Display（玻璃加工經驗）+ Samsung Electronics（HBM/Foundry）+ SEMCO（substrate）整合
    - 主要 takeaway：**對台廠設備不直接競爭**（採購 LPKF + Disco），**但對台廠 OSAT 在 Apple/Google/AVGO 鏈是平行存在的規模壓制**
  - **對台廠的核心結論**：
    1. **Absolics 客戶 design-in 揭露排序**：AMD（最具體 volume sample）→ AWS（延後）→ AVGO/Marvell（non-embedding 未公開）→ Intel licensing 受惠 → NVDA 未確認
    2. **SEMCO 對 [[鈦昇]] 是平行存在 + 間接威脅**（採購 LPKF 設備強化 LPKF IP 收入 → 鈦昇 IP 風險上升；fab 服務層搶 Apple/Google/AVGO 鏈 → 台 OSAT 機會被擋）
    3. **韓系自家分裂**：SK 集團 [[Absolics]] vs Samsung 集團 [[Samsung Electro-Mechanics]] 兩條軌道對撞——SK 早 1 年量產但規模小、Samsung 晚 1 年但規模 30 倍 + Samsung HBM4 集團整合 → 中長期 SEMCO 勝率更高
    4. **bull/bear 結論**：**整體是「加大餅」**（驗證 panel-level glass interposer 路線、創造設備需求 → 台廠設備鏈全受惠），**但同時「分食 fab 服務層的餅」**（從 [[日月光 ASE]] / [[Amkor]] / [[Powertech 力成]] / [[東捷]] 等台廠 OSAT 手中拿 Apple/Google/AVGO 鏈 panel-level interposer 訂單）
    5. **五軸評分**：
       - [[Absolics]] 16/25（路線敏感 4 / 站別關鍵 5 / 耗材 2 / IP 2 / 客戶分散 3）—— 與 [[Amkor]] 16/25 並列「美亞 OSAT-style 整合方」
       - [[Samsung Electro-Mechanics]] 19/25（路線敏感 5 / 站別關鍵 4 / 耗材 2 / IP 3 / 客戶分散 5）—— 列「foreign competitor」第三高（次於 [[Disco Corp]] 21/25、[[LPKF]] 20/25）
  - 同步更新：index.md（新增「TGV 韓國陣營」分類段 + 待 ingest 清單兩家打勾）
  - 累計：43 concept + **36 entity** + 41 summary

## 2026-06-05（追補：ABF 載板三雄 displacement 對沖視角）

- ingest: **ABF 載板三雄**（[[欣興]] 3037 / [[南電]] 8046 / [[景碩]] 3189，台股）— WebSearch 驅動建檔 + displacement concept 校準
  - **目的**：完成 [[ABF 載板 vs 玻璃基板 displacement]] concept 內三家命運的實證填補，從「subagent 推測」→「實證 entity」
  - entity [[欣興]]（3037.TW，台股 ABF 龍頭）— 跨 Intel + TSMC 兩大體系**唯一**
    - 市值 NT$1.54 兆 / PE 142.9（TTM）/ Forward PE ~55-60（2026 EPS ~17）/ 已發行 15.9 億股
    - **2026 Q1 EPS NT$3.28 = 13 季新高**（QoQ +41%、YoY +447%）
    - **2026 CapEx NT$254 億**（+30.93%、70% 投 ABF）+ 2027 長交期設備 25 億
    - 載板產能 YoY 2026 **+35%~+40%**
    - **高階 ABF（16L+）占 ABF 營收 60%、AI 相關 >50%、GPU AI server 20-30%**
    - **NVDA Blackwell 載板第二供應商、份額 30%**（IBIDEN #1）
    - 跨 Intel EMIB/Foveros（全球僅 IBIDEN + 欣興兩家有量級供應）+ TSMC CoWoS/CoPoS
    - AMD EFB 體系欽點、2026-2027 在台百億美金擴產直接點名
    - **玻璃 design partner with Intel**：2026-03 完成 sample 一階驗證（搭聯致 SR-6000RE 低 CTE 介電）、2026-07 自建 TGV 試產線完工、2026 Q4 批量裝機、2027 小量、2028 商業化
    - 大摩 EPS 2025-2028 CAGR **105%**
    - Re-rate 三角形 3/4（OpEx 因 CapEx 加碼遞延折舊）
    - **校準後 displacement 命運：受惠（雙曲線）**——concept 內「受害 + 受惠」中「受惠」比例 > 「受害」
    - 主要 takeaway：**displacement 中最不會被切的台廠**，因已在玻璃 side 拿到 Intel design partner 位
  - entity [[南電]]（8046.TW，台股 ABF #2 + 800G/1.6T 寡占）— ASIC 三巨頭隱形賣水人
    - 市值 ~NT$5,685 億（6.46 億股 × NT$880）/ PE ~290（TTM 低基期）/ Forward PE ~108（2026 EPS 估 ~8）
    - **2026 Q1 EPS NT$2.03**（QoQ +9%、YoY +534%）/ OP margin 8.6%
    - 2025 全年 EPS NT$3.01、營收 NT$401.7 億、毛利率 15.85%（仍在谷底回升）
    - **IC 載板占營收 85%**（ABF 50-55% + BT 30%）、網通 49%
    - **ASIC 三巨頭（AVGO + AMD + Marvell）合計 60% 營收** = 集中極高
    - **800G/1.6T 高階交換器市佔 >70%**（隱形龍頭）
    - 高階 ABF 占營收：2025 H1 <20% → **2027 >40%**（翻倍以上）
    - **NVDA Vera Rubin（CoWoS-L + ABF）路線**：Rubin R100 Q4 2026 sample / 2027 Q1 量產 / Rubin Ultra 因 yield 縮成 dual-die / **不轉 CoWoP** = 南電 NVDA 線 2026 H2 ramp
    - 玻璃自做**落後欣興**：研發樣品有但卡雷射槽孔 + 穿孔電鍍 + 增層材質
    - 客戶玻璃化威脅：**AVGO Tomahawk 8 走玻璃路徑**（Toppan 新加坡/日本 JV 線）+ AMD/Marvell 跟進 → 2028 後 ASIC 高階 ABF TAM 被切
    - 大摩 EPS 2025-2028 CAGR **113%**（三雄最高）/ 外資目標價最高 NT$1,115
    - Re-rate 三角形 2/4（毛利率 15.85% 仍低 + CapEx 折舊壓力）
    - **校準後 displacement 命運：短期受惠（2026-2027）/ 中期受害（2028+）**——concept 原預測「純受害？取決於 NVDA 路線」**已部分翻案**（NVDA 仍 ABF），但 ASIC 玻璃化中期威脅未變
    - 主要 takeaway：**「短期 ABF 王者、中期 displacement 主受害者」**雙面性最大
  - entity [[景碩]]（3189.TW，台股 ABF #3 + BT 強項）— **相對受益者**
    - 市值 NT$2,866 億（5.27 億股 × NT$544）/ PE 145.56（TTM）/ Forward PE ~60-70（2026 EPS 預估 7.75-9.2）
    - **2026 Q1 EPS NT$1.17**（QoQ -17%、YoY +92%）
    - 2025 Q3 毛利率 **18.96%**、淨利率 5.92%
    - 主業 mix：**ABF 40% + BT 33% + 隱形眼鏡/消費 18% + 基地台 5%** = **三雄客戶分散度最高**
    - **2026 打入 NVDA AI GPU 第三供應商**（IBIDEN #1 + 欣興 #2 + 景碩 #3）
    - **美系 AI CPU 供貨率 10% → 50%**（重大訂單外溢受惠）= 來自 IBIDEN/欣興產能爆滿外溢
    - **ABF 稼動率 86% → 95%**
    - BT 33% 受惠 T-glass 缺料漲價（手機高階 + 記憶體）
    - 2026-2027 ABF 擴產 +25%、CapEx **NT$235 億**（$744M）
    - 2026 全年營收 YoY 估 +30%
    - 玻璃對應策略：**觀望 + 後段 RDL 增層卡位**（不自做 core、做 RDL 增層與細微線路電鍍）
    - 外資目標價：富邦 NT$620、美銀 NT$565
    - Re-rate 三角形 3/4（毛利率僅 18.96% 但稼動率拉升）
    - **校準後 displacement 命運：相對受益**——concept 內「中低階守住、相對受益」**完全成立 + 加碼校準**（不只「相對受益」，還拿到 AI CPU 訂單外溢 + NVDA AI GPU design-in）
    - 主要 takeaway：**三家中 risk-adjusted return 最佳**（客戶分散度最高 + displacement 曝險最低 + 兩個雙曲線受惠）
  - **三家業務 mix 對照**（2026）：
    | 公司 | 高階 ABF | 中階 ABF | BT | 其他 | AI 集中度 |
    |---|---|---|---|---|---|
    | 欣興 | 高（60% ABF / 16L+）| 中 | 低 | HDI/PCB | 50%+（AI 載板）|
    | 南電 | 中→高（2027 >40%）| 中 | 高（30%）| 隱形眼鏡少 | ASIC 60%（AVGO/AMD/Marvell）|
    | 景碩 | 低 | 中（主力）| 高（33%）| 隱形眼鏡 18% + 基地台 5% | <30%（AI CPU 外溢 + NVDA #3）|
  - **三家對玻璃基板應對策略**：
    1. **欣興 = 自做（Intel design partner）**：2026-03 sample 通過、2026-07 試產線、2028 量產
    2. **南電 = 自研樣品但落後**：卡雷射槽孔 + 穿孔電鍍、增層材質需重做
    3. **景碩 = 觀望 + 後段 RDL 增層**：不自做 core、做後段
  - **校準後 displacement 命運排序**：
    1. **欣興**：**受惠（雙曲線）**——displacement 過渡期最大贏家
    2. **景碩**：**相對受益**——risk-adjusted return 最佳、客戶分散度最高
    3. **南電**：**短期受惠 / 中期受害**——2028 後 ASIC 玻璃化主要受害者
  - **pair trade 提案**：
    - 「做多 TGV 設備廠 + 做空 ABF 廠」**最佳對沖 = [[鈦昇]] / [[雷科]] / [[弘塑]] / [[辛耘]] 多 + 南電 空**（南電是 displacement 中期主受害者、Forward PE 108 已 price in 多年漲價）
    - 「做多玻璃材料 + 做多 ABF 廠」**互補配對 = [[Corning]] / [[AGC]] 多 + 景碩 多**（景碩是 displacement 中期最不受害的 ABF 廠 + 高 risk-adjusted）
    - 「displacement 雙頭曝險買單一 entity = 欣興」（自身 ABF 漲價週期受惠 + 玻璃 design partner 期權同時持有）
  - **五軸評分**（路線敏感 / 站別關鍵 / 耗材 / IP / 客戶分散，滿分 5/5/5/5/5 = 25）：
    - **欣興 19/25**（路線敏感 4 / 站別關鍵 5 / 耗材 4 / IP 3 / 客戶分散 3）—— 雙曲線受惠
    - **南電 14/25**（路線敏感 5 / 站別關鍵 4 / 耗材 3 / IP 1 / 客戶分散 1）—— ASIC 集中 60% + IP 弱 + 玻璃落後
    - **景碩 17/25**（路線敏感 3 / 站別關鍵 3 / 耗材 4 / 玻璃化曝險低 = IP 不適用算 2 / 客戶分散 5）—— risk-adjusted 最佳
  - 同步更新：
    - index.md（新增「ABF 載板廠（displacement 對沖視角）」分類段 + 待 ingest 清單三家打勾）
    - [[ABF 載板 vs 玻璃基板 displacement]] concept（三家段落 update 為實證版 + 增加最新校準）
  - 累計：43 concept + **39 entity** + 41 summary

## 2026-06-05（追補：IBIDEN 4062.JP 補完 ABF 廠四家圖譜）

- ingest: **[[IBIDEN]]**（4062.JP，日股，foreign competitor 變體）— WebSearch 驅動建檔（12 次 WebSearch + 3 次 WebFetch）
  - **目的**：補齊 ABF 廠四家圖譜（[[欣興]] + [[南電]] + [[景碩]] + IBIDEN）+ subagent 之前提到「NVDA AI GPU 第一供應商 IBIDEN #1 + 欣興 #2 + 景碩 #3」的 #1 漏網
  - entity [[IBIDEN]]（4062.JP，全球 ABF #1 + NVDA AI GPU 歷史獨家）
    - 市值 **¥4.78 兆**（USD 330 億，2026-05-13）/ Forward PE 60 / TTM PE 84-106（峰值 2026-03）
    - 股價 ¥21,135（2026-06-02）/ 52 週區間 ¥2,853 → ¥22,670 / 12 個月漲幅 **+530%**
    - **FY2026 全年（截至 2026-03）**：營收 **¥4,162 億**（+12.7% YoY）/ OP **¥620.3 億**（+30.3%）/ 淨利 **¥637.1 億**（+89.0%）/ EPS **¥228.16**
    - **Electronics segment（IC 基板）= 65% 營收**：¥2,433 億（+23.4% YoY）/ OP ¥452.5 億（+68.5% YoY）= 主成長引擎
    - **Ceramics segment**（汽車排氣濾清器）= 23%：-1.8% / OP -37.4% = 拖後腿
    - **FY2027 自家指引**：營收 ¥5,000 億（+20.1%）/ OP ¥900 億（+45.1%）= 營業槓桿全開
    - **市佔**：AI server build-up substrate 2023 **85%** 一家獨大 → 2026 降至 **55%**（[[欣興]] 拉至 25%）
    - **NVDA Blackwell 載板 75%**（[[欣興]] 25%）= 絕對龍頭
    - Intel EMIB 全球僅兩家有量級供應之一（搭 [[欣興]]、加 Shinko + AT&S）
    - Apple iPhone 18 / M5 mac 載板（旗艦消費級）+ 開始 allocate（限量）= 賣方市場
    - **三年 CapEx ¥5,000 億日圓**（USD 32-33 億，2026-2028）：
      - 河間 Gama Plant **¥2,200 億**（FY2027 起陸續量產）
      - 大野 Ono Plant **¥2,800 億**（2025-10 開、FY2027 階段性量產）
      - AI 用 IC 基板產能 FY2028 擴至 2024 的 **2.5 倍**
    - **NVDA Vera Rubin / Rubin Ultra 仍走 CoWoS-L + ABF**（不轉 CoWoP，已校準）= IBIDEN 主場繼續吃到 2028
      - Rubin Ultra 載板**比 Rubin 大、層數多** = ABF 用量 15-18 倍 = IBIDEN 受惠倍增
    - 玻璃基板對應策略：**觀望 / 探索**
      - 2023-2027 CapEx 計畫明確列「glass core substrate」R&D
      - 停在 exploration stage、未 sample 通過 / 未量產時程
      - **沒拿到玻璃 design partner 位**（Intel CW Forest → [[欣興]] / Apple Baltra → [[Samsung Electro-Mechanics]] / AVGO T8 → Toppan）
      - 跟 [[南電]] 同檔（兩家都「樣品有但落後」）、落後 [[欣興]] + [[Samsung Electro-Mechanics]] + [[Absolics]]
    - MLCC 嵌入式基板：5,000 億涵蓋這條路線、[[Samsung Electro-Mechanics]] 先發 IBIDEN 追擊 = 開第二戰場
    - 分析師目標價：平均 ¥8,359 / 最高 ¥13,900 / 最低 ¥5,000（10 家）— **股價已遠超 sellside 平均** = 市場比分析師更看多 or 將迎目標價上修週期
    - Re-rate 三角形 **3/4**（OpEx ⚠️ 因 5,000 億 CapEx 折舊壓力 FY2027-2030 + Ceramics 拖累）
    - **校準 displacement 命運：受惠（短期 2026-2028 ABF 大循環）+ 玻璃化曝險中等（長期 2028 後）**
    - 主要 takeaway：**「ABF 載板絕對龍頭 + 玻璃化觀望者」雙面**——跟 [[南電]] 像（兩家都「ABF 王者 + 玻璃落後」），但 IBIDEN 客戶結構（NVDA + Intel + Apple）優於南電（AVGO + AMD + Marvell 60% 集中）
  - **vs 台廠 ABF 三雄整合對照**：

    | 維度 | IBIDEN | [[欣興]] | [[南電]] | [[景碩]] |
    |---|---|---|---|---|
    | ABF 全球排名 | **#1** | #2 | #3 | #4 |
    | AI server build-up 市佔 | **55%** | ~25% | <10% | <5% |
    | NVDA Blackwell 載板 | **75%** | 25% | 0%（吃 Vera Rubin）| 第三供應商 design-in |
    | NVDA Vera Rubin（ABF）| 主供 | 主供 | **2026 H2 ramp** | 第三 design-in |
    | Intel EMIB | 主供 | 主供 | 弱 | 弱 |
    | AMD EFB | 弱 | 欽點 | 欽點 | 欽點 |
    | AVGO ASIC | 弱 | 有 | **強（含 Marvell 60%）** | 弱 |
    | Apple | 強（iPhone/M）| 弱 | 弱 | BT |
    | 玻璃自做進度 | **觀望** | **Intel design partner** | 樣品有但落後 | **觀望（後段 RDL）** |
    | 五軸總分 | **19/25** | **19/25** | 14/25 | 17/25 |
    | Forward PE | 60 | 55-60 | **108** | 60-70 |
    | 12 個月股價漲幅 | **+530%** | +770% | n/a | n/a |
    | Re-rate 三角形 | 3/4 | 3/4 | 2/4 | 3/4 |

  - **IBIDEN vs [[南電]] displacement 命運對照（兩家「ABF 王者 + 玻璃落後」）**：
    - 相似：兩家玻璃進度都「樣品有但落後 [[欣興]]」、都沒拿 Intel/Apple/AVGO 玻璃 design partner 位
    - 差異 #1（客戶結構）：IBIDEN（NVDA + Intel + Apple 三強）vs [[南電]]（AVGO + AMD + Marvell ASIC 60% 集中）→ IBIDEN 客戶結構優於 [[南電]]
    - 差異 #2（玻璃化曝險）：IBIDEN 客戶（NVDA Rubin Ultra 確認 ABF / Intel EMIB 推 ASIC / Apple Baltra 已被 SEMCO 拿但 iPhone 載板仍 IBIDEN）= **玻璃化曝險「分散且時程模糊」** vs [[南電]]（Tomahawk 8 玻璃化已確認、AMD/Marvell 跟進）= **玻璃化曝險「集中且時程明確」**
    - 差異 #3（規模壁壘）：IBIDEN AI build-up 55% 一家獨大 vs [[南電]] 集中 ASIC 60% 但市佔分散 → IBIDEN 規模壁壘更高
    - 結論：**IBIDEN 不是「純受害」**（NVDA Rubin Ultra 仍走 ABF + Intel EMIB 撐第二曲線 + Apple iPhone 載板續吃 = 至少撐到 2028）、vs [[南電]] 是「ASIC 玻璃化主受害者」（2028 後 ASIC ABF TAM 被切）
  - **bull / bear for 台廠 ABF 三雄**：
    1. **Bull**：IBIDEN 守舊不轉玻璃 → [[欣興]] 在玻璃 side 反超（Intel design partner 位）+ IBIDEN 擴產確認 ABF 大循環、訂單外溢 → [[景碩]] risk-adjusted 最佳
    2. **Bear**：IBIDEN 自轉玻璃成功 → 鎖死 NVDA / Apple / Intel 鏈 → [[欣興]] 只剩 ABF 老本、[[南電]] 失去 ASIC 路徑 + IBIDEN 5,000 億 CapEx 倍增產能 → 2028 後 ABF 供過於求、漲價週期提前結束
  - **bull / bear for 台廠 TGV 設備廠**（[[鈦昇]] / [[雷科]] / [[弘塑]] / [[辛耘]] / [[萬潤]] / [[敘豐]]）：
    1. **Bull**：IBIDEN 玻璃化慢 → TGV 設備鏈台廠先吃過渡期 + IBIDEN 5,000 億擴 ABF 同時 R&D 玻璃 = 設備需求兩條軌道 + [[敘豐]] 跟欣興同步擴
    2. **Bear**：IBIDEN 玻璃化突破 → 採購 [[LPKF]] / [[Disco Corp]] 設備（日德陣營）→ 台 TGV 設備廠被擋在 IBIDEN 鏈外
  - **五軸評分**（路線敏感 / 站別關鍵 / 耗材 / IP / 客戶分散）：
    - **IBIDEN 19/25**（4 / 5 / 3 / 4 / 3）—— 與 [[欣興]] 並列 ABF 鏈最高、勝在「IP」（百年技術 + 全製程內製）/ [[欣興]] 勝在「耗材」（電鍍蝕刻消耗 + [[敘豐]] 在地化）
  - **整合啟示**：補 IBIDEN 後 ABF 廠四家圖譜新洞察：
    1. **NVDA Blackwell 載板分配確定**：IBIDEN 75% + 欣興 25%（之前只知道「欣興是第二」，現在知道 #1 與 #2 比例 3:1）
    2. **AI server build-up 兩段式變化**：2023 IBIDEN 85% 一家獨大 → 2026 IBIDEN 55% + 欣興 25%（欣興 5 年內從 ~10% 翻 2.5 倍至 25%）= **欣興是過去 3 年最大贏家**（而不是 IBIDEN）
    3. **玻璃化路線 ABF 四廠全落後韓國**：[[Samsung Electro-Mechanics]]（Apple Baltra design-in）+ [[Absolics]]（AMD MI400）vs IBIDEN（觀望）+ 欣興（Intel design partner 但量產 2028）+ 南電（樣品落後）+ 景碩（觀望 RDL）→ **2030 玻璃化主流期到來時、ABF 四家排名可能完全洗牌**
    4. **IBIDEN ≠ [[南電]]**：兩家都「ABF 王者 + 玻璃落後」但 IBIDEN 客戶結構（NVDA + Intel + Apple）優於南電（AVGO + AMD + Marvell 60% 集中）= **IBIDEN 不是純受害、是「ABF 大循環 2026-2028 主受惠 + 玻璃化緩慢 displacement 2028+」**
    5. **pair trade 校準**：「做多玻璃材料 + 做空 IBIDEN（or 南電）= 押 2028 後 displacement」、「做多 IBIDEN + 做多欣興 = 雙重壓 ABF 大循環」（IBIDEN 海外 hedge + 欣興 + 玻璃 option）
    6. **MLCC 嵌入式基板第二戰場揭曉**：SEMCO 先發、IBIDEN 5,000 億追擊、欣興 / 南電 / 景碩跟進 → 同樣四家戰場、台廠落後最大
  - 同步更新：
    - index.md（「ABF 載板廠 displacement 對沖視角」分類段加 IBIDEN 為第一個 + 待 ingest 清單打勾）
    - 本 log.md（加追補段落）
  - 累計：43 concept + **40 entity** + 41 summary

## 2026-06-05（追補：F&S Electron — Absolics 唯一 TGV contract fab 外包商）

- ingest: entity [[F&S Electron]]（韓國未上市 / S.E.A. 子公司）— WebSearch 驅動建檔
  - **觸發背景**：Absolics entity 內標示「F&S Electron 獨家 TGV 設備合約 2026-03 到期 → Absolics 轉 dual sourcing → 第二供應商 slot 空出」是 [[鈦昇]] 的潛在期權窗口；需要把 F&S Electron 獨立 entity 化以校準 thesis
  - **資料豐富度**：**medium**（介於路徑 A 完整 entity 與路徑 B concept 註解之間，最終走路徑 A 因為 5 個獨立來源組合起來夠 sticky）
  - **公司結構（high confidence）**：
    - 2021-05 Incheon 成立、雙 CEO（Choi Byung-chul + Shin Jae-ho）
    - 量產廠 Songdo cleanroom 2024-05 啟用、R&D Gumi、員工 36（YoY -5%）
    - 母公司：S.E.A.（에스이에이）+ Fuseimenix（후세메닉스）雙股東
    - **2025-11 S.E.A. 取得 majority stake**（垂直整合「設備 + 服務」雙層押注，類 [[LPKF]] + Vitrion 模式）
    - 私募未上市、Series A、僅 4 件韓國註冊專利
  - **業務（high confidence）**：
    - 唯一已公開客戶 [[Absolics]]、做 TGV 雷射鑽孔 + Metallization (PVD) 一站式 contract fab
    - 510×515mm panel、sub-10μm 線路精度
    - 2024-05 業界首發量產半導體玻璃基板
  - **S.E.A. 母公司快照**：2024 營收 USD 80M（89% 賣美國）+ USD 47M backlog、CEO Jaeho Shin（前三星貿易）、280 員工、四韓國廠 + 馬來西亞、550+ 出貨設備
  - **無法驗證的細節**：
    - F&S Electron 自身財報（營收、毛利）
    - 設備規格（laser 類型、孔密度、aspect ratio、yield）
    - IP 持有現況（是否買 LPKF LIDE / 與 LPKF IP 衝突）
    - second supplier 第二位是誰（dual sourcing 結果未揭露）
  - **鈦昇拿 Absolics second source slot 的四道障礙**：
    - **IP 戰** 🔴 binary（LPKF LIDE EPO/KPCA/中國三線確認、Absolics 是 Intel licensing 受惠者不會冒 IP 風險）
    - **地緣** 🟠 high（Absolics 是 SK 集團 + Georgia + CHIPS Act 政治組合，優先韓國本土 Philoptics/Hana/PNT/LG）
    - **技術差距** 🟡 medium（鈦昇是「設備商」而非「contract fab 玩家」業務模式錯位）
    - **產能 + 客戶優先序** 🟠 high（鈦昇 Intel/TSMC 已有 anchor、不會把產能優先給 Absolics）
    - → 機率 **<15%**
  - **2026 Q1/Q2 追蹤訊號**：（a）SKC 2026 Q2 法說會、（b）TrendForce/The Elec dual sourcing 第二位名單、（c）F&S Electron 員工人數變化、（d）Absolics Phase 2 重啟、（e）S.E.A. 海外擴張、（f）鈦昇法說會是否提 SK 集團接觸、（g）2027 Q1 Absolics 公開 AMD MI400 量產供應商鏈
  - **五軸評分 13/25**（不適合直接比較設備商）；客戶分散 1/5 是極端風險訊號（Absolics 議價權反向放大）
  - 同步更新：
    - [[Absolics]] entity（line 103 F&S Electron 加 wikilink）
    - index.md（新增 [[F&S Electron]] 到「TGV 韓國陣營」分類 + 待 ingest 清單三家打勾）
  - 累計：43 concept + **40 entity** + 41 summary

## 2026-06-05（追補：台廠 MLCC 二強 — [[國巨]] + [[華新科]] — [[MLCC 嵌入式基板賽道]] 校準）

- ingest: entity [[國巨]] + [[華新科]]（WebSearch 12 query 驅動建檔）
  - **觸發背景**：[[IBIDEN]] 5,000 億日圓擴 ABF + 揭示「MLCC 嵌入式基板第二戰場」、SEMCO 先發、需要把台廠 MLCC 二強建檔以校準「台廠落後最大」結論
  - **資料豐富度**：**high**（2026 Q1 法說會 + 大摩 / 摩根大通研報 + 多份產業研報 + 陳泰銘登首富新聞催化齊備）
  - **[[國巨]] 結構性 thesis（high confidence）**：
    - 全球**鉭電容 #1**（>50% 市佔）+ 晶片電阻 #1 + MLCC #3
    - 三連併購（Pulse 2018 / KEMET 2020 USD 18 億 / Shibaura 2026/01 USD 44 億）= 一站式被動元件 = 「**併購王**」護城河
    - 2026 Q1 營收 NT$381.66 億 +22.7% YoY / EPS 3.90 +44.7% YoY / 毛利率 38.1% +2.5pp YoY = **Re-rate 三角形 4/4 滿**
    - AI 占 14-15%（從 2024 的 4% 跳升 = AI 滲透加速）/ 鉭電容線 AI 占比 >30% / 接單出貨比 1.3
    - 大摩 / 摩根大通目標 NT$1,010 / 1,000+（PE 60x ✕ EPS 17）
    - 陳泰銘 2026/05/20 登台灣首富 NT$4,900 億 = 媒體 / 散戶層資訊擴散完成
  - **[[華新科]] 結構性 thesis（high confidence）**：
    - 台廠 MLCC 二哥 + 大中華 #1 + 全球 #4（~14% 市佔）
    - **MLCC 純度 46.4%**（比國巨 17.7% 高 3 倍）→ 純漲價週期 beta
    - 2026 Q1 營收 NT$95.38 億 +14% YoY / EPS 1.69 +40-69.7% YoY / 毛利率僅 **18.3%**（vs 國巨 38.1% 差距巨大）
    - AI 占 5-10%（AI 應用毛利率比公司均高 10pp）
    - 中高壓 MLCC（630V → 1,000V+）+ LTCC + 安規電容切 AI 電源 + 車用
    - 「**台灣 R&D + 馬來西亞量產**」雙核心、車規認證 3-5 個月訂單能見度
    - 法人 EPS 估從 4.74（2025）→ 5.5-7.5（2026 中位 5.76-6）/ 市值 NT$2,052 億 / PE 81
- **[[MLCC 嵌入式基板賽道]] 校準（vs IBIDEN subagent 預測「台廠落後最大」）**：
  - **MLCC 嵌入式戰場分數**：
    - SEMCO ✅（先發 + LSC + silicon capacitor + 自己用 + Apple/AWS/AVGO）
    - 村田 ✅（iPaS / EMSC / GRU 0402 嵌入式 + 高階壟斷 >40%）
    - [[IBIDEN]] ⚠️ 追擊（5,000 億日圓擴產 + 開始 R&D embedded）
    - 欣興 / 南電 / 景碩 ⚠️ 觀望（沒看到嵌入式專案公開資料）
    - **[[國巨]] ❌**（無 embedded MLCC 產品 + 無載板廠盟友 = **不在第二戰場**）
    - **[[華新科]] ❌❌**（規模太小 + 技術 + 通路三缺 = **完全缺席**）
  - **校準結論：「台廠落後最大」=「台廠載板廠 + MLCC 廠 = 兩條線都不領先」確認**
    - 載板廠：欣興 + 南電 + 景碩 ABF 強、嵌入式 R&D 落後 SEMCO / IBIDEN
    - MLCC 廠：[[國巨]] + [[華新科]] **沒有任何嵌入式產品線、沒有跟載板廠合作**
    - **集團整合層完全缺位**（Samsung = SEMCO + DRAM / 三星電子全鏈整合 / 國巨 + 載板三雄無資本紐帶）
    - 但 **niche 還在**：[[國巨]] 鉭電容 / 晶片電阻全球壟斷可以「**賣標品給載板廠**」吃間接溢出
- **AI server 曝險強弱對比**：
  - [[國巨]]：AI 直接占 14-15% / 鉭電容線 >30% / 接單出貨比 1.3 / NVDA AVL 認證 / GB200 X6S 用量 85%（強）
  - [[華新科]]：AI 直接占 5-10% / 透過 EMS / 電源廠間接 / 高毛利率 mix 但量級小（中弱）
  - → 強度比：[[國巨]] : [[華新科]] = **3:1**（直接客戶滲透度差）
- **嵌入式戰場應對策略**：
  - [[國巨]]：**無公開策略**——靠鉭電容 + 晶片電阻全球壟斷吃間接溢出 + Shibaura 感測整合 / **沒看到 embedded MLCC R&D 路線圖**
  - [[華新科]]：**規模太小無資源**——靠中高壓 MLCC + LTCC 切 AI 電源 + 車用利基 / 完全不嘗試嵌入式
- **五軸評分**（路線敏感 / 站別關鍵 / 耗材 / IP / 客戶分散）：
  - [[國巨]] **18/25**（4 / 4 / 3 / 4 / 3）：勝在 IP（鉭電容 + 晶片電阻全球壟斷）+ 客戶分散度高（全平台賣水人）/ 失分在站別關鍵（不在嵌入式 / 玻璃化路線中）
  - [[華新科]] **13/25**（3 / 3 / 3 / 2 / 2）：純 MLCC beta、所有維度都是「跟隨者 + 次級轉單」/ IP 跟客戶分散全弱
  - 跟既有 entity 對照：
    - vs [[欣興]] 19/25：[[國巨]] 18/25 接近，[[欣興]] 強在玻璃化雙曲線（拿到下一輪入場券）/ [[國巨]] 強在多軌（電阻 + 鉭 + MLCC + 磁性 + 感測）/ 但**[[欣興]]在「嵌入式 + 玻璃化」未來戰場有位置，[[國巨]]沒有**
    - vs [[南電]] 14/25：[[南電]] PE 100+ / Re-rate 2/4 / 客戶集中 60% / [[國巨]] 38.1% 毛利 + 4/4 + 多客戶分散 = **[[國巨]]> [[南電]]在「再投資品質」維度**
- **Pair trade 提案：「做多 ABF 廠 + 做空 MLCC 廠」是否合理？**
  - **否**（至少 2026-2027 不合理）：
    1. **時間維度問題**：嵌入式戰場 2027-2028 才放量 / 2026 ABF + MLCC **同步缺貨同步漲價** = pair trade 在 2026 是 **double long beta**、不是 hedge
    2. **MLCC 漲價週期還沒結束**：村田 + Panasonic + 國巨 + KEMET 三波漲價 / 高盛喊 MLCC = 下一個記憶體 / 2027 用量 = 2025 的 4 倍
    3. **嵌入式 ≠ MLCC 消失**：MLCC 用量翻倍同時嵌入式比例提升 = MLCC TAM 雙重擴張、不是替代
  - **更精準的 pair trade**：
    1. **做多 [[國巨]] + 做空 [[華新科]]**（做多「**鉭電容 + 晶片電阻壟斷 + 高毛利**」、做空「**純 MLCC beta + 18.3% 毛利率 + PE 81**」）= **MLCC mix 質差 pair trade**
    2. **做多 [[欣興]] + 做空 [[南電]]**（做多「**玻璃 design partner**」、做空「**ASIC 玻璃化主受害 + PE 100+**」）= **顯影路線 pair trade**
    3. **做多 [[IBIDEN]] + 做空 [[華新科]]**（做多「**ABF + 嵌入式雙佔位**」、做空「**MLCC 純跟隨者**」）= **嵌入式戰場主從 pair trade**
  - **不要做的 pair**：做多 ABF 廠 + 做空國巨 = ABF 廠正在向上突破、國巨同步突破、估值合理性各異但 beta 同向
- **跟既有 [[ABF 載板 vs 玻璃基板 displacement]] / [[MLCC 嵌入式基板賽道]] 補充**：
  - 確認「**台廠落後**」結論：MLCC 兩強 + 載板三雄都沒有「嵌入式專案」公開資料
  - 但補充一個 **niche window**：[[國巨]] **鉭電容 + 晶片電阻**部分在 GPU 旁邊 PCB 配置場景仍稀缺（X6S 85% 用量、低 ESR 高密度）→ **鉭電容線可能在嵌入式之外保留結構性需求**（嵌入式不能取代鉭電容）
- 同步更新：
  - index.md（新增「標的：MLCC / 被動元件」分類段 + 兩家 entity）
  - 本 log.md（追補段落）
- 累計：43 concept + **42 entity** + 41 summary

## 2026-06-05（追補：MLCC 嵌入式基板賽道 concept + 村田 Murata entity — 第二戰場補完）

- ingest: concept [[MLCC 嵌入式基板賽道]] + entity [[村田 Murata]]（6981.JP）
  - **觸發背景**：[[IBIDEN]] subagent 報告結論「**MLCC 嵌入式基板第二戰場揭曉**：SEMCO 先發、IBIDEN ¥5,000 億追擊、欣興/南電/景碩跟進 → 同樣四家戰場、台廠落後最大」需要獨立 concept 化 + 國際對應 entity 補位
  - **WebSearch 11 次**驗證關鍵 claim（Murata MLCC 市佔、嵌入式技術 ECP/LSC、SEMCO 先發、IBIDEN 追擊、Taiyo Yuden 1005 size 22μF 首發、Yageo Q1 2026 業績、信昌電 NVDA Rubin 1MW、矽電容寡占破局）
  - **核心發現（concept 層級）**：
    1. **嵌入式技術不是 binary、是三線並行**：
       - **嵌入式 MLCC（ECP）**：把分立 MLCC 埋入載板、靠近 die——[[太陽誘電 Taiyo Yuden]] 2025 世界首發 1005 size 22μF
       - **嵌入式矽電容（Silicon Capacitor）**：完全不同類別、silicon-based 不是 ceramic、ESL/ESR 比 MLCC 低 100 倍——[[村田 Murata]] + [[TSMC]] 歷史寡占、SEMCO USD 10 億合約破局
       - **嵌入式電感 / iPaS 整合模組**：[[村田 Murata]] iPaS™（鋁電解 + 平面 coil + VPD）+ [[TDK]] SESUB（IC + passives 一起埋）
       - **LSC（Land Side Capacitor）**：非嵌入、貼在 substrate 背面 die 投影下、1-10MHz 快速電流響應
    2. **SEMCO「先發」具體內容**：
       - 越南廠 2026-04 宣布 USD 1.2B 投資 + MLCC 嵌入式專線 + 2026 H2 量產 NVDA Grok3 LPU 為首發客戶
       - 2026 全年 ABF 售罄（Alphabet/Tesla/Apple/AWS/AVGO）+ 矽電容 USD 10 億合約（2027-01 起）= **Murata + TSMC 寡占首度破局**
       - 「智慧型手機模組 10 年累積嵌入式經驗」是技術底層
    3. **村田對嵌入式賽道的應對 = 三線並進**（不是觀望、不是合作、是自己做）：
       - 線 1 分立 MLCC（現金牛，AI rack BOM 倍增直接吃到 USD 1,530 → 4,320）
       - 線 2 iPaS 嵌入式（已商業化、AI 數據中心 power module）
       - 線 3 矽電容（與 TSMC 寡占、AI server power delivery 必經之路）
       - → 是賽道**唯一「不被切的純被動元件廠」**
    4. **對 [[國巨]] / [[華新科]] 影響預測（subagent 結論 + 本次補完）**：
       - **[[國巨]]**：MLCC 嵌入式戰場「落後」（無 embedded MLCC 產品 + 無載板廠盟友）、但鉭電容線 (>30% 鉭電容收入綁 AI server) + 晶片電阻是嵌入式不能取代的 niche
       - **[[華新科]]**：MLCC 嵌入式戰場「完全缺席」、信昌電子公司中高壓 MLCC 在 NVDA Rubin 1MW 機櫃高壓 MLCC 倍增（3-4K → 10K+ 顆）有結構性需求、但嵌入式滲透到高壓時會被切
       - **市場尚未討論這個曝險**——AI server MLCC BOM 倍增是看好敘事、displacement 是反向敘事
    5. **整合啟示：MLCC 嵌入式戰場 vs TGV/玻璃化第一戰場的結構性差別**：
       - 玻璃化是**換零件**：基板材料 ABF → 玻璃、台廠設備鏈（[[鈦昇]]/[[雷科]]）**反而拿到 first-mover**
       - 嵌入式是**換結構**：BOM 分立 → 嵌入、台廠 ABF 廠 + MLCC 廠**雙線受壓**
       - 第一戰場「玻璃 TAM 從零起 + ABF 高階被切」、第二戰場「MLCC TAM 結構性變化 + 嵌入式 TAM 新增 + 純 MLCC 廠被切」
       - 台廠 ABF + MLCC 兩個產業在台灣**沒有共同集團整合**（日韓有 IBIDEN+村田 + SEMCO 集團內閉環）→ **第二戰場對台廠真實更不利**
       - 投資啟示：**做多村田 vs 做空台廠純 MLCC 廠**是嵌入式戰場 pair trade
  - **村田 entity 五軸 24/25**：路線敏感 5 / 站別關鍵 5 / 耗材 5 / IP 4 / 客戶分散 5 = **賽道最高分**（19/25 SEMCO + IBIDEN、~18/25 Taiyo Yuden、~14/25 國巨、~12/25 華新科）
  - **村田 Re-rate 三角形 3/4**：營收品質 / 毛利率 / 營業利益滿、OpEx 一 ⚠️ 因 ¥330 億 CapEx 含 ¥80 億 emergency 與 ¥50 億 impairment
  - 同步更新：
    - index.md（[[MLCC 嵌入式基板賽道]] 加在「TGV / 玻璃基板賽道」分類末段、[[村田 Murata]] 加在「MLCC / 被動元件」分類段首）
    - [[ABF 載板 vs 玻璃基板 displacement]] concept（末段新加「跟第二戰場（嵌入式 MLCC）的關係」）
    - 本 log.md（追補段落）
  - 累計：**44 concept + 43 entity + 41 summary**
- ingest: **光通訊 / DCI 第三戰場開戰** — Leo DCI/Hyper-Rail 研究筆記驅動 + WebSearch 補完
  - 1 raw (`raw/2026-06-05_Leo-DCI-Hyper-Rail-CIEN-COHR-LITE-NOK.md`) → 2 concept
  - method：subagent + ~13 WebSearch 並行驗證（Ciena 官方 / Nokia 官方 / Ciena Q2 2026 法說會逐字稿 / DriveNets scale across 定義 / Lumentum Q3 FY2026 出貨 / Jevons 學術原典 / DeepSeek 案例 / saturation 失效條件）
  - concepts:
    - [[Hyper Rail / Multi-Rail（光通訊整合技術）]] — CIEN/NOK 把 EDFA+WSS 整合成 1U 4-rail，128-160 fiber pairs/rack（32x-40x 密度），2027 起放量；補完 Leo 直覺到 LCOS WSS 像素提升 + EDFA pump 整合的精確機制
    - [[Jevons Paradox（投資版）]] — 學術原典（Jevons 1865 煤炭）+ AI/cloud/DeepSeek/Hyper-Rail 案例 + 三條失效情境（saturation/replacement/regulation）+ 五軸框架整合
  - 關鍵 finding:
    - **Hyper-Rail vs Multi-Rail 是同概念不同命名**（Ciena 先發、Nokia OFC 業界用語），但**規格差距 25%**（NOK 160 vs CIEN 128）+ **時程倒過來**（NOK 2026 H2、CIEN 2027 起跑、CIEN 首單已在手）
    - **scale across = NVDA Spectrum-XGS 詞彙**（DriveNets 寫成業界定義）= 跨 DC / 跨園區 / 80-1000km / **由 DCI 廠商（CIEN/NOK）掌控控制權，不在 NVDA 手裡**
    - **Leo「pump laser 用量會反而上升」判斷正確且保守**：rough estimate 4-6x TAM（單機 4x × 部署量 1.5x），Lumentum Q3 FY2026 pump laser 出貨 **+80% YoY** 已 P&L 印證
    - **對 [[CPO 供應鏈圖譜]] 第 2 層補強**：LITE/COHR pump laser 業務不會被 CPO 整合掉——CPO 是 intra-rack scale up、Hyper-Rail 是 inter-DC scale across，**兩條獨立第二曲線**
  - 同步更新：
    - index.md（新增「光通訊 / DCI（第三戰場）」分類；「待 ingest 延伸 半導體 / 算力供應鏈 entity」段落補註 LITE/COHR/CIEN/NOK 已 partial 補充於 Hyper-Rail concept）
    - 本 log.md（追加本段）
  - 待 ingest：CIEN/NOK/LITE/COHR 四家 entity 走 [[公司 Entity 模板（Step 1-3 三段式）]] 三段式（concept 已蓋技術面，個股財務狀態快照下次）
  - 累計：**46 concept + 43 entity + 41 summary**
- ingest: **光通訊光引擎兩家 entity 補完** — Lumentum / Coherent
  - method：subagent + 10 WebSearch 並行（Q3 FY2026 法說 / NVDA $2B 戰略 / pump laser 競爭 / SiC vs Wolfspeed / 估值 / Hyper Rail 受惠 / 6-inch InP 產能 / 1.6T 模組需求 / CPO Spectrum-X / NOK Multi-Rail 規格）
  - entities:
    - [[Lumentum]]（NASDAQ: LITE）— **InP / EML / pump laser 純度首選**
      - Q3 FY2026 營收 $808M（+90% YoY）/ Non-GAAP OP margin 32.2% / 47.9% 毛利
      - 200G EML **全球唯一量產者**、pump laser 全球前三、OCS backlog >$400M、CPO 多億美元 2027 H1 訂單
      - NVDA 2026-03-02 $2B 戰略投資 + Greensboro NC 6-inch InP 廠（2028 中量產）
      - 供需缺口 >30%（CEO 揭露）
      - Forward PE 52-59 / 12 個月 +1,542% / Re-rate 4/4
      - 五軸 19/25（路線 4 / 站別 5 / 耗材 3 / IP 5 / 客戶 2）
    - [[Coherent]]（NYSE: COHR）— **光通訊 + SiC 雙曲線**
      - Q3 FY2026 營收 $1.81B（+21% YoY）/ Datacenter & Comm 75% +41% / Industrial 25% +2%
      - 光收發器全球 ~25% 市佔（FY2025 $5.81B、規模龍頭）+ 6-inch InP 線追趕 EML（next quarter 2x、2027 年底再 2x）
      - SiC 150mm/200mm 10kV 量產 + 300mm 平台 + Thermadite XPU cooling
      - NVDA 2026-03-02 $2B 戰略投資（與 LITE 同日同額對倒）+ CPO 多年供應協議 + AI 訂單能見度 **2028**
      - Forward PE 44-49 / 12 個月 +362% / Re-rate 3/4
      - 五軸 19/25（路線 4 / 站別 4 / 耗材 3 / IP 4 / 客戶 4）
  - **Leo thesis 校準（必返回）**：
    - 「LITE 純度首選 + COHR SiC 後來成優勢」**完全成立**——五軸總分 19/19 打平、各有勝場
    - LITE 勝在「**laser 純度 + EML IP**」（200G EML 唯一量產 + InP 純度）
    - COHR 勝在「**SiC 第二曲線 + 客戶分散度**」（AI 雲端 + EV + 工業 + 半導體製程四軌客戶）
    - NVDA 同日同額投兩家 = 戰略**不選邊**+ lock up 全球高階雷射元件至 2027
    - **Hyper Rail 受惠程度**：兩家**對等受惠**——Ciena 把 pump laser 整合（LITE/COHR 都供）、Nokia 1830 GX Multi-Rail 160 fiber pairs/rack 需要 pump laser 數量增加（兩家分食）
    - 校準後押法：**LITE + COHR 一籃子**（過去 [[CPO 供應鏈圖譜]] 寫「不押光引擎誰贏」現已改為「光引擎 2-3 家寡占成形」）
  - 同步更新：
    - index.md（新增「光通訊 / DCI / 光引擎（第五波）」分類段；「待 ingest」內 LITE / COHR partial 補充改為 ✅ 已建）
    - [[CPO 供應鏈圖譜]] 第 2 層 + 第 7 層 + 賣水人位階 + 待 ingest + 相關連結 五處 wikilink 補完
    - [[SiTime]] 待 ingest 段（客戶列表 LITE/COHR wikilink）
    - 本 log.md（追加本段）
  - 本 subagent 貢獻：entity +2（Lumentum + Coherent）
  - 注：同期另一 subagent 並行建 [[Ciena]] / [[Nokia]] entity，整體累計待主 agent 合併後標定（實際檔案計數：48 entity）
- ingest: **DCI 設備商雙頭 entity 補完** — Ciena (CIEN) / Nokia (NOK)
  - 1 raw（同 [[Hyper Rail / Multi-Rail（光通訊整合技術）]] concept、`raw/2026-06-05_Leo-DCI-Hyper-Rail-CIEN-COHR-LITE-NOK.md`）→ 2 entity
  - method：subagent + 10 WebSearch 並行（Ciena Q2 FY2026 法說會 / HyperRail 部署 / cloud 客戶集中度 / WaveLogic 6 / supply constraint / Nokia 1830 GX RD66 D2ILA / Multi-Rail 出貨 / Infinera 整合 / Q1 2026 hyperscaler 訂單 / Nokia vs Ericsson 分歧）
  - entities：
    - [[Ciena]]（NYSE: CIEN）— **DCI 純度王 + scale across 物理層絕對龍頭**
      - WaveLogic 6 Extreme 1.6T 單載波全球第一、HyperRail RLS co-designed with hyperscaler
      - **Industry's first multi-rail order 已收**（hundreds of millions、跨多年）、2026 standardization → **2027 deployment ramp**
      - FY2026 Q2 營收 $1.57B（YoY **+40%**）/ Cloud 客戶 46%（YoY +70%）/ 兩家客戶占 34%（A: $321M、B: $212M）
      - Backlog **$7.7B**（QoQ +$600M）= ~1.2 年能見度
      - FY2026 全年指引 $6.3B（+32%）
      - Forward PE 80-91x / GF Value 估 532% overvalued
      - Re-rate 3/4、五軸 **19/25**（路線 5 / 站別 5 / 耗材 3 / IP 5 / **客戶分散僅 1**）
      - **「supply constrained」CFO 法說會明示** = Leo 訂單外溢 thesis 校準成立
    - [[Nokia]]（NYSE: NOK / NOKIA.HE）— **DCI 廣度王 + Infinera 整合 hyperscaler 對沖配置**
      - **9 of top 10 hyperscaler 都用 Nokia 光網路** = 廣度王
      - 1830 GX RD66 + D2ILA Multi-Rail OLS **2026 H2 出貨**（160 fiber pairs/rack、規格略勝 CIEN 128）
      - Infinera 併購（$2.3B、2025-02 完成）帶入自研 coherent DSP + InP fab = **部分內製**降低對 LITE/COHR 依賴
      - Q1 2026 集團營收 €4.50B、Optical Networks €821M（YoY **+20% comparable / +56% reported**）
      - AI & Cloud 訂單 **€1B**（+49%）、占集團 8%
      - NI segment GM 43.4%、FY2026 NI 指引 +12-14% / Optical+IP +18-20%
      - Forward PE **43x**（vs CIEN 80-91x **折價一半**）/ 分析師目標 $12.9-13.12（共識）vs 現價 $16.62（市場已超共識）
      - Re-rate 2/4（Mobile Networks 拖累）、五軸 **18/25**（路線 3 / 站別 4 / 耗材 3 / IP 4 / **客戶分散 4 壓制 CIEN**）
      - **跟 Ericsson 已策略分歧**：Ericsson 退出 DCI / 聚焦 5G 獨立 RAN、Nokia 走 hyperscaler 光網路 + NVDA 5G/6G AI-RAN 抱大腿
  - **Leo thesis 校準（必返回）**：
    - 「CIEN Hyper Rail 2027 部署 + 供應跟不上需求」**完全成立**（CFO 法說會明示）
    - 「NOK Multi-Rail 2026 H2 出貨」**完全成立**（1830 GX RD66 + D2ILA 官方公告）
    - 「Hyper Rail 跟 Multi-Rail 概念相同、細節有差異」**完全成立**——兩家都是「multi-fiber-pair 共用 amplifier / pump laser」整合架構；CIEN 128 fiber pairs vs NOK 160 fiber pairs、NOK 規格略勝
    - 「NOK 沒落後」**完全成立、甚至樂觀有理**——Nokia 規格略勝 + 出貨時程領先 + 9 of top 10 滲透 + Q1 2026 €1B hyperscaler 訂單
    - 「訂單外溢給 NOK」**方向正確、可量化**——CIEN supply-constrained 官方確認 + Nokia Q1 2026 hyperscaler 訂單 €1B (+49%) 是承接證據
    - **新增校準（純度 vs 廣度框架）**：
      - CIEN = 純度王（DCI 100%）+ 高估值（PE 80-91x）+ 高客戶集中度（兩家占 34%）= **三高 entity**
      - NOK = 廣度王（DCI 是 Network Infra 一支）+ 中估值（PE 43x）+ 低客戶集中度（9 of top 10）= **三中 entity**
      - CIEN 對 DCI thesis 槓桿大、NOK 對 DCI thesis 槓桿被 Mobile 稀釋一半但業務多元緩衝
  - **CIEN/NOK 對 [[Lumentum]] / [[Coherent]] 採購關係（校準）**：
    - **CIEN ramp = LITE/COHR 高槓桿受惠**（CIEN 100% 外採 pump laser + WSS + DSP 自研但其他元件外採）
    - **Nokia ramp = LITE/COHR 中度受惠**（部分 InP 元件 Infinera 自研、pump laser + WSS 仍外採）
    - [[Coherent]] Q3 FY2026 法說會「leading DCI OEM 拿到 uncooled 3-pin micropump multiyear design win」極大概率匹配 CIEN 或 NOK 或兩家
    - → 修正 [[CPO 供應鏈圖譜]] 賣水人位階「兩家對等受惠」描述：CIEN ramp 對 LITE/COHR 槓桿 > NOK ramp 對 LITE/COHR 槓桿（因 Infinera 部分內製）
  - 同步更新：
    - index.md「光通訊 / DCI / 光引擎（第五波）」分類段新增 [[Ciena]] / [[Nokia]] 兩條目（與 LITE/COHR 同段）
    - index.md「待 ingest 延伸 半導體 / 算力供應鏈 entity」段 CIEN/NOK partial → ✅ 已建
    - 本 log.md（追加本段）
  - 累計：**46 concept + 47 entity + 41 summary**（DCI 兩家 +2）
- ingest: **信昌電 6173 補完**（MLCC 賽道中高壓 niche 漏網）— 單 entity 補建
  - 觸發：[[MLCC 嵌入式基板賽道]] subagent 點名「信昌電中高壓 MLCC 在 NVDA Rubin 1MW 機櫃結構性受惠（3-4K → 10K+ 顆），但嵌入式滲透到高壓時會被切」
  - method：6 WebSearch + 2 WebFetch（BigGo FY2026 Q1 法說會 + 鉅亨網法說會詳細）並行
  - entity [[信昌電]]（6173.TWO）— **全台唯一陶瓷粉末自製 + 中高壓大尺寸 MLCC 垂直整合 niche specialist**
    - 上櫃股、母公司 **[[華新科]] 持股 43.13%**（集團子公司）
    - 主攻 1206-2220 + 千伏級 + **Mega Cap 堆疊式電容（單價 7-9x 一般單體）** + **NP0 共振電容（單價 3x+ 同尺寸 X7R）**
    - 2026 Q1 營收 NT$10.17 億（+8% YoY）/ EPS NT$1.19（+70% YoY）/ 毛利率 **28.4%**（+6.1pp YoY 跳升，從 22.3% 大幅 re-rate）
    - 市值 NT$370.7 億 / PE 57.77（同業均 119.07，**折價一半**）/ Re-rate 三角形 **3/4**
    - AI 占 6.5-8% → 全年 >10%、16 週交期 + 85-90% 稼動率 + 訂單能見度 6 個月以上
    - 客戶結構：透過電源 / BBU 大廠進 **NVDA Rubin AVL**（公司未具名、工商時報 2026-05-07 報導）
  - **⭐ NVDA Rubin 1MW 機櫃曝險數字驗證**（公司法說 2026-05-21 親口）：
    - GB200 132kW 機櫃：單 5.5kW PSU = 1,400-1,800 顆大尺寸 MLCC、單 BBU = 700-960 顆 → **單機櫃 3-4K 顆**
    - Rubin 1MW 機櫃：**逾 10,000 顆**（公司明示「直接突破 1 萬顆大關」）
    - ⚠️ **單一來源警告**：3K → 10K+ 僅公司法說自己揭露、未交叉驗證外資 / Digitimes / 賣方研報
    - 但 [[MLCC 嵌入式基板賽道]] concept 已引用 EE Times / Big News Network 「VR200 NVL72 機櫃 MLCC BOM USD 4,320（GB300 1,530 → +182%）」= 方向一致（~2.5-3x BOM 倍增）
  - **跟 [[國巨]] / [[華新科]] 業務 mix 差異化**（重要區分）：
    - [[國巨]]：鉭電容 #1（>50%）+ 晶片電阻 #1 + MLCC #3、全品線併購王、X6S 0402-0805 中小尺寸（GB200 主板 85%）
    - [[華新科]]：MLCC 純度 46.4% + 中階通用 + 630V 中高壓研發中、馬來西亞地緣分散
    - **信昌電**：MLCC 52% + 介電粉末 24% + **1206-2220 大尺寸 + 千伏級 niche**、垂直整合粉末自製
    - 三家**完全不重疊**：國巨打主板小尺寸、華新科打中階通用 + 中高壓研發、**信昌電專攻電源 PSU/BBU 大尺寸高壓**
  - **MLCC 嵌入式戰場曝險分析**：
    - **短期**（2026-2028）：✅ **niche 不被切**（中高壓嵌入式商業化未到、信昌電大放量）
    - **中長期**（2029-2031）：⚠️ **時程賽跑**——[[村田 Murata]] 2026 已量產 **1.25kV C0G 1210 size** = 高壓 MLCC 嵌入化物理條件具備
    - 真正威脅來自村田 / SEMCO 高壓嵌入版本，不是國內競爭
  - **五軸評分 19/25**（賽道 4 + 客戶分散 2 + IP 4 + 時點 5 + 估值 4）
    - 跟 [[Ciena]] / [[Coherent]] / [[Lumentum]] / [[Nokia]] / [[IBIDEN]] / [[欣興]] 同分
    - **niche 押注的高分代表**（賽道 + IP + 時點 + 估值四軸滿、客戶分散因 AI niche pure-play 本質弱）
  - **pair trade「多信昌電 / 空 [[華新科]]」分析**：
    - 體質 / 估值 / Re-rate / 嵌入式曝險四軸**全勝信昌電**：毛利率 +10pp、PE 折價 30%、Re-rate 3/4 vs 2/4
    - **同集團風險**（[[華新科]] 43.13% 持股）+ 流動性差距（370 億 vs 2,052 億）+ 上櫃處置股風險
    - **結論**：信昌電可獨立做多、不需 pair；如要對沖，**空中國 MLCC / 空 [[南電]] / 空通用 MLCC ETF** 比空 [[華新科]] 乾淨
  - 同步更新：index.md（MLCC 段補入信昌電條目）、log.md 追加本段
  - 累計：**46 concept + 48 entity + 41 summary**（信昌電 +1）

- 2026-06-05 ingest（[[太陽誘電 Taiyo Yuden]] + [[TDK]]） — **日系國際被動元件三巨頭最後兩隻補齊**（村田 + Taiyo Yuden + TDK，[[MLCC 嵌入式基板賽道]] 第二戰場完整 4 大玩家 entity 落地）
  - 任務來源：[[MLCC 嵌入式基板賽道]] subagent 之前漏網的「日陣營協同 / IP first-mover + 多元組合王」兩隻
  - 完成兩個 foreign_competitor entity：
    - [[太陽誘電 Taiyo Yuden]]（6976.JP）— **嵌入式 MLCC（ECP）IP 世界首發者**
      - 2025-08 玉村廠量產 1005M 22μF 嵌入式 MLCC（X6S 4V / X7T 2.5V）
      - 2025-11 加碼量產 2012 size 100μF 嵌入式 MLCC（sample ¥120/顆）= lineup 完整
      - FY2025 營收 ¥3,553 億（+4.1%）、淨利 ¥148 億（+535.9%、5.4 倍暴衝）、Q4 訂單破 ¥1,000 億（五年首見）+ book-to-bill 1.25
      - FY2026 自家指引營收 ¥3,840 億（+8.1%）+ OP +50%
      - 市值 ¥2.01 兆（USD 135 億）、一年漲 555%、Forward PE 82、分析師中位目標 ¥5,739（隱含 -64%、已 priced in to perfection）
      - 美系大型券商目標價 ¥7,100、CEO 對 AI 需求稱 "scary"
      - 全球 MLCC top 4（市佔 ~10%、日陣營第三）
      - **MLCC 嵌入式戰場：IP first-mover + lineup 完整**（純嵌入式 MLCC 路線、不同 Murata iPaS 鋁電解 + coil 整合模組範式）
      - 客戶 design-in 名單**未公開**（無 NVDA / Apple / hyperscaler 確認）= **校準點 1**
      - Re-rate 三角形 3/4 滿
      - 五軸 **19/25**：IP 軸 5 分（賽道唯一 5 分）、客戶分散 1 分（賽道倒數）= 純 IP first-mover 押注
      - 最大威脅：[[Samsung Electro-Mechanics]] 越南 USD 12 億嵌入式 MLCC 產線 2026 H2 量產 → first-mover IP 時間窗口僅 12-18 月
    - [[TDK]]（6762.JP）— **多元組合王 + SESUB 嵌入式模組獨家 + Apple iPhone 電池主供 + HDD 磁頭**
      - 四大事業群（能源裝置 55% / 被動元件 24% / 磁性 11% / 感測器 9%）
      - SESUB（Semiconductor Embedded in SUBstrate）：300μm 1-2-1 4 層基板 + IC + passives 全嵌、面積比傳統模組減 65%、偏 smartphone PMU + Bluetooth + 健康穿戴
      - FY2026 營收 ¥2.50 兆（+13.6%）、OP ¥272.4 億（+21.5%）創新高、四事業群全增
      - **CEO Saito 宣告 AI data center 用被動元件 10 倍成長 by FY2031**、AI 占總營收 15% by FY2027
      - 矽負極第 4 代 2026-09 上市（Apple 折疊機 / iPhone 17 Air 採用）
      - FY2027 自家指引營收 ¥2,580 億（+3%）+ OP ¥295 億（+8.3%）+ HDD 磁頭出貨 +50%、CapEx ¥370 億（+¥90 億）
      - 市值 ¥7.50 兆（USD ~470 億）、Forward PE 33.12、分析師中位目標 ¥2,947（隱含 -28%、已 priced in）
      - **MLCC 嵌入式戰場：SESUB 模組差異化 + 鋁電解 AI PSU 多腳賣水**
      - SESUB **尚未切到 AI server**（仍偏 smartphone PMU + Bluetooth + 健康穿戴）= **校準點 2**
      - Re-rate 三角形 2/4 滿（FY2027 OP 指引 +8.3% 比 FY2026 +21.5% 大幅放緩）
      - 五軸 **19/25**：多元組合 5 軸均 3-4 分無 weakness、規模 + 客戶廣度勝 Taiyo Yuden、IP 純度輸 Taiyo Yuden / Murata
  - **必返回 6 個問題的答案**：
    1. **太陽誘電 ECP 首發具體客戶**：**未公開**——產品 spec、廠房、時程全揭露（玉村 2025-08 + 11 量產），但客戶 design-in 名單沒公開；只有 CEO 評論 AI 需求 "scary" 暗示能見度極強。**結論：標「未驗證」**
    2. **TDK SESUB vs Murata iPaS 哪家技術更領先**：**範式不同、不直撞**——
       - SESUB = IC + passives 全埋 300μm 4 層、偏 smartphone PMU + Bluetooth（成熟商業化）
       - iPaS = 鋁電解 + 平面 coil + VPD power module、偏 AI server / accelerator package（高端化）
       - **客戶滲透 Murata iPaS 領先**（已切 AI 數據中心 power module）、技術新穎度兩家相當
       - 規模對比：村田 ¥18.97 兆 vs TDK ¥7.50 兆（2.5 倍）
       - **校準：iPaS 在 AI 鏈領先、SESUB 在 smartphone 鏈領先**
    3. **兩家對 [[國巨]] / [[華新科]] 是「擴大餅」還是「分食餅」**：
       - 中短期（2026-2028）：**擴大餅為主**——AI server MLCC TAM 4 倍（Goldman 估 FY2025→FY2030 ¥2,150 億→¥9,200 億）、台廠跟著吃漲價
       - 中長期（2028+）：**分食餅為主**——日陣營三家整鏈閉環、台廠純分立 MLCC 廠無嵌入式產品線、design partner 機會被擠
       - **對信昌電高壓 MLCC 利基的直接威脅**：TDK 高壓 + 鋁電解 800V → NVDA Rubin 1MW 機櫃高壓鏈直接競爭
       - **結論**：bull（量增）vs bear（mix 切走 mid-high end）並存、但 2028+ bear case 漸顯
    4. **五軸評分 + 跟既有對照**：
       - 太陽誘電 **19/25**、TDK **19/25**——與 SEMCO / IBIDEN 並列賽道第二集團
       - 村田 24/25 仍是賽道最高、5 軸均勝
       - 對照：太陽誘電 IP 軸 5 分賽道唯一、TDK 5 軸均 3-4 分多元組合無 weakness
    5. **校準之前 MLCC subagent 的估算（太陽誘電 18 / TDK 17）**：
       - **太陽誘電：18 → 19**（IP 軸從 4 改 5、因 2025-11 完整 lineup 確認 + 玉村廠製程 know-how 證實）
       - **TDK：17 → 19**（路線軸從 3 改 4，因 FY2026 CEO Saito AI 10 倍成長宣告 + Infineon SiC + 矽負極第 4 代多元線兌現；耗材軸從 4 維持但因 Apple 電池 + HDD 半耗材性質）
       - 兩家都實際比之前估值高 1-2 分、反映過去 6-12 月 AI 鏈兌現速度
    6. **嵌入式戰場 4 大玩家排名**：
       - **#1 [[村田 Murata]]（24/25）**——分立 MLCC 70%+ 高階 + iPaS 商業化 + 矽電容寡占三線並進全吃
       - **#2 [[Samsung Electro-Mechanics]]（19/25）**——載板 + MLCC + 矽電容 + Samsung 集團整合、規模 USD 92B、越南 USD 12 億產線 2026 H2 量產
       - **#3 [[太陽誘電 Taiyo Yuden]]（19/25）**——嵌入式 MLCC IP first-mover、lineup 完整、規模 USD 135 億 = 純技術突破型
       - **#4 [[TDK]]（19/25）**——多元組合王、SESUB 模組獨家但偏 smartphone、AI server 嵌入式 IP 仍輸 Taiyo Yuden / Murata
       - **=（#5 [[IBIDEN]] 19/25 載板廠陣營、不直接競爭）**
  - 同步更新：
    - index.md「MLCC / 被動元件」段插入 [[太陽誘電 Taiyo Yuden]] + [[TDK]] 兩條目（在村田之後 / 國巨之前）
    - [[MLCC 嵌入式基板賽道]] concept 的「待 ingest 延伸」段標 ✅ 已建
    - 本 log.md 追加本段
  - 累計：**46 concept + 50 entity + 41 summary**（Taiyo Yuden + TDK +2）

## 2026-06-08

- ingest: [[SK Hynix]] entity（**HBM 全球 #1 + NVDA 多年合約 anchor**）
  - 來源：raw/2026-06-08_Leo-黃仁勳定調記憶體結構性短缺-SK-Hynix-合約.md（Leo 個人觀察筆記 + 13 個 web 來源驗證）
  - 走完整 [[公司 Entity 模板（Step 1-3 三段式）]] + foreign_competitor 變體 + 時效 metadata（as_of/check_after/expires_on）
  - 核心 thesis：
    1. **HBM 全球市佔 50-62%**（Counterpoint Q3 2025 53% / Astute Q2 62% / TrendForce 2026 50%）vs Samsung 25-40% / Micron 5-20%
    2. **2026-06-08 NVDA multi-year partnership** = 不只 HBM、是全棧記憶體（HBM4 + LPDDR5X + 3D NAND）綁定四產品線（Vera Rubin / Vera CPU / RTX Spark / Jetson Thor）
    3. **NVDA HBM4 訂單分配**：SK Hynix ~70% / Samsung 25-30% / Micron 5-10%（UBS / TrendForce 2026 估計）
    4. **HBM 消耗晶圓是 DDR5 的 3 倍**（每 GB）+ SK Hynix 30% DRAM 產能已轉 HBM、2027 將近 40%
    5. **Q1 2026 營收 KRW 52.58T**（YoY **+198%**）+ OP **KRW 37.61T**（OP margin **72%**）+ 淨利率 77% = AI infra 等級獲利力
    6. **Forward PE 5.9-6.4x** vs Micron 7.8-9x = **Korea Discount 25-30%**；目標價共識 KRW 2.07M（+8.7% upside）/ fair value upgrade KRW 2.26M → 3.33M（+19% → +74%）
  - **NVDA 合約 4 產品線 specific terms**（已驗證）：
    - Vera Rubin AI 超級電腦：R100 GPU 288GB HBM4 @ 22 TB/s（2.75x Blackwell）、2027 H1 launch
    - Vera CPU：1.5TB LPDDR5X @ 1.2 TB/s、<30W、SOCAMM2 192GB 模組已量產
    - RTX Spark AI PC：128GB LPDDR5X @ 300 GB/s
    - Jetson Thor 機器人：128GB LPDDR5X @ 273 GB/s、256-bit bus
  - **2026-06-08 韓股熔斷**：KOSPI -8.29% 至 7,484（史上第 9 次熔斷）、SK Hynix -7.68% 收 KRW 1,911,000、Samsung -10.18%；三角觸發（Broadcom AI guidance miss + Fed 升息恐慌 + 伊朗以色列衝突）；典型 [[資訊擴散四階段]] 階段 3-4 散戶恐慌訊號
  - **對 [[PB 估值法（記憶體週期）]] thesis 的挑戰**：
    - PB 派：景氣循環、用 PB 守底
    - SK Hynix 案：Q1 OP 72% / NVDA 多年合約 / Hyperscaler 預付到 2028 / 客戶提議買 EUV + 出資建廠 = 結構性短缺
    - **混合估值法**：一般 DRAM（~40% 營收）走 PB / HBM 部分（~60% 營收）走 Forward PE 15-25x infra 級
    - 加權公平 PE 10-15x = 50-130% upside
  - **Leo 判斷校準**：「現在結構性短缺而非景氣循環」**thesis 成立**——5 大支撐：
    1. HBM/DDR5 wafer 3:1 物理性消耗倍數
    2. NVDA 多年合約 + 全棧記憶體綁定（不是純買賣）
    3. Macquarie 預測 2027 HBM 合約價 +50%、SK 集團主席「短缺到 2030」
    4. 客戶提議出資建廠 + 買 EUV 機器 = 產業內部訊號
    5. Samsung HBM4 落後 SK Hynix 2-3 季 + MR-MUF 製程 20% 良率優勢 = 結構性領先
  - **五軸評分 23/25**：
    - 賽道 5/5（HBM AI infra 最稀缺）
    - 路線 5/5（MR-MUF + HBM4 多軌）
    - IP / 站別 5/5（HBM3E/HBM4 全球首發、NVDA co-design）
    - 客戶分散 3/5（NVDA 集中度但 Google/AMD/全 hyperscaler 補位）
    - 時點 / 估值 5/5（Forward PE 6.4x 嚴重折價 + KOSPI 熔斷加碼點）
  - 同步更新：
    - [[HBM iPhone moment]] concept：末段加「2026-06-08 NVDA-SK Hynix 多年合約 anchor 確認」，連結 [[PB 估值法（記憶體週期）]] / [[SK Hynix]] / 半導體基礎建設化
    - index.md 新建「標的：記憶體（第五波 — HBM iPhone moment anchor）」段，置於「中國 AI」之前
    - 本 log.md 追加本段
  - 累計：**46 concept + 51 entity + 41 summary**（SK Hynix +1）

- ingest: concept [[AI 記憶體結構性供給短缺]]（**對抗 [[PB 估值法（記憶體週期）]] 的新估值範式 anchor concept**）— raw: `2026-06-08_Leo-黃仁勳定調記憶體結構性短缺-SK-Hynix-合約.md`、Leo 命題「建一個對抗 PB 派的 concept」
  - 任務性質：thesis 對抗型 concept，**核心命題：景氣循環論 vs 結構性短缺論**
  - 預期差來源：市場仍用 [[PB 估值法（記憶體週期）]] 景氣循環框架（KOSPI 給 SK Hynix Forward PE 5.92x、看作循環股），但 NVDA 2026-06-08 multi-year contract + 物理產能限制證實 thesis 已 over-shoot
  - 結構性短缺三大物理 driver（全部 WebSearch 驗證）：
    1. **HBM 每 GB 消耗 DDR5 三倍 wafer**（Tom's Hardware / TechTimes 2026-06）+ 每 wafer 營收 3-5x → 廠商已切走 93% 合計產能至 HBM
    2. **CoWoS 即使翻倍仍 sold out 至 2027**（TSMC 2024 35K → 2026 130K → 2027 170K wafer/月、仍 50+ weeks lead time），DRAM 廠擴產解不了封裝瓶頸
    3. **NVDA 4 條路線圖綁定**：
       - Vera Rubin AI 超級電腦 → HBM4 288 GB/22 TB/s（NVL72 rack 20.7 TB HBM4 + 54 TB LPDDR5X）
       - Vera CPU → LPDDR5X 1.5 TB / 1.2 TB/s（1024-bit / 8 SOCAMM）
       - RTX Spark AI PC → LPDDR5X 128 GB / 301 GB/s（GB10 Superchip）
       - Jetson Thor → LPDDR5X 128 GB / 273 GB/s
  - 震撼數字：Vera Rubin rack 記憶體 = $2M / $7.8M = **26% BOM**，前代 $373K → 暴增 **435-485%**（Tom's Hardware / wccftech）
  - 黃仁勳定調事件（2026-06-08）：
    - SK Hynix x NVDA multi-year technology partnership（[SK hynix Newsroom](https://news.skhynix.com/multi-year-tech-partnership-with-nvidia/) 一手）
    - 「AI 相關股票其實很便宜」+ 警告 shortage「持續多年」+「從 wafer 到 cable connector 全部短缺」
    - 同日 KOSPI 8.29% 熔斷（Samsung -10.18% / SK Hynix -7.68%）= [[資訊擴散四階段]] 末段警訊 + 1.02 億散戶帳戶單日熔斷
    - 三因子驅動熔斷：Broadcom 指引失望 + Fed 升息預期 + 以伊衝突
  - **核心 framework 創新：雙引擎估值（thesis switching trigger）**
    - HBM segment = Forward PE / DCF（infra 框架）
    - 傳統 DRAM / NAND = PB 估值法（[[PB 估值法（記憶體週期）]] 仍適用）
    - 切換 trigger：HBM 占比 > 40% + ASP YoY > 30% → 切到結構性短缺框架
    - 退場 trigger：HBM ASP 連續兩季 QoQ 負成長 → 退回 PB 框架
    - 校準 [[宋分備忘錄 #1 — CSP-AI 通縮]]「2028 預付訂單」: 現實已 over-shoot 到 2030 multi-year design-in（OpenAI Stargate 900K wafer/月 LOI + Micron 5 年合約 + SK Group Chey 2030 預警）
  - 風險完整評估（thesis 失效情境）：
    1. 模型效率躍進（DeepSeek 2.0、MLA + MoE）→ 但 [[Jevons Paradox（投資版）]] 反向
    2. AI 需求結構性放緩（CSP CapEx 物理上限、Micron Idaho fab 2027/2028 first-mover oversupply 是 bear case 時間錨）
    3. 替代記憶體技術（STT-MRAM、HBF、HBM4E + glass interposer 2028 路線）
    4. 反壟斷干預（2002 DRAM USD 6 億罰款歷史先例、NVDA-SK Hynix multi-year 審查風險）
    5. 韓國勞工 / 地緣風險（2026-05 Samsung 4.5 萬人罷工威脅）
    6. 散戶過度進場（已是訊號、韓股熔斷 1.02 億帳戶）
  - WebSearch 9 次驗證（HBM 3x wafer ratio / NVDA 多年合約 / Vera Rubin specs / Vera CPU / RTX Spark / Jetson Thor / CoWoS bottleneck / DRAM shortage 2030 / SK Hynix valuation / Vera Rubin rack BOM / bear case + DeepSeek tension）
  - 同步更新：
    - [[PB 估值法（記憶體週期）]] update：加入「⚠️ 2026-06-08 校準」段（雙引擎結構 + thesis switching trigger + LTA 部分修正 + 預付訂單意義重新解讀）；frontmatter updated 2026-06-04 → 2026-06-08、加入 raw source；標題改 → 「跟 [[HBM iPhone moment]] / [[AI 記憶體結構性供給短缺]] 的張力」；相關連結補 [[AI 記憶體結構性供給短缺]]
    - index.md：新建「**記憶體（HBM / DRAM 估值範式之爭）**」段（置於「Jevons Paradox」之後 / 「TGV / 玻璃基板賽道」之前），三條目（PB 估值法 / HBM iPhone moment / AI 記憶體結構性供給短缺 ⭐）成為 thesis triad
    - 本 log.md 追加本段
  - 累計：**47 concept + 51 entity + 41 summary**（AI 記憶體結構性供給短缺 +1）

- ingest: HBM **BIG 3 #2 + #3 entity 建檔（Samsung Electronics + Micron）** ⭐
  - 來源：raw/2026-06-08_Leo-黃仁勳定調記憶體結構性短缺-SK-Hynix-合約.md（與 SK Hynix entity 同源、互補完成 BIG 3 三家）
  - method：subagent 並行（與 SK Hynix subagent 同步、分頭做 BIG 3 #1/#2/#3）；8-12 WebSearch query/家 × 2 家 = ~24 query 全程 1 round
  - 同步更新：
    - [[Samsung Electronics]]（主公司 005930.KS）entity 建檔（明確區隔 [[Samsung Electro-Mechanics]] 子公司 009150.KS）
    - [[Micron]]（MU.NASDAQ）entity 建檔
    - index.md 把已建的 SK Hynix（line 112）section 合併進「記憶體 BIG 3 / HBM」段，三家齊整於 [[NVDA]]/AI 半導體之後、[[OpenAI]] 模型公司之前
  - **必返回 6 個問題的答案**：
    1. **HBM BIG 3 市佔 2026 最新對照**：
       - **SK Hynix**：50-62% HBM 市佔（最寬區間）、NVDA HBM4 份額 **60-70%**、Q2 2025 巔峰 62% / DRAM Q1 2026 ~27%
       - **Samsung**：25-40%（區間擴大、HBM4 開始反超 Micron）、NVDA HBM4 份額 **25-30%**、Google TPU 60%+ 主供、DRAM Q1 2026 **#1 重奪 38.5%**
       - **Micron**：5-24%（變化最大、Q3 2025 短暫越車 Samsung 至 18-21%）、NVDA HBM4 份額 **10-20%**、DRAM Q1 2026 #3 22.4%
       - **差距**：SK 是 Samsung 的 1.5-2 倍、Micron 是 Samsung 的 ~50-60%；NVDA HBM4 份額三家差距更明顯（60-70% vs 25-30% vs 10-20%）
    2. **Samsung HBM 追趕進度**：
       - **HBM3E**：Samsung 2025-09 終於通過 NVDA 12-Hi 認證（18 個月開發後）、過去 5 次失敗
       - **HBM4**：Samsung **業界第一家量產**（2026-02-12 Pyeongtaek P4/P5 月產 170k → 250k Q4）、HBM4 業界第一家量產給 NVDA 而非 SK Hynix
       - **HBM4E**：Samsung **業界第一家 sample**（2026-06-01）、Rubin Ultra 2027 design-in 領先
       - **校準**：Samsung HBM3E 落後但 HBM4 已**並駕齊驅** + HBM4E 領先；但 NVDA HBM4 25-30% 份額仍輸 SK 1.5-2 倍（NVDA 結構性綁 SK）
    3. **Micron 美國 anchor 對 NVDA 訂單影響**：
       - **CHIPS Act USD 6.4B 直補 + Big Beautiful Bill ITC**：USD 200B 20 年美國投資（USD 150B 製造 + USD 50B R&D + 9 萬工作）
       - **Idaho Fab #1**（2027 開出 DRAM 量產）+ **Fab #2**（2026 開工、2028 量產 + HBM 封裝）+ **New York 4 廠** + **Virginia HBM 封裝**
       - 對 NVDA 訂單影響：**地緣政治護城河 + 美系陣營偏好** → Micron 拿到 SOCAMM2 LPDDR5X 業界首發 design-in + HBM4 認證；但 NVDA HBM 主合約份額仍是 SK 60-70% 結構性綁定（非美國 anchor 能逆轉）
       - **校準**：Micron 美國 anchor 是「**估值便宜的政治護城河**」（Forward PE 8.45）而非「能搶 SK 主合約的籌碼」
    4. **Samsung 三條腿哪條最受惠 AI**：
       - **記憶體（HBM/DRAM）**：⭐⭐⭐⭐⭐ Q1 2026 DS OP KRW 53.7T（YoY **+48 倍**）、HBM 全 sold-out、Memory 段 OP > FY2025 全年
       - **Foundry**：⭐⭐⭐ Tesla AI6 USD 16.5B 至 2033 + Qualcomm S8E5 + Galaxy S26 Exynos 2600 captive，但**仍輸 TSMC 60+ 個百分點** + 2nm 良率 40-60% vs TSMC 60%+
       - **終端（DX）**：⭐⭐ Q1 2026 OP **YoY -35%**、Apple 高端流失、Galaxy 中國品牌夾擊
       - **Display（SDC）**：⭐⭐⭐ Apple iPhone OLED 主供 = 受惠 Apple 18/iPhone 18 顯示器訂單
       - **結論**：記憶體段 = 100% 受惠（Q1 2026 OP 占公司 93%+ OP）、Foundry = 期權（2028 Taylor 量產才實現）、終端 = 壓力源、Display = 順風車
    5. **五軸評分**：
       - **Samsung Electronics 21/25**——僅次 Murata 24（賽道最高）、SK Hynix（預估 22+）、與 Disco Corp 21 / Samsung Electro-Mechanics 19 並列
       - **Micron 20/25**——與 LPKF 並列、僅次於 Disco 21 / SK Hynix 22+ / Samsung 21
       - **三家差距**：SK Hynix 22+ > Samsung 21 > Micron 20——五軸分數差距僅 1-2 分（不像 HBM 市佔差距大），反映 BIG 3 都是相對 quality compounder
    6. **Leo 判斷校準「美光 / 三星都是 HBM 受惠者」**：
       - **成立但要打折**——三家不是齊頭並進、是「SK Hynix 領跑 + Samsung 追擊 + Micron 第三集團」三層結構
       - **HBM 純度排名**（推測 Leo 投資考慮）：SK Hynix（NVDA 多年合約綁定 + 50-62% 市佔）> Micron（HBM 全售罄 + Forward PE 8.45 最便宜）> Samsung（三條腿稀釋）
       - **三條腿排名**（如果你看 Samsung 的整鏈閉環）：Samsung > SK Hynix > Micron
       - **估值便宜排名**：Micron PE 8.45 > SK Hynix PE 6.4 (Korea Discount) > Samsung PE 23.92（最貴）
       - **NVDA 集中度排名**：SK Hynix（NVDA 主供）> Micron > Samsung（Google TPU 主供）
       - **校準結論**：「**美光 + 三星都受惠 HBM**」成立，但**投資策略要區分**：
         - 想要 HBM 純度 + NVDA 直接綁 → SK Hynix
         - 想要 HBM 純度 + 估值便宜 + 美國 anchor → Micron
         - 想要整鏈閉環 + 三條腿 + Foundry option → Samsung
         - 想要 HBM 玻璃載板 / MLCC / 相機模組 → Samsung Electro-Mechanics 子公司（**不要混淆**）
  - 累計：**47 concept + 53 entity + 41 summary**（Samsung Electronics + Micron +2）

## 2026-06-08 — ingest: 玻璃基板時間線 anchor + 2 新 entity + 4 update

- ingest: **2 新 entity + 4-5 既有 entity / concept update**（Leo 2026-06-08 raw + WebSearch 驅動）
  - 1 raw（`raw/2026-06-08_Leo-玻璃基板時間線-TrendForce-Serenity.md`）+ 10 WebSearch + 3 WebFetch
  - 觸發：Leo 整理 TrendForce + [[Serenity]] X 玻璃基板時間線（SKC Absolics 2026 H2 / SEMCO 2027 H2 / Intel 2030 / TSMC CoPoS 2-3 年）
  - 2 新 entity：
    - **[[Sumitomo Chemical]]**（4005.JP，住友化學）
      - 日本綜合化學集團 + 韓國 Dongwoo Fine-Chem 100% 子公司、SEMCO Glass Core JV 小股東 + Dongwoo Pyeongtaek 廠地
      - 市值 JPY 747B（USD 5B）、ICT & Mobility Solutions 段 FY24 JPY 607B（+19.6B YoY）/ Core OP +20.5B / ROIC 11% FY2027 目標
      - 半導體業務：光阻劑（ArF immersion + i-line thick film）+ 高純度製程化學品（Dongwoo 韓國 + 美國新廠）+ 化合物半導體 + 顯示器材料
      - 玻璃 core JV 角色：**化學材料側貢獻 + 韓國本土製造在地化**（推測）—— **具體技術角色未公開、2026 H2 正式合約才會揭露**（標 medium confidence）
      - 五軸 **20/25**（路線 3 / 站別 3 / 耗材 5 / IP 4 / 客戶分散 5）= 中性耗材賣水人 + JV 股權順手押注
      - Re-rate 三角形 0-1/4：綜合化學集團、不是純 thesis 半導體 / 玻璃 pure play
    - **[[Serenity]]**（@aleabitoreddit，X KOL）
      - 前 Reddit r/WSB 老手 + AI 研究科學家 + RISC-V Foundation 成員、2025 中期轉場 X
      - 2026-04：210k 粉絲 / YTD +1,525% / 16+ 部位翻倍；2026-05-06：付費訂閱 4.6 萬人（差 1,000 人超越 Elon Musk）、被中文圈譽為「AI 供應鏈教父」
      - 「Bottleneck Theory（瓶頸論）」：不買 NVDA、買 NVDA / 雲端業者**不能沒有的、無法被取代的物理供應鏈節點**
      - 13 層 AI 物理供應鏈框架、重押光電（AXTI 5x / AAOI 5x / [[Lumentum|LITE]] / SIVE / TSEM / AEHR）
      - 補的位階：**第一位英文圈 + 中文圈現象級雙語擴散的 chokepoint 分析師**（vs [[sennn.nnna]] 繁中製程級深度 / [[宋分（美股送分題）]] 估值教學 / wallstengine 法說會轉述 / aoyamaa 公司七件事）
  - 4 既有 entity / concept update：
    - **[[Absolics]]** 催化段加「🆕 2026-06-08 TrendForce 校準」anchor + AMAT 玻璃 handling 設備合作開發補強（specialized robotics + suction-based 運輸系統解玻璃易碎難題）+ wikilink [[Sumitomo Chemical]] / [[Serenity]]
    - **[[Samsung Electro-Mechanics]]** 催化段加「🆕 2026-06-08 TrendForce 校準」anchor（2027 H2 量產 + Sumitomo 合作 + Apple/AVGO/雲端目標客戶確認）+ 韓+日整鏈閉環四方描述
    - **[[玻璃基板與 FOPLP 賽道]]** concept 開頭新加「⭐ 2026-06-08 完整時間線（TrendForce + Serenity 整理）」段：四節點時間線表 + 三段式 narrative（2026 H2 第一波 anchor / 2027 H2 主流 / 2028+ TAM 放大）+ 校準訊號（AMAT 設備合作 + 魏哲家 CoPoS 2-3 年 + Intel 2030 雙廠標準化）
    - **[[Intel]]** entity 新加「玻璃基板路線」段（IP licensing 2025-08 + Clearwater Forest 2026 H2 + EMIB 給 Amkor）+ 「🆕 2026-06-08 校準」催化段（2030 量產 + 亞利桑那 / 新墨西哥州雙廠標準化）+ 風險段（量產時程落後 Absolics / SEMCO / TSMC）
    - **[[TSMC]]** entity 新加「CoPoS 玻璃中介層」段（魏哲家 2026-06 股東會 + pilot line + Corning 玻璃 sheet 合作）+ 「🆕 2026-06-08 校準」催化段（CoPoS 2-3 年量才放大）
  - 同步更新：
    - index.md：「分析師」段加 [[Serenity]]、「TGV 玻璃材料」段加 [[Sumitomo Chemical]]、Absolics + SEMCO 條目加 2026-06-08 校準標籤
    - 本 log.md（追加本段）
  - **必返回 5 問答**：
    1. **Sumitomo Chemical 在 SEMCO 玻璃 core JV 的具體角色**：**未公開**（公告僅提「technology accumulated by Sumitomo Chemical」+ Dongwoo Pyeongtaek 廠地 + 小股東）—— 推測**化學材料側貢獻（光阻 / 樹脂 / 高純度製程化學品）+ 韓國本土製造在地化**，但不會自己賣玻璃 sheet（vs AGC / Corning）；2026 H2 正式合約才揭露 → 標**「未驗證、推測角色」medium confidence**
    2. **Serenity X profile 找到了沒**：✅ 完整——@aleabitoreddit、前 r/WSB + AI 研究員、2025 中轉場 X、Bottleneck Theory、210k → 500k 粉絲、付費訂閱 4.6 萬人、重押光電（AXTI/AAOI/LITE）= 中文圈現象級雙語擴散
    3. **TrendForce 時間線 vs 之前 Absolics subagent 報告對照**：**一致 + 補強**——Absolics 2026 H2 量產（wiki 既有 entity 一致）+ AMD MI400（一致）+ AWS Trainium（既有）+ AVGO non-embedding（既有）；新訊號**「Applied Materials 支持」不只 29.9% 持股、還包括玻璃高速組裝 handling 設備合作開發**（從 Digitimes / SKC 1.2 trillion won 增資相關報導補強）
    4. **「Applied Materials 支持 Absolics」具體細節**：（a）2023-01 AMAT 出資 USD 39M / 51 億韓元、取得 29.9% 持股（既有）；（b）**2025-2026 玻璃 handling 設備合作開發**（新）—— specialized robotics + suction-based 運輸系統解玻璃易碎難題（high-speed assembly bottleneck）、是設備 + 投資雙重承諾、不只財務 stake；（c）AMAT 同時是 SEMCO / Intel 等對手鏈的設備商 → 中性賣水人結構維持
    5. **魏哲家「CoPoS 2-3 年」校準是否真有此發言**：✅ **真有**——2026-06 TSMC 股東會明確表態「先進封裝永遠是世界第一、CoPoS 試產線已建置、CoPoS 仍需 2-3 年量才會明顯擴大」（聯合新聞網 / 經濟日報 / 業務情報媒體多家報導）；跟 TrendForce 市場預期相當接近（2028-2029 量產）= Leo 引用準確
  - 累計：**47 concept + 55 entity + 41 summary**（Sumitomo Chemical + Serenity +2）

- ingest: **[[AI infra CapEx 三階段論]] 第三階段最關鍵 anchor entity — IQE**（Leo 2026-06-08 raw 補完 + 三家整鏈喊緊時序檢核）
  - 1 新 entity：
    - **[[IQE]]**（LSE: IQE.L、International Quantum Epitaxy）
      - 全球純 play 化合物半導體 epi（磊晶）代工龍頭、InP / GaAs / GaN / VCSEL 整合 epiwafer foundry
      - **2024 推出全球首條 6" InP DFB Laser 平台**（同業仍主流 4 吋、單晶圓 die ~2.25x）+ 6" InP PIN photodetector / FP / EML
      - InP epi 全球**三家獨立 pure-play** 之一（vs LandMark Optoelectronics、VPE），是 [[Lumentum]] / [[Coherent]] 自家 InP fab 容量瓶頸補位
      - **2026-04 £81M 融資 + MACOM £45M 戰略入股 11.5% + 長期供應協議**（COO+VP 進董事會）、淨現金 +£27.9M
      - FY 2025 photonics 段 £57.1M（+15% YoY）、總營收 £97.3M（-17.6% YoY 因 wireless -40%）、**FY 2026 自家指引 >20% 成長 + adjusted EBITDA 轉盈剛起步**
      - 產能：**英 3 廠**（Cardiff HQ、Newport 大廠世界最大化合物 epi foundry、Milton Keynes）+ **美 3 廠**（Greensboro NC 主力、Taunton MA、Spokane WA；Pennsylvania Bethlehem 2024-12 售出）+ **台 1 廠**
      - 市值 **£594M（USD $688M）**、12M 漲幅 +900-1,300%、Re-rate 0-1/4（仍 thesis 階段）
      - 五軸 **17/25**（路線 4 / 站別 4 / 耗材 3 / IP 4 / 客戶分散 2）= **比 LITE/COHR 低 2 分**，主要在站別 / IP 略遜（非 EML 唯一量產者、非規模龍頭）
      - **三階段論第三階段最關鍵 anchor 上游 entity**
  - 2 既有 entity update：
    - **[[Coherent]]** 催化段加 🆕 2026-06-08 InP 供應緊繃 anchor（InP delivery >26 週 + 影響 15-20% 營收 + 整鏈三家 2026-05 同月喊緊時序校準）+ wikilink [[IQE]] + sources 加 2026-06-08 raw
    - **[[Lumentum]]** 催化段加 🆕 2026-06-08 InP 供應緊繃 anchor（供應限制延伸 2026 全年 + EML 缺口 >30% + 日本 wafer fab fully allocated）+ wikilink [[IQE]] + sources 加 2026-06-08 raw
  - 1 既有 concept update：
    - **[[AI infra CapEx 三階段論]]** 訊號 2 表格三家公司加日期具體時點（COHR 2026-05-06 / LITE 2026-05-05 / IQE 2026-04 + 2026-05-28）+ wikilink IQE 全部由 ⚠️ 改為 ✅
  - 同步：
    - index.md：新增「**標的：InP 上游 epi / 化合物半導體（第五波）**」sub-section + [[IQE]] 條目（在 Nokia 之後、中國 AI 之前）
    - 本 log.md（追加本段）
  - **必返回 6 問答**：
    1. **IQE 2025-2026 具體融資金額 + 20%+ 成長指引 source**：✅ **£81M 總計（2026-04 公告）**——MACOM £45M（£30M 股權 = 151.5M 股 @ 19.8p 取得 11.5% + £15M 無息可轉換票據）+ £23M 現有 noteholder 再投資 + £13M placing/retail；HSBC RCF 還清後淨現金 +£27.9M。FY 2026 指引 **>20% 營收成長 + high-single digit ~ low double-digit £M adjusted EBITDA**（2026-05-28 IQE FY 2025 results 公告）
    2. **IQE 美/英/台產能比例 + 主要客戶**：英 3 廠（Cardiff、Newport 大廠、Milton Keynes）+ 美 3 廠（Greensboro NC、Taunton MA、Spokane WA；Pennsylvania Bethlehem 2024-12 售出）+ 台 1 廠（位置公開度有限）；**主要客戶**：MACOM（11.5% 股權 + 長期供應）+ [[Lumentum]] / [[Coherent]] 業界共識補位但**未直接 disclosure**（confidence: medium）+ 美國國防 / 航太（aerospace & defence 段 H2 2025 美軍方資金釋出）+ 智慧手機 VCSEL
    3. **IQE vs [[Sumitomo Chemical]] InP 業務對比**：**完全不是對手、是平行賽道**——[[Sumitomo Chemical]]（4005.JP）主做半導體光阻劑 + 高純度製程化學品 + SEMCO 玻璃 JV、不直接做 InP；**真正的 InP 對手是 Sumitomo Electric（5802.JP）+ SESMI**，他們做 InP **substrate**（基板）= IQE 的**上游原料**。IQE 是 substrate 之上的 epi 層代工，跟 LandMark Optoelectronics / VPE 並列三家獨立 pure-play epi house
    4. **Coherent + Lumentum + IQE 三家「整鏈喊緊」是否真的成立（時序檢核）**：✅ **完全成立 + 時序高度收斂**——LITE Q3 FY26 法說 **2026-05-05**（供應限制延伸 2026 全年 + EML 缺口 >30%）+ COHR Q3 FY26 法說 **2026-05-06**（InP delivery >26 週 + 影響 15-20% 營收）+ IQE FY 2025 results **2026-05-28**（£81M 融資 + FY 2026 >20% 成長指引）= **三家在 2026-05 4 週內同月喊緊**、整鏈瓶頸時序高度收斂、**不是巧合**
    5. **五軸評分**：IQE **17/25**（路線 4 / 站別 4 / 耗材 3 / IP 4 / 客戶分散 2）；比 LITE 19/25 + COHR 19/25 **低 2 分**——主要在站別（不是 EML 唯一量產者）+ IP（不是 InP 純度首選）略遜；但反映「pure play 上游期權」性質
    6. **三階段論第三階段最有 alpha 的 entity 是 IQE 還是 LITE/COHR？**
       - **IQE = 最尖端 alpha + 最尖端風險**（最小市值 + 純 thesis + 6" 平台 industry-first option、若 thesis 完美實現 +200%、若 thesis 失效 -50%+）
       - **LITE = 最確定品質 alpha**（200G EML 唯一量產者 + NVDA $2B + Greensboro 2028 anchor 確定，回檔 floor 較硬）
       - **COHR = 最 hedged 但 alpha 較小**（SiC 第二曲線 hedge、回檔最輕但翻倍空間最有限）
       - **Leo 最佳策略：「LITE + COHR 一籃子 anchor 部位 + IQE 5-10% 衛星期權部位」**——anchor 是 thesis 不變的核心、IQE 是「第三階段最尖端 alpha + 最尖端風險」的選擇權型衛星部位、必須**季季追蹤** photonics 段成長率 + LITE/COHR fab 進度 + MACOM 關係穩定性
  - 累計：**47 concept + 56 entity + 41 summary**（IQE +1）

## 2026-06-08（CPO 戰場 4 家漏網 entity 補位 — Stage 1 MPS）
- ingest: **CPO 漏網 entity 第 1 家 — [[MPS]]（MPWR、Monolithic Power Systems）**（subagent 並行交付、逐一落地）
  - 任務背景：CPO 戰場 8 層分工已建主要玩家（[[AVGO]] / [[Marvell]] / [[Lumentum]] / [[Coherent]] / [[Ciena]] / [[Nokia]] / [[SiTime]] / [[TSMC]] / [[IQE]]），仍漏 4 家：MPS（第 7 層電源）/ Amphenol（第 6 層連接器）/ POET Technologies（矽光初創）/ Ayar Labs（光晶片初創，需先確認 public/private）
  - 走 [[公司 Entity 模板（Step 1-3 三段式）]] + foreign competitor 變體 + 時效 metadata + 五軸 25 分制
  - **[[MPS]]**（NASDAQ: MPWR）—— CPO 第 7 層電源賣水人
    - 一句話定位：「**AI server 電源管理 IC 最薄但最關鍵站位**」——BCD 製程整合 + 模組化 power module 雙產品線、直接卡在 NVDA GPU + hyperscaler AI server 的「最後一吋電源轉換」
    - Q1 2026 營收 **$804.2M（YoY +26.1%、QoQ +7.1%、創高）**、EPS $5.10 beat、**Enterprise Data YoY +97.7%**
    - Q2 2026 指引 **$890-910M**（加速）、Enterprise Data 段全年成長下限指引從 +50% **拉高到 +85%**、製造產能目標上修到 **$6B**
    - **NVDA Blackwell 60-70% 流失給 Infineon**（Edgewater Research / Stocktwits 2025-04 起證實）+ Renesas 切入 digital power
    - **NVDA Vera Rubin（VR200 NVL144 / R200 HGX）反攻 ~70% 市佔**（KeyBanc 供應鏈研究 2025-10）+ 預估 **2026 增收 $100M+、2027 年化 $420M、EPS +$4**
    - **CPO 第 7 層光模組電源切入**（Q1 2026 法說會明點 enterprise data 成長驅動 = "AI、server power、optical modules"）
    - 股價 **$1,624.99（2026-06-02）**、市值 **~$81-83B**、Forward PE **52-68 倍**（GuruFocus 52、Simply Wall St 68）、GF Value 判定 overvalued 54%（公允價值 $1,053）
    - GAAP 毛利率 **55-56%**、12M YTD +70%
    - Re-rate 三角形 **2/4**（營收品質 + 營業利益 ✅、毛利率 + OpEx ⚠️）
    - 五軸 **17/25**（路線 3 / 站別 4 / 耗材 3 / IP 3 / 客戶分散 4）
    - vs [[SiTime]] 21/25：SiTime 中性純度 + 平方放大 vs MPS 可替代 + 線性放大 = **SiTime 為 CPO 中性賣水人首選，MPS 為 AI server 電源 + CPO 第 7 層配套**
    - vs [[Marvell]] 18/25：Marvell IP 路線數略勝、MPS 客戶分散勝 = 接近平手
    - **Rubin 反攻時程**：2026 Q1-Q2 黃金期 / Q3-Q4 空窗（Blackwell 流失影響顯現、Rubin 未量產）/ 2027 H1 Rubin 量產（市場 price in）/ 2027 H2 Rubin Ultra 才是真 alpha（5.7kW GPU = power IC BOM 三倍放大）
  - 同步：
    - index.md：**「標的：半導體製造 / 算力供應鏈」** 段加入 [[MPS]] 條目（在 [[SiTime]] 之後）
    - 本 log.md（追加本段）
  - 必返回 5 點：
    1. **Ticker**：MPWR（NASDAQ）✅ 確認 public
    2. **一句話定位**：AI 資料中心電源管理 IC「最薄但最關鍵」站位、CPO 第 7 層中性賣水人
    3. **五軸總分**：**17/25**
    4. **CPO 戰場位置 + 對台廠意義**：第 7 層電源（與 Renesas / Infineon / ADI / TXN 同層）；台廠 ODM（鴻海/廣達/緯穎）透過 ODM 採購 MPS PMIC = 間接連動；台達電/光寶為「電源系統」廠（PSU+BBU）= 層級不同、無直接競爭
    5. **五大催化 / 風險**：
       - 催化：Vera Rubin 70% 反攻 + 光模組電源 CPO 切入 + Enterprise Data +85% 下限指引 + 製造產能 $6B 上修 + 1.6T 光模組 BOM 翻倍
       - 風險：NVDA 集中度（估 15-25% 營收）+ Blackwell 60-70% 流失給 Infineon + Forward PE 52-68 估值高 + 2026 Q3-Q4 空窗期 + GF Value overvalued 54%

- ingest: **CPO 漏網 entity 第 2 家 — [[Amphenol]]（APH）**（subagent 並行交付、逐一落地）
  - **[[Amphenol]]**（NYSE: APH）—— CPO 第 6 層連接器三軌賣水人
    - 一句話定位：「**全球高速互連 connector 龍頭、CPO 第 6 層三軌賣水人（高速電 + 光纖 + 電源）**」——電子連接器 / 互連方案龍頭、IT Datacom 段最大且最快成長（Q1 2026 占 41%）
    - Q1 2026 營收 **$7.62B（YoY +58%、創高、beat $7.09B 預期）**、EPS $1.06（+68% YoY、beat $0.94）
    - **IT Datacom 段 +99% YoY（含 CCS）/ organic +81%** = 純 AI 驅動成長
    - **訂單 $9.435B（YoY +78%、book-to-bill 1.24:1）** = 訂單能見度 4-6 季
    - Q2 2026 指引 **$8.1-8.2B**（YoY +43-45%）+ EPS $1.14-1.16（+41-43%）
    - **NVDA GB200 NVL72 NVLink spine 獨家初始 Paladin HD 224G/s connector + Ultrapass backplane**（每 NVL72 用 18 個、每 Blackwell GPU 連 72 differential pair）
    - **2026-01 完成 $10.5B 收購 CommScope CCS**（fiber optic + rack-to-rack、2026 全年加 $4.1B 營收、EPS +$0.15）= **主動 hedge 光化風險**戰略
    - 股價 **$139.56（近 2026-05）**、市值 **$157B**、Forward PE **29.15-29.51**、GF Value $133（fairly valued、stock 略 overvalued 4.9%）、GF Score 97/100、12M +98.4%
    - 客戶分散度極高：**100,000+ 客戶、無單一客戶超過 10%**（vs MPS NVDA 集中度 15-25%）
    - 競爭對手：TE Connectivity（TEL）、Molex（Koch 子公司、私有）、Yamaichi、Hirose、Foxconn FIT
    - Re-rate 三角形 **3/4**（營收品質 + 毛利率 + 營業利益 ✅、OpEx ⚠️ CCS 整合）
    - 五軸 **20/25**（路線 5 / 站別 4 / 耗材 4 / IP 3 / 客戶分散 4）
    - vs MPS 17/25 + SiTime 21/25：APH 寬度 + 估值乾淨 + 客戶分散最高、是「**乾淨進場 AI infra exposure 最佳選擇**」
    - 中期風險：2028-2030 scale-up 224G 銅纜 backplane 光化（部分萎縮 30-40%）、但 mix shift 到 MPO/MTP 光纖 connector + 電源 connector（CCS 補完）
  - 同步：
    - index.md：**「標的：半導體製造 / 算力供應鏈」** 段加入 [[Amphenol]] 條目（在 [[MPS]] 之後）
    - 本 log.md（追加本段）
  - 必返回 5 點：
    1. **Ticker**：APH（NYSE）✅ 確認 public
    2. **一句話定位**：全球高速互連 connector 龍頭、CPO 第 6 層三軌賣水人（高速電 + 光纖 + 電源）、「乾淨進場 AI infra exposure 最佳選擇」
    3. **五軸總分**：**20/25**（4 家中第 2 高）
    4. **CPO 戰場位置 + 對台廠意義**：第 6 層連接器（與 TE Connectivity / Molex / Foxconn FIT 同層）；**台廠：鴻海 FIT 是 APH 直接對手**（高速 connector 領域）、鴻海整機 server（NVDA DGX）APH 是 backplane connector 直接供應、廣達/緯穎 ODM 也採購 APH connector
    5. **五大催化 / 風險**：
       - 催化：NVDA GB200 NVL72 Paladin HD 獨家初始 + CommScope CCS $10.5B 收購補完光纖 + 訂單 $9.4B book-to-bill 1.24 + Q2 指引 +41-43% + 客戶分散度高（>100,000 客戶無單一 >10%）
       - 風險：2028-2030 scale-up 銅纜 backplane 光化 + CommScope CCS 整合風險（商譽 ~$5B+）+ Forward PE 29-30 已 price in + AI CapEx 週期化風險 + China 製造/銷售曝險

- ingest: **CPO 漏網 entity 第 3 家 — [[POET Technologies]]（POET / PTK）**（subagent 並行交付、逐一落地）
  - **[[POET Technologies]]**（NASDAQ: POET / TSXV: PTK）—— CPO 第 2 層光引擎整合 platform 初創 option play
    - 一句話定位：「**矽光 Optical Interposer / EOI 整合 platform 初創、CPO 第 2 層 option play**」——把 lasers + modulators + 矽電子整合在 wafer-scale interposer、alignment-free wafer-scale 製程核心 IP
    - **Ticker**：POET（NASDAQ）+ PTK（TSXV）= ✅ 確認 public（dual-listed）
    - Q1 2026 營收 **$503K（YoY +200% 但規模仍極小）**、beat $250K 預期
    - Q1 2026 淨損 **-$12.3M（-$0.08 EPS）**（vs 2025 Q1 淨利 $6.3M 大幅倒退）
    - 累計 R&D ~$20M（800G + 1.6T Tx/Rx chiplets + Optical Interposer + 外部光源 + CPO）
    - **2026-05-14 與 Lumilens 簽戰略供應 + JV**：初始 **$50M PO + $500M five-year framework** + 22.9M 股 warrant @ $8.25 九年期、工程樣品 **2026 H2** / 量產 **2027** 對齊 hyperscaler
    - 自家 2026 規劃出貨 **>30,000 光引擎**
    - 歷史合作：Mitsubishi Electric Teralight 1.6T（4 lasers vs 業界 8 lasers）+ Foxconn FIT 800G/1.6T pluggable（馬來西亞廠）+ Celestial AI ELS（已被 [[Marvell]] 收）
    - **Nightmare Market Research 2026 公開質疑** Marvell / Foxconn / LITEON / Lumilens 多家 partnership 為「recycled hollow promotion」
    - 股價 **$11.68（2026-06-07）**、52 週區間 **$3.87-$20.81（5x 區間）**
    - 市值多源差異大：$0.93B / $2.05B / $2.27B（計算方式不一致需查證、warrant 結構複雜）
    - **無 forward PE**（虧損中）= 無估值錨點
    - Re-rate 三角形 **0/4**（典型矽光初創）
    - 五軸 **13/25**（路線 3 / 站別 2 / 耗材 3 / IP 3 / 客戶分散 2）= 4 家中最低
    - 競爭定位（重要校準）：
      - **Ayar Labs 被 [[NVDA]] $6.5B 收（2026-05）**= 矽光閉門 + POET 短期打擊
      - **Celestial AI 被 [[Marvell]] 收（2025-08）**= POET 客戶關係變更
      - **POET 是矽光初創整合 platform「最後一家獨立 option」**
      - vs Lightmatter（光學運算未上市）/ AVGO 自研 / TSMC + OSAT 整合
    - **投資定性**：「**催化劑驅動 option play**」、不適合 anchor 部位、衛星 1-3%（不超過 5%）
    - 退場條件：30,000 光引擎指引 miss / Lumilens framework 實現率 <20% / 任何主要 partnership 再被質疑 dead / 稀釋融資 round >$50M
  - 同步：
    - index.md：**「標的：光通訊 / DCI / 光引擎（第五波）」** 段加入 [[POET Technologies]] 條目（在 [[Nokia]] 之後）
    - 本 log.md（追加本段）
  - 必返回 5 點：
    1. **Ticker**：POET（NASDAQ） + PTK（TSXV）✅ public 確認 + dual-listed
    2. **一句話定位**：矽光 Optical Interposer / EOI 整合 platform 初創、CPO 第 2 層「催化劑驅動 option play」、最後一家獨立矽光整合 platform（Ayar/Celestial 已被收）
    3. **五軸總分**：**13/25**（4 家中最低）
    4. **CPO 戰場位置 + 對台廠意義**：第 2 層光引擎（整合 platform 端）+ 跨第 5 層先進封裝；**台廠 Foxconn FIT 是 POET 製造夥伴**（馬來西亞廠 800G/1.6T pluggable）、其他模組廠（旭創/新易盛/Innolight）未直接採用 POET 光引擎
    5. **五大催化 / 風險**：
       - 催化：Lumilens $50M PO + $500M five-year framework + 工程樣品 2026 H2 / 量產 2027 + 30,000 光引擎出貨指引 + Mitsubishi Teralight 4 lasers 成本優勢 + Foxconn FIT 馬來西亞廠
       - 風險（**遠多於催化**）：Q1 $503K 規模極小 + Nightmare Market Research 質疑多家 partnership dead + Ayar/Celestial 被收後賽道整合擠壓 + 市值來源差異大（$0.93-2.27B）+ 5x 區間極高波動 + 無 PE 估值錨點 + 反覆稀釋融資 + 執行風險 > 技術風險

- ingest: **codex P1-7 補位 — 3D NAND 沒獨立戰場**（1 concept + 3 entity、NVDA 路線圖第三條記憶體腿補完）
  - 1 新 concept：
    - **[[AI infra 3D NAND 戰場]]**
      - 回答 codex P1-7 提的關鍵問題「3D NAND 是主戰場還是附屬 BOM？」→ Leo 判斷 **「半主戰場 + 半附屬 BOM」**（目前 60% 附屬 BOM、40% 主戰場、2027 H2 HBF 落地後升到 60% 主戰場）
      - 三軸對照：HBM（主記憶體 / 寡占 3 家）vs LPDDR5X（系統記憶體）vs **3D NAND（儲存 / 6 家分食）**
      - 4 大玩家結構（Q1 2026 Counterpoint）：Samsung 29% / SK+Solidigm 22% / Kioxia 14% / Micron 13% / SanDisk 13% / YMTC 13%
      - **NAND BIG 6 結構變化（2025-2026）**：
        - 2025-02-24 [[Western Digital]] 分拆 SanDisk → WDC 變純 HDD、SanDisk 接 NAND（NASDAQ: SNDK）
        - 2024-12-18 [[Kioxia]] IPO（1,455 yen → 36,000 yen 18M +2,400%）
        - SK Hynix 透過 [[Solidigm]] 全包 enterprise QLC（51% majority share 2025）
      - **NVDA 4 產品路線圖 NAND 用量**：Vera Rubin NVL72 = 1,152TB SSD/rack（ICMS）= NAND BOM $1M+/rack；其他 3 個產品（Vera CPU / RTX Spark / Jetson Thor）NAND 是 BOM 配角但路線圖鎖死
      - Enterprise SSD vs Consumer NAND：合約價 Q1 2026 +60% vs +40% / 同 wafer 切 enterprise = 切 consumer 3-5 倍營收 / Phison CEO 2026 售罄、2027 pricing apocalypse
      - **PB 估值法仍適用嗎**：✅ 分段適用——Consumer NAND 保 PB / Enterprise SSD 切 Forward PE 10-15x / AI Enterprise SSD 切 Forward PE 15-20x（infra 半套用）
      - **HBF (High Bandwidth Flash) 2026-02-25 SanDisk + SK Hynix 標準化**：NAND-based 替代 HBM 部分功能、容量 8-16× HBM、頻寬 1.6TB/s、量產 2027；NAND 開始長出 HBM 形狀
      - **與 HBM iPhone moment 對比**：本 concept 是它「**遲到 12-18 個月的姊妹篇**」（2026 H2 啟動、2027 H1 anchor 確認、2028 全 re-rate）
  - 3 新 entity：
    - **[[Kioxia]]**（TYO: 285A、原 Toshiba Memory）
      - **NAND #3（14% 市佔）+ Enterprise SSD 純度最高 pure-play + 日本國家半導體最後一張牌**
      - 2024-12-18 從 Bain Capital 私有化 6 年後 IPO 重返東京 Prime Market（1,455 yen → 36,000 yen / 18 個月 +2,400%）
      - FY2025 營收 **¥2.34T**（YoY +37%）+ OP **¥876B**（YoY +95%）創歷史新高、Q4 OP +314% QoQ
      - **BiCS 8（218-layer）量產 + BiCS 10（332-layer）2026 提前量產**（原 2027、加速到 2026）
      - **CBA 製程獨家**（CMOS Bonded to Array）vs Samsung V9 string stacking 製程哲學分歧
      - Bain Capital 持股 <30%（2026-03 減持後）+ 套現 $3.5B + Nikkei 225 納入（2025 H2）
      - 跟 SanDisk 從 JV 解體（2024-2025）→ HBF 標準化合作重建（製造分離、客戶分離 50/50、HBF 三方標準化）
      - 市值 USD ~110-125B / Forward PE 15-20x / Re-rate 4/4
      - **五軸 19/25**（時點扣分 +2,400% 後接 Bain 棒、其他四軸接近 HBM BIG 3 水準）
    - **[[Western Digital]]**（NASDAQ: WDC、2025-02-24 純 HDD 公司）
      - ⚠️ **2025-02-24 完成 SanDisk spin-off 後變身純 HDD pure-play**——本 entity 不再是 NAND 戰場玩家、是 NAND 戰場 rival（HDD 端）
      - **全球 HDD 雙頭壟斷 #1（45% 市佔 / nearline 主導）+ AI 資料中心儲存 rival storage 最大受惠者**
      - Q3 FY2026 營收 **$3.34B**（YoY +45%）+ Cloud **$3.0B**（占 89%、YoY +48%）+ nearline 出貨 **199 EB**（YoY +37%）
      - GAAP 毛利率 **50.2%** + non-GAAP 50.5% 創歷史新高（UltraSMR mix > 50% margin booster）
      - **2026 全年 HDD 產能售罄 + 多年合約延伸 2027-2028** + Q4 guidance $3.65B / 毛利率 51-52%
      - 12 個月漲幅 **+880-970%**（mega re-rate）/ YTD 2026 +115-155%（S&P 500 top-5 performer）
      - HAMR 路線追 Seagate 落後（Seagate 已先 ramp、WDC 2026 H2 起追）
      - 市值 USD ~$180B / Forward PE 15-25x / Re-rate 4/4
      - **五軸 15/25**（NAND 戰場 rival、非戰場玩家、賽道扣分；但 storage AI 主題 1-2% 衛星對沖配置）
    - **[[Solidigm]]**（[[SK Hynix]] 100% 子公司 / 私有公司 / 不可直接押注 stub entity）
      - **SK 集團 Enterprise QLC SSD pure-play 子公司**（QLC 全球市佔 **51% / majority share**）+ **從 Intel NAND 部門 2021 USD 9B 收購**而來
      - 2024 全年營收 **KRW 9.3T** / 淨利 KRW 613B / **2026 估營收 11.8T**（USD ~$8.6B）/ 淨利 **1.4T**（+128%）
      - **Enterprise 100% pivot 完成**（2024 退出 consumer 市場）+ **245TB PCIe Gen5 QLC**（PS1101 / PS1012）AI workload 主推
      - 黃仁勳 2026-06-08 NVDA-SK Hynix 多年合約「3D NAND 棧」隱性主供之一
      - 跟 [[Kioxia]] 對比：純度更高（95%+ Enterprise vs Kioxia 50%）但製程跟隨（V8/V9 vs Kioxia BiCS 8/10 領先）
      - **押注路徑：必須透過 [[SK Hynix]] 母公司**（KRX: 000660）——Solidigm 是 SK Hynix HBM 主戰場 + NAND 第二曲線整合的隱性 sweetener
      - 假設 IPO 五軸 17/25（時點扣分 private 無估值釋放）；但作為 SK Hynix 23/25 評分的一部分已含
  - 同步：
    - index.md：
      - 「3D NAND / Enterprise SSD（codex P1-7 補位、第七波）」concept 段加 [[AI infra 3D NAND 戰場]]
      - 「標的：3D NAND / Enterprise SSD（第七波）」entity 段加 [[Kioxia]] / [[Solidigm]] / [[Western Digital]]（在 Micron 之後）
    - 本 log.md（追加本段）
  - **必返回 6 問答**：
    1. **4 玩家 NAND 市佔 2026 最新**（Q1 2026 Counterpoint Research）：
       - Samsung **29%**（#1）
       - SK Hynix + Solidigm **22%**（#2、合計）
       - Kioxia **14%**（#3）
       - Micron **13%**（#4 ties）
       - SanDisk **13%**（#4 ties、從 WDC 2025-02-24 spin-off 後獨立）
       - YMTC **13%**（中國本土）
       - → CR3 65%、6 家分食 vs HBM 3 家寡占 = NAND 估值結構性輸 HBM 一個量級
    2. **AI 用 NAND（Enterprise SSD） vs Consumer NAND 規格 / 利潤差**：
       - **介面**：Consumer PCIe Gen4 為主 / **Enterprise PCIe Gen5 量產 → Gen6 規劃 2027**
       - **容量單顆**：Consumer 256GB-2TB / **Enterprise 61TB → 245TB**（SK Hynix PS1012/PS1101）
       - **耐用度**：Consumer 0.3-1 DWPD / Enterprise 1-10 DWPD
       - **PLP（電源保護）**：Consumer 無 / Enterprise 必備
       - **散熱**：Consumer 被動 / Enterprise **液冷支援**（Solidigm liquid-cooled SSD）
       - **合約價（Q1 2026 TrendForce）**：Client SSD QoQ +40% / **Enterprise SSD QoQ +60%**
       - **wafer 經濟**：「同一片 wafer 切 enterprise = 切 consumer 的 **3-5 倍營收**」→ 廠商集體把 wafer 從 Client 切到 Enterprise
       - **市場結構**：Enterprise SSD 2026 起成為 NAND 最大 application segment（TrendForce 確認）
    3. **NAND 在 NVDA 路線圖每個產品的具體用量**：
       - **Vera Rubin AI 超級電腦（NVL72）**：**1,152TB SSD / rack**（ICMS = Inference Context Memory Storage）= NAND BOM **$1M+ / rack**（13% of $7.8M）= **唯一主戰場用量**
       - **Vera CPU**（standalone Arm 88 核）：OS + checkpoint storage（容量未揭露、推測 <100GB / chip）= **<5% BOM**（LPDDR5X 才是主軸）
       - **RTX Spark AI PC**（GB10 Superchip）：4-8TB local SSD 推估（NVIDIA 未明確）= **~10% BOM**（LPDDR5X 128GB 是主記憶體）
       - **Jetson Thor 機器人**：128GB-1TB SSD 推估 = **~10% BOM**（LPDDR5X 128GB 是主記憶體）
       - → **Vera Rubin ICMS 是唯一「主戰場」**、其他 3 個 NAND 是「BOM 配角但路線圖鎖死」
       - **2026 估計 30,000 units Vera Rubin → NAND 需求 34.6M TB = 全球 NAND 產能 2.8%**
       - **2027 估計 100,000 units → 115.2M TB = 全球 9.3%**（NAND 廠當前**沒 price in**）
    4. **NAND 是主戰場還是附屬 BOM？— Leo 判斷**：
       - **「半主戰場 + 半附屬 BOM」**——目前 60% 附屬 BOM、40% 主戰場
       - **2027 H2 HBF 落地 + Vera Rubin 100K units 出貨後**，會升到「60% 主戰場 + 40% BOM」
       - **但永遠不會像 HBM 那樣 100% 主戰場**——物理性質決定（可獨立採購 + 6 家分食 + QLC commodity 屬性）
       - **理由**：
         - HBM die-bonded lock-in、6 家分食 NAND 物理可獨立採購、估值結構差一級
         - HBM 寡占 3 家、NAND 6 家分食 = 議價力結構性弱
         - HBM 有 NVDA multi-year contract anchor、NAND 仍按 segment / 多源策略採購
         - **但 NAND 開始長出 HBM 形狀**：HBF 標準化（NAND-as-DRAM）+ Solidigm Enterprise 100% pivot + Kioxia FY2025 OP +95% = 結構性新需求軸成形
    5. **三家五軸評分（25 分制）**：
       - **[[Kioxia]] 19/25**（賽道 4 / 路線 4 / IP 4 / 客戶分散 4 / 時點 3）= 比 HBM BIG 3 略低一級、時點扣分（+2,400% 漲幅後 Bain 仍 30% 持股 overhang）
       - **[[Solidigm]] 17/25 假設**（賽道 4 / 路線 3 / IP 3 / 客戶分散 4 / 時點 3）= 私有公司不可直接押、必須透過 [[SK Hynix]] 母公司套利
       - **[[Western Digital]] 15/25**（賽道 3 / 路線 3 / IP 3 / 客戶分散 3 / 時點 3）= NAND 戰場 rival、非戰場玩家、賽道扣分；storage AI 主題對沖配置
       - 對照 HBM BIG 3：[[SK Hynix]] 23/25、[[Samsung Electronics]] 21/25、[[Micron]] 20/25 = NAND 戰場 entity 仍輸 HBM 戰場 entity 1-2 軸
    6. **PB 估值法仍適用 NAND 嗎？**：
       - **適用、但需要分段估值改良版**
       - **Consumer NAND**（手機 / PC）= **PB 框架完全適用**
       - **Mobile eMMC / UFS** = PB 框架
       - **Enterprise SSD（datacenter）**= **混合：PB 守底 + Forward PE 10-15x**
       - **AI Enterprise SSD（NVDA ICMS）**= **Forward PE 15-20x**（infra 級半套用、不到 HBM 廠 40-60x 水準）
       - **Thesis switching trigger**：Enterprise SSD 營收占比 > 50% + ASP QoQ > 40% → 切到 Forward PE 框架（Kioxia FY2025 已過、SanDisk FY2026 Q3 已過、Solidigm 透過母公司套利）
       - **退場時點**：Enterprise SSD ASP 連續兩季 QoQ 負成長 → 退回 PB 框架
       - **跟 HBM 差別**：HBM iPhone moment 是「全 segment re-rate」（傳統 DRAM 都被拉上）、3D NAND 是「分段 re-rate」（Enterprise SSD 拉、Consumer NAND 仍週期）
  - 累計：**48 concept + 59 entity + 41 summary**（[[AI infra 3D NAND 戰場]] concept +1、[[Kioxia]] / [[Solidigm]] / [[Western Digital]] entity +3）

## 2026-06-08（ingest #43）— AI infra 電力戰場（第八波 / codex P1-3 校準補位）

- **觸發**：Codex 對抗審核 **P1-3**「AI infra 戰場缺『電力 / 散熱』主戰場；賣水人頁已有電力鏈，[[MLCC 嵌入式基板賽道]]/[[信昌電]]頁也反覆提 1MW rack / 800V HVDC → 建議新增 Power + Thermal battlefield、不要只放在 MLCC 附屬敘事」校準。
  - 過去這層**附屬**在 [[賣水人選股邏輯（投資版）]] 的「電力供應鏈」子段（Vistra/Constellation/GE Vernova 三家點名但無 entity）+ [[信昌電]] entity 內 NVDA Rubin 1MW 機櫃曝險段 + [[資本重分配（從人力到算力）]] concept 內「電力供應鏈」段
  - 現獨立為**第八波（第六戰場）** = AI infra 戰場圖譜：①光通訊/DCI ②MLCC嵌入式 ③TGV玻璃基板 ④ABF載板 displacement ⑤InP上游 epi ⑥電力 ⑦3D NAND
- **新建檔案**（3 entity + 1 concept）：
  - `wiki/concepts/AI infra 電力戰場.md`（concept、繁中、source URL 完整、時效 metadata）
  - `wiki/entities/Constellation Energy.md`（entity、NASDAQ: CEG、Mega Cap、五軸 22/25）
  - `wiki/entities/Vistra.md`（entity、NYSE: VST、Mega Cap、五軸 23/25）
  - `wiki/entities/GE Vernova.md`（entity、NYSE: GEV、Mega Cap、五軸 22/25）
- **核心數字** anchor（codex P1-3 必須引用）：
  - **NVDA Rubin 1MW 機櫃 vs GB200 132kW = 5-8x 電力需求**（Schneider Electric 2025-10 + Introl 2026 + 信昌電法說 2026-05-21 三來源交叉驗證、TechPowerUp 揭露 Rubin 600-1,000kW 範圍）
  - **800V HVDC NVDA 31 家伙伴**（China Energy Storage 2025-11-25 揭露：ABB / Eaton / Schneider / Vertiv / Infineon / STM / Navitas 等）
  - 過去 12 個月美國 IPP 累計 hyperscaler PPA：CEG 5,650+ MW + VST 3,000+ MW + Talen 1,920 MW ≈ **>10 GW** 已鎖
  - 2026-2030 hyperscaler 新增電力需求估算 **+50-80 GW**（缺口比已鎖大 5-8x）= **真正的物理瓶頸**

### 三家具體 hyperscaler 合約（codex 校準必返回）

- **CEG**：
  - **[[Microsoft]] 20 年 PPA 835 MW**（Three Mile Island Unit 1 復役 = 重命名 Crane Clean Energy Center / CCEC、**首次美國商業退役核電復役**、2028 H1 上線提前一年）
  - **[[Meta]] 20 年 PPA 1,121 MW**（Clinton Power Station 現有核電廠延伸）
  - 其他累計 **>5,650 MW** hyperscaler PPA + PJM submit 5,000MW 新容量
  - **$16.4B 併購 Calpine（EV $26.6B、2026-01 完成）** + Trump 政府 **$1B 貸款支持 TMI 復役**
- **VST**：
  - **[[Meta]] 20 年 PPA ~2,600 MW**（跨 PJM 三廠核電、含 uprate、2026-01 簽）
  - **[[AMZN]] AWS 多年 PPA**（規模未公開）
  - 累計 **>3,000 MW** hyperscaler PPA
  - **Cogentrix $4-4.7B 收購**（5,496 MW 跨 PJM/ISO-NE/ERCOT 三 ISO、2026 mid-late 完成）
  - TXU Energy 德州零售 retail
- **GEV**：
  - **MSFT + AWS + Meta + Crusoe** variable agreements **至 2035**
  - Q1 2026 Electrification 段拿 **$2.4B data center 訂單**（>整個 2025 全年）
  - **Prolec GE $5.275B 全額收購**（2026-02 完成、北美變壓器 #1）+ Prolec backlog 收購宣布後 **+25% 至 $5B**
  - **Gas Power backlog 100 GW**（FY 2026 末 ≥110GW、其中 **20 GW 直接綁 data center 客戶**、production slot 排到 2030）
  - **EMS 軟體 Q1 + Q2 2026 首兩個 hyperscaler 訂單**

### NVDA Rubin 1MW 機櫃對電力 TAM 量化（vs GB200）

- GB200 132 kW → Rubin Ultra Kyber 600-1,000 kW = **純物理需求 5-8x**
- 全美 hyperscaler 估算 **50,000-80,000 個 1MW rack**（2026-2030）
- 對應變壓器需求 **60,000-120,000 MVA**（GEV Prolec 北美 #1 主受惠）
- CEG MSFT TMI 835 MW = **~835 個 1MW rack 純物理上限對照**（含 PUE 1.2-1.4 折扣後 ~500-600 個 servable）
- VST Meta 2,600 MW = **~2,600 個 1MW rack 純物理上限對照**
- 800V HVDC vs 54V rack：電壓提高 14.8x → 銅用量減少 45% + 端對端效率提升 5%

### 800V HVDC 趨勢具體標的（哪家最受惠？）

| 排名 | 玩家 | 戰場位置 | 為什麼最受惠 |
|---|---|---|---|
| **#1 (整合王)** | **GEV**（已 ingest） | 全棧 power-to-rack 整合 OEM | 從燃氣輪機 → 變壓器 → 開關 → 機架配電唯一一家 |
| #2 | Eaton（ETN，⚠️ 待 ingest） | 800V DC reference architecture | 2025-10 首發、NVDA 共同制定者 |
| #3 (高 alpha) | Navitas（NVTS，⚠️ 待 ingest） | GaN power IC pure-play | 10kW 98.5% 效率、800V HVDC 純度首選 |
| #4 | STM / TI / Infineon | 800V→12V/6V GaN power module | 半導體大廠多軌、NVDA 共同開發 |
| #5 | Schneider Electric / Vertiv | UPS + 機房配電整合 | NVDA 31 家伙伴之一、整合平台 |
| #6 | **[[信昌電]]**（已 ingest） | 機櫃內中高壓 MLCC（PSU + BBU） | NVDA Rubin 10K+ 顆 / 機櫃 |

### 三家五軸評分（25 分制、codex 校準必返回）

| 軸 | CEG | VST | GEV |
|---|---|---|---|
| 賽道純度 | 5 | 5 | 5 |
| 客戶分散 | 4 | **5** | **5** |
| IP / 護城河 | **5** | 4 | 4 |
| 時點對位 | 5 | 5 | 5 |
| 估值合理性 | 3 | **4** | 3 |
| **總分** | **22/25** | **23/25** | **22/25** |
| **戰場位置** | 第一層電力產生 #1 | 第一層電力產生 #2 | 第二層電力傳輸 #1 |
| **獨特優勢** | TMI 政治焦點 + 規模 | 客戶分散 + 跨三 ISO + PE 最便宜 | 唯一 power-to-rack 全棧 OEM |

→ **VST 五軸最高（客戶分散 + 估值最佳）、CEG/GEV 並列 22 分**

### 跟 [[宋分 #20 — 能源結構性剛需]] thesis 校準（codex 校準必返回）

**三標準全滿**：

| 條件 | 滿足 ✅/❌ | 證據 |
|---|---|---|
| **1. 長期供給結構改變** | ✅ **完全滿足** | TMI 首次美國商業退役核電復役、Calpine $16.4B 整合、Prolec $5.275B 整合、gas turbine slot 排到 2030、NVDA 800V HVDC 把 architecture 從 54V 重定義 |
| **2. 持續性 CapEx** | ✅ **完全滿足** | CEG 五年 >$30B + VST 五年 >$10B + GEV 五年 >$10B + 31 家 NVDA 800V HVDC 伙伴 R&D |
| **3. 可持續現金流** | ✅ **完全滿足** | 20 年 PPA + 17 年 PPA + GEV agreements 至 2035 鎖死、20-100GW backlog 平均能見度 10 年 |

→ **電力戰場是宋分 thesis 中最完整的結構性重估個案**（vs 油氣需戰爭 catalyst 不確定、太陽能仍補貼依賴）

### 電力戰場 anchor 玩家排名（codex 校準必返回）

- **#1 CEG**（電力產生 / 核電）= 規模 + TMI 政治焦點 + 政策紅利
- **#2 GEV**（電力傳輸 / 變壓器 + gas turbine + power-to-rack）= **唯一全棧 OEM**
- **#3 VST**（電力產生 / 核電 + 氣電 + retail）= 客戶分散 + 估值最佳 + 跨三 ISO
- #4 Talen Energy（TLN、核電 pure-play、AWS PPA、⚠️ 待 ingest）
- #5 Eaton（ETN、800V DC 首發、⚠️ 待 ingest）
- #6 ABB / Schneider / Vertiv / Navitas / STM / TI / Infineon（800V HVDC 配套，⚠️ 待 ingest）
- #7 [[信昌電]]（機櫃內 PSU MLCC、已 ingest）

### 跟既有 wiki 連結

- [[AI infra CapEx 三階段論]]：電力戰場是第三階段下半場 anchor、是「物理瓶頸」最強證據
- [[賣水人選股邏輯（投資版）]]：電力戰場 = 「賣水人之中的賣水人」最高純度版本（不押 AI 誰贏、所有 hyperscaler 都需要 24/7 carbon-free baseload）
- [[宋分備忘錄 #3 — AI 半導體受惠者擴散]]：電力戰場 = 「被遺忘 AI 受惠者」放大版（vs 宋分原文點名 TXN/ADI 類比 IC）
- [[宋分 #20 — 能源結構性剛需]]：三標準全滿、最完整結構性重估個案
- [[效率→安全切換]]：電力戰場 = AI 公司「要 24/7 不斷算力」的安全代價、不再追求 cheapest spot price
- [[信昌電]]：機櫃內 PSU MLCC（第三層）配套 CEG/VST 的電力供給（第一層）+ GEV 的變壓器（第二層）= **三戰場垂直 stack**
- [[控制點轉移（投資版）]]：NVDA 800V HVDC 把控制點從晶片推到電網、CEG/VST/GEV 在第一第二層拿控制點
- [[半導體基礎建設化]]：電力公司走同一路徑（從週期股 → 結構性成長股）
- [[CapEx 見頂辯論]]：電力公司是「CapEx 不會見頂」的物理證據（gas turbine slot 排到 2030+）

### 本次三家全使用標準格式

- [[公司 Entity 模板（Step 1-3 三段式）]]：一句話定位 + 三層 thesis（產業 / 目的 / 供應）+ 財務狀態快照
- foreign competitor 變體：Mega Cap + 美股 ticker 雙軌處理（NASDAQ: CEG / NYSE: VST / NYSE: GEV）
- 時效 metadata（as_of / check_after / expires_on / evidence_url）
- source URL 完整（每家 10-15 個來源）
- ⭐ 電力戰場位置（三層分工標籤）
- ⭐ NVDA Rubin 1MW 機櫃曝險量化（含警語）
- ⭐ 跟 hyperscaler 直接合約清單

### 更新檔案

- `wiki/index.md`：
  - 方法論段加「AI infra 電力戰場（第八波）」concept 段（在 3D NAND 段之後）
  - entity 段加「標的：AI infra 電力戰場 anchor triplet（第八波）」段（在 MLCC 段之後）
- `wiki/log.md`：本段

### 下一步 ingest 延伸

- Talen Energy（TLN）— 核電 pure-play、AWS $18B 17 年 1,920MW PPA、是「期權型 alpha」
- Eaton（ETN）— 800V DC reference architecture 首發、NVDA 共同制定者
- ABB / Schneider Electric / Vertiv / Navitas / Infineon / Hitachi Energy / Siemens Energy
- 姊妹題 [[AI infra 散熱戰場]] concept 獨立化（codex P1-3 同時點名 Power + Thermal）

累計：**49 concept + 62 entity + 41 summary**（[[AI infra 電力戰場]] concept +1、[[Constellation Energy]] / [[Vistra]] / [[GE Vernova]] entity +3）

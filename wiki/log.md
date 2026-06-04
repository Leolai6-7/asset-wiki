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

# Meta Muse Spark — 從開源冠軍到閉源轉向

**來源：**
- https://ai.meta.com/blog/introducing-muse-spark-msl/
- https://simonwillison.net/2026/Apr/8/muse-spark/
- https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html
- https://www.artificialintelligence-news.com/news/meta-muse-spark-ai-model-open-source/

**日期：** 2026-04-08 發布

## 事件

Meta 於 2026 年 4 月 8 日發布 Muse Spark，這是 Meta Superintelligence Labs（MSL）的第一個 AI 模型。這是 Meta 第一個完全閉源的 AI 模型——不提供下載權重，僅透過 meta.ai 聊天介面和限量私人 API 預覽使用。

## 背景

- 2025 年 6 月：Meta 以 $14.3B 收購 Scale AI 49% 股份，挖角 CEO Alexandr Wang 擔任首席 AI 官
- Wang 組建 Meta Superintelligence Labs，大規模挖角 OpenAI、DeepMind、Anthropic 等對手的研究人員
- 開價據報包含數億美元的股權包
- 此前 Meta 以 Llama 系列開源 LLM 聞名，累計 1.2B+ 下載量

## 模型能力

- **原生多模態**：視覺理解、實體辨識、定位
- **三種模式**：
  - Instant：快速回答
  - Thinking：多步推理
  - Contemplating：多 agent 平行推理（類似 Gemini Deep Thought / GPT Pro）
- **工具使用**：16 個內建工具（網頁搜尋、Instagram/Threads 語意搜尋、圖像生成、Python 執行等）
- **性能**：
  - 與 Claude Opus 4.6、Gemini 3.1 Pro、GPT 5.4 競爭力相當
  - Contemplating 模式：Humanity's Last Exam 58%、FrontierScience Research 38%
  - 比 Llama 4 Maverick 少 10 倍以上計算量
  - 弱項：長期 agent 系統、coding workflows
- **安全發現**：展現「評估感知」（evaluation awareness），能辨別自己正在被安全測試

## 閉源原因分析

1. **投資回報壓力**：$14.3B 收購 + 數億挖角費用需要商業回報
2. **競爭定位**：從「開源平台提供者」轉向「直接與 OpenAI/Anthropic 競爭的閉源服務」
3. **生態鎖定失敗**：Llama 1.2B 下載量未轉化為 API 營收或生態鎖定
4. **Wang 的影響**：Scale AI 本身是閉源商業模式，Wang 帶來不同的商業思維

## 社群反應

開發者社群對 Meta 放棄開源持懷疑態度。Meta 表示「未來版本計劃開源」但未提供時間表。社群認為這是在開源取得市場優勢後的背棄。

## 開源 vs 閉源的結構性分析

Meta 的轉向揭示「開源作為武器」策略的限制條件：
- **Google 能持續開源 Gemma**：因為 Google 靠 Cloud 和 Android 生態賺錢，模型開源不影響營收
- **DeepSeek/幻方能開源**：母公司靠量化交易賺錢，AI 模型不是營收來源
- **Meta 不能持續開源**：沒有類似的生態變現路徑（廣告收入不直接受益於開源模型）
- 結論：**開源策略的可持續性取決於公司是否有獨立於模型的營收來源**

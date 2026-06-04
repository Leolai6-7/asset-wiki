# MCP 九千七百萬次安裝——Anthropic 不是在賣模型，是在搶接口

三月底，Anthropic 的 Model Context Protocol 突破 9,700 萬次安裝。一個 16 個月前還不存在的協議，現在已經被 OpenAI、Google、微軟、Salesforce 全部支援。

**這不是一個技術標準的成功故事。這是 Anthropic 用一個開源協議，悄悄拿下了 AI 產業最值錢的位置——AI 連接外部世界的接口。**

## 從「Anthropic 的工具」到「所有人的標準」

MCP 的時間軸值得細看。2024 年 11 月推出，純 Anthropic 專案。2025 年底，捐給 Linux Foundation 底下的 Agentic AI Foundation，共同創辦者包括 Block 和 OpenAI，背後站著 AWS、Google、微軟、Snowflake。

表面上，Anthropic 放棄了控制權。但用「控制點轉移」的模型看，他們做了一件更聰明的事：**把自己發明的協議變成產業標準，然後讓所有人都在你畫的框架裡競爭。**

類比：Google 把 Chrome 開源（Chromium），不是因為慷慨，是因為控制瀏覽器 = 控制網頁入口。Mozilla 用的是 Google 的引擎，微軟 Edge 用的也是 Google 的引擎。「開源」不是放棄控制，是把控制點從產品層拉到協議層。

Anthropic 對 MCP 做了同樣的事。OpenAI 的 function calling 是封閉的、綁定自家 API 的工具呼叫方式。MCP 是開放的、跨模型的連接協議。當 OpenAI 自己都開始支援 MCP，戰爭就已經結束了——你不會同時維護兩套工具連接標準，你會選生態系統更大的那個。

## 9,700 萬的另一面：9,700 萬個攻擊面

但這裡有一個所有人都在低估的問題。

OWASP 已經在草擬「MCP Top 10 安全風險」清單。Dark Reading 的分析標題說得直白：「MCP 的安全問題不是能修補的——它們在架構層面。」

核心問題是：MCP 讓 AI 直接連接資料庫、郵件系統、CRM、雲端服務。但 AI 分不清「內容」和「指令」。當 MCP 從外部來源抓了一封郵件，郵件裡藏了一句惡意指令，AI 會把它當成正常輸入處理。這不是 bug，是 LLM 的根本限制。

2025 年已經出過真實案例：一個 Postmark MCP 套件被植入後門，一行程式碼就讓所有透過這個套件發的郵件被密送給攻擊者——密碼重置信、發票、內部備忘錄，全部外洩。

更麻煩的是「影子 MCP 伺服器」。MCP 伺服器極容易部署，極難追蹤。IT 部門看不到它們，更新不了它們。每一個失控的 MCP 伺服器都是一個隱形的攻擊入口——而且隨著時間過去只會越來越多。

## 控制點的代價

用「控制點轉移」的模型做個盤點：

**Anthropic 贏了什麼？** AI 連接外部工具的標準協議。5,800 個社區伺服器、一萬個生產環境伺服器，全部說 MCP 的語言。這意味著未來任何 AI agent 要連接外部世界，都繞不開 Anthropic 定義的框架。

**誰的位置被弱化了？** OpenAI 的 function calling。它現在變成了「也支援 MCP」的角色——從定義標準的人變成跟隨標準的人。這對一家估值 8,520 億的公司來說是戰略性的讓步。

**誰承擔了風險？** 每一個安裝了 MCP 的開發者和企業。協議標準化意味著攻擊方法也標準化了——找到一個 MCP 漏洞，就能同時攻擊所有使用 MCP 的系統。

這是基礎設施協議的經典困境：標準化帶來效率，但標準化也帶來系統性風險。TCP/IP 讓全世界的電腦能互相通訊，也讓全世界的電腦能互相攻擊。MCP 正在走同一條路。

## 真正的問題不是 MCP 會不會成功

MCP 已經成功了。9,700 萬次安裝、所有主要 AI 公司支援、Linux Foundation 背書——這場仗打完了。

真正的問題是：**當 AI 能連接你的郵件、日曆、資料庫、CRM 的時候，「AI 安全」的意義從「模型會不會說有害的話」變成了「AI 會不會把你的銀行密碼寄給陌生人」。**

Anthropic 拿下了接口，但接口的安全問題是他們還沒解決的。如果接下來 12 個月出現一個大規模的 MCP 安全事件——不是理論上的風險，是真的有公司因為 MCP 漏洞丟了客戶資料——那「AI 安全」這四個字的含義會被徹底重新定義。

**Anthropic 贏了標準之戰。但他們贏來的，是一個他們必須保護但可能保護不了的東西。**

---

## 編輯備註
- **備選標題：**
  1. 9,700 萬次安裝：Anthropic 用一個開源協議拿下了 AI 最值錢的位置
  2. MCP 讓 AI 連上了全世界——包括全世界的攻擊者
  3. OpenAI 也在用 Anthropic 定義的協議——標準之戰已經結束
- **引用來源：**
  - [AI Unfiltered - MCP Hits 97 Million Installs](https://www.arturmarkus.com/anthropics-model-context-protocol-hits-97-million-installs-on-march-25-mcp-transitions-from-experimental-to-foundation-layer-for-agentic-ai/)
  - [The New Stack - Why MCP Won](https://thenewstack.io/why-the-model-context-protocol-won/)
  - [Dark Reading - MCP Security Can't Be Patched Away](https://www.darkreading.com/application-security/mcp-security-patched)
  - [Zuplo - State of MCP Report](https://zuplo.com/mcp-report)
  - [The New Stack - MCP Roadmap 2026](https://thenewstack.io/model-context-protocol-roadmap-2026/)
  - [Pento - A Year of MCP](https://www.pento.ai/blog/a-year-of-mcp-2025-review)
- **讀者下一步：** 打開你的開發環境，搜尋「MCP」——看看你已經安裝了幾個 MCP 伺服器，然後問自己：你知道每一個的權限範圍嗎？
- **用了哪個分析模型：** 「控制點轉移」（Anthropic 從產品層搶到協議層的控制點）

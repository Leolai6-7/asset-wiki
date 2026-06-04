# Netflix 開源了第一個 AI 模型——但它不是在做慈善

Netflix 上週在 Hugging Face 上放出了 VOID——它的第一個開源 AI 模型。這個模型做一件事：從影片裡刪除物件，然後重新生成被刪除物件影響過的所有物理效果。

不只是把東西抹掉、補上背景。如果你從車禍畫面中移除一台車，VOID 會讓剩下的那台車繼續正常行駛，碎片和火焰消失，路面恢復完整。在 25 人的盲測中，VOID 以 64.8% 的偏好率擊敗了 Runway（18.4%）。

**一家串流公司做出了比專業影片編輯工具更好的 AI 模型。然後免費送出去。為什麼？**

## 表面是開源，賭注是後製產業的重新定義

用「表面 vs 賭注」的模型看。

**表面上，** Netflix 在做技術社群貢獻。Apache 2.0 授權，商用自由，任何人都可以用。看起來像 Google 開源 TensorFlow、Meta 開源 Llama 的劇本。

**實際上，** Netflix 在重新定義什麼叫「後製」。

傳統影視後製是勞力密集、成本高昂的環節。一個幾秒鐘的物件移除鏡頭，可能需要特效團隊花幾天手工處理。Runway 和 Adobe 已經在用 AI 簡化這個流程——但它們是賣工具的公司，每個功能都要收費。

Netflix 不賣工具。Netflix 是全世界最大的影片買家。它每年花幾百億美元製作和購買內容。如果後製成本降低 50%，受益最大的不是工具供應商，是 Netflix 自己。

**開源 VOID 的邏輯跟 Google 開源 Android 一樣：把別人的利潤中心變成免費的基礎設施，降低自己的成本結構。**

## 誰被取代了

畫一下錢的流向。

VOID 出現之前：Netflix 付錢給後製公司 → 後製公司用 Adobe/Runway 工具 → 工具公司收 SaaS 費用。三層都在賺錢。

VOID 出現之後：Netflix 免費提供工具 → 後製流程被壓縮 → 工具公司的這塊收入消失。

Runway 上個月才剛融了新一輪，估值繼續漲。但 Netflix 用一個開源模型證明了：在「影片物件移除」這個具體任務上，免費的 VOID 比 Runway 的付費工具更好。這不代表 Runway 馬上會倒——但它的護城河剛被一個不靠賣工具賺錢的公司挖了一鏟。

## 物理感知是技術取捨的結果

VOID 的技術亮點是「物理感知」——它不只刪除物件，還理解物件被刪除後其他東西應該怎麼動。這靠的是一個叫「四值遮罩」（quadmask）的設計：分別標記「要刪除的物件」、「重疊區域」、「受影響的物件」和「保留的背景」。

用技術取捨的模型看：VOID 選了「深度理解場景物理」，放棄了「通用生成能力」。它不能生成新內容、不能做風格轉換、不能加特效——它只做一件事，但做到最好。

這個選擇揭示了 Netflix 的優先順序：它不需要一個什麼都能做的 AI 影片工具，它需要一個能精確解決後製痛點的專門工具。這也是為什麼它敢開源——**一個專精的工具對競爭對手的威脅有限，但對整個產業的成本結構影響巨大。**

## 內容平台做 AI 工具的意義

Netflix 做 VOID 有一個更大的含義：**當內容平台開始自己做 AI 工具，工具公司的處境就會很尷尬。**

Adobe 和 Runway 的商業模式是「我賣工具，你做內容」。但 Netflix 說：「我自己做工具，而且免費給所有人用。」Netflix 不需要工具賺錢——它需要的是更便宜的內容生產。

如果 Disney、Amazon Prime、Apple TV 也開始做類似的事呢？每個內容平台都有動機開源 AI 後製工具，因為降低後製成本直接增加它們的利潤。而每多一個免費工具，付費工具公司的市場就小一塊。

**VOID 不是 Netflix 的產品。是 Netflix 投向後製工具市場的一顆手榴彈。**

---

## 編輯備註
- **備選標題：**
  1. Netflix VOID 擊敗 Runway——一家串流公司為什麼要做 AI 影片工具
  2. 免費的 AI 後製工具比付費的好：Netflix 正在改寫影視工具產業的規則
  3. Netflix 開源 AI 的邏輯跟 Google 開源 Android 一樣：把別人的利潤變成自己的基礎設施
- **引用來源：**
  - [MarkTechPost - Netflix VOID erases objects](https://www.marktechpost.com/2026/04/04/netflix-ai-team-just-open-sourced-void-an-ai-model-that-erases-objects-from-videos-physics-and-all/)
  - [The Decoder - VOID rewrites physics](https://the-decoder.com/netflix-open-sources-void-an-ai-framework-that-erases-video-objects-and-rewrites-the-physics-they-left-behind/)
  - [The Register - Netflix video AI](https://www.theregister.com/2026/04/03/netflix_video_ai/)
  - [gHacks - Netflix VOID for editing scenes](https://www.ghacks.net/2026/04/04/netflix-introduces-void-ai-model-for-editing-video-scenes-without-reshooting/)
  - [HuggingFace - netflix/void-model](https://huggingface.co/netflix/void-model)
- **讀者下一步：** 如果你做影片，去 Hugging Face 下載 VOID 試試。如果你投資影視工具公司（Runway、Pika），問自己一個問題：如果 Netflix、Disney、Amazon 都開始開源自己的 AI 後製工具，這些公司的護城河還在嗎？
- **用了哪個分析模型：** 「表面 vs 賭注」（表面是開源貢獻，賭注是降低自身內容成本）+「誰付錢」（Netflix 不靠工具賺錢，所以能免費送）

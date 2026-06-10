---
title: AI 資安攻防成本曲線
aliases: [AI 資安成本曲線, AI 資安攻防, AI Security Cost Curve]
type: concept
created: 2026-06-04
as_of: 2026-06-04
check_after: 2026-09-15
updated: 2026-06-04
sources:
  - raw/2026-04-06_Claude花4000美元找到22個Firefox漏洞——但這不是你該興奮的原因.md
  - raw/2026-04-09_資安產業結構-紅藍隊分離與商業模式.md
tags: [資安, AI, 攻防, 成本曲線, Claude, 漏洞, AI-SPM]
thesis_dependency: AI-capex
confidence: medium
---

# AI 資安攻防成本曲線

[[Anthropic]] Claude $4K 找 Firefox 22 個漏洞事件揭示：AI 把資安「攻擊發現」和「防守覆蓋」兩條成本曲線**同時往下打**，但**速率不對稱**。

## 一句話

> 防守先賺到窗口期，攻擊隨後跟上 → 資安總支出**不降反升**。

## 兩條曲線同時下降

```
傳統時代：
攻擊發現成本: $$$$$$ （需要頂尖白帽團隊）
防守覆蓋成本: $$$$$$ （高貴 SOC + 人力監控）
總支出:     ←─ 由「能不能負擔」決定，廣度有限

AI 時代：
攻擊發現成本: $    （Claude $4K = 22 個漏洞）
防守覆蓋成本: $$   （AI-SPM 自動化）
總支出:     ↑↑↑  （頻率 × 覆蓋率倍增）
```

## 為什麼總支出**反而上升**

- 攻擊頻率 **倍增 × 倍增**（小公司也能用 AI 發起攻擊）
- 防守覆蓋率 **倍增**（更多企業願意買 AI-SPM）
- 結果：資安總市場**結構性 ↑**

## AI 攻防不對稱窗口

→ [[AI 攻防不對稱窗口]]（待 ingest）

防守暫時領先：
- AI 發現漏洞 >> AI 利用漏洞（exploit 難度高）
- Claude 找 22 個 Firefox 漏洞，**但真實 exploit 數量遠少**
- 軍備競賽會收斂，但**目前防守端先賺**

## 商業模式轉換

→ 連 [[紅藍隊分離]]、[[AppSec 平台訂閱化]]

### 紅藍隊分離
- **紅隊**（攻擊性測試）：傳統高貴顧問業 → AI 自動化（成本崩塌）
- **藍隊**（防守）：傳統 SIEM/SOC → **agentic SOC** + **AI-SPM**

### 商業模式從「奢侈品」變「剛需」
| 從 | 到 |
|---|---|
| 有預算才做的奢侈品 | **不做就是失職**的剛需 |
| 一次性審計（六位數） | ARR 訂閱（四位數但覆蓋更廣） |
| 純白帽人力 | AI + 人力 hybrid |

## 投資受惠/受害

### 受惠（賣水人邏輯）
- **CrowdStrike (CRWD)**：XDR + agentic SOC 龍頭
- **Palo Alto (PANW)**：Prisma Cloud + AI Access Security 平台
- **Cloudflare (NET)**：AI Gateway 新 SKU
- **Zscaler (ZS)**：SSE 邊界防護
- **Wiz**：雲端 CSPM（被 Google $32B 收購中）
- **Snyk / Semgrep**：AppSec / SAST AI 化先驅
- **Okta / CyberArk**：身分是新邊界

### 受害
- 傳統白帽顧問（FY、Mandiant 模式）
- 純人力 SOC

### 中性受惠 model layer
- [[Anthropic]]：Firefox 案例把「安全」變企業溢價賣點 → **model layer 守毛利的 playbook**

## 跟其他 wiki 概念連結

- [[賣水人選股邏輯（投資版）]]：資安賽道是 AI 中性受惠
- [[效率→安全切換]]：宋分備忘錄 #6 的「成本不會回到以前」在資安的具體實現
- [[Anthropic]]：Firefox 案例是 model layer 守毛利的範例
- [[接口控制權]]：MCP 大規模安全事件會重定義整個賽道
- 連 llm-wiki [[AI 資安研究]]

## 待 ingest 賽道 entity

- CrowdStrike、Palo Alto、Cloudflare、Zscaler、Wiz、Snyk、Semgrep、Okta、CyberArk
- 這些是 [[賣水人選股邏輯（投資版）]] 在 AI 資安賽道的具體標的

## 相關連結

- [[Anthropic]]
- [[紅藍隊分離]]
- [[賣水人選股邏輯（投資版）]]
- [[效率→安全切換]]
- [[接口控制權]]
- [[MCP（Model Context Protocol）]]

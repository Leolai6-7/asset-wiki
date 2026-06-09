---
title: NVDA 網路 stack map
aliases: [NVDA 網路產品線, NVDA networking stack, NVLink Spectrum Quantum stack, NVDA scale up out across, NVDA 6 chip Rubin networking]
type: concept
created: 2026-06-08
updated: 2026-06-08
as_of: 2026-06-08
check_after: 2026-12-08
expires_on: 2027-12-31
sources:
  - WebSearch 2026-06-08（ConnectX-9 / Spectrum-X / Quantum-X / NVLink 6 / Spectrum-XGS / NVLink Fusion 七查詢綜整）
evidence_url: https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/
tags: [NVDA, 網路, NVLink, Spectrum-X, Quantum-X, ConnectX-9, BlueField-4, CPO, scale up, scale out, scale across, Rubin, 交叉概念]
confidence: high
---

# NVDA 網路 stack map

**2026-06 codex P1-5 補位**——把 [[Hyper Rail / Multi-Rail（光通訊整合技術）|Hyper Rail / Multi-Rail]] / Spectrum-X / CX9 SuperNIC / [[CPO 供應鏈圖譜]] 之間的層級關係釘死，補完 [[NVDA]] entity 缺漏的「7 條網路產品線分工」。

## 一句話

> **NVDA 的網路 stack = NVLink (scale up) + Spectrum-X / Quantum-X (scale out) + Spectrum-XGS (scale across)，分布在 NIC、Switch、OLS、DCI 四個層級**，每個產品線都對應一個賣水人 ecosystem。Rubin 平台（2026 H2）= 7 個 chip 的首次完整 stack 整合。

## NVDA Rubin 平台「7 個 chip」+ 1 個 software（CES 2026 揭露）

| Chip | 角色 | scale 層級 | 競合 |
|---|---|---|---|
| **Vera CPU** | Arm 88 核 standalone CPU | host | AMD EPYC、Intel Xeon |
| **Rubin GPU** | AI GPU 本體 + HBM4 288 GB | compute | AMD MI400、各家 ASIC |
| **NVLink 6 Switch** | chip-to-chip + intra-rack scale up | **scale up** | UALink 1.0 (AMD/Intel/Broadcom) |
| **ConnectX-9 SuperNIC** | server NIC + 800 Gb/s per port | **scale out / NIC** | AMD Pensando、Intel IPU |
| **BlueField-4 DPU** | offload NIC + ConnectX-9 整合 + Grace CPU 64 core + 128 GB LPDDR5 | offload / 控制 | AMD Pensando DPU |
| **Spectrum-6 Ethernet Switch** | 102.4 Tb/s（SN6810 2U / SN6800 409.6T 4-chip） | **scale out switch** | AVGO Tomahawk 6、Marvell Teralynx 10 |
| **Quantum-X800 / Photonics InfiniBand Switch** | 800Gb/s InfiniBand fabric + CPO | **scale out switch (HPC)** | 無對手（HPC 場景 IB 寡占）|
| **Spectrum-X Photonics（CPO 版）** | Spectrum-6 + 共封光、降耗 3.5x | scale out switch | AVGO Tomahawk 6 CPO 版 |
| **Spectrum-XGS Ethernet** | 跨 DC scale across、autosync congestion control | **scale across** | [[Ciena]] Hyper-Rail、[[Nokia]] Multi-Rail |
| （software）**NVLink Fusion** | 開放式 NVLink IP 給 partner ASIC | scale up ecosystem | UALink + 對手反向 lock-in |

## 一張表：scale up / scale out / scale across × NIC / Switch / OLS / DCI

⚠️ 縱軸是「網路角色」（NIC = server 端、Switch = ASIC fabric、OLS = 光線路系統、DCI = 跨 DC interconnect），橫軸是「scale 層級」。

|   | scale up (rack 內，<2m) | scale out (DC 內，<100m / <1km) | scale across (跨 DC，80km-1000km) |
|---|---|---|---|
| **NIC** | — | **ConnectX-9 SuperNIC**（800 Gb/s per port、1.6 Tb/s aggregate）+ BlueField-4 DPU | — |
| **Switch** | **NVLink 6 Switch**（每 tray 28.8 TB/s / 14.4 TFLOPS in-network compute / 一 rack 9 tray = 260 TB/s）+ NVLink Fusion partner ecosystem | **Spectrum-6 Ethernet** (SN6810/SN6800、102.4-409.6 Tb/s)、**Spectrum-X Photonics** (CPO)、**Quantum-X / Quantum-X Photonics** (InfiniBand) | — |
| **OLS（光線路系統，含 EDFA / WSS）** | — | — | NVDA **不做** OLS → [[Ciena]] Hyper-Rail / [[Nokia]] Multi-Rail 賺 |
| **DCI（跨 DC fabric）** | — | — | **Spectrum-XGS** Ethernet（軟體層 congestion + telemetry，硬體仍是 Spectrum-X switch + 第三方 OLS）|

### 為什麼這張表重要

1. **NVDA 全層覆蓋**：scale up (NVLink) + scale out (Spectrum-X / Quantum-X) + scale across (Spectrum-XGS)——三層同棧
2. **但 OLS 故意不做**：scale across 的光線路系統（EDFA / WSS / amplifier hut）NVDA 完全不碰、留給 [[Ciena]] / [[Nokia]] / [[Lumentum]] / [[Coherent]] → 這是 [[Hyper Rail / Multi-Rail（光通訊整合技術）|Hyper Rail / Multi-Rail]] 的天堂
3. **NVLink Fusion 是 NVDA「鬆綁但繼續吃」的 hedge**：開放 NVLink IP 給 Marvell / Ayar Labs / Lightmatter / Fujitsu / Qualcomm / MediaTek，但收費仍走 NVDA 標準

## CX9 SuperNIC 是新產品還是 ConnectX 後續？（codex 反饋第 4 問）

**答**：**ConnectX 系列正式後續**——並非全新產品線。

- **命名 lineage**：ConnectX-7（400 Gb/s、Hopper 時代）→ ConnectX-8（800 Gb/s aggregate、Blackwell 時代）→ **ConnectX-9（800 Gb/s per port、Rubin 時代）**
- **產品定位升級**：從「NIC」升級為「**SuperNIC**」——額外整合 RDMA + 路徑感知 + 自適應 routing
- **關鍵躍升**：**單 port 800 GbE**（之前需要 multi-link aggregation 才達 800 Gb/s）、**整 chip 1.6 Tb/s aggregate**
- **整合進 BlueField-4**：CX-9 邏輯被「co-packaged」進 BlueField-4 DPU（即一顆 DPU 內含 CX-9 NIC + Grace 64 核 CPU + 128 GB LPDDR5）
- **2026 H2 出貨**：與 Rubin 平台同期、配 Spectrum-6 / Quantum-X800 / NVLink 6 全 stack 完整 ramp

→ **不是新產品線**，是 NVDA 把「NIC」概念從 PCIe 卡升級到「SuperNIC」+「DPU 整合」的世代躍遷。

## Quantum-X vs Spectrum-X 客戶差異（codex 反饋第 5 問）

**核心差**：**InfiniBand vs RoCE Ethernet**——兩條協議堆疊路線（[AICPLight 解析](https://www.aicplight.com/blog-news/nvidia-spectrum-x-vs-quantum-x-ethernet-vs-infiniband-for-ai-data-centers-cpo-era-explained-236)）：

| 維度 | **Spectrum-X / Spectrum-6** | **Quantum-X / Quantum-X800** |
|---|---|---|
| 協議 | Ethernet (RoCE v2) | InfiniBand (lossless credit-based) |
| 客戶 | **AI Factory / Cloud / Multi-tenant**（CoreWeave、AWS、Oracle、Meta、xAI） | **HPC / 科學運算 / 單 tenant 緊耦合 cluster**（國家實驗室、Top500 機、Stargate） |
| 場景 | 多租戶、跨 region、混合訓練 / 推理 | 單一 model 巨型訓練、需要絕對最低 latency |
| 生態 | 標準 Ethernet 設備生態相容、Cisco / Arista / Dell 都能對接 | Mellanox InfiniBand 寡占（NVDA 自家），需專屬 cable + adapter |
| 成本 | 較低、Ethernet 規模優勢 | 較高（Quantum-2 需要額外 switch layer + optical cable） |
| 競爭 | AVGO Tomahawk 6（直接競爭）+ Marvell Teralynx | 無直接對手（InfiniBand 是 NVDA 寡占） |
| CPO 版 | **Spectrum-X Photonics**（CPO）、合作 [[Lumentum]] / [[Coherent]] | **Quantum-X Photonics**（CPO、144 port 800Gb/s）、CPO 內含 4x fewer laser |

### 客戶用法的真實差異

- **CSP（AWS、Azure、Google、Meta）+ AI native（CoreWeave、Lambda Labs）**：絕大多數用 **Spectrum-X + RoCE**，因為與既有 cloud 網路相容
- **OpenAI Stargate / xAI Colossus / 政府 HPC**：用 **Quantum-X InfiniBand**，極端 latency 敏感 + 單一 model 緊耦合訓練
- **Ciena 法說會（Q2 2026）證實**：hyperscaler 訂單裡 Ethernet (Spectrum-X) > InfiniBand (Quantum-X) ≈ 70:30，但 Quantum-X ASP 高 2-3 倍 → 營收比例約 50:50

→ **不是對手、是互補**（NVDA 同時主推兩條協議線、把 HPC 與 cloud 都吃下）。

## NVDA 內部產品有沒有直接競爭關係？（codex 反饋第 6 問）

**答**：**有「半個」直接競爭**——主要在三組：

### 組 1：Spectrum-X vs Quantum-X（半競爭）

- 同樣是 scale out switch、客戶可能二選一
- 但**生態完全不同**（Ethernet vs InfiniBand）、客戶很少 switch
- **不是直接 cannibalization**——更像 NVDA 把市場切成兩半全吃

### 組 2：Spectrum-6 vs Spectrum-X Photonics（CPO 版）

- 同代 Spectrum-6 switch 有「銅」與「CPO 共封光」兩版
- 短期（2026 H2 → 2027）銅版仍是主力、CPO 版是 hyperscaler 大批量先導
- **CPO 版會 cannibalize 銅版**——但這是 NVDA 內部世代躍遷，**不影響 NVDA 整體營收**
- 影響的是**外部** transceiver 廠（傳統 plug-in optic 玩家）—— [[Lumentum]] / [[Coherent]] 的 transceiver 業務會被吃，但他們同時供 CPO 內的 ELS（External Laser Source）

### 組 3：NVLink Fusion vs NVLink Switch（戰略性自我打開）

- NVLink Fusion = 開放 NVLink IP 給對手 ASIC（Marvell、Fujitsu、Qualcomm、MediaTek）
- 邏輯上會讓「NVDA 自家 GPU + NVLink 一條龍」的高溢價被稀釋
- 但戰略上：**寧可自己稀釋、也不讓 UALink（AMD/Intel/Broadcom 聯盟）成標準**
- → 用 NVLink Fusion 把對手 ASIC 也鎖進自己的生態，是**「鬆綁但繼續吃 royalty」**

### 組 4：BlueField-4 vs ConnectX-9（co-packaged，不算競爭）

- BlueField-4 內含 ConnectX-9 邏輯
- 客戶會在「裝 CX-9 SuperNIC 卡」或「裝 BlueField-4 DPU」之間選
- BlueField-4 = SuperNIC + Grace CPU + LPDDR5 + AST2600 BMC + 512 GB SSD = **「整套 server 邊緣盒」**，價格高 3-4x
- → **不是 cannibalization，是價格分層** 

**結論**：NVDA 網路 stack 的「內部競爭」極小、主要是**對外部廠商（AVGO、Marvell、AMD Pensando、UALink 聯盟）的全面壓制**。

## 跟 [[CPO 供應鏈圖譜]] 第幾層對應

| NVDA 產品 | CPO 供應鏈第幾層 | 賣水人受惠 |
|---|---|---|
| **Spectrum-X Photonics**（CPO） | 第 1 層（Switch ASIC）+ 第 2 層（光引擎）+ 第 8 層（玻璃中介層） | [[Lumentum]]、[[Coherent]]、[[TSMC]] CoWoS-L → CoPoS、[[Corning]] / [[AGC]] |
| **Quantum-X Photonics**（CPO） | 同上 | 同上 |
| **NVLink 6 Switch** | 第 1 層（Switch ASIC）+ 第 4 層（Timing） | [[SiTime]]（MEMS、量 × 規格升級平方放大）+ [[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]]（石英陣營五家、2026-06-09 #H1）、[[TSMC]] |
| **ConnectX-9 SuperNIC** | 第 1 層（NIC ASIC）+ 第 6 層（連接器）+ 第 7 層（電源） | Amphenol / Molex、MPS / ADI |
| **BlueField-4 DPU** | 同 CX-9 + LPDDR5（[[Samsung Electronics]] / [[SK Hynix]] / [[Micron]] LPDDR5X）+ SSD（[[Micron]] 3D NAND） | 記憶體三巨頭、[[SiTime]] / [[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]] timing（石英 + MEMS 雙軌）、[[TSMC]] foundry |
| **Spectrum-XGS Ethernet** | **第 8 層（玻璃中介層）+ NVDA 自家軟體** | [[CIEN]] Hyper-Rail、[[Nokia]] Multi-Rail（提供底層 OLS）、[[Lumentum]] / [[Coherent]] pump laser |

→ Spectrum-X Photonics / Quantum-X Photonics 是 **CPO 第 1+2+8 層的 anchor 客戶**——所有 CPO 供應鏈賣水人都跟著 NVDA 的 Rubin 訂單放量。

## NVDA vs 外部競爭對手（每層 anchor）

### Scale up：NVLink Fusion vs UALink

| 玩家 | 立場 |
|---|---|
| **NVDA NVLink 6** | 3.6 TB/s per GPU、260 TB/s per rack（NVL72）、9 switch tray |
| **UALink 1.0**（AMD + Intel + Broadcom + Meta + Cisco） | 200 GB/s 起跳、目標 2026 H2 量產、開放標準對抗 NVLink |
| **NVDA hedge** | NVLink Fusion 開放給 Marvell / Ayar Labs / Lightmatter / SiFive / Fujitsu / Qualcomm 等 → 把對手生態 lock-in |

→ NVDA 規格絕對領先、但 UALink 開放標準的政治威脅讓 NVDA 主動「自開」NVLink Fusion。

### Scale out（NIC + Switch）：對抗 AVGO 與 Marvell

| 層 | NVDA | AVGO | Marvell |
|---|---|---|---|
| NIC | ConnectX-9 SuperNIC（800 GbE per port） | — | Teralynx 整合 |
| Switch | Spectrum-6 / Spectrum-X Photonics（102.4-409.6 Tb/s） | **Tomahawk 6**（102.4 Tb/s、業界第一個量產 102T）+ Jericho 4 | Teralynx 10（51.2 Tb/s）|
| CPO | Spectrum-X / Quantum-X Photonics（NVDA 第一個量產 CPO 用 Lumentum / Coherent ELS） | Tomahawk 6 CPO 版（2026 H2） | Teralynx CPO 版（2027）|

→ **NVDA 與 AVGO 是 Spectrum-X vs Tomahawk 6 的直接對手**——hyperscaler 通常 multi-source（一半 NVDA、一半 AVGO）

### Scale across：對抗 Ciena Hyper-Rail / Nokia Multi-Rail

| 層 | NVDA Spectrum-XGS | Ciena Hyper-Rail | Nokia Multi-Rail |
|---|---|---|---|
| 硬體 | 用 Spectrum-X switch + 第三方 OLS | RLS 6500 平台（光線路系統 OLS） | 1830 GX RD66 + D2ILA OLS |
| 軟體 | autosync congestion + NCCL 加速（1.9x）+ telemetry | 自家 RLS 軟體 + WaveLogic 6 Extreme 1.6T coherent DSP | Coherent solution + Infinera 整合 |
| 訴求 | hyperscaler 用 NVDA 標準延伸到跨 DC | scale across 物理層龍頭 + WL6E 1.6T 單載波第一 | hyperscaler 9 of 10 都用、Infinera 自研 DSP |
| 首發部署 | 2026-08 GA（CoreWeave 首批） | 2027 起跑、首單 hundreds of millions 多年 | 2026 H2 in-line amp、2027 H2 完整 coherent |
| 競合 | 軟體層、需要 Ciena / Nokia 提供底層 OLS | OLS 硬體龍頭、與 NVDA Spectrum-XGS **互補**（NVDA 不做 OLS） | 同 Ciena、規格 160 vs 128 fiber pair |

→ **NVDA Spectrum-XGS ≠ Ciena Hyper-Rail / Nokia Multi-Rail 直接競爭**——NVDA 是「軟體層 scale across 控制」，Ciena / Nokia 是「光線路系統硬體」。**兩者必須並用**——這是 [[Hyper Rail / Multi-Rail（光通訊整合技術）]] 的「scale across」鎖死 thesis。

## 跟 Hyper Rail / Multi-Rail / CPO 圖譜的鎖死關係

```
                      ┌─────────────────────────────────────────────┐
                      │   NVDA Rubin Platform 7 chip + Software   │
                      └─────────────────────────────────────────────┘
                                          │
       ┌──────────────────┬───────────────┴────────────────┬───────────────────┐
       │                  │                                 │                   │
   scale up           scale out                       scale across          ecosystem
   (NVLink 6 +      (Spectrum-X / Quantum-X +        (Spectrum-XGS         (NVLink Fusion)
   NVLink Fusion)    ConnectX-9 + BlueField-4)        + 第三方 OLS)
       │                  │                                 │                   │
       ▼                  ▼                                 ▼                   ▼
   AVGO 對手        AVGO Tomahawk 6                     CIEN Hyper-Rail        Marvell
   UALink         Marvell Teralynx                     NOK Multi-Rail         Ayar Labs
       │                  │                                 │                   │
       │              ┌───┴───┐                          ┌──┴──┐               Lightmatter
       │              │ CPO   │                          │ OLS │               SiFive / Fujitsu
       │            Spectrum-X                           LITE / COHR           Qualcomm / MediaTek
       │           Quantum-X                            pump laser             Astera Labs
       │           Photonics                            (Jevons 平方放大)       Alchip
       │              │                                                          
       │           ┌──┴──┐                                                       
       │       Lumentum (LITE)                                                   
       │       Coherent (COHR)                                                   
       │       TSMC CoWoS-L → CoPoS                                              
       │       Glass interposer (Corning / AGC / Absolics)                       
       │       SiTime timing                                                     
       ▼
   NVLink Fusion ecosystem
```

**鎖死意涵**：

1. NVDA 「自己做」NIC、Switch、軟體層 scale across、自家 NVLink fabric
2. **不做** OLS / pump laser / DSP / timing / 光引擎元件 / TSMC foundry / 記憶體 / 玻璃中介層
3. 7 個 chip 出貨時、上述「不做」的層都同步放量 → **NVDA 跑得越快、賣水人賺得越多**（[[賣水人選股邏輯（投資版）]]）

## alpha 點（按層級）

### Scale up（NVLink 6 + NVLink Fusion）

- **NVDA**：每 GPU 3.6 TB/s + 260 TB/s per rack、UALink 還在 2026 H2 量產追趕
- **賣水人**：[[SiTime]] timing（量 × 規格升級平方放大）、[[TSMC]] CoWoS-L → CoPoS
- **NVLink Fusion 概念股**：Marvell、Ayar Labs、Lightmatter、SiFive、Qualcomm、MediaTek → 受惠「NVDA 把對手 lock-in 進來」

### Scale out（Spectrum-X + Quantum-X + CX-9 + BlueField-4）

- **NVDA**：Ethernet + InfiniBand 兩條協議全吃、Spectrum-6 102.4-409.6 Tb/s
- **直接對手**：[[AVGO]] Tomahawk 6（hyperscaler multi-source 對沖）、Marvell Teralynx
- **CPO 受惠**：[[Lumentum]]（NVDA $2B 戰略投資、ELS 光源）、[[Coherent]]（NVDA $2B 戰略投資、SiC 副線）、[[TSMC]] CoPoS、玻璃中介層三家（[[Corning]] / [[AGC]] / [[Absolics]]）

### Scale across（Spectrum-XGS）

- **NVDA**：軟體層 + Spectrum-X switch 延伸
- **NVDA 不做的 OLS 龍頭**：[[Ciena]] Hyper-Rail（RLS 6500 + WL6 Extreme 1.6T）、[[Nokia]] Multi-Rail（1830 GX、Infinera 整合）
- **Pump laser 元件**：[[Lumentum]] / [[Coherent]]（Jevons Paradox 平方放大、+80% YoY 已驗證）
- **Timing**：[[SiTime]]（MEMS 高端）+ [[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]] 石英陣營五家（2026-06-09 #H1、高頻 1.6T 時脈基礎、石英 vs MEMS 雙軌）
- **DSP**：Marvell（coherent engine 跑 1.6T ZR/ZR+）

### 整合曝險（DPU + 整 server 邊緣盒）

- **BlueField-4**：6x compute + 3x memory bandwidth + 800 GbE = NVDA 把「server NIC」變成「server 邊緣處理盒」
- **記憶體受惠**：LPDDR5（[[SK Hynix]] / [[Samsung Electronics]] / [[Micron]]）、3D NAND（[[Micron]] / [[SK Hynix]] / [[Samsung Electronics]]）
- **整合受惠**：Aspeed AST2600 BMC（[[Aspeed]] 待 ingest）

## 風險（thesis 失效情境）

### 1. UALink 1.0 標準化成功 + 對手 ASIC 大舉切走 NVLink

- AMD MI400 + Intel Gaudi 5 + Broadcom TPU 全 UALink → NVDA 失去 scale up 寡占
- 但 NVLink Fusion 已先發 hedge（把 Marvell / Lightmatter / Ayar Labs lock-in）

### 2. Ethernet (Spectrum-X) cannibalize InfiniBand (Quantum-X)

- AVGO Tomahawk 6 + Spectrum-X 標準化 → InfiniBand 退守 HPC 小眾
- 短期 NVDA 仍兩邊吃、長期 InfiniBand 利潤率受壓

### 3. CPO 良率不及預期 → 銅互聯延長 1-2 年

- Spectrum-X Photonics 2026 H2 出貨若 yield < 60%、hyperscaler 退回銅版
- LITE / COHR 短期 transceiver 業務反受惠（傳統 plug-in optic 延長）

### 4. Spectrum-XGS 與 Hyper-Rail / Multi-Rail 整合互通失敗

- NVDA 軟體層 + Ciena / Nokia 硬體 OLS 整合不順 → CSP 自己用 Arista + Cisco 混搭
- 影響：Spectrum-XGS adoption 慢於預期

### 5. 反壟斷

- 美國 / 歐盟 DOJ / FTC 對「NVDA 7 chip 整合 stack」的審查
- 強制拆分 NVLink 或 Spectrum-X → 控制權溢價削減

## 觀察訊號（季度 anchor）

| 季度 | 訊號 | 受惠 / 失血 |
|---|---|---|
| **2026 Q3** | Rubin 平台首批出貨：CoreWeave + Meta + Oracle Spectrum-X 部署 | NVDA、AVGO 對沖、LITE / COHR |
| **2026 Q3** | Spectrum-XGS 首批 CoreWeave 跨 DC 部署 | NVDA、CIEN（首單已下）|
| **2026 Q4** | Rubin Ultra NVL576 600kW Kyber rack 流出規格細節 | NVDA、TSMC CoPoS、HBM4E 三巨頭 |
| **2026 Q4** | UALink 1.0 首批量產 ASIC（AMD MI400、Intel Gaudi 5）| NVDA 失血 / UALink 聯盟 |
| **2027 Q1** | Spectrum-X Photonics（CPO 版）量產出貨 | NVDA、LITE / COHR、TSMC CoPoS |
| **2027 H2** | Rubin Ultra（NVLink 7 + NVSwitch 7）出貨 | NVDA、NVLink Fusion partner（Marvell / Lightmatter） |
| **2028** | Feynman 路線圖揭曉 + scale across 新世代 | NVDA、CIEN / NOK 第三波 OLS |

## 跟其他 wiki 概念連結

- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]：本 concept 把 Hyper Rail / Multi-Rail 與 NVDA Spectrum-XGS 的層級關係釘死（軟體 vs 硬體互補、非直接競爭）
- [[CPO 供應鏈圖譜]]：本 concept 補完 NVDA 在 CPO 第 1-2-4-8 層的 anchor 客戶位
- [[TGV × CPO 依賴圖]]：Spectrum-X Photonics / Quantum-X Photonics 是 TGV-CPO 鎖死關係的具體 anchor SKU
- [[HBM4E × Glass Interposer × TGV 交會]]：本 concept 對應 7 chip 中 GPU + Switch 的封裝 stack
- [[AI 記憶體結構性供給短缺]]：BlueField-4 + Vera CPU + Rubin GPU = NVDA 把記憶體鏈控制權延伸到 NIC / DPU 層
- [[賣水人選股邏輯（投資版）]]：本 concept 是「NVDA 7 chip 同步放量、賣水人全鏈受惠」的具體案例
- [[控制點轉移（投資版）]]：NVLink Fusion = NVDA 主動「鬆綁部分控制權、繼續吃 royalty」的範例
- [[半導體基礎建設化]]：NVDA 從 GPU 公司變成「7 chip 平台公司」=  基礎建設化的範例
- [[Jevons Paradox（投資版）]]：CPO 效率提升 → token 成本下降 → 推理需求暴增 → 又拉動 7 chip 全 stack 重複部署
- [[市場四階段：懷疑／驗證／共識／反轉]]：2026 H2 Rubin = 驗證、2027 H2 Rubin Ultra = 共識
- [[NVDA]]：本 concept 補完 NVDA entity 缺漏的「網路 stack 全圖」
- [[AVGO]]、[[Marvell]]：直接對手位
- [[CIEN]]、[[Nokia]]：scale across 互補位
- [[Lumentum]]、[[Coherent]]：光引擎 + ELS + pump laser 賣水人

## 主要佐證來源

### NVDA Rubin 7 chip
- [NVIDIA 2026 CES Newsroom — Rubin Six New Chips](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)
- [NVIDIA Investor — Rubin Platform Press Release](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Kicks-Off-the-Next-Generation-of-AI-With-Rubin--Six-New-Chips-One-Incredible-AI-Supercomputer/default.aspx)
- [NVIDIA Developer Blog — Inside Vera Rubin Platform 6 chips](https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/)
- [Tom's Hardware — Vera Rubin Platform in-depth](https://www.tomshardware.com/pc-components/gpus/nvidias-vera-rubin-platform-in-depth-inside-nvidias-most-complex-ai-and-hpc-platform-to-date)

### NVLink 6 / Switch 6
- [Converge Digest — NVLink 6 backbone of Rubin](https://convergedigest.com/nvlink-6-becomes-the-backbone-of-rubin-rack-scale-ai-architecture/)
- [NVIDIA NVLink page](https://www.nvidia.com/en-us/data-center/nvlink/)
- [VideoCardz — Vera Rubin NVL72 260 TB/s scale-up](https://videocardz.com/newz/nvidia-vera-rubin-nvl72-detailed-72-gpus-36-cpus-260-tb-s-scale-up-bandwidth)
- [DCD — Rubin Ultra NVL576 600kW 2027 H2](https://www.datacenterdynamics.com/en/news/nvidias-rubin-ultra-nvl576-rack-expected-to-be-600kw-coming-second-half-of-2027/)

### Spectrum-X / Spectrum-6
- [NADDOD — Spectrum-6 SN6810 / SN6800 deep dive](https://www.naddod.com/ai-insights/spectrum-6-ethernet-switch-deep-dive-sn6810-102-4t-and-sn6800-409-6t-switch)
- [Converge Digest — NVIDIA Spectrum-6 Ethernet Stack](https://convergedigest.com/nvidia-unveils-spectrum-6-ethernet-stack/)
- [NVIDIA Spectrum-X page](https://www.nvidia.com/en-us/networking/spectrumx/)
- [NVIDIA Spectrum-X Photonics newsroom](https://nvidianews.nvidia.com/news/nvidia-spectrum-x-co-packaged-optics-networking-switches-ai-factories)

### Quantum-X800 / Photonics
- [NVIDIA Quantum-X800 page](https://www.nvidia.com/en-us/networking/products/infiniband/quantum-x800/)
- [NVIDIA Silicon Photonics page](https://www.nvidia.com/en-us/networking/products/silicon-photonics/)
- [Tom's Hardware — Nvidia 400 Tb/s photonics millions of GPUs](https://www.tomshardware.com/networking/nvidias-silicon-photonics-based-1-6-tb-s-switch-platforms-enable-clusters-with-millions-of-gpus)
- [AICPLight — Spectrum-X vs Quantum-X explained](https://www.aicplight.com/blog-news/nvidia-spectrum-x-vs-quantum-x-ethernet-vs-infiniband-for-ai-data-centers-cpo-era-explained-236)

### ConnectX-9 SuperNIC
- [NVIDIA ConnectX-9 datasheet](https://resources.nvidia.com/en-us-accelerated-networking-resource-library/connectx-9-supernic-datasheet)
- [NVIDIA Docs — ConnectX-9 Specifications](https://docs.nvidia.com/networking/display/connectx9supernic/specifications)
- [NADDOD — ConnectX-9 800G Ethernet breakthrough](https://www.naddod.com/ai-insights/nvidia-connectx-9-supernic-analysis-1x800g-ethernet-breakthrough)

### BlueField-4 DPU
- [NVIDIA Developer Blog — BlueField-4 CMX Context Memory](https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/)
- [ServeTheHome — Rubin Compute Platform at CES 2026](https://www.servethehome.com/nvidia-launches-next-generation-rubin-ai-compute-platform-at-ces-2026/)
- [Chiplog — BlueField-4 DPU analysis](https://www.chiplog.io/p/analysis-of-nvidias-bluefield-4-dpu)

### Spectrum-XGS（scale across）
- [NVIDIA Newsroom — Spectrum-XGS Giga-Scale AI](https://nvidianews.nvidia.com/news/nvidia-introduces-spectrum-xgs-ethernet-to-connect-distributed-data-centers-into-giga-scale-ai-super-factories)
- [NVIDIA Developer Blog — Scale-Across Networking](https://developer.nvidia.com/blog/how-to-connect-distributed-data-centers-into-large-ai-factories-with-scale-across-networking/)
- [SDxCentral — Spectrum-XGS one gigantic GPU](https://www.sdxcentral.com/news/nvidias-new-spectrum-xgs-aims-to-turn-multiple-data-centers-into-one-gigantic-gpu/)

### NVLink Fusion
- [NVIDIA NVLink Fusion page](https://www.nvidia.com/en-us/data-center/nvlink-fusion/)
- [NVIDIA Newsroom — Marvell joins NVLink Fusion](https://nvidianews.nvidia.com/news/nvidia-ai-ecosystem-expands-as-marvell-joins-forces-through-nvlink-fusion)
- [Ayar Labs — joins NVLink Fusion](https://ayarlabs.com/news/ayar-labs-joins-nvidia-nvlink-fusion-ecosystem-to-bring-co-packaged-optics-to-rack-scale-ai-infrastructure/)
- [Lightmatter — joins NVLink Fusion](https://lightmatter.co/press-release/lightmatter-joins-nvidia-nvlink-fusion/)
- [The Next Platform — $2B Marvell NVLink Fusion](https://www.nextplatform.com/connect/2026/03/31/the-2-billion-nvidia-deal-with-marvell-is-about-a-lot-more-than-nvlink-fusion/5213790)

## 相關連結

- [[Hyper Rail / Multi-Rail（光通訊整合技術）]]
- [[CPO 供應鏈圖譜]]
- [[TGV × CPO 依賴圖]]
- [[HBM4E × Glass Interposer × TGV 交會]]
- [[AI 記憶體結構性供給短缺]]
- [[賣水人選股邏輯（投資版）]]
- [[控制點轉移（投資版）]]
- [[半導體基礎建設化]]
- [[Jevons Paradox（投資版）]]
- [[市場四階段：懷疑／驗證／共識／反轉]]
- [[資訊擴散四階段]]
- [[NVDA]]、[[AVGO]]、[[Marvell]]
- [[Ciena]]、[[Nokia]]
- [[Lumentum]]、[[Coherent]]
- [[TSMC]]
- [[SiTime]]（MEMS）+ [[TXC]] / [[NDK]] / [[Epson]] / [[Kyocera]] / [[Rakon]]（石英陣營五家、2026-06-09 #H1 補完）
- [[SK Hynix]]、[[Samsung Electronics]]、[[Micron]]

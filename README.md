# TWBbot

以 Python 與 Pycord 開發的開源 Discord 機器人。

提供一般實用指令、文字編碼與雜湊計算，以及 YouTube 音樂播放等功能，並採用模組化架構管理機器人指令。

## 功能特色

### 一般指令

| 指令 | 功能 |
|---|---|
| `/help` | 顯示機器人指令列表 |
| `/ping` | 查看機器人延遲 |
| `/covid感染人數` | 查詢台灣昨日 COVID-19 確診人數 |
| `/rickroll` | Rickroll 彩蛋 |

### 音樂播放（Beta）

提供 YouTube 音樂播放相關功能。此功能目前仍處於實驗階段，部分指令可能因 Discord 斜線指令遷移而無法使用。

| 指令 | 功能 |
|---|---|
| `/加入語音` | 讓機器人加入使用者所在的語音頻道 |
| `/play` | 播放 YouTube 音樂 |
| `/resume` | 繼續播放音樂 |
| `/pause` | 暫停播放 |
| `/stop` | 停止播放 |
| `/離開語音` | 讓機器人離開語音頻道 |
| `/clear` | 清理多餘的音訊檔案 |

### 編碼與雜湊

| 指令 | 功能 |
|---|---|
| `/base64_enc` | 將文字編碼為 Base64 |
| `/base64_dec` | 將 Base64 解碼為文字 |
| `/hash` | 計算文字的雜湊值 |

> **注意：** Base64 是編碼方式，不是加密演算法；雜湊也不等同於加密，不能用來還原原始文字。

## 技術架構

- **Python**：主要開發語言。
- **Pycord**：Discord API 封裝與斜線指令支援。
- **模組化指令系統**：透過 `commands/` 目錄載入獨立指令模組。
- **JSON 設定檔**：保存機器人狀態、指令說明與開發者資訊。
- **YouTube 音訊相關套件**：支援音樂播放功能。

## 專案結構

```text
TWBbot/
├── bot.py                  # 機器人進入點與初始化
├── commands/               # 指令模組
├── config/
│   ├── commands.json       # 指令說明與 Help 頁面內容
│   ├── state.json          # 機器人狀態與活動文字
│   └── author.json         # 開發者資訊
├── requirements.txt        # Python 相依套件
├── token.json              # Discord Bot Token 設定
└── LICENSE                 # MIT License
```

## 安裝與執行

### 1. 環境需求

- Python
- Discord Bot Application 與 Bot Token
- 已安裝相依套件的執行環境
- 若要使用音樂功能，還需要符合相關套件需求的音訊播放環境

### 2. 下載專案

```bash
git clone https://github.com/Thomas10409/TWBbot.git
cd TWBbot
```

### 3. 建立虛擬環境（建議）

Windows：

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux / macOS：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. 安裝相依套件

```bash
python -m pip install -r requirements.txt
```

若安裝或執行時遇到 Discord 套件衝突，請檢查 `requirements.txt` 中 `discord.py` 與 `py-cord` 的版本相容性，避免同時安裝互相衝突的套件。

### 5. 設定 Bot Token

將 Discord Developer Portal 取得的 Bot Token 設定至本機的 `token.json`：

```json
{
    "token": "YOUR_DISCORD_BOT_TOKEN"
}
```

請勿將真實 Token 提交至 GitHub。建議將 `token.json` 加入 `.gitignore`，並使用不納入版本控制的本機設定檔。

### 6. 啟動機器人

```bash
python bot.py
```

啟動後，觀察終端機輸出，確認機器人是否成功登入，以及各個指令模組是否載入成功。

## 設定檔說明

### `config/state.json`

設定機器人的在線狀態與活動文字：

```json
{
    "state": "discord.Status.online",
    "state_text": "狀態文字"
}
```

實際可用的狀態值應符合程式所使用的 Discord API 格式。

### `config/author.json`

設定 Help 頁面顯示的開發者資訊：

```json
{
    "bot_author": "開發者名稱"
}
```

### `config/commands.json`

定義 Help 頁面所顯示的指令名稱、說明與版面設定。新增或修改指令時，請確認相關設定與實際指令模組一致。

## 開發與擴充

本專案採用獨立指令模組的設計。新增功能時，可在 `commands/` 目錄建立新的 Python 模組，並依照現有的 Pycord Extension 架構實作。

啟動時，主程式會掃描 `commands/` 目錄中的 Python 檔案，嘗試載入各個模組，並輸出載入結果，方便追蹤指令初始化問題。

新增指令後，亦應同步更新 `config/commands.json`，確保 Help 頁面的指令資訊正確。

## 已知限制與待辦事項

- 音樂功能仍處於 Beta 階段，部分指令尚未正常運作。
- 部分舊有功能需要配合 Discord 斜線指令機制調整。
- 音訊播放相關依賴與套件版本仍需確認相容性。
- 可進一步改善錯誤處理、設定驗證與模組載入機制。
- 可增加更多實用工具與互動功能。

## 授權條款

本專案採用 [MIT License](LICENSE)。

Copyright (c) 2024 Thomas10409


# Baseball Hub ⚾｜MLB 歷年數據與 30 隊圖鑑

這是一個以繁體中文撰寫的 GitHub Pages 靜態教學網站，依照 `AGENTS.md` 的規範，用 JSON 擴充球隊、球員及歷年統計資料。

## 功能

- 全站改為白底深字、淺綠重點的高對比設計
- **歷年獎項頁面**：2023–2025 年 MVP、賽揚獎、新人王、年度總教練，美聯／國聯逐年切換
- **季後賽結果頁面**：2023–2025 年官方查證資料（2023 僅世界大賽／聯盟冠軍賽），年份與輪次篩選，冠軍與比分


- MLB 30 支球隊索引，依美聯／國聯、東中西區篩選
- 球員搜尋及詳細資訊
- 切換球員的已收錄賽季（示範：Aaron Judge、Shohei Ohtani 的 2024、2025 打擊數據）
- 打擊／投球數據模板，缺少資料時顯示 `—` 或未提供
- 球隊逐季代表人物欄位；缺資料時不會虛構王牌投手
- MLB、FanGraphs、Baseball Savant 及 Baseball America 的外部連結欄位（只顯示已查證網址）
- 常用傳統及入門進階指標解說

> **重要**：目前為「可運作的架構與局部示範資料」，不是 30 隊完整球員／年度數據資料庫。`data/pitching.json` 暫為空陣列。未經核實的數字與代表人選不會自動填入。網頁沒有爬蟲，也不會在瀏覽器抓取第三方數據。

## 目錄

```
index.html
AGENTS.md
README.md
css/style.css
js/main.js
js/data-bundle.js  # 離線開啟備援資料
tools/build_bundle.py  # 同步 JSON 至離線快取
data/teams.json
data/players.json
data/batting.json
data/pitching.json
data/team-highlights.json
data/glossary.json
data/awards.json
data/postseason.json
assets/baseball.svg
```

## 本地預覽

可以直接雙擊 `index.html` 開啟；網站會使用 `js/data-bundle.js` 內的離線快取資料。

建議正式測試時，從專案根目錄執行：

```bash
python -m http.server 8000
```

在瀏覽器開啟 `http://localhost:8000/`。網站透過 HTTP 開啟時優先讀取 `data/*.json`；直接雙擊 HTML 時，則自動切換到離線資料快取。

## GitHub Pages

1. 建立公開 GitHub repository（例如 `baseball-hub`）。
2. 將 **ZIP 解壓縮後 `baseball-hub` 目錄內的所有檔案** 上傳到 repository 根目錄（`index.html` 必須在根目錄）。
3. **Settings → Pages → Build and deployment → Deploy from a branch**。
4. 選擇 **main** 與 **/(root)**，儲存並等待 GitHub 完成部署。
5. 網址一般是 `https://<username>.github.io/baseball-hub/`。

## 來源與著作權

- 打者示範數據依 [Baseball Savant - Aaron Judge](https://baseballsavant.mlb.com/savant-player/aaron-judge-592450) 與 [Baseball Savant - Shohei Ohtani](https://baseballsavant.mlb.com/savant-player/shohei-ohtani-660271) 網頁上可核對的 2024/2025 例行賽資料建立。
- FanGraphs／MLB／Baseball America 只以已查證的外部連結引導使用者查看原站；**不代表獲授權抓取／大量再發布第三方數據**。
- 外部網址、內容、訂閱限制可能變動。未經核實的數據不應添加。
- 這是非官方課堂展示專案，沒有使用官方球員照片或球隊 Logo。

## AI 擴充示範指令

> 請先閱讀 AGENTS.md 與 README.md，替 Baseball Hub 的 `data/batting.json` 新增一筆已核實的歷年成績，附上賽季與原始來源連結；不要修改現有 HTML 模板，並驗證 JSON 和網站的賽季選單。

## 新增或修改資料後

更新 `data/*.json` 後，請執行：

```bash
python tools/build_bundle.py
```

這會同步更新 `js/data-bundle.js`，確保雙擊預覽看到新資料。GitHub Pages 正常使用 JSON 資料。

## 圖片功能（新版）
球隊列表與球隊詳情可顯示 `logoUrl`，球員卡片與球員詳情可顯示 `photoUrl`。示範網址為 MLB 遠端圖片來源（需連網）；如失效或未設定，自動顯示備援棒球圖案。更新 JSON 後請執行 `python tools/build_bundle.py`。

**授權提醒**：MLB 官方隊徽、球員照片可能受著作權及商標權保護，公開使用須確認有適當許可。這份教學專案不包含官方圖片檔，也不代表遠端存取等於取得再公開授權。若無權利，建議將 `logoUrl`、`photoUrl` 設為 `null` 並使用備援圖示，或提供可合法使用的替代圖片。

## 更新年度獎項與季後賽資料

請分別編輯 `data/awards.json` 和 `data/postseason.json`，新增條目時保留官方來源網址，避免重複 ID；更新後執行 `python tools/build_bundle.py`。詳細欄位規範請見 `AGENTS.md`。這兩頁目前只收錄部分已核實年度，不代表所有歷史年度均已完整建立。


## 2026 更新：獎項、季後賽、球員合約與自由球員

- 2026 獎項：新人王、年度總教練已收錄；截至台灣時間 2026-11-11，賽揚獎（11/12）、MVP（11/13）仍待公布。顯示官方預定日期。
- 2026 季後賽：收錄 11 組已完賽系列賽，釀酒人贏得世界大賽，資料連結至 MLB 官方。
- 球員資料中的合約剩餘年限按「2026 球季結束後」估算，已核實 4 名示範球員；合約選擇權會影響實際年限。
- 新增 `data/free-agents.json`，可選擇 2024-25、2025-26、2026-27 休賽季並搜尋。歷年有已簽約球隊，最新年度沒有確認簽約的示範球員顯示「待確認」。此非完整自由球員名單。
- 編輯 JSON 後請執行 `python tools/build_bundle.py` 以同步離線快取。

資料更新日期：2026-11-11；本站為課堂展示用的非即時整理。

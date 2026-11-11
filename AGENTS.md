# AGENTS.md — Baseball Hub

## 專案目的
Baseball Hub 是以繁體中文介紹 MLB 球員與棒球知識的靜態網站，適合初學者閱讀，也方便日後持續擴充。這份文件是 AI 代理開發本專案時必須遵守的規範。

## 技術與部署
- 使用 HTML5、CSS3、原生 JavaScript（傳統 defer scripts，以支援 file:// 離線預覽），不使用後端與資料庫。
- 全部資源使用相對路徑，確保能部署於 `https://<username>.github.io/<repository>/`。
- 禁止加入需要 API Key 的瀏覽器請求或未經驗證的即時數據。
- 所有頁面必須支援手機與桌面、鍵盤操作及基本無障礙功能。

## 視覺規範
- 風格：白色背景、深墨綠文字、淺灰綠卡片、俐落字體、大量留白，使用森林綠作重點色，避免深底閱讀困難。
- 全站使用 `css/style.css` 設計 token，不直接在 HTML 寫大量行內樣式。
- 標題、導覽、球員卡片與按鈕沿用現有元件，不自行新增不一致的版型。
- 圖形優先使用 CSS 或自製 SVG，避免未經授權的球員照片與球隊商標。

## 專案結構
```
baseball-hub/
├── AGENTS.md
├── README.md
├── index.html
├── css/style.css
├── js/main.js
├── js/data-bundle.js       # 自動生成的雙擊預覽快取
├── tools/build_bundle.py  # 快取生成工具
├── data/teams.json
├── data/players.json
├── data/batting.json
├── data/pitching.json
├── data/team-highlights.json
├── data/glossary.json
├── data/awards.json         # 逐年獎項得主
├── data/postseason.json     # 逐年系列賽結果
└── assets/baseball.svg
```

## 資料格式：球員
新增球員請先編輯 `data/players.json`，不可複製另一份 HTML 頁面。每筆球員需有：
- `id`：英文小寫 kebab-case，永久且不重複
- `name`：常見中文名
- `englishName`：英文名
- `team`：資料撰寫時的球隊名稱；異動時應核實更新
- `position`：位置（如 OF、P/DH）
- `number`：背號，以字串儲存；無法確認用 `—`
- `tags`：特色標籤陣列
- `summary`：40–100 字的繁體中文簡介
- `highlights`：2–4 個具體特色，禁止虛構統計
- `accent`：CSS 允許的色票（`gold` / `blue` / `red`）

## 資料格式：棒球知識
編輯 `data/glossary.json`，每篇條目使用現有 `term`、`name`、`description` 欄位，首次使用術語時提供英文或縮寫。

## 新增內容標準流程
1. 先閱讀 `AGENTS.md`、`README.md` 與既有 JSON 範例。
2. 判斷新增球員、球隊、賽季成績或知識條目，優先在對應 JSON 新增物件。
3. 保持欄位完整、標點與口吻一致，確保 `id` 不重複。
4. 不新增無來源的年度戰績、薪資、排行或即時數據。需使用時先查證並標註日期與來源。
5. 不修改既有內容的資訊架構或 UI 元件，除非任務明確要求。
6. 每次編輯 `data/*.json` 後執行 `python tools/build_bundle.py` 同步離線預覽快取，不可手動修改 `js/data-bundle.js`。
7. 本地測試：JSON 可解析、搜尋與篩選正常、卡片能開啟詳情、手機版可用、沒有壞連結。
8. 確保使用 GitHub Pages 子路徑時仍可載入 JS、CSS、JSON 與 SVG。

## AI 範例指令
「先閱讀 AGENTS.md。請在 `data/players.json` 新增一位球員，遵守現有 JSON 欄位與繁體中文風格。不要重寫首頁或加入沒有來源的統計數字。完成後檢查 JSON 格式與畫面顯示。」

## 交付檢查清單
- [ ] 首頁可以瀏覽
- [ ] 球員搜尋與篩選正常
- [ ] 棒球知識可點擊閱讀
- [ ] 響應式與鍵盤可操作
- [ ] JSON 結構正確
- [ ] GitHub Pages 可正常載入資源

## 9. 歷年數據與外部來源（本版增補，優先遵守）

- 資料分開存於 `data/players.json`、`data/teams.json`、`data/batting.json`、`data/pitching.json`、`data/team-highlights.json`、`data/glossary.json`。
- 球員資料的 `team` 使用球隊代碼；歷年紀錄以 `playerId`、`season`、`team` 關聯，避免把目前球隊誤當所有賽季球隊。
- 網頁可依球員與賽季切換數據；未收錄或無法核實的統計值必須顯示 `—`，不得填入 0 或推估值。
- 2024、2025 年部分打者成績僅作為已核實示範，不代表完整資料庫；新資料必須標明賽季、來源網址、統計口徑。進階數據如 fWAR、bWAR、wRC+、OPS+ 不得混淆來源或自行聲稱等價。
- 30 隊索引可以先完整建立；但年度王牌投手／核心打者應依出賽量、統計、角色等有據可查的選擇標準，逐季獨立評選。未評選時使用 `null`，不得憑印象補完。
- 每位球員的 `links` 可以包含 `mlb`、`fangraphs`、`savant`、`baseballAmerica`；球隊可以包含 `officialUrl`、`prospectsUrl` 等已確認的 https 網址，沒有已驗證連結就略過，不得猜測 slug 或 ID。
- 外部連結應以新分頁開啟，使用 `rel="noopener noreferrer"`，連結文案必須清楚標示來源；若指向可能付費的 Baseball America 文章，提醒可能需要訂閱。
- MLB、FanGraphs、Baseball America、Baseball Savant 均為第三方網站。預設只提供已查證的超連結；未經許可不得以自動爬蟲、批次下載、反爬繞過、直接內嵌內容方式取得資料。若要匯入資料，先確認來源的授權與使用條款，優先採明確允許的手動匯出或取得許可的資料介面。
- 純前端不得儲存 API 金鑰或執行第三方抓取；若未來需要更新流程，使用獨立的離線腳本，經人工檢查才將 JSON 更新至儲存庫。
- 網站為課堂教學展示，不是即時數據、官方平台，也不得使用未授權的球員照片及球隊標誌。
- 開發前應閱讀實際現有檔案；新增內容優先修改 JSON，不重複建立球員 HTML。

## 10. 離線預覽與測試
- `index.html` 使用兩個依序執行的 `defer` 腳本，先載入 `js/data-bundle.js`，再執行 `js/main.js`。
- HTTP / GitHub Pages 優先讀取 `data/*.json`，`file://` 模式使用已同步的離線快取。
- 修改 JSON 後必須執行 `python tools/build_bundle.py`，並分別測試直接雙擊開啟與 HTTP 預覽。
- 發佈前檢查球隊篩選、球員搜尋、詳情開啟、賽季切換、外部連結。

## 11. 球隊隊徽與球員照片
- `data/teams.json` 可加入 `mlbTeamId` 與 `logoUrl`；`data/players.json` 可加入 `mlbId` 與 `photoUrl`。
- 影像網址只允許 `https://`，由 `js/main.js` 共用元件顯示，不在 HTML 硬編碼圖像。
- 卡片與詳情都應顯示圖片；載入失敗、未設定圖片或無網路時顯示備援圖示，仍可閱讀文字及使用功能。
- 圖片必須有描述性 `alt`、維持比例及手機版排版，並避免因圖片失敗影響 UI。
- 官方隊徽和球員照片可能受到商標權、著作權及肖像授權限制。此版僅在 JSON 示範第三方官方圖片的遠端網址，不包含下載或轉存。公開網站使用前，須確認可使用的授權或替換為獲授權素材；公開可存取不等於允許再發布。
- 新增照片或隊徽時不得猜測球員/球隊的識別碼，必須對照官方資料核實；避免不明來源或可能不符合使用條款的圖片。
- 修改 JSON 後執行 `python tools/build_bundle.py`，確保離線資料同步。

## 歷年獎項頁面（新增）
- 來源：`data/awards.json`，資料必須核對 MLB 官方獎項網站或可信來源。
- 欄位：`id`, `season`, `category`（MVP/CY/ROY/MOY）, `league`（AL/NL）, `winner`, `englishName`, `team`, `source`。
- 每年度、每獎項、每聯盟只能有一個得主記錄；特殊並列結果須先修改 schema 才能輸入。
- 預設只顯示已驗證的 2023–2025 資料；2026 及歷年其他獎項需核實後擴充。
- 年度切換、獎項篩選由 `js/main.js` 共用模板呈現，不可為每年新增 HTML。

## 季後賽結果頁面（新增）
- 來源：`data/postseason.json`，逐筆記錄一組系列賽的勝者與敗者，不自行推算比賽結果。
- 欄位：`id`, `season`, `round`（WS/CS/DS/WC）, `league`（MLB/AL/NL）, `winner`, `loser`, `wins`, `losses`, `source`。
- 系列賽分數代表勝出球隊取得的勝場，與敗方取得的勝場；不能混成單場比分。
- 各年未收錄的對戰必須顯示「未收錄」，不得誤稱為完整賽程；官方不同年代的賽制可能不同。
- 必須有年份與輪次篩選、世界大賽冠軍摘要及外部官方回顧連結。
- 新增或修改 JSON 後，執行 `python tools/build_bundle.py` 更新離線預覽快取。

## 新版視覺與可及性檢查
- 維持白色與高對比深色文字；不可在白底使用接近白色字或很淡的淺灰字。
- 桌面與手機版均能閱讀獎項卡片、比分、外部來源。
- 標準 `<select>` 支援鍵盤操作，更新後由 `aria-live` 區域公告內容變更。


## 2026 年資料、合約年限與自由球員（2026-11-11 更新）

- 獎項 `data/awards.json` 包含 `status` (`announced` 或 `pending`)、`announcedAt`（台灣日期 YYYY-MM-DD）與 `source`。尚未揭曉必須用 `winner: null`，畫面顯示「尚未公布」及官方預定時間，不可推測。
- 季後賽 `data/postseason.json` 每個系列賽均需由 MLB 官方賽季歷史頁驗證勝隊、敗隊、勝敗場數。
- 球員 `data/players.json` 可加入 `contract`：`throughSeason`（保證年限截至的球季）、`asOf`、`status`、`note`、`source`。顯示「2026 球季結束後尚有幾個未來球季」時，計算 `max(0, throughSeason - 2026)`。合約含選擇權、跳脫條款或複雜遞延時，必須提示；未查核不能填入。
- 自由球員資料放 `data/free-agents.json`，每筆包含 `id`、`offseason` (例如 `2026-27`)、`name`、`englishName`、`position`、`previousTeam`、`status` (`signed`/`unsigned`)、`destination`、`source`、`note`。當年度 `unsigned` 時 `destination` 必須為 `null`。歷年 `signed` 必須填真正簽約隊伍（允許原隊續約）。
- 休賽季名稱 `2026-27` 指 2026 球季結束後、2027 賽季開始前。**自由球員不是交易球員**；需先查核球員確實取得自由球員身分。
- 自由球員只顯示已查證的代表名單，不宣稱完整收錄。2026-27 年資料可能因簽約而快速改變，修改前必須重新核對 MLB 交易公告。
- 禁止直接批量擷取 FanGraphs、Baseball America 等限制自動化訪問的服務。可使用已查證的外部連結。
- 修改任一 JSON 後，執行 `python tools/build_bundle.py` 更新雙擊開啟時使用的資料備援。驗證所有選單、搜尋、合約文字及外部網址。

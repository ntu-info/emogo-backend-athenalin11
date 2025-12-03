# EmoGo Backend 部署完整指南

## 📋 部署檢查清單

- [ ] 設定 MongoDB Atlas
- [ ] 在 MongoDB 中建立測試資料
- [ ] 部署到 Render
- [ ] 設定環境變數
- [ ] 測試 API 端點
- [ ] 更新 README.md 中的實際 URI
- [ ] 提交到 GitHub
- [ ] 上傳到 NTU COOL

---

## 第一步：設定 MongoDB Atlas

### 1.1 建立 MongoDB Atlas 帳號
1. 前往 https://www.mongodb.com/cloud/atlas
2. 點擊 "Try Free" 註冊帳號
3. 登入後，選擇建立 **FREE** tier 的 Cluster

### 1.2 設定網路存取
1. 在左側選單點擊 **Network Access**
2. 點擊 **Add IP Address**
3. 選擇 **Allow Access from Anywhere**
4. IP Address 輸入：`0.0.0.0/0`
5. 點擊 **Confirm**

### 1.3 建立資料庫使用者
1. 在左側選單點擊 **Database Access**
2. 點擊 **Add New Database User**
3. 選擇 **Password** 認證方式
4. 輸入使用者名稱和密碼（請記住這些資訊！）
5. 在 **Database User Privileges** 選擇 **Read and write to any database**
6. 點擊 **Add User**

### 1.4 取得連接字串
1. 點擊 **Database** (左側選單)
2. 點擊您的 Cluster 的 **Connect** 按鈕
3. 選擇 **MongoDB Compass**
4. 複製連接字串，格式如下：
   ```
   mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/
   ```
5. 將 `<username>` 和 `<password>` 替換為您剛才建立的使用者資訊

範例：
```
mongodb+srv://myuser:mypassword123@cluster0.abc123.mongodb.net/
```

---

## 第二步：使用 MongoDB Compass 建立測試資料

### 2.1 下載並安裝 MongoDB Compass
- 下載連結：https://www.mongodb.com/try/download/compass

### 2.2 連接到您的資料庫
1. 開啟 MongoDB Compass
2. 點擊左上角的 **+** (New Connection)
3. 貼上您的連接字串
4. 點擊 **Save & Connect**

### 2.3 建立資料庫和集合
1. 點擊 **Create Database**
2. Database Name: `emogo_db`
3. Collection Name: `vlogs`
4. 點擊 **Create Database**

5. 在 `emogo_db` 下再建立兩個 collections:
   - `sentiments`
   - `gps_coordinates`

### 2.4 新增測試資料

#### 在 `vlogs` collection 中新增資料：
1. 點擊 `vlogs` collection
2. 點擊 **ADD DATA** → **Insert Document**
3. 貼上以下 JSON：
```json
{
  "user_id": "user001",
  "title": "美好的一天",
  "content": "今天去了台北101，心情很好！",
  "video_url": "https://example.com/videos/taipei101.mp4",
  "timestamp": {"$date": "2025-12-01T10:00:00Z"}
}
```
4. 重複步驟，新增更多資料（參考 `sample_data.py`）

#### 在 `sentiments` collection 中新增資料：
```json
{
  "user_id": "user001",
  "emotion": "happy",
  "score": 0.85,
  "text": "今天天氣真好，心情很棒！",
  "timestamp": {"$date": "2025-12-01T10:30:00Z"}
}
```

#### 在 `gps_coordinates` collection 中新增資料：
```json
{
  "user_id": "user001",
  "latitude": 25.0330,
  "longitude": 121.5654,
  "accuracy": 10.5,
  "timestamp": {"$date": "2025-12-01T10:00:00Z"}
}
```

---

## 第三步：部署到 Render

### 3.1 準備 GitHub Repository
1. 確保所有檔案都已提交到 GitHub
```bash
git add .
git commit -m "Add EmoGo backend with MongoDB integration"
git push
```

### 3.2 在 Render 建立 Web Service
1. 前往 https://render.com/
2. 註冊/登入帳號
3. 點擊 **New +** → **Web Service**
4. 連接您的 GitHub 帳號
5. 選擇 `emogo-backend-athenalin11` repository

### 3.3 設定 Web Service
填入以下資訊：

- **Name**: `emogo-backend-athenalin11` (或您喜歡的名稱)
- **Region**: `Singapore` (最接近台灣)
- **Branch**: `main`
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Instance Type**: `Free`

### 3.4 設定環境變數
1. 在 **Environment Variables** 區域
2. 點擊 **Add Environment Variable**
3. Key: `MONGODB_URI`
4. Value: 貼上您的 MongoDB 連接字串
   ```
   mongodb+srv://myuser:mypassword123@cluster0.abc123.mongodb.net/
   ```
5. 點擊 **Add**

### 3.5 部署
1. 點擊 **Create Web Service**
2. 等待部署完成（約 5-10 分鐘）
3. 部署成功後，您會看到類似這樣的 URL：
   ```
   https://emogo-backend-athenalin11.onrender.com
   ```

---

## 第四步：測試 API

### 4.1 測試基本端點
在瀏覽器中訪問：
```
https://your-app-name.onrender.com/
```
應該會看到歡迎訊息。

### 4.2 測試健康檢查
```
https://your-app-name.onrender.com/health
```
確認 `database: "connected"`

### 4.3 查看 API 文件
```
https://your-app-name.onrender.com/docs
```
這是互動式的 Swagger UI，可以直接測試 API。

### 4.4 測試資料匯出（重要！這是作業要求）
```
https://your-app-name.onrender.com/export/all
```
應該會看到您在 MongoDB 中建立的所有測試資料。

### 4.5 測試個別資料類型
- Vlogs: `https://your-app-name.onrender.com/export/vlogs`
- Sentiments: `https://your-app-name.onrender.com/export/sentiments`
- GPS: `https://your-app-name.onrender.com/export/gps`

---

## 第五步：更新 README.md

### 5.1 更新實際的 URI
1. 打開 `README.md`
2. 將所有 `your-app-name` 替換為您實際的應用程式名稱
3. 例如：
```markdown
**主要資料匯出 API（包含所有三種資料類型）:**
https://emogo-backend-athenalin11.onrender.com/export/all
```

### 5.2 提交更新
```bash
git add README.md
git commit -m "Update README with actual deployment URLs"
git push
```

---

## 第六步：提交作業

### 6.1 確認檢查清單
- [x] MongoDB Atlas 已設定並有測試資料
- [x] Render 部署成功
- [x] `/export/all` 端點可以訪問並顯示所有三種資料
- [x] README.md 中已列出實際的 URI
- [x] 所有更新已推送到 GitHub

### 6.2 提交到 NTU COOL
1. 複製您的 GitHub repository URL
   ```
   https://github.com/ntu-info/emogo-backend-athenalin11
   ```
2. 在 12/4 (四) 晚上 8:00 前提交到 NTU COOL

---

## 🔍 常見問題

### Q1: Render 部署失敗怎麼辦？
**A:** 檢查 Render 的 Logs，常見原因：
- `requirements.txt` 格式錯誤
- MongoDB URI 設定錯誤
- Start Command 錯誤

### Q2: API 回傳 "database: disconnected"？
**A:** 檢查：
- MongoDB Atlas 的 Network Access 是否設定為 `0.0.0.0/0`
- 環境變數 `MONGODB_URI` 是否正確
- MongoDB 使用者帳號密碼是否正確

### Q3: `/export/all` 顯示空資料？
**A:** 
- 確認在 MongoDB Compass 中確實有建立測試資料
- 資料庫名稱是否為 `emogo_db`
- Collection 名稱是否為 `vlogs`, `sentiments`, `gps_coordinates`

### Q4: Render 免費版本的限制？
**A:** 
- 15 分鐘沒有請求會自動休眠
- 下次訪問需要等待約 30 秒喚醒
- 每月有 750 小時免費使用時間

### Q5: 如何新增更多測試資料？
**A:** 使用 `/docs` 端點的 Swagger UI，可以直接在瀏覽器中測試 POST 請求：
1. 訪問 `https://your-app-name.onrender.com/docs`
2. 展開 `POST /vlogs` (或其他端點)
3. 點擊 "Try it out"
4. 填入 JSON 資料
5. 點擊 "Execute"

---

## 📞 需要幫助？

如果遇到問題：
1. 檢查 Render 的 Logs
2. 檢查 MongoDB Atlas 的連接設定
3. 使用 `/health` 端點確認服務狀態
4. 查看 FastAPI 的錯誤訊息（在 `/docs` 中測試）

---

**祝部署順利！🚀**

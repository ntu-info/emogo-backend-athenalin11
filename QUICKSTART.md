# 🚀 快速入門 - 3 個步驟完成部署

## Step 1: 設定 MongoDB Atlas (10 分鐘)

1. 前往 https://www.mongodb.com/cloud/atlas 註冊
2. 建立免費 Cluster
3. Network Access → Add IP → `0.0.0.0/0` (允許所有 IP)
4. Database Access → 建立使用者 (記住帳號密碼！)
5. Connect → MongoDB Compass → 複製連接字串

**您的連接字串範例：**
```
mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/
```

---

## Step 2: 建立測試資料 (5 分鐘)

### 使用 MongoDB Compass：
1. 下載 MongoDB Compass: https://www.mongodb.com/try/download/compass
2. 連接到您的資料庫（貼上連接字串）
3. 建立資料庫 `emogo_db`，包含 3 個 collections:
   - `vlogs`
   - `sentiments`
   - `gps_coordinates`

### 快速新增測試資料：
在每個 collection 中新增至少一筆資料（參考 `sample_data.py`）

**Vlogs 範例：**
```json
{
  "user_id": "test_user",
  "title": "測試 Vlog",
  "content": "這是測試內容",
  "timestamp": {"$date": "2025-12-01T10:00:00Z"}
}
```

**Sentiments 範例：**
```json
{
  "user_id": "test_user",
  "emotion": "happy",
  "score": 0.8,
  "text": "心情不錯",
  "timestamp": {"$date": "2025-12-01T10:00:00Z"}
}
```

**GPS 範例：**
```json
{
  "user_id": "test_user",
  "latitude": 25.0330,
  "longitude": 121.5654,
  "timestamp": {"$date": "2025-12-01T10:00:00Z"}
}
```

---

## Step 3: 部署到 Render (10 分鐘)

### 3.1 推送到 GitHub
```bash
git add .
git commit -m "Complete EmoGo backend setup"
git push
```

### 3.2 在 Render 部署
1. 前往 https://render.com/
2. New + → Web Service
3. 連接 GitHub → 選擇此 repository
4. 設定：
   - **Name**: `emogo-backend-你的名字`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     - Key: `MONGODB_URI`
     - Value: `你的MongoDB連接字串`
5. Create Web Service

### 3.3 等待部署完成（5-10 分鐘）
部署完成後會得到 URL，例如：
```
https://emogo-backend-你的名字.onrender.com
```

---

## ✅ 驗證部署成功

訪問以下網址確認：

1. **基本檢查**: `https://你的網址.onrender.com/`
   - 應該看到歡迎訊息

2. **健康檢查**: `https://你的網址.onrender.com/health`
   - 確認 `"database": "connected"`

3. **資料匯出** (作業要求): `https://你的網址.onrender.com/export/all`
   - 應該看到您建立的測試資料

4. **API 文件**: `https://你的網址.onrender.com/docs`
   - 互動式 API 文件

---

## 📝 最後步驟

### 1. 更新 README.md
將 `README.md` 中的 `your-app-name` 全部替換為您實際的應用程式名稱。

### 2. 再次推送到 GitHub
```bash
git add README.md
git commit -m "Update deployment URLs"
git push
```

### 3. 提交作業
- 截止時間: **2025/12/4 (四) 晚上 8:00**
- 提交內容: GitHub Repository URL
- 提交到: NTU COOL

---

## 🎯 作業要求檢查清單

- [ ] MongoDB Atlas 已設定
- [ ] 三個 collections 都有測試資料 (vlogs, sentiments, gps_coordinates)
- [ ] Render 部署成功
- [ ] `/export/all` 可以訪問並顯示所有資料
- [ ] README.md 中列出了實際的資料匯出 URI
- [ ] 推送到 GitHub
- [ ] 在期限前提交到 NTU COOL

---

## ⚡ 重要提醒

1. **MongoDB URI 要保密！** 不要將真實的 URI 提交到 GitHub（使用環境變數）
2. **Render 免費版會休眠** - 15 分鐘沒請求會自動休眠，下次訪問需等待約 30 秒
3. **測試資料要完整** - 確保三種資料類型都有至少 2-3 筆資料
4. **README 要更新** - 務必填入實際的部署 URL

---

需要詳細步驟？請參考 `DEPLOYMENT_GUIDE.md`

**祝順利完成作業！** 🎉

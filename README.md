[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/e7FBMwSa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21890628&assignment_repo_type=AssignmentRepo)

# EmoGo Backend - FastAPI + MongoDB

這是 EmoGo 的後端 API，使用 FastAPI 和 MongoDB Atlas 建立。

## 🌐 資料匯出/下載頁面 URI

**主要資料匯出 API（包含所有三種資料類型）:**
```
https://your-app-name.onrender.com/export/all
```

**個別資料類型匯出 API:**
- Vlogs 資料: `https://your-app-name.onrender.com/export/vlogs`
- 情感資料: `https://your-app-name.onrender.com/export/sentiments`
- GPS 座標: `https://your-app-name.onrender.com/export/gps`

**API 文件（互動式測試介面）:**
```
https://your-app-name.onrender.com/docs
```

> **注意**: 請將 `your-app-name` 替換為您在 Render 上實際部署的應用程式名稱。

## 📊 資料類型

本 API 收集並管理三種類型的資料：

1. **Vlogs（影音日誌）**
   - 使用者 ID
   - 標題
   - 內容
   - 影片/音訊 URL
   - 時間戳記

2. **Sentiments（情感資料）**
   - 使用者 ID
   - 情緒類型（happy, sad, angry, neutral 等）
   - 情感分數（0-1）
   - 文字內容
   - 時間戳記

3. **GPS Coordinates（GPS 座標）**
   - 使用者 ID
   - 經度
   - 緯度
   - 精確度
   - 時間戳記

## 🚀 API 端點

### 基本端點
- `GET /` - API 首頁和端點列表
- `GET /docs` - Swagger UI 互動式 API 文件
- `GET /health` - 健康檢查
- `GET /stats` - 資料庫統計資訊

### Vlogs API
- `POST /vlogs` - 新增 vlog
- `GET /vlogs` - 取得所有 vlogs
- `GET /vlogs/{user_id}` - 取得特定使用者的 vlogs

### Sentiments API
- `POST /sentiments` - 新增情感資料
- `GET /sentiments` - 取得所有情感資料
- `GET /sentiments/{user_id}` - 取得特定使用者的情感資料

### GPS API
- `POST /gps` - 新增 GPS 座標
- `GET /gps` - 取得所有 GPS 座標
- `GET /gps/{user_id}` - 取得特定使用者的 GPS 座標

### 資料匯出 API（作業要求）
- `GET /export/all` - **匯出所有三種類型的資料**
- `GET /export/vlogs` - 僅匯出 vlogs
- `GET /export/sentiments` - 僅匯出情感資料
- `GET /export/gps` - 僅匯出 GPS 座標

## 🛠️ 部署步驟

### 1. 設定 MongoDB Atlas

1. 前往 [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. 建立帳號並創建一個免費的 Cluster
3. 在 Network Access 中，設定允許的 IP 為 `0.0.0.0/0`（允許所有 IP）
4. 在 Database Access 中建立資料庫使用者
5. 取得連接字串（Connection String），格式如下：
   ```
   mongodb+srv://username:password@cluster.mongodb.net/
   ```

### 2. 部署到 Render

1. 前往 [Render](https://render.com/)
2. 建立新的 Web Service
3. 連接此 GitHub repository
4. 設定以下資訊：
   - **Name**: 您的應用程式名稱
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. 在 Environment Variables 中新增：
   - Key: `MONGODB_URI`
   - Value: 您的 MongoDB 連接字串
6. 點擊 "Create Web Service"

### 3. 測試部署

部署完成後，訪問以下網址測試：
- `https://your-app-name.onrender.com/` - 檢查 API 是否運作
- `https://your-app-name.onrender.com/docs` - 查看 API 文件
- `https://your-app-name.onrender.com/health` - 檢查資料庫連接狀態

## 📝 本地開發

### 安裝依賴
```bash
pip install -r requirements.txt
```

### 設定環境變數
在專案根目錄建立 `.env` 檔案：
```
MONGODB_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/
```

### 執行應用程式
```bash
uvicorn main:app --reload
```

應用程式將在 `http://localhost:8000` 啟動。

## 📖 使用範例

### 新增 Vlog
```bash
curl -X POST "https://your-app-name.onrender.com/vlogs" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "title": "My Day",
    "content": "Today was great!",
    "video_url": "https://example.com/video.mp4"
  }'
```

### 新增情感資料
```bash
curl -X POST "https://your-app-name.onrender.com/sentiments" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "emotion": "happy",
    "score": 0.85,
    "text": "Feeling great today!"
  }'
```

### 新增 GPS 座標
```bash
curl -X POST "https://your-app-name.onrender.com/gps" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "latitude": 25.0330,
    "longitude": 121.5654,
    "accuracy": 10.5
  }'
```

### 匯出所有資料
```bash
curl "https://your-app-name.onrender.com/export/all"
```

## 🔧 技術棧

- **FastAPI**: 現代、快速的 Python Web 框架
- **MongoDB Atlas**: 雲端 NoSQL 資料庫
- **Motor**: MongoDB 的非同步 Python 驅動程式
- **Render**: 應用程式部署平台

## 📦 相依套件

- `fastapi[all]` - FastAPI 框架及所有擴充功能
- `motor[srv]` - MongoDB 非同步驅動程式
- `pymongo` - MongoDB Python 驅動程式
- `python-multipart` - 處理表單資料

## 📄 授權

此專案為 NTU 資訊所課程作業專案。

## 👥 作者

- 學生: athenalin11
- 課程: NTU 資訊所

---

**截止日期**: 2025/12/4 (四) 晚上 8:00 PM
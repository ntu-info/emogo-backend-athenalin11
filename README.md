[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/e7FBMwSa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21890628&assignment_repo_type=AssignmentRepo)

# EmoGo Backend API

> 一個使用 FastAPI 和 MongoDB 建立的情緒日誌後端系統，用於收集和管理使用者的影音日誌（Vlogs）、情感資料（Sentiments）和 GPS 座標資訊。

**作者**: athenalin11  
**課程**: NTU 資訊所  
**部署狀態**: ✅ Live on Render  
**資料庫**: MongoDB Atlas

---

## 📖 專案概述

### 核心概念

EmoGo Backend 是一個 RESTful API 服務，旨在支援情緒追蹤應用程式的後端需求。本專案展示了現代 Web 開發的核心技術棧：

- **非同步程式設計**: 使用 Python 的 async/await 語法，實現高效能的非阻塞 I/O 操作
- **NoSQL 資料庫**: 採用 MongoDB 的靈活文件模型，適合處理多樣化的使用者資料
- **雲端部署**: 整合 Render（應用程式）和 MongoDB Atlas（資料庫）的雲端服務
- **API 設計**: 遵循 RESTful 原則，提供清晰的資源端點和標準 HTTP 方法

### 技術架構

```
┌─────────────┐         ┌──────────────┐         ┌─────────────────┐
│   使用者     │  HTTP   │   FastAPI    │  Motor  │  MongoDB Atlas  │
│  (客戶端)   │ ◄─────► │   (Render)   │ ◄─────► │   (雲端資料庫)   │
└─────────────┘         └──────────────┘         └─────────────────┘
```

### 應用場景

此 API 可用於：
- 📝 記錄使用者的日常生活影音日誌
- 😊 追蹤和分析情緒變化趨勢
- 📍 收集地理位置資訊，建立情緒地圖
- 📊 提供資料匯出功能，支援進一步分析

---

## 🌐 作業要求：資料匯出/下載頁面 URI

> **本 API 提供完整的資料匯出功能，TAs 和老師可以透過以下 URI 查看和下載所有資料。**

### 主要資料匯出端點（包含所有三種資料類型）

**完整資料匯出 API:**
```
https://emogo-backend-athenalin11.onrender.com/export/all
```

此端點會返回所有三種資料類型：
- ✅ **Vlogs**（影音日誌）
- ✅ **Sentiments**（情感資料）
- ✅ **GPS Coordinates**（GPS 座標）

### 個別資料類型匯出端點

如需查看特定類型的資料：

| 資料類型 | API 端點 |
|---------|---------|
| 📹 Vlogs（影音日誌） | `https://emogo-backend-athenalin11.onrender.com/export/vlogs` |
| 😊 Sentiments（情感資料） | `https://emogo-backend-athenalin11.onrender.com/export/sentiments` |
| 📍 GPS（座標資料） | `https://emogo-backend-athenalin11.onrender.com/export/gps` |

### 互動式 API 文件

**Swagger UI（可直接測試所有 API）:**
```
https://emogo-backend-athenalin11.onrender.com/docs
```

---

## 📊 資料模型說明

本系統收集並管理三種類型的使用者資料：

### 1. Vlogs（影音日誌）

記錄使用者的影音內容和日誌。

**資料結構:**
```json
{
  "user_id": "使用者 ID",
  "title": "日誌標題",
  "content": "文字內容",
  "video_url": "影片連結（選填）",
  "audio_url": "音訊連結（選填）",
  "timestamp": "時間戳記"
}
```

### 2. Sentiments（情感資料）

追蹤使用者的情緒狀態和感受。

**資料結構:**
```json
{
  "user_id": "使用者 ID",
  "emotion": "情緒類型（如：happy, sad, excited, neutral）",
  "score": "情緒分數（0-1 之間的浮點數）",
  "text": "情緒描述文字（選填）",
  "timestamp": "時間戳記"
}
```

### 3. GPS Coordinates（GPS 座標）

記錄使用者的地理位置資訊。

**資料結構:**
```json
{
  "user_id": "使用者 ID",
  "latitude": "緯度",
  "longitude": "經度",
  "accuracy": "精確度（選填）",
  "timestamp": "時間戳記"
}
```

---

## � 使用方法

### 快速開始

#### 1. 查看所有資料

在瀏覽器中訪問：
```
https://emogo-backend-athenalin11.onrender.com/export/all
```

#### 2. 使用互動式 API 文件

訪問 Swagger UI 測試所有端點：
```
https://emogo-backend-athenalin11.onrender.com/docs
```

在這裡您可以：
- 📖 查看所有 API 端點的詳細說明
- 🧪 直接在瀏覽器中測試 API
- 📝 查看請求和回應的 JSON 格式範例

### API 端點總覽

#### 系統端點
| 端點 | 方法 | 說明 |
|------|------|------|
| `/` | GET | API 首頁，顯示所有可用端點 |
| `/health` | GET | 健康檢查，確認資料庫連接狀態 |
| `/stats` | GET | 獲取資料庫統計資訊 |
| `/docs` | GET | Swagger UI 互動式文件 |

#### Vlogs（影音日誌）端點
| 端點 | 方法 | 說明 |
|------|------|------|
| `/vlogs` | POST | 新增一筆 vlog |
| `/vlogs` | GET | 取得所有 vlogs（可設定 limit） |
| `/vlogs/{user_id}` | GET | 取得特定使用者的 vlogs |
| `/export/vlogs` | GET | 匯出所有 vlog 資料 |

#### Sentiments（情感資料）端點
| 端點 | 方法 | 說明 |
|------|------|------|
| `/sentiments` | POST | 新增一筆情感資料 |
| `/sentiments` | GET | 取得所有情感資料 |
| `/sentiments/{user_id}` | GET | 取得特定使用者的情感資料 |
| `/export/sentiments` | GET | 匯出所有情感資料 |

#### GPS（座標）端點
| 端點 | 方法 | 說明 |
|------|------|------|
| `/gps` | POST | 新增一筆 GPS 座標 |
| `/gps` | GET | 取得所有 GPS 座標 |
| `/gps/{user_id}` | GET | 取得特定使用者的 GPS 座標 |
| `/export/gps` | GET | 匯出所有 GPS 座標 |

#### 資料匯出端點
| 端點 | 方法 | 說明 |
|------|------|------|
| `/export/all` | GET | **匯出所有三種類型的資料**（作業要求） |

### 使用範例

#### 範例 1: 新增 Vlog

**使用 curl:**
```bash
curl -X POST "https://emogo-backend-athenalin11.onrender.com/vlogs" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "title": "美好的一天",
    "content": "今天天氣很好！",
    "video_url": "https://example.com/video.mp4"
  }'
```

**使用 Python:**
```python
import requests

url = "https://emogo-backend-athenalin11.onrender.com/vlogs"
data = {
    "user_id": "user123",
    "title": "美好的一天",
    "content": "今天天氣很好！",
    "video_url": "https://example.com/video.mp4"
}

response = requests.post(url, json=data)
print(response.json())
```

**使用 JavaScript (fetch):**
```javascript
fetch('https://emogo-backend-athenalin11.onrender.com/vlogs', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    user_id: 'user123',
    title: '美好的一天',
    content: '今天天氣很好！',
    video_url: 'https://example.com/video.mp4'
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

#### 範例 2: 新增情感資料

**使用 curl:**
```bash
curl -X POST "https://emogo-backend-athenalin11.onrender.com/sentiments" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "emotion": "happy",
    "score": 0.85,
    "text": "心情很好！"
  }'
```

#### 範例 3: 新增 GPS 座標

**使用 curl:**
```bash
curl -X POST "https://emogo-backend-athenalin11.onrender.com/gps" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "user123",
    "latitude": 25.0330,
    "longitude": 121.5654,
    "accuracy": 10.5
  }'
```

#### 範例 4: 匯出所有資料

**使用 curl:**
```bash
curl "https://emogo-backend-athenalin11.onrender.com/export/all"
```

**使用瀏覽器:**
直接訪問 `https://emogo-backend-athenalin11.onrender.com/export/all`

**回應範例:**
```json
{
  "export_date": "2025-12-04T10:30:00",
  "total_records": 9,
  "vlogs": {
    "count": 3,
    "data": [...]
  },
  "sentiments": {
    "count": 3,
    "data": [...]
  },
  "gps_coordinates": {
    "count": 3,
    "data": [...]
  }
}
```

---

## 🛠️ 技術棧

### 後端框架
- **[FastAPI](https://fastapi.tiangolo.com/)** - 現代、高效能的 Python Web 框架
  - 自動生成 API 文件（Swagger UI）
  - 原生支援非同步程式設計（async/await）
  - 基於 Pydantic 的資料驗證
  - 型別提示和自動補全

### 資料庫
- **[MongoDB Atlas](https://www.mongodb.com/cloud/atlas)** - 雲端 NoSQL 資料庫
  - 靈活的文件式資料模型
  - 雲端託管，自動備份
  - 免費方案支援

- **[Motor](https://motor.readthedocs.io/)** - MongoDB 的非同步 Python 驅動程式
  - 與 FastAPI 的非同步特性完美配合
  - 高效能的資料庫操作

### 部署平台
- **[Render](https://render.com/)** - 現代化的雲端應用部署平台
  - 免費方案
  - 自動化部署（Git push 後自動更新）
  - HTTPS 支援

### 開發工具
- **Python 3.10+** - 程式語言
- **Uvicorn** - ASGI 伺服器
- **Pydantic** - 資料驗證和設定管理

---

## 📦 專案結構

```
emogo-backend-athenalin11/
├── main.py                 # FastAPI 主程式，包含所有 API 端點
├── requirements.txt        # Python 套件依賴
├── render.yaml            # Render 部署設定
├── README.md              # 專案說明文件（本檔案）
├── .env.example           # 環境變數範例
├── .gitignore             # Git 忽略檔案設定
├── sample_data.py         # 測試資料範例
├── QUICKSTART.md          # 快速入門指南
├── DEPLOYMENT_GUIDE.md    # 詳細部署指南
└── CHECKLIST.md           # 作業完成檢查清單
```

---

## 🔧 本地開發

### 環境需求
- Python 3.10 或更高版本
- MongoDB Atlas 帳號
- Git

### 安裝步驟

1. **Clone 此 repository**
```bash
git clone https://github.com/ntu-info/emogo-backend-athenalin11.git
cd emogo-backend-athenalin11
```

2. **安裝依賴套件**
```bash
pip install -r requirements.txt
```

3. **設定環境變數**

建立 `.env` 檔案：
```bash
cp .env.example .env
```

編輯 `.env`，填入您的 MongoDB 連接字串：
```
MONGODB_URI=mongodb+srv://你的帳號:你的密碼@cluster.mongodb.net/
```

4. **執行應用程式**
```bash
uvicorn main:app --reload
```

應用程式將在 `http://localhost:8000` 啟動。

5. **測試 API**

訪問 `http://localhost:8000/docs` 查看 API 文件並測試端點。

---

## 🌐 部署說明

本專案已部署至 Render，使用以下配置：

### 部署架構
```
GitHub Repository → Render (自動部署) → 運行中的 API
                                    ↓
                              MongoDB Atlas (雲端資料庫)
```

### 環境變數設定
在 Render 的環境變數中設定：
- `MONGODB_URI`: MongoDB Atlas 連接字串

### 部署指令
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

詳細部署步驟請參考 `DEPLOYMENT_GUIDE.md`。

---

## 💡 核心功能特色

### 1. 完整的 CRUD 操作
- ✅ Create（新增）: POST 端點用於新增各類資料
- ✅ Read（讀取）: GET 端點用於查詢資料
- ✅ 支援按使用者 ID 篩選
- ✅ 可設定查詢數量限制

### 2. 資料匯出功能
- 📤 支援完整資料匯出（所有類型）
- 📤 支援個別資料類型匯出
- 📊 自動統計資料筆數
- 🕒 記錄匯出時間

### 3. 健康監控
- 💚 資料庫連接狀態檢查
- 📈 即時統計資訊
- ⏱️ 時間戳記記錄

### 4. 開發者友善
- 📖 自動生成 API 文件（Swagger UI）
- 🧪 內建測試介面
- 🔍 詳細的錯誤訊息
- 📝 完整的資料驗證

---

## 📚 相關文件

- 📘 [快速入門指南](QUICKSTART.md) - 3 步驟完成部署
- 📗 [完整部署指南](DEPLOYMENT_GUIDE.md) - 詳細的部署步驟說明
- 📙 [檢查清單](CHECKLIST.md) - 作業完成檢查項目
- 📄 [測試資料範例](sample_data.py) - 範例資料結構

---

## ⚠️ 注意事項

### Render 免費方案限制
- ⏰ 15 分鐘無請求會自動休眠
- 🔄 休眠後首次訪問需等待約 30 秒喚醒
- 💾 每月 750 小時免費使用時間

### 資料庫安全
- 🔒 MongoDB URI 包含敏感資訊，已使用環境變數保護
- 🚫 請勿將真實的連接字串提交到 GitHub
- ✅ 本專案使用 `.gitignore` 排除 `.env` 檔案

### 時區說明
- 🌍 API 回傳的時間戳記使用 UTC 時間
- 🇹🇼 台灣時間 = UTC 時間 + 8 小時

---

## 🎓 學習成果

透過完成本專案，掌握了以下技能：

### 後端開發
- ✅ RESTful API 設計原則
- ✅ 非同步程式設計（async/await）
- ✅ 資料驗證和錯誤處理
- ✅ API 文件自動生成

### 資料庫操作
- ✅ NoSQL 資料庫設計
- ✅ MongoDB CRUD 操作
- ✅ 非同步資料庫驅動（Motor）
- ✅ 雲端資料庫管理（MongoDB Atlas）

### DevOps
- ✅ 雲端部署（Render）
- ✅ 環境變數管理
- ✅ 版本控制（Git/GitHub）
- ✅ CI/CD 基礎概念

### 軟體工程實踐
- ✅ 專案結構規劃
- ✅ 文件撰寫
- ✅ 程式碼組織
- ✅ 最佳實踐應用

---

## 🔗 相關連結

- 🌐 **Live API**: https://emogo-backend-athenalin11.onrender.com
- 📖 **API 文件**: https://emogo-backend-athenalin11.onrender.com/docs
- 📊 **資料匯出**: https://emogo-backend-athenalin11.onrender.com/export/all
- 💚 **健康檢查**: https://emogo-backend-athenalin11.onrender.com/health
- 📂 **GitHub**: https://github.com/ntu-info/emogo-backend-athenalin11

---

## 📄 授權

此專案為 NTU 資訊所課程作業專案。

---

## � 作者資訊

**學生**: athenalin11  
**課程**: NTU 資訊所  
**完成日期**: 2025/12/04

---

## 📞 支援

如有問題或建議，歡迎：
- 📧 透過 GitHub Issues 回報問題
- 💬 查看 API 文件了解詳細用法
- 📖 參考相關文件獲取更多資訊

---

**🎉 感謝使用 EmoGo Backend API！**
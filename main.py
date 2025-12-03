from typing import Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from datetime import datetime
import os
import json

# MongoDB 連接設定
# 請將此 URI 替換為您自己的 MongoDB Atlas URI
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb+srv://your_username:your_password@your_cluster.mongodb.net/")
DB_NAME = "emogo_db"  # 資料庫名稱

app = FastAPI(
    title="EmoGo Backend API",
    description="EmoGo 後端 API - 收集並管理 vlogs、情感資料和 GPS 座標",
    version="1.0.0"
)

# 資料模型定義
class Vlog(BaseModel):
    user_id: str
    title: Optional[str] = None
    content: str
    video_url: Optional[str] = None
    audio_url: Optional[str] = None
    timestamp: Optional[datetime] = None

class Sentiment(BaseModel):
    user_id: str
    emotion: str  # 例如: happy, sad, angry, neutral
    score: float  # 情感分數 0-1
    text: Optional[str] = None
    timestamp: Optional[datetime] = None

class GPSCoordinate(BaseModel):
    user_id: str
    latitude: float
    longitude: float
    accuracy: Optional[float] = None
    timestamp: Optional[datetime] = None

# MongoDB 連接事件
@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(MONGODB_URI)
    app.mongodb = app.mongodb_client[DB_NAME]
    print(f"Connected to MongoDB: {DB_NAME}")

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
    print("Disconnected from MongoDB")

# 基本路由
@app.get("/")
async def root():
    return {
        "message": "Welcome to EmoGo Backend API",
        "version": "1.0.0",
        "endpoints": {
            "docs": "/docs",
            "vlogs": "/vlogs",
            "sentiments": "/sentiments",
            "gps": "/gps",
            "export_all": "/export/all"
        }
    }

# === Vlog 相關 API ===
@app.post("/vlogs", status_code=201)
async def create_vlog(vlog: Vlog):
    """新增一筆 vlog 資料"""
    vlog_dict = vlog.dict()
    if vlog_dict.get("timestamp") is None:
        vlog_dict["timestamp"] = datetime.utcnow()
    
    result = await app.mongodb["vlogs"].insert_one(vlog_dict)
    vlog_dict["_id"] = str(result.inserted_id)
    return {"message": "Vlog created successfully", "id": str(result.inserted_id)}

@app.get("/vlogs")
async def get_vlogs(limit: int = 100):
    """取得所有 vlogs 資料"""
    vlogs = await app.mongodb["vlogs"].find().to_list(limit)
    for vlog in vlogs:
        vlog["_id"] = str(vlog["_id"])
    return {"count": len(vlogs), "data": vlogs}

@app.get("/vlogs/{user_id}")
async def get_vlogs_by_user(user_id: str, limit: int = 100):
    """根據 user_id 取得 vlogs"""
    vlogs = await app.mongodb["vlogs"].find({"user_id": user_id}).to_list(limit)
    for vlog in vlogs:
        vlog["_id"] = str(vlog["_id"])
    return {"count": len(vlogs), "data": vlogs}

# === Sentiment 相關 API ===
@app.post("/sentiments", status_code=201)
async def create_sentiment(sentiment: Sentiment):
    """新增一筆情感資料"""
    sentiment_dict = sentiment.dict()
    if sentiment_dict.get("timestamp") is None:
        sentiment_dict["timestamp"] = datetime.utcnow()
    
    result = await app.mongodb["sentiments"].insert_one(sentiment_dict)
    return {"message": "Sentiment created successfully", "id": str(result.inserted_id)}

@app.get("/sentiments")
async def get_sentiments(limit: int = 100):
    """取得所有情感資料"""
    sentiments = await app.mongodb["sentiments"].find().to_list(limit)
    for sentiment in sentiments:
        sentiment["_id"] = str(sentiment["_id"])
    return {"count": len(sentiments), "data": sentiments}

@app.get("/sentiments/{user_id}")
async def get_sentiments_by_user(user_id: str, limit: int = 100):
    """根據 user_id 取得情感資料"""
    sentiments = await app.mongodb["sentiments"].find({"user_id": user_id}).to_list(limit)
    for sentiment in sentiments:
        sentiment["_id"] = str(sentiment["_id"])
    return {"count": len(sentiments), "data": sentiments}

# === GPS 相關 API ===
@app.post("/gps", status_code=201)
async def create_gps_coordinate(gps: GPSCoordinate):
    """新增一筆 GPS 座標資料"""
    gps_dict = gps.dict()
    if gps_dict.get("timestamp") is None:
        gps_dict["timestamp"] = datetime.utcnow()
    
    result = await app.mongodb["gps_coordinates"].insert_one(gps_dict)
    return {"message": "GPS coordinate created successfully", "id": str(result.inserted_id)}

@app.get("/gps")
async def get_gps_coordinates(limit: int = 100):
    """取得所有 GPS 座標資料"""
    coordinates = await app.mongodb["gps_coordinates"].find().to_list(limit)
    for coord in coordinates:
        coord["_id"] = str(coord["_id"])
    return {"count": len(coordinates), "data": coordinates}

@app.get("/gps/{user_id}")
async def get_gps_by_user(user_id: str, limit: int = 100):
    """根據 user_id 取得 GPS 座標"""
    coordinates = await app.mongodb["gps_coordinates"].find({"user_id": user_id}).to_list(limit)
    for coord in coordinates:
        coord["_id"] = str(coord["_id"])
    return {"count": len(coordinates), "data": coordinates}

# === 資料匯出 API（作業要求的核心功能）===
@app.get("/export/all")
async def export_all_data():
    """
    匯出所有三種類型的資料（vlogs, sentiments, GPS coordinates）
    這是作業要求的主要 endpoint
    """
    # 取得所有資料
    vlogs = await app.mongodb["vlogs"].find().to_list(1000)
    sentiments = await app.mongodb["sentiments"].find().to_list(1000)
    gps_coordinates = await app.mongodb["gps_coordinates"].find().to_list(1000)
    
    # 轉換 ObjectId 為字串
    for vlog in vlogs:
        vlog["_id"] = str(vlog["_id"])
        if "timestamp" in vlog and vlog["timestamp"]:
            vlog["timestamp"] = vlog["timestamp"].isoformat()
    
    for sentiment in sentiments:
        sentiment["_id"] = str(sentiment["_id"])
        if "timestamp" in sentiment and sentiment["timestamp"]:
            sentiment["timestamp"] = sentiment["timestamp"].isoformat()
    
    for coord in gps_coordinates:
        coord["_id"] = str(coord["_id"])
        if "timestamp" in coord and coord["timestamp"]:
            coord["timestamp"] = coord["timestamp"].isoformat()
    
    return {
        "export_date": datetime.utcnow().isoformat(),
        "total_records": len(vlogs) + len(sentiments) + len(gps_coordinates),
        "vlogs": {
            "count": len(vlogs),
            "data": vlogs
        },
        "sentiments": {
            "count": len(sentiments),
            "data": sentiments
        },
        "gps_coordinates": {
            "count": len(gps_coordinates),
            "data": gps_coordinates
        }
    }

@app.get("/export/vlogs")
async def export_vlogs():
    """僅匯出 vlogs 資料"""
    vlogs = await app.mongodb["vlogs"].find().to_list(1000)
    for vlog in vlogs:
        vlog["_id"] = str(vlog["_id"])
        if "timestamp" in vlog and vlog["timestamp"]:
            vlog["timestamp"] = vlog["timestamp"].isoformat()
    return {"count": len(vlogs), "data": vlogs}

@app.get("/export/sentiments")
async def export_sentiments():
    """僅匯出情感資料"""
    sentiments = await app.mongodb["sentiments"].find().to_list(1000)
    for sentiment in sentiments:
        sentiment["_id"] = str(sentiment["_id"])
        if "timestamp" in sentiment and sentiment["timestamp"]:
            sentiment["timestamp"] = sentiment["timestamp"].isoformat()
    return {"count": len(sentiments), "data": sentiments}

@app.get("/export/gps")
async def export_gps():
    """僅匯出 GPS 座標資料"""
    coordinates = await app.mongodb["gps_coordinates"].find().to_list(1000)
    for coord in coordinates:
        coord["_id"] = str(coord["_id"])
        if "timestamp" in coord and coord["timestamp"]:
            coord["timestamp"] = coord["timestamp"].isoformat()
    return {"count": len(coordinates), "data": coordinates}

# === 統計資料 API ===
@app.get("/stats")
async def get_statistics():
    """取得資料庫統計資訊"""
    vlog_count = await app.mongodb["vlogs"].count_documents({})
    sentiment_count = await app.mongodb["sentiments"].count_documents({})
    gps_count = await app.mongodb["gps_coordinates"].count_documents({})
    
    return {
        "total_vlogs": vlog_count,
        "total_sentiments": sentiment_count,
        "total_gps_coordinates": gps_count,
        "total_records": vlog_count + sentiment_count + gps_count
    }

# === 健康檢查 API ===
@app.get("/health")
async def health_check():
    """檢查服務狀態"""
    try:
        # 測試資料庫連接
        await app.mongodb.command("ping")
        return {
            "status": "healthy",
            "database": "connected",
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }
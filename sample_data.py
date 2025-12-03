"""
測試資料範例
您可以在 MongoDB Compass 中使用這些 JSON 資料來建立測試資料
"""

# === Vlogs 測試資料 ===
vlogs_sample = [
    {
        "user_id": "user001",
        "title": "美好的一天",
        "content": "今天去了台北101，心情很好！",
        "video_url": "https://example.com/videos/taipei101.mp4",
        "timestamp": "2025-12-01T10:00:00Z"
    },
    {
        "user_id": "user001",
        "title": "咖啡廳時光",
        "content": "在咖啡廳工作，很放鬆",
        "audio_url": "https://example.com/audios/coffee.mp3",
        "timestamp": "2025-12-01T14:30:00Z"
    },
    {
        "user_id": "user002",
        "title": "晨跑記錄",
        "content": "今天早上跑了5公里",
        "video_url": "https://example.com/videos/morning_run.mp4",
        "timestamp": "2025-12-01T06:00:00Z"
    }
]

# === Sentiments 測試資料 ===
sentiments_sample = [
    {
        "user_id": "user001",
        "emotion": "happy",
        "score": 0.85,
        "text": "今天天氣真好，心情很棒！",
        "timestamp": "2025-12-01T10:30:00Z"
    },
    {
        "user_id": "user001",
        "emotion": "neutral",
        "score": 0.50,
        "text": "平靜的一天",
        "timestamp": "2025-12-01T15:00:00Z"
    },
    {
        "user_id": "user002",
        "emotion": "excited",
        "score": 0.92,
        "text": "剛完成馬拉松，超興奮！",
        "timestamp": "2025-12-01T08:30:00Z"
    },
    {
        "user_id": "user002",
        "emotion": "tired",
        "score": 0.35,
        "text": "有點累了",
        "timestamp": "2025-12-01T20:00:00Z"
    }
]

# === GPS Coordinates 測試資料 ===
gps_sample = [
    {
        "user_id": "user001",
        "latitude": 25.0330,
        "longitude": 121.5654,
        "accuracy": 10.5,
        "timestamp": "2025-12-01T10:00:00Z"
    },
    {
        "user_id": "user001",
        "latitude": 25.0340,
        "longitude": 121.5644,
        "accuracy": 8.2,
        "timestamp": "2025-12-01T14:30:00Z"
    },
    {
        "user_id": "user002",
        "latitude": 25.0420,
        "longitude": 121.5580,
        "accuracy": 12.0,
        "timestamp": "2025-12-01T06:00:00Z"
    },
    {
        "user_id": "user002",
        "latitude": 25.0435,
        "longitude": 121.5595,
        "accuracy": 9.5,
        "timestamp": "2025-12-01T08:30:00Z"
    }
]

if __name__ == "__main__":
    import json
    
    print("=== Vlogs 測試資料 ===")
    print(json.dumps(vlogs_sample, indent=2, ensure_ascii=False))
    print("\n=== Sentiments 測試資料 ===")
    print(json.dumps(sentiments_sample, indent=2, ensure_ascii=False))
    print("\n=== GPS Coordinates 測試資料 ===")
    print(json.dumps(gps_sample, indent=2, ensure_ascii=False))

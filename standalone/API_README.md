# YTConverter API

REST API 介面，可透過 HTTP 請求使用 YTConverter 功能。

## 安裝

```bash
pip install flask
```

## 啟動 API 伺服器

```bash
python api.py
```

伺服器將在 `http://localhost:5000` 啟動。

## API 端點

### 1. 下載影片/音訊

**端點:** `POST /download`

**請求範例:**
```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "format": "mp3",
  "destination": "C:/Users/Han/Downloads/audio"
}
```

**參數:**
- `url` (必填): YouTube 影片網址
- `format` (選填): 輸出格式 `mp3` 或 `mp4`，預設為 `mp3`
- `destination` (選填): 下載路徑，不指定則使用預設路徑

**回應範例:**
```json
{
  "status": "success",
  "message": "MP3 downloaded successfully",
  "destination": "C:/Users/Han/Downloads/audio"
}
```

### 2. 取得影片資訊

**端點:** `POST /info`

**請求範例:**
```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID"
}
```

**回應範例:**
```json
{
  "title": "影片標題",
  "duration": 180,
  "uploader": "頻道名稱",
  "thumbnail": "https://..."
}
```

### 3. 健康檢查

**端點:** `GET /health`

**回應範例:**
```json
{
  "status": "ok"
}
```

## 使用範例

### Python
```python
import requests

# 下載 MP3
response = requests.post('http://localhost:5000/download', json={
    'url': 'https://www.youtube.com/watch?v=VIDEO_ID',
    'format': 'mp3'
})
print(response.json())

# 取得影片資訊
response = requests.post('http://localhost:5000/info', json={
    'url': 'https://www.youtube.com/watch?v=VIDEO_ID'
})
print(response.json())
```

### cURL
```bash
# 下載 MP3
curl -X POST http://localhost:5000/download \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.youtube.com/watch?v=VIDEO_ID","format":"mp3"}'

# 取得影片資訊
curl -X POST http://localhost:5000/info \
  -H "Content-Type: application/json" \
  -d '{"url":"https://www.youtube.com/watch?v=VIDEO_ID"}'
```

### JavaScript (fetch)
```javascript
// 下載 MP3
fetch('http://localhost:5000/download', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    url: 'https://www.youtube.com/watch?v=VIDEO_ID',
    format: 'mp3'
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

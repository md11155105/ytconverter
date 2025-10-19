import requests

# 測試健康檢查
print("Testing health check...")
response = requests.get('http://localhost:5000/health')
print(response.json())

# 測試下載
print("\nTesting download...")
response = requests.post('http://localhost:5000/download', json={
    'url': 'https://www.youtube.com/watch?v=BD2YOIWYhXY',
    'format': 'mp3'
})
print(response.json())

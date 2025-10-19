from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import os
import sys
import subprocess as s
from pathlib import Path
import platform
import re
import yt_dlp
import json

app = Flask(__name__)

# Swagger UI 配置
SWAGGER_URL = '/api/docs'
API_URL = '/api/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "YTConverter API"}
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

def is_android():
    return (
        "ANDROID_ROOT" in os.environ
        or "TERMUX_VERSION" in os.environ
        or "com.termux" in os.getenv("HOME", "")
    )

def get_default_path(format_type):
    system = platform.system()
    home = Path.home()
    
    if system == "Windows":
        base_download = home / "Downloads"
    elif system == "Darwin":
        base_download = home / "Downloads"
    elif is_android():
        base_download = Path("/storage/emulated/0/Download")
    else:
        base_download = home / "Downloads"
    
    if format_type == "mp3":
        destination = base_download / "audio"
    else:
        destination = base_download / "videos"
    
    destination.mkdir(parents=True, exist_ok=True)
    return str(destination)

@app.route('/download', methods=['POST'])
def download():
    data = request.json
    url = data.get('url')
    format_type = data.get('format', 'mp3')
    destination = data.get('destination')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    url_pattern = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/.+$")
    if not url_pattern.match(url):
        return jsonify({'error': 'Invalid YouTube URL'}), 400
    
    if not destination:
        destination = get_default_path(format_type)
    
    try:
        if format_type == 'mp3':
            s.call([
                sys.executable, "-m", "yt_dlp",
                "-f", "bestaudio/best",
                "-x", "--audio-format", "mp3",
                "-o", os.path.join(destination, "%(title)s.%(ext)s"),
                url
            ])
        else:
            ydl_opts = {
                "format": "bestvideo+bestaudio/best",
                "outtmpl": os.path.join(destination, "%(title)s.%(ext)s"),
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        
        return jsonify({
            'status': 'success',
            'message': f'{format_type.upper()} downloaded successfully',
            'destination': destination
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/info', methods=['POST'])
def get_info():
    data = request.json
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    try:
        ydl_opts = {'quiet': True, 'no_warnings': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({
                'title': info.get('title'),
                'duration': info.get('duration'),
                'uploader': info.get('uploader'),
                'thumbnail': info.get('thumbnail')
            }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/api/swagger.json')
def swagger_spec():
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "YTConverter API",
            "description": "YouTube 影片/音訊下載 API",
            "version": "1.0.0"
        },
        "servers": [{"url": "http://localhost:5000"}],
        "paths": {
            "/download": {
                "post": {
                    "summary": "下載 YouTube 影片或音訊",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "required": ["url"],
                                    "properties": {
                                        "url": {"type": "string", "example": "https://www.youtube.com/watch?v=VIDEO_ID"},
                                        "format": {"type": "string", "enum": ["mp3", "mp4"], "default": "mp3"},
                                        "destination": {"type": "string", "example": "C:/Users/Han/Downloads/audio"}
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "下載成功",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "status": {"type": "string"},
                                            "message": {"type": "string"},
                                            "destination": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        },
                        "400": {"description": "請求錯誤"},
                        "500": {"description": "伺服器錯誤"}
                    }
                }
            },
            "/info": {
                "post": {
                    "summary": "取得 YouTube 影片資訊",
                    "requestBody": {
                        "required": True,
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "required": ["url"],
                                    "properties": {
                                        "url": {"type": "string", "example": "https://www.youtube.com/watch?v=VIDEO_ID"}
                                    }
                                }
                            }
                        }
                    },
                    "responses": {
                        "200": {
                            "description": "成功取得資訊",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "title": {"type": "string"},
                                            "duration": {"type": "integer"},
                                            "uploader": {"type": "string"},
                                            "thumbnail": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        },
                        "400": {"description": "請求錯誤"},
                        "500": {"description": "伺服器錯誤"}
                    }
                }
            },
            "/health": {
                "get": {
                    "summary": "健康檢查",
                    "responses": {
                        "200": {
                            "description": "服務正常",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {
                                            "status": {"type": "string"}
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return jsonify(spec)

@app.route('/')
def index():
    return jsonify({
        'message': 'YTConverter API',
        'docs': 'http://localhost:5000/api/docs'
    })

if __name__ == '__main__':
    print("\n" + "="*50)
    print("YTConverter API 已啟動")
    print("Swagger UI: http://localhost:5000/api/docs")
    print("="*50 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)

import os
from pathlib import Path

import requests
from dotenv import load_dotenv


load_dotenv(Path(__file__).with_name(".env"))

base_url = os.getenv("OLLAMA_BASE_URL", "").strip().rstrip("/")

if not base_url:
    raise SystemExit("Chưa điền OLLAMA_BASE_URL trong .env.")

try:
    response = requests.get(
        f"{base_url}/api/tags",
        timeout=30
    )
    response.raise_for_status()

    models = response.json()["models"]

    print("Kết nối thành công!")
    for model in models:
        print("-", model["name"])

except requests.RequestException as error:
    print("Loại lỗi:", type(error).__name__)

    if error.response is not None:
        print("HTTP:", error.response.status_code)
        print("Nội dung:", error.response.text[:500])
    else:
        print("Không nhận được phản hồi HTTP từ server.")

except (ValueError, KeyError):
    print("Server không trả về danh sách mô hình đúng định dạng.")
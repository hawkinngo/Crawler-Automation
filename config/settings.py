import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# CẤU HÌNH KẾT NỐI
# Cấu hình tới Brain
BRAIN_IP = os.getenv("BRAIN_IP", "10.10.86.50")

# Model AI sử dụng
AI_MODEL_NAME = "llama3.1"


# CẤU HÌNH ĐƯỜNG DẪN
# Cấu hình đường dẫn
BASE_DIR = Path(__file__).resolve().parent.parent

# Path Scripts: chỗ chứa script do AI viết ra (sẽ được tái sử dụng)
SCRIPTS_DIR = BASE_DIR / "sandbox" / "generated_scripts"

# Nơi chứa data tạm thời
TEMP_DIR = BASE_DIR / "sandbox" / "temp_execution"

# Tự động tạo thư mục nếu chưa có
SCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)


# CẤU HÌNH CRAWLER
# Giả lập trình duyệt Chrome
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

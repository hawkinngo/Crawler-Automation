Crawler-Automation/
│
├── .env                        # Chứa IP Workstation, DB User/Pass (MẬT)
├── .gitignore                  # Chặn file rác, file .env
├── requirements.txt            # Các thư viện: ollama, playwright, duckduckgo...
├── main_app.py                 # File chạy UI (Streamlit) cho người dùng nhập
│
├── config/                     # Cấu hình hệ thống
│   ├── settings.py             # Load biến môi trường, check path
│   └── prompts.py              # (QUAN TRỌNG) Chứa các câu "thần chú" dạy AI
│
├── core/                       # Các module chức năng cốt lõi
│   ├── infrastructure.py       # Quản lý Wake-on-LAN, check sức khỏe Server
│   ├── llm_engine.py           # Hàm giao tiếp với Llama 3.1 (Gửi/Nhận)
│   ├── db_client.py            # Hàm lưu data vào Mongo, lưu log vào Qdrant
│   └── discovery.py            # Hàm dùng DuckDuckGo tìm nguồn web
│
├── agents/                     # Các "nhân viên" AI cụ thể
│   ├── architect_agent.py      # Phân tích HTML -> Tạo Schema JSON
│   ├── coder_agent.py          # Viết code Playwright -> Tự sửa lỗi (Self-heal)
│   └── review_agent.py         # (Tương lai) Đánh giá xem data crawl về có rác không
│
├── sandbox/                    # "Công trường" - Nơi code được sinh ra và chạy
│   ├── generated_scripts/      # Chứa các file .py AI viết xong (lưu lại dùng sau)
│   ├── temp_execution/         # Nơi chạy file tạm (viết xong, chạy, xóa)
│   └── logs/                   # Log lỗi để AI đọc và sửa
│
└── utils/                      # Các hàm tiện ích
    ├── html_cleaner.py         # Rút gọn HTML trước khi gửi cho AI (đỡ tốn token)
    └── text_parser.py          # Chuẩn hóa giá tiền "3 tỷ" -> 3000000000
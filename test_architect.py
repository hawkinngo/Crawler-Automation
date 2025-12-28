# test_architect.py
from core.infrastructure import InfrastructureManager
from agents.architect_agent import ArchitectAgent

def test_blueprint():
    # 1. Đánh thức Server
    infra = InfrastructureManager()
    if not infra.wake_up_brain():
        return

    # 2. Khởi tạo Architect
    architect = ArchitectAgent()
    
    # 3. Chọn 1 link thực tế (Lấy từ kết quả Discovery hồi nãy hoặc link này test cho dễ)
    # Ví dụ trang tin tức hoặc trang bán hàng đơn giản
    test_url = "https://hoanglongcomputer.vn/may-tinh-van-phong-moi-core-i5-4570-ram-8g-ssd-250g" 
    intent = "Lấy dùm tiêu đề, giá bán, và link của sản phẩm"

    # 4. Chạy phân tích
    schema = architect.analyze_website(test_url, intent)
    
    if schema:
        print("\n🎉 THÀNH CÔNG! Đã có bản thiết kế để đưa cho thợ Code.")
        # Lưu lại file json để bước sau dùng
        import json
        with open("blueprint.json", "w") as f:
            json.dump(schema, f)
    else:
        print("\n😭 THẤT BẠI. Architect không nhìn ra cấu trúc.")

if __name__ == "__main__":
    test_blueprint()
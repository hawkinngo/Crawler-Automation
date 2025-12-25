# core/infrastructure.py
import os
import time
import socket
import paramiko
from dotenv import load_dotenv

# Load biến từ file .env
load_dotenv()

class InfrastructureManager:
    def __init__(self):
        self.ws_ip = os.getenv("WORKSTATION_IP")
        self.ws_mac = os.getenv("WORKSTATION_MAC")
        self.ws_port = int(os.getenv("WORKSTATION_CHECK_PORT", 22))
        
        self.mini_ip = os.getenv("MINI_PC_IP")
        self.mini_user = os.getenv("MINI_PC_USER")
        self.mini_pass = os.getenv("MINI_PC_PASS")

    def is_brain_online(self):
        """Kiểm tra xem Workstation có đang mở mắt (mở cổng) không"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1) # Check nhanh trong 1s
            result = sock.connect_ex((self.ws_ip, self.ws_port))
            sock.close()
            return result == 0
        except:
            return False

    def wake_up_brain(self):
        """Quy trình gọi dậy: Laptop -> SSH MiniPC -> WOL Workstation"""
        if self.is_brain_online():
            print("⚡ BRAIN (Workstation) đang Online. Sẵn sàng!")
            return True

        print(f"💤 BRAIN đang ngủ tại {self.ws_ip}. Đang kết nối Mini PC để kích hoạt...")
        
        try:
            # 1. SSH vào Mini PC
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.mini_ip, username=self.mini_user, password=self.mini_pass)
            
            # 2. Gửi lệnh Magic Packet từ Mini PC
            # Lưu ý: Mini PC phải cài sẵn: apt install wakeonlan
            cmd = f"wakeonlan {self.ws_mac}"
            stdin, stdout, stderr = ssh.exec_command(cmd)
            
            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            
            ssh.close()

            if "Sending magic packet" in output or not error:
                print(f"📡 Đã bắn tín hiệu WoL: {output}")
            else:
                print(f"❌ Lỗi gửi WoL: {error}")
                return False

            # 3. Chờ Workstation tỉnh dậy
            print("⏳ Đang chờ hệ thống khởi động (Timeout 90s)...")
            # Loop check mỗi 2s, tối đa 45 lần (90s)
            for i in range(45):
                if self.is_brain_online():
                    print("\n🚀 BRAIN ĐÃ TỈNH DẬY! Kết nối thành công.")
                    time.sleep(5) # Chờ thêm 5s cho service Ollama kịp load model
                    return True
                print(".", end="", flush=True)
                time.sleep(2)
            
            print("\n❌ Thất bại: Workstation không phản hồi sau 90s.")
            return False

        except Exception as e:
            print(f"\n❌ Lỗi nghiêm trọng trong quá trình Wake-on-LAN: {e}")
            return False
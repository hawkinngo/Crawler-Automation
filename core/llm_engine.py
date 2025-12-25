import re
import ollama
from config.settings import BRAIN_IP, AI_MODEL_NAME


class LLMEngine:
    def __init__(self):
        self.client = ollama.Client(host=f'http://{BRAIN_IP}:11434')
        self.model = AI_MODEL_NAME

    def generate_code(self, prompt, system_instruction=None):
        """
        Gửi yêu cầu viết code cho AI và nhận về code sạch.
        """
        messages = []

        # 1. Thêm vai trò (System Prompt) nếu có
        if system_instruction:
            messages.append({
                "role": "system",
                "content": system_instruction
            })

        # 2. Thêm yêu cầu người dùng
        messages.append({
            "role": "user",
            "content": prompt
        })

        print(f"🤖 Brain ({self.model}) đang suy nghĩ...")

        try:
            # 3. Gọi API
            response = self.client.chat(model=self.model, messages=messages)
            raw_content = response["message"]["content"]

            # 4. Làm sạch code (Extract Code Block)
            clean_code = self._extract_code_block(raw_content)
            return clean_code

        except Exception as e:
            print(f"❌ Lỗi kết nối Ollama: {e}")
            return None

    def _extract_code_block(self, text):
        """
        Hàm phụ trợ: Lọc lấy phần code nằm giữa ```python và ```
        """
        # Regex tìm đoạn văn bản nằm giữa ```python ... ``` hoặc ``` ... ```
        pattern = r"```(?:python)?\n(.*?)```"
        match = re.search(pattern, text, re.DOTALL)

        if match:
            return match.group(1).strip()
        else:
            return text.strip()


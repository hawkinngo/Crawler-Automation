import json
from playwright.sync_api import sync_playwright
from core.llm_engine import LLMEngine
from utils.html_parser import clean_html_for_ai
from config.settings import USER_AGENT


class ArchitectAgent:
    def __init__(self):
        self.brain = LLMEngine()

    def analyze_website(self, url, user_intent):
        """
        Vào trang web -> Lấy HTML -> Nhờ AI đoán CSS Selectors
        """
        print(f"🏗️  Architect đang khảo sát địa hình: {url}")

        # 1. Lấy HTML bằng Playwright
        raw_html = ""
        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(
                    headless=True,
                    args=["--no-sandbox", "--disable-setuid-sandbox"],
                )
                page = browser.new_page(user_agent=USER_AGENT)
                page.goto(url, timeout=30000)
                page.wait_for_load_state("networkidle")  # Chờ web load xong
                raw_html = page.content()
                browser.close()
        except Exception as e:
            print(f"Lỗi tải trang web: ", e)
            return None

        # 2. Làm sạch HTML
        clean_html = clean_html_for_ai(raw_html=raw_html)
        print(
            f"🧹 Đã làm sạch HTML. Kích thước gốc: {len(raw_html)} -> Còn lại: {len(clean_html)}"
        )

        # 3. Soạn "Thần chú" (Prompt) cho AI
        prompt = f"""
        I have a clean HTML of a website. My goal is: "{user_intent}".
        Please analyze the HTML below and identify the CSS Selectors to extract data.
        
        HTML CONTENT:
        ```html
        {clean_html}
        ```
        
        REQUIREMENT:
        Return a JSON object (NO EXPLANATION) with this structure:
        {{
            "container_selector": "The CSS selector for the main wrapper of EACH item (e.g., .product-item, .card)",
            "fields": {{
                "title": "CSS selector for the title text",
                "price": "CSS selector for the price text",
                "link": "CSS selector for the <a> tag link"
            }}
        }}
        """

        # 4. Gửi cho não bộ
        system_instruction = (
            "You are an expert Web Scraper. You only output valid JSON."
        )
        response = self.brain.generate_code(prompt, system_instruction)

        # 5. Parse kết quả trả về
        try:
            if response:
                schema = json.loads(response)
                print("✅ Architect đã vẽ xong bản đồ (Schema):")
                print(json.dumps(schema, indent=2))
                return schema
        except json.JSONDecodeError:
            print("❌ AI trả về định dạng không phải JSON chuẩn. Raw:", response)
            return None

        return None

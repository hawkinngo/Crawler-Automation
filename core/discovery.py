from ddgs import DDGS
import time

class DiscoveryEngine:
    def __init__(self, max_results=5):
        self.max_results = max_results
        self.ddgs = DDGS()


    def search_internet(self, query, verify_ssl=True):
        """
        Tìm kiếm trên DuckDuckGo và trả về danh sách URL sạch.
        """
        print(f"🕵️  Đang quét Internet với từ khóa: '{query}'...")

        results = []
        try:
            # "-filetype:pdf" loại bỏ file tài liệu khó đọc
            refined_query = f"{query} -filetype:pdf -site:google.com"

            # Thực hiện search
            ddg_results = self.ddgs.text(refined_query, max_results=self.max_results)

            if not ddg_results:
                print("Không tìm thấy kết quả")
                return []

            # Format lại kết quả
            for res in ddg_results:
                results.append({
                    "title": res.get("title", "No Title"),
                    "url": res.get("href", ""),
                    "snippet": res.get("body", "")
                })

            print(f"Đã tìm thấy {len(results)} nguồn dữ liệu tiềm năng")
            return results
        except Exception as e:
            print(f"❌ Lỗi khi tìm kiếm: {e}")
            return []


    def simple_filter(self, results, must_contain_words=[]):
        """
        Hàm lọc phụ: Chỉ lấy các trang có chứa từ khóa nhất định trong URL hoặc Title
        Ví dụ: must_contain_words=['mua-ban', 'gia']
        """
        if not must_contain_words:
            return results


        filtered = []
        for res in results:
            text_to_check = (res["title"] + res["url"]).lower()

            # Nếu chưa ít nhát 1 từ khóa trong danh sách
            if any(word in text_to_check for word in must_contain_words):
                filtered.append(res)

        return filtered
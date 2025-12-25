from core.discovery import DiscoveryEngine
from core.llm_engine import LLMEngine

def test_discovery():
    finder = DiscoveryEngine(max_results=2)

    find_text = "Giá cà phê hôm nay thế nào"

    urls = finder.search_internet(find_text)


    # 4. In kết quả
    print("\n--- KẾT QUẢ TÌM KIẾM ---")
    for idx, item in enumerate(urls, 1):
        print(f"{idx}. {item['title']}")
        print(f"   Link: {item['url']}")
        print(f"   Mô tả: {item['snippet'][:100]}...") # In 100 ký tự đầu
        print("-" * 30)


if __name__ == "__main__":
    test_discovery()
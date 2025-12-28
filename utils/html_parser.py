from bs4 import BeautifulSoup, Comment


def clean_html_for_ai(raw_html):
    """
    Rút gọn HTML: Chỉ giữ lại cấu trúc thẻ và nội dung quan trọng.
    Loại bỏ JS, CSS, Comment để giảm tải cho AI.
    """
    soup = BeautifulSoup(raw_html, "lxml")

    # 1. Loại bỏ các thẻ không cần thiết (Rác)
    for tag in soup(['script', 'style', 'svg', 'noscript', 'iframe', 'footer', 'header']):
        tag.decompose()


    # 2. Loại bỏ comments
    for comment in soup.find_all(text=lambda text: isinstance(text, Comment)):
        comment.extract()


    # 3. Loại bỏ các thuộc tính (attributes) rườm rà, chỉ giữ lại class và id
    # (Vì Playwright chủ yếu dùng class/id để select)
    for tag in soup.find_all(True):
        allowed_attrs = ['class', 'id', 'href']
        attrs = dict(tag.attrs)
        for attr in attrs:
            if attr not in allowed_attrs:
                del tag[attr]

    
    # 4. Trả về HTML gọn nhẹ (Pretty print)
    # Giới hạn ký tự nếu cần (Llama 3.1 context window khoảng 8k-128k tùy bản)
    clean_text = soup.prettify()


    # Cắt bớt nếu quá dài (để test nhanh), lấy 1500 dòng đầu tiên
    lines = clean_text.split('\n')
    return '\n'.join(lines[:1500])
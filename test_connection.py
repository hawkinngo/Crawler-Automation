from core.infrastructure import InfrastructureManager
from core.llm_engine import LLMEngine

def test_system():
    # Gọi AI dậy
    infra = InfrastructureManager()
    if not infra.wake_up_brain():
        print("❌ Server không dậy. Dừng cuộc chơi.")
        return

    # 2.Kết nối vơi WS
    brain = LLMEngine()

    # 3. Thử làm việc với AI
    prompt = "Viết một hàm Python tính dãy số Fibonacci thứ n."
    system_instruction = "You are a senior python developer. Only output python code, no explanation."

    code = brain.generate_code(prompt=prompt, system_instruction=system_instruction)

    if code:
        print("\n✅ KẾT QUẢ THÀNH CÔNG! Code AI viết ra là:")
        print("-" * 40)
        print(code)
        print("-" * 40)
    else:
        print("❌ AI không trả lời.")


if __name__ == "__main__":
    test_system()
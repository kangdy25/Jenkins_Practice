def add(a, b):
    return a + b

if __name__ == "__main__":
    result = add(10, 20)
    print(f"계산 결과: 10 + 20 = {result}")
    assert result == 30, "테스트 실패 ㅜㅜ"
    print("✅ 애플리케이션 실행 및 자체 테스트 통과! 가보자잇!!!")
# 예외 처리(exception 클래스)
try:
    x = int(input("숫자를 입력하세요 : "))
    print(x)
except ValueError:      # ValueError as e: 생략 가능
    print("유효한 숫자가 아닙니다. 유효한 숫자를 입력하세요.")
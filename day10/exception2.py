# 다중 try ~ except 구문

try:
    data = [50, 30, 70, 90]
    # print(data[0])
    # print(data[4])

    x = int(input("정수를 입력하세요(0~3까지) : "))
    print(data[x])
except IndexError:      #as e: 생략 가능
    print("0~3까지 입력하세요.")
except ValueError:
    print("숫자가 아닙니다. 정수를 입력하세요.")
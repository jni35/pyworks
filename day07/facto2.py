# 1부터 n까지 곱하기 - 재귀함수
def facto(n):
    if n <= 1:      # 최종값(마지막값)
        return 1
    else:
        return n*facto(n-1)     # 마지막보다 큰 값

print(facto(1))     # 1
print(facto(2))     # 2 x facto(2)
print(facto(3))     # 3 x facto(2)
print(facto(5))     # 5 x facto(4)
print(facto(10))    # 10 x facto(9)


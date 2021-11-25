# 거듭제곱 함수 만들기
def my_pow(x,y):    #x:밑, y:지수, 2의 4제곱 = 2x2x2x2
    num = 1 #곱하기 초기화는 1
    for i in range(y):
        num *= x
    return num

print(my_pow(2, 4))     #호출
print(pow(2, 4))        #내장 함수

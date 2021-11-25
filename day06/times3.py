# 1~100까지의 수 중에서 배수 출력

def times(x):
    # 배수 계산하기
    global count    # 전역변수임을 표시
    for i in range(1, 101):
        if i % x == 0:
            count += 1
            print(i, end=' ')
            # print(count)
count = 0
times(3)
print("\n3의 배수의 개수 : "+str(count)+"개")


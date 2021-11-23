#중첩 for문

# 5행 5열 문자 출력
for i in range(0,5):
    for j in range(0,5):
        print("$", end=" ")
    print()

# 직각 삼각형  출력
for i in range(0,5):
    for j in range(0,i+1):
        print("$", end=" ")
    print()

# 역직각 삼각형  출력
for i in range(0,5):
    for j in range(0,5-i):
        print("$", end=" ")
    print()

# 5행 5열안에 1부터 순차적으로 증가하기
for i in range(0, 5):
    for j in range(1, 6):
        num = i*5+j
        print(num, end=" ")
    print()


# 0*5+1 = 1,2,3,4,5
# 1*5+1 = 6,7,8,9,10
# 2*5+1 = 11,12,13,14,15

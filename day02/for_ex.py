#반복문 - for
#1부터 5까지 출력

for i in (1, 2, 3, 4, 5):
    print(i, end=" ")

print()

for i in range(1,6,1):  #range(초기값, 종료값-1,증가값)
    print(i, end=" ")

print()

#1부터 10까지의 홀수 출력
for i in range(1,11):
    #홀수 처리
    if i % 2 == 1:
        print(i, end=" ")

print()

#1부터 10까지의 합계 출력
sum_v = 0
for i in range(1,11):
    sum_v += i
    print("i = ", i, ",sum_v = ", sum_v)

print("sum = ", sum_v)


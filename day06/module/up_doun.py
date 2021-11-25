#
import random

com = random.randint(1, 100)
min_v = 1
max_v = 100
for i in range(10):
    # 사용자가 추측한 숫자
    guess = int(input("맞혀 보세요([%d회] %d~%d) ->" % (i+1, min_v, max_v)))
    if guess == com:
        print("정답!!")
        break
    elif guess > com:
        print("너무 커요!")
        max_v = guess
    else:
        print("너무 작아요!")
        min_v = guess

print("정답 : %d" % com)
print("점수 : %d점" % ((10 - i)*10))  #점수 = 남은 회수 * 10

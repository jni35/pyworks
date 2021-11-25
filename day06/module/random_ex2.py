# random 모듈 사용하기
import random
# 주사위 10번 던지기

# for x in range(10):
#     dice = random.randint(1,6)
#     print(dice)

# 주사위 2개 만들어서 눈의 수가 같으면 "double!!" 출력
for x in range(10):
    dice1= random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print(total)
    if dice1 == dice2:
        print("Doulble!!")



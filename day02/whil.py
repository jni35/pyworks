#while ~ break 문
'''
#1부터 10까지 출력
i = 0
while True:
    i += 1
    if i>10:
        break
    print(i)
'''

# 키가 'y'이면 계속, 'n'이면 중단, 그 외의 키는 '정상 답변이 아닙니다.'
while True:
    key = input("반복을 계속 할까요?(y/n)")
    if key == "y" or key == "Y" :
        input("계속 반복")
    elif key == "n" or key == "N":
        input("반복  중단")
        break
    else:
        print("정상 답변이 아닙니다.")

    

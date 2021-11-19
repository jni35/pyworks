#윤년을 판단하는 프로그램
#윤년은 4년마다 오고,
#100으로 나누어 떨어지지 않으나 400년 마다 온다.
year = int(input("년도 입력 : "))

if year%4==0 and year%100 != 0 or year%4 == 0:
    print("윤년 입니다.")
else:
    print("평년입니다.")
    

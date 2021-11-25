#체질량 지수 계산하기
name = input("이름을 입력하세요:")
height = float(input("키(cm)를 입력하세요:"))
height = height/100
weight = float(input("몸무게(kg)를 입력하세요:"))

bmi = weight/(height*height)

print("{}님의 bmi는 {:.1f}입니다.".format(name, bmi))
#{:.1f}=소숫점 첫째 자리 까지 나온다.
#{:.2f}=소숫점 둘때 자리 까지 나온다.
print("%s님의 bmi는 %.2f입니다." % (name, bmi))
#%d=정수, %f=실수, %s=문자열
# 변수가 여러개일 때는 "(변수,변수,변수)" 꼭! 표기해 주기

if bmi < 20:
    print("저체중 입니다.")
elif bmi < 25:
    print("정상 입니다.")
elif bmi < 30:
    print("과제중 입니다.")
else:
    print("비만 입니다.")

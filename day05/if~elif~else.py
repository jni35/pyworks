#체질량 지수 계산하기
name = input("이름을 입력하세요:")
height = float(input("키(cm)를 입력하세요:"))
height = height/100
weight = float(input("몸무게(kg)를 입력하세요:"))
bmi = weight//(height*height)

print(name + "님의 bmi는" + str(bmi) + "입니다.")

if bmi < 20:
    print("저체중 입니다.")
elif 20 <= bmi < 25:
    print("정상 입니다.")
elif 25 <= bmi < 30:
    print("과제중 입니다.")
else:
    print("비만 입니다.")

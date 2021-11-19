# if ~ elif ~ else
#놀이공원 입장료 계산 프로그램

age = 15
charge = 0
if age < 8:
    print("미취학 아동입니다.")
    charge = 1000
elif age >= 8 and age<14:
    print("초등학생 입니다.")
    charge = 2000
elif age<20:
    print("중.고등학생 입니다.")
    charge = 2500
else:
    print("일반인 입니다.")
    charge = 3000

print("입장료는 " + str(charge)+"원 입니다.")

     

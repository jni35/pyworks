#도형의 면적 계산하기
#실수(소수점이 있는 수)로 입력

#사각형의 면적 계산
width = float(input("가로 길이(cm) 입력 : "))
height = float(input("세로 길이(cm) 입력 : "))

area = width*height
# print("사각형의 면적 :" + str(area) + "cm")
print("사각형의 면적 : {}cm".format(area))



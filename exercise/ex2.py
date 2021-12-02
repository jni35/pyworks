#112
#1
A = [80, 75, 55]
sum = 0
for score in A:
    sum += score
avg = sum/len(A)
print("평균 :", avg)

#2
if(13/2==0):
    print("짝수")
else:
    print("짝수 x")

#3
pin = "881120-1068234"
yymmdd = pin[:6]
num = pin[8:]
print(yymmdd)
print(num)

#4
pin = "881120-1068234"
print(pin[7])

#5
#변수명.replace("바꿀 부분","바꿀 내용")
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)


# 명령행에서 합계 계산하기
import sys

number = sys.argv[1:]

sum_v = 0
for i in number:
    sum_v += int(i)

print("합계 : " + str(sum_v))


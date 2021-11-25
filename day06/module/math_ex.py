import math
import random

# 반올림
print(round(2.54))          #내장 함수

# 올림
print(math.ceil(2.11))      #3

# 버림
print(math.floor(5.12))     #5

# 제곱근
print(math.sqrt(25))        #5.0

# 난수
print(random.random())

# 주사위
print(math.floor(random.random()*6+1))

# 원주율
print(math.pi)
# 원의 넓이
r = 4
area = math.pi*r*r
print("원의 넓이 : %.2f"%area)

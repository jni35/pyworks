# 주요 내장 함수
# all - 반복자료안에 0이 있으면 true, 아니면 false
import math

print(all([1, 2, 3]))   #true
print(all([1, 0, 3]))   #false

# any - 반복자료안에 모두 0일때만 false, 나머지는 true
print(any([1, 0, 3]))   #true

# eval - 문자열 표현 -> 숫자로 변환
print(eval("1+2"))  #3

# list() - 자료를 리스트로 반환
print(list('python'))

# 절대값
print(abs(-10))     #10

# 반올림
print(round(4.7))   #5
print(round(4.51))  #5
print(round(4.32))  #4

# 합계
print(sum([1, 2, 3, 4]))    #10

# 최소값
print(sum([1, 2, 3, 4]))    #1

# 거듭제곱
print(pow(2, 4))    #16


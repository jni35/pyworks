#tuple(튜플) 자료구조
#요소를 추가, 삭제, 변경할 수 없다.
#요소 추가시에는
#리스트와 인텍싱이나 슬라이싱 방식이 같음
#소괄호()를 사용

#튜플의 생성 및 초기화
t1 = () #빈 튜플 생성
print(t1)
print(type(t1))     #자료형은 tuple


t1 = (1, )  #1개 추가시 콤마를 붙임, 숫자와 구분
print(t1)
print(type(t1)) #자료형은 tuple
'''
t1 = (1)
print(t1)
print(type(t1)) #자료형은 int
'''

t2 = (2, 3, 4)
t1 = t1+t2
print(t1)

#인덱싱과 슬라이싱
print(t1[0])
print(t1[-1])
print(t1[2:])   #3,4

#수정, 삭제 불가
# t1[1] = 5
# del t1[1]

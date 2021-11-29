# Student 클래스를 외부에서 사용하기 - 모듈로 사용하기
# 객체 리스트 사용하기
from classlib.student import Student

'''
s = Student("김하나, 3")
print(s)
'''

s = [
    Student("김하나",3),
    Student("이두울",2),
    Student("김세엣",1),
    ]

# print(s[1])
# print(s[2])


print("********** 학생 명단 **********")
for i in s:
    print(i)
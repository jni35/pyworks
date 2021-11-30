# Employee 클래스 정의
from day09.class_live.person import person

class Employee(person):     #person 클래스를 상속 받음
    # pass
    def __init__(self,name, age, employeeID):
        super().__init__(name, age)        #부모 멤버 super()함수로 명시
        self.employeeID = employeeID       #자기 맴버 초기화

    def __str__(self):      #부모__str__()함수상속 - 재정의(오버라이드)
        return super().__str__() + "사번 : " + str(self.employeeID)

e = Employee("이강", 25, 101)
print(e)
# print("이름 : ", e.name)
# print("나이 : ", str(e.age))
# print("사번 : ", str(e.employeeID))

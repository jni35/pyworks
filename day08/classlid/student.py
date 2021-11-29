# 생성자(constructor) - 매개변수가 있는 생성자
class Student:
    def __init__(self, name, grade):        # 생성자로 매개 변수를 전달
       self.name = name
       self.grade = grade

    def __str__(self):      # 객체의 맴버정보를 출력하는 함수
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)

if __name__ == "__main__":       # name변수의 이름이 main이라면
    s1 = Student("콩쥐", 1)       # s1 객체 생성
    print(s1)

    s2 = Student("팥쥐", 2)       # s2 객체 생성
    print(s2)
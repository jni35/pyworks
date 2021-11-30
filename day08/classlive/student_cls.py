# Student 클래스 만들기
# class 는 self 키워드를 사용한다.
#def init() - 생성자(Constructor) 함수 사용
class Student:
    def __init__(self):     # initiol(생성자)
        self.name = "콩쥐"    # 맴버 변수
        self.grade = 1
        print("생성자 함수 입니다.")    # 가장 먼저 출력

    def learn(self):
        return "수업을 듣습니다."

s = Student()       # Student 클래스의 객체(인스턴트) s 생성
print("이름 : "+s.name)
print("학년 : "+str(s.grade))
print(s.learn())



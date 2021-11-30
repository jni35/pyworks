# 클래스 변수 - 인스턴트 변수와 대응하는 개념

class Counter:
    x = 0       # 클래스 변수(self를 사용하지 않음)

    def __init__(self):
        Counter.x += 1      # 클래스 변수 이름은 클래스 이름으로 직겁 접근

    def getcount(self):
        return self.x

c1 = Counter()
print(c1.getcount())    #1

c2 = Counter()
print(c2.getcount())    #2

c3 = Counter()
print(c3.getcount())    #3
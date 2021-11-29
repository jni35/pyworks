# counter 클래스 만들기

class Counter:
    def __init__(self):
        self.x = 0      # 시작 0으로 초기화(인스턴스 변수)
        self.x += 1     # 1증가

    def getcount(self):
        return self.x

    c1 = Counter()          #c1은 인스턴트 객체
    print(c1.getcount())    #1

    c2 = Counter()
    print(c2.getcount())


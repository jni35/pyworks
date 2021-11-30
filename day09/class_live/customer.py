# customer 클래스
class Customer:
    def __init__(self, cid, name):
        self.cid = cid          # 고객 아이디
        self.name = name        # 고객 이름
        self.cgrade = "SILVER"  # 고객 등급
        self.bouns_point = 0
        self.bouns_ratio = 0.01

    def getname(self):
        return self.name

    def calc_price(self, price):
        self.bouns_point += int(price * self.bouns_ratio)   # 포인트는 정수로 변경 - 가격*보너스적립룰
        return price

    def __str__(self):
        return "{}님의 등급은 {}이고, 보너스 포인트는 {}점입니다."\
            .format(self.name, self.cgrade, self.bouns_point)


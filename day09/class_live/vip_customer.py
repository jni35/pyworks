# vip customer 클래스 정의
from day09.class_live.customer import Customer

class VipCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)     # 부모 멤버 상속
        self.agent = agent              # 전문 상담원 배치
        self.cgrade = "VIP"             # VIP 등급
        self.sale_ratio = 0.1           # 구매 할인율 10%
        self.bouns_ratio = 0.05         # 보너스 적립율 5%

        def calc_price(self, price):    # 부모 매서드 재정의
            price -= int(price * self.sale_ratio)
            self.bouns_point += int(price * self.bouns_ratio)  # 포인트는 정수로 변경 - 가격*보너스적립룰
            return price

        def __str__(self):              # 부모 정보 상속
            return "{}님의 등급은 {}이고, 보너스 포인트는 {}점입니다." \
                .format(self.name, self.cgrade, self.bouns_point)
# vip customer 클래스 정의
from day09.class_lib.customer import Customer

class VIPCustomer(Customer):
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)     # 부모 멤버 상속
        self.agent = agent              # 전문 상담원 배치
        self.cgrade = "VIP"             # VIP 등급
        self.sale_ratio = 0.1           # 구매 할인율 10%
        self.bouns_ratio = 0.05         # 보너스 적립율 5%

        def calc_price(self, price):  # 부모 매서드 재정의
            price -= int(price * self.sale_ratio) \
                # 할인된 가격 = 가격 - ( 가격 * 구매 할인율)
            self.bouns_point += int(price * self.bouns_ratio)  # 포인트는 정수로 변경 - 가격*보너스적립룰
            return price
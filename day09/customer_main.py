from day09.class_live.customer import Customer
from day09.class_live.gold_customer import GoldCustomer
from day09.class_live.vip_customer import VipCustomer

c = Customer(101, "놀부")               # Customer 객체 생성
g = GoldCustomer(201, "흥부")           # GoldCustomer 객체 생성
v = VipCustomer(301, "심청", 1004)      # VipCustomer 객체 생성

#제품 구매
cost_c = c.calc_price(10000)
cost_g = g.calc_price(10000)
cost_v = v.calc_price(10000)

#제품 지불 비용 출력
print(c.getname() + "님의 지불비용은" + str(cost_c) + "원 입니다.")
print(g.getname() + "님의 지불비용은" + str(cost_g) + "원 입니다.")
print(v.getname() + "님의 지불비용은" + str(cost_v) + "원 입니다.")

#객체 정보
print(c)
print(g)
print(v)



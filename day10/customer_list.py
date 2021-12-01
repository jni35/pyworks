# 리스트로 고객 관리하기
from day09.class_lib.customer import Customer
from day09.class_lib.gold_customer import GoldCustomer
from day09.class_lib.vip_customer import VIPCustomer

customer = [
    Customer(101, "놀부"),            # Customer 객체 생성
    Customer(102, "팥쥐"),
    GoldCustomer(201, "흥부"),        # GoldCustomer 객체 생성
    GoldCustomer(202, "콩쥐"),
    VIPCustomer(301, "심청", 1234)    # VIPCustomer 객체 생성
    ]

print("*****구매 가격과 보너스 포인트 계산*****")
for c in customer:
    cost = c.calc_price(10000)
    print(c.getname() + "님의 지불금액은" + str(cost) + "원 입니다.")

print("***** 고객 정보 출력 *****")
for i in customer:
    print(i)
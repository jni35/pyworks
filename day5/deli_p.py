# 배송비 계산하기
# 상품 가격이 20000원 미만이면 배송비(2500원) 포함하고
# 아니면 배송비 미포함
def get_price(unit_price, quantity): #단위당 가격, 수량
    delivery_fee = 2500
    price = unit_price*quantity #(주문 상품가격 = 해당 제품 * 수량)
    #배송비 포함 작성
    if price < 20000:
        price += delivery_fee
        return price
    else:
        return price

price1 = get_price(15000, 2)
price2 = get_price(5000, 3)

print("상품1 가격은"+str(price1)+"원 입니다.")
print("상품2 가격은"+format(price2, ",d")+"원 입니다.")
# 천 단위 구분기호 : format(price2, ",d")

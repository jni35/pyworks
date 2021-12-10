import re

# compile -> byte 코드로 바꿈, 함수의 매게변수로 정규식 사용
p = re.compile("[a-z]+")
# [a-z]+ 범위안 반복 소문자 일치
m = p.match("afternoon")
# match() 첫 문자가 일치 하면 결과로 반환(true)
# 일치하지 않으면 none을 반환
print(m)

m2=p.match("2021,python")
print(m2)

s=p.search("2021 python")   # 전체를 검색해서 일치하면 결과를 반환함
print(s)
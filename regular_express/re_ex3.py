import re

str = "Two is too"
m1 = re.findall('T[ow]o', str)
print(m1)

m2 = re.findall("T[ow]o", str, re.IGNORECASE)   # 대소문자 구분 안함
print(m2)

m3 = re.findall("T[ow]o", str)
print(m3)

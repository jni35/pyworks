import re

str = "123?45yy7890 hi"
# pat = re.compile('[0-9]{1,3}')
# m = re.findall(pat, str)    #리스트로 반환
m = re.findall('[0-9]{1,3}', str)    #리스트로 반환 findall(정규식, 문자열)
print(m)

m2 = re.findall('[A-z]+', str)
print(m2)
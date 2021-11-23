# 문자열 슬라이싱
s = "20211123cold"
year = s[:4]    #마지막 위치 -1
day = s[4:-4]
weather = s[8:]

print(year)
print(day)
print(weather)

# 주민번호
id_card = "881120-1068234"
yymmdd = id_card[:6]    #주민번호 앞부분
num = id_card[7:]       #주민번호 뒷부분
num_hidden = '*' * len(num)
print(yymmdd)
print(num)
print(yymmdd + "-" + num_hidden)
#find() 함수 - 문자의 위치(인덱스 번호)를 찾는 함수
s = "Hello, welcome to my website!"
print(s.find("H"))      #0번 위치
print(s.find("ll"))     #첫번째 문자 위치
print(s.find("k"))      #찾는 문자가 없으면 -1

s = s.find("welcome")   #단어로 검색: 첫 문자 위치
print(s)

#strip()함수 - 공백 제거
str1 = " hi,  soo!"
print(str1.strip())
print(str1.lstrip())    #Left strip()

txt = "   banana    "
x = txt.strip()
print("Of all fruits", x, "is my favorite")


#isnumeric()  숫자인지 검사하는 함수
text1 = "123".isnumeric()
print(text1) #True

text2 = "123abc".isnumeric()
print(text2)









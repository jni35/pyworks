#변수 사용하기
#한줄 주석은 #을 사용하고
#여러줄 주석은 ''' 또는 """로 감싼다.

print("***회원가입***")
userid = "hangul"
userpw = "han1234"
name = "한글"
phone = "010-1234-5678"
age = 35

'''
print("아이디 :", userid)
print("비밀번호 :", userpw)
print("이름 :", name)
print("전화번호 : ", phone)
print("나이 :", age)
'''

print("="*30)
print("아이디 : "+ userid)
print("비밀번호 : "+ userpw)
print("이름 : "+ name)
print("전화번호 : "+ phone)
print("나이 : "+ str(age))
#숫자는 문자 자료형으로 형변환 시켜 주어야 한다. -str() 사용
print("="*30)




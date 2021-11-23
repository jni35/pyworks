# 딕셔너리(dictionary)
# 키(key)와 값(value)의 쌍
person = {}     #빈 딕셔너리
person["name"] = '한국인'
person["age"] = '27'
person["phone"] = '010-1234-5678'
print(person)

#수정
person["age"] = 30
print(person)
print(type(person))

#삭제
del person["phone"]
print(person)

#전체 출력
for key in person:
    print(key)          #key 출력
    print(person[key])  #volue 출력
    print(key, person[key])




# person  클래스 만들기
# 접근 제한 방법 - 변수이름 앞에 (언더스코어)를 1개, 2래 붙임
# 접근 방법 - get + 변수이름(), set + 변수이름()으로 만들어 속성을
# public 으로 바꿈

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {}, 나이 : {}".format(self.name, self.age)

if __name__ =="__main__":
    p = person("김하늘", 21)
    print(p)
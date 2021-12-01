# 예외 처리 미루기
# 사용하는 곳에서 예외를 처리함
class Animal:
    def cry(self):
        # print("소리를 낸다.")
        raise NotImplementedError   # 구현하지 않으면 예러 발생

class Dog(Animal): #Animal 상속
    # pass
    def cry(self):
        print("월~ 월~")


class Cat(Animal):
    def cry(self):
        print("냐~옹 냐~옹")

dog = Dog()
dog.cry()

cat = Cat()
cat.cry()



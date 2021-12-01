# Dog 클래스 만들기
class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
        self.tricks = []    #인스턴트 멤버 리스트

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog("Elsa")
dog1.add_trick("play deed")
print(dog1.tricks)

dog2 = Dog("buddy")
dog2.add_trick("roll over")
print(dog2.tricks)
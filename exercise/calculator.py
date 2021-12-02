#1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

if __name__ == "__main__":
    cal = Calculator()
    print(cal.add(50))
    print(cal.add(60))


